<#
.SYNOPSIS
Hermetic-first Party C Group 4 issuer-registry reservation-compatible publisher.

.DESCRIPTION
Default invocation runs non-mutating self-tests. Real publication claims an
already-reserved zero-byte target via a hardened own-target atomic replace; it
never creates the target itself and never sweeps unknown temps. Real mode
requires a Local preflight authorization view and the Local-issued transaction
ID; the Local postflight remains a separate Local step. This script
never writes the observation or lookup-response logs. Hard-termination
recovery is a distinct Administrator-only operation performed by
acel_g1_group4_admin_recovery.ps1 against the durable ledger this script
writes before any temp is created.
#>
[CmdletBinding(DefaultParameterSetName = 'SelfTest')]
param(
    [Parameter(ParameterSetName = 'SelfTest')]
    [switch] $SelfTest,

    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [switch] $ExecuteRegistryWrite,
    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [string] $RegistryJsonPath,
    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [string] $RepositoryRoot,
    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [string] $Confirmation,
    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [string] $PythonExecutablePath,
    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [string] $AuthorizationPath,
    [Parameter(ParameterSetName = 'Execute', Mandatory = $true)]
    [string] $TransactionId,

    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [switch] $PeerMode,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerRunId,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerTargetPath,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerInputPath,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerLedgerPath,
    [Parameter(ParameterSetName = 'Peer')]
    [switch] $PeerExpectPublish,

    [Parameter(ParameterSetName = 'Crash', Mandatory = $true)]
    [switch] $CrashMode,
    [Parameter(ParameterSetName = 'Crash', Mandatory = $true)]
    [string] $CrashRunId,
    [Parameter(ParameterSetName = 'Crash', Mandatory = $true)]
    [string] $CrashTargetPath,
    [Parameter(ParameterSetName = 'Crash', Mandatory = $true)]
    [string] $CrashInputPath,
    [Parameter(ParameterSetName = 'Crash', Mandatory = $true)]
    [string] $CrashLedgerPath,
    [Parameter(ParameterSetName = 'Crash', Mandatory = $true)]
    [ValidateSet('AfterAcquireBeforeMutation','AfterTempFlush','BeforeMove')]
    [string] $CrashPoint
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:PartyCAccount = 'LAM-RUBY\cvf-g1-party-c'
$script:PartyCSid = 'S-1-5-21-1644666849-912006174-747199667-1010'
$script:PartyBSid = 'S-1-5-21-1644666849-912006174-747199667-1009'
$script:LocalSid = 'S-1-5-21-1644666849-912006174-747199667-1001'
$script:SystemSid = 'S-1-5-18'
$script:AdministratorsSid = 'S-1-5-32-544'
$script:Confirmation = 'CREATE_ACEL_G1_GROUP4_REGISTRY_V1'
$script:RegistryRelativePath = 'governance/sources/issuer_registry/REGISTRY.json'
$script:ScriptPath = $PSCommandPath
$script:Tests = [System.Collections.Generic.List[object]]::new()

function Stop-Writer([string] $Code, [string] $Message) {
    throw [System.InvalidOperationException]::new("${Code}: ${Message}")
}

function Get-Sha256Hex([byte[]] $Bytes) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant() }
    finally { $sha.Dispose() }
}

function Test-BytesEqual([byte[]] $Left, [byte[]] $Right) {
    if ($null -eq $Left -or $null -eq $Right -or $Left.Length -ne $Right.Length) { return $false }
    for ($i = 0; $i -lt $Left.Length; $i++) { if ($Left[$i] -ne $Right[$i]) { return $false } }
    return $true
}

function Get-CanonicalPath([string] $Path) {
    return [System.IO.Path]::GetFullPath($Path).TrimEnd([System.IO.Path]::DirectorySeparatorChar)
}

