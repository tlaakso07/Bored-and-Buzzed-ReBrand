---
title: Claude CLI
tags: [cli, claude, ai]
---

# Claude CLI (Claude Code)

> The primary interface for all AI-assisted work on this engagement. Runs as an interactive agent in the terminal with access to all tools, skills, and MCPs configured in this vault.

## Status
🟢 Operational
Version: 2.1.129
Binary: `/Users/trevorlaakso/.local/bin/claude`

## Key Commands

```bash
# Start an interactive session
claude

# Run a one-shot prompt
claude "what's the status of Phase 1?"

# Continue last session
claude --continue

# Start with a specific model
claude --model claude-opus-4-7

# List configured MCPs
claude mcp list

# Add an MCP server
claude mcp add <name> -- <command>
```

## How It's Configured for This Engagement
- **Skills:** 6 installed in `.claude/skills/` — obsidian-markdown, bases, json-canvas, obsidian-cli, defuddle, karpathy-guidelines
- **MCPs:** Firecrawl, Playwright, Kie AI, Google Maps — all registered in `~/.claude/.mcp.json`
- **Ruflo plugins:** ruflo-core, swarm, goals, intelligence
- **Session protocol:** Reads `Handoff/Handoff.md` + `Memory/MEMORY.md` at every session start
- **Master config:** `CLAUDE.md` — all work traces back here

## Notes
- The `.claude/CLAUDE.md` file in this vault contains all skill triggers and vault defaults
- Memory is symlinked: vault `Memory/` ↔ `~/.claude/projects/.../memory/`
- Related: [[MCP/MCP]], [[Skills/Skills]], [[Memory/MEMORY]]

---
*[[CLAUDE]] — master document*
