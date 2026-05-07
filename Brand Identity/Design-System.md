---
title: Bored N Buzzed — Eastside Premium Design System
tags: [brand, design-system, tokens, components, phase-1]
status: active
date: 2026-05-06
---

# Design System — Bored N Buzzed Eastside Premium

> **Source of truth for every asset this brand produces — digital and in-store.**
> Any asset that doesn't trace back to this document is off-brand.
> Built from: brand sprint + DESIGN.md + Logo-Usage-Guide + Brand-Voice + Brand-Pillars

---

## What This Document Is

This is the single design language for Bored N Buzzed. It answers the question **"what does on-brand look like?"** for every asset type: website, Instagram, price cards, event flyers, digital displays, email, and signage.

Three rule layers govern all decisions:
1. **[[Brand Identity/Visuals/design-tokens.json|design-tokens.json]]** — Machine-readable token definitions (3-layer: Primitive → Semantic → Component)
2. **[[Brand Identity/Visuals/design-tokens.css|design-tokens.css]]** — CSS variable file for all web/digital assets
3. **This document** — Human interpretation: what to use, when, and why

---

## Design Language in One Sentence

> Warm dark. Aged gold. Expressive marks deployed in a premium system.

The brand is not trying to look like a dispensary. It's trying to look like the editorial cannabis destination the Eastside has been waiting for. Every design decision should ask: *does this look like something you'd find at a Kinfolk-shot Ace Hotel, or does it look like a deal flyer?*

---

## Core Token Quick Reference

| Token | Value | Use |
|---|---|---|
| `--color-bg` | `#0D0D0B` | All page/canvas backgrounds |
| `--color-surface` | `#161612` | Cards, panels, section fills |
| `--color-surface-raised` | `#1F1F19` | Elevated surfaces, hover states |
| `--color-border` | `#2A2A24` | Dividers, card edges — no shadows |
| `--color-text-primary` | `#F4EFE6` | All primary copy |
| `--color-text-secondary` | `#8D867A` | Labels, captions, nav links |
| `--color-text-muted` | `#5A544E` | Placeholder, disabled |
| `--color-accent` | `#C9A84C` | Gold — CTAs, active, highlights (max 3× per viewport) |
| `--color-accent-hover` | `#B8963C` | Deeper on hover — never brighter |
| `--color-navy` | `#0F2640` | Section bgs (events, hero anchors) — not primary UI |
| `--font-display` | Clash Display 700 | Display headings only — H1, H2 |
| `--font-body` | DM Sans 400/500/600 | All prose, UI, navigation, labels |
| `--font-mono` | JetBrains Mono 400 | THC%, prices, specs, data — never prose |

---

## Typography System

### Scale

| Role | Font | Weight | Size | Leading | Tracking |
|---|---|---|---|---|---|
| H1 / Display | Clash Display | 700 | `clamp(2.5rem, 6vw, 5rem)` | 1.05 | -0.02em |
| H2 | Clash Display | 700 | `clamp(1.75rem, 4vw, 3rem)` | 1.1 | -0.01em |
| H3 / Subhead | DM Sans | 600 | `clamp(1.125rem, 2.5vw, 1.5rem)` | 1.2 | 0 |
| Body | DM Sans | 400 | 1rem | 1.65 | 0 |
| UI / Button | DM Sans | 600 | 0.9375rem | — | 0 |
| Label / Caption | DM Sans | 500 | 0.8125rem | 1.4 | 0.01em |
| Eyebrow | DM Sans | 500 | 0.75rem | 1.4 | 0.08em |
| Tag | DM Sans | 500 | 0.75rem | — | 0.08em |
| Data / Price / THC | JetBrains Mono | 400 | 0.875rem | 1.5 | 0 |

### Rules

- **Clash Display:** H1 and H2 only. Never body, navigation, labels, buttons.
- **DM Sans:** Everything else — prose, UI, navigation, captions, buttons, labels.
- **JetBrains Mono:** Data only — THC/CBD percentages, prices, product specs, weight, dates.
- **Case:** Sentence case everywhere. Title Case for proper names. NO ALL CAPS on body text.
- **Max measure:** 65 characters on body paragraphs — line length matters.
- **Eyebrow tags** (uppercase labels above a heading): always JetBrains Mono OR DM Sans 500 with `letter-spacing: 0.08em` — never Clash Display.

