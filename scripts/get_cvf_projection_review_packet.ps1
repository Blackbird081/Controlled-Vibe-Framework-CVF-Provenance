<#
.SYNOPSIS
    CVF Continuous Projection T2 read-only governed review-packet drafter.

.DESCRIPTION
    Deterministic, read-only drafter. It consumes exactly one already-produced
    drift receipt supplied through the required -ReceiptPath parameter, and it
    emits one ordered JSON review-packet draft to stdout only. It performs NO
    filesystem write, adds NO apply/copy/output-path/commit/persistence mode,
    never re-runs the real-root three-root scan (that is T4-owned), and never
    invokes the accepted mapper or drift receipt. The generated draft is a
    review-required, uncommitted draft that authorizes no reviewer decision.

    The drafter reads the receipt's frozen output schema (16 surface rows, the
    tracked/ignored public-target split, the reconciled disposition summary,
    the no-target-write confirmation, and the mapper receipt identity) and
    projects it into five review content groups: source facts, affected
    projections, recommended reviewer actions, the public/provenance boundary,
    and evidence. It is fail-closed: any missing required receipt field, failed
    reconciliation, unknown disposition, or affected-projection/action
    cardinality mismatch produces one JSON diagnostic on stderr with code
    UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT, a nonzero exit, and no stdout success
    draft.

.PARAMETER ReceiptPath
    Required. Path to one existing UTF-8 JSON drift receipt file produced by
    scripts\get_cvf_projection_drift_receipt.ps1 (reused accepted receipt or a
    disposable fixture receipt). The file is read only; it is never modified.

.OUTPUTS
    On success: one ordered JSON review-packet draft on stdout, and exit 0.
    On any invalid receipt: one JSON diagnostic on stderr, no stdout draft, and
    a nonzero exit.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\get_cvf_projection_review_packet.ps1 -ReceiptPath receipt.json

.NOTES
    This script has no ProvenanceRoot, PublicSyncRoot, CvfWebRoot, PolicyPath,
    OutputPath, apply, copy, commit, public-sync, or auto-approve parameter. It
    reads one receipt file and writes one draft to stdout. Tests may capture
    that stdout inside their own disposable temp directory; the captured draft
    is never a persistent worker output.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ReceiptPath
)

$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# Frozen T2 draft output contract constants. Source of truth:
# docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T2_GOVERNED_REVIEW_PACKET_DRAFTING_2026-07-20.md
# Frozen T2 Draft Output Contract section. These are transcribed here as an
# immutable, source-local set so the draft contract cannot silently drift.
# ---------------------------------------------------------------------------
$script:DraftSchemaVersion = '1.0.0'
$script:DraftStatus = 'REVIEW_REQUIRED_UNCOMMITTED'
$script:ClaimBoundaryLiteral = 'DRAFT_ONLY_REVIEWER_DECISION_REQUIRED_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION'
$script:InvalidReceiptCode = 'UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT'

# Dispositions that produce NO affected-projection row and NO action row.
# NOTE: disposition tokens are frozen canonical CVF enum values. Membership
# must be evaluated ordinally/case-sensitively (PowerShell's default
# -contains/-notcontains and Hashtable/OrderedDictionary key lookups are
# culture- and case-INSENSITIVE, which would silently accept noncanonical
# tokens such as "current" or "missing_target"). All lookups below use
# explicit ordinal comparers or the -c-prefixed case-sensitive operators.
$script:ExcludedDispositions = @('CURRENT', 'NOT_APPLICABLE_WITH_REASON')

