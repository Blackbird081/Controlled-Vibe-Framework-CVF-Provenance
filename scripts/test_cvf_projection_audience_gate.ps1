<#
.SYNOPSIS
    CVF Continuous Projection T3 disposable-fixture proof suite for
    scripts\get_cvf_projection_audience_gate.ps1.

.DESCRIPTION
    Self-contained PowerShell test runner. It builds disposable fixture T1
    receipt, T2 draft, and T3 audience-evidence JSON files under $env:TEMP
    and invokes the gate as a child process over those explicit file paths.
    It never touches a real provenance, public-sync, or cvf-web root, and it
    cleans its own temp area in a `finally` block. It asserts the gate's
    frozen contract: deterministic output, all seven positive rows, each
    terminal status, source-identity mismatch, missing/extra/duplicate/
    reordered/renamed assessment rows, enum casing, Boolean type errors,
    empty locators, receipt/draft contract violations, and the absence of
    any root/output/apply/copy/commit/push/browser/provider/network
    parameter. Returns nonzero on any failed assertion.

    Run: powershell -NoProfile -ExecutionPolicy Bypass -File scripts\test_cvf_projection_audience_gate.ps1
#>

[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$gatePath = Join-Path $scriptRoot 'get_cvf_projection_audience_gate.ps1'

$testRunId = [guid]::NewGuid().ToString('N').Substring(0, 8)
$tempRoot = Join-Path $env:TEMP "cvf_audience_gate_test_$testRunId"

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

function New-FixtureReceiptObject {
    param([string]$ReceiptId = 'FIXTURE_T1_RECEIPT_ID_0001')
    $rows = @(1..16 | ForEach-Object {
        [ordered]@{
            surface = "fixture-surface-$_"; semanticOwner = "fixture-owner-$_";
            projectionTarget = "fixture-target-$_"; evidenceClass = 'source';
            audience = @('reviewer'); driftDisposition = 'CURRENT';
            sourceHash = $null; targetHash = $null; reviewerNote = "fixture-note-$_"
        }
    })
    return [ordered]@{
        receiptId         = $ReceiptId
        schemaVersion     = '1.0.0'
        rootsObserved     = [ordered]@{ provenance = 'PASS'; publicSync = 'PASS'; cvfWeb = 'PASS' }
        rows              = $rows
        publicTargetState = [ordered]@{
            trackedDeniedPaths  = @()
            trackedDeniedCount  = 0
            ignoredResiduePaths = @()
            ignoredResidueCount = 0
        }
        summary           = [ordered]@{
            rowCount            = 16
            byDisposition       = [ordered]@{}
            reconciliationMatch = $true
        }
        mapperReceiptId   = 'FIXTURE_MAPPER_RECEIPT_ID_0001'
        noTargetWriteConfirmation = 'CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.'
        errors            = @()
    }
}

function New-FixtureDraftObject {
    param([string]$SourceReceiptId = 'FIXTURE_T1_RECEIPT_ID_0001')
    return [ordered]@{
        schemaVersion              = '1.0.0'
        draftStatus                = 'REVIEW_REQUIRED_UNCOMMITTED'
        authorizesDecision         = $false
        sourceFacts                = [ordered]@{
            receiptId                = $SourceReceiptId
            receiptSchemaVersion     = '1.0.0'
            receiptRowCount          = 16
            reconciliationMatch      = $true
            rootsObserved            = [ordered]@{ provenance = 'PASS'; publicSync = 'PASS'; cvfWeb = 'PASS' }
            publicTargetState        = [ordered]@{ trackedDeniedCount = 0; ignoredResidueCount = 0 }
            noTargetWriteConfirmation = 'CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.'
        }
        affectedProjections        = @()
        recommendedReviewerActions = @()
        publicProvenanceBoundary   = [ordered]@{
            sourceAuthority          = 'PROVENANCE_ROOT'
            observedTarget           = 'PUBLIC_SYNC_ROOT'
            publicMutationAuthorized = $false
            applyOrCopyAuthorized    = $false
            autoApproveAuthorized    = $false
            persistence              = 'STDOUT_ONLY_UNCOMMITTED'
        }
        evidence                    = [ordered]@{
            sourceReceiptId                = $SourceReceiptId
            mapperReceiptId                = 'FIXTURE_MAPPER_RECEIPT_ID_0001'
            receiptNoTargetWriteConfirmation = 'CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.'
            receiptReconciliationMatch     = $true
            affectedProjectionCount        = 0
            actionCount                    = 0
        }
        claimBoundary               = 'DRAFT_ONLY_REVIEWER_DECISION_REQUIRED_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION'
        draftId                      = 'FIXTURE_DRAFT_ID_0001'
    }
}

function New-AssessmentRow {
    param(
        [int]$Ordinal, [string]$Surface, [string]$Criterion, [string]$Audience,
        [string]$Status = 'PASS', [string]$Locator = $null, [string]$Observation = $null
    )
    if (-not $Locator) { $Locator = "evidence-locator-$Ordinal" }
    if (-not $Observation) { $Observation = "observation-$Ordinal" }
    return [ordered]@{
        ordinal         = $Ordinal
        surface         = $Surface
        criterion       = $Criterion
        audience        = $Audience
        status          = $Status
        evidenceLocator = $Locator
        observation     = $Observation
        reviewerOwned   = $true
    }
}

function New-FixtureAssessments {
    param([string]$OverrideStatus = $null, [int]$OverrideOrdinal = -1)
    $rows = @(
        (New-AssessmentRow 1 'public-readme' 'progressive_disclosure' 'end_user'),
        (New-AssessmentRow 2 'public-readme' 'language_clarity' 'end_user'),
        (New-AssessmentRow 3 'public-readme' 'first_action' 'end_user'),
        (New-AssessmentRow 4 'cvf-web' 'progressive_disclosure' 'end_user'),
        (New-AssessmentRow 5 'cvf-web' 'navigation_clarity' 'end_user'),
        (New-AssessmentRow 6 'cvf-web' 'developer_depth' 'developer'),
        (New-AssessmentRow 7 'external-agent-context' 'evidence_route' 'external_agent')
    )
    if ($OverrideStatus -and $OverrideOrdinal -ge 1) {
        $rows[$OverrideOrdinal - 1].status = $OverrideStatus
    }
    return $rows
}

function New-FixtureEvidenceObject {
    param([object[]]$Assessments)
    return [ordered]@{
        audienceEvidenceSchemaVersion = 'cvf.continuousProjectionAudienceEvidence.t3.v1'
        assessments                    = $Assessments
    }
}

function Write-JsonFixture {
    param([object]$Data, [string]$Path)
    $json = $Data | ConvertTo-Json -Depth 40
    [System.IO.File]::WriteAllText($Path, $json, [System.Text.UTF8Encoding]::new($false))
}

function Invoke-Gate {
    <# Runs the gate as a child process via the call operator and captures
       stdout and stderr as two separate streams. #>
    param([string[]]$GateArgs)
    $script:caseIndex++
    $errFile = Join-Path $tempRoot "stderr_$($script:caseIndex).txt"
    $prevPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $stdoutLines = & powershell -NoProfile -ExecutionPolicy Bypass -File $gatePath @GateArgs 2>$errFile
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

    $validReceiptPath = Join-Path $tempRoot 'valid_receipt.json'
    $validDraftPath = Join-Path $tempRoot 'valid_draft.json'
    Write-JsonFixture -Data (New-FixtureReceiptObject) -Path $validReceiptPath
    Write-JsonFixture -Data (New-FixtureDraftObject) -Path $validDraftPath

    # -----------------------------------------------------------------
    # Case 1: seven-row positive fixture -> gateStatus=PASS
    # -----------------------------------------------------------------
    $validEvidencePath = Join-Path $tempRoot 'valid_evidence.json'
    Write-JsonFixture -Data (New-FixtureEvidenceObject -Assessments (New-FixtureAssessments)) -Path $validEvidencePath
    $run1 = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath)
    Assert-True ($run1.ExitCode -eq 0) 'positive_fixture_exit_zero' $run1.Stderr
    Assert-True ($null -ne $run1.Json) 'positive_fixture_json_parses' $run1.Stdout
    Assert-True ($run1.Json.gateStatus -eq 'PASS') 'positive_fixture_gate_status_pass' "$($run1.Json.gateStatus)"
    Assert-True (@($run1.Json.assessments).Count -eq 7) 'positive_fixture_row_count_seven' "$(@($run1.Json.assessments).Count)"
    Assert-True ($run1.Json.authorizesMutation -eq $false) 'positive_fixture_authorizes_mutation_false' "$($run1.Json.authorizesMutation)"
    Assert-True ($run1.Json.schemaVersion -eq 'cvf.continuousProjectionAudienceGate.t3.v1') 'positive_fixture_schema_version' $run1.Json.schemaVersion
    Assert-True ($run1.Json.claimBoundary -eq 'READ_ONLY_EVIDENCE_GATE_NO_SEMANTIC_DECISION_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION') 'positive_fixture_claim_boundary_exact' $run1.Json.claimBoundary
    Assert-True (@($run1.Json.errors).Count -eq 0) 'positive_fixture_errors_empty' "$(@($run1.Json.errors).Count)"
    $expectedTopOrder = @('schemaVersion', 'gateStatus', 'sourceFreshnessStatus', 'audiencePresentationStatus', 'authorizesMutation', 'inputReceiptId', 'assessments', 'summary', 'errors', 'claimBoundary')
    $actualTopOrder = @($run1.Json.PSObject.Properties.Name)
    Assert-True (($actualTopOrder -join ',') -eq ($expectedTopOrder -join ',')) 'positive_fixture_top_level_field_order_exact' ($actualTopOrder -join ',')

    # -----------------------------------------------------------------
    # Case 2: deterministic repeated run over the same three inputs
    # -----------------------------------------------------------------
    $run1b = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath)
    Assert-True ($run1.Stdout -eq $run1b.Stdout) 'deterministic_repeated_run' 'stdout differed across repeated runs over the same inputs'

    # -----------------------------------------------------------------
    # Case 3: valid FAIL fixture -> gateStatus=FAIL
    # -----------------------------------------------------------------
    $failEvidencePath = Join-Path $tempRoot 'fail_evidence.json'
    Write-JsonFixture -Data (New-FixtureEvidenceObject -Assessments (New-FixtureAssessments -OverrideStatus 'FAIL' -OverrideOrdinal 3)) -Path $failEvidencePath
    $runFail = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $failEvidencePath)
    Assert-True ($runFail.ExitCode -eq 0) 'fail_fixture_exit_zero' $runFail.Stderr
    Assert-True ($runFail.Json.gateStatus -eq 'FAIL') 'fail_fixture_gate_status_fail' "$($runFail.Json.gateStatus)"

    # -----------------------------------------------------------------
    # Case 4: valid REVIEW_REQUIRED fixture -> gateStatus=REVIEW_REQUIRED
    # -----------------------------------------------------------------
    $reviewEvidencePath = Join-Path $tempRoot 'review_evidence.json'
    Write-JsonFixture -Data (New-FixtureEvidenceObject -Assessments (New-FixtureAssessments -OverrideStatus 'REVIEW_REQUIRED' -OverrideOrdinal 6)) -Path $reviewEvidencePath
    $runReview = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $reviewEvidencePath)
    Assert-True ($runReview.ExitCode -eq 0) 'review_required_fixture_exit_zero' $runReview.Stderr
    Assert-True ($runReview.Json.gateStatus -eq 'REVIEW_REQUIRED') 'review_required_fixture_gate_status' "$($runReview.Json.gateStatus)"

    # -----------------------------------------------------------------
    # Case 5: FAIL takes precedence over REVIEW_REQUIRED when both present
    # -----------------------------------------------------------------
    $mixedAssessments = New-FixtureAssessments -OverrideStatus 'REVIEW_REQUIRED' -OverrideOrdinal 2
    $mixedAssessments[4].status = 'FAIL'
    $mixedEvidencePath = Join-Path $tempRoot 'mixed_evidence.json'
    Write-JsonFixture -Data (New-FixtureEvidenceObject -Assessments $mixedAssessments) -Path $mixedEvidencePath
    $runMixed = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $mixedEvidencePath)
    Assert-True ($runMixed.Json.gateStatus -eq 'FAIL') 'fail_precedence_over_review_required' "$($runMixed.Json.gateStatus)"

    # -----------------------------------------------------------------
    # Fail-closed helper
    # -----------------------------------------------------------------
    function Test-FailClosed {
        param([object]$ReceiptObject, [object]$DraftObject, [object]$EvidenceObject, [string]$CaseName)
        $rPath = Join-Path $tempRoot "${CaseName}_receipt.json"
        $dPath = Join-Path $tempRoot "${CaseName}_draft.json"
        $ePath = Join-Path $tempRoot "${CaseName}_evidence.json"
        Write-JsonFixture -Data $ReceiptObject -Path $rPath
        Write-JsonFixture -Data $DraftObject -Path $dPath
        Write-JsonFixture -Data $EvidenceObject -Path $ePath
        $run = Invoke-Gate -GateArgs @('-ReceiptPath', $rPath, '-ReviewPacketPath', $dPath, '-AudienceEvidencePath', $ePath)
        Assert-True ($run.ExitCode -ne 0) "${CaseName}_nonzero_exit" "$($run.ExitCode)"
        Assert-True ([string]::IsNullOrWhiteSpace($run.Stdout)) "${CaseName}_no_stdout_success_object" "stdout was not empty: $($run.Stdout)"
        Assert-True ($run.Stderr -match 'UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE') "${CaseName}_unsupported_code" $run.Stderr
        return $run
    }

    $validReceiptObj = New-FixtureReceiptObject
    $validDraftObj = New-FixtureDraftObject
    $validAssessments = New-FixtureAssessments

    # -----------------------------------------------------------------
    # Case 6: identity mismatch -- T2 draft source receipt identity does not
    # match the T1 receipt receiptId
    # -----------------------------------------------------------------
    $mismatchedDraft = New-FixtureDraftObject -SourceReceiptId 'DOES_NOT_MATCH_T1_RECEIPT_ID'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $mismatchedDraft -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_identity_mismatch' | Out-Null

    # -----------------------------------------------------------------
    # Case 7: missing assessment row (six rows instead of seven)
    # -----------------------------------------------------------------
    $sixRows = @($validAssessments[0..5])
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $sixRows) -CaseName 'negative_missing_row' | Out-Null

    # -----------------------------------------------------------------
    # Case 8: extra assessment row (eight rows instead of seven)
    # -----------------------------------------------------------------
    $eightRows = @($validAssessments + (New-AssessmentRow 8 'extra-surface' 'extra_criterion' 'end_user'))
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $eightRows) -CaseName 'negative_extra_row' | Out-Null

    # -----------------------------------------------------------------
    # Case 9: duplicate ordinal
    # -----------------------------------------------------------------
    $dupOrdinalRows = New-FixtureAssessments
    $dupOrdinalRows[6].ordinal = 6
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $dupOrdinalRows) -CaseName 'negative_duplicate_ordinal' | Out-Null

    # -----------------------------------------------------------------
    # Case 10: reordered rows (ordinals present but shuffled positions)
    # -----------------------------------------------------------------
    $reorderedRows = New-FixtureAssessments
    $tmp = $reorderedRows[0]; $reorderedRows[0] = $reorderedRows[1]; $reorderedRows[1] = $tmp
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $reorderedRows) -CaseName 'negative_reordered_rows' | Out-Null

    # -----------------------------------------------------------------
    # Case 11: renamed surface (an assessment surface does not match the
    # frozen identity for its ordinal)
    # -----------------------------------------------------------------
    $renamedSurfaceRows = New-FixtureAssessments
    $renamedSurfaceRows[0].surface = 'renamed-public-readme'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $renamedSurfaceRows) -CaseName 'negative_renamed_surface' | Out-Null

    # -----------------------------------------------------------------
    # Case 12: renamed criterion
    # -----------------------------------------------------------------
    $renamedCriterionRows = New-FixtureAssessments
    $renamedCriterionRows[3].criterion = 'renamed_criterion'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $renamedCriterionRows) -CaseName 'negative_renamed_criterion' | Out-Null

    # -----------------------------------------------------------------
    # Case 13: renamed audience
    # -----------------------------------------------------------------
    $renamedAudienceRows = New-FixtureAssessments
    $renamedAudienceRows[5].audience = 'renamed_audience'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $renamedAudienceRows) -CaseName 'negative_renamed_audience' | Out-Null

    # -----------------------------------------------------------------
    # Case 14: enum casing -- lowercase status must fail closed, not be
    # accepted through case-insensitive membership
    # -----------------------------------------------------------------
    $lowercaseStatusRows = New-FixtureAssessments
    $lowercaseStatusRows[0].status = 'pass'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $lowercaseStatusRows) -CaseName 'negative_lowercase_status_enum' | Out-Null

    # -----------------------------------------------------------------
    # Case 15: unknown status token
    # -----------------------------------------------------------------
    $unknownStatusRows = New-FixtureAssessments
    $unknownStatusRows[0].status = 'MOSTLY_FINE'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $unknownStatusRows) -CaseName 'negative_unknown_status_token' | Out-Null

    # -----------------------------------------------------------------
    # Case 16: Boolean type error -- reviewerOwned as string "true" must not
    # be accepted through PowerShell truthy coercion
    # -----------------------------------------------------------------
    $stringReviewerOwnedRows = New-FixtureAssessments
    $stringReviewerOwnedRows[0].reviewerOwned = 'true'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $stringReviewerOwnedRows) -CaseName 'negative_reviewer_owned_string_true' | Out-Null

    $numericReviewerOwnedRows = New-FixtureAssessments
    $numericReviewerOwnedRows[0].reviewerOwned = 1
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $numericReviewerOwnedRows) -CaseName 'negative_reviewer_owned_numeric_one' | Out-Null

    $falseReviewerOwnedRows = New-FixtureAssessments
    $falseReviewerOwnedRows[0].reviewerOwned = $false
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $falseReviewerOwnedRows) -CaseName 'negative_reviewer_owned_false' | Out-Null

    # -----------------------------------------------------------------
    # Case 17: empty evidenceLocator / observation
    # -----------------------------------------------------------------
    $emptyLocatorRows = New-FixtureAssessments
    $emptyLocatorRows[0].evidenceLocator = ''
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $emptyLocatorRows) -CaseName 'negative_empty_evidence_locator' | Out-Null

    $whitespaceObservationRows = New-FixtureAssessments
    $whitespaceObservationRows[0].observation = '   '
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $whitespaceObservationRows) -CaseName 'negative_whitespace_observation' | Out-Null

    # -----------------------------------------------------------------
    # Case 18: non-ASCII evidenceLocator / observation
    # -----------------------------------------------------------------
    $nonAsciiLocatorRows = New-FixtureAssessments
    $nonAsciiLocatorRows[0].evidenceLocator = "locator-$([char]0x00e9)"
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $nonAsciiLocatorRows) -CaseName 'negative_non_ascii_evidence_locator' | Out-Null

    # -----------------------------------------------------------------
    # Case 19: missing required assessment field
    # -----------------------------------------------------------------
    $missingFieldRows = New-FixtureAssessments
    $missingFieldRows[0].Remove('observation') | Out-Null
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $missingFieldRows) -CaseName 'negative_missing_assessment_field' | Out-Null

    # -----------------------------------------------------------------
    # Case 20: missing top-level audienceEvidenceSchemaVersion field
    # -----------------------------------------------------------------
    $missingSchemaEvidence = New-FixtureEvidenceObject -Assessments $validAssessments
    $missingSchemaEvidence.Remove('audienceEvidenceSchemaVersion') | Out-Null
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject $missingSchemaEvidence -CaseName 'negative_missing_schema_version_field' | Out-Null

    # -----------------------------------------------------------------
    # Case 21: wrong audienceEvidenceSchemaVersion value
    # -----------------------------------------------------------------
    $wrongSchemaEvidence = New-FixtureEvidenceObject -Assessments $validAssessments
    $wrongSchemaEvidence.audienceEvidenceSchemaVersion = 'cvf.continuousProjectionAudienceEvidence.t3.v2'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $validDraftObj -EvidenceObject $wrongSchemaEvidence -CaseName 'negative_wrong_schema_version_value' | Out-Null

    # -----------------------------------------------------------------
    # Case 22: T1 receipt contract violations
    # -----------------------------------------------------------------
    $badReconcileReceipt = New-FixtureReceiptObject
    $badReconcileReceipt.summary.reconciliationMatch = $false
    Test-FailClosed -ReceiptObject $badReconcileReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_reconciliation_not_true' | Out-Null

    $stringReconcileReceipt = New-FixtureReceiptObject
    $stringReconcileReceipt.summary.reconciliationMatch = 'true'
    Test-FailClosed -ReceiptObject $stringReconcileReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_reconciliation_string_true' | Out-Null

    $nonEmptyErrorsReceipt = New-FixtureReceiptObject
    $nonEmptyErrorsReceipt.errors = @([ordered]@{ code = 'X'; message = 'y' })
    Test-FailClosed -ReceiptObject $nonEmptyErrorsReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_nonempty_errors' | Out-Null

    $missingReceiptFieldReceipt = New-FixtureReceiptObject
    $missingReceiptFieldReceipt.Remove('mapperReceiptId') | Out-Null
    Test-FailClosed -ReceiptObject $missingReceiptFieldReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_missing_top_level_field' | Out-Null

    $badWriteConfirmationReceipt = New-FixtureReceiptObject
    $badWriteConfirmationReceipt.noTargetWriteConfirmation = 'NOT_THE_EXPECTED_CONFIRMATION'
    Test-FailClosed -ReceiptObject $badWriteConfirmationReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_bad_write_confirmation' | Out-Null

    $prefixOnlyWriteConfirmationReceipt = New-FixtureReceiptObject
    $prefixOnlyWriteConfirmationReceipt.noTargetWriteConfirmation = 'CONFIRMED_NO_TARGET_WRITE: forged suffix'
    Test-FailClosed -ReceiptObject $prefixOnlyWriteConfirmationReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_nonexact_write_confirmation' | Out-Null

    $wrongReceiptSchema = New-FixtureReceiptObject
    $wrongReceiptSchema.schemaVersion = '9.9.9'
    Test-FailClosed -ReceiptObject $wrongReceiptSchema -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_wrong_schema_version' | Out-Null

    $shortReceipt = New-FixtureReceiptObject
    $shortReceipt.rows = @($shortReceipt.rows[0..14])
    $shortReceipt.summary.rowCount = 15
    Test-FailClosed -ReceiptObject $shortReceipt -DraftObject $validDraftObj -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_wrong_row_count' | Out-Null

    $emptyReceiptId = New-FixtureReceiptObject
    $emptyReceiptId.receiptId = ''
    Test-FailClosed -ReceiptObject $emptyReceiptId -DraftObject (New-FixtureDraftObject -SourceReceiptId '') -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_receipt_empty_identity' | Out-Null

    # -----------------------------------------------------------------
    # Case 23: T2 draft contract violations
    # -----------------------------------------------------------------
    $badDraftStatus = New-FixtureDraftObject
    $badDraftStatus.draftStatus = 'AUTO_APPROVED'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $badDraftStatus -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_wrong_status' | Out-Null

    $badAuthorizesDecisionDraft = New-FixtureDraftObject
    $badAuthorizesDecisionDraft.authorizesDecision = $true
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $badAuthorizesDecisionDraft -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_authorizes_decision_true' | Out-Null

    $stringAuthorizesDecisionDraft = New-FixtureDraftObject
    $stringAuthorizesDecisionDraft.authorizesDecision = 'false'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $stringAuthorizesDecisionDraft -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_authorizes_decision_string_false' | Out-Null

    $badClaimBoundaryDraft = New-FixtureDraftObject
    $badClaimBoundaryDraft.claimBoundary = 'SOMETHING_ELSE'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $badClaimBoundaryDraft -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_bad_claim_boundary' | Out-Null

    $missingDraftField = New-FixtureDraftObject
    $missingDraftField.Remove('evidence') | Out-Null
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $missingDraftField -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_missing_top_level_field' | Out-Null

    $wrongDraftSchema = New-FixtureDraftObject
    $wrongDraftSchema.schemaVersion = '9.9.9'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $wrongDraftSchema -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_wrong_schema_version' | Out-Null

    $emptyDraftId = New-FixtureDraftObject
    $emptyDraftId.draftId = ''
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $emptyDraftId -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_empty_identity' | Out-Null

    $wrongDraftSourceCount = New-FixtureDraftObject
    $wrongDraftSourceCount.sourceFacts.receiptRowCount = 0
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $wrongDraftSourceCount -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_wrong_source_row_count' | Out-Null

    $stringDraftSourceCount = New-FixtureDraftObject
    $stringDraftSourceCount.sourceFacts.receiptRowCount = '16'
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $stringDraftSourceCount -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_string_source_row_count' | Out-Null

    $mutationDraft = New-FixtureDraftObject
    $mutationDraft.publicProvenanceBoundary.publicMutationAuthorized = $true
    Test-FailClosed -ReceiptObject $validReceiptObj -DraftObject $mutationDraft -EvidenceObject (New-FixtureEvidenceObject -Assessments $validAssessments) -CaseName 'negative_draft_public_mutation_true' | Out-Null

    # -----------------------------------------------------------------
    # Case 24: not-valid-JSON and missing files for all three inputs fail
    # closed
    # -----------------------------------------------------------------
    $badJsonPath = Join-Path $tempRoot 'not_json.json'
    [System.IO.File]::WriteAllText($badJsonPath, 'this is not json {', [System.Text.UTF8Encoding]::new($false))
    $runBadReceiptJson = Invoke-Gate -GateArgs @('-ReceiptPath', $badJsonPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath)
    Assert-True ($runBadReceiptJson.ExitCode -ne 0 -and [string]::IsNullOrWhiteSpace($runBadReceiptJson.Stdout) -and $runBadReceiptJson.Stderr -match 'UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE') 'negative_unparseable_receipt_json' $runBadReceiptJson.Stderr

    $runMissingReceipt = Invoke-Gate -GateArgs @('-ReceiptPath', (Join-Path $tempRoot 'does_not_exist.json'), '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath)
    Assert-True ($runMissingReceipt.ExitCode -ne 0 -and [string]::IsNullOrWhiteSpace($runMissingReceipt.Stdout) -and $runMissingReceipt.Stderr -match 'UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE') 'negative_missing_receipt_file' $runMissingReceipt.Stderr

    $runMissingEvidence = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', (Join-Path $tempRoot 'does_not_exist_2.json'))
    Assert-True ($runMissingEvidence.ExitCode -ne 0 -and [string]::IsNullOrWhiteSpace($runMissingEvidence.Stdout) -and $runMissingEvidence.Stderr -match 'UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE') 'negative_missing_evidence_file' $runMissingEvidence.Stderr

    # -----------------------------------------------------------------
    # Case 25: no mutation surface -- attempted root/output/apply/copy/commit/
    # push/browser/provider/network parameters are rejected (the gate
    # declares only the three required parameters, so binding fails nonzero)
    # -----------------------------------------------------------------
    $runExtraRoot = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath, '-ProvenanceRoot', 'C:\should-not-bind')
    Assert-True ($runExtraRoot.ExitCode -ne 0) 'attempted_provenance_root_parameter_rejected' "$($runExtraRoot.ExitCode)"

    $runExtraOutput = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath, '-OutputPath', (Join-Path $tempRoot 'should_not_write.json'))
    Assert-True ($runExtraOutput.ExitCode -ne 0) 'attempted_output_path_parameter_rejected' "$($runExtraOutput.ExitCode)"
    Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot 'should_not_write.json'))) 'attempted_output_path_wrote_no_file' 'a file was written for a rejected output-path parameter'

    $runExtraApply = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath, '-Apply')
    Assert-True ($runExtraApply.ExitCode -ne 0) 'attempted_apply_parameter_rejected' "$($runExtraApply.ExitCode)"

    $runExtraCommit = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath, '-Commit')
    Assert-True ($runExtraCommit.ExitCode -ne 0) 'attempted_commit_parameter_rejected' "$($runExtraCommit.ExitCode)"

    $runExtraBrowser = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath, '-Browser')
    Assert-True ($runExtraBrowser.ExitCode -ne 0) 'attempted_browser_parameter_rejected' "$($runExtraBrowser.ExitCode)"

    $runExtraProvider = Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath, '-ProviderApiKey', 'x')
    Assert-True ($runExtraProvider.ExitCode -ne 0) 'attempted_provider_parameter_rejected' "$($runExtraProvider.ExitCode)"

    # -----------------------------------------------------------------
    # Case 26: no apply/copy/output/network mode in the gate source, and the
    # gate writes no file (output goes to stdout only)
    # -----------------------------------------------------------------
    $gateSource = Get-Content -LiteralPath $gatePath -Raw -Encoding utf8
    $forbiddenTokens = @('Copy-Item', 'Move-Item', 'Set-Content', 'Out-File', 'WriteAllBytes',
        'Invoke-WebRequest', 'Invoke-RestMethod', 'System\.Net\.Http', 'New-Object\s+Net\.WebClient',
        '\[Parameter.*\]\s*\[string\]\$OutputPath', 'param\([^)]*OutputPath', 'param\([^)]*ProvenanceRoot')
    $foundForbidden = @($forbiddenTokens | Where-Object { $gateSource -match $_ })
    Assert-True (@($foundForbidden).Count -eq 0) 'no_apply_copy_network_mode_in_source' ($foundForbidden -join ',')
    Assert-True ($gateSource -notmatch 'CLAUDE\.md') 'provider_specific_memory_not_used_as_authority' 'provider-specific memory reference found in gate source'
    $workDir = Join-Path $tempRoot 'writecheck'
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null
    $filesBefore = @(Get-ChildItem -LiteralPath $workDir -Recurse -File | ForEach-Object { $_.FullName })
    $prevLoc = Get-Location
    Set-Location $workDir
    try { Invoke-Gate -GateArgs @('-ReceiptPath', $validReceiptPath, '-ReviewPacketPath', $validDraftPath, '-AudienceEvidencePath', $validEvidencePath) | Out-Null } finally { Set-Location $prevLoc }
    $filesAfter = @(Get-ChildItem -LiteralPath $workDir -Recurse -File | ForEach-Object { $_.FullName })
    Assert-True (@($filesAfter).Count -eq @($filesBefore).Count) 'gate_writes_no_file' "before=$(@($filesBefore).Count) after=$(@($filesAfter).Count)"

    # -----------------------------------------------------------------
    # Case 27: stdout has no BOM and no secret-like content
    # -----------------------------------------------------------------
    $stdoutBytes = [System.Text.Encoding]::UTF8.GetBytes($run1.Stdout)
    $hasBom = $stdoutBytes.Length -ge 3 -and $stdoutBytes[0] -eq 0xEF -and $stdoutBytes[1] -eq 0xBB -and $stdoutBytes[2] -eq 0xBF
    Assert-True (-not $hasBom) 'gate_stdout_has_no_bom' 'stdout has a UTF-8 BOM'
    Assert-True ($run1.Stdout -notmatch '(?i)(api[_-]?key|secret|password|bearer\s)') 'gate_no_secret_like_content' 'possible secret-like token found'

    $total = $script:passCount + $script:failCount
    Write-Output ''
    Write-Output '=== CVF Continuous Projection T3 Audience Gate Proof Suite ==='
    $script:results | ForEach-Object { Write-Output $_ }
    Write-Output ''
    Write-Output "Total: $total, Pass: $($script:passCount), Fail: $($script:failCount)"

    if ($script:failCount -gt 0) { exit 1 } else { exit 0 }
} finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
