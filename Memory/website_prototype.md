---
name: Website Prototype — v4
description: Current state of the B&B website prototype as of Session 18 (2026-05-07). Design direction, key decisions, iteration history, what's next.
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

## Session 18 Changes (2026-05-07)

- **Apple design pass:** Pill buttons globally (`button:not(.cat-tab){border-radius:9999px}`), 17px body, h2/h3 letter-spacing, always-on product card shadow `rgba(0,0,0,.22) 0 4px 20px`, hover lift + scale
- **Wyld Relaxing Collection:** 4 edible cards added to product grid (Cards 13–16). Images from wyldhemp.com CDN. Elderberry Sleep ($18), Boysenberry Dream ($18), Sour Cherry Mellow ($14), Marionberry Mellow ($14)
- **Jim Jones photos:** 3 real B&B event photos scraped from borednbuzzed.com/wp-content/uploads/2025/08/. 3-column photo strip added to Culture/Events section beneath YouTube embed. Hero mosaic was added then removed per user request.
- **Hero cleanup:** Eyebrow strip ("Kirkland, WA · Open Now · Est. 2023") and graffiti logo (Square Logo size.png) removed from hero per user direction.
- **Interior photo:** `bnb-interior.png` saved to `Website/` folder. Tested as hero background — user reverted to base state. **Will be implemented properly next session.**

## Current Hero State

No eyebrow strip. No graffiti logo. Hero contains:
- Coaster badge (top right, desktop only)
- Tagline: "Kirkland's home for curated cannabis. Premium selection. Real community."
- Shop the Menu + Our Story CTAs
- Address / Hours / Phone strip

Background: dark gradient (navy mood gradients + grain/halftone texture). **Next session goal:** implement `bnb-interior.png` as full-bleed hero background with proper dark overlay and content layout.

## Design Direction (LOCKED)

- **Energy:** Streetwear/lifestyle — loud, alive, community-forward. NOT sterile tech startup.
- **Typography:** Clash Display for display headings. DM Sans 17px body. JetBrains Mono for labels/mono.
- **Texture:** SVG `feTurbulence` grain at 5.5% opacity + halftone dot grid (30px, gold 7%). Both on hero AND brand story section.
- **Marquee:** Two bands — gold/navy deals ticker (32s, left) + muted reversed brand voice (38s, right). Pauses on hover. First item is "The Eastside Standard."
- **Rings:** Gold at 18/28/40% opacity. Anything lower reads as navy. Use `--ro` CSS variable.
- **Badge:** Coaster front image. Always `object-cover rounded-full` to clip the white square background.
- **Buttons:** Pill grammar — all interactive buttons except `.cat-tab` category filter strip.
- **Product cards:** Always-on shadow `rgba(0,0,0,.22) 0 4px 20px`. Hover: lift + scale + deeper shadow.

## Logo Placement

| Logo | Location |
|---|---|
| `Square Logo size.png` | Top nav only (h-16, 64px) — removed from hero in Session 18 |
| `BNB Coaster front.png` | Hero badge (top right, desktop) + brand story badge |
| `BNB LOGO.png` | Footer — `filter:invert(1)` to make white on dark |
| `BNB LOGO (Facebook Cover).png` | Hero background watermark — `opacity:.022; filter:invert(1)` |

## Product Grid (16 cards)

Cards 1–12: Soulshine, Kush Mountain, 28 Herbs, Cormorant, Mama J's (flower, vapes, concentrates, pre-rolls, edibles)
Cards 13–16: **Wyld Relaxing Collection** (edibles) — Elderberry Sleep, Boysenberry Dream, Sour Cherry Mellow, Marionberry Mellow

## Real B&B Photos Available

Located in `Website/` and remotely:
- `bnb-interior.png` — AI-rendered interior concept. Dark wall with gold "BORED AND BUZZED" lettering, two velvet chairs, plant, shelf display. **Use as hero background next session.**
- `https://borednbuzzed.com/wp-content/uploads/2025/08/Jimm-Jones-1-819x1024.png` — Jim Jones event photo 1
- `https://borednbuzzed.com/wp-content/uploads/2025/08/Jimm-Jones-2-1-819x1024.png` — Jim Jones event photo 2
- `https://borednbuzzed.com/wp-content/uploads/2025/08/Jimm-Jones-3-1-819x1024.png` — Jim Jones event photo 3 (all 3 currently in Culture/Events photo strip)

## What's Not Done Yet

- Hero photo implementation (next session — `bnb-interior.png`)
- Real product photography (currently using Wyld CDN + Leafly CDN + emoji/gradient placeholders)
- POS integration (Dutchie or equivalent — live inventory sync)
- Mobile polish pass (hero type wraps correctly, sidebar filter collapse)
- Production build: React + Vite + Tailwind npm (do this when design is locked)
- WebGPU/Three.js hero FX (optional enhancement after production build)
