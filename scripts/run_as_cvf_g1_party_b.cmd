@echo off
setlocal EnableExtensions

set "CVF_ACCOUNT=cvf-g1-party-b"
set "CVF_EXPECTED_SID=S-1-5-21-1644666849-912006174-747199667-1009"
set "CVF_PYTHON_DIR=C:\Users\DELL\AppData\Local\Programs\Python\Python311"
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

pwsh.exe -NoProfile -Command "$u=Get-LocalUser -Name $env:CVF_ACCOUNT -ErrorAction Stop; if (-not $u.Enabled) { Write-Error '[ACCOUNT_DISABLED] Party B is disabled.'; exit 4 }; if (-not $u.PasswordRequired) { Write-Error '[PASSWORD_NOT_REQUIRED] Party B must require a password.'; exit 5 }; if ($u.SID.Value -ne $env:CVF_EXPECTED_SID) { Write-Error ('[SID_MISMATCH] Actual SID is '+$u.SID.Value); exit 6 }; $isAdmin=@(Get-LocalGroupMember -SID 'S-1-5-32-544' -ErrorAction Stop | Where-Object { $_.SID -eq $u.SID }).Count -gt 0; if ($isAdmin) { Write-Error '[ACCOUNT_IS_ADMIN] Party B must remain a standard user.'; exit 7 }"
if errorlevel 1 exit /b %ERRORLEVEL%

if not exist "%CVF_PYTHON_DIR%\python.exe" (
  echo [PYTHON_NOT_FOUND] Required Python runtime is unavailable at "%CVF_PYTHON_DIR%\python.exe".
  exit /b 8
)

icacls "%CVF_PYTHON_DIR%\python.exe" 2>nul | findstr /I /C:"%COMPUTERNAME%\%CVF_ACCOUNT%" >nul
if errorlevel 1 (
  echo [PYTHON_ACCESS_NOT_PROVISIONED] Party B lacks Read and Execute access to the pinned Python runtime.
  exit /b 9
)

if not exist "%CVF_REPO%\governance\sources\verifier_key_registry\REGISTRY.json" (
  echo [GROUP1_REGISTRY_MISSING] The source registry is unavailable.
  exit /b 10
)

if exist "%CVF_REPO%\governance\sources\registry_observation_log\LOG.jsonl" (
  echo [FIRST_OBSERVATION_ALREADY_EXISTS] T3C-C2 authorizes genesis creation only.
  echo Stop and return to Local review; do not append through this launcher.
  exit /b 11
)

if /I "%~1"=="--check" (
  echo READY: %COMPUTERNAME%\%CVF_ACCOUNT%
  echo SID: %CVF_EXPECTED_SID%
  echo PYTHON: %CVF_PYTHON_DIR%\python.exe ^(Party B Read and Execute ACL present^)
  echo REPO: %CVF_REPO%
  echo TARGET: governance\sources\registry_observation_log\LOG.jsonl ^(absent as required^)
  exit /b 0
)

echo Opening the Group 3 first-observation ceremony as %COMPUTERNAME%\%CVF_ACCOUNT%.
echo Windows will request that account's password securely.
echo After login, type exactly: EXECUTE GROUP 3 OBSERVATION WRITE
runas /profile /user:"%COMPUTERNAME%\%CVF_ACCOUNT%" "pwsh.exe -NoExit -NoProfile -Command $nodeDir='C:\nvm4w\nodejs'; $pythonDir='%CVF_PYTHON_DIR%'; $env:Path=$pythonDir+';'+$env:Path; if (Test-Path -LiteralPath $nodeDir) { $env:Path=$nodeDir+';'+$env:Path }; Set-Location -LiteralPath '%CVF_REPO%'; & '.\scripts\acel_g1_party_b_group3_observation_writer.ps1' -ExecuteWrite -ExpectedAccountName 'LAM-RUBY\cvf-g1-party-b' -ExpectedAccountSid 'S-1-5-21-1644666849-912006174-747199667-1009'"
exit /b %ERRORLEVEL%