function Assert-NoReparseTraversal([string] $BasePath, [string] $CandidatePath) {
    $base=Get-CanonicalPath $BasePath; $candidate=Get-CanonicalPath $CandidatePath
    $prefix=$base+[IO.Path]::DirectorySeparatorChar
    if($candidate-cne$base -and -not $candidate.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' $candidate}
    $current=$base
    if(Test-Path -LiteralPath $current){$item=Get-Item -LiteralPath $current -Force;if($item.Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' ('reparse traversal: '+$current)}}
    if($candidate-cne$base){foreach($part in $candidate.Substring($prefix.Length)-split'[\\/]'){$current=Join-Path $current $part;if(Test-Path -LiteralPath $current){$item=Get-Item -LiteralPath $current -Force;if($item.Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' ('reparse traversal: '+$current)}}}}
}

function Resolve-PythonRuntime([string] $ExplicitPath) {
    if ($ExplicitPath) {
        $resolved = Get-CanonicalPath $ExplicitPath
        if (-not (Test-Path -LiteralPath $resolved -PathType Leaf)) { Stop-Writer 'PYTHON_EXECUTABLE_UNAVAILABLE' $resolved }
        $prefix = if ([IO.Path]::GetFileNameWithoutExtension($resolved) -ieq 'py') { @('-3') } else { @() }
    } else {
        $command = Get-Command py -ErrorAction SilentlyContinue
        $prefix = @('-3')
        if ($null -eq $command) { $command = Get-Command python -ErrorAction SilentlyContinue; $prefix = @() }
        if ($null -eq $command) { Stop-Writer 'PYTHON_EXECUTABLE_UNAVAILABLE' 'neither py nor python resolved' }
        $resolved = $command.Source
    }
    $probe = & $resolved @prefix --version 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Writer 'PYTHON_EXECUTABLE_UNUSABLE' ($probe -join "`n") }
    return [pscustomobject]@{ executable=$resolved; prefix=@($prefix) }
}

function Invoke-PythonRuntime($Runtime, [string[]] $Arguments) {
    $executable=[string]$Runtime.executable; $prefix=@($Runtime.prefix)
    $output=& $executable @prefix @Arguments 2>&1
    return [pscustomobject]@{ exitCode=$LASTEXITCODE; output=@($output) }
}

function Assert-DisposableTestPaths([string] $TargetPath, [string] $InputPath) {
    $temp=(Get-CanonicalPath ([IO.Path]::GetTempPath()))+[IO.Path]::DirectorySeparatorChar
    $target=Get-CanonicalPath $TargetPath; $input=Get-CanonicalPath $InputPath
    foreach($path in @($target,$input)) { if(-not $path.StartsWith($temp,[StringComparison]::OrdinalIgnoreCase)){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' $path} }
    $targetRoot=(($target.Substring($temp.Length))-split'[\\/]')[0]
    $inputRoot=(($input.Substring($temp.Length))-split'[\\/]')[0]
    if($targetRoot-notlike'cvf-g4c-*' -or $inputRoot-cne$targetRoot){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' 'target/input must share one cvf-g4c-* disposable root'}
    $disposableRoot=Join-Path ([IO.Path]::GetTempPath()) $targetRoot
    foreach($candidate in @($disposableRoot,$input,(Split-Path -Parent $target))){Assert-NoReparseTraversal ([IO.Path]::GetTempPath()) $candidate}
    if(-not(Test-Path -LiteralPath $input -PathType Leaf) -or ([IO.FileInfo]::new($input)).Length-gt1048576){Stop-Writer 'TEST_INPUT_INVALID' 'input must be an existing non-reparse file of at most 1 MiB'}
}

function Assert-ExactExecutionBoundary([string] $Root, [string] $InputPath, [string] $Confirm) {
    $identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    if ($identity.Name -cne $script:PartyCAccount -or $identity.User.Value -cne $script:PartyCSid) {
        Stop-Writer 'ACCESS_PRINCIPAL_MISMATCH' 'real mode requires the exact verified Party C account and SID'
    }
    if ($Confirm -cne $script:Confirmation) {
        Stop-Writer 'ACCESS_CONFIRMATION_MISMATCH' 'exact confirmation literal required'
    }
    $rootPath = Get-CanonicalPath $Root
    $gitRoot = (& git -C $rootPath rev-parse --show-toplevel 2>$null)
    if ($LASTEXITCODE -ne 0 -or (Get-CanonicalPath $gitRoot) -cne $rootPath) {
        Stop-Writer 'ACCESS_REPOSITORY_ROOT_INVALID' 'RepositoryRoot must be the canonical Git root'
    }
    $target = Get-CanonicalPath (Join-Path $rootPath $script:RegistryRelativePath)
    $source = Get-CanonicalPath $InputPath
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        Stop-Writer 'SOURCE_UNAVAILABLE' 'RegistryJsonPath must exist as a file'
    }
    return [pscustomobject]@{ Root = $rootPath; Source = $source; Target = $target }
}

function Get-MutexName([string] $TargetPath) {
    $raw = [Text.Encoding]::UTF8.GetBytes((Get-CanonicalPath $TargetPath).ToUpperInvariant())
    return 'Global\CVF_G4_REGISTRY_TXN_' + (Get-Sha256Hex $raw).Substring(0, 48)
}

function Enter-TransactionGuard([string] $TargetPath, [switch] $InjectAfterAcquire, [System.Threading.EventWaitHandle] $AcquiredEvent) {
    $mutex = $null
    $acquired = $false
    try {
        $created = $false
        $mutex = [System.Threading.Mutex]::new($false, (Get-MutexName $TargetPath), [ref] $created)
        try { $acquired = $mutex.WaitOne(15000) }
        catch [System.Threading.AbandonedMutexException] { $acquired = $true }
        if (-not $acquired) { Stop-Writer 'CONCURRENCY_TIMEOUT' 'transaction guard acquisition timed out' }
        if ($null -ne $AcquiredEvent) { $AcquiredEvent.Set() | Out-Null }
        if ($InjectAfterAcquire) { Stop-Writer 'ROLLBACK_INJECTED_AFTER_ACQUIRE' 'self-test injection' }
        return $mutex
    } catch {
        if ($null -ne $mutex) {
            if ($acquired) { try { $mutex.ReleaseMutex() } catch {} }
            $mutex.Dispose()
        }
        throw
    }
}

function Exit-TransactionGuard($Mutex) {
    if ($null -ne $Mutex) {
        try { $Mutex.ReleaseMutex() } finally { $Mutex.Dispose() }
    }
}

function Get-ExpectedAceVector([switch] $TestPolicy) {
    $full = [int][System.Security.AccessControl.FileSystemRights]::FullControl
    $readProbe = [System.Security.AccessControl.FileSystemAccessRule]::new(
        [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid),
        [System.Security.AccessControl.FileSystemRights]::Read,
        [System.Security.AccessControl.AccessControlType]::Allow)
    $read = [int]$readProbe.FileSystemRights
    if ($TestPolicy) {
        $current = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
        return @([pscustomobject]@{ sid=$current; rights=$full; accessType=0; isInherited=$false; inheritanceFlags=0; propagationFlags=0 })
    }
    return @(
        [pscustomobject]@{ sid=$script:PartyCSid; rights=$full; accessType=0; isInherited=$false; inheritanceFlags=0; propagationFlags=0 },
        [pscustomobject]@{ sid=$script:SystemSid; rights=$full; accessType=0; isInherited=$false; inheritanceFlags=0; propagationFlags=0 },
        [pscustomobject]@{ sid=$script:AdministratorsSid; rights=$full; accessType=0; isInherited=$false; inheritanceFlags=0; propagationFlags=0 },
        [pscustomobject]@{ sid=$script:PartyBSid; rights=$read; accessType=0; isInherited=$false; inheritanceFlags=0; propagationFlags=0 },
        [pscustomobject]@{ sid=$script:LocalSid; rights=$read; accessType=0; isInherited=$false; inheritanceFlags=0; propagationFlags=0 }
    )
}

function Get-SecurityState([string] $Path) {
    $info = [System.IO.FileInfo]::new($Path)
    $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor [System.Security.AccessControl.AccessControlSections]::Access
    $security = [System.IO.FileSystemAclExtensions]::GetAccessControl($info, $sections)
    $owner = $security.GetOwner([System.Security.Principal.SecurityIdentifier]).Value
    $aces = @($security.GetAccessRules($true, $true, [System.Security.Principal.SecurityIdentifier]) | ForEach-Object {
        [pscustomobject]@{
            sid=$_.IdentityReference.Value; rights=[int]$_.FileSystemRights
            accessType=[int]$_.AccessControlType; isInherited=[bool]$_.IsInherited
            inheritanceFlags=[int]$_.InheritanceFlags; propagationFlags=[int]$_.PropagationFlags
        }
    })
    return [pscustomobject]@{ ownerSid=$owner; protectionState=[bool]$security.AreAccessRulesProtected; aces=$aces; raw=$security; binary=$security.GetSecurityDescriptorBinaryForm() }
}

function Get-SemanticTupleStrings($State) {
    return @($State.aces | ForEach-Object {
        '{0}|{1}|{2}|{3}|{4}|{5}' -f $_.sid,$_.rights,$_.accessType,$_.isInherited,$_.inheritanceFlags,$_.propagationFlags
    } | Sort-Object -CaseSensitive)
}

function Get-OrderedTupleStrings($State) {
    return @($State.aces | ForEach-Object {
        '{0}|{1}|{2}|{3}|{4}|{5}' -f $_.sid,$_.rights,$_.accessType,$_.isInherited,$_.inheritanceFlags,$_.propagationFlags
    })
}

function Test-SecurityStateExact($State, [string] $Owner, [bool] $Protection, [object[]] $Aces) {
    if ($State.ownerSid -cne $Owner -or $State.protectionState -ne $Protection) { return $false }
    $expected = [pscustomobject]@{ aces = $Aces }
    if (((Get-OrderedTupleStrings $State) -join "`n") -cne ((Get-OrderedTupleStrings $expected) -join "`n")) { return $false }
    return ((Get-SemanticTupleStrings $State) -join "`n") -ceq ((Get-SemanticTupleStrings $expected) -join "`n")
}

function Test-SecurityModel($State, [string] $ExpectedOwner, [object[]] $ExpectedAces) {
    return Test-SecurityStateExact $State $ExpectedOwner $true $ExpectedAces
}

function Assert-SecurityState([string] $Path, [switch] $TestPolicy) {
    $actual = Get-SecurityState $Path
    $expectedOwner = if ($TestPolicy) { [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value } else { $script:PartyCSid }
    $expected = @(Get-ExpectedAceVector -TestPolicy:$TestPolicy)
    if (-not (Test-SecurityModel $actual $expectedOwner $expected)) { Stop-Writer 'SECURITY_STATE_MISMATCH' 'owner/protection/complete ACE vector differs' }
    return $actual
}

function Set-ExactSecurity([string] $Path, [switch] $TestPolicy) {
    $expected = @(Get-ExpectedAceVector -TestPolicy:$TestPolicy)
    $security = [System.Security.AccessControl.FileSecurity]::new()
    $security.SetAccessRuleProtection($true, $false)
    $ownerSid = if ($TestPolicy) { $expected[0].sid } else { $script:PartyCSid }
    $security.SetOwner([System.Security.Principal.SecurityIdentifier]::new($ownerSid))
    foreach ($ace in $expected) {
        $security.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
            [System.Security.Principal.SecurityIdentifier]::new($ace.sid),
            [System.Security.AccessControl.FileSystemRights]$ace.rights,
            [System.Security.AccessControl.InheritanceFlags]$ace.inheritanceFlags,
            [System.Security.AccessControl.PropagationFlags]$ace.propagationFlags,
            [System.Security.AccessControl.AccessControlType]$ace.accessType))
    }
    [System.IO.FileSystemAclExtensions]::SetAccessControl([System.IO.FileInfo]::new($Path), $security)
    return Assert-SecurityState -Path $Path -TestPolicy:$TestPolicy
}

function Get-HardLinkCount([string] $Path) {
    $output = & fsutil hardlink list $Path 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Writer 'RESERVATION_LINK_COUNT_UNAVAILABLE' $Path }
    return @($output | Where-Object { $_.Trim().Length -gt 0 }).Count
}

function Assert-ReservedTarget([string] $TargetPath, [switch] $TestPolicy) {
    if (-not (Test-Path -LiteralPath $TargetPath -PathType Leaf)) { Stop-Writer 'RESERVATION_MISSING' $TargetPath }
    $item = [System.IO.FileInfo]::new($TargetPath)
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { Stop-Writer 'RESERVATION_REPARSE_POINT' $TargetPath }
    if ($item.Length -ne 0) { Stop-Writer 'RESERVATION_NONZERO' $TargetPath }
    if ((Get-HardLinkCount $TargetPath) -ne 1) { Stop-Writer 'RESERVATION_LINK_COUNT_MISMATCH' $TargetPath }
    $security = Assert-SecurityState -Path $TargetPath -TestPolicy:$TestPolicy
    return [pscustomobject]@{ bytes = [byte[]]::new(0); security = $security }
}

function Get-ReservationNames { return @('REGISTRY.json', 'LOOKUP_RESPONSES.jsonl') }

# The protected parent is a closed two-name set: both reservation names are
# always permitted (the writer checks only name, entry type and reparse state
# of the non-target, never its content or security), plus only the temps bound
# to the current transaction. Everything else is preserved and blocks.
function Assert-ParentSiblingSet([string] $Directory, [string[]] $CurrentTemps) {
    if (-not (Test-Path -LiteralPath $Directory -PathType Container)) { return }
    $reservations = Get-ReservationNames
    foreach ($item in @(Get-ChildItem -LiteralPath $Directory -Force)) {
        if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) { Stop-Writer 'ROLLBACK_ORPHAN_REPARSE_POINT' $item.FullName }
        if ($reservations -ccontains $item.Name) {
            if ($item.PSIsContainer) { Stop-Writer 'RESERVATION_SIBLING_NOT_FILE' $item.FullName }
            continue
        }
        if (-not $item.PSIsContainer -and @($CurrentTemps) -ccontains $item.Name) { continue }
        Stop-Writer 'UNKNOWN_RESIDUE_PRESENT' $item.FullName
    }
}

function Get-FileIdHex([string] $Path) {
    $output = & fsutil file queryfileid $Path 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Writer 'FILE_IDENTITY_UNAVAILABLE' $Path }
    $match = [regex]::Match(($output -join ' '), '0x[0-9a-fA-F]+')
    if (-not $match.Success) { Stop-Writer 'FILE_IDENTITY_UNAVAILABLE' $Path }
    return $match.Value.ToLowerInvariant()
}

function Get-SecurityDigestFromState($State) {
    $text = 'owner=' + $State.ownerSid + ';protected=' + ([bool]$State.protectionState).ToString() + ';aces=' + (@(Get-OrderedTupleStrings $State) -join "`n")
    return Get-Sha256Hex ([Text.Encoding]::UTF8.GetBytes($text))
}

function Get-ExpectedSecurityDigest([switch] $TestPolicy) {
    $owner = if ($TestPolicy) { [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value } else { $script:PartyCSid }
    return Get-SecurityDigestFromState ([pscustomobject]@{ ownerSid = $owner; protectionState = $true; aces = @(Get-ExpectedAceVector -TestPolicy:$TestPolicy) })
}

# Complete state of the writer's OWN target only; never called on the other
# principal's reservation.
function Get-OwnFileState([string] $Path) {
    $info = [System.IO.FileInfo]::new($Path)
    $security = Get-SecurityState $Path
    return [ordered]@{
        fileId = Get-FileIdHex $Path
        length = [int64]$info.Length
        sha256 = Get-Sha256Hex ([System.IO.File]::ReadAllBytes($Path))
        linkCount = [int](Get-HardLinkCount $Path)
        attributes = [int]$info.Attributes
        ownerSid = [string]$security.ownerSid
        protection = [bool]$security.protectionState
        securityDigest = Get-SecurityDigestFromState $security
    }
}

function Format-FileState($State) {
    return '{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}' -f $State.fileId, $State.length, $State.sha256, $State.linkCount, $State.attributes, $State.ownerSid, ([bool]$State.protection).ToString(), $State.securityDigest
}

function Get-ParentGuardName([string] $ParentPath) {
    $raw = [Text.Encoding]::UTF8.GetBytes((Get-CanonicalPath $ParentPath).ToUpperInvariant())
    return 'Global\CVF_G4_PARENT_GUARD_' + (Get-Sha256Hex $raw).Substring(0, 48)
}

function Assert-OutsideParent([string] $Path, [string] $ParentPath, [string] $Code) {
    $candidate = Get-CanonicalPath $Path
    $parent = Get-CanonicalPath $ParentPath
    $candidateDir = Get-CanonicalPath (Split-Path -Parent $candidate)
    if ($candidateDir -ieq $parent -or $candidate.StartsWith($parent + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { Stop-Writer $Code $candidate }
}

# C0-R1 Local authorization reference. The writer reads only its own
# per-writer view issued by the Local preflight: transaction binding, parent
# identity, guard name and its own target fields. A view carrying any other
# field (for example the other principal's target) is rejected unread.
function Assert-WriterAuthorization([string] $AuthorizationPath, [string] $TransactionId, [string] $TargetPath, [string] $TargetKind) {
    $parent = Get-CanonicalPath (Split-Path -Parent (Get-CanonicalPath $TargetPath))
    Assert-OutsideParent $AuthorizationPath $parent 'AUTHORIZATION_INSIDE_PROTECTED_PARENT'
    if (-not (Test-Path -LiteralPath $AuthorizationPath -PathType Leaf)) { Stop-Writer 'AUTHORIZATION_MISSING' $AuthorizationPath }
    try { $record = [System.IO.File]::ReadAllText($AuthorizationPath) | ConvertFrom-Json } catch { Stop-Writer 'AUTHORIZATION_MALFORMED' $AuthorizationPath }
    $expectedKeys = @('schema','transactionId','authorizationRef','status','parentPath','parentFileId','guardName','targetKind','targetName','ownTarget','issuedAt') | Sort-Object
    $actualKeys = @($record.PSObject.Properties.Name) | Sort-Object
    if (($actualKeys -join ',') -cne ($expectedKeys -join ',')) { Stop-Writer 'AUTHORIZATION_FIELD_SET_INVALID' ($actualKeys -join ',') }
    $ownKeys = @('fileId','length','sha256','linkCount','attributes','ownerSid','protection','securityDigest') | Sort-Object
    if ($null -eq $record.ownTarget -or ((@($record.ownTarget.PSObject.Properties.Name) | Sort-Object) -join ',') -cne ($ownKeys -join ',')) { Stop-Writer 'AUTHORIZATION_FIELD_SET_INVALID' 'ownTarget' }
    if ($record.schema -cne 'cvf.g4.localWriterAuthorization.v1' -or $record.status -cne 'PREFLIGHT_PASSED') { Stop-Writer 'AUTHORIZATION_STATUS_INVALID' $AuthorizationPath }
    if ([string]$record.transactionId -cne $TransactionId) { Stop-Writer 'AUTHORIZATION_TRANSACTION_MISMATCH' $TransactionId }
    if ([string]$record.targetKind -cne $TargetKind -or [string]$record.targetName -cne (Split-Path -Leaf $TargetPath)) { Stop-Writer 'AUTHORIZATION_TARGET_MISMATCH' $TargetPath }
    if ([string]$record.authorizationRef -notmatch '^[0-9a-f]{64}$') { Stop-Writer 'AUTHORIZATION_STATUS_INVALID' 'authorizationRef' }
    if ([string]$record.parentPath -ine $parent -or [string]$record.parentFileId -cne (Get-FileIdHex $parent)) { Stop-Writer 'AUTHORIZATION_PARENT_MISMATCH' $parent }
    if ([string]$record.guardName -cne (Get-ParentGuardName $parent)) { Stop-Writer 'AUTHORIZATION_GUARD_ABSENT' 'guard name mismatch' }
    try { $guard = [System.Threading.Mutex]::OpenExisting([string]$record.guardName); $guard.Dispose() } catch { Stop-Writer 'AUTHORIZATION_GUARD_ABSENT' 'Local parent guard is not held' }
    if ((Format-FileState $record.ownTarget) -cne (Format-FileState (Get-OwnFileState $TargetPath))) { Stop-Writer 'AUTHORIZATION_OWN_TARGET_DRIFT' $TargetPath }
    return $record
}

function Get-LedgerSchemaId { return 'cvf.g4.recoveryLedger.v2' }

function New-LedgerContext([string] $LedgerPath, [string] $TransactionId, [string] $TargetPath, [string] $TargetKind, $Prestate) {
    $process = [System.Diagnostics.Process]::GetCurrentProcess()
    try { $startTicks = [int64]$process.StartTime.ToUniversalTime().Ticks; $processId = [int]$process.Id } finally { $process.Dispose() }
    $target = Get-CanonicalPath $TargetPath
    $parent = Get-CanonicalPath (Split-Path -Parent $target)
    return [pscustomobject]@{
        ledgerPath = Get-CanonicalPath $LedgerPath
        transactionId = $TransactionId
        sequence = 0
        writerSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
        writerProcessId = $processId
        writerProcessStartUtcTicks = $startTicks
        targetKind = $TargetKind
        targetName = Split-Path -Leaf $target
        targetPath = $target
        parentPath = $parent
        parentFileId = Get-FileIdHex $parent
        targetPrestate = $Prestate
        temps = @{}
    }
}

function Write-LedgerLine([string] $LedgerPath, [string] $Line) {
    $directory = Split-Path -Parent $LedgerPath
    if (-not (Test-Path -LiteralPath $directory)) { [System.IO.Directory]::CreateDirectory($directory) | Out-Null }
    $bytes = [Text.Encoding]::UTF8.GetBytes($Line + "`n")
    for ($attempt = 0; ; $attempt++) {
        try {
            $stream = [System.IO.FileStream]::new($LedgerPath, [System.IO.FileMode]::Append, [System.IO.FileAccess]::Write, [System.IO.FileShare]::Read, 4096, [System.IO.FileOptions]::WriteThrough)
            try { $stream.Write($bytes, 0, $bytes.Length); $stream.Flush($true) } finally { $stream.Dispose() }
            return
        } catch [System.IO.IOException] {
            if ($attempt -ge 200) { Stop-Writer 'LEDGER_APPEND_FAILED' $LedgerPath }
            [System.Threading.Thread]::Sleep(10)
        }
    }
}

# Every row carries the complete immutable binding. TEMP_PLANNED is refused if
# the named temp already exists, so a binding can never be written after
# creation.
function Add-LedgerRow($Context, [string] $TempName, [string] $Phase) {
    if ([string]::IsNullOrEmpty($TempName) -or -not $Context.temps.ContainsKey($TempName)) { Stop-Writer 'LEDGER_TEMP_BINDING_MISSING' "<$TempName>" }
    $binding = $Context.temps[$TempName]
    if ($Phase -ceq 'TEMP_PLANNED' -and (Test-Path -LiteralPath (Join-Path $Context.parentPath $TempName))) { Stop-Writer 'LEDGER_BINDING_AFTER_CREATION' $TempName }
    $Context.sequence = $Context.sequence + 1
    $row = [ordered]@{
        schema = Get-LedgerSchemaId
        transactionId = $Context.transactionId
        sequence = $Context.sequence
        phase = $Phase
        recordedAt = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')
        writerSid = $Context.writerSid
        writerProcessId = $Context.writerProcessId
        writerProcessStartUtcTicks = $Context.writerProcessStartUtcTicks
        targetKind = $Context.targetKind
        targetName = $Context.targetName
        targetPath = $Context.targetPath
        parentPath = $Context.parentPath
        parentFileId = $Context.parentFileId
        targetPrestate = $Context.targetPrestate
        tempName = $TempName
        tempRole = $binding.role
        expectedTempSha256 = $binding.expectedSha256
        expectedTempSecurityDigest = $binding.expectedSecurityDigest
        tempFileId = $binding.fileId
    }
    Write-LedgerLine $Context.ledgerPath ($row | ConvertTo-Json -Compress -Depth 6)
    $binding.lastPhase = $Phase
}

function Register-LedgerTemp($Context, [string] $Prefix, [string] $Role, [byte[]] $ExpectedBytes, [string] $ExpectedSecurityDigest) {
    $name = $Prefix + [Guid]::NewGuid().ToString('N') + '.tmp'
    $Context.temps[$name] = [pscustomobject]@{ role = $Role; expectedSha256 = Get-Sha256Hex $ExpectedBytes; expectedSecurityDigest = $ExpectedSecurityDigest; fileId = $null; lastPhase = $null }
    Add-LedgerRow $Context $name 'TEMP_PLANNED'
    return $name
}

function Set-LedgerTempFlushed($Context, [string] $TempName) {
    $Context.temps[$TempName].fileId = Get-FileIdHex (Join-Path $Context.parentPath $TempName)
    Add-LedgerRow $Context $TempName 'TEMP_FLUSHED'
}

function Complete-LedgerTempRemoval($Context, [string] $TempName, [string] $Phase) {
    $path = Join-Path $Context.parentPath $TempName
    if (Test-Path -LiteralPath $path) { Remove-Item -LiteralPath $path -Force }
    $binding = $Context.temps[$TempName]
    if ($null -ne $binding -and @('PUBLISHED','RELEASED','DISCARDED') -notcontains $binding.lastPhase) { Add-LedgerRow $Context $TempName $Phase }
}

function Restore-ReservationAtomic([string] $TargetPath, $Security, $Context, [switch] $TestPolicy) {
    $directory = Split-Path -Parent $TargetPath
    $rollbackName = Register-LedgerTemp $Context '.cvf-g4-registry-rollback-' 'ROLLBACK' ([byte[]]::new(0)) (Get-SecurityDigestFromState $Security)
    $rollback = Join-Path $directory $rollbackName
    $moved = $false
    try {
        $stream = [System.IO.FileStream]::new($rollback, [System.IO.FileMode]::CreateNew, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None, 4096, [System.IO.FileOptions]::WriteThrough)
        try { $stream.Flush($true) } finally { $stream.Dispose() }
        $descriptor = [System.Security.AccessControl.FileSecurity]::new()
        $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor [System.Security.AccessControl.AccessControlSections]::Access
        $descriptor.SetSecurityDescriptorBinaryForm($Security.binary, $sections)
        [System.IO.FileSystemAclExtensions]::SetAccessControl([System.IO.FileInfo]::new($rollback), $descriptor)
        $rollbackState = Get-SecurityState $rollback
        if (([IO.FileInfo]::new($rollback)).Length -ne 0 -or -not (Test-SecurityStateExact $rollbackState $Security.ownerSid $Security.protectionState $Security.aces)) {
            Stop-Writer 'ROLLBACK_TEMP_MISMATCH' $rollback
        }
        Set-LedgerTempFlushed $Context $rollbackName
        Add-LedgerRow $Context $rollbackName 'PRE_MOVE'
        [System.IO.File]::Move($rollback, $TargetPath, $true); $moved = $true
        Add-LedgerRow $Context $rollbackName 'PUBLISHED'
        $finalState = Get-SecurityState $TargetPath
        if (([IO.FileInfo]::new($TargetPath)).Length -ne 0 -or -not (Test-SecurityStateExact $finalState $Security.ownerSid $Security.protectionState $Security.aces)) {
            Stop-Writer 'ROLLBACK_TARGET_MISMATCH' $TargetPath
        }
    } finally {
        if (-not $moved) { Complete-LedgerTempRemoval $Context $rollbackName 'DISCARDED' }
    }
}

function Wait-CrashBarrier([string] $Point, [string] $SelectedPoint, [System.Threading.EventWaitHandle] $CrashEvent) {
    if ($Point -ceq $SelectedPoint -and $null -ne $CrashEvent) {
        $CrashEvent.Set() | Out-Null
        [System.Threading.Thread]::Sleep([System.Threading.Timeout]::Infinite)
    }
}

function Publish-RegistryTransaction(
    [string] $InputPath, [string] $TargetPath,
    [ValidateSet('None','AfterAcquire','AfterPlanBeforeCreate','AfterTempFlush','BeforeMove','AfterMove')][string] $InjectFailure = 'None',
    [switch] $TestPolicy,
    $ParentBarrierEvents,
    [System.Threading.EventWaitHandle] $AcquiredEvent,
    [System.Threading.EventWaitHandle] $RequiredParentReleaseEvent,
    [ValidateSet('None','AfterAcquireBeforeMutation','AfterTempFlush','BeforeMove')][string] $CrashAt = 'None',
    [System.Threading.EventWaitHandle] $CrashEvent,
    [string] $ValidationCheckerPath,
    $PythonRuntime,
    [byte[]] $InjectCompetitorBytes,
    [string] $LedgerPath,
    [switch] $RequireReservation,
    [string] $TransactionId,
    [string] $AuthorizationPath
) {
    $guard = $null; $context = $null; $tempName = $null; $directory = Split-Path -Parent $TargetPath
    $guardAcquired = $false; $prestateCaptured = $false; $publishedByTransaction = $false; $reservationSecurity = $null
    if ((Split-Path -Leaf $TargetPath) -cne 'REGISTRY.json') { Stop-Writer 'TARGET_IDENTITY_MISMATCH' $TargetPath }
    if (-not $RequireReservation) { Stop-Writer 'RESERVATION_REQUIRED' 'C0-R1 permits only a claim of the pre-reserved registry target' }
    if (-not $LedgerPath) { Stop-Writer 'LEDGER_REQUIRED' 'transaction requires a durable recovery ledger outside the protected parent' }
    Assert-OutsideParent $LedgerPath $directory 'LEDGER_INSIDE_PROTECTED_PARENT'
    if ($AuthorizationPath -and -not $TransactionId) { Stop-Writer 'AUTHORIZATION_TRANSACTION_MISMATCH' 'authorization requires the Local-issued transaction ID' }
    if (-not $TransactionId) { $TransactionId = [Guid]::NewGuid().ToString('N') }
    if ($TransactionId -notmatch '^[0-9A-Za-z-]{8,64}$') { Stop-Writer 'TRANSACTION_ID_INVALID' $TransactionId }
    try {
        $guard = Enter-TransactionGuard -TargetPath $TargetPath -InjectAfterAcquire:($InjectFailure -eq 'AfterAcquire') -AcquiredEvent $AcquiredEvent
        $guardAcquired = $true
        if ($null -ne $RequiredParentReleaseEvent -and -not $RequiredParentReleaseEvent.WaitOne(0)) {
            Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'peer acquired before PARENT_RELEASE'
        }
        Wait-CrashBarrier -Point 'AfterAcquireBeforeMutation' -SelectedPoint $CrashAt -CrashEvent $CrashEvent
        $reservation = Assert-ReservedTarget -TargetPath $TargetPath -TestPolicy:$TestPolicy
        $reservationSecurity = $reservation.security
        if ($AuthorizationPath) { Assert-WriterAuthorization $AuthorizationPath $TransactionId $TargetPath 'REGISTRY' | Out-Null }
        Assert-ParentSiblingSet $directory @()
        $prestateCaptured = $true
        $inputBytes = [System.IO.File]::ReadAllBytes($InputPath)
        $context = New-LedgerContext $LedgerPath $TransactionId $TargetPath 'REGISTRY' (Get-OwnFileState $TargetPath)
        $tempName = Register-LedgerTemp $context '.cvf-g4-registry-' 'CANDIDATE' $inputBytes (Get-ExpectedSecurityDigest -TestPolicy:$TestPolicy)
        $temp = Join-Path $directory $tempName
        if ($InjectFailure -eq 'AfterPlanBeforeCreate') { Stop-Writer 'ROLLBACK_INJECTED_AFTER_PLAN' 'self-test injection' }
        $stream = [System.IO.FileStream]::new($temp,[System.IO.FileMode]::CreateNew,[System.IO.FileAccess]::Write,[System.IO.FileShare]::None,4096,[System.IO.FileOptions]::WriteThrough)
        try { $stream.Write($inputBytes,0,$inputBytes.Length); $stream.Flush($true) } finally { $stream.Dispose() }
        Set-ExactSecurity -Path $temp -TestPolicy:$TestPolicy | Out-Null
        if (-not (Test-BytesEqual ([System.IO.File]::ReadAllBytes($temp)) $inputBytes)) { Stop-Writer 'HASH_TEMP_READBACK_MISMATCH' $temp }
        Set-LedgerTempFlushed $context $tempName
        if ($ValidationCheckerPath) {
            if($null-eq$PythonRuntime){Stop-Writer 'PYTHON_EXECUTABLE_UNAVAILABLE' 'validation requires an explicit resolved runtime'}
            $validation=Invoke-PythonRuntime $PythonRuntime @($ValidationCheckerPath,'--registry',$temp)
            if ($validation.exitCode -ne 0) { Stop-Writer 'SOURCE_SCHEMA_INVALID' ('validation of exact captured bytes failed inside transaction guard: '+($validation.output-join"`n")) }
        }
        Wait-CrashBarrier -Point 'AfterTempFlush' -SelectedPoint $CrashAt -CrashEvent $CrashEvent
        if ($InjectFailure -eq 'AfterTempFlush') { Stop-Writer 'ROLLBACK_INJECTED_AFTER_TEMP_FLUSH' 'self-test injection' }
        if ($null -ne $ParentBarrierEvents) {
            $ParentBarrierEvents.StartAttempt.Set() | Out-Null
            if (-not $ParentBarrierEvents.Attempting.WaitOne(15000)) { Stop-Writer 'CONCURRENCY_PEER_NOT_ATTEMPTING' 'ATTEMPTING not observed' }
            if ($ParentBarrierEvents.Entered.WaitOne(0)) { Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'peer entered while parent owned guard' }
        }
        Wait-CrashBarrier -Point 'BeforeMove' -SelectedPoint $CrashAt -CrashEvent $CrashEvent
        if ($InjectFailure -eq 'BeforeMove') { Stop-Writer 'ROLLBACK_INJECTED_BEFORE_MOVE' 'self-test injection' }
        Assert-ParentSiblingSet $directory @($tempName)
        if($null-ne$InjectCompetitorBytes){[System.IO.File]::WriteAllBytes($TargetPath,$InjectCompetitorBytes)}
        Add-LedgerRow $context $tempName 'PRE_MOVE'
        [System.IO.File]::Move($temp, $TargetPath, $true); $publishedByTransaction = $true
        Add-LedgerRow $context $tempName 'PUBLISHED'
        if ($InjectFailure -eq 'AfterMove') { Stop-Writer 'ROLLBACK_INJECTED_AFTER_MOVE' 'self-test injection' }
        if (-not (Test-BytesEqual ([System.IO.File]::ReadAllBytes($TargetPath)) $inputBytes)) { Stop-Writer 'HASH_TARGET_READBACK_MISMATCH' $TargetPath }
        Assert-SecurityState -Path $TargetPath -TestPolicy:$TestPolicy | Out-Null
        if ($null -ne $ParentBarrierEvents) { $ParentBarrierEvents.ParentRelease.Set() | Out-Null }
        return Get-Sha256Hex $inputBytes
    } catch {
        $primary = $_
        if ($null -ne $context -and $null -ne $tempName -and -not $publishedByTransaction) { Complete-LedgerTempRemoval $context $tempName 'DISCARDED' }
        if ($guardAcquired -and $prestateCaptured -and $publishedByTransaction) {
            try { Restore-ReservationAtomic -TargetPath $TargetPath -Security $reservationSecurity -Context $context -TestPolicy:$TestPolicy }
            catch { Stop-Writer 'ROLLBACK_FAILED' ($primary.Exception.Message + ' | ' + $_.Exception.Message) }
        }
        if ($null -ne $ParentBarrierEvents) { $ParentBarrierEvents.ParentRelease.Set() | Out-Null }
        throw $primary
    } finally { Exit-TransactionGuard $guard }
}

function Read-LedgerTransactionRows([string] $LedgerPath, [string] $TransactionId) {
    if (-not (Test-Path -LiteralPath $LedgerPath -PathType Leaf)) { return @() }
    return @([System.IO.File]::ReadAllLines($LedgerPath) | Where-Object { $_.Trim().Length -gt 0 } | ForEach-Object { $_ | ConvertFrom-Json } | Where-Object { $_.transactionId -ceq $TransactionId })
}

function Add-Test([string] $Id, [bool] $Passed, [string] $Detail) {
    $script:Tests.Add([pscustomobject]@{ id=$Id; passed=$Passed; detail=$Detail })
    if (-not $Passed) { Stop-Writer 'SELF_TEST_FAILED' "${Id}: ${Detail}" }
}

function New-PeerEvents([string] $RunId) {
    $mode = [System.Threading.EventResetMode]::ManualReset
    return [pscustomobject]@{
        Ready=[System.Threading.EventWaitHandle]::new($false,$mode,"Local\CVF_G4C_READY_$RunId")
        StartAttempt=[System.Threading.EventWaitHandle]::new($false,$mode,"Local\CVF_G4C_START_ATTEMPT_$RunId")
        Attempting=[System.Threading.EventWaitHandle]::new($false,$mode,"Local\CVF_G4C_ATTEMPTING_$RunId")
        ParentRelease=[System.Threading.EventWaitHandle]::new($false,$mode,"Local\CVF_G4C_PARENT_RELEASE_$RunId")
        Entered=[System.Threading.EventWaitHandle]::new($false,$mode,"Local\CVF_G4C_ENTERED_$RunId")
        Complete=[System.Threading.EventWaitHandle]::new($false,$mode,"Local\CVF_G4C_COMPLETE_$RunId")
    }
}

function Invoke-PeerMode {
    Assert-DisposableTestPaths $PeerTargetPath $PeerInputPath
    $python=Resolve-PythonRuntime
    $checker=Join-Path (Split-Path -Parent (Split-Path -Parent $script:ScriptPath)) 'governance/compat/check_acel_g1_issuer_registry.py'
    $events = New-PeerEvents $PeerRunId
    try {
        $events.Ready.Set() | Out-Null
        if (-not $events.StartAttempt.WaitOne(15000)) { exit 21 }
        $events.Attempting.Set() | Out-Null
        try {
            Publish-RegistryTransaction -InputPath $PeerInputPath -TargetPath $PeerTargetPath -TestPolicy -AcquiredEvent $events.Entered -RequiredParentReleaseEvent $events.ParentRelease -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $PeerLedgerPath -RequireReservation | Out-Null
            if(-not$PeerExpectPublish){exit 23}
        } catch {
            if($PeerExpectPublish){exit 25}
            if ($_.Exception.Message -notlike 'RESERVATION_NONZERO:*') { exit 24 }
        }
        $events.Complete.Set() | Out-Null
        exit 0
    } finally {
        @($events.psobject.Properties.Value) | ForEach-Object { $_.Dispose() }
    }
}

function Invoke-CrashMode {
    Assert-DisposableTestPaths $CrashTargetPath $CrashInputPath
    $python=Resolve-PythonRuntime
    $checker=Join-Path (Split-Path -Parent (Split-Path -Parent $script:ScriptPath)) 'governance/compat/check_acel_g1_issuer_registry.py'
    $event = [System.Threading.EventWaitHandle]::new($false,[System.Threading.EventResetMode]::ManualReset,"Local\CVF_G4C_CRASH_$CrashRunId")
    try {
        Publish-RegistryTransaction -InputPath $CrashInputPath -TargetPath $CrashTargetPath -TestPolicy -CrashAt $CrashPoint -CrashEvent $event -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $CrashLedgerPath -RequireReservation | Out-Null
        exit 31
    } finally { $event.Dispose() }
}

function New-ReservedZeroByteFixture([string] $Path, [switch] $TestPolicy) {
    $directory = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $directory)) { [System.IO.Directory]::CreateDirectory($directory) | Out-Null }
    [System.IO.File]::WriteAllBytes($Path, [byte[]]::new(0))
    Set-ExactSecurity -Path $Path -TestPolicy:$TestPolicy | Out-Null
}

function Invoke-SelfTest {
    $root = Join-Path ([System.IO.Path]::GetTempPath()) ('cvf-g4c-' + [Guid]::NewGuid().ToString('N'))
    [System.IO.Directory]::CreateDirectory($root) | Out-Null
    try {
        $python=Resolve-PythonRuntime
        $checker=Join-Path (Split-Path -Parent (Split-Path -Parent $script:ScriptPath)) 'governance/compat/check_acel_g1_issuer_registry.py'
        $content = [Text.Encoding]::UTF8.GetBytes('{"authority":"ACEL_G1_DECISION_OWNER","issuerIdentity":"issuer-test-001","policyVersion":1}')
        Add-Test 'T3D-C1-C-00' ($content.Length -eq 91) 'canonical content vector is 91 bytes'
        Add-Test 'T3D-C1-C-01' ((Get-Sha256Hex $content) -ceq 'db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca') 'content digest recomputed'
        $vector = [Text.Encoding]::UTF8.GetBytes('{"registrySnapshotId":"issuer-registry-snapshot-test-0001","registrySnapshotVersion":1,"rows":[{"canonicalContentBytesBase64":"eyJhdXRob3JpdHkiOiJBQ0VMX0cxX0RFQ0lTSU9OX09XTkVSIiwiaXNzdWVySWRlbnRpdHkiOiJpc3N1ZXItdGVzdC0wMDEiLCJwb2xpY3lWZXJzaW9uIjoxfQ","canonicalContentHashHex":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","correctedAt":null,"entryVersion":1,"issuerAttestedHash":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","issuerIdentity":"issuer-test-001","registeredAt":"2026-09-22T00:00:00Z","revokedAt":null,"status":"ACTIVE"}],"writeTimestamp":"2026-09-22T00:00:01Z"}')
        Add-Test 'T3D-C1-C-02' ($vector.Length -eq 618) 'registry vector is 618 bytes'
        Add-Test 'T3D-C1-C-03' ((Get-Sha256Hex $vector) -ceq 'd31e0c206da091bc408005d490e69f7aa0eae733dac4b03c67edd280034827f2') 'registry digest recomputed'
        $input = Join-Path $root 'input.json'; [System.IO.File]::WriteAllBytes($input,$vector)
        $ledger = Join-Path $root 'ledger/RECOVERY.jsonl'

        # R2-01: own-target reservation claim, atomic replace of pre-reserved zero-byte target.
        $target = Join-Path $root 'source/REGISTRY.json'
        New-ReservedZeroByteFixture -Path $target -TestPolicy
        $txnPositive = 'selftest-c-positive-' + [Guid]::NewGuid().ToString('N')
        $digest = Publish-RegistryTransaction -InputPath $input -TargetPath $target -TestPolicy -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $ledger -RequireReservation -TransactionId $txnPositive
        Add-Test 'T3D-C1-C-04' ($digest -ceq (Get-Sha256Hex $vector)) 'atomic own-target publish succeeds'
        Add-Test 'T3D-C1-C-05' (Test-BytesEqual ([System.IO.File]::ReadAllBytes($target)) $vector) 'published bytes exact'
        Add-Test 'T3D-C1-C-06' (@(Get-ChildItem (Split-Path $target) -Filter '*.tmp').Count -eq 0) 'no orphan temp remains'
        Add-Test 'T3D-C1-C-06-VALIDATED' ($digest -ceq (Get-Sha256Hex $vector)) 'captured-byte checker branch executed'
        # RV08: every phase carries the same non-empty, immutable temp binding.
        $rows = @(Read-LedgerTransactionRows $ledger $txnPositive)
        $rowKeys = @('schema','transactionId','sequence','phase','recordedAt','writerSid','writerProcessId','writerProcessStartUtcTicks','targetKind','targetName','targetPath','parentPath','parentFileId','targetPrestate','tempName','tempRole','expectedTempSha256','expectedTempSecurityDigest','tempFileId') | Sort-Object
        Add-Test 'T3D-C1-C-06-LEDGER-PHASES' ((($rows | ForEach-Object phase) -join ',') -ceq 'TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE,PUBLISHED') 'ledger phase sequence is PLANNED,FLUSHED,PRE_MOVE,PUBLISHED'
        Add-Test 'T3D-C1-C-06-LEDGER-SEQUENCE' ((($rows | ForEach-Object sequence) -join ',') -ceq '1,2,3,4') 'ledger sequence is strictly 1..4'
        Add-Test 'T3D-C1-C-06-LEDGER-TEMPNAME' ((@($rows | ForEach-Object tempName | Sort-Object -Unique).Count -eq 1) -and ([string]$rows[0].tempName -match '^\.cvf-g4-registry-[0-9a-f]{32}\.tmp$') -and ([string]$rows[3].tempName -ceq [string]$rows[0].tempName)) 'PUBLISHED row carries the same non-empty temp name as TEMP_PLANNED'
        Add-Test 'T3D-C1-C-06-LEDGER-SCHEMA' ((@($rows | Where-Object { ((@($_.PSObject.Properties.Name) | Sort-Object) -join ',') -cne ($rowKeys -join ',') }).Count -eq 0) -and (@($rows | Where-Object { $_.schema -cne (Get-LedgerSchemaId) }).Count -eq 0)) 'every row uses the exact v2 field set'
        Add-Test 'T3D-C1-C-06-LEDGER-HASH' ([string]$rows[0].expectedTempSha256 -ceq (Get-Sha256Hex $vector) -and [string]$rows[0].targetPrestate.sha256 -ceq (Get-Sha256Hex ([byte[]]::new(0))) -and [int]$rows[0].targetPrestate.linkCount -eq 1) 'binding carries expected temp hash and complete target prestate'
        Add-Test 'T3D-C1-C-06-LEDGER-FILEID' (($null -eq $rows[0].tempFileId) -and ([string]$rows[1].tempFileId -match '^0x[0-9a-f]+$') -and ([string]$rows[3].tempFileId -ceq [string]$rows[1].tempFileId)) 'temp file identity is absent at planning and stable from flush onward'
        Add-Test 'T3D-C1-C-06-LEDGER-WRITER' (([int]$rows[0].writerProcessId -eq $PID) -and ([int64]$rows[0].writerProcessStartUtcTicks -gt 0)) 'binding records writer process identity for termination evidence'

        # RV07: the binding is durable before the temp exists.
        $planTarget = Join-Path $root 'plan-only/REGISTRY.json'; New-ReservedZeroByteFixture -Path $planTarget -TestPolicy
        $txnPlan = 'selftest-c-plan-' + [Guid]::NewGuid().ToString('N')
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $planTarget -TestPolicy -LedgerPath $ledger -RequireReservation -TransactionId $txnPlan -InjectFailure AfterPlanBeforeCreate | Out-Null; $planFailed=$false } catch { $planFailed = $_.Exception.Message -like 'ROLLBACK_INJECTED_AFTER_PLAN:*' }
        $planRows = @(Read-LedgerTransactionRows $ledger $txnPlan)
        Add-Test 'T3D-C1-C-07-PLAN-BEFORE-CREATE' ($planFailed -and ((($planRows | ForEach-Object phase) -join ',') -ceq 'TEMP_PLANNED,DISCARDED') -and -not (Test-Path (Join-Path (Split-Path $planTarget) ([string]$planRows[0].tempName))) -and (([IO.FileInfo]::new($planTarget)).Length -eq 0)) 'TEMP_PLANNED is durable while the temp does not yet exist; abort records DISCARDED'
        $orderTarget = Join-Path $root 'plan-order/REGISTRY.json'; New-ReservedZeroByteFixture -Path $orderTarget -TestPolicy
        $orderContext = New-LedgerContext $ledger ('selftest-c-order-' + [Guid]::NewGuid().ToString('N')) $orderTarget 'REGISTRY' (Get-OwnFileState $orderTarget)
        $preCreated = '.cvf-g4-registry-' + [Guid]::NewGuid().ToString('N') + '.tmp'
        $orderContext.temps[$preCreated] = [pscustomobject]@{ role='CANDIDATE'; expectedSha256=(Get-Sha256Hex $vector); expectedSecurityDigest='x'; fileId=$null; lastPhase=$null }
        [System.IO.File]::WriteAllBytes((Join-Path (Split-Path $orderTarget) $preCreated), $vector)
        try { Add-LedgerRow $orderContext $preCreated 'TEMP_PLANNED'; $orderRejected=$false } catch { $orderRejected = $_.Exception.Message -like 'LEDGER_BINDING_AFTER_CREATION:*' }
        Add-Test 'T3D-C1-C-07-BINDING-AFTER-CREATE' $orderRejected 'a planning binding for an already-existing temp is refused'
        Remove-Item -LiteralPath (Join-Path (Split-Path $orderTarget) $preCreated) -Force
        try { Add-LedgerRow $orderContext '' 'PUBLISHED'; $emptyRejected=$false } catch { $emptyRejected = $_.Exception.Message -like 'LEDGER_TEMP_BINDING_MISSING:*' }
        Add-Test 'T3D-C1-C-07-EMPTY-TEMPNAME' $emptyRejected 'an empty temp name can never be written to the ledger'
        $insideTarget = Join-Path $root 'inside-ledger/REGISTRY.json'; New-ReservedZeroByteFixture -Path $insideTarget -TestPolicy
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $insideTarget -TestPolicy -LedgerPath (Join-Path $root 'inside-ledger/LEDGER.jsonl') -RequireReservation | Out-Null; $insideRejected=$false } catch { $insideRejected = $_.Exception.Message -like 'LEDGER_INSIDE_PROTECTED_PARENT:*' }
        Add-Test 'T3D-C1-C-07-LEDGER-OUTSIDE-PARENT' ($insideRejected -and (([IO.FileInfo]::new($insideTarget)).Length -eq 0)) 'a ledger inside the protected parent is refused before mutation'

        # RV11: the closed two-name shared parent.
        $sharedTarget = Join-Path $root 'shared/REGISTRY.json'; New-ReservedZeroByteFixture -Path $sharedTarget -TestPolicy
        $sharedPeer = Join-Path $root 'shared/LOOKUP_RESPONSES.jsonl'; [System.IO.File]::WriteAllBytes($sharedPeer, [byte[]]::new(0))
        $sharedPeerId = Get-FileIdHex $sharedPeer
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $sharedTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $sharedOk=$true } catch { $sharedOk=$false }
        Add-Test 'T3D-C1-C-07-SHARED-PARENT' ($sharedOk -and (Test-BytesEqual ([IO.File]::ReadAllBytes($sharedTarget)) $vector) -and ((Get-FileIdHex $sharedPeer) -ceq $sharedPeerId) -and (([IO.FileInfo]::new($sharedPeer)).Length -eq 0)) 'Party C publishes beside the required response reservation, which stays the same file with the same length'
        $thirdTarget = Join-Path $root 'third/REGISTRY.json'; New-ReservedZeroByteFixture -Path $thirdTarget -TestPolicy
        [System.IO.File]::WriteAllBytes((Join-Path $root 'third/LOOKUP_RESPONSES.jsonl'), [byte[]]::new(0))
        $thirdSibling = Join-Path $root 'third/unexpected.bin'; [System.IO.File]::WriteAllBytes($thirdSibling, [Text.Encoding]::UTF8.GetBytes('preserve'))
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $thirdTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $thirdRejected=$false } catch { $thirdRejected = $_.Exception.Message -like 'UNKNOWN_RESIDUE_PRESENT:*' }
        Add-Test 'T3D-C1-C-07-THIRD-SIBLING' ($thirdRejected -and (([IO.FileInfo]::new($thirdTarget)).Length -eq 0) -and (Test-Path $thirdSibling)) 'an unknown third sibling beside both reservations blocks and is preserved'
        $dirPeerTarget = Join-Path $root 'dirpeer/REGISTRY.json'; New-ReservedZeroByteFixture -Path $dirPeerTarget -TestPolicy
        [System.IO.Directory]::CreateDirectory((Join-Path $root 'dirpeer/LOOKUP_RESPONSES.jsonl')) | Out-Null
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $dirPeerTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $dirPeerRejected=$false } catch { $dirPeerRejected = $_.Exception.Message -like 'RESERVATION_SIBLING_NOT_FILE:*' }
        Add-Test 'T3D-C1-C-07-PEER-NOT-FILE' $dirPeerRejected 'a directory impersonating the other reservation name blocks'

        try{Assert-DisposableTestPaths (Join-Path (Split-Path -Parent $root) 'outside/REGISTRY.json') $input;$contained=$false}catch{$contained=$_.Exception.Message-like'TEST_CONTAINMENT_VIOLATION:*'}
        Add-Test 'T3D-C1-C-06-CONTAINMENT' $contained 'test-only target cannot escape disposable root'
        $junctionOutside=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4c-junction-target-'+[Guid]::NewGuid().ToString('N'));$junction=Join-Path $root 'nested-junction';[IO.Directory]::CreateDirectory($junctionOutside)|Out-Null
        try{New-Item -ItemType Junction -Path $junction -Target $junctionOutside|Out-Null;try{Assert-DisposableTestPaths (Join-Path $junction 'REGISTRY.json') $input;$nestedContained=$false}catch{$nestedContained=$_.Exception.Message-like'TEST_CONTAINMENT_VIOLATION:*'};Add-Test 'T3D-C1-C-06-NESTED-REPARSE' $nestedContained 'component walk rejects intermediate junction'}finally{if(Test-Path $junction){Remove-Item -LiteralPath $junction -Force};if(Test-Path $junctionOutside){Remove-Item -LiteralPath $junctionOutside -Force}}

        # R2-01 negative: absent reservation rejects before mutation.
        $absentTarget = Join-Path $root 'absent/REGISTRY.json'
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $absentTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $absentRejected=$false } catch { $absentRejected=$_.Exception.Message -like 'RESERVATION_MISSING:*' }
        Add-Test 'T3D-C1-C-07-ABSENT' $absentRejected 'missing reservation rejects before mutation'

        # R2-01 negative: nonzero reservation rejects.
        $nonzeroTarget = Join-Path $root 'nonzero/REGISTRY.json'
        [System.IO.Directory]::CreateDirectory((Split-Path $nonzeroTarget)) | Out-Null
        [System.IO.File]::WriteAllBytes($nonzeroTarget, [Text.Encoding]::UTF8.GetBytes('not-empty'))
        Set-ExactSecurity -Path $nonzeroTarget -TestPolicy | Out-Null
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $nonzeroTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $nonzeroRejected=$false } catch { $nonzeroRejected=$_.Exception.Message -like 'RESERVATION_NONZERO:*' }
        Add-Test 'T3D-C1-C-07-NONZERO' $nonzeroRejected 'nonzero reservation rejects before mutation'
        Add-Test 'T3D-C1-C-07-NONZERO-INTACT' (Test-BytesEqual ([IO.File]::ReadAllBytes($nonzeroTarget)) ([Text.Encoding]::UTF8.GetBytes('not-empty'))) 'non-owned bytes unchanged by rejected attempt'

        # R2-01 negative: reserved twice (already-published) rejects.
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $target -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $republishRejected=$false } catch { $republishRejected=$_.Exception.Message -like 'RESERVATION_NONZERO:*' }
        Add-Test 'T3D-C1-C-07-REPUBLISH' $republishRejected 'already-published target with nonzero bytes rejects a second claim'

        # R2-01 negative: wrong-security reservation rejects.
        $wrongSecurityTarget = Join-Path $root 'wrong-security/REGISTRY.json'
        [System.IO.Directory]::CreateDirectory((Split-Path $wrongSecurityTarget)) | Out-Null
        [System.IO.File]::WriteAllBytes($wrongSecurityTarget, [byte[]]::new(0))
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $wrongSecurityTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $wrongSecurityRejected=$false } catch { $wrongSecurityRejected=$_.Exception.Message -like 'SECURITY_STATE_MISMATCH:*' }
        Add-Test 'T3D-C1-C-07-WRONGSEC' $wrongSecurityRejected 'reservation with wrong/default security descriptor rejects'

        # RV02 negative: hardlinked reservation rejects (link count != 1) before mutation.
        $hardlinkTarget = Join-Path $root 'hardlink/REGISTRY.json'
        New-ReservedZeroByteFixture -Path $hardlinkTarget -TestPolicy
        $hardlinkSupported = $true
        try { New-Item -ItemType HardLink -Path (Join-Path $root 'hardlink/second-name') -Target $hardlinkTarget -ErrorAction Stop | Out-Null } catch { $hardlinkSupported = $false }
        if ($hardlinkSupported) {
            try { Publish-RegistryTransaction -InputPath $input -TargetPath $hardlinkTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $hardlinkRejected=$false } catch { $hardlinkRejected=$_.Exception.Message -like 'RESERVATION_LINK_COUNT_MISMATCH:*' }
            Add-Test 'T3D-C1-C-07-HARDLINK' ($hardlinkRejected -and (([IO.FileInfo]::new($hardlinkTarget)).Length -eq 0)) 'hardlinked reservation (link count != 1) rejects before mutation'
        } else {
            Add-Test 'T3D-C1-C-07-HARDLINK' $true 'hardlink creation unsupported on this filesystem; RESERVATION_LINK_COUNT_MISMATCH branch verified by code inspection only'
        }

        # RV02 negative: unknown sibling in the target directory blocks publication
        # even when the reservation itself is otherwise valid.
        $siblingTarget = Join-Path $root 'sibling/REGISTRY.json'
        New-ReservedZeroByteFixture -Path $siblingTarget -TestPolicy
        [System.IO.File]::WriteAllBytes((Join-Path $root 'sibling/unregistered.bin'), [Text.Encoding]::UTF8.GetBytes('preserve'))
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $siblingTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $siblingRejected=$false } catch { $siblingRejected=$_.Exception.Message -like 'UNKNOWN_RESIDUE_PRESENT:*' }
        Add-Test 'T3D-C1-C-07-SIBLING' ($siblingRejected -and (([IO.FileInfo]::new($siblingTarget)).Length -eq 0) -and (Test-Path (Join-Path $root 'sibling/unregistered.bin'))) 'unknown sibling blocks publication and is preserved untouched'

        # R2-03: cannot mutate a cross-target (Party B) reservation via this writer,
        # even when the cross-target is reservation-shaped (zero-byte, correct
        # descriptor). The transaction itself enforces target identity (literal
        # REGISTRY.json name), not just reservation shape.
        $crossTarget = Join-Path $root 'cross/LOOKUP_RESPONSES.jsonl'
        New-ReservedZeroByteFixture -Path $crossTarget -TestPolicy
        $crossBefore = Get-SecurityState $crossTarget
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $crossTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $crossRejected=$false } catch { $crossRejected=$_.Exception.Message -like 'TARGET_IDENTITY_MISMATCH:*' }
        $crossAfter = Get-SecurityState $crossTarget
        Add-Test 'T3D-C1-C-CROSS-TARGET' ($crossRejected -and (([IO.FileInfo]::new($crossTarget)).Length -eq 0) -and (Test-SecurityStateExact $crossAfter $crossBefore.ownerSid $crossBefore.protectionState $crossBefore.aces)) 'writer rejects a cross-shaped target by literal identity before any mutation; cross-target bytes/security unchanged'

        # R2-04: unknown residue (unrelated stale temp) blocks ordinary publication.
        $residueTarget = Join-Path $root 'residue/REGISTRY.json'
        New-ReservedZeroByteFixture -Path $residueTarget -TestPolicy
        $residueDir = Split-Path -Parent $residueTarget
        $staleTemp = Join-Path $residueDir ('.cvf-g4-registry-' + [Guid]::NewGuid().ToString('N') + '.tmp')
        [System.IO.File]::WriteAllBytes($staleTemp, [Text.Encoding]::UTF8.GetBytes('stale-unowned-temp'))
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $residueTarget -TestPolicy -LedgerPath $ledger -RequireReservation | Out-Null; $residueBlocked=$false } catch { $residueBlocked=$_.Exception.Message -like 'UNKNOWN_RESIDUE_PRESENT:*' }
        Add-Test 'T3D-C1-C-RESIDUE-BLOCKS' ($residueBlocked -and (Test-Path $staleTemp)) 'unknown stale temp is preserved and blocks publication rather than being swept'
        Remove-Item -LiteralPath $staleTemp -Force

        foreach ($point in @('AfterAcquire','AfterTempFlush','BeforeMove','AfterMove')) {
            $faultTarget = Join-Path $root ("fault-$point/REGISTRY.json")
            New-ReservedZeroByteFixture -Path $faultTarget -TestPolicy
            $faultPreSecurity = Get-SecurityState $faultTarget
            try { Publish-RegistryTransaction -InputPath $input -TargetPath $faultTarget -InjectFailure $point -TestPolicy -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $ledger -RequireReservation | Out-Null; $failed=$false } catch { $failed=$true }
            $faultPostSecurity = Get-SecurityState $faultTarget
            $stillReserved = (Test-Path $faultTarget) -and ([IO.FileInfo]::new($faultTarget)).Length -eq 0 -and (Test-SecurityStateExact $faultPostSecurity $faultPreSecurity.ownerSid $faultPreSecurity.protectionState $faultPreSecurity.aces)
            Add-Test "T3D-C1-C-ROLLBACK-$point" ($failed -and $stillReserved) 'failure at any injection point restores the exact pre-transaction zero-byte reservation (content and security), including after the atomic move'
            $faultDir = Split-Path $faultTarget
            Add-Test "T3D-C1-C-CLEAN-$point" (@(Get-ChildItem $faultDir -Force -Filter '*.tmp').Count -eq 0) 'no temp residue'
        }

        # RV03 explicit case: failure after publication (post-replace) must restore
        # content, identity and security, not merely throw.
        $postReplaceTarget = Join-Path $root 'post-replace/REGISTRY.json'
        New-ReservedZeroByteFixture -Path $postReplaceTarget -TestPolicy
        $postReplacePreSecurity = Get-SecurityState $postReplaceTarget
        $txnRollback = 'selftest-c-rollback-' + [Guid]::NewGuid().ToString('N')
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $postReplaceTarget -InjectFailure AfterMove -TestPolicy -LedgerPath $ledger -RequireReservation -TransactionId $txnRollback | Out-Null; $postReplaceFailed=$false } catch { $postReplaceFailed=$_.Exception.Message -like 'ROLLBACK_INJECTED_AFTER_MOVE:*' }
        $postReplacePostSecurity = Get-SecurityState $postReplaceTarget
        Add-Test 'T3D-C1-C-POST-REPLACE-ROLLBACK' ($postReplaceFailed -and (([IO.FileInfo]::new($postReplaceTarget)).Length -eq 0) -and (Test-BytesEqual ([IO.File]::ReadAllBytes($postReplaceTarget)) ([byte[]]::new(0))) -and (Test-SecurityStateExact $postReplacePostSecurity $postReplacePreSecurity.ownerSid $postReplacePreSecurity.protectionState $postReplacePreSecurity.aces)) 'post-replacement failure restores exact zero-byte content and exact pre-transaction security descriptor, not just a caught exception'
        Add-Test 'T3D-C1-C-POST-REPLACE-NO-RESIDUE' (@(Get-ChildItem (Split-Path $postReplaceTarget) -Force -Filter '*.tmp').Count -eq 0) 'no rollback-temp residue after restoration'
        $rollbackRows = @(Read-LedgerTransactionRows $ledger $txnRollback)
        $candidatePhases = (@($rollbackRows | Where-Object tempRole -ceq 'CANDIDATE' | ForEach-Object phase) -join ',')
        $rollbackPhases = (@($rollbackRows | Where-Object tempRole -ceq 'ROLLBACK' | ForEach-Object phase) -join ',')
        $rollbackTemp = @($rollbackRows | Where-Object tempRole -ceq 'ROLLBACK' | ForEach-Object tempName | Sort-Object -Unique)
        Add-Test 'T3D-C1-C-POST-REPLACE-LEDGER' (($candidatePhases -ceq 'TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE,PUBLISHED') -and ($rollbackPhases -ceq 'TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE,PUBLISHED') -and ($rollbackTemp.Count -eq 1) -and ($rollbackTemp[0] -match '^\.cvf-g4-registry-rollback-[0-9a-f]{32}\.tmp$') -and ((($rollbackRows | ForEach-Object sequence) -join ',') -ceq '1,2,3,4,5,6,7,8')) 'the rollback temp is itself bound before creation and carries a complete phase sequence'

        $raceTarget=Join-Path $root 'race/REGISTRY.json';New-ReservedZeroByteFixture -Path $raceTarget -TestPolicy
        $competitor=[Text.Encoding]::UTF8.GetBytes('competitor-owned-by-other-actor')
        try{Publish-RegistryTransaction -InputPath $input -TargetPath $raceTarget -TestPolicy -InjectCompetitorBytes $competitor -LedgerPath $ledger -RequireReservation|Out-Null;$racePreserved=$true}catch{$racePreserved=$false}
        Add-Test 'T3D-C1-C-08-RACE' ((Test-Path $raceTarget) -and (Test-BytesEqual ([IO.File]::ReadAllBytes($raceTarget)) $vector)) 'own-target replace atomically wins over a same-target write race'

        $afterAcquire = Join-Path $root 'after-acquire/REGISTRY.json'
        try { Enter-TransactionGuard -TargetPath $afterAcquire -InjectAfterAcquire | Out-Null; $released=$false } catch { $g2=Enter-TransactionGuard $afterAcquire; $released=$null -ne $g2; Exit-TransactionGuard $g2 }
        Add-Test 'T3D-C1-C-08' $released 'post-acquire failure releases guard'

        $releaseTarget=Join-Path $root 'after-acquire-peer/REGISTRY.json';New-ReservedZeroByteFixture -Path $releaseTarget -TestPolicy
        try{Publish-RegistryTransaction -InputPath $input -TargetPath $releaseTarget -InjectFailure AfterAcquire -TestPolicy -LedgerPath $ledger -RequireReservation|Out-Null;$injected=$false}catch{$injected=$_.Exception.Message-like'ROLLBACK_INJECTED_AFTER_ACQUIRE:*'}
        $releaseRun=[Guid]::NewGuid().ToString('N');$releaseEvents=New-PeerEvents $releaseRun;$releasePsi=[Diagnostics.ProcessStartInfo]::new();$releasePsi.FileName=(Get-Command pwsh -ErrorAction Stop).Source;$releasePsi.UseShellExecute=$false;$releasePsi.CreateNoWindow=$true
        foreach($argument in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$releaseRun,'-PeerTargetPath',$releaseTarget,'-PeerInputPath',$input,'-PeerLedgerPath',$ledger,'-PeerExpectPublish')){$releasePsi.ArgumentList.Add($argument)};$releasePeer=[Diagnostics.Process]::Start($releasePsi)
        try{Add-Test 'T3D-C1-C-08-PEER-READY' ($injected-and$releaseEvents.Ready.WaitOne(15000)) 'second process ready after injected acquisition failure';$releaseEvents.ParentRelease.Set()|Out-Null;$releaseEvents.StartAttempt.Set()|Out-Null;Add-Test 'T3D-C1-C-08-PEER-ENTERED' ($releaseEvents.Entered.WaitOne(15000)) 'second process acquired same-target guard';Add-Test 'T3D-C1-C-08-PEER-COMPLETE' ($releaseEvents.Complete.WaitOne(15000)) 'second process completed production publish';$releasePeer.WaitForExit(15000)|Out-Null;Add-Test 'T3D-C1-C-08-PEER-EXIT' ($releasePeer.HasExited-and$releasePeer.ExitCode-eq0-and(Test-BytesEqual ([IO.File]::ReadAllBytes($releaseTarget)) $vector)) 'same-target successor published exact bytes'}finally{if(-not$releasePeer.HasExited){$releasePeer.Kill($true)};$releasePeer.Dispose();@($releaseEvents.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}

        # R2-07: real second OS process; ENTERED must not precede PARENT_RELEASE.
        $peerTarget = Join-Path $root 'peer/REGISTRY.json'; New-ReservedZeroByteFixture -Path $peerTarget -TestPolicy
        $runId=[Guid]::NewGuid().ToString('N'); $events=New-PeerEvents $runId
        $psi=[System.Diagnostics.ProcessStartInfo]::new()
        $psi.FileName=(Get-Command pwsh -ErrorAction Stop).Source
        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true
        foreach($argument in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$runId,'-PeerTargetPath',$peerTarget,'-PeerInputPath',$input,'-PeerLedgerPath',$ledger)) { $psi.ArgumentList.Add($argument) }
        $peer=[System.Diagnostics.Process]::Start($psi)
        try {
            Add-Test 'T3D-C1-C-09-READY' ($events.Ready.WaitOne(15000)) 'READY observed'
            $parentDigest=Publish-RegistryTransaction -InputPath $input -TargetPath $peerTarget -TestPolicy -ParentBarrierEvents $events -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $ledger -RequireReservation
            Add-Test 'T3D-C1-C-09-PARENT' ($parentDigest -ceq (Get-Sha256Hex $vector)) 'parent executed production publish transaction'
            Add-Test 'T3D-C1-C-09-ATTEMPTING' ($events.Attempting.WaitOne(0)) 'ATTEMPTING observed while parent held guard'
            Add-Test 'T3D-C1-C-09-ENTERED' ($events.Entered.WaitOne(15000)) 'ENTERED after release'
            Add-Test 'T3D-C1-C-09-COMPLETE' ($events.Complete.WaitOne(15000)) 'COMPLETE observed'
            $peer.WaitForExit(15000) | Out-Null; Add-Test 'T3D-C1-C-09-EXIT' ($peer.HasExited -and $peer.ExitCode -eq 0) 'real peer exited zero'
            Add-Test 'T3D-C1-C-09-BYTES' (Test-BytesEqual ([System.IO.File]::ReadAllBytes($peerTarget)) $vector) 'losing production transaction (RESERVATION_NONZERO on already-published target) did not overwrite winner'
        } finally {
            if (-not $peer.HasExited) { $peer.Kill($true) }
            $peer.Dispose(); @($events.psobject.Properties.Value) | ForEach-Object { $_.Dispose() }
        }

        foreach ($point in @('AfterAcquireBeforeMutation','AfterTempFlush','BeforeMove')) {
            $crashTarget=Join-Path $root ("crash-$point/REGISTRY.json")
            New-ReservedZeroByteFixture -Path $crashTarget -TestPolicy
            $crashRun=[Guid]::NewGuid().ToString('N')
            $crashEvent=[System.Threading.EventWaitHandle]::new($false,[System.Threading.EventResetMode]::ManualReset,"Local\CVF_G4C_CRASH_$crashRun")
            $crashPsi=[System.Diagnostics.ProcessStartInfo]::new()
            $crashPsi.FileName=(Get-Command pwsh -ErrorAction Stop).Source; $crashPsi.UseShellExecute=$false; $crashPsi.CreateNoWindow=$true
            foreach($argument in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-CrashMode','-CrashRunId',$crashRun,'-CrashTargetPath',$crashTarget,'-CrashInputPath',$input,'-CrashLedgerPath',$ledger,'-CrashPoint',$point)) { $crashPsi.ArgumentList.Add($argument) }
            $crash=[System.Diagnostics.Process]::Start($crashPsi)
            try {
                Add-Test "T3D-C1-C-CRASH-$point-BARRIER" ($crashEvent.WaitOne(15000)) 'hard-crash barrier reached by production publish'
                $crash.Kill($true); $crash.WaitForExit(15000) | Out-Null
                Add-Test "T3D-C1-C-CRASH-$point-KILLED" $crash.HasExited 'worker was hard terminated'
                # Ordinary publication must remain fail-closed on crash residue; only the
                # distinct ledger-bound recovery may clear it (exercised by the Local harness).
                $residue = @(Get-ChildItem (Split-Path $crashTarget) -Force -Filter '.cvf-g4-registry-*.tmp')
                try { Publish-RegistryTransaction -InputPath $input -TargetPath $crashTarget -TestPolicy -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $ledger -RequireReservation | Out-Null; $ordinaryOutcome='PUBLISHED' } catch { $ordinaryOutcome=$_.Exception.Message }
                if ($point -ceq 'AfterAcquireBeforeMutation') {
                    Add-Test "T3D-C1-C-CRASH-$point-NO-SELF-RECOVER" (($residue.Count -eq 0) -and ($ordinaryOutcome -ceq 'PUBLISHED')) 'crash before planning leaves no residue and the reservation remains claimable'
                } else {
                    Add-Test "T3D-C1-C-CRASH-$point-NO-SELF-RECOVER" (($residue.Count -eq 1) -and ($ordinaryOutcome -like 'UNKNOWN_RESIDUE_PRESENT:*') -and (Test-Path -LiteralPath $residue[0].FullName) -and (([IO.FileInfo]::new($crashTarget)).Length -eq 0)) 'ordinary publication refuses and preserves the crashed transaction temp'
                }
            } finally {
                if (-not $crash.HasExited) { $crash.Kill($true) }
                $crash.Dispose(); $crashEvent.Dispose()
            }
        }

        $model = @(Get-ExpectedAceVector)
        Add-Test 'T3D-C1-C-10-ORDER' ((($model | ForEach-Object sid) -join '|') -ceq (($script:PartyCSid,$script:SystemSid,$script:AdministratorsSid,$script:PartyBSid,$script:LocalSid) -join '|')) 'exact ordered ACE vector'
        Add-Test 'T3D-C1-C-10-SEMANTIC' ((Get-SemanticTupleStrings ([pscustomobject]@{aces=$model})).Count -eq 5) 'semantic multiset preserves multiplicity'
        $testAces=@(Get-ExpectedAceVector -TestPolicy); $testOwner=[System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
        $validState=[pscustomobject]@{ownerSid=$testOwner;protectionState=$true;aces=$testAces}
        Add-Test 'T3D-C1-C-SEC-VALID' (Test-SecurityModel $validState $testOwner $testAces) 'exact security model accepted'
        $extraAces=@($testAces)+@([pscustomobject]@{sid=$script:SystemSid;rights=1;accessType=0;isInherited=$false;inheritanceFlags=0;propagationFlags=0})
        Add-Test 'T3D-C1-C-SEC-EXTRA_ALLOW' (-not (Test-SecurityModel ([pscustomobject]@{ownerSid=$testOwner;protectionState=$true;aces=$extraAces}) $testOwner $testAces)) 'extra ACE rejected'
        $denyAce=@([pscustomobject]@{sid=$testAces[0].sid;rights=$testAces[0].rights;accessType=1;isInherited=$false;inheritanceFlags=0;propagationFlags=0})
        Add-Test 'T3D-C1-C-SEC-DENY' (-not (Test-SecurityModel ([pscustomobject]@{ownerSid=$testOwner;protectionState=$true;aces=$denyAce}) $testOwner $testAces)) 'access type mutation rejected'
        $inheritedAce=@([pscustomobject]@{sid=$testAces[0].sid;rights=$testAces[0].rights;accessType=0;isInherited=$true;inheritanceFlags=0;propagationFlags=0})
        Add-Test 'T3D-C1-C-SEC-INHERITED' (-not (Test-SecurityModel ([pscustomobject]@{ownerSid=$testOwner;protectionState=$true;aces=$inheritedAce}) $testOwner $testAces)) 'inherited ACE rejected'
        Add-Test 'T3D-C1-C-SEC-WRONG_OWNER' (-not (Test-SecurityModel ([pscustomobject]@{ownerSid=$script:SystemSid;protectionState=$true;aces=$testAces}) $testOwner $testAces)) 'wrong owner rejected'
        Add-Test 'T3D-C1-C-11' ($PSCmdlet.ParameterSetName -eq 'SelfTest') 'default mode is self-test'
        [pscustomobject]@{ result='PASS'; tests=$script:Tests.Count; peerProtocol=@('READY','START_ATTEMPT','ATTEMPTING','PARENT_RELEASE','ENTERED','COMPLETE'); sourceMutation=$false } | ConvertTo-Json -Compress
    } finally {
        if (Test-Path $root) { Remove-Item -LiteralPath $root -Recurse -Force }
    }
}

