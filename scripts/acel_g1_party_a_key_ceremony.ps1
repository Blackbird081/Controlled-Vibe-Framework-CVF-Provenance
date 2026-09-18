<#
.SYNOPSIS
    ACEL G1 T3A-C1 principal-bound Ed25519 key ceremony tool (fail-closed).

.DESCRIPTION
    Generates one Ed25519 signing key while logged on interactively as an exact
    expected Windows principal, protects the private PKCS8 material with Windows
    DPAPI CurrentUser before it ever reaches disk, and writes only a DPAPI
    ciphertext blob plus a non-secret public metadata document outside the
    repository.

    Default invocation is a hermetic self-test that proves every guard using
    ephemeral keys under the CURRENT user's temporary directory and removes
    them. A real ceremony requires -ExecuteCeremony, an exact principal name and
    SID match, a non-elevated interactive session, and a typed confirmation.

    This tool does not create the Group 1 registry, does not issue a lifecycle
    receipt, does not promote a key, and makes no source-readiness claim.

.PARAMETER SelfTest
    Run hermetic positive and negative self-tests as the current user. This is
    the default when no mode is chosen and never targets the expected principal.

.PARAMETER ExecuteCeremony
    Perform the real ceremony. Requires the current process identity to match
    both -ExpectedAccountName and -ExpectedAccountSid exactly, a non-elevated
    interactive host, and an interactive typed confirmation.

.PARAMETER ExpectedAccountName
    Exact expected Windows account name, e.g. 'HOSTNAME\cvf-g1-party-a'. A bare
    name is qualified with the local computer name before comparison.

.PARAMETER ExpectedAccountSid
    Exact expected Windows account SID.

.PARAMETER OutputDirectory
    Destination directory for the encrypted blob and public metadata. Must
    resolve outside the repository and under the current user's LocalAppData.

.PARAMETER KeyId
    Stable key identity recorded in public metadata.

.PARAMETER ValidityDays
    Whole days from creation to recorded expiry.

.EXAMPLE
    pwsh -NoProfile -File scripts/acel_g1_party_a_key_ceremony.ps1 -SelfTest

.NOTES
    Claim boundary: tooling only. Running the self-test proves guard behavior,
    not that any Party A ceremony occurred.
