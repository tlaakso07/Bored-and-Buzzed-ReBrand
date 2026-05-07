---
name: Website Prototype — v4
description: Current state of the B&B website prototype as of Session 19 (2026-05-07). Design direction, hero photo, layout decisions, what's next.
type: project
originSessionId: 28d97ddd-d7cf-4f9a-972a-2020b465b11a
---
Current working file: `Website/BnB-Website-Prototype-v4.html`
Standalone (offline): `Website/BnB-Website-Standalone.html`

**Why:** Phase 2 website redesign. Goal is to convert Eastside cannabis search traffic into in-store foot traffic. Prototype phase uses Tailwind CDN for speed; production build will be React + Vite + Tailwind npm.

**How to apply:** Always iterate on v4 (or increment to v5) — never go back to v1–v3. Design direction locked: streetwear/lifestyle energy, NOT tech startup or sterile.

## Iteration History

| Version | Key Change |
|---|---|
| v1 | Initial prototype from impeccable + ui-ux-pro-max audit of Uncle Ike's |
| v2 | Audit fixes: contrast pass (WCAG AA), focus rings, touch targets |
| v3 | Logo integration (all 4 logos), full high-end redesign with concentric rings |
| v4 | **Current.** Tailwind CDN rebuild. Streetwear hero. Dual scrolling marquee. SVG grain + halftone. |

## Session 19 Changes (2026-05-07)

- **Old ape photo removed**: First hero photo (ape with neon) removed per user — not happy with it. Three.js, Spring physics, canvas element all stripped. Hero returned to clean atmospheric dark base.
- **Hero layout restructure**: Tagline paragraph removed. Two-column bottom layout:
  - Left: Shop the Menu + Our Story buttons side-by-side (under "BORED N BUZZED" in image)
  - Right: Address · Hours · Phone (under "Stay One Puff Ahead" in image)
- **New hero photo**: `bnb-hero-bg.jpg` — square 2048×2054px, JPEG 92%, 1.14MB. Neon ape scene with cannabis plants, "BORED N BUZZED" left, ape center, "Stay One Puff Ahead" right.
- **Implementation**: `object-cover object-center` — uniform scale only, zero distortion. `min-height: clamp(480px, 52vw, 680px)`. Bottom gradient 40% height for text readability.
- **Standalone sync**: JPEG base64-embedded (~1.5MB encoded) — works from `file://`.

## Current Hero State

No tagline. No heading. Layout:
- Full-bleed square photo, `object-cover object-center`, no stretch
- Bottom 40% darkened gradient (95%→70%→transparent)
- Grain overlay 4% on top
- **Left bottom**: Shop the Menu + Our Story (side by side, `flex-row gap-4`)
- **Right bottom**: Address · Hours · Phone (`flex items-center gap-6`)
- Container: `flex items-end justify-between` — buttons and info span full width

## Design Direction (LOCKED)

- **Energy:** Streetwear/lifestyle — loud, alive, community-forward. NOT sterile tech startup.
- **Typography:** Clash Display for display headings. DM Sans 17px body. JetBrains Mono for labels/mono.
- **Texture:** SVG `feTurbulence` grain at 4-5.5% opacity + halftone dot grid (30px, gold 7%). Both on hero AND brand story section.
- **Marquee:** Two bands — gold/navy deals ticker (32s, left) + muted reversed brand voice (38s, right). Pauses on hover.
- **Buttons:** Pill grammar — all interactive buttons except `.cat-tab` category filter strip.
- **Product cards:** Always-on shadow `rgba(0,0,0,.22) 0 4px 20px`. Hover: lift + scale + deeper shadow.

## Logo Placement

| Logo | Location |
|---|---|
| `Square Logo size.png` | Top nav only (h-16, 64px) |
| `BNB Coaster front.png` | Brand story badge |
| `BNB LOGO.png` | Footer — `filter:invert(1)` |
| `BNB LOGO (Facebook Cover).png` | Hero background watermark (if used) |

## Product Grid (16 cards)

Cards 1–12: Soulshine, Kush Mountain, 28 Herbs, Cormorant, Mama J's (flower, vapes, concentrates, pre-rolls, edibles)
Cards 13–16: Wyld Relaxing Collection (edibles) — Elderberry Sleep, Boysenberry Dream, Sour Cherry Mellow, Marionberry Mellow

## Hero JS (current — simplified atmosphere)

No Three.js. No Spring physics. No card tilt. Just:
- Mouse position tracking → `bgEl` radial glow follows cursor
- Text parallax on `#hero-text` (subtle drift)
- 22 gold particles floating upward

## What's Not Done Yet

- **Review hero in browser** — confirm crop looks right, tune `52vw` if needed
- Real product photography (currently using Wyld CDN + Leafly CDN + placeholders)
- POS integration (Dutchie or equivalent — live inventory sync)
- Mobile polish pass
- Production build: React + Vite + Tailwind npm
- Platform audits: Weedmaps, Leafly, Google, Yelp
