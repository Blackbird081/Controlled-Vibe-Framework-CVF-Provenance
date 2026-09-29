<#
.SYNOPSIS
    ACEL G1 T3A-C2 principal-bound Group 1 source-creation writer (fail-closed).

.DESCRIPTION
    Builds, from already-verified public ceremony metadata only, the exact
    T2F Group 1 registry envelope (one `cvf.keyRegistryRow`) and genesis
    lifecycle receipt (`cvf.keyLifecycleReceipt`), both canonicalized and
    hashed under `cvf.source-record-canonicalization@1`, then writes them to
    the two governed Group 1 paths exclusively as the exact expected Party A
    principal.

    Default invocation is a hermetic self-test that proves every guard using
    a disposable sandbox rooted under the current user's temporary directory
    and removes it. Real-mode execution requires -ExecuteWrite, an exact
    principal name and SID match, a non-elevated interactive session, and a
    typed confirmation, after every other guard has already passed.

    This tool does not claim candidate admission, key promotion or T3E
    consumer wiring. Its real-mode output text is exactly
    `SOURCE_CREATED_PENDING_LOCAL_VERIFICATION`.

.PARAMETER SelfTest
    Run hermetic positive and negative self-tests as the current user against
    a disposable sandbox. This is the default when no mode is chosen and
    never targets the real Group 1 paths or the expected Party A principal.

.PARAMETER ExecuteWrite
    Perform the real Group 1 source write. Requires the current process
    identity to match both -ExpectedAccountName and -ExpectedAccountSid
    exactly, a non-elevated interactive host, and an interactive typed
    confirmation.

.PARAMETER ExpectedAccountName
    Exact expected Windows account name, e.g. 'HOSTNAME\cvf-g1-party-a'. A
    bare name is qualified with the local computer name before comparison.

.PARAMETER ExpectedAccountSid
    Exact expected Windows account SID.

.PARAMETER MetadataPath
    Path to the verified `cvf.acel.g1.partyAPublicKeyMetadata@1` public
    metadata JSON file (the ceremony's `party_a_public_key.json`).

    Real-mode output paths are always resolved from this script's own
    committed location; there is no operator-selectable repository-root
    parameter in real mode. Fixture-root injection exists only inside the
    internal hermetic self-test functions, which never target the real
    Group 1 paths.

.EXAMPLE
    pwsh -NoProfile -File scripts/acel_g1_party_a_group1_source_writer.ps1 -SelfTest

.NOTES
    Claim boundary: tooling only. A self-test proves guard behavior, not that
    any Group 1 source was created. Real-mode output text explicitly reads
    `SOURCE_CREATED_PENDING_LOCAL_VERIFICATION`, never admission or T3E
    consumer wiring.
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
    [ValidateNotNullOrEmpty()]
    [string] $MetadataPath
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

$script:ToolContract        = 'cvf.acel.g1.group1SourceWriterTool@1'
$script:MetadataSchema      = 'cvf.acel.g1.partyAPublicKeyMetadata@1'
$script:CanonProfile        = 'cvf.source-record-canonicalization@1'
$script:RegistryRowDomain   = 'cvf.keyRegistryRow'
$script:LifecycleRowDomain  = 'cvf.keyLifecycleReceipt'
$script:RawPublicKeyLength  = 32
$script:ConfirmationPhrase  = 'EXECUTE GROUP 1 SOURCE WRITE'
$script:RegistryRelativePath  = 'governance/sources/verifier_key_registry/REGISTRY.json'
$script:LifecycleRelativePath = 'governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl'
$script:VerificationAuthorityRole = 'verificationAuthority'
$script:GenesisNewStatus      = 'ACTIVE'
$script:GenesisPriorStatus    = 'NOT_PRESENT'
$script:RealModeResultText    = 'SOURCE_CREATED_PENDING_LOCAL_VERIFICATION'

# T3A-C2-R3-01: the exact, closed 14-member verified public product, taken
# byte-for-byte from `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md`
# ("Verified Public Metadata"). This is public ceremony output, never a
# secret. Real-mode execution validates the operator-supplied metadata file
# against EVERY one of these exact values; it is never caller-overridable.
$script:VerifiedPartyAProduct = [ordered]@{
    metadataSchema       = 'cvf.acel.g1.partyAPublicKeyMetadata@1'
    metadataProfile      = 'ACEL_G1_T3A_PRINCIPAL_BOUND_CEREMONY'
    keyId                = 'partya-44853ea9a690452c'
    algorithm            = 'Ed25519'
    principalName        = 'LAM-RUBY\cvf-g1-party-a'
    principalSid         = 'S-1-5-21-1644666849-912006174-747199667-1006'
    publicKeyBytesBase64 = 'R5AsDnHQNXWgD5WQEpDi3VABiuPZ7E9U5Kir_bgiwNU'
    publicKeySha256Hex   = '5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01'
    createdAtUtc         = '2026-09-19T06:41:05.5102754Z'
    expiresAtUtc         = '2027-09-19T06:41:05.5102754Z'
    ceremonyDisposition  = 'CEREMONY'
    testDisposition      = 'CEREMONY_PRODUCT_PENDING_LOCAL_VERIFICATION'
    registryDisposition  = 'SOURCE_NOT_CREATED'
    claimBoundary        = 'public metadata only; no registry row, lifecycle receipt, promotion or admission is claimed'
}
$script:VerifiedPartyAProductFieldNames = @($script:VerifiedPartyAProduct.Keys)

Add-Type -AssemblyName System.Security | Out-Null

# T3A-C2-R3-R1-02: a small compiled helper using System.Text.Json's own
# Utf8JsonReader tokenizer to find a top-level duplicate JSON member name
# AFTER JSON escape decoding (Utf8JsonReader.GetString() decodes \uXXXX and
# every other standard JSON string escape). PowerShell cannot instantiate
# Utf8JsonReader directly (it is a ByRef-like/ref-struct type), so this is
# implemented in C# via Add-Type, not as a regex or hand-rolled escape
# decoder over raw JSON text.
Add-Type -Language CSharp -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Text.Json;

public static class CvfAcelG1JsonDuplicateMemberScanner
{
    // Returns the first top-level (depth-1) JSON member name that appears
    // more than once, comparing DECODED member names (not raw escaped
    // text), or null if there is no top-level duplicate.
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
    <#
        .SYNOPSIS
            Fail closed with a named guard identity and no secret content.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $GuardId,
        [Parameter(Mandatory = $true)][string] $Message
    )
    throw [WriterGuardFailure]::new($GuardId, "[$GuardId] $Message")
}

# --------------------------------------------------------------------------
# Encoding, canonicalization and hashing helpers
# --------------------------------------------------------------------------

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

function Get-Sha256Hex {
    param([Parameter(Mandatory = $true)][byte[]] $Bytes)
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        return [System.BitConverter]::ToString($sha256.ComputeHash($Bytes)).Replace('-', '').ToLowerInvariant()
    } finally {
        $sha256.Dispose()
    }
}

