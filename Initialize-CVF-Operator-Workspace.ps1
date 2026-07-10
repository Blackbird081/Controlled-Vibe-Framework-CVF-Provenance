<#
.SYNOPSIS
    Interactive fresh-clone entrypoint for creating or refreshing a CVF Workspace.

.DESCRIPTION
    Run this file from a trusted CVF provenance clone. With no arguments it
    shows profile options, asks for the workspace path, confirms the plan, and
    creates or refreshes the workspace. Agents may use the non-interactive
    parameters after the operator has selected a path and profile.
#>

param(
    [string]$WorkspaceRoot = "",

    [ValidateSet("", "public-free", "paid-user-safe", "operator-local")]
    [string]$ProfileName = "",

    [switch]$NonInteractive,

    [switch]$PlanOnly,

    [switch]$SkipEnforcementGate
)

$ErrorActionPreference = "Stop"
$publicRemote = "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git"
$provenanceRemote = "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git"
$provenanceRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$interactive = -not $NonInteractive

function Write-Step([string]$Message) {
    Write-Host "[STEP] $Message" -ForegroundColor Cyan
}

function Write-Ok([string]$Message) {
    Write-Host "[OK]   $Message" -ForegroundColor Green
}

function Invoke-CheckedPowerShell {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ScriptPath,

        [string[]]$Arguments = @()
    )

    & powershell -NoProfile -ExecutionPolicy Bypass -File $ScriptPath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code $LASTEXITCODE`: $ScriptPath"
    }
}

function Select-WorkspaceProfile {
    Write-Host ""
    Write-Host "CVF Workspace Setup" -ForegroundColor Cyan
    Write-Host "===================" -ForegroundColor Cyan
    Write-Host "1. operator-local   Recommended for the private operator machine"
    Write-Host "2. paid-user-safe   Shared team or future paid-user workspace"
    Write-Host "3. public-free      Lightest public-safe workspace"
    Write-Host "4. Cancel"
    Write-Host ""

    while ($true) {
        $choice = Read-Host "Select profile [1-4]"
        switch ($choice) {
            "1" { return "operator-local" }
            "2" { return "paid-user-safe" }
            "3" { return "public-free" }
            "4" { return "" }
            default { Write-Host "Enter 1, 2, 3, or 4." -ForegroundColor Yellow }
        }
    }
}

function Assert-Prerequisites {
    foreach ($command in @("git", "powershell")) {
        if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
            throw "Required command is not available in PATH: $command"
        }
    }

    if (-not (Test-Path -LiteralPath (Join-Path $provenanceRoot ".git") -PathType Container)) {
        throw "Run this file from a cloned CVF provenance repository."
    }

    $remote = (git -C $provenanceRoot remote get-url origin 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $remote -ne $provenanceRemote) {
        throw "Provenance origin mismatch. Expected: $provenanceRemote; found: $remote"
    }

    foreach ($relativePath in @(
        "scripts\install_cvf_workspace.ps1",
        "scripts\install_cvf_workspace_root_wrappers_public.ps1",
        "scripts\sync_cvf_workspace_rule_pack.ps1"
    )) {
        $path = Join-Path $provenanceRoot $relativePath
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Required workspace source is missing: $path"
        }
    }
}

function Assert-WorkspaceBoundary([string]$Path) {
    if (Test-Path -LiteralPath (Join-Path $Path ".git") -PathType Container) {
        throw "Workspace root must not be a git repository: $Path"
    }

    if ($Path.TrimEnd("\") -eq $provenanceRoot.TrimEnd("\")) {
        throw "Workspace root must be separate from the provenance repository."
    }
}

function Get-ActiveProfile([string]$Path) {
    $activePath = Join-Path $Path "CVF_RULE_PACKS\ACTIVE_RULE_PACK.json"
    if (-not (Test-Path -LiteralPath $activePath -PathType Leaf)) {
        return $null
    }
    return (Get-Content -LiteralPath $activePath -Raw -Encoding utf8 | ConvertFrom-Json)
}

function Install-NewWorkspace([string]$Path, [string]$Profile) {
    $baseProfile = $Profile
    if ($Profile -eq "operator-local") {
        $baseProfile = "paid-user-safe"
    }

    Write-Step "Installing hidden public core and '$baseProfile' base profile"
    Invoke-CheckedPowerShell `
        -ScriptPath (Join-Path $provenanceRoot "scripts\install_cvf_workspace.ps1") `
        -Arguments @("-WorkspaceRoot", $Path, "-ProfileName", $baseProfile)

    Write-Step "Aligning root wrappers and guides with the trusted provenance clone"
    Invoke-CheckedPowerShell `
        -ScriptPath (Join-Path $provenanceRoot "scripts\install_cvf_workspace_root_wrappers_public.ps1") `
        -Arguments @("-WorkspaceRoot", $Path)
}

function Refresh-ExistingWorkspace([string]$Path) {
    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    if (-not (Test-Path -LiteralPath $corePath -PathType Container)) {
        throw "Workspace exists but hidden public core is missing: $corePath"
    }

    $remote = (git -C $corePath remote get-url origin 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $remote -ne $publicRemote) {
        throw "Hidden core origin mismatch. Expected: $publicRemote; found: $remote"
    }

    $dirty = @(git -C $corePath status --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw "Could not read hidden core status."
    }
    if ($dirty.Count -gt 0) {
        throw "Hidden public core is dirty. Review it before workspace refresh."
    }

    Write-Step "Fast-forwarding hidden public core"
    git -C $corePath pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        throw "Hidden public core fast-forward failed."
    }

    Write-Step "Refreshing workspace root wrappers and guides"
    Invoke-CheckedPowerShell `
        -ScriptPath (Join-Path $provenanceRoot "scripts\install_cvf_workspace_root_wrappers_public.ps1") `
        -Arguments @("-WorkspaceRoot", $Path)
}

function Apply-SelectedProfile([string]$Path, [string]$Profile) {
    if ($Profile -eq "operator-local") {
        Write-Step "Applying private operator-local rule pack"
        Invoke-CheckedPowerShell `
            -ScriptPath (Join-Path $provenanceRoot "scripts\sync_cvf_workspace_rule_pack.ps1") `
            -Arguments @(
                "-WorkspaceRoot", $Path,
                "-ProfileName", "operator-local",
                "-AllowProvenanceContinuity"
            )
        return
    }

    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    $profileScript = Join-Path $corePath "scripts\sync_cvf_workspace_public_profile.ps1"
    Write-Step "Applying public-safe '$Profile' profile"
    Invoke-CheckedPowerShell `
        -ScriptPath $profileScript `
        -Arguments @("-WorkspaceRoot", $Path, "-ProfileName", $Profile)
}

function Test-WorkspaceResult([string]$Path, [string]$Profile) {
    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    $remote = (git -C $corePath remote get-url origin).Trim()
    if ($remote -ne $publicRemote) {
        throw "Post-install hidden core remote mismatch: $remote"
    }

    $active = Get-ActiveProfile -Path $Path
    if ($null -eq $active -or $active.activeProfile -ne $Profile) {
        throw "Post-install active profile mismatch. Expected: $Profile"
    }

    foreach ($requiredRootFile in @(
        "WORKSPACE_RULES.md",
        "CVF_WORKSPACE_CLASSIFICATION_GUIDE.md",
        "CVF_WORKSPACE_MEMORY.md",
        "AGENT_HANDOFF.md",
        "New-CVF-Governed-Project.ps1",
        "Run-CVF-NewProject-Enforcement.ps1"
    )) {
        if (-not (Test-Path -LiteralPath (Join-Path $Path $requiredRootFile) -PathType Leaf)) {
            throw "Post-install workspace artifact is missing: $requiredRootFile"
        }
    }

    if ($Profile -ne "operator-local") {
        $manager = Join-Path $Path "Manage-CVF-Workspace.ps1"
        Invoke-CheckedPowerShell `
            -ScriptPath $manager `
            -Arguments @("-Action", "Status")
    }

    if (-not $SkipEnforcementGate) {
        Write-Step "Running workspace project-enforcement gate"
        Invoke-CheckedPowerShell `
            -ScriptPath (Join-Path $Path "Run-CVF-NewProject-Enforcement.ps1")
    }

    $coreCommit = (git -C $corePath rev-parse --short HEAD).Trim()
    Write-Ok "Workspace ready"
    Write-Host "  Root:           $Path"
    Write-Host "  Profile:        $Profile"
    Write-Host "  Public core:    $coreCommit"
    Write-Host "  Classification: $(Join-Path $Path 'CVF_WORKSPACE_CLASSIFICATION_GUIDE.md')"
    Write-Host "  Next command:   .\New-CVF-Governed-Project.ps1 -ProjectName <name>"
}

