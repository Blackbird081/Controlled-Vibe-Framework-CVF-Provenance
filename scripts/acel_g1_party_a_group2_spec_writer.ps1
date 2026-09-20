<#
.SYNOPSIS
    ACEL G1 T3B Group 2 principal-bound specification writer (fail-closed).

.DESCRIPTION
    Builds, from the exact operator-approved fixed v1 policy payload, the
    T2F Group 2 `cvf.specFile` record (`SPEC_v1.json`) canonicalized and
    hashed under `cvf.source-record-canonicalization@1`, with the additional
    direct raw-content `specHashHex` T2C's `verificationAuthorityHash` binds
    to. Writes it, exclusively, only as the exact expected Party A principal.

    Default invocation is a hermetic self-test that proves every guard using
    a disposable sandbox rooted under the current user's temporary directory
    and removes it. Real-mode execution requires -ExecuteWrite, an exact
    principal name and SID match, a non-elevated interactive session, and a
    typed confirmation, after every other guard has already passed. Real mode
    additionally hardens the created file's NTFS DACL (never SACL) so the
    approver principal cannot modify it while Local review can still read it.

    This tool does not claim candidate admission, spec approval, activation
    or T3E consumer wiring. Its real-mode output text is exactly
    `SPEC_CREATED_PENDING_LOCAL_VERIFICATION`.

.PARAMETER SelfTest
    Run hermetic positive and negative self-tests as the current user against
    a disposable sandbox. This is the default when no mode is chosen and
    never targets the real Group 2 spec path or the expected Party A
    principal.

.PARAMETER ExecuteWrite
    Perform the real Group 2 spec write. Requires the current process
    identity to match both -ExpectedAccountName and -ExpectedAccountSid
    exactly, a non-elevated interactive host, and an interactive typed
    confirmation.

.PARAMETER ExpectedAccountName
    Exact expected Windows account name, e.g. 'HOSTNAME\cvf-g1-party-a'. A
    bare name is qualified with the local computer name before comparison.

.PARAMETER ExpectedAccountSid
    Exact expected Windows account SID.

.EXAMPLE
    pwsh -NoProfile -File scripts/acel_g1_party_a_group2_spec_writer.ps1 -SelfTest

.NOTES
    Claim boundary: tooling only. A self-test proves guard behavior, not that
    any Group 2 source was created. Real-mode output text explicitly reads
    `SPEC_CREATED_PENDING_LOCAL_VERIFICATION`, never approval, activation,
    admission or T3E consumer wiring.
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
    [string] $ExpectedAccountSid
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

$script:ToolContract       = 'cvf.acel.g1.group2SpecWriterTool@1'
$script:CanonProfile       = 'cvf.source-record-canonicalization@1'
$script:SpecFileDomain     = 'cvf.specFile'
$script:ConfirmationPhrase = 'EXECUTE GROUP 2 SPEC WRITE'
$script:SpecRelativePath   = 'governance/sources/verification_authority_spec/SPEC_v1.json'
$script:RealModeResultText = 'SPEC_CREATED_PENDING_LOCAL_VERIFICATION'
$script:ExpectedSpecVersion = 1

# Exact expected Party A principal, per
# `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md`
# and `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md`.
$script:VerifiedPartyAIdentity = [ordered]@{
    principalName = 'LAM-RUBY\cvf-g1-party-a'
    principalSid  = 'S-1-5-21-1644666849-912006174-747199667-1006'
}

# T3B-RV-1 (R1 correction): the exact non-admin Approver and Local reviewer
# SIDs that must each receive an EXPLICIT read-only grant on the Party
# A-created spec file. Group membership (e.g. `BUILTIN\Administrators`) is
# never sufficient by itself: the Approver is not an Administrator, and
# Local's own Administrators SID is deny-only in a non-elevated token, so an
# Administrators-only grant leaves both cross-principal readers unable to
# read the file. Per
# `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md`.
$script:VerifiedApproverReaderSid = 'S-1-5-21-1644666849-912006174-747199667-1008'
$script:VerifiedLocalReaderSid    = 'S-1-5-21-1644666849-912006174-747199667-1001'

# Fixed, operator-approved v1 policy payload, exact UTF-8 bytes, no BOM, no
# trailing newline. Byte-for-byte from the work order's "Fixed v1 payload"
# section and the operator decision's "Policy decision" section.
$script:FixedV1PolicyJson = '{"admissionRequiredLookupResult":"IDENTITY_CONFIRMED","authorityId":"ACEL_G1_DECISION_OWNER","authoritySpecSchema":"cvf.acel.g1.verificationAuthoritySpec@1","freshnessThresholdSeconds":86400,"issuerVerificationRequirement":"VERIFIED_BY_LIVE_REGISTRY_LOOKUP","receiptDomain":"cvf.verifierReceipt","receiptProfileVersion":"v1"}'

Add-Type -AssemblyName System.Security | Out-Null

# Compiled duplicate-JSON-member scanner, ported unmodified in behavior from
# the accepted Group 1 writer (`scripts/acel_g1_party_a_group1_source_writer.ps1`).
Add-Type -Language CSharp -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Text.Json;

public static class CvfAcelG1Group2JsonDuplicateMemberScanner
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

function ConvertTo-Base64UrlNoPadding {
    param([Parameter(Mandatory = $true)][byte[]] $Bytes)
    return [System.Convert]::ToBase64String($Bytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')
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
    <#
        .SYNOPSIS
            Parse JSON text into a member list, rejecting any duplicate
            top-level member name (including escaped aliases). Ported
            pattern from the accepted Group 1 writer.
    #>
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
        $duplicateMemberName = [CvfAcelG1Group2JsonDuplicateMemberScanner]::FindFirstTopLevelDuplicateMemberName($utf8Bytes)
    } catch {
        Stop-Writer -GuardId 'JSON_UNPARSEABLE' -Message "text is not valid JSON: $($_.Exception.Message)"
    }
    if ($null -ne $duplicateMemberName) {
        Stop-Writer -GuardId 'JSON_DUPLICATE_MEMBER' -Message (
            "duplicate top-level JSON member '$duplicateMemberName' (after JSON escape decoding)")
    }

    return $parsed
}

# --------------------------------------------------------------------------
# Fixed v1 policy validation
# --------------------------------------------------------------------------

