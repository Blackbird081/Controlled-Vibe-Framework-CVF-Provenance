<#
.SYNOPSIS
    CVF Continuous Projection T2 disposable-fixture proof suite for
    scripts\get_cvf_projection_review_packet.ps1.

.DESCRIPTION
    Self-contained PowerShell test runner. It builds disposable fixture drift
    receipts under $env:TEMP, and for one reused-accepted-receipt case it runs
    the unmodified accepted drift receipt script
    (scripts\get_cvf_projection_drift_receipt.ps1) with a stub mapper against
    disposable temp roots. It never touches the real provenance or public-sync
    roots and cleans its own temp area in a `finally` block. It asserts the
    drafter's frozen stdout-only ordered-JSON contract: exact top-level field
    order, the five review content groups, the disposition-to-action mapping,
    determinism, fail-closed negative cases, and the absence of any
    output-path/apply/copy mode. It returns nonzero on any failed assertion.

    Run: powershell -NoProfile -ExecutionPolicy Bypass -File scripts\test_cvf_projection_review_packet.ps1
#>

[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$drafterPath = Join-Path $scriptRoot 'get_cvf_projection_review_packet.ps1'
$driftReceiptPath = Join-Path $scriptRoot 'get_cvf_projection_drift_receipt.ps1'

$testRunId = [guid]::NewGuid().ToString('N').Substring(0, 8)
$tempRoot = Join-Path $env:TEMP "cvf_review_packet_test_$testRunId"

$script:passCount = 0
$script:failCount = 0
$script:results = [System.Collections.Generic.List[string]]::new()
$script:caseIndex = 0

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

function New-ReceiptRow {
    param([string]$Surface, [string]$Disposition, [string]$Note = $null,
        [string[]]$Audience = @('developer'))
    return [ordered]@{
        surface          = $Surface
        semanticOwner    = "owner of $Surface"
        projectionTarget = "target of $Surface"
        evidenceClass    = 'source'
        audience         = $Audience
        driftDisposition = $Disposition
        sourceHash       = $null
        targetHash       = $null
        reviewerNote     = $Note
    }
}

function New-FixtureReceiptObject {
    <# Builds a 16-row receipt object covering all five supported dispositions
       plus both excluded dispositions, matching the frozen drift-receipt
       output schema. #>
    return [ordered]@{
        receiptId         = 'FIXTURE_RECEIPT_ID_0001'
        schemaVersion     = '1.0.0'
        rootsObserved     = [ordered]@{ provenance = 'PASS'; publicSync = 'PASS'; cvfWeb = 'PASS' }
        rows              = @(
            (New-ReceiptRow 'mapped:AGENTS.md' 'MISSING_TARGET'),
            (New-ReceiptRow 'mapped:public-core-continuation' 'STALE_TARGET'),
            (New-ReceiptRow 'mapped:scripts/install_cvf_workspace_root_wrappers.ps1' 'CURRENT'),
            (New-ReceiptRow 'allowedRootFiles:byte-identical-eight' 'CURRENT'),
            (New-ReceiptRow 'allowedRootFiles:target-only-six' 'SOURCE_AUTHORITY_BLOCKED'),
            (New-ReceiptRow 'denied:docs/baselines' 'SEMANTIC_REVIEW_REQUIRED' 'triage note'),
            (New-ReceiptRow 'denied:docs/reviews' 'SEMANTIC_REVIEW_REQUIRED' 'triage note'),
            (New-ReceiptRow 'denied:docs/roadmaps' 'SEMANTIC_REVIEW_REQUIRED' 'triage note'),
            (New-ReceiptRow 'denied:root-agent-handoffs' 'SEMANTIC_REVIEW_REQUIRED' 'triage note'),
            (New-ReceiptRow 'allowedTrees' 'SEMANTIC_REVIEW_REQUIRED' 'triage note'),
            (New-ReceiptRow 'allowedDocsPaths' 'SEMANTIC_REVIEW_REQUIRED' 'triage note'),
            (New-ReceiptRow 'denyPatterns' 'CURRENT'),
            (New-ReceiptRow 'cvfWeb:sot3-parity' 'CURRENT'),
            (New-ReceiptRow 'policy:sync-parity' 'CURRENT'),
            (New-ReceiptRow 'manual:technical-product-catalog' 'NOT_APPLICABLE_WITH_REASON'),
            (New-ReceiptRow 'presentation:README' 'AUDIENCE_PRESENTATION_RISK' 'audience note')
        )
        publicTargetState = [ordered]@{
            trackedDeniedPaths  = @()
            trackedDeniedCount  = 0
            ignoredResiduePaths = @()
            ignoredResidueCount = 0
        }
        summary           = [ordered]@{
            rowCount            = 16
            byDisposition       = [ordered]@{ CURRENT = 5 }
            reconciliationMatch = $true
        }
        mapperReceiptId   = 'FIXTURE_MAPPER_RECEIPT_ID_0001'
        noTargetWriteConfirmation = 'CONFIRMED_NO_TARGET_WRITE: fixture receipt, zero filesystem writes.'
        errors            = @()
    }
}

function Write-ReceiptFixture {
    param([object]$Receipt, [string]$Path)
    $json = $Receipt | ConvertTo-Json -Depth 40
    [System.IO.File]::WriteAllText($Path, $json, [System.Text.UTF8Encoding]::new($false))
}

function Invoke-Drafter {
    <# Runs the drafter as a child process via the call operator (which quotes
       space-containing paths correctly) and captures stdout and stderr as two
       separate streams, so a fail-closed run's empty stdout can be asserted
       independently of its stderr diagnostic. #>
    param([string[]]$DrafterArgs)
    $script:caseIndex++
    $errFile = Join-Path $tempRoot "stderr_$($script:caseIndex).txt"
    $prevPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $stdoutLines = & powershell -NoProfile -ExecutionPolicy Bypass -File $drafterPath @DrafterArgs 2>$errFile
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $prevPreference
    }
    $stdout = ($stdoutLines | Out-String -Width 8192)
    $stderr = if (Test-Path -LiteralPath $errFile) { [System.IO.File]::ReadAllText($errFile) } else { '' }
    $json = $null
    if ($stdout.Trim()) { try { $json = $stdout | ConvertFrom-Json } catch { $json = $null } }
    return [pscustomobject]@{
        ExitCode = $exitCode
        Stdout   = $stdout
        Stderr   = $stderr
        Json     = $json
    }
}

