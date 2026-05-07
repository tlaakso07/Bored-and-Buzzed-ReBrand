---
title: GitHub CLI
tags: [cli, github, git, version-control]
---

# GitHub CLI (gh)

> GitHub from the terminal — manage repos, PRs, issues, and version control for vault assets, brand docs, and templates.

## Status
🟢 Operational
Version: 2.89.0
Binary: `/opt/homebrew/bin/gh`

## Key Commands

```bash
# Auth status
gh auth status

# Create a repo
gh repo create buzzed-rebrand --private

# Clone a repo
gh repo clone <repo>

# Create a PR
gh pr create --title "Brand identity assets" --body "Phase 1 deliverables"

# View open PRs
gh pr list

# Create an issue
gh issue create --title "Platform audit" --body "Audit all 4 platforms"

# View repo status
gh repo view
```

## Use Cases for This Engagement
- Version control for brand assets, templates, and creative files
- Track deliverables as GitHub issues tied to each phase
- PR workflow for reviewing copy and creative before it ships to client
- Backup vault docs to a private GitHub repo

> [!note] No repo has been created yet for this engagement. Set up when version control is needed for deliverables.

---
*[[CLAUDE]] — master document*