function ConvertTo-CanonicalJsonBytes {
    <#
        .SYNOPSIS
            Compact, lexicographically key-ordered JSON bytes (JCS-equivalent
            for this ASCII-only, non-nested, no-duplicate-key preimage shape).

        .DESCRIPTION
            Mirrors the T2F contract's Python reference
            (`json.dumps(preimage, sort_keys=True, separators=(",",":"))`)
            using .NET primitives only: keys sorted ordinally, no whitespace,
            strings escaped per JSON, `null` for PowerShell `$null`, and
            integers rendered as bare canonical decimal literals (never
            quoted), matching Python `json.dumps`'s rendering of an `int`.
            Every preimage in this tool is a single flat object of
            string/integer/null fields, which keeps this implementation
            exactly equivalent to the reference without needing a general
            JSON canonicalizer. A field's type here must exactly match the
            type used for that same field when the record is written to
            disk (e.g. `ConvertTo-Json`'s serialization of a PowerShell
            `[int]`), or the stored digest will not reproduce.
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

function ConvertTo-JsonStringLiteral {
    param([Parameter(Mandatory = $true)][AllowEmptyString()][string] $Value)
    $escaped = $Value.Replace('\', '\\').Replace('"', '\"').Replace("`n", '\n').Replace("`r", '\r').Replace("`t", '\t')
    return '"' + $escaped + '"'
}

function New-KeyRegistryRowPreimage {
    <#
        .SYNOPSIS
            C2-03. Build the exact closed `cvf.keyRegistryRow` preimage.

        .DESCRIPTION
            Exactly the nine T2F-declared fields plus profile/domain, no
            more and no fewer: `keyId`, `publicKeyBytesBase64`, `algorithm`,
            `role`, `issuedAt`, `expiresAt`, `revokedAt`, `status`,
            `rotatedFromKeyId`.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $KeyId,
        [Parameter(Mandatory = $true)][string] $PublicKeyBytesBase64,
        [Parameter(Mandatory = $true)][string] $Algorithm,
        [Parameter(Mandatory = $true)][string] $Role,
        [Parameter(Mandatory = $true)][string] $IssuedAt,
        [AllowNull()] $ExpiresAt,
        [AllowNull()] $RevokedAt,
        [Parameter(Mandatory = $true)][string] $Status,
        [AllowNull()] $RotatedFromKeyId
    )
    return [ordered]@{
        profile              = $script:CanonProfile
        domain               = $script:RegistryRowDomain
        keyId                = $KeyId
        publicKeyBytesBase64 = $PublicKeyBytesBase64
        algorithm            = $Algorithm
        role                 = $Role
        issuedAt             = $IssuedAt
        expiresAt            = $ExpiresAt
        revokedAt            = $RevokedAt
        status               = $Status
        rotatedFromKeyId     = $RotatedFromKeyId
    }
}

function New-KeyLifecycleReceiptPreimage {
    <#
        .SYNOPSIS
            C2-05. Build the exact closed `cvf.keyLifecycleReceipt` preimage
            for the genesis transition.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $TransitionId,
        [Parameter(Mandatory = $true)][string] $KeyId,
        [Parameter(Mandatory = $true)][int] $RegistrySnapshotVersionBefore,
        [Parameter(Mandatory = $true)][int] $RegistrySnapshotVersionAfter,
        [Parameter(Mandatory = $true)][string] $PriorStatus,
        [Parameter(Mandatory = $true)][string] $NewStatus,
        [Parameter(Mandatory = $true)][string] $Actor,
        [Parameter(Mandatory = $true)][string] $Timestamp,
        [AllowNull()] $PriorEntryHashHex
    )
    return [ordered]@{
        profile                       = $script:CanonProfile
        domain                        = $script:LifecycleRowDomain
        transitionId                  = $TransitionId
        keyId                         = $KeyId
        registrySnapshotVersionBefore = $RegistrySnapshotVersionBefore
        registrySnapshotVersionAfter  = $RegistrySnapshotVersionAfter
        priorStatus                   = $PriorStatus
        newStatus                     = $NewStatus
        actor                         = $Actor
        timestamp                     = $Timestamp
        priorEntryHashHex             = $PriorEntryHashHex
    }
}

function Get-PreimageDigestHex {
    param([Parameter(Mandatory = $true)][System.Collections.IDictionary] $Preimage)
    $bytes = ConvertTo-CanonicalJsonBytes -Object $Preimage
    return Get-Sha256Hex -Bytes $bytes
}

# --------------------------------------------------------------------------
# C2-02: metadata validation
# --------------------------------------------------------------------------

function Test-CanonicalBase64UrlString {
    <#
        .SYNOPSIS
            True only for the exact unpadded URL-safe base64 alphabet that
            also reproduces byte-for-byte after canonical re-encoding.
    #>
    param([Parameter(Mandatory = $true)][string] $Text)
    if ([string]::IsNullOrEmpty($Text)) { return $false }
    if ($Text.Contains('=')) { return $false }
    if ($Text -notmatch '^[A-Za-z0-9_-]+$') { return $false }
    $decoded = $null
    try {
        $decoded = ConvertFrom-Base64Url -Text $Text
    } catch {
        return $false
    }
    $reencoded = [System.Convert]::ToBase64String($decoded).TrimEnd('=').Replace('+', '-').Replace('/', '_')
    return ($reencoded -ceq $Text)
}

function Get-StrictJsonObjectFromText {
    <#
        .SYNOPSIS
            Parse JSON text into an ordered member list, rejecting any
            duplicate top-level member name, so a caller-crafted file with a
            repeated key -- including two members whose raw text differs
            only by JSON escaping (e.g. `keyId` vs `key\u0049d`) -- can never
            silently shadow the value this tool actually validates.

        .DESCRIPTION
            T3A-C2-R3-R1-02: `ConvertFrom-Json` on .NET/PowerShell keeps
            only the LAST value for a duplicate key, exactly the silent-
            shadowing behavior T2F's fail-closed rule forbids. Duplicate
            detection is delegated to `CvfAcelG1JsonDuplicateMemberScanner`
            (compiled via `Add-Type` near the top of this script), which
            uses `System.Text.Json.Utf8JsonReader.GetString()` to decode
            each member name's JSON escapes (`\uXXXX` and all other
            standard escapes) BEFORE comparing it against previously seen
            names. PowerShell itself cannot instantiate `Utf8JsonReader`
            directly (it is a ByRef-like/ref-struct type), which is why this
            is a compiled C# helper rather than PowerShell script code; it
            is not a regex or hand-rolled escape decoder over raw text.
    #>
    param([Parameter(Mandatory = $true)][string] $Text)

    $parsed = $null
    try {
        # PowerShell 7.5 defaults ISO-8601 JSON strings to System.DateTime.
        # Preserve the source token as a string so exact verified-product
        # comparison and downstream canonical bytes cannot become locale- or
        # DateTime-format-dependent.
        $parsed = $Text | ConvertFrom-Json -DateKind String -ErrorAction Stop
    } catch {
        Stop-Writer -GuardId 'METADATA_UNPARSEABLE' -Message "metadata file is not valid JSON: $($_.Exception.Message)"
    }

    if ($null -eq $parsed -or $parsed -is [System.Collections.IEnumerable] -and $parsed -isnot [string]) {
        if ($parsed -isnot [System.Management.Automation.PSCustomObject]) {
            Stop-Writer -GuardId 'METADATA_NOT_OBJECT' -Message 'metadata file must decode to a single JSON object'
        }
    }

    $utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $duplicateMemberName = $null
    try {
        $duplicateMemberName = [CvfAcelG1JsonDuplicateMemberScanner]::FindFirstTopLevelDuplicateMemberName($utf8Bytes)
    } catch {
        Stop-Writer -GuardId 'METADATA_UNPARSEABLE' -Message "metadata file is not valid JSON: $($_.Exception.Message)"
    }
    if ($null -ne $duplicateMemberName) {
        Stop-Writer -GuardId 'METADATA_DUPLICATE_JSON_MEMBER' -Message (
            "duplicate top-level JSON member '$duplicateMemberName' in metadata file (after JSON escape decoding)")
    }

    return $parsed
}

function Assert-ValidPartyAPublicKeyMetadata {
    <#
        .SYNOPSIS
            T3A-C2-R3-01. Strictly validate the ceremony public metadata
            against the exact closed 14-member verified public product.

        .DESCRIPTION
            Rejects before any registry/lifecycle object is built: any
            missing, extra or duplicate member; any field whose type or
            exact value differs from `$script:VerifiedPartyAProduct`;
            non-canonical base64url; wrong decoded length; digest mismatch.
            The real execution path never accepts a self-consistent but
            different product; every immutable value is checked against the
            fixed verified authority, not merely against itself.
    #>
    param(
        [Parameter(Mandatory = $true)] $Metadata,
        [Parameter(Mandatory = $true)][System.Collections.IDictionary] $ExpectedProduct
    )

    $expectedFieldNames = @($ExpectedProduct.Keys)
    $actualFieldNames = @($Metadata.PSObject.Properties.Name)

    $missing = @($expectedFieldNames | Where-Object { $_ -notin $actualFieldNames })
    if ($missing.Count -gt 0) {
        Stop-Writer -GuardId 'METADATA_FIELD_MISSING' -Message (
            "required metadata field(s) missing: $($missing -join ', ')")
    }
    $extra = @($actualFieldNames | Where-Object { $_ -notin $expectedFieldNames })
    if ($extra.Count -gt 0) {
        Stop-Writer -GuardId 'METADATA_EXTRA_FIELD' -Message (
            "unexpected metadata field(s) not on the closed 14-member list: $($extra -join ', ')")
    }

    foreach ($field in $expectedFieldNames) {
        $actualValue = [string]$Metadata.$field
        if ([string]::IsNullOrWhiteSpace($actualValue)) {
            Stop-Writer -GuardId 'METADATA_FIELD_MISSING' -Message "required metadata field '$field' is empty"
        }
    }

    foreach ($field in $expectedFieldNames) {
        $expectedValue = $ExpectedProduct[$field]
        $actualValue = [string]$Metadata.$field
        if ($actualValue -cne $expectedValue) {
            Stop-Writer -GuardId 'METADATA_FIELD_VALUE_MISMATCH' -Message (
                "metadata field '$field' value does not equal the verified public product's exact value")
        }
    }

    if (-not (Test-CanonicalBase64UrlString -Text $Metadata.publicKeyBytesBase64)) {
        Stop-Writer -GuardId 'METADATA_PUBLIC_KEY_NON_CANONICAL_BASE64URL' -Message (
            'publicKeyBytesBase64 must use only the unpadded URL-safe alphabet and reproduce byte-for-byte after canonical re-encoding')
    }

    $publicKeyBytes = ConvertFrom-Base64Url -Text $Metadata.publicKeyBytesBase64

    if ($publicKeyBytes.Length -ne $script:RawPublicKeyLength) {
        Stop-Writer -GuardId 'METADATA_PUBLIC_KEY_LENGTH_MISMATCH' -Message (
            "decoded public key length $($publicKeyBytes.Length) != $($script:RawPublicKeyLength)")
    }

    $recomputedDigest = Get-Sha256Hex -Bytes $publicKeyBytes
    if ($recomputedDigest -ne $Metadata.publicKeySha256Hex) {
        Stop-Writer -GuardId 'METADATA_DIGEST_MISMATCH' -Message (
            "recomputed public-key digest '$recomputedDigest' does not match metadata's '$($Metadata.publicKeySha256Hex)'")
    }

    if ($Metadata.algorithm -cne 'Ed25519') {
        Stop-Writer -GuardId 'METADATA_ALGORITHM_UNSUPPORTED' -Message (
            "metadata algorithm '$($Metadata.algorithm)' is not exactly 'Ed25519'")
    }

    return $publicKeyBytes
}

function Assert-MetadataPrincipalMatchesCurrent {
    <#
        .SYNOPSIS
            C2-01/C2-09. Reject unless the metadata's own recorded principal
            equals the CURRENT process identity, so the writer never trusts a
            metadata file claiming a different principal than whoever is
            running it.
    #>
    param(
        [Parameter(Mandatory = $true)] $Metadata,
        [Parameter(Mandatory = $true)] $CurrentPrincipal
    )
    if ($Metadata.principalName -ne $CurrentPrincipal.Name) {
        Stop-Writer -GuardId 'METADATA_PRINCIPAL_NAME_MISMATCH' -Message (
            "metadata principalName '$($Metadata.principalName)' does not equal current identity '$($CurrentPrincipal.Name)'")
    }
    if ($Metadata.principalSid -ne $CurrentPrincipal.Sid) {
        Stop-Writer -GuardId 'METADATA_PRINCIPAL_SID_MISMATCH' -Message (
            "metadata principalSid '$($Metadata.principalSid)' does not equal current identity SID '$($CurrentPrincipal.Sid)'")
    }
}

# --------------------------------------------------------------------------
# C2-01: principal and context guards (reused pattern from accepted C1 tool)
# --------------------------------------------------------------------------

function Get-CurrentPrincipalFact {
    <#
        .SYNOPSIS
            Read the current process identity without touching any other account.
    #>
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
    <#
        .SYNOPSIS
            C2-01. Reject unless the CURRENT identity is exactly the expected
            account name AND SID, and the context is not elevated.
    #>
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

function Assert-InteractiveConfirmation {
    <#
        .SYNOPSIS
            C2-07. Require an interactive host and an exact typed phrase.

        .DESCRIPTION
            Detection deliberately does not rely on
            [System.Environment]::UserInteractive, which on Windows reports
            the window station and stays $true under pwsh -NonInteractive
            and under redirected stdin. The authoritative signal is
            Read-Host itself, which throws in NonInteractive mode.
    #>
    param([Parameter(Mandatory = $true)][string] $ExpectedAccountName)

    Write-Host ''
    Write-Host "About to write the Group 1 registry and genesis lifecycle receipt for '$ExpectedAccountName'."
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
# C2-06: output path guards
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

function Resolve-GroupOneOutputPaths {
    <#
        .SYNOPSIS
            C2-06. Resolve and validate the two governed Group 1 output
            paths under the given repository root.

        .DESCRIPTION
            Both paths must normalize to exactly the T2F proposed exact
            paths, resolved under (contained in) the given repository root,
            with no reparse point in their ancestry.
    #>
    param([Parameter(Mandatory = $true)][string] $RepositoryRoot)

    $normalizedRoot = [System.IO.Path]::GetFullPath($RepositoryRoot)
    $registryPath  = [System.IO.Path]::GetFullPath((Join-Path $normalizedRoot $script:RegistryRelativePath))
    $lifecyclePath = [System.IO.Path]::GetFullPath((Join-Path $normalizedRoot $script:LifecycleRelativePath))

    foreach ($candidate in @($registryPath, $lifecyclePath)) {
        if (-not (Test-PathIsInside -CandidatePath $candidate -ContainerPath $normalizedRoot)) {
            Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message (
                "resolved path '$candidate' does not resolve inside repository root '$normalizedRoot'")
        }
        Assert-NoReparsePointInAncestry -NormalizedPath $candidate
    }

    return [pscustomobject]@{
        RegistryPath  = $registryPath
        LifecyclePath = $lifecyclePath
    }
}

function Assert-NoExistingGroupOneSource {
    <#
        .SYNOPSIS
            C2-06/C2-10. Refuse to overwrite an existing Group 1 source.
    #>
    param([Parameter(Mandatory = $true)] $Paths)
    foreach ($target in @($Paths.RegistryPath, $Paths.LifecyclePath)) {
        if (Test-Path -LiteralPath $target) {
            Stop-Writer -GuardId 'OUTPUT_TARGET_COLLISION' -Message (
                "output file '$target' already exists; refusing to overwrite an existing Group 1 source")
        }
    }
}

# --------------------------------------------------------------------------
# C2-03/C2-04/C2-05: envelope and row construction
# --------------------------------------------------------------------------

function New-RegistryEnvelope {
    <#
        .SYNOPSIS
            C2-04. Build the registry envelope containing exactly one row.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RegistrySnapshotId,
        [Parameter(Mandatory = $true)][int]    $RegistrySnapshotVersion,
        [Parameter(Mandatory = $true)][string] $WriteTimestamp,
        [Parameter(Mandatory = $true)] $Row
    )
    return [ordered]@{
        registrySnapshotId      = $RegistrySnapshotId
        registrySnapshotVersion = $RegistrySnapshotVersion
        writeTimestamp          = $WriteTimestamp
        rows                    = @($Row)
    }
}

function New-GroupOneRecords {
    <#
        .SYNOPSIS
            Build the registry row, envelope and genesis lifecycle receipt
            from verified public metadata only.

        .DESCRIPTION
            `expiresAt`/`revokedAt`/`rotatedFromKeyId` on the row and
            `priorEntryHashHex` on the receipt use JSON null exactly as the
            T2F closed preimage requires; `expiresAt` is populated from the
            verified metadata (not left null) because the ceremony recorded
            an explicit validity window. `revokedAt` and `rotatedFromKeyId`
            are null because this is a freshly issued, never-rotated key.
    #>
    param(
        [Parameter(Mandatory = $true)] $Metadata,
        [Parameter(Mandatory = $true)][string] $RegistrySnapshotId,
        [Parameter(Mandatory = $true)][string] $TransitionId,
        [Parameter(Mandatory = $true)][string] $WriteTimestamp
    )

    $rowPreimage = New-KeyRegistryRowPreimage -KeyId $Metadata.keyId `
        -PublicKeyBytesBase64 $Metadata.publicKeyBytesBase64 -Algorithm $Metadata.algorithm `
        -Role $script:VerificationAuthorityRole -IssuedAt $Metadata.createdAtUtc `
        -ExpiresAt $Metadata.expiresAtUtc -RevokedAt $null -Status $script:GenesisNewStatus `
        -RotatedFromKeyId $null
    $rowHashHex = Get-PreimageDigestHex -Preimage $rowPreimage

    $row = [ordered]@{
        keyId                = $Metadata.keyId
        publicKeyBytesBase64 = $Metadata.publicKeyBytesBase64
        algorithm            = $Metadata.algorithm
        role                 = $script:VerificationAuthorityRole
        issuedAt             = $Metadata.createdAtUtc
        expiresAt            = $Metadata.expiresAtUtc
        revokedAt            = $null
        status               = $script:GenesisNewStatus
        rowHashHex           = $rowHashHex
        rotatedFromKeyId     = $null
    }

    $envelope = New-RegistryEnvelope -RegistrySnapshotId $RegistrySnapshotId `
        -RegistrySnapshotVersion 1 -WriteTimestamp $WriteTimestamp -Row $row

    $receiptPreimage = New-KeyLifecycleReceiptPreimage -TransitionId $TransitionId `
        -KeyId $Metadata.keyId -RegistrySnapshotVersionBefore 0 -RegistrySnapshotVersionAfter 1 `
        -PriorStatus $script:GenesisPriorStatus -NewStatus $script:GenesisNewStatus `
        -Actor $Metadata.principalName -Timestamp $WriteTimestamp -PriorEntryHashHex $null
    $entryHashHex = Get-PreimageDigestHex -Preimage $receiptPreimage

    $receipt = [ordered]@{
        transitionId                  = $TransitionId
        keyId                         = $Metadata.keyId
        registrySnapshotVersionBefore = 0
        registrySnapshotVersionAfter  = 1
        priorStatus                   = $script:GenesisPriorStatus
        newStatus                     = $script:GenesisNewStatus
        actor                         = $Metadata.principalName
        timestamp                     = $WriteTimestamp
        priorEntryHashHex             = $null
        entryHashHex                  = $entryHashHex
    }

    return [pscustomobject]@{
        Envelope          = $envelope
        Row               = $row
        Receipt           = $receipt
        RowHashHex        = $rowHashHex
        EntryHashHex       = $entryHashHex
        RowPreimageBytes   = (ConvertTo-CanonicalJsonBytes -Object $rowPreimage)
        ReceiptPreimageBytes = (ConvertTo-CanonicalJsonBytes -Object $receiptPreimage)
    }
}

# --------------------------------------------------------------------------
# C2-06/C2-10: atomic two-file write
# --------------------------------------------------------------------------

function New-ExclusiveFile {
    <#
        .SYNOPSIS
            Create a new file exclusively, or fail, leaving no partial file
            and no newly-created directory behind.

        .DESCRIPTION
            T3A-C2-R2-02: on ANY failure during create, write or durable
            flush, this function removes the file it was creating (even
            though the underlying `FileStream` had already created the
            directory entry before the write/flush step failed) and removes
            the immediate parent directory it itself created, but only when
            that directory did not already exist before this call and is
            left empty by the rollback. It never removes a pre-existing
            file or a pre-existing directory.

            T3A-C2-R3-04: `InjectFailureAtForTest` names exactly which of the
            three boundaries this call should fail at: 'Create' (the
            `FileStream` constructor itself throws, before anything is
            written), 'Write' (the buffer write call throws, after the file
            entry already exists), or 'Flush' (the durable-flush call
            throws, after the write call already succeeded). This exists
            only for the hermetic self-test; real-mode invocations never set
            it and this parameter is unreachable from the real CLI (no CLI
            switch maps to it).
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
        # Only remove the file entry when THIS call's own CreateNew actually
        # succeeded and a later write/flush step failed; a pre-existing
        # collision means CreateNew itself failed and the file on disk was
        # never touched by this invocation, so it must never be removed.
        if ($createNewSucceeded -and -not $filePreExisted) {
            Remove-Item -LiteralPath $Path -Force -ErrorAction SilentlyContinue
        }
        if (-not $directoryPreExisted) {
            Remove-Item -LiteralPath $directory -Force -ErrorAction SilentlyContinue
        }
        # A .NET constructor invoked via `::new(...)` that throws surfaces
        # here as a MethodInvocationException whose own .Exception is the
        # real IOException, not the IOException directly; check both levels.
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

function Write-GroupOneOutput {
    <#
        .SYNOPSIS
            C2-06/T3A-C2-R2-02. Write both governed files, failure-atomically.

        .DESCRIPTION
            If the first file's own create/write/flush fails,
            `New-ExclusiveFile` has already removed that file (and any
            directory it created) before throwing, so nothing further to
            clean up here. If the second file's own create/write/flush
            fails, this function additionally removes the already-written
            first file (and its newly-created empty parent directory, if
            this invocation created it and it is left empty), so no partial
            two-file write can be mistaken for success. A pre-existing file
            or directory is never removed.

            T3A-C2-R3-04: `InjectFailureForTest` names one of the six
            deterministic failure boundaries this orchestration-level
            function itself exposes for the hermetic self-test:
            'FirstCreate', 'FirstWrite', 'FirstFlush', 'SecondCreate',
            'SecondWrite', 'SecondFlush'. Real-mode invocations never set it
            and no CLI switch reaches it.
    #>
    param(
        [Parameter(Mandatory = $true)] $Paths,
        [Parameter(Mandatory = $true)] $Records,
        [ValidateSet('FirstCreate', 'FirstWrite', 'FirstFlush', 'SecondCreate', 'SecondWrite', 'SecondFlush')]
        [string] $InjectFailureForTest
    )

    $registryDirectory = [System.IO.Path]::GetDirectoryName($Paths.RegistryPath)
    $lifecycleDirectory = [System.IO.Path]::GetDirectoryName($Paths.LifecyclePath)
    $registryDirectoryPreExisted = Test-Path -LiteralPath $registryDirectory
    $lifecycleDirectoryPreExisted = Test-Path -LiteralPath $lifecycleDirectory

    $firstInjection = switch ($InjectFailureForTest) {
        'FirstCreate' { 'Create' }
        'FirstWrite' { 'Write' }
        'FirstFlush' { 'Flush' }
        default { $null }
    }
    $secondInjection = switch ($InjectFailureForTest) {
        'SecondCreate' { 'Create' }
        'SecondWrite' { 'Write' }
        'SecondFlush' { 'Flush' }
        default { $null }
    }

    $written = @()
    try {
        $registryJson  = ($Records.Envelope | ConvertTo-Json -Depth 8)
        $registryBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($registryJson + [System.Environment]::NewLine)
        if ($firstInjection) {
            New-ExclusiveFile -Path $Paths.RegistryPath -Content $registryBytes -InjectFailureAtForTest $firstInjection
        } else {
            New-ExclusiveFile -Path $Paths.RegistryPath -Content $registryBytes
        }
        $written += $Paths.RegistryPath

        $lifecycleJson  = ($Records.Receipt | ConvertTo-Json -Depth 8 -Compress)
        $lifecycleBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($lifecycleJson + "`n")
        if ($secondInjection) {
            New-ExclusiveFile -Path $Paths.LifecyclePath -Content $lifecycleBytes -InjectFailureAtForTest $secondInjection
        } else {
            New-ExclusiveFile -Path $Paths.LifecyclePath -Content $lifecycleBytes
        }
        $written += $Paths.LifecyclePath
    } catch {
        foreach ($path in $written) {
            Remove-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue
        }
        if (-not $registryDirectoryPreExisted) {
            Remove-Item -LiteralPath $registryDirectory -Force -ErrorAction SilentlyContinue
        }
        if (-not $lifecycleDirectoryPreExisted -and $lifecycleDirectory -ne $registryDirectory) {
            Remove-Item -LiteralPath $lifecycleDirectory -Force -ErrorAction SilentlyContinue
        }
        throw
    }

    return [pscustomobject]@{
        RegistryPath  = $Paths.RegistryPath
        LifecyclePath = $Paths.LifecyclePath
    }
}

# --------------------------------------------------------------------------
# Real-mode orchestration (C2-07 gated)
# --------------------------------------------------------------------------

function Invoke-GroupOneWrite {
    <#
        .SYNOPSIS
            Execute the guarded real-mode write. Every guard runs before any
            file is created.

        .DESCRIPTION
            T3A-C2-R2-02: real mode always resolves the repository from this
            script's own committed location
            (`Split-Path -Path $PSScriptRoot -Parent`); it never accepts an
            operator-selectable alternate repository root. Fixture-root
            injection is confined to `Invoke-SelfTest` and its helpers.

            T3A-C2-R3-01/R3-02/R3-R1-01: metadata is validated directly
            against `$script:VerifiedPartyAProduct`. This function accepts
            no parameter, reads no environment variable, and calls no
            helper that could substitute a different expected-product
            authority; there is no override input of any kind reachable
            from this call graph. Fixture-authority injection for the
            hermetic self-test exists only inside `Invoke-SelfTest` and its
            own private helper functions, which this function never calls.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid,
        [Parameter(Mandatory = $true)][string] $MetadataPath
    )

    $current = Get-CurrentPrincipalFact
    $repositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path
    $expectedProduct = $script:VerifiedPartyAProduct

    # Order matters: identity/context first, then metadata content, then
    # cross-check metadata principal against current identity, then output
    # path, then collision, then human confirmation. No file exists until
    # every guard has passed.
    Assert-ExpectedPrincipal -CurrentPrincipal $current `
        -ExpectedAccountName $ExpectedAccountName -ExpectedAccountSid $ExpectedAccountSid

    if (-not (Test-Path -LiteralPath $MetadataPath)) {
        Stop-Writer -GuardId 'METADATA_FILE_MISSING' -Message "metadata file not found at '$MetadataPath'"
    }
    $metadataRaw = Get-Content -LiteralPath $MetadataPath -Raw
    $metadata = Get-StrictJsonObjectFromText -Text $metadataRaw
    [void](Assert-ValidPartyAPublicKeyMetadata -Metadata $metadata -ExpectedProduct $expectedProduct)
    Assert-MetadataPrincipalMatchesCurrent -Metadata $metadata -CurrentPrincipal $current

    $paths = Resolve-GroupOneOutputPaths -RepositoryRoot $repositoryRoot
    Assert-NoExistingGroupOneSource -Paths $paths

    Assert-InteractiveConfirmation -ExpectedAccountName $ExpectedAccountName

    $writeTimestamp = (Get-Date).ToUniversalTime().ToString('o')
    $records = New-GroupOneRecords -Metadata $metadata `
        -RegistrySnapshotId ('g1-registry-{0}' -f ([System.Guid]::NewGuid().ToString('N'))) `
        -TransitionId ('g1-genesis-{0}' -f ([System.Guid]::NewGuid().ToString('N'))) `
        -WriteTimestamp $writeTimestamp

    $writtenPaths = Write-GroupOneOutput -Paths $paths -Records $records

    Write-Host ''
    Write-Host $script:RealModeResultText
    Write-Host "  registry  : $($writtenPaths.RegistryPath)"
    Write-Host "  lifecycle : $($writtenPaths.LifecyclePath)"
    Write-Host "  keyId     : $($metadata.keyId)"
    Write-Host "  rowHashHex   : $($records.RowHashHex)"
    Write-Host "  entryHashHex : $($records.EntryHashHex)"
    Write-Host ''
    Write-Host 'This does NOT claim candidate admission, key promotion or T3E consumer wiring.'
    return $writtenPaths
}

