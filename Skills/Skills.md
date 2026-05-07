---
title: Skills
tags: [skills, plugins]
---

# Skills

> Agent skill plugins installed in this vault. All creative and content output for the B&B engagement runs through these skills. Configured in `.claude/CLAUDE.md` — skills activate automatically based on context.
> **Source repos:** open-design (nexu-io), claudekit, kepano, andrej-karpathy-skills, awesome-design-md (VoltAgent)

---

## Vault & Infrastructure Skills

| Skill | Trigger | Purpose |
|---|---|---|
| `obsidian-markdown` | Any `.md` file created or edited | Wikilinks, callouts, embeds, frontmatter, tags |
| `obsidian-bases` | `.base` files, database views, filtered collections | Build Bases that aggregate notes by tag, folder, or property |
| `json-canvas` | `.canvas` files, visual maps, flowcharts | Spatial layout of connected ideas |
| `obsidian-cli` | Live vault interactions | Create/read/search notes via CLI (requires Obsidian open) |
| `defuddle` | Any URL provided for research or saving | Scrape clean markdown from web pages — always preferred over WebFetch |
| `karpathy-guidelines` | Always active | Think Before Coding · Simplicity First · Surgical Changes · Goal-Driven Execution |

---

## Design Skills — Brand Foundation

### `brand`
- **Trigger:** Brand voice work, visual identity, messaging frameworks, style guides, tone of voice
- **What it does:** Defines and enforces brand voice, visual identity standards, and messaging hierarchy. Has built-in scripts to inject brand context into every prompt so output stays on-brand automatically.
- **B&B advantage:** This is the Phase 1 skill. Run it first to define B&B's voice, visual identity, and messaging pillars. Every other skill pulls from what this one establishes — nothing ships without it.

### `brandkit`
- **Trigger:** Building or outputting brand kit deliverables
- **What it does:** Outputs structured brand kit components — logo system specs, color palette with hex/usage rules, typography pairings, spacing systems, and usage guidelines.
- **B&B advantage:** The tangible deliverable from the brand sprint. Use it to produce the B&B brand kit doc — the single reference every designer, vendor, and partner uses to stay on-brand.

### `design-brief`
- **Trigger:** Before starting any new asset — say "create a design brief for [asset]"
- **What it does:** Parses a structured brief using I-Lang protocol format. Forces explicit decisions on palette, typography, layout, mood, density, and constraints before any pixel is made. Eliminates vague briefs like "make it premium."
- **B&B advantage:** Use this before every new asset type — event poster, social campaign, in-store display. It forces the right questions up front and means the first draft is rarely thrown away. The discipline that separates agencies from freelancers.

### `design-system`
- **Trigger:** Building or enforcing consistency across multiple assets
- **What it does:** Establishes a single design language — reusable tokens (colors, type, spacing, components) so every asset from a price card to an Instagram post looks like it came from the same brand.
- **B&B advantage:** Critical for multi-channel consistency. In-store signage, digital displays, website, and social must feel like one brand. This skill is what makes that happen at scale without drift.

### `taste-skill`
- **Trigger:** Every visual or content output — runs as an automatic quality gate
- **What it does:** Overrides default LLM design biases with metric-based rules. Sets design variance (8), motion intensity (6), and visual density (4) baselines. Kills generic, AI-looking output before it ships.
- **B&B advantage:** The non-negotiable quality filter. If something looks like a cannabis stock photo from 2018, this skill catches it and forces a better direction. Run it on everything before delivery.

---

## Design Skills — Content Production

### `social-carousel`
- **Trigger:** "Create a carousel post" / "Instagram carousel" / "multi-panel post"
- **What it does:** Generates 3-panel 1080×1080 cinematic carousel series with connected headlines, brand mark, numbered panels, captions, and loop affordance — built specifically for Instagram carousel format.
- **B&B advantage:** Carousels are the highest-engagement format on Instagram. Use for: new product education (strain profiles, terpene guides), event announcements, "Top 5 picks this week," vendor spotlights. Each series tells a story across 3 slides and drives saves + shares.

