
---
title: Bored N Buzzed — Website Audit
date: 2026-05-06
tags: [audit, website, brand, phase-1]
status: complete
---

# Website Audit — borednbuzzed.com
**Scraped:** 2026-05-06 · **Pages crawled:** 34 · **Tools:** Firecrawl full crawl + branding extraction

> [!tip] How to use this
> This is the baseline. Everything we build in the rebrand is measured against what exists here. Read this before the brand sprint.

---

## Current Brand Identity (Extracted)

### Visual Design System
| Element | Current State |
|---|---|
| **Primary color** | #FFD10B (bright yellow) |
| **Secondary color** | #0274BE (blue) |
| **Accent** | #69727D (gray) |
| **Background** | #FFFFFF (white) |
| **Text** | #111111 |
| **Font** | Montserrat — used for everything (headings, body, nav) |
| **Heading sizes** | H1: 49px · H2: 42px · Body: 14px |
| **Border radius** | 3px |
| **Heading style** | ALL CAPS throughout |
| **Color feel** | Generic, mid-market, not premium |

### Current Tagline
> "STAY ONE PUFF AHEAD"

### Name (official)
**Bored N Buzzed** (not "Bored and Buzzed" — note for rebrand)

### Tech Stack
- WordPress 6.9.4 + Elementor 4.0.0
- POS: **POSaBit** (ecomm-app.posabit.com/bored-n-buzzed-kirkland)
- Rewards: take.cards/PEM8L (Apple/Google Wallet)

---

## Site Map (All Pages)

### Core
- `/` — Homepage
- `/about/` — About page
- `/findus/` — Location + hours
- `/contact/` — ⚠️ BROKEN (template data — see Bugs section)
- `/privacypolicy/`

### Shop / Menu
- `/shop-flower/` — Menu embed (POSaBit), noindex
- `/menu/` — Menu embed, noindex
- `/flower/` — Category page + education
- `/edibles/` — Category page + education
- `/concentrate/` — Category page + education

### Deals & Promotions
- `/daily-deals/` — Full daily deal calendar
- `/promos-discounts/` — Brand spotlights + featured products
- `/28-herbs/` — Monthly brand promo page

### Brand Partner Pages
- `/mfused/` · `/soulshine/` · `/skyhigh/` · `/picc/`
- Kush Mountain referenced in nav but no page

### Rewards
- `/rewards-program/` — Points-based loyalty wallet

### Events / Entertainment
- `/entertainment/` — Events hub
- `/blog-events-b1/` — Jim Jones event recap (Oct 2025)
- `/blog-events-b2/` — Mirra Bellevue afterparty

### Blog / Education
- `/blog/` — Blog index
- `/blog-beginners-guide/` — Dispensary beginner guide (Mar 2026)
- `/blogterpenes/` — Cannabis terpenes explainer (Mar 2026)
- `/elementor-page-7323/` — WA cannabis laws (Apr 2026)
- `/blogs-events-b2/` — MarkTellsYa partnership (Jan 2026)
- `/medical/` — Cannabis 101 hub (misnamed URL)

---

## Current Positioning

### How They Describe Themselves
> "We're offering premium flower, concentrates, edibles, and good vibes. We're more than just a dispensary — We're a laid-back destination built for curious minds. Whether you're a connoisseur or just canna-curious, stop by, stay chill, and get buzzed."

> "At Bored N Buzzed, we believe cannabis should be approachable, enjoyable, and responsibly shared. We look forward to welcoming you in and becoming your go-to cannabis destination."

### Three Brand Pillars (Current)
1. **Friendly Service** — "down-to-earth, genuinely knowledgeable, actually listens"
2. **Best Prices** — "No inflated shelf prices, no confusing tiers — just solid weed at prices that make sense"
3. **Best Selection** — "hand-pick strains... if we wouldn't buy it ourselves, we're not selling it"

### Service Area Claimed
Kirkland · Woodinville · Redmond · Bothell (and beyond)

### Tone Assessment
- Casual, approachable, playful
- Deal-forward — almost everything is framed around discounts
- Some hip-hop/culture adjacency (Jim Jones, MarkTellsYa)
- Inconsistent — ranges from slang ("CATCH US OUTSIDE, HOW BOUT THAT?") to generic SEO copy in blog posts
- "Solid weed at prices that make sense" actively signals mid-market, not premium

---

## Deal Structure (Current)

### Daily Deals
| Day | Deal |
|---|---|
| Monday | 30% off 3+ edibles |
| Tuesday | 30% off 3+ top shelf brands |
| Wednesday | 30% off 3g+ concentrate |
| Thursday | 30% off 3+ prerolls |
| Friday | 30% off 3+ flower |
| Sat/Sun | Spend $100 = 20% · $200 = 25% · $300 = 30% |

