---
title: Ruflo Full Install — When the Time Comes
tags:
  - tools
  - ruflo
  - future
  - infrastructure
aliases:
  - Ruflo Full Scale
---

# Ruflo Full Install — When the Time Comes

> [!tip] Why This Note Exists
> We installed Ruflo in plugin-lite mode (4 plugins, zero file changes) to protect our vault config. This note documents the full-scale install path for when we're ready to commit to the complete system.

---

## What We Have Now (Lite Mode)

Four plugins installed via slash commands — no files added to vault, no MCP server, no hooks:

| Plugin | Purpose |
|---|---|
| `ruflo-core` | Foundation |
| `ruflo-swarm` | Parallel research coordination |
| `ruflo-goals` | Break campaigns into executable plans |
| `ruflo-intelligence` | Learn from successful patterns |

---

## What Full Install Adds

- **98 agents** — specialized for code, testing, security, docs, architecture
- **MCP server** — unlocks `memory_store`, `swarm_init`, `agent_spawn` tools callable from Claude
- **Hooks system** — auto-routes tasks in the background without prompting
- **Vector memory (AgentDB)** — HNSW-indexed persistent memory, 150x–12,500x faster search
- **12 background workers** — auto-audit, auto-optimize, test gap detection
- **30 skills** — installed into `.claude/skills/`
- **60+ CLI commands**

---

## Pre-Flight Checklist Before Full Install

> [!warning] Do These First
> The full install modifies `.claude/` and will add a `CLAUDE.md` — back everything up before running.

- [ ] Back up `.claude/CLAUDE.md` (has skill triggers + vault session protocol)
- [ ] Back up `CLAUDE.md` (master brand document — must not be overwritten)
- [ ] Back up `Memory/MEMORY.md`
- [ ] Note current MCP config in `~/.claude/.mcp.json`
- [ ] Confirm Ruflo's install won't clobber Firecrawl or Kie AI MCP entries

---

## The Install Commands

```bash
# Option 1 — interactive wizard (recommended first time)
npx ruflo@latest init wizard

# Option 2 — non-interactive
npx ruflo@latest init

# Option 3 — global install
npm install -g ruflo@latest

# Add as MCP server in Claude Code
claude mcp add ruflo -- npx ruflo@latest mcp start
```

---

## Post-Install: Merge Strategy

After running the install, the key files to reconcile:

1. **`.claude/CLAUDE.md`** — Ruflo will add its own. Merge our skill triggers + session protocol back in.
2. **`CLAUDE.md`** — Check if Ruflo touched it. Our brand master doc must stay intact.
3. **`~/.claude/.mcp.json`** — Confirm Firecrawl and Kie AI entries survived.
4. **Hooks** — Review what Ruflo installed. Remove any hooks that conflict with our session start/end protocol.

---

## When Is the Right Time?

> [!question] Triggers for upgrading
> - We're running multi-source research across 5+ platforms simultaneously
> - We want persistent vector memory that survives session resets
> - We need autonomous background agents (e.g. auto-monitor Weedmaps/Leafly listings)
> - The swarm slash commands feel limiting and we want the full MCP tool surface

---

## References

- Ruflo repo: [github.com/ruvnet/ruflo](https://github.com/ruvnet/ruflo)
- Web UI: [flo.ruv.io](https://flo.ruv.io)
- Goal planner: [goal.ruv.io](https://goal.ruv.io)
- Related: [[MCP/MCP]], [[Skills/Skills]], [[CLAUDE]]



---
*[[CLAUDE]] — master document*