---
name: ikes-design
description: Design system skill for ikes. Activate when building UI components, pages, or any visual elements. Provides exact color tokens, typography scale, spacing grid, component patterns, and craft rules. Read references/DESIGN.md before writing any CSS or JSX. Includes ultra-mode visual journey: read references/ANIMATIONS.md, references/LAYOUT.md, references/COMPONENTS.md, and references/INTERACTIONS.md for full motion and layout details.
---

# ikes Design System

You are building UI for **ikes**. Light-themed, neutral palette, sans-serif typography (Saira), compact density on a 4px grid, expressive motion.

## Visual Reference

**IMPORTANT**: Study ALL screenshots below before writing any UI. Match colors, typography, spacing, layout, and motion exactly as shown.

### Homepage

![ikes Homepage](screenshots/homepage.png)

### Scroll Journey (Cinematic Visual States)

> These screenshots capture the website at different scroll depths. The design changes dramatically as you scroll — each frame shows a different cinematic state. Replicate these exact visual transitions.

#### 0% — Hero / Above the fold

![Scroll 0%](screens/scroll/scroll-000.png)

#### 17% — Mid-page at 17% scroll

![Scroll 17%](screens/scroll/scroll-017.png)

#### 33% — Mid-page at 33% scroll

![Scroll 33%](screens/scroll/scroll-033.png)

#### 50% — Mid-page at 50% scroll

![Scroll 50%](screens/scroll/scroll-050.png)

#### 67% — Mid-page at 67% scroll

![Scroll 67%](screens/scroll/scroll-067.png)

#### 83% — Mid-page at 83% scroll

![Scroll 83%](screens/scroll/scroll-083.png)

#### 100% — Footer / End of page

![Scroll 100%](screens/scroll/scroll-100.png)

> Read `references/DESIGN.md` for full token details. Read `references/ANIMATIONS.md` for motion specs. Read `references/LAYOUT.md` for layout structure. Read `references/COMPONENTS.md` for component patterns.

## Ultra Reference Files

This package includes extended documentation. **Read these files before implementing:**

| File | Contents |
|------|----------|
| `references/DESIGN.md` | Full design system tokens, colors, typography, spacing |
| `references/VISUAL_GUIDE.md` | **START HERE** — Master visual guide with all screenshots embedded |
| `references/ANIMATIONS.md` | CSS keyframes, scroll triggers, motion library stack, video specs |
| `references/LAYOUT.md` | Flex/grid containers, page structure, spacing relationships |
| `references/COMPONENTS.md` | DOM component patterns, HTML structure, class fingerprints |
| `references/INTERACTIONS.md` | Hover/focus states with before/after style diffs |
| `screens/scroll/` | 7 scroll journey screenshots showing cinematic states |

## Design Philosophy

- **Layered depth** — use shadow tokens to create a sense of physical layering. Each elevation level has a specific shadow.
- **Gradient accents** — gradients are used thoughtfully for emphasis, not decoration.
- **Type pairing** — Saira for body/UI text, Futura for headings/display. Never introduce a third typeface.
- **compact density** — 4px base grid. Every dimension is a multiple of 4.
- **neutral palette** — the color temperature runs neutral, matching the sans-serif typography.
- **Expressive motion** — animations are an integral part of the experience. Use spring physics and layout animations.

## Color System

### Core Palette

| Role | Token | Hex | Use |
|------|-------|-----|-----|
| Background | `--background` | `#ffffff` | Page/app background |
| Surface | `--surface` | `#f1f1f1` | Cards, panels, modals |
| Text Primary | `--text-primary` | `#121212` | Headings, body text |
| Text Muted | `--text-muted` | `#bfc7ad` | Captions, placeholders |
| Border | `--border` | `#353b41` | Dividers, card borders |

### Status Colors

| Status | Hex | Use |
|--------|-----|-----|
| Danger | `#f88240` | Errors, destructive actions |

### Extended Palette

- **color-slate:** `#1d222c`
- **tw-ring-color:** `#6b7280`
- **color-canopy:** `#2f4257`
- **color-black:** `#000000` — Deep background layer or shadow color
- `#4a5565`
- **tw-ring-color:** `#5a6b70`
- **toastify-spinner-color:** `#616161`
- **color-primary-500:** `#9fa791`

### CSS Variable Tokens

```css
--toastify-toast-background: #fff;
--color-primary-900: #3d4235;
--color-primary-800: #525947;
--color-primary-700: #6b7360;
--color-primary-600: #858d78;
--color-primary-500: #9fa791;
--color-primary-400: #b3bba7;
--color-primary-300: #bfc7ad;
--color-primary-200: #d0d6c5;
--color-primary-100: #e2e6db;
--color-primary-50: #f3f5f0;
--color-secondary-700: #be521a;
--color-secondary-600: #e0611f;
--color-secondary-500: #f88240;
--color-secondary-400: #fa9b66;
--color-secondary-300: #fbb48c;
--color-secondary-200: #fccdb2;
--color-secondary-50: #fef3ec;
--color-background-900: #0f1423;
--color-background-800: #141414;
```

## Typography

### Font Stack

- **Saira** — Heading 1, Heading 2
- **Futura** — Body, Caption
- **SFMono-Regular** — Code

### Font Sources

```css
@font-face {
  font-family: "Futura";
  src: url("fonts/Futura-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Saira";
  src: url("fonts/Saira-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Saira";
  src: url("fonts/Saira-Regular.ttf") format("truetype");
  font-weight: 400;
}
```

### Type Scale

| Role | Family | Size | Weight |
|------|--------|------|--------|
| Heading 1 | Saira | 128px | 700 |
| Heading 2 | Saira | 1.5rem | 700 |
| Body | Futura | .875rem | 400 |
| Caption | Futura | 1.25rem | 400 |
| Code | SFMono-Regular | 14px | 400 |

### Typography Rules

- Body/UI: **Saira**, Headings: **Futura** — these are the only display fonts
- Max 3-4 font sizes per screen
- Headings: weight 600-700, body: weight 400
- Use color and opacity for text hierarchy, not additional font sizes
- Line height: 1.5 for body, 1.2 for headings

## Spacing & Layout

### Base Grid: 4px

Every dimension (margin, padding, gap, width, height) must be a multiple of **4px**.

### Spacing Scale

`4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 64, 80` px

