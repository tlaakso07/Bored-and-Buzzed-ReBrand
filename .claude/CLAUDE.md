# Skills — Buzzed Rebrand Vault

Skills installed in `.claude/skills/`. These activate automatically based on context. All work in this vault should use these skills to their full advantage.

---

## obsidian-markdown
- **Skill:** `.claude/skills/obsidian-markdown/SKILL.md`
- **Trigger:** Any time a `.md` file is created or edited in this vault
- **Use for:** Wikilinks (`[[Note]]`), callouts (`> [!type]`), embeds (`![[file]]`), frontmatter properties, tags, block IDs
- **Do NOT use:** Standard Markdown links for internal notes — always use wikilinks so Obsidian tracks renames
- **References:** `references/CALLOUTS.md`, `references/EMBEDS.md`, `references/PROPERTIES.md`

## obsidian-bases
- **Skill:** `.claude/skills/obsidian-bases/SKILL.md`
- **Trigger:** When creating `.base` files, database views, table/card views, filtered note collections, or computed properties
- **Use for:** Building Bases that aggregate notes by tag, folder, or property — e.g. a task tracker Base, a content calendar Base, a vendor directory Base

## json-canvas
- **Skill:** `.claude/skills/json-canvas/SKILL.md`
- **Trigger:** When creating or editing `.canvas` files, visual maps, flowcharts, or node/edge diagrams
- **Use for:** Visual project maps, campaign flow diagrams, brand identity canvases — any spatial layout of connected ideas

## obsidian-cli
- **Skill:** `.claude/skills/obsidian-cli/SKILL.md`
- **Status:** 🟢 Operational — binary at `/opt/homebrew/bin/obsidian`, CLI enabled in Obsidian settings
- **Trigger:** When interacting with a live Obsidian instance — reading active note, creating notes via CLI, searching vault, managing tasks or properties programmatically
- **Always use:** `vault="Buzzed Rebrand"` as first parameter to target this vault
- **Requires:** Obsidian app open
- **Reference:** `[[CLI/Obsidian CLI]]`

## defuddle
- **Skill:** `.claude/skills/defuddle/SKILL.md`
- **Trigger:** Any time the user provides a URL to read, research, or save into the vault — competitor pages, WSLCB rules, Weedmaps/Leafly listings, press coverage, influencer profiles
- **Use instead of:** WebFetch for standard web pages — defuddle removes clutter and saves tokens
- **Do NOT use for:** URLs ending in `.md` — those are already markdown, use WebFetch directly
- **Output:** Always use `--md` flag. Save research into the vault under `Reports/` or the relevant section folder.

## karpathy-guidelines
- **Skill:** `.claude/skills/karpathy-guidelines/SKILL.md`
- **Trigger:** All sessions — always active
- **Principles:**
  1. **Think Before Coding** — state assumptions, surface tradeoffs, ask before guessing
  2. **Simplicity First** — minimum work that solves the problem, no speculative features
  3. **Surgical Changes** — touch only what the task requires, clean up only your own mess
  4. **Goal-Driven Execution** — define success criteria, loop until verified

---

## Ruflo Plugins (Lite Mode)

Installed via `/plugin` — slash commands only. No MCP server. No files in vault. Upgrade path: `[[Notes/Ruflo Full Install — When the Time Comes]]`.

### ruflo-swarm
- **Trigger:** Any research task spanning 3+ platforms or sources simultaneously
- **Use for:** Running platform audits in parallel (Weedmaps + Leafly + Google + Yelp at once), multi-source competitor analysis
- **Do NOT use:** For single-source reads — defuddle handles those faster

### ruflo-goals
- **Trigger:** Starting a new phase, campaign, or sprint — any task that needs to be broken into ordered steps
- **Use for:** Brand identity sprint planning, Phase 1 task sequencing, campaign milestone mapping
- **Output:** Executable step-by-step plan with success criteria per step

### ruflo-intelligence
- **Trigger:** After completing a research block or content task
- **Use for:** Logging what worked — which sources were most valuable, which copy approaches landed, which research patterns to repeat
- **Why:** Builds a learning layer specific to cannabis/Eastside market over time

### ruflo-core
- **Trigger:** Never called directly — foundation for other ruflo-* plugins
- **Note:** Must be installed for swarm/goals/intelligence to function
- **Hook status:** All hooks patched — PreToolUse, PostToolUse, and Stop hooks replaced with `exit 0` no-ops. If ruflo-core is reinstalled, re-apply the fix to `~/.claude/plugins/cache/ruflo/ruflo-core/0.2.0/hooks/hooks.json`.

