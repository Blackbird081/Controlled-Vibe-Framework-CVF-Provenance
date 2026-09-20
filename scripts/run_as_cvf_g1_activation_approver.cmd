@echo off
setlocal EnableExtensions

set "CVF_ACCOUNT=cvf-g1-approver"
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

pwsh.exe -NoProfile -Command "$u=Get-LocalUser -Name $env:CVF_ACCOUNT -ErrorAction Stop; if (-not $u.Enabled) { Write-Error '[ACCOUNT_DISABLED] Approved account is disabled.'; exit 4 }; if (-not $u.PasswordRequired) { Write-Error '[PASSWORD_NOT_REQUIRED] Run elevated: net user cvf-g1-approver /passwordreq:yes'; exit 5 }; $isAdmin=@(Get-LocalGroupMember -SID 'S-1-5-32-544' -ErrorAction Stop | Where-Object { $_.SID -eq $u.SID }).Count -gt 0; if ($isAdmin) { Write-Error '[ACCOUNT_IS_ADMIN] Remove the approver from the local Administrators group.'; exit 6 }"
if errorlevel 1 exit /b %ERRORLEVEL%

if /I "%~1"=="--check" (
  echo READY: %COMPUTERNAME%\%CVF_ACCOUNT%
  echo REPO: %CVF_REPO%
  exit /b 0
)

echo Opening PowerShell 7 as %COMPUTERNAME%\%CVF_ACCOUNT%.
echo Windows will request that account's password securely.
runas /profile /user:"%COMPUTERNAME%\%CVF_ACCOUNT%" "pwsh.exe -NoExit -NoProfile -Command $nodeDir='C:\nvm4w\nodejs'; if (Test-Path -LiteralPath $nodeDir) { $env:Path=$nodeDir+';'+$env:Path }; Set-Location -LiteralPath '%CVF_REPO%'"
exit /b %ERRORLEVEL%