### Spacing as Meaning

| Spacing | Use |
|---------|-----|
| 4-8px | Tight: related items (icon + label, avatar + name) |
| 12-16px | Medium: between groups within a section |
| 24-32px | Wide: between distinct sections |
| 48px+ | Vast: major page section breaks |

### Border Radius

Scale: `initial, .25rem, .75rem, 1rem, 2rem, 2px, 5%, 6px, 24px, 28px, 100%`
Default: `2px`

### Container

Max-width: `96rem`, centered with auto margins.

### Breakpoints

| Name | Value |
|------|-------|
| sm | 40rem |
| md | 48rem |
| lg | 64rem |
| xl | 80rem |
| 2xl | 96rem |
| xs | 480px |

Mobile-first: design for small screens, layer on responsive overrides.

## Component Patterns

### Card

```css
.card {
  background: #f1f1f1;
  border: 1px solid #353b41;
  border-radius: 2px;
  padding: 16px;
  box-shadow: var(--toastify-toast-shadow);
}
```

```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content goes here.</p>
</div>
```

### Button

```css
/* Primary */
.btn-primary {
  background: #cccccc;
  color: #121212;
  border-radius: 2px;
  padding: 8px 16px;
  font-weight: 500;
  transition: opacity 150ms ease;
}
.btn-primary:hover { opacity: 0.9; }

/* Ghost */
.btn-ghost {
  background: transparent;
  border: 1px solid #353b41;
  color: #121212;
  border-radius: 2px;
  padding: 8px 16px;
}
```

```html
<button class="btn-primary">Get Started</button>
<button class="btn-ghost">Learn More</button>
```

### Input

```css
.input {
  background: #ffffff;
  border: 1px solid #353b41;
  border-radius: 2px;
  padding: 8px 12px;
  color: #121212;
  font-size: 14px;
}
.input:focus { border-color: var(--accent); outline: none; }
```

```html
<input class="input" type="text" placeholder="Search..." />
```

### Badge / Chip

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 8px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
  background: #f1f1f1;
  color: #bfc7ad;
}
```

```html
<span class="badge">New</span>
<span class="badge">Beta</span>
```

### Modal / Dialog

```css
.modal-backdrop { background: rgba(0, 0, 0, 0.6); }
.modal {
  background: #f1f1f1;
  border: 1px solid #353b41;
  border-radius: 100%;
  padding: 24px;
  max-width: 480px;
  width: 90vw;
  box-shadow: 0 10px 15px -3px #0000004d,0 4px 6px -2px #0003;
}
```

```html
<div class="modal-backdrop">
  <div class="modal">
    <h2>Dialog Title</h2>
    <p>Dialog content.</p>
    <button class="btn-primary">Confirm</button>
    <button class="btn-ghost">Cancel</button>
  </div>
</div>
```

### Table

```css
.table { width: 100%; border-collapse: collapse; }
.table th {
  text-align: left;
  padding: 8px 12px;
  font-weight: 500;
  font-size: 12px;
  color: #bfc7ad;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid #353b41;
}
.table td {
  padding: 12px;
  border-bottom: 1px solid #353b41;
}
```

```html
<table class="table">
  <thead><tr><th>Name</th><th>Status</th><th>Date</th></tr></thead>
  <tbody>
    <tr><td>Item One</td><td>Active</td><td>Jan 1</td></tr>
    <tr><td>Item Two</td><td>Pending</td><td>Jan 2</td></tr>
  </tbody>
