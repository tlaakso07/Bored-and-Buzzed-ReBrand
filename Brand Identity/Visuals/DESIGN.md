# Bored N Buzzed — Eastside Premium Design System

> **Phase 1 Brand Sprint · Antigravity Agency · 2026-05-06**
> Built from: Firecrawl full-site audit (34 pages) + SkillUI extraction + NotebookLM market intelligence synthesis

---

## 0. Strategic Foundation

**Core Insight (NotebookLM synthesis):**
> "The Culture's Outpost in the Suburbs."

The Eastside is affluent and polished, but often feels culturally isolated from authentic cannabis culture. Bored N Buzzed is the only destination that brings genuine street culture and high-end cannabis craft directly to the tech-wealth of Kirkland, Redmond, Woodinville, and Bothell. The new identity is the bridge between **suburban sophistication and urban authenticity** — not just "premium," but the curated, high-end access point for culture that the Eastside usually has to cross the bridge to find.

**What we are eliminating:**
- Deal-first positioning, percentage-off callouts as primary visual hierarchy
- Generic cannabis tropes (leaf imagery, stoner aesthetics, green-everything)
- The current yellow #FFD10B — retained as spirit, elevated to gold
- The current blue #0274BE — retained as spirit, elevated to deep navy
- Montserrat-as-everything
- ALL CAPS body text and navigation
- Discount culture copy ("solid weed at prices that make sense")

**What we are preserving:**
- Community warmth and approachability
- Educational mission (terpenes, Cannabis 101 — this is premium)
- Events muscle (Jim Jones, vendor days — this is differentiation)
- Eastside geographic identity and service area pride
- The loyalty to craft and curation in product selection

---

## 1. Visual Theme & Atmosphere

- **Mood:** Editorial — authoritative, aspirational, culture-forward
- **Feel:** The cover of a premium lifestyle magazine printed on warm-toned stock. Serious weight, but inviting. The kind of place you slow down and look at.
- **Atmosphere:** Warm dark. Like aged oak, candlelight, and a well-curated record collection. Premium, but not cold. Eastside, but not pretentious.
- **References:** Kinfolk Magazine × Highsnobiety × Ace Hotel lobby — editorial premium with genuine cultural credibility
- **Anti-references:** Generic dispensary green. Stoner aesthetics. Deal-of-the-day banners. "Bro" cannabis culture.

---

## 2. Color Palette & Roles

### Core Palette — Warm Dark

| Token | Hex | Role | Notes |
|---|---|---|---|
| `--color-bg` | `#0D0D0B` | Page background | Warm near-black — never pure #000000 |
| `--color-surface` | `#161612` | Card + section surfaces | Slight warmth vs. background |
| `--color-surface-raised` | `#1F1F19` | Elevated cards, hover states | Visible lift without shadow |
| `--color-border` | `#2A2A24` | Dividers, card outlines | Warm dark — use over box-shadow |
| `--color-text-primary` | `#F4EFE6` | Primary text | Warm cream — not clinical white |
| `--color-text-secondary` | `#8D867A` | Secondary text, captions, labels | Warm stone |
| `--color-text-muted` | `#5A544E` | Placeholder, disabled states | |

### Accent Palette — Elevated Gold

> Spirit of #FFD10B preserved. Energy and warmth retained. Budget signaling eliminated.

| Token | Hex | Role | Notes |
|---|---|---|---|
| `--color-accent` | `#C9A84C` | CTAs, active states, highlights | "Aged gold" not "traffic light" |
| `--color-accent-hover` | `#B8963C` | Hover state | Deeper, not lighter |
| `--color-accent-subtle` | `rgba(201,168,76,0.10)` | Tag backgrounds, light fills | |
| `--color-accent-border` | `rgba(201,168,76,0.25)` | Gold-tinted borders on tags | |

### Depth Palette — Deep Navy

> Spirit of #0274BE preserved. Corporate flatness eliminated. Used sparingly for depth.

| Token | Hex | Role | Notes |
|---|---|---|---|
| `--color-navy` | `#0F2640` | Deep anchor color | Use for section backgrounds, not primary UI |
| `--color-navy-muted` | `#1A3D5C` | Navy elevated | Secondary navy surfaces |

### CSS Variable Block

```css
:root {
  /* Core */
  --color-bg: #0D0D0B;
  --color-surface: #161612;
  --color-surface-raised: #1F1F19;
  --color-border: #2A2A24;
  --color-text-primary: #F4EFE6;
  --color-text-secondary: #8D867A;
  --color-text-muted: #5A544E;

  /* Accent — Gold */
  --color-accent: #C9A84C;
  --color-accent-hover: #B8963C;
  --color-accent-subtle: rgba(201, 168, 76, 0.10);
  --color-accent-border: rgba(201, 168, 76, 0.25);

  /* Depth — Navy */
  --color-navy: #0F2640;
  --color-navy-muted: #1A3D5C;

  /* Fonts */
  --font-display: 'Clash Display', sans-serif;
  --font-body: 'DM Sans', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Spacing */
  --spacing-section: 80px;
  --spacing-content: 40px;
  --max-width: 1280px;
}
```

