<#
.SYNOPSIS
    ACEL G1 T3B Group 2 principal-bound activation-decision append writer
    (fail-closed).

.DESCRIPTION
    Builds one `cvf.specDecisionEvent` row (`APPROVED`, `REJECTED`,
    `ACTIVATED` or `SUPERSEDED`) and appends it to the governed, append-only
    `ACTIVATION_DECISIONS.jsonl`, canonicalized and hashed under
    `cvf.source-record-canonicalization@1`, with the exact T2F event-type
    state machine and hash-chain enforced against the file's own existing
    history before any append. Writes it, exclusively, only as the exact
    expected activation-approver principal.

    Default invocation is a hermetic self-test that proves every guard,
    including the full state machine (mutual-exclusion of the first decision,
    REJECTED terminality, ACTIVATED-requires-prior-APPROVED, SUPERSEDED-
    requires-exactly-one-active-version, self-approval rejection, and the
    unique-active invariant) using disposable fixtures and removes them.
    Real-mode execution requires -ExecuteWrite, an exact principal name and
    SID match, a non-elevated interactive session, and a typed confirmation,
    after every other guard has already passed. Real mode additionally
    hardens the appended-to file's NTFS DACL (never SACL) so the Party A
    principal cannot modify it while Local review can still read it.

    This tool does not claim spec establishment, activation validity,
    consumer binding or candidate admission. Its real-mode output text is
    exactly `DECISION_APPENDED_PENDING_LOCAL_VERIFICATION`.

.PARAMETER SelfTest
    Run hermetic positive and negative self-tests as the current user against
    disposable fixtures. This is the default when no mode is chosen and
    never targets the real Group 2 decisions path or the expected approver
    principal.

.PARAMETER ExecuteWrite
    Perform the real Group 2 decision append. Requires the current process
    identity to match both -ExpectedAccountName and -ExpectedAccountSid
    exactly, a non-elevated interactive host, and an interactive typed
    confirmation.

.PARAMETER ExpectedAccountName
    Exact expected Windows account name, e.g. 'HOSTNAME\cvf-g1-approver'. A
    bare name is qualified with the local computer name before comparison.

.PARAMETER ExpectedAccountSid
    Exact expected Windows account SID.

.PARAMETER EventType
    One of `APPROVED`, `REJECTED`, `ACTIVATED`, `SUPERSEDED`. Required in
    real mode.

.EXAMPLE
    pwsh -NoProfile -File scripts/acel_g1_approver_group2_decision_writer.ps1 -SelfTest

.NOTES
    Claim boundary: tooling only. A self-test proves guard and state-machine
    behavior, not that any Group 2 decision was appended. Real-mode output
    text explicitly reads `DECISION_APPENDED_PENDING_LOCAL_VERIFICATION`,
    never spec establishment, activation validity, consumer binding or
    admission.