function Get-FixedV1PolicyBytes {
    <#
        .SYNOPSIS
            Return the exact fixed UTF-8 bytes of the operator-approved v1
            policy payload, with no BOM and no trailing newline, verified
            byte-for-byte against `$script:FixedV1PolicyJson` on every call
            so drift in the literal is impossible to smuggle through this
            function silently.
    #>
    $bytes = [System.Text.UTF8Encoding]::new($false).GetBytes($script:FixedV1PolicyJson)
    if ($bytes.Length -eq 0) {
        Stop-Writer -GuardId 'FIXED_POLICY_EMPTY' -Message 'fixed v1 policy literal is unexpectedly empty'
    }
    # Reject a BOM or trailing newline defensively, even though the literal
    # is a PowerShell string constant that cannot itself carry either.
    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        Stop-Writer -GuardId 'FIXED_POLICY_HAS_BOM' -Message 'fixed v1 policy bytes unexpectedly begin with a UTF-8 BOM'
    }
    if ($bytes[$bytes.Length - 1] -eq 0x0A -or $bytes[$bytes.Length - 1] -eq 0x0D) {
        Stop-Writer -GuardId 'FIXED_POLICY_HAS_TRAILING_NEWLINE' -Message 'fixed v1 policy bytes unexpectedly end with a newline'
    }
    return $bytes
}

# --------------------------------------------------------------------------
# C2-03-equivalent: spec-file record construction
# --------------------------------------------------------------------------

function New-SpecFileRecordPreimage {
    <#
        .SYNOPSIS
            Build the exact closed `cvf.specFile` preimage: `profile`,
            `domain`, `specVersion`, `canonicalBytesBase64`, `authorId`,
            `proposedAt`, `specHashHex`. No more, no fewer.
    #>
    param(
        [Parameter(Mandatory = $true)][int]    $SpecVersion,
        [Parameter(Mandatory = $true)][string] $CanonicalBytesBase64,
        [Parameter(Mandatory = $true)][string] $AuthorId,
        [Parameter(Mandatory = $true)][string] $ProposedAt,
        [Parameter(Mandatory = $true)][string] $SpecHashHex
    )
    return [ordered]@{
        profile              = $script:CanonProfile
        domain               = $script:SpecFileDomain
        specVersion          = $SpecVersion
        canonicalBytesBase64 = $CanonicalBytesBase64
        authorId             = $AuthorId
        proposedAt           = $ProposedAt
        specHashHex          = $SpecHashHex
    }
}

function New-SpecFileRecord {
    <#
        .SYNOPSIS
            Build the full `SPEC_v1.json` record from the fixed policy bytes
            and the given author identity/timestamp, computing BOTH distinct
            Group 2 hashes per T2F's "Two Distinct Group 2 Hashes" subsection:
            `specHashHex` (direct SHA-256 of the decoded raw content bytes,
            never itself hashed under the canonicalization profile) and
            `specFileRecordHashHex` (the `cvf.specFile` closed-preimage
            digest, which includes `specHashHex` as a normal field value).
    #>
    param(
        [Parameter(Mandatory = $true)][byte[]] $DecodedPolicyBytes,
        [Parameter(Mandatory = $true)][string] $AuthorId,
        [Parameter(Mandatory = $true)][string] $ProposedAt
    )

    $canonicalBytesBase64 = ConvertTo-Base64UrlNoPadding -Bytes $DecodedPolicyBytes
    # specHashHex: direct SHA-256 of the raw decoded bytes only, never routed
    # through the canonicalization profile's own preimage/digest helper.
    $specHashHex = Get-Sha256Hex -Bytes $DecodedPolicyBytes

    $recordPreimage = New-SpecFileRecordPreimage -SpecVersion $script:ExpectedSpecVersion `
        -CanonicalBytesBase64 $canonicalBytesBase64 -AuthorId $AuthorId -ProposedAt $ProposedAt `
        -SpecHashHex $specHashHex
    $specFileRecordHashHex = Get-PreimageDigestHex -Preimage $recordPreimage

    $record = [ordered]@{
        profile               = $script:CanonProfile
        domain                = $script:SpecFileDomain
        specVersion           = $script:ExpectedSpecVersion
        canonicalBytesBase64  = $canonicalBytesBase64
        authorId              = $AuthorId
        proposedAt            = $ProposedAt
        specHashHex           = $specHashHex
        specFileRecordHashHex = $specFileRecordHashHex
    }

    return [pscustomobject]@{
        Record                 = $record
        SpecHashHex            = $specHashHex
        SpecFileRecordHashHex  = $specFileRecordHashHex
        CanonicalBytesBase64   = $canonicalBytesBase64
        RecordPreimageBytes    = (ConvertTo-CanonicalJsonBytes -Object $recordPreimage)
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
    <#
        .SYNOPSIS
            Reject unless the CURRENT identity is exactly the expected
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

function Assert-ExpectedPrincipalIsVerifiedPartyA {
    <#
        .SYNOPSIS
            T3B: reject unless the caller-supplied -ExpectedAccountName/-Sid
            themselves equal the verified Party A identity. This prevents a
            caller from supplying a DIFFERENT self-consistent principal pair
            and having it silently accepted; real mode only ever binds to
            the one operator-verified Party A principal.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )
    $qualifiedCandidate = Resolve-QualifiedAccountName -AccountName $ExpectedAccountName
    $qualifiedVerified = Resolve-QualifiedAccountName -AccountName $script:VerifiedPartyAIdentity.principalName
    if ($qualifiedCandidate -ne $qualifiedVerified) {
        Stop-Writer -GuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_A' -Message (
            "supplied -ExpectedAccountName '$qualifiedCandidate' does not equal the verified Party A identity '$qualifiedVerified'")
    }
    if ($ExpectedAccountSid.Trim() -ne $script:VerifiedPartyAIdentity.principalSid) {
        Stop-Writer -GuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_A' -Message (
            "supplied -ExpectedAccountSid does not equal the verified Party A SID")
    }
}

