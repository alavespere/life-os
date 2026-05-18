$today  = Get-Date -Format 'yyyy-MM-dd'
$hour   = (Get-Date).Hour
$vault  = "C:\Users\aaron.lavespere\Documents\Aaron's Life & Business OS"
$note   = Join-Path $vault "BuildSafe IQ\Operations\Daily Notes\$today.md"
$logDir = Join-Path $vault "_OS\_brain\Agent_Logs"
$state  = Join-Path $vault "_OS\_scripts\.reminded-$today"

if ($hour -lt 17)              { exit 0 }
if (-not (Test-Path $note))    { exit 0 }

$text = Get-Content $note -Raw -ErrorAction SilentlyContinue
if (-not $text -or $text.Length -lt 400) { exit 0 }

$log = Get-ChildItem $logDir -Filter "$today*.md" -ErrorAction SilentlyContinue
if ($log) { exit 0 }

if (Test-Path $state) { exit 0 }

New-Item -Path $state -ItemType File -Force | Out-Null

Write-Output ""
Write-Output "END-OF-DAY: /review has not been run. Type /review to save decisions to memory.md and sync brain files to Drive."
