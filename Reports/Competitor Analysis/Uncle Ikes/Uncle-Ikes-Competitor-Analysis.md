---
title: Uncle Ike's — Competitor Analysis
tags: [competitor, website, seo, wireframe, uncle-ikes]
date: 2026-05-06
status: complete
---

# Uncle Ike's — Competitor Analysis
> Scraped 2026-05-06 via SkillUI ultra + Firecrawl. Use as the structural blueprint for B&B website build.

---

## 1. Tech Stack (Confirmed)

| Layer | Technology |
|---|---|
| Framework | React + React Router v7 (Remix-style SSR) |
| Styling | Tailwind CSS (custom config, custom color tokens) |
| State | React Query (TanStack Query) — dehydrated state on page load |
| Build | Vite (confirmed via asset fingerprints: `root-C3bBtHE4.css`, `pages-DGAywfuL.css`) |
| POS/Menu | Dutchie (confirmed via `dopeapps.io` CDN, coupon system, product API) |
| GTM | Google Tag Manager (GTM-XXXXXXX) |
| Images | Cloudflare/DopeApps CDN (`static.dopeapps.io`) |

**B&B Build Target:** Same stack — React + Tailwind + Vite + React Query. Dutchie or equivalent POS integration.

---

## 2. Site Architecture / URL Map

```
ikes.com/
├── /menu                          → Main shop (redirects to /categories/*)
├── /categories/
│   ├── /flower                    → Flower catalog (2,432 total products)
│   ├── /edibles
│   │   └── /edible-liquid
│   ├── /concentrates
│   ├── /vaporizers
│   │   ├── /cartridge
│   │   └── /disposable-vapes
│   ├── /pre-rolls
│   │   ├── /preroll
│   │   ├── /preroll-pack
│   │   ├── /infused-preroll
│   │   └── /infused-preroll-pack
│   ├── /topicals
│   └── /accessories
├── /specials                      → Active deals page
├── /price-match                   → Price match guarantee
├── /locations                     → All 5 store locations
│   └── /locations/white-center
├── /[location]-menu               → Per-location menu pages
├── /[location]-specials           → Per-location specials
├── /about
├── /blog
├── /faqs
├── /jobs
├── /vendor-delivery
├── /search
├── /cart
├── /privacy-policy
├── /terms-of-use
└── /consumer-health-data
```

**Shortcut SEO URLs** (redirect to categories):
`/flower`, `/indica`, `/edibles`, `/gummies`, `/candy`

---

## 3. Location Gate UX Pattern

Every page entry triggers a full-screen location selector modal before showing any content.

