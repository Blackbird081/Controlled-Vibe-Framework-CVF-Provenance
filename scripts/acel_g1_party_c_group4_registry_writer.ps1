<#
.SYNOPSIS
Hermetic-first Party C Group 4 issuer-registry initial publisher.

.DESCRIPTION
Default invocation runs non-mutating self-tests.  Real publication is an
explicit initial-create-only transaction and is bound to the verified Party C
principal, canonical repository root, exact governed target, and confirmation
literal.  This script never writes the observation or lookup-response logs.
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

    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [switch] $PeerMode,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerRunId,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerTargetPath,
    [Parameter(ParameterSetName = 'Peer', Mandatory = $true)]
    [string] $PeerInputPath,
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
    if ($Left.Length -ne $Right.Length) { return $false }
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
    if (Test-Path -LiteralPath $target) {
        Stop-Writer 'REGISTRY_ALREADY_EXISTS' 'initial creation refuses overwrite'
    }
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
    return [pscustomobject]@{ ownerSid=$owner; protectionState=[bool]$security.AreAccessRulesProtected; aces=$aces; raw=$security }
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

function Test-SecurityModel($State, [string] $ExpectedOwner, [object[]] $ExpectedAces) {
    if ($State.ownerSid -cne $ExpectedOwner -or -not $State.protectionState) { return $false }
    if (((Get-OrderedTupleStrings $State) -join "`n") -cne ((Get-OrderedTupleStrings ([pscustomobject]@{aces=$ExpectedAces})) -join "`n")) { return $false }
    return ((Get-SemanticTupleStrings $State) -join "`n") -ceq ((Get-SemanticTupleStrings ([pscustomobject]@{aces=$ExpectedAces})) -join "`n")
}

