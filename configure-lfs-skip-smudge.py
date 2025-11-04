#!/usr/bin/env python3
"""Configure Git LFS to keep only the current platform's binaries.

This helper does two things:

1. Enables `lfs.fetchinclude` for the detected platform/arch and sets
   `lfs.fetchexclude` for the other supported targets so future pulls stay lean.
2. Optionally performs a one-off cleanup that removes previously downloaded
   binaries for the excluded platforms and prunes the local LFS cache.

It is safe to rerun; settings are idempotent and cleanup is optional.

Usage:
    configure-lfs-skip-smudge.py          # Configure for current platform
    configure-lfs-skip-smudge.py --undo   # Undo all LFS configuration
"""

from __future__ import annotations

import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path


SUPPORTED_TARGETS = (
    "linux/amd64",
    "linux/arm64",
    "macos/arm64",
)


class CommandError(RuntimeError):
    pass


def run(
    cmd: list[str], *, env: dict[str, str] | None = None, check: bool = True
) -> subprocess.CompletedProcess:
    """Run a command, pretty printing the invocation."""

    print(f"→ {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, check=False)
    if check and result.returncode != 0:
        raise CommandError(f"command failed: {' '.join(cmd)}")
    return result


def ensure_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"{name} is required but not on PATH")


def repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit("Run this script from inside the repository")
    return Path(result.stdout.strip())


def git_config_get_all(key: str) -> list[str]:
    result = subprocess.run(
        ["git", "config", "--local", "--get-all", key],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def unset_value(key: str, value: str) -> None:
    regex = re.escape(value)
    run(["git", "config", "--local", "--unset-all", key, regex], check=False)


def detect_target() -> str:
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        system = "macos"
    elif system != "linux":
        raise SystemExit(f"Unsupported OS: {system}")

    if machine in {"x86_64", "amd64"}:
        arch = "amd64"
    elif machine in {"aarch64", "arm64"}:
        arch = "arm64"
    else:
        raise SystemExit(f"Unsupported architecture: {machine}")

    target = f"{system}/{arch}"
    if target not in SUPPORTED_TARGETS:
        raise SystemExit(f"Unsupported target: {target}")
    return target


def configure_lfs(target: str) -> tuple[str, list[str]]:
    include_pattern = f"{target}/**"
    exclude_dirs = [t for t in SUPPORTED_TARGETS if t != target]

    run(["git", "lfs", "install", "--local", "--skip-smudge"], check=True)

    run(
        [
            "git",
            "config",
            "--local",
            "--replace-all",
            "lfs.fetchinclude",
            include_pattern,
        ]
    )

    existing_excludes = git_config_get_all("lfs.fetchexclude")
    for value in existing_excludes:
        if any(value.startswith(prefix) for prefix in SUPPORTED_TARGETS):
            unset_value("lfs.fetchexclude", value)

    for directory in exclude_dirs:
        pattern = f"{directory}/**"
        run(
            ["git", "config", "--local", "--add", "lfs.fetchexclude", pattern],
            check=True,
        )

    return include_pattern, exclude_dirs


def prompt_cleanup() -> bool:
    try:
        answer = (
            input(
                "Run cleanup to drop already-downloaded binaries for other platforms? [y/N] "
            )
            .strip()
            .lower()
        )
    except EOFError:
        return False
    return answer in {"y", "yes"}


def cleanup(exclude_dirs: list[str]) -> None:
    env = os.environ.copy()
    env["GIT_LFS_SKIP_SMUDGE"] = "1"

    print("Resetting working tree with smudge disabled...")
    run(["git", "reset", "--hard", "HEAD"], env=env)

    cleaned: list[str] = []
    for directory in exclude_dirs:
        path = Path(directory)
        if path.exists():
            print(f"Removing {directory} ...")
            shutil.rmtree(path)
        cleaned.append(directory)

    if cleaned:
        print("Restoring pointer files...")
        run(["git", "checkout", "--", *cleaned], env=env)

    print("Pruning local Git LFS cache...")
    run(["git", "lfs", "prune", "--force", "--recent=0"])


def undo_lfs_configuration() -> None:
    """Undo all LFS configuration changes."""
    print("Undoing Git LFS configuration...\n")

    # Reinstall git-lfs without --skip-smudge
    print("Reinstalling git-lfs without skip-smudge...")
    run(["git", "lfs", "install", "--local", "--force"], check=True)

    # Remove fetchinclude settings
    existing_includes = git_config_get_all("lfs.fetchinclude")
    if existing_includes:
        print("Removing lfs.fetchinclude settings...")
        for value in existing_includes:
            unset_value("lfs.fetchinclude", value)

    # Remove fetchexclude settings
    existing_excludes = git_config_get_all("lfs.fetchexclude")
    if existing_excludes:
        print("Removing lfs.fetchexclude settings...")
        for value in existing_excludes:
            unset_value("lfs.fetchexclude", value)

    print("\nConfiguration reset complete!")
    print("\nTo download all LFS files, run:")
    print("  git lfs pull")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Configure Git LFS to keep only current platform's binaries"
    )
    parser.add_argument(
        "--undo",
        action="store_true",
        help="Undo all LFS configuration changes",
    )
    args = parser.parse_args()

    ensure_tool("git")
    ensure_tool("git-lfs")

    root = repo_root()
    os.chdir(root)

    if args.undo:
        undo_lfs_configuration()
        return

    target = detect_target()
    print(f"Detected platform: {target}\n")

    include_pattern, excludes = configure_lfs(target)

    print("Configuration updated")
    print(f"  lfs.fetchinclude = {include_pattern}")
    print(f"  lfs.fetchexclude = {', '.join(f'{e}/**' for e in excludes)}\n")

    if prompt_cleanup():
        cleanup(excludes)
        print(
            "Cleanup finished. This clone now only stores binaries for this platform.\n"
        )
    else:
        print("Skipped cleanup. You can run it later with:")
        print("  GIT_LFS_SKIP_SMUDGE=1 git reset --hard HEAD")
        for directory in excludes:
            print(f"  rm -rf {directory}")
        print("  git lfs prune --force --recent=0\n")

    print("Useful commands:")
    print(f'  git lfs pull --include="{include_pattern}"')
    print(f'  git lfs checkout --include="{include_pattern}"')
    print("  git lfs ls-files")
    print()
    print("To undo these settings:")
    print("  ./configure-lfs-skip-smudge.py --undo")


if __name__ == "__main__":
    try:
        main()
    except CommandError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
