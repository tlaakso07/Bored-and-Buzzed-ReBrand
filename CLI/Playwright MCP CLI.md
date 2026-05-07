---
title: Playwright MCP CLI
tags: [cli, playwright, browser-automation]
---

# Playwright MCP CLI

> Browser automation binary — powers the Playwright MCP server that Claude uses for live browser control, screenshots, and platform interaction.

## Status
🟢 Installed
Binary: `/opt/homebrew/bin/playwright-mcp`

## How It's Used
Playwright MCP runs as a server that Claude calls via the MCP protocol. The CLI binary starts that server. You don't invoke it directly — Claude uses it through the MCP tools.

```bash
# Start the MCP server manually (Claude handles this automatically)
playwright-mcp
```

## MCP Tools Available to Claude
| Tool | What It Does |
|---|---|
| Navigate | Go to any URL in a real browser |
| Screenshot | Capture full page or element screenshots |
| Click / Fill | Interact with buttons, forms, inputs |
| Evaluate | Run JavaScript in the browser context |

## Use Cases for This Engagement
- Screenshot Bored and Buzzed platform listings (Weedmaps, Leafly, Google, Yelp) for the Phase 1 audit
- Capture competitor listing layouts side-by-side for benchmarking
- Verify listing updates went live after edits
- Handle login-gated pages that Firecrawl can't reach

## Related
- [[MCP/Playwright]] — MCP server documentation
- [[MCP/Firecrawl]] — Use Firecrawl for non-interactive scraping

---
*[[CLAUDE]] — master document*
