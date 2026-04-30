# Google Drive Bridge — Setup Guide
_One-time 5-minute setup. Syncs _brain/ to Google Drive so Claude.ai can read your context on mobile._

---

## What This Does

Creates a Windows symbolic link from a Google Drive folder to your vault's `_OS/_brain/` folder. Once done:

- `soul.md`, `user.md`, `memory.md` are live-synced to Google Drive automatically
- Claude.ai (browser or mobile) can read them via the Google Drive MCP connector
- Every Claude.ai session can start with full context — no re-explaining who you are

---

## Prerequisites

- Google Drive for Desktop installed and signed in (`drive.google.com/drive/downloads`)
- PowerShell (run as Administrator)

---

## Step 1 — Find Your Google Drive Path

Open File Explorer and find where Google Drive syncs locally. Usually one of:
- `C:\Users\aaron.lavespere\Google Drive\`
- `C:\Users\aaron.lavespere\My Drive\`
- `G:\My Drive\`

Confirm the path before running the command below.

---

## Step 2 — Run the Symlink Command

Open PowerShell as Administrator. Replace the Google Drive path if yours differs:

```powershell
New-Item -ItemType SymbolicLink `
  -Path "C:\Users\aaron.lavespere\Google Drive\BuildSafe Brain" `
  -Target "C:\Users\aaron.lavespere\Documents\Aaron's Life & Business OS\_OS\_brain"
```

This creates a folder called "BuildSafe Brain" in your Google Drive that mirrors `_OS/_brain/` in real time.

---

## Step 3 — Verify the Sync

1. Open Google Drive for Desktop — confirm "BuildSafe Brain" folder appears and is syncing
2. Open `drive.google.com` in browser — confirm you can see `soul.md`, `user.md`, `memory.md`

---

## Step 4 — Test in Claude.ai

Open Claude.ai in browser. Start a new conversation:

> "Read my brain files from Google Drive folder 'BuildSafe Brain' before we begin."

Claude should read all three files and respond with full context about BuildSafe IQ, the team, and current priorities.

---

## Using Claude.ai With Full Context (Mobile Workflow)

Once the bridge is active, Claude.ai becomes your on-the-go interface:

**Mid-day from mobile:**
> "Read my brain files from Drive. I just heard back from Burns & Wilcox on the [client] submission. Pull up my Gmail thread with them and tell me the status and recommended response."

**Quick research:**
> "Read my brain files from Drive. I need a 3-paragraph summary of what excess & surplus lines carriers look for in a high-rise COI — written in my voice for a LinkedIn post."

---

## MCP Connectors to Activate in Claude.ai

Go to `claude.ai → Settings → Integrations` and connect:
- **Google Drive** — required for brain file access
- **Gmail** — enables broker follow-up tracking
- **Google Calendar** — enables calendar-aware `/today` briefs

---

## Notes

- The symlink is one-directional in terms of editing: always edit brain files in Obsidian, not in Drive
- Google Drive syncs the files automatically — no manual uploads needed after setup
- If you rename or move `_OS/_brain/`, the symlink breaks — update it using the same command with the new path
