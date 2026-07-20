<#
.SYNOPSIS
    CVF Continuous Projection T3 read-only audience and presentation evidence
    gate.

.DESCRIPTION
    Deterministic, read-only evidence gate. It consumes exactly three already
    existing local JSON files supplied through the required -ReceiptPath,
    -ReviewPacketPath, and -AudienceEvidencePath parameters, and emits one
    JSON object to stdout. It performs NO filesystem write, adds NO root,
    output, apply, copy, commit, push, browser, or network parameter, never
    re-runs the accepted T1 receipt or T2 drafter, and never scans a real
    root. It validates that the T1 receipt reconciles cleanly, that the T2
    draft is uncommitted and non-authorizing and matches the T1 receipt
    identity, and that a reviewer-owned seven-row audience evidence packet is
    complete and internally consistent, then reports one terminal gate
    status. It performs NO semantic judgment of its own: the audience
    assessment status values are reviewer-owned inputs, not inferred here.

.PARAMETER ReceiptPath
    Required. Path to one existing UTF-8 JSON T1 drift receipt file produced
    by scripts\get_cvf_projection_drift_receipt.ps1 (reused accepted receipt
    or a disposable fixture receipt). Read only; never modified.

.PARAMETER ReviewPacketPath
    Required. Path to one existing UTF-8 JSON T2 review-packet draft file
    produced by scripts\get_cvf_projection_review_packet.ps1. Read only;
    never modified.

.PARAMETER AudienceEvidencePath
    Required. Path to one existing UTF-8 JSON reviewer-owned audience
    evidence file conforming to schema version
    cvf.continuousProjectionAudienceEvidence.t3.v1. Read only; never
    modified.