### `social-content`
- **Trigger:** Any Instagram, TikTok, or Facebook content creation
- **What it does:** Full social content engine — hooks, captions, carousels, Reels scripts, Stories, content calendars. Pulls brand voice and audience context before writing so output is platform-native and on-brand.
- **B&B advantage:** The daily content workhorse. Use it to build out the bi-weekly content calendar, write captions in brand voice, and script Reels. Feed it the brand context from `brand` skill and it stays consistent every time.

### `copywriting`
- **Trigger:** Any written content — product descriptions, signage, promo copy, in-store text, web copy
- **What it does:** Brand-voice copywriting across every format. Applies messaging hierarchy, tone, and compliance constraints. Writes copy that sounds like a premium brand, not a dispensary price sheet.
- **B&B advantage:** Every word in the store and online should sound the same. Use for product descriptions, price cards, flyers, website copy, promo announcements, and the staff education binder. Run through compliance check after every output.

### `image-poster`
- **Trigger:** "Create a poster" / "product key art" / "event poster" / "promotional image"
- **What it does:** Single-image poster and key art generation. Provider-agnostic — works with Kie AI MCP for actual image output. Produces print-ready PNG/JPEG files.
- **B&B advantage:** Event posters, vendor day promotions, new product drop announcements, in-store wall art. One command produces key art. Pair with `design-brief` first to lock in the brief, then fire this skill for the output.

### `magazine-poster`
- **Trigger:** "Magazine poster" / "editorial poster" / "premium print-style asset"
- **What it does:** Editorial-style poster — oversized serif headline, struck-through word, italic accent, 2-column body, 6 annotated sections. Reads like a Sunday paper full-page essay or a thoughtful launch poster.
- **B&B advantage:** The premium card to play. Use for brand launch materials, high-end event promotions, and any content where B&B needs to look like the most elevated dispensary in the room. Instantly elevates perceived brand value beyond anything competitors are doing.

### `ad-creative`
- **Trigger:** Paid ad creative for Meta/Instagram
- **What it does:** Builds ad creative concepts and copy for paid social. Cannabis ad restriction-aware — writes within WA state and Meta compliance constraints. Covers static, carousel, and video formats.
- **B&B advantage:** When organic content transitions to paid promotion. Knows the rules built-in — no compliance surprises. Use for boosted posts and any paid campaign once the brand is defined and organic is dialed in.

### `email-marketing`
- **Trigger:** "Email campaign" / "newsletter" / "product launch email" / "promo blast"
- **What it does:** Brand product-launch email — masthead with wordmark, hero image, headline lockup, body copy, primary CTA, and specs grid. Pure HTML layout with table fallback for all email clients.
- **B&B advantage:** Customer list is a long-term owned asset — more reliable than social algorithms. Use for new product drops, monthly promos, event announcements, and vendor day invites. Compliance-check before send — no health claims, 21+ language required.

---

## Design Skills — Digital & Motion

### `impeccable`
- **Trigger:** Any screen-based or digital asset — website, digital displays, landing pages, online menus
- **What it does:** Deep UI/UX polish. Audits digital assets for visual hierarchy, cognitive load, accessibility, typography, spacing, layout, and motion. Takes designs from functional to premium.
- **B&B advantage:** The website redesign skill. Also use for digital display graphics that loop in-store, Weedmaps/Leafly listing visuals, and any digital touchpoint. Closes the gap between "it works" and "it looks like the best dispensary on the Eastside."

### `web-prototype`
- **Trigger:** "Mock up the website" / "prototype the homepage" / "show me what the site could look like"
- **What it does:** Generates self-contained single-file HTML web prototypes — landing pages, marketing pages, product pages. No framework required, opens in any browser immediately.
- **B&B advantage:** Website redesign mockups you can open in a browser and show the client the same session. Use before any dev work begins to align on look/feel fast. Also useful for prototyping the digital menu layout and online ordering flow.

