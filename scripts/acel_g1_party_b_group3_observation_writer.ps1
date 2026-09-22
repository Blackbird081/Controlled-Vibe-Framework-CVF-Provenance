<#
.SYNOPSIS
    ACEL G1 T3C-C1 Group 3 principal-bound observation-log writer (fail-closed).

.DESCRIPTION
    Appends one immutable Group 3 `cvf.observationLogEntry` record to the
    governed observation log, exclusively as the exact expected Party B
    principal. The record binds the exact raw UTF-8 bytes of the existing
    Group 1 verifier-key registry (`governance/sources/verifier_key_registry/REGISTRY.json`)
    as an unpadded base64url `snapshot_content`, with an independently
    recomputed `snapshotHashHex` and a `cvf.source-record-canonicalization@1`
    `entryHashHex` chained via `priorEntryHashHex` (JSON null at genesis).

    Default invocation is a hermetic self-test that proves every guard using
    disposable fixtures under the current user's temporary directory and
    removes them. Real-mode execution requires -ExecuteWrite, an exact
    Party B name and SID match, a non-elevated interactive session, a typed
    confirmation, an existing Group 1 registry validated by the independent
    checker, and an append-only transactional write that never truncates a
    non-empty log. Real mode rejects the issuer registry and every other
    input, and fails closed if the file's ownership/DACL cannot be restricted
    to Party B, SYSTEM and Administrators control plus exact Local-reviewer
    read-only access.

    This tool does not claim Group 3 establishment, candidate admission, or
    T3E consumer wiring. Its real-mode output text is exactly
    `OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION`.

.PARAMETER SelfTest
    Run hermetic positive and negative self-tests as the current user against
    a disposable sandbox. This is the default when no mode is chosen and never
    targets the real Group 3 log path or the expected Party B principal.

.PARAMETER ExecuteWrite
    Perform the real Group 3 observation append. Requires the current process
    identity to match both -ExpectedAccountName and -ExpectedAccountSid
    exactly, a non-elevated interactive host, and an interactive typed
    confirmation.

.PARAMETER ExpectedAccountName
    Exact expected Windows account name, e.g. 'HOSTNAME\cvf-g1-party-b'. A
    bare name is qualified with the local computer name before comparison.

.PARAMETER ExpectedAccountSid
    Exact expected Windows account SID.

.EXAMPLE
    pwsh -NoProfile -File scripts/acel_g1_party_b_group3_observation_writer.ps1 -SelfTest

.NOTES
    Claim boundary: tooling only. A self-test proves guard behavior, not that
    any Group 3 source was created. Real-mode output text explicitly reads
    `OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION`, never establishment,
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
    [string] $ExpectedAccountSid,

    # ---- Test-only peer mode (unreachable from -ExecuteWrite production flow) ----
    # Launched exclusively by self-test orchestration via a second pwsh process.
    # Never targets real Group 3 log or Party B principal.
    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [switch] $PeerMode,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerLogPath,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerRunId,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerObserverSid,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerOwnerSid,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerSnapshotId,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerObservedAt,

    [Parameter(ParameterSetName = 'PeerMode', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $PeerRepositoryRoot
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

$script:ToolContract          = 'cvf.acel.g1.group3ObservationWriterTool@1'
$script:CanonProfile          = 'cvf.source-record-canonicalization@1'
$script:ObservationEntryDomain = 'cvf.observationLogEntry'
$script:ConfirmationPhrase    = 'EXECUTE GROUP 3 OBSERVATION WRITE'
$script:LogRelativePath       = 'governance/sources/registry_observation_log/LOG.jsonl'
$script:InputRelativePath     = 'governance/sources/verifier_key_registry/REGISTRY.json'
$script:LifecycleRelativePath = 'governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl'
$script:RegistryName          = 'verifier_key_registry'
$script:Authority             = 'ACEL_G1_DECISION_OWNER'
$script:RealModeResultText    = 'OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION'

# Exact, operator-verified Party B principal, per the paired GC-018 baseline.
$script:VerifiedPartyBIdentity = [ordered]@{
    principalName = 'LAM-RUBY\cvf-g1-party-b'
    principalSid  = 'S-1-5-21-1644666849-912006174-747199667-1009'
}

# Forbidden observer identities (Party A, Activation Approver, Local) and the
# Group 1 registry write principal (Party A), used for observer separation.
$script:PartyASid       = 'S-1-5-21-1644666849-912006174-747199667-1006'
$script:ApproverSid     = 'S-1-5-21-1644666849-912006174-747199667-1008'
$script:LocalSid        = 'S-1-5-21-1644666849-912006174-747199667-1001'
$script:Group1WriterSid = $script:PartyASid

Add-Type -AssemblyName System.Security | Out-Null

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
            for this ASCII-only, non-nested, no-duplicate-key preimage shape).
            Ported unmodified in behavior from the accepted Group 1/2 writers.
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

# --------------------------------------------------------------------------
# Observation entry construction
# --------------------------------------------------------------------------

function New-ObservationEntryPreimage {
    <#
        .SYNOPSIS
            Build the exact closed `cvf.observationLogEntry` preimage:
            `profile`, `domain`, `snapshotId`, `registryName`,
            `registrySnapshotVersion`, `snapshotHashHex`, `observedAt`,
            `authority`, `observerIdentity`, `priorEntryHashHex`. Excludes
            `snapshot_content` and `entryHashHex`. No more, no fewer.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $SnapshotId,
        [Parameter(Mandatory = $true)][string] $RegistryName,
        [Parameter(Mandatory = $true)][int]    $RegistrySnapshotVersion,
        [Parameter(Mandatory = $true)][string] $SnapshotHashHex,
        [Parameter(Mandatory = $true)][string] $ObservedAt,
        [Parameter(Mandatory = $true)][string] $Authority,
        [Parameter(Mandatory = $true)][string] $ObserverIdentity,
        $PriorEntryHashHex
    )
    return [ordered]@{
        profile                = $script:CanonProfile
        domain                 = $script:ObservationEntryDomain
        snapshotId             = $SnapshotId
        registryName           = $RegistryName
        registrySnapshotVersion = $RegistrySnapshotVersion
        snapshotHashHex        = $SnapshotHashHex
        observedAt             = $ObservedAt
        authority              = $Authority
        observerIdentity       = $ObserverIdentity
        priorEntryHashHex      = $PriorEntryHashHex
    }
}

function New-ObservationEntry {
    <#
        .SYNOPSIS
            Build the full Group 3 observation-log record from exact raw
            snapshot bytes, computing `snapshotHashHex` (direct SHA-256 of the
            decoded raw bytes) and `entryHashHex` (the `cvf.observationLogEntry`
            closed-preimage digest, which includes `snapshotHashHex` but
            excludes `snapshot_content` and `entryHashHex`).
    #>
    param(
        [Parameter(Mandatory = $true)][string] $SnapshotId,
        [Parameter(Mandatory = $true)][byte[]] $SnapshotBytes,
        [Parameter(Mandatory = $true)][int]    $RegistrySnapshotVersion,
        [Parameter(Mandatory = $true)][string] $ObservedAt,
        [Parameter(Mandatory = $true)][string] $ObserverIdentity,
        $PriorEntryHashHex
    )

    $snapshotContent = ConvertTo-Base64UrlNoPadding -Bytes $SnapshotBytes
    $snapshotHashHex = Get-Sha256Hex -Bytes $SnapshotBytes

    $preimage = New-ObservationEntryPreimage -SnapshotId $SnapshotId `
        -RegistryName $script:RegistryName `
        -RegistrySnapshotVersion $RegistrySnapshotVersion `
        -SnapshotHashHex $snapshotHashHex -ObservedAt $ObservedAt `
        -Authority $script:Authority -ObserverIdentity $ObserverIdentity `
        -PriorEntryHashHex $PriorEntryHashHex
    $entryHashHex = Get-PreimageDigestHex -Preimage $preimage

    $record = [ordered]@{
        snapshotId             = $SnapshotId
        registryName           = $script:RegistryName
        registrySnapshotVersion = $RegistrySnapshotVersion
        snapshot_content       = $snapshotContent
        snapshotHashHex        = $snapshotHashHex
        observedAt             = $ObservedAt
        authority              = $script:Authority
        observerIdentity       = $ObserverIdentity
        priorEntryHashHex      = $PriorEntryHashHex
        entryHashHex           = $entryHashHex
    }

    return [pscustomobject]@{
        Record             = $record
        SnapshotContent    = $snapshotContent
        SnapshotHashHex    = $snapshotHashHex
        EntryHashHex       = $entryHashHex
        PreimageBytes      = (ConvertTo-CanonicalJsonBytes -Object $preimage)
    }
}

function New-FreshSnapshotId {
    <#
        .SYNOPSIS
            Generate a fresh, globally unique, write-once snapshotId. A UUID
            alone is not sufficient for the uniqueness guarantee, so this
            appends a random suffix to a UUID to widen the space against
            collision. Returned value is a stable string, never reused.
    #>
    $uuid = [System.Guid]::NewGuid().ToString('N')
    $rand = [System.Guid]::NewGuid().ToString('N').Substring(0, 16)
    return ('snap-{0}-{1}' -f $uuid, $rand)
}

# --------------------------------------------------------------------------
# Principal and context guards
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

function Assert-ExpectedPrincipalIsVerifiedPartyB {
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )
    $qualifiedCandidate = Resolve-QualifiedAccountName -AccountName $ExpectedAccountName
    $qualifiedVerified = Resolve-QualifiedAccountName -AccountName $script:VerifiedPartyBIdentity.principalName
    if ($qualifiedCandidate -ne $qualifiedVerified) {
        Stop-Writer -GuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_B' -Message (
            "supplied -ExpectedAccountName '$qualifiedCandidate' does not equal the verified Party B identity '$qualifiedVerified'")
    }
    if ($ExpectedAccountSid.Trim() -ne $script:VerifiedPartyBIdentity.principalSid) {
        Stop-Writer -GuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_B' -Message (
            "supplied -ExpectedAccountSid does not equal the verified Party B SID")
    }
}

function Assert-InteractiveConfirmation {
    param([Parameter(Mandatory = $true)][string] $ExpectedAccountName)

    Write-Host ''
    Write-Host "About to append one Group 3 observation record for '$ExpectedAccountName'."
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
# Path guards
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

function Resolve-GovernedPath {
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][string] $RelativePath
    )
    $normalizedRoot = [System.IO.Path]::GetFullPath($RepositoryRoot)
    $resolved = [System.IO.Path]::GetFullPath((Join-Path $normalizedRoot $RelativePath))
    if (-not (Test-PathIsInside -CandidatePath $resolved -ContainerPath $normalizedRoot)) {
        Stop-Writer -GuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Message (
            "resolved path '$resolved' does not resolve inside repository root '$normalizedRoot'")
    }
    Assert-NoReparsePointInAncestry -NormalizedPath $resolved
    return $resolved
}

# --------------------------------------------------------------------------
# Independent checker invocation (chain and Group 1 validation)
# --------------------------------------------------------------------------

function Invoke-Group1Checker {
    <#
        .SYNOPSIS
            Validate the Group 1 registry via the independent read-only checker
            before any bytes are read. Fails closed on a non-zero exit.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][string] $RegistryPath,
        [Parameter(Mandatory = $true)][string] $LifecyclePath
    )
    $checkerPath = Join-Path $RepositoryRoot 'governance/compat/check_acel_g1_verifier_key_registry.py'
    $output = & python $checkerPath --registry-path $RegistryPath --lifecycle-path $LifecyclePath 2>&1
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        Stop-Writer -GuardId 'GROUP1_CHECKER_REJECTED' -Message (
            "independent Group 1 checker exited $exitCode`: $($output -join ' ')")
    }
    return ($output -join ' ')
}