# Frozen disposition-to-action mapping. Only these five dispositions are
# recommendable; any other disposition on an affected row is unknown and
# fails closed. Backed by a Dictionary with an ordinal comparer (not
# [ordered]@{}, whose key lookup is case-insensitive) so a noncanonical
# lowercase or mixed-case token is never accepted as a known disposition.
$script:ActionMap = [System.Collections.Generic.Dictionary[string, string]]::new([System.StringComparer]::Ordinal)
$script:ActionMap.Add('MISSING_TARGET', 'REVIEW_MISSING_TARGET_NO_COPY_AUTHORIZED')
$script:ActionMap.Add('STALE_TARGET', 'REVIEW_STALE_TARGET_DIFF_NO_APPLY_AUTHORIZED')
$script:ActionMap.Add('SEMANTIC_REVIEW_REQUIRED', 'REVIEW_SEMANTIC_OWNER_AND_TARGET')
$script:ActionMap.Add('SOURCE_AUTHORITY_BLOCKED', 'KEEP_BLOCKED_PENDING_SOURCE_AUTHORITY')
$script:ActionMap.Add('AUDIENCE_PRESENTATION_RISK', 'REVIEW_AUDIENCE_PRESENTATION')

# Required top-level receipt fields and required per-row fields.
$script:RequiredReceiptFields = @(
    'receiptId', 'schemaVersion', 'rootsObserved', 'rows', 'publicTargetState',
    'summary', 'mapperReceiptId', 'noTargetWriteConfirmation', 'errors'
)
$script:RequiredRowFields = @(
    'surface', 'semanticOwner', 'projectionTarget', 'evidenceClass', 'audience',
    'driftDisposition', 'sourceHash', 'targetHash', 'reviewerNote'
)
$script:RequiredRowCount = 16

function Test-HasProperty {
    param([object]$InputObject, [string]$Name)
    if ($null -eq $InputObject) { return $false }
    return (@($InputObject.PSObject.Properties.Name) -contains $Name)
}

function Assert-ValidReceipt {
    <# Fail-closed receipt validation. Throws an error whose message begins
       with the invalid-receipt code on any shape violation, so every invalid
       receipt maps to exactly one diagnostic code. #>
    param([object]$Receipt)

    if ($null -eq $Receipt) {
        throw "$($script:InvalidReceiptCode): receipt did not parse as a JSON object"
    }

    foreach ($field in $script:RequiredReceiptFields) {
        if (-not (Test-HasProperty -InputObject $Receipt -Name $field)) {
            throw "$($script:InvalidReceiptCode): missing required receipt field '$field'"
        }
    }

    foreach ($summaryField in @('rowCount', 'reconciliationMatch')) {
        if (-not (Test-HasProperty -InputObject $Receipt.summary -Name $summaryField)) {
            throw "$($script:InvalidReceiptCode): missing required receipt field 'summary.$summaryField'"
        }
    }

    $rows = @($Receipt.rows)
    if ($rows.Count -ne $script:RequiredRowCount) {
        throw "$($script:InvalidReceiptCode): receipt row count is $($rows.Count), expected $($script:RequiredRowCount)"
    }

    foreach ($row in $rows) {
        foreach ($rowField in $script:RequiredRowFields) {
            if (-not (Test-HasProperty -InputObject $row -Name $rowField)) {
                throw "$($script:InvalidReceiptCode): a receipt row is missing required field '$rowField'"
            }
        }
    }

    $errors = @($Receipt.errors)
    if ($errors.Count -ne 0) {
        throw "$($script:InvalidReceiptCode): receipt errors array is not empty ($($errors.Count) entries)"
    }

    if ([int]$Receipt.summary.rowCount -ne $script:RequiredRowCount) {
        throw "$($script:InvalidReceiptCode): summary.rowCount is $($Receipt.summary.rowCount), expected $($script:RequiredRowCount)"
    }

    # summary.reconciliationMatch must be an actual JSON boolean `true`, not a
    # PowerShell-coerced equivalent. PowerShell's -ne/-eq operators coerce the
    # right-hand operand to the left operand's type, so a JSON string "true"
    # (-eq $true stringifies to "True", a case-insensitive string match) or a
    # JSON number 1 (-eq $true coerces $true to 1) would otherwise pass. The
    # explicit -is [bool] type check closes both loopholes.
    if (-not ($Receipt.summary.reconciliationMatch -is [bool]) -or ($Receipt.summary.reconciliationMatch -ne $true)) {
        throw "$($script:InvalidReceiptCode): summary.reconciliationMatch is not a JSON boolean true"
    }
}