### CDN Import

```css
@import url('https://api.fontshare.com/v2/css?f[]=clash-display@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=JetBrains+Mono:wght@400&display=swap');
```

---

## Color System

### The Four Groups

**1. Warm Dark Core** — page, surface, border
`#0D0D0B` → `#161612` → `#1F1F19` → `#2A2A24`
> Each step adds warmth and lift. Used in sequence — never jump two steps.

**2. Text Stack** — cream to muted
`#F4EFE6` → `#8D867A` → `#5A544E`
> Always warm-toned. Never pure white. Never pure gray.

**3. Aged Gold Accent** — the brand's energy
`#C9A84C` → `#B8963C` → `rgba(201,168,76,0.25)` → `rgba(201,168,76,0.10)`
> Use the solid at full strength for CTAs. Use the alphas for fills and borders. Max 3× solid uses per viewport.

**4. Deep Navy Depth** — for anchoring
`#0F2640` → `#1A3D5C`
> Not a UI color. A section color. Use for event backdrops, hero anchors, section transitions.

### What's Retired

| Old value | Why retired | Replacement |
|---|---|---|
| `#FFD10B` | Budget-signaling saturation | `#C9A84C` (spirit retained) |
| `#0274BE` | Corporate flatness | `#0F2640` (spirit retained) |
| `#000000` | Pure black reads cheap | `#0D0D0B` |
| `#FFFFFF` | Clinical — wrong warmth | `#F4EFE6` |

---

## Component Specifications

### Buttons

| State | Background | Text | Border | Transform |
|---|---|---|---|---|
| Default | `#C9A84C` | `#0D0D0B` | none | — |
| Hover | `#B8963C` | `#0D0D0B` | none | `translateY(-1px)` |
| Active | `#B8963C` | `#0D0D0B` | none | `scale(0.98)` |
| Disabled | `rgba(201,168,76,0.3)` | `rgba(13,13,11,0.5)` | none | — |

**Secondary button:** `bg: transparent` · `color: #C9A84C` · `border: rgba(201,168,76,0.25)` → on hover: `border: #C9A84C`
**Ghost button:** `bg: transparent` · `color: #8D867A` · `border: #2A2A24`

**Never:** pill/rounded-full buttons. **Border-radius: 3px (—radius-sm)** on all buttons. Period.

---

### Cards

| Property | Default | Hover |
|---|---|---|
| Background | `#161612` | `#1F1F19` |
| Border | `1px solid #2A2A24` | `1px solid rgba(201,168,76,0.25)` |
| Border radius | `4px` | `4px` |
| Padding | `32px` | `32px` |
| Shadow | none | none |

**Navy card variant:** bg `#0F2640` · border `#1A3D5C` — for event features, premium moments.

**Never use box-shadow for card separation.** Borders do the structural work. Shadow is reserved for floating elements (modals, dropdowns).

---

### Navigation

| Property | Value |
|---|---|
| Height | 64px |
| Background | `rgba(13,13,11,0.85)` + `backdrop-filter: blur(12px)` |
| Bottom border | `1px solid #2A2A24` |
| Link — default | `#8D867A` (DM Sans 500, 15px) |
| Link — hover | `#F4EFE6` |
| Link — active | `#C9A84C` |

---

### Tags & Badges

| Property | Value |
|---|---|
| Background | `rgba(201,168,76,0.10)` |
| Border | `1px solid rgba(201,168,76,0.25)` |
| Text | `#C9A84C` |
| Font | JetBrains Mono 400, 0.6875rem |
| Case | UPPERCASE |
| Letter-spacing | 0.08em |
| Border-radius | 2px |
| Padding | 4px 10px |

Used for: THC classification (INDICA / SATIVA / HYBRID), product tiers, event types, strain category labels.

---

### Form Inputs

| State | Border | Background | Text |
|---|---|---|---|
| Default | `#2A2A24` | transparent | `#F4EFE6` |
| Focus | `#C9A84C` | transparent | `#F4EFE6` |
| Placeholder | `#2A2A24` | transparent | `#5A544E` |
| Error | `rgba(220,50,50,0.6)` | transparent | `#F4EFE6` |

