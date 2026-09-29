<#
.SYNOPSIS
    CVF Projection Automation T2 disposable three-root proof runner.

.DESCRIPTION
    Proves the accepted T1 mapper (scripts\get_cvf_projection_map.ps1) end to
    end against three disposable, git-initialized fixture roots (provenance,
    public-sync, cvf-web) built under one unique temp parent. It never uses a
    real repository root as a proof target, never contacts a network, and
    never modifies scripts\cvf-public-sync.ps1, scripts\get_cvf_projection_map.ps1,
    scripts\cvf_projection_policy.json, or any other committed source.

    The fixture provenance root receives a literal copy of the current,
    committed scripts\cvf-public-sync.ps1 as read-only policy-parity source
    evidence only; this copy is never executed or dot-sourced anywhere in
    this runner or in the mapper it invokes.

    The proof runs the committed mapper twice against the same fixture and
    committed scripts\cvf_projection_policy.json, compares the two receipts
    for byte-identical stdout and receipt ID, validates schema/parity/count/
    secret/BOM properties, and proves zero filesystem or git-status delta
    across all three disposable roots before and after every mapper
    invocation. The governed proof receipt is written to the real
    docs/reviews/ path only when -GovernedReceiptPath is explicitly supplied;
    by default the receipt goes to a temp-only location.

    The unique temp parent is always deleted in a `finally` block, including
    on early failure.

.PARAMETER GovernedReceiptPath
    Optional. When supplied, the deterministic proof receipt from the second
    mapper run is also written to this path (expected:
    docs/reviews/CVF_PROJECTION_AUTOMATION_T2_THREE_ROOT_PROOF_RECEIPT_2026-07-18.json).
    When omitted, the receipt is written to a temp-only location and the
    governed path is never touched.

.OUTPUTS
    Named PASS/FAIL assertion lines and a final total. Exit code 0 when every
    assertion passes; nonzero otherwise.
#>

[CmdletBinding()]
param(
    [string]$GovernedReceiptPath,
    [switch]$CleanupFailureSelfTestChild,
    [string]$CleanupFailureSelfTestRoot
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $scriptRoot '..')).ProviderPath
$mapperPath = Join-Path $scriptRoot 'get_cvf_projection_map.ps1'
$policyPath = Join-Path $scriptRoot 'cvf_projection_policy.json'
$realSyncScriptPath = Join-Path $scriptRoot 'cvf-public-sync.ps1'

$proofRunId = [guid]::NewGuid().ToString('N').Substring(0, 8)
$tempRoot = if ($CleanupFailureSelfTestRoot) {
    $CleanupFailureSelfTestRoot
} else {
    Join-Path $env:TEMP "cvf_three_root_proof_$proofRunId"
}

$script:passCount = 0
$script:failCount = 0
$script:results = [System.Collections.Generic.List[string]]::new()

function Assert-True {
    param([bool]$Condition, [string]$CaseName, [string]$Detail = '')
    if ($Condition) {
        $script:passCount++
        $script:results.Add("PASS: $CaseName")
    } else {
        $script:failCount++
        $script:results.Add("FAIL: $CaseName -- $Detail")
    }
}

function Remove-ProofTempRoot {
    param([string]$Path)
    if (Test-Path -LiteralPath $Path) {
        Remove-Item -LiteralPath $Path -Recurse -Force -ErrorAction SilentlyContinue
    }
}

function New-DisposableGitRepo {
    param([string]$Path, [string]$OriginUrl)
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
    Push-Location $Path
    try {
        & git init -q *>$null
        & git config user.email 'proof@example.invalid' *>$null
        & git config user.name 'CVF Three-Root Proof' *>$null
        & git config core.autocrlf false *>$null
        if ($OriginUrl) {
            & git remote add origin $OriginUrl *>$null
        }
        'proof fixture' | Out-File -FilePath (Join-Path $Path 'README.md') -Encoding utf8 -NoNewline
        & git add -A *>$null
        & git commit -q -m 'proof fixture init' *>$null
    } finally {
        Pop-Location
    }
}