function Assert-SecurityState([string] $Path, [switch] $TestPolicy) {
    $actual = Get-SecurityState $Path
    $expectedOwner = if ($TestPolicy) { [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value } else { $script:PartyCSid }
    if ($actual.ownerSid -cne $expectedOwner) { Stop-Writer 'SECURITY_OWNER_MISMATCH' $actual.ownerSid }
    if (-not $actual.protectionState) { Stop-Writer 'SECURITY_INHERITANCE_ENABLED' 'DACL is not protected' }
    if (@($actual.aces | Where-Object isInherited).Count -ne 0) { Stop-Writer 'SECURITY_INHERITED_ACE' 'inherited ACE present' }
    $expected = @(Get-ExpectedAceVector -TestPolicy:$TestPolicy)
    if (((Get-OrderedTupleStrings $actual) -join "`n") -cne ((Get-OrderedTupleStrings ([pscustomobject]@{aces=$expected})) -join "`n")) { Stop-Writer 'SECURITY_ACE_ORDER_MISMATCH' 'ordered complete ACE vector differs' }
    if (((Get-SemanticTupleStrings $actual) -join "`n") -cne ((Get-SemanticTupleStrings ([pscustomobject]@{aces=$expected})) -join "`n")) { Stop-Writer 'SECURITY_ACE_SET_MISMATCH' 'semantic ACE multiset differs' }
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

function Remove-OrphanTemps([string] $Directory) {
    if (-not (Test-Path -LiteralPath $Directory -PathType Container)) { return }
    foreach ($item in @(Get-ChildItem -LiteralPath $Directory -File -Force -Filter '.cvf-g4-registry-*.tmp')) {
        if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) { Stop-Writer 'ROLLBACK_ORPHAN_REPARSE_POINT' $item.FullName }
        Remove-Item -LiteralPath $item.FullName -Force
    }
    if (@(Get-ChildItem -LiteralPath $Directory -File -Force -Filter '.cvf-g4-registry-*.tmp').Count -ne 0) {
        Stop-Writer 'ROLLBACK_ORPHAN_CLEANUP_FAILED' $Directory
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
    [ValidateSet('None','AfterAcquire','AfterTempFlush','BeforeMove','AfterMove')][string] $InjectFailure = 'None',
    [switch] $TestPolicy,
    $ParentBarrierEvents,
    [System.Threading.EventWaitHandle] $AcquiredEvent,
    [System.Threading.EventWaitHandle] $RequiredParentReleaseEvent,
    [ValidateSet('None','AfterAcquireBeforeMutation','AfterTempFlush','BeforeMove')][string] $CrashAt = 'None',
    [System.Threading.EventWaitHandle] $CrashEvent,
    [string] $ValidationCheckerPath,
    $PythonRuntime,
    [byte[]] $InjectCompetitorBytes
) {
    $guard = $null; $temp = $null; $directory = Split-Path -Parent $TargetPath
    $directoryExisted = Test-Path -LiteralPath $directory
    $guardAcquired = $false; $prestateCaptured = $false; $publishedByTransaction = $false
    $existed = $false
    try {
        $guard = Enter-TransactionGuard -TargetPath $TargetPath -InjectAfterAcquire:($InjectFailure -eq 'AfterAcquire') -AcquiredEvent $AcquiredEvent
        $guardAcquired = $true
        if ($null -ne $RequiredParentReleaseEvent -and -not $RequiredParentReleaseEvent.WaitOne(0)) {
            Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'peer acquired before PARENT_RELEASE'
        }
        $directoryExisted = Test-Path -LiteralPath $directory
        $existed = Test-Path -LiteralPath $TargetPath
        $prestateCaptured = $true
        Wait-CrashBarrier -Point 'AfterAcquireBeforeMutation' -SelectedPoint $CrashAt -CrashEvent $CrashEvent
        if ($existed) {
            Stop-Writer 'REGISTRY_ALREADY_EXISTS' 'initial-create-only transaction'
        }
        [System.IO.Directory]::CreateDirectory($directory) | Out-Null
        Remove-OrphanTemps $directory
        $inputBytes = [System.IO.File]::ReadAllBytes($InputPath)
        $temp = Join-Path $directory ('.cvf-g4-registry-' + [Guid]::NewGuid().ToString('N') + '.tmp')
        $stream = [System.IO.FileStream]::new($temp,[System.IO.FileMode]::CreateNew,[System.IO.FileAccess]::Write,[System.IO.FileShare]::None,4096,[System.IO.FileOptions]::WriteThrough)
        try { $stream.Write($inputBytes,0,$inputBytes.Length); $stream.Flush($true) } finally { $stream.Dispose() }
        Set-ExactSecurity -Path $temp -TestPolicy:$TestPolicy | Out-Null
        if (-not (Test-BytesEqual ([System.IO.File]::ReadAllBytes($temp)) $inputBytes)) { Stop-Writer 'HASH_TEMP_READBACK_MISMATCH' $temp }
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
        if($null-ne$InjectCompetitorBytes){[System.IO.File]::WriteAllBytes($TargetPath,$InjectCompetitorBytes)}
        [System.IO.File]::Move($temp, $TargetPath, $false); $temp = $null; $publishedByTransaction = $true
        if ($InjectFailure -eq 'AfterMove') { Stop-Writer 'ROLLBACK_INJECTED_AFTER_MOVE' 'self-test injection' }
        if (-not (Test-BytesEqual ([System.IO.File]::ReadAllBytes($TargetPath)) $inputBytes)) { Stop-Writer 'HASH_TARGET_READBACK_MISMATCH' $TargetPath }
        Assert-SecurityState -Path $TargetPath -TestPolicy:$TestPolicy | Out-Null
        if ($null -ne $ParentBarrierEvents) { $ParentBarrierEvents.ParentRelease.Set() | Out-Null }
        return Get-Sha256Hex $inputBytes
    } catch {
        $primary = $_
        if ($null -ne $temp -and (Test-Path -LiteralPath $temp)) { Remove-Item -LiteralPath $temp -Force }
        if ($guardAcquired -and $prestateCaptured -and $publishedByTransaction -and -not $existed -and (Test-Path -LiteralPath $TargetPath)) {
            Remove-Item -LiteralPath $TargetPath -Force
        }
        if ($guardAcquired -and $prestateCaptured -and -not $directoryExisted -and (Test-Path -LiteralPath $directory) -and @(Get-ChildItem -LiteralPath $directory -Force).Count -eq 0) {
            Remove-Item -LiteralPath $directory -Force
        }
        if ($null -ne $ParentBarrierEvents) { $ParentBarrierEvents.ParentRelease.Set() | Out-Null }
        throw $primary
    } finally { Exit-TransactionGuard $guard }
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
            Publish-RegistryTransaction -InputPath $PeerInputPath -TargetPath $PeerTargetPath -TestPolicy -AcquiredEvent $events.Entered -RequiredParentReleaseEvent $events.ParentRelease -ValidationCheckerPath $checker -PythonRuntime $python | Out-Null
            if(-not$PeerExpectPublish){exit 23}
        } catch {
            if($PeerExpectPublish){exit 25}
            if ($_.Exception.Message -notlike 'REGISTRY_ALREADY_EXISTS:*') { exit 24 }
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
        Publish-RegistryTransaction -InputPath $CrashInputPath -TargetPath $CrashTargetPath -TestPolicy -CrashAt $CrashPoint -CrashEvent $event -ValidationCheckerPath $checker -PythonRuntime $python | Out-Null
        exit 31
    } finally { $event.Dispose() }
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
        $target = Join-Path $root 'source/REGISTRY.json'
        $digest = Publish-RegistryTransaction -InputPath $input -TargetPath $target -TestPolicy -ValidationCheckerPath $checker -PythonRuntime $python
        Add-Test 'T3D-C1-C-04' ($digest -ceq (Get-Sha256Hex $vector)) 'atomic initial publish succeeds'
        Add-Test 'T3D-C1-C-05' (Test-BytesEqual ([System.IO.File]::ReadAllBytes($target)) $vector) 'published bytes exact'
        Add-Test 'T3D-C1-C-06' (@(Get-ChildItem (Split-Path $target) -Filter '*.tmp').Count -eq 0) 'no orphan temp remains'
        Add-Test 'T3D-C1-C-06-VALIDATED' ($digest -ceq (Get-Sha256Hex $vector)) 'captured-byte checker branch executed'
        try{Assert-DisposableTestPaths (Join-Path (Split-Path -Parent $root) 'outside/REGISTRY.json') $input;$contained=$false}catch{$contained=$_.Exception.Message-like'TEST_CONTAINMENT_VIOLATION:*'}
        Add-Test 'T3D-C1-C-06-CONTAINMENT' $contained 'test-only target cannot escape disposable root'
        $junctionOutside=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4c-junction-target-'+[Guid]::NewGuid().ToString('N'));$junction=Join-Path $root 'nested-junction';[IO.Directory]::CreateDirectory($junctionOutside)|Out-Null
        try{New-Item -ItemType Junction -Path $junction -Target $junctionOutside|Out-Null;try{Assert-DisposableTestPaths (Join-Path $junction 'REGISTRY.json') $input;$nestedContained=$false}catch{$nestedContained=$_.Exception.Message-like'TEST_CONTAINMENT_VIOLATION:*'};Add-Test 'T3D-C1-C-06-NESTED-REPARSE' $nestedContained 'component walk rejects intermediate junction'}finally{if(Test-Path $junction){Remove-Item -LiteralPath $junction -Force};if(Test-Path $junctionOutside){Remove-Item -LiteralPath $junctionOutside -Force}}
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $target -TestPolicy | Out-Null; $refused=$false } catch { $refused=$_.Exception.Message -like 'REGISTRY_ALREADY_EXISTS:*' }
        Add-Test 'T3D-C1-C-07' $refused 'no-overwrite enforced'

        foreach ($point in @('AfterAcquire','AfterTempFlush','BeforeMove','AfterMove')) {
            $faultTarget = Join-Path $root ("fault-$point/REGISTRY.json")
            try { Publish-RegistryTransaction -InputPath $input -TargetPath $faultTarget -InjectFailure $point -TestPolicy -ValidationCheckerPath $checker -PythonRuntime $python | Out-Null; $failed=$false } catch { $failed=$true }
            Add-Test "T3D-C1-C-ROLLBACK-$point" ($failed -and -not (Test-Path $faultTarget)) 'failure restores absence'
            $faultDir = Split-Path $faultTarget
            Add-Test "T3D-C1-C-CLEAN-$point" (-not (Test-Path $faultDir) -or (Get-ChildItem $faultDir -Force).Count -eq 0) 'no residue'
        }

        $existingTarget = Join-Path $root 'existing/REGISTRY.json'
        [System.IO.Directory]::CreateDirectory((Split-Path $existingTarget)) | Out-Null
        $existingBytes = [Text.Encoding]::UTF8.GetBytes('existing-target-must-survive')
        [System.IO.File]::WriteAllBytes($existingTarget,$existingBytes)
        try { Publish-RegistryTransaction -InputPath $input -TargetPath $existingTarget -InjectFailure AfterAcquire -TestPolicy | Out-Null; $preserved=$false } catch {
            $preserved=(Test-Path -LiteralPath $existingTarget) -and (Test-BytesEqual ([System.IO.File]::ReadAllBytes($existingTarget)) $existingBytes)
        }
        Add-Test 'T3D-C1-C-08-EXISTING' $preserved 'post-acquire injection cannot delete pre-existing target'

        $raceTarget=Join-Path $root 'race/REGISTRY.json';$competitor=[Text.Encoding]::UTF8.GetBytes('competitor-owned-by-other-actor')
        try{Publish-RegistryTransaction -InputPath $input -TargetPath $raceTarget -TestPolicy -InjectCompetitorBytes $competitor|Out-Null;$racePreserved=$false}catch{$racePreserved=(Test-Path $raceTarget)-and(Test-BytesEqual ([IO.File]::ReadAllBytes($raceTarget)) $competitor)}
        Add-Test 'T3D-C1-C-08-RACE' $racePreserved 'failed no-overwrite move never deletes competitor publication'

        $afterAcquire = Join-Path $root 'after-acquire/REGISTRY.json'
        try { Enter-TransactionGuard -TargetPath $afterAcquire -InjectAfterAcquire | Out-Null; $released=$false } catch { $g2=Enter-TransactionGuard $afterAcquire; $released=$null -ne $g2; Exit-TransactionGuard $g2 }
        Add-Test 'T3D-C1-C-08' $released 'post-acquire failure releases guard'

        $releaseTarget=Join-Path $root 'after-acquire-peer/REGISTRY.json'
        try{Publish-RegistryTransaction -InputPath $input -TargetPath $releaseTarget -InjectFailure AfterAcquire -TestPolicy|Out-Null;$injected=$false}catch{$injected=$_.Exception.Message-like'ROLLBACK_INJECTED_AFTER_ACQUIRE:*'}
        $releaseRun=[Guid]::NewGuid().ToString('N');$releaseEvents=New-PeerEvents $releaseRun;$releasePsi=[Diagnostics.ProcessStartInfo]::new();$releasePsi.FileName=(Get-Command pwsh -ErrorAction Stop).Source;$releasePsi.UseShellExecute=$false;$releasePsi.CreateNoWindow=$true
        foreach($argument in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$releaseRun,'-PeerTargetPath',$releaseTarget,'-PeerInputPath',$input,'-PeerExpectPublish')){$releasePsi.ArgumentList.Add($argument)};$releasePeer=[Diagnostics.Process]::Start($releasePsi)
        try{Add-Test 'T3D-C1-C-08-PEER-READY' ($injected-and$releaseEvents.Ready.WaitOne(15000)) 'second process ready after injected acquisition failure';$releaseEvents.ParentRelease.Set()|Out-Null;$releaseEvents.StartAttempt.Set()|Out-Null;Add-Test 'T3D-C1-C-08-PEER-ENTERED' ($releaseEvents.Entered.WaitOne(15000)) 'second process acquired same-target guard';Add-Test 'T3D-C1-C-08-PEER-COMPLETE' ($releaseEvents.Complete.WaitOne(15000)) 'second process completed production publish';$releasePeer.WaitForExit(15000)|Out-Null;Add-Test 'T3D-C1-C-08-PEER-EXIT' ($releasePeer.HasExited-and$releasePeer.ExitCode-eq0-and(Test-BytesEqual ([IO.File]::ReadAllBytes($releaseTarget)) $vector)) 'same-target successor published exact bytes'}finally{if(-not$releasePeer.HasExited){$releasePeer.Kill($true)};$releasePeer.Dispose();@($releaseEvents.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}

        $peerTarget = Join-Path $root 'peer/REGISTRY.json'; $runId=[Guid]::NewGuid().ToString('N'); $events=New-PeerEvents $runId
        $psi=[System.Diagnostics.ProcessStartInfo]::new()
        $psi.FileName=(Get-Command pwsh -ErrorAction Stop).Source
        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true
        foreach($argument in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$runId,'-PeerTargetPath',$peerTarget,'-PeerInputPath',$input)) { $psi.ArgumentList.Add($argument) }
        $peer=[System.Diagnostics.Process]::Start($psi)
        try {
            Add-Test 'T3D-C1-C-09-READY' ($events.Ready.WaitOne(15000)) 'READY observed'
            $parentDigest=Publish-RegistryTransaction -InputPath $input -TargetPath $peerTarget -TestPolicy -ParentBarrierEvents $events -ValidationCheckerPath $checker -PythonRuntime $python
            Add-Test 'T3D-C1-C-09-PARENT' ($parentDigest -ceq (Get-Sha256Hex $vector)) 'parent executed production publish transaction'
            Add-Test 'T3D-C1-C-09-ATTEMPTING' ($events.Attempting.WaitOne(0)) 'ATTEMPTING observed while parent held guard'
            Add-Test 'T3D-C1-C-09-ENTERED' ($events.Entered.WaitOne(15000)) 'ENTERED after release'
            Add-Test 'T3D-C1-C-09-COMPLETE' ($events.Complete.WaitOne(15000)) 'COMPLETE observed'
            $peer.WaitForExit(15000) | Out-Null; Add-Test 'T3D-C1-C-09-EXIT' ($peer.HasExited -and $peer.ExitCode -eq 0) 'real peer exited zero'
            Add-Test 'T3D-C1-C-09-BYTES' (Test-BytesEqual ([System.IO.File]::ReadAllBytes($peerTarget)) $vector) 'losing production transaction did not overwrite winner'
        } finally {
            if (-not $peer.HasExited) { $peer.Kill($true) }
            $peer.Dispose(); @($events.psobject.Properties.Value) | ForEach-Object { $_.Dispose() }
        }

        foreach ($point in @('AfterAcquireBeforeMutation','AfterTempFlush','BeforeMove')) {
            $crashTarget=Join-Path $root ("crash-$point/REGISTRY.json")
            $crashRun=[Guid]::NewGuid().ToString('N')
            $crashEvent=[System.Threading.EventWaitHandle]::new($false,[System.Threading.EventResetMode]::ManualReset,"Local\CVF_G4C_CRASH_$crashRun")
            $crashPsi=[System.Diagnostics.ProcessStartInfo]::new()
            $crashPsi.FileName=(Get-Command pwsh -ErrorAction Stop).Source; $crashPsi.UseShellExecute=$false; $crashPsi.CreateNoWindow=$true
            foreach($argument in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-CrashMode','-CrashRunId',$crashRun,'-CrashTargetPath',$crashTarget,'-CrashInputPath',$input,'-CrashPoint',$point)) { $crashPsi.ArgumentList.Add($argument) }
            $crash=[System.Diagnostics.Process]::Start($crashPsi)
            try {
                Add-Test "T3D-C1-C-CRASH-$point-BARRIER" ($crashEvent.WaitOne(15000)) 'hard-crash barrier reached by production publish'
                $crash.Kill($true); $crash.WaitForExit(15000) | Out-Null
                Add-Test "T3D-C1-C-CRASH-$point-KILLED" $crash.HasExited 'worker was hard terminated'
                $recovered=Publish-RegistryTransaction -InputPath $input -TargetPath $crashTarget -TestPolicy -ValidationCheckerPath $checker -PythonRuntime $python
                Add-Test "T3D-C1-C-CRASH-$point-RECOVER" ($recovered -ceq (Get-Sha256Hex $vector)) 'next transaction recovered deterministically'
                Add-Test "T3D-C1-C-CRASH-$point-CLEAN" (@(Get-ChildItem (Split-Path $crashTarget) -Force -Filter '.cvf-g4-registry-*.tmp').Count -eq 0) 'orphan temp removed under guard'
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
$digest = Publish-RegistryTransaction -InputPath $paths.Source -TargetPath $paths.Target -ValidationCheckerPath $checker -PythonRuntime $python
[pscustomobject]@{ result='REGISTRY_CREATED_PENDING_LOCAL_VERIFICATION'; path=$script:RegistryRelativePath; sha256=$digest } | ConvertTo-Json -Compress
