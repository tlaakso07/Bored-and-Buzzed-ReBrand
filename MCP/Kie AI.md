---
title: Kie AI MCP
tags: [mcp, kie-ai, image-generation, video-generation, creative]
---

# Kie AI MCP

> AI-powered image and video generation. Use for social content visuals, promotional graphics, product imagery, and event materials — directly from Claude, no separate tool needed.

## Status
🟡 Configured — API key set, verify before first use

## Config
```json
{
  "kie-ai": {
    "command": "npx",
    "args": ["-y", "@felores/kie-ai-mcp-server"],
    "env": {
      "KIE_AI_API_KEY": "3cd158999f101d65265295561cb585dd"
    }
  }
}
```

> [!warning] Verify Before First Use
> Kie AI was configured in Session 01 but has not been health-checked since. Run a test generation before relying on it for a deadline.

## Use Cases for This Engagement

### Phase 2 — Social Content
- Generate product lifestyle imagery for Instagram/TikTok
- Create visual backgrounds and graphic elements for feed posts
- Build promotional graphic templates for weekly deals

### Phase 2 — In-Store Assets
- Generate design concepts for signage and display graphics
- Create digital display loop visuals
- Produce Canva-ready background images

### Phase 3 — Events & Growth
- Event promotional posters and flyers
- Vendor day announcement graphics
- Ambassador and influencer-ready creative assets

## Compliance Note
> [!warning] All AI-generated imagery must pass the compliance checklist before use.
> No imagery that could appeal to minors. No health claims in visuals. Age-gate required on all digital placements. See [[Compliance/Compliance]].

## Workflow
1. Generate concept via Claude + Kie AI MCP
2. Review for brand alignment (once brand identity is defined — see [[Brand Identity/Brand Identity]])
3. Run compliance check
4. Export/save to `In-Store Assets/` or `Social Media/` folder as applicable

---
*[[CLAUDE]] — master document*