function Invoke-Mapper {
    param(
        [string]$ProvenanceRoot,
        [string]$PublicSyncRoot,
        [string]$CvfWebRoot,
        [string]$PolicyPath,
        [string]$ReceiptOutputPath,
        [string]$WorkingDirectory
    )
    $argList = @(
        '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $mapperPath,
        '-ProvenanceRoot', $ProvenanceRoot,
        '-PublicSyncRoot', $PublicSyncRoot,
        '-CvfWebRoot', $CvfWebRoot,
        '-PolicyPath', $PolicyPath
    )
    if ($ReceiptOutputPath) {
        $argList += @('-ReceiptOutputPath', $ReceiptOutputPath)
    }
    $prevLocation = Get-Location
    if ($WorkingDirectory) { Set-Location $WorkingDirectory }
    try {
        $stdout = & powershell -NoProfile -ExecutionPolicy Bypass @argList 2>&1
        $exitCode = $LASTEXITCODE
    } finally {
        Set-Location $prevLocation
    }
    $stdoutText = ($stdout -join "`n")
    $json = $null
    try { $json = $stdoutText | ConvertFrom-Json } catch { $json = $null }
    return [pscustomobject]@{
        ExitCode = $exitCode
        StdoutText = $stdoutText
        Json = $json
    }
}

function Get-RootSnapshot {
    param([string]$RootPath)
    $status = (& git -C $RootPath status --porcelain) -join "`n"
    $files = Get-ChildItem -LiteralPath $RootPath -Recurse -File -Force |
        ForEach-Object { $_.FullName } | Sort-Object
    return [pscustomobject]@{
        Status = $status
        Files = $files
    }
}

function Compare-RootSnapshot {
    param([pscustomobject]$Before, [pscustomobject]$After)
    $statusMatch = ($Before.Status -eq $After.Status)
    $filesDiff = Compare-Object -ReferenceObject $Before.Files -DifferenceObject $After.Files -SyncWindow 0
    $filesMatch = (@($filesDiff).Count -eq 0)
    return [pscustomobject]@{
        StatusMatch = $statusMatch
        FilesMatch = $filesMatch
    }
}