try {
    New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

    # -----------------------------------------------------------------
    # Case 1: valid fixture receipt drafts a complete, ordered packet
    # -----------------------------------------------------------------
    $validReceipt = Join-Path $tempRoot 'valid_receipt.json'
    Write-ReceiptFixture -Receipt (New-FixtureReceiptObject) -Path $validReceipt
    $run1 = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $validReceipt)
    Assert-True ($run1.ExitCode -eq 0) 'valid_receipt_exit_zero' $run1.Stderr
    Assert-True ($null -ne $run1.Json) 'valid_receipt_json_parses' $run1.Stdout
    $expectedOrder = @('schemaVersion', 'draftStatus', 'authorizesDecision', 'sourceFacts',
        'affectedProjections', 'recommendedReviewerActions', 'publicProvenanceBoundary',
        'evidence', 'claimBoundary', 'draftId')
    $actualOrder = @($run1.Json.PSObject.Properties.Name)
    Assert-True (($actualOrder -join ',') -eq ($expectedOrder -join ',')) 'top_level_field_order_exact' ($actualOrder -join ',')
    Assert-True ($run1.Json.schemaVersion -eq '1.0.0') 'schema_version_constant' $run1.Json.schemaVersion
    Assert-True ($run1.Json.draftStatus -eq 'REVIEW_REQUIRED_UNCOMMITTED') 'draftStatus_review_required_uncommitted' $run1.Json.draftStatus
    Assert-True ($run1.Json.authorizesDecision -eq $false) 'authorizes_decision_false' "$($run1.Json.authorizesDecision)"
    Assert-True ($run1.Json.claimBoundary -eq 'DRAFT_ONLY_REVIEWER_DECISION_REQUIRED_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION') 'claim_boundary_literal_exact' $run1.Json.claimBoundary
    Assert-True ($run1.Json.draftId -match '^[0-9A-F]{64}$') 'draft_id_upper_sha256' $run1.Json.draftId

    # -----------------------------------------------------------------
    # Case 2: five content groups present with exact field shapes
    # -----------------------------------------------------------------
    $sf = @($run1.Json.sourceFacts.PSObject.Properties.Name)
    $expectedSf = @('receiptId', 'receiptSchemaVersion', 'receiptRowCount', 'reconciliationMatch', 'rootsObserved', 'publicTargetState', 'noTargetWriteConfirmation')
    Assert-True (($sf -join ',') -eq ($expectedSf -join ',')) 'sourceFacts_field_shape' ($sf -join ',')
    Assert-True ($run1.Json.sourceFacts.receiptId -eq 'FIXTURE_RECEIPT_ID_0001') 'sourceFacts_receipt_id_carried' $run1.Json.sourceFacts.receiptId
    Assert-True ($run1.Json.sourceFacts.receiptRowCount -eq 16) 'sourceFacts_row_count_sixteen' "$($run1.Json.sourceFacts.receiptRowCount)"
    $ppb = @($run1.Json.publicProvenanceBoundary.PSObject.Properties.Name)
    $expectedPpb = @('sourceAuthority', 'observedTarget', 'publicMutationAuthorized', 'applyOrCopyAuthorized', 'autoApproveAuthorized', 'persistence')
    Assert-True (($ppb -join ',') -eq ($expectedPpb -join ',')) 'publicProvenanceBoundary_field_shape' ($ppb -join ',')
    Assert-True ($run1.Json.publicProvenanceBoundary.publicMutationAuthorized -eq $false -and $run1.Json.publicProvenanceBoundary.applyOrCopyAuthorized -eq $false -and $run1.Json.publicProvenanceBoundary.autoApproveAuthorized -eq $false) 'publicProvenanceBoundary_all_false' 'a boundary authorization flag was not false'
    Assert-True ($run1.Json.publicProvenanceBoundary.persistence -eq 'STDOUT_ONLY_UNCOMMITTED') 'publicProvenanceBoundary_persistence_stdout_only' $run1.Json.publicProvenanceBoundary.persistence
    $ev = @($run1.Json.evidence.PSObject.Properties.Name)
    $expectedEv = @('sourceReceiptId', 'mapperReceiptId', 'receiptNoTargetWriteConfirmation', 'receiptReconciliationMatch', 'affectedProjectionCount', 'actionCount')
    Assert-True (($ev -join ',') -eq ($expectedEv -join ',')) 'evidence_field_shape' ($ev -join ',')
    Assert-True ($run1.Json.evidence.mapperReceiptId -eq 'FIXTURE_MAPPER_RECEIPT_ID_0001') 'evidence_mapper_receipt_id_carried' $run1.Json.evidence.mapperReceiptId
    Assert-True (@($run1.Json.recommendedReviewerActions).Count -gt 0) 'recommendedReviewerActions_present' 'no actions emitted'

    # -----------------------------------------------------------------
    # Case 3: every supported disposition is mapped; excluded dispositions
    # produce no affected-projection row and no action row
    # -----------------------------------------------------------------
    $affectedSurfaces = @($run1.Json.affectedProjections | ForEach-Object { $_.surface })
    # 6 SEMANTIC_REVIEW_REQUIRED + 1 SOURCE_AUTHORITY_BLOCKED + 1 AUDIENCE_PRESENTATION_RISK
    # + 1 MISSING_TARGET + 1 STALE_TARGET = 10 affected; the 5 CURRENT and 1
    # NOT_APPLICABLE_WITH_REASON rows are excluded.
    Assert-True (@($affectedSurfaces).Count -eq 10) 'affected_projection_count_ten' "count=$(@($affectedSurfaces).Count)"
    Assert-True ($affectedSurfaces -notcontains 'mapped:scripts/install_cvf_workspace_root_wrappers.ps1' -and $affectedSurfaces -notcontains 'denyPatterns') 'current_disposition_excluded' 'a CURRENT row leaked into affected projections'
    Assert-True ($affectedSurfaces -notcontains 'manual:technical-product-catalog') 'not_applicable_disposition_excluded' 'a NOT_APPLICABLE_WITH_REASON row leaked into affected projections'
    function Get-Action([object]$Run, [string]$Surface) {
        return (@($Run.Json.recommendedReviewerActions | Where-Object { $_.surface -eq $Surface })[0]).recommendedAction
    }
    Assert-True ((Get-Action $run1 'mapped:AGENTS.md') -eq 'REVIEW_MISSING_TARGET_NO_COPY_AUTHORIZED') 'action_map_missing_target' (Get-Action $run1 'mapped:AGENTS.md')
    Assert-True ((Get-Action $run1 'mapped:public-core-continuation') -eq 'REVIEW_STALE_TARGET_DIFF_NO_APPLY_AUTHORIZED') 'action_map_stale_target' (Get-Action $run1 'mapped:public-core-continuation')
    Assert-True ((Get-Action $run1 'denied:docs/baselines') -eq 'REVIEW_SEMANTIC_OWNER_AND_TARGET') 'action_map_semantic_review' (Get-Action $run1 'denied:docs/baselines')
    Assert-True ((Get-Action $run1 'allowedRootFiles:target-only-six') -eq 'KEEP_BLOCKED_PENDING_SOURCE_AUTHORITY') 'action_map_source_authority_blocked' (Get-Action $run1 'allowedRootFiles:target-only-six')
    Assert-True ((Get-Action $run1 'presentation:README') -eq 'REVIEW_AUDIENCE_PRESENTATION') 'action_map_audience_presentation' (Get-Action $run1 'presentation:README')
    $decisionAuthorities = @($run1.Json.recommendedReviewerActions | ForEach-Object { $_.decisionAuthority } | Sort-Object -Unique)
    Assert-True (($decisionAuthorities -join ',') -eq 'REVIEWER_ONLY') 'action_decision_authority_reviewer_only' ($decisionAuthorities -join ',')
    $actionRowShape = @($run1.Json.recommendedReviewerActions[0].PSObject.Properties.Name)
    $expectedActionShape = @('surface', 'driftDisposition', 'recommendedAction', 'reviewerNote', 'decisionAuthority')
    Assert-True (($actionRowShape -join ',') -eq ($expectedActionShape -join ',')) 'action_row_field_shape' ($actionRowShape -join ',')
    $affRowShape = @($run1.Json.affectedProjections[0].PSObject.Properties.Name)
    $expectedAffShape = @('surface', 'semanticOwner', 'projectionTarget', 'evidenceClass', 'audience', 'driftDisposition', 'sourceHash', 'targetHash', 'reviewerNote')
    Assert-True (($affRowShape -join ',') -eq ($expectedAffShape -join ',')) 'affected_row_field_shape' ($affRowShape -join ',')

    # -----------------------------------------------------------------
    # Case 4: affected projections are sorted ordinally by surface
    # -----------------------------------------------------------------
    $sortedSurfaces = [string[]]@($affectedSurfaces)
    [System.Array]::Sort($sortedSurfaces, [System.StringComparer]::Ordinal)
    Assert-True (($affectedSurfaces -join "`n") -eq ($sortedSurfaces -join "`n")) 'affected_projections_sorted_ordinally_by_surface' ($affectedSurfaces -join ',')

    # -----------------------------------------------------------------
    # Case 5: affected-projection/action cardinality invariant holds
    # -----------------------------------------------------------------
    Assert-True (@($run1.Json.affectedProjections).Count -eq @($run1.Json.recommendedReviewerActions).Count) 'affected_action_cardinality_matches' 'affected and action counts differ'
    Assert-True ($run1.Json.evidence.affectedProjectionCount -eq @($run1.Json.affectedProjections).Count -and $run1.Json.evidence.actionCount -eq @($run1.Json.recommendedReviewerActions).Count) 'evidence_counts_match_groups' 'evidence counts do not match emitted group sizes'

    # -----------------------------------------------------------------
    # Case 6: deterministic repeated run over the same receipt
    # -----------------------------------------------------------------
    $run1b = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $validReceipt)
    Assert-True ($run1.Stdout -eq $run1b.Stdout) 'deterministic_repeated_run_draft' 'stdout differed across repeated runs over the same receipt'
    Assert-True ($run1.Json.draftId -eq $run1b.Json.draftId) 'deterministic_repeated_run_draft_id' 'draftId differed across repeated runs'

    # -----------------------------------------------------------------
    # Case 7: stdout has no BOM and no secret-like content
    # -----------------------------------------------------------------
    $stdoutBytes = [System.Text.Encoding]::UTF8.GetBytes($run1.Stdout)
    $hasBom = $stdoutBytes.Length -ge 3 -and $stdoutBytes[0] -eq 0xEF -and $stdoutBytes[1] -eq 0xBB -and $stdoutBytes[2] -eq 0xBF
    Assert-True (-not $hasBom) 'draft_stdout_has_no_bom' 'stdout has a UTF-8 BOM'
    Assert-True ($run1.Stdout -notmatch '(?i)(api[_-]?key|secret|password|bearer\s)') 'draft_no_secret_like_content' 'possible secret-like token found'

    # -----------------------------------------------------------------
    # Case 8: fail-closed negative cases -- each emits no stdout draft and a
    # single UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT diagnostic on stderr
    # -----------------------------------------------------------------
    function Test-FailClosed {
        param([object]$ReceiptObject, [string]$CaseName)
        $path = Join-Path $tempRoot "$CaseName.json"
        Write-ReceiptFixture -Receipt $ReceiptObject -Path $path
        $run = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $path)
        Assert-True ($run.ExitCode -ne 0) "${CaseName}_nonzero_exit" "$($run.ExitCode)"
        Assert-True ([string]::IsNullOrWhiteSpace($run.Stdout)) "${CaseName}_no_stdout_draft" "stdout was not empty: $($run.Stdout)"
        Assert-True ($run.Stderr -match 'UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT') "${CaseName}_unsupported_code" $run.Stderr
        return $run
    }

    $missingTop = New-FixtureReceiptObject; $missingTop.Remove('mapperReceiptId') | Out-Null
    Test-FailClosed -ReceiptObject $missingTop -CaseName 'negative_missing_top_level_field' | Out-Null

    $missingRowField = New-FixtureReceiptObject; $missingRowField.rows[0].Remove('reviewerNote') | Out-Null
    Test-FailClosed -ReceiptObject $missingRowField -CaseName 'negative_missing_row_field' | Out-Null

    $badRowCount = New-FixtureReceiptObject; $badRowCount.rows = @($badRowCount.rows[0..14])
    Test-FailClosed -ReceiptObject $badRowCount -CaseName 'negative_row_count_not_sixteen' | Out-Null

    $nonEmptyErrors = New-FixtureReceiptObject; $nonEmptyErrors.errors = @([ordered]@{ code = 'X'; message = 'y' })
    Test-FailClosed -ReceiptObject $nonEmptyErrors -CaseName 'negative_nonempty_errors' | Out-Null

    $badReconcile = New-FixtureReceiptObject; $badReconcile.summary.reconciliationMatch = $false
    Test-FailClosed -ReceiptObject $badReconcile -CaseName 'negative_reconciliation_not_true' | Out-Null

    $badSummaryCount = New-FixtureReceiptObject; $badSummaryCount.summary.rowCount = 15
    Test-FailClosed -ReceiptObject $badSummaryCount -CaseName 'negative_summary_row_count_mismatch' | Out-Null

    $unknownDisp = New-FixtureReceiptObject; $unknownDisp.rows[0].driftDisposition = 'TOTALLY_UNKNOWN_DISPOSITION'
    $unknownRun = Test-FailClosed -ReceiptObject $unknownDisp -CaseName 'negative_unknown_disposition'
    Assert-True ($unknownRun.Stderr -match 'unknown driftDisposition') 'negative_unknown_disposition_message' $unknownRun.Stderr

    # -----------------------------------------------------------------
    # Case 8b: exact-enum, case-sensitive disposition validation -- a
    # lowercase variant of a canonical disposition token must fail closed
    # rather than being silently accepted via case-insensitive membership or
    # map lookup.
    # -----------------------------------------------------------------
    $lowerActionDisp = New-FixtureReceiptObject; $lowerActionDisp.rows[0].driftDisposition = 'missing_target'
    $lowerActionRun = Test-FailClosed -ReceiptObject $lowerActionDisp -CaseName 'negative_lowercase_action_disposition_fails_closed'
    Assert-True ($lowerActionRun.Stderr -match 'unknown driftDisposition') 'negative_lowercase_action_disposition_message' $lowerActionRun.Stderr

    $lowerExcludedDisp = New-FixtureReceiptObject; $lowerExcludedDisp.rows[2].driftDisposition = 'current'
    $lowerExcludedRun = Test-FailClosed -ReceiptObject $lowerExcludedDisp -CaseName 'negative_lowercase_excluded_disposition_fails_closed'
    Assert-True ($lowerExcludedRun.Stderr -match 'unknown driftDisposition') 'negative_lowercase_excluded_disposition_message' $lowerExcludedRun.Stderr

    # -----------------------------------------------------------------
    # Case 8c: summary.reconciliationMatch must be an actual JSON boolean
    # true -- a JSON string "true" or a JSON number 1 must fail closed
    # instead of being accepted through PowerShell's -eq/-ne type coercion.
    # -----------------------------------------------------------------
    $reconStringTrue = New-FixtureReceiptObject; $reconStringTrue.summary.reconciliationMatch = 'true'
    $reconStringRun = Test-FailClosed -ReceiptObject $reconStringTrue -CaseName 'negative_reconciliation_match_string_true'
    Assert-True ($reconStringRun.Stderr -match 'reconciliationMatch') 'negative_reconciliation_match_string_true_message' $reconStringRun.Stderr

    $reconNumericOne = New-FixtureReceiptObject; $reconNumericOne.summary.reconciliationMatch = 1
    $reconNumericRun = Test-FailClosed -ReceiptObject $reconNumericOne -CaseName 'negative_reconciliation_match_numeric_one'
    Assert-True ($reconNumericRun.Stderr -match 'reconciliationMatch') 'negative_reconciliation_match_numeric_one_message' $reconNumericRun.Stderr

    # -----------------------------------------------------------------
    # Case 8d: affected-surface/action cardinality integrity mismatch -- a
    # receipt that retains exactly 16 rows but reports the same affected
    # surface twice (a legitimate malformed-receipt condition, not a
    # test-only runtime switch) must fail closed as a cardinality/identity
    # integrity violation.
    # -----------------------------------------------------------------
    $dupSurfaceReceipt = New-FixtureReceiptObject
    $dupSurfaceReceipt.rows[6].surface = $dupSurfaceReceipt.rows[5].surface
    $dupSurfaceRun = Test-FailClosed -ReceiptObject $dupSurfaceReceipt -CaseName 'negative_affected_surface_cardinality_duplicate'
    Assert-True ($dupSurfaceRun.Stderr -match 'cardinality') 'negative_affected_surface_cardinality_duplicate_message' $dupSurfaceRun.Stderr
    Assert-True (@($dupSurfaceReceipt.rows).Count -eq 16) 'negative_affected_surface_cardinality_duplicate_row_count_still_sixteen' "$(@($dupSurfaceReceipt.rows).Count)"

    # -----------------------------------------------------------------
    # Case 9: not-valid-JSON receipt and missing receipt file fail closed
    # -----------------------------------------------------------------
    $badJsonPath = Join-Path $tempRoot 'not_json.json'
    [System.IO.File]::WriteAllText($badJsonPath, 'this is not json {', [System.Text.UTF8Encoding]::new($false))
    $runBadJson = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $badJsonPath)
    Assert-True ($runBadJson.ExitCode -ne 0 -and [string]::IsNullOrWhiteSpace($runBadJson.Stdout) -and $runBadJson.Stderr -match 'UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT') 'negative_unparseable_json_fail_closed' $runBadJson.Stderr
    $runMissing = Invoke-Drafter -DrafterArgs @('-ReceiptPath', (Join-Path $tempRoot 'does_not_exist.json'))
    Assert-True ($runMissing.ExitCode -ne 0 -and [string]::IsNullOrWhiteSpace($runMissing.Stdout) -and $runMissing.Stderr -match 'UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT') 'negative_missing_receipt_file_fail_closed' $runMissing.Stderr

    # -----------------------------------------------------------------
    # Case 10: an attempted output-path/apply/copy parameter is rejected
    # (the drafter declares only -ReceiptPath, so binding fails nonzero)
    # -----------------------------------------------------------------
    $runOutputPath = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $validReceipt, '-OutputPath', (Join-Path $tempRoot 'should_not_write.json'))
    Assert-True ($runOutputPath.ExitCode -ne 0) 'attempted_output_path_parameter_rejected' "$($runOutputPath.ExitCode)"
    Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot 'should_not_write.json'))) 'attempted_output_path_wrote_no_file' 'a file was written for a rejected output-path parameter'
    $runApply = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $validReceipt, '-Apply')
    Assert-True ($runApply.ExitCode -ne 0) 'attempted_apply_parameter_rejected' "$($runApply.ExitCode)"

    # -----------------------------------------------------------------
    # Case 11: no apply/copy/output mode in the drafter source, and the
    # drafter writes no file (draft goes to stdout only)
    # -----------------------------------------------------------------
    $drafterSource = Get-Content -LiteralPath $drafterPath -Raw -Encoding utf8
    $forbiddenTokens = @('Copy-Item', 'Move-Item', 'Set-Content', 'Out-File', 'WriteAllText', 'WriteAllBytes', '\[Parameter.*\]\s*\[string\]\$OutputPath', 'param\([^)]*OutputPath')
    $foundForbidden = @($forbiddenTokens | Where-Object { $drafterSource -match $_ })
    Assert-True (@($foundForbidden).Count -eq 0) 'no_apply_copy_mode_in_source' ($foundForbidden -join ',')
    Assert-True ($drafterSource -notmatch 'CLAUDE\.md') 'provider_specific_memory_not_used_as_authority' 'provider-specific memory reference found in drafter source'
    $workDir = Join-Path $tempRoot 'writecheck'
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null
    $filesBefore = @(Get-ChildItem -LiteralPath $workDir -Recurse -File | ForEach-Object { $_.FullName })
    $prevLoc = Get-Location
    Set-Location $workDir
    try { Invoke-Drafter -DrafterArgs @('-ReceiptPath', $validReceipt) | Out-Null } finally { Set-Location $prevLoc }
    $filesAfter = @(Get-ChildItem -LiteralPath $workDir -Recurse -File | ForEach-Object { $_.FullName })
    Assert-True (@($filesAfter).Count -eq @($filesBefore).Count) 'drafter_writes_no_file' "before=$(@($filesBefore).Count) after=$(@($filesAfter).Count)"

    # -----------------------------------------------------------------
    # Case 12: reused accepted receipt -- the unmodified accepted drift
    # receipt script (run with a stub mapper over disposable temp roots,
    # never a real-root scan) produces a receipt the drafter consumes
    # -----------------------------------------------------------------
    $reuseParent = Join-Path $tempRoot 'reuse'
    $prov = Join-Path $reuseParent 'provenance'
    $pub = Join-Path $reuseParent 'public-sync'
    $web = Join-Path $reuseParent 'cvf-web'
    New-Item -ItemType Directory -Path $prov -Force | Out-Null
    New-Item -ItemType Directory -Path $pub -Force | Out-Null
    New-Item -ItemType Directory -Path $web -Force | Out-Null
    $policyFixture = Join-Path $reuseParent 'policy.json'
    [System.IO.File]::WriteAllText($policyFixture, '{}', [System.Text.UTF8Encoding]::new($false))
    $stubMapper = Join-Path $reuseParent 'stub_mapper.ps1'
    @'