function Get-Sha256UpperHex {
    param([string]$Text)
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $hash = $sha.ComputeHash($bytes)
        return (-join ($hash | ForEach-Object { $_.ToString('X2') }))
    } finally {
        $sha.Dispose()
    }
}

function New-AffectedProjectionRow {
    param([object]$Row)
    return [ordered]@{
        surface          = $Row.surface
        semanticOwner    = $Row.semanticOwner
        projectionTarget = $Row.projectionTarget
        evidenceClass    = $Row.evidenceClass
        audience         = @($Row.audience)
        driftDisposition = $Row.driftDisposition
        sourceHash       = $Row.sourceHash
        targetHash       = $Row.targetHash
        reviewerNote     = $Row.reviewerNote
    }
}

function New-RecommendedActionRow {
    param([object]$Row, [string]$Action)
    return [ordered]@{
        surface           = $Row.surface
        driftDisposition  = $Row.driftDisposition
        recommendedAction = $Action
        reviewerNote      = $Row.reviewerNote
        decisionAuthority = 'REVIEWER_ONLY'
    }
}

function Write-Diagnostic {
    param([string]$Code, [string]$Message, [string]$Path)
    $diagnostic = [ordered]@{
        code        = $Code
        message     = $Message
        receiptPath = $Path
        draftStatus = 'NOT_EMITTED_FAIL_CLOSED'
    }
    $diagnosticJson = $diagnostic | ConvertTo-Json -Depth 20 -Compress
    [Console]::Error.WriteLine($diagnosticJson)
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

try {
    if (-not (Test-Path -LiteralPath $ReceiptPath -PathType Leaf)) {
        throw "$($script:InvalidReceiptCode): receipt file not found: $ReceiptPath"
    }

    $receiptText = [System.IO.File]::ReadAllText($ReceiptPath)
    $receipt = $null
    try {
        $receipt = $receiptText | ConvertFrom-Json
    } catch {
        throw "$($script:InvalidReceiptCode): receipt file is not valid JSON: $ReceiptPath"
    }

    Assert-ValidReceipt -Receipt $receipt

    $rows = @($receipt.rows)

    # Affected projections: rows whose driftDisposition is neither CURRENT nor
    # NOT_APPLICABLE_WITH_REASON, sorted ordinally by surface. -cnotcontains is
    # the case-sensitive variant of -notcontains; the default -notcontains is
    # case-insensitive and would wrongly exclude a noncanonical lowercase
    # "current" token as if it were the canonical CURRENT disposition.
    $affectedUnsorted = @($rows | Where-Object { $script:ExcludedDispositions -cnotcontains $_.driftDisposition })

    # Fail-closed affected-surface identity integrity check: every affected
    # row must carry a unique surface value. A duplicate affected surface
    # means the same projection surface was reported twice (possibly with
    # conflicting drift facts), which must be rejected before it could
    # silently collapse into a mismatched affected/action cardinality further
    # below. Uses an ordinal HashSet so exact-duplicate surface identity is
    # always detected regardless of hashtable culture/case defaults.
    $seenAffectedSurfaces = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
    $duplicateAffectedSurfaces = [System.Collections.Generic.List[string]]::new()
    foreach ($r in $affectedUnsorted) {
        if (-not $seenAffectedSurfaces.Add($r.surface)) {
            $duplicateAffectedSurfaces.Add($r.surface)
        }
    }
    if ($duplicateAffectedSurfaces.Count -gt 0) {
        $dupList = (@($duplicateAffectedSurfaces) | Sort-Object -Unique) -join ', '
        throw "$($script:InvalidReceiptCode): affected-surface/action cardinality integrity mismatch: duplicate affected surface identity detected for '$dupList'"
    }

    # Sort ordinally by surface (Sort-Object is culture-aware, so sort explicitly).
    $affectedSurfaces = [string[]]@($affectedUnsorted | ForEach-Object { $_.surface })
    [System.Array]::Sort($affectedSurfaces, [System.StringComparer]::Ordinal)
    $affectedBySurface = @{}
    foreach ($r in $affectedUnsorted) { $affectedBySurface[$r.surface] = $r }
    $affected = @($affectedSurfaces | ForEach-Object { $affectedBySurface[$_] })

    $affectedProjections = @()
    $recommendedActions = @()
    foreach ($row in $affected) {
        $affectedProjections += (New-AffectedProjectionRow -Row $row)
        if (-not $script:ActionMap.ContainsKey($row.driftDisposition)) {
            throw "$($script:InvalidReceiptCode): unknown driftDisposition '$($row.driftDisposition)' on surface '$($row.surface)'"
        }
        $recommendedActions += (New-RecommendedActionRow -Row $row -Action $script:ActionMap[$row.driftDisposition])
    }

    # Fail-closed cardinality invariant: exactly one action row per affected
    # projection surface. The duplicate-surface integrity check above is the
    # primary reachable trigger for an affected/action count divergence; this
    # final count comparison remains as a defense-in-depth post-condition.
    if (@($recommendedActions).Count -ne @($affectedProjections).Count) {
        throw "$($script:InvalidReceiptCode): affected-projection/action cardinality mismatch: affected=$(@($affectedProjections).Count) actions=$(@($recommendedActions).Count)"
    }

    $sourceFacts = [ordered]@{
        receiptId                = $receipt.receiptId
        receiptSchemaVersion     = $receipt.schemaVersion
        receiptRowCount          = @($rows).Count
        reconciliationMatch      = $receipt.summary.reconciliationMatch
        rootsObserved            = $receipt.rootsObserved
        publicTargetState        = $receipt.publicTargetState
        noTargetWriteConfirmation = $receipt.noTargetWriteConfirmation
    }

    $publicProvenanceBoundary = [ordered]@{
        sourceAuthority         = 'PROVENANCE_ROOT'
        observedTarget          = 'PUBLIC_SYNC_ROOT'
        publicMutationAuthorized = $false
        applyOrCopyAuthorized   = $false
        autoApproveAuthorized   = $false
        persistence             = 'STDOUT_ONLY_UNCOMMITTED'
    }

    $evidence = [ordered]@{
        sourceReceiptId                = $receipt.receiptId
        mapperReceiptId                = $receipt.mapperReceiptId
        receiptNoTargetWriteConfirmation = $receipt.noTargetWriteConfirmation
        receiptReconciliationMatch     = $receipt.summary.reconciliationMatch
        affectedProjectionCount        = @($affectedProjections).Count
        actionCount                    = @($recommendedActions).Count
    }

    # Fields 1-9 in exact ordinal order. draftId (field 10) is the uppercase
    # SHA-256 of the compact JSON of fields 1-9, so identical receipt content
    # produces byte-identical output.
    $draftBody = [ordered]@{
        schemaVersion             = $script:DraftSchemaVersion
        draftStatus               = $script:DraftStatus
        authorizesDecision        = $false
        sourceFacts               = $sourceFacts
        affectedProjections       = @($affectedProjections)
        recommendedReviewerActions = @($recommendedActions)
        publicProvenanceBoundary  = $publicProvenanceBoundary
        evidence                  = $evidence
        claimBoundary             = $script:ClaimBoundaryLiteral
    }

    $canonicalJsonForHash = $draftBody | ConvertTo-Json -Depth 20 -Compress
    $draftId = Get-Sha256UpperHex -Text $canonicalJsonForHash

    $draft = [ordered]@{}
    foreach ($key in $draftBody.Keys) { $draft[$key] = $draftBody[$key] }
    $draft['draftId'] = $draftId

    $draftJson = $draft | ConvertTo-Json -Depth 20
    Write-Output $draftJson
    exit 0
} catch {
    $message = $_.Exception.Message
    if ($message -match "^$([regex]::Escape($script:InvalidReceiptCode)):") {
        $detail = ($message -split ':', 2)[1].Trim()
    } else {
        $detail = $message
    }
    Write-Diagnostic -Code $script:InvalidReceiptCode -Message $detail -Path $ReceiptPath
    exit 1
}
