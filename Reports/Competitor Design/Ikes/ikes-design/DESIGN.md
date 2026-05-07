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
  src: url("https://ikes.com/fonts/Futura.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Saira";
  src: url("https://ikes.com/fonts/Saira-VariableFont_wdth,wght.ttf") format("truetype");
  font-weight: 100;
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
- **Spacing scale:** 4, 6, 8, 12, 14, 16, 20, 24, 32, 80
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
