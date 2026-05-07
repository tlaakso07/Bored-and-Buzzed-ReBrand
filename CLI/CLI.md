---
title: CLI Tools
tags: [cli, infrastructure, tools]
---

# CLI Tools

> Command-line tools installed and available for this engagement. These run locally in the terminal — distinct from MCPs (which are servers Claude calls via protocol).

---

## Installed CLIs

| Tool | Version | Purpose | Status |
|---|---|---|---|
| [[CLI/Obsidian CLI\|Obsidian CLI]] | — | Read, create, search, manage vault notes live | 🟢 Operational |
| [[CLI/Claude CLI\|Claude CLI]] | 2.1.129 | Claude Code — the main agent interface | 🟢 Operational |
| [[CLI/Ruflo CLI\|Ruflo]] | 3.7.0-alpha.7 | Multi-agent AI orchestration, swarm, goals, intelligence | 🟢 Operational |
| NotebookLM CLI | 0.3.4 | Create notebooks, add sources, generate audio/video/quizzes via CLI | 🟢 Operational — run `notebooklm login` first |
| [[CLI/GitHub CLI\|GitHub CLI (gh)]] | 2.89.0 | Repo management, PRs, version control for vault assets | 🟢 Operational |
| [[CLI/Playwright MCP CLI\|Playwright MCP]] | — | Browser automation via command line | 🟢 Installed |
| [[CLI/Node & npx\|Node & npx]] | v25.9.0 | JavaScript runtime — powers all MCP servers and npx tools | 🟢 Operational |
| [[CLI/Homebrew\|Homebrew]] | 5.1.8 | macOS package manager — installs and updates all other CLIs | 🟢 Operational |
| [[CLI/SkillUI CLI\|SkillUI]] | 1.3.2 | Reverse-engineer any website's design system into a Claude-ready skill | 🟢 Operational |

---

## How CLIs Map to the Plan

### Phase 1 — Foundation
- **Obsidian CLI** → Read/write vault notes programmatically during brand sprint
- **Claude CLI** → Primary interface for all session work
- **Ruflo** → Break Phase 1 into a goals plan; run parallel platform research with swarm

### Phase 2 — Build
- **Playwright MCP** → Automate listing verification across Weedmaps, Leafly, Google, Yelp
- **Ruflo** → Intelligence layer learns what content and copy patterns work
- **gh** → Version control for brand assets and templates

### Phase 3 — Grow
- **Ruflo** → Swarm handles multi-source influencer and competitor research simultaneously
- **Obsidian CLI** → Programmatic updates to content calendar and task tracking
- **Node/npx** → Powers all MCP servers throughout every phase

---

## CLI vs. MCP — When to Use Which

| Situation | Use |
|---|---|
| Interacting with the vault | Obsidian CLI |
| Scraping a website | Firecrawl MCP or defuddle |
| Automating a browser | Playwright MCP (server) |
| Running parallel research tasks | Ruflo swarm |
| Managing files and git history | gh CLI |
| Installing a new tool | Homebrew |
| Extracting a competitor's design system | SkillUI |
| Pulling visual reference from a premium brand | SkillUI --mode ultra |

---
*[[CLAUDE]] — master document*
