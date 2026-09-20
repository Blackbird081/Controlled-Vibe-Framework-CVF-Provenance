@echo off
setlocal EnableExtensions

set "CVF_ACCOUNT=cvf-g1-party-a"
for %%I in ("%~dp0..") do set "CVF_REPO=%%~fI"

where pwsh.exe >nul 2>nul
if errorlevel 1 (
  echo [PWSH_NOT_FOUND] PowerShell 7 pwsh.exe is not available on PATH.
  exit /b 2
)

net user "%CVF_ACCOUNT%" >nul 2>nul
if errorlevel 1 (
  echo [ACCOUNT_NOT_FOUND] Local account "%CVF_ACCOUNT%" does not exist.
  exit /b 3
)

if /I "%~1"=="--check" (
  echo READY: %COMPUTERNAME%\%CVF_ACCOUNT%
  echo REPO: %CVF_REPO%
  exit /b 0
)

echo Opening the Group 2 spec ceremony as %COMPUTERNAME%\%CVF_ACCOUNT%.
echo Windows will request that account's password securely.
echo After login, type exactly: EXECUTE GROUP 2 SPEC WRITE
runas /profile /user:"%COMPUTERNAME%\%CVF_ACCOUNT%" "pwsh.exe -NoExit -NoProfile -Command $nodeDir='C:\nvm4w\nodejs'; if (Test-Path -LiteralPath $nodeDir) { $env:Path=$nodeDir+';'+$env:Path }; Set-Location -LiteralPath '%CVF_REPO%'; & '.\scripts\acel_g1_party_a_group2_spec_writer.ps1' -ExecuteWrite -ExpectedAccountName 'LAM-RUBY\cvf-g1-party-a' -ExpectedAccountSid 'S-1-5-21-1644666849-912006174-747199667-1006'"
exit /b %ERRORLEVEL%
