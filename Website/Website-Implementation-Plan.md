# Bored and Buzzed Website Redesign — Phase 2 Build

This document outlines the architecture and execution plan to build the new Bored and Buzzed (B&B) headless e-commerce website. We are replicating the speed, stability, and AI-friendly architecture observed in our competitor analysis, but elevating it with our Phase 1 "Eastside Standard" premium design system.

## Goal Description
Build a premium, headless React web application for Bored and Buzzed. The site will be decoupled from the inventory backend. We will integrate the POSaBIT API to dynamically handle products, inventory, and cart operations, while leveraging Vite, React Query, and Tailwind CSS for the frontend UI.

> [!IMPORTANT]
> ## User Review Required
> Please review this architecture plan. We are committing to a headless React/Vite stack with POSaBIT. If the POSaBIT API requires specific credentials or a GraphQL vs. REST approach, we will need to confirm those integration docs before coding.

> [!WARNING]
> ## Open Questions
> 1. Do you already have the **POSaBIT API Keys / Developer Documentation** for the Kirkland store? 
> 2. Are we hosting this on **Vercel** or **Netlify** for fast edge deployments?

---

## Proposed Architecture

### 1. The Tech Stack
- **Framework:** React + Vite (Fast builds, optimal for AI component generation)
- **Styling:** Tailwind CSS (configured exactly to B&B's JSON design tokens: Warm Dark `#0D0D0B`, Aged Gold `#C9A84C`)
- **State Management:** TanStack Query (React Query) for caching POSaBIT data and instant page loads.
- **Inventory & E-commerce:** POSaBIT Headless API.
- **Routing:** React Router v7.

### 2. File & Component Structure
We will initialize the codebase with the following core directories:

#### [NEW] `/src/api/posabit.js`
The core integration layer. All calls to fetch strains, check inventory, and submit orders to POSaBIT will run through this isolated client.

#### [NEW] `/tailwind.config.js`
Customized to enforce our Phase 1 brand tokens. It will restrict colors, fonts (`Clash Display`, `DM Sans`, `JetBrains Mono`), and asymmetric layouts so AI-generated components cannot hallucinate off-brand styles.

#### [NEW] `/src/components/`
- **`/layout`**: Age Gate, TopNav, Footer.
- **`/shop`**: ProductCard, FilterSidebar, CategoryBar.
- **`/ui`**: Reusable premium tokens (Buttons, Badges, Modals).

---

## Execution Phases

### Phase 2.1: Infrastructure & Scaffolding (In a New Repository)
- Initialize new GitHub repository for `bnb-web`.
- Run `npx create-vite-app` (React + SWC).
- Install Tailwind CSS, TanStack Query, and React Router.
- Load Phase 1 design tokens into `tailwind.config.js`.
- Add local webfonts (Clash Display, DM Sans, JetBrains Mono).

### Phase 2.2: POSaBIT Integration Layer
- Build the fetch client for the POSaBIT API.
- Set up React Query hooks (`useProducts`, `useCategories`, `useCart`).
- Create dummy mock data mirroring POSaBIT's schema so we can build the UI immediately without waiting for API keys if they are delayed.

### Phase 2.3: Core UI Development
- **Age Gate:** Full-screen 21+ compliance block.
- **Hero & Navigation:** Premium dark-mode header with sticky navigation.
- **Menu/Shop:** The two-column e-commerce grid (Filters on left, Products on right).
- **Product Cards:** Interactive cards showing Strain type, THC%, and Add to Cart functionality.

### Phase 2.4: Polish & Compliance
- Run the `impeccable` design skill across the digital assets for a deep UI/UX audit.
- Ensure WA State WSLCB compliance disclaimers are present in the footer and Age Gate.

---

## Verification Plan

### Automated Tests
- Build test to ensure Vite compiles successfully (`npm run build`).
- Verify Tailwind purges unused CSS properly.

### Manual Verification
- Deploy to a Vercel staging link.
- Trevor to test the POSaBIT product sync (verify a price change in POSaBIT reflects on the staging site instantly via React Query).
- Verify the mobile responsive layout (filters collapsing into a drawer).



---
*[[CLAUDE]] — master document · [[Website/Website|Website Section]]*