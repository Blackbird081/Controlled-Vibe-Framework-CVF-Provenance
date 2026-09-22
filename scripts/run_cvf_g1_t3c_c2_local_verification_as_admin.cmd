@echo off
setlocal

if /I "%~1"=="--elevated" goto elevated

echo Requesting Administrator approval for the one-time T3C-C2 Local-read ACL repair.
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "Start-Process -FilePath '%~f0' -Verb RunAs -ArgumentList '--elevated' -Wait"
exit /b %ERRORLEVEL%

:elevated
pwsh.exe -NoProfile -File "%~dp0acel_g1_t3c_c2_local_read_acl_repair.ps1"
set "CVF_EXIT=%ERRORLEVEL%"
echo.
if "%CVF_EXIT%"=="0" (
  echo Verification and ACL repair completed. Return to the reviewer session.
) else (
  echo Verification or ACL repair failed with exit code %CVF_EXIT%.
)
pause
exit /b %CVF_EXIT%