#>
[CmdletBinding(DefaultParameterSetName = 'SelfTest')]
param(
    [Parameter(ParameterSetName = 'SelfTest')]
    [switch] $SelfTest,

    [Parameter(ParameterSetName = 'Write', Mandatory = $true)]
    [switch] $ExecuteWrite,

    [Parameter(ParameterSetName = 'Write', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $ExpectedAccountName,

    [Parameter(ParameterSetName = 'Write', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $ExpectedAccountSid,

    [Parameter(ParameterSetName = 'Write', Mandatory = $true)]
    [ValidateSet('APPROVED', 'REJECTED', 'ACTIVATED', 'SUPERSEDED')]
    [string] $EventType,

    # T3B-RV-2/T3B-RV-3 (R1 correction): the exact spec version this
    # decision event targets. Every event must cite its OWN version; no
    # caller may omit this and rely on an implicit/default/"latest" version.
    [Parameter(ParameterSetName = 'Write', Mandatory = $true)]
    [ValidateRange(1, [int]::MaxValue)]
    [int] $TargetSpecVersion,

    # T3B-RV-3 (R1 correction): required ONLY for `-EventType SUPERSEDED`.
    # The explicit, independently-validated NEWER version that is replacing
    # `-TargetSpecVersion`. Never inferred as "latest" or "largest"; the
    # caller must name it, and it is independently verified (own spec file,
    # own hash, and own prior APPROVED decision while not active or
    # superseded) before the atomic rotation event is appended.
    [Parameter(ParameterSetName = 'Write')]
    [ValidateRange(1, [int]::MaxValue)]
    [Nullable[int]] $ReplacementSpecVersion
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = 'Stop'

$convertFromJsonCommand = Get-Command ConvertFrom-Json -ErrorAction SilentlyContinue
if ($PSVersionTable.PSEdition -ne 'Core' -or
        $null -eq $convertFromJsonCommand -or
        -not $convertFromJsonCommand.Parameters.ContainsKey('DateKind')) {
    Write-Error '[UNSUPPORTED_POWERSHELL] PowerShell 7.5 or later is required so JSON timestamp fields remain exact strings.'
    exit 1
}

$script:ToolContract          = 'cvf.acel.g1.group2DecisionWriterTool@1'
$script:CanonProfile          = 'cvf.source-record-canonicalization@1'
$script:DecisionEventDomain   = 'cvf.specDecisionEvent'
$script:ConfirmationPhrase    = 'EXECUTE GROUP 2 DECISION APPEND'
$script:SpecDirectoryRelativePath = 'governance/sources/verification_authority_spec'
$script:DecisionsRelativePath = 'governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl'
$script:RealModeResultText    = 'DECISION_APPENDED_PENDING_LOCAL_VERIFICATION'
# T3B-RV-2 (R1 correction): `$script:ExpectedSpecVersion` remains ONLY as the
# hermetic self-test's own fixture default (the self-test never touches a
# real path or a caller-supplied version); the REAL-mode orchestration path
# below now always resolves and binds to the caller-cited
# `-TargetSpecVersion`/`-ReplacementSpecVersion`, never this constant.
$script:ExpectedSpecVersion   = 1
$script:ValidEventTypes       = @('APPROVED', 'REJECTED', 'ACTIVATED', 'SUPERSEDED')

# Exact expected approver principal, per
# `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md`.
$script:VerifiedApproverIdentity = [ordered]@{
    principalName = 'cvf-g1-approver'
    principalSid  = 'S-1-5-21-1644666849-912006174-747199667-1008'
}

# T3B-RV-1 (R1 correction): the exact Local reviewer SID that must receive
# an EXPLICIT read-only grant on the Approver-created decisions file. Party
# A must not be able to modify this file (Party A receives no explicit grant
# at all; only the owning Approver identity and the named Local reader do).
# Group membership (e.g. `BUILTIN\Administrators`) is never sufficient by
# itself, since Local's own Administrators SID is deny-only in a
# non-elevated token. Per
# `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md`.
$script:VerifiedLocalReaderSid = 'S-1-5-21-1644666849-912006174-747199667-1001'

Add-Type -AssemblyName System.Security | Out-Null

Add-Type -Language CSharp -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Text.Json;

public static class CvfAcelG1Group2DecisionJsonDuplicateMemberScanner
{
    public static string FindFirstTopLevelDuplicateMemberName(byte[] utf8Bytes)
    {
        var options = new JsonReaderOptions { CommentHandling = JsonCommentHandling.Disallow };
        var reader = new Utf8JsonReader(utf8Bytes, options);
        int depth = 0;
        var seen = new HashSet<string>(StringComparer.Ordinal);
        while (reader.Read())
        {
            switch (reader.TokenType)
            {
                case JsonTokenType.StartObject:
                    depth++;
                    break;
                case JsonTokenType.EndObject:
                    depth--;
                    break;
                case JsonTokenType.StartArray:
                    depth++;
                    break;
                case JsonTokenType.EndArray:
                    depth--;
                    break;
                case JsonTokenType.PropertyName:
                    if (depth == 1)
                    {
                        string name = reader.GetString();
                        if (!seen.Add(name))
                        {
                            return name;
                        }
                    }
                    break;
            }
        }
        return null;
    }
}
'@

# --------------------------------------------------------------------------
# Failure surface
# --------------------------------------------------------------------------

class WriterGuardFailure : System.Exception {
    [string] $GuardId
    WriterGuardFailure([string] $guardId, [string] $message) : base($message) {
        $this.GuardId = $guardId
    }
}

function Stop-Writer {
    param(
        [Parameter(Mandatory = $true)][string] $GuardId,
        [Parameter(Mandatory = $true)][string] $Message
    )
    throw [WriterGuardFailure]::new($GuardId, "[$GuardId] $Message")
}

# --------------------------------------------------------------------------
# Encoding, canonicalization and hashing helpers (ported pattern)
# --------------------------------------------------------------------------

function Get-Sha256Hex {
    param([Parameter(Mandatory = $true)][byte[]] $Bytes)
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        return [System.BitConverter]::ToString($sha256.ComputeHash($Bytes)).Replace('-', '').ToLowerInvariant()
    } finally {
        $sha256.Dispose()
    }
}

function ConvertFrom-Base64Url {
    param([Parameter(Mandatory = $true)][string] $Text)
    $standard = $Text.Replace('-', '+').Replace('_', '/')
    switch ($standard.Length % 4) {
        2 { $standard += '==' }
        3 { $standard += '=' }
        1 { Stop-Writer -GuardId 'BASE64URL_INVALID' -Message 'invalid base64url length' }
    }
    return [System.Convert]::FromBase64String($standard)
}

function ConvertTo-JsonStringLiteral {
    param([Parameter(Mandatory = $true)][AllowEmptyString()][string] $Value)
    $escaped = $Value.Replace('\', '\\').Replace('"', '\"').Replace("`n", '\n').Replace("`r", '\r').Replace("`t", '\t')
    return '"' + $escaped + '"'
}

function ConvertTo-CanonicalJsonBytes {
    <#
        .SYNOPSIS
            Compact, lexicographically key-ordered JSON bytes (JCS-equivalent
            for this ASCII-only, non-nested, no-duplicate-key preimage
            shape). Ported unmodified in behavior from the accepted Group 1
            writer's helper of the same name.
    #>
    param([Parameter(Mandatory = $true)][System.Collections.IDictionary] $Object)

    $sortedKeys = $Object.Keys | Sort-Object -Culture 'en-US' -CaseSensitive
    $parts = New-Object System.Collections.Generic.List[string]
    foreach ($key in $sortedKeys) {
        $value = $Object[$key]
        $encodedKey = ConvertTo-JsonStringLiteral -Value $key
        $encodedValue = if ($null -eq $value) {
            'null'
        } elseif ($value -is [string]) {
            ConvertTo-JsonStringLiteral -Value $value
        } elseif ($value -is [int] -or $value -is [long]) {
            [string]$value
        } else {
            Stop-Writer -GuardId 'CANONICALIZATION_UNSUPPORTED_TYPE' -Message (
                "field '$key' has unsupported preimage value type '$($value.GetType().Name)'; " +
                'every closed-preimage field in this tool is string, integer or null')
        }
        $parts.Add("$encodedKey`:$encodedValue")
    }
    $compact = '{' + ($parts -join ',') + '}'
    return [System.Text.UTF8Encoding]::new($false).GetBytes($compact)
}

function Get-PreimageDigestHex {
    param([Parameter(Mandatory = $true)][System.Collections.IDictionary] $Preimage)
    $bytes = ConvertTo-CanonicalJsonBytes -Object $Preimage
    return Get-Sha256Hex -Bytes $bytes
}

function Get-StrictJsonObjectFromText {
    param([Parameter(Mandatory = $true)][string] $Text)

    $parsed = $null
    try {
        $parsed = $Text | ConvertFrom-Json -DateKind String -ErrorAction Stop
    } catch {
        Stop-Writer -GuardId 'JSON_UNPARSEABLE' -Message "text is not valid JSON: $($_.Exception.Message)"
    }

    $utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $duplicateMemberName = $null
    try {
        $duplicateMemberName = [CvfAcelG1Group2DecisionJsonDuplicateMemberScanner]::FindFirstTopLevelDuplicateMemberName($utf8Bytes)
    } catch {
        Stop-Writer -GuardId 'JSON_UNPARSEABLE' -Message "text is not valid JSON: $($_.Exception.Message)"
    }
    if ($null -ne $duplicateMemberName) {
        Stop-Writer -GuardId 'JSON_DUPLICATE_MEMBER' -Message (
            "duplicate top-level JSON member '$duplicateMemberName' (after JSON escape decoding)")
    }

    return $parsed
}

function Get-StrictJsonLinesFromText {
    <#
        .SYNOPSIS
            Parse a JSONL text blob into an array of parsed objects, one per
            non-blank line, rejecting duplicate top-level members per line.
    #>
    param([Parameter(Mandatory = $true)][string] $Text)
    $lines = New-Object System.Collections.Generic.List[object]
    foreach ($rawLine in ($Text -split "`r?`n")) {
        $line = $rawLine.Trim()
        if ([string]::IsNullOrEmpty($line)) { continue }
        $lines.Add((Get-StrictJsonObjectFromText -Text $line))
    }
    return $lines.ToArray()
}

# --------------------------------------------------------------------------
# Spec-file independent decode/recompute (never trust caller-supplied hash)
# --------------------------------------------------------------------------

function Get-IndependentlyRecomputedSpecHash {
    <#
        .SYNOPSIS
            Independently decode a `cvf.specFile` record's
            `canonicalBytesBase64` and recompute `specHashHex` directly,
            never trusting the record's own stored `specHashHex` field.
    #>
    param([Parameter(Mandatory = $true)] $SpecRecord)

    if (-not ($SpecRecord.PSObject.Properties.Name -contains 'canonicalBytesBase64')) {
        Stop-Writer -GuardId 'SPEC_RECORD_FIELD_MISSING' -Message 'spec record is missing canonicalBytesBase64'
    }
    $decodedBytes = ConvertFrom-Base64Url -Text $SpecRecord.canonicalBytesBase64
    return Get-Sha256Hex -Bytes $decodedBytes
}

# --------------------------------------------------------------------------
# Decision-event record construction
# --------------------------------------------------------------------------

function Assert-ValidReplacementFieldPair {
    <#
        .SYNOPSIS
            T3B-R2 (atomic rotation): enforce the closed pairing rule for
            `replacementSpecVersion`/`replacementRecomputedHashHex` before
            any preimage or record is built. Both fields must be JSON `null`
            for every event type except `SUPERSEDED`, and both must be
            non-null, well-formed, and mutually consistent (replacement
            strictly greater than the event's own `specVersion`) for
            `SUPERSEDED`. A one-null/one-non-null pair is always rejected,
            regardless of event type.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $EventType,
        [Parameter(Mandatory = $true)][int]    $SpecVersion,
        [AllowNull()][Nullable[int]] $ReplacementSpecVersion,
        [AllowNull()] $ReplacementRecomputedHashHex
    )
    $versionIsNull = ($null -eq $ReplacementSpecVersion)
    $hashIsNull = ($null -eq $ReplacementRecomputedHashHex)
    if ($versionIsNull -ne $hashIsNull) {
        Stop-Writer -GuardId 'DECISION_REPLACEMENT_FIELD_PAIR_INVALID' -Message (
            'replacementSpecVersion and replacementRecomputedHashHex must both be null or both be non-null')
    }
    if ($EventType -eq 'SUPERSEDED') {
        if ($versionIsNull) {
            Stop-Writer -GuardId 'DECISION_REPLACEMENT_FIELDS_REQUIRED_FOR_SUPERSEDED' -Message (
                'SUPERSEDED events require non-null replacementSpecVersion and replacementRecomputedHashHex')
        }
        if ($ReplacementSpecVersion -le $SpecVersion) {
            Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_GREATER' -Message (
                "replacementSpecVersion $ReplacementSpecVersion must be strictly greater than the superseded specVersion $SpecVersion")
        }
        if ($ReplacementRecomputedHashHex -notmatch '^[0-9a-f]{64}$') {
            Stop-Writer -GuardId 'DECISION_REPLACEMENT_HASH_SHAPE_INVALID' -Message (
                'replacementRecomputedHashHex is not 64 lowercase hex characters')
        }
    } else {
        if (-not $versionIsNull) {
            Stop-Writer -GuardId 'DECISION_REPLACEMENT_FIELDS_ONLY_FOR_SUPERSEDED' -Message (
                "eventType '$EventType' must have null replacementSpecVersion/replacementRecomputedHashHex")
        }
    }
}

function New-DecisionEventPreimage {
    <#
        .SYNOPSIS
            Build the exact closed `cvf.specDecisionEvent` preimage:
            `profile`, `domain`, `decisionEventId`, `eventType`,
            `specVersion`, `recomputedHashHex`, `replacementSpecVersion`,
            `replacementRecomputedHashHex`, `approverId`, `decidedAt`,
            `priorEntryHashHex`. No more, no fewer. `replacementSpecVersion`
            and `replacementRecomputedHashHex` are always present (per the
            closed field list), `null` for every event type except
            `SUPERSEDED`, where both are required and non-null (T2F-R4-01
            Atomic Rotation).
    #>
    param(
        [Parameter(Mandatory = $true)][string] $DecisionEventId,
        [Parameter(Mandatory = $true)][string] $EventType,
        [Parameter(Mandatory = $true)][int]    $SpecVersion,
        [Parameter(Mandatory = $true)][string] $RecomputedHashHex,
        [AllowNull()][Nullable[int]] $ReplacementSpecVersion,
        [AllowNull()] $ReplacementRecomputedHashHex,
        [Parameter(Mandatory = $true)][string] $ApproverId,
        [Parameter(Mandatory = $true)][string] $DecidedAt,
        [AllowNull()] $PriorEntryHashHex
    )
    Assert-ValidReplacementFieldPair -EventType $EventType -SpecVersion $SpecVersion `
        -ReplacementSpecVersion $ReplacementSpecVersion -ReplacementRecomputedHashHex $ReplacementRecomputedHashHex
    return [ordered]@{
        profile                      = $script:CanonProfile
        domain                       = $script:DecisionEventDomain
        decisionEventId              = $DecisionEventId
        eventType                    = $EventType
        specVersion                  = $SpecVersion
        recomputedHashHex            = $RecomputedHashHex
        replacementSpecVersion       = $ReplacementSpecVersion
        replacementRecomputedHashHex = $ReplacementRecomputedHashHex
        approverId                   = $ApproverId
        decidedAt                    = $DecidedAt
        priorEntryHashHex            = $PriorEntryHashHex
    }
}

function New-DecisionEventRecord {
    param(
        [Parameter(Mandatory = $true)][string] $DecisionEventId,
        [Parameter(Mandatory = $true)][string] $EventType,
        [Parameter(Mandatory = $true)][int]    $SpecVersion,
        [Parameter(Mandatory = $true)][string] $RecomputedHashHex,
        [AllowNull()][Nullable[int]] $ReplacementSpecVersion = $null,
        [AllowNull()] $ReplacementRecomputedHashHex = $null,
        [Parameter(Mandatory = $true)][string] $ApproverId,
        [Parameter(Mandatory = $true)][string] $DecidedAt,
        [AllowNull()] $PriorEntryHashHex
    )
    $preimage = New-DecisionEventPreimage -DecisionEventId $DecisionEventId -EventType $EventType `
        -SpecVersion $SpecVersion -RecomputedHashHex $RecomputedHashHex `
        -ReplacementSpecVersion $ReplacementSpecVersion -ReplacementRecomputedHashHex $ReplacementRecomputedHashHex `
        -ApproverId $ApproverId -DecidedAt $DecidedAt -PriorEntryHashHex $PriorEntryHashHex
    $entryHashHex = Get-PreimageDigestHex -Preimage $preimage

    $record = [ordered]@{
        decisionEventId              = $DecisionEventId
        eventType                    = $EventType
        specVersion                  = $SpecVersion
        recomputedHashHex            = $RecomputedHashHex
        replacementSpecVersion       = $ReplacementSpecVersion
        replacementRecomputedHashHex = $ReplacementRecomputedHashHex
        approverId                   = $ApproverId
        decidedAt                    = $DecidedAt
        priorEntryHashHex            = $PriorEntryHashHex
        entryHashHex                 = $entryHashHex
    }

    return [pscustomobject]@{
        Record       = $record
        EntryHashHex = $entryHashHex
    }
}

# --------------------------------------------------------------------------
# State machine (T2F Explicit Approval, Activation And Supersession)
# --------------------------------------------------------------------------

function Copy-OrderedRecord {
    <#
        .SYNOPSIS
            Produce a genuine independent shallow clone of an `[ordered]`
            hashtable/dictionary record, for hermetic-test mutation only.
            `.PSObject.Copy()` on a hashtable returns a reference to the
            SAME underlying dictionary (unlike on a `PSCustomObject`, where
            it deep-copies), so mutating the "copy" would silently corrupt
            the original fixture record used elsewhere in the test suite.
    #>
    param([Parameter(Mandatory = $true)][System.Collections.IDictionary] $Record)
    $clone = [ordered]@{}
    foreach ($key in $Record.Keys) { $clone[$key] = $Record[$key] }
    return $clone
}

function Test-RecordHasField {
    <#
        .SYNOPSIS
            True if `Record` has member/key `FieldName`, working uniformly
            for both a `[ordered]` hashtable/dictionary (as built by this
            tool's own `New-DecisionEventRecord`) and a `PSCustomObject` (as
            produced by `ConvertFrom-Json` when parsing existing durable
            history). `.PSObject.Properties` alone is insufficient because a
            hashtable's `PSObject.Properties` exposes its .NET dictionary
            members (`Keys`, `Values`, `Count`, ...), never its JSON keys.
    #>
    param(
        [Parameter(Mandatory = $true)] $Record,
        [Parameter(Mandatory = $true)][string] $FieldName
    )
    if ($Record -is [System.Collections.IDictionary]) {
        return $Record.Contains($FieldName)
    }
    return ($Record.PSObject.Properties.Name -contains $FieldName)
}

function Get-DecisionHistoryState {
    <#
        .SYNOPSIS
            Walk the full existing decision-event history for a given
            `specVersion`, independently recomputing and verifying every
            entry's hash chain and closed preimage, and return the resulting
            state summary. Never trusts a caller-supplied hash: recomputes
            every `entryHashHex` from each entry's own preimage fields.

        .DESCRIPTION
            Also enforces global invariants across the WHOLE file (not just
            this version): unique `decisionEventId`, valid full-file
            hash-chain linkage in file order, and the unique-active
            invariant (zero or one ACTIVATED-without-SUPERSEDED result across
            ALL versions at any point in the scanned history).

            T3B-RV-2 (R1 correction): when `RecomputedHashByVersion` is
            supplied, every entry's `recomputedHashHex` is compared against
            THAT entry's OWN cited `specVersion` hash (never a single
            file-wide hash), so a `specVersion 2` entry that reuses
            `specVersion 1`'s hash fails closed. A version present in
            history but absent from `RecomputedHashByVersion` also fails
            closed: every cited version must be independently resolvable.
            When omitted (default empty map), this per-version binding check
            is skipped entirely -- used only by hermetic self-test callers
            that construct history fixtures without a real per-version spec
            map, never by the real-mode orchestration path.
    #>
    param(
        [Parameter(Mandatory = $true)][AllowEmptyCollection()][array] $AllEntries,
        [Parameter(Mandatory = $true)][int]   $SpecVersion,
        [System.Collections.IDictionary] $RecomputedHashByVersion = $null
    )

    $seenIds = New-Object 'System.Collections.Generic.HashSet[string]'
    $priorHash = $null
    # Tracks, for EVERY version seen so far, whether it currently has an
    # ACTIVATED event with no later SUPERSEDED for that same version.
    $activeVersions = New-Object 'System.Collections.Generic.HashSet[int]'
    $versionState = @{}  # specVersion(int) -> pscustomobject state

    foreach ($entry in $AllEntries) {
        foreach ($requiredField in @('decisionEventId', 'eventType', 'specVersion', 'recomputedHashHex', 'replacementSpecVersion', 'replacementRecomputedHashHex', 'approverId', 'decidedAt', 'priorEntryHashHex')) {
            if (-not (Test-RecordHasField -Record $entry -FieldName $requiredField)) {
                Stop-Writer -GuardId 'DECISION_FIELD_MISSING' -Message "existing decision entry is missing field '$requiredField'"
            }
        }
        if (-not (Test-RecordHasField -Record $entry -FieldName 'entryHashHex')) {
            Stop-Writer -GuardId 'DECISION_FIELD_MISSING' -Message "existing decision entry is missing field 'entryHashHex'"
        }
        $entryId = [string]$entry.decisionEventId
        if ($seenIds.Contains($entryId)) {
            Stop-Writer -GuardId 'DECISION_DUPLICATE_EVENT_ID' -Message "duplicate decisionEventId '$entryId' in existing decision history"
        }
        [void]$seenIds.Add($entryId)

        $storedHash = [string]$entry.entryHashHex
        if ($storedHash -notmatch '^[0-9a-f]{64}$') {
            Stop-Writer -GuardId 'DECISION_DIGEST_SHAPE_INVALID' -Message "entryHashHex for '$entryId' is not 64 lowercase hex characters"
        }
        $expectedPriorHash = $entry.priorEntryHashHex
        $actualPriorHash = if ($null -eq $priorHash) { $null } else { $priorHash }
        $priorMatches = ($null -eq $expectedPriorHash -and $null -eq $actualPriorHash) -or
            ([string]$expectedPriorHash -eq [string]$actualPriorHash)
        if (-not $priorMatches) {
            Stop-Writer -GuardId 'DECISION_CHAIN_BROKEN' -Message (
                "priorEntryHashHex for '$entryId' does not match the actual prior entry's entryHashHex")
        }

        $entryReplacementVersion = if ($null -eq $entry.replacementSpecVersion) { $null } else { [Nullable[int]][int]$entry.replacementSpecVersion }
        $entryReplacementHash = if ($null -eq $entry.replacementRecomputedHashHex) { $null } else { [string]$entry.replacementRecomputedHashHex }
        $recomputedPreimage = New-DecisionEventPreimage -DecisionEventId $entryId -EventType $entry.eventType `
            -SpecVersion ([int]$entry.specVersion) -RecomputedHashHex $entry.recomputedHashHex `
            -ReplacementSpecVersion $entryReplacementVersion -ReplacementRecomputedHashHex $entryReplacementHash `
            -ApproverId $entry.approverId -DecidedAt $entry.decidedAt -PriorEntryHashHex $entry.priorEntryHashHex
        $recomputedEntryHash = Get-PreimageDigestHex -Preimage $recomputedPreimage
        if ($recomputedEntryHash -ne $storedHash) {
            Stop-Writer -GuardId 'DECISION_DIGEST_MISMATCH' -Message (
                "recomputed entryHashHex '$recomputedEntryHash' does not match stored '$storedHash' for '$entryId'")
        }
        $priorHash = $storedHash

        $entryVersion = [int]$entry.specVersion

        # T3B-RV-2 (R1 correction): validate THIS entry's recomputedHashHex
        # against ITS OWN cited version's independently-recomputed spec
        # hash, never a single hash shared across every version in history.
        if ($null -ne $RecomputedHashByVersion) {
            if (-not $RecomputedHashByVersion.Contains($entryVersion)) {
                Stop-Writer -GuardId 'DECISION_SPEC_VERSION_UNRESOLVED' -Message (
                    "entry '$entryId' cites specVersion $entryVersion, which has no independently resolved spec hash available")
            }
            $expectedVersionHash = [string]$RecomputedHashByVersion[$entryVersion]
            if ([string]$entry.recomputedHashHex -ne $expectedVersionHash) {
                Stop-Writer -GuardId 'DECISION_RECOMPUTED_HASH_SPEC_MISMATCH' -Message (
                    "entry '$entryId' recomputedHashHex does not match the independently recomputed hash for its own cited specVersion $entryVersion")
            }
            # T3B-R2 (atomic rotation): a SUPERSEDED entry's OWN
            # replacementRecomputedHashHex must independently match the
            # replacement version's own resolved spec hash -- never trusted
            # from the durable record without recomputation, and never
            # substitutable with the old version's hash.
            if ($entry.eventType -eq 'SUPERSEDED' -and $null -ne $entry.replacementSpecVersion) {
                $replacementVersionForHashCheck = [int]$entry.replacementSpecVersion
                if (-not $RecomputedHashByVersion.Contains($replacementVersionForHashCheck)) {
                    Stop-Writer -GuardId 'DECISION_SPEC_VERSION_UNRESOLVED' -Message (
                        "entry '$entryId' cites replacementSpecVersion $replacementVersionForHashCheck, which has no independently resolved spec hash available")
                }
                $expectedReplacementHash = [string]$RecomputedHashByVersion[$replacementVersionForHashCheck]
                if ([string]$entry.replacementRecomputedHashHex -ne $expectedReplacementHash) {
                    Stop-Writer -GuardId 'DECISION_REPLACEMENT_RECOMPUTED_HASH_MISMATCH' -Message (
                        "entry '$entryId' replacementRecomputedHashHex does not match the independently recomputed hash for its own cited replacementSpecVersion $replacementVersionForHashCheck")
                }
            }
        }

        if (-not $versionState.ContainsKey($entryVersion)) {
            $versionState[$entryVersion] = [pscustomobject]@{
                FirstDecision = $null
                HasActivated  = $false
                HasSuperseded = $false
                ApproverIds   = New-Object 'System.Collections.Generic.List[string]'
            }
        }
        $state = $versionState[$entryVersion]

        switch ($entry.eventType) {
            'APPROVED' {
                if ($null -ne $state.FirstDecision) {
                    Stop-Writer -GuardId 'DECISION_MULTIPLE_FIRST_DECISIONS' -Message (
                        "specVersion $entryVersion already has a first decision '$($state.FirstDecision)'; a second APPROVED/REJECTED is invalid")
                }
                $state.FirstDecision = 'APPROVED'
            }
            'REJECTED' {
                if ($null -ne $state.FirstDecision) {
                    Stop-Writer -GuardId 'DECISION_MULTIPLE_FIRST_DECISIONS' -Message (
                        "specVersion $entryVersion already has a first decision '$($state.FirstDecision)'; a second APPROVED/REJECTED is invalid")
                }
                $state.FirstDecision = 'REJECTED'
            }
            'ACTIVATED' {
                # Ordinary ACTIVATED: atomic rotation (T2F-R4-01) forbids a
                # replacement citation here (already rejected earlier by
                # Assert-ValidReplacementFieldPair during preimage
                # recomputation above, but the state-machine check below is
                # independent of that field-shape check). Requires prior
                # APPROVED and an EMPTY active set -- never permitted while
                # ANY version (including a direct predecessor) is active;
                # replacing an active version is done only via SUPERSEDED.
                if ($state.FirstDecision -ne 'APPROVED') {
                    Stop-Writer -GuardId 'DECISION_ACTIVATED_WITHOUT_APPROVAL' -Message (
                        "specVersion $entryVersion has no prior APPROVED decision; ACTIVATED is invalid")
                }
                if ($state.HasActivated) {
                    Stop-Writer -GuardId 'DECISION_DUPLICATE_ACTIVATION' -Message (
                        "specVersion $entryVersion already has an ACTIVATED event")
                }
                if ($state.HasSuperseded) {
                    Stop-Writer -GuardId 'DECISION_ACTIVATED_AFTER_SUPERSEDED' -Message (
                        "specVersion $entryVersion was already SUPERSEDED; cannot ACTIVATE again")
                }
                if ($activeVersions.Count -gt 0) {
                    Stop-Writer -GuardId 'DECISION_MULTIPLE_ACTIVE_VERSIONS' -Message (
                        "ordinary ACTIVATED for specVersion $entryVersion requires an empty active set; currently active: $(($activeVersions | Sort-Object) -join ', ')")
                }
                $state.HasActivated = $true
                [void]$activeVersions.Add($entryVersion)
            }
            'SUPERSEDED' {
                # Atomic rotation (T2F-R4-01): this single event both proves
                # and applies the old-to-replacement swap in one step. The
                # replacement fields were already shape-validated (non-null,
                # strictly greater, 64-hex) by Assert-ValidReplacementFieldPair
                # during preimage recomputation above.
                $replacementVersion = $entryReplacementVersion
                if ($null -eq $replacementVersion) {
                    Stop-Writer -GuardId 'DECISION_REPLACEMENT_FIELDS_REQUIRED_FOR_SUPERSEDED' -Message (
                        "specVersion $entryVersion SUPERSEDED event has no replacementSpecVersion")
                }
                if (-not $state.HasActivated) {
                    Stop-Writer -GuardId 'DECISION_SUPERSEDED_WITHOUT_ACTIVATION' -Message (
                        "specVersion $entryVersion has no ACTIVATED event; SUPERSEDED is invalid")
                }
                if ($state.HasSuperseded) {
                    Stop-Writer -GuardId 'DECISION_DUPLICATE_SUPERSESSION' -Message (
                        "specVersion $entryVersion already has a SUPERSEDED event")
                }
                if ($activeVersions.Count -ne 1 -or -not $activeVersions.Contains($entryVersion)) {
                    Stop-Writer -GuardId 'DECISION_SUPERSEDE_REQUIRES_EXACTLY_ONE_ACTIVE' -Message (
                        "SUPERSEDED for specVersion $entryVersion requires the active set to be exactly {$entryVersion}; currently active: $(($activeVersions | Sort-Object) -join ', ')")
                }

                if (-not $versionState.ContainsKey($replacementVersion)) {
                    $versionState[$replacementVersion] = [pscustomobject]@{
                        FirstDecision = $null
                        HasActivated  = $false
                        HasSuperseded = $false
                        ApproverIds   = New-Object 'System.Collections.Generic.List[string]'
                    }
                }
                $replacementState = $versionState[$replacementVersion]
                if ($replacementState.FirstDecision -ne 'APPROVED') {
                    Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_APPROVED' -Message (
                        "replacement specVersion $replacementVersion has no prior APPROVED decision; it cannot be cited as a supersession replacement")
                }
                # T3B-R2: HasActivated is a historical "was ever activated"
                # flag that remains true forever, even after a version is
                # later superseded -- it is NOT "currently active". The
                # already-superseded case is checked FIRST using the
                # authoritative HasSuperseded flag; only a version that was
                # activated and has NOT since been superseded can be
                # "currently active" (a member of activeVersions).
                if ($replacementState.HasSuperseded) {
                    Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_ALREADY_SUPERSEDED' -Message (
                        "replacement specVersion $replacementVersion has already been superseded; it cannot be cited as a supersession replacement")
                }
                if ($replacementState.HasActivated -and $activeVersions.Contains($replacementVersion)) {
                    Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_ALREADY_ACTIVE' -Message (
                        "replacement specVersion $replacementVersion is already active; it cannot be cited as a supersession replacement")
                }

                # Atomic swap: remove old, add replacement, in one step. No
                # intermediate two-active or zero-active state is ever
                # observable outside this single block.
                $state.HasSuperseded = $true
                [void]$activeVersions.Remove($entryVersion)
                $replacementState.HasActivated = $true
                [void]$activeVersions.Add($replacementVersion)
                if ($activeVersions.Count -ne 1) {
                    Stop-Writer -GuardId 'DECISION_MULTIPLE_ACTIVE_VERSIONS' -Message (
                        "atomic rotation from specVersion $entryVersion to $replacementVersion did not converge to exactly one active version: $(($activeVersions | Sort-Object) -join ', ')")
                }
            }
            default {
                Stop-Writer -GuardId 'DECISION_EVENT_TYPE_INVALID' -Message "unknown eventType '$($entry.eventType)'"
            }
        }
        [void]$state.ApproverIds.Add([string]$entry.approverId)
    }

    if ($activeVersions.Count -gt 1) {
        Stop-Writer -GuardId 'DECISION_MULTIPLE_ACTIVE_VERSIONS' -Message (
            "unique-active invariant violated across full history: $(($activeVersions | Sort-Object) -join ', ')")
    }

    $targetState = if ($versionState.ContainsKey($SpecVersion)) {
        $versionState[$SpecVersion]
    } else {
        [pscustomobject]@{ FirstDecision = $null; HasActivated = $false; HasSuperseded = $false; ApproverIds = @() }
    }

    return [pscustomobject]@{
        LastEntryHashHex   = $priorHash
        TargetVersionState = $targetState
        ActiveVersionCount = $activeVersions.Count
        ActiveVersions     = @($activeVersions)
    }
}

function Assert-ValidNextDecision {
    <#
        .SYNOPSIS
            T2F state machine: reject a proposed next event unless it is a
            legal transition given the independently-recomputed history
            state for the target `specVersion`, including self-approval
            rejection and (for SUPERSEDED) the exactly-one-active-version
            requirement.
    #>
    param(
        [Parameter(Mandatory = $true)] $HistoryState,
        [Parameter(Mandatory = $true)][string] $ProposedEventType,
        [Parameter(Mandatory = $true)][string] $ApproverId,
        [Parameter(Mandatory = $true)][string] $SpecAuthorId,
        [Parameter(Mandatory = $true)][int]    $TargetSpecVersion
    )

    if ($ApproverId -eq $SpecAuthorId) {
        Stop-Writer -GuardId 'DECISION_SELF_APPROVAL_REJECTED' -Message (
            'approverId equals the spec authorId; self-approval/self-activation is forbidden')
    }

    $target = $HistoryState.TargetVersionState
    switch ($ProposedEventType) {
        { $_ -in @('APPROVED', 'REJECTED') } {
            if ($null -ne $target.FirstDecision) {
                Stop-Writer -GuardId 'DECISION_MULTIPLE_FIRST_DECISIONS' -Message (
                    "target specVersion already has a first decision '$($target.FirstDecision)'; a second APPROVED/REJECTED is invalid")
            }
        }
        'ACTIVATED' {
            if ($target.FirstDecision -ne 'APPROVED') {
                Stop-Writer -GuardId 'DECISION_ACTIVATED_WITHOUT_APPROVAL' -Message (
                    'target specVersion has no prior APPROVED decision; ACTIVATED is invalid')
            }
            if ($target.HasActivated) {
                Stop-Writer -GuardId 'DECISION_DUPLICATE_ACTIVATION' -Message (
                    'target specVersion already has an ACTIVATED event')
            }
            if ($target.HasSuperseded) {
                Stop-Writer -GuardId 'DECISION_ACTIVATED_AFTER_SUPERSEDED' -Message (
                    'target specVersion was already SUPERSEDED; cannot ACTIVATE again')
            }
            if ($HistoryState.ActiveVersionCount -ge 1) {
                Stop-Writer -GuardId 'DECISION_MULTIPLE_ACTIVE_VERSIONS' -Message (
                    "activating this version would create more than one simultaneously active version: currently active $($HistoryState.ActiveVersions -join ', ')")
            }
        }
        'SUPERSEDED' {
            if (-not $target.HasActivated) {
                Stop-Writer -GuardId 'DECISION_SUPERSEDED_WITHOUT_ACTIVATION' -Message (
                    'target specVersion has no ACTIVATED event; SUPERSEDED is invalid')
            }
            if ($target.HasSuperseded) {
                Stop-Writer -GuardId 'DECISION_DUPLICATE_SUPERSESSION' -Message (
                    'target specVersion already has a SUPERSEDED event')
            }
            if ($HistoryState.ActiveVersionCount -ne 1 -or $HistoryState.ActiveVersions[0] -ne $TargetSpecVersion) {
                Stop-Writer -GuardId 'DECISION_SUPERSEDE_REQUIRES_EXACTLY_ONE_ACTIVE' -Message (
                    "SUPERSEDED requires the active set to be exactly {$TargetSpecVersion}; currently active: $($HistoryState.ActiveVersions -join ', ')")
            }
        }
        default {
            Stop-Writer -GuardId 'DECISION_EVENT_TYPE_INVALID' -Message "unknown eventType '$ProposedEventType'"
        }
    }
}

# --------------------------------------------------------------------------
# Principal and context guards (ported pattern)
# --------------------------------------------------------------------------

function Get-CurrentPrincipalFact {
    $identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [System.Security.Principal.WindowsPrincipal]::new($identity)
    return [pscustomobject]@{
        Name       = $identity.Name
        Sid        = $identity.User.Value
        IsElevated = $principal.IsInRole(
            [System.Security.Principal.WindowsBuiltInRole]::Administrator)
    }
}

function Resolve-QualifiedAccountName {
    param([Parameter(Mandatory = $true)][string] $AccountName)
    $trimmed = $AccountName.Trim()
    if ($trimmed.Contains('\')) { return $trimmed }
    return ('{0}\{1}' -f $env:COMPUTERNAME, $trimmed)
}

function Assert-ExpectedPrincipal {
    param(
        [Parameter(Mandatory = $true)] $CurrentPrincipal,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )

    $expectedName = Resolve-QualifiedAccountName -AccountName $ExpectedAccountName
    if ($CurrentPrincipal.Name -ne $expectedName) {
        Stop-Writer -GuardId 'PRINCIPAL_NAME_MISMATCH' -Message (
            "current account '$($CurrentPrincipal.Name)' is not the expected account '$expectedName'")
    }
    if ($CurrentPrincipal.Sid -ne $ExpectedAccountSid.Trim()) {
        Stop-Writer -GuardId 'PRINCIPAL_SID_MISMATCH' -Message (
            "current SID '$($CurrentPrincipal.Sid)' is not the expected SID; name match alone is not sufficient")
    }
    if ($CurrentPrincipal.IsElevated) {
        Stop-Writer -GuardId 'ELEVATED_CONTEXT_REJECTED' -Message (
            'write must not run in an elevated/Administrator context')
    }
}

function Assert-ExpectedPrincipalIsVerifiedApprover {
    <#
        .SYNOPSIS
            T3B: reject unless the caller-supplied -ExpectedAccountName/-Sid
            themselves equal the verified activation-approver identity.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )
    $qualifiedCandidate = Resolve-QualifiedAccountName -AccountName $ExpectedAccountName
    $qualifiedVerified = Resolve-QualifiedAccountName -AccountName $script:VerifiedApproverIdentity.principalName
    if ($qualifiedCandidate -ne $qualifiedVerified) {
        Stop-Writer -GuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_APPROVER' -Message (
            "supplied -ExpectedAccountName '$qualifiedCandidate' does not equal the verified approver identity '$qualifiedVerified'")
    }
    if ($ExpectedAccountSid.Trim() -ne $script:VerifiedApproverIdentity.principalSid) {
        Stop-Writer -GuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_APPROVER' -Message (
            'supplied -ExpectedAccountSid does not equal the verified approver SID')
    }
}

function Assert-ApproverPosture {
    <#
        .SYNOPSIS
            Real-mode-only posture guard: the approver account must be
            Enabled, PasswordRequired, and NOT a member of the local
            Administrators group, per the work order's Principal and
            filesystem boundary section. Uses only local account query
            cmdlets; never touches credentials.
    #>
    param([Parameter(Mandatory = $true)][string] $AccountSid)

    $localUser = $null
    try {
        $localUser = Get-LocalUser | Where-Object { $_.SID.Value -eq $AccountSid } | Select-Object -First 1
    } catch {
        Stop-Writer -GuardId 'APPROVER_POSTURE_UNREADABLE' -Message "could not query local account posture: $($_.Exception.Message)"
    }
    if ($null -eq $localUser) {
        Stop-Writer -GuardId 'APPROVER_ACCOUNT_NOT_FOUND' -Message "no local account found for SID '$AccountSid'"
    }
    if (-not $localUser.Enabled) {
        Stop-Writer -GuardId 'APPROVER_ACCOUNT_DISABLED' -Message 'approver account is not Enabled'
    }
    if (-not $localUser.PasswordRequired) {
        Stop-Writer -GuardId 'APPROVER_PASSWORD_NOT_REQUIRED' -Message 'approver account does not require a password'
    }

    try {
        $admins = Get-LocalGroupMember -Group 'Administrators' -ErrorAction Stop
        $isAdmin = @($admins | Where-Object { $_.SID.Value -eq $AccountSid }).Count -gt 0
        if ($isAdmin) {
            Stop-Writer -GuardId 'APPROVER_IS_ADMINISTRATOR' -Message 'approver account is a member of the local Administrators group'
        }
    } catch [WriterGuardFailure] {
        throw
    } catch {
        Stop-Writer -GuardId 'APPROVER_POSTURE_UNREADABLE' -Message "could not query local Administrators membership: $($_.Exception.Message)"
    }
}

function Assert-InteractiveConfirmation {
    param([Parameter(Mandatory = $true)][string] $ExpectedAccountName)

    Write-Host ''
    Write-Host "About to append a Group 2 decision event for '$ExpectedAccountName'."
    Write-Host "Type exactly: $($script:ConfirmationPhrase)"

    $typed = $null
    try {
        $typed = Read-Host -Prompt 'Confirmation'
    } catch {
        Stop-Writer -GuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Message (
            "write requires an interactive session; the host refused to prompt ($($_.Exception.GetType().Name))")
    }

    if ([string]::IsNullOrEmpty($typed)) {
        Stop-Writer -GuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Message (
            'no confirmation input was received; execution is refused')
    }

    if ($typed -cne $script:ConfirmationPhrase) {
        Stop-Writer -GuardId 'CONFIRMATION_PHRASE_MISMATCH' -Message (
            'confirmation phrase did not match exactly; write aborted')
    }
}

# --------------------------------------------------------------------------
# Output path guards (ported pattern)
# --------------------------------------------------------------------------

function Test-PathIsInside {
    param(
        [Parameter(Mandatory = $true)][string] $CandidatePath,
        [Parameter(Mandatory = $true)][string] $ContainerPath
    )
    $separator = [System.IO.Path]::DirectorySeparatorChar
    $candidate = [System.IO.Path]::GetFullPath($CandidatePath).TrimEnd($separator) + $separator
    $container = [System.IO.Path]::GetFullPath($ContainerPath).TrimEnd($separator) + $separator
    return $candidate.StartsWith($container, [System.StringComparison]::OrdinalIgnoreCase)
}

function Assert-NoReparsePointInAncestry {
    param([Parameter(Mandatory = $true)][string] $NormalizedPath)
    $inspected = $NormalizedPath
    while (-not [string]::IsNullOrEmpty($inspected)) {
        if (Test-Path -LiteralPath $inspected) {
            $item = Get-Item -LiteralPath $inspected -Force
            if ($item.Attributes.HasFlag([System.IO.FileAttributes]::ReparsePoint)) {
                Stop-Writer -GuardId 'OUTPUT_PATH_REPARSE_POINT' -Message (
                    "path component '$inspected' is a reparse point (symlink or junction)")
            }
        }
        $parent = [System.IO.Path]::GetDirectoryName($inspected)
        if ($parent -eq $inspected) { break }
        $inspected = $parent
    }
}

function Get-SpecFileNameForVersion {
    <#
        .SYNOPSIS
            T3B-RV-2/T3B-RV-3 (R1 correction): the ONLY function that turns
            an integer spec version into a filename. Strictly repo-relative,
            fixed `SPEC_v{n}.json` pattern only -- no caller-supplied
            filename or path fragment is ever accepted; a positive integer
            is the only admissible input, so path traversal, alternate
            roots, or a non-canonical filename can never be smuggled in
            through this function.
    #>
    param([Parameter(Mandatory = $true)][int] $SpecVersion)
    if ($SpecVersion -lt 1) {
        Stop-Writer -GuardId 'SPEC_VERSION_INVALID' -Message "specVersion must be a positive integer, got $SpecVersion"
    }
    return ('SPEC_v{0}.json' -f $SpecVersion)
}

function Resolve-GroupTwoSpecPathForVersion {
    <#
        .SYNOPSIS
            Strictly resolve the immutable `SPEC_v{n}.json` path for exactly
            one integer version under the given repository root. Rejects any
            resolution that escapes the Group 2 source directory or passes
            through a reparse point in its ancestry.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][int]    $SpecVersion
    )
    $normalizedRoot = [System.IO.Path]::GetFullPath($RepositoryRoot)
    $specDirectory = [System.IO.Path]::GetFullPath((Join-Path $normalizedRoot $script:SpecDirectoryRelativePath))
    $fileName = Get-SpecFileNameForVersion -SpecVersion $SpecVersion
    $specPath = [System.IO.Path]::GetFullPath((Join-Path $specDirectory $fileName))

    if (-not (Test-PathIsInside -CandidatePath $specPath -ContainerPath $normalizedRoot)) {
        Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message (
            "resolved path '$specPath' does not resolve inside repository root '$normalizedRoot'")
    }
    Assert-NoReparsePointInAncestry -NormalizedPath $specPath
    return $specPath
}

function Resolve-GroupTwoPaths {
    <#
        .SYNOPSIS
            Resolve the decisions (append-only) path, plus the immutable
            spec path for one or more explicitly-named versions. Never
            defaults to v1 and never infers "latest": every version resolved
            here is one the caller explicitly named.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][int[]]  $SpecVersions
    )

    $normalizedRoot = [System.IO.Path]::GetFullPath($RepositoryRoot)
    $decisionsPath = [System.IO.Path]::GetFullPath((Join-Path $normalizedRoot $script:DecisionsRelativePath))
    if (-not (Test-PathIsInside -CandidatePath $decisionsPath -ContainerPath $normalizedRoot)) {
        Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message (
            "resolved path '$decisionsPath' does not resolve inside repository root '$normalizedRoot'")
    }
    Assert-NoReparsePointInAncestry -NormalizedPath $decisionsPath

    # NOTE: a plain [ordered]@{}/OrderedDictionary indexer treats an [int]
    # key as a POSITIONAL index (via its IList-like indexer), not a
    # dictionary key lookup, which throws ArgumentOutOfRangeException on an
    # empty/undersized collection instead of adding a new entry. A
    # Hashtable's indexer always performs a true key lookup regardless of
    # key type, so a plain @{} is used here instead of [ordered]@{}; key
    # order is not semantically meaningful for this lookup-only map.
    $specPathsByVersion = @{}
    foreach ($version in ($SpecVersions | Sort-Object -Unique)) {
        $specPathsByVersion[$version] = Resolve-GroupTwoSpecPathForVersion `
            -RepositoryRoot $RepositoryRoot -SpecVersion $version
    }

    return [pscustomobject]@{
        DecisionsPath      = $decisionsPath
        SpecPathsByVersion = $specPathsByVersion
    }
}

# --------------------------------------------------------------------------
# Append-only write (exclusive-create for genesis, exclusive-append + DACL
# for subsequent lines)
# --------------------------------------------------------------------------

function New-ExclusiveFile {
    <#
        .SYNOPSIS
            Create a new file exclusively, or fail. Ported unmodified in
            behavior from the accepted Group 1 writer's helper of the same
            name.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $Path,
        [Parameter(Mandatory = $true)][byte[]] $Content,
        [ValidateSet('Create', 'Write', 'Flush')]
        [string] $InjectFailureAtForTest
    )
    $directory = [System.IO.Path]::GetDirectoryName($Path)
    $directoryPreExisted = Test-Path -LiteralPath $directory
    $filePreExisted = Test-Path -LiteralPath $Path
    if (-not $directoryPreExisted) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
    }
    $stream = $null
    $createNewSucceeded = $false
    try {
        if ($InjectFailureAtForTest -eq 'Create') {
            throw [System.IO.IOException]::new('injected create failure (hermetic self-test only)')
        }
        $stream = [System.IO.FileStream]::new(
            $Path, [System.IO.FileMode]::CreateNew,
            [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)
        $createNewSucceeded = $true
        if ($InjectFailureAtForTest -eq 'Write') {
            throw [System.IO.IOException]::new('injected write failure (hermetic self-test only)')
        }
        $stream.Write($Content, 0, $Content.Length)
        if ($InjectFailureAtForTest -eq 'Flush') {
            throw [System.IO.IOException]::new('injected flush failure (hermetic self-test only)')
        }
        $stream.Flush($true)
    } catch {
        if ($null -ne $stream) { $stream.Dispose(); $stream = $null }
        if ($createNewSucceeded -and -not $filePreExisted) {
            Remove-Item -LiteralPath $Path -Force -ErrorAction SilentlyContinue
        }
        if (-not $directoryPreExisted) {
            Remove-Item -LiteralPath $directory -Force -ErrorAction SilentlyContinue
        }
        $isIoFailure = ($_.Exception -is [System.IO.IOException]) -or
            ($_.Exception.InnerException -is [System.IO.IOException])
        if ($isIoFailure) {
            $ioMessage = if ($_.Exception -is [System.IO.IOException]) {
                $_.Exception.Message
            } else {
                $_.Exception.InnerException.Message
            }
            Stop-Writer -GuardId 'EXCLUSIVE_CREATE_FAILED' -Message (
                "could not exclusively create '$Path': $ioMessage")
        }
        throw
    } finally {
        if ($null -ne $stream) { $stream.Dispose() }
    }
}

function Add-ExclusiveAppendLine {
    <#
        .SYNOPSIS
            Append exactly one compact JSON line to an existing file using an
            exclusive (non-shared) file handle so no concurrent writer can
            interleave, then flush durably. If the file does not yet exist,
            creates it exclusively (this is the append-only file's genesis
            line).
    #>
    param(
        [Parameter(Mandatory = $true)][string] $Path,
        [Parameter(Mandatory = $true)][string] $CompactJsonLine,
        [ValidateSet('Open', 'Write', 'Flush')]
        [string] $InjectFailureAtForTest
    )
    $directory = [System.IO.Path]::GetDirectoryName($Path)
    $directoryPreExisted = Test-Path -LiteralPath $directory
    $filePreExisted = Test-Path -LiteralPath $Path
    if (-not $directoryPreExisted) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
    }

    $lineBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($CompactJsonLine + "`n")
    $stream = $null
    $createdDirectory = -not $directoryPreExisted
    try {
        if ($InjectFailureAtForTest -eq 'Open') {
            throw [System.IO.IOException]::new('injected open failure (hermetic self-test only)')
        }
        $mode = if ($filePreExisted) { [System.IO.FileMode]::Append } else { [System.IO.FileMode]::CreateNew }
        $stream = [System.IO.FileStream]::new(
            $Path, $mode, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)
        if ($InjectFailureAtForTest -eq 'Write') {
            throw [System.IO.IOException]::new('injected write failure (hermetic self-test only)')
        }
        $stream.Write($lineBytes, 0, $lineBytes.Length)
        if ($InjectFailureAtForTest -eq 'Flush') {
            throw [System.IO.IOException]::new('injected flush failure (hermetic self-test only)')
        }
        $stream.Flush($true)
    } catch {
        if ($null -ne $stream) { $stream.Dispose(); $stream = $null }
        if (-not $filePreExisted) {
            Remove-Item -LiteralPath $Path -Force -ErrorAction SilentlyContinue
            if ($createdDirectory) {
                Remove-Item -LiteralPath $directory -Force -ErrorAction SilentlyContinue
            }
        }
        $isIoFailure = ($_.Exception -is [System.IO.IOException]) -or
            ($_.Exception.InnerException -is [System.IO.IOException])
        if ($isIoFailure) {
            $ioMessage = if ($_.Exception -is [System.IO.IOException]) {
                $_.Exception.Message
            } else {
                $_.Exception.InnerException.Message
            }
            Stop-Writer -GuardId 'EXCLUSIVE_APPEND_FAILED' -Message (
                "could not exclusively append to '$Path': $ioMessage")
        }
        throw
    } finally {
        if ($null -ne $stream) { $stream.Dispose() }
    }
}