Label always above input. 8px gap. DM Sans 500, 0.8125rem, `#8D867A`.

---

### Price Cards (In-Store + Digital Menu)

Structure:
```
[HEADER — bg: #0D0D0B] — thin gold bar (1px #C9A84C) — [PRODUCT NAME + STRAIN TAGS]
[BODY — bg: #161612] — [PRICE in JetBrains Mono] · [THC% in gold Mono] · [WEIGHT in stone Mono]
```

Rules:
- Price always JetBrains Mono — the only element that size and weight at that scale
- THC/CBD always in `#C9A84C` (gold) — it's the data that makes the sale
- Weight/volume always in `#8D867A` (stone secondary)
- Product name always DM Sans 600 — not Clash Display (too big for card context)
- The gold accent bar is the brand signal — 1px, full-width, between header and body

---

## Layout System

### Core Layout Rules (DESIGN_VARIANCE: 8)

- **Asymmetric by default.** `grid-template-columns: 3fr 2fr` for feature sections.
- **Never 3 equal columns** — use 2-col zig-zag, 1-col-full, or asymmetric fraction grid.
- **Never centered hero on desktop** — 60/40 split: text left, visual right.
- **Max content width:** 1280px
- **Section spacing:** 80px (top and bottom)
- **Content padding:** 40px horizontal at desktop
- **Mobile padding:** 20px horizontal
- **Column gap:** 40px
- **Base unit:** 4px (all spacing is multiples)

### Spacing Scale

`4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128px`

---

## Logo Deployment

### Asset Quick Reference

| File | Format | Use |
|---|---|---|
| `BNB LOGO.png` | PNG / black | Light bgs, print, coasters |
| `BNB LOGO (Facebook Cover).png` | PNG / white | Dark bgs, digital, social headers |
| `Square Logo size.png` | PNG / white | Square crops, profile frames |
| `BNB Coaster front.png` | PNG / badge | Lifestyle, events, merch |

Full usage rules: **[[Brand Identity/BnB Logos/Logo-Usage-Guide]]**

### Logo Color Treatments (CSS)

```css
/* White version — for dark backgrounds */
.logo-white { filter: brightness(0) invert(1); }

/* Gold version — for premium moments */
.logo-gold {
  filter: brightness(0) saturate(100%) invert(68%) sepia(48%) saturate(500%) hue-rotate(5deg) brightness(95%);
}

/* Black — as-is on light backgrounds */
.logo-black { /* no filter needed */ }
```

---

## Cross-Touchpoint Consistency Matrix

| Asset | Background | Logo | Primary font | Accent use |
|---|---|---|---|---|
| Website header | `#0D0D0B` | White wordmark | DM Sans nav | Gold on active |
| Website hero | `#0D0D0B` | None / wordmark | Clash Display H1 | 1× gold CTA |
| Digital display | `#0D0D0B` or `#0F2640` | White wordmark | Clash Display | Gold bar accent |
| Instagram feed | `#0D0D0B` | White wordmark | Clash Display | Gold sparing |
| Instagram Stories | `#0D0D0B` | Badge centered | DM Sans | Gold CTA |
| Price card (digital) | `#161612` | Header gold bar | JetBrains Mono | Gold THC%, bar |
| Price card (print) | Cream / white | Black wordmark | DM Sans | N/A (print) |
| Event flyer (digital) | `#0F2640` | White wordmark + badge | Clash Display | Gold ring on badge |
| Event flyer (print) | `#0F2640` | White wordmark | Clash Display | Gold |
| In-store signage | `#0D0D0B` | White wordmark | DM Sans | Gold accent bar |
| Merch (dark stock) | Black | White wordmark | N/A | Gold foil treatment |
| Merch (light stock) | Cream | Black wordmark | N/A | Black ink |
| Email header | `#0D0D0B` | White wordmark | Clash Display | Gold CTA |

---

## Asset-Specific Rules

### Social (Instagram, TikTok, Facebook)

