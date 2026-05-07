---
title: Ruflo CLI
tags: [cli, ruflo, ai-orchestration]
---

# Ruflo CLI

> Multi-agent AI orchestration for Claude Code. Installed in plugin-lite mode — slash commands for swarm coordination, goal planning, and intelligent pattern learning.

## Status
🟡 Installed (v3.7.0-alpha.7) — 4 `/plugin install` commands still pending from Trevor

## Version
```bash
npx ruflo --version
# ruflo v3.7.0-alpha.7
```

## Plugin Install Commands (Run These)

```
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
/plugin install ruflo-goals@ruflo
/plugin install ruflo-intelligence@ruflo
```

> [!warning] These are Claude Code slash commands — paste them one at a time in the Claude Code prompt, not in the terminal.

## Installed Plugins & Slash Commands

| Plugin | Command | Use |
|---|---|---|
| ruflo-core | — | Foundation, required by others |
| ruflo-swarm | `/swarm` | Parallel research across 3+ platforms simultaneously |
| ruflo-goals | `/goals` | Break campaigns and sprints into executable step plans |
| ruflo-intelligence | `/intelligence` | Learn from successful patterns, get smarter over time |

## Use Cases for This Engagement

### Phase 1
- `/goals` → Generate an executable plan for the brand identity sprint
- `/swarm` → Audit Weedmaps + Leafly + Google + Yelp at the same time

### Phase 2
- `/swarm` → Multi-platform content research in parallel
- `/intelligence` → Track which copy and creative approaches perform best

### Phase 3
- `/swarm` → Simultaneous influencer research across Instagram, TikTok, local blogs
- `/goals` → Campaign milestone planning for events and pop-ups

## Full Upgrade Path
Lite mode chosen to protect vault config. Full install when ready:
See `[[Notes/Ruflo Full Install — When the Time Comes]]`

---
*[[CLAUDE]] — master document*
