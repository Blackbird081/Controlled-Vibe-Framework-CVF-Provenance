param(
    [Parameter(Mandatory = $true)]
    [string]$WorkspaceRoot
)

$ErrorActionPreference = "Stop"

function Write-Ok([string]$Message) {
    Write-Host "[OK]   $Message" -ForegroundColor Green
}

function Set-WorkspaceArtifact {
    param(
        [string]$Path,
        [string]$Content
    )

    Set-Content -LiteralPath $Path -Value $Content -Encoding utf8
    Write-Ok "Updated workspace artifact: $Path"
}

$workspaceRootResolved = [System.IO.Path]::GetFullPath($WorkspaceRoot)
if (-not (Test-Path -LiteralPath $workspaceRootResolved -PathType Container)) {
    throw "Workspace root not found: $workspaceRootResolved"
}

$governedProjectWrapper = @'
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectName,

    [string]$ProjectRepo = "",

    [switch]$CheckLiveReadiness,

    [switch]$AllowOfflinePinnedCore
)

$ErrorActionPreference = "Stop"

function Write-Info([string]$Message) {
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

$workspaceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$corePath = Join-Path $workspaceRoot ".Controlled-Vibe-Framework-CVF"
$bootstrapScript = Join-Path $corePath "scripts\new-cvf-workspace.ps1"
$doctorScript = Join-Path $corePath "scripts\check_cvf_workspace_agent_enforcement.ps1"
$gateScript = Join-Path $workspaceRoot "Run-CVF-NewProject-Enforcement.ps1"
$projectPath = Join-Path $workspaceRoot $ProjectName

foreach ($requiredPath in @($bootstrapScript, $doctorScript, $gateScript)) {
    if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
        throw "Required script not found: $requiredPath"
    }
}

Write-Info "Workspace root: $workspaceRoot"
Write-Info "Project name:   $ProjectName"

$bootstrapArgs = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $bootstrapScript,
    "-WorkspaceRoot", $workspaceRoot,
    "-ProjectName", $ProjectName
)

if (-not [string]::IsNullOrWhiteSpace($ProjectRepo)) {
    $bootstrapArgs += "-ProjectRepo"
    $bootstrapArgs += $ProjectRepo
}

& powershell @bootstrapArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Info "Running project doctor..."

$doctorArgs = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $doctorScript,
    "-ProjectPath", $projectPath
)

if ($CheckLiveReadiness) {
    $doctorArgs += "-CheckLiveReadiness"
}

if ($AllowOfflinePinnedCore) {
    $doctorArgs += "-AllowOfflinePinnedCore"
}

& powershell @doctorArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Info "Running workspace-wide new-project gate..."

$gateArgs = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $gateScript
)

if ($CheckLiveReadiness) {
    $gateArgs += "-CheckLiveReadiness"
}

if ($AllowOfflinePinnedCore) {
    $gateArgs += "-AllowOfflinePinnedCore"
}

& powershell @gateArgs
exit $LASTEXITCODE
'@

$workspaceGateWrapper = @'
param(
    [switch]$CheckLiveReadiness,
    [switch]$AllowOfflinePinnedCore
)

$ErrorActionPreference = "Stop"

$workspaceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$corePath = Join-Path $workspaceRoot ".Controlled-Vibe-Framework-CVF"
$gateScript = Join-Path $corePath "scripts\check_cvf_workspace_new_project_enforcement.ps1"

if (-not (Test-Path -LiteralPath $gateScript -PathType Leaf)) {
    throw "Workspace gate script not found: $gateScript"
}

$args = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $gateScript,
    "-WorkspaceRoot", $workspaceRoot
)

if ($CheckLiveReadiness) {
    $args += "-CheckLiveReadiness"
}

if ($AllowOfflinePinnedCore) {
    $args += "-AllowOfflinePinnedCore"
}

& powershell @args
exit $LASTEXITCODE
'@

