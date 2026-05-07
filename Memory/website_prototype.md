---
name: Website Prototype — v4
description: Current state of the B&B website prototype as of Session 17 (2026-05-07). Design direction, key decisions, iteration history, and what's next.
type: project
originSessionId: a77dcea3-4b3e-4aa9-ad77-05666d5d8d63
---
Current working file: `Website/BnB-Website-Prototype-v4.html`

**Why:** Phase 2 website redesign. Goal is to convert Eastside cannabis search traffic into in-store foot traffic. Prototype phase uses Tailwind CDN for speed; production build will be React + Vite + Tailwind npm.

**How to apply:** Always iterate on v4 (or increment to v5) — never go back to v1–v3. The design direction is locked: streetwear/lifestyle energy, NOT tech startup or sterile.

## Iteration History

| Version | Key Change |
|---|---|
| v1 | Initial prototype from impeccable + ui-ux-pro-max audit of Uncle Ike's |
| v2 | Audit fixes: `--muted` contrast pass (WCAG AA), focus rings, touch targets, deal card anti-pattern removal |
| v3 | Logo integration (all 4 logos placed), full high-end redesign with concentric rings, massive hero |
| v4 | **Current.** Tailwind CDN rebuild. Streetwear energy hero. Dual scrolling marquee. SVG grain + halftone textures. |

## Design Direction (LOCKED)

- **Energy:** Streetwear/lifestyle — loud, alive, community-forward. NOT sterile tech startup.
- **Typography:** Clash Display at `clamp(52px, 10.5vw, 158px)` for hero H1. "EASTSIDE" as gold outline text (`-webkit-text-stroke`). Gold period on "STANDARD."
- **Texture:** SVG `feTurbulence` grain at 5.5% opacity + halftone dot grid (30px, gold 7%). Both on hero AND brand story section.
- **Marquee:** Two bands — gold/navy deals ticker (32s, left) + muted reversed brand voice (38s, right). Pauses on hover.
- **Rings:** Gold at 18/28/40% opacity. Anything lower reads as navy. Use `--ro` CSS variable.
- **Badge:** Coaster front image. Always `object-cover rounded-full` to clip the white square background.

## Logo Placement

| Logo | Location |
|---|---|
| `Square Logo size.png` | Top nav — `h-16` (64px) |
| `BNB Coaster front.png` | Age gate + hero badge + brand story badge |
| `BNB LOGO.png` | Footer — `filter:invert(1)` to make white on dark |
| `BNB LOGO (Facebook Cover).png` | Hero background watermark — `opacity:.022; filter:invert(1)` |

## What's Not Done Yet

- Real product photography (currently using emoji/gradient placeholders)
- POS integration (Dutchie or equivalent — live inventory sync)
- Mobile polish pass (hero type wraps correctly, sidebar filter collapse)
- Production build: React + Vite + Tailwind npm (do this when design is locked)
- WebGPU/Three.js hero FX (optional enhancement after production build)
