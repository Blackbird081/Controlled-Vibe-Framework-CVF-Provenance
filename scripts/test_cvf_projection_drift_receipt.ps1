<#
.SYNOPSIS
    CVF Continuous Projection T1 disposable-fixture proof suite for
    scripts\get_cvf_projection_drift_receipt.ps1.

.DESCRIPTION
    Self-contained PowerShell test runner. It builds temporary disposable git
    repositories under $env:TEMP for every case, never touches the real
    provenance or public-sync roots, and cleans its own temp area in a
    `finally` block. It returns nonzero on any failed assertion.

    Run: powershell -NoProfile -ExecutionPolicy Bypass -File scripts\test_cvf_projection_drift_receipt.ps1
#>

[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$driftReceiptPath = Join-Path $scriptRoot 'get_cvf_projection_drift_receipt.ps1'
$mapperPath = Join-Path $scriptRoot 'get_cvf_projection_map.ps1'

$testRunId = [guid]::NewGuid().ToString('N').Substring(0, 8)
$tempRoot = Join-Path $env:TEMP "cvf_drift_receipt_test_$testRunId"

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

function New-DisposableGitRepo {
    param([string]$Path, [string]$OriginUrl)
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
    Push-Location $Path
    try {
        & git init -q 2>&1 | Out-Null
        & git config core.autocrlf false 2>&1 | Out-Null
        & git config user.email 'test@example.invalid' 2>&1 | Out-Null
        & git config user.name 'CVF Test Fixture' 2>&1 | Out-Null
        if ($OriginUrl) {
            & git remote add origin $OriginUrl 2>&1 | Out-Null
        }
        'fixture' | Out-File -FilePath (Join-Path $Path 'README.md') -Encoding utf8
        & git add -A 2>&1 | Out-Null
        & git commit -q -m 'fixture init' 2>&1 | Out-Null
    } finally {
        Pop-Location
    }
}

function New-BasePolicyFixture {
    param([string]$PublicRemote = 'https://example.invalid/public-sync.git', [string]$ProvenanceRemote = 'https://example.invalid/provenance-marker-repo.git')
    return [pscustomobject]@{
        schemaVersion = '1.0.0'
        sourceOfTruth = [pscustomobject]@{ path = 'scripts/cvf-public-sync.ps1'; note = 'fixture' }
        expectedRemotes = [pscustomobject]@{
            provenanceRemote = $ProvenanceRemote
            publicRemote = $PublicRemote
        }
        allowedTrees = @('AllowedTree')
        allowedRootFiles = @('README.md')
        allowedScriptFiles = @()
        allowedWorkspaceTemplateFiles = @()
        allowedDocsPaths = @()
        mappedFiles = @()
        denyPatterns = @('DENY_ME')
        denyExceptions = @()
        candidateActionEnum = @('COPY_CANDIDATE_ABSENT_TARGET', 'FLAG_SEMANTIC_REVIEW_CHANGED', 'SKIP_UNCHANGED', 'SKIP_DENIED', 'SKIP_NOT_ALLOWLISTED')
        semanticReviewBoundary = [pscustomobject]@{ note = 'fixture'; autoApproveForbidden = $true }
        cvfWebObservation = [pscustomobject]@{
            packageJsonPath = 'package.json'
            runtimeModulesPath = 'runtime-modules.ts'
            expectedSot3RegistryIds = @('cvf-refinery', 'cvf-truth-kernel', 'cvf-truth-flow')
        }
    }
}

function Write-PolicyFixture {
    param([string]$Path, [pscustomobject]$Policy)
    ($Policy | ConvertTo-Json -Depth 20) | Out-File -FilePath $Path -Encoding utf8
}

function Write-SyncScriptFixture {
    <# Mirrors the accepted mapper's Get-PsArrayValues regex expectation
       (`@\((.*?)\r?\n\)`): each array needs its closing paren on its own
       line, so every element must be on its own line too. #>
    param([string]$Path, [pscustomobject]$Policy)

    function Format-PsArray([object[]]$Values) {
        # A bare '@()' (no newline before the closing paren) breaks the
        # accepted mapper's Get-PsArrayValues regex
        # ($VarName\s*=\s*@\((.*?)\r?\n\)) when two or more empty arrays
        # are declared back to back: with no '\r?\n)' inside the first
        # empty '@()', the non-greedy body match skips past it and keeps
        # consuming text until it reaches the next '\r?\n)' it can find,
        # silently absorbing the following variable declarations into the
        # first array's parsed body. Always emitting the open paren,
        # newline, and close paren on separate lines -- even for an empty
        # array -- keeps every declaration's regex match bounded to just
        # that declaration, matching how the real committed
        # scripts/cvf-public-sync.ps1 never declares two empty arrays in a
        # row without this shape.
        if (@($Values).Count -eq 0) { return "@(`r`n)" }
        $lines = @($Values | ForEach-Object { "    '$($_ -replace "'", "''")'" })
        return "@(`r`n$($lines -join ",`r`n")`r`n)"
    }

    $content = @(
        "`$PUBLIC_REMOTE = '$($Policy.expectedRemotes.publicRemote)'"
        "`$ALLOWED_TREES = $(Format-PsArray $Policy.allowedTrees)"
        "`$ALLOWED_ROOT_FILES = $(Format-PsArray $Policy.allowedRootFiles)"
        "`$ALLOWED_SCRIPT_FILES = $(Format-PsArray $Policy.allowedScriptFiles)"
        "`$ALLOWED_WORKSPACE_TEMPLATE_FILES = $(Format-PsArray $Policy.allowedWorkspaceTemplateFiles)"
        "`$ALLOWED_DOCS_PATHS = $(Format-PsArray $Policy.allowedDocsPaths)"
        "`$DENY_PATTERNS = $(Format-PsArray $Policy.denyPatterns)"
        "`$DENY_EXCEPTIONS = $(Format-PsArray $Policy.denyExceptions)"
        "`$MAPPED_FILES = @()"
    ) -join "`r`n`r`n"
    [System.IO.File]::WriteAllText($Path, $content, [System.Text.Encoding]::UTF8)
}

function New-StandardFixtureSet {
    param([string]$Parent)
    $prov = Join-Path $Parent 'provenance'
    $pub = Join-Path $Parent 'public-sync'
    $web = Join-Path $Parent 'cvf-web'

    $policy = New-BasePolicyFixture
    New-DisposableGitRepo -Path $prov -OriginUrl $policy.expectedRemotes.provenanceRemote
    New-DisposableGitRepo -Path $pub -OriginUrl $policy.expectedRemotes.publicRemote
    New-Item -ItemType Directory -Path $web -Force | Out-Null

    $scriptsDir = Join-Path $prov 'scripts'
    New-Item -ItemType Directory -Path $scriptsDir -Force | Out-Null
    $policyPath = Join-Path $scriptsDir 'cvf_projection_policy.json'
    Write-PolicyFixture -Path $policyPath -Policy $policy
    Write-SyncScriptFixture -Path (Join-Path $scriptsDir 'cvf-public-sync.ps1') -Policy $policy
    Push-Location $prov
    try { & git add -A 2>&1 | Out-Null; & git commit -q -m 'add policy fixtures' 2>&1 | Out-Null } finally { Pop-Location }

    '{}' | Out-File -FilePath (Join-Path $web 'package.json') -Encoding utf8
    New-Item -ItemType Directory -Path (Join-Path $web 'src/lib/server') -Force | Out-Null
    '// fixture' | Out-File -FilePath (Join-Path $web 'src/lib/server/runtime-modules.ts') -Encoding utf8

    return [pscustomobject]@{
        ProvenanceRoot = $prov
        PublicSyncRoot = $pub
        CvfWebRoot     = $web
        PolicyPath     = $policyPath
    }
}

function Invoke-DriftReceipt {
    param(
        [string]$ProvenanceRoot,
        [string]$PublicSyncRoot,
        [string]$CvfWebRoot,
        [string]$PolicyPath,
        [string]$ReceiptOutputPath,
        [int]$ScanTimeoutSeconds = 60,
        [string]$MapperPathOverride,
        [string]$WorkingDirectory
    )
    $argList = @(
        '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $driftReceiptPath,
        '-ProvenanceRoot', $ProvenanceRoot,
        '-PublicSyncRoot', $PublicSyncRoot,
        '-CvfWebRoot', $CvfWebRoot,
        '-PolicyPath', $PolicyPath,
        '-ScanTimeoutSeconds', $ScanTimeoutSeconds
    )
    if ($ReceiptOutputPath) { $argList += @('-ReceiptOutputPath', $ReceiptOutputPath) }
    if ($MapperPathOverride) { $argList += @('-MapperPath', $MapperPathOverride) }

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

try {
    New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

    # -----------------------------------------------------------------
    # Case 1: standard fixture set produces a valid, deterministic receipt
    # -----------------------------------------------------------------
    $set1 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case1')
    $run1a = Invoke-DriftReceipt -ProvenanceRoot $set1.ProvenanceRoot -PublicSyncRoot $set1.PublicSyncRoot -CvfWebRoot $set1.CvfWebRoot -PolicyPath $set1.PolicyPath
    Assert-True ($run1a.ExitCode -eq 0) 'standard_fixture_exit_zero' $run1a.StdoutText
    Assert-True ($null -ne $run1a.Json) 'standard_fixture_json_parses' $run1a.StdoutText
    Assert-True ($run1a.Json.rows.Count -eq 16) 'standard_fixture_row_count_sixteen' "count=$($run1a.Json.rows.Count)"
    Assert-True ($run1a.Json.summary.rowCount -eq 16) 'standard_fixture_summary_row_count' "count=$($run1a.Json.summary.rowCount)"
    Assert-True ($run1a.Json.summary.reconciliationMatch -eq $true) 'standard_fixture_reconciliation_match' ($run1a.Json.summary | ConvertTo-Json -Compress)
    Assert-True ($run1a.Json.noTargetWriteConfirmation -match '^CONFIRMED_NO_TARGET_WRITE') 'standard_fixture_no_target_write_confirmation' $run1a.Json.noTargetWriteConfirmation
    Assert-True ($null -ne $run1a.Json.receiptId -and $run1a.Json.receiptId.Length -eq 64) 'standard_fixture_receipt_id_present' "$($run1a.Json.receiptId)"
    $requiredRowFields = @('surface', 'semanticOwner', 'projectionTarget', 'evidenceClass', 'audience', 'driftDisposition', 'sourceHash', 'targetHash', 'reviewerNote')
    $rowFieldFailures = @($run1a.Json.rows | Where-Object {
        $present = @($_.PSObject.Properties.Name)
        @($requiredRowFields | Where-Object { $present -notcontains $_ }).Count -gt 0
    })
    Assert-True ($rowFieldFailures.Count -eq 0) 'schema_every_row_has_all_required_fields' "rows missing fields=$($rowFieldFailures.Count)"
    $surfaces = @($run1a.Json.rows | ForEach-Object { $_.surface })
    $sortedSurfaces = [string[]]@($surfaces)
    [System.Array]::Sort($sortedSurfaces, [System.StringComparer]::Ordinal)
    Assert-True (($surfaces -join "`n") -eq ($sortedSurfaces -join "`n")) 'schema_rows_sorted_by_surface' ($surfaces -join ',')
    $noteFailures = @($run1a.Json.rows | Where-Object {
        $_.driftDisposition -in @('SEMANTIC_REVIEW_REQUIRED', 'AUDIENCE_PRESENTATION_RISK') -and [string]::IsNullOrWhiteSpace($_.reviewerNote)
    })
    Assert-True ($noteFailures.Count -eq 0) 'schema_required_reviewer_notes_present' "rows missing note=$($noteFailures.Count)"
    $audienceOrder = @('end_user', 'developer', 'external_agent', 'reviewer')
    $audienceFailures = @($run1a.Json.rows | Where-Object {
        $actual = @($_.audience)
        $expected = @($audienceOrder | Where-Object { $actual -contains $_ })
        ($actual -join ',') -ne ($expected -join ',')
    })
    Assert-True ($audienceFailures.Count -eq 0) 'schema_audience_arrays_use_enum_order' "rows out of order=$($audienceFailures.Count)"
    Assert-True (@($run1a.Json.rows | Where-Object { $_.evidenceClass -eq 'source' }).Count -eq 14) 'frozen_contract_source_evidence_count_fourteen' 'source evidence count drifted'
    Assert-True (@($run1a.Json.rows | Where-Object { $_.evidenceClass -eq 'reviewer' }).Count -eq 2) 'frozen_contract_reviewer_evidence_count_two' 'reviewer evidence count drifted'

    # -----------------------------------------------------------------
    # Case 2: deterministic repeated run (byte-identical receiptId)
    # -----------------------------------------------------------------
    $run1b = Invoke-DriftReceipt -ProvenanceRoot $set1.ProvenanceRoot -PublicSyncRoot $set1.PublicSyncRoot -CvfWebRoot $set1.CvfWebRoot -PolicyPath $set1.PolicyPath
    Assert-True ($run1a.Json.receiptId -eq $run1b.Json.receiptId -and $run1a.Json.receiptId) 'deterministic_repeated_run_receipt_id' 'receiptId differed or empty'
    Assert-True ($run1a.StdoutText -eq $run1b.StdoutText) 'deterministic_repeated_run_byte_identical' 'stdout differed across repeated runs'

    # -----------------------------------------------------------------
    # Case 2A: mapper observations drive missing/stale/current freshness
    # without changing frozen ownership, audience, or source authority.
    # -----------------------------------------------------------------
    $signalMapperPath = Join-Path $tempRoot 'signal_mapper_stub.ps1'
    @'
param([string]$ProvenanceRoot,[string]$PublicSyncRoot,[string]$CvfWebRoot,[string]$PolicyPath)
$receipt = [ordered]@{
    receiptId = 'fixture-mapper-receipt'
    rootsValidated = [ordered]@{ provenance = 'PASS'; publicSync = 'PASS'; cvfWeb = 'PASS' }
    candidates = @(
        [ordered]@{ sourcePath = 'governance/toolkit/05_OPERATION/CVF_PUBLIC_CORE_AGENTS.md'; candidateAction = 'COPY_CANDIDATE_ABSENT_TARGET'; matchedAllowlistRule = 'mappedFiles' },
        [ordered]@{ sourcePath = 'governance/toolkit/05_OPERATION/CVF_PUBLIC_CORE_CONTINUATION.md'; candidateAction = 'FLAG_SEMANTIC_REVIEW_CHANGED'; matchedAllowlistRule = 'mappedFiles' },
        [ordered]@{ sourcePath = 'scripts/install_cvf_workspace_root_wrappers_public.ps1'; candidateAction = 'SKIP_UNCHANGED'; matchedAllowlistRule = 'mappedFiles' }
    )
}
Write-Output ($receipt | ConvertTo-Json -Depth 10)
exit 0
'@ | Out-File -FilePath $signalMapperPath -Encoding utf8
    $signalRun = Invoke-DriftReceipt -ProvenanceRoot $set1.ProvenanceRoot -PublicSyncRoot $set1.PublicSyncRoot -CvfWebRoot $set1.CvfWebRoot -PolicyPath $set1.PolicyPath -MapperPathOverride $signalMapperPath
    Assert-True ($signalRun.ExitCode -eq 0) 'mapper_signal_fixture_exit_zero' $signalRun.StdoutText
    Assert-True (($signalRun.Json.rows | Where-Object { $_.surface -eq 'mapped:AGENTS.md' }).driftDisposition -eq 'MISSING_TARGET') 'mapper_signal_missing_target_classified' 'mapped AGENTS row did not become MISSING_TARGET'
    Assert-True (($signalRun.Json.rows | Where-Object { $_.surface -eq 'mapped:public-core-continuation' }).driftDisposition -eq 'STALE_TARGET') 'mapper_signal_stale_target_classified' 'mapped continuation row did not become STALE_TARGET'
    Assert-True (($signalRun.Json.rows | Where-Object { $_.surface -eq 'mapped:scripts/install_cvf_workspace_root_wrappers.ps1' }).driftDisposition -eq 'CURRENT') 'mapper_signal_current_classified' 'mapped wrapper row did not remain CURRENT'
    Assert-True (($signalRun.Json.rows | Where-Object { $_.surface -eq 'allowedRootFiles:target-only-six' }).driftDisposition -eq 'SOURCE_AUTHORITY_BLOCKED') 'mapper_signal_target_only_block_preserved' 'target-only source authority was changed'

    # -----------------------------------------------------------------
    # Case 3: six target-only root files remain frozen SOURCE_AUTHORITY_BLOCKED
    # -----------------------------------------------------------------
    $targetOnlyRow = $run1a.Json.rows | Where-Object { $_.surface -eq 'allowedRootFiles:target-only-six' }
    Assert-True ($null -ne $targetOnlyRow) 'target_only_six_row_present' 'row missing'
    Assert-True ($targetOnlyRow.driftDisposition -eq 'SOURCE_AUTHORITY_BLOCKED') 'target_only_six_source_authority_blocked' "$($targetOnlyRow.driftDisposition)"

    # -----------------------------------------------------------------
    # Case 4: dirty provenance root fails closed, inheriting the mapper's code
    # -----------------------------------------------------------------
    $set4 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case4')
    'dirty' | Out-File -FilePath (Join-Path $set4.ProvenanceRoot 'dirty.txt') -Encoding utf8
    $run4 = Invoke-DriftReceipt -ProvenanceRoot $set4.ProvenanceRoot -PublicSyncRoot $set4.PublicSyncRoot -CvfWebRoot $set4.CvfWebRoot -PolicyPath $set4.PolicyPath
    Assert-True ($run4.ExitCode -ne 0) 'dirty_provenance_root_nonzero_exit' "$($run4.ExitCode)"
    Assert-True ($run4.Json.errors[0].code -eq 'DIRTY_PROVENANCE_ROOT') 'dirty_provenance_root_code_inherited' $run4.StdoutText
    Remove-Item -LiteralPath (Join-Path $set4.ProvenanceRoot 'dirty.txt') -Force -ErrorAction SilentlyContinue

    # -----------------------------------------------------------------
    # Case 5: dirty public-sync root fails closed, inheriting the mapper's code
    # -----------------------------------------------------------------
    $set5 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case5')
    'dirty' | Out-File -FilePath (Join-Path $set5.PublicSyncRoot 'dirty.txt') -Encoding utf8
    $run5 = Invoke-DriftReceipt -ProvenanceRoot $set5.ProvenanceRoot -PublicSyncRoot $set5.PublicSyncRoot -CvfWebRoot $set5.CvfWebRoot -PolicyPath $set5.PolicyPath
    Assert-True ($run5.ExitCode -ne 0) 'dirty_public_root_nonzero_exit' "$($run5.ExitCode)"
    Assert-True ($run5.Json.errors[0].code -eq 'DIRTY_PUBLIC_ROOT') 'dirty_public_root_code_inherited' $run5.StdoutText

    # -----------------------------------------------------------------
    # Case 6: wrong provenance remote fails closed, inheriting the mapper's code
    # -----------------------------------------------------------------
    $set6 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case6')
    Push-Location $set6.ProvenanceRoot
    try { & git remote set-url origin 'https://example.invalid/WRONG.git' 2>&1 | Out-Null } finally { Pop-Location }
    $run6 = Invoke-DriftReceipt -ProvenanceRoot $set6.ProvenanceRoot -PublicSyncRoot $set6.PublicSyncRoot -CvfWebRoot $set6.CvfWebRoot -PolicyPath $set6.PolicyPath
    Assert-True ($run6.ExitCode -ne 0) 'wrong_provenance_remote_nonzero_exit' "$($run6.ExitCode)"
    Assert-True ($run6.Json.errors[0].code -eq 'WRONG_PROVENANCE_REMOTE') 'wrong_provenance_remote_code_inherited' $run6.StdoutText

    # -----------------------------------------------------------------
    # Case 7: timeout is fail-closed -- a deliberately slow mapper stand-in
    # never scans a real repository root; it only proves the timeout path.
    # -----------------------------------------------------------------
    $slowMapperPath = Join-Path $tempRoot 'slow_mapper_stub.ps1'
    @'
param([string]$ProvenanceRoot,[string]$PublicSyncRoot,[string]$CvfWebRoot,[string]$PolicyPath,[string]$ReceiptOutputPath)
Start-Sleep -Seconds 30
Write-Output (@{ receiptId = "should-not-be-reached" } | ConvertTo-Json)
exit 0
'@ | Out-File -FilePath $slowMapperPath -Encoding utf8

    $set7 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case7')
    $timeoutStart = Get-Date
    $run7 = Invoke-DriftReceipt -ProvenanceRoot $set7.ProvenanceRoot -PublicSyncRoot $set7.PublicSyncRoot -CvfWebRoot $set7.CvfWebRoot -PolicyPath $set7.PolicyPath -ScanTimeoutSeconds 2 -MapperPathOverride $slowMapperPath
    $timeoutElapsed = (Get-Date) - $timeoutStart
    Assert-True ($run7.ExitCode -ne 0) 'timeout_nonzero_exit' "$($run7.ExitCode)"
    Assert-True ($run7.Json.errors[0].code -eq 'RECEIPT_TIMEOUT_INCONCLUSIVE') 'timeout_receipt_timeout_inconclusive_code' $run7.StdoutText
    Assert-True ($null -eq $run7.Json.receiptId) 'timeout_no_receipt_id_emitted' "$($run7.Json.receiptId)"
    Assert-True ($timeoutElapsed.TotalSeconds -lt 20) 'timeout_bounded_wall_clock' "elapsed=$($timeoutElapsed.TotalSeconds)s"
    Assert-True ($run7.Json.noTargetWriteConfirmation -match '^CONFIRMED_NO_TARGET_WRITE') 'timeout_no_target_write_confirmation_present' $run7.Json.noTargetWriteConfirmation

    # -----------------------------------------------------------------
    # Case 8: timeout never writes a receipt file
    # -----------------------------------------------------------------
    $timeoutReceiptPath = Join-Path $tempRoot 'timeout-receipt.json'
    $run8 = Invoke-DriftReceipt -ProvenanceRoot $set7.ProvenanceRoot -PublicSyncRoot $set7.PublicSyncRoot -CvfWebRoot $set7.CvfWebRoot -PolicyPath $set7.PolicyPath -ScanTimeoutSeconds 2 -MapperPathOverride $slowMapperPath -ReceiptOutputPath $timeoutReceiptPath -WorkingDirectory $tempRoot
    Assert-True ($run8.ExitCode -ne 0) 'timeout_with_receipt_path_nonzero_exit' "$($run8.ExitCode)"
    Assert-True (-not (Test-Path -LiteralPath $timeoutReceiptPath)) 'timeout_no_receipt_file_written' 'receipt file unexpectedly present after timeout'

    # -----------------------------------------------------------------
    # Case 9: tracked-versus-ignored public target state is a distinct,
    # deterministic split (never conflated into one filesystem count)
    # -----------------------------------------------------------------
    $set9 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case9')
    $baselinesDir = Join-Path $set9.PublicSyncRoot 'docs/baselines'
    New-Item -ItemType Directory -Path $baselinesDir -Force | Out-Null
    'tracked content' | Out-File -FilePath (Join-Path $baselinesDir 'tracked_one.md') -Encoding utf8
    Push-Location $set9.PublicSyncRoot
    try {
        '.gitignore does not exist yet; add ignore rule then untracked file' | Out-Null
        "docs/baselines/ignored_one.md" | Out-File -FilePath (Join-Path $set9.PublicSyncRoot '.gitignore') -Encoding utf8
        'ignored content' | Out-File -FilePath (Join-Path $baselinesDir 'ignored_one.md') -Encoding utf8
        'mapped public continuation fixture' | Out-File -FilePath (Join-Path $set9.PublicSyncRoot 'AGENT_HANDOFF.md') -Encoding utf8
        & git add -A 2>&1 | Out-Null
        & git commit -q -m 'add tracked baseline plus gitignore' 2>&1 | Out-Null
    } finally { Pop-Location }
    $run9 = Invoke-DriftReceipt -ProvenanceRoot $set9.ProvenanceRoot -PublicSyncRoot $set9.PublicSyncRoot -CvfWebRoot $set9.CvfWebRoot -PolicyPath $set9.PolicyPath
    Assert-True ($run9.ExitCode -eq 0) 'tracked_ignored_fixture_exit_zero' $run9.StdoutText
    Assert-True ($run9.Json.publicTargetState.trackedDeniedCount -eq 1) 'tracked_ignored_tracked_count_one' "$($run9.Json.publicTargetState.trackedDeniedCount)"
    Assert-True ($run9.Json.publicTargetState.ignoredResidueCount -eq 1) 'tracked_ignored_ignored_count_one' "$($run9.Json.publicTargetState.ignoredResidueCount)"
    Assert-True ($run9.Json.publicTargetState.trackedDeniedPaths -contains 'docs/baselines/tracked_one.md') 'tracked_ignored_tracked_path_correct' ($run9.Json.publicTargetState.trackedDeniedPaths -join ',')
    Assert-True ($run9.Json.publicTargetState.ignoredResiduePaths -contains 'docs/baselines/ignored_one.md') 'tracked_ignored_ignored_path_correct' ($run9.Json.publicTargetState.ignoredResiduePaths -join ',')
    Assert-True (@($run9.Json.publicTargetState.trackedDeniedPaths) -notcontains 'docs/baselines/ignored_one.md') 'tracked_ignored_no_conflation_tracked_side' 'ignored file leaked into tracked set'
    Assert-True (@($run9.Json.publicTargetState.ignoredResiduePaths) -notcontains 'docs/baselines/tracked_one.md') 'tracked_ignored_no_conflation_ignored_side' 'tracked file leaked into ignored set'
    Assert-True (@($run9.Json.publicTargetState.trackedDeniedPaths) -notcontains 'AGENT_HANDOFF.md') 'mapped_agent_handoff_exception_not_denied' 'mapped AGENT_HANDOFF.md leaked into tracked denied set'
    Assert-True (@($run9.Json.publicTargetState.ignoredResiduePaths) -notcontains 'AGENT_HANDOFF.md') 'mapped_agent_handoff_exception_not_residue' 'mapped AGENT_HANDOFF.md leaked into ignored residue set'

    # -----------------------------------------------------------------
    # Case 10: no target mutation -- provenance and public-sync git status
    # and recursive file inventories are unchanged after every invocation
    # -----------------------------------------------------------------
    $set10 = New-StandardFixtureSet -Parent (Join-Path $tempRoot 'case10')
    $provStatusBefore = & git -C $set10.ProvenanceRoot status --porcelain
    $pubStatusBefore = & git -C $set10.PublicSyncRoot status --porcelain
    $provFilesBefore = @(Get-ChildItem -LiteralPath $set10.ProvenanceRoot -Recurse -File | ForEach-Object { $_.FullName })
    $pubFilesBefore = @(Get-ChildItem -LiteralPath $set10.PublicSyncRoot -Recurse -File | ForEach-Object { $_.FullName })
    $run10 = Invoke-DriftReceipt -ProvenanceRoot $set10.ProvenanceRoot -PublicSyncRoot $set10.PublicSyncRoot -CvfWebRoot $set10.CvfWebRoot -PolicyPath $set10.PolicyPath
    $provStatusAfter = & git -C $set10.ProvenanceRoot status --porcelain
    $pubStatusAfter = & git -C $set10.PublicSyncRoot status --porcelain
    $provFilesAfter = @(Get-ChildItem -LiteralPath $set10.ProvenanceRoot -Recurse -File | ForEach-Object { $_.FullName })
    $pubFilesAfter = @(Get-ChildItem -LiteralPath $set10.PublicSyncRoot -Recurse -File | ForEach-Object { $_.FullName })
    Assert-True ($run10.ExitCode -eq 0) 'no_mutation_fixture_exit_zero' $run10.StdoutText
    Assert-True (($provStatusBefore -join "`n") -eq ($provStatusAfter -join "`n")) 'no_target_git_status_change_provenance' 'provenance git status changed'
    Assert-True (($pubStatusBefore -join "`n") -eq ($pubStatusAfter -join "`n")) 'no_target_git_status_change_public' 'public-sync git status changed'
    $provFilesDiff = Compare-Object -ReferenceObject $provFilesBefore -DifferenceObject $provFilesAfter -SyncWindow 0
    $pubFilesDiff = Compare-Object -ReferenceObject $pubFilesBefore -DifferenceObject $pubFilesAfter -SyncWindow 0
    Assert-True (@($provFilesDiff).Count -eq 0) 'no_target_filesystem_change_provenance' ($provFilesDiff | Out-String)
    Assert-True (@($pubFilesDiff).Count -eq 0) 'no_target_filesystem_change_public' ($pubFilesDiff | Out-String)

    # -----------------------------------------------------------------
    # Case 11: receipt content is secret-free and has no BOM
    # -----------------------------------------------------------------
    Assert-True ($run1a.StdoutText -notmatch '(?i)(api[_-]?key|secret|password|bearer\s)') 'receipt_no_secret_like_content_emitted' 'possible secret-like token found'
    $receiptBytes = [System.Text.Encoding]::UTF8.GetBytes($run1a.StdoutText)
    $hasBom = $receiptBytes.Length -ge 3 -and $receiptBytes[0] -eq 0xEF -and $receiptBytes[1] -eq 0xBB -and $receiptBytes[2] -eq 0xBF
    Assert-True (-not $hasBom) 'receipt_stdout_has_no_bom' 'stdout has a UTF-8 BOM'

    # -----------------------------------------------------------------
    # Case 12: no apply/copy mode -- the script source itself never invokes
    # a copy/move/write against ProvenanceRoot, PublicSyncRoot, or CvfWebRoot
    # -----------------------------------------------------------------
    $scriptSource = Get-Content -LiteralPath $driftReceiptPath -Raw -Encoding utf8
    $forbiddenTokens = @('Copy-Item', 'Move-Item', 'Set-Content', 'Out-File.*ProvenanceRoot', 'Out-File.*PublicSyncRoot')
    $foundForbidden = @($forbiddenTokens | Where-Object { $scriptSource -match $_ })
    Assert-True (@($foundForbidden).Count -eq 0) 'no_apply_copy_mode_in_source' ($foundForbidden -join ',')
    Assert-True ($scriptSource -notmatch 'CLAUDE\.md') 'provider_specific_memory_not_used_as_authority' 'provider-specific memory reference found in receipt implementation'

    $total = $script:passCount + $script:failCount
    Write-Output ''
    Write-Output "=== CVF Continuous Projection T1 Drift Receipt Proof Suite ==="
    $script:results | ForEach-Object { Write-Output $_ }
    Write-Output ''
    Write-Output "Total: $total, Pass: $($script:passCount), Fail: $($script:failCount)"

    if ($script:failCount -gt 0) { exit 1 } else { exit 0 }
} finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