$overlayProfilesWrapper = @'
param(
    [string]$ProfileName = "",
    [switch]$AsJson,
    [switch]$ShowFiles,
    [string]$ProvenanceRepoPath = ""
)

$ErrorActionPreference = "Stop"

function Resolve-CvfProvenanceRepoPath {
    param(
        [string]$WorkspaceRoot,
        [string]$ProvidedPath
    )

    $candidates = [System.Collections.Generic.List[string]]::new()
    foreach ($candidate in @($ProvidedPath, $env:CVF_PROVENANCE_REPO_PATH)) {
        if (-not [string]::IsNullOrWhiteSpace($candidate)) {
            $null = $candidates.Add($candidate)
        }
    }

    $workspaceParent = Split-Path -Parent $WorkspaceRoot
    foreach ($name in @(
        "Controlled-Vibe-Framework-CVF-Provenance",
        ".Controlled-Vibe-Framework-CVF-Provenance",
        "CVF-Provenance"
    )) {
        $null = $candidates.Add((Join-Path $workspaceParent $name))
    }

    foreach ($candidate in @($candidates | Select-Object -Unique)) {
        $resolved = [System.IO.Path]::GetFullPath($candidate)
        $reportScript = Join-Path $resolved "scripts\get_cvf_workspace_overlay_profile_report.ps1"
        if ((Test-Path -LiteralPath $resolved -PathType Container) -and
            (Test-Path -LiteralPath $reportScript -PathType Leaf)) {
            return $resolved
        }
    }

    throw "Provenance repo path not resolved. Pass -ProvenanceRepoPath, set CVF_PROVENANCE_REPO_PATH, or place the repo next to the workspace as Controlled-Vibe-Framework-CVF-Provenance."
}

$workspaceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$provenanceRepoResolved = Resolve-CvfProvenanceRepoPath -WorkspaceRoot $workspaceRoot -ProvidedPath $ProvenanceRepoPath
$reportScript = Join-Path $provenanceRepoResolved "scripts\get_cvf_workspace_overlay_profile_report.ps1"

$args = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $reportScript
)

if (-not [string]::IsNullOrWhiteSpace($ProfileName)) {
    $args += "-ProfileName"
    $args += $ProfileName
}

if ($AsJson) {
    $args += "-AsJson"
}

if ($ShowFiles) {
    $args += "-ShowFiles"
}

& powershell @args
exit $LASTEXITCODE
'@

$overlayUpdateWrapper = @'
param(
    [string]$ProfileName = "provenance-local",

    [string]$ProvenanceRepoPath = "",

    [switch]$UpdateProjectManifests,

    [switch]$AllowPendingCoreBackup,

    [switch]$KeepStaging
)

$ErrorActionPreference = "Stop"

