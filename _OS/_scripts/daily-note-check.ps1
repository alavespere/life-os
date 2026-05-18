# daily-note-check.ps1
# UserPromptSubmit hook — fires on every message Aaron sends.
# If today's Daily Note does not exist, outputs an instruction that Claude sees
# and acts on before processing Aaron's message.
# Silent (no output) if daily note already exists.

$today     = Get-Date -Format 'yyyy-MM-dd'
$vaultPath = "C:\Users\aaron.lavespere\Documents\Aaron's Life & Business OS"
$notePath  = Join-Path $vaultPath "BuildSafe IQ\Operations\Daily Notes\$today.md"

if (-not (Test-Path $notePath)) {
    Write-Output "HOOK — DAILY NOTE MISSING: No Daily Note exists for $today. Before doing anything else, run /today: create today's Daily Note from the template at _OS/Templates/Daily Note Template.md, read the last 3 Agent_Logs for carry-forward context, check open tasks in _OS/_tasks/, and output the structured daily brief. Do this first, then address Aaron's request."
}
# If note exists: no output — Claude proceeds normally.