### `video-shortform`
- **Trigger:** "Create a Reel" / "TikTok video" / "short-form video" / "product reveal clip"
- **What it does:** 3–10 second short-form video clips — product reveals, motion teasers, ambient loops. Works with Seedance 2, Kling, or Veo 3. Outputs MP4.
- **B&B advantage:** The Reels and TikTok engine. New product drops, store ambiance loops, event hype clips, strain spotlight reveals. Short enough to produce fast and post daily. Pair with `11-social-hook` for the caption and hook.

### `motion-frames`
- **Trigger:** "Animated hero" / "motion design" / "loop" / "video poster" / "digital display animation"
- **What it does:** Single-frame motion compositions with looping CSS animations — rotating type, animated globe, parallax labels, ticking timers. Renders as a hero video poster ready for any keyframe exporter.
- **B&B advantage:** In-store digital display loops and animated social content. A premium dispensary should not have static screens — this skill produces the looping ambient visuals that make the store feel elevated. Also produces Instagram Stories animations and animated post headers.

---

## Design Skills — Lifestyle & Vertical

### `14-food-beverage`
- **Trigger:** Lifestyle, product, and experiential content — anything sensory or aspirational
- **What it does:** Food & beverage industry content framework. Applies CPG brand positioning techniques — makes products feel premium, experiential, and desirable through visual and copy language.
- **B&B advantage:** The closest available vertical to cannabis. Use when products need to feel luxurious — product photography direction, vendor day content, tasting notes, strain highlight posts. Think Whole Foods product copy, not a dispensary menu printout.

---

## Design Skills — Advanced Visual FX

### `webgpu-threejs-tsl`
- **Trigger:** "WebGPU effect" / "3D visual" / "particle system" / "animated hero" / "shader effect" / "cinematic web experience"
- **What it does:** Full knowledge base for building GPU-accelerated 3D graphics in the browser using Three.js with WebGPU renderer and TSL (Three.js Shading Language). Covers node materials, GPU compute shaders, particle systems, post-processing effects (bloom, blur, DOF), custom WGSL, and animated materials — all written in JavaScript, no GLSL strings needed.
- **B&B advantage:** The weapon no other dispensary on the Eastside has. Use for:
  - **Website hero** — Cinematic particle fields, atmospheric fog effects, animated brand mark — a landing experience that immediately signals premium and different
  - **Digital in-store displays** — GPU-powered looping ambient visuals that make the store feel like a high-end retail environment, not a dispensary
  - **Social visual FX** — Post-processed product reveals, particle burst transitions, motion graphics that look like they cost a production budget
  - **Brand launch moment** — The Phase 1 brand reveal can ship with a WebGPU-powered web experience competitors literally cannot replicate with a template

---

## Design Skills — Intelligence & Research

### `ui-ux-pro-max`
- **Trigger:** Any design decision that needs structured intelligence — style selection, typography pairings, color palettes, UX patterns, landing page structure, or generating a full design system from a brief
- **What it does:** Searchable design intelligence database — 67 UI styles (glassmorphism, brutalism, editorial, neumorphism, etc.), 161 UX reasoning rules, typography pairings, color palettes by product type, landing page structures, and a Design System Generator (v2.0 flagship). Uses BM25 + regex hybrid search. CLI-based, runs locally.
- **CLI:** `python3 .claude/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "<query>" --domain <style|typography|color|landing|ux|product>`
- **B&B advantage:** Run this before any digital design work begins. Query "premium cannabis dispensary" for style direction and get CSS keywords, AI prompt language, and implementation checklists — structured inputs for every other design skill. Use the Design System Generator to produce a complete recommended design system at the start of the website redesign.

---

## Craft Reference Docs

> Loaded from `open-design/craft/` — universal quality rules that inform all design output. Not slash commands — these are reference docs Claude pulls from automatically when doing design work.

