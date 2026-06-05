# 🛠️ dotbins Tool Collection

[![dotbins](https://img.shields.io/badge/powered%20by-dotbins-blue.svg?style=flat-square)](https://github.com/basnijholt/dotbins) [![Version](https://img.shields.io/badge/version-2.10.1-green.svg?style=flat-square)](https://github.com/basnijholt/dotbins/releases)

This directory contains command-line tools automatically managed by [dotbins](https://github.com/basnijholt/dotbins).

## 📋 Table of Contents

- [What is dotbins?](#-what-is-dotbins)
- [Installed Tools](#-installed-tools)
- [Tool Statistics](#-tool-statistics)
- [Shell Integration](#-shell-integration)
- [Installing and Updating Tools](#-installing-and-updating-tools)
- [Quick Commands](#-quick-commands)
- [Configuration File](#-configuration-file)
- [Additional Information](#ℹ️-additional-information)

## 📦 What is dotbins?

**dotbins** is a utility for managing CLI tool binaries in your dotfiles repository. It downloads and organizes binaries for popular command-line tools across multiple platforms (macOS, Linux) and architectures (amd64, arm64).

**Key features:**

- ✅ **Cross-platform support** - Manages tools for different OSes and CPU architectures
- ✅ **No admin privileges** - Perfect for systems where you lack sudo access
- ✅ **Version tracking** - Keeps track of installed tools with update timestamps
- ✅ **GitHub integration** - Automatically downloads from GitHub releases
- ✅ **Simple configuration** - YAML-based config with auto-detection capabilities

Learn more: [github.com/basnijholt/dotbins](https://github.com/basnijholt/dotbins)

## 🔍 Installed Tools

| Tool | Repository | Version | Updated | Platforms & Architectures |
| :--- | :--------- | :------ | :------ | :------------------------ |
| [atuin](https://github.com/atuinsh/atuin) | atuinsh/atuin | 18.16.1 | Jun 05, 2026 | linux (amd64, arm64) • macos (arm64) |
| [bat](https://github.com/sharkdp/bat) | sharkdp/bat | 0.26.1 | Dec 11, 2025 | linux (amd64, arm64) • macos (arm64) |
| [bun](https://github.com/oven-sh/bun) | oven-sh/bun | bun-v1.3.14 | Jun 05, 2026 | linux (amd64, arm64) • macos (arm64) |
| [delta](https://github.com/dandavison/delta) | dandavison/delta | 0.19.2 | Apr 06, 2026 | linux (amd64, arm64) • macos (arm64) |
| [direnv](https://github.com/direnv/direnv) | direnv/direnv | 2.37.1 | Oct 08, 2025 | linux (amd64, arm64) • macos (arm64) |
| [duf](https://github.com/muesli/duf) | muesli/duf | 0.9.1 | Oct 08, 2025 | linux (amd64, arm64) • macos (arm64) |
| [dust](https://github.com/bootandy/dust) | bootandy/dust | 1.2.4 | Jan 21, 2026 | linux (amd64, arm64) • macos (arm64) |
| [eza](https://github.com/eza-community/eza) | eza-community/eza | 0.23.4 | Oct 08, 2025 | linux (amd64, arm64) |
| [fd](https://github.com/sharkdp/fd) | sharkdp/fd | 10.4.2 | Apr 06, 2026 | linux (amd64, arm64) • macos (arm64) |
| [fzf](https://github.com/junegunn/fzf) | junegunn/fzf | 0.73.1 | Jun 05, 2026 | linux (amd64, arm64) • macos (arm64) |
| [hyperfine](https://github.com/sharkdp/hyperfine) | sharkdp/hyperfine | 1.20.0 | Nov 26, 2025 | linux (amd64, arm64) • macos (arm64) |
| [keychain](https://github.com/danielrobbins/keychain) | danielrobbins/keychain | 2.9.8 | Dec 11, 2025 | linux (amd64, arm64) • macos (arm64) |
| [lazygit](https://github.com/jesseduffield/lazygit) | jesseduffield/lazygit | 0.62.2 | Jun 05, 2026 | linux (amd64, arm64) • macos (arm64) |
| [micromamba](https://github.com/mamba-org/micromamba-releases) | mamba-org/micromamba-releases | 2.8.0-0 | Jun 05, 2026 | linux (amd64, arm64) • macos (arm64) |
| [rg](https://github.com/BurntSushi/ripgrep) | BurntSushi/ripgrep | 15.1.0 | Oct 23, 2025 | linux (amd64, arm64) • macos (arm64) |
| [starship](https://github.com/starship/starship) | starship/starship | 1.25.1 | May 07, 2026 | linux (amd64, arm64) • macos (arm64) |
| [uv](https://github.com/astral-sh/uv) | astral-sh/uv | 0.11.19 | Jun 05, 2026 | linux (amd64, arm64) • macos (arm64) |
| [yazi](https://github.com/sxyazi/yazi) | sxyazi/yazi | 26.5.6 | May 07, 2026 | linux (amd64, arm64) • macos (arm64) |
| [zoxide](https://github.com/ajeetdsouza/zoxide) | ajeetdsouza/zoxide | 0.9.9 | Apr 06, 2026 | linux (amd64, arm64) • macos (arm64) |

## 📊 Tool Statistics

<div align='center'><h3>📦 56 Tools | 💾 790.35 MB Total Size</h3></div>

| Tool | Total Size | Avg Size per Architecture |
| :--- | :-------- | :------------------------ |
| bun | 236.18 MB | 78.73 MB |
| uv | 152.25 MB | 50.75 MB |
| atuin | 82.68 MB | 27.56 MB |
| yazi | 60.78 MB | 20.26 MB |
| lazygit | 52.87 MB | 17.62 MB |
| micromamba | 51.75 MB | 17.25 MB |
| starship | 29.84 MB | 9.95 MB |
| direnv | 22.62 MB | 7.54 MB |
| delta | 18.8 MB | 6.27 MB |
| bat | 17.89 MB | 5.96 MB |
| fzf | 13.47 MB | 4.49 MB |
| rg | 13.39 MB | 4.46 MB |
| fd | 10.04 MB | 3.35 MB |
| duf | 8.86 MB | 2.95 MB |
| dust | 7.97 MB | 2.66 MB |
| eza | 4.25 MB | 2.12 MB |
| hyperfine | 3.6 MB | 1.2 MB |
| zoxide | 2.97 MB | 1012.35 KB |
| keychain | 143.84 KB | 47.95 KB |

## 💻 Shell Integration

Add one of the following snippets to your shell configuration file to use the platform-specific binaries:

For **Bash**:
```bash
source $HOME/.dotbins/shell/bash.sh
```

For **Zsh**:
```bash
source $HOME/.dotbins/shell/zsh.sh
```

For **Fish**:
```fish
source $HOME/.dotbins/shell/fish.fish
```

For **Nushell**:
```nu
source $HOME/.dotbins/shell/nushell.nu
```

## 🔄 Installing and Updating Tools

### Install or update all tools
```bash
dotbins sync
```

### Install or update specific tools only
```bash
dotbins sync tool1 tool2
```

### Install or update for current platform only
```bash
dotbins sync --current
```

### Force reinstall of all tools
```bash
dotbins sync --force
```


## 🚀 Quick Commands

<details>
<summary>All available commands</summary>

```
dotbins list           # List all available tools
dotbins init           # Initialize directory structure
dotbins sync           # Install and update tools to their latest versions
dotbins readme         # Regenerate this README
dotbins status         # Show installed tool versions
dotbins get REPO       # Install tool directly to ~/.local/bin
```

For detailed usage information, run `dotbins --help` or `dotbins <command> --help`
</details>

## 📁 Configuration File

dotbins is configured using a YAML file (`dotbins.yaml`).
This configuration defines which tools to manage, their sources, and platform compatibility.

**Current Configuration:**

```yaml
tools_dir: ~/.dotbins

platforms:
  linux:
    - amd64
    - arm64
  macos:
    - arm64

tools:
  delta: dandavison/delta
  duf: muesli/duf
  dust: bootandy/dust
  fd: sharkdp/fd
  hyperfine: sharkdp/hyperfine
  rg: BurntSushi/ripgrep
  yazi: sxyazi/yazi

  bat:
    repo: sharkdp/bat
    shell_code:
      bash,zsh: |
        alias bat="bat --paging=never"
        alias cat="bat --plain --paging=never"
  bun:
    repo: oven-sh/bun
    arch_map:
      amd64: x64
      arm64: aarch64
    asset_patterns:
      linux: bun-linux-{arch}.zip
      macos: bun-darwin-{arch}.zip
    shell_code:
      bash,zsh: |
        alias bunx="bun x"
  direnv:
    repo: direnv/direnv
    shell_code:
      bash,zsh: |
        eval "$(direnv hook __DOTBINS_SHELL__)"
  eza:
    repo: eza-community/eza
    shell_code:
      bash,zsh: |
        alias l="eza --long --all --git --icons=auto"
  fzf:
    repo: junegunn/fzf
    shell_code:
      zsh: |
        source <(fzf --zsh)
      bash: |
        eval "$(fzf --bash)"
  lazygit:
    repo: jesseduffield/lazygit
    shell_code:
      bash,zsh: |
        alias lg="lazygit"
  micromamba:
    repo: mamba-org/micromamba-releases
    shell_code:
      bash,zsh: |
        alias mm="micromamba"
  starship:
    repo: starship/starship
    shell_code:
      bash,zsh: |
        eval "$(starship init __DOTBINS_SHELL__)"
  zoxide:
    repo: ajeetdsouza/zoxide
    shell_code:
      bash,zsh: |
        eval "$(zoxide init __DOTBINS_SHELL__)"
  atuin:
    repo: atuinsh/atuin
    shell_code:
      bash,zsh: |
        eval "$(atuin init __DOTBINS_SHELL__ --disable-up-arrow)"

  keychain:
    repo: danielrobbins/keychain
    asset_patterns: keychain

  uv:
    repo: astral-sh/uv
    binary_name: [uv, uvx]
    path_in_archive: [uv-*/uv, uv-*/uvx]
```

## ℹ️ Additional Information

* This README was automatically generated on Jun 05, 2026
* Current platform: **macos/arm64**
* For more information on dotbins, visit https://github.com/basnijholt/dotbins