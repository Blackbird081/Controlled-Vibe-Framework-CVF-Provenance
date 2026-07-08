<#
.SYNOPSIS
    CVF Public Sync - Luong 2

.DESCRIPTION
    Sync allowed files from the governance repo to the public-sync repo,
    then push to GitHub. Uses an explicit allowlist - never copies internal
    governance artifacts (AGENT_HANDOFF, baselines, reviews, roadmaps).

    Usage:
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -DryRun
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -NoPush
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -NoCommit
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -WorkspaceKitOnly -NoCommit

    -DryRun : Show what would be copied/pushed without making changes
    -NoPush : Copy files and commit but do not push to GitHub
    -NoCommit : Copy files only; leave the public-sync worktree pending for review
    -WorkspaceKitOnly : Sync only the bounded public workspace reconciliation kit
#>

param(
    [switch]$DryRun,
    [switch]$NoPush,
    [switch]$NoCommit,
    [switch]$WorkspaceKitOnly
)

$ErrorActionPreference = 'Stop'

$GOVERNANCE_ROOT  = Split-Path -Parent $PSScriptRoot
$PUBLIC_SYNC_ROOT = 'D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync'
$PUBLIC_REMOTE    = 'https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git'

# Allowlist: directory trees that may be synced
$ALLOWED_TREES = @(
    'EXTENSIONS',
    'ECOSYSTEM',
    'governance',
    'v1.0',
    'v1.1',
    'tools',
    '.github',
    'App onboarding'
)

# Allowlist: root-level files that may be synced
$ALLOWED_ROOT_FILES = @(
    'ARCHITECTURE.md',
    'CHANGELOG.md',
    'CODEOWNERS',
    'CONTRIBUTING.md',
    'CONTRIBUTORS.md',
    'COST_AND_QUOTA.md',
    'GOVERNANCE.md',
    'LICENSE',
    'PROVIDERS.md',
    'PROVENANCE.md',
    'README.md',
    'SECURITY.md',
    'netlify.toml',
    'package.json',
    'package-lock.json'
)

# Allowlist: public-safe scripts only. Do not export the provenance operation
# scripts directory wholesale.
$ALLOWED_SCRIPT_FILES = @(
    'scripts\bootstrap_foundations.ps1',
    'scripts\bootstrap_foundations.sh',
    'scripts\check_cvf_workspace_agent_enforcement.ps1',
    'scripts\check_cvf_workspace_new_project_enforcement.ps1',
    'scripts\ingest_cvf_downstream_knowledge.ps1',
    'scripts\install_cvf_hooks.ps1',
    'scripts\new-cvf-workspace.ps1',
    'scripts\update_cvf_workspace_public_core.ps1',
    'scripts\w114_cp7_multi_sample_downstream_proof.ps1',
    'scripts\write_cvf_workspace_web_evidence_bridge.ps1'
)

# Mapped exports keep private provenance root files private while still
# publishing a public-safe root front door.
$MAPPED_FILES = @(
    @{
        Source      = 'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_AGENTS.md'
        Destination = 'AGENTS.md'
    },
    @{
        Source      = 'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_CONTINUATION.md'
        Destination = 'AGENT_HANDOFF.md'
    },
    @{
        Source      = 'scripts\install_cvf_workspace_root_wrappers_public.ps1'
        Destination = 'scripts\install_cvf_workspace_root_wrappers.ps1'
    }
)

$WORKSPACE_KIT_FILES = @(
    'docs\GET_STARTED.md',
    'docs\reference\CVF_NEW_MACHINE_SETUP_CHECKLIST.md',
    'docs\reference\CVF_W114_PUBLIC_EVIDENCE_PACKET_2026-04-23.md',
    'docs\reference\CVF_WORKSPACE_RULES.md',
    'governance\toolkit\05_OPERATION\CVF_DOWNSTREAM_AGENTS_TEMPLATE.md',
    'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_AGENTS.md',
    'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_CONTINUATION.md',
    'governance\toolkit\05_OPERATION\CVF_WORKSPACE_ISOLATION_GUARD.md'
) + $ALLOWED_SCRIPT_FILES

# Allowlist: docs/ sub-paths that may be synced
# baselines/, reviews/, roadmaps/ are intentionally absent
$ALLOWED_DOCS_PATHS = @(
    'docs\GET_STARTED.md',
    'docs\CHEAT_SHEET.md',
    'docs\CVF_ARCHITECTURE_DECISIONS.md',
    'docs\CVF_CORE_KNOWLEDGE_BASE.md',
    'docs\EXPORT_MANIFEST.md',
    'docs\concepts',
    'docs\guides',
    'docs\reference',
    'docs\benchmark'
)