---

## Design Skills

Installed in `.claude/skills/` alongside infrastructure skills. These are the creative engine — every visual, copy, and content output for the B&B engagement runs through one of these skills.

---

### taste-skill
- **Skill:** `.claude/skills/taste-skill/SKILL.md`
- **Trigger:** Any time a visual or UI asset is being created or reviewed — automatic quality gate
- **What it does:** The anti-slop enforcer. Overrides default LLM design biases with metric-based rules. Sets design variance, motion intensity, and visual density baselines. Enforces visual hierarchy, kills generic output, and forces every asset to feel intentional and premium — not AI-generated.
- **Use for:** Any design output where "good enough" isn't good enough

### brand
- **Skill:** `.claude/skills/brand/SKILL.md`
- **Trigger:** Brand voice work, visual identity, messaging frameworks, style guides, tone of voice
- **What it does:** The Phase 1 foundation skill. Defines and enforces brand voice, visual identity standards, messaging hierarchy, and asset consistency. Has built-in scripts to inject brand context into any prompt so every output stays on-brand.
- **Use for:** Brand identity sprint, tone of voice doc, style guide, any asset that needs to match brand

### brandkit
- **Skill:** `.claude/skills/brandkit/SKILL.md`
- **Trigger:** When building or outputting brand kit deliverables
- **What it does:** Outputs structured brand kit components — logo system specs, color palette with hex/usage rules, typography pairings, spacing systems, and usage guidelines. The tangible deliverable from the brand sprint.
- **Use for:** Building the B&B brand kit doc, color palette finalization, typography selection

### social-content
- **Skill:** `.claude/skills/social-content/SKILL.md`
- **Trigger:** Any Instagram, TikTok, or Facebook content creation
- **What it does:** Full social content engine — hooks, captions, carousels, Reels scripts, Stories, content calendars. Pulls brand voice and audience context before writing so output is on-brand and platform-native, not generic.
- **Use for:** Daily content creation, content calendar buildout, Reels scripting, caption writing

### copywriting
- **Skill:** `.claude/skills/copywriting/SKILL.md`
- **Trigger:** Any written content — product descriptions, signage, promo copy, in-store text, web copy
- **What it does:** Brand-voice copywriting across every format. Applies messaging hierarchy, tone, and compliance constraints. Writes copy that sounds like a premium brand, not a dispensary price sheet.
- **Use for:** Product descriptions, price cards, flyers, website copy, promo announcements, staff binder

### ad-creative
- **Skill:** `.claude/skills/ad-creative/SKILL.md`
- **Trigger:** Paid ad creative for Meta/Instagram
- **What it does:** Builds ad creative concepts and copy for paid social. Compliance-aware — understands cannabis ad restrictions and writes within them. Covers static, carousel, and video ad formats.
- **Use for:** Meta/IG ad campaigns, boosted posts, any paid creative brief

### impeccable
- **Skill:** `.claude/skills/impeccable/SKILL.md`
- **Trigger:** Any screen-based or digital asset — website, digital displays, landing pages, menus
- **What it does:** Deep UI/UX polish. Audits digital assets for visual hierarchy, cognitive load, accessibility, typography, spacing, layout, and motion. Takes designs from functional to premium. Covers website, digital display loops, online menus, and any digital touchpoint.
- **Use for:** Website redesign, digital display graphics, Weedmaps/Leafly listing visuals, any digital asset review

### design-system
- **Skill:** `.claude/skills/design-system/SKILL.md`
- **Trigger:** When building or enforcing consistency across multiple assets
- **What it does:** Establishes a single design language across all B&B touchpoints — in-store and digital. Defines reusable tokens (colors, type, spacing, components) so every asset from a price card to an Instagram post looks like it came from the same brand.
- **Use for:** Building the B&B design system, Canva template system, ensuring in-store and digital assets stay consistent

### 14-food-beverage
- **Skill:** `.claude/skills/14-food-beverage/SKILL.md`
- **Trigger:** Lifestyle, product, and experiential content — anything that should feel sensory and aspirational
- **What it does:** Food & beverage industry content framework — the closest available vertical to cannabis. Knows how to make products feel premium, experiential, and desirable through visual and copy language. Applies lifestyle positioning techniques used by top CPG brands.
- **Use for:** Product highlight content, vendor day promotions, any content where the product should feel luxurious or aspirational

### image
- **Skill:** `.claude/skills/image/SKILL.md`
- **Trigger:** When generating images for content, mockups, or creative concepts
- **What it does:** Image generation skill — creates visuals for social content, promotional graphics, in-store design concepts, and creative mockups. Use with Kie AI MCP for actual generation output.
- **Use for:** Social content visuals, in-store asset mockups, product photography concepts, creative direction references