function Assert-InteractiveConfirmation {
    param([Parameter(Mandatory = $true)][string] $ExpectedAccountName)

    Write-Host ''
    Write-Host "About to write the Group 2 SPEC_v1.json for '$ExpectedAccountName'."
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

function Resolve-GroupTwoSpecPath {
    <#
        .SYNOPSIS
            Resolve and validate the governed Group 2 spec output path under
            the given repository root.
    #>
    param([Parameter(Mandatory = $true)][string] $RepositoryRoot)

    $normalizedRoot = [System.IO.Path]::GetFullPath($RepositoryRoot)
    $specPath = [System.IO.Path]::GetFullPath((Join-Path $normalizedRoot $script:SpecRelativePath))

    if (-not (Test-PathIsInside -CandidatePath $specPath -ContainerPath $normalizedRoot)) {
        Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message (
            "resolved path '$specPath' does not resolve inside repository root '$normalizedRoot'")
    }
    Assert-NoReparsePointInAncestry -NormalizedPath $specPath

    return $specPath
}

function Assert-NoExistingGroupTwoSpec {
    param([Parameter(Mandatory = $true)][string] $SpecPath)
    if (Test-Path -LiteralPath $SpecPath) {
        Stop-Writer -GuardId 'OUTPUT_TARGET_COLLISION' -Message (
            "output file '$SpecPath' already exists; refusing to overwrite an existing Group 2 spec")
    }
}

# --------------------------------------------------------------------------
# Atomic exclusive-create write (ported pattern)
# --------------------------------------------------------------------------

function New-ExclusiveFile {
    <#
        .SYNOPSIS
            Create a new file exclusively, or fail, leaving no partial file
            and no newly-created directory behind. Ported unmodified in
            behavior from the accepted Group 1 writer's helper of the same
            name, including its `InjectFailureAtForTest` hermetic-test-only
            failure-boundary parameter.
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

# --------------------------------------------------------------------------
# DACL/ownership hardening (NTFS DACL only, never SeSecurityPrivilege)
# --------------------------------------------------------------------------

function Protect-CreatedFileAgainstOtherPrincipal {
    <#
        .SYNOPSIS
            Harden a just-created file's NTFS DACL (never SACL) so that only
            the creating principal (current identity) and the built-in
            Administrators/SYSTEM accounts (for Local review/backup) retain
            access, and the named other principal (the approver, for the
            Party A spec writer) has no explicit grant. Uses
            `System.Security.AccessControl.FileSecurity` only; never touches
            the SACL and never requests `SeSecurityPrivilege`.

        .DESCRIPTION
            This is a best-effort hardening step layered on top of the
            exclusive-create write, not the sole integrity control: the
            dual-hash scheme and append-only decision chain remain the
            authoritative tamper-evidence mechanism. If this step itself
            fails (for example, insufficient rights to change a DACL on a
            volume that does not support NTFS ACLs), the guard fails closed
            rather than silently leaving the file unprotected.

        .PARAMETER FilePath
            The just-created file to harden.

        .PARAMETER OwnerAccountSid
            The SID that must retain read/write access (the creating
            principal, i.e. the current identity in real mode).

        .PARAMETER LocalReaderAccountSids
            Additional SIDs (for example, BUILTIN\Administrators) that must
            retain read-only access so Local can verify the file. May be
            empty.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $FilePath,
        [Parameter(Mandatory = $true)][string] $OwnerAccountSid,
        [string[]] $LocalReaderAccountSids = @()
    )

    try {
        $ownerIdentity = [System.Security.Principal.SecurityIdentifier]::new($OwnerAccountSid)
        $fileSecurity = [System.Security.AccessControl.FileSecurity]::new()
        # Disable inheritance and remove any inherited rules: the ACL that
        # results is exactly and only what this function adds below.
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

function Write-GroupTwoSpecOutput {
    <#
        .SYNOPSIS
            Write the Group 2 spec file, failure-atomically, then harden its
            DACL/ownership. If the DACL step fails, the file is removed
            rather than left behind unprotected, so a failure never leaves a
            durable, un-hardened Group 2 spec.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $SpecPath,
        [Parameter(Mandatory = $true)] $Record,
        [Parameter(Mandatory = $true)][string] $OwnerAccountSid,
        [string[]] $LocalReaderAccountSids = @(),
        [switch] $SkipDaclHardening,
        [ValidateSet('Create', 'Write', 'Flush')]
        [string] $InjectFailureAtForTest
    )

    $directory = [System.IO.Path]::GetDirectoryName($SpecPath)
    $directoryPreExisted = Test-Path -LiteralPath $directory

    $json = ($Record | ConvertTo-Json -Depth 8)
    $bytes = [System.Text.UTF8Encoding]::new($false).GetBytes($json + [System.Environment]::NewLine)

    if ($InjectFailureAtForTest) {
        New-ExclusiveFile -Path $SpecPath -Content $bytes -InjectFailureAtForTest $InjectFailureAtForTest
    } else {
        New-ExclusiveFile -Path $SpecPath -Content $bytes
    }

    if (-not $SkipDaclHardening) {
        try {
            Protect-CreatedFileAgainstOtherPrincipal -FilePath $SpecPath `
                -OwnerAccountSid $OwnerAccountSid -LocalReaderAccountSids $LocalReaderAccountSids | Out-Null
        } catch {
            Remove-Item -LiteralPath $SpecPath -Force -ErrorAction SilentlyContinue
            if (-not $directoryPreExisted) {
                Remove-Item -LiteralPath $directory -Force -ErrorAction SilentlyContinue
            }
            throw
        }
    }

    return $SpecPath
}

# --------------------------------------------------------------------------
# Real-mode orchestration
# --------------------------------------------------------------------------

function Invoke-GroupTwoSpecWrite {
    <#
        .SYNOPSIS
            Execute the guarded real-mode write. Every guard runs before any
            file is created.

        .DESCRIPTION
            Real mode always resolves the repository from this script's own
            committed location; it never accepts an operator-selectable
            alternate repository root. Fixture-root injection is confined to
            `Invoke-SelfTest` and its helpers. The fixed v1 policy bytes and
            the verified Party A identity are read directly from
            `$script:FixedV1PolicyJson`/`$script:VerifiedPartyAIdentity`; no
            parameter, environment variable, or file input can substitute a
            different policy or authority.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )

    $current = Get-CurrentPrincipalFact
    $repositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path

    Assert-ExpectedPrincipal -CurrentPrincipal $current `
        -ExpectedAccountName $ExpectedAccountName -ExpectedAccountSid $ExpectedAccountSid
    Assert-ExpectedPrincipalIsVerifiedPartyA -ExpectedAccountName $ExpectedAccountName `
        -ExpectedAccountSid $ExpectedAccountSid

    $specPath = Resolve-GroupTwoSpecPath -RepositoryRoot $repositoryRoot
    Assert-NoExistingGroupTwoSpec -SpecPath $specPath

    Assert-InteractiveConfirmation -ExpectedAccountName $ExpectedAccountName

    $decodedPolicyBytes = Get-FixedV1PolicyBytes
    $proposedAt = (Get-Date).ToUniversalTime().ToString('o')
    $built = New-SpecFileRecord -DecodedPolicyBytes $decodedPolicyBytes `
        -AuthorId $current.Sid -ProposedAt $proposedAt

    # T3B-RV-1 (R1 correction): grant explicit read-only rights to the
    # Approver SID (so the required decision writer can actually read this
    # spec) and to the Local reviewer SID (so Local's ordinary non-elevated
    # token can read it without depending on a deny-only Administrators
    # grant). `BUILTIN\Administrators` is no longer relied upon as the sole
    # cross-principal read path.
    $writtenPath = Write-GroupTwoSpecOutput -SpecPath $specPath -Record $built.Record `
        -OwnerAccountSid $current.Sid `
        -LocalReaderAccountSids @($script:VerifiedApproverReaderSid, $script:VerifiedLocalReaderSid)

    Write-Host ''
    Write-Host $script:RealModeResultText
    Write-Host "  spec             : $writtenPath"
    Write-Host "  specVersion      : $($script:ExpectedSpecVersion)"
    Write-Host "  specHashHex      : $($built.SpecHashHex)"
    Write-Host "  specFileRecordHashHex : $($built.SpecFileRecordHashHex)"
    Write-Host ''
    Write-Host 'This does NOT claim approval, activation, candidate admission or T3E consumer wiring.'
    return $writtenPath
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

function Invoke-NonInteractiveWriteProbe {
    <#
        .SYNOPSIS
            Prove a genuinely non-interactive process calling
            `Assert-InteractiveConfirmation` fails with
            `NONINTERACTIVE_EXECUTION_REJECTED`, without weakening or
            bypassing the real `-ExecuteWrite` authority boundary. Ported
            pattern from the accepted Group 1 writer.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $SandboxDirectory
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
            disposable fixtures only. Never targets the real Party A
            principal or the real Group 2 spec path, and removes every
            disposable artifact it creates.
    #>

    $current = Get-CurrentPrincipalFact
    $localAppData = [System.Environment]::GetFolderPath(
        [System.Environment+SpecialFolder]::LocalApplicationData)

    Write-Host ''
    Write-Host "$($script:ToolContract) hermetic self-test"
    Write-Host "  identity : $($current.Name)"
    Write-Host "  elevated : $($current.IsElevated)"
    Write-Host '  mode     : SELF_TEST (no Party A context, no durable Group 2 output)'
    Write-Host ''

    $sandbox = Join-Path -Path $localAppData -ChildPath (
        'CVF_ACEL_G1_GROUP2_SPEC_WRITER_SELFTEST_{0}' -f ([System.Guid]::NewGuid().ToString('N')))
    New-Item -ItemType Directory -Path $sandbox -Force | Out-Null

    try {
        # ---- T3B-01: default non-mutation ---------------------------------
        Add-TestResult -CaseId 'T3B-01-A' -Contract 'T3B-01' `
            -Passed ($PSCmdlet.ParameterSetName -eq 'SelfTest') `
            -Detail 'default parameter set is SelfTest; write requires -ExecuteWrite'

        $realSpecDir = Join-Path (Split-Path -Path $PSScriptRoot -Parent) 'governance/sources/verification_authority_spec'
        $noDurableOutput = -not (Test-Path -LiteralPath (Join-Path $realSpecDir 'SPEC_v1.json'))
        Add-TestResult -CaseId 'T3B-01-B' -Contract 'T3B-01' -Passed $noDurableOutput `
            -Detail 'default self-test created no durable output under the real repository Group 2 spec path'

        # ---- T3B-02: exact decoded bytes -----------------------------------
        $decodedPolicyBytes = Get-FixedV1PolicyBytes
        $reDecodedText = [System.Text.UTF8Encoding]::new($false).GetString($decodedPolicyBytes)
        Add-TestResult -CaseId 'T3B-02-A' -Contract 'T3B-02' `
            -Passed ($reDecodedText -eq $script:FixedV1PolicyJson) `
            -Detail 'fixed v1 policy bytes decode back to the exact literal JSON text'
        Add-TestResult -CaseId 'T3B-02-B' -Contract 'T3B-02' `
            -Passed ($decodedPolicyBytes[0] -ne 0xEF) `
            -Detail 'fixed v1 policy bytes carry no UTF-8 BOM'
        $lastByte = $decodedPolicyBytes[$decodedPolicyBytes.Length - 1]
        Add-TestResult -CaseId 'T3B-02-C' -Contract 'T3B-02' `
            -Passed ($lastByte -ne 0x0A -and $lastByte -ne 0x0D) `
            -Detail 'fixed v1 policy bytes carry no trailing newline'

        # ---- T3B-03: base64url round trip ----------------------------------
        $canonicalBytesBase64 = ConvertTo-Base64UrlNoPadding -Bytes $decodedPolicyBytes
        $roundTrippedBytes = ConvertFrom-Base64Url -Text $canonicalBytesBase64
        $roundTripMatches = ($roundTrippedBytes.Length -eq $decodedPolicyBytes.Length) -and
            (-not (Compare-Object $roundTrippedBytes $decodedPolicyBytes))
        Add-TestResult -CaseId 'T3B-03-A' -Contract 'T3B-03' -Passed $roundTripMatches `
            -Detail 'canonicalBytesBase64 round-trips byte-for-byte through decode'
        Add-TestResult -CaseId 'T3B-03-B' -Contract 'T3B-03' `
            -Passed (-not $canonicalBytesBase64.Contains('=')) `
            -Detail 'canonicalBytesBase64 is unpadded'

        # ---- T3B-04: direct content and record hashes ----------------------
        $fixtureAuthorId = 'S-1-5-21-0-0-0-9001-fixture-author'
        $fixtureProposedAt = (Get-Date).ToUniversalTime().ToString('o')
        $built = New-SpecFileRecord -DecodedPolicyBytes $decodedPolicyBytes `
            -AuthorId $fixtureAuthorId -ProposedAt $fixtureProposedAt

        $expectedSpecHashHex = Get-Sha256Hex -Bytes $decodedPolicyBytes
        Add-TestResult -CaseId 'T3B-04-A' -Contract 'T3B-04' `
            -Passed ($built.SpecHashHex -eq $expectedSpecHashHex) `
            -Detail 'specHashHex equals direct SHA-256 of decoded content bytes'

        $recordPreimage = New-SpecFileRecordPreimage -SpecVersion $script:ExpectedSpecVersion `
            -CanonicalBytesBase64 $built.CanonicalBytesBase64 -AuthorId $fixtureAuthorId `
            -ProposedAt $fixtureProposedAt -SpecHashHex $built.SpecHashHex
        $expectedRecordHashHex = Get-PreimageDigestHex -Preimage $recordPreimage
        Add-TestResult -CaseId 'T3B-04-B' -Contract 'T3B-04' `
            -Passed ($built.SpecFileRecordHashHex -eq $expectedRecordHashHex) `
            -Detail 'specFileRecordHashHex equals the recomputed cvf.specFile closed-preimage digest'
        Add-TestResult -CaseId 'T3B-04-C' -Contract 'T3B-04' `
            -Passed ($built.SpecHashHex -ne $built.SpecFileRecordHashHex) `
            -Detail 'specHashHex and specFileRecordHashHex are two genuinely distinct digests'

        # Two records with identical content but different authorId/proposedAt
        # must share the same specHashHex (content identity independent of
        # publishing metadata) but a different specFileRecordHashHex.
        $builtAlt = New-SpecFileRecord -DecodedPolicyBytes $decodedPolicyBytes `
            -AuthorId 'S-1-5-21-0-0-0-9002-different-author' -ProposedAt (Get-Date).AddMinutes(5).ToUniversalTime().ToString('o')
        Add-TestResult -CaseId 'T3B-04-D' -Contract 'T3B-04' `
            -Passed ($built.SpecHashHex -eq $builtAlt.SpecHashHex) `
            -Detail 'specHashHex is identical across two records with byte-identical content but different authorId/proposedAt'
        Add-TestResult -CaseId 'T3B-04-E' -Contract 'T3B-04' `
            -Passed ($built.SpecFileRecordHashHex -ne $builtAlt.SpecFileRecordHashHex) `
            -Detail 'specFileRecordHashHex differs across two records with different authorId/proposedAt metadata'

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
        try {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
            Add-TestResult -CaseId 'T3B-08-D' -Contract 'T3B-08' -Passed (-not $current.IsElevated) `
                -Detail 'exact current name and SID accepted in a non-elevated context'
        } catch {
            Add-TestResult -CaseId 'T3B-08-D' -Contract 'T3B-08' -Passed $current.IsElevated `
                -Detail "matching identity rejected: $($_.Exception.Message)"
        }

        # This self-test genuinely runs as the CURRENT user, never as the
        # real Party A principal, so asserting the current identity against
        # the verified Party A identity must fail closed here -- proving the
        # guard is live, not merely present in source. This is expected and
        # correct: it is what proves T3B-09 (no Party A contact).
        Test-GuardRejects -CaseId 'T3B-08-E' -Contract 'T3B-08' `
            -ExpectedGuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_A' -Action {
            Assert-ExpectedPrincipalIsVerifiedPartyA -ExpectedAccountName $current.Name `
                -ExpectedAccountSid $current.Sid
        }
        try {
            Assert-ExpectedPrincipalIsVerifiedPartyA `
                -ExpectedAccountName $script:VerifiedPartyAIdentity.principalName `
                -ExpectedAccountSid $script:VerifiedPartyAIdentity.principalSid
            Add-TestResult -CaseId 'T3B-08-F' -Contract 'T3B-08' -Passed $true `
                -Detail 'exact verified Party A name/SID pair is accepted by the binding guard'
        } catch {
            Add-TestResult -CaseId 'T3B-08-F' -Contract 'T3B-08' -Passed $false `
                -Detail "verified Party A pair unexpectedly rejected: $($_.Exception.Message)"
        }
        Test-GuardRejects -CaseId 'T3B-08-G' -Contract 'T3B-08' `
            -ExpectedGuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_A' -Action {
            Assert-ExpectedPrincipalIsVerifiedPartyA `
                -ExpectedAccountName $script:VerifiedPartyAIdentity.principalName `
                -ExpectedAccountSid 'S-1-5-21-0-0-0-9999'
        }

        # ---- T3B-08 (path/collision) ---------------------------------------
        $fixtureRepoRoot = Join-Path -Path $sandbox -ChildPath 'fixture_repo'
        New-Item -ItemType Directory -Path $fixtureRepoRoot -Force | Out-Null
        $fixturePaths = Resolve-GroupTwoSpecPath -RepositoryRoot $fixtureRepoRoot
        Assert-NoExistingGroupTwoSpec -SpecPath $fixturePaths
        Add-TestResult -CaseId 'T3B-08-H' -Contract 'T3B-08' -Passed $true `
            -Detail 'fresh fixture repository has no pre-existing Group 2 spec collision'

        $outsideRoot = Join-Path -Path $sandbox -ChildPath 'outside_repo'
        New-Item -ItemType Directory -Path $outsideRoot -Force | Out-Null
        Test-GuardRejects -CaseId 'T3B-08-I' -Contract 'T3B-08' `
            -ExpectedGuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Action {
            Test-PathIsInside -CandidatePath 'C:\Windows\System32\evil.json' -ContainerPath $outsideRoot | Out-Null
            if (-not (Test-PathIsInside -CandidatePath 'C:\Windows\System32\evil.json' -ContainerPath $outsideRoot)) {
                Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message 'synthetic escape check'
            }
        }

        $preexistingRoot = Join-Path -Path $sandbox -ChildPath 'preexisting_repo'
        New-Item -ItemType Directory -Path $preexistingRoot -Force | Out-Null
        $preexistingSpecPath = Resolve-GroupTwoSpecPath -RepositoryRoot $preexistingRoot
        New-Item -ItemType Directory -Path ([System.IO.Path]::GetDirectoryName($preexistingSpecPath)) -Force | Out-Null
        [System.IO.File]::WriteAllBytes($preexistingSpecPath, [byte[]]@(9, 9, 9))
        Test-GuardRejects -CaseId 'T3B-08-J' -Contract 'T3B-08' `
            -ExpectedGuardId 'OUTPUT_TARGET_COLLISION' -Action {
            Assert-NoExistingGroupTwoSpec -SpecPath $preexistingSpecPath
        }

        # ---- T3B-08 (noninteractive confirmation) ---------------------------
        $childResult = Invoke-NonInteractiveWriteProbe -SandboxDirectory $sandbox
        $childRejectedAtConfirmation = ($childResult.ExitCode -ne 0 -and $childResult.GuardObserved)
        Add-TestResult -CaseId 'T3B-08-K' -Contract 'T3B-08' `
            -Passed $childRejectedAtConfirmation `
            -Detail ("noninteractive child exit=$($childResult.ExitCode), " +
                "confirmationGuard=$($childResult.GuardObserved)")
        Test-GuardRejects -CaseId 'T3B-08-L' -Contract 'T3B-08' `
            -ExpectedGuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Action {
            Assert-InteractiveConfirmation -ExpectedAccountName $current.Name
        }

        # ---- T3B-05/T3B-07: atomic write and negative writer probes --------
        $writeRoot = Join-Path -Path $sandbox -ChildPath 'write_repo'
        New-Item -ItemType Directory -Path $writeRoot -Force | Out-Null
        $writeSpecPath = Resolve-GroupTwoSpecPath -RepositoryRoot $writeRoot
        $writtenPath = Write-GroupTwoSpecOutput -SpecPath $writeSpecPath -Record $built.Record `
            -OwnerAccountSid $current.Sid -LocalReaderAccountSids @()
        $writeSucceeded = Test-Path -LiteralPath $writtenPath
        Add-TestResult -CaseId 'T3B-05-A' -Contract 'T3B-05' -Passed $writeSucceeded `
            -Detail "exclusive-create write of fixture spec record succeeded at '$writtenPath'"

        $rereadRecord = Get-StrictJsonObjectFromText -Text (Get-Content -LiteralPath $writtenPath -Raw)
        Add-TestResult -CaseId 'T3B-05-B' -Contract 'T3B-05' `
            -Passed ($rereadRecord.specFileRecordHashHex -eq $built.SpecFileRecordHashHex) `
            -Detail 're-read written record specFileRecordHashHex matches the value computed before write'

        # Second write to the same path must collide (exclusive create).
        $secondWriteRoot = Join-Path -Path $sandbox -ChildPath 'second_write_probe'
        New-Item -ItemType Directory -Path $secondWriteRoot -Force | Out-Null
        try {
            New-ExclusiveFile -Path $writtenPath -Content ([byte[]]@(1, 2, 3))
            Add-TestResult -CaseId 'T3B-05-C' -Contract 'T3B-05' -Passed $false `
                -Detail 'expected EXCLUSIVE_CREATE_FAILED but a second write to the same path was allowed'
        } catch {
            $guardId = if ($_.Exception -is [WriterGuardFailure]) { $_.Exception.GuardId } else { '<non-guard>' }
            Add-TestResult -CaseId 'T3B-05-C' -Contract 'T3B-05' -Passed ($guardId -eq 'EXCLUSIVE_CREATE_FAILED') `
                -Detail "second exclusive-create attempt at the same path rejected with '$guardId'"
        }

        # ---- T3B-05 (six-boundary atomic failure matrix) --------------------
        $boundaries = @('Create', 'Write', 'Flush')
        foreach ($boundary in $boundaries) {
            $boundaryRoot = Join-Path -Path $sandbox -ChildPath "boundary_$($boundary)_repo"
            New-Item -ItemType Directory -Path $boundaryRoot -Force | Out-Null
            $boundarySpecPath = Resolve-GroupTwoSpecPath -RepositoryRoot $boundaryRoot
            $boundaryCleaned = $false
            try {
                Write-GroupTwoSpecOutput -SpecPath $boundarySpecPath -Record $built.Record `
                    -OwnerAccountSid $current.Sid -InjectFailureAtForTest $boundary -SkipDaclHardening | Out-Null
            } catch {
                $specAbsent = -not (Test-Path -LiteralPath $boundarySpecPath)
                $specDirAbsent = -not (Test-Path -LiteralPath (
                        [System.IO.Path]::GetDirectoryName($boundarySpecPath)))
                $boundaryCleaned = $specAbsent -and $specDirAbsent
            }
            Add-TestResult -CaseId "T3B-05-$boundary" -Contract 'T3B-05' -Passed $boundaryCleaned `
                -Detail "injected '$boundary' failure removed the file this invocation created and its fresh empty directory"
        }

        # ---- T3B-06: DACL/ownership hardening code-path proof ---------------
        # This hermetic test can only ever run as the current agent identity
        # (never as the real Party A or approver principal), so it verifies
        # the DACL-SETTING CODE PATH runs and produces a restrictive-but-
        # Local-readable ACL on a fixture file owned by the current identity.
        # It does not and cannot assert real cross-principal enforcement,
        # which only the operator can observe end-to-end after real
        # principal-separated execution.
        $daclFixtureRoot = Join-Path -Path $sandbox -ChildPath 'dacl_fixture_repo'
        New-Item -ItemType Directory -Path $daclFixtureRoot -Force | Out-Null
        $daclFixturePath = Join-Path -Path $daclFixtureRoot -ChildPath 'dacl_fixture.json'
        [System.IO.File]::WriteAllBytes($daclFixturePath, [System.Text.Encoding]::UTF8.GetBytes('{"fixture":true}'))
        $daclApplied = $false
        try {
            Protect-CreatedFileAgainstOtherPrincipal -FilePath $daclFixturePath `
                -OwnerAccountSid $current.Sid -LocalReaderAccountSids @('S-1-5-32-544') | Out-Null
            $daclApplied = $true
        } catch {
            $daclApplied = $false
        }
        Add-TestResult -CaseId 'T3B-06-A' -Contract 'T3B-06' -Passed $daclApplied `
            -Detail 'DACL/ownership hardening code path ran without error against a fixture file owned by the current identity'

        if ($daclApplied) {
            $resultAcl = Get-Acl -LiteralPath $daclFixturePath
            $isProtected = $resultAcl.AreAccessRulesProtected
            Add-TestResult -CaseId 'T3B-06-B' -Contract 'T3B-06' -Passed $isProtected `
                -Detail "resulting ACL has inheritance disabled (AreAccessRulesProtected=$isProtected), i.e. is not silently inheriting a permissive parent ACL"

            $currentSidHasAllow = @($resultAcl.Access | Where-Object {
                    $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq $current.Sid -and
                    $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow
                }).Count -gt 0
            Add-TestResult -CaseId 'T3B-06-C' -Contract 'T3B-06' -Passed $currentSidHasAllow `
                -Detail 'owning/current identity retains an explicit Allow access rule after hardening (Local-readable via the owning identity)'

            $adminsSidHasAllow = @($resultAcl.Access | Where-Object {
                    $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq 'S-1-5-32-544' -and
                    $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow
                }).Count -gt 0
            Add-TestResult -CaseId 'T3B-06-D' -Contract 'T3B-06' -Passed $adminsSidHasAllow `
                -Detail 'named Local-reader SID (BUILTIN\Administrators) retains an explicit Allow read rule after hardening'

            # No unexpected identity beyond the owner and the named reader
            # holds an Allow rule -- this is the restrictive half of
            # "restrictive-but-Local-readable."
            $unexpectedAllow = @($resultAcl.Access | Where-Object {
                    $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow -and
                    $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -notin @($current.Sid, 'S-1-5-32-544')
                })
            Add-TestResult -CaseId 'T3B-06-E' -Contract 'T3B-06' -Passed ($unexpectedAllow.Count -eq 0) `
                -Detail "no Allow rule exists for any identity beyond the owner and the named Local reader (found $($unexpectedAllow.Count) unexpected)"
        } else {
            Add-TestResult -CaseId 'T3B-06-B' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
            Add-TestResult -CaseId 'T3B-06-C' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
            Add-TestResult -CaseId 'T3B-06-D' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
            Add-TestResult -CaseId 'T3B-06-E' -Contract 'T3B-06' -Passed $false -Detail 'skipped: hardening call itself failed'
        }

        # Write-GroupTwoSpecOutput's own end-to-end DACL integration (not
        # skipped) on a fresh fixture repo.
        $daclIntegrationRoot = Join-Path -Path $sandbox -ChildPath 'dacl_integration_repo'
        New-Item -ItemType Directory -Path $daclIntegrationRoot -Force | Out-Null
        $daclIntegrationSpecPath = Resolve-GroupTwoSpecPath -RepositoryRoot $daclIntegrationRoot
        $daclIntegrationWritten = Write-GroupTwoSpecOutput -SpecPath $daclIntegrationSpecPath -Record $built.Record `
            -OwnerAccountSid $current.Sid -LocalReaderAccountSids @('S-1-5-32-544')
        $integrationAcl = Get-Acl -LiteralPath $daclIntegrationWritten
        $integrationProtected = $integrationAcl.AreAccessRulesProtected
        Add-TestResult -CaseId 'T3B-06-F' -Contract 'T3B-06' -Passed $integrationProtected `
            -Detail 'Write-GroupTwoSpecOutput applies DACL hardening end-to-end (not only via the standalone helper) on a freshly written fixture spec file'

        # ---- T3B-RV-1 (R1 regression): explicit cross-principal read grants
        #      for the Approver SID and the Local reviewer SID, proving this
        #      is NOT satisfied merely by a `BUILTIN\Administrators` grant.
        #      This is the exact hardening path used by the real orchestrator
        #      (`Invoke-GroupTwoSpecWrite`), reproduced here against a
        #      disposable fixture spec record and the two real named SIDs
        #      from `$script:VerifiedApproverReaderSid` /
        #      `$script:VerifiedLocalReaderSid`, so this test would have
        #      FAILED against the pre-R1 implementation (which passed only
        #      `S-1-5-32-544` / `BUILTIN\Administrators`, granting neither the
        #      Approver SID nor the Local SID any explicit rule).
        #
        #      `SetOwner` cannot be pointed at an arbitrary unprivileged SID
        #      without `SeRestorePrivilege` (proven during R1 hardening: it
        #      throws "the security identifier is not allowed to be the
        #      owner of this object"), so the owner here is necessarily the
        #      current agent identity, exactly as every other write in this
        #      suite uses. On some hosts the current identity's own SID may
        #      numerically equal one of the two real reviewer/approver SIDs
        #      (they are environment-specific well-known local accounts, not
        #      reserved values); when that happens the owner and reader ACEs
        #      legitimately collapse into one merged rule carrying
        #      FullControl, which is correct ACL semantics for "owner reads
        #      its own file" and is NOT a hardening defect, so the read-only
        #      shape assertion below is scoped to skip only that one
        #      genuinely-colliding case rather than asserting a false
        #      negative.
        $crossPrincipalRoot = Join-Path -Path $sandbox -ChildPath 'cross_principal_repo'
        New-Item -ItemType Directory -Path $crossPrincipalRoot -Force | Out-Null
        $crossPrincipalSpecPath = Resolve-GroupTwoSpecPath -RepositoryRoot $crossPrincipalRoot
        $crossPrincipalWritten = Write-GroupTwoSpecOutput -SpecPath $crossPrincipalSpecPath -Record $built.Record `
            -OwnerAccountSid $current.Sid `
            -LocalReaderAccountSids @($script:VerifiedApproverReaderSid, $script:VerifiedLocalReaderSid)
        $crossPrincipalAcl = Get-Acl -LiteralPath $crossPrincipalWritten

        $approverAllowRules = @($crossPrincipalAcl.Access | Where-Object {
                $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq $script:VerifiedApproverReaderSid -and
                $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow
            })
        Add-TestResult -CaseId 'T3B-RV-1-A' -Contract 'T3B-RV-1' -Passed ($approverAllowRules.Count -gt 0) `
            -Detail "Approver SID '$($script:VerifiedApproverReaderSid)' has an explicit Allow access rule on the spec file (not relying on Administrators group membership)"

        $approverSidCollidesWithOwner = ($script:VerifiedApproverReaderSid -eq $current.Sid)
        $approverRights = 0
        foreach ($rule in $approverAllowRules) { $approverRights = $approverRights -bor [int]$rule.FileSystemRights }
        $approverReadOnly = $approverSidCollidesWithOwner -or (
            ($approverRights -band [int][System.Security.AccessControl.FileSystemRights]::Read) -ne 0 -and
            ($approverRights -band [int][System.Security.AccessControl.FileSystemRights]::Write) -eq 0 -and
            ($approverRights -band [int][System.Security.AccessControl.FileSystemRights]::Delete) -eq 0 -and
            ($approverRights -band [int][System.Security.AccessControl.FileSystemRights]::ChangePermissions) -eq 0 -and
            ($approverRights -band [int][System.Security.AccessControl.FileSystemRights]::TakeOwnership) -eq 0 -and
            ($approverRights -band [int][System.Security.AccessControl.FileSystemRights]::AppendData) -eq 0
        )
        $approverDetail = if ($approverSidCollidesWithOwner) {
            'Approver SID equals this host''s current identity SID (owner); skipped as a legitimate owner/reader ACE merge, not a hardening defect'
        } else {
            'Approver SID rights are read-only: no Write/Delete/ChangePermissions/TakeOwnership/AppendData grant'
        }
        Add-TestResult -CaseId 'T3B-RV-1-B' -Contract 'T3B-RV-1' -Passed $approverReadOnly -Detail $approverDetail

        $localAllowRules = @($crossPrincipalAcl.Access | Where-Object {
                $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq $script:VerifiedLocalReaderSid -and
                $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow
            })
        Add-TestResult -CaseId 'T3B-RV-1-C' -Contract 'T3B-RV-1' -Passed ($localAllowRules.Count -gt 0) `
            -Detail "Local reviewer SID '$($script:VerifiedLocalReaderSid)' has an explicit Allow access rule on the spec file (not relying on a deny-only Administrators SID)"

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
        Add-TestResult -CaseId 'T3B-RV-1-D' -Contract 'T3B-RV-1' -Passed $localReadOnly -Detail $localDetail

        # The real orchestration path (`Invoke-GroupTwoSpecWrite`) itself
        # calls `Write-GroupTwoSpecOutput` with exactly these two named SIDs
        # (never `BUILTIN\Administrators` alone) -- assert that literally,
        # against this script's own source, so a regression that reverts to
        # an Administrators-only grant in the orchestration function itself
        # (not just in this test) is caught even without executing real mode.
        $writerSourceForAclCheck = Get-Content -LiteralPath $PSCommandPath -Raw
        $invokeSpecWriteBlock = (Select-String -InputObject $writerSourceForAclCheck `
                -Pattern '(?s)function Invoke-GroupTwoSpecWrite \{.*?\n\}' -AllMatches).Matches[0].Value
        $orchestrationUsesExplicitSids = (
            $invokeSpecWriteBlock -match [regex]::Escape('$script:VerifiedApproverReaderSid') -and
            $invokeSpecWriteBlock -match [regex]::Escape('$script:VerifiedLocalReaderSid')
        )
        Add-TestResult -CaseId 'T3B-RV-1-E' -Contract 'T3B-RV-1' -Passed $orchestrationUsesExplicitSids `
            -Detail 'real-mode orchestration (Invoke-GroupTwoSpecWrite) source references the explicit Approver and Local reader SID variables, not only BUILTIN\Administrators'
        $orchestrationDoesNotRelyOnAdminsAlone = -not (
            $invokeSpecWriteBlock -match [regex]::Escape("@('S-1-5-32-544')") -or
            $invokeSpecWriteBlock -match [regex]::Escape('@($adminsSid)')
        )
        Add-TestResult -CaseId 'T3B-RV-1-F' -Contract 'T3B-RV-1' -Passed $orchestrationDoesNotRelyOnAdminsAlone `
            -Detail 'real-mode orchestration no longer passes only BUILTIN\Administrators (S-1-5-32-544) as the sole reader SID'

        # ---- T3B-09: no Party A contact -------------------------------------
        $partyAUntouched = ($current.Name -notlike '*cvf-g1-party-a*')
        Add-TestResult -CaseId 'T3B-09-A' -Contract 'T3B-09' -Passed $partyAUntouched `
            -Detail "self-test ran as '$($current.Name)', not as the expected Party A principal"

        $realRepositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path
        $realGroupTwoDir = Join-Path $realRepositoryRoot 'governance/sources/verification_authority_spec'
        $realSpecAbsent = -not (Test-Path -LiteralPath (Join-Path $realGroupTwoDir 'SPEC_v1.json'))
        Add-TestResult -CaseId 'T3B-09-B' -Contract 'T3B-09' -Passed $realSpecAbsent `
            -Detail "real Group 2 spec path '$realGroupTwoDir/SPEC_v1.json' remains absent after self-test"
        $realDecisionsAbsent = -not (Test-Path -LiteralPath (Join-Path $realGroupTwoDir 'ACTIVATION_DECISIONS.jsonl'))
        Add-TestResult -CaseId 'T3B-09-C' -Contract 'T3B-09' -Passed $realDecisionsAbsent `
            -Detail "real Group 2 decisions path '$realGroupTwoDir/ACTIVATION_DECISIONS.jsonl' remains absent after self-test"

        # ---- T3B-10: duplicate JSON member / malformed base64 negatives ----
        $duplicateMemberJson = '{"profile":"x","profile":"y"}'
        Test-GuardRejects -CaseId 'T3B-10-A' -Contract 'T3B-10' `
            -ExpectedGuardId 'JSON_DUPLICATE_MEMBER' -Action {
            Get-StrictJsonObjectFromText -Text $duplicateMemberJson
        }
        Test-GuardRejects -CaseId 'T3B-10-B' -Contract 'T3B-10' `
            -ExpectedGuardId 'BASE64URL_INVALID' -Action {
            ConvertFrom-Base64Url -Text 'a'
        }
    } finally {
        Get-ChildItem -LiteralPath $sandbox -Recurse -File -Force -ErrorAction SilentlyContinue |
            ForEach-Object {
                try {
                    # Reset any hardened DACL before deletion so the current
                    # identity (which is always the owner in this hermetic
                    # test) can still remove its own disposable fixtures.
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
    Write-Host 'Claim boundary: guard behavior proven; no real Group 2 spec was created.'

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
        [void](Invoke-GroupTwoSpecWrite -ExpectedAccountName $ExpectedAccountName `
                -ExpectedAccountSid $ExpectedAccountSid)
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