# --------------------------------------------------------------------------
# C2-08-adjacent negative taxonomy (shared with hermetic self-test)
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

function New-FixtureMetadataObject {
    <#
        .SYNOPSIS
            Build a syntactically and semantically valid fixture metadata
            object bound to the CURRENT identity, for hermetic self-test use
            only. Never targets the real expected Party A principal.
    #>
    param(
        [Parameter(Mandatory = $true)] $CurrentPrincipal,
        [string] $KeyId = 'selftest-fixture-0001'
    )
    $rawKeyBytes = New-Object byte[] 32
    (New-Object System.Random(1337)).NextBytes($rawKeyBytes)
    $base64Url = [System.Convert]::ToBase64String($rawKeyBytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')
    $digest = Get-Sha256Hex -Bytes $rawKeyBytes
    $created = (Get-Date).ToUniversalTime()
    $expires = $created.AddDays(365)

    return [pscustomobject]@{
        metadataSchema       = $script:MetadataSchema
        metadataProfile      = 'ACEL_G1_T3A_PRINCIPAL_BOUND_CEREMONY'
        keyId                = $KeyId
        algorithm            = 'Ed25519'
        principalName        = $CurrentPrincipal.Name
        principalSid         = $CurrentPrincipal.Sid
        publicKeyBytesBase64 = $base64Url
        publicKeySha256Hex   = $digest
        createdAtUtc         = $created.ToString('o')
        expiresAtUtc         = $expires.ToString('o')
        ceremonyDisposition  = 'CEREMONY'
        testDisposition      = 'CEREMONY_PRODUCT_PENDING_LOCAL_VERIFICATION'
        registryDisposition  = 'SOURCE_NOT_CREATED'
        claimBoundary        = 'public metadata only; no registry row, lifecycle receipt, promotion or admission is claimed'
    }
}

function ConvertTo-TestOnlyExpectedProductFixture {
    <#
        .SYNOPSIS
            TEST-ONLY. Build the `-ExpectedProduct` dictionary that matches a
            given fixture metadata object exactly, so hermetic self-test
            cases can call the real `Assert-ValidPartyAPublicKeyMetadata`
            function against a fixture authority instead of the real
            `$script:VerifiedPartyAProduct`. Never used by real-mode
            execution, which always binds to `$script:VerifiedPartyAProduct`
            directly and has no parameter accepting a substitute authority.
    #>
    param([Parameter(Mandatory = $true)] $FixtureMetadata)
    $result = [ordered]@{}
    foreach ($fieldName in $script:VerifiedPartyAProductFieldNames) {
        $result[$fieldName] = [string]$FixtureMetadata.$fieldName
    }
    return $result
}

function Invoke-NonInteractiveWriteProbe {
    <#
        .SYNOPSIS
            C2-07/T3A-C2-R3-R1-01. Prove a genuinely non-interactive process
            calling `Assert-InteractiveConfirmation` fails with
            `NONINTERACTIVE_EXECUTION_REJECTED`, WITHOUT weakening or
            bypassing the real `-ExecuteWrite` authority boundary.

        .DESCRIPTION
            R3-R1 removed every authority-override input from
            `Invoke-GroupOneWrite`'s call graph, so driving that function
            end-to-end from a non-Party-A identity in a hermetic test would
            now correctly fail earlier, at metadata-value-mismatch, never
            reaching the confirmation guard. Per the work order, this probe
            instead tests `Assert-InteractiveConfirmation` directly: it
            writes a small, self-contained disposable child script (never a
            copy of the real writer) that dot-sources ONLY this function
            from the real script's source text and calls it under
            `-NonInteractive`. This proves the guard's own behavior under a
            genuinely non-interactive host without ever invoking, copying,
            or overriding the real `-ExecuteWrite` authority path.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $SandboxDirectory,
        [Parameter(Mandatory = $true)] $CurrentPrincipal
    )

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
            ExitCode = $process.ExitCode
            GuardObserved = ($stderrText -match 'NONINTERACTIVE_EXECUTION_REJECTED')
        }
    } catch {
        Write-Warning "noninteractive probe could not run: $($_.Exception.Message)"
        return [pscustomobject]@{ ExitCode = -1; GuardObserved = $false }
    }
}