- **Feed posts:** Dark bg (#0D0D0B), Clash Display headline, max 2 lines of copy visible, no ALL CAPS
- **Reels thumbnail:** Same dark base, bold left-aligned headline, badge in corner as brand identifier
- **Story:** Full-bleed dark or navy, badge centered, DM Sans body, gold CTA button
- **Profile avatar:** Badge (BNB Coaster front.png) — circular, no modification needed
- **Always:** 21+ language in bio, no health claims, no price promotion in paid content

### In-Store Digital Displays

- **Format:** 16:9 loops, full-bleed backgrounds
- **Template structure:**
  - Top-left: white wordmark (small, 32-40px height)
  - Bottom-right: badge (80-100px diameter)
  - Center: product name in Clash Display + specs in JetBrains Mono
  - Thin gold horizontal rule (1px `#C9A84C`) separates sections
- **Background:** `#0D0D0B` standard · `#0F2640` for featured/event content
- **Never:** Busy photographic backgrounds without dark overlay at 70%+ opacity

### In-Store Print Signage

- **Light signage (walls, frames):** Black wordmark on cream (#F4EFE6) — approachable, editorial
- **Header strips:** White wordmark on #0D0D0B bar — product name in DM Sans below
- **Featured product callouts:** Gold (#C9A84C) accent dot or bar left edge, product name DM Sans 600, price JetBrains Mono

### Canva Template Guidance

For team members building in Canva:
- **Hex codes to save:** `#0D0D0B` · `#161612` · `#F4EFE6` · `#C9A84C` · `#8D867A` · `#0F2640`
- **Fonts in Canva:** Use `DM Sans` (available in Canva Free) + upload Clash Display if needed
- **Grid:** Canva 40px gutters, asymmetric — never centered layouts
- **Logo file to use:** "BNB LOGO (Facebook Cover).png" for dark backgrounds, "BNB LOGO.png" for light

---

## Quality Gate — Every Asset

Before any asset ships, it must pass all 7:

- [ ] Background is from the approved token set — never a random color
- [ ] No ALL CAPS body text or navigation
- [ ] No health or medical benefit claims (WSLCB)
- [ ] 21+ language present on all digital assets
- [ ] Accent gold appears max 3× per asset (more = deal flyer, not premium)
- [ ] Price and THC data use JetBrains Mono — not DM Sans
- [ ] Logo placement follows Logo-Usage-Guide — no crop, no skew, no effects

Full pre-publish checklist: **[[Compliance/Compliance]]**

---

## What This System Replaces

| Old pattern | New pattern | Why |
|---|---|---|
| #FFD10B yellow everywhere | `#C9A84C` gold, used sparingly | Budget signaling → premium signal |
| Montserrat for everything | Clash Display (display) + DM Sans (body) + JetBrains Mono (data) | One font = no hierarchy |
| Centered hero layouts | 60/40 asymmetric split | Centered = generic |
| Box-shadow on cards | Border only | Shadows feel cheap at this palette |
| ALL CAPS CTAs | Sentence case, weight-driven hierarchy | Shouting ≠ premium |
| Discount-led messaging | Product/community-led messaging | Deals follow brand, not vice versa |
| 3-column equal feature rows | 2-col zig-zag or 1+2 fractional | Equal columns = zero tension |
| Pill/rounded buttons | 3px radius buttons | Pill = generic SaaS, not cultural |

---

## File Index

| File | Location | Purpose |
|---|---|---|
| `design-tokens.json` | `Brand Identity/Visuals/` | 3-layer machine-readable tokens |
| `design-tokens.css` | `Brand Identity/Visuals/` | CSS variables for all web/digital |
| `DESIGN.md` | `Brand Identity/Visuals/` | Full design system specification |
| `brief-preview.html` | `Brand Identity/Visuals/` | Live token preview |
| `Logo-Usage-Guide.md` | `Brand Identity/BnB Logos/` | Logo deployment rules |
| `logo-preview.html` | `Brand Identity/BnB Logos/` | Live logo variant preview |
| `BnB-Brand-Kit.html` | `Brand Identity/` | Full Phase 1 brand kit deliverable |
| `Brand-Voice.md` | `Brand Identity/Voice/` | Copy tone, voice principles |
| `Brand-Pillars.md` | `Brand Identity/Pillars/` | 3 brand pillars + messaging matrix |

---

*[[CLAUDE]] · [[Brand Identity/Brand Identity]] · [[Brand Identity/Visuals/DESIGN.md]] · [[Brand Identity/BnB Logos/Logo-Usage-Guide]]*