### Loyalty Rewards (Points)
- Earn: $1 = 1 point
- 100 pts = 10% off · 250 pts = 20% off · 500 pts = 25% off · 800 pts = 30% off
- First visit: 30% off · Birthday: 30% off · Google review: 25% off
- Referral: referred friend gets 30% off, referrer gets 25% off

### Active Brand Deals (at audit)
30% off: 28 Herbs, Mfused, Soulshine, PICC, Sky High, Kush Mountain
40% off: Fireline, Artizen, Desert Dream

---

## Product Categories
- Flower
- Edibles (gummies, chocolates, drinks, capsules)
- Concentrates (shatter, wax/budder, live resin, rosin, diamonds & sauce)
- Vapes (510-thread, disposable, pods)
- Pre-Rolls (infused/hash via PICC partnership)
- Topicals (mentioned in Cannabis 101, no product page)

### Named Products Found
- Mfused Super Fog (concentrate)
- Soulshine Himalayan Blackberry (flower)
- PICC Ichi-Roll (preroll — patented hash blend tech)
- Sky High Gardens Pineapple Chunk (flower — pesticide-free, hand-trimmed, LED)
- Good Tide Hash Rosin Gummies
- Journeyman Berries (vegan, gluten-free edibles)
- Desert Dream carts (distillate — mango, berry)
- Artizen (indoor, HPS + LED)

---

## Events & Community (Hidden Premium Signals)

> [!tip] These are premium positioning seeds — currently buried and under-leveraged
- **Jim Jones Live** (Oct 1, 2025) — In-store event, limited merch drop (B&B tees/hats), partner brands Sky High Gardens + WYLD Gummies
- **Mirra Afterparty** (Oct 3, 2025) — Bellevue afterparty tie-in
- **MarkTellsYa Partnership** (Jan 2026) — Local Seattle content creator, Seahawks playoff street content
- **Vendor Days** — Regular in-store brand meetups (mentioned in About, no dedicated page or calendar found)

**The Jim Jones event quote — the best copy on the site:**
> "At the end of the day, it wasn't just an event — it was a reminder of why we do what we do. We're here for the people, the culture, and the moments that bring us together. Stay tuned, Kirkland. This is just the beginning."

---

## ⚠️ Bugs & Issues (Fix These)

| Issue | Page | Priority |
|---|---|---|
| Contact page is live with placeholder data ("Urban Jungle Co.," Illinois address, fake numbers) | `/contact/` | 🔴 Critical |
| Default WordPress "Hello World" post never deleted | `/hello-world/` | 🟡 Medium |
| Blank Elementor draft page is publicly accessible | `/elementor-page-1147/` | 🟡 Medium |
| Soulshine page typo: "HIGHTER PURPOSE" | `/soulshine/` | 🟡 Medium |
| Menu embeds showed 0 products at crawl time — verify POSaBit sync is live | All menu pages | 🔴 Verify |
| No social media URLs wired up on contact page (links to "#") | `/contact/` | 🟡 Medium |

---

## Brand Assessment: Where It Stands

### What's Working
- Events program shows real premium/cultural ambition
- Vendor Days is a genuine differentiator with community value
- Education content (terpenes, Cannabis 101) is a premium positioning move
- Rewards program is generous and well-structured
- Service area coverage of the Eastside is real and documented
- Some genuine voice in the Jim Jones recap — shows they can write at a higher level

### What's Not Working
- **Deal-first from the first pixel.** The homepage is a scrolling discount catalog. Premium brands don't lead with discounts.
- **"Solid weed at prices that make sense"** — this line directly undermines any premium claim.
- **Yellow + blue color palette** is generic, low-budget, and indistinguishable from a dollar store.
- **No visual identity** beyond basic colors and a single font.
- **No Eastside story.** Being in Kirkland is mentioned in the About blurb, that's it.
- **Tone is all over the place.** "CATCH US OUTSIDE, HOW BOUT THAT?" vs. formal blog SEO copy vs. casual weed culture slang.
- **No photography direction.** The site has essentially no original photography visible in the crawl.
- **Generic About page.** "Cannabis should be approachable, enjoyable, and responsibly shared" — this could be any dispensary anywhere.

### The Gap
They have the ingredients: location, events muscle, community ties, a curated product line, strong vendor relationships. What's missing is the frame — a premium, Eastside-specific brand identity that makes all of those ingredients feel intentional and aspirational instead of incidental.

---

*[[CLAUDE]] → [[Brand Identity/Brand Identity]] → Phase 1 brand sprint*