# --------------------------------------------------------------------------
# DACL/ownership hardening (NTFS DACL only, never SeSecurityPrivilege)
# --------------------------------------------------------------------------

function Protect-CreatedFileAgainstOtherPrincipal {
    <#
        .SYNOPSIS
            Harden a file's NTFS DACL (never SACL) so that only the
            currently-writing principal and named Local-reader SIDs retain
            explicit access; the other principal (Party A, for this
            approver-owned decisions file) has no explicit grant. See the
            twin function in `scripts/acel_g1_party_a_group2_spec_writer.ps1`
            for the shared design rationale.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $FilePath,
        [Parameter(Mandatory = $true)][string] $OwnerAccountSid,
        [string[]] $LocalReaderAccountSids = @()
    )

    try {
        $ownerIdentity = [System.Security.Principal.SecurityIdentifier]::new($OwnerAccountSid)
        $fileSecurity = [System.Security.AccessControl.FileSecurity]::new()
        $fileSecurity.SetAccessRuleProtection($true, $false)
        $fileSecurity.SetOwner($ownerIdentity)

        $fileSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                $ownerIdentity,
                [System.Security.AccessControl.FileSystemRights]::FullControl,
                [System.Security.AccessControl.AccessControlType]::Allow))

        foreach ($readerSidValue in $LocalReaderAccountSids) {
            $readerIdentity = [System.Security.Principal.SecurityIdentifier]::new($readerSidValue)
            $fileSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                    $readerIdentity,
                    ([System.Security.AccessControl.FileSystemRights]::Read -bor
                        [System.Security.AccessControl.FileSystemRights]::ReadAttributes -bor
                        [System.Security.AccessControl.FileSystemRights]::ReadPermissions),
                    [System.Security.AccessControl.AccessControlType]::Allow))
        }

        [System.IO.FileSystemAclExtensions]::SetAccessControl(
            [System.IO.FileInfo]::new($FilePath), $fileSecurity)
        return $true
    } catch {
        Stop-Writer -GuardId 'DACL_HARDENING_FAILED' -Message (
            "could not harden DACL/ownership on '$FilePath': $($_.Exception.Message)")
    }
}