function Write-Info([string]$Message) {
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Ok([string]$Message) {
    Write-Host "[OK]   $Message" -ForegroundColor Green
}

function Resolve-CvfProvenanceRepoPath {
    param(
        [string]$WorkspaceRoot,
        [string]$ProvidedPath
    )

    $candidates = [System.Collections.Generic.List[string]]::new()
    foreach ($candidate in @($ProvidedPath, $env:CVF_PROVENANCE_REPO_PATH)) {
        if (-not [string]::IsNullOrWhiteSpace($candidate)) {
            $null = $candidates.Add($candidate)
        }
    }

    $workspaceParent = Split-Path -Parent $WorkspaceRoot
    foreach ($name in @(
        "Controlled-Vibe-Framework-CVF-Provenance",
        ".Controlled-Vibe-Framework-CVF-Provenance",
        "CVF-Provenance"
    )) {
        $null = $candidates.Add((Join-Path $workspaceParent $name))
    }

    foreach ($candidate in @($candidates | Select-Object -Unique)) {
        $resolved = [System.IO.Path]::GetFullPath($candidate)
        $applyScript = Join-Path $resolved "scripts\apply_cvf_workspace_overlay.ps1"
        if ((Test-Path -LiteralPath $resolved -PathType Container) -and
            (Test-Path -LiteralPath $applyScript -PathType Leaf)) {
            return $resolved
        }
    }

    throw "Provenance repo path not resolved. Pass -ProvenanceRepoPath, set CVF_PROVENANCE_REPO_PATH, or place the repo next to the workspace as Controlled-Vibe-Framework-CVF-Provenance."
}

$workspaceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspaceRootResolved = [System.IO.Path]::GetFullPath($workspaceRoot)
$provenanceRepoResolved = Resolve-CvfProvenanceRepoPath -WorkspaceRoot $workspaceRoot -ProvidedPath $ProvenanceRepoPath
$applyScript = Join-Path $provenanceRepoResolved "scripts\apply_cvf_workspace_overlay.ps1"
$reportScript = Join-Path $provenanceRepoResolved "scripts\get_cvf_workspace_overlay_profile_report.ps1"
$receiptPath = Join-Path $workspaceRoot "CVF_WORKSPACE_OVERLAY_STATUS.json"

if (-not (Test-Path -LiteralPath $applyScript -PathType Leaf)) {
    throw "Overlay apply script not found: $applyScript"
}

Write-Info "Workspace root:       $workspaceRootResolved"
Write-Info "Overlay profile:      $ProfileName"
Write-Info "Provenance repo path: $provenanceRepoResolved"

$args = @(
    "-ExecutionPolicy", "Bypass",
    "-File", $applyScript,
    "-WorkspaceRoot", $workspaceRoot,
    "-ProfileName", $ProfileName
)

if ($UpdateProjectManifests) {
    $args += "-UpdateProjectManifests"
}

if ($AllowPendingCoreBackup) {
    $args += "-AllowPendingCoreBackup"
}

if ($KeepStaging) {
    $args += "-KeepStaging"
}

& powershell @args
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$corePath = Join-Path $workspaceRootResolved ".Controlled-Vibe-Framework-CVF"
$coreHead = (git -C $corePath rev-parse --short HEAD 2>$null | Out-String).Trim()
$coreOriginMain = (git -C $corePath rev-parse --short origin/main 2>$null | Out-String).Trim()
$corePending = @(git -C $corePath status --porcelain 2>$null)
$profileReport = $null
if (Test-Path -LiteralPath $reportScript -PathType Leaf) {
    $rawReport = & powershell -ExecutionPolicy Bypass -File $reportScript -ProfileName $ProfileName -AsJson
    if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace(($rawReport | Out-String))) {
        $profileReport = ($rawReport | Out-String) | ConvertFrom-Json
    }
}