| Doc | What it enforces |
|---|---|
| `craft/anti-ai-slop.md` | Explicit rules for avoiding generic AI-looking output — the slop blocklist |
| `craft/typography.md` | Type scale, pairing rules, hierarchy — premium typography standards |
| `craft/color.md` | Color theory, palette construction, contrast — premium color standards |
| `craft/animation-discipline.md` | Motion principles, timing, easing — no gratuitous animation |

---

## Vault Defaults (enforced by skills)
- Frontmatter with `title` + `tags` on every note
- `[[wikilinks]]` for all internal links — never `[text](path.md)`
- Callouts for highlighted information (`> [!note]`, `> [!tip]`, `> [!warning]`)
- defuddle for all web research — output saved to `Reports/` or relevant section folder
- All notes link back to [[CLAUDE]] as the master document

---

---

## Reference Brand Library — DESIGN.md Collection

> 70 pre-extracted design systems from world-class brands. Stored in `Brand Identity/Reference Brands/`. Not a slash command — used by referencing a brand's `DESIGN.md` directly as context when building any asset.

### What a DESIGN.md Contains

Every brand folder has a `DESIGN.md` that documents the complete visual language of that brand — exact color hex values with their roles, typography specs (font family, size, weight, line height, letter spacing), spacing scale, component patterns, surface logic, motion principles, and a written description of the brand's visual atmosphere. Claude reads this the same way a designer reads a style guide brief.

### How to Use It for B&B

**The workflow:**
1. Identify the visual direction you want for an asset
2. Tell Claude which reference brand(s) to pull from
3. Claude reads that brand's `DESIGN.md` and applies its design DNA to the B&B brief
4. The output matches the quality and visual language of a world-class brand — adapted to B&B's identity

**Example prompts:**
- *"Build the B&B homepage hero using the Starbucks DESIGN.md as the visual reference — warm palette, community feel, premium retail energy"*
- *"Design a product spotlight carousel in the style of Apple's DESIGN.md — minimal, product-first, white space"*
- *"Write a vendor day event poster using Ferrari's DESIGN.md as the luxury reference point — ultra-premium positioning"*
- *"Create a B&B loyalty program page inspired by Spotify's DESIGN.md — dark editorial, culture-forward"*
- *"Design in-store digital display loops referencing Linear's DESIGN.md — dark premium, cinematic"*

You can also blend references: *"Combine Starbucks' warmth with Nike's typographic authority for the B&B brand launch page"*

### Brand Directory — Full Library

**Premium Retail & Lifestyle (direct B&B parallels)**

| Brand | Visual DNA | B&B Use Case |
|---|---|---|
| `starbucks` | Warm cream canvas, 4-tier green system, full-pill buttons, community-first retail | Closest parallel — loyalty program, in-store experience, warm brand system |
| `nike` | Photography-first, extreme typographic contrast, pure black/white, kinetic brand voice | Brand launch posters, product drops, campaign imagery direction |
| `apple` | Restraint as luxury, white space, product elevation, near-zero chrome | Website hero, product photography art direction, premium minimalism |
| `spotify` | Dark editorial premium, culture-adjacent, lifestyle-first not product-first | Social content aesthetic, dark-mode digital assets, culture/community content |
| `airbnb` | Warm, community-rooted, experiential, Rauschgold coral accent | Eastside community content, event promotions, local-first messaging |

**Ultra-Luxury Reference (aspirational ceiling)**

| Brand | Visual DNA | B&B Use Case |
|---|---|---|
| `ferrari` | Red as ceremony, carbon-black surfaces, ultra-premium restraint | High-end event materials, premium product tier positioning, luxury anchor |
| `bugatti` | Darkness as power, gold as earned signal, extreme material richness | Ultra-premium brand moments — the top of the B&B positioning range |
| `lamborghini` | Bold geometric tension, angular energy, visual aggression | High-impact campaign visuals, product reveal animations |
| `bmw` | Precision engineering aesthetic, cool premium, architectural clarity | Brand identity system structure, typography discipline |
| `bmw-m` | Performance intensity, motorsport energy, high-contrast drama | Event hype content, vendor day energy, product launch urgency |
| `tesla` | Modern premium minimalism, confident white space, tech-forward | Website redesign direction, digital-first assets |

