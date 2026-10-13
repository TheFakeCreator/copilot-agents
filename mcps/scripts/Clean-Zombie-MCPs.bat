@echo off
echo ==================================================
echo Antigravity IDE: Cleaning up orphaned MCP processes
echo ==================================================
echo.
echo Scanning for hung Python processes belonging to youtube-screenshot and youtube-transcript...
powershell -Command "Get-WmiObject Win32_Process | Where-Object { $_.CommandLine -match 'youtube-screenshot' -or $_.CommandLine -match 'youtube-transcript' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host 'Killed zombie process ID: ' $_.ProcessId }"
echo.
echo Cleanup complete! Ports have been freed.
echo You can now safely launch the Antigravity IDE.
echo.
pause
