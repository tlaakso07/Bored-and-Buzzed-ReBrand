---
title: SkillUI CLI
tags: [cli, design, tools]
---

# SkillUI CLI

> Reverse-engineer any website's design system into a Claude-ready skill. The fastest way to pull reference design DNA from any brand and use it immediately.

**Version:** 1.3.2
**Install:** `npm install -g skillui`
**Status:** 🟢 Operational
**Source:** [github.com/amaancoderx/npxskillui](https://github.com/amaancoderx/npxskillui)

---

## What It Does

Point SkillUI at any URL, directory, or repo. It crawls the site and extracts the complete design system — colors, typography, spacing, animations, components, screenshots — then packages everything into a folder with a `SKILL.md` and `CLAUDE.md` that Claude Code reads automatically.

Open the output folder in Claude Code and the design language is already loaded as context. Ask Claude to build an asset and it matches the exact visual system of the reference site.

> [!tip]
> This is the fastest way to pull visual inspiration from any premium brand and immediately apply it to B&B creative work — without guessing or describing it in words.

---

## Modes

| Mode | Command | Best For |
|---|---|---|
| **Default** | `skillui --url <url>` | Colors, type, spacing, fonts — fast, no browser needed |
| **Ultra** | `skillui --url <url> --mode ultra` | Full extraction: scroll screenshots, animations, interactions, component patterns |
| **Dir** | `skillui --dir ./path` | Scan a local codebase for design tokens |
| **Repo** | `skillui --repo <github-url>` | Clone and scan any public repo |

---

## B&B Use Cases

### Competitor Intelligence
Extract the design system of every major Eastside and Seattle dispensary. Understand exactly what they're doing visually — then do it better.

```bash
skillui --url https://[competitor-dispensary].com --mode ultra --out "./Reports/Competitor Design"
```

### Premium Reference Brands
Pull design DNA from premium CPG and lifestyle brands B&B wants to emulate — the visual standards to aim for.

```bash
skillui --url https://[premium-brand].com --mode ultra --out "./Brand Identity/Reference Brands"
```

### Weedmaps / Leafly Design Patterns
Extract platform design conventions so in-store and digital assets are built to match the platforms customers are already used to.

```bash
skillui --url https://weedmaps.com --out "./Reports/Platform Design"
```

---

## Output Structure

```
[site-name]-design/
├── SKILL.md              ← Auto-loaded by Claude Code
├── CLAUDE.md             ← Project context for the extracted design
├── DESIGN.md             ← Full design system tokens
├── references/
│   ├── ANIMATIONS.md     ← Motion specs and keyframes
│   ├── LAYOUT.md         ← Grid and layout containers
│   ├── COMPONENTS.md     ← DOM component patterns
│   ├── INTERACTIONS.md   ← Hover/focus state diffs
│   └── VISUAL_GUIDE.md   ← All screenshots in sequence
├── screens/              ← Scroll journey + section screenshots (ultra)
├── tokens/
│   ├── colors.json
│   ├── spacing.json
│   └── typography.json
└── fonts/                ← Bundled Google Fonts (woff2)
```

> [!note]
> Save output folders to `Reports/Competitor Design/` or `Brand Identity/Reference Brands/` to keep the vault organized and reference them from other notes.

---

## Key Flags

```bash
--mode ultra          Full visual extraction (requires Playwright — already installed)
--screens <n>         Pages to crawl in ultra mode (default: 5, max: 20)
--out <path>          Output directory
--name <string>       Override the project name
--format design-md    Output DESIGN.md only, skip .skill packaging
```

---

## Workflow: Reference Brand → B&B Asset

1. Run SkillUI on the reference brand in ultra mode
2. Save output to `Brand Identity/Reference Brands/[brand-name]/`
3. Open Claude Code in that folder — it loads the design system automatically
4. Describe the B&B asset you want to build
5. Claude produces output matching the reference brand's visual DNA, adapted to B&B

---

## Related
- [[CLI/CLI]] — Full CLI index
- [[Brand Identity/Brand Identity]] — Where reference brand research feeds in
- [[Reports/Reports]] — Where competitor design extractions are saved
- [[CLAUDE]] — Master project document