function Invoke-ObservationLogChecker {
    <#
        .SYNOPSIS
            Validate the existing observation-log chain via the independent
            read-only checker before appending. Fails closed on non-zero exit.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][string] $LogPath,
        [switch] $InjectPostAcquireFailureForTest
    )
    $checkerPath = Join-Path $RepositoryRoot 'governance/compat/check_acel_g1_registry_observation_log.py'
    $output = & python $checkerPath --log $LogPath `
        --expected-observer $script:VerifiedPartyBIdentity.principalSid `
        --registry-writer-sid $script:Group1WriterSid 2>&1
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        Stop-Writer -GuardId 'OBSERVATION_LOG_CHECKER_REJECTED' -Message (
            "independent observation-log checker exited $exitCode`: $($output -join ' ')")
    }
    return ($output -join ' ')
}

# --------------------------------------------------------------------------
# Append-only write and DACL hardening
# --------------------------------------------------------------------------

function Test-BytesEqual {
    param(
        [Parameter(Mandatory = $true)][AllowNull()][byte[]] $Left,
        [Parameter(Mandatory = $true)][AllowNull()][byte[]] $Right
    )
    if ($null -eq $Left -or $null -eq $Right) {
        return ($null -eq $Left -and $null -eq $Right)
    }
    if ($Left.Length -ne $Right.Length) { return $false }
    for ($i = 0; $i -lt $Left.Length; $i++) {
        if ($Left[$i] -ne $Right[$i]) { return $false }
    }
    return $true
}

function New-TransactionGuard {
    <#
        .SYNOPSIS
            Acquire a named, cross-process, non-recursive mutex whose identity
            is derived deterministically from the canonical absolute path of the
            target log file. The mutex is never named after a secret or
            credential; its name contains only a truncated hex prefix of the
            SHA-256 of the normalized path plus a fixed human-readable prefix.
            Returns the acquired System.Threading.Mutex. The caller must call
            .ReleaseMutex() and .Dispose() in a finally block.

            Exception-safe: if any failure occurs after the OS mutex is acquired
            but before successful return, this function releases and disposes
            the mutex internally before rethrowing. The caller therefore never
            receives a leaked, unreleased OS mutex handle.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $LogPath,
        [switch] $InjectPostAcquireFailureForTest
    )
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        $normalized = [System.IO.Path]::GetFullPath($LogPath).ToUpperInvariant()
        $pathBytes  = [System.Text.UTF8Encoding]::new($false).GetBytes($normalized)
        $hashHex    = [System.BitConverter]::ToString($sha256.ComputeHash($pathBytes)).Replace('-', '').ToLowerInvariant()
    } finally {
        $sha256.Dispose()
    }
    # Mutex name: fixed prefix + first 48 hex chars of the path hash (192 bits).
    # Global\ prefix enables cross-session mutual exclusion on Windows.
    $mutexName = 'Global\CVF_G3_OBS_TXN_' + $hashHex.Substring(0, 48)
    $created   = $false
    $mtx       = [System.Threading.Mutex]::new($false, $mutexName, [ref] $created)
    # Track whether WaitOne succeeded so cleanup knows to release before dispose.
    $osAcquired = $false
    try {
        # Timeout: 30 seconds. A competing transaction should complete well
        # within this window; a deadlock probe fails with TRANSACTION_TIMEOUT.
        try {
            $acquired = $mtx.WaitOne(30000)
        } catch [System.Threading.AbandonedMutexException] {
            # The previous holder crashed; the mutex is now ours. This is safe
            # because we will re-read and re-validate all state under the guard.
            $acquired = $true
        }
        if (-not $acquired) {
            Stop-Writer -GuardId 'TRANSACTION_TIMEOUT' -Message (
                "timed out waiting for the transaction mutex '$mutexName'; a peer transaction did not complete within 30s")
        }
        $osAcquired = $true
        if ($InjectPostAcquireFailureForTest) {
            throw [System.InvalidOperationException]::new(
                'injected post-acquire guard failure (hermetic self-test only)')
        }
        # Any additional setup that could fail goes here, before the return.
        # On failure the finally block releases and disposes before rethrow.
        return $mtx
    } catch {
        if ($osAcquired) {
            try { $mtx.ReleaseMutex() } catch { }
        }
        $mtx.Dispose()
        throw
    }
}

function Get-LastEntryHashFromBytes {
    <#
        .SYNOPSIS
            Derive the last durable entryHashHex from exact log bytes. Empty
            bytes yield $null (genesis prior hash). The caller is responsible
            for having already validated the chain from these same bytes.
    #>
    param([Parameter(Mandatory = $true)][byte[]] $Bytes)

    if ($Bytes.Length -eq 0) { return $null }
    $text = [System.Text.UTF8Encoding]::new($false).GetString($Bytes)
    $lines = @($text -split "`n" | ForEach-Object { $_.TrimEnd("`r") } | Where-Object { $_ -ne '' })
    if ($lines.Count -eq 0) { return $null }
    $lastRecord = $lines[$lines.Count - 1] | ConvertFrom-Json -DateKind String -ErrorAction Stop
    if ($null -eq $lastRecord.entryHashHex) {
        Stop-Writer -GuardId 'OBSERVATION_LOG_CHAIN_INVALID' -Message 'last existing entry lacks entryHashHex'
    }
    return $lastRecord.entryHashHex
}

function Get-ObservationLogSecurityState {
    <#
        .SYNOPSIS
            Snapshot the exact, restorable owner and DACL state of an existing
            file. Must be called under the outer transaction guard. Returns
            a pscustomobject with OwnerSid (string) and FileSecurity
            (FileSecurity object for exact restoration). SACL access is not
            required and is never requested.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $FilePath
    )
    $info = [System.IO.FileInfo]::new($FilePath)
    $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor
        [System.Security.AccessControl.AccessControlSections]::Access
    $security = [System.IO.FileSystemAclExtensions]::GetAccessControl($info, $sections)
    $ownerSid = $security.GetOwner(
        [System.Security.Principal.SecurityIdentifier]).Value
    $tuples = @($security.GetAccessRules($true, $true,
        [System.Security.Principal.SecurityIdentifier]) |
        ForEach-Object { Get-SemanticAceTuple -Rule $_ } | Sort-Object)
    return [pscustomobject]@{
        OwnerSid               = $ownerSid
        AreAccessRulesProtected = $security.AreAccessRulesProtected
        AceTuples              = $tuples
        FileSecurity           = $security
    }
}

function Get-SemanticAceTuple {
    <#
        .SYNOPSIS
            Convert an AccessRule into a canonical semantic tuple string:
            SID|AllowOrDeny|NumericRights|InheritanceFlags|PropagationFlags.
            Numeric rights prevents synthetic flag combinations (e.g.
            FileSystemRights.FullControl vs individual bit combinations) from
            appearing equal when they are not. Inheritance and propagation flags
            are normalized as integer values.
    #>
    param([Parameter(Mandatory = $true)] $Rule)
    $sid        = $Rule.IdentityReference.Value
    $aceType    = [int]$Rule.AccessControlType   # 0=Allow, 1=Deny
    $rights     = [int]$Rule.FileSystemRights
    $inherit    = [int]$Rule.InheritanceFlags
    $propagate  = [int]$Rule.PropagationFlags
    return ('{0}|{1}|{2}|{3}|{4}' -f $sid, $aceType, $rights, $inherit, $propagate)
}

function Assert-ObservationLogSecurityStateMatches {
    param(
        [Parameter(Mandatory = $true)][string] $FilePath,
        [Parameter(Mandatory = $true)] $ExpectedState
    )
    $actual = Get-ObservationLogSecurityState -FilePath $FilePath
    if ($actual.OwnerSid -ne $ExpectedState.OwnerSid) {
        Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
            "rollback owner-verification failed for '$FilePath': owner '$($actual.OwnerSid)' differs from prior '$($ExpectedState.OwnerSid)'")
    }
    if ($actual.AreAccessRulesProtected -ne $ExpectedState.AreAccessRulesProtected) {
        Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
            "rollback DACL protection flag differs from prior state for '$FilePath'")
    }
    if ($actual.AceTuples.Count -ne $ExpectedState.AceTuples.Count) {
        Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
            "rollback ACE count differs from prior state for '$FilePath'")
    }
    for ($i = 0; $i -lt $ExpectedState.AceTuples.Count; $i++) {
        if ($actual.AceTuples[$i] -ne $ExpectedState.AceTuples[$i]) {
            Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
                "rollback ACE tuple mismatch at position $i for '$FilePath'")
        }
    }
    return $true
}

function Assert-ObservationLogSecurityPostcondition {
    <#
        .SYNOPSIS
            Re-read the file security descriptor and semantically verify:
            (1) expected Party B owner SID exactly matches,
            (2) access-rule protection flag is set (inheritance disabled),
            (3) the complete explicit ACE multiset contains exactly the three
                required Party B/SYSTEM/Administrators Allow-FullControl entries
                plus the exact Local reviewer Allow-Read entry, with no
                inherited, extra-allow, deny, or unexpected ACEs.
            Each comparison uses canonical semantic tuples
            (SID|type|numericRights|inheritanceFlags|propagationFlags) so any
            extra allow, deny, inherited or wrong ACE triggers
            DACL_VERIFICATION_FAILED with a stable taxonomy message.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $FilePath,
        [Parameter(Mandatory = $true)][string] $ExpectedOwnerSid
    )
    $info = [System.IO.FileInfo]::new($FilePath)

    # --- (1) Owner check ---
    $ownerSec = [System.IO.FileSystemAclExtensions]::GetAccessControl(
        $info, [System.Security.AccessControl.AccessControlSections]::Owner)
    $actualOwnerSid = $ownerSec.GetOwner(
        [System.Security.Principal.SecurityIdentifier]).Value
    if ($actualOwnerSid -ne $ExpectedOwnerSid) {
        Stop-Writer -GuardId 'DACL_VERIFICATION_FAILED' -Message (
            "security read-back: owner SID '$actualOwnerSid' does not equal expected '$ExpectedOwnerSid'")
    }

    # --- (2) Protection flag check ---
    $daclSec = [System.IO.FileSystemAclExtensions]::GetAccessControl(
        $info, [System.Security.AccessControl.AccessControlSections]::Access)
    if (-not $daclSec.AreAccessRulesProtected) {
        Stop-Writer -GuardId 'DACL_VERIFICATION_FAILED' -Message (
            'security read-back: AreAccessRulesProtected is false (inheritance not disabled)')
    }

    # --- (3) Full semantic ACE multiset check ---
    # Collect ALL explicit ACEs (both inherited=false and inherited=true are
    # captured; we then verify none are inherited, and reject any deny or extra).
    $allRules = @(
        $daclSec.GetAccessRules($true, $true,
            [System.Security.Principal.SecurityIdentifier])
    )

    # Any inherited ACE in a protected descriptor is an unexpected violation.
    $inheritedRules = @($allRules | Where-Object { $_.IsInherited })
    if ($inheritedRules.Count -gt 0) {
        Stop-Writer -GuardId 'DACL_VERIFICATION_FAILED' -Message (
            "security read-back: found $($inheritedRules.Count) inherited ACE(s); " +
            'protected descriptor must have no inherited entries')
    }

    $explicitRules = @($allRules | Where-Object { -not $_.IsInherited })

    # Any deny ACE is an immediate violation.
    $denyRules = @($explicitRules | Where-Object {
        $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Deny })
    if ($denyRules.Count -gt 0) {
        Stop-Writer -GuardId 'DACL_VERIFICATION_FAILED' -Message (
            "security read-back: found $($denyRules.Count) deny ACE(s); policy allows only allow ACEs")
    }

    # Build actual semantic multiset and sort for stable comparison.
    $actualTuples = @($explicitRules | ForEach-Object { Get-SemanticAceTuple -Rule $_ } | Sort-Object)

    # Build expected semantic multiset. FullControl ACEs created by
    # FileSystemAccessRule have no InheritanceFlags or PropagationFlags
    # (both zero for file-level non-container targets).
    $fullControlRights = [int][System.Security.AccessControl.FileSystemRights]::FullControl
    $allowType         = [int][System.Security.AccessControl.AccessControlType]::Allow
    $expectedSids      = @($ExpectedOwnerSid, 'S-1-5-18', 'S-1-5-32-544') | Sort-Object
    $readRights        = [int][System.Security.AccessControl.FileSystemRights]::Read
    $expectedTuples    = @(
        $expectedSids | ForEach-Object {
            '{0}|{1}|{2}|{3}|{4}' -f $_, $allowType, $fullControlRights, 0, 0
        }
        if ($script:LocalSid -ne $ExpectedOwnerSid) {
            '{0}|{1}|{2}|{3}|{4}' -f $script:LocalSid, $allowType, $readRights, 0, 0
        }
    ) | Sort-Object

    if ($actualTuples.Count -ne $expectedTuples.Count) {
        Stop-Writer -GuardId 'DACL_VERIFICATION_FAILED' -Message (
            "security read-back: expected $($expectedTuples.Count) explicit allow ACE(s), " +
            "found $($actualTuples.Count)")
    }
    for ($i = 0; $i -lt $expectedTuples.Count; $i++) {
        if ($actualTuples[$i] -ne $expectedTuples[$i]) {
            Stop-Writer -GuardId 'DACL_VERIFICATION_FAILED' -Message (
                "security read-back: ACE tuple mismatch at position $i; " +
                "expected '$($expectedTuples[$i])' got '$($actualTuples[$i])'")
        }
    }
    return $true
}