#>
[CmdletBinding(DefaultParameterSetName = 'SelfTest')]
param(
    [Parameter(ParameterSetName = 'SelfTest')]
    [switch] $SelfTest,

    [Parameter(ParameterSetName = 'Ceremony', Mandatory = $true)]
    [switch] $ExecuteCeremony,

    [Parameter(ParameterSetName = 'Ceremony', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $ExpectedAccountName,

    [Parameter(ParameterSetName = 'Ceremony', Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string] $ExpectedAccountSid,

    [Parameter(ParameterSetName = 'Ceremony')]
    [string] $OutputDirectory,

    [Parameter(ParameterSetName = 'Ceremony')]
    [string] $KeyId,

    [Parameter(ParameterSetName = 'Ceremony')]
    [ValidateRange(1, 3650)]
    [int] $ValidityDays = 365
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = 'Stop'

$script:ToolContract       = 'cvf.acel.g1.keyCeremonyTool@1'
$script:MetadataSchema     = 'cvf.acel.g1.partyAPublicKeyMetadata@1'
$script:MetadataProfile    = 'ACEL_G1_T3A_PRINCIPAL_BOUND_CEREMONY'
$script:Algorithm          = 'Ed25519'
$script:HelperFileName     = 'acel_g1_party_a_key_ceremony.js'
$script:Pkcs8DerLength     = 48
$script:RawPublicKeyLength = 32
$script:ConfirmationPhrase = 'EXECUTE PARTY A CEREMONY'
$script:BlobFileName       = 'party_a_private_key.dpapi'
$script:MetadataFileName   = 'party_a_public_key.json'

Add-Type -AssemblyName System.Security | Out-Null

# --------------------------------------------------------------------------
# Failure surface
# --------------------------------------------------------------------------

class CeremonyGuardFailure : System.Exception {
    [string] $GuardId
    CeremonyGuardFailure([string] $guardId, [string] $message) : base($message) {
        $this.GuardId = $guardId
    }
}

function Stop-Ceremony {
    <#
        .SYNOPSIS
            Fail closed with a named guard identity and no secret content.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $GuardId,
        [Parameter(Mandatory = $true)][string] $Message
    )
    throw [CeremonyGuardFailure]::new($GuardId, "[$GuardId] $Message")
}

# --------------------------------------------------------------------------
# Encoding and hashing helpers
# --------------------------------------------------------------------------

function ConvertTo-Base64Url {
    param([Parameter(Mandatory = $true)][byte[]] $Bytes)
    return [System.Convert]::ToBase64String($Bytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')
}

function ConvertFrom-Base64Url {
    param([Parameter(Mandatory = $true)][string] $Text)
    $standard = $Text.Replace('-', '+').Replace('_', '/')
    switch ($standard.Length % 4) {
        2 { $standard += '==' }
        3 { $standard += '=' }
        1 { Stop-Ceremony -GuardId 'BASE64URL_INVALID' -Message 'invalid base64url length' }
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

function Clear-ByteArray {
    <#
        .SYNOPSIS
            Best-effort in-place zeroing of a secret byte buffer.

        .DESCRIPTION
            Best-effort only: the .NET runtime may already hold copies that this
            cannot reach. It reduces, but does not eliminate, in-memory exposure.
    #>
    param([byte[]] $Bytes)
    if ($null -ne $Bytes) { [System.Array]::Clear($Bytes, 0, $Bytes.Length) }
}

function Clear-FileBestEffort {
    <#
        .SYNOPSIS
            Overwrite a temporary file's bytes before deletion.
    #>
    param([Parameter(Mandatory = $true)][string] $Path)
    try {
        $length = (Get-Item -LiteralPath $Path -Force).Length
        if ($length -gt 0) {
            [System.IO.File]::WriteAllBytes($Path, (New-Object byte[] $length))
        }
    } catch {
        Write-Verbose "best-effort clear failed for '$Path': $($_.Exception.Message)"
    }
}

# --------------------------------------------------------------------------
# C1-01 / C1-02: principal and context guards
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
    <#
        .SYNOPSIS
            Qualify a bare account name with the local computer name so that
            comparison is always domain-qualified on both sides.
    #>
    param([Parameter(Mandatory = $true)][string] $AccountName)

    $trimmed = $AccountName.Trim()
    if ($trimmed.Contains('\')) { return $trimmed }
    return ('{0}\{1}' -f $env:COMPUTERNAME, $trimmed)
}

function Assert-ExpectedPrincipal {
    <#
        .SYNOPSIS
            C1-01/C1-02. Reject unless the CURRENT identity is exactly the
            expected account name AND SID, and the context is not elevated.

        .DESCRIPTION
            Both name and SID must match; neither alone is sufficient, because a
            renamed account keeps its SID and a recreated account reuses a name.
            This runs before any key generation so a wrong identity can never
            reach the helper.
    #>
    param(
        [Parameter(Mandatory = $true)] $CurrentPrincipal,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid
    )

    $expectedName = Resolve-QualifiedAccountName -AccountName $ExpectedAccountName
    if ($CurrentPrincipal.Name -ne $expectedName) {
        Stop-Ceremony -GuardId 'PRINCIPAL_NAME_MISMATCH' -Message (
            "current account '$($CurrentPrincipal.Name)' is not the expected " +
            "account '$expectedName'; log on as the expected principal instead")
    }

    if ($CurrentPrincipal.Sid -ne $ExpectedAccountSid.Trim()) {
        Stop-Ceremony -GuardId 'PRINCIPAL_SID_MISMATCH' -Message (
            "current SID '$($CurrentPrincipal.Sid)' is not the expected SID; " +
            'name match alone is not sufficient identity proof')
    }

    if ($CurrentPrincipal.IsElevated) {
        Stop-Ceremony -GuardId 'ELEVATED_CONTEXT_REJECTED' -Message (
            'ceremony must not run in an elevated/Administrator context')
    }
}

function Assert-ExpectedAccountUsable {
    <#
        .SYNOPSIS
            C1-02. Inspect (never mutate) the expected local account and reject a
            disabled or already-expired account.

        .DESCRIPTION
            Read-only Get-LocalUser inspection. If the account cannot be read the
            ceremony fails closed rather than assuming it is healthy.
    #>
    param([Parameter(Mandatory = $true)][string] $ExpectedAccountName)

    $qualified = Resolve-QualifiedAccountName -AccountName $ExpectedAccountName
    $localName = $qualified.Split('\')[-1]

    $account = $null
    try {
        $account = Get-LocalUser -Name $localName -ErrorAction Stop
    } catch {
        Stop-Ceremony -GuardId 'ACCOUNT_STATE_UNREADABLE' -Message (
            "could not read local account '$localName': $($_.Exception.Message)")
    }

    if (-not $account.Enabled) {
        Stop-Ceremony -GuardId 'ACCOUNT_DISABLED' -Message (
            "local account '$localName' is disabled")
    }

    if ($null -ne $account.AccountExpires -and $account.AccountExpires -le (Get-Date)) {
        Stop-Ceremony -GuardId 'ACCOUNT_EXPIRED' -Message (
            "local account '$localName' expired at $($account.AccountExpires.ToString('o'))")
    }

    return $account
}

function Assert-InteractiveConfirmation {
    <#
        .SYNOPSIS
            C1-08. Require an interactive host and an exact typed phrase.

        .DESCRIPTION
            A non-interactive session is rejected outright so that no scheduled
            task, pipeline or agent can perform the ceremony unattended.

            Detection deliberately does not rely on
            [System.Environment]::UserInteractive: on Windows that property
            reports the window station, and it stays $true under pwsh
            -NonInteractive and under redirected stdin, so it would not stop an
            automated run. The authoritative signal is Read-Host itself, which
            throws PSInvalidOperationException in NonInteractive mode. Any
            failure to obtain a typed answer is therefore treated as
            non-interactive and rejected, never as an approval.
    #>
    param([Parameter(Mandatory = $true)][string] $ExpectedAccountName)

    Write-Host ''
    Write-Host "About to generate a NEW $($script:Algorithm) signing key for '$ExpectedAccountName'."
    Write-Host 'Private material will be DPAPI-protected for this user only and never printed.'
    Write-Host "Type exactly: $($script:ConfirmationPhrase)"

    $typed = $null
    try {
        $typed = Read-Host -Prompt 'Confirmation'
    } catch {
        Stop-Ceremony -GuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Message (
            'ceremony requires an interactive session; the host refused to prompt ' +
            "($($_.Exception.GetType().Name)), so execution is refused")
    }

    # An empty or absent answer is a non-answer, not a confirmation.
    if ([string]::IsNullOrEmpty($typed)) {
        Stop-Ceremony -GuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Message (
            'no confirmation input was received; execution is refused')
    }

    if ($typed -cne $script:ConfirmationPhrase) {
        Stop-Ceremony -GuardId 'CONFIRMATION_PHRASE_MISMATCH' -Message (
            'confirmation phrase did not match exactly; ceremony aborted')
    }
}

# --------------------------------------------------------------------------
# C1-03: output path guard
# --------------------------------------------------------------------------

function Get-RepositoryRoot {
    <#
        .SYNOPSIS
            Resolve the repository root that output must stay outside of.
    #>
    $scriptDirectory = Split-Path -Path $PSCommandPath -Parent
    return (Resolve-Path -LiteralPath (Split-Path -Path $scriptDirectory -Parent)).Path
}

function Test-PathIsInside {
    <#
        .SYNOPSIS
            Directory-boundary containment test on normalized full paths.

        .DESCRIPTION
            Compares with a trailing separator so that a sibling directory whose
            name merely starts with the container name is not treated as inside.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $CandidatePath,
        [Parameter(Mandatory = $true)][string] $ContainerPath
    )

    $separator = [System.IO.Path]::DirectorySeparatorChar
    $candidate = [System.IO.Path]::GetFullPath($CandidatePath).TrimEnd($separator) + $separator
    $container = [System.IO.Path]::GetFullPath($ContainerPath).TrimEnd($separator) + $separator
    return $candidate.StartsWith($container, [System.StringComparison]::OrdinalIgnoreCase)
}

function Resolve-CeremonyOutputDirectory {
    <#
        .SYNOPSIS
            C1-03. Resolve and validate the output directory.

        .DESCRIPTION
            The directory must normalize (so '..' traversal is resolved before
            judgment, not after), must be under the current user's LocalAppData,
            and must not be inside the repository. Symbolic links and junctions
            are rejected because a reparse point can redirect a permitted path
            into the repository or another user's tree after validation.
    #>
    param(
        [Parameter(Mandatory = $true)][AllowEmptyString()][string] $CandidateDirectory,
        [Parameter(Mandatory = $true)][string] $RepositoryRoot
    )

    if ([string]::IsNullOrWhiteSpace($CandidateDirectory)) {
        Stop-Ceremony -GuardId 'OUTPUT_PATH_EMPTY' -Message 'output directory was empty'
    }

    $expanded = [System.Environment]::ExpandEnvironmentVariables($CandidateDirectory)
    if (-not [System.IO.Path]::IsPathRooted($expanded)) {
        Stop-Ceremony -GuardId 'OUTPUT_PATH_NOT_ABSOLUTE' -Message (
            "output directory '$CandidateDirectory' must be an absolute path")
    }

    # Normalize first: this collapses '..' so a traversal path is judged by where
    # it actually lands rather than by how it is spelled.
    $normalized = [System.IO.Path]::GetFullPath($expanded)

    $localAppData = [System.Environment]::GetFolderPath(
        [System.Environment+SpecialFolder]::LocalApplicationData)
    if ([string]::IsNullOrWhiteSpace($localAppData)) {
        Stop-Ceremony -GuardId 'LOCALAPPDATA_UNRESOLVED' -Message (
            'could not resolve the current user LocalAppData directory')
    }

    if (Test-PathIsInside -CandidatePath $normalized -ContainerPath $RepositoryRoot) {
        Stop-Ceremony -GuardId 'OUTPUT_INSIDE_REPOSITORY' -Message (
            "output directory '$normalized' resolves inside the repository")
    }

    if (-not (Test-PathIsInside -CandidatePath $normalized -ContainerPath $localAppData)) {
        Stop-Ceremony -GuardId 'OUTPUT_OUTSIDE_LOCALAPPDATA' -Message (
            "output directory '$normalized' is not under the current user LocalAppData")
    }

    # Reject reparse points on the target and on every existing ancestor, since
    # any of them can redirect the final location.
    $inspected = $normalized
    while (-not [string]::IsNullOrEmpty($inspected)) {
        if (Test-Path -LiteralPath $inspected) {
            $item = Get-Item -LiteralPath $inspected -Force
            if ($item.Attributes.HasFlag([System.IO.FileAttributes]::ReparsePoint)) {
                Stop-Ceremony -GuardId 'OUTPUT_PATH_REPARSE_POINT' -Message (
                    "path component '$inspected' is a reparse point (symlink or junction)")
            }
        }
        $parent = [System.IO.Path]::GetDirectoryName($inspected)
        if ($parent -eq $inspected) { break }
        $inspected = $parent
    }

    return $normalized
}

function Assert-NoExistingCeremonyOutput {
    <#
        .SYNOPSIS
            C1-03/C1-07. Refuse to overwrite an existing ceremony output.
    #>
    param([Parameter(Mandatory = $true)][string] $OutputDirectory)

    foreach ($name in @($script:BlobFileName, $script:MetadataFileName)) {
        $target = Join-Path -Path $OutputDirectory -ChildPath $name
        if (Test-Path -LiteralPath $target) {
            Stop-Ceremony -GuardId 'OUTPUT_TARGET_COLLISION' -Message (
                "output file '$target' already exists; refusing to overwrite key material")
        }
    }
}

# --------------------------------------------------------------------------
# C1-04 / C1-05: generation and DPAPI protection
# --------------------------------------------------------------------------

function Invoke-KeyGeneratorHelper {
    <#
        .SYNOPSIS
            C1-04. Run the Node helper and capture its single stdout payload.

        .DESCRIPTION
            The payload is captured, never echoed. stderr is surfaced as failure
            text only. The returned object carries secret private material and
            must be cleared by the caller.
    #>
    param([Parameter(Mandatory = $true)][string] $HelperPath)

    if (-not (Test-Path -LiteralPath $HelperPath)) {
        Stop-Ceremony -GuardId 'HELPER_MISSING' -Message "generator helper not found at '$HelperPath'"
    }

    $process = $null
    try {
        # Redirect through anonymous process pipes, never filesystem paths.
        # The helper stdout contains plaintext PKCS8 and therefore must remain
        # in memory until DPAPI protection; Start-Process file redirection is
        # forbidden here even when followed by best-effort deletion.
        $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
        $startInfo.FileName = 'node'
        $startInfo.UseShellExecute = $false
        $startInfo.CreateNoWindow = $true
        $startInfo.RedirectStandardOutput = $true
        $startInfo.RedirectStandardError = $true
        [void]$startInfo.ArgumentList.Add($HelperPath)

        $process = [System.Diagnostics.Process]::new()
        $process.StartInfo = $startInfo
        if (-not $process.Start()) {
            Stop-Ceremony -GuardId 'HELPER_START_FAILED' -Message 'generator helper did not start'
        }

        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()
        $process.WaitForExit()
        $raw = $stdoutTask.GetAwaiter().GetResult()
        $errorText = $stderrTask.GetAwaiter().GetResult()

        if ($process.ExitCode -ne 0) {
            Stop-Ceremony -GuardId 'HELPER_FAILED' -Message (
                "generator helper exited with $($process.ExitCode): $errorText")
        }

        if ([string]::IsNullOrWhiteSpace($raw)) {
            Stop-Ceremony -GuardId 'HELPER_EMPTY_OUTPUT' -Message 'generator helper produced no output'
        }

        $payload = $raw | ConvertFrom-Json

        if ($payload.algorithm -ne $script:Algorithm) {
            Stop-Ceremony -GuardId 'HELPER_ALGORITHM_MISMATCH' -Message (
                "helper returned algorithm '$($payload.algorithm)', expected '$($script:Algorithm)'")
        }
        if ($payload.selfTestSignatureVerified -ne $true) {
            Stop-Ceremony -GuardId 'HELPER_SELFTEST_FAILED' -Message (
                'helper did not report a verified sign/verify self-test')
        }

        $privateBytes = [System.Convert]::FromBase64String($payload.privateKeyPkcs8DerBase64)
        if ($privateBytes.Length -ne $script:Pkcs8DerLength) {
            Stop-Ceremony -GuardId 'HELPER_PRIVATE_LENGTH_MISMATCH' -Message (
                "helper private key length $($privateBytes.Length) != $($script:Pkcs8DerLength)")
        }

        $publicBytes = ConvertFrom-Base64Url -Text $payload.publicKeyRawBase64Url
        if ($publicBytes.Length -ne $script:RawPublicKeyLength) {
            Stop-Ceremony -GuardId 'HELPER_PUBLIC_LENGTH_MISMATCH' -Message (
                "helper public key length $($publicBytes.Length) != $($script:RawPublicKeyLength)")
        }

        $computedDigest = Get-Sha256Hex -Bytes $publicBytes
        if ($computedDigest -ne $payload.publicKeySha256Hex) {
            Stop-Ceremony -GuardId 'HELPER_DIGEST_MISMATCH' -Message (
                'helper public-key digest does not match the recomputed digest')
        }

        return [pscustomobject]@{
            PrivateKeyPkcs8Der = $privateBytes
            PublicKeyRaw       = $publicBytes
            PublicKeyBase64Url = $payload.publicKeyRawBase64Url
            PublicKeySha256Hex = $computedDigest
        }
    } finally {
        if ($null -ne $process) { $process.Dispose() }
    }
}

function Protect-PrivateKeyBytes {
    <#
        .SYNOPSIS
            C1-05. DPAPI CurrentUser protection with a fixed entropy label.
    #>
    param([Parameter(Mandatory = $true)][byte[]] $PrivateKeyBytes)

    $entropy = [System.Text.Encoding]::UTF8.GetBytes($script:ToolContract)
    return [System.Security.Cryptography.ProtectedData]::Protect(
        $PrivateKeyBytes, $entropy,
        [System.Security.Cryptography.DataProtectionScope]::CurrentUser)
}

function Unprotect-PrivateKeyBytes {
    <#
        .SYNOPSIS
            C1-05. DPAPI CurrentUser unprotect used by the self-test roundtrip.
    #>
    param([Parameter(Mandatory = $true)][byte[]] $ProtectedBytes)

    $entropy = [System.Text.Encoding]::UTF8.GetBytes($script:ToolContract)
    return [System.Security.Cryptography.ProtectedData]::Unprotect(
        $ProtectedBytes, $entropy,
        [System.Security.Cryptography.DataProtectionScope]::CurrentUser)
}

# --------------------------------------------------------------------------
# C1-06 / C1-07: metadata and atomic write
# --------------------------------------------------------------------------

function New-PublicKeyMetadata {
    <#
        .SYNOPSIS
            C1-06. Build the non-secret public metadata document.

        .DESCRIPTION
            Contains only public fields. No private DER, no seed, no DPAPI
            plaintext, no confirmation phrase. The disposition fields keep a
            self-test artifact from ever reading as a real ceremony product.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $KeyId,
        [Parameter(Mandatory = $true)][string] $PrincipalName,
        [Parameter(Mandatory = $true)][string] $PrincipalSid,
        [Parameter(Mandatory = $true)][string] $PublicKeyBase64Url,
        [Parameter(Mandatory = $true)][string] $PublicKeySha256Hex,
        [Parameter(Mandatory = $true)][int]    $ValidityDays,
        [Parameter(Mandatory = $true)][ValidateSet('CEREMONY', 'SELF_TEST')][string] $Disposition
    )

    $createdAt = (Get-Date).ToUniversalTime()
    $expiresAt = $createdAt.AddDays($ValidityDays)

    $testDisposition = if ($Disposition -eq 'SELF_TEST') {
        'TEST_ONLY_NON_OPERATIONAL'
    } else {
        'CEREMONY_PRODUCT_PENDING_LOCAL_VERIFICATION'
    }

    return [ordered]@{
        metadataSchema       = $script:MetadataSchema
        metadataProfile      = $script:MetadataProfile
        keyId                = $KeyId
        algorithm            = $script:Algorithm
        principalName        = $PrincipalName
        principalSid         = $PrincipalSid
        publicKeyBytesBase64 = $PublicKeyBase64Url
        publicKeySha256Hex   = $PublicKeySha256Hex
        createdAtUtc         = $createdAt.ToString('o')
        expiresAtUtc         = $expiresAt.ToString('o')
        ceremonyDisposition  = $Disposition
        testDisposition      = $testDisposition
        registryDisposition  = 'SOURCE_NOT_CREATED'
        claimBoundary        = 'public metadata only; no registry row, lifecycle receipt, promotion or admission is claimed'
    }
}

function New-ExclusiveFile {
    <#
        .SYNOPSIS
            C1-07. Create a new file exclusively, or fail.

        .DESCRIPTION
            CreateNew mode makes existence-then-write a single atomic decision,
            so a concurrent writer cannot be silently overwritten.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $Path,
        [Parameter(Mandatory = $true)][byte[]] $Content
    )

    $stream = $null
    try {
        $stream = [System.IO.FileStream]::new(
            $Path,
            [System.IO.FileMode]::CreateNew,
            [System.IO.FileAccess]::Write,
            [System.IO.FileShare]::None)
        $stream.Write($Content, 0, $Content.Length)
        $stream.Flush($true)
    } catch [System.IO.IOException] {
        Stop-Ceremony -GuardId 'EXCLUSIVE_CREATE_FAILED' -Message (
            "could not exclusively create '$Path': $($_.Exception.Message)")
    } finally {
        if ($null -ne $stream) { $stream.Dispose() }
    }
}

function Write-CeremonyOutput {
    <#
        .SYNOPSIS
            C1-07. Write both outputs, removing every partial file on failure.

        .DESCRIPTION
            If the second write fails, the first is deleted, so a half-finished
            ceremony cannot be mistaken for a successful one.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $OutputDirectory,
        [Parameter(Mandatory = $true)][byte[]] $ProtectedPrivateKey,
        [Parameter(Mandatory = $true)] $Metadata
    )

    $blobPath     = Join-Path -Path $OutputDirectory -ChildPath $script:BlobFileName
    $metadataPath = Join-Path -Path $OutputDirectory -ChildPath $script:MetadataFileName
    $written      = @()

    try {
        New-ExclusiveFile -Path $blobPath -Content $ProtectedPrivateKey
        $written += $blobPath

        $json  = ($Metadata | ConvertTo-Json -Depth 8)
        $bytes = [System.Text.UTF8Encoding]::new($false).GetBytes($json + [System.Environment]::NewLine)
        New-ExclusiveFile -Path $metadataPath -Content $bytes
        $written += $metadataPath
    } catch {
        foreach ($path in $written) {
            Remove-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue
        }
        throw
    }

    return [pscustomobject]@{
        ProtectedPrivateKeyPath = $blobPath
        PublicMetadataPath      = $metadataPath
    }
}

function Set-CeremonyDirectoryAcl {
    <#
        .SYNOPSIS
            Restrict the output directory to the current user.

        .DESCRIPTION
            Disables inheritance and grants only the current identity. This is
            defense in depth, not isolation: another process running as the same
            user shares this user's DPAPI context.
    #>
    param([Parameter(Mandatory = $true)][string] $OutputDirectory)

    try {
        $acl = Get-Acl -LiteralPath $OutputDirectory
        $acl.SetAccessRuleProtection($true, $false)
        foreach ($rule in @($acl.Access)) { [void]$acl.RemoveAccessRule($rule) }
        $identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
        $acl.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                $identity.User,
                [System.Security.AccessControl.FileSystemRights]::FullControl,
                @([System.Security.AccessControl.InheritanceFlags]::ContainerInherit,
                  [System.Security.AccessControl.InheritanceFlags]::ObjectInherit),
                [System.Security.AccessControl.PropagationFlags]::None,
                [System.Security.AccessControl.AccessControlType]::Allow))
        Set-Acl -LiteralPath $OutputDirectory -AclObject $acl
        return $true
    } catch {
        Write-Warning "could not harden ACL on '$OutputDirectory': $($_.Exception.Message)"
        return $false
    }
}

function Test-RecoveredKeySignature {
    <#
        .SYNOPSIS
            Reconstruct a key from recovered PKCS8 and verify it signs correctly.

        .DESCRIPTION
            Delegates to Node, because .NET on PowerShell 7 has no first-class
            Ed25519 signer. The PKCS8 is passed on stdin so it never appears in a
            command line, process listing or log.
    #>
    param(
        [Parameter(Mandatory = $true)][byte[]] $RecoveredPkcs8,
        [Parameter(Mandatory = $true)][byte[]] $PublicKeyRaw
    )

    $verifierScript = @'
const crypto = require("crypto");
let raw = "";
process.stdin.on("data", d => raw += d).on("end", () => {
  try {
    const input = JSON.parse(raw);
    const priv = crypto.createPrivateKey({
      key: Buffer.from(input.pkcs8, "base64"), format: "der", type: "pkcs8" });
    const spki = crypto.createPublicKey(priv).export({ type: "spki", format: "der" });
    const derived = spki.subarray(spki.length - 32).toString("base64");
    if (derived !== input.publicKey) { process.stdout.write("MISMATCH"); return; }
    const challenge = crypto.randomBytes(32);
    const signature = crypto.sign(null, challenge, priv);
    const pub = crypto.createPublicKey({ key: spki, format: "der", type: "spki" });
    process.stdout.write(crypto.verify(null, challenge, pub, signature) ? "VERIFIED" : "INVALID");
  } catch (e) { process.stdout.write("ERROR"); }
});
'@

    $payload = @{
        pkcs8     = [System.Convert]::ToBase64String($RecoveredPkcs8)
        publicKey = [System.Convert]::ToBase64String($PublicKeyRaw)
    } | ConvertTo-Json -Compress

    $scriptFile = Join-Path -Path ([System.IO.Path]::GetTempPath()) `
        -ChildPath ('cvf_verify_{0}.js' -f ([System.Guid]::NewGuid().ToString('N')))
    try {
        [System.IO.File]::WriteAllText($scriptFile, $verifierScript)
        $result = ($payload | & node $scriptFile) 2>&1
        return ("$result".Trim() -eq 'VERIFIED')
    } finally {
        if (Test-Path -LiteralPath $scriptFile) {
            Clear-FileBestEffort -Path $scriptFile
            Remove-Item -LiteralPath $scriptFile -Force -ErrorAction SilentlyContinue
        }
    }
}

function Test-SecretPattern {
    <#
        .SYNOPSIS
            C1-06. Scan text for private material or secret-shaped field names.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $Text,
        [Parameter(Mandatory = $true)][byte[]] $PrivateKeyBytes,
        [Parameter(Mandatory = $true)][byte[]] $ProtectedBytes
    )

    $privateBase64 = [System.Convert]::ToBase64String($PrivateKeyBytes)
    $privateHex    = [System.BitConverter]::ToString($PrivateKeyBytes).Replace('-', '')
    $protectedB64  = [System.Convert]::ToBase64String($ProtectedBytes)

    foreach ($needle in @($privateBase64, $privateHex, $protectedB64)) {
        if ($Text.IndexOf($needle, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
            return $true
        }
    }

    foreach ($pattern in @('privateKey', 'PRIVATE KEY', 'pkcs8', 'seed', 'dpapi', 'password', 'secret')) {
        if ($Text -match [System.Text.RegularExpressions.Regex]::Escape($pattern)) { return $true }
    }
    return $false
}

function Test-PlaintextPrivateKeyOnDisk {
    <#
        .SYNOPSIS
            C1-05. Assert that no file under a directory holds the raw PKCS8.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $Directory,
        [Parameter(Mandatory = $true)][byte[]] $PrivateKeyBytes
    )

    foreach ($file in (Get-ChildItem -LiteralPath $Directory -Recurse -File -Force -ErrorAction SilentlyContinue)) {
        $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
        if ($bytes.Length -lt $PrivateKeyBytes.Length) { continue }
        for ($offset = 0; $offset -le ($bytes.Length - $PrivateKeyBytes.Length); $offset++) {
            $found = $true
            for ($index = 0; $index -lt $PrivateKeyBytes.Length; $index++) {
                if ($bytes[$offset + $index] -ne $PrivateKeyBytes[$index]) { $found = $false; break }
            }
            if ($found) { return $true }
        }
    }
    return $false
}

# --------------------------------------------------------------------------
# Ceremony (C1-08 gated)
# --------------------------------------------------------------------------

function Invoke-KeyCeremony {
    <#
        .SYNOPSIS
            Execute the guarded ceremony. Every guard runs before generation.
    #>
    param(
        [Parameter(Mandatory = $true)][string] $ExpectedAccountName,
        [Parameter(Mandatory = $true)][string] $ExpectedAccountSid,
        [Parameter(Mandatory = $true)][string] $OutputDirectory,
        [Parameter(Mandatory = $true)][string] $KeyId,
        [Parameter(Mandatory = $true)][int]    $ValidityDays
    )

    $repositoryRoot = Get-RepositoryRoot
    $current        = Get-CurrentPrincipalFact

    # Order matters: identity and context first, then account state, then path,
    # then human confirmation. No key exists until all of them pass.
    Assert-ExpectedPrincipal -CurrentPrincipal $current `
        -ExpectedAccountName $ExpectedAccountName -ExpectedAccountSid $ExpectedAccountSid
    [void](Assert-ExpectedAccountUsable -ExpectedAccountName $ExpectedAccountName)

    $resolvedOutput = Resolve-CeremonyOutputDirectory `
        -CandidateDirectory $OutputDirectory -RepositoryRoot $repositoryRoot

    if (-not (Test-Path -LiteralPath $resolvedOutput)) {
        New-Item -ItemType Directory -Path $resolvedOutput -Force | Out-Null
    }
    if (-not (Set-CeremonyDirectoryAcl -OutputDirectory $resolvedOutput)) {
        Stop-Ceremony -GuardId 'ACL_HARDENING_FAILED' -Message (
            "could not establish the required principal-only ACL on '$resolvedOutput'")
    }
    Assert-NoExistingCeremonyOutput -OutputDirectory $resolvedOutput

    Assert-InteractiveConfirmation -ExpectedAccountName $ExpectedAccountName

    $helperPath = Join-Path -Path (Split-Path -Path $PSCommandPath -Parent) `
        -ChildPath $script:HelperFileName

    $material  = $null
    $protected = $null
    try {
        $material  = Invoke-KeyGeneratorHelper -HelperPath $helperPath
        $protected = Protect-PrivateKeyBytes -PrivateKeyBytes $material.PrivateKeyPkcs8Der

        $metadata = New-PublicKeyMetadata -KeyId $KeyId `
            -PrincipalName $current.Name -PrincipalSid $current.Sid `
            -PublicKeyBase64Url $material.PublicKeyBase64Url `
            -PublicKeySha256Hex $material.PublicKeySha256Hex `
            -ValidityDays $ValidityDays -Disposition 'CEREMONY'

        $written = Write-CeremonyOutput -OutputDirectory $resolvedOutput `
            -ProtectedPrivateKey $protected -Metadata $metadata

        Write-Host ''
        Write-Host 'Ceremony completed. Private material was never written in plaintext.'
        Write-Host "  protected private key : $($written.ProtectedPrivateKeyPath)"
        Write-Host "  public metadata       : $($written.PublicMetadataPath)"
        Write-Host "  keyId                 : $KeyId"
        Write-Host "  publicKeySha256Hex    : $($material.PublicKeySha256Hex)"
        Write-Host ''
        Write-Host 'This does NOT create a Group 1 registry row, lifecycle receipt or admission.'
        return $written
    } finally {
        if ($null -ne $material) { Clear-ByteArray -Bytes $material.PrivateKeyPkcs8Der }
        Clear-ByteArray -Bytes $protected
    }
}

# --------------------------------------------------------------------------
# C1-09: hermetic self-test
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
    <#
        .SYNOPSIS
            Assert that a guarded action fails closed with the expected guard id.
    #>
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
        $guardId = if ($inner -is [CeremonyGuardFailure]) { $inner.GuardId } else { '<non-guard>' }
        $matched = ($guardId -eq $ExpectedGuardId)
        $detail = if ($matched) {
            "rejected with '$guardId'"
        } else {
            "expected '$ExpectedGuardId' but got '$guardId': $($inner.Message)"
        }
        Add-TestResult -CaseId $CaseId -Contract $Contract -Passed $matched -Detail $detail
    }
}

function Invoke-NonInteractiveCeremonyProbe {
    <#
        .SYNOPSIS
            C1-08. Prove a genuinely non-interactive -ExecuteCeremony run fails.

        .DESCRIPTION
            Spawns this same script in a real pwsh -NonInteractive child using
            the current non-elevated principal and a disposable output path.
            Identity/account/path guards must pass so the child reaches the
            confirmation boundary. The exact NONINTERACTIVE guard must stop it
            before generation. Returns structured result evidence.
    #>
    param([Parameter(Mandatory = $true)][string] $SandboxDirectory)

    $current     = Get-CurrentPrincipalFact
    $probeOutput = Join-Path -Path $SandboxDirectory -ChildPath 'noninteractive_probe'
    $stdoutFile  = Join-Path -Path $SandboxDirectory -ChildPath 'probe_stdout.txt'
    $stderrFile  = Join-Path -Path $SandboxDirectory -ChildPath 'probe_stderr.txt'

    try {
        $arguments = @(
            '-NoProfile', '-NonInteractive', '-File', "`"$PSCommandPath`"",
            '-ExecuteCeremony',
            '-ExpectedAccountName', $current.Name,
            '-ExpectedAccountSid', $current.Sid,
            '-OutputDirectory', "`"$probeOutput`""
        )
        $process = Start-Process -FilePath 'pwsh' -ArgumentList $arguments `
            -NoNewWindow -Wait -PassThru `
            -RedirectStandardOutput $stdoutFile -RedirectStandardError $stderrFile

        $stderrText = Get-Content -LiteralPath $stderrFile -Raw -ErrorAction SilentlyContinue
        $producedFiles = if (Test-Path -LiteralPath $probeOutput) {
            @(Get-ChildItem -LiteralPath $probeOutput -Recurse -File -Force -ErrorAction SilentlyContinue).Count
        } else { 0 }
        return [pscustomobject]@{
            ExitCode = $process.ExitCode
            GuardObserved = ($stderrText -match 'NONINTERACTIVE_EXECUTION_REJECTED')
            ProducedFileCount = $producedFiles
        }
    } catch {
        Write-Warning "noninteractive probe could not run: $($_.Exception.Message)"
        return [pscustomobject]@{ ExitCode = -1; GuardObserved = $false; ProducedFileCount = -1 }
    }
}

function Invoke-SelfTest {
    <#
        .SYNOPSIS
            C1-09. Hermetic positive and negative tests as the CURRENT user.

        .DESCRIPTION
            Uses only ephemeral keys in a disposable directory under this user's
            LocalAppData and removes them. It never targets the expected Party A
            principal, never reads an existing key, and produces no durable
            ceremony artifact.
    #>

    $current        = Get-CurrentPrincipalFact
    $repositoryRoot = Get-RepositoryRoot
    $localAppData   = [System.Environment]::GetFolderPath(
        [System.Environment+SpecialFolder]::LocalApplicationData)

    Write-Host ''
    Write-Host "$($script:ToolContract) hermetic self-test"
    Write-Host "  identity : $($current.Name)"
    Write-Host "  elevated : $($current.IsElevated)"
    Write-Host '  mode     : SELF_TEST (no Party A context, no durable ceremony output)'
    Write-Host ''

    $sandbox = Join-Path -Path $localAppData -ChildPath (
        'CVF_ACEL_G1_KEY_CEREMONY_SELFTEST_{0}' -f ([System.Guid]::NewGuid().ToString('N')))
    New-Item -ItemType Directory -Path $sandbox -Force | Out-Null

    $material       = $null
    $protectedBytes = $null
    try {
        # ---- C1-01: identity guards -------------------------------------
        Test-GuardRejects -CaseId 'C1-01-A' -Contract 'C1-01' `
            -ExpectedGuardId 'PRINCIPAL_NAME_MISMATCH' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName 'NOT-THIS-HOST\definitely-not-current-user' `
                -ExpectedAccountSid $current.Sid
        }

        Test-GuardRejects -CaseId 'C1-01-B' -Contract 'C1-01' `
            -ExpectedGuardId 'PRINCIPAL_SID_MISMATCH' -Action {
            # Correct name, wrong SID: name match alone must not be enough.
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name `
                -ExpectedAccountSid 'S-1-5-21-0-0-0-4999'
        }

        try {
            Assert-ExpectedPrincipal -CurrentPrincipal $current `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
            Add-TestResult -CaseId 'C1-01-C' -Contract 'C1-01' -Passed (-not $current.IsElevated) `
                -Detail 'exact current name and SID accepted in a non-elevated context'
        } catch {
            Add-TestResult -CaseId 'C1-01-C' -Contract 'C1-01' -Passed $current.IsElevated `
                -Detail "matching identity rejected: $($_.Exception.Message)"
        }

        # ---- C1-02: elevated context and account state ------------------
        $elevatedProbe = [pscustomobject]@{
            Name = $current.Name; Sid = $current.Sid; IsElevated = $true
        }
        Test-GuardRejects -CaseId 'C1-02-A' -Contract 'C1-02' `
            -ExpectedGuardId 'ELEVATED_CONTEXT_REJECTED' -Action {
            Assert-ExpectedPrincipal -CurrentPrincipal $elevatedProbe `
                -ExpectedAccountName $current.Name -ExpectedAccountSid $current.Sid
        }

        Test-GuardRejects -CaseId 'C1-02-B' -Contract 'C1-02' `
            -ExpectedGuardId 'ACCOUNT_STATE_UNREADABLE' -Action {
            # Inspection-only: a nonexistent account must fail closed rather than
            # be assumed healthy. No account is created or modified.
            Assert-ExpectedAccountUsable -ExpectedAccountName 'cvf-nonexistent-probe-account-0000'
        }

        # ---- C1-03: output path guards ----------------------------------
        Test-GuardRejects -CaseId 'C1-03-A' -Contract 'C1-03' `
            -ExpectedGuardId 'OUTPUT_INSIDE_REPOSITORY' -Action {
            Resolve-CeremonyOutputDirectory `
                -CandidateDirectory (Join-Path $repositoryRoot 'governance') `
                -RepositoryRoot $repositoryRoot
        }

        Test-GuardRejects -CaseId 'C1-03-B' -Contract 'C1-03' `
            -ExpectedGuardId 'OUTPUT_OUTSIDE_LOCALAPPDATA' -Action {
            # Traversal that normalizes out of LocalAppData must be judged by its
            # resolved target, not by how it is spelled.
            Resolve-CeremonyOutputDirectory `
                -CandidateDirectory (Join-Path $localAppData '..\..\..\cvf-traversal-probe') `
                -RepositoryRoot $repositoryRoot
        }

        Test-GuardRejects -CaseId 'C1-03-C' -Contract 'C1-03' `
            -ExpectedGuardId 'OUTPUT_PATH_NOT_ABSOLUTE' -Action {
            Resolve-CeremonyOutputDirectory -CandidateDirectory 'relative\keys' `
                -RepositoryRoot $repositoryRoot
        }

        Test-GuardRejects -CaseId 'C1-03-D' -Contract 'C1-03' `
            -ExpectedGuardId 'OUTPUT_PATH_EMPTY' -Action {
            Resolve-CeremonyOutputDirectory -CandidateDirectory '' -RepositoryRoot $repositoryRoot
        }

        $resolvedSandbox = Resolve-CeremonyOutputDirectory -CandidateDirectory $sandbox `
            -RepositoryRoot $repositoryRoot
        Add-TestResult -CaseId 'C1-03-E' -Contract 'C1-03' `
            -Passed ($resolvedSandbox -eq [System.IO.Path]::GetFullPath($sandbox)) `
            -Detail 'disposable LocalAppData sandbox accepted'

        $aclHardened = Set-CeremonyDirectoryAcl -OutputDirectory $sandbox
        $sandboxAcl = Get-Acl -LiteralPath $sandbox
        $currentSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
        $unexpectedAllow = @($sandboxAcl.Access | Where-Object {
                $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Allow `
                -and $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -ne $currentSid
            })
        Add-TestResult -CaseId 'C1-03-F' -Contract 'C1-03' `
            -Passed ($aclHardened -and $sandboxAcl.AreAccessRulesProtected `
                -and $unexpectedAllow.Count -eq 0) `
            -Detail 'sandbox ACL inheritance disabled and allow rules restricted to current SID'

        # ---- C1-04: generator helper ------------------------------------
        $helperPath = Join-Path -Path (Split-Path -Path $PSCommandPath -Parent) `
            -ChildPath $script:HelperFileName
        $captureProbe = Join-Path -Path $sandbox -ChildPath 'in_memory_capture_probe'
        New-Item -ItemType Directory -Path $captureProbe -Force | Out-Null
        $priorTemp = $env:TEMP
        $priorTmp = $env:TMP
        try {
            $env:TEMP = $captureProbe
            $env:TMP = $captureProbe
            $material = Invoke-KeyGeneratorHelper -HelperPath $helperPath
        } finally {
            $env:TEMP = $priorTemp
            $env:TMP = $priorTmp
        }
        Add-TestResult -CaseId 'C1-04-A' -Contract 'C1-04' `
            -Passed ($material.PrivateKeyPkcs8Der.Length -eq $script:Pkcs8DerLength `
                -and $material.PublicKeyRaw.Length -eq $script:RawPublicKeyLength) `
            -Detail ("PKCS8 DER $($material.PrivateKeyPkcs8Der.Length) bytes, " +
                "raw public key $($material.PublicKeyRaw.Length) bytes")

        Add-TestResult -CaseId 'C1-04-B' -Contract 'C1-04' `
            -Passed ((ConvertTo-Base64Url -Bytes $material.PublicKeyRaw) -eq $material.PublicKeyBase64Url) `
            -Detail 'public key base64url encoding round-trips'

        Test-GuardRejects -CaseId 'C1-04-C' -Contract 'C1-04' `
            -ExpectedGuardId 'HELPER_MISSING' -Action {
            Invoke-KeyGeneratorHelper -HelperPath (Join-Path $sandbox 'no_such_helper.js')
        }

        $captureResidue = @(Get-ChildItem -LiteralPath $captureProbe -File -Force -ErrorAction SilentlyContinue)
        Add-TestResult -CaseId 'C1-04-D' -Contract 'C1-04' `
            -Passed ($captureResidue.Count -eq 0) `
            -Detail 'helper stdout/stderr capture remained in memory and created no temporary file'

        # ---- C1-05: DPAPI roundtrip and signature proof -----------------
        $protectedBytes = Protect-PrivateKeyBytes -PrivateKeyBytes $material.PrivateKeyPkcs8Der
        $ciphertextDiffers = ([System.Convert]::ToBase64String($protectedBytes) -ne
            [System.Convert]::ToBase64String($material.PrivateKeyPkcs8Der))
        Add-TestResult -CaseId 'C1-05-A' -Contract 'C1-05' -Passed $ciphertextDiffers `
            -Detail "DPAPI ciphertext ($($protectedBytes.Length) bytes) differs from plaintext"

        $recovered = Unprotect-PrivateKeyBytes -ProtectedBytes $protectedBytes
        $roundTripMatches = [System.Linq.Enumerable]::SequenceEqual(
            [byte[]]$recovered, [byte[]]$material.PrivateKeyPkcs8Der)
        Add-TestResult -CaseId 'C1-05-B' -Contract 'C1-05' -Passed $roundTripMatches `
            -Detail 'DPAPI CurrentUser unprotect reproduced the original PKCS8 bytes'

        # Prove the protected key is still a usable signing key by reconstructing
        # it and verifying a signature against the published public bytes.
        $signatureVerified = Test-RecoveredKeySignature `
            -RecoveredPkcs8 $recovered -PublicKeyRaw $material.PublicKeyRaw
        Add-TestResult -CaseId 'C1-05-C' -Contract 'C1-05' -Passed $signatureVerified `
            -Detail 'recovered key signed a challenge that verified against the public key'

        Clear-ByteArray -Bytes $recovered

        # ---- C1-06: metadata shape --------------------------------------
        $metadata = New-PublicKeyMetadata -KeyId 'selftest-ephemeral' `
            -PrincipalName $current.Name -PrincipalSid $current.Sid `
            -PublicKeyBase64Url $material.PublicKeyBase64Url `
            -PublicKeySha256Hex $material.PublicKeySha256Hex `
            -ValidityDays 1 -Disposition 'SELF_TEST'

        $requiredFields = @(
            'metadataSchema', 'metadataProfile', 'keyId', 'algorithm',
            'principalName', 'principalSid', 'publicKeyBytesBase64',
            'publicKeySha256Hex', 'createdAtUtc', 'expiresAtUtc',
            'ceremonyDisposition', 'testDisposition')
        $missing = @($requiredFields | Where-Object { -not $metadata.Contains($_) })
        Add-TestResult -CaseId 'C1-06-A' -Contract 'C1-06' -Passed ($missing.Count -eq 0) `
            -Detail ("required metadata fields present ($($requiredFields.Count)); missing: " +
                $(if ($missing.Count -eq 0) { 'none' } else { $missing -join ',' }))

        $metadataJson = $metadata | ConvertTo-Json -Depth 8
        $secretLeak = Test-SecretPattern -Text $metadataJson `
            -PrivateKeyBytes $material.PrivateKeyPkcs8Der -ProtectedBytes $protectedBytes
        Add-TestResult -CaseId 'C1-06-B' -Contract 'C1-06' -Passed (-not $secretLeak) `
            -Detail 'metadata contains no private DER, DPAPI blob or secret-shaped field'

        Add-TestResult -CaseId 'C1-06-C' -Contract 'C1-06' `
            -Passed ($metadata['testDisposition'] -eq 'TEST_ONLY_NON_OPERATIONAL') `
            -Detail 'self-test metadata is marked TEST_ONLY_NON_OPERATIONAL'

        # ---- C1-07: exclusive create, no plaintext, cleanup -------------
        $written = Write-CeremonyOutput -OutputDirectory $sandbox `
            -ProtectedPrivateKey $protectedBytes -Metadata $metadata
        $bothWritten = (Test-Path -LiteralPath $written.ProtectedPrivateKeyPath) -and
        (Test-Path -LiteralPath $written.PublicMetadataPath)
        Add-TestResult -CaseId 'C1-07-A' -Contract 'C1-07' -Passed $bothWritten `
            -Detail 'ephemeral blob and metadata created in the disposable sandbox'

        $plaintextOnDisk = Test-PlaintextPrivateKeyOnDisk -Directory $sandbox `
            -PrivateKeyBytes $material.PrivateKeyPkcs8Der
        Add-TestResult -CaseId 'C1-07-B' -Contract 'C1-07' -Passed (-not $plaintextOnDisk) `
            -Detail 'no file in the sandbox contains the plaintext private key'

        Test-GuardRejects -CaseId 'C1-07-C' -Contract 'C1-07' `
            -ExpectedGuardId 'OUTPUT_TARGET_COLLISION' -Action {
            Assert-NoExistingCeremonyOutput -OutputDirectory $sandbox
        }

        Test-GuardRejects -CaseId 'C1-07-D' -Contract 'C1-07' `
            -ExpectedGuardId 'EXCLUSIVE_CREATE_FAILED' -Action {
            New-ExclusiveFile -Path $written.PublicMetadataPath -Content ([byte[]]@(1, 2, 3))
        }

        # Injected failure: the metadata write fails, so the already-written blob
        # must be removed and no partial ceremony can appear successful.
        $partialDirectory = Join-Path -Path $sandbox -ChildPath 'partial'
        New-Item -ItemType Directory -Path $partialDirectory -Force | Out-Null
        $blockingMetadata = Join-Path -Path $partialDirectory -ChildPath $script:MetadataFileName
        New-ExclusiveFile -Path $blockingMetadata -Content ([byte[]]@(0))
        $partialBlob = Join-Path -Path $partialDirectory -ChildPath $script:BlobFileName
        $cleanedUp = $false
        try {
            Write-CeremonyOutput -OutputDirectory $partialDirectory `
                -ProtectedPrivateKey $protectedBytes -Metadata $metadata | Out-Null
        } catch {
            $cleanedUp = -not (Test-Path -LiteralPath $partialBlob)
        }
        Add-TestResult -CaseId 'C1-07-E' -Contract 'C1-07' -Passed $cleanedUp `
            -Detail 'injected metadata-write failure removed the partial private-key blob'

        # ---- C1-08: execution gating ------------------------------------
        Add-TestResult -CaseId 'C1-08-A' -Contract 'C1-08' `
            -Passed ($PSCmdlet.ParameterSetName -eq 'SelfTest') `
            -Detail 'default parameter set is SelfTest; ceremony requires -ExecuteCeremony'

        $noDurableOutput = -not (Test-Path -LiteralPath (Join-Path -Path (
                    [System.Environment]::GetFolderPath(
                        [System.Environment+SpecialFolder]::LocalApplicationData)) `
                    -ChildPath 'CVF\ACEL_G1\party_a_key'))
        Add-TestResult -CaseId 'C1-08-B' -Contract 'C1-08' -Passed $noDurableOutput `
            -Detail 'default self-test created no durable ceremony output directory'

        # Real non-interactive execution with the exact current identity. This
        # must pass the earlier guards and fail specifically at confirmation.
        $childResult = Invoke-NonInteractiveCeremonyProbe -SandboxDirectory $sandbox
        $childRejectedAtConfirmation = ($childResult.ExitCode -ne 0 `
            -and $childResult.GuardObserved `
            -and $childResult.ProducedFileCount -eq 0)
        Add-TestResult -CaseId 'C1-08-C' -Contract 'C1-08' `
            -Passed $childRejectedAtConfirmation `
            -Detail ("noninteractive child exit=$($childResult.ExitCode), " +
                "confirmationGuard=$($childResult.GuardObserved), " +
                "files=$($childResult.ProducedFileCount)")

        Test-GuardRejects -CaseId 'C1-08-D' -Contract 'C1-08' `
            -ExpectedGuardId 'NONINTERACTIVE_EXECUTION_REJECTED' -Action {
            # Read-Host is unavailable in this captured-output context, so the
            # confirmation guard must fail closed rather than treat a missing
            # answer as approval.
            Assert-InteractiveConfirmation -ExpectedAccountName $current.Name
        }

        # ---- C1-09: no Party A contact ----------------------------------
        $partyAUntouched = ($current.Name -notlike '*cvf-g1-party-a*')
        Add-TestResult -CaseId 'C1-09-A' -Contract 'C1-09' -Passed $partyAUntouched `
            -Detail "self-test ran as '$($current.Name)', not as the expected Party A principal"
    } finally {
        if ($null -ne $material) { Clear-ByteArray -Bytes $material.PrivateKeyPkcs8Der }
        if ($null -ne $protectedBytes) { Clear-ByteArray -Bytes $protectedBytes }
        if (Test-Path -LiteralPath $sandbox) {
            Get-ChildItem -LiteralPath $sandbox -Recurse -File -Force -ErrorAction SilentlyContinue |
                ForEach-Object { Clear-FileBestEffort -Path $_.FullName }
            Remove-Item -LiteralPath $sandbox -Recurse -Force -ErrorAction SilentlyContinue
        }
        $removed = -not (Test-Path -LiteralPath $sandbox)
        Add-TestResult -CaseId 'CLEANUP-A' -Contract 'C1-09' -Passed $removed `
            -Detail "disposable sandbox removed: $sandbox"
    }

    $failed = @($script:TestResults | Where-Object { -not $_.Passed })
    Write-Host ''
    Write-Host ('Self-test cases: {0} total, {1} passed, {2} failed.' -f
        $script:TestResults.Count, ($script:TestResults.Count - $failed.Count), $failed.Count)
    Write-Host 'Claim boundary: guard behavior proven; no Party A ceremony was performed.'

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
    if ($PSCmdlet.ParameterSetName -eq 'Ceremony') {
        if ([string]::IsNullOrWhiteSpace($OutputDirectory)) {
            $OutputDirectory = Join-Path -Path ([System.Environment]::GetFolderPath(
                    [System.Environment+SpecialFolder]::LocalApplicationData)) `
                -ChildPath 'CVF\ACEL_G1\party_a_key'
        }
        if ([string]::IsNullOrWhiteSpace($KeyId)) {
            $KeyId = 'partya-{0}' -f ([System.Guid]::NewGuid().ToString('N').Substring(0, 16))
        }
        [void](Invoke-KeyCeremony -ExpectedAccountName $ExpectedAccountName `
                -ExpectedAccountSid $ExpectedAccountSid -OutputDirectory $OutputDirectory `
                -KeyId $KeyId -ValidityDays $ValidityDays)
        exit 0
    }

    exit (Invoke-SelfTest)
} catch {
    # Guard failures already carry their own "[GUARD_ID] " prefix; only an
    # unexpected exception needs one added.
    $message = if ($_.Exception -is [CeremonyGuardFailure]) {
        $_.Exception.Message
    } else {
        '[UNHANDLED] {0}' -f $_.Exception.Message
    }
    Write-Error $message
    exit 1
}
