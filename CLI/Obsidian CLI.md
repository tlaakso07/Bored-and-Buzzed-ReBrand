---
title: Obsidian CLI
tags: [cli, obsidian, vault]
---

# Obsidian CLI

> Interact with the live Obsidian vault from the terminal. Create notes, search content, append tasks, manage properties — all without opening the app manually.

## Status
🟢 Operational
Binary: `/opt/homebrew/bin/obsidian` → `Obsidian.app/Contents/MacOS/obsidian-cli`
Requires: Obsidian app open + CLI enabled (Settings → General → Advanced)

## Vault Targeting

Always target this vault explicitly:

```bash
obsidian vault="Buzzed Rebrand" <command>
```

## Key Commands

```bash
# Search vault
obsidian vault="Buzzed Rebrand" search query="brand identity" limit=10

# Read a note
obsidian vault="Buzzed Rebrand" read file="CLAUDE"

# Create a note
obsidian vault="Buzzed Rebrand" create name="Note Name" content="# Heading\nContent" silent

# Append to a note
obsidian vault="Buzzed Rebrand" append file="Note Name" content="- New line"

# Set a property
obsidian vault="Buzzed Rebrand" property:set name="status" value="complete" file="Note Name"

# List tasks
obsidian vault="Buzzed Rebrand" tasks daily todo

# Get backlinks
obsidian vault="Buzzed Rebrand" backlinks file="CLAUDE"

# List all tags
obsidian vault="Buzzed Rebrand" tags sort=count counts
```

## Use Cases for This Engagement
- Create new brand sprint notes and research docs from Claude sessions
- Search vault for related content before creating duplicates
- Append to running logs (content calendar, event recaps, review trackers)
- Set `status` and `phase` properties on notes programmatically
- Pull task lists for daily/weekly work reviews

---
*[[CLAUDE]] — master document*
