# review-reminder.ps1
# Stop hook — fires after every Claude response turn.
# Guards: only after 5pm, only if work was done today (daily note has content),
# only if /review hasn't been run yet today, and at most once per day.
# If all guards pass: outputs a reminder Aaron sees in the UI.

$today     = Get-Date -Format 'yyyy-MM-dd'
$hour      = (Get-Date).Hour
$vaultPath = "C:\Users\aaron.lavespere\Documents\Aaron's Life & Business OS"
$notePath  = Join-Path $vaultPath "BuildSafe IQ\Operations\Daily Notes\$today.md"
$logDir    = Join-Path $vaultPath "_OS\_brain\Agent_Logs"
$stateFile = Join-Path $vaultPath "_OS\_scripts\.review-reminded-$today"

# Guard 1: Only after 5pm
if ($hour -lt 17) { exit 0 }

# Guard 2: Only if daily note exists
if (-not (Test-Path $notePath)) { exit 0 }

# Guard 3: Only if daily note has real content (not just the blank template)
$content = Get-Content $notePath -Raw -ErrorAction SilentlyContinue
if (-not $content -or $content.Length -lt 400) { exit 0 }

# Guard 4: Only if /review hasn't already run today (no Agent_Log for today)
$todayLog = Get-ChildItem $logDir -Filter "$today*.md" -ErrorAction SilentlyContinue
if ($todayLog) { exit 0 }

# Guard 5: Only once per day — check state file
if (Test-Path $stateFile) { exit 0 }

# All guards passed — fire the reminder once
New-Item -Path $stateFile -ItemType File -Force | Out-Null

Write-Output ""
Write-Output "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
Write-Output "END-OF-DAY REMINDER"
Write-Output "/review has not been run today."
Write-Output "Run it to save decisions to memory.md and sync brain files to Drive."
Write-Output "Just type: /review"
Write-Output "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