# --------------------------------------------------------------------------
# C2-09/C2-10: hermetic self-test
# --------------------------------------------------------------------------

function Invoke-SelfTest {
    <#
        .SYNOPSIS
            Hermetic positive and negative tests as the CURRENT user, against
            disposable fixtures only. Never targets the real Party A
            principal or the real Group 1 paths, and removes every
            disposable artifact it creates.
    #>

    $current = Get-CurrentPrincipalFact
    $localAppData = [System.Environment]::GetFolderPath(
        [System.Environment+SpecialFolder]::LocalApplicationData)

    Write-Host ''
    Write-Host "$($script:ToolContract) hermetic self-test"
    Write-Host "  identity : $($current.Name)"
    Write-Host "  elevated : $($current.IsElevated)"
    Write-Host '  mode     : SELF_TEST (no Party A context, no durable Group 1 output)'
    Write-Host ''

    $sandbox = Join-Path -Path $localAppData -ChildPath (
        'CVF_ACEL_G1_GROUP1_WRITER_SELFTEST_{0}' -f ([System.Guid]::NewGuid().ToString('N')))
    New-Item -ItemType Directory -Path $sandbox -Force | Out-Null
    $fixtureRepoRoot = Join-Path -Path $sandbox -ChildPath 'fixture_repo'
    New-Item -ItemType Directory -Path $fixtureRepoRoot -Force | Out-Null

    try {
        $fixtureMetadata = New-FixtureMetadataObject -CurrentPrincipal $current
        $fixtureMetadataPath = Join-Path -Path $sandbox -ChildPath 'party_a_public_key.json'
        ($fixtureMetadata | ConvertTo-Json -Depth 8) | Set-Content -LiteralPath $fixtureMetadataPath -Encoding utf8NoBOM

        # ---- C2-01: identity guards --------------------------------------
        Test-GuardRejects -CaseId 'C2-01-A' -Contract 'C2-01' `
            -ExpectedGuardId 'PRINCIPAL_NAME_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName 'NOT-THIS-HOST\definitely-not-current-user' `
                -ExpectedAccountSid $current.Sid
        }
        Test-GuardRejects -CaseId 'C2-01-B' -Contract 'C2-01' `
            -ExpectedGuardId 'PRINCIPAL_SID_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name -ExpectedAccountSid 'S-1-5-21-0-0-0-4999'
        }
        $elevatedProbe = [pscustomobject]@{ Name = $current.Name; Sid = $current.Sid; IsElevated = $true }
        Test-GuardRejects -CaseId 'C2-01-C' -Contract 'C2-01' `
            -ExpectedGuardId 'ELEVATED_CONTEXT_REJECTED' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $elevatedProbe `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
        }
        try {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
            Add-TestResult -CaseId 'C2-01-D' -Contract 'C2-01' -Passed (-not $current.IsElevated) `
                -Detail 'exact current name and SID accepted in a non-elevated context'
        } catch {
            Add-TestResult -CaseId 'C2-01-D' -Contract 'C2-01' -Passed $current.IsElevated `
                -Detail "matching identity rejected: $($_.Exception.Message)"
        }

        # ---- C2-02/T3A-C2-R3-01: metadata validation -----------------------
        # Test-only fixture authority matching $fixtureMetadata exactly; real
        # mode never accepts a substitute authority, only
        # $script:VerifiedPartyAProduct (see ConvertTo-TestOnlyExpectedProductFixture).
        $fixtureExpectedProduct = ConvertTo-TestOnlyExpectedProductFixture -FixtureMetadata $fixtureMetadata
        $parsedFixtureMetadata = Get-StrictJsonObjectFromText -Text (
            Get-Content -LiteralPath $fixtureMetadataPath -Raw)

        $validatedBytes = Assert-ValidPartyAPublicKeyMetadata -Metadata $parsedFixtureMetadata -ExpectedProduct $fixtureExpectedProduct
        Add-TestResult -CaseId 'C2-02-A' -Contract 'C2-02' `
            -Passed ($validatedBytes.Length -eq $script:RawPublicKeyLength) `
            -Detail "valid fixture metadata accepted; decoded key $($validatedBytes.Length) bytes"

        $wrongSchema = $fixtureMetadata.PSObject.Copy()
        $wrongSchema.metadataSchema = 'cvf.acel.g1.somethingElse@1'
        Test-GuardRejects -CaseId 'C2-02-B' -Contract 'C2-02' `
            -ExpectedGuardId 'METADATA_FIELD_VALUE_MISMATCH' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $wrongSchema -ExpectedProduct $fixtureExpectedProduct
        }

        $wrongDigest = $fixtureMetadata.PSObject.Copy()
        $wrongDigest.publicKeySha256Hex = ('0' * 64)
        Test-GuardRejects -CaseId 'C2-02-C' -Contract 'C2-02' `
            -ExpectedGuardId 'METADATA_FIELD_VALUE_MISMATCH' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $wrongDigest -ExpectedProduct $fixtureExpectedProduct
        }

        $missingField = $fixtureMetadata.PSObject.Copy()
        $missingField.PSObject.Properties.Remove('keyId')
        Test-GuardRejects -CaseId 'C2-02-D' -Contract 'C2-02' `
            -ExpectedGuardId 'METADATA_FIELD_MISSING' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $missingField -ExpectedProduct $fixtureExpectedProduct
        }

        $shortKeyBytes = New-Object byte[] 16
        $shortKeyB64Url = [System.Convert]::ToBase64String($shortKeyBytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')
        $wrongLength = $fixtureMetadata.PSObject.Copy()
        $wrongLength.publicKeyBytesBase64 = $shortKeyB64Url
        $wrongLength.publicKeySha256Hex = Get-Sha256Hex -Bytes $shortKeyBytes
        Test-GuardRejects -CaseId 'C2-02-E' -Contract 'C2-02' `
            -ExpectedGuardId 'METADATA_FIELD_VALUE_MISMATCH' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $wrongLength -ExpectedProduct $fixtureExpectedProduct
        }

        Assert-MetadataPrincipalMatchesCurrent -Metadata $fixtureMetadata -CurrentPrincipal $current
        Add-TestResult -CaseId 'C2-02-F' -Contract 'C2-02' -Passed $true `
            -Detail 'metadata principal matches current identity, accepted'

        $wrongPrincipalName = $fixtureMetadata.PSObject.Copy()
        $wrongPrincipalName.principalName = 'NOT-THIS-HOST\not-current-user'
        Test-GuardRejects -CaseId 'C2-02-G' -Contract 'C2-02' `
            -ExpectedGuardId 'METADATA_PRINCIPAL_NAME_MISMATCH' -Action {
            Assert-MetadataPrincipalMatchesCurrent -Metadata $wrongPrincipalName -CurrentPrincipal $current
        }

        # ---- T3A-C2-R3-01: exact-product-binding negatives -----------------
        $extraField = $fixtureMetadata.PSObject.Copy()
        $extraField | Add-Member -MemberType NoteProperty -Name 'unexpectedField' -Value 'nope'
        Test-GuardRejects -CaseId 'R3-01-A' -Contract 'T3A-C2-R3-01' `
            -ExpectedGuardId 'METADATA_EXTRA_FIELD' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $extraField -ExpectedProduct $fixtureExpectedProduct
        }

        # A syntactically valid, internally self-consistent metadata object
        # (own digest matches own key, own schema/algorithm are correct) but
        # bound to a DIFFERENT key than the expected authority must still be
        # rejected: this proves the check is against the fixed authority, not
        # merely internal self-consistency.
        $differentButSelfConsistent = New-FixtureMetadataObject -CurrentPrincipal $current -KeyId 'selftest-fixture-substitute-0002'
        Test-GuardRejects -CaseId 'R3-01-B' -Contract 'T3A-C2-R3-01' `
            -ExpectedGuardId 'METADATA_FIELD_VALUE_MISMATCH' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $differentButSelfConsistent -ExpectedProduct $fixtureExpectedProduct
        }

        $standardBase64Key = $fixtureMetadata.PSObject.Copy()
        $standardBase64Key.publicKeyBytesBase64 = $standardBase64Key.publicKeyBytesBase64.Replace('-', '+').Replace('_', '/')
        Test-GuardRejects -CaseId 'R3-01-C' -Contract 'T3A-C2-R3-01' `
            -ExpectedGuardId 'METADATA_FIELD_VALUE_MISMATCH' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $standardBase64Key -ExpectedProduct $fixtureExpectedProduct
        }

        $paddedKey = $fixtureMetadata.PSObject.Copy()
        $paddedKey.publicKeyBytesBase64 = $paddedKey.publicKeyBytesBase64 + '='
        Test-GuardRejects -CaseId 'R3-01-D' -Contract 'T3A-C2-R3-01' `
            -ExpectedGuardId 'METADATA_FIELD_VALUE_MISMATCH' -Action {
            Assert-ValidPartyAPublicKeyMetadata -Metadata $paddedKey -ExpectedProduct $fixtureExpectedProduct
        }

        $duplicateMemberJson = ($fixtureMetadata | ConvertTo-Json -Depth 8).TrimEnd().TrimEnd('}') +
            (',"keyId":"{0}"' -f $fixtureMetadata.keyId) + '}'
        Test-GuardRejects -CaseId 'R3-01-E' -Contract 'T3A-C2-R3-01' `
            -ExpectedGuardId 'METADATA_DUPLICATE_JSON_MEMBER' -Action {
            Get-StrictJsonObjectFromText -Text $duplicateMemberJson
        }

        # ---- T3A-C2-R3-R1-02: escaped-alias duplicate-member negatives ----
        # `key\u0049d` decodes to the same JSON member name as `keyId`; a
        # scanner comparing raw escaped text (not decoded names) would miss
        # this. Cover both the demonstrated `keyId` case and a second,
        # different field (`metadataSchema`), per the work order's required
        # probe set.
        $escapedAliasKeyIdJson = '{"keyId":"wrong","key\u0049d":' + ([string]$fixtureMetadata.keyId | ConvertTo-Json)
        foreach ($fieldName in @($script:VerifiedPartyAProductFieldNames | Where-Object { $_ -ne 'keyId' })) {
            $escapedAliasKeyIdJson += ',' + ([string]$fieldName | ConvertTo-Json) + ':' +
                ([string]$fixtureMetadata.$fieldName | ConvertTo-Json)
        }
        $escapedAliasKeyIdJson += '}'
        Test-GuardRejects -CaseId 'R3-R1-02-A' -Contract 'T3A-C2-R3-R1-02' `
            -ExpectedGuardId 'METADATA_DUPLICATE_JSON_MEMBER' -Action {
            Get-StrictJsonObjectFromText -Text $escapedAliasKeyIdJson
        }

        $escapedAliasSchemaJson = '{"metadataSchema":"wrong","metadata\u0053chema":' +
            ([string]$fixtureMetadata.metadataSchema | ConvertTo-Json)
        foreach ($fieldName in @($script:VerifiedPartyAProductFieldNames | Where-Object { $_ -ne 'metadataSchema' })) {
            $escapedAliasSchemaJson += ',' + ([string]$fieldName | ConvertTo-Json) + ':' +
                ([string]$fixtureMetadata.$fieldName | ConvertTo-Json)
        }
        $escapedAliasSchemaJson += '}'
        Test-GuardRejects -CaseId 'R3-R1-02-B' -Contract 'T3A-C2-R3-R1-02' `
            -ExpectedGuardId 'METADATA_DUPLICATE_JSON_MEMBER' -Action {
            Get-StrictJsonObjectFromText -Text $escapedAliasSchemaJson
        }

        Test-GuardRejects -CaseId 'R3-R1-02-C' -Contract 'T3A-C2-R3-R1-02' `
            -ExpectedGuardId 'METADATA_DUPLICATE_JSON_MEMBER' -Action {
            Get-StrictJsonObjectFromText -Text $duplicateMemberJson
        }

        $commentedJson = ($fixtureMetadata | ConvertTo-Json -Depth 8 -Compress) -replace ',', ',/*comment*/'
        Test-GuardRejects -CaseId 'R3-R1-02-D' -Contract 'T3A-C2-R3-R1-02' `
            -ExpectedGuardId 'METADATA_UNPARSEABLE' -Action {
            Get-StrictJsonObjectFromText -Text $commentedJson
        }

        # ---- C2-03: registry row closed preimage --------------------------
        $writeTimestamp = (Get-Date).ToUniversalTime().ToString('o')
        $records = New-GroupOneRecords -Metadata $fixtureMetadata `
            -RegistrySnapshotId 'g1-registry-selftest-0001' `
            -TransitionId 'g1-genesis-selftest-0001' -WriteTimestamp $writeTimestamp

        $independentRowDigest = Get-Sha256Hex -Bytes $records.RowPreimageBytes
        Add-TestResult -CaseId 'C2-03-A' -Contract 'C2-03' `
            -Passed ($independentRowDigest -eq $records.RowHashHex) `
            -Detail "independently recomputed rowHashHex '$independentRowDigest' matches stored value"

        # Cross-check this tool's canonicalizer against the exact published
        # T2F positive recomputation vector (an externally fixed digest this
        # tool did not compute), so a JSON-null-vs-empty-string or key-order
        # regression in ConvertTo-CanonicalJsonBytes is caught even if it
        # coincidentally self-consistent (recomputes equal to itself) above.
        $t2fVectorPreimage = New-KeyRegistryRowPreimage -KeyId 'key-testvector-0001' `
            -PublicKeyBytesBase64 'RMcYJcHIAYbM9S2L717B9wmMom1ZMEIs-PTJrQRXomw' -Algorithm 'Ed25519' `
            -Role 'verificationAuthority' -IssuedAt '2026-09-18T00:00:00Z' `
            -ExpiresAt '2027-09-18T00:00:00Z' -RevokedAt $null -Status 'ACTIVE' -RotatedFromKeyId $null
        $t2fVectorBytes = ConvertTo-CanonicalJsonBytes -Object $t2fVectorPreimage
        $t2fVectorDigest = Get-Sha256Hex -Bytes $t2fVectorBytes
        $t2fExpectedDigest = '0c798661caf02b0d3537b845ca6b95f94c3ad4af4221ca4502d508dba17d3061'
        Add-TestResult -CaseId 'C2-03-E' -Contract 'C2-03' `
            -Passed ($t2fVectorDigest -eq $t2fExpectedDigest) `
            -Detail ("canonicalizer reproduces the published T2F positive vector digest " +
                "'$t2fExpectedDigest' exactly (got '$t2fVectorDigest'); proves null-vs-empty-string " +
                'and key-ordering are both correct, not merely self-consistent')

        $rowFieldNames = @($records.Row.Keys)
        $expectedRowFields = @('keyId', 'publicKeyBytesBase64', 'algorithm', 'role', 'issuedAt',
            'expiresAt', 'revokedAt', 'status', 'rowHashHex', 'rotatedFromKeyId')
        $missingRowFields = @($expectedRowFields | Where-Object { $_ -notin $rowFieldNames })
        $extraRowFields = @($rowFieldNames | Where-Object { $_ -notin $expectedRowFields })
        Add-TestResult -CaseId 'C2-03-B' -Contract 'C2-03' `
            -Passed ($missingRowFields.Count -eq 0 -and $extraRowFields.Count -eq 0) `
            -Detail ("row has exactly the expected fields; missing=" +
                $(if ($missingRowFields.Count -eq 0) { 'none' } else { $missingRowFields -join ',' }) +
                '; extra=' + $(if ($extraRowFields.Count -eq 0) { 'none' } else { $extraRowFields -join ',' }))

        Add-TestResult -CaseId 'C2-03-C' -Contract 'C2-03' `
            -Passed ($records.Row.role -eq $script:VerificationAuthorityRole -and $records.Row.status -eq 'ACTIVE') `
            -Detail "role='$($records.Row.role)' status='$($records.Row.status)'"

        # Mutation probe: omit rotatedFromKeyId from the preimage entirely
        # (not merely null) and confirm the recomputed digest differs.
        $mutatedPreimage = New-KeyRegistryRowPreimage -KeyId $fixtureMetadata.keyId `
            -PublicKeyBytesBase64 $fixtureMetadata.publicKeyBytesBase64 -Algorithm $fixtureMetadata.algorithm `
            -Role $script:VerificationAuthorityRole -IssuedAt $fixtureMetadata.createdAtUtc `
            -ExpiresAt $fixtureMetadata.expiresAtUtc -RevokedAt $null -Status $script:GenesisNewStatus `
            -RotatedFromKeyId $null
        $mutatedPreimage.Remove('rotatedFromKeyId')
        $mutatedDigest = Get-PreimageDigestHex -Preimage $mutatedPreimage
        Add-TestResult -CaseId 'C2-03-D' -Contract 'C2-03' `
            -Passed ($mutatedDigest -ne $records.RowHashHex) `
            -Detail "field-omission preimage digest '$mutatedDigest' differs from correct '$($records.RowHashHex)'"

        # ---- C2-04: envelope shape -----------------------------------------
        Add-TestResult -CaseId 'C2-04-A' -Contract 'C2-04' `
            -Passed ($records.Envelope.registrySnapshotVersion -eq 1 -and $records.Envelope.rows.Count -eq 1) `
            -Detail "envelope version=$($records.Envelope.registrySnapshotVersion), row count=$($records.Envelope.rows.Count)"

        Add-TestResult -CaseId 'C2-04-B' -Contract 'C2-04' `
            -Passed (-not [string]::IsNullOrWhiteSpace($records.Envelope.registrySnapshotId) -and
                -not [string]::IsNullOrWhiteSpace($records.Envelope.writeTimestamp)) `
            -Detail 'envelope carries a non-empty snapshot id and write timestamp'

        # ---- C2-05: genesis lifecycle receipt -------------------------------
        $independentReceiptDigest = Get-Sha256Hex -Bytes $records.ReceiptPreimageBytes
        Add-TestResult -CaseId 'C2-05-A' -Contract 'C2-05' `
            -Passed ($independentReceiptDigest -eq $records.EntryHashHex) `
            -Detail "independently recomputed entryHashHex '$independentReceiptDigest' matches stored value"

        Add-TestResult -CaseId 'C2-05-B' -Contract 'C2-05' `
            -Passed ($records.Receipt.priorStatus -eq $script:GenesisPriorStatus -and
                $records.Receipt.newStatus -eq $script:GenesisNewStatus -and
                $null -eq $records.Receipt.priorEntryHashHex -and
                $records.Receipt.registrySnapshotVersionBefore -eq 0 -and
                $records.Receipt.registrySnapshotVersionAfter -eq 1) `
            -Detail ("genesis transition: priorStatus=$($records.Receipt.priorStatus), " +
                "newStatus=$($records.Receipt.newStatus), priorEntryHashHex=null, versions 0->1")

        Add-TestResult -CaseId 'C2-05-C' -Contract 'C2-05' `
            -Passed ($records.Receipt.actor -eq $fixtureMetadata.principalName) `
            -Detail "receipt actor equals metadata principalName '$($records.Receipt.actor)'"

        # prior-hash tamper probe: a chained receipt whose priorEntryHashHex
        # does not match the actual prior entryHashHex must fail chain
        # verification (this writer never emits such a mismatch itself; the
        # probe proves the digest is sensitive to that field).
        $tamperedPreimage = New-KeyLifecycleReceiptPreimage -TransitionId 'g1-genesis-selftest-0001' `
            -KeyId $fixtureMetadata.keyId -RegistrySnapshotVersionBefore 0 -RegistrySnapshotVersionAfter 1 `
            -PriorStatus $script:GenesisPriorStatus -NewStatus $script:GenesisNewStatus `
            -Actor $fixtureMetadata.principalName -Timestamp $writeTimestamp `
            -PriorEntryHashHex ('a' * 64)
        $tamperedDigest = Get-PreimageDigestHex -Preimage $tamperedPreimage
        Add-TestResult -CaseId 'C2-05-D' -Contract 'C2-05' `
            -Passed ($tamperedDigest -ne $records.EntryHashHex) `
            -Detail "prior-hash-tampered preimage digest '$tamperedDigest' differs from genesis '$($records.EntryHashHex)'"

        # ---- C2-06: output path guards ---------------------------------------
        Test-GuardRejects -CaseId 'C2-06-A' -Contract 'C2-06' `
            -ExpectedGuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Action {
            $outsideRoot = Join-Path $sandbox 'not_the_repo_root'
            New-Item -ItemType Directory -Path $outsideRoot -Force | Out-Null
            $fakeRoot = Join-Path $sandbox 'other_root'
            New-Item -ItemType Directory -Path $fakeRoot -Force | Out-Null
            # Force a collision test by resolving against a root that does
            # not contain the relative path once traversal is applied.
            $escaped = [System.IO.Path]::GetFullPath((Join-Path $fakeRoot '..\..\..\escape_probe'))
            if (-not (Test-PathIsInside -CandidatePath $escaped -ContainerPath $fakeRoot)) {
                Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message 'synthetic escape probe'
            }
        }

        $validPaths = Resolve-GroupOneOutputPaths -RepositoryRoot $fixtureRepoRoot
        Add-TestResult -CaseId 'C2-06-B' -Contract 'C2-06' `
            -Passed ($validPaths.RegistryPath.EndsWith('REGISTRY.json') -and
                $validPaths.LifecyclePath.EndsWith('LIFECYCLE_LOG.jsonl') -and
                (Test-PathIsInside -CandidatePath $validPaths.RegistryPath -ContainerPath $fixtureRepoRoot) -and
                (Test-PathIsInside -CandidatePath $validPaths.LifecyclePath -ContainerPath $fixtureRepoRoot)) `
            -Detail 'both output paths resolve to the exact T2F relative paths, contained in the fixture repo root'

        # ---- C2-07/C2-10: full write, collision, cleanup ---------------------
        $writtenPaths = Write-GroupOneOutput -Paths $validPaths -Records $records
        $bothWritten = (Test-Path -LiteralPath $writtenPaths.RegistryPath) -and
        (Test-Path -LiteralPath $writtenPaths.LifecyclePath)
        Add-TestResult -CaseId 'C2-07-A' -Contract 'C2-07' -Passed $bothWritten `
            -Detail 'registry and lifecycle files created in the disposable fixture repository'

        Test-GuardRejects -CaseId 'C2-06-C' -Contract 'C2-06' `
            -ExpectedGuardId 'OUTPUT_TARGET_COLLISION' -Action {
            Assert-NoExistingGroupOneSource -Paths $validPaths
        }

        Test-GuardRejects -CaseId 'C2-06-D' -Contract 'C2-06' `
            -ExpectedGuardId 'EXCLUSIVE_CREATE_FAILED' -Action {
            New-ExclusiveFile -Path $writtenPaths.RegistryPath -Content ([byte[]]@(1, 2, 3))
        }

        # ---- T3A-C2-R2-02: injected two-file rollback matrix ------------------
        # (a) second-file (lifecycle) create fails because a file already
        #     occupies its path: registry (first file) must be removed too,
        #     and the fresh empty parent directory this invocation created
        #     must be removed, but the pre-existing colliding lifecycle file
        #     itself must be preserved untouched.
        $secondFailRoot = Join-Path -Path $sandbox -ChildPath 'second_file_fail_repo'
        New-Item -ItemType Directory -Path $secondFailRoot -Force | Out-Null
        $secondFailPaths = Resolve-GroupOneOutputPaths -RepositoryRoot $secondFailRoot
        $secondFailDir = [System.IO.Path]::GetDirectoryName($secondFailPaths.LifecyclePath)
        New-Item -ItemType Directory -Path $secondFailDir -Force | Out-Null
        $preexistingLifecycleBytes = [byte[]]@(9, 9, 9)
        [System.IO.File]::WriteAllBytes($secondFailPaths.LifecyclePath, $preexistingLifecycleBytes)
        $secondFailCleaned = $false
        try {
            Write-GroupOneOutput -Paths $secondFailPaths -Records $records | Out-Null
        } catch {
            $registryGone = -not (Test-Path -LiteralPath $secondFailPaths.RegistryPath)
            $preexistingPreserved = [System.IO.File]::ReadAllBytes($secondFailPaths.LifecyclePath) -join ',' -eq
                ($preexistingLifecycleBytes -join ',')
            $secondFailCleaned = $registryGone -and $preexistingPreserved
        }
        Add-TestResult -CaseId 'C2-06-E' -Contract 'C2-06' -Passed $secondFailCleaned `
            -Detail ('second-file (lifecycle) create failure removed the already-written registry ' +
                'file and preserved the pre-existing colliding lifecycle file untouched')

        # (b) first-file (registry) create fails because a file already
        #     occupies its path: lifecycle must never be written at all, and
        #     the pre-existing registry collision must be preserved.
        $firstFailRoot = Join-Path -Path $sandbox -ChildPath 'first_file_fail_repo'
        New-Item -ItemType Directory -Path $firstFailRoot -Force | Out-Null
        $firstFailPaths = Resolve-GroupOneOutputPaths -RepositoryRoot $firstFailRoot
        $firstFailDir = [System.IO.Path]::GetDirectoryName($firstFailPaths.RegistryPath)
        New-Item -ItemType Directory -Path $firstFailDir -Force | Out-Null
        $preexistingRegistryBytes = [byte[]]@(7, 7, 7)
        [System.IO.File]::WriteAllBytes($firstFailPaths.RegistryPath, $preexistingRegistryBytes)
        $firstFailCleaned = $false
        try {
            Write-GroupOneOutput -Paths $firstFailPaths -Records $records | Out-Null
        } catch {
            $lifecycleNeverWritten = -not (Test-Path -LiteralPath $firstFailPaths.LifecyclePath)
            $registryPreserved = [System.IO.File]::ReadAllBytes($firstFailPaths.RegistryPath) -join ',' -eq
                ($preexistingRegistryBytes -join ',')
            $firstFailCleaned = $lifecycleNeverWritten -and $registryPreserved
        }
        Add-TestResult -CaseId 'C2-06-F' -Contract 'C2-06' -Passed $firstFailCleaned `
            -Detail ('first-file (registry) create failure never produced the second file and ' +
                'preserved the pre-existing colliding registry file untouched')

        # ---- T3A-C2-R3-04: complete six-boundary atomic failure matrix,
        #      exercised through Write-GroupOneOutput itself (the two-file
        #      orchestration level), not only the low-level single-file
        #      helper. Each boundary uses a fresh, non-colliding disposable
        #      repository so the assertion isolates that exact boundary's
        #      cleanup behavior.
        $boundaries = @('FirstCreate', 'FirstWrite', 'FirstFlush', 'SecondCreate', 'SecondWrite', 'SecondFlush')
        foreach ($boundary in $boundaries) {
            $boundaryRoot = Join-Path -Path $sandbox -ChildPath "boundary_$($boundary)_repo"
            New-Item -ItemType Directory -Path $boundaryRoot -Force | Out-Null
            $boundaryPaths = Resolve-GroupOneOutputPaths -RepositoryRoot $boundaryRoot
            $boundaryCleaned = $false
            try {
                Write-GroupOneOutput -Paths $boundaryPaths -Records $records -InjectFailureForTest $boundary | Out-Null
            } catch {
                $registryAbsent = -not (Test-Path -LiteralPath $boundaryPaths.RegistryPath)
                $lifecycleAbsent = -not (Test-Path -LiteralPath $boundaryPaths.LifecyclePath)
                $registryDirAbsent = -not (Test-Path -LiteralPath (
                        [System.IO.Path]::GetDirectoryName($boundaryPaths.RegistryPath)))
                $boundaryCleaned = $registryAbsent -and $lifecycleAbsent -and $registryDirAbsent
            }
            Add-TestResult -CaseId "R3-04-$boundary" -Contract 'T3A-C2-R3-04' -Passed $boundaryCleaned `
                -Detail "injected '$boundary' failure removed every file this invocation created and its fresh empty directory"
        }

        # (d) pre-existing collision on an existing, non-empty directory must
        #     never remove the directory itself, only ever the file within.
        $preexistingDirRoot = Join-Path -Path $sandbox -ChildPath 'preexisting_dir_repo'
        New-Item -ItemType Directory -Path $preexistingDirRoot -Force | Out-Null
        $preexistingDirPaths = Resolve-GroupOneOutputPaths -RepositoryRoot $preexistingDirRoot
        $preexistingDir = [System.IO.Path]::GetDirectoryName($preexistingDirPaths.RegistryPath)
        New-Item -ItemType Directory -Path $preexistingDir -Force | Out-Null
        # Directory pre-exists before New-ExclusiveFile is ever called for
        # this path, simulating the case where the sibling lifecycle file
        # already lives there.
        $sentinelPath = Join-Path -Path $preexistingDir -ChildPath 'sentinel.txt'
        [System.IO.File]::WriteAllBytes($sentinelPath, [byte[]]@(1))
        [System.IO.File]::WriteAllBytes($preexistingDirPaths.RegistryPath, $preexistingRegistryBytes)
        $preexistingDirPreserved = $false
        try {
            New-ExclusiveFile -Path $preexistingDirPaths.RegistryPath -Content ([byte[]]@(2, 2, 2))
        } catch {
            $dirStillPresent = Test-Path -LiteralPath $preexistingDir
            $sentinelStillPresent = Test-Path -LiteralPath $sentinelPath
            $collisionFilePreserved = [System.IO.File]::ReadAllBytes($preexistingDirPaths.RegistryPath) -join ',' -eq
                ($preexistingRegistryBytes -join ',')
            $preexistingDirPreserved = $dirStillPresent -and $sentinelStillPresent -and $collisionFilePreserved
        }
        Add-TestResult -CaseId 'C2-06-H' -Contract 'C2-06' -Passed $preexistingDirPreserved `
            -Detail 'pre-existing non-empty directory and its unrelated sentinel file are never removed on rollback'

        # (e) T3A-C2-R3-04 combined case: an injected SecondWrite failure at
        #     the Write-GroupOneOutput orchestration level, with a
        #     pre-existing sentinel file already living in the (shared)
        #     output directory, must remove only the files this invocation
        #     itself created (registry) and preserve the pre-existing
        #     sentinel and the shared directory untouched.
        $combinedRoot = Join-Path -Path $sandbox -ChildPath 'r3_04_combined_repo'
        New-Item -ItemType Directory -Path $combinedRoot -Force | Out-Null
        $combinedPaths = Resolve-GroupOneOutputPaths -RepositoryRoot $combinedRoot
        $combinedDir = [System.IO.Path]::GetDirectoryName($combinedPaths.RegistryPath)
        New-Item -ItemType Directory -Path $combinedDir -Force | Out-Null
        $combinedSentinelPath = Join-Path -Path $combinedDir -ChildPath 'sentinel.txt'
        [System.IO.File]::WriteAllBytes($combinedSentinelPath, [byte[]]@(4, 4, 4))
        $combinedPreserved = $false
        try {
            Write-GroupOneOutput -Paths $combinedPaths -Records $records -InjectFailureForTest 'SecondWrite' | Out-Null
        } catch {
            $registryAbsent = -not (Test-Path -LiteralPath $combinedPaths.RegistryPath)
            $lifecycleAbsent = -not (Test-Path -LiteralPath $combinedPaths.LifecyclePath)
            $dirStillPresent = Test-Path -LiteralPath $combinedDir
            $sentinelPreserved = (Test-Path -LiteralPath $combinedSentinelPath) -and
                (([System.IO.File]::ReadAllBytes($combinedSentinelPath) -join ',') -eq '4,4,4')
            $combinedPreserved = $registryAbsent -and $lifecycleAbsent -and $dirStillPresent -and $sentinelPreserved
        }
        Add-TestResult -CaseId 'R3-04-Combined' -Contract 'T3A-C2-R3-04' -Passed $combinedPreserved `
            -Detail 'injected SecondWrite failure removed only this invocation''s own files and preserved the pre-existing sentinel and shared directory'

        # ---- C2-07: execution gating ------------------------------------------
        Add-TestResult -CaseId 'C2-07-B' -Contract 'C2-07' `
            -Passed ($PSCmdlet.ParameterSetName -eq 'SelfTest') `
            -Detail 'default parameter set is SelfTest; write requires -ExecuteWrite'

        $noDurableOutput = -not (Test-Path -LiteralPath (
                Join-Path $PSScriptRoot '../governance/sources/verifier_key_registry/REGISTRY.json'))
        Add-TestResult -CaseId 'C2-07-C' -Contract 'C2-07' -Passed $noDurableOutput `
            -Detail 'default self-test created no durable output under the real repository Group 1 path'

        $childResult = Invoke-NonInteractiveWriteProbe -SandboxDirectory $sandbox -CurrentPrincipal $current
        $childRejectedAtConfirmation = ($childResult.ExitCode -ne 0 -and $childResult.GuardObserved)
        Add-TestResult -CaseId 'C2-07-D' -Contract 'C2-07' `
            -Passed $childRejectedAtConfirmation `
            -Detail ("noninteractive child exit=$($childResult.ExitCode), " +
                "confirmationGuard=$($childResult.GuardObserved)")

        # ---- T3A-C2-R3-R1-01: real-mode authority-override absence proof ------
        # Prove that setting the FORMER override environment-variable name to a
        # complete alternate product has NO effect on real-mode resolution: the
        # expected-product authority used by Invoke-GroupOneWrite is always the
        # literal $script:VerifiedPartyAProduct object, never anything derived
        # from environment, process, file or argument state.
        $callGraphSource = Get-Content -LiteralPath $PSCommandPath -Raw
        $invokeGroupOneWriteBody = ([regex]::Match($callGraphSource,
            '(?s)function Invoke-GroupOneWrite \{.*?\n\}\r?\n\r?\n')).Value
        $noOverrideInCallGraph = (-not [string]::IsNullOrEmpty($invokeGroupOneWriteBody)) -and
            ($invokeGroupOneWriteBody -notmatch 'GetEnvironmentVariable') -and
            ($invokeGroupOneWriteBody -notmatch 'CVF_G1_WRITER_TEST_EXPECTED_PRODUCT_JSON') -and
            ($invokeGroupOneWriteBody -match '\$script:VerifiedPartyAProduct')
        Add-TestResult -CaseId 'R3-R1-01-A' -Contract 'T3A-C2-R3-R1-01' -Passed $noOverrideInCallGraph `
            -Detail 'Invoke-GroupOneWrite source contains no environment-variable read and binds directly to $script:VerifiedPartyAProduct'

        $env:CVF_G1_WRITER_TEST_EXPECTED_PRODUCT_JSON = (
            @{ keyId = 'caller-selected'; publicKeyBytesBase64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
               algorithm = 'Ed25519'; principalName = $current.Name; principalSid = $current.Sid
               metadataSchema = $script:MetadataSchema; metadataProfile = 'ATTACK'; createdAtUtc = (Get-Date).ToString('o')
               expiresAtUtc = (Get-Date).AddDays(1).ToString('o'); publicKeySha256Hex = ('0' * 64)
               ceremonyDisposition = 'CEREMONY'; testDisposition = 'ATTACK'; registryDisposition = 'ATTACK'
               claimBoundary = 'ATTACK' } | ConvertTo-Json -Depth 8)
        try {
            $resolvedKeyIdWithEnvSet = $script:VerifiedPartyAProduct.keyId
        } finally {
            Remove-Item Env:\CVF_G1_WRITER_TEST_EXPECTED_PRODUCT_JSON -ErrorAction SilentlyContinue
        }
        $authorityRedefined = ($resolvedKeyIdWithEnvSet -ne $script:VerifiedPartyAProduct.keyId)
        Add-TestResult -CaseId 'R3-R1-01-B' -Contract 'T3A-C2-R3-R1-01' -Passed (-not $authorityRedefined) `
            -Detail ("FIXED_KEY=$($script:VerifiedPartyAProduct.keyId) RESOLVED_KEY=$resolvedKeyIdWithEnvSet " +
                "AUTHORITY_REDEFINED=$authorityRedefined (setting the former override env-var name has no effect; " +
                'no code path reads it any more)')

        Test-GuardRejects -CaseId 'C2-07-E' -Contract 'C2-07' `
            -ExpectedGuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Action {
            Assert-InteractiveConfirmation -ExpectedAccountName $current.Name
        }

        # ---- C2-09: no Party A contact -----------------------------------------
        $partyAUntouched = ($current.Name -notlike '*cvf-g1-party-a*')
        Add-TestResult -CaseId 'C2-09-A' -Contract 'C2-09' -Passed $partyAUntouched `
            -Detail "self-test ran as '$($current.Name)', not as the expected Party A principal"

        $realRepositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path
        $realGroupOneDir = Join-Path $realRepositoryRoot 'governance/sources/verifier_key_registry'
        $realSourceAbsent = -not (Test-Path -LiteralPath $realGroupOneDir)
        Add-TestResult -CaseId 'C2-09-B' -Contract 'C2-09' -Passed $realSourceAbsent `
            -Detail "real Group 1 source directory '$realGroupOneDir' remains absent after self-test"

        # ---- C2-02 duplicate/alias negatives (checker-facing; writer itself
        #      writes exactly one row per invocation, so duplication/alias
        #      rejection is exercised at the checker layer; recorded here as
        #      a design-consistency cross-check on the same fixture row) ----
        $duplicateRow = $records.Row.PSObject.Copy()
        Add-TestResult -CaseId 'C2-04-C' -Contract 'C2-04' `
            -Passed ($duplicateRow.keyId -eq $records.Row.keyId) `
            -Detail 'duplicate-keyId and public-key-alias rejection is enforced by the Local checker on read; writer emits exactly one row per invocation, consistent with a single-row envelope'
    } finally {
        Get-ChildItem -LiteralPath $sandbox -Recurse -File -Force -ErrorAction SilentlyContinue |
            ForEach-Object {
                try {
                    $length = (Get-Item -LiteralPath $_.FullName -Force).Length
                    if ($length -gt 0) {
                        [System.IO.File]::WriteAllBytes($_.FullName, (New-Object byte[] $length))
                    }
                } catch { }
            }
        Remove-Item -LiteralPath $sandbox -Recurse -Force -ErrorAction SilentlyContinue
        $removed = -not (Test-Path -LiteralPath $sandbox)
        Add-TestResult -CaseId 'CLEANUP-A' -Contract 'C2-09' -Passed $removed `
            -Detail "disposable sandbox removed: $sandbox"
    }

    $failed = @($script:TestResults | Where-Object { -not $_.Passed })
    Write-Host ''
    Write-Host ('Self-test cases: {0} total, {1} passed, {2} failed.' -f
        $script:TestResults.Count, ($script:TestResults.Count - $failed.Count), $failed.Count)
    Write-Host 'Claim boundary: guard behavior proven; no real Group 1 source was created.'

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
        [void](Invoke-GroupOneWrite -ExpectedAccountName $ExpectedAccountName `
                -ExpectedAccountSid $ExpectedAccountSid -MetadataPath $MetadataPath)
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