**Digital Premium (website + UI reference)**

| Brand | Visual DNA | B&B Use Case |
|---|---|---|
| `linear.app` | Dark obsidian surfaces, razor-sharp typography, motion-first — gold standard of premium dark UI | Website dark mode, digital display loops, premium digital baseline |
| `framer` | Motion-forward, cinematic transitions, bold gradient moments | Website animation direction, interactive hero sections |
| `raycast` | Dark cinematic premium, glowing accent system, tight spatial rhythm | Digital displays, dark-themed social content, app-like web experience |
| `vercel` | Clean dark precision, engineering credibility, confident minimal | Website technical sections, digital menus, POS interface inspiration |
| `notion` | Editorial clean, generous white space, content-first hierarchy | Staff binder design, documentation, editorial content layouts |
| `stripe` | Trust-engineering through design, precise color system, financial premium | Loyalty/rewards program UI, checkout flow, membership tiers |
| `superhuman` | Extreme UI polish, every pixel intentional, speed-forward | Highest-polish digital touchpoints — sets the quality ceiling |

**Culture & Media (content aesthetic reference)**

| Brand | Visual DNA | B&B Use Case |
|---|---|---|
| `theverge` | Bold editorial energy, strong typographic hierarchy, culture-forward | Editorial social content, long-form brand stories |
| `wired` | Intellectual authority, bold typography, magazine-grade layout | Brand storytelling, thought-leadership content, premium editorial |
| `pinterest` | Visual-discovery grid, warm aspiration, collections aesthetic | Product photography grid, mood board content, inspiration carousels |
| `playstation` | Gaming premium, dark cinematic surfaces, community-first | Youth-adjacent content, gaming/culture crossover moments |

**Warm Consumer Brands (accessible premium)**

| Brand | Visual DNA | B&B Use Case |
|---|---|---|
| `shopify` | Merchant-warmth, approachable premium, earth tones | E-commerce product pages, online ordering UX |
| `uber` | Confident black, motion-forward, city-native | Delivery/convenience messaging, dark brand moments |
| `mastercard` | Overlapping circle geometry, bold simplicity, global confidence | Partnership co-branding, loyalty tier design |

**Full Library (all 70 brands)**

> airbnb · airtable · apple · binance · bmw · bmw-m · bugatti · cal · claude · clay · clickhouse · cohere · coinbase · composio · cursor · elevenlabs · expo · ferrari · figma · framer · hashicorp · ibm · intercom · kraken · lamborghini · linear.app · lovable · mastercard · meta · minimax · mintlify · miro · mistral.ai · mongodb · nike · notion · nvidia · ollama · opencode.ai · pinterest · playstation · posthog · raycast · renault · replicate · resend · revolut · runwayml · sanity · sentry · shopify · spacex · spotify · starbucks · stripe · supabase · superhuman · tesla · theverge · together.ai · uber · vercel · vodafone · voltagent · warp · webflow · wired · wise · x.ai · zapier

**Stored in:** `Brand Identity/Reference Brands/`
**Format:** Each folder contains `DESIGN.md` (full design system) + `README.md` (overview)

---

## Skill Sources

| Source | Skills |
|---|---|
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | social-carousel, image-poster, magazine-poster, email-marketing, video-shortform, motion-frames, design-brief, web-prototype + craft docs |
| [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | webgpu-threejs-tsl |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | ui-ux-pro-max |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 70 brand DESIGN.md reference files → `Brand Identity/Reference Brands/` |
| claudekit | brand, brandkit, ad-creative, copywriting, social-content, design-system, image, impeccable, taste-skill, 14-food-beverage |
| kepano | obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle |
| andrej-karpathy-skills | karpathy-guidelines |

**Skills installed to:** `.claude/skills/`
**Reference brands installed to:** `Brand Identity/Reference Brands/`
**Config:** `.claude/CLAUDE.md`
