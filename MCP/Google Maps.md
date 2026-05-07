---
title: Google Maps MCP
tags: [mcp, google-maps]
---

# Google Maps MCP

> Local business research, competitor location mapping, and place data for Kirkland/Eastside area.

## Status
🔴 Not Operational — API key required

## How to Get a Google Maps API Key

1. Go to **Google Cloud Console** → `console.cloud.google.com`
2. Create a new project (or select an existing one)
3. Go to **APIs & Services → Library**
4. Enable the **Maps JavaScript API** and **Places API**
5. Go to **APIs & Services → Credentials**
6. Click **Create Credentials → API Key**
7. Copy the key and add it to `~/.claude/.mcp.json` (see below)

> **Tip:** Under "Restrict key," limit it to the APIs you enabled to keep it secure.

## Config Location
`~/.claude/.mcp.json`

## Configuration (once key is obtained)
```json
{
  "google-maps": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-google-maps"],
    "env": {
      "GOOGLE_MAPS_API_KEY": "YOUR_KEY_HERE"
    }
  }
}
```

## Use Cases for This Engagement
- Map cannabis dispensary competitors on the Eastside
- Pull Google Business data for Bored and Buzzed
- Research Kirkland area foot traffic and demographics
- Find local event venues for pop-up planning

---
*[[CLAUDE]] — master document*