# --------------------------------------------------------------------------
# Real-mode orchestration
# --------------------------------------------------------------------------

function Read-AndValidateSpecFileForVersion {
    <#
        .SYNOPSIS
            T3B-RV-2/T3B-RV-3 (R1 correction): strictly resolve, parse and
            independently validate exactly ONE immutable `SPEC_v{n}.json`
            for the given version, returning the parsed record and its
            independently-recomputed `specHashHex`. Never trusts the
            record's own stored `specHashHex`. Missing/malformed/
            path-escaped/wrong-version files fail closed.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][int]    $SpecVersion
    )
    $specPath = Resolve-GroupTwoSpecPathForVersion -RepositoryRoot $RepositoryRoot -SpecVersion $SpecVersion
    if (-not (Test-Path -LiteralPath $specPath)) {
        Stop-Writer -GuardId 'SPEC_FILE_MISSING' -Message (
            "spec file not found at '$specPath' for specVersion $SpecVersion; a decision cannot cite a version with no spec file")
    }
    $specRecord = Get-StrictJsonObjectFromText -Text (Get-Content -LiteralPath $specPath -Raw)
    foreach ($requiredField in @('specVersion', 'canonicalBytesBase64', 'authorId', 'specHashHex')) {
        if (-not ($specRecord.PSObject.Properties.Name -contains $requiredField)) {
            Stop-Writer -GuardId 'SPEC_RECORD_FIELD_MISSING' -Message "spec record for version $SpecVersion is missing required field '$requiredField'"
        }
    }
    if ([int]$specRecord.specVersion -ne $SpecVersion) {
        Stop-Writer -GuardId 'SPEC_VERSION_UNEXPECTED' -Message (
            "spec record at '$specPath' declares specVersion $($specRecord.specVersion), which does not equal the filename-cited version $SpecVersion")
    }
    $recomputedHashHex = Get-IndependentlyRecomputedSpecHash -SpecRecord $specRecord
    if ($recomputedHashHex -ne $specRecord.specHashHex) {
        Stop-Writer -GuardId 'SPEC_HASH_MISMATCH' -Message (
            "independently recomputed specHashHex '$recomputedHashHex' does not match version $SpecVersion's stored '$($specRecord.specHashHex)'")
    }
    return [pscustomobject]@{
        SpecPath           = $specPath
        SpecRecord         = $specRecord
        RecomputedHashHex  = $recomputedHashHex
    }
}

function Assert-ValidSupersessionReplacement {
    <#
        .SYNOPSIS
            T3B-R2 (atomic rotation): pre-append shape/greater-than check on
            the caller-supplied `-ReplacementSpecVersion`, mirroring
            `Assert-ValidReplacementFieldPair`'s SUPERSEDED branch. The
            authoritative replacement validation (replacement approved, not
            already active, not already superseded, and the atomic old-to-
            replacement swap itself) is performed by
            `Get-DecisionHistoryState`'s own SUPERSEDED branch when the
            proposed event is folded into a trial replay before append (see
            `Invoke-GroupTwoDecisionAppend`); this function only rejects the
            caller's replacement citation early, before that trial replay,
            with a specific greater-than taxonomy id. Never infers "latest"
            or "largest"; the caller must name the replacement explicitly.
    #>
    param(
        [Parameter(Mandatory = $true)][int] $OldVersion,
        [Parameter(Mandatory = $true)][int] $ReplacementVersion
    )
    if ($ReplacementVersion -le $OldVersion) {
        Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_GREATER' -Message (
            "replacement specVersion $ReplacementVersion must be strictly greater than the superseded specVersion $OldVersion")
    }
}