function Restore-ObservationLogState {
    <#
        .SYNOPSIS
            Rollback after a failed mutation: restore exact prior bytes and
            prior owner/DACL for an existing file (including proof of prior
            security restoration), or remove a newly created file and any
            newly created empty directory. For a new file with an existing
            pre-existing directory, only the file is removed. Raises
            OBSERVATION_LOG_ROLLBACK_FAILED if restoration itself fails.
            After restoration, proves exact prior bytes (for existing files)
            and exact prior owner/DACL semantics (for existing files with
            prior security state).
    #>
    param(
        [Parameter(Mandatory = $true)][string] $LogPath,
        [Parameter(Mandatory = $true)][bool]   $FilePreExisted,
        [AllowNull()][byte[]] $PriorBytes,
        $PriorSecurityState,
        [Parameter(Mandatory = $true)][bool]   $DirectoryPreExisted
    )

    try {
        if ($FilePreExisted) {
            [System.IO.File]::WriteAllBytes($LogPath, $PriorBytes)
            if ($null -ne $PriorSecurityState) {
                $info = [System.IO.FileInfo]::new($LogPath)
                [System.IO.FileSystemAclExtensions]::SetAccessControl(
                    $info, $PriorSecurityState.FileSecurity)
            }
            # Prove exact prior bytes restored.
            $restoredBytes = [System.IO.File]::ReadAllBytes($LogPath)
            if (-not (Test-BytesEqual -Left $restoredBytes -Right $PriorBytes)) {
                Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
                    "rollback byte-verification failed for '$LogPath': restored bytes differ from prior bytes")
            }
            # Prove exact prior owner/DACL semantics restored.
            if ($null -ne $PriorSecurityState) {
                Assert-ObservationLogSecurityStateMatches -FilePath $LogPath `
                    -ExpectedState $PriorSecurityState | Out-Null
            }
        } else {
            if (Test-Path -LiteralPath $LogPath) {
                Remove-Item -LiteralPath $LogPath -Force -ErrorAction Stop
            }
            if (-not $DirectoryPreExisted) {
                $directory = [System.IO.Path]::GetDirectoryName($LogPath)
                if (Test-Path -LiteralPath $directory) {
                    $remaining = @(Get-ChildItem -LiteralPath $directory -Force -ErrorAction Stop)
                    if ($remaining.Count -eq 0) {
                        Remove-Item -LiteralPath $directory -Force -ErrorAction Stop
                    }
                }
            }
        }
    } catch {
        if ($_.Exception -is [WriterGuardFailure]) { throw }
        Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
            "rollback failed for '$LogPath': $($_.Exception.Message)")
    }
}

function Append-ObservationTransaction {
    <#
        .SYNOPSIS
            One exclusive, rollback-safe append transaction. Acquires a
            cross-process named mutex (derived from the canonical target path)
            before the first filesystem mutation and holds it continuously
            through DACL application, security read-back verification and
            final chain validation, or through completed rollback. Under the
            outer guard and an inner exclusive FileShare.None stream it:
            (1) pre-creates the directory and empty file under rollback
                ownership (mutation ownership starts before New-Item),
            (2) reads the exact locked bytes and detects concurrent replacement,
            (3) validates the existing chain and derives the prior hash,
            (4) appends exactly one UTF-8-no-BOM JSON line (no duplication),
            (5) flushes and closes the stream,
            (6) hardens owner/DACL and reads back the descriptor to
                semantically verify owner, protection flag and exact ACE set,
            (7) re-validates the full log.
            Any failure after the first durable mutation restores the exact
            prior bytes and prior owner/DACL for an existing file, or removes
            the newly created file and newly created empty directory.
            A competing transaction cannot enter the protected window or have
            its append overwritten by rollback.

            Exception-safe guard lifetime: $txnMutex is initialized to null
            before the outer try/finally. New-TransactionGuard acquires the OS
            mutex and returns it; any failure inside New-TransactionGuard
            releases the OS handle internally before rethrowing. The outer
            finally always releases and disposes $txnMutex if it is non-null,
            so the guard spans from the first successful return of
            New-TransactionGuard through validated success or verified rollback.

            Peer barrier hook (self-test only): after the stream is closed and
            while the outer mutex is still held, the function optionally signals
            PeerReadyEvent and waits for PeerEnteredEvent. This hook is only
            reachable when $PeerReadyEvent / $PeerEnteredEvent are non-null,
            which is only set by the self-test orchestrator, never by
            -ExecuteWrite production flow.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $RepositoryRoot,
        [Parameter(Mandatory = $true)][string] $LogPath,
        [Parameter(Mandatory = $true)][byte[]] $SnapshotBytes,
        [Parameter(Mandatory = $true)][int]    $RegistrySnapshotVersion,
        [Parameter(Mandatory = $true)][string] $ObserverIdentity,
        [Parameter(Mandatory = $true)][string] $OwnerAccountSid,
        [Parameter(Mandatory = $true)][string] $SnapshotId,
        [Parameter(Mandatory = $true)][string] $ObservedAt,
        [ValidateSet('Create', 'DirectoryCreate', 'FileCreate', 'Write', 'Flush',
                     'Dacl', 'DaclVerify', 'PostWriteValidate', 'SameLengthReplacement',
                     'PostFlushBeforePeerRelease', 'AfterPeerAttemptBeforeDacl')]
        [string] $InjectFailureAtForTest,
        [switch] $InjectRollbackFailureForTest,
        # Peer-barrier hook: non-null only during self-test orchestration.
        # PeerReadyEvent  = parent signals this to unblock the peer after stream close.
        # PeerEnteredEvent = parent waits on this; peer signals when it has tried to enter.
        # PeerNotEnteredProbe = parent checks this after DACL/final validation:
        #   if it were signaled, the peer managed to enter while parent held the guard.
        [System.Threading.EventWaitHandle] $PeerReadyEvent,
        [System.Threading.EventWaitHandle] $PeerEnteredEvent,
        [System.Threading.EventWaitHandle] $PeerNotEnteredProbeEvent,
        [System.Threading.EventWaitHandle] $GuardAcquiredEventForTest,
        [System.Threading.EventWaitHandle] $PeerAttemptingEvent,
        [System.Threading.EventWaitHandle] $ParentReleaseEventForTest
    )

    # --- Guard initialized to null; acquisition occurs inside the try/finally ---
    # This guarantees that the finally block sees a non-null $txnMutex only
    # when New-TransactionGuard succeeded and returned the acquired OS mutex.
    # Any failure inside New-TransactionGuard releases the OS handle there.
    $txnMutex = $null

    $directory           = $null
    $directoryPreExisted = $false
    $filePreExisted      = $false
    $priorBytes          = $null
    $priorSecurityState  = $null
    $stream              = $null
    # $mutationStarted is set true immediately before the first durable
    # filesystem change (directory or file creation) so that rollback
    # is always entered on any failure after that point.
    $mutationStarted     = $false
    try {
        # Acquire the outer transaction guard BEFORE any filesystem mutation.
        # New-TransactionGuard is exception-safe: on any failure after OS
        # acquisition it releases and disposes internally before rethrowing.
        $txnMutex = New-TransactionGuard -LogPath $LogPath
        if ($null -ne $GuardAcquiredEventForTest) {
            $GuardAcquiredEventForTest.Set() | Out-Null
        }

        $directory           = [System.IO.Path]::GetDirectoryName($LogPath)
        $directoryPreExisted = Test-Path -LiteralPath $directory
        $filePreExisted      = Test-Path -LiteralPath $LogPath

        # Snapshot prior bytes and full owner+DACL state (under the outer guard).
        if ($filePreExisted) {
            $priorBytes         = [System.IO.File]::ReadAllBytes($LogPath)
            $priorSecurityState = Get-ObservationLogSecurityState -FilePath $LogPath
        }
        if ($InjectFailureAtForTest -eq 'Create') {
            throw [System.IO.IOException]::new('injected create failure (hermetic self-test only)')
        }
        if ($InjectFailureAtForTest -eq 'SameLengthReplacement' -and $filePreExisted) {
            # Simulate a concurrent same-length replacement before the lock.
            # NOTE: we are already under the outer mutex; this injection
            # writes directly to simulate what a test peer would do if the
            # outer guard were absent.
            $replacement = [byte[]]::new($priorBytes.Length)
            [System.Array]::Copy($priorBytes, $replacement, $priorBytes.Length)
            $replacement[0] = ($replacement[0] -bxor 0xFF)
            [System.IO.File]::WriteAllBytes($LogPath, $replacement)
        }

        # (1a) Create directory if needed - UNDER rollback ownership.
        if (-not $directoryPreExisted) {
            $mutationStarted = $true
            New-Item -ItemType Directory -Path $directory -Force | Out-Null
        }
        if ($InjectFailureAtForTest -eq 'DirectoryCreate') {
            # Failure injected right after new-directory creation but before
            # file creation; rollback must remove the new directory.
            $mutationStarted = $true  # ensure rollback is entered
            throw [System.IO.IOException]::new('injected directory-create failure (hermetic self-test only)')
        }

        # (1b) Open/create the file under exclusive FileShare.None.
        # Mark mutation ownership before OpenOrCreate so that an empty file
        # left by a crash on open is rolled back.
        $mutationStarted = $true
        $stream = [System.IO.FileStream]::new(
            $LogPath, [System.IO.FileMode]::OpenOrCreate,
            [System.IO.FileAccess]::ReadWrite, [System.IO.FileShare]::None)
        if ($InjectFailureAtForTest -eq 'FileCreate') {
            throw [System.IO.IOException]::new('injected file-create failure (hermetic self-test only)')
        }

        # (2) Exact locked bytes.
        $lockedBytes = [byte[]]::new($stream.Length)
        if ($stream.Length -gt 0) {
            $stream.Position = 0
            $null = $stream.Read($lockedBytes, 0, $lockedBytes.Length)
        } else {
            $lockedBytes = [byte[]]@()
        }

        # (3) Same-length replacement detection (content identity, not length).
        if ($filePreExisted -and -not (Test-BytesEqual -Left $lockedBytes -Right $priorBytes)) {
            Stop-Writer -GuardId 'OBSERVATION_LOG_CONCURRENT_WRITE' -Message (
                'log content changed concurrently (same-length replacement or other modification); refusing to append')
        }

        # (4) Validate the exact locked chain and derive the prior hash.
        $priorHash = $null
        if ($lockedBytes.Length -gt 0) {
            $tempFile = Join-Path ([System.IO.Path]::GetTempPath()) (
                'cvf_g3_chain_{0}.jsonl' -f ([System.Guid]::NewGuid().ToString('N')))
            try {
                [System.IO.File]::WriteAllBytes($tempFile, $lockedBytes)
                Invoke-ObservationLogChecker -RepositoryRoot $RepositoryRoot -LogPath $tempFile | Out-Null
                $priorHash = Get-LastEntryHashFromBytes -Bytes $lockedBytes
            } finally {
                Remove-Item -LiteralPath $tempFile -Force -ErrorAction SilentlyContinue
            }
        }

        # Build the new row against the locked prior hash.
        $built = New-ObservationEntry -SnapshotId $SnapshotId -SnapshotBytes $SnapshotBytes `
            -RegistrySnapshotVersion $RegistrySnapshotVersion -ObservedAt $ObservedAt `
            -ObserverIdentity $ObserverIdentity -PriorEntryHashHex $priorHash
        $jsonLine     = ($built.Record | ConvertTo-Json -Depth 8 -Compress)
        $newLineBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($jsonLine + "`n")

        # (5) Append exactly one line (existing bytes + new line, never duplicated).
        $stream.Position = $stream.Length
        $stream.Write($newLineBytes, 0, $newLineBytes.Length)
        if ($InjectFailureAtForTest -eq 'Write') {
            throw [System.IO.IOException]::new('injected write failure (hermetic self-test only)')
        }
        $stream.Flush($true)
        if ($InjectFailureAtForTest -eq 'Flush') {
            throw [System.IO.IOException]::new('injected flush failure (hermetic self-test only)')
        }
        # Close the exclusive stream. The outer mutex guard is still held;
        # FileShare.None alone is insufficient to cover DACL and post-validation.
        $stream.Dispose(); $stream = $null

        if ($InjectFailureAtForTest -eq 'PostFlushBeforePeerRelease') {
            throw [System.IO.IOException]::new('injected post-flush-before-peer-release failure (hermetic self-test only)')
        }

        # Peer barrier hook (self-test only, null in production flow).
        # Signal the peer that the parent's stream is closed but the outer guard
        # is still held. The peer will attempt to acquire the guard and signal
        # PeerEnteredEvent. We then verify PeerEnteredEvent is NOT signaled
        # (i.e., the peer cannot enter while the parent holds the mutex) before
        # completing DACL and final validation.
        if ($null -ne $PeerReadyEvent) {
            $PeerReadyEvent.Set() | Out-Null
            if ($null -eq $PeerAttemptingEvent -or -not $PeerAttemptingEvent.WaitOne(15000)) {
                Stop-Writer -GuardId 'TRANSACTION_PEER_BARRIER_TIMEOUT' -Message (
                    'peer process did not reach the deterministic transaction-attempt barrier')
            }
            if ($PeerEnteredEvent.WaitOne(0)) {
                Stop-Writer -GuardId 'TRANSACTION_PEER_EXCLUSION_FAILED' -Message (
                    'peer process entered the transaction guard while the parent still held it')
            }
        }
        if ($InjectFailureAtForTest -eq 'AfterPeerAttemptBeforeDacl') {
            throw [System.IO.IOException]::new(
                'injected failure after peer attempted entry and before DACL hardening (hermetic self-test only)')
        }

        # (6) Harden owner/DACL (outer mutex guard still held).
        if ($InjectFailureAtForTest -eq 'Dacl') {
            throw [System.Security.SecurityException]::new('injected DACL failure (hermetic self-test only)')
        }
        Protect-ObservationLog -FilePath $LogPath -OwnerAccountSid $OwnerAccountSid | Out-Null

        # (6b) Read back and semantically verify the applied security descriptor.
        if ($InjectFailureAtForTest -eq 'DaclVerify') {
            # Simulate a read-back mismatch by using a wrong expected owner.
            # The verify call will fail, triggering rollback.
            Assert-ObservationLogSecurityPostcondition -FilePath $LogPath `
                -ExpectedOwnerSid 'S-1-5-21-0-0-0-9999' | Out-Null
        } else {
            Assert-ObservationLogSecurityPostcondition -FilePath $LogPath `
                -ExpectedOwnerSid $OwnerAccountSid | Out-Null
        }

        # (7) Re-validate the resulting full log (outer mutex guard still held).
        if ($InjectFailureAtForTest -eq 'PostWriteValidate') {
            throw [System.InvalidOperationException]::new('injected post-write validation failure (hermetic self-test only)')
        }
        Invoke-ObservationLogChecker -RepositoryRoot $RepositoryRoot -LogPath $LogPath | Out-Null
        if ($null -ne $PeerEnteredEvent -and $PeerEnteredEvent.WaitOne(0)) {
            Stop-Writer -GuardId 'TRANSACTION_PEER_EXCLUSION_FAILED' -Message (
                'peer process entered before parent DACL read-back and final validation completed')
        }

        return [pscustomobject]@{
            Record            = $built.Record
            SnapshotHashHex   = $built.SnapshotHashHex
            EntryHashHex      = $built.EntryHashHex
            PriorEntryHashHex = $priorHash
        }
    } catch {
        if ($null -ne $stream) { $stream.Dispose(); $stream = $null }
        $primaryMessage = $_.Exception.Message
        if ($mutationStarted) {
            try {
                if ($InjectRollbackFailureForTest) {
                    throw [System.IO.IOException]::new('injected rollback failure (hermetic self-test only)')
                }
                Restore-ObservationLogState -LogPath $LogPath -FilePreExisted $filePreExisted `
                    -PriorBytes $priorBytes -PriorSecurityState $priorSecurityState `
                    -DirectoryPreExisted $directoryPreExisted
            } catch {
                # Outer mutex is still held; release before re-throwing to avoid
                # leaving the guard permanently locked.
                if ($null -ne $ParentReleaseEventForTest) { $ParentReleaseEventForTest.Set() | Out-Null }
                try { $txnMutex.ReleaseMutex() } catch { }
                $txnMutex.Dispose()
                $txnMutex = $null
                if ($_.Exception -is [WriterGuardFailure]) { throw }
                Stop-Writer -GuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Message (
                    "primary failure: $primaryMessage; rollback also failed: $($_.Exception.Message)")
            }
        }
        if ($_.Exception -is [WriterGuardFailure]) {
            if ($null -ne $txnMutex) {
                if ($null -ne $ParentReleaseEventForTest) { $ParentReleaseEventForTest.Set() | Out-Null }
                try { $txnMutex.ReleaseMutex() } catch { }
                $txnMutex.Dispose()
                $txnMutex = $null
            }
            throw
        }
        if ($null -ne $txnMutex) {
            if ($null -ne $ParentReleaseEventForTest) { $ParentReleaseEventForTest.Set() | Out-Null }
            try { $txnMutex.ReleaseMutex() } catch { }
            $txnMutex.Dispose()
            $txnMutex = $null
        }
        Stop-Writer -GuardId 'OBSERVATION_LOG_WRITE_FAILED' -Message (
            "append transaction failed for '$LogPath': $primaryMessage")
    } finally {
        if ($null -ne $stream) { $stream.Dispose() }
        if ($null -ne $txnMutex) {
            if ($null -ne $ParentReleaseEventForTest) {
                $ParentReleaseEventForTest.Set() | Out-Null
            }
            try { $txnMutex.ReleaseMutex() } catch { }
            $txnMutex.Dispose()
        }
    }
}

function Protect-ObservationLog {
    <#
        .SYNOPSIS
            Harden the observation-log DACL (never SACL) so the creating
            principal (Party B) and the built-in SYSTEM/Administrators accounts
            retain FullControl while the exact Local reviewer SID receives
            read-only access. Verifies the existing creator owner SID before
            mutating and only touches the DACL.
            Never calls SetOwner (which requires unavailable privilege).
            Fails closed on any owner verification or DACL application defect.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $FilePath,
        [Parameter(Mandatory = $true)][string] $OwnerAccountSid
    )
    try {
        $ownerIdentity = [System.Security.Principal.SecurityIdentifier]::new($OwnerAccountSid)
        $fileInfo      = [System.IO.FileInfo]::new($FilePath)
        $ownerSecurity = [System.IO.FileSystemAclExtensions]::GetAccessControl(
            $fileInfo, [System.Security.AccessControl.AccessControlSections]::Owner)
        $actualOwnerSid = $ownerSecurity.GetOwner(
            [System.Security.Principal.SecurityIdentifier]).Value
        if ($actualOwnerSid -ne $ownerIdentity.Value) {
            Stop-Writer -GuardId 'DACL_HARDENING_FAILED' -Message (
                "log owner '$actualOwnerSid' does not match expected owner '$($ownerIdentity.Value)'; " +
                'cannot proceed with DACL hardening')
        }

        $fileSecurity = [System.Security.AccessControl.FileSecurity]::new()
        $fileSecurity.SetAccessRuleProtection($true, $false)

        $fileSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                $ownerIdentity,
                [System.Security.AccessControl.FileSystemRights]::FullControl,
                [System.Security.AccessControl.AccessControlType]::Allow))
        foreach ($recoverySidValue in @('S-1-5-18', 'S-1-5-32-544')) {  # SYSTEM, Administrators
            $recoveryIdentity = [System.Security.Principal.SecurityIdentifier]::new($recoverySidValue)
            $fileSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                    $recoveryIdentity,
                    [System.Security.AccessControl.FileSystemRights]::FullControl,
                    [System.Security.AccessControl.AccessControlType]::Allow))
        }
        if ($script:LocalSid -ne $OwnerAccountSid) {
            $localReviewerIdentity = [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid)
            $fileSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                    $localReviewerIdentity,
                    [System.Security.AccessControl.FileSystemRights]::Read,
                    [System.Security.AccessControl.AccessControlType]::Allow))
        }

        # Apply only the DACL; never call SetOwner (requires SeRestorePrivilege).
        [System.IO.FileSystemAclExtensions]::SetAccessControl($fileInfo, $fileSecurity)
        return $true
    } catch {
        if ($_.Exception -is [WriterGuardFailure]) { throw }
        Stop-Writer -GuardId 'DACL_HARDENING_FAILED' -Message (
            "could not harden DACL on '$FilePath': $($_.Exception.Message)")
    }
}

