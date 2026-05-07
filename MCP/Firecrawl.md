---
title: Firecrawl MCP
tags: [mcp, firecrawl, research]
---

# Firecrawl MCP

> Web scraping and crawling tool. Use for competitor research, platform audits, content extraction, and any deep crawl of external sites.

## Status
🟢 Operational

## Config Location
`~/.claude/.mcp.json`

## Configuration
```json
{
  "firecrawl": {
    "command": "npx",
    "args": ["-y", "firecrawl-mcp"],
    "env": {
      "FIRECRAWL_API_KEY": "fc-04ddfaee35a14d38a7b7b020288f4e07"
    }
  }
}
```

## Available Tools
| Tool | Purpose |
|---|---|
| `firecrawl_scrape` | Scrape a single page to clean markdown |
| `firecrawl_crawl` | Crawl an entire site recursively |
| `firecrawl_search` | Search the web and return results |
| `firecrawl_extract` | Extract structured data from pages |
| `firecrawl_map` | Map all URLs on a site |
| `firecrawl_parse` | Parse raw HTML to markdown |
| `firecrawl_browser_*` | Browser automation tools |

## Use Cases for This Engagement

### Phase 1 — Audit & Research
- Crawl Bored and Buzzed website — full content audit before redesign
- Scrape Weedmaps and Leafly competitor listings for benchmarking
- Research WSLCB compliance rules and restrictions
- Competitor brand, SEO, and copy analysis

### Phase 2 — Build & Monitor
- Extract structured product data from POS/menu pages
- Monitor competitor listing changes (price, copy, photos)
- Scrape Google/Yelp reviews for sentiment analysis

### Phase 3 — Grow
- Influencer profile research across platforms
- Press and media mention monitoring
- Event venue and competitor event research

## Notes
- Prefer `defuddle` for simple single-page reads (faster, fewer tokens)
- Use Firecrawl for full site crawls, structured extraction, or JS-heavy pages
- Results should be saved to `[[Reports/Reports]]`
- Pairs with Playwright for sites that require login or heavy JavaScript

---
*[[CLAUDE]] — master document*
