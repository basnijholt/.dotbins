# dotbins Tool Collection

This directory contains CLI tools managed by [dotbins](https://github.com/basnijholt/dotbins) v0.8.1.post3+ga3dc00a.

## 🛠️ Installed Tools

| Tool                                                           | Repository                    | Version | Updated                    | Platform             | Architecture            |
| -------------------------------------------------------------- | ----------------------------- | ------- | -------------------------- | -------------------- | ----------------------- |
| [atuin](https://github.com/atuinsh/atuin)                      | atuinsh/atuin                 | 18.4.0  | 2025-03-17T10:31:50.145654 | linux (amd64, arm64) | macos (arm64 (current)) |
| [bat](https://github.com/sharkdp/bat)                          | sharkdp/bat                   | 0.25.0  | 2025-03-17T10:31:50.290697 | linux (amd64, arm64) | macos (arm64 (current)) |
| [delta](https://github.com/dandavison/delta)                   | dandavison/delta              | 0.18.2  | 2025-03-17T10:31:49.459999 | linux (amd64, arm64) | macos (arm64 (current)) |
| [direnv](https://github.com/direnv/direnv)                     | direnv/direnv                 | 2.35.0  | 2025-03-17T20:31:44.792607 | linux (amd64, arm64) | macos (arm64 (current)) |
| [eget](https://github.com/zyedidia/eget)                       | zyedidia/eget                 | 1.3.4   | 2025-03-17T10:31:50.368733 | linux (amd64, arm64) | macos (arm64 (current)) |
| [eza](https://github.com/eza-community/eza)                    | eza-community/eza             | 0.20.24 | 2025-03-17T10:31:49.690870 | linux (amd64, arm64) |
| [fzf](https://github.com/junegunn/fzf)                         | junegunn/fzf                  | 0.60.3  | 2025-03-17T10:31:50.185663 | linux (amd64, arm64) | macos (arm64 (current)) |
| [git-lfs](https://github.com/git-lfs/git-lfs)                  | git-lfs/git-lfs               | 3.6.1   | 2025-03-17T10:31:50.039547 | linux (amd64, arm64) | macos (arm64 (current)) |
| [lazygit](https://github.com/jesseduffield/lazygit)            | jesseduffield/lazygit         | 0.48.0  | 2025-03-17T20:31:44.626871 | linux (amd64, arm64) | macos (arm64 (current)) |
| [micromamba](https://github.com/mamba-org/micromamba-releases) | mamba-org/micromamba-releases | 2.0.7-0 | 2025-03-17T10:31:50.263784 | linux (amd64, arm64) | macos (arm64 (current)) |
| [ripgrep](https://github.com/BurntSushi/ripgrep)               | BurntSushi/ripgrep            | 14.1.1  | 2025-03-17T10:31:49.221497 | linux (amd64, arm64) | macos (arm64 (current)) |
| [uv](https://github.com/astral-sh/uv)                          | astral-sh/uv                  | 0.6.7   | 2025-03-17T20:31:44.570002 | linux (amd64, arm64) | macos (arm64 (current)) |
| [zoxide](https://github.com/ajeetdsouza/zoxide)                | ajeetdsouza/zoxide            | 0.9.7   | 2025-03-17T10:31:49.177880 | linux (amd64, arm64) | macos (arm64 (current)) |

## 💻 Shell Integration

Add one of the following snippets to your shell configuration file to use the platform-specific binaries:

### Bash/Zsh

```bash
# dotbins - Add platform-specific binaries to PATH
_os=$(uname -s | tr '[:upper:]' '[:lower:]')
[[ "$_os" == "darwin" ]] && _os="macos"

_arch=$(uname -m)
[[ "$_arch" == "x86_64" ]] && _arch="amd64"
[[ "$_arch" == "aarch64" || "$_arch" == "arm64" ]] && _arch="arm64"

export PATH="$HOME/.mydotbins/tools/$_os/$_arch/bin:$PATH"
```

### Fish

```fish
# dotbins - Add platform-specific binaries to PATH
set -l _os (uname -s | tr '[:upper:]' '[:lower:]')
test "$_os" = "darwin"; and set _os "macos"

set -l _arch (uname -m)
test "$_arch" = "x86_64"; and set _arch "amd64"
test "$_arch" = "aarch64" -o "$_arch" = "arm64"; and set _arch "arm64"

fish_add_path $HOME/.mydotbins/tools/$_os/$_arch/bin
```

### Nushell

```nu
# dotbins - Add platform-specific binaries to PATH
let _os = (sys).host.name | str downcase
let _os = if $_os == "darwin" { "macos" } else { $_os }

let _arch = (sys).host.arch
let _arch = if $_arch == "x86_64" { "amd64" } else if $_arch in ["aarch64", "arm64"] { "arm64" } else { $_arch }

$env.PATH = [$"$HOME/.mydotbins/tools/$_os/$_arch/bin", ...$env.PATH]
```

## 🔄 Updating Tools

To update all tools, run:

```bash
dotbins update
```

To update specific tools only:

```bash
dotbins update tool1 tool2
```

To update tools for your current platform/architecture only:

```bash
dotbins update --current
```

## ℹ️ Additional Information

This README was automatically generated on 2025-03-17
For more information on dotbins, visit https://github.com/basnijholt/dotbins