</table>
```

### Navigation

```css
.nav {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  border-bottom: 1px solid #353b41;
}
.nav-link {
  color: #bfc7ad;
  padding: 8px 12px;
  border-radius: 2px;
  transition: color 150ms;
}
.nav-link:hover { color: #121212; }
```

```html
<nav class="nav">
  <a href="/" class="nav-link active">Home</a>
  <a href="/about" class="nav-link">About</a>
  <a href="/pricing" class="nav-link">Pricing</a>
  <button class="btn-primary" style="margin-left: auto">Get Started</button>
</nav>
```

### Extracted Components

These components were found in the codebase:

**Button** (`html`)

**Input** (`html`)

**Navigation** (`html`)

**Footer** (`html`)

## Page Structure

The following page sections were detected:

- **Navigation** — Top navigation bar (10 items)
- **Hero** — Hero/banner section with headline and CTAs
- **Faq** — FAQ/accordion section
- **Footer** — Page footer with links and info (20 items)

When building pages, follow this section order and structure.

## Animation & Motion

This project uses **expressive motion**. Animations are part of the design language.

### CSS Animations

- `Toastify__trackProgress`
- `Toastify__bounceInRight`
- `Toastify__bounceOutRight`
- `Toastify__bounceInLeft`
- `Toastify__bounceOutLeft`

### Motion Tokens

- **Duration scale:** `.2s`, `.3s`, `.5s`, `.6s`, `.7s`, `1s`, `100ms`, `150ms`, `200ms`, `300ms`
- **Easing functions:** `ease`, `cubic-bezier(.215,.61,.355,1)`, `ease-in`
- **Animated properties:** `transform`

### Motion Guidelines

- **Duration:** Use values from the duration scale above. Short (.2s) for micro-interactions, long (300ms) for page transitions
- **Easing:** Use `ease` as the default easing curve
- **Direction:** Elements enter from bottom/right, exit to top/left
- **Reduced motion:** Always respect `prefers-reduced-motion` — disable animations when set

## Depth & Elevation

### Shadow Tokens

- Subtle: `0 .25rem 1.5rem #0006,0 0 0 1px #ffffff0d`
- Subtle: `0 .5rem 2rem #00000080,0 0 0 1px #ffffff14`
- Raised (cards, buttons): `var(--toastify-toast-shadow)`
- Raised (cards, buttons): `0 0 0 1px var(--color-primary-700),0 2px 4px #0003`
- Raised (cards, buttons): `0 2px 4px #0003`
- Raised (cards, buttons): `0 0 0 2px var(--color-primary-800),0 0 8px var(--color-primary-500)`

### Z-Index Scale

`0, 1, 2, 5, 10, 20, 30, 35, 40, 50, 60, 70, 90, 100, 101, 9998, 9999`

Use these exact values — never invent z-index values.

## Anti-Patterns (Never Do)

- **No blur effects** — no backdrop-blur, no filter: blur()
- **No zebra striping** — tables and lists use borders for separation
- **No invented colors** — every hex value must come from the palette above
- **No arbitrary spacing** — every dimension is a multiple of 4px
- **No extra fonts** — only Saira and Futura and SFMono-Regular are allowed
- **No arbitrary border-radius** — use the scale: .25rem, .75rem, 1rem, 2rem, 2px, 6px, 24px, 28px
- **No opacity for disabled states** — use muted colors instead

## Workflow

1. **Read** `references/DESIGN.md` before writing any UI code
2. **Pick colors** from the Color System section — never invent new ones
3. **Set typography** — Saira, Futura, SFMono-Regular only, using the type scale
4. **Build layout** on the 4px grid — check every margin, padding, gap
5. **Match components** to patterns above before creating new ones
6. **Apply elevation** — use shadow tokens
7. **Validate** — every value traces back to a design token. No magic numbers.

## Brand Spec

- **Favicon:** `/favicon.ico`
- **Site URL:** `https://ikes.com/`
- **Brand typeface:** Saira

## Quick Reference

```
Background:     #ffffff
Surface:        #f1f1f1
Text:           #121212 / #bfc7ad
Accent:         (not extracted)
Border:         #353b41
Font:           Saira
Spacing:        4px grid
Radius:         2px
Components:     9 detected
```

## When to Trigger

Activate this skill when:
- Creating new components, pages, or visual elements for ikes
- Writing CSS, Tailwind classes, styled-components, or inline styles
- Building page layouts, templates, or responsive designs
- Reviewing UI code for design consistency
- The user mentions "ikes" design, style, UI, or theme
- Generating mockups, wireframes, or visual prototypes

---

# Full Reference Files

> Every output file is embedded below. Claude has full design system context from /skills alone.

## Design System Tokens (DESIGN.md)

# ikes DESIGN.md

> Auto-generated design system — reverse-engineered via static analysis by skillui.
> Frameworks: None detected
> Colors: 20 · Fonts: 3 · Components: 9
> Icon library: not detected · State: not detected
> Primary theme: light · Dark mode toggle: no · Motion: expressive

## Visual Reference

**Match this design exactly** — study colors, fonts, spacing, and component shapes before writing any UI code.

![ikes Homepage](../screenshots/homepage.png)

---

## 1. Visual Theme & Atmosphere

This is a **light-themed** interface with a neutral, approachable feel. The light background emphasizes content clarity. Typography pairs **Futura** for display/headings with **Saira** for body text, creating clear visual hierarchy through type contrast. Spacing follows a **4px base grid** (compact density), with scale: 4, 6, 8, 12, 14, 16, 20, 24px. Motion is expressive — spring physics, layout animations, and staggered reveals are part of the visual language.

---

## 2. Color Palette & Roles

| Token | Hex | Role | Use |
|---|---|---|---|
| toastify-color-light | `#ffffff` | background | Page background, darkest surface |
| color-frost | `#f1f1f1` | surface | Card and panel backgrounds |
| toastify-color-dark | `#121212` | text-primary | Headings and body text |
| color-sage | `#bfc7ad` | text-muted | Captions, placeholders, secondary info |
| border | `#353b41` | border | Dividers, card borders, outlines |
| color-salmon | `#f88240` | danger | Error states, destructive actions |
| color-slate | `#1d222c` | unknown | Palette color |
| tw-ring-color | `#6b7280` | unknown | Palette color |
| color-canopy | `#2f4257` | unknown | Palette color |
| color-black | `#000000` | unknown | Palette color |
| unknown | `#4a5565` | unknown | Palette color |
| tw-ring-color | `#5a6b70` | unknown | Palette color |
| toastify-spinner-color | `#616161` | unknown | Palette color |
| color-primary-500 | `#9fa791` | unknown | Palette color |
| toastify-color-error | `#e74d3c` | unknown | Palette color |
| color-primary-200 | `#d0d6c5` | unknown | Palette color |
| unknown | `#768a8b` | unknown | Palette color |
| unknown | `#2a2a2a` | unknown | Palette color |
| unknown | `#d1d5db` | unknown | Palette color |
| toastify-text-color-light | `#757575` | unknown | Palette color |

### CSS Variable Tokens

```css
--toastify-toast-background: #fff;
--tw-border-style: solid;
--color-primary-900: #3d4235;
--color-primary-800: #525947;
--color-primary-700: #6b7360;
--color-primary-600: #858d78;
--color-primary-500: #9fa791;
--color-primary-400: #b3bba7;
--color-primary-300: #bfc7ad;
--color-primary-200: #d0d6c5;
--color-primary-100: #e2e6db;
--color-primary-50: #f3f5f0;
--color-secondary-700: #be521a;
--color-secondary-600: #e0611f;
--color-secondary-500: #f88240;
--color-secondary-400: #fa9b66;
--color-secondary-300: #fbb48c;
--color-secondary-200: #fccdb2;
--color-secondary-50: #fef3ec;
--color-background-900: #0f1423;
```


---

## 3. Typography Rules

**Font Stack:**
- **Saira** — Heading 1, Heading 2
- **Futura** — Body, Caption
- **SFMono-Regular** — Code

**Font Sources:**

```css
@font-face {
  font-family: "Futura";
  src: url("fonts/Futura-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Saira";
  src: url("fonts/Saira-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Saira";
  src: url("fonts/Saira-Regular.ttf") format("truetype");
  font-weight: 400;
}
```

| Role | Font | Size | Weight |
|---|---|---|---|
| Heading 1 | Saira | 128px | 700 |
| Heading 2 | Saira | 1.5rem | 700 |
| Body | Futura | .875rem | 400 |
| Caption | Futura | 1.25rem | 400 |
| Code | SFMono-Regular | 14px | 400 |

**Typographic Rules:**
- Limit to 3 font families max per screen
- Use **Saira** for body/UI text, **Futura** for display/headings
- Maintain consistent hierarchy: no more than 3-4 font sizes per screen
- Headings use bold (600-700), body uses regular (400)
- Line height: 1.5 for body text, 1.2 for headings
- Use color and opacity for secondary hierarchy, not additional font sizes


---

## 4. Component Stylings

### Layout (1)

**Footer** — `html`

### Navigation (1)

**Navigation** — `html`

### Data Display (2)

**Badge** — `html`

**List** — `html`

### Data Input (2)

**Button** — `html`
- Animation: 

**Input** — `html`
- State: :focus, :placeholder

### Overlay (1)

**Modal** — `html`

### Media (2)

**Image** — `html`

**Map/Canvas** — `html`



---

## 5. Layout Principles

- **Base spacing unit:** 4px
- **Spacing scale:** 4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 64, 80
- **Border radius:** initial, .25rem, .75rem, 1rem, 2rem, 2px, 5%, 6px, 24px, 28px, 100%
- **Max content width:** 96rem

**Spacing as Meaning:**
| Spacing | Use |
|---|---|
| 4-8px | Tight: related items within a group |
| 12-16px | Medium: between groups |
| 24-32px | Wide: between sections |
| 48px+ | Vast: major section breaks |


---

## 6. Depth & Elevation

### Flat — subtle depth hints

- `0 .25rem 1.5rem #0006,0 0 0 1px #ffffff0d`
- `0 .5rem 2rem #00000080,0 0 0 1px #ffffff14`

### Raised — cards, buttons, interactive elements

- `var(--toastify-toast-shadow)`
- `0 0 0 1px var(--color-primary-700),0 2px 4px #0003`
- `0 2px 4px #0003`

### Floating — dropdowns, popovers, modals

- `0 10px 15px -3px #0000004d,0 4px 6px -2px #0003`
- `0 10px 15px -3px color-mix(in srgb,var(--color-black) 30%,transparent),0 4px 6px -2px color-mix(in srgb,var(--color-black) 20%,transparent)`

### Overlay — full-screen overlays, top-level dialogs

- `rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px`
- `rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 25px 50px -12px`

### Z-Index Scale

`0, 1, 2, 5, 10, 20, 30, 35, 40, 50, 60, 70, 90, 100, 101, 9998, 9999`



---

## 7. Animation & Motion

This project uses **expressive motion**. Animations are an integral part of the experience.

### CSS Animations

- `@keyframes Toastify__trackProgress`
- `@keyframes Toastify__bounceInRight`
- `@keyframes Toastify__bounceOutRight`
- `@keyframes Toastify__bounceInLeft`
- `@keyframes Toastify__bounceOutLeft`
- `@keyframes Toastify__bounceInUp`
- `@keyframes Toastify__bounceOutUp`
- `@keyframes Toastify__bounceInDown`

### Animated Components

- **Button**: 

### Motion Guidelines

- Duration: 150-300ms for micro-interactions, 300-500ms for page transitions
- Easing: `ease-out` for enters, `ease-in` for exits
- Always respect `prefers-reduced-motion`


---

## 8. Do's and Don'ts

### Do's

- Use `#ffffff` as the primary page background
- Pair **Saira** (body) with **Futura** (display) — these are the only allowed fonts
- Follow the **4px** spacing grid for all margins, padding, and gaps
- Use the defined shadow tokens for elevation — see Section 6
- Use border-radius from the scale: initial, .25rem, .75rem, 1rem, 2rem
- Reuse existing components from Section 4 before creating new ones

### Don'ts

- Don't introduce colors outside this palette — extend the design tokens first
- Don't introduce additional font families beyond Saira and Futura and SFMono-Regular
- Don't use arbitrary spacing values — stick to multiples of 4px
- Don't create custom box-shadow values outside the system tokens
- Don't use arbitrary border-radius values — pick from the defined scale
- Don't duplicate component patterns — check Section 4 first
- Don't use backdrop-blur or blur effects

### Anti-Patterns (detected from codebase)

- No blur or backdrop-blur effects
- No zebra striping on tables/lists


---

## 9. Responsive Behavior

| Name | Value | Source |
|---|---|---|
| sm | 40rem | css |
| md | 48rem | css |
| lg | 64rem | css |
| xl | 80rem | css |
| 2xl | 96rem | css |
| xs | 480px | css |

**Approach:** Use `@media (min-width: ...)` queries matching the breakpoints above.


---

## 10. Agent Prompt Guide

Use these as starting points when building new UI:

### Build a Card

```
Background: #f1f1f1
Border: 1px solid #353b41
Radius: 2px
Padding: 16px
Font: Saira
Use shadow tokens from Section 6.
```

### Build a Button

```
Primary: bg var(--accent), text white
Ghost: bg transparent, border #353b41
Padding: 8px 16px
Radius: 2px
Hover: opacity 0.9 or lighter shade
Focus: ring with var(--accent)
```

### Build a Page Layout

```
Background: #ffffff
Max-width: 96rem, centered
Grid: 4px base
Responsive: mobile-first, breakpoints from Section 9
```

### Build a Stats Card

```
Surface: #f1f1f1
Label: #bfc7ad (muted, 12px, uppercase)
Value: #121212 (primary, 24-32px, bold)
Status: use success/warning/danger from Section 2
```

### Build a Form

```
Input bg: #ffffff
Input border: 1px solid #353b41
Focus: border-color var(--accent)
Label: #bfc7ad 12px
Spacing: 16px between fields
Radius: 2px
```

### General Component

```
1. Read DESIGN.md Sections 2-6 for tokens
2. Colors: only from palette
3. Font: Saira, type scale from Section 3
4. Spacing: 4px grid
5. Components: match patterns from Section 4
6. Elevation: shadow tokens
```

## Visual Guide — Screenshots (VISUAL_GUIDE.md)

# ikes — Visual Guide

> Master visual reference. Study every screenshot carefully before implementing any UI.
> Match colors, layout, typography, spacing, and motion states exactly.

## Scroll Journey

The page has cinematic scroll animations. Each screenshot below shows the exact visual state at that scroll depth.
**Replicate these transitions precisely** — the design changes dramatically as you scroll.

### Hero — Above the fold

*Scroll position: 0px of 900px total*

![Hero — Above the fold](../screens/scroll/scroll-000.png)

### 17% scroll depth

*Scroll position: 0px of 900px total*

![17% scroll depth](../screens/scroll/scroll-017.png)

### 33% scroll depth

*Scroll position: 0px of 900px total*

![33% scroll depth](../screens/scroll/scroll-033.png)

### 50% scroll depth

*Scroll position: 0px of 900px total*

![50% scroll depth](../screens/scroll/scroll-050.png)

### 67% scroll depth

*Scroll position: 0px of 900px total*

![67% scroll depth](../screens/scroll/scroll-067.png)

### 83% scroll depth

*Scroll position: 0px of 900px total*

![83% scroll depth](../screens/scroll/scroll-083.png)

### Footer — End of page

*Scroll position: 0px of 900px total*

![Footer — End of page](../screens/scroll/scroll-100.png)

## Full Page Screenshots

### Central District - Seattle's Premier Cannabis Dispensary

*URL: `https://ikes.com/`*

![Central District - Seattle's Premier Cannabis Dispensary](../screens/pages/home.png)

## Animations & Motion (ANIMATIONS.md)

# Animation Reference

> Cinematic motion design extracted from live DOM. Follow these specs exactly to recreate the experience.

## Motion Technology Stack

Pure CSS animations — no external animation libraries detected.

## Scroll Journey

The page is **900px** tall. Each frame below shows what the user sees at that scroll depth.

> **Use these screenshots to understand WHAT animates, WHEN it animates, and HOW it moves.**

### 0% — Top / Hero
Scroll position: 0px

![Scroll 0%](../screens/scroll/scroll-000.png)

### 17% — Opening Section
Scroll position: 0px

![Scroll 17%](../screens/scroll/scroll-017.png)

### 33% — First Feature Section
Scroll position: 0px

![Scroll 33%](../screens/scroll/scroll-033.png)

### 50% — Mid-Page
Scroll position: 0px

![Scroll 50%](../screens/scroll/scroll-050.png)

### 67% — Lower Content
Scroll position: 0px

![Scroll 67%](../screens/scroll/scroll-067.png)

### 83% — Near Footer
Scroll position: 0px

![Scroll 83%](../screens/scroll/scroll-083.png)

### 100% — Bottom / Footer
Scroll position: 0px

![Scroll 100%](../screens/scroll/scroll-100.png)

## CSS Keyframes (33 extracted)

### `@keyframes fa-spin`

Duration: `var(--fa-animation-duration,2s)` · Easing: `var(--fa-animation-timing,linear)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-spin`, `.fa-pulse, .fa-spin-pulse`

```css
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```

> Transform/motion animation

### `@keyframes fa-beat`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,ease-in-out)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-beat`

```css
@keyframes fa-beat {
  0%, 90% {
    transform: scale(1);
  }
  45% {
    transform: scale(var(--fa-beat-scale,1.25));
  }
}
```

> Transform/motion animation

### `@keyframes fa-bounce`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,cubic-bezier(.28,.84,.42,1))` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-bounce`

```css
@keyframes fa-bounce {
  0% {
    transform: scale(1) translateY(0px);
  }
  10% {
    transform: scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9))translateY(0);
  }
  30% {
    transform: scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1))translateY(var(--fa-bounce-height,-.5em));
  }
  50% {
    transform: scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95))translateY(0);
  }
  57% {
    transform: scale(1,1)translateY(var(--fa-bounce-rebound,-.125em));
  }
  64% {
    transform: scale(1) translateY(0px);
  }
  100% {
    transform: scale(1) translateY(0px);
  }
}
```

> Transform/motion animation

### `@keyframes fa-fade`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-fade`

```css
@keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity,.4);
  }
}
```

> Opacity fade

### `@keyframes fa-beat-fade`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-beat-fade`

```css
@keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity,.4);
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(var(--fa-beat-fade-scale,1.125));
  }
}
```

> Fade + motion enter animation

### `@keyframes fa-flip`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,ease-in-out)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-flip`

```css
@keyframes fa-flip {
  50% {
    transform: rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));
  }
}
```

> Transform/motion animation

### `@keyframes fa-shake`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,linear)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-shake`

```css
@keyframes fa-shake {
  0% {
    transform: rotate(-15deg);
  }
  4% {
    transform: rotate(15deg);
  }
  8%, 24% {
    transform: rotate(-18deg);
  }
  12%, 28% {
    transform: rotate(18deg);
  }
  16% {
    transform: rotate(-22deg);
  }
  20% {
    transform: rotate(22deg);
  }
  32% {
    transform: rotate(-12deg);
  }
  36% {
    transform: rotate(12deg);
  }
  40%, 100% {
    transform: rotate(0deg);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__trackProgress`

Duration: `auto` · Easing: `linear` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.Toastify__progress-bar--animated`

```css
@keyframes Toastify__trackProgress {
  0% {
    transform: scaleX(1);
  }
  100% {
    transform: scaleX(0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__bounceInRight`

Used by: `.Toastify__bounce-enter--top-right, .Toastify__bounce-enter--bottom-right`

```css
@keyframes Toastify__bounceInRight {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(3000px, 0px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(-25px, 0px, 0px);
  }
  75% {
    transform: translate3d(10px, 0px, 0px);
  }
  90% {
    transform: translate3d(-5px, 0px, 0px);
  }
  100% {
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutRight`

Used by: `.Toastify__bounce-exit--top-right, .Toastify__bounce-exit--bottom-right`

```css
@keyframes Toastify__bounceOutRight {
  20% {
    opacity: 1;
    transform: translate3d(-20px,var(--y),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(2000px,var(--y),0);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceInLeft`

Used by: `.Toastify__bounce-enter--top-left, .Toastify__bounce-enter--bottom-left`

```css
@keyframes Toastify__bounceInLeft {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(-3000px, 0px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(25px, 0px, 0px);
  }
  75% {
    transform: translate3d(-10px, 0px, 0px);
  }
  90% {
    transform: translate3d(5px, 0px, 0px);
  }
  100% {
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutLeft`

Used by: `.Toastify__bounce-exit--top-left, .Toastify__bounce-exit--bottom-left`

```css
@keyframes Toastify__bounceOutLeft {
  20% {
    opacity: 1;
    transform: translate3d(20px,var(--y),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(-2000px,var(--y),0);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceInUp`

Used by: `.Toastify__bounce-enter--bottom-center`

```css
@keyframes Toastify__bounceInUp {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0px, 3000px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(0px, -20px, 0px);
  }
  75% {
    transform: translate3d(0px, 10px, 0px);
  }
  90% {
    transform: translate3d(0px, -5px, 0px);
  }
  100% {
    transform: translateZ(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutUp`

Used by: `.Toastify__bounce-exit--top-center`

```css
@keyframes Toastify__bounceOutUp {
  20% {
    transform: translate3d(0,calc(var(--y) - 10px),0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0,calc(var(--y) + 20px),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(0px, -2000px, 0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceInDown`

Used by: `.Toastify__bounce-enter--top-center`

```css
@keyframes Toastify__bounceInDown {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0px, -3000px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(0px, 25px, 0px);
  }
  75% {
    transform: translate3d(0px, -10px, 0px);
  }
  90% {
    transform: translate3d(0px, 5px, 0px);
  }
  100% {
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutDown`

Used by: `.Toastify__bounce-exit--bottom-center`

```css
@keyframes Toastify__bounceOutDown {
  20% {
    transform: translate3d(0,calc(var(--y) - 10px),0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0,calc(var(--y) + 20px),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(0px, 2000px, 0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__zoomIn`

Used by: `.Toastify__zoom-enter`

```css
@keyframes Toastify__zoomIn {
  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__zoomOut`

Used by: `.Toastify__zoom-exit`

```css
@keyframes Toastify__zoomOut {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: translate3d(0,var(--y),0) scale3d(.3,.3,.3);
  }
  100% {
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__flipIn`

Used by: `.Toastify__flip-enter`

```css
@keyframes Toastify__flipIn {
  0% {
    transform: perspective(400px) rotateX(90deg);
    animation-timing-function: ease-in;
    opacity: 0;
  }
  40% {
    transform: perspective(400px) rotateX(-20deg);
    animation-timing-function: ease-in;
  }
  60% {
    transform: perspective(400px) rotateX(10deg);
    opacity: 1;
  }
  80% {
    transform: perspective(400px) rotateX(-5deg);
  }
  100% {
    transform: perspective(400px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__flipOut`

Used by: `.Toastify__flip-exit`

```css
@keyframes Toastify__flipOut {
  0% {
    transform: translate3d(0,var(--y),0) perspective(400px);
  }
  30% {
    transform: translate3d(0,var(--y),0) perspective(400px) rotateX(-20deg);
    opacity: 1;
  }
  100% {
    transform: translate3d(0,var(--y),0) perspective(400px) rotateX(90deg);
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__slideInRight`

Used by: `.Toastify__slide-enter--top-right, .Toastify__slide-enter--bottom-right`

```css
@keyframes Toastify__slideInRight {
  0% {
    transform: translate3d(110%, 0px, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideInLeft`

Used by: `.Toastify__slide-enter--top-left, .Toastify__slide-enter--bottom-left`

```css
@keyframes Toastify__slideInLeft {
  0% {
    transform: translate3d(-110%, 0px, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideInUp`

Used by: `.Toastify__slide-enter--bottom-center`

```css
@keyframes Toastify__slideInUp {
  0% {
    transform: translate3d(0px, 110%, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideInDown`

Used by: `.Toastify__slide-enter--top-center`

```css
@keyframes Toastify__slideInDown {
  0% {
    transform: translate3d(0px, -110%, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutRight`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--top-right, .Toastify__slide-exit--bottom-right`

```css
@keyframes Toastify__slideOutRight {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(110%,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutLeft`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--top-left, .Toastify__slide-exit--bottom-left`

```css
@keyframes Toastify__slideOutLeft {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(-110%,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutDown`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--bottom-center`

```css
@keyframes Toastify__slideOutDown {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(0px, 500px, 0px);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutUp`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--top-center`

```css
@keyframes Toastify__slideOutUp {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(0px, -500px, 0px);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__spin`

Duration: `0.65s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.Toastify__spinner`

```css
@keyframes Toastify__spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```

> Transform/motion animation

### `@keyframes toastSlideInRight`

Duration: `0.3s` · Easing: `ease-out` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.Toastify__slide-enter--top-right, .Toastify__slide-enter--bottom-right`

```css
@keyframes toastSlideInRight {
  0% {
    opacity: 0;
    transform: translate(100%);
  }
  100% {
    opacity: 1;
    transform: translate(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes toastSlideOutRight`

Duration: `0.2s` · Easing: `ease-in` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.Toastify__slide-exit--top-right, .Toastify__slide-exit--bottom-right`

```css
@keyframes toastSlideOutRight {
  0% {
    opacity: 1;
    transform: translate(0px);
  }
  100% {
    opacity: 0;
    transform: translate(100%);
  }
}
```

> Fade + motion enter animation

### `@keyframes spin`

```css
@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}
```

> Transform/motion animation

### `@keyframes pulse`

```css
@keyframes pulse {
  50% {
    opacity: 0.5;
  }
}
```

> Opacity fade

## Motion Tokens (CSS Variables)

### Duration Tokens

```css
--default-transition-duration: .15s;
```

### Easing Tokens

```css
--ease-in-out: cubic-bezier(.4,0,.2,1);
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--ease-out: cubic-bezier(0,0,.2,1);
```

## Global Transition Declarations

These `transition` values were extracted from CSS rules across the site:

```css
transition: transform 0.3s;
transition: opacity 0.1s;
transition: 0.3s;
transition: transform 0.2s;
transition: top 0.2s;
transition: 0.2s;
transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
transition: 0.15s;
```

## How to Recreate This Motion Design

### Step 2 — Scroll-Reveal Pattern

Elements that animate into view follow this pattern:

```css
/* Initial hidden state */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity .15s cubic-bezier(.4,0,.2,1),
              transform .15s cubic-bezier(.4,0,.2,1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Step 3 — Key Motion Principles

- **Duration scale:** `.15s` · `0.3s` · `0.1s` · `0.2s` — use these values, never invent new durations
- **Always add** `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`

### Step 4 — Scroll Journey Reference

Match what happens at each scroll position:

- **0%** (`0px`) → `screens/scroll/scroll-000.png`
- **17%** (`0px`) → `screens/scroll/scroll-017.png`
- **33%** (`0px`) → `screens/scroll/scroll-033.png`
- **50%** (`0px`) → `screens/scroll/scroll-050.png`
- **67%** (`0px`) → `screens/scroll/scroll-067.png`
- **83%** (`0px`) → `screens/scroll/scroll-083.png`
- **100%** (`0px`) → `screens/scroll/scroll-100.png`

## Layout & Grid (LAYOUT.md)

# Layout Reference

> Auto-extracted from live DOM. Use this to understand how the site is structured spatially.

## Spacing System

**Base grid:** 4px

**Scale:** `4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 64, 80` px

| Spacing | Semantic Use |
|---------|-------------|
| 4px | Tight — within a component |
| 8px | Medium — between sibling items |
| 16px | Wide — between sections |
| 32px | Vast — major section breaks |

## Flex Layouts

| Element | Direction | Justify | Align | Gap | Children |
|---------|-----------|---------|-------|-----|----------|
| `div.fixed.inset-0` | row | center | center | — | 3 |
| `div.flex.justify-center` | row | center | — | — | 1 |
| `div.flex.flex-col` | column | — | — | 16px | 2 |

## Layout Rules

- Primary layout system: **Flexbox**
- Every spacing value must be a multiple of **4px**
- Never use arbitrary margin/padding values outside the spacing scale

## Component Patterns (COMPONENTS.md)

# Component Reference

> Repeated DOM patterns detected by structural analysis. Each component appeared 3+ times.

No repeated components detected (Playwright required).

## Interactions & States (INTERACTIONS.md)

# Interaction Reference

> Micro-interactions extracted from live DOM. Recreate these exactly for authentic feel.

## Coverage

| Component Type | Count | States Captured |
|----------------|-------|----------------|
| Button | 2 | default, hover, focus |

## Transition System

These transition declarations were extracted from interactive elements:

```css
transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), translate 0.2s cubic-bezier(0.4, 0, 0.2, 1), scale 0.2s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.2s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

Apply these to all interactive elements. Never invent new durations or easings.

## Button Interactions

### Button 1 — `YES, I AM 21+`

**States:**

- Default: `../screens/states/button-1-default.png`
- Hover: `../screens/states/button-1-hover.png`
- Focus: `../screens/states/button-1-focus.png`

**On hover:**

```css
/* background-color: rgb(248, 130, 64) → */ background-color: rgb(179, 187, 167);
```

**On focus:**

```css
/* outline: rgb(26, 26, 26) none 3px → */ outline: rgb(179, 187, 167) solid 2px;
/* outline-color: rgb(26, 26, 26) → */ outline-color: rgb(179, 187, 167);
```

**Transition:** `transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), translate 0.2s cubic-bezier(0.4, 0, 0.2, 1), scale 0.2s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.2s cubic-bezier(0.4, 0, 0.2, 1)`

### Button 2 — `NO, I AM UNDER 21`

**States:**

- Default: `../screens/states/button-2-default.png`
- Hover: `../screens/states/button-2-hover.png`
- Focus: `../screens/states/button-2-focus.png`

**On hover:**

```css
/* color: oklab(0.958141 0.0000436902 0.0000191331 / 0.5) → */ color: rgb(241, 241, 241);
/* border-color: oklab(0.958141 0.0000436902 0.0000191331 / 0.5) → */ border-color: rgb(241, 241, 241);
/* outline: oklab(0.958141 0.0000436902 0.0000191331 / 0.5) none 3px → */ outline: rgb(241, 241, 241) none 3px;
/* outline-color: oklab(0.958141 0.0000436902 0.0000191331 / 0.5) → */ outline-color: rgb(241, 241, 241);
```

**On focus:**

```css
/* outline: oklab(0.958141 0.0000436902 0.0000191331 / 0.5) none 3px → */ outline: rgb(179, 187, 167) solid 2px;
/* outline-color: oklab(0.958141 0.0000436902 0.0000191331 / 0.5) → */ outline-color: rgb(179, 187, 167);
```

**Transition:** `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1)`

## Interaction Rules

- Hover effects include **color transitions** — use the extracted values, not approximations
- Focus states use **outline** (not box-shadow) — always match the extracted focus ring
- Transition durations in use: `0.2s`, `0.15s`
- Always respect `prefers-reduced-motion` — set all transitions to `0s` when enabled

## Design Tokens — JSON Files

### tokens/colors.json
```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "core": {
    "surface": {
      "value": "#f1f1f1",
      "role": "surface",
      "name": "color-frost"
    },
    "background": {
      "value": "#ffffff",
      "role": "background",
      "name": "toastify-color-light"
    },
    "text-primary": {
      "value": "#121212",
      "role": "text-primary",
      "name": "toastify-color-dark"
    },
    "text-muted": {
      "value": "#bfc7ad",
      "role": "text-muted",
      "name": "color-sage"
    },
    "border": {
      "value": "#353b41",
      "role": "border"
    }
  },
  "status": {
    "danger": {
      "value": "#f88240",
      "role": "danger",
      "name": "color-salmon"
    }
  },
  "extended": {
    "color-slate": {
      "value": "#1d222c",
      "role": "unknown",
      "name": "color-slate"
    },
    "tw-ring-color": {
      "value": "#5a6b70",
      "role": "unknown",
      "name": "tw-ring-color"
    },
    "color-canopy": {
      "value": "#2f4257",
      "role": "unknown",
      "name": "color-canopy"
    },
    "color-black": {
      "value": "#000000",
      "role": "unknown",
      "name": "color-black"
    },
    "color-4a5565": {
      "value": "#4a5565",
      "role": "unknown"
    },
    "toastify-spinner-color": {
      "value": "#616161",
      "role": "unknown",
      "name": "toastify-spinner-color"
    },
    "color-primary-500": {
      "value": "#9fa791",
      "role": "unknown",
      "name": "color-primary-500"
    },
    "toastify-color-error": {
      "value": "#e74d3c",
      "role": "unknown",
      "name": "toastify-color-error"
    },
    "color-primary-200": {
      "value": "#d0d6c5",
      "role": "unknown",
      "name": "color-primary-200"
    },
    "color-768a8b": {
      "value": "#768a8b",
      "role": "unknown"
    },
    "color-2a2a2a": {
      "value": "#2a2a2a",
      "role": "unknown"
    },
    "color-d1d5db": {
      "value": "#d1d5db",
      "role": "unknown"
    },
    "toastify-text-color-light": {
      "value": "#757575",
      "role": "unknown",
      "name": "toastify-text-color-light"
    }
  },
  "meta": {
    "theme": "light",
    "extracted": "2026-05-07"
  }
}
```

### tokens/spacing.json
```json
{
  "base": {
    "value": "4px",
    "description": "Grid unit — all spacing must be multiples of this"
  },
  "unit": "px",
  "scale": {
    "xs": {
      "value": "4px",
      "px": 4
    },
    "sm": {
      "value": "6px",
      "px": 6
    },
    "md": {
      "value": "8px",
      "px": 8
    },
    "lg": {
      "value": "12px",
      "px": 12
    },
    "xl": {
      "value": "14px",
      "px": 14
    },
    "2xl": {
      "value": "16px",
      "px": 16
    },
    "3xl": {
      "value": "20px",
      "px": 20
    },
    "4xl": {
      "value": "24px",
      "px": 24
    },
    "5xl": {
      "value": "32px",
      "px": 32
    },
    "6xl": {
      "value": "40px",
      "px": 40
    }
  },
  "multipliers": {
    "1x": {
      "value": "4px",
      "raw": 4
    },
    "2x": {
      "value": "8px",
      "raw": 8
    },
    "3x": {
      "value": "12px",
      "raw": 12
    },
    "4x": {
      "value": "16px",
      "raw": 16
    },
    "5x": {
      "value": "20px",
      "raw": 20
    },
    "6x": {
      "value": "24px",
      "raw": 24
    },
    "7x": {
      "value": "28px",
      "raw": 28
    },
    "8x": {
      "value": "32px",
      "raw": 32
    },
    "9x": {
      "value": "36px",
      "raw": 36
    },
    "10x": {
      "value": "40px",
      "raw": 40
    },
    "11x": {
      "value": "44px",
      "raw": 44
    },
    "12x": {
      "value": "48px",
      "raw": 48
    },
    "13x": {
      "value": "52px",
      "raw": 52
    },
    "14x": {
      "value": "56px",
      "raw": 56
    },
    "15x": {
      "value": "60px",
      "raw": 60
    },
    "16x": {
      "value": "64px",
      "raw": 64
    }
  },
  "meta": {
    "totalValues": 12,
    "min": 4,
    "max": 80
  }
}
```

### tokens/typography.json
```json
{
  "families": [
    "Saira",
    "Futura",
    "SFMono-Regular"
  ],
  "scale": {
    "heading-1": {
      "fontFamily": "Saira",
      "fontSize": "128px",
      "fontWeight": "700",
      "lineHeight": null,
      "source": "css"
    },
    "heading-2": {
      "fontFamily": "Saira",
      "fontSize": "1.5rem",
      "fontWeight": "700",
      "lineHeight": null,
      "source": "css"
    },
    "body": {
      "fontFamily": "Futura",
      "fontSize": ".875rem",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "css"
    },
    "caption": {
      "fontFamily": "Futura",
      "fontSize": "1.25rem",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "css"
    },
    "code": {
      "fontFamily": "SFMono-Regular",
      "fontSize": "14px",
      "fontWeight": "400",
      "lineHeight": null,
      "source": "css"
    }
  },
  "fontFaces": [
    {
      "family": "Futura",
      "src": "https://ikes.com/fonts/Futura.ttf",
      "format": "truetype",
      "weight": "400"
    },
    {
      "family": "Saira",
      "src": "https://ikes.com/fonts/Saira-VariableFont_wdth,wght.ttf",
      "format": "truetype",
      "weight": "100"
    }
  ],
  "rules": {
    "maxSizesPerScreen": 4,
    "headingWeightRange": "600-700",
    "bodyWeight": 400,
    "lineHeightBody": 1.5,
    "lineHeightHeading": 1.2
  }
}
```

## Bundled Fonts (fonts/)

The following font files are bundled in the `fonts/` directory:

- `fonts/Futura-Regular.ttf`
- `fonts/Saira-Black.ttf`
- `fonts/Saira-Bold.ttf`
- `fonts/Saira-ExtraBold.ttf`
- `fonts/Saira-ExtraLight.ttf`
- `fonts/Saira-Light.ttf`
- `fonts/Saira-Medium.ttf`
- `fonts/Saira-Regular.ttf`
- `fonts/Saira-SemiBold.ttf`
- `fonts/Saira-Thin.ttf`

Use these local font files in `@font-face` declarations instead of fetching from Google Fonts.

## Screenshots Inventory (screens/)

> Study all screenshots carefully before implementing any UI. Match every visual detail exactly.

### Scroll Journey (screens/scroll/)

*Cinematic scroll states — page visual at each scroll depth*

![scroll-000.png](screens/scroll/scroll-000.png)

![scroll-017.png](screens/scroll/scroll-017.png)

![scroll-033.png](screens/scroll/scroll-033.png)

![scroll-050.png](screens/scroll/scroll-050.png)

![scroll-067.png](screens/scroll/scroll-067.png)

![scroll-083.png](screens/scroll/scroll-083.png)

![scroll-100.png](screens/scroll/scroll-100.png)

### Full Page Screenshots (screens/pages/)

*Full-page screenshots of each crawled URL*

![home.png](screens/pages/home.png)

### Interaction States (screens/states/)

*Hover, focus, and active state captures*

![button-1-default.png](screens/states/button-1-default.png)

![button-1-focus.png](screens/states/button-1-focus.png)

![button-1-hover.png](screens/states/button-1-hover.png)

![button-2-default.png](screens/states/button-2-default.png)

![button-2-focus.png](screens/states/button-2-focus.png)

![button-2-hover.png](screens/states/button-2-hover.png)

### Screenshot Index (screens/INDEX.md)

# Screenshot Index

## Scroll Journey

> Shows the cinematic state at each point of the page

| Scroll | Y Position | File |
|--------|-----------|------|
| 0% | 0px | `screens/scroll/scroll-000.png` |
| 17% | 0px | `screens/scroll/scroll-017.png` |
| 33% | 0px | `screens/scroll/scroll-033.png` |
| 50% | 0px | `screens/scroll/scroll-050.png` |
| 67% | 0px | `screens/scroll/scroll-067.png` |
| 83% | 0px | `screens/scroll/scroll-083.png` |
| 100% | 0px | `screens/scroll/scroll-100.png` |

## Pages

| Page | URL | File |
|------|-----|------|
| Central District - Seattle's Premier Cannabis Dispensary | `https://ikes.com/` | `screens/pages/home.png` |

## Homepage Screenshots (screenshots/)

![homepage.png](screenshots/homepage.png)

