param(
    [Parameter(Mandatory = $true)]
    [string]$WorkspaceRoot,

    [Parameter(Mandatory = $true)]
    [string]$ProfileName,

    [string]$StagingRoot = "",

    [switch]$UpdateProjectManifests,

    [switch]$AllowPendingCoreBackup,

    [switch]$KeepStaging
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$exportScript = Join-Path $PSScriptRoot "export_cvf_workspace_overlay.ps1"
$reconcileScript = Join-Path $PSScriptRoot "update_cvf_workspace_public_core.ps1"

function Write-Info([string]$Message) { Write-Host "[INFO] $Message" -ForegroundColor Cyan }
function Write-Ok([string]$Message) { Write-Host "[OK]   $Message" -ForegroundColor Green }

if (-not (Test-Path -LiteralPath $exportScript -PathType Leaf)) {
    throw "Export script not found: $exportScript"
}

if (-not (Test-Path -LiteralPath $reconcileScript -PathType Leaf)) {
    throw "Workspace reconcile script not found: $reconcileScript"
}

$workspaceResolved = [System.IO.Path]::GetFullPath($WorkspaceRoot)
if (-not (Test-Path -LiteralPath $workspaceResolved -PathType Container)) {
    throw "Workspace root not found: $workspaceResolved"
}

$stagingResolved = if ([string]::IsNullOrWhiteSpace($StagingRoot)) {
    Join-Path $workspaceResolved "_cvf-overlay-staging"
} else {
    [System.IO.Path]::GetFullPath($StagingRoot)
}

$profileStagingPath = Join-Path $stagingResolved $ProfileName

Write-Info "Workspace root: $workspaceResolved"
Write-Info "Profile:        $ProfileName"
Write-Info "Staging path:   $profileStagingPath"

& powershell -ExecutionPolicy Bypass -File $exportScript `
    -ProfileName $ProfileName `
    -OutputPath $profileStagingPath `
    -Force
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$reconcileArgs = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $reconcileScript,
    "-WorkspaceRoot", $workspaceResolved,
    "-OverlaySourcePath", $profileStagingPath
)

if ($UpdateProjectManifests) {
    $reconcileArgs += "-UpdateProjectManifests"
}

if ($AllowPendingCoreBackup) {
    $reconcileArgs += "-AllowPendingCoreBackup"
}

& powershell @reconcileArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if (-not $KeepStaging) {
    Remove-Item -LiteralPath $profileStagingPath -Recurse -Force
    if ((Test-Path -LiteralPath $stagingResolved -PathType Container) -and
        -not (Get-ChildItem -LiteralPath $stagingResolved -Force | Select-Object -First 1)) {
        Remove-Item -LiteralPath $stagingResolved -Force
    }
}

Write-Host ""
Write-Ok "Workspace overlay applied."
Write-Host "Suggested verification:" -ForegroundColor Yellow
Write-Host "  powershell -ExecutionPolicy Bypass -File `"$workspaceResolved\.Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1`" -ProjectPath `"$workspaceResolved\vehicle-management-system`""