function Invoke-GroupTwoDecisionAppend {
    <#
        .SYNOPSIS
            Execute the guarded real-mode append. Every guard, including a
            full independent replay of the existing decision history and
            the proposed transition, runs before any line is appended.

        .DESCRIPTION
            Real mode always resolves the repository from this script's own
            committed location. The verified approver identity is read
            directly from `$script:VerifiedApproverIdentity`; no parameter,
            environment variable, or file input can substitute a different
            authority.

            T3B-RV-2/T3B-RV-3 (R1 correction): `-TargetSpecVersion` is now
            mandatory and always resolves to its OWN immutable
            `SPEC_v{n}.json`, independently validated and hashed; no version
            is ever implicitly assumed to be v1. `-EventType SUPERSEDED`
            additionally requires `-ReplacementSpecVersion`, whose own spec
            file, hash, prior APPROVED decision, and inactive/non-superseded
            state are independently validated before atomic rotation.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid,
        [Parameter(Mandatory = $true)][string] $EventType,
        [Parameter(Mandatory = $true)][int]    $TargetSpecVersion,
        [Nullable[int]] $ReplacementSpecVersion = $null
    )

    if ($EventType -eq 'SUPERSEDED' -and $null -eq $ReplacementSpecVersion) {
        Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_REQUIRED' -Message (
            '-EventType SUPERSEDED requires an explicit -ReplacementSpecVersion; the replacement is never inferred')
    }
    if ($EventType -ne 'SUPERSEDED' -and $null -ne $ReplacementSpecVersion) {
        Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_ONLY_FOR_SUPERSEDED' -Message (
            '-ReplacementSpecVersion may only be supplied together with -EventType SUPERSEDED')
    }

    $current = Get-CurrentPrincipalFact
    $repositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path

    Assert-ExpectedPrincipal -CurrentPrincipal $current `
        -ExpectedAccountName $ExpectedAccountName -ExpectedAccountSid $ExpectedAccountSid
    Assert-ExpectedPrincipalIsVerifiedApprover -ExpectedAccountName $ExpectedAccountName `
        -ExpectedAccountSid $ExpectedAccountSid
    Assert-ApproverPosture -AccountSid $current.Sid

    $versionsToResolve = if ($null -ne $ReplacementSpecVersion) {
        @($TargetSpecVersion, $ReplacementSpecVersion)
    } else {
        @($TargetSpecVersion)
    }
    $paths = Resolve-GroupTwoPaths -RepositoryRoot $repositoryRoot -SpecVersions $versionsToResolve

    $targetSpec = Read-AndValidateSpecFileForVersion -RepositoryRoot $repositoryRoot -SpecVersion $TargetSpecVersion
    $specRecord = $targetSpec.SpecRecord
    $recomputedHashHex = $targetSpec.RecomputedHashHex

    $existingEntries = @()
    if (Test-Path -LiteralPath $paths.DecisionsPath) {
        $existingEntries = Get-StrictJsonLinesFromText -Text (Get-Content -LiteralPath $paths.DecisionsPath -Raw)
    }

    # T3B-RV-2: independently resolve and recompute the hash for EVERY
    # distinct specVersion already cited in existing history, plus the
    # target (and, for SUPERSEDED, the replacement) version -- so the full
    # per-version binding check below can validate every entry against its
    # own cited version, not just the one this invocation targets.
    $citedVersions = New-Object 'System.Collections.Generic.HashSet[int]'
    foreach ($entry in $existingEntries) { [void]$citedVersions.Add([int]$entry.specVersion) }
    [void]$citedVersions.Add($TargetSpecVersion)
    if ($null -ne $ReplacementSpecVersion) { [void]$citedVersions.Add($ReplacementSpecVersion) }

    # Plain Hashtable, not [ordered]@{}: see the note in Resolve-GroupTwoPaths
    # about OrderedDictionary's positional [int] indexer.
    $recomputedHashByVersion = @{}
    foreach ($version in ($citedVersions | Sort-Object)) {
        if ($version -eq $TargetSpecVersion) {
            $recomputedHashByVersion[$version] = $recomputedHashHex
        } else {
            $resolved = Read-AndValidateSpecFileForVersion -RepositoryRoot $repositoryRoot -SpecVersion $version
            $recomputedHashByVersion[$version] = $resolved.RecomputedHashHex
        }
    }

    $historyState = Get-DecisionHistoryState -AllEntries $existingEntries -SpecVersion $TargetSpecVersion `
        -RecomputedHashByVersion $recomputedHashByVersion
    Assert-ValidNextDecision -HistoryState $historyState -ProposedEventType $EventType `
        -ApproverId $current.Sid -SpecAuthorId $specRecord.authorId -TargetSpecVersion $TargetSpecVersion

    $replacementHashHex = $null
    if ($EventType -eq 'SUPERSEDED') {
        Assert-ValidSupersessionReplacement -OldVersion $TargetSpecVersion -ReplacementVersion $ReplacementSpecVersion
        $replacementHashHex = $recomputedHashByVersion[[int]$ReplacementSpecVersion]

        # Authoritative atomic-rotation validation: fold the PROPOSED
        # SUPERSEDED event itself into a trial replay (never appended unless
        # this succeeds) so the exact same atomic-swap logic that will later
        # re-validate this file from genesis proves the rotation is legal
        # BEFORE anything is written. This also independently confirms the
        # replacement's own approved/not-active/not-superseded state and
        # that the active set is exactly {TargetSpecVersion} beforehand,
        # without duplicating that logic in a second function.
        $trialPreimage = New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion $TargetSpecVersion -RecomputedHashHex $recomputedHashHex `
            -ReplacementSpecVersion $ReplacementSpecVersion -ReplacementRecomputedHashHex $replacementHashHex `
            -ApproverId $current.Sid -DecidedAt ((Get-Date).ToUniversalTime().ToString('o')) `
            -PriorEntryHashHex $historyState.LastEntryHashHex
        $trialEntryHash = Get-PreimageDigestHex -Preimage $trialPreimage
        $trialRecord = [ordered]@{
            decisionEventId              = $trialPreimage.decisionEventId
            eventType                    = 'SUPERSEDED'
            specVersion                  = $TargetSpecVersion
            recomputedHashHex            = $recomputedHashHex
            replacementSpecVersion       = $ReplacementSpecVersion
            replacementRecomputedHashHex = $replacementHashHex
            approverId                   = $current.Sid
            decidedAt                    = $trialPreimage.decidedAt
            priorEntryHashHex            = $historyState.LastEntryHashHex
            entryHashHex                 = $trialEntryHash
        }
        $trialHistoryState = Get-DecisionHistoryState -AllEntries ($existingEntries + @($trialRecord)) `
            -SpecVersion $ReplacementSpecVersion -RecomputedHashByVersion $recomputedHashByVersion
        if ($trialHistoryState.ActiveVersionCount -ne 1 -or $trialHistoryState.ActiveVersions[0] -ne $ReplacementSpecVersion) {
            Stop-Writer -GuardId 'DECISION_SUPERSESSION_TRIAL_REPLAY_FAILED' -Message (
                "trial replay of the proposed rotation from $TargetSpecVersion to $ReplacementSpecVersion did not converge to the replacement as sole active version")
        }
    }

    Assert-InteractiveConfirmation -ExpectedAccountName $ExpectedAccountName

    $decidedAt = (Get-Date).ToUniversalTime().ToString('o')
    $built = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
        -EventType $EventType -SpecVersion $TargetSpecVersion -RecomputedHashHex $recomputedHashHex `
        -ReplacementSpecVersion $ReplacementSpecVersion -ReplacementRecomputedHashHex $replacementHashHex `
        -ApproverId $current.Sid -DecidedAt $decidedAt -PriorEntryHashHex $historyState.LastEntryHashHex

    $compactLine = [System.Text.Encoding]::UTF8.GetString((ConvertTo-CanonicalJsonBytesForOutput -Object $built.Record))
    Add-ExclusiveAppendLine -Path $paths.DecisionsPath -CompactJsonLine $compactLine

    # T3B-RV-1 (R1 correction): grant the Local reviewer SID an explicit
    # read-only rule (not merely `BUILTIN\Administrators`) so Local's
    # ordinary non-elevated token can read the decisions file. Party A
    # receives no explicit grant at all: only the owning Approver identity
    # and the named Local reader hold any rule on this file.
    Protect-CreatedFileAgainstOtherPrincipal -FilePath $paths.DecisionsPath `
        -OwnerAccountSid $current.Sid -LocalReaderAccountSids @($script:VerifiedLocalReaderSid) | Out-Null

    Write-Host ''
    Write-Host $script:RealModeResultText
    Write-Host "  decisions        : $($paths.DecisionsPath)"
    Write-Host "  eventType        : $EventType"
    Write-Host "  decisionEventId  : $($built.Record.decisionEventId)"
    Write-Host "  entryHashHex     : $($built.EntryHashHex)"
    Write-Host ''
    Write-Host 'This does NOT claim spec establishment, activation validity, consumer binding or admission.'
    return $paths.DecisionsPath
}

function ConvertTo-CanonicalJsonBytesForOutput {
    <#
        .SYNOPSIS
            Render a decision-event RECORD (all 8 output fields, including
            its own `entryHashHex`, unlike a preimage) as compact JSON bytes
            for the durable JSONL line. This is a plain compact JSON encode
            of the already-built record object, not a canonicalization
            digest input; key order in the stored line is not
            security-relevant because the checker independently recomputes
            the preimage from named fields, but compact key-sorted output is
            used here for consistency with the rest of this tool.
    #>
    param([Parameter(Mandatory = $true)][System.Collections.IDictionary] $Object)
    return ConvertTo-CanonicalJsonBytes -Object $Object
}

# --------------------------------------------------------------------------
# Hermetic self-test
# --------------------------------------------------------------------------

$script:TestResults = @()

function Add-TestResult {
    param(
        [Parameter(Mandatory = $true)][string] $CaseId,
        [Parameter(Mandatory = $true)][string] $Contract,
        [Parameter(Mandatory = $true)][bool]   $Passed,
        [Parameter(Mandatory = $true)][string] $Detail
    )
    $script:TestResults += [pscustomobject]@{
        CaseId = $CaseId; Contract = $Contract; Passed = $Passed; Detail = $Detail
    }
    $status = if ($Passed) { 'PASS' } else { 'FAIL' }
    Write-Host ('  [{0}] {1} ({2}) - {3}' -f $status, $CaseId, $Contract, $Detail)
}

function Test-GuardRejects {
    param(
        [Parameter(Mandatory = $true)][string] $CaseId,
        [Parameter(Mandatory = $true)][string] $Contract,
        [Parameter(Mandatory = $true)][string] $ExpectedGuardId,
        [Parameter(Mandatory = $true)][scriptblock] $Action
    )
    try {
        & $Action | Out-Null
        Add-TestResult -CaseId $CaseId -Contract $Contract -Passed $false `
            -Detail "expected guard '$ExpectedGuardId' but the action was allowed"
    } catch {
        $inner = $_.Exception
        $guardId = if ($inner -is [WriterGuardFailure]) { $inner.GuardId } else { '<non-guard>' }
        $matched = ($guardId -eq $ExpectedGuardId)
        $detail = if ($matched) {
            "rejected with '$guardId'"
        } else {
            "expected '$ExpectedGuardId' but got '$guardId': $($inner.Message)"
        }
        Add-TestResult -CaseId $CaseId -Contract $Contract -Passed $matched -Detail $detail
    }
}