param([string]$ProvenanceRoot,[string]$PublicSyncRoot,[string]$CvfWebRoot,[string]$PolicyPath)
$receipt = [ordered]@{
    receiptId = 'reused-accepted-mapper-receipt'
    rootsValidated = [ordered]@{ provenance = 'PASS'; publicSync = 'PASS'; cvfWeb = 'PASS' }
    candidates = @()
}
Write-Output ($receipt | ConvertTo-Json -Depth 10)
exit 0
'@ | Out-File -FilePath $stubMapper -Encoding utf8

    $reuseReceiptPath = Join-Path $reuseParent 'reused_receipt.json'
    $driftArgs = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $driftReceiptPath,
        '-ProvenanceRoot', $prov, '-PublicSyncRoot', $pub, '-CvfWebRoot', $web,
        '-PolicyPath', $policyFixture, '-MapperPath', $stubMapper)
    $driftOut = & powershell @driftArgs
    $driftExit = $LASTEXITCODE
    $driftText = ($driftOut -join "`n")
    [System.IO.File]::WriteAllText($reuseReceiptPath, $driftText, [System.Text.UTF8Encoding]::new($false))
    Assert-True ($driftExit -eq 0) 'reused_accepted_receipt_produced' $driftText
    $reuseRun = Invoke-Drafter -DrafterArgs @('-ReceiptPath', $reuseReceiptPath)
    Assert-True ($reuseRun.ExitCode -eq 0) 'reused_accepted_receipt_drafts_ok' $reuseRun.Stderr
    Assert-True ($null -ne $reuseRun.Json -and $reuseRun.Json.draftStatus -eq 'REVIEW_REQUIRED_UNCOMMITTED') 'reused_accepted_receipt_review_required' $reuseRun.Stdout
    Assert-True ((@($reuseRun.Json.PSObject.Properties.Name) -join ',') -eq ($expectedOrder -join ',')) 'reused_accepted_receipt_field_order' (@($reuseRun.Json.PSObject.Properties.Name) -join ',')
    Assert-True (@($reuseRun.Json.affectedProjections).Count -eq @($reuseRun.Json.recommendedReviewerActions).Count) 'reused_accepted_receipt_cardinality_matches' 'reused receipt affected/action mismatch'

    $total = $script:passCount + $script:failCount
    Write-Output ''
    Write-Output '=== CVF Continuous Projection T2 Review-Packet Drafter Proof Suite ==='
    $script:results | ForEach-Object { Write-Output $_ }
    Write-Output ''
    Write-Output "Total: $total, Pass: $($script:passCount), Fail: $($script:failCount)"

    if ($script:failCount -gt 0) { exit 1 } else { exit 0 }
} finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
