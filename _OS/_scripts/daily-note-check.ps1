$today = Get-Date -Format 'yyyy-MM-dd'
$vault = "C:\Users\aaron.lavespere\Documents\Aaron's Life & Business OS"
$note  = Join-Path $vault "BuildSafe IQ\Operations\Daily Notes\$today.md"

if (-not (Test-Path $note)) {
    Write-Output "HOOK: No Daily Note for $today. Run /today first: create the note from the template, check Agent_Logs and tasks, output the daily brief. Do this before addressing anything else."
}