try {
    New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

    if ($CleanupFailureSelfTestChild) {
        throw 'INTENTIONAL_CLEANUP_FAILURE_SELF_TEST'
    }

    # -----------------------------------------------------------------
    # Assertion 1: real committed mapper/policy/sync-script exist before
    # any fixture is built (source parity precondition).
    # -----------------------------------------------------------------
    Assert-True (Test-Path -LiteralPath $mapperPath -PathType Leaf) 'committed_mapper_exists' 'get_cvf_projection_map.ps1 not found'
    Assert-True (Test-Path -LiteralPath $policyPath -PathType Leaf) 'committed_policy_exists' 'cvf_projection_policy.json not found'
    Assert-True (Test-Path -LiteralPath $realSyncScriptPath -PathType Leaf) 'committed_sync_script_exists' 'cvf-public-sync.ps1 not found'

    # -----------------------------------------------------------------
    # Build the unique temp parent with provenance, public-sync, cvf-web,
    # and receipt-output subdirectories (Required Implementation bullet 1).
    # -----------------------------------------------------------------
    $provRoot = Join-Path $tempRoot 'provenance'
    $pubRoot = Join-Path $tempRoot 'public-sync'
    $cvfWebRoot = Join-Path $tempRoot 'cvfweb'
    $receiptOutputDir = Join-Path $tempRoot 'receipt-output'
    New-Item -ItemType Directory -Path $receiptOutputDir -Force | Out-Null

    $policy = Get-Content -LiteralPath $policyPath -Raw -Encoding utf8 | ConvertFrom-Json

    New-DisposableGitRepo -Path $provRoot -OriginUrl $policy.expectedRemotes.provenanceRemote
    New-DisposableGitRepo -Path $pubRoot -OriginUrl $policy.expectedRemotes.publicRemote
    New-DisposableGitRepo -Path $cvfWebRoot -OriginUrl ''
    New-Item -ItemType Directory -Path (Join-Path $cvfWebRoot 'src\lib\server') -Force | Out-Null
    Assert-True (Test-Path -LiteralPath $provRoot -PathType Container) 'temp_parent_provenance_root_created' 'provenance fixture dir missing'
    Assert-True (Test-Path -LiteralPath $pubRoot -PathType Container) 'temp_parent_public_sync_root_created' 'public-sync fixture dir missing'
    Assert-True (Test-Path -LiteralPath $cvfWebRoot -PathType Container) 'temp_parent_cvfweb_root_created' 'cvf-web fixture dir missing'

    # -----------------------------------------------------------------
    # Assertion: fixture origins match policy URLs exactly, with zero
    # network access performed (git remote add only, no fetch/clone).
    # -----------------------------------------------------------------
    $provOrigin = (& git -C $provRoot remote get-url origin)
    $pubOrigin = (& git -C $pubRoot remote get-url origin)
    Assert-True ($provOrigin -eq $policy.expectedRemotes.provenanceRemote) 'fixture_provenance_origin_matches_policy' "found: $provOrigin"
    Assert-True ($pubOrigin -eq $policy.expectedRemotes.publicRemote) 'fixture_public_sync_origin_matches_policy' "found: $pubOrigin"

    # -----------------------------------------------------------------
    # Copy the current committed cvf-public-sync.ps1 into the disposable
    # provenance root as read-only policy-parity source evidence, then
    # commit it. This copy is never executed or dot-sourced.
    # -----------------------------------------------------------------
    New-Item -ItemType Directory -Path (Join-Path $provRoot 'scripts') -Force | Out-Null
    Copy-Item -LiteralPath $realSyncScriptPath -Destination (Join-Path $provRoot 'scripts\cvf-public-sync.ps1') -Force

    # Build a bounded candidate set covering absent, changed, unchanged,
    # denied, not-allowlisted, mapped export, and cvf-web SOT3 observation.
    'root readme content' | Out-File -LiteralPath (Join-Path $provRoot 'README.md') -Encoding utf8 -NoNewline
    'license text' | Out-File -LiteralPath (Join-Path $provRoot 'LICENSE') -Encoding utf8 -NoNewline
    New-Item -ItemType Directory -Path (Join-Path $provRoot 'EXTENSIONS\SAMPLE_EXT') -Force | Out-Null
    'extension source content' | Out-File -LiteralPath (Join-Path $provRoot 'EXTENSIONS\SAMPLE_EXT\index.ts') -Encoding utf8 -NoNewline
    New-Item -ItemType Directory -Path (Join-Path $provRoot 'docs\reference') -Force | Out-Null
    'reference doc content' | Out-File -LiteralPath (Join-Path $provRoot 'docs\reference\SAMPLE_REF.md') -Encoding utf8 -NoNewline
    New-Item -ItemType Directory -Path (Join-Path $provRoot 'governance\toolkit\05_OPERATION') -Force | Out-Null
    'mapped agents content' | Out-File -LiteralPath (Join-Path $provRoot 'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_AGENTS.md') -Encoding utf8 -NoNewline
    'mapped continuation content' | Out-File -LiteralPath (Join-Path $provRoot 'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_CONTINUATION.md') -Encoding utf8 -NoNewline
    New-Item -ItemType Directory -Path (Join-Path $provRoot 'scripts') -Force | Out-Null
    'wrapper install content' | Out-File -LiteralPath (Join-Path $provRoot 'scripts\install_cvf_workspace_root_wrappers_public.ps1') -Encoding utf8 -NoNewline
    '.env secret content' | Out-File -LiteralPath (Join-Path $provRoot '.env.local') -Encoding utf8 -NoNewline
    'unlisted operator note' | Out-File -LiteralPath (Join-Path $provRoot 'UNLISTED_NOTE.txt') -Encoding utf8 -NoNewline

    'root readme content' | Out-File -LiteralPath (Join-Path $pubRoot 'README.md') -Encoding utf8 -NoNewline
    New-Item -ItemType Directory -Path (Join-Path $pubRoot 'EXTENSIONS\SAMPLE_EXT') -Force | Out-Null
    'DIFFERENT already-published extension content' | Out-File -LiteralPath (Join-Path $pubRoot 'EXTENSIONS\SAMPLE_EXT\index.ts') -Encoding utf8 -NoNewline

    & git -C $provRoot add -A *>$null
    & git -C $provRoot commit -q -m 'proof candidate fixture' *>$null
    & git -C $pubRoot add -A *>$null
    & git -C $pubRoot commit -q -m 'proof target fixture' *>$null

    @'
{
  "name": "fixture-cvf-web",
  "version": "0.0.0-fixture",
  "dependencies": {
    "cvf-refinery": "file:../CVF_REFINERY",
    "cvf-truth-kernel": "file:../CVF_TRUTH_KERNEL",
    "cvf-truth-flow": "file:../CVF_TRUTH_FLOW"
  }
}
'@ | Out-File -LiteralPath (Join-Path $cvfWebRoot 'package.json') -Encoding utf8

    @"
const MODULES = [
    { id: 'cvf-refinery', name: 'CVF Refinery' },
    { id: 'cvf-truth-kernel', name: 'CVF Truth Kernel' },
    { id: 'cvf-truth-flow', name: 'CVF Truth Flow' },
];
"@ | Out-File -LiteralPath (Join-Path $cvfWebRoot 'src\lib\server\runtime-modules.ts') -Encoding utf8

    & git -C $cvfWebRoot add -A *>$null
    & git -C $cvfWebRoot commit -q -m 'proof cvf-web fixture' *>$null

    Assert-True ((& git -C $provRoot status --porcelain) -join '' -eq '') 'fixture_provenance_clean_after_seed' 'provenance fixture not clean after seeding'
    Assert-True ((& git -C $pubRoot status --porcelain) -join '' -eq '') 'fixture_public_sync_clean_after_seed' 'public-sync fixture not clean after seeding'
    Assert-True ((& git -C $cvfWebRoot status --porcelain) -join '' -eq '') 'fixture_cvfweb_clean_after_seed' 'cvf-web fixture not clean after seeding'

    # -----------------------------------------------------------------
    # Capture before-snapshot for all three roots.
    # -----------------------------------------------------------------
    $provBefore = Get-RootSnapshot -RootPath $provRoot
    $pubBefore = Get-RootSnapshot -RootPath $pubRoot
    $cvfWebBefore = Get-RootSnapshot -RootPath $cvfWebRoot

    # -----------------------------------------------------------------
    # Invoke the committed mapper twice using the committed policy file.
    # -----------------------------------------------------------------
    $tempReceiptPath1 = Join-Path $receiptOutputDir 'proof_receipt_run1.json'
    $tempReceiptPath2 = Join-Path $receiptOutputDir 'proof_receipt_run2.json'

    $run1 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath $tempReceiptPath1 -WorkingDirectory $receiptOutputDir
    Assert-True ($run1.ExitCode -eq 0) 'mapper_run_one_exit_zero' $run1.StdoutText

    $run2 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath $tempReceiptPath2 -WorkingDirectory $receiptOutputDir
    Assert-True ($run2.ExitCode -eq 0) 'mapper_run_two_exit_zero' $run2.StdoutText

    # -----------------------------------------------------------------
    # Determinism: byte-identical stdout and receipt ID across both runs.
    # -----------------------------------------------------------------
    Assert-True ($run1.StdoutText -eq $run2.StdoutText) 'deterministic_two_runs_byte_identical' 'stdout differed between the two proof runs'
    Assert-True ($run1.Json.receiptId -and $run1.Json.receiptId -eq $run2.Json.receiptId) 'deterministic_two_runs_receipt_id_stable' 'receiptId differed or was empty'

    # -----------------------------------------------------------------
    # Schema/parity/error/count validation on the second run's receipt.
    # -----------------------------------------------------------------
    $receipt = $run2.Json
    Assert-True ($receipt.schemaVersion -eq '1.0.0') 'receipt_schema_version_is_1_0_0' "found: $($receipt.schemaVersion)"
    Assert-True ($receipt.sourceRoot -eq 'PROVENANCE_ROOT' -and $receipt.targetRoot -eq 'PUBLIC_SYNC_ROOT' -and $receipt.cvfWebRoot -eq 'CVF_WEB_ROOT') 'receipt_root_labels_are_fixed_literals' 'root labels are not the fixed literal set'
    Assert-True ($receipt.rootsValidated.provenance -eq 'PASS' -and $receipt.rootsValidated.publicSync -eq 'PASS') 'receipt_roots_validated_pass' 'rootsValidated is not both PASS'

    $parityProps = @($receipt.policyParity.PSObject.Properties)
    $parityAllMatch = ($parityProps.Count -gt 0) -and (@($parityProps | Where-Object { $_.Value -ne 'MATCH' }).Count -eq 0)
    Assert-True $parityAllMatch 'receipt_all_nine_parity_values_match' ($receipt.policyParity | ConvertTo-Json -Compress)
    Assert-True ($parityProps.Count -eq 9) 'receipt_parity_has_nine_groups' "found $($parityProps.Count) groups"

    Assert-True (@($receipt.errors).Count -eq 0) 'receipt_zero_errors' ($receipt.errors | ConvertTo-Json -Compress)

    $candidates = @($receipt.candidates)
    $reconTotal = $receipt.summary.copyCandidateAbsentCount + $receipt.summary.semanticReviewFlagCount + $receipt.summary.skipUnchangedCount + $receipt.summary.deniedPathCount + $receipt.summary.notAllowlistedCount
    Assert-True ($reconTotal -eq $receipt.summary.totalCandidates) 'receipt_count_reconciliation' "sum=$reconTotal total=$($receipt.summary.totalCandidates)"
    Assert-True ($receipt.summary.reconciliationMatch -eq $true) 'receipt_reconciliation_match_true' "found: $($receipt.summary.reconciliationMatch)"
    Assert-True ($receipt.summary.totalCandidates -eq $candidates.Count) 'receipt_total_candidates_matches_array_length' "summary=$($receipt.summary.totalCandidates) array=$($candidates.Count)"

    # -----------------------------------------------------------------
    # Candidate action coverage: absent, changed, unchanged, denied,
    # not-allowlisted, mapped export.
    # -----------------------------------------------------------------
    Assert-True (@($candidates | Where-Object { $_.candidateAction -eq 'COPY_CANDIDATE_ABSENT_TARGET' }).Count -ge 1) 'proof_covers_absent_target' 'no COPY_CANDIDATE_ABSENT_TARGET row found'
    Assert-True (@($candidates | Where-Object { $_.candidateAction -eq 'FLAG_SEMANTIC_REVIEW_CHANGED' }).Count -ge 1) 'proof_covers_changed_semantic_review' 'no FLAG_SEMANTIC_REVIEW_CHANGED row found'
    Assert-True (@($candidates | Where-Object { $_.candidateAction -eq 'SKIP_UNCHANGED' }).Count -ge 1) 'proof_covers_unchanged_skip' 'no SKIP_UNCHANGED row found'
    Assert-True (@($candidates | Where-Object { $_.candidateAction -eq 'SKIP_DENIED' }).Count -ge 1) 'proof_covers_denied' 'no SKIP_DENIED row found'
    Assert-True (@($candidates | Where-Object { $_.candidateAction -eq 'SKIP_NOT_ALLOWLISTED' }).Count -ge 1) 'proof_covers_not_allowlisted' 'no SKIP_NOT_ALLOWLISTED row found'
    Assert-True (@($candidates | Where-Object { $_.matchedAllowlistRule -eq 'mappedFiles' }).Count -ge 1) 'proof_covers_mapped_export' 'no mappedFiles-matched row found'

    # -----------------------------------------------------------------
    # SOT3 registry observation: all three current entries observed.
    # -----------------------------------------------------------------
    $sot3Rows = @($receipt.cvfWebObservation.sot3ObservedEntries)
    Assert-True ($sot3Rows.Count -eq 3) 'proof_sot3_observed_three_entries' "found $($sot3Rows.Count)"
    $allThreePresent = (@($sot3Rows | Where-Object { $_.presentInDependencies -and $_.presentInRegistry }).Count -eq 3)
    Assert-True $allThreePresent 'proof_sot3_all_three_present' ($sot3Rows | ConvertTo-Json -Compress)

    # -----------------------------------------------------------------
    # Containment-count reconciliation: pathEscapeChecksRun equals
    # candidate count plus one (for the receipt path itself).
    # -----------------------------------------------------------------
    Assert-True ($receipt.pathEscapeChecksRun -eq ($candidates.Count + 1)) 'receipt_path_escape_checks_reconcile' "found $($receipt.pathEscapeChecksRun) expected $($candidates.Count + 1)"

    # -----------------------------------------------------------------
    # No BOM in the written receipt file.
    # -----------------------------------------------------------------
    $receiptBytes = [System.IO.File]::ReadAllBytes($tempReceiptPath2)
    $hasBom = ($receiptBytes.Length -ge 3 -and $receiptBytes[0] -eq 0xEF -and $receiptBytes[1] -eq 0xBB -and $receiptBytes[2] -eq 0xBF)
    Assert-True (-not $hasBom) 'receipt_file_has_no_bom' 'receipt file starts with a UTF-8 BOM'

    # -----------------------------------------------------------------
    # No secret-like fixture content emitted (the .env.local file's
    # content, not just its path, must never appear).
    # -----------------------------------------------------------------
    Assert-True ($run2.StdoutText -notmatch 'secret content') 'receipt_no_secret_like_content_emitted' 'secret-like fixture content leaked into receipt'

    # -----------------------------------------------------------------
    # Real repository roots were never used as proof targets: confirm
    # neither mapper invocation referenced the real repo root path.
    # -----------------------------------------------------------------
    Assert-True ($tempRoot.StartsWith($env:TEMP, [System.StringComparison]::OrdinalIgnoreCase)) 'proof_fixture_root_is_under_temp' 'temp parent is not under $env:TEMP'
    Assert-True (-not $provRoot.StartsWith($repoRoot, [System.StringComparison]::OrdinalIgnoreCase)) 'proof_provenance_fixture_is_not_real_repo_root' 'provenance fixture path overlaps the real repository root'

    # -----------------------------------------------------------------
    # Governed proof receipt: written only when explicitly requested,
    # using the same second-run mapper invocation's deterministic bytes.
    # -----------------------------------------------------------------
    if ($GovernedReceiptPath) {
        $governedDir = Split-Path -Parent $GovernedReceiptPath
        $governedFileName = Split-Path -Leaf $GovernedReceiptPath
        $governedRun = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath $governedFileName -WorkingDirectory $governedDir
        Assert-True ($governedRun.ExitCode -eq 0) 'governed_proof_receipt_generated' $governedRun.StdoutText
        Assert-True (Test-Path -LiteralPath $GovernedReceiptPath -PathType Leaf) 'governed_proof_receipt_path_exists' 'governed proof receipt was not written'
        Assert-True ($governedRun.Json.receiptId -eq $run2.Json.receiptId) 'governed_proof_receipt_id_matches_proof_runs' "governed=$($governedRun.Json.receiptId) proof=$($run2.Json.receiptId)"
        $governedBytes = [System.IO.File]::ReadAllBytes((Resolve-Path -LiteralPath $GovernedReceiptPath).ProviderPath)
        Assert-True ([System.Linq.Enumerable]::SequenceEqual([byte[]]$receiptBytes, [byte[]]$governedBytes)) 'governed_proof_receipt_bytes_match_proof_runs' 'governed receipt bytes differ from the repeated proof receipt'
    }

    # -----------------------------------------------------------------
    # After-snapshot for all three git roots. This occurs after the
    # optional governed-receipt invocation so every mapper call is covered.
    # -----------------------------------------------------------------
    $provAfter = Get-RootSnapshot -RootPath $provRoot
    $pubAfter = Get-RootSnapshot -RootPath $pubRoot
    $cvfWebAfter = Get-RootSnapshot -RootPath $cvfWebRoot

    $provCompare = Compare-RootSnapshot -Before $provBefore -After $provAfter
    $pubCompare = Compare-RootSnapshot -Before $pubBefore -After $pubAfter
    $cvfWebCompare = Compare-RootSnapshot -Before $cvfWebBefore -After $cvfWebAfter

    Assert-True $provCompare.StatusMatch 'proof_provenance_git_status_unchanged' 'provenance git status changed across mapper invocations'
    Assert-True $provCompare.FilesMatch 'proof_provenance_file_inventory_unchanged' 'provenance file inventory changed across mapper invocations'
    Assert-True $pubCompare.StatusMatch 'proof_public_sync_git_status_unchanged' 'public-sync git status changed across mapper invocations'
    Assert-True $pubCompare.FilesMatch 'proof_public_sync_file_inventory_unchanged' 'public-sync file inventory changed across mapper invocations'
    Assert-True $cvfWebCompare.StatusMatch 'proof_cvfweb_git_status_unchanged' 'cvf-web git status changed across mapper invocations'
    Assert-True $cvfWebCompare.FilesMatch 'proof_cvfweb_file_inventory_unchanged' 'cvf-web file inventory changed across mapper invocations'

    # Exercise the same cleanup helper on a normal path, then force an early
    # child-process failure and prove its finally block removes its temp root.
    $successCleanupRoot = Join-Path $env:TEMP "cvf_cleanup_success_$proofRunId"
    New-Item -ItemType Directory -Path $successCleanupRoot -Force | Out-Null
    Remove-ProofTempRoot -Path $successCleanupRoot
    Assert-True (-not (Test-Path -LiteralPath $successCleanupRoot)) 'cleanup_success_path_removes_temp_parent' 'normal cleanup helper left its temp parent behind'

    $failureCleanupRoot = Join-Path $env:TEMP "cvf_cleanup_failure_$proofRunId"
    $failurePsi = [System.Diagnostics.ProcessStartInfo]::new()
    $failurePsi.FileName = 'powershell.exe'
    $failurePsi.UseShellExecute = $false
    $failurePsi.RedirectStandardOutput = $true
    $failurePsi.RedirectStandardError = $true
    $failurePsi.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`" -CleanupFailureSelfTestChild -CleanupFailureSelfTestRoot `"$failureCleanupRoot`""
    $failureProcess = [System.Diagnostics.Process]::Start($failurePsi)
    $failureStdout = $failureProcess.StandardOutput.ReadToEnd()
    $failureStderr = $failureProcess.StandardError.ReadToEnd()
    $failureProcess.WaitForExit()
    Assert-True ($failureProcess.ExitCode -ne 0) 'cleanup_failure_path_self_test_exits_nonzero' ($failureStdout + $failureStderr)
    Assert-True (-not (Test-Path -LiteralPath $failureCleanupRoot)) 'cleanup_failure_path_removes_temp_parent' 'forced-failure child left its temp parent behind'

    # -----------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------
    Write-Host ''
    Write-Host '=== CVF Projection Automation T2 Three-Root Proof ===' -ForegroundColor Cyan
    $script:results | ForEach-Object {
        if ($_ -like 'PASS:*') { Write-Host $_ -ForegroundColor Green } else { Write-Host $_ -ForegroundColor Red }
    }
    Write-Host ''
    Write-Host "TOTAL: $($script:passCount + $script:failCount)  PASS: $($script:passCount)  FAIL: $($script:failCount)" -ForegroundColor Cyan

    if ($script:failCount -gt 0) {
        exit 1
    }
    exit 0
} finally {
    Remove-ProofTempRoot -Path $tempRoot
}
