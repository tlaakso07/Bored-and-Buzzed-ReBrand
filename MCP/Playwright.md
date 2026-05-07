---
title: Playwright MCP
tags: [mcp, playwright, browser-automation]
---

# Playwright MCP

> Browser automation — control a real browser to interact with web pages, take screenshots, fill forms, and navigate JS-heavy sites that Firecrawl or defuddle can't handle.

## Status
🟢 Installed — binary at `/opt/homebrew/bin/playwright-mcp`

## Config
```json
{
  "playwright": {
    "command": "playwright-mcp"
  }
}
```

## What It Can Do
- Navigate to any URL in a real browser
- Take screenshots of full pages or specific elements
- Fill forms and click buttons (login flows, search, filters)
- Scrape pages that require JavaScript rendering
- Automate repetitive tasks across multiple platforms

## Use Cases for This Engagement

### Phase 1 — Audits
- Screenshot every Bored and Buzzed listing: Weedmaps, Leafly, Google Business, Yelp
- Document current state of all platforms before any changes
- Capture competitor listing layouts for comparison

### Phase 2 — Verification
- Confirm listing updates went live correctly after edits
- Monitor review counts and star ratings across platforms
- Verify social profile bios, links, and pinned posts are current

### Phase 3 — Monitoring
- Automate weekly competitor checks — flag price or copy changes
- Document event promotion across competitor social pages

## When to Use vs. Firecrawl
| Use Playwright | Use Firecrawl |
|---|---|
| Login-gated pages | Public pages, no auth needed |
| Screenshots needed | Text/data extraction needed |
| Interactive flows | Bulk crawling a whole site |
| JS-heavy SPAs | Standard HTML content |

---
*[[CLAUDE]] — master document*
