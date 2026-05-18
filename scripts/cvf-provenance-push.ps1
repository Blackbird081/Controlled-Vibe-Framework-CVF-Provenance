<#
.SYNOPSIS
    CVF Provenance Push - Luong 1

.DESCRIPTION
    Run the full CVF pre-push governance hook chain locally to verify all files
    pass guard checks, then enable the provenance push URL, push to the archive,
    and lock the URL again immediately.

    The hook chain runs BEFORE the push URL is ever enabled. If any check fails,
    the URL stays locked and nothing is pushed.

    Usage:
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -Branch main
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -DryRun
        powershell -ExecutionPolicy Bypass -File scripts\cvf-provenance-push.ps1 -DryRun -ParallelPreflight

    -DryRun : Run the hook chain but do not actually push
    -ParallelPreflight : Run the local pre-push checks in parallel with
      [done/total] progress before any push URL is enabled
#>

param(
    [string]$Branch  = 'main',
    [switch]$DryRun,
    [switch]$ParallelPreflight,
    [int]$MaxParallelChecks = 6
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
if ($DryRun) { Write-Host '  Mode   : DRY RUN - governance check only, no push' -ForegroundColor Yellow }
if ($ParallelPreflight) { Write-Host "  Checks : PARALLEL PREFLIGHT - max $MaxParallelChecks concurrent checks" -ForegroundColor Yellow }
Write-Host ''

# Step 1: Run full pre-push governance hook chain
Write-Host '[1/4] Running CVF pre-push governance hook chain...' -ForegroundColor Yellow
Write-Host '      This verifies all files pass guard checks before the push URL is enabled.'
Write-Host '      Progress is streamed live; each check reports [current/total].'
Write-Host ''

$hookArgs = @('governance/compat/run_local_governance_hook_chain.py', '--hook', 'pre-push')
if ($ParallelPreflight) {
    $hookArgs += @('--parallel', '--max-workers', "$MaxParallelChecks")
}

& python @hookArgs
$hookExit   = $LASTEXITCODE

if ($hookExit -ne 0) {
    Write-Host ''
    Write-Host '[ABORT] Governance hook chain FAILED. Push URL remains locked.' -ForegroundColor Red
    Write-Host '        Fix the violations above, then re-run this script.' -ForegroundColor Red
    exit $hookExit
}

Write-Host ''
Write-Host '      Hook chain passed.' -ForegroundColor Green
Write-Host ''

if ($DryRun) {
    Write-Host '[DRY RUN] Governance checks passed. Push skipped (-DryRun).' -ForegroundColor Yellow
    Write-Host '          Run without -DryRun to push to provenance archive.' -ForegroundColor Yellow
    exit 0
}

# Step 2: Enable push URL
Write-Host '[2/4] Enabling push URL...' -ForegroundColor Yellow
git remote set-url --push origin $PROVENANCE_URL
Write-Host '      Push URL set.' -ForegroundColor Green

try {
    # Step 3: Push (pre-push hook will run again - fast because no changes)
    Write-Host "[3/4] Pushing $Branch to provenance archive..." -ForegroundColor Yellow
    git push origin $Branch
    Write-Host '      Push complete.' -ForegroundColor Green
}
finally {
    # Step 4: Lock immediately (runs even if push fails)
    Write-Host '[4/4] Locking push URL...' -ForegroundColor Yellow
    git remote set-url --push origin $DISABLED_MARKER
    $locked = git remote get-url --push origin
    if ($locked -eq $DISABLED_MARKER) {
        Write-Host '      Push URL locked.' -ForegroundColor Green
    } else {
        Write-Host "[WARN] Lock may have failed. Current push URL: $locked" -ForegroundColor Red
    }
}

Write-Host ''
Write-Host 'Done. Push URL is locked again.' -ForegroundColor Cyan
Write-Host ''