```
┌─────────────────────────────────────────────────────┐
│  [dark bg: Urbangraffiti-dark.jpg + 40% overlay]    │
│  ┌───────────────────────────────────────────────┐  │
│  │  [Logo]    ALL STORES OPEN 8AM-11:45PM  [H1]  │  │
│  │                                               │  │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌────┐  │  │
│  │  │ IMG  │ │ IMG  │ │ IMG  │ │ IMG  │ │IMG │  │  │
│  │  │      │ │      │ │      │ │      │ │    │  │  │
│  │  │CAPOL │ │CENTR │ │ LAKE │ │OLIVE │ │W.C.│  │  │
│  │  │ HILL │ │ DIST │ │ CITY │ │ WAY  │ │OUT │  │  │
│  │  │address│ │address│ │address│ │address│ │addr│  │  │
│  │  └──────┘ └──────┘ └──────┘ └──────┘ └────┘  │  │
│  │                                               │  │
│  │  ☐ I agree to Privacy Policy & Terms         │  │
│  │                          [CONTINUE →]         │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

**Key CSS patterns:**
- `fixed inset-0 z-50` — full-screen overlay
- `bg-[url('/images/Urbangraffiti-dark.jpg')] bg-cover`
- Modal: `bg-background backdrop-blur-sm rounded-4xl border border-frost/50`
- Location cards: `grid-cols-2 md:grid-cols-3 lg:grid-cols-5`
- Active selection: `border-4 border-secondary-500` (orange highlight)
- CTA: `bg-secondary-500 text-on-secondary font-bold uppercase tracking-wider rounded-lg`

**B&B Adaptation:** Single location (Kirkland) — replace with age verification gate only, skip location selector.

---

## 4. Navigation Structure

```
[Logo]  [Menu] [Specials] [Locations] [Blog] [About]    [Search 🔍] [Cart 🛒]
```

- Sticky top nav
- Logo: SVG at `h-8 md:h-10` (32-40px tall)
- Hours prominently displayed: **ALL STORES OPEN 8AM – 11:45PM**
- Nav items: uppercase, bold, tracking-wider
- CTA elements: search icon + cart icon (right-aligned)

---

## 5. Menu / Product Page Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│ [STICKY NAV]                                                │
├────────────────┬────────────────────────────────────────────┤
│                │  Flower  (480)          Sort: Popular ▼    │
│  CATEGORIES    ├─────────────────────────────────────────────┤
│  ─────────── │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     │
│  Flower       │  │[IMG] │ │[IMG] │ │[IMG] │ │[IMG] │     │
│  Edibles      │  │      │ │      │ │      │ │      │     │
│  Concentrates │  │Name  │ │Name  │ │Name  │ │Name  │     │
│  Vaporizers   │  │Brand │ │Brand │ │Brand │ │Brand │     │
│  Pre-Rolls    │  │Indica│ │Sativa│ │Hybrid│ │Indica│     │
│  Topicals     │  │THC % │ │THC % │ │THC % │ │THC % │     │
│  Accessories  │  │$XX   │ │$XX   │ │$XX   │ │$XX   │     │
│               │  │[ADD] │ │[ADD] │ │[ADD] │ │[ADD] │     │
│  FILTERS      │  └──────┘ └──────┘ └──────┘ └──────┘     │
│  ─────────── │                                             │
│  Strain Type  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     │
│  Brand        │  │[IMG] │ │[IMG] │ │[IMG] │ │[IMG] │     │
│  Price        │  └──────┘ └──────┘ └──────┘ └──────┘     │
│  THC %        │                                             │
│  Weight       │  [LOAD MORE / PAGINATION]                  │
│  On Sale      │                                             │
└────────────────┴────────────────────────────────────────────┘
```

**Product Card Fields:**
- Product image (full card width)
- Product name
- Brand name
- Strain type indicator (Indica / Sativa / Hybrid / CBD)
- THC% 
- Weight options (1g / 2g / 3.5g / 7g / 14g / 28g)
- Price
- Add to Cart CTA
- On-sale badge (if applicable)

**Sort Options:** Popular (default), Newest, Price Low-High, Price High-Low, THC%
**Filter Options:** Strain Type, Brand, Price Range, THC%, Weight, On Sale Only, In Stock Only
**Page Size:** 20 products per page

---

## 6. Product Inventory Scale

| Category | Count |
|---|---|
| Flower | 480 |
| Concentrate | 262 |
| Cartridge | 262 |
| Disposable Vapes | 268 |
| Preroll Pack | 116 |
| Infused Preroll | 123 |
| Infused Preroll Pack | 123 |
| Edible (Solid) | 197 |
| Edible (Liquid) | 74 |
| Low THC Drinks | 97 |
| Topical | 15 |
| **TOTAL** | **2,432** |

**Strain Split (Flower):** Indica 693 · Hybrid 607 · Sativa 579 · CBD 57

**Weight Distribution:** Gram (1g) = 1,184 products — by far the most common size offered.

---

## 7. Specials / Deals Structure

Active deals as of 2026-05-06:

| Deal | Products |
|---|---|
| 50% off - Mama J's Brands | 124 |
| 50% Off Cookies 7g | 12 |
| 40% Off - Brands | 747 |
| 30% Off - Brands | 1,008 |
| 40% Off - Ounces $99+ | 38 |
| 50% Off - Mr. Moxey's Mints | 7 |
| 50% off - Journeyman | 28 |
| 50% off - Phat Panda Brands | 288 |
| 50% Off - Flash Sale Items | — |
| 7 For $70 Carts | 27 |
| 50% - Clearance Blow Out | 128 |