.OUTPUTS
    On success (input is well-formed, even when a terminal assessment
    resolves to FAIL or REVIEW_REQUIRED): one ordered JSON gate object on
    stdout, and exit 0.
    On malformed or contradictory input: one JSON diagnostic on stdout with
    code UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE, and a nonzero exit. No
    success object is ever emitted for a malformed-input run.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\get_cvf_projection_audience_gate.ps1 `
      -ReceiptPath receipt.json -ReviewPacketPath draft.json -AudienceEvidencePath evidence.json

.NOTES
    This script has no ProvenanceRoot, PublicSyncRoot, CvfWebRoot, PolicyPath,
    OutputPath, apply, copy, commit, push, browser, or provider parameter. It
    reads three explicit local files and writes one JSON object to stdout
    only. Frozen claim boundary:
    READ_ONLY_EVIDENCE_GATE_NO_SEMANTIC_DECISION_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ReceiptPath,

    [Parameter(Mandatory = $true)]
    [string]$ReviewPacketPath,

    [Parameter(Mandatory = $true)]
    [string]$AudienceEvidencePath
)

$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# Frozen T3 contract constants. Source of truth:
# docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T3_AUDIENCE_PRESENTATION_GATE_2026-07-20.md
# Frozen T3 Audience Evidence Contract and Frozen T3 Gate Interface And Output
# Contract sections. Transcribed here as an immutable, source-local set so
# the gate contract cannot silently drift.
# ---------------------------------------------------------------------------
$script:AudienceEvidenceSchemaVersion = 'cvf.continuousProjectionAudienceEvidence.t3.v1'
$script:AudienceGateSchemaVersion = 'cvf.continuousProjectionAudienceGate.t3.v1'
$script:ReceiptSchemaVersion = '1.0.0'
$script:DraftSchemaVersion = '1.0.0'
$script:InvalidCode = 'UNSUPPORTED_OR_INVALID_AUDIENCE_EVIDENCE'
$script:RequiredReceiptRowCount = 16
$script:RequiredReceiptRowFields = @(
    'surface', 'semanticOwner', 'projectionTarget', 'evidenceClass', 'audience',
    'driftDisposition', 'sourceHash', 'targetHash', 'reviewerNote'
)
$script:FrozenNoTargetWriteConfirmation = 'CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.'
$script:RequiredAssessmentFields = @('ordinal', 'surface', 'criterion', 'audience', 'status', 'evidenceLocator', 'observation', 'reviewerOwned')
$script:AllowedStatuses = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
foreach ($s in @('PASS', 'FAIL', 'REVIEW_REQUIRED')) { [void]$script:AllowedStatuses.Add($s) }

# The seven frozen ordered assessment identities (ordinal, surface, criterion, audience).
$script:FrozenAssessmentIdentities = @(
    [ordered]@{ ordinal = 1; surface = 'public-readme'; criterion = 'progressive_disclosure'; audience = 'end_user' },
    [ordered]@{ ordinal = 2; surface = 'public-readme'; criterion = 'language_clarity'; audience = 'end_user' },
    [ordered]@{ ordinal = 3; surface = 'public-readme'; criterion = 'first_action'; audience = 'end_user' },
    [ordered]@{ ordinal = 4; surface = 'cvf-web'; criterion = 'progressive_disclosure'; audience = 'end_user' },
    [ordered]@{ ordinal = 5; surface = 'cvf-web'; criterion = 'navigation_clarity'; audience = 'end_user' },
    [ordered]@{ ordinal = 6; surface = 'cvf-web'; criterion = 'developer_depth'; audience = 'developer' },
    [ordered]@{ ordinal = 7; surface = 'external-agent-context'; criterion = 'evidence_route'; audience = 'external_agent' }
)

$script:RequiredReceiptFields = @(
    'receiptId', 'schemaVersion', 'rootsObserved', 'rows', 'publicTargetState',
    'summary', 'mapperReceiptId', 'noTargetWriteConfirmation', 'errors'
)
$script:RequiredDraftFields = @(
    'schemaVersion', 'draftStatus', 'authorizesDecision', 'sourceFacts',
    'affectedProjections', 'recommendedReviewerActions', 'publicProvenanceBoundary',
    'evidence', 'claimBoundary', 'draftId'
)
$script:FrozenDraftStatus = 'REVIEW_REQUIRED_UNCOMMITTED'
$script:FrozenDraftClaimBoundary = 'DRAFT_ONLY_REVIEWER_DECISION_REQUIRED_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION'
$script:FrozenGateClaimBoundary = 'READ_ONLY_EVIDENCE_GATE_NO_SEMANTIC_DECISION_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION'

function Test-HasProperty {
    param([object]$InputObject, [string]$Name)
    if ($null -eq $InputObject) { return $false }
    return (@($InputObject.PSObject.Properties.Name) -contains $Name)
}

function Read-JsonFile {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "$($script:InvalidCode): $Label file not found: $Path"
    }
    $text = [System.IO.File]::ReadAllText($Path)
    try {
        return ($text | ConvertFrom-Json)
    } catch {
        throw "$($script:InvalidCode): $Label file is not valid JSON: $Path"
    }
}

function Assert-ValidReceipt {
    param([object]$Receipt)
    if ($null -eq $Receipt) {
        throw "$($script:InvalidCode): T1 receipt did not parse as a JSON object"
    }
    foreach ($field in $script:RequiredReceiptFields) {
        if (-not (Test-HasProperty -InputObject $Receipt -Name $field)) {
            throw "$($script:InvalidCode): T1 receipt missing required field '$field'"
        }
    }
    if ($Receipt.schemaVersion -isnot [string] -or [string]$Receipt.schemaVersion -cne $script:ReceiptSchemaVersion) {
        throw "$($script:InvalidCode): T1 receipt schemaVersion is not '$($script:ReceiptSchemaVersion)'"
    }
    if ($Receipt.receiptId -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$Receipt.receiptId)) {
        throw "$($script:InvalidCode): T1 receipt receiptId is empty or non-string"
    }
    if (-not (Test-HasProperty -InputObject $Receipt.summary -Name 'rowCount')) {
        throw "$($script:InvalidCode): T1 receipt missing required field 'summary.rowCount'"
    }
    if (-not (Test-HasProperty -InputObject $Receipt.summary -Name 'reconciliationMatch')) {
        throw "$($script:InvalidCode): T1 receipt missing required field 'summary.reconciliationMatch'"
    }
    if (-not ($Receipt.summary.reconciliationMatch -is [bool]) -or ($Receipt.summary.reconciliationMatch -ne $true)) {
        throw "$($script:InvalidCode): T1 receipt summary.reconciliationMatch is not a JSON boolean true"
    }
    $rows = @($Receipt.rows)
    if ($rows.Count -ne $script:RequiredReceiptRowCount) {
        throw "$($script:InvalidCode): T1 receipt row count is $($rows.Count), expected $($script:RequiredReceiptRowCount)"
    }
    if ($Receipt.summary.rowCount -isnot [int] -and $Receipt.summary.rowCount -isnot [long]) {
        throw "$($script:InvalidCode): T1 receipt summary.rowCount is not a JSON integer"
    }
    if ([int]$Receipt.summary.rowCount -ne $script:RequiredReceiptRowCount) {
        throw "$($script:InvalidCode): T1 receipt summary.rowCount is $($Receipt.summary.rowCount), expected $($script:RequiredReceiptRowCount)"
    }
    foreach ($row in $rows) {
        foreach ($field in $script:RequiredReceiptRowFields) {
            if (-not (Test-HasProperty -InputObject $row -Name $field)) {
                throw "$($script:InvalidCode): T1 receipt row missing required field '$field'"
            }
        }
    }
    $errors = @($Receipt.errors)
    if ($errors.Count -ne 0) {
        throw "$($script:InvalidCode): T1 receipt errors array is not empty ($($errors.Count) entries)"
    }
    if ($Receipt.noTargetWriteConfirmation -isnot [string] -or [string]$Receipt.noTargetWriteConfirmation -cne $script:FrozenNoTargetWriteConfirmation) {
        throw "$($script:InvalidCode): T1 receipt noTargetWriteConfirmation is not an exact no-target-write confirmation"
    }
}

function Assert-ValidDraft {
    param([object]$Draft, [object]$Receipt)
    if ($null -eq $Draft) {
        throw "$($script:InvalidCode): T2 draft did not parse as a JSON object"
    }
    foreach ($field in $script:RequiredDraftFields) {
        if (-not (Test-HasProperty -InputObject $Draft -Name $field)) {
            throw "$($script:InvalidCode): T2 draft missing required field '$field'"
        }
    }
    if ($Draft.schemaVersion -isnot [string] -or [string]$Draft.schemaVersion -cne $script:DraftSchemaVersion) {
        throw "$($script:InvalidCode): T2 draft schemaVersion is not '$($script:DraftSchemaVersion)'"
    }
    if ($Draft.draftId -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$Draft.draftId)) {
        throw "$($script:InvalidCode): T2 draft draftId is empty or non-string"
    }
    if ([string]$Draft.draftStatus -cne $script:FrozenDraftStatus) {
        throw "$($script:InvalidCode): T2 draft draftStatus is not '$($script:FrozenDraftStatus)'"
    }
    if (-not ($Draft.authorizesDecision -is [bool]) -or ($Draft.authorizesDecision -ne $false)) {
        throw "$($script:InvalidCode): T2 draft authorizesDecision is not a JSON boolean false"
    }
    if ([string]$Draft.claimBoundary -cne $script:FrozenDraftClaimBoundary) {
        throw "$($script:InvalidCode): T2 draft claimBoundary does not match the frozen no-mutation claim boundary"
    }
    if (-not (Test-HasProperty -InputObject $Draft.sourceFacts -Name 'receiptId')) {
        throw "$($script:InvalidCode): T2 draft sourceFacts missing required field 'receiptId'"
    }
    if ([string]$Draft.sourceFacts.receiptId -cne [string]$Receipt.receiptId) {
        throw "$($script:InvalidCode): T2 draft source receipt identity does not match the T1 receipt receiptId"
    }
    foreach ($field in @('receiptSchemaVersion', 'receiptRowCount', 'reconciliationMatch', 'noTargetWriteConfirmation')) {
        if (-not (Test-HasProperty -InputObject $Draft.sourceFacts -Name $field)) {
            throw "$($script:InvalidCode): T2 draft sourceFacts missing required field '$field'"
        }
    }
    if ([string]$Draft.sourceFacts.receiptSchemaVersion -cne $script:ReceiptSchemaVersion) {
        throw "$($script:InvalidCode): T2 draft sourceFacts.receiptSchemaVersion does not match the accepted T1 schema"
    }
    if (($Draft.sourceFacts.receiptRowCount -isnot [int] -and $Draft.sourceFacts.receiptRowCount -isnot [long]) -or
        [long]$Draft.sourceFacts.receiptRowCount -ne $script:RequiredReceiptRowCount) {
        throw "$($script:InvalidCode): T2 draft sourceFacts.receiptRowCount is not the JSON integer $($script:RequiredReceiptRowCount)"
    }
    if (-not ($Draft.sourceFacts.reconciliationMatch -is [bool]) -or $Draft.sourceFacts.reconciliationMatch -ne $true) {
        throw "$($script:InvalidCode): T2 draft sourceFacts.reconciliationMatch is not a JSON boolean true"
    }
    if ([string]$Draft.sourceFacts.noTargetWriteConfirmation -cne $script:FrozenNoTargetWriteConfirmation) {
        throw "$($script:InvalidCode): T2 draft sourceFacts.noTargetWriteConfirmation is not exact"
    }
    foreach ($field in @('publicMutationAuthorized', 'applyOrCopyAuthorized', 'autoApproveAuthorized')) {
        if (-not (Test-HasProperty -InputObject $Draft.publicProvenanceBoundary -Name $field) -or
            $Draft.publicProvenanceBoundary.$field -isnot [bool] -or $Draft.publicProvenanceBoundary.$field -ne $false) {
            throw "$($script:InvalidCode): T2 draft publicProvenanceBoundary.$field is not a JSON boolean false"
        }
    }
}

function Assert-ValidAudienceEvidence {
    param([object]$Evidence)
    if ($null -eq $Evidence) {
        throw "$($script:InvalidCode): audience evidence did not parse as a JSON object"
    }
    if (-not (Test-HasProperty -InputObject $Evidence -Name 'audienceEvidenceSchemaVersion')) {
        throw "$($script:InvalidCode): audience evidence missing required field 'audienceEvidenceSchemaVersion'"
    }
    if ([string]$Evidence.audienceEvidenceSchemaVersion -cne $script:AudienceEvidenceSchemaVersion) {
        throw "$($script:InvalidCode): audience evidence audienceEvidenceSchemaVersion is not '$($script:AudienceEvidenceSchemaVersion)'"
    }
    if (-not (Test-HasProperty -InputObject $Evidence -Name 'assessments')) {
        throw "$($script:InvalidCode): audience evidence missing required field 'assessments'"
    }

    $assessments = @($Evidence.assessments)
    if ($assessments.Count -ne 7) {
        throw "$($script:InvalidCode): audience evidence assessment row count is $($assessments.Count), expected 7"
    }

    $seenOrdinals = [System.Collections.Generic.HashSet[int]]::new()
    for ($i = 0; $i -lt $assessments.Count; $i++) {
        $row = $assessments[$i]
        foreach ($field in $script:RequiredAssessmentFields) {
            if (-not (Test-HasProperty -InputObject $row -Name $field)) {
                throw "$($script:InvalidCode): audience evidence assessment at index $i is missing required field '$field'"
            }
        }

        if ($row.ordinal -isnot [int] -and $row.ordinal -isnot [long]) {
            throw "$($script:InvalidCode): audience evidence assessment at index $i has non-integer 'ordinal'"
        }
        $ordinalInt = [int]$row.ordinal
        if (-not $seenOrdinals.Add($ordinalInt)) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal '$ordinalInt' is duplicated"
        }

        $expected = $script:FrozenAssessmentIdentities[$i]
        if ($ordinalInt -ne [int]$expected.ordinal) {
            throw "$($script:InvalidCode): audience evidence assessment at index $i has wrong ordinal '$ordinalInt', expected '$($expected.ordinal)' (reordered or renumbered row)"
        }
        if ([string]$row.surface -cne [string]$expected.surface) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has wrong surface '$($row.surface)', expected '$($expected.surface)'"
        }
        if ([string]$row.criterion -cne [string]$expected.criterion) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has wrong criterion '$($row.criterion)', expected '$($expected.criterion)'"
        }
        if ([string]$row.audience -cne [string]$expected.audience) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has wrong audience '$($row.audience)', expected '$($expected.audience)'"
        }

        if ($row.reviewerOwned -isnot [bool] -or $row.reviewerOwned -ne $true) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt reviewerOwned is not a JSON boolean true"
        }

        if ($row.status -isnot [string] -or -not $script:AllowedStatuses.Contains([string]$row.status)) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has invalid status '$($row.status)'"
        }

        if ($row.evidenceLocator -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$row.evidenceLocator)) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has empty or non-string evidenceLocator"
        }
        if (-not [System.Text.Encoding]::ASCII.GetString([System.Text.Encoding]::ASCII.GetBytes($row.evidenceLocator)).Equals($row.evidenceLocator)) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt evidenceLocator is not ASCII text"
        }

        if ($row.observation -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$row.observation)) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has empty or non-string observation"
        }
        if (-not [System.Text.Encoding]::ASCII.GetString([System.Text.Encoding]::ASCII.GetBytes($row.observation)).Equals($row.observation)) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt observation is not ASCII text"
        }

        $extra = @($row.PSObject.Properties.Name | Where-Object { $script:RequiredAssessmentFields -cnotcontains $_ })
        if (@($extra).Count -gt 0) {
            throw "$($script:InvalidCode): audience evidence assessment ordinal $ordinalInt has unexpected extra field(s): $($extra -join ', ')"
        }
    }

    if ($seenOrdinals.Count -ne 7) {
        throw "$($script:InvalidCode): audience evidence assessment ordinals are not exactly 1..7"
    }
}

function New-AssessmentOutputRow {
    param([object]$Row)
    return [ordered]@{
        ordinal         = [int]$Row.ordinal
        surface         = $Row.surface
        criterion       = $Row.criterion
        audience        = $Row.audience
        status          = $Row.status
        evidenceLocator = $Row.evidenceLocator
        observation     = $Row.observation
        reviewerOwned   = $Row.reviewerOwned
    }
}

function Get-TerminalGateStatus {
    param([object[]]$Assessments)
    $statuses = @($Assessments | ForEach-Object { [string]$_.status })
    if (@($statuses | Where-Object { $_ -ceq 'FAIL' }).Count -gt 0) { return 'FAIL' }
    if (@($statuses | Where-Object { $_ -ceq 'REVIEW_REQUIRED' }).Count -gt 0) { return 'REVIEW_REQUIRED' }
    return 'PASS'
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

try {
    $receipt = Read-JsonFile -Path $ReceiptPath -Label 'T1 receipt'
    Assert-ValidReceipt -Receipt $receipt

    $draft = Read-JsonFile -Path $ReviewPacketPath -Label 'T2 review-packet draft'
    Assert-ValidDraft -Draft $draft -Receipt $receipt

    $evidence = Read-JsonFile -Path $AudienceEvidencePath -Label 'audience evidence'
    Assert-ValidAudienceEvidence -Evidence $evidence

    $assessmentsUnsorted = @($evidence.assessments)
    $assessmentsSorted = @($assessmentsUnsorted | Sort-Object -Property { [int]$_.ordinal })
    $assessments = @($assessmentsSorted | ForEach-Object { New-AssessmentOutputRow -Row $_ })

    $terminalStatus = Get-TerminalGateStatus -Assessments $assessments

    $byStatus = [ordered]@{}
    foreach ($row in $assessments) {
        $key = [string]$row.status
        if (-not $byStatus.Contains($key)) { $byStatus[$key] = 0 }
        $byStatus[$key] = $byStatus[$key] + 1
    }

    $summary = [ordered]@{
        assessmentCount      = $assessments.Count
        byStatus              = $byStatus
        sourceFreshnessStatus = 'PASS'
        audiencePresentationStatus = $terminalStatus
    }

    $gate = [ordered]@{
        schemaVersion              = $script:AudienceGateSchemaVersion
        gateStatus                 = $terminalStatus
        sourceFreshnessStatus      = 'PASS'
        audiencePresentationStatus = $terminalStatus
        authorizesMutation         = $false
        inputReceiptId              = $receipt.receiptId
        assessments                 = $assessments
        summary                     = $summary
        errors                      = @()
        claimBoundary               = $script:FrozenGateClaimBoundary
    }

    $gateJson = $gate | ConvertTo-Json -Depth 20
    Write-Output $gateJson
    exit 0
} catch {
    $message = $_.Exception.Message
    if ($message -match "^$([regex]::Escape($script:InvalidCode)):") {
        $detail = ($message -split ':', 2)[1].Trim()
    } else {
        $detail = $message
    }
    $diagnostic = [ordered]@{
        code          = $script:InvalidCode
        message       = $detail
        gateStatus    = 'NOT_EMITTED_FAIL_CLOSED'
    }
    $diagnosticJson = $diagnostic | ConvertTo-Json -Depth 20 -Compress
    [Console]::Error.WriteLine($diagnosticJson)
    exit 1
}