### webgpu-threejs-tsl
- **Skill:** `.claude/skills/webgpu-threejs-tsl/SKILL.md`
- **Trigger:** "WebGPU" / "3D visual" / "particle system" / "shader" / "animated hero" / "cinematic web experience" / "GPU effect"
- **What it does:** Full knowledge base for GPU-accelerated 3D graphics in the browser — Three.js WebGPU renderer, TSL node materials, compute shaders, particle systems, post-processing (bloom, DOF, blur), WGSL integration. Written in JavaScript, no GLSL strings.
- **Use for:** Website hero experiences, in-store digital display loops, social motion FX, brand launch web experiences — the visual layer no competitor can replicate with a template
- **B&B play:** Premium dispensary positioning requires premium digital experiences. WebGPU makes the website feel like a different category entirely.

### ui-ux-pro-max
- **Skill:** `.claude/skills/ui-ux-pro-max/CLAUDE.md`
- **Trigger:** Any design decision requiring structured intelligence — style selection, typography pairings, color palettes, UX patterns, landing page structure, or generating a complete design system from a brief
- **What it does:** Searchable design intelligence database — 67 UI styles (glassmorphism, brutalism, editorial, etc.), 161 UX reasoning rules, typography pairings, color systems by product type, landing page structures, and a Design System Generator. Uses BM25 + regex hybrid search. CLI: `python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain <style|typography|color|landing|ux|product>`
- **Use for:** Starting any digital design task — query before designing so every output is grounded in proven patterns, not guessed defaults. Run Design System Generator at the start of website redesign or brand sprint.
- **B&B play:** Query "premium cannabis dispensary" to get style recommendations with CSS keywords and AI prompt language ready for the website and in-store displays.

---

## Session Start Protocol

At the start of every new session:
1. Read `Handoff/Handoff.md` to find the most recent session
2. Read that session's handoff note in full
3. Read `Memory/MEMORY.md` index and any relevant memory files
4. Check `CLAUDE.md` for any updates since last session
5. Ask the user what they want to work on — do not assume

At the end of every session:
1. Write a new handoff note: `Handoff/Session-XX-YYYY-MM-DD.md`
2. Add it to the top of the `Handoff/Handoff.md` index
3. Update any memory files that changed
4. Keep the handoff tight — what was done, decisions made, what's pending, first thing next session

---

## Vault Defaults

When creating any note in this vault:
- Use frontmatter with at least `title` and `tags`
- Use `[[wikilinks]]` for all internal references, never `[text](path.md)`
- Use callouts for important information (`> [!note]`, `> [!warning]`, `> [!tip]`)
- Save scraped web content with defuddle, not raw HTML or WebFetch output
- All notes connect back to `[[CLAUDE]]` as the master document

## Reference Brand Library

70 world-class brand DESIGN.md files in `Brand Identity/Reference Brands/`. Each contains the complete visual language of that brand — exact colors, typography, spacing, surface logic, component patterns, atmosphere description.

**How to use:** Reference a brand by name in any design request. Claude reads its `DESIGN.md` and applies that visual DNA to the B&B brief.

**Top picks for B&B work:**
- `starbucks` — warm premium retail baseline, loyalty/community, the closest parallel
- `nike` — typographic authority, photography-first, kinetic brand voice
- `apple` — restraint as luxury, product elevation, minimal chrome
- `spotify` — dark editorial premium, culture-adjacent lifestyle positioning
- `ferrari` / `bugatti` — ultra-luxury ceiling, ceremony through restraint
- `linear.app` / `raycast` — dark premium digital UI baseline
- `airbnb` — community-rooted, warm, experiential — Eastside local angle

**Blending:** "Starbucks warmth with Nike typographic authority" is a valid brief — name two references and Claude applies both.

---

## Quick Reference

| Need | Go to |
|---|---|
| CLI tool docs & commands | `[[CLI/CLI]]` |
| MCP server docs & phase maps | `[[MCP/MCP]]` |
| Full Ruflo upgrade path | `[[Notes/Ruflo Full Install — When the Time Comes]]` |
| Compliance pre-publish checklist | `[[Compliance/Compliance]]` |
| Current phase tasks | `[[CLAUDE]]` → Priority Task List |
| Session handoff | `[[Handoff/Handoff]]` |
| All design skills + usage guide | `[[Skills/Skills]]` |
| Reference brand library | `Brand Identity/Reference Brands/` |
