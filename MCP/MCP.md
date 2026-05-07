---
title: MCP Servers
tags: [mcp, infrastructure]
---

# MCP Servers

> Model Context Protocol servers connected to this engagement. Configured in `~/.claude/.mcp.json`. These are the tools Claude can reach beyond its own context — web, browser, maps, and media generation.

---

## Status Board

| Server | Status | Primary Use |
|---|---|---|
| [[MCP/Firecrawl\|Firecrawl]] | 🟢 Connected | Web scraping, site crawls, competitor research |
| [[MCP/Playwright\|Playwright]] | 🟢 Installed | Browser automation, platform audits, screenshots |
| [[MCP/Kie AI\|Kie AI]] | 🟡 Configured | AI image & video generation for social content |
| [[MCP/Google Maps\|Google Maps]] | 🔴 Needs API key | Competitor mapping, local business data, Eastside market |

---

## How MCPs Map to the Plan

### Phase 1 — Foundation
- **Firecrawl** → Crawl Bored and Buzzed website + competitor listings for the platform audit
- **Playwright** → Automate Weedmaps, Leafly, Google, Yelp audits — screenshot every listing
- **Google Maps** → Map every dispensary competitor on the Eastside *(blocked until API key)*

### Phase 2 — Build
- **Firecrawl** → Monitor competitor listings for changes; extract structured product data
- **Playwright** → Automate listing update verification across platforms
- **Kie AI** → Generate social content imagery, product visuals, promotional graphics

### Phase 3 — Grow
- **Kie AI** → Event promotional materials, influencer-ready creative assets
- **Google Maps** → Event venue research, foot traffic and demographic data for pop-up planning
- **Firecrawl** → Influencer profile research, press coverage monitoring

---

## Config Location
All servers configured in `~/.claude/.mcp.json`.

---
*[[CLAUDE]] — master document*