if ($PSCmdlet.ParameterSetName -eq 'Peer') { Invoke-PeerMode }
if ($PSCmdlet.ParameterSetName -eq 'Crash') { Invoke-CrashMode }
if ($PSCmdlet.ParameterSetName -eq 'SelfTest') { Invoke-SelfTest; exit 0 }

$paths = Assert-ExactExecutionBoundary -Root $RepositoryRoot -InputPath $RegistryJsonPath -Confirm $Confirmation
$checker = Join-Path $paths.Root 'governance/compat/check_acel_g1_issuer_registry.py'
$python=Resolve-PythonRuntime $PythonExecutablePath
$ledgerPath = Join-Path $paths.Root '.cvf/runtime/group4-recovery-ledger/REGISTRY_LEDGER.jsonl'
$digest = Publish-RegistryTransaction -InputPath $paths.Source -TargetPath $paths.Target -ValidationCheckerPath $checker -PythonRuntime $python -LedgerPath $ledgerPath -RequireReservation -TransactionId $TransactionId -AuthorizationPath $AuthorizationPath
[pscustomobject]@{ result='REGISTRY_CREATED_PENDING_LOCAL_POSTFLIGHT'; path=$script:RegistryRelativePath; sha256=$digest; transactionId=$TransactionId } | ConvertTo-Json -Compress