try {
    Assert-Prerequisites

    if ([string]::IsNullOrWhiteSpace($ProfileName)) {
        if (-not $interactive) {
            throw "-ProfileName is required with -NonInteractive."
        }
        $ProfileName = Select-WorkspaceProfile
        if ([string]::IsNullOrWhiteSpace($ProfileName)) {
            Write-Host "Setup cancelled." -ForegroundColor Yellow
            exit 0
        }
    }

    $defaultWorkspace = Join-Path (Split-Path -Parent $provenanceRoot) "CVF-Workspace"
    if ([string]::IsNullOrWhiteSpace($WorkspaceRoot)) {
        if (-not $interactive) {
            throw "-WorkspaceRoot is required with -NonInteractive."
        }
        $enteredPath = Read-Host "Workspace path [$defaultWorkspace]"
        if ([string]::IsNullOrWhiteSpace($enteredPath)) {
            $WorkspaceRoot = $defaultWorkspace
        }
        else {
            $WorkspaceRoot = $enteredPath
        }
    }

    $workspaceResolved = [System.IO.Path]::GetFullPath($WorkspaceRoot)
    Assert-WorkspaceBoundary -Path $workspaceResolved
    $coreExists = Test-Path -LiteralPath (Join-Path $workspaceResolved ".Controlled-Vibe-Framework-CVF") -PathType Container
    $operation = if ($coreExists) { "REFRESH_EXISTING" } else { "CREATE_NEW" }
    $activeBefore = Get-ActiveProfile -Path $workspaceResolved

    if (-not $coreExists -and (Test-Path -LiteralPath $workspaceResolved -PathType Container)) {
        $existingItems = @(Get-ChildItem -LiteralPath $workspaceResolved -Force)
        if ($existingItems.Count -gt 0) {
            throw "New workspace target is not empty. Select an empty folder or an existing CVF Workspace with a hidden public core."
        }
    }

    if (
        $null -ne $activeBefore -and
        $activeBefore.activeProfile -eq "operator-local" -and
        $ProfileName -ne "operator-local"
    ) {
        throw "Refusing to convert an operator-local workspace in place. Create a separate clean public or paid-user workspace."
    }

    Write-Host ""
    Write-Host "Setup plan" -ForegroundColor Cyan
    Write-Host "  Provenance: $provenanceRoot"
    Write-Host "  Workspace:  $workspaceResolved"
    Write-Host "  Profile:    $ProfileName"
    Write-Host "  Operation:  $operation"
    Write-Host "  Boundary:   workspace root stays non-git; application projects stay outside hidden core"

    if ($PlanOnly) {
        Write-Ok "Plan validated; no files changed"
        exit 0
    }

    if ($interactive) {
        $confirmation = Read-Host "Continue? [Y/N]"
        if ($confirmation -notmatch "^(?i:y|yes)$") {
            Write-Host "Setup cancelled." -ForegroundColor Yellow
            exit 0
        }
    }

    New-Item -ItemType Directory -Path $workspaceResolved -Force | Out-Null
    if ($coreExists) {
        Refresh-ExistingWorkspace -Path $workspaceResolved
    }
    else {
        Install-NewWorkspace -Path $workspaceResolved -Profile $ProfileName
    }

    Apply-SelectedProfile -Path $workspaceResolved -Profile $ProfileName
    Test-WorkspaceResult -Path $workspaceResolved -Profile $ProfileName
}
catch {
    Write-Host "[FAILED] $($_.Exception.Message)" -ForegroundColor Red
    if ($interactive) {
        [void](Read-Host "Press Enter to close")
    }
    exit 1
}

if ($interactive) {
    [void](Read-Host "Press Enter to close")
}