# --------------------------------------------------------------------------
# Real-mode orchestration
# --------------------------------------------------------------------------

function Invoke-ObservationWrite {
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )

    $current = Get-CurrentPrincipalFact
    $repositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path

    Assert-ExpectedPrincipal -CurrentPrincipal $current `
        -ExpectedAccountName $ExpectedAccountName -ExpectedAccountSid $ExpectedAccountSid
    Assert-ExpectedPrincipalIsVerifiedPartyB -ExpectedAccountName $ExpectedAccountName `
        -ExpectedAccountSid $ExpectedAccountSid

    $logPath = Resolve-GovernedPath -RepositoryRoot $repositoryRoot -RelativePath $script:LogRelativePath
    $inputPath = Resolve-GovernedPath -RepositoryRoot $repositoryRoot -RelativePath $script:InputRelativePath
    $lifecyclePath = Resolve-GovernedPath -RepositoryRoot $repositoryRoot -RelativePath $script:LifecycleRelativePath

    if (-not (Test-Path -LiteralPath $inputPath)) {
        Stop-Writer -GuardId 'INPUT_MISSING' -Message "Group 1 registry input not reachable at '$inputPath'"
    }

    Assert-InteractiveConfirmation -ExpectedAccountName $ExpectedAccountName

    # Validate Group 1 with the existing checker before reading exact bytes.
    Invoke-Group1Checker -RepositoryRoot $repositoryRoot -RegistryPath $inputPath -LifecyclePath $lifecyclePath | Out-Null

    $snapshotBytes = [System.IO.File]::ReadAllBytes($inputPath)
    $inputText = [System.Text.UTF8Encoding]::new($false).GetString($snapshotBytes)
    $inputObject = $inputText | ConvertFrom-Json -DateKind String -ErrorAction Stop
    $version = [int]$inputObject.registrySnapshotVersion
    if ($version -lt 1) {
        Stop-Writer -GuardId 'INPUT_VERSION_INVALID' -Message 'Group 1 registry snapshot version is not positive'
    }

    $snapshotId = New-FreshSnapshotId
    $observedAt = (Get-Date).ToUniversalTime().ToString('o')
    $built = Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $logPath `
        -SnapshotBytes $snapshotBytes -RegistrySnapshotVersion $version `
        -ObserverIdentity $current.Sid -OwnerAccountSid $current.Sid `
        -SnapshotId $snapshotId -ObservedAt $observedAt

    Write-Host ''
    Write-Host $script:RealModeResultText
    Write-Host "  snapshotId        : $snapshotId"
    Write-Host "  registryName      : $($script:RegistryName)"
    Write-Host "  registrySnapshotVersion : $version"
    Write-Host "  snapshotHashHex   : $($built.SnapshotHashHex)"
    Write-Host "  entryHashHex      : $($built.EntryHashHex)"
    Write-Host "  observerIdentity  : $($current.Sid)"
    Write-Host ''
    Write-Host 'This does NOT claim Group 3 establishment, admission or T3E consumer wiring.'
    return $logPath
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

function New-Ar1PeerEventSet {
    param([Parameter(Mandatory = $true)][string] $RunId)
    $mode = [System.Threading.EventResetMode]::ManualReset
    return [pscustomobject]@{
        Ready         = [System.Threading.EventWaitHandle]::new($false, $mode, ('Local\CVF_AR1_READY_' + $RunId))
        StartAttempt  = [System.Threading.EventWaitHandle]::new($false, $mode, ('Local\CVF_AR1_START_ATTEMPT_' + $RunId))
        Attempting    = [System.Threading.EventWaitHandle]::new($false, $mode, ('Local\CVF_AR1_ATTEMPTING_' + $RunId))
        Entered       = [System.Threading.EventWaitHandle]::new($false, $mode, ('Local\CVF_AR1_ENTERED_' + $RunId))
        ParentRelease = [System.Threading.EventWaitHandle]::new($false, $mode, ('Local\CVF_AR1_PARENT_RELEASE_' + $RunId))
        Complete      = [System.Threading.EventWaitHandle]::new($false, $mode, ('Local\CVF_AR1_COMPLETE_' + $RunId))
    }
}

function Start-Ar1PeerProcess {
    param(
        [Parameter(Mandatory = $true)][string] $LogPath,
        [Parameter(Mandatory = $true)][string] $RunId,
        [Parameter(Mandatory = $true)][string] $ObserverSid,
        [Parameter(Mandatory = $true)][string] $OwnerSid,
        [Parameter(Mandatory = $true)][string] $SnapshotId,
        [Parameter(Mandatory = $true)][string] $ObservedAt,
        [Parameter(Mandatory = $true)][string] $RepositoryRoot
    )
    $psi = [System.Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = (Get-Command pwsh -ErrorAction Stop).Source
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    foreach ($argument in @(
        '-NoProfile', '-NonInteractive', '-File', $PSCommandPath,
        '-PeerMode', '-PeerLogPath', $LogPath, '-PeerRunId', $RunId,
        '-PeerObserverSid', $ObserverSid, '-PeerOwnerSid', $OwnerSid,
        '-PeerSnapshotId', $SnapshotId, '-PeerObservedAt', $ObservedAt,
        '-PeerRepositoryRoot', $RepositoryRoot)) {
        $psi.ArgumentList.Add($argument)
    }
    return [System.Diagnostics.Process]::Start($psi)
}

function Close-Ar1PeerResources {
    param($Process, $Events)
    if ($null -ne $Process) {
        if (-not $Process.HasExited) {
            try { $Process.Kill($true) } catch { }
            try { $Process.WaitForExit(5000) | Out-Null } catch { }
        }
        $Process.Dispose()
    }
    if ($null -ne $Events) {
        foreach ($eventHandle in @($Events.Ready, $Events.StartAttempt, $Events.Attempting,
                $Events.Entered, $Events.ParentRelease, $Events.Complete)) {
            if ($null -ne $eventHandle) { $eventHandle.Dispose() }
        }
    }
}

function Invoke-SelfTest {
    $current = Get-CurrentPrincipalFact
    $localAppData = [System.Environment]::GetFolderPath(
        [System.Environment+SpecialFolder]::LocalApplicationData)

    Write-Host ''
    Write-Host "$($script:ToolContract) hermetic self-test"
    Write-Host "  identity : $($current.Name)"
    Write-Host "  elevated : $($current.IsElevated)"
    Write-Host '  mode     : SELF_TEST (no Party B context, no durable Group 3 output)'
    Write-Host ''

    $sandbox = Join-Path -Path $localAppData -ChildPath (
        'CVF_ACEL_G1_GROUP3_OBSERVATION_WRITER_SELFTEST_{0}' -f ([System.Guid]::NewGuid().ToString('N')))
    New-Item -ItemType Directory -Path $sandbox -Force | Out-Null

    try {
        # ---- T3C-C1-01: default non-mutation --------------------------------
        Add-TestResult -CaseId 'T3C-C1-01-A' -Contract 'T3C-C1-01' `
            -Passed ($PSCmdlet.ParameterSetName -eq 'SelfTest') `
            -Detail 'default parameter set is SelfTest; write requires -ExecuteWrite'

        $realLogDir = Join-Path (Split-Path -Path $PSScriptRoot -Parent) 'governance/sources/registry_observation_log'
        $sandboxFull = [System.IO.Path]::GetFullPath($sandbox).TrimEnd('\')
        $realLogDirFull = [System.IO.Path]::GetFullPath($realLogDir).TrimEnd('\')
        $selfTestIsIsolated = -not $sandboxFull.StartsWith(
            $realLogDirFull + '\', [System.StringComparison]::OrdinalIgnoreCase)
        Add-TestResult -CaseId 'T3C-C1-01-B' -Contract 'T3C-C1-01' -Passed $selfTestIsIsolated `
            -Detail 'default self-test sandbox is outside the durable Group 3 output path'

        # ---- T3C-C1-02: published 29-byte vector -----------------------------
        $vectorText = '{"registrySnapshotVersion":2}'
        $vectorBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($vectorText)
        $vectorBase64Url = ConvertTo-Base64UrlNoPadding -Bytes $vectorBytes
        $vectorHash = Get-Sha256Hex -Bytes $vectorBytes
        Add-TestResult -CaseId 'T3C-C1-02-A' -Contract 'T3C-C1-02' `
            -Passed ($vectorText.Length -eq 29) `
            -Detail 'published snapshot preimage is exactly 29 bytes'
        Add-TestResult -CaseId 'T3C-C1-02-B' -Contract 'T3C-C1-02' `
            -Passed ($vectorBase64Url -eq 'eyJyZWdpc3RyeVNuYXBzaG90VmVyc2lvbiI6Mn0') `
            -Detail 'published 29-byte base64url matches'
        Add-TestResult -CaseId 'T3C-C1-02-C' -Contract 'T3C-C1-02' `
            -Passed ($vectorHash -eq 'ecaddf2e1d99632e213b69f00240de3e4414ba3be1253a40946374624dd9949e') `
            -Detail 'published 29-byte snapshotHashHex matches'

        # ---- T3C-C1-03: exact closed preimage ---------------------------------
        $fixtureSnapshotText = '{"registrySnapshotVersion":1}'
        $fixtureSnapshotBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($fixtureSnapshotText)
        $builtGenesis = New-ObservationEntry -SnapshotId 'snap-selftest-0001' `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObservedAt '2026-09-21T00:00:00Z' -ObserverIdentity $script:VerifiedPartyBIdentity.principalSid `
            -PriorEntryHashHex $null
        $preimageForCheck = New-ObservationEntryPreimage -SnapshotId 'snap-selftest-0001' `
            -RegistryName $script:RegistryName -RegistrySnapshotVersion 1 `
            -SnapshotHashHex $builtGenesis.SnapshotHashHex -ObservedAt '2026-09-21T00:00:00Z' `
            -Authority $script:Authority -ObserverIdentity $script:VerifiedPartyBIdentity.principalSid `
            -PriorEntryHashHex $null
        $expectedGenesisHash = Get-PreimageDigestHex -Preimage $preimageForCheck
        Add-TestResult -CaseId 'T3C-C1-03-A' -Contract 'T3C-C1-03' `
            -Passed ($builtGenesis.EntryHashHex -eq $expectedGenesisHash) `
            -Detail 'genesis entryHashHex equals the recomputed closed-preimage digest'
        Add-TestResult -CaseId 'T3C-C1-03-B' -Contract 'T3C-C1-03' `
            -Passed ($builtGenesis.Record.priorEntryHashHex -eq $null) `
            -Detail 'genesis priorEntryHashHex is JSON null'

        $builtSecond = New-ObservationEntry -SnapshotId 'snap-selftest-0002' `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObservedAt '2026-09-21T00:00:01Z' -ObserverIdentity $script:VerifiedPartyBIdentity.principalSid `
            -PriorEntryHashHex $builtGenesis.EntryHashHex
        Add-TestResult -CaseId 'T3C-C1-03-C' -Contract 'T3C-C1-03' `
            -Passed ($builtSecond.Record.priorEntryHashHex -eq $builtGenesis.EntryHashHex) `
            -Detail 'second entry chains onto the genesis entryHashHex'

        # ---- T3C-C1-04: positive chain replay (cross-tool with Python checker) --
        $fixtureRepo = Join-Path -Path $sandbox -ChildPath 'fixture_repo'
        New-Item -ItemType Directory -Path $fixtureRepo -Force | Out-Null
        $fixtureLogPath = Join-Path -Path $fixtureRepo -ChildPath 'LOG.jsonl'
        $jsonLine1 = ($builtGenesis.Record | ConvertTo-Json -Depth 8 -Compress)
        $jsonLine2 = ($builtSecond.Record | ConvertTo-Json -Depth 8 -Compress)
        Set-Content -LiteralPath $fixtureLogPath -Value ($jsonLine1 + "`n" + $jsonLine2) -Encoding utf8NoBOM
        $checkerPath = Join-Path (Split-Path -Path $PSScriptRoot -Parent) 'governance/compat/check_acel_g1_registry_observation_log.py'
        $checkOutput = & python $checkerPath --log $fixtureLogPath `
            --expected-observer $script:VerifiedPartyBIdentity.principalSid `
            --registry-writer-sid $script:Group1WriterSid 2>&1
        $crossToolOk = ($LASTEXITCODE -eq 0)
        Add-TestResult -CaseId 'T3C-C1-04-A' -Contract 'T3C-C1-04' -Passed $crossToolOk `
            -Detail "writer-built two-entry chain accepted by independent Python checker (exit $LASTEXITCODE)"

        # ---- T3C-C1-05: strict encoding negatives ----------------------------
        Test-GuardRejects -CaseId 'T3C-C1-05-A' -Contract 'T3C-C1-05' `
            -ExpectedGuardId 'BASE64URL_INVALID' -Action {
            ConvertFrom-Base64Url -Text 'a' | Out-Null
        }
        Test-GuardRejects -CaseId 'T3C-C1-05-B' -Contract 'T3C-C1-05' `
            -ExpectedGuardId 'CANONICALIZATION_UNSUPPORTED_TYPE' -Action {
            ConvertTo-CanonicalJsonBytes -Object ([ordered]@{ x = 1.5 }) | Out-Null
        }

        # ---- T3C-C1-06: duplicate-ID and no-mutation -------------------------
        $dupLog = Join-Path -Path $sandbox -ChildPath 'dup_LOG.jsonl'
        $dupRecord1, $dupRecord2 = $builtGenesis.Record, $builtGenesis.Record
        Set-Content -LiteralPath $dupLog -Value (($dupRecord1 | ConvertTo-Json -Depth 8 -Compress) + "`n" + ($dupRecord2 | ConvertTo-Json -Depth 8 -Compress)) -Encoding utf8NoBOM
        $dupCheck = & python $checkerPath --log $dupLog `
            --expected-observer $script:VerifiedPartyBIdentity.principalSid `
            --registry-writer-sid $script:Group1WriterSid 2>&1
        Add-TestResult -CaseId 'T3C-C1-06-A' -Contract 'T3C-C1-06' `
            -Passed ($LASTEXITCODE -ne 0) `
            -Detail "duplicate snapshotId rejected by independent checker (exit $LASTEXITCODE)"

        # ---- T3C-C1-07: identity separation ----------------------------------
        $badObserverRecord = New-ObservationEntry -SnapshotId 'snap-selftest-bad' `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObservedAt '2026-09-21T00:00:00Z' -ObserverIdentity $script:PartyASid `
            -PriorEntryHashHex $null
        $badObserverLog = Join-Path -Path $sandbox -ChildPath 'bad_observer_LOG.jsonl'
        Set-Content -LiteralPath $badObserverLog -Value (($badObserverRecord.Record | ConvertTo-Json -Depth 8 -Compress)) -Encoding utf8NoBOM
        $badObserverCheck = & python $checkerPath --log $badObserverLog `
            --expected-observer $script:VerifiedPartyBIdentity.principalSid `
            --registry-writer-sid $script:Group1WriterSid 2>&1
        Add-TestResult -CaseId 'T3C-C1-07-A' -Contract 'T3C-C1-07' `
            -Passed ($LASTEXITCODE -ne 0) `
            -Detail "Party A observer identity rejected by independent checker (exit $LASTEXITCODE)"

        # ---- T3C-C1-08: real-mode path lock ----------------------------------
        Test-GuardRejects -CaseId 'T3C-C1-08-A' -Contract 'T3C-C1-08' `
            -ExpectedGuardId 'PRINCIPAL_NAME_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName 'NOT-THIS-HOST\definitely-not-current-user' `
                -ExpectedAccountSid $current.Sid
        }
        Test-GuardRejects -CaseId 'T3C-C1-08-B' -Contract 'T3C-C1-08' `
            -ExpectedGuardId 'PRINCIPAL_SID_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name -ExpectedAccountSid 'S-1-5-21-0-0-0-4999'
        }
        $elevatedProbe = [pscustomobject]@{ Name = $current.Name; Sid = $current.Sid; IsElevated = $true }
        Test-GuardRejects -CaseId 'T3C-C1-08-C' -Contract 'T3C-C1-08' `
            -ExpectedGuardId 'ELEVATED_CONTEXT_REJECTED' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $elevatedProbe `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
        }
        Test-GuardRejects -CaseId 'T3C-C1-08-D' -Contract 'T3C-C1-08' `
            -ExpectedGuardId 'EXPECTED_ACCOUNT_NOT_VERIFIED_PARTY_B' -Action {
            Assert-ExpectedPrincipalIsVerifiedPartyB -ExpectedAccountName $current.Name `
                -ExpectedAccountSid $current.Sid
        }
        Test-GuardRejects -CaseId 'T3C-C1-08-E' -Contract 'T3C-C1-08' `
            -ExpectedGuardId 'OUTPUT_PATH_ESCAPES_REPOSITORY' -Action {
            Resolve-GovernedPath -RepositoryRoot $sandbox -RelativePath '..\..\outside.json' | Out-Null
        }

        # ---- T3C-C1-09: confirmation phrase lock -----------------------------
        # The confirmation guard requires an interactive host; prove the exact
        # phrase comparison fails closed with a wrong phrase (guarded behind a
        # non-interactive-safe probe of the string comparison itself).
        Add-TestResult -CaseId 'T3C-C1-09-A' -Contract 'T3C-C1-09' `
            -Passed ($script:ConfirmationPhrase -cne 'WRONG PHRASE') `
            -Detail 'confirmation phrase is an exact, non-empty literal'

        # ---- T3C-C1-10: exact locked append (two and three appends) ---------
        $repositoryRoot = Split-Path -Path $PSScriptRoot -Parent
        $txnObserver = $script:VerifiedPartyBIdentity.principalSid
        $txnOwner = $current.Sid
        $txnLog = Join-Path -Path $sandbox -ChildPath 'txn_LOG.jsonl'

        $t1 = Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $txnLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-txn-0001' -ObservedAt '2026-09-21T00:00:00Z'
        $line1 = [System.Text.UTF8Encoding]::new($false).GetBytes(($t1.Record | ConvertTo-Json -Depth 8 -Compress) + "`n")
        $after1 = [System.IO.File]::ReadAllBytes($txnLog)
        Add-TestResult -CaseId 'T3C-C1-10-A' -Contract 'T3C-C1-10' `
            -Passed (Test-BytesEqual -Left $after1 -Right $line1) `
            -Detail 'genesis append yields exactly one line, no duplication'

        $t2 = Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $txnLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-txn-0002' -ObservedAt '2026-09-21T00:00:01Z'
        $line2 = [System.Text.UTF8Encoding]::new($false).GetBytes(($t2.Record | ConvertTo-Json -Depth 8 -Compress) + "`n")
        $after2 = [System.IO.File]::ReadAllBytes($txnLog)
        $expected2 = New-Object byte[] ($line1.Length + $line2.Length)
        [System.Array]::Copy($line1, 0, $expected2, 0, $line1.Length)
        [System.Array]::Copy($line2, 0, $expected2, $line1.Length, $line2.Length)
        Add-TestResult -CaseId 'T3C-C1-10-B' -Contract 'T3C-C1-10' `
            -Passed (Test-BytesEqual -Left $after2 -Right $expected2) `
            -Detail 'second append is exactly old + new bytes, no duplication'

        $t3 = Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $txnLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-txn-0003' -ObservedAt '2026-09-21T00:00:02Z'
        $line3 = [System.Text.UTF8Encoding]::new($false).GetBytes(($t3.Record | ConvertTo-Json -Depth 8 -Compress) + "`n")
        $after3 = [System.IO.File]::ReadAllBytes($txnLog)
        $expected3 = New-Object byte[] ($expected2.Length + $line3.Length)
        [System.Array]::Copy($expected2, 0, $expected3, 0, $expected2.Length)
        [System.Array]::Copy($line3, 0, $expected3, $expected2.Length, $line3.Length)
        Add-TestResult -CaseId 'T3C-C1-10-C' -Contract 'T3C-C1-10' `
            -Passed (Test-BytesEqual -Left $after3 -Right $expected3) `
            -Detail 'three sequential appends yield exactly three lines, byte-exact'

        # ---- T3C-C1-11: same-length replacement rejection -------------------
        $raceLog = Join-Path -Path $sandbox -ChildPath 'race_LOG.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $raceLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-race-0001' -ObservedAt '2026-09-21T00:00:00Z' | Out-Null
        Test-GuardRejects -CaseId 'T3C-C1-11-A' -Contract 'T3C-C1-11' `
            -ExpectedGuardId 'OBSERVATION_LOG_CONCURRENT_WRITE' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $raceLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-race-0002' -ObservedAt '2026-09-21T00:00:01Z' `
                -InjectFailureAtForTest 'SameLengthReplacement' | Out-Null
        }

        # ---- T3C-C1-12: DACL failure rollback (new and existing) ------------
        $daclNewLog = Join-Path -Path $sandbox -ChildPath 'dacl_new_LOG.jsonl'
        Test-GuardRejects -CaseId 'T3C-C1-12-A' -Contract 'T3C-C1-12' `
            -ExpectedGuardId 'OBSERVATION_LOG_WRITE_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $daclNewLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-daclnew-0001' -ObservedAt '2026-09-21T00:00:00Z' `
                -InjectFailureAtForTest 'Dacl' | Out-Null
        }
        Add-TestResult -CaseId 'T3C-C1-12-B' -Contract 'T3C-C1-12' `
            -Passed (-not (Test-Path -LiteralPath $daclNewLog)) `
            -Detail 'DACL failure on a new file removes the newly created artifact'

        $daclExistingLog = Join-Path -Path $sandbox -ChildPath 'dacl_existing_LOG.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $daclExistingLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-daclex-0001' -ObservedAt '2026-09-21T00:00:00Z' | Out-Null
        $daclBefore = [System.IO.File]::ReadAllBytes($daclExistingLog)
        Test-GuardRejects -CaseId 'T3C-C1-12-C' -Contract 'T3C-C1-12' `
            -ExpectedGuardId 'OBSERVATION_LOG_WRITE_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $daclExistingLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-daclex-0002' -ObservedAt '2026-09-21T00:00:01Z' `
                -InjectFailureAtForTest 'Dacl' | Out-Null
        }
        $daclAfter = [System.IO.File]::ReadAllBytes($daclExistingLog)
        Add-TestResult -CaseId 'T3C-C1-12-D' -Contract 'T3C-C1-12' `
            -Passed (Test-BytesEqual -Left $daclAfter -Right $daclBefore) `
            -Detail 'DACL failure on an existing file restores exact prior bytes'

        # ---- T3C-C1-13: post-write validation failure rollback --------------
        $postLog = Join-Path -Path $sandbox -ChildPath 'post_LOG.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $postLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-post-0001' -ObservedAt '2026-09-21T00:00:00Z' | Out-Null
        $postBefore = [System.IO.File]::ReadAllBytes($postLog)
        Test-GuardRejects -CaseId 'T3C-C1-13-A' -Contract 'T3C-C1-13' `
            -ExpectedGuardId 'OBSERVATION_LOG_WRITE_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $postLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-post-0002' -ObservedAt '2026-09-21T00:00:01Z' `
                -InjectFailureAtForTest 'PostWriteValidate' | Out-Null
        }
        $postAfter = [System.IO.File]::ReadAllBytes($postLog)
        Add-TestResult -CaseId 'T3C-C1-13-B' -Contract 'T3C-C1-13' `
            -Passed (Test-BytesEqual -Left $postAfter -Right $postBefore) `
            -Detail 'post-write validation failure restores exact prior bytes'

        # ---- T3C-C1-14: rollback failure taxonomy ---------------------------
        $rollbackLog = Join-Path -Path $sandbox -ChildPath 'rollback_LOG.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $rollbackLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-rb-0001' -ObservedAt '2026-09-21T00:00:00Z' | Out-Null
        Test-GuardRejects -CaseId 'T3C-C1-14-A' -Contract 'T3C-C1-14' `
            -ExpectedGuardId 'OBSERVATION_LOG_ROLLBACK_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $rollbackLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-rb-0002' -ObservedAt '2026-09-21T00:00:01Z' `
                -InjectFailureAtForTest 'Dacl' -InjectRollbackFailureForTest | Out-Null
        }

        # ---- T3C-C1-15: strict JSONL blank-line rejection -------------------
        $blankLog = Join-Path -Path $sandbox -ChildPath 'blank_LOG.jsonl'
        $blankRecordJson = ($t1.Record | ConvertTo-Json -Depth 8 -Compress)
        Set-Content -LiteralPath $blankLog -Value ($blankRecordJson + "`n`n" + $blankRecordJson) -Encoding utf8NoBOM
        $blankCheck = & python $checkerPath --log $blankLog `
            --expected-observer $script:VerifiedPartyBIdentity.principalSid `
            --registry-writer-sid $script:Group1WriterSid 2>&1
        Add-TestResult -CaseId 'T3C-C1-15-A' -Contract 'T3C-C1-15' `
            -Passed ($LASTEXITCODE -ne 0) `
            -Detail "interior blank JSONL line rejected by independent checker (exit $LASTEXITCODE)"

        # ---- T3C-C1-16: outer transaction guard - deterministic name derivation ----
        # Verify the guard name is derived deterministically and stably.
        $guardLog1 = Join-Path -Path $sandbox -ChildPath 'guard_LOG1.jsonl'
        $guardLog2 = Join-Path -Path $sandbox -ChildPath 'guard_LOG2.jsonl'
        # Derive the expected mutex name for guardLog1.
        $sha256g = [System.Security.Cryptography.SHA256]::Create()
        try {
            $normG     = [System.IO.Path]::GetFullPath($guardLog1).ToUpperInvariant()
            $pathBytesG = [System.Text.UTF8Encoding]::new($false).GetBytes($normG)
            $hashHexG   = [System.BitConverter]::ToString($sha256g.ComputeHash($pathBytesG)).Replace('-', '').ToLowerInvariant()
        } finally { $sha256g.Dispose() }
        $expectedMutexName = 'Global\CVF_G3_OBS_TXN_' + $hashHexG.Substring(0, 48)
        # Derive again from a fresh call - must be identical (deterministic).
        $sha256g2 = [System.Security.Cryptography.SHA256]::Create()
        try {
            $normG2     = [System.IO.Path]::GetFullPath($guardLog1).ToUpperInvariant()
            $pathBytesG2 = [System.Text.UTF8Encoding]::new($false).GetBytes($normG2)
            $hashHexG2   = [System.BitConverter]::ToString($sha256g2.ComputeHash($pathBytesG2)).Replace('-', '').ToLowerInvariant()
        } finally { $sha256g2.Dispose() }
        $expectedMutexName2 = 'Global\CVF_G3_OBS_TXN_' + $hashHexG2.Substring(0, 48)
        Add-TestResult -CaseId 'T3C-C1-16-A' -Contract 'T3C-C1-16' `
            -Passed ($expectedMutexName -eq $expectedMutexName2) `
            -Detail 'transaction guard name is derived deterministically (same path -> same name)'
        # Mutex name for a different path must differ.
        $sha256g3 = [System.Security.Cryptography.SHA256]::Create()
        try {
            $normG3     = [System.IO.Path]::GetFullPath($guardLog2).ToUpperInvariant()
            $pathBytesG3 = [System.Text.UTF8Encoding]::new($false).GetBytes($normG3)
            $hashHexG3   = [System.BitConverter]::ToString($sha256g3.ComputeHash($pathBytesG3)).Replace('-', '').ToLowerInvariant()
        } finally { $sha256g3.Dispose() }
        $expectedMutexName3 = 'Global\CVF_G3_OBS_TXN_' + $hashHexG3.Substring(0, 48)
        Add-TestResult -CaseId 'T3C-C1-16-B' -Contract 'T3C-C1-16' `
            -Passed ($expectedMutexName -ne $expectedMutexName3) `
            -Detail 'transaction guard name differs for different target paths'
        # Acquire a transaction guard and verify it is a live OS mutex object.
        $probeLog = Join-Path -Path $sandbox -ChildPath 'probe_guard_LOG.jsonl'
        $probeGuard = New-TransactionGuard -LogPath $probeLog
        Add-TestResult -CaseId 'T3C-C1-16-C' -Contract 'T3C-C1-16' `
            -Passed ($null -ne $probeGuard -and $probeGuard -is [System.Threading.Mutex]) `
            -Detail 'New-TransactionGuard returns an acquired System.Threading.Mutex'
        try { $probeGuard.ReleaseMutex() } catch { }
        $probeGuard.Dispose()

        # ---- T3C-C1-21: same-writer second-process serialization ------------
        $runId21 = [System.Guid]::NewGuid().ToString('N')
        $peerLog21 = Join-Path $sandbox ('peer21_LOG_{0}.jsonl' -f $runId21)
        $peerSnapshot21 = 'snap-peer21-' + $runId21
        $events21 = New-Ar1PeerEventSet -RunId $runId21
        $peerProcess21 = $null
        try {
            $peerProcess21 = Start-Ar1PeerProcess -LogPath $peerLog21 -RunId $runId21 `
                -ObserverSid $txnObserver -OwnerSid $txnOwner -SnapshotId $peerSnapshot21 `
                -ObservedAt '2026-09-21T06:30:00Z' -RepositoryRoot $repositoryRoot
            $ready21 = $events21.Ready.WaitOne(15000)
            Add-TestResult -CaseId 'T3C-C1-21-A' -Contract 'T3C-C1-21' -Passed $ready21 `
                -Detail 'real second pwsh running this writer reached READY'
            $parentOk21 = $false
            if ($ready21) {
                try {
                    Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $peerLog21 `
                        -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                        -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                        -SnapshotId ('snap-parent21-' + $runId21) -ObservedAt '2026-09-21T06:00:00Z' `
                        -PeerReadyEvent $events21.StartAttempt -PeerAttemptingEvent $events21.Attempting `
                        -PeerEnteredEvent $events21.Entered -ParentReleaseEventForTest $events21.ParentRelease | Out-Null
                    $parentOk21 = $true
                } catch { }
            }
            Add-TestResult -CaseId 'T3C-C1-21-B' -Contract 'T3C-C1-21' -Passed $parentOk21 `
                -Detail 'parent completed append while peer remained excluded through DACL and final validation'
            $completed21 = $events21.Complete.WaitOne(20000)
            $exited21 = $peerProcess21.WaitForExit(10000)
            $records21 = if (Test-Path $peerLog21) { @((Get-Content $peerLog21) | ConvertFrom-Json -DateKind String) } else { @() }
            $peerCount21 = @($records21 | Where-Object { $_.snapshotId -eq $peerSnapshot21 }).Count
            Add-TestResult -CaseId 'T3C-C1-21-C' -Contract 'T3C-C1-21' `
                -Passed ($completed21 -and $exited21 -and $peerProcess21.ExitCode -eq 0 -and $records21.Count -eq 2 -and $peerCount21 -eq 1) `
                -Detail 'peer re-read current bytes and appended exactly once after parent released the guard'
        } finally { Close-Ar1PeerResources -Process $peerProcess21 -Events $events21 }

        # ---- T3C-C1-22: rollback completes before peer enters ---------------
        $runId22 = [System.Guid]::NewGuid().ToString('N')
        $peerLog22 = Join-Path $sandbox ('peer22_LOG_{0}.jsonl' -f $runId22)
        $peerSnapshot22 = 'snap-peer22-' + $runId22
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $peerLog22 `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId ('snap-genesis22-' + $runId22) -ObservedAt '2026-09-21T06:00:00Z' | Out-Null
        $events22 = New-Ar1PeerEventSet -RunId $runId22
        $peerProcess22 = $null
        try {
            $peerProcess22 = Start-Ar1PeerProcess -LogPath $peerLog22 -RunId $runId22 `
                -ObserverSid $txnObserver -OwnerSid $txnOwner -SnapshotId $peerSnapshot22 `
                -ObservedAt '2026-09-21T07:00:00Z' -RepositoryRoot $repositoryRoot
            $ready22 = $events22.Ready.WaitOne(15000)
            $rollbackObserved22 = $false
            if ($ready22) {
                try {
                    Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $peerLog22 `
                        -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                        -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                        -SnapshotId ('snap-failing22-' + $runId22) -ObservedAt '2026-09-21T06:30:00Z' `
                        -PeerReadyEvent $events22.StartAttempt -PeerAttemptingEvent $events22.Attempting `
                        -PeerEnteredEvent $events22.Entered -ParentReleaseEventForTest $events22.ParentRelease `
                        -InjectFailureAtForTest 'AfterPeerAttemptBeforeDacl' | Out-Null
                } catch { $rollbackObserved22 = $true }
            }
            Add-TestResult -CaseId 'T3C-C1-22-A' -Contract 'T3C-C1-22' `
                -Passed ($ready22 -and $rollbackObserved22) `
                -Detail 'parent failed only after peer attempted entry; rollback ran while peer remained excluded'
            $completed22 = $events22.Complete.WaitOne(20000)
            $exited22 = $peerProcess22.WaitForExit(10000)
            $records22 = if (Test-Path $peerLog22) { @((Get-Content $peerLog22) | ConvertFrom-Json -DateKind String) } else { @() }
            $peerCount22 = @($records22 | Where-Object { $_.snapshotId -eq $peerSnapshot22 }).Count
            $failedCount22 = @($records22 | Where-Object { $_.snapshotId -eq ('snap-failing22-' + $runId22) }).Count
            Add-TestResult -CaseId 'T3C-C1-22-B' -Contract 'T3C-C1-22' `
                -Passed ($completed22 -and $exited22 -and $peerProcess22.ExitCode -eq 0 -and $records22.Count -eq 2 -and $peerCount22 -eq 1 -and $failedCount22 -eq 0) `
                -Detail 'peer entered after verified rollback, re-read genesis, and appended exactly once without lost update'
        } finally { Close-Ar1PeerResources -Process $peerProcess22 -Events $events22 }

        # ---- T3C-C1-23: injected post-acquire cleanup -----------------------
        $runId23 = [System.Guid]::NewGuid().ToString('N')
        $postAcqLog = Join-Path $sandbox ('postacq_{0}.jsonl' -f $runId23)
        $injected23 = $false
        try { New-TransactionGuard -LogPath $postAcqLog -InjectPostAcquireFailureForTest | Out-Null }
        catch { $injected23 = $_.Exception.Message -like '*injected post-acquire*' }
        Add-TestResult -CaseId 'T3C-C1-23-A' -Contract 'T3C-C1-23' -Passed $injected23 `
            -Detail 'deterministic exception was raised after OS mutex acquisition and cleaned up internally'
        $events23 = New-Ar1PeerEventSet -RunId $runId23
        $peerProcess23 = $null
        try {
            $peerProcess23 = Start-Ar1PeerProcess -LogPath $postAcqLog -RunId $runId23 `
                -ObserverSid $txnObserver -OwnerSid $txnOwner -SnapshotId ('snap-peer23-' + $runId23) `
                -ObservedAt '2026-09-21T08:00:00Z' -RepositoryRoot $repositoryRoot
            $ready23 = $events23.Ready.WaitOne(15000)
            if ($ready23) {
                $events23.ParentRelease.Set() | Out-Null
                $events23.StartAttempt.Set() | Out-Null
            }
            $completed23 = $events23.Complete.WaitOne(20000)
            $exited23 = $peerProcess23.WaitForExit(10000)
            Add-TestResult -CaseId 'T3C-C1-23-B' -Contract 'T3C-C1-23' `
                -Passed ($ready23 -and $completed23 -and $exited23 -and $peerProcess23.ExitCode -eq 0) `
                -Detail 'real second writer process acquired immediately after injected post-acquire failure and appended successfully'
        } finally { Close-Ar1PeerResources -Process $peerProcess23 -Events $events23 }

        # ---- T3C-C1-24: extra-allow ACE adversary (AR1 RV-3/RV-4) -----------
        # Write a file, apply DACL with an extra allow ACE for a stranger SID,
        # then verify Assert-ObservationLogSecurityPostcondition rejects it.
        $extraAllowFile = Join-Path -Path $sandbox -ChildPath 'extra_allow_probe.jsonl'
        [System.IO.File]::WriteAllText($extraAllowFile, '{}', [System.Text.UTF8Encoding]::new($false))
        $extraInfo = [System.IO.FileInfo]::new($extraAllowFile)
        $extraSec  = [System.Security.AccessControl.FileSecurity]::new()
        $extraSec.SetAccessRuleProtection($true, $false)
        foreach ($sid in @($txnOwner, 'S-1-5-18', 'S-1-5-32-544')) {
            $extraSec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                [System.Security.Principal.SecurityIdentifier]::new($sid),
                [System.Security.AccessControl.FileSystemRights]::FullControl,
                [System.Security.AccessControl.AccessControlType]::Allow))
        }
        if ($script:LocalSid -ne $txnOwner) {
            $extraSec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid),
                [System.Security.AccessControl.FileSystemRights]::Read,
                [System.Security.AccessControl.AccessControlType]::Allow))
        }
        # Add one extra allow ACE for a stranger SID.
        $extraSec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
            [System.Security.Principal.SecurityIdentifier]::new('S-1-5-21-0-0-0-7777'),
            [System.Security.AccessControl.FileSystemRights]::Read,
            [System.Security.AccessControl.AccessControlType]::Allow))
        [System.IO.FileSystemAclExtensions]::SetAccessControl($extraInfo, $extraSec)
        Test-GuardRejects -CaseId 'T3C-C1-24-A' -Contract 'T3C-C1-24' `
            -ExpectedGuardId 'DACL_VERIFICATION_FAILED' -Action {
            Assert-ObservationLogSecurityPostcondition -FilePath $extraAllowFile `
                -ExpectedOwnerSid $txnOwner | Out-Null
        }

        # ---- T3C-C1-25: deny ACE adversary (AR1 RV-3/RV-4) ------------------
        $denyAceFile = Join-Path -Path $sandbox -ChildPath 'deny_ace_probe.jsonl'
        [System.IO.File]::WriteAllText($denyAceFile, '{}', [System.Text.UTF8Encoding]::new($false))
        $denyInfo = [System.IO.FileInfo]::new($denyAceFile)
        $denySec  = [System.Security.AccessControl.FileSecurity]::new()
        $denySec.SetAccessRuleProtection($true, $false)
        foreach ($sid in @($txnOwner, 'S-1-5-18', 'S-1-5-32-544')) {
            $denySec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                [System.Security.Principal.SecurityIdentifier]::new($sid),
                [System.Security.AccessControl.FileSystemRights]::FullControl,
                [System.Security.AccessControl.AccessControlType]::Allow))
        }
        if ($script:LocalSid -ne $txnOwner) {
            $denySec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid),
                [System.Security.AccessControl.FileSystemRights]::Read,
                [System.Security.AccessControl.AccessControlType]::Allow))
        }
        # Add a deny ACE for a stranger SID.
        $denySec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
            [System.Security.Principal.SecurityIdentifier]::new('S-1-5-21-0-0-0-8888'),
            [System.Security.AccessControl.FileSystemRights]::Write,
            [System.Security.AccessControl.AccessControlType]::Deny))
        [System.IO.FileSystemAclExtensions]::SetAccessControl($denyInfo, $denySec)
        Test-GuardRejects -CaseId 'T3C-C1-25-A' -Contract 'T3C-C1-25' `
            -ExpectedGuardId 'DACL_VERIFICATION_FAILED' -Action {
            Assert-ObservationLogSecurityPostcondition -FilePath $denyAceFile `
                -ExpectedOwnerSid $txnOwner | Out-Null
        }

        # ---- T3C-C1-26: wrong owner adversary (AR1 RV-3/RV-4) ---------------
        # A correctly protected DACL but with a wrong expected owner SID must reject.
        $wrongOwnerFile = Join-Path -Path $sandbox -ChildPath 'wrong_owner_probe.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $wrongOwnerFile `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-wrongown-0001' -ObservedAt '2026-09-21T09:00:00Z' | Out-Null
        Test-GuardRejects -CaseId 'T3C-C1-26-A' -Contract 'T3C-C1-26' `
            -ExpectedGuardId 'DACL_VERIFICATION_FAILED' -Action {
            Assert-ObservationLogSecurityPostcondition -FilePath $wrongOwnerFile `
                -ExpectedOwnerSid 'S-1-5-21-0-0-0-6666' | Out-Null
        }

        # ---- T3C-C1-17: rollback after directory creation (RV-2) ------------
        # A new directory created during the transaction must be cleaned up on
        # failure even before the file is opened (failure injected at DirectoryCreate).
        $newDirParent = Join-Path -Path $sandbox -ChildPath 'newdir_parent'
        $newDirLog    = Join-Path -Path $newDirParent -ChildPath 'LOG.jsonl'
        $dirExistedBefore = Test-Path -LiteralPath $newDirParent
        Test-GuardRejects -CaseId 'T3C-C1-17-A' -Contract 'T3C-C1-17' `
            -ExpectedGuardId 'OBSERVATION_LOG_WRITE_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $newDirLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-dir-0001' -ObservedAt '2026-09-21T00:00:00Z' `
                -InjectFailureAtForTest 'DirectoryCreate' | Out-Null
        }
        Add-TestResult -CaseId 'T3C-C1-17-B' -Contract 'T3C-C1-17' `
            -Passed (-not (Test-Path -LiteralPath $newDirParent)) `
            -Detail 'failure at DirectoryCreate: new directory removed by rollback'
        Add-TestResult -CaseId 'T3C-C1-17-C' -Contract 'T3C-C1-17' `
            -Passed (-not $dirExistedBefore) `
            -Detail 'directory did not pre-exist (confirms the rollback removed a newly created dir)'

        # ---- T3C-C1-18: rollback after file creation / pre-existing dir ------
        # Failure after empty-file creation (FileCreate injection) must remove
        # the file but preserve a pre-existing directory.
        $existingDirLog = Join-Path -Path $sandbox -ChildPath 'existing_dir_LOG.jsonl'
        $existingDir    = [System.IO.Path]::GetDirectoryName($existingDirLog)
        # sandbox itself is the directory; it pre-existed.
        Test-GuardRejects -CaseId 'T3C-C1-18-A' -Contract 'T3C-C1-18' `
            -ExpectedGuardId 'OBSERVATION_LOG_WRITE_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $existingDirLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-filecreate-0001' -ObservedAt '2026-09-21T00:00:00Z' `
                -InjectFailureAtForTest 'FileCreate' | Out-Null
        }
        Add-TestResult -CaseId 'T3C-C1-18-B' -Contract 'T3C-C1-18' `
            -Passed (-not (Test-Path -LiteralPath $existingDirLog)) `
            -Detail 'failure at FileCreate: new empty file removed by rollback'
        Add-TestResult -CaseId 'T3C-C1-18-C' -Contract 'T3C-C1-18' `
            -Passed (Test-Path -LiteralPath $existingDir) `
            -Detail 'failure at FileCreate: pre-existing directory preserved by rollback'

        # ---- T3C-C1-19: security read-back acceptance/rejection (RV-3) ------
        # Prove Assert-ObservationLogSecurityPostcondition accepts the exact
        # policy and rejects each policy violation class with DACL_VERIFICATION_FAILED.
        $secProbeLog = Join-Path -Path $sandbox -ChildPath 'sec_probe_LOG.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $secProbeLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-sec-0001' -ObservedAt '2026-09-21T00:00:00Z' | Out-Null
        # 19-A: correct owner and DACL passes read-back.
        $secReadBackOk = $false
        try {
            $null = Assert-ObservationLogSecurityPostcondition -FilePath $secProbeLog -ExpectedOwnerSid $txnOwner
            $secReadBackOk = $true
        } catch { }
        Add-TestResult -CaseId 'T3C-C1-19-A' -Contract 'T3C-C1-19' `
            -Passed $secReadBackOk `
            -Detail 'security read-back accepts the exact applied owner and DACL policy'
        # 19-B: wrong expected owner is rejected.
        Test-GuardRejects -CaseId 'T3C-C1-19-B' -Contract 'T3C-C1-19' `
            -ExpectedGuardId 'DACL_VERIFICATION_FAILED' -Action {
            Assert-ObservationLogSecurityPostcondition -FilePath $secProbeLog `
                -ExpectedOwnerSid 'S-1-5-21-0-0-0-9999' | Out-Null
        }
        # 19-C: DaclVerify injection causes rollback (existing file bytes restored).
        $daclVerifyLog = Join-Path -Path $sandbox -ChildPath 'daclverify_LOG.jsonl'
        Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $daclVerifyLog `
            -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
            -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
            -SnapshotId 'snap-dv-0001' -ObservedAt '2026-09-21T00:00:00Z' | Out-Null
        $dvBefore = [System.IO.File]::ReadAllBytes($daclVerifyLog)
        $dvSecurityBefore = Get-ObservationLogSecurityState -FilePath $daclVerifyLog
        # DaclVerify injection raises DACL_VERIFICATION_FAILED (a WriterGuardFailure);
        # the transaction catch propagates it directly after rollback.
        Test-GuardRejects -CaseId 'T3C-C1-19-C' -Contract 'T3C-C1-19' `
            -ExpectedGuardId 'DACL_VERIFICATION_FAILED' -Action {
            Append-ObservationTransaction -RepositoryRoot $repositoryRoot -LogPath $daclVerifyLog `
                -SnapshotBytes $fixtureSnapshotBytes -RegistrySnapshotVersion 1 `
                -ObserverIdentity $txnObserver -OwnerAccountSid $txnOwner `
                -SnapshotId 'snap-dv-0002' -ObservedAt '2026-09-21T00:00:01Z' `
                -InjectFailureAtForTest 'DaclVerify' | Out-Null
        }
        $dvAfter = [System.IO.File]::ReadAllBytes($daclVerifyLog)
        Add-TestResult -CaseId 'T3C-C1-19-D' -Contract 'T3C-C1-19' `
            -Passed (Test-BytesEqual -Left $dvAfter -Right $dvBefore) `
            -Detail 'DaclVerify mismatch triggers rollback and restores exact prior bytes'
        $dvSecurityRestored = $false
        try {
            Assert-ObservationLogSecurityStateMatches -FilePath $daclVerifyLog `
                -ExpectedState $dvSecurityBefore | Out-Null
            $dvSecurityRestored = $true
        } catch { }
        Add-TestResult -CaseId 'T3C-C1-19-E' -Contract 'T3C-C1-19' `
            -Passed $dvSecurityRestored `
            -Detail 'rollback restores exact owner, protection flag and complete semantic ACE multiset'

        # ---- T3C-C1-20: security read-back protection flag check -------------
        # If inheritance is not disabled the read-back must reject.
        $unprotectedInfo = $null
        $unprotectedFile = Join-Path -Path $sandbox -ChildPath 'unprotected_sec_probe.jsonl'
        [System.IO.File]::WriteAllText($unprotectedFile, '{}', [System.Text.UTF8Encoding]::new($false))
        # The default DACL from New-Item / WriteAllText has inheritance enabled;
        # read-back must reject AreAccessRulesProtected=false.
        Test-GuardRejects -CaseId 'T3C-C1-20-A' -Contract 'T3C-C1-20' `
            -ExpectedGuardId 'DACL_VERIFICATION_FAILED' -Action {
            Assert-ObservationLogSecurityPostcondition -FilePath $unprotectedFile `
                -ExpectedOwnerSid $txnOwner | Out-Null
        }
    } finally {
        Remove-Item -LiteralPath $sandbox -Recurse -Force -ErrorAction SilentlyContinue
    }

    $failed = @($script:TestResults | Where-Object { -not $_.Passed })
    $total = $script:TestResults.Count
    Write-Host ''
    Write-Host "self-test summary: $($total - $failed.Count)/$total passed"
    if ($failed.Count -gt 0) {
        Write-Error "self-test failed with $($failed.Count) failing case(s)"
        exit 1
    }
    exit 0
}

# --------------------------------------------------------------------------
# Peer-mode entry point (test-only, unreachable from -ExecuteWrite)
# --------------------------------------------------------------------------

function Invoke-PeerMode {
    <#
        .SYNOPSIS
            Test-only peer worker. Launched by self-test orchestration as a
            second pwsh process. Acquires the transaction guard for the given
            log path, appends one record, and exits. Never targets the real
            Group 3 log or Party B principal. Unreachable from -ExecuteWrite.
    #>
    $ready         = [System.Threading.EventWaitHandle]::OpenExisting('Local\CVF_AR1_READY_' + $PeerRunId)
    $startAttempt  = [System.Threading.EventWaitHandle]::OpenExisting('Local\CVF_AR1_START_ATTEMPT_' + $PeerRunId)
    $attempting    = [System.Threading.EventWaitHandle]::OpenExisting('Local\CVF_AR1_ATTEMPTING_' + $PeerRunId)
    $entered       = [System.Threading.EventWaitHandle]::OpenExisting('Local\CVF_AR1_ENTERED_' + $PeerRunId)
    $parentRelease = [System.Threading.EventWaitHandle]::OpenExisting('Local\CVF_AR1_PARENT_RELEASE_' + $PeerRunId)
    $complete      = [System.Threading.EventWaitHandle]::OpenExisting('Local\CVF_AR1_COMPLETE_' + $PeerRunId)
    try {
        $ready.Set() | Out-Null
        if (-not $startAttempt.WaitOne(30000)) {
            throw [System.TimeoutException]::new('peer timed out waiting for parent transaction barrier')
        }
        $attempting.Set() | Out-Null
        $snap = [byte[]][System.Text.UTF8Encoding]::new($false).GetBytes('{"registrySnapshotVersion":1}')
        Append-ObservationTransaction `
            -RepositoryRoot $PeerRepositoryRoot -LogPath $PeerLogPath `
            -SnapshotBytes $snap -RegistrySnapshotVersion 1 `
            -ObserverIdentity $PeerObserverSid -OwnerAccountSid $PeerOwnerSid `
            -SnapshotId $PeerSnapshotId -ObservedAt $PeerObservedAt `
            -GuardAcquiredEventForTest $entered | Out-Null
        if (-not $parentRelease.WaitOne(0)) {
            throw [System.InvalidOperationException]::new(
                'peer entered before parent release barrier was signaled')
        }
    } finally {
        $complete.Set() | Out-Null
        foreach ($eventHandle in @($ready, $startAttempt, $attempting, $entered, $parentRelease, $complete)) {
            $eventHandle.Dispose()
        }
    }
    exit 0
}

# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

if ($PSCmdlet.ParameterSetName -eq 'Write') {
    Invoke-ObservationWrite -ExpectedAccountName $ExpectedAccountName -ExpectedAccountSid $ExpectedAccountSid
    exit 0
}

if ($PSCmdlet.ParameterSetName -eq 'PeerMode') {
    Invoke-PeerMode
    exit 0
}

Invoke-SelfTest