$selectionTags = if ($null -ne $profileReport) {
    @($profileReport.includeSelectionTags | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
} else {
    @()
}
$artifactIds = if ($null -ne $profileReport) {
    @($profileReport.includeArtifactIds | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
} else {
    @()
}
$includePaths = if ($null -ne $profileReport) {
    @($profileReport.includePaths | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
} else {
    @()
}

$profileSelection = if ($null -ne $profileReport) {
    [PSCustomObject]@{
        includeSelectionTags = [object[]]@($selectionTags)
        includeArtifactIds = [object[]]@($artifactIds)
        includePaths = [object[]]@($includePaths)
    }
} else {
    [PSCustomObject]@{
        includeSelectionTags = [object[]]@()
        includeArtifactIds = [object[]]@()
        includePaths = [object[]]@()
    }
}

$receipt = [ordered]@{
    workspaceRoot = $workspaceRootResolved
    hiddenCorePath = $corePath
    profileName = $ProfileName
    provenanceRepoPath = $provenanceRepoResolved
    appliedAt = (Get-Date).ToString("s")
    hiddenCoreHead = $coreHead
    hiddenCoreOriginMain = $coreOriginMain
    hiddenCoreHasPendingOverlay = ($corePending.Count -gt 0)
    hiddenCorePendingPaths = @($corePending)
    resolvedProfiles = if ($null -ne $profileReport) { @($profileReport.resolvedProfiles) } else { @() }
    resolvedPathCount = if ($null -ne $profileReport) { [int]$profileReport.resolvedPathCount } else { 0 }
    profileSelection = $profileSelection
    continuitySurfaces = [ordered]@{
        cvfSession = Test-Path (Join-Path $corePath "CVF_SESSION")
        cvfSessionMemory = Test-Path (Join-Path $corePath "CVF_SESSION_MEMORY.md")
        activeVersionedHandoff = @(
            Get-ChildItem -LiteralPath $corePath -Filter "AGENT_HANDOFF_V*.md" -File -ErrorAction SilentlyContinue |
            Sort-Object Name |
            Select-Object -ExpandProperty Name
        )
    }
}

$receipt | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $receiptPath -Encoding utf8

$verifyProjectPath = Join-Path $workspaceRootResolved "vehicle-management-system"
$verifyTarget = if (Test-Path -LiteralPath $verifyProjectPath -PathType Container) {
    $verifyProjectPath
} else {
    "<project-path>"
}

Write-Ok "Overlay status receipt written: $receiptPath"
Write-Host "Suggested verification:" -ForegroundColor Yellow
Write-Host "  powershell -ExecutionPolicy Bypass -File `"$workspaceRootResolved\.Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1`" -ProjectPath `"$verifyTarget`""
exit 0
'@

$userGuide = @"
# CVF Workspace User Guide

This workspace is the local operator/user area for downstream projects that use
CVF rules without mixing project code into the CVF core itself.

## 1. Workspace Layout

```text
CVF-Workspace/
  .Controlled-Vibe-Framework-CVF/        # hidden public CVF core clone
  <Project-A>/                           # downstream project
  <Project-B>/                           # downstream project
  WORKSPACE_RULES.md
  WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json
  New-CVF-Governed-Project.ps1
  Run-CVF-NewProject-Enforcement.ps1
  Update-CVF-Workspace-Overlay.ps1
  Get-CVF-Workspace-OverlayProfiles.ps1
  CVF_WORKSPACE_OVERLAY_STATUS.json
  CVF_WORKSPACE_USER_GUIDE.md
```

Rules:

- The workspace root is not a git repo.
- Project code stays in sibling folders, not inside `.Controlled-Vibe-Framework-CVF/`.
- CVF core maintenance and workspace reconciliation run from the hidden core.

## 2. What The Hidden CVF Folder Is

`.Controlled-Vibe-Framework-CVF/` is a clone of the public repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Use it for:

- workspace bootstrap scripts
- workspace doctor / enforcement gate
- public-safe rules, guides, and continuation surfaces

Do not use it as the place to build the downstream app itself.

## 3. Fastest Safe Flow

For a brand-new governed project, use one command from the workspace root:

```powershell
powershell -ExecutionPolicy Bypass -File ".\New-CVF-Governed-Project.ps1" `
  -ProjectName "<project-name>"
```

If the project already has a remote repo:

```powershell
powershell -ExecutionPolicy Bypass -File ".\New-CVF-Governed-Project.ps1" `
  -ProjectName "<project-name>" `
  -ProjectRepo "<git-url>"
```

What this wrapper does:

- runs CVF bootstrap for the target project
- runs the project doctor
- runs the workspace-wide new-project enforcement gate

If this one command finishes with PASS, the new project is in the governed flow.

## 4. Daily Commands

Refresh the hidden public core:

```powershell
powershell -ExecutionPolicy Bypass -File ".Controlled-Vibe-Framework-CVF\scripts\update_cvf_workspace_public_core.ps1" `
  -WorkspaceRoot "$workspaceRootResolved" `
  -UpdateProjectManifests
```

Bootstrap a new project:

```powershell
powershell -ExecutionPolicy Bypass -File ".Controlled-Vibe-Framework-CVF\scripts\new-cvf-workspace.ps1" `
  -WorkspaceRoot "$workspaceRootResolved" `
  -ProjectName "<project-name>"
```

Run the doctor for one governed project:

```powershell
powershell -ExecutionPolicy Bypass -File ".Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1" `
  -ProjectPath "$workspaceRootResolved\<project-name>"
```

Run the workspace-wide new-project enforcement gate:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Run-CVF-NewProject-Enforcement.ps1"
```

Optional secret-free readiness check:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Run-CVF-NewProject-Enforcement.ps1" `
  -CheckLiveReadiness
```

## 5. Overlay Commands

Preview available overlay profiles:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Get-CVF-Workspace-OverlayProfiles.ps1"

powershell -ExecutionPolicy Bypass -File ".\Get-CVF-Workspace-OverlayProfiles.ps1" `
  -ProfileName "premium-workspace" `
  -ShowFiles
```

Apply a reviewed provenance overlay onto the hidden core:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Update-CVF-Workspace-Overlay.ps1" `
  -ProfileName "provenance-local" `
  -UpdateProjectManifests
```

If the provenance repo is not a sibling of this workspace, pass it explicitly:

```powershell
powershell -ExecutionPolicy Bypass -File ".\Update-CVF-Workspace-Overlay.ps1" `
  -ProfileName "provenance-local" `
  -ProvenanceRepoPath "D:\path\to\Controlled-Vibe-Framework-CVF-Provenance" `
  -UpdateProjectManifests
```

The overlay wrappers resolve the provenance repo in this order:

1. explicit `-ProvenanceRepoPath`
2. environment variable `CVF_PROVENANCE_REPO_PATH`
3. sibling folder `..\Controlled-Vibe-Framework-CVF-Provenance`

Each successful apply also refreshes:

- `CVF_WORKSPACE_OVERLAY_STATUS.json`

That receipt tells you which overlay profile is currently active, which
provenance repo was used as source, what public-base commit the hidden core is
on, which profile chain resolved, and whether the hidden core currently has
pending overlay changes.

## 6. Overlay Tiers For This Workspace

This workspace now supports three practical layers:

- `public-core`: only the public hidden core clone
- `premium-workspace`: curated provenance overlay with extra guards/rules but no private session continuity state
- `provenance-local`: local-only overlay that also adds canonical internal continuity surfaces such as `CVF_SESSION/`

Recommended usage:

- public-safe downstream use: keep `public-core`
- curated orientation-only or governance-only bundles: use a premium lane profile
- paid/internal downstream kit: use `premium-workspace`
- paid/internal downstream kit with optional operator + skill references: use `premium-extended-workspace`
- this operator machine with full continuity: use `provenance-local`
- this operator machine with full continuity + optional operator/skill lanes: use `provenance-extended-local`

Examples:

```powershell
# Curated premium layer
powershell -ExecutionPolicy Bypass -File ".\Update-CVF-Workspace-Overlay.ps1" `
  -ProfileName "premium-workspace" `
  -UpdateProjectManifests

# Extended premium layer
powershell -ExecutionPolicy Bypass -File ".\Update-CVF-Workspace-Overlay.ps1" `
  -ProfileName "premium-extended-workspace" `
  -UpdateProjectManifests

# Full local continuity layer
powershell -ExecutionPolicy Bypass -File ".\Update-CVF-Workspace-Overlay.ps1" `
  -ProfileName "provenance-local" `
  -UpdateProjectManifests

# Full local continuity + operator/skill lanes
powershell -ExecutionPolicy Bypass -File ".\Update-CVF-Workspace-Overlay.ps1" `
  -ProfileName "provenance-extended-local" `
  -UpdateProjectManifests
```

Important boundary:

- overlay is local-first and does not push anything to GitHub
- the hidden core still tracks the public remote as its base
- a local overlay can leave the hidden core worktree dirty; the doctor reports that as a bounded warning, not a hard failure

## 7. Legacy Projects Vs New Projects

This workspace uses:

- `WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json` to grandfather old sibling repos
- the workspace gate to enforce rules for any new sibling repo not listed in the baseline

Meaning:

- old projects can remain as-is for now
- every new governed project must pass the doctor
- `vehicle-management-system` is the current reference sample

## 8. What A Proper New Governed Project Must Have

After bootstrap, a governed project should contain at minimum:

- `.cvf/manifest.json`
- `.cvf/policy.json`
- `AGENTS.md`
- `docs/CVF_BOOTSTRAP_LOG_YYYYMMDD.md`
- `knowledge/README.md`

If these are missing, the project is not yet agent-enforcement-ready.

## 9. Why You May Or May Not See `CVF_SESSION`

That depends on the active overlay tier.

With `public-core` and `premium-workspace`, the hidden folder is still a public
CVF core base and should not depend on private session memory folders such as:

- `CVF_SESSION/`
- `CVF_SESSION_MEMORY.md`
- private internal continuity ledgers

Those surfaces belong to the provenance/internal side and are not part of the
public-safe workspace kit.

With `provenance-local`, those canonical continuity surfaces are intentionally
layered into the hidden core for this machine only.

For this public workspace, continuity is carried through these public-safe
surfaces instead:

- `.Controlled-Vibe-Framework-CVF\AGENT_HANDOFF.md`
- `.Controlled-Vibe-Framework-CVF\AGENTS.md`
- `.Controlled-Vibe-Framework-CVF\docs\reference\CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`
- each downstream project's `.cvf/manifest.json`
- each downstream project's `.cvf/policy.json`
- each downstream project's `AGENTS.md`
- each downstream project's bootstrap log under `docs/`

This is enough for downstream governed usage. It is not meant to expose the full
private memory system used in the provenance repo.

## 10. What The Workspace Inherits From CVF

This workspace inherits a strong public-safe operational subset of CVF:

- workspace isolation rules
- bootstrap contract
- doctor / enforcement gate
- downstream `AGENTS.md`
- `.cvf/manifest.json` and `.cvf/policy.json`
- public continuation and governance bootstrap surfaces

It does **not** inherit the full private provenance system:

- no `CVF_SESSION/`
- no private session-memory ledgers
- no internal review/archive packets
- no unpublished operator-only continuity state

That is intentional, not a missing installation.

The practical rule is:

- if a CVF capability has been promoted into public-safe scripts, guards, templates, or docs, the workspace can inherit it
- if a capability still depends on private provenance memory or internal audit state, the workspace should not inherit it directly

So the workspace does inherit useful CVF governance behavior, but not the full
internal memory substrate of the provenance repo.

The exception is the explicit `provenance-local` overlay, which is a deliberate
local operator choice and should not be confused with the public-safe default.

## 11. Practical Operating Rule

Use this decision rule:

- If you are maintaining CVF itself, work in the dedicated public/provenance clones outside this workspace.
- If you are building a downstream app with CVF rules, work inside the project folder under `CVF-Workspace`.
- If you add a new project, bootstrap it first, then run the enforcement gate.
"@

Set-WorkspaceArtifact -Path (Join-Path $workspaceRootResolved "New-CVF-Governed-Project.ps1") -Content $governedProjectWrapper
Set-WorkspaceArtifact -Path (Join-Path $workspaceRootResolved "Run-CVF-NewProject-Enforcement.ps1") -Content $workspaceGateWrapper
Set-WorkspaceArtifact -Path (Join-Path $workspaceRootResolved "Get-CVF-Workspace-OverlayProfiles.ps1") -Content $overlayProfilesWrapper
Set-WorkspaceArtifact -Path (Join-Path $workspaceRootResolved "Update-CVF-Workspace-Overlay.ps1") -Content $overlayUpdateWrapper
Set-WorkspaceArtifact -Path (Join-Path $workspaceRootResolved "CVF_WORKSPACE_USER_GUIDE.md") -Content $userGuide
