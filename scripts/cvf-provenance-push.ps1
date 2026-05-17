<#
.SYNOPSIS
    CVF Provenance Push - Luong 1

.DESCRIPTION
    Enable push URL, push to provenance archive, lock URL again immediately.
    Must be called explicitly by operator. Never runs automatically.

    Usage:
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -Branch main
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -DryRun
#>

param(
    [string]$Branch  = 'main',
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$PROVENANCE_URL  = 'https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git'
$DISABLED_MARKER = 'DISABLED_PROVENANCE_ARCHIVE_DO_NOT_PUSH_FROM_THIS_WORKSPACE'
$REPO_ROOT       = Split-Path -Parent $PSScriptRoot

Set-Location $REPO_ROOT

# Guard: must be in the governance repo
$currentFetch = git remote get-url origin 2>$null
if ($currentFetch -notmatch 'CVF-Provenance') {
    Write-Host '[ABORT] This script must be run from the CVF governance (provenance) repo.' -ForegroundColor Red
    Write-Host "        Current origin fetch URL: $currentFetch" -ForegroundColor Red
    exit 1
}

# Guard: push URL must currently be disabled
$currentPush = git remote get-url --push origin 2>$null
if ($currentPush -ne $DISABLED_MARKER) {
    Write-Host '[ABORT] Push URL is not in the expected disabled state.' -ForegroundColor Red
    Write-Host "        Found: $currentPush" -ForegroundColor Red
    Write-Host '        Lock the push URL manually before re-running.' -ForegroundColor Red
    exit 1
}

# Guard: clean working tree
$status = git status --porcelain
if ($status) {
    Write-Host '[ABORT] Working tree is not clean. Commit or stash changes first.' -ForegroundColor Red
    git status --short
    exit 1
}

Write-Host ''
Write-Host 'CVF Provenance Push' -ForegroundColor Cyan
Write-Host '===================' -ForegroundColor Cyan
Write-Host "  Repo   : $REPO_ROOT"
Write-Host "  Target : $PROVENANCE_URL"
Write-Host "  Branch : $Branch"
if ($DryRun) { Write-Host '  Mode   : DRY RUN - no changes made' -ForegroundColor Yellow }
Write-Host ''

if (-not $DryRun) {
    # Step 1: Enable push URL
    Write-Host '[1/3] Enabling push URL...' -ForegroundColor Yellow
    git remote set-url --push origin $PROVENANCE_URL
    Write-Host '      Push URL set.' -ForegroundColor Green

    try {
        # Step 2: Push
        Write-Host "[2/3] Pushing $Branch to provenance archive..." -ForegroundColor Yellow
        git push origin $Branch
        Write-Host '      Push complete.' -ForegroundColor Green
    }
    finally {
        # Step 3: Lock immediately (runs even if push fails)
        Write-Host '[3/3] Locking push URL...' -ForegroundColor Yellow
        git remote set-url --push origin $DISABLED_MARKER
        Write-Host '      Push URL locked.' -ForegroundColor Green
    }

    Write-Host ''
    Write-Host 'Done. Push URL is locked again.' -ForegroundColor Cyan

} else {
    Write-Host "[DRY RUN] Would enable push URL: $PROVENANCE_URL" -ForegroundColor Yellow
    Write-Host "[DRY RUN] Would push branch: $Branch" -ForegroundColor Yellow
    Write-Host "[DRY RUN] Would lock push URL back to: $DISABLED_MARKER" -ForegroundColor Yellow
    Write-Host ''
    Write-Host 'Run without -DryRun to execute.' -ForegroundColor Cyan
}
