---
title: Node & npx
tags: [cli, node, npx, runtime]
---

# Node.js & npx

> JavaScript runtime and package runner — the engine that powers every MCP server and npx-based tool in this engagement.

## Status
🟢 Operational
Node version: v25.9.0
Binary: `/opt/homebrew/bin/node` · `/opt/homebrew/bin/npx`

## What It Powers

| Tool | How Node/npx Is Used |
|---|---|
| Firecrawl MCP | `npx -y firecrawl-mcp` |
| Kie AI MCP | `npx -y @felores/kie-ai-mcp-server` |
| Google Maps MCP | `npx -y @modelcontextprotocol/server-google-maps` |
| Ruflo | `npx ruflo@latest` |

## Common Commands

```bash
# Check versions
node --version
npx --version

# Run any npx tool without installing
npx <package-name>

# Update a global package
npm install -g <package>@latest

# Check what's globally installed
npm list -g --depth=0
```

## Notes
- All MCP servers in `~/.claude/.mcp.json` rely on Node/npx being available
- If an MCP server fails to connect, check Node is on PATH first
- Keep Node updated via Homebrew: `brew upgrade node`

---
*[[CLAUDE]] — master document*