**Pattern:** Heavy discounting — 30–50% off is standard. Multiple concurrent brand-specific deals. Urgency-driven naming ("Flash Sale," "Blow Out").

**B&B Angle:** B&B should be selective — premium positioning means fewer, more intentional deals. "Drop Pricing" > "Blow Out."

---

## 8. Brand Positioning / Copy

**Store description (verbatim):**
> "Your Most Trusted Cannabis Dispensary — Uncle Ike's Pot Shop provides a diverse range of cannabis products catering to both recreational and medicinal purposes. Our well-trained Budtenders are dedicated to addressing your inquiries and assisting you in selecting the right products tailored to your individual requirements. Our extensive inventory encompasses various offerings, catering to varying budgetary considerations and preferences. Uncle Ike's prides itself on fostering a contemporary, inviting environment where patrons can comfortably engage. We regularly feature promotions, flash sales, and discounted items."

**OG / Meta title pattern:** `[Page] | [Location Name]`
**Meta description pattern:** `Shop our [category] at [Location]. Browse [product types] in Seattle.`

**Tone:** Functional, accessible, volume-first. No craft/premium language. "Diverse range" / "varying budgetary considerations" — commoditized.

---

## 9. SEO Signals

| Page | Title | Description |
|---|---|---|
| Homepage | Central District - Seattle's Premier Cannabis Dispensary | Shop premium cannabis products at Uncle Ike's. Browse our selection of flower, edibles, concentrates, and more. |
| Menu/Flower | Shop Cannabis Menu \| Central District | Shop our full menu of premium cannabis products at Central District. Browse flower, edibles, vapes, pre-rolls and more in Seattle. |
| Specials | Cannabis Specials - Uncle Ikes | Check out our latest deals and save on premium cannabis products. |

**Breadcrumb schema:** `Home > Categories > Flower`
**Location structured data:** per-store slug URLs (`/central-district-menu`, `/capitol-hill-menu`)

**B&B SEO Opportunities:**
- Target "Kirkland dispensary" / "Eastside cannabis" / "Redmond dispensary" — Ikes is Seattle-only, no Eastside presence
- Long-tail: "best dispensary Kirkland WA" / "cannabis delivery Kirkland" / "dispensary near Bellevue"
- B&B can own the entire Eastside SERP — Ikes doesn't compete there

---

## 10. Design System Summary (for B&B Build Reference)

| Token | Ikes Value | B&B Equivalent |
|---|---|---|
| Primary CTA | `#F88240` (orange) | `#C9A84C` (aged gold) |
| Background | Dark (`#0D0D0B` approx) | `#0D0D0B` (warm dark) |
| Text | `#F4EFE6` (frost) | `#F4EFE6` (cream) |
| Border | `frost/50` (white 50%) | `frost/20` |
| Heading Font | Saira | Clash Display |
| Body Font | Futura / Saira | DM Sans |
| Border Radius CTA | `rounded-lg` (8px) | `rounded-sm` (2px) — more premium |
| Max Width | 96rem | 96rem |
| Grid | 4px base | 4px base |
| Layout | Symmetric grid | Asymmetric (DESIGN_VARIANCE: 8) |

---

## 11. B&B Competitive Advantages

| Ikes Weakness | B&B Opportunity |
|---|---|
| Seattle-only, no Eastside presence | Own every Eastside/Kirkland cannabis search query |
| Functional, commodity positioning | Premium, craft-forward, community-rooted brand |
| Heavy discounting signals low-price brand | Curated selection = perceived quality |
| Generic copy ("diverse range," "budgetary considerations") | Voice: "The Eastside Standard" — confident, specific |
| No craft/artisan brand story | B&B has vendor relationships (SKÖRD etc.) — story-driven |
| Multi-location complexity | Single-location focus = deeper community connection |
| No blog/SEO content strategy | B&B can own educational cannabis content for Eastside |
| Dark UX (age gate on every page) | B&B: smoother entry, premium first impression |

---

*[[CLAUDE]] · [[Reports/Reports]] · Source: SkillUI ultra + Firecrawl 2026-05-06*
