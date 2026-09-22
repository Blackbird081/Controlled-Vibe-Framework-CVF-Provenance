@echo off
setlocal

if /I "%~1"=="--check" (
  pwsh.exe -NoProfile -File "%~dp0provision_cvf_g1_party_c.ps1" -Check
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="--elevated" goto elevated

echo Requesting Administrator approval to provision the dedicated CVF G1 Party C account.
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "Start-Process -FilePath '%~f0' -Verb RunAs -ArgumentList '--elevated' -Wait"
exit /b %ERRORLEVEL%

:elevated
pwsh.exe -NoProfile -File "%~dp0provision_cvf_g1_party_c.ps1" -ExecuteProvision
exit /b %ERRORLEVEL%