# Denylist: explicit patterns checked at copy time (defense-in-depth)
$DENY_PATTERNS = @(
    '^AGENT_HANDOFF',
    '^docs[/\\]baselines[/\\]',
    '^docs[/\\]reviews[/\\]',
    '^docs[/\\]roadmaps[/\\]',
    # Internal operation scripts - provenance repo only
    'scripts[/\\]cvf-provenance-push\.ps1$',
    'scripts[/\\]cvf-public-sync\.ps1$',
    '\.env$',
    '\.env\.local$',
    '\.env\.[^e]',
    '[/\\]node_modules[/\\]',
    '[/\\]\.next[/\\]',
    '[/\\]\.next-',
    '[/\\]coverage[/\\]',
    '[/\\]test-results[/\\]',
    '[/\\]playwright-report[/\\]',
    '[/\\]__pycache__[/\\]',
    '[/\\]\.data[/\\]',
    '\.tsbuildinfo$',
    '\.pyc$',
    '\.log$',
    '\.tmp$'
)

# -----------------------------------------------------------------------

function Test-Denied {
    param([string]$RelPath)
    foreach ($pattern in $DENY_PATTERNS) {
        if ($RelPath -match $pattern) { return $true }
    }
    return $false
}

function Get-AllowedFiles {
    $files = [System.Collections.Generic.List[string]]::new()

    # Root-level files
    foreach ($f in $ALLOWED_ROOT_FILES) {
        $full = Join-Path $GOVERNANCE_ROOT $f
        if (Test-Path $full -PathType Leaf) { $files.Add($f) }
    }

    # Public-safe scripts
    foreach ($scriptPath in $ALLOWED_SCRIPT_FILES) {
        $full = Join-Path $GOVERNANCE_ROOT $scriptPath
        if (Test-Path $full -PathType Leaf) { $files.Add($scriptPath) }
    }

    # Allowed directory trees
    foreach ($tree in $ALLOWED_TREES) {
        $treeRoot = Join-Path $GOVERNANCE_ROOT $tree
        if (-not (Test-Path $treeRoot)) { continue }
        Get-ChildItem -Recurse -File $treeRoot | ForEach-Object {
            $rel = $_.FullName.Substring($GOVERNANCE_ROOT.Length + 1)
            if (-not (Test-Denied $rel)) { $files.Add($rel) }
        }
    }

    # docs/ sub-paths
    foreach ($docPath in $ALLOWED_DOCS_PATHS) {
        $full = Join-Path $GOVERNANCE_ROOT $docPath
        if (-not (Test-Path $full)) { continue }
        if (Test-Path $full -PathType Leaf) {
            if (-not (Test-Denied $docPath)) { $files.Add($docPath) }
        } else {
            Get-ChildItem -Recurse -File $full | ForEach-Object {
                $rel = $_.FullName.Substring($GOVERNANCE_ROOT.Length + 1)
                if (-not (Test-Denied $rel)) { $files.Add($rel) }
            }
        }
    }

    return ($files | Sort-Object -Unique)
}

# -----------------------------------------------------------------------

# Validate governance repo
if (-not (Test-Path $GOVERNANCE_ROOT)) {
    Write-Host "[ABORT] Governance repo not found: $GOVERNANCE_ROOT" -ForegroundColor Red
    exit 1
}

# Validate public-sync repo
if (-not (Test-Path $PUBLIC_SYNC_ROOT)) {
    Write-Host "[ABORT] Public-sync repo not found: $PUBLIC_SYNC_ROOT" -ForegroundColor Red
    exit 1
}

# Validate public-sync remote URL
$pubRemote = git -C $PUBLIC_SYNC_ROOT remote get-url origin 2>$null
if ($pubRemote -ne $PUBLIC_REMOTE) {
    Write-Host '[ABORT] Public-sync repo origin does not match expected URL.' -ForegroundColor Red
    Write-Host "        Expected : $PUBLIC_REMOTE"
    Write-Host "        Found    : $pubRemote"
    exit 1
}

# -----------------------------------------------------------------------

Write-Host ''
Write-Host 'CVF Public Sync' -ForegroundColor Cyan
Write-Host '===============' -ForegroundColor Cyan
Write-Host "  From : $GOVERNANCE_ROOT"
Write-Host "  To   : $PUBLIC_SYNC_ROOT"
if ($DryRun) { Write-Host '  Mode : DRY RUN' -ForegroundColor Yellow }
if ($NoPush) { Write-Host '  Push : DISABLED (-NoPush)' -ForegroundColor Yellow }
Write-Host ''

