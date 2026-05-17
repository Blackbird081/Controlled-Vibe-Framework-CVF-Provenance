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

    -DryRun : Show what would be copied/pushed without making changes
    -NoPush : Copy files and commit but do not push to GitHub
#>

param(
    [switch]$DryRun,
    [switch]$NoPush
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
Write-Host "  $($allowedFiles.Count) files in allowlist."
Write-Host ''

if ($DryRun) {
    Write-Host 'Files that would be synced (first 50):' -ForegroundColor Yellow
    $allowedFiles | Select-Object -First 50 | ForEach-Object { Write-Host "  + $_" }
    if ($allowedFiles.Count -gt 50) {
        Write-Host "  ... and $($allowedFiles.Count - 50) more"
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

$govHead = git -C $GOVERNANCE_ROOT rev-parse --short HEAD
$govMsg  = git -C $GOVERNANCE_ROOT log -1 --pretty=%s

Write-Host 'Staging changes...' -ForegroundColor Yellow
git add -A

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