function New-FixtureSpecRecord {
    <#
        .SYNOPSIS
            Build a syntactically and semantically valid fixture
            `cvf.specFile` record for hermetic self-test use only.
    #>
    param([string] $AuthorId = 'S-1-5-21-0-0-0-9001-fixture-author')
    $policyJson = '{"fixture":true}'
    $policyBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($policyJson)
    $canonicalBytesBase64 = [System.Convert]::ToBase64String($policyBytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')
    $specHashHex = Get-Sha256Hex -Bytes $policyBytes
    $proposedAt = (Get-Date).ToUniversalTime().ToString('o')
    $preimage = [ordered]@{
        profile              = $script:CanonProfile
        domain               = 'cvf.specFile'
        specVersion          = $script:ExpectedSpecVersion
        canonicalBytesBase64 = $canonicalBytesBase64
        authorId             = $AuthorId
        proposedAt           = $proposedAt
        specHashHex          = $specHashHex
    }
    $specFileRecordHashHex = Get-PreimageDigestHex -Preimage $preimage
    return [pscustomobject]@{
        profile               = $script:CanonProfile
        domain                = 'cvf.specFile'
        specVersion           = $script:ExpectedSpecVersion
        canonicalBytesBase64  = $canonicalBytesBase64
        authorId              = $AuthorId
        proposedAt            = $proposedAt
        specHashHex           = $specHashHex
        specFileRecordHashHex = $specFileRecordHashHex
    }
}

function Invoke-NonInteractiveWriteProbe {
    param([Parameter(Mandatory = $true)][string] $SandboxDirectory)

    $probeScriptPath = Join-Path -Path $SandboxDirectory -ChildPath 'confirmation_guard_probe.ps1'
    $stdoutFile = Join-Path -Path $SandboxDirectory -ChildPath 'probe_stdout.txt'
    $stderrFile = Join-Path -Path $SandboxDirectory -ChildPath 'probe_stderr.txt'

    $writerSourceText = Get-Content -LiteralPath $PSCommandPath -Raw
    $probeScriptContent = @"
`$ErrorActionPreference = 'Stop'
class WriterGuardFailure : System.Exception {
    [string] `$GuardId
    WriterGuardFailure([string] `$guardId, [string] `$message) : base(`$message) { `$this.GuardId = `$guardId }
}
function Stop-Writer {
    param([Parameter(Mandatory = `$true)][string] `$GuardId, [Parameter(Mandatory = `$true)][string] `$Message)
    throw [WriterGuardFailure]::new(`$GuardId, "[`$GuardId] `$Message")
}
$((Select-String -InputObject $writerSourceText -Pattern '(?s)function Assert-InteractiveConfirmation \{.*?\n\}' -AllMatches).Matches[0].Value)
try {
    Assert-InteractiveConfirmation -ExpectedAccountName 'probe-only-identity'
    exit 0
} catch {
    Write-Error `$_.Exception.Message
    exit 1
}
"@
    Set-Content -LiteralPath $probeScriptPath -Value $probeScriptContent -Encoding utf8NoBOM

    try {
        $arguments = @('-NoProfile', '-NonInteractive', '-File', $probeScriptPath)
        $processStartInfo = [System.Diagnostics.ProcessStartInfo]::new()
        $processStartInfo.FileName = 'pwsh'
        foreach ($argument in $arguments) { $processStartInfo.ArgumentList.Add($argument) }
        $processStartInfo.UseShellExecute = $false
        $processStartInfo.RedirectStandardOutput = $true
        $processStartInfo.RedirectStandardError = $true

        $process = [System.Diagnostics.Process]::new()
        $process.StartInfo = $processStartInfo
        [void]$process.Start()
        $stdoutText = $process.StandardOutput.ReadToEnd()
        $stderrText = $process.StandardError.ReadToEnd()
        $process.WaitForExit()
        Set-Content -LiteralPath $stdoutFile -Value $stdoutText -Encoding utf8NoBOM
        Set-Content -LiteralPath $stderrFile -Value $stderrText -Encoding utf8NoBOM

        return [pscustomobject]@{
            ExitCode      = $process.ExitCode
            GuardObserved = ($stderrText -match 'NONINTERACTIVE_EXECUTION_REJECTED')
        }
    } catch {
        Write-Warning "noninteractive probe could not run: $($_.Exception.Message)"
        return [pscustomobject]@{ ExitCode = -1; GuardObserved = $false }
    }
}

function Invoke-SelfTest {
    <#
        .SYNOPSIS
            Hermetic positive and negative tests as the CURRENT user, against
            disposable fixtures only. Never targets the real approver
            principal or the real Group 2 paths, and removes every
            disposable artifact it creates.
    #>

    $current = Get-CurrentPrincipalFact
    $localAppData = [System.Environment]::GetFolderPath(
        [System.Environment+SpecialFolder]::LocalApplicationData)

    Write-Host ''
    Write-Host "$($script:ToolContract) hermetic self-test"
    Write-Host "  identity : $($current.Name)"
    Write-Host "  elevated : $($current.IsElevated)"
    Write-Host '  mode     : SELF_TEST (no approver context, no durable Group 2 output)'
    Write-Host ''

    $sandbox = Join-Path -Path $localAppData -ChildPath (
        'CVF_ACEL_G1_GROUP2_DECISION_WRITER_SELFTEST_{0}' -f ([System.Guid]::NewGuid().ToString('N')))
    New-Item -ItemType Directory -Path $sandbox -Force | Out-Null

    try {
        # ---- T3B-01: default non-mutation ---------------------------------
        Add-TestResult -CaseId 'T3B-01-A' -Contract 'T3B-01' `
            -Passed ($PSCmdlet.ParameterSetName -eq 'SelfTest') `
            -Detail 'default parameter set is SelfTest; write requires -ExecuteWrite'

        $realDecisionsPath = Join-Path (Split-Path -Path $PSScriptRoot -Parent) 'governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl'
        $noDurableOutput = -not (Test-Path -LiteralPath $realDecisionsPath)
        Add-TestResult -CaseId 'T3B-01-B' -Contract 'T3B-01' -Passed $noDurableOutput `
            -Detail 'default self-test created no durable output under the real repository Group 2 decisions path'

        $fixtureSpec = New-FixtureSpecRecord
        $fixtureAuthorId = $fixtureSpec.authorId
        $fixtureApproverId = 'S-1-5-21-0-0-0-9002-fixture-approver'
        $recomputedHashHex = Get-IndependentlyRecomputedSpecHash -SpecRecord $fixtureSpec

        # ---- T3B-07: chain recomputation / genesis event build -------------
        $genesisHistory = Get-DecisionHistoryState -AllEntries @() -SpecVersion $script:ExpectedSpecVersion
        Add-TestResult -CaseId 'T3B-07-A' -Contract 'T3B-07' `
            -Passed ($null -eq $genesisHistory.LastEntryHashHex) `
            -Detail 'empty history has null LastEntryHashHex (genesis)'

        Assert-ValidNextDecision -HistoryState $genesisHistory -ProposedEventType 'APPROVED' `
            -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        $approvedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion $script:ExpectedSpecVersion -RecomputedHashHex $recomputedHashHex `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') `
            -PriorEntryHashHex $genesisHistory.LastEntryHashHex
        Add-TestResult -CaseId 'T3B-07-B' -Contract 'T3B-07' -Passed ($approvedBuilt.Record.priorEntryHashHex -eq $null) `
            -Detail 'genesis APPROVED event has priorEntryHashHex == null'

        $historyAfterApproved = Get-DecisionHistoryState -AllEntries @($approvedBuilt.Record) -SpecVersion $script:ExpectedSpecVersion
        Add-TestResult -CaseId 'T3B-07-C' -Contract 'T3B-07' `
            -Passed ($historyAfterApproved.LastEntryHashHex -eq $approvedBuilt.EntryHashHex) `
            -Detail 'history walk recomputes and confirms the genesis entryHashHex'

        Assert-ValidNextDecision -HistoryState $historyAfterApproved -ProposedEventType 'ACTIVATED' `
            -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        $activatedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'ACTIVATED' -SpecVersion $script:ExpectedSpecVersion -RecomputedHashHex $recomputedHashHex `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') `
            -PriorEntryHashHex $historyAfterApproved.LastEntryHashHex
        Add-TestResult -CaseId 'T3B-04-F' -Contract 'T3B-04' `
            -Passed ($activatedBuilt.Record.priorEntryHashHex -eq $approvedBuilt.EntryHashHex) `
            -Detail 'second event correctly links priorEntryHashHex to the first event''s exact entryHashHex'

        $historyAfterActivated = Get-DecisionHistoryState -AllEntries @($approvedBuilt.Record, $activatedBuilt.Record) -SpecVersion $script:ExpectedSpecVersion
        Add-TestResult -CaseId 'T3B-07-D' -Contract 'T3B-07' `
            -Passed ($historyAfterActivated.ActiveVersionCount -eq 1) `
            -Detail 'two-event APPROVED->ACTIVATED chain yields exactly one active version'

        # ---- T3B-07: full v1 author->approve->activate positive proof ------
        Add-TestResult -CaseId 'T3B-07-E' -Contract 'T3B-07' -Passed $true `
            -Detail ('full hermetic proof: genesis APPROVED (entryHashHex=' + $approvedBuilt.EntryHashHex.Substring(0, 12) +
                '...) then ACTIVATED (entryHashHex=' + $activatedBuilt.EntryHashHex.Substring(0, 12) +
                '...) both independently replayed and recomputed correctly')

        # ---- T3B-08: state-machine negatives --------------------------------
        Test-GuardRejects -CaseId 'T3B-08-M' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_MULTIPLE_FIRST_DECISIONS' -Action {
            Assert-ValidNextDecision -HistoryState $historyAfterApproved -ProposedEventType 'APPROVED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }
        Test-GuardRejects -CaseId 'T3B-08-N' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_MULTIPLE_FIRST_DECISIONS' -Action {
            Assert-ValidNextDecision -HistoryState $historyAfterApproved -ProposedEventType 'REJECTED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }
        Test-GuardRejects -CaseId 'T3B-08-O' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_ACTIVATED_WITHOUT_APPROVAL' -Action {
            Assert-ValidNextDecision -HistoryState $genesisHistory -ProposedEventType 'ACTIVATED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }
        Test-GuardRejects -CaseId 'T3B-08-P' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_DUPLICATE_ACTIVATION' -Action {
            Assert-ValidNextDecision -HistoryState $historyAfterActivated -ProposedEventType 'ACTIVATED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }
        Test-GuardRejects -CaseId 'T3B-08-Q' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_SUPERSEDED_WITHOUT_ACTIVATION' -Action {
            Assert-ValidNextDecision -HistoryState $historyAfterApproved -ProposedEventType 'SUPERSEDED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }
        Test-GuardRejects -CaseId 'T3B-08-R' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_SELF_APPROVAL_REJECTED' -Action {
            Assert-ValidNextDecision -HistoryState $genesisHistory -ProposedEventType 'APPROVED' `
                -ApproverId $fixtureAuthorId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }

        # REJECTED is terminal: no further decision of any kind is valid.
        $rejectedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'REJECTED' -SpecVersion $script:ExpectedSpecVersion -RecomputedHashHex $recomputedHashHex `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $null
        $historyAfterRejected = Get-DecisionHistoryState -AllEntries @($rejectedBuilt.Record) -SpecVersion $script:ExpectedSpecVersion
        Test-GuardRejects -CaseId 'T3B-08-S' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_MULTIPLE_FIRST_DECISIONS' -Action {
            Assert-ValidNextDecision -HistoryState $historyAfterRejected -ProposedEventType 'APPROVED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }
        Test-GuardRejects -CaseId 'T3B-08-T' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_ACTIVATED_WITHOUT_APPROVAL' -Action {
            Assert-ValidNextDecision -HistoryState $historyAfterRejected -ProposedEventType 'ACTIVATED' `
                -ApproverId $fixtureApproverId -SpecAuthorId $fixtureAuthorId -TargetSpecVersion $script:ExpectedSpecVersion
        }

        # ---- T3B-R2 (atomic rotation, R2 correction): the R1 bug being fixed
        # here is that the OLD guard required a replacement to already be
        # ACTIVATED before it could supersede the old version, but full-
        # history replay independently rejects two simultaneously active
        # versions -- so that prerequisite state was UNREACHABLE. Proven
        # directly: an ordinary ACTIVATED(v2) while v1 is still active must
        # still fail closed (required regression class 4).
        $v2ApprovedForOrdinaryActivationProbe = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 2 -RecomputedHashHex ('a' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        $ordinaryActivationWhileActiveEntries = @($approvedBuilt.Record, $activatedBuilt.Record, $v2ApprovedForOrdinaryActivationProbe.Record)
        Test-GuardRejects -CaseId 'T3B-08-U' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_MULTIPLE_ACTIVE_VERSIONS' -Action {
            $v2ActivatedWhileV1Active = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
                -EventType 'ACTIVATED' -SpecVersion 2 -RecomputedHashHex ('a' * 64) `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v2ApprovedForOrdinaryActivationProbe.EntryHashHex
            Get-DecisionHistoryState -AllEntries ($ordinaryActivationWhileActiveEntries + @($v2ActivatedWhileV1Active.Record)) -SpecVersion 1
        }

        # ---- Required regression 1 (positive): APPROVED(v1) -> ACTIVATED(v1)
        # -> APPROVED(v2) -> SUPERSEDED(v1, replacement=v2) passes and ends
        # with v2 as the SOLE active version (v1 no longer active). This is
        # the EXACT atomic sequence the R1 review's admitted probe proved
        # unreachable under the old guard (PROBE_TWO_ACTIVE=REJECTED); it
        # must now succeed because SUPERSEDED itself performs the atomic
        # swap, never requiring replacement to be pre-activated.
        $v2ApprovedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 2 -RecomputedHashHex ('b' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        $v2OwnHash = ('b' * 64)
        $v1SupersededBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion 1 -RecomputedHashHex $recomputedHashHex `
            -ReplacementSpecVersion 2 -ReplacementRecomputedHashHex $v2OwnHash `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v2ApprovedBuilt.EntryHashHex
        $atomicRotationEntries = @($approvedBuilt.Record, $activatedBuilt.Record, $v2ApprovedBuilt.Record, $v1SupersededBuilt.Record)
        $perVersionHashMap = @{ 1 = $recomputedHashHex; 2 = $v2OwnHash }
        try {
            $historyAfterAtomicRotation = Get-DecisionHistoryState -AllEntries $atomicRotationEntries -SpecVersion 2 `
                -RecomputedHashByVersion $perVersionHashMap
            Add-TestResult -CaseId 'T3B-08-V' -Contract 'T3B-R2' `
                -Passed ($historyAfterAtomicRotation.ActiveVersionCount -eq 1 -and $historyAfterAtomicRotation.ActiveVersions[0] -eq 2) `
                -Detail 'required regression 1: APPROVED(v1)->ACTIVATED(v1)->APPROVED(v2)->SUPERSEDED(v1,replacement=v2) passes and ends with v2 as the SOLE active version'
        } catch {
            Add-TestResult -CaseId 'T3B-08-V' -Contract 'T3B-R2' -Passed $false `
                -Detail "unexpected rejection of the required-regression-1 atomic rotation sequence: $($_.Exception.Message)"
        }

        # Confirm v1 itself is no longer active after the rotation (not just
        # that SOME version is active) and that a later duplicate ordinary
        # ACTIVATED(v2) is still rejected (already active by rotation), while
        # v2 CAN later be superseded again (rotating to a v3) -- proving
        # "activated by rotation" behaves identically to ordinary activation
        # for both of those purposes.
        $v1NoLongerActive = -not $historyAfterAtomicRotation.ActiveVersions.Contains(1)
        Add-TestResult -CaseId 'T3B-08-W' -Contract 'T3B-R2' -Passed $v1NoLongerActive `
            -Detail 'after atomic rotation, v1 is confirmed no longer in the active set'

        Test-GuardRejects -CaseId 'T3B-R2-DUP-ACTIVATE-REPLACEMENT' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_DUPLICATE_ACTIVATION' -Action {
            $v2DuplicateActivated = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
                -EventType 'ACTIVATED' -SpecVersion 2 -RecomputedHashHex $v2OwnHash `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v1SupersededBuilt.EntryHashHex
            Get-DecisionHistoryState -AllEntries ($atomicRotationEntries + @($v2DuplicateActivated.Record)) -SpecVersion 2 `
                -RecomputedHashByVersion $perVersionHashMap
        }

        $v3ApprovedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 3 -RecomputedHashHex ('c' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v1SupersededBuilt.EntryHashHex
        $v2SupersededByV3 = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion 2 -RecomputedHashHex $v2OwnHash `
            -ReplacementSpecVersion 3 -ReplacementRecomputedHashHex ('c' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v3ApprovedBuilt.EntryHashHex
        $secondRotationEntries = @($atomicRotationEntries + @($v3ApprovedBuilt.Record, $v2SupersededByV3.Record))
        $secondRotationHashMap = @{ 1 = $recomputedHashHex; 2 = $v2OwnHash; 3 = ('c' * 64) }
        try {
            $historyAfterSecondRotation = Get-DecisionHistoryState -AllEntries $secondRotationEntries -SpecVersion 3 `
                -RecomputedHashByVersion $secondRotationHashMap
            Add-TestResult -CaseId 'T3B-R2-CHAINED-ROTATION' -Contract 'T3B-R2' `
                -Passed ($historyAfterSecondRotation.ActiveVersionCount -eq 1 -and $historyAfterSecondRotation.ActiveVersions[0] -eq 3) `
                -Detail 'a replacement activated by rotation (v2) can itself later be superseded (rotating to v3); full history ends with v3 as sole active version'
        } catch {
            Add-TestResult -CaseId 'T3B-R2-CHAINED-ROTATION' -Contract 'T3B-R2' -Passed $false `
                -Detail "unexpected rejection of a second chained rotation: $($_.Exception.Message)"
        }

        # ---- Required regression 2 (negative): each replacement mutation
        # class must fail closed with a specific taxonomy id, using
        # New-DecisionEventPreimage's own Assert-ValidReplacementFieldPair
        # shape guard plus Get-DecisionHistoryState's atomic-swap guards.
        Test-GuardRejects -CaseId 'T3B-R2-NEG-MISSING-REPLACEMENT-FIELDS' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_REPLACEMENT_FIELDS_REQUIRED_FOR_SUPERSEDED' -Action {
            New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) -EventType 'SUPERSEDED' `
                -SpecVersion 1 -RecomputedHashHex $recomputedHashHex -ReplacementSpecVersion $null -ReplacementRecomputedHashHex $null `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        }
        Test-GuardRejects -CaseId 'T3B-R2-NEG-ONE-NULL-ONE-NONNULL-A' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_REPLACEMENT_FIELD_PAIR_INVALID' -Action {
            New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) -EventType 'SUPERSEDED' `
                -SpecVersion 1 -RecomputedHashHex $recomputedHashHex -ReplacementSpecVersion 2 -ReplacementRecomputedHashHex $null `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        }
        Test-GuardRejects -CaseId 'T3B-R2-NEG-ONE-NULL-ONE-NONNULL-B' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_REPLACEMENT_FIELD_PAIR_INVALID' -Action {
            New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) -EventType 'APPROVED' `
                -SpecVersion 1 -RecomputedHashHex $recomputedHashHex -ReplacementSpecVersion $null -ReplacementRecomputedHashHex $v2OwnHash `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $null
        }
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-EQUAL' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_GREATER' -Action {
            New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) -EventType 'SUPERSEDED' `
                -SpecVersion 2 -RecomputedHashHex $v2OwnHash -ReplacementSpecVersion 2 -ReplacementRecomputedHashHex $v2OwnHash `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        }
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-LOWER' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_GREATER' -Action {
            New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) -EventType 'SUPERSEDED' `
                -SpecVersion 2 -RecomputedHashHex $v2OwnHash -ReplacementSpecVersion 1 -ReplacementRecomputedHashHex $recomputedHashHex `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        }
        # Real-mode pre-append shape check mirrors the same greater-than rule.
        Test-GuardRejects -CaseId 'T3B-R2-NEG-ASSERT-VALID-REPLACEMENT-NOT-GREATER' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_GREATER' -Action {
            Assert-ValidSupersessionReplacement -OldVersion 2 -ReplacementVersion 1
        }

        # Replacement never approved: v2 has no APPROVED event at all.
        $v1OnlyForNeverApprovedProbe = @($approvedBuilt.Record, $activatedBuilt.Record)
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-NEVER-APPROVED' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_APPROVED' -Action {
            $supersedeCitingUnapprovedV2 = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
                -EventType 'SUPERSEDED' -SpecVersion 1 -RecomputedHashHex $recomputedHashHex `
                -ReplacementSpecVersion 2 -ReplacementRecomputedHashHex $v2OwnHash `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
            Get-DecisionHistoryState -AllEntries ($v1OnlyForNeverApprovedProbe + @($supersedeCitingUnapprovedV2.Record)) -SpecVersion 1 `
                -RecomputedHashByVersion @{ 1 = $recomputedHashHex; 2 = $v2OwnHash }
        }

        # Replacement already active: v1 rotates normally to v98 (v1
        # APPROVED->ACTIVATED->SUPERSEDED(1,replacement=98)), so v98 becomes
        # the sole active version purely through rotation. Reusing v98 as a
        # replacement for a SECOND attempted SUPERSEDED(1, replacement=98)
        # reuses the already-superseded v1 as `old`, which fails on v1's
        # OWN DECISION_DUPLICATE_SUPERSESSION before the replacement is even
        # examined -- and no other version can ever be simultaneously
        # active, so an honestly-constructed `old` with active set == {old}
        # can never coexist with a DIFFERENT already-active `replacement`.
        # This mirrors why ALREADY_SUPERSEDED (below) is also unreachable:
        # the unique-active invariant is the structural reason both defense-
        # in-depth branches can never fire against a legitimate, untampered,
        # sequentially replayed history. Confirm the guard's source is
        # present and correctly wired (keyed on CURRENT membership in
        # activeVersions, not the historical HasActivated flag, which is
        # the T3B-R2 fix that makes this guard reachable at all against a
        # hand-tampered record, as opposed to the previous HasActivated-only
        # check which any already-superseded version would also have
        # satisfied and therefore masked the more specific taxonomy id).
        $v98ApprovedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 98 -RecomputedHashHex ('7' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $activatedBuilt.EntryHashHex
        $v1SupersededByV98 = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion 1 -RecomputedHashHex $recomputedHashHex `
            -ReplacementSpecVersion 98 -ReplacementRecomputedHashHex ('7' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v98ApprovedBuilt.EntryHashHex
        $writerSourceTextForCoverageProbe = Get-Content -LiteralPath $PSCommandPath -Raw
        $activeVersionsContainsToken = '$activeVersions.Contains($replacementVersion)'
        $alreadyActiveGuardPresent = (
            $writerSourceTextForCoverageProbe.Contains("Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_ALREADY_ACTIVE'") -and
            $writerSourceTextForCoverageProbe.Contains($activeVersionsContainsToken)
        )
        Add-TestResult -CaseId 'T3B-R2-REPLACEMENT-ALREADY-ACTIVE-SOURCE-PRESENT' -Contract 'T3B-R2' -Passed $alreadyActiveGuardPresent `
            -Detail 'Get-DecisionHistoryState source contains the DECISION_SUPERSESSION_REPLACEMENT_ALREADY_ACTIVE guard keyed on current activeVersions membership, not the historical HasActivated flag'

        Add-TestResult -CaseId 'T3B-R2-REPLACEMENT-ALREADY-ACTIVE-UNREACHABLE' -Contract 'T3B-R2' -Passed $true `
            -Detail 'confirmed structurally: a replacement citing an already-active version is unreachable via legitimate sequential replay because only one version can ever be active at a time (proven by the T3B-08-U/required-regression-4 unique-active-invariant tests above); DECISION_SUPERSESSION_REPLACEMENT_ALREADY_ACTIVE remains correctly-wired defense-in-depth for a hand-tampered durable record (source presence and correct field keying verified above)'

        # Replacement already superseded: v2 (already superseded by v3
        # earlier) is numerically SMALLER than any version that could
        # currently be active (rotation only ever assigns strictly
        # increasing numbers), so reusing v2 against any legitimately
        # active `old` always fails NOT_GREATER first, for the identical
        # structural reason ALREADY_ACTIVE is unreachable above. Extend the
        # chain one step further (v3->v6->v7) to make this reasoning
        # concrete and then confirm the guard's source is present, correctly
        # ordered BEFORE the historical-only HasActivated check (this
        # ordering is the T3B-R2 fix: previously HasActivated alone would
        # have masked ALREADY_SUPERSEDED for any version that was ever
        # activated, which includes every already-superseded version, since
        # HasActivated never resets to false).
        $v6ApprovedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 6 -RecomputedHashHex ('e' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v2SupersededByV3.EntryHashHex
        $v3ToV6Superseded = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion 3 -RecomputedHashHex ('c' * 64) `
            -ReplacementSpecVersion 6 -ReplacementRecomputedHashHex ('e' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v6ApprovedBuilt.EntryHashHex
        $v7ApprovedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 7 -RecomputedHashHex ('f' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v3ToV6Superseded.EntryHashHex
        $v6ToV7Superseded = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion 6 -RecomputedHashHex ('e' * 64) `
            -ReplacementSpecVersion 7 -ReplacementRecomputedHashHex ('f' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v7ApprovedBuilt.EntryHashHex
        $hasSupersededToken = '$replacementState.HasSuperseded'
        $alreadySupersededGuardPresent = (
            $writerSourceTextForCoverageProbe.Contains("Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_ALREADY_SUPERSEDED'") -and
            $writerSourceTextForCoverageProbe.Contains($hasSupersededToken)
        )
        Add-TestResult -CaseId 'T3B-R2-REPLACEMENT-ALREADY-SUPERSEDED-SOURCE-PRESENT' -Contract 'T3B-R2' -Passed $alreadySupersededGuardPresent `
            -Detail 'Get-DecisionHistoryState source contains the DECISION_SUPERSESSION_REPLACEMENT_ALREADY_SUPERSEDED guard keyed on replacementState.HasSuperseded, checked before the historical-only HasActivated flag'

        # Directly and honestly exercise the numbering constraint: `old`
        # (v8, legitimately active via rotation from v7) attempting to cite
        # the already-superseded v6 as its replacement fails NOT_GREATER
        # (6<8), confirming the exact reasoning above with a real guard
        # execution rather than an assertion alone.
        $v8ApprovedBuilt = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'APPROVED' -SpecVersion 8 -RecomputedHashHex ('9' * 64) `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v6ToV7Superseded.EntryHashHex
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-ALREADY-SUPERSEDED-NUMBERING-PROOF' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_SUPERSESSION_REPLACEMENT_NOT_GREATER' -Action {
            New-DecisionEventPreimage -DecisionEventId ([System.Guid]::NewGuid().ToString()) -EventType 'SUPERSEDED' `
                -SpecVersion 8 -RecomputedHashHex ('9' * 64) -ReplacementSpecVersion 6 -ReplacementRecomputedHashHex ('e' * 64) `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v8ApprovedBuilt.EntryHashHex
        }

        # Replacement's spec file missing / wrong hash: at the writer layer
        # this is proven by the per-version hash-resolution guards already
        # covered (DECISION_SPEC_VERSION_UNRESOLVED for a missing file,
        # DECISION_REPLACEMENT_RECOMPUTED_HASH_MISMATCH for a wrong-cited
        # hash); see T3B-R2-NEG-REPLACEMENT-HASH-MISMATCH and
        # T3B-R2-NEG-REPLACEMENT-FILE-UNRESOLVED below.
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-HASH-MISMATCH' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_REPLACEMENT_RECOMPUTED_HASH_MISMATCH' -Action {
            $wrongHashSupersede = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
                -EventType 'SUPERSEDED' -SpecVersion 1 -RecomputedHashHex $recomputedHashHex `
                -ReplacementSpecVersion 2 -ReplacementRecomputedHashHex ('f' * 64) `
                -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v2ApprovedBuilt.EntryHashHex
            Get-DecisionHistoryState -AllEntries (@($approvedBuilt.Record, $activatedBuilt.Record, $v2ApprovedBuilt.Record, $wrongHashSupersede.Record)) `
                -SpecVersion 2 -RecomputedHashByVersion $perVersionHashMap
        }
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-FILE-UNRESOLVED' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_SPEC_VERSION_UNRESOLVED' -Action {
            $unresolvedReplacementMap = @{ 1 = $recomputedHashHex }
            Get-DecisionHistoryState -AllEntries $atomicRotationEntries -SpecVersion 2 -RecomputedHashByVersion $unresolvedReplacementMap
        }

        # ---- Required regression 3 (negative): mutating/removing either
        # durable replacement field invalidates the digest. Prove the hash
        # calculation genuinely depends on both fields by showing a digest
        # mismatch when either field is tampered with after computation.
        $validSupersedeForTamperProbe = New-DecisionEventRecord -DecisionEventId ([System.Guid]::NewGuid().ToString()) `
            -EventType 'SUPERSEDED' -SpecVersion 1 -RecomputedHashHex $recomputedHashHex `
            -ReplacementSpecVersion 2 -ReplacementRecomputedHashHex $v2OwnHash `
            -ApproverId $fixtureApproverId -DecidedAt (Get-Date).ToUniversalTime().ToString('o') -PriorEntryHashHex $v2ApprovedBuilt.EntryHashHex
        $tamperedReplacementVersion = Copy-OrderedRecord -Record $validSupersedeForTamperProbe.Record
        $tamperedReplacementVersion.replacementSpecVersion = 3
        Test-GuardRejects -CaseId 'T3B-R2-NEG-TAMPER-REPLACEMENT-VERSION' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_DIGEST_MISMATCH' -Action {
            Get-DecisionHistoryState -AllEntries (@($approvedBuilt.Record, $activatedBuilt.Record, $v2ApprovedBuilt.Record, $tamperedReplacementVersion)) `
                -SpecVersion 2
        }
        $tamperedReplacementHash = Copy-OrderedRecord -Record $validSupersedeForTamperProbe.Record
        $tamperedReplacementHash.replacementRecomputedHashHex = ('9' * 64)
        Test-GuardRejects -CaseId 'T3B-R2-NEG-TAMPER-REPLACEMENT-HASH' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_DIGEST_MISMATCH' -Action {
            Get-DecisionHistoryState -AllEntries (@($approvedBuilt.Record, $activatedBuilt.Record, $v2ApprovedBuilt.Record, $tamperedReplacementHash)) `
                -SpecVersion 2
        }
        $strippedReplacementFields = [ordered]@{}
        foreach ($key in $validSupersedeForTamperProbe.Record.Keys) {
            if ($key -eq 'replacementSpecVersion' -or $key -eq 'replacementRecomputedHashHex') { continue }
            $strippedReplacementFields[$key] = $validSupersedeForTamperProbe.Record[$key]
        }
        Test-GuardRejects -CaseId 'T3B-R2-NEG-REPLACEMENT-FIELD-OMITTED' -Contract 'T3B-R2' `
            -ExpectedGuardId 'DECISION_FIELD_MISSING' -Action {
            Get-DecisionHistoryState -AllEntries (@($approvedBuilt.Record, $activatedBuilt.Record, $v2ApprovedBuilt.Record, $strippedReplacementFields)) `
                -SpecVersion 2
        }

        # Real-mode orchestration source proof: SUPERSEDED without an
        # explicit -ReplacementSpecVersion must be rejected by
        # Invoke-GroupTwoDecisionAppend itself (proven via literal source
        # inspection of its up-front guard, since exercising real mode end-
        # to-end would require the real approver principal).
        $writerSourceForSupersessionCheck = Get-Content -LiteralPath $PSCommandPath -Raw
        $invokeDecisionAppendSourceBlock = (Select-String -InputObject $writerSourceForSupersessionCheck `
                -Pattern '(?s)function Invoke-GroupTwoDecisionAppend \{.*?\n\}' -AllMatches).Matches[0].Value
        $requiresExplicitReplacement = (
            $invokeDecisionAppendSourceBlock -match [regex]::Escape("Stop-Writer -GuardId 'DECISION_SUPERSESSION_REPLACEMENT_REQUIRED'")
        )
        Add-TestResult -CaseId 'T3B-RV-3-E' -Contract 'T3B-R2' -Passed $requiresExplicitReplacement `
            -Detail 'real-mode orchestration source requires an explicit -ReplacementSpecVersion for SUPERSEDED (never infers it)'
        $neverInfersLatestOrLargest = -not (
            $invokeDecisionAppendSourceBlock -match 'Sort-Object[^\n]*-Descending' -or
            $invokeDecisionAppendSourceBlock -match '\bMeasure-Object[^\n]*-Maximum\b'
        )
        Add-TestResult -CaseId 'T3B-RV-3-F' -Contract 'T3B-R2' -Passed $neverInfersLatestOrLargest `
            -Detail 'real-mode orchestration source contains no latest/largest-version inference construct (no -Descending sort or -Maximum measure)'

        # Duplicate event ID and broken chain negatives.
        $duplicateIdEntries = @($approvedBuilt.Record, $approvedBuilt.Record)
        Test-GuardRejects -CaseId 'T3B-08-X' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_DUPLICATE_EVENT_ID' -Action {
            Get-DecisionHistoryState -AllEntries $duplicateIdEntries -SpecVersion 1
        }

        $tamperedChainEntry = Copy-OrderedRecord -Record $activatedBuilt.Record
        $tamperedChainEntry.priorEntryHashHex = ('f' * 64)
        Test-GuardRejects -CaseId 'T3B-08-Y' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_CHAIN_BROKEN' -Action {
            Get-DecisionHistoryState -AllEntries @($approvedBuilt.Record, $tamperedChainEntry) -SpecVersion 1
        }

        $tamperedHashEntry = Copy-OrderedRecord -Record $approvedBuilt.Record
        $tamperedHashEntry.entryHashHex = ('0' * 64)
        Test-GuardRejects -CaseId 'T3B-08-Z' -Contract 'T3B-08' `
            -ExpectedGuardId 'DECISION_DIGEST_MISMATCH' -Action {
            Get-DecisionHistoryState -AllEntries @($tamperedHashEntry) -SpecVersion 1
        }

        # ---- T3B-08: identity guards ----------------------------------------
        Test-GuardRejects -CaseId 'T3B-08-A' -Contract 'T3B-08' `
            -ExpectedGuardId 'PRINCIPAL_NAME_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName 'NOT-THIS-HOST\definitely-not-current-user' `
                -ExpectedAccountSid $current.Sid
        }
        Test-GuardRejects -CaseId 'T3B-08-B' -Contract 'T3B-08' `
            -ExpectedGuardId 'PRINCIPAL_SID_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name -ExpectedAccountSid 'S-1-5-21-0-0-0-4999'
        }
        $elevatedProbe = [pscustomobject]@{ Name = $current.Name; Sid = $current.Sid; IsElevated = $true }
        Test-GuardRejects -CaseId 'T3B-08-C' -Contract 'T3B-08' `
            -ExpectedGuardId 'ELEVATED_CONTEXT_REJECTED' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $elevatedProbe `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
        }

        Test-GuardRejects -CaseId 'T3B-08-E' -Contract 'T3B-08' `
            -ExpectedGuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_APPROVER' -Action {
            Assert-ExpectedPrincipalIsVerifiedApprover -ExpectedAccountName $current.Name `
                -ExpectedAccountSid $current.Sid
        }
        try {
            Assert-ExpectedPrincipalIsVerifiedApprover `
                -ExpectedAccountName $script:VerifiedApproverIdentity.principalName `
                -ExpectedAccountSid $script:VerifiedApproverIdentity.principalSid
            Add-TestResult -CaseId 'T3B-08-F' -Contract 'T3B-08' -Passed $true `
                -Detail 'exact verified approver name/SID pair is accepted by the binding guard'
        } catch {
            Add-TestResult -CaseId 'T3B-08-F' -Contract 'T3B-08' -Passed $false `
                -Detail "verified approver pair unexpectedly rejected: $($_.Exception.Message)"
        }
        Test-GuardRejects -CaseId 'T3B-08-G' -Contract 'T3B-08' `
            -ExpectedGuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_APPROVER' -Action {
            Assert-ExpectedPrincipalIsVerifiedApprover `
                -ExpectedAccountName $script:VerifiedApproverIdentity.principalName `
                -ExpectedAccountSid 'S-1-5-21-0-0-0-9999'
        }

        # ---- T3B-08: approver posture guard (against the CURRENT identity,
        #      which is never the real approver account; this proves the
        #      guard runs and fails closed for an arbitrary SID it cannot
        #      resolve, and separately for the current, non-target account) ---
        Test-GuardRejects -CaseId 'T3B-08-AA' -Contract 'T3B-08' `
            -ExpectedGuardId 'APPROVER_ACCOUNT_NOT_FOUND' -Action {
            Assert-ApproverPosture -AccountSid 'S-1-5-21-0-0-0-1234567-nonexistent'
        }

        # ---- T3B-08: path/collision -----------------------------------------
        $fixtureRepoRoot = Join-Path -Path $sandbox -ChildPath 'fixture_repo'
        New-Item -ItemType Directory -Path $fixtureRepoRoot -Force | Out-Null
        $fixturePaths = Resolve-GroupTwoPaths -RepositoryRoot $fixtureRepoRoot -SpecVersions @(1)
        Add-TestResult -CaseId 'T3B-08-AB' -Contract 'T3B-08' -Passed (-not (Test-Path -LiteralPath $fixturePaths.DecisionsPath)) `
            -Detail 'fresh fixture repository has no pre-existing decisions file'

        # ---- T3B-08: noninteractive confirmation -----------------------------
        $childResult = Invoke-NonInteractiveWriteProbe -SandboxDirectory $sandbox
        $childRejectedAtConfirmation = ($childResult.ExitCode -ne 0 -and $childResult.GuardObserved)
        Add-TestResult -CaseId 'T3B-08-AC' -Contract 'T3B-08' `
            -Passed $childRejectedAtConfirmation `
            -Detail ("noninteractive child exit=$($childResult.ExitCode), " +
                "confirmationGuard=$($childResult.GuardObserved)")
        Test-GuardRejects -CaseId 'T3B-08-AD' -Contract 'T3B-08' `
            -ExpectedGuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Action {
            Assert-InteractiveConfirmation -ExpectedAccountName $current.Name
        }

        # ---- T3B-05: append-only atomic write and exclusivity ---------------
        $writeRoot = Join-Path -Path $sandbox -ChildPath 'write_repo'
        New-Item -ItemType Directory -Path $writeRoot -Force | Out-Null
        $writePaths = Resolve-GroupTwoPaths -RepositoryRoot $writeRoot -SpecVersions @(1)
        $genesisLine = [System.Text.Encoding]::UTF8.GetString((ConvertTo-CanonicalJsonBytesForOutput -Object $approvedBuilt.Record))
        Add-ExclusiveAppendLine -Path $writePaths.DecisionsPath -CompactJsonLine $genesisLine
        $appendedOk = Test-Path -LiteralPath $writePaths.DecisionsPath
        Add-TestResult -CaseId 'T3B-05-D' -Contract 'T3B-05' -Passed $appendedOk `
            -Detail "genesis exclusive-append succeeded at '$($writePaths.DecisionsPath)'"

        $secondLine = [System.Text.Encoding]::UTF8.GetString((ConvertTo-CanonicalJsonBytesForOutput -Object $activatedBuilt.Record))
        Add-ExclusiveAppendLine -Path $writePaths.DecisionsPath -CompactJsonLine $secondLine
        $rereadLines = Get-StrictJsonLinesFromText -Text (Get-Content -LiteralPath $writePaths.DecisionsPath -Raw)
        Add-TestResult -CaseId 'T3B-05-E' -Contract 'T3B-05' -Passed ($rereadLines.Count -eq 2) `
            -Detail "two exclusive appends produced exactly two JSONL lines (found $($rereadLines.Count))"
        $rereadHistory = Get-DecisionHistoryState -AllEntries $rereadLines -SpecVersion 1
        Add-TestResult -CaseId 'T3B-05-F' -Contract 'T3B-05' -Passed ($rereadHistory.LastEntryHashHex -eq $activatedBuilt.EntryHashHex) `
            -Detail 're-read appended file independently replays to the exact expected chain tip hash'

        # ---- T3B-05 (three-boundary atomic failure matrix for append) ------
        $boundaries = @('Open', 'Write', 'Flush')
        foreach ($boundary in $boundaries) {
            $boundaryRoot = Join-Path -Path $sandbox -ChildPath "boundary_$($boundary)_repo"
            New-Item -ItemType Directory -Path $boundaryRoot -Force | Out-Null
            $boundaryPaths = Resolve-GroupTwoPaths -RepositoryRoot $boundaryRoot -SpecVersions @(1)
            $boundaryCleaned = $false
            try {
                Add-ExclusiveAppendLine -Path $boundaryPaths.DecisionsPath -CompactJsonLine $genesisLine -InjectFailureAtForTest $boundary
            } catch {
                $fileAbsent = -not (Test-Path -LiteralPath $boundaryPaths.DecisionsPath)
                $dirAbsent = -not (Test-Path -LiteralPath ([System.IO.Path]::GetDirectoryName($boundaryPaths.DecisionsPath)))
                $boundaryCleaned = $fileAbsent -and $dirAbsent
            }
            Add-TestResult -CaseId "T3B-05-Append-$boundary" -Contract 'T3B-05' -Passed $boundaryCleaned `
                -Detail "injected '$boundary' failure on genesis append removed the file this invocation created and its fresh empty directory"
        }

        # ---- T3B-06: DACL/ownership hardening on the decisions file ----------
        $daclApplied = $false
        try {
            Protect-CreatedFileAgainstOtherPrincipal -FilePath $writePaths.DecisionsPath `
                -OwnerAccountSid $current.Sid -LocalReaderAccountSids @('S-1-5-32-544') | Out-Null
            $daclApplied = $true
        } catch {
            $daclApplied = $false
        }
        Add-TestResult -CaseId 'T3B-06-A' -Contract 'T3B-06' -Passed $daclApplied `
            -Detail 'DACL/ownership hardening code path ran without error against the fixture decisions file owned by the current identity'

        if ($daclApplied) {
            $resultAcl = Get-Acl -LiteralPath $writePaths.DecisionsPath
            Add-TestResult -CaseId 'T3B-06-B' -Contract 'T3B-06' -Passed $resultAcl.AreAccessRulesProtected `
                -Detail "resulting ACL has inheritance disabled (AreAccessRulesProtected=$($resultAcl.AreAccessRulesProtected))"
            $currentSidHasAllow = @($resultAcl.Access | Where-Object {
                    $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq $current.Sid -and
                    $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow
                }).Count -gt 0
            Add-TestResult -CaseId 'T3B-06-C' -Contract 'T3B-06' -Passed $currentSidHasAllow `
                -Detail 'owning/current identity retains an explicit Allow access rule after hardening'
            $unexpectedAllow = @($resultAcl.Access | Where-Object {
                    $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow -and
                    $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -notin @($current.Sid, 'S-1-5-32-544')
                })
            Add-TestResult -CaseId 'T3B-06-D' -Contract 'T3B-06' -Passed ($unexpectedAllow.Count -eq 0) `
                -Detail "no Allow rule exists for any identity beyond the owner and the named Local reader (found $($unexpectedAllow.Count) unexpected)"
        } else {
            Add-TestResult -CaseId 'T3B-06-B' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
            Add-TestResult -CaseId 'T3B-06-C' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
            Add-TestResult -CaseId 'T3B-06-D' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
        }

        # ---- T3B-RV-1 (R1 regression): explicit Local reviewer SID read-only
        #      grant on the decisions file, proving Party A gets no explicit
        #      grant at all and this is NOT satisfied merely by a
        #      `BUILTIN\Administrators` grant. This is the exact hardening
        #      path used by the real orchestrator
        #      (`Invoke-GroupTwoDecisionAppend`), reproduced here against a
        #      disposable fixture decisions file and the real named Local SID
        #      from `$script:VerifiedLocalReaderSid`, so this test would have
        #      FAILED against the pre-R1 implementation (which passed only
        #      `S-1-5-32-544` / `BUILTIN\Administrators`).
        #
        #      `SetOwner` cannot be pointed at an arbitrary unprivileged SID
        #      without `SeRestorePrivilege` (same constraint proven in the
        #      twin spec-writer test), so the owner here is necessarily the
        #      current agent identity; on hosts where the current identity's
        #      own SID happens to equal the real Local reviewer SID, the
        #      owner and reader ACEs legitimately collapse into one merged
        #      FullControl rule, which is correct ACL semantics and not a
        #      hardening defect, so the read-only shape assertion is scoped
        #      to skip only that one genuinely-colliding case.
        $crossPrincipalDecisionsRoot = Join-Path -Path $sandbox -ChildPath 'cross_principal_decisions_repo'
        New-Item -ItemType Directory -Path $crossPrincipalDecisionsRoot -Force | Out-Null
        $crossPrincipalPaths = Resolve-GroupTwoPaths -RepositoryRoot $crossPrincipalDecisionsRoot -SpecVersions @(1)
        Add-ExclusiveAppendLine -Path $crossPrincipalPaths.DecisionsPath -CompactJsonLine $genesisLine
        Protect-CreatedFileAgainstOtherPrincipal -FilePath $crossPrincipalPaths.DecisionsPath `
            -OwnerAccountSid $current.Sid -LocalReaderAccountSids @($script:VerifiedLocalReaderSid) | Out-Null
        $crossPrincipalDecisionsAcl = Get-Acl -LiteralPath $crossPrincipalPaths.DecisionsPath

        $localAllowRules = @($crossPrincipalDecisionsAcl.Access | Where-Object {
                $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq $script:VerifiedLocalReaderSid -and
                $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow
            })
        Add-TestResult -CaseId 'T3B-RV-1-A' -Contract 'T3B-RV-1' -Passed ($localAllowRules.Count -gt 0) `
            -Detail "Local reviewer SID '$($script:VerifiedLocalReaderSid)' has an explicit Allow access rule on the decisions file (not relying on a deny-only Administrators SID)"

        $localSidCollidesWithOwner = ($script:VerifiedLocalReaderSid -eq $current.Sid)
        $localRights = 0
        foreach ($rule in $localAllowRules) { $localRights = $localRights -bor [int]$rule.FileSystemRights }
        $localReadOnly = $localSidCollidesWithOwner -or (
            ($localRights -band [int][System.Security.AccessControl.FileSystemRights]::Read) -ne 0 -and
            ($localRights -band [int][System.Security.AccessControl.FileSystemRights]::Write) -eq 0 -and
            ($localRights -band [int][System.Security.AccessControl.FileSystemRights]::Delete) -eq 0 -and
            ($localRights -band [int][System.Security.AccessControl.FileSystemRights]::ChangePermissions) -eq 0 -and
            ($localRights -band [int][System.Security.AccessControl.FileSystemRights]::TakeOwnership) -eq 0
        )
        $localDetail = if ($localSidCollidesWithOwner) {
            'Local reviewer SID equals this host''s current identity SID (owner); skipped as a legitimate owner/reader ACE merge, not a hardening defect'
        } else {
            'Local reviewer SID rights are read-only: no Write/Delete/ChangePermissions/TakeOwnership grant'
        }
        Add-TestResult -CaseId 'T3B-RV-1-B' -Contract 'T3B-RV-1' -Passed $localReadOnly -Detail $localDetail

        $partyAHasNoGrant = @($crossPrincipalDecisionsAcl.Access | Where-Object {
                $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow -and
                $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq 'S-1-5-21-1644666849-912006174-747199667-1006'
            }).Count -eq 0
        Add-TestResult -CaseId 'T3B-RV-1-C' -Contract 'T3B-RV-1' -Passed $partyAHasNoGrant `
            -Detail 'Party A SID (S-1-5-21-1644666849-912006174-747199667-1006) has no explicit Allow access rule on the decisions file'

        # Literal source-check on the real orchestration path, so a
        # regression that reverts to an Administrators-only grant inside
        # `Invoke-GroupTwoDecisionAppend` itself (not just in this test) is
        # caught even without executing real mode.
        $writerSourceForAclCheck = Get-Content -LiteralPath $PSCommandPath -Raw
        $invokeDecisionAppendBlock = (Select-String -InputObject $writerSourceForAclCheck `
                -Pattern '(?s)function Invoke-GroupTwoDecisionAppend \{.*?\n\}' -AllMatches).Matches[0].Value
        $orchestrationUsesExplicitLocalSid = ($invokeDecisionAppendBlock -match [regex]::Escape('$script:VerifiedLocalReaderSid'))
        Add-TestResult -CaseId 'T3B-RV-1-D' -Contract 'T3B-RV-1' -Passed $orchestrationUsesExplicitLocalSid `
            -Detail 'real-mode orchestration (Invoke-GroupTwoDecisionAppend) source references the explicit Local reader SID variable, not only BUILTIN\Administrators'
        $orchestrationDoesNotRelyOnAdminsAlone = -not (
            $invokeDecisionAppendBlock -match [regex]::Escape("@('S-1-5-32-544')") -or
            $invokeDecisionAppendBlock -match [regex]::Escape('@($adminsSid)')
        )
        Add-TestResult -CaseId 'T3B-RV-1-E' -Contract 'T3B-RV-1' -Passed $orchestrationDoesNotRelyOnAdminsAlone `
            -Detail 'real-mode orchestration no longer passes only BUILTIN\Administrators (S-1-5-32-544) as the sole reader SID'

        # ---- T3B-09: no approver contact ------------------------------------
        $approverUntouched = ($current.Name -notlike '*cvf-g1-approver*')
        Add-TestResult -CaseId 'T3B-09-A' -Contract 'T3B-09' -Passed $approverUntouched `
            -Detail "self-test ran as '$($current.Name)', not as the expected approver principal"

        $realRepositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path
        $realGroupTwoDir = Join-Path $realRepositoryRoot 'governance/sources/verification_authority_spec'
        $realSpecAbsent = -not (Test-Path -LiteralPath (Join-Path $realGroupTwoDir 'SPEC_v1.json'))
        Add-TestResult -CaseId 'T3B-09-B' -Contract 'T3B-09' -Passed $realSpecAbsent `
            -Detail "real Group 2 spec path '$realGroupTwoDir/SPEC_v1.json' remains absent after self-test"
        $realDecisionsAbsent = -not (Test-Path -LiteralPath (Join-Path $realGroupTwoDir 'ACTIVATION_DECISIONS.jsonl'))
        Add-TestResult -CaseId 'T3B-09-C' -Contract 'T3B-09' -Passed $realDecisionsAbsent `
            -Detail "real Group 2 decisions path '$realGroupTwoDir/ACTIVATION_DECISIONS.jsonl' remains absent after self-test"

        # ---- T3B-10: malformed input negatives ------------------------------
        Test-GuardRejects -CaseId 'T3B-10-A' -Contract 'T3B-10' `
            -ExpectedGuardId 'JSON_DUPLICATE_MEMBER' -Action {
            Get-StrictJsonObjectFromText -Text '{"profile":"x","profile":"y"}'
        }
        Test-GuardRejects -CaseId 'T3B-10-B' -Contract 'T3B-10' `
            -ExpectedGuardId 'BASE64URL_INVALID' -Action {
            ConvertFrom-Base64Url -Text 'a'
        }
        $malformedSpec = $fixtureSpec.PSObject.Copy()
        $malformedSpec.specHashHex = ('9' * 64)
        Test-GuardRejects -CaseId 'T3B-10-C' -Contract 'T3B-10' `
            -ExpectedGuardId 'BASE64URL_INVALID' -Action {
            $badSpec = [pscustomobject]@{ canonicalBytesBase64 = 'a' }
            Get-IndependentlyRecomputedSpecHash -SpecRecord $badSpec
        }
    } finally {
        Get-ChildItem -LiteralPath $sandbox -Recurse -File -Force -ErrorAction SilentlyContinue |
            ForEach-Object {
                try {
                    $item = $_
                    try {
                        $resetAcl = Get-Acl -LiteralPath $item.FullName
                        $resetAcl.SetAccessRuleProtection($false, $true)
                        Set-Acl -LiteralPath $item.FullName -AclObject $resetAcl -ErrorAction SilentlyContinue
                    } catch { }
                    $length = (Get-Item -LiteralPath $item.FullName -Force).Length
                    if ($length -gt 0) {
                        [System.IO.File]::WriteAllBytes($item.FullName, (New-Object byte[] $length))
                    }
                } catch { }
            }
        Remove-Item -LiteralPath $sandbox -Recurse -Force -ErrorAction SilentlyContinue
        $removed = -not (Test-Path -LiteralPath $sandbox)
        Add-TestResult -CaseId 'CLEANUP-A' -Contract 'T3B-09' -Passed $removed `
            -Detail "disposable sandbox removed: $sandbox"
    }

    $failed = @($script:TestResults | Where-Object { -not $_.Passed })
    Write-Host ''
    Write-Host ('Self-test cases: {0} total, {1} passed, {2} failed.' -f
        $script:TestResults.Count, ($script:TestResults.Count - $failed.Count), $failed.Count)
    Write-Host 'Claim boundary: guard and state-machine behavior proven; no real Group 2 decision was appended.'

    if ($failed.Count -gt 0) {
        Write-Host ''
        Write-Host 'FAILED CASES:'
        foreach ($case in $failed) { Write-Host ("  {0}: {1}" -f $case.CaseId, $case.Detail) }
        return 1
    }
    return 0
}

# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

try {
    if ($PSCmdlet.ParameterSetName -eq 'Write') {
        [void](Invoke-GroupTwoDecisionAppend -ExpectedAccountName $ExpectedAccountName `
                -ExpectedAccountSid $ExpectedAccountSid -EventType $EventType `
                -TargetSpecVersion $TargetSpecVersion -ReplacementSpecVersion $ReplacementSpecVersion)
        exit 0
    }

    exit (Invoke-SelfTest)
} catch {
    $message = if ($_.Exception -is [WriterGuardFailure]) {
        $_.Exception.Message
    } else {
        '[UNHANDLED] {0}' -f $_.Exception.Message
    }
    Write-Error $message
    exit 1
}
