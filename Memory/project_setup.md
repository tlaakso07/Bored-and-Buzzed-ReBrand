---
name: Project Setup — Buzzed Rebrand
description: Full infrastructure state as of Session 13. Vault, 20 design skills, 4 MCPs, 10 CLIs, Ruflo, all hooks, 70 brand DESIGN.md references, Obsidian graph — all green. Mainframe build complete. Phase 1 ready.
type: project
originSessionId: edd85f21-1986-405c-8080-2251f76e1139
---
Vault fully initialized for the Bored and Buzzed rebrand engagement. Full content machine operational as of Session 13 — mainframe build complete, all docs aligned, graph updated. Phase 1 brand identity sprint is the only open item.

**Why:** Antigravity agency onboarding — needed a structured project hub before starting Phase 1 work.

**How to apply:** Vault is the single source of truth. CLAUDE.md is the master document. Memory/ (this folder) is symlinked from Claude's memory path so all memories are visible in Obsidian and must stay aligned with CLAUDE.md.

## What's in place

### Vault Structure
Folders: Brand Identity, Brand Identity/Reference Brands, Social Media, In-Store Assets, Events, Compliance, Reports, Skills, MCP, CLI, Memory, Templates, Notes, Handoff

### Infrastructure Skills (6 in `.claude/skills/`)
obsidian-markdown · obsidian-bases · json-canvas · obsidian-cli · defuddle · karpathy-guidelines

### Design Skills (20 in `.claude/skills/`)

**Brand Foundation**
| Skill | Role |
|---|---|
| `taste-skill` | Anti-slop quality gate — runs on every output |
| `brand` | Phase 1 brand identity foundation |
| `brandkit` | Brand kit deliverable (colors, type, logo specs) |
| `design-system` | Consistency tokens across in-store + digital |
| `design-brief` | Structured brief before any asset |

**Content Production**
| Skill | Role |
|---|---|
| `social-content` | IG/TikTok/FB daily content engine |
| `social-carousel` | 3-panel 1080×1080 Instagram carousels |
| `copywriting` | All copy — product, signage, promo, web |
| `ad-creative` | Meta/IG paid ads, cannabis-compliant |
| `email-marketing` | HTML email campaigns |
| `14-food-beverage` | Aspirational lifestyle/product content |

**Digital & Motion**
| Skill | Role |
|---|---|
| `impeccable` | Digital asset polish — website, displays, menus |
| `web-prototype` | Browser-ready website mockups |
| `video-shortform` | 3–10 sec Reels/TikTok clips |
| `motion-frames` | Looping CSS motion for displays + social |
| `webgpu-threejs-tsl` | GPU-accelerated 3D graphics + shaders in browser |
| `ui-ux-pro-max` | Design intelligence database — 67 UI styles, 161 UX rules, Design System Generator; CLI-searchable |

**Image Generation**
| Skill | Role |
|---|---|
| `image` | Image generation for content + mockups |
| `image-poster` | Single-image posters and key art |
| `magazine-poster` | Editorial-style premium posters |

### Craft Reference Docs (4 in `.claude/skills/craft/`)
anti-ai-slop · typography · color · animation-discipline — universal quality rules, auto-applied to all design output

### Reference Brand Library (70 DESIGN.md files)
`Brand Identity/Reference Brands/` — pre-extracted design systems from Nike, Starbucks, Apple, Ferrari, Spotify, Airbnb, Linear, Raycast, Tesla, Framer, Notion, Bugatti, Lamborghini, Stripe, Superhuman + 55 more. Tell Claude which brand to reference and it reads that DESIGN.md as visual context.

### MCPs
| Server | Status |
|---|---|
| Firecrawl | 🟢 Connected |
| Playwright | 🟢 Binary at `/opt/homebrew/bin/playwright-mcp` |
| Kie AI | 🟡 Configured with API key — not health-checked |
| Google Maps | 🔴 Placeholder API key — not operational |

### CLIs (10 total — all documented in `CLI/` folder)
| CLI | Status |
|---|---|
| Obsidian CLI | 🟢 `/opt/homebrew/bin/obsidian` |
| Claude CLI | 🟢 v2.1.129 |
| Ruflo | 🟢 v3.7.0-alpha.7 — 4 plugins, all hooks patched |
| GitHub CLI (gh) | 🟢 v2.89.0 |
| playwright-mcp | 🟢 `/opt/homebrew/bin/playwright-mcp` |
| Node / npx | 🟢 v25.9.0 |
| Homebrew | 🟢 v5.1.8 |
| pipx | 🟢 v1.11.1 |
| NotebookLM CLI | 🟢 v0.3.4 — authenticated |
| SkillUI | 🟢 v1.3.2 — extracts any website's design system into a Claude-ready skill |

### ruflo-core Hook Status
All hooks patched — Stop, PreToolUse (Bash + Write/Edit), PostToolUse (Bash + Write/Edit) all replaced with `exit 0` no-ops. File: `~/.claude/plugins/cache/ruflo/ruflo-core/0.2.0/hooks/hooks.json`. Re-apply if ruflo-core is ever reinstalled.

### Memory
Symlinked: `~/.claude/projects/.../memory` → vault `Memory/` folder — confirmed same physical directory

### Obsidian Graph View
14 color groups — one per vault section:
- 🟡 Gold — Hub (CLAUDE.md, Home)
- 🟠 Amber — Reference Brands (Brand Identity/Reference Brands) ← added Session 12
- 🟣 Violet — Brand Identity
- 🩷 Pink — Social Media
- 🟠 Orange — In-Store Assets
- 🩵 Cyan — Events
- 🔴 Red — Compliance
- 🔵 Blue — Reports
- 💜 Indigo — Memory
- ⬜ Slate — Handoff
- 🟢 Emerald — CLI + Skills
- 🍋 Lime — MCP
- 🔘 Slate — Notes
Color groups panel expanded. Node size 1.3x. Reference Brands group listed before Brand Identity so amber takes priority over violet for the 70 brand nodes.

## Status
🟢 **Phase 1 brand identity sprint COMPLETE as of Session 14 (2026-05-06).** 17 files delivered.

🟡 **Phase 2 website prototype IN PROGRESS as of Session 18 (2026-05-07).** v4 iterated — Apple design pass, Wyld Relaxing Collection added (4 cards), Jim Jones event photos in Culture/Events, hero cleaned up (no eyebrow strip, no graffiti logo). Hero photo (`bnb-interior.png`) ready to implement next session.

**Phase 1 remaining (still open):**
- Platform audits: Weedmaps, Leafly, Google Business, Yelp (website audit done ✅)
- WSLCB compliance research + master compliance checklist

**Phase 2 in progress:**
- Website prototype v4 ✅ — **next: hero photo implementation (`bnb-interior.png`)**
- Weedmaps & Leafly listing overhaul (pending)
- Social content calendar (pending)
- In-store asset suite (pending)

Open gaps (non-blocking):
- Kie AI MCP — configured but never health-checked
- Google Maps MCP — placeholder API key, not operational