---

## 3. Typography Rules

### Font Imports

```css
@import url('https://api.fontshare.com/v2/css?f[]=clash-display@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=JetBrains+Mono:wght@400&display=swap');
```

### Type Scale

| Role | Family | Weight | Size | Leading | Tracking |
|---|---|---|---|---|---|
| Display / H1 | Clash Display | 700 | `clamp(2.5rem, 6vw, 5rem)` | 1.05 | -0.02em |
| H2 | Clash Display | 700 | `clamp(1.75rem, 4vw, 3rem)` | 1.1 | -0.01em |
| H3 / Subhead | DM Sans | 600 | `clamp(1.125rem, 2.5vw, 1.5rem)` | 1.2 | 0 |
| Body | DM Sans | 400 | 1rem | 1.65 | 0 |
| Label / Caption | DM Sans | 500 | 0.8125rem | 1.4 | 0.01em |
| Tag / Eyebrow | DM Sans | 500 | 0.75rem | 1.4 | 0.08em (uppercase) |
| Data / Price / THC% | JetBrains Mono | 400 | 0.875rem | 1.5 | 0 |

### Typography Rules
- **Clash Display:** display headings only — never body, never navigation, never labels
- **DM Sans:** all prose, UI copy, navigation, labels, captions
- **JetBrains Mono:** THC/CBD percentages, prices, product specs, dates — never for prose
- **Case:** Sentence case or Title Case — NO ALL CAPS on any body text or navigation
- **Max measure:** 65ch on body paragraphs — line length enforced
- **Tracking:** -0.02em on display, 0 on body, 0.08em on uppercase labels only

---

## 4. Component Stylings

### Buttons

```css
/* Primary — Gold fill */
.btn-primary {
  background: var(--color-accent);
  color: #0D0D0B;
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 0.9375rem;
  padding: 12px 28px;
  border-radius: 3px;
  border: none;
  transition: transform 0.15s ease, opacity 0.15s ease;
}
.btn-primary:hover { transform: translateY(-1px); opacity: 0.92; }
.btn-primary:active { transform: translateY(0) scale(0.98); }

/* Secondary — Gold outline */
.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: 1px solid var(--color-accent-border);
  /* same padding, radius, font as primary */
}
.btn-secondary:hover { border-color: var(--color-accent); }

/* Ghost — for tertiary actions */
.btn-ghost {
  background: transparent;
  color: var(--color-text-secondary);
  border: 1px solid var(--color-border);
}
```

- border-radius: 3px — not pill, not square. Intentional, precise.
- No rounded-full buttons.
- No emoji or icon clutter inside buttons unless functionally necessary.

### Cards

```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 4px;
  padding: 32px;
}
/* Hover state */
.card:hover {
  background: var(--color-surface-raised);
  border-color: var(--color-accent-border);
}
```

- No generic box-shadow — borders create separation
- Padding: 32px — generous but not wasteful
- Cards used for product listings, event features, educational modules only

### Navigation

```css
nav {
  background: rgba(13, 13, 11, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border);
}
nav a {
  color: var(--color-text-secondary);
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 0.9375rem;
  transition: color 0.15s ease;
}
nav a:hover { color: var(--color-text-primary); }
nav a.active { color: var(--color-accent); }
```

### Tags & Badges

```css
.tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  background: var(--color-accent-subtle);
  border: 1px solid var(--color-accent-border);
  border-radius: 2px;
  font-family: var(--font-mono);
  font-size: 0.6875rem;
  color: var(--color-accent);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
```

### Form Inputs

```css
.input-field {
  background: transparent;
  border: 1px solid var(--color-border);
  border-radius: 3px;
  padding: 12px 16px;
  font-family: var(--font-body);
  font-size: 0.9375rem;
  color: var(--color-text-primary);
  width: 100%;
}
.input-field::placeholder { color: var(--color-text-muted); }
.input-field:focus {
  outline: none;
  border-color: var(--color-accent);
}
label {
  font-size: 0.8125rem;
  font-weight: 500;
  color: var(--color-text-secondary);
  margin-bottom: 8px;
  display: block;
}
```

---

## 5. Layout Principles

- **Max content width:** 1280px
- **Layout model:** Asymmetric — default `grid-template-columns: 3fr 2fr` for feature sections
- **Section spacing:** 80px
- **Content padding:** 40px horizontal at desktop, 20px on mobile
- **Column gutter:** 40px
- **Base spacing unit:** 4px

