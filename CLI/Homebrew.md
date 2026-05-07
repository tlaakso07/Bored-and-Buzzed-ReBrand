---
title: Homebrew
tags: [cli, homebrew, package-manager]
---

# Homebrew

> macOS package manager — installs and maintains every CLI tool in this engagement.

## Status
🟢 Operational
Version: 5.1.8
Binary: `/opt/homebrew/bin/brew`

## What It Manages for This Engagement

| Package | Installed Via |
|---|---|
| `obsidian` (CLI) | `brew install --cask obsidian` |
| `gh` | `brew install gh` |
| `node` / `npx` | `brew install node` |
| `playwright-mcp` | `brew install playwright-mcp` |

## Key Commands

```bash
# Update Homebrew itself
brew update

# Upgrade all packages
brew upgrade

# Install a package
brew install <package>

# Install a macOS app (cask)
brew install --cask <app>

# Check what's installed
brew list

# Search for a package
brew search <name>

# Check for issues
brew doctor
```

## Notes
- Run `brew update && brew upgrade` periodically to keep all CLIs current
- If a CLI stops working, `brew doctor` is the first diagnostic step

---
*[[CLAUDE]] — master document*
