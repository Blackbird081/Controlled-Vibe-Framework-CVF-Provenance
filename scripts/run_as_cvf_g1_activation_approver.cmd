@echo off
setlocal EnableExtensions

set "CVF_ACCOUNT=cvf-g1-activation-approver"
for %%I in ("%~dp0..") do set "CVF_REPO=%%~fI"

where pwsh.exe >nul 2>nul
if errorlevel 1 (
  echo [PWSH_NOT_FOUND] PowerShell 7 pwsh.exe is not available on PATH.
  exit /b 2
)

net user "%CVF_ACCOUNT%" >nul 2>nul
if errorlevel 1 (
  echo [ACCOUNT_NOT_FOUND] Local account "%CVF_ACCOUNT%" does not exist yet.
  echo Create the approved standard local account before using this launcher.
  exit /b 3
)

if /I "%~1"=="--check" (
  echo READY: %COMPUTERNAME%\%CVF_ACCOUNT%
  echo REPO: %CVF_REPO%
  exit /b 0
)

echo Opening PowerShell 7 as %COMPUTERNAME%\%CVF_ACCOUNT%.
echo Windows will request that account's password securely.
runas /profile /user:"%COMPUTERNAME%\%CVF_ACCOUNT%" "pwsh.exe -NoExit -NoProfile -Command $nodeDir='C:\nvm4w\nodejs'; if (Test-Path -LiteralPath $nodeDir) { $env:Path=$nodeDir+';'+$env:Path }; Set-Location -LiteralPath '%CVF_REPO%'"
exit /b %ERRORLEVEL%