### Asymmetric Logic (DESIGN_VARIANCE: 8)
- Hero: 60/40 split — text left, visual right — never centered on desktop
- Product editorial: alternating left/right image/text pairs with deliberate white-space
- Community/events: magazine-style asymmetric grid with fractional columns
- Never: 3 equal columns in a feature row — use 2-column zig-zag or 1-col-full instead

### Spacing Scale (4px base)
```
4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128px
```

---

## 6. Depth & Elevation

- **Default:** No box-shadow. Depth comes from surface color variation and border contrast.
- **Elevated surfaces:** step up from `--color-bg` → `--color-surface` → `--color-surface-raised`
- **When shadow is required** (modal, dropdown, floating element):
  `box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5)` — tinted toward bg, never bright
- **Gold glow (CTAs only, max 1× per viewport):**
  `box-shadow: 0 0 24px rgba(201, 168, 76, 0.15)` — subtle, never neon
- **Z-index system:** 10 (sticky nav) · 50 (dropdowns) · 100 (modals) · 999 (toast/alert)

---

## 7. Do's and Don'ts

### Do's
- Use `#C9A84C` gold as the single accent — max 3× per viewport
- Add `rgba(255, 244, 220, 0.02)` as surface overlay tint for warmth on dark sections
- Use Clash Display for headings only — DM Sans carries the brand's warmth and approachability
- Photograph products like high-end spirits or CPG: elevated lighting, negative space, studio quality
- Let whitespace do structural work — silence communicates premium
- Reference the Eastside authentically: Juanita Beach, Totem Lake, actual Kirkland geography
- Use JetBrains Mono exclusively for product data (THC%, prices, specs)

### Don'ts
- NO cannabis leaf imagery or stereotypical green branding
- NO ALL CAPS body text, navigation, or CTAs
- NO deal-first, discount-led messaging above the fold
- NO 3-column equal card feature rows — break the grid (DESIGN_VARIANCE: 8)
- NO pill/rounded-full buttons
- NO generic stock photo humans
- NO Inter, Roboto, or Montserrat as primary typefaces
- NO pure `#000000` backgrounds — use `#0D0D0B`
- NO neon glows or oversaturated glow effects on text or UI
- NO percentage-off callouts as primary visual hierarchy
- NO carousel patterns (excludes: `carousel`)

---

## 8. Responsive Behavior

| Breakpoint | Value | Layout behavior |
|---|---|---|
| `sm` | 640px | Stack all asymmetric layouts to single column |
| `md` | 768px | Allow 2-column grids |
| `lg` | 1024px | Full asymmetric layout active |
| `xl` | 1280px | Max-width constraint kicks in |

- **Hero sections:** always `min-h-[100dvh]` — never `h-screen` (iOS Safari bug)
- **Type:** fluid via `clamp()` on all display headings — no hard breaks
- **Mobile padding:** 20px horizontal content padding at < 768px
- **Images:** `max-width: 100%`, aspect-ratio locked, never overflow

---

## 9. Agent Prompt Guide

When building any Bored N Buzzed Eastside Premium asset, begin with:

```
Background: #0D0D0B (warm near-black)
Primary text: #F4EFE6 (warm cream)
Accent: #C9A84C (aged gold — use max 3× per viewport)
Display font: Clash Display 700
Body font: DM Sans 400/500/600
Mono font: JetBrains Mono 400 (prices, THC%, data only)
Layout: Asymmetric — 3fr 2fr or 60/40 split. Never centered hero.
Borders over shadows for separation.
No deal percentages in hero or above fold.
No pill buttons. Border-radius: 3-4px on all interactive elements.
Silence is luxury — whitespace is a design element, not empty space.
```

---

## Appendix — Dimensions Resolved

| Dimension | Value | Rule applied |
|---|---|---|
| `palette` | `monochrome_dark_warm` (custom extension) | Editorial mood on dark base; warm tinting added for cannabis lifestyle warmth |
| `accent` | `elevated_gold` (custom extension of coral/warm default) | Spirit of current #FFD10B retained; saturation reduced, richness increased |
| `typography` | `dm_sans` | Highest legibility + warmth for community-forward brand |
| `display` | `clash_display` | Explicitly selected over space_grotesk for editorial authority at DESIGN_VARIANCE: 8 |
| `layout` | `asymmetric` | DESIGN_VARIANCE: 8 (taste-skill) mandates non-centered, fractional grid |
| `mood` | `editorial` | Derived from NotebookLM core insight: cultural authority + suburban premium |
| `density` | `balanced` (80px section gap) | VISUAL_DENSITY: 4 (taste-skill); premium breathing room without art-gallery emptiness |
| `exclude` | `stock_photos, carousel, discount_messaging, all_caps_body, cannabis_leaf_imagery` | Audit findings: these patterns actively undermine premium positioning |

---

*[[CLAUDE]] · [[Brand Identity/Brand Identity]] · [[Brand Identity/Visuals/brief-preview.html]]*