Write-Host 'Collecting allowed files...' -ForegroundColor Yellow
$allowedFiles = Get-AllowedFiles
if ($WorkspaceKitOnly) {
    $allowedFiles = @($allowedFiles | Where-Object { $_ -in $WORKSPACE_KIT_FILES })
}
Write-Host "  $($allowedFiles.Count) files in allowlist."
Write-Host ''

if ($DryRun) {
    Write-Host 'Files that would be synced (first 50):' -ForegroundColor Yellow
    $allowedFiles | Select-Object -First 50 | ForEach-Object { Write-Host "  + $_" }
    if ($allowedFiles.Count -gt 50) {
        Write-Host "  ... and $($allowedFiles.Count - 50) more"
    }
    Write-Host ''
    Write-Host 'Mapped exports:' -ForegroundColor Yellow
    foreach ($mapping in $MAPPED_FILES) {
        Write-Host "  + $($mapping.Source) -> $($mapping.Destination)"
    }
    Write-Host ''
    Write-Host 'DRY RUN complete. No changes made.' -ForegroundColor Cyan
    exit 0
}

# Copy files
Write-Host 'Copying files...' -ForegroundColor Yellow
$copied  = 0
$denied  = 0

foreach ($rel in $allowedFiles) {
    $src = Join-Path $GOVERNANCE_ROOT $rel
    $dst = Join-Path $PUBLIC_SYNC_ROOT $rel

    if (Test-Denied $rel) {
        Write-Host "  [DENIED] $rel" -ForegroundColor Red
        $denied++
        continue
    }

    $dstDir = Split-Path $dst -Parent
    if (-not (Test-Path $dstDir)) {
        New-Item -ItemType Directory -Force $dstDir | Out-Null
    }
    Copy-Item -Force $src $dst
    $copied++
}

foreach ($mapping in $MAPPED_FILES) {
    $src = Join-Path $GOVERNANCE_ROOT $mapping.Source
    $dst = Join-Path $PUBLIC_SYNC_ROOT $mapping.Destination
    if (-not (Test-Path $src -PathType Leaf)) {
        throw "Mapped public export source not found: $src"
    }
    $dstDir = Split-Path $dst -Parent
    if (-not (Test-Path $dstDir)) {
        New-Item -ItemType Directory -Force $dstDir | Out-Null
    }
    Copy-Item -Force $src $dst
    $copied++
}

Write-Host "  Copied : $copied"
Write-Host "  Denied : $denied"
Write-Host ''

# Commit
Set-Location $PUBLIC_SYNC_ROOT

$gitStatus = git status --porcelain
if (-not $gitStatus) {
    Write-Host 'No changes detected in public-sync repo. Nothing to commit.' -ForegroundColor Yellow
    exit 0
}

if ($NoCommit) {
    Write-Host 'Public-sync worktree updated. Skipping commit and push (-NoCommit).' -ForegroundColor Yellow
    Write-Host "Review pending changes in: $PUBLIC_SYNC_ROOT" -ForegroundColor Yellow
    exit 0
}

$govHead = git -C $GOVERNANCE_ROOT rev-parse --short HEAD
$govMsg  = git -C $GOVERNANCE_ROOT log -1 --pretty=%s

Write-Host 'Staging changes...' -ForegroundColor Yellow
git add -A
foreach ($mapping in $MAPPED_FILES) {
    git add -f -- $mapping.Destination
}

$commitMsg = @"
sync: public surface update from governance@$govHead

Source: $govHead - $govMsg

Synced via cvf-public-sync.ps1 allowlist.
Internal artifacts excluded: AGENT_HANDOFF, baselines, reviews, roadmaps.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
"@

Write-Host 'Committing...' -ForegroundColor Yellow
git commit -m $commitMsg
Write-Host ''

# Push
if (-not $NoPush) {
    Write-Host "Pushing to $PUBLIC_REMOTE ..." -ForegroundColor Yellow
    git push origin main
    Write-Host ''
    Write-Host 'Public sync complete.' -ForegroundColor Green
} else {
    Write-Host 'Committed locally. Skipping push (-NoPush).' -ForegroundColor Yellow
    Write-Host "Run 'git push origin main' in $PUBLIC_SYNC_ROOT when ready." -ForegroundColor Yellow
}

Write-Host ''
