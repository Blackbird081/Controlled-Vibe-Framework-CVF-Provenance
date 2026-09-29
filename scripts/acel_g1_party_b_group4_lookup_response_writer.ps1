<#
.SYNOPSIS
Hermetic-first Party B Group 4 lookup-response reservation-compatible
initializer and appender.
.DESCRIPTION
Default invocation runs non-mutating tests. Real initialization claims an
already-reserved zero-byte target via a target-preserving atomic replace with
exactly zero bytes; it never creates the target itself and never sweeps
unknown temps. Real initialization requires a Local preflight authorization
view and the Local-issued transaction ID; the Local postflight is separate. Peer and crash modes are test-only and accept only disposable
paths below the system temp root. Hard-termination recovery is a distinct
Administrator-only operation performed by acel_g1_group4_admin_recovery.ps1
against the durable ledger this script writes before any temp is created.
#>
[CmdletBinding(DefaultParameterSetName='SelfTest')]
param(
 [Parameter(ParameterSetName='SelfTest')][switch]$SelfTest,
 [Parameter(ParameterSetName='Initialize',Mandatory=$true)][switch]$InitializeResponseLog,
 [Parameter(ParameterSetName='Append',Mandatory=$true)][switch]$ExecuteLookupAppend,
 [Parameter(ParameterSetName='Append',Mandatory=$true)][string]$RequestJsonPath,
 [Parameter(ParameterSetName='Initialize',Mandatory=$true)][Parameter(ParameterSetName='Append',Mandatory=$true)][string]$RepositoryRoot,
 [Parameter(ParameterSetName='Initialize',Mandatory=$true)][Parameter(ParameterSetName='Append',Mandatory=$true)][string]$Confirmation,
 [Parameter(ParameterSetName='Initialize',Mandatory=$true)][Parameter(ParameterSetName='Append',Mandatory=$true)][string]$PythonExecutablePath,
 [Parameter(ParameterSetName='Initialize',Mandatory=$true)][string]$AuthorizationPath,
 [Parameter(ParameterSetName='Initialize',Mandatory=$true)][string]$TransactionId,
 [Parameter(ParameterSetName='Peer',Mandatory=$true)][switch]$PeerMode,
 [Parameter(ParameterSetName='Peer',Mandatory=$true)][string]$PeerRunId,
 [Parameter(ParameterSetName='Peer',Mandatory=$true)][string]$PeerFixtureRoot,
 [Parameter(ParameterSetName='Peer')][switch]$PeerExpectAppend,
 [Parameter(ParameterSetName='Peer')][switch]$PeerExpectInitialize,
 [Parameter(ParameterSetName='Crash',Mandatory=$true)][switch]$CrashMode,
 [Parameter(ParameterSetName='Crash',Mandatory=$true)][string]$CrashRunId,
 [Parameter(ParameterSetName='Crash',Mandatory=$true)][string]$CrashFixtureRoot,
 [Parameter(ParameterSetName='Crash',Mandatory=$true)][ValidateSet('AfterAcquireBeforeMutation','AfterTempFlush','BeforeReplace')][string]$CrashPoint
)
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$script:PartyBAccount='LAM-RUBY\cvf-g1-party-b';$script:PartyBSid='S-1-5-21-1644666849-912006174-747199667-1009';$script:PartyCSid='S-1-5-21-1644666849-912006174-747199667-1010';$script:LocalSid='S-1-5-21-1644666849-912006174-747199667-1001';$script:SystemSid='S-1-5-18';$script:AdministratorsSid='S-1-5-32-544'
$script:Confirmation='EXECUTE_ACEL_G1_GROUP4_PARTY_B_WRITE_V1';$script:RegistryRelative='governance/sources/issuer_registry/REGISTRY.json';$script:ResponseRelative='governance/sources/issuer_registry/LOOKUP_RESPONSES.jsonl';$script:ObservationRelative='governance/sources/registry_observation_log/LOG.jsonl';$script:ScriptPath=$PSCommandPath;$script:Tests=[Collections.Generic.List[object]]::new()

function Stop-Writer([string]$Code,[string]$Message){throw [InvalidOperationException]::new("${Code}: ${Message}")}
function Get-CanonicalPath([string]$Path){[IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar)}
function Assert-NoReparseTraversal([string]$BasePath,[string]$CandidatePath){$base=Get-CanonicalPath $BasePath;$candidate=Get-CanonicalPath $CandidatePath;$prefix=$base+[IO.Path]::DirectorySeparatorChar;if($candidate-cne$base-and-not$candidate.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' $candidate};$current=$base;if(Test-Path -LiteralPath $current){$item=Get-Item -LiteralPath $current -Force;if($item.Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' ('reparse traversal: '+$current)}};if($candidate-cne$base){foreach($part in $candidate.Substring($prefix.Length)-split'[\\/]'){$current=Join-Path $current $part;if(Test-Path -LiteralPath $current){$item=Get-Item -LiteralPath $current -Force;if($item.Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' ('reparse traversal: '+$current)}}}}}
function Get-Sha256Hex([byte[]]$Bytes){$s=[Security.Cryptography.SHA256]::Create();try{([Convert]::ToHexString($s.ComputeHash($Bytes))).ToLowerInvariant()}finally{$s.Dispose()}}
function Test-BytesEqual([byte[]]$Left,[byte[]]$Right){if($null-eq$Left-or$null-eq$Right-or$Left.Length-ne$Right.Length){return $false};for($i=0;$i-lt$Left.Length;$i++){if($Left[$i]-ne$Right[$i]){return $false}};return $true}
function Get-MutexName([string]$Target){'Global\CVF_G4_RESPONSE_TXN_'+(Get-Sha256Hex ([Text.Encoding]::UTF8.GetBytes((Get-CanonicalPath $Target).ToUpperInvariant()))).Substring(0,48)}
function Resolve-PythonRuntime([string]$ExplicitPath){if($ExplicitPath){$resolved=Get-CanonicalPath $ExplicitPath;if(-not(Test-Path -LiteralPath $resolved -PathType Leaf)){Stop-Writer 'PYTHON_EXECUTABLE_UNAVAILABLE' $resolved};$prefix=if([IO.Path]::GetFileNameWithoutExtension($resolved)-ieq'py'){@('-3')}else{@()}}else{$command=Get-Command py -ErrorAction SilentlyContinue;$prefix=@('-3');if($null-eq$command){$command=Get-Command python -ErrorAction SilentlyContinue;$prefix=@()};if($null-eq$command){Stop-Writer 'PYTHON_EXECUTABLE_UNAVAILABLE' 'neither py nor python resolved'};$resolved=$command.Source};$probe=&$resolved @prefix --version 2>&1;if($LASTEXITCODE-ne0){Stop-Writer 'PYTHON_EXECUTABLE_UNUSABLE' ($probe-join"`n")};[pscustomobject]@{executable=$resolved;prefix=@($prefix)}}
function Invoke-PythonRuntime($Runtime,[string[]]$Arguments){$exe=[string]$Runtime.executable;$prefix=@($Runtime.prefix);$out=&$exe @prefix @Arguments 2>&1;[pscustomobject]@{exitCode=$LASTEXITCODE;output=@($out)}}
function Assert-DisposableFixtureRoot([string]$Path){$full=Get-CanonicalPath $Path;$tempRoot=Get-CanonicalPath([IO.Path]::GetTempPath());$temp=$tempRoot+[IO.Path]::DirectorySeparatorChar;if(-not$full.StartsWith($temp,[StringComparison]::OrdinalIgnoreCase)){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' $full};$first=(($full.Substring($temp.Length))-split'[\\/]')[0];if($first-notlike'cvf-g4b-*'){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' $full};Assert-NoReparseTraversal $tempRoot $full;$full}
function Enter-Guard([string]$Target,[switch]$InjectAfterAcquire,[Threading.EventWaitHandle]$AcquiredEvent){$m=$null;$held=$false;try{$created=$false;$m=[Threading.Mutex]::new($false,(Get-MutexName $Target),[ref]$created);try{$held=$m.WaitOne(15000)}catch [Threading.AbandonedMutexException]{$held=$true};if(-not$held){Stop-Writer 'CONCURRENCY_TIMEOUT' 'guard timeout'};if($null-ne$AcquiredEvent){$AcquiredEvent.Set()|Out-Null};if($InjectAfterAcquire){Stop-Writer 'ROLLBACK_INJECTED_AFTER_ACQUIRE' 'self-test injection'};return $m}catch{if($null-ne$m){if($held){try{$m.ReleaseMutex()}catch{}};$m.Dispose()};throw}}
function Exit-Guard($Mutex){if($null-ne$Mutex){try{$Mutex.ReleaseMutex()}finally{$Mutex.Dispose()}}}

function Get-ExpectedAceVector([switch]$TestPolicy){$full=[int][Security.AccessControl.FileSystemRights]::FullControl;$probe=[Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new($script:LocalSid),[Security.AccessControl.FileSystemRights]::Read,[Security.AccessControl.AccessControlType]::Allow);$read=[int]$probe.FileSystemRights;if($TestPolicy){$current=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value;return @([pscustomobject]@{sid=$current;rights=$full;accessType=0;isInherited=$false;inheritanceFlags=0;propagationFlags=0})};@([pscustomobject]@{sid=$script:PartyBSid;rights=$full;accessType=0;isInherited=$false;inheritanceFlags=0;propagationFlags=0},[pscustomobject]@{sid=$script:SystemSid;rights=$full;accessType=0;isInherited=$false;inheritanceFlags=0;propagationFlags=0},[pscustomobject]@{sid=$script:AdministratorsSid;rights=$full;accessType=0;isInherited=$false;inheritanceFlags=0;propagationFlags=0},[pscustomobject]@{sid=$script:LocalSid;rights=$read;accessType=0;isInherited=$false;inheritanceFlags=0;propagationFlags=0})}
function Get-SecurityState([string]$Path){$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$s=[IO.FileSystemAclExtensions]::GetAccessControl([IO.FileInfo]::new($Path),$sections);$aces=@($s.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier])|ForEach-Object{[pscustomobject]@{sid=$_.IdentityReference.Value;rights=[int]$_.FileSystemRights;accessType=[int]$_.AccessControlType;isInherited=[bool]$_.IsInherited;inheritanceFlags=[int]$_.InheritanceFlags;propagationFlags=[int]$_.PropagationFlags}});[pscustomobject]@{ownerSid=$s.GetOwner([Security.Principal.SecurityIdentifier]).Value;protectionState=[bool]$s.AreAccessRulesProtected;aces=$aces;raw=$s;binary=$s.GetSecurityDescriptorBinaryForm()}}
function Get-OrderedTupleStrings($State){@($State.aces|ForEach-Object{'{0}|{1}|{2}|{3}|{4}|{5}'-f$_.sid,$_.rights,$_.accessType,$_.isInherited,$_.inheritanceFlags,$_.propagationFlags})}
function Get-SemanticTupleStrings($State){@(Get-OrderedTupleStrings $State|Sort-Object -CaseSensitive)}
function Test-SecurityStateExact($State,[string]$Owner,[bool]$Protection,[object[]]$Aces){if($State.ownerSid-cne$Owner-or$State.protectionState-ne$Protection){return $false};$expected=[pscustomobject]@{aces=$Aces};if(((Get-OrderedTupleStrings $State)-join"`n")-cne((Get-OrderedTupleStrings $expected)-join"`n")){return $false};((Get-SemanticTupleStrings $State)-join"`n")-ceq((Get-SemanticTupleStrings $expected)-join"`n")}
function Test-SecurityModel($State,[string]$Owner,[object[]]$Aces){Test-SecurityStateExact $State $Owner $true $Aces}
function Assert-Security([string]$Path,[switch]$TestPolicy){$a=Get-SecurityState $Path;$e=@(Get-ExpectedAceVector -TestPolicy:$TestPolicy);$owner=if($TestPolicy){$e[0].sid}else{$script:PartyBSid};if(-not(Test-SecurityModel $a $owner $e)){Stop-Writer 'SECURITY_STATE_MISMATCH' 'owner/protection/ordered complete ACE vector or semantic multiset differs'};$a}
function Set-ExactSecurity([string]$Path,[switch]$TestPolicy){$e=@(Get-ExpectedAceVector -TestPolicy:$TestPolicy);$s=[Security.AccessControl.FileSecurity]::new();$s.SetAccessRuleProtection($true,$false);$owner=if($TestPolicy){$e[0].sid}else{$script:PartyBSid};$s.SetOwner([Security.Principal.SecurityIdentifier]::new($owner));foreach($ace in $e){$s.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new($ace.sid),[Security.AccessControl.FileSystemRights]$ace.rights,[Security.AccessControl.InheritanceFlags]$ace.inheritanceFlags,[Security.AccessControl.PropagationFlags]$ace.propagationFlags,[Security.AccessControl.AccessControlType]$ace.accessType))};[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($Path),$s);Assert-Security $Path -TestPolicy:$TestPolicy|Out-Null}
function Get-HardLinkCount([string]$Path){$output=&fsutil hardlink list $Path 2>&1;if($LASTEXITCODE-ne0){Stop-Writer 'RESERVATION_LINK_COUNT_UNAVAILABLE' $Path};@($output|Where-Object{$_.Trim().Length-gt0}).Count}
function Assert-ReservedZeroByte([string]$Path,[switch]$TestPolicy){if(-not(Test-Path -LiteralPath $Path -PathType Leaf)){Stop-Writer 'RESERVATION_MISSING' $Path};$item=[IO.FileInfo]::new($Path);if($item.Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Writer 'RESERVATION_REPARSE_POINT' $Path};if($item.Length-ne0){Stop-Writer 'RESERVATION_NONZERO' $Path};if((Get-HardLinkCount $Path)-ne1){Stop-Writer 'RESERVATION_LINK_COUNT_MISMATCH' $Path};Assert-Security $Path -TestPolicy:$TestPolicy|Out-Null}

function Get-ReservationNames { return @('REGISTRY.json', 'LOOKUP_RESPONSES.jsonl') }

# Closed two-name protected parent: both reservation names are permitted (only
# name, entry type and reparse state of the non-target are checked; its content
# and security are never read here), plus only this transaction's bound temps.
function Assert-ParentSiblingSet([string] $Directory, [string[]] $CurrentTemps) {
    if (-not (Test-Path -LiteralPath $Directory -PathType Container)) { return }
    $reservations = Get-ReservationNames
    foreach ($item in @(Get-ChildItem -LiteralPath $Directory -Force)) {
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { Stop-Writer 'ROLLBACK_ORPHAN_REPARSE_POINT' $item.FullName }
        if ($reservations -ccontains $item.Name) {
            if ($item.PSIsContainer) { Stop-Writer 'RESERVATION_SIBLING_NOT_FILE' $item.FullName }
            continue
        }
        if (-not $item.PSIsContainer -and @($CurrentTemps) -ccontains $item.Name) { continue }
        Stop-Writer 'UNKNOWN_RESIDUE_PRESENT' $item.FullName
    }
}

# Append (T3E) directory hygiene: fail closed on any writer-pattern residue.
function Remove-OrphanTemps([string]$Directory){if(-not(Test-Path $Directory -PathType Container)){return};foreach($pattern in @('.cvf-g4-response-*.tmp','.cvf-g4-capture-*.tmp','.cvf-g4-rollback-*.tmp')){foreach($item in @(Get-ChildItem -LiteralPath $Directory -File -Force -Filter $pattern)){if($item.Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Writer 'ROLLBACK_ORPHAN_REPARSE_POINT' $item.FullName};Stop-Writer 'UNKNOWN_RESIDUE_PRESENT' $item.FullName}}}
function Wait-CrashBarrier([string]$Point,[string]$Selected,[Threading.EventWaitHandle]$Event){if($Point-ceq$Selected-and$null-ne$Event){$Event.Set()|Out-Null;[Threading.Thread]::Sleep([Threading.Timeout]::Infinite)}}

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
    $owner = if ($TestPolicy) { [Security.Principal.WindowsIdentity]::GetCurrent().User.Value } else { $script:PartyBSid }
    return Get-SecurityDigestFromState ([pscustomobject]@{ ownerSid = $owner; protectionState = $true; aces = @(Get-ExpectedAceVector -TestPolicy:$TestPolicy) })
}

# Complete state of the writer's OWN target only.
function Get-OwnFileState([string] $Path) {
    $info = [IO.FileInfo]::new($Path)
    $security = Get-SecurityState $Path
    return [ordered]@{
        fileId = Get-FileIdHex $Path
        length = [int64]$info.Length
        sha256 = Get-Sha256Hex ([IO.File]::ReadAllBytes($Path))
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

# C0-R1 Local authorization reference: only the per-writer view (transaction,
# parent identity, guard and own-target fields). Any extra field is rejected.
function Assert-WriterAuthorization([string] $AuthorizationPath, [string] $TransactionId, [string] $TargetPath, [string] $TargetKind) {
    $parent = Get-CanonicalPath (Split-Path -Parent (Get-CanonicalPath $TargetPath))
    Assert-OutsideParent $AuthorizationPath $parent 'AUTHORIZATION_INSIDE_PROTECTED_PARENT'
    if (-not (Test-Path -LiteralPath $AuthorizationPath -PathType Leaf)) { Stop-Writer 'AUTHORIZATION_MISSING' $AuthorizationPath }
    try { $record = [IO.File]::ReadAllText($AuthorizationPath) | ConvertFrom-Json } catch { Stop-Writer 'AUTHORIZATION_MALFORMED' $AuthorizationPath }
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
    try { $guard = [Threading.Mutex]::OpenExisting([string]$record.guardName); $guard.Dispose() } catch { Stop-Writer 'AUTHORIZATION_GUARD_ABSENT' 'Local parent guard is not held' }
    if ((Format-FileState $record.ownTarget) -cne (Format-FileState (Get-OwnFileState $TargetPath))) { Stop-Writer 'AUTHORIZATION_OWN_TARGET_DRIFT' $TargetPath }
    return $record
}

function Get-LedgerSchemaId { return 'cvf.g4.recoveryLedger.v2' }

function New-LedgerContext([string] $LedgerPath, [string] $TransactionId, [string] $TargetPath, [string] $TargetKind, $Prestate) {
    $process = [Diagnostics.Process]::GetCurrentProcess()
    try { $startTicks = [int64]$process.StartTime.ToUniversalTime().Ticks; $processId = [int]$process.Id } finally { $process.Dispose() }
    $target = Get-CanonicalPath $TargetPath
    $parent = Get-CanonicalPath (Split-Path -Parent $target)
    return [pscustomobject]@{
        ledgerPath = Get-CanonicalPath $LedgerPath
        transactionId = $TransactionId
        sequence = 0
        writerSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
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
    if (-not (Test-Path -LiteralPath $directory)) { [IO.Directory]::CreateDirectory($directory) | Out-Null }
    $bytes = [Text.Encoding]::UTF8.GetBytes($Line + "`n")
    for ($attempt = 0; ; $attempt++) {
        try {
            $stream = [IO.FileStream]::new($LedgerPath, [IO.FileMode]::Append, [IO.FileAccess]::Write, [IO.FileShare]::Read, 4096, [IO.FileOptions]::WriteThrough)
            try { $stream.Write($bytes, 0, $bytes.Length); $stream.Flush($true) } finally { $stream.Dispose() }
            return
        } catch [IO.IOException] {
            if ($attempt -ge 200) { Stop-Writer 'LEDGER_APPEND_FAILED' $LedgerPath }
            [Threading.Thread]::Sleep(10)
        }
    }
}

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

# With a ledger context the unique temp name is generated and durably bound
# (TEMP_PLANNED with expected content hash and security digest) before the file
# is created. Without a context this helper is only a unit-test primitive.
function Write-HardenedTemp([string]$Directory,[string]$Prefix,[byte[]]$Bytes,[switch]$TestPolicy,[switch]$InjectHardeningFailure,$Context,[string]$Role='CAPTURE',[switch]$InjectAfterPlan){
    if ($null -ne $Context) {
        $name = Register-LedgerTemp $Context $Prefix $Role $Bytes (Get-ExpectedSecurityDigest -TestPolicy:$TestPolicy)
        if ($InjectAfterPlan) { Complete-LedgerTempRemoval $Context $name 'DISCARDED'; Stop-Writer 'ROLLBACK_INJECTED_AFTER_PLAN' 'self-test injection' }
    } else { $name = $Prefix + [Guid]::NewGuid().ToString('N') + '.tmp' }
    $path = Join-Path $Directory $name
    try {
        $stream=[IO.FileStream]::new($path,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None,4096,[IO.FileOptions]::WriteThrough)
        try{if($Bytes.Length){$stream.Write($Bytes,0,$Bytes.Length)};$stream.Flush($true)}finally{$stream.Dispose()}
        if($InjectHardeningFailure){Stop-Writer 'HARDENING_INJECTED_FAILURE' 'self-test'}
        Set-ExactSecurity $path -TestPolicy:$TestPolicy
        if(-not(Test-BytesEqual ([IO.File]::ReadAllBytes($path)) $Bytes)){Stop-Writer 'HASH_TEMP_READBACK_MISMATCH' $path}
        if ($null -ne $Context) { Set-LedgerTempFlushed $Context $name }
        return $path
    } catch {
        if ($null -ne $Context) { Complete-LedgerTempRemoval $Context $name 'DISCARDED' } elseif (Test-Path -LiteralPath $path) { Remove-Item -LiteralPath $path -Force }
        throw
    }
}

function Restore-ExistingAtomic([string]$Target,[byte[]]$Bytes,$Security,$Context,[switch]$TestPolicy){
    $dir=Split-Path -Parent $Target
    $rollbackName = Register-LedgerTemp $Context '.cvf-g4-rollback-' 'ROLLBACK' $Bytes (Get-SecurityDigestFromState $Security)
    $rollback = Join-Path $dir $rollbackName
    $moved = $false
    try{
        $stream=[IO.FileStream]::new($rollback,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None,4096,[IO.FileOptions]::WriteThrough)
        try{if($Bytes.Length){$stream.Write($Bytes,0,$Bytes.Length)};$stream.Flush($true)}finally{$stream.Dispose()}
        $descriptor=[Security.AccessControl.FileSecurity]::new();$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access
        $descriptor.SetSecurityDescriptorBinaryForm($Security.binary,$sections);[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($rollback),$descriptor)
        $state=Get-SecurityState $rollback
        if(-not(Test-BytesEqual ([IO.File]::ReadAllBytes($rollback)) $Bytes)-or-not(Test-SecurityStateExact $state $Security.ownerSid $Security.protectionState $Security.aces)){Stop-Writer 'ROLLBACK_TEMP_MISMATCH' $rollback}
        Set-LedgerTempFlushed $Context $rollbackName
        Add-LedgerRow $Context $rollbackName 'PRE_MOVE'
        [IO.File]::Move($rollback,$Target,$true);$moved=$true
        Add-LedgerRow $Context $rollbackName 'PUBLISHED'
        $actual=Get-SecurityState $Target
        if(-not(Test-BytesEqual ([IO.File]::ReadAllBytes($Target)) $Bytes)-or-not(Test-SecurityStateExact $actual $Security.ownerSid $Security.protectionState $Security.aces)){Stop-Writer 'ROLLBACK_TARGET_MISMATCH' $Target}
    }finally{ if(-not $moved){ Complete-LedgerTempRemoval $Context $rollbackName 'DISCARDED' } }
}

function Write-CopyOnWriteTransaction([string]$Target,[byte[]]$FinalBytes,[ValidateSet('None','AfterAcquire','AfterPlanBeforeCreate','AfterTempFlush','BeforeReplace','AfterReplace')][string]$InjectFailure='None',[switch]$RequireReservation,[switch]$TestPolicy,$ParentBarrierEvents,[Threading.EventWaitHandle]$AcquiredEvent,[Threading.EventWaitHandle]$RequiredParentReleaseEvent,[ValidateSet('None','AfterAcquireBeforeMutation','AfterTempFlush','BeforeReplace')][string]$CrashAt='None',[Threading.EventWaitHandle]$CrashEvent,[string]$RegistryPath,[string]$CheckerPath,$PythonRuntime,[byte[]]$InjectCompetitorBytes,[string]$LedgerPath,[string]$TransactionId,[string]$AuthorizationPath){
 $guard=$null;$context=$null;$candidateName=$null;$captureName=$null;$dir=Split-Path -Parent $Target;$guardAcquired=$false;$prestateCaptured=$false;$publishedByTransaction=$false;$prior=$null;$security=$null
 if($RequireReservation-and(Split-Path -Leaf $Target)-cne'LOOKUP_RESPONSES.jsonl'){Stop-Writer 'TARGET_IDENTITY_MISMATCH' $Target}
 if(-not$LedgerPath){Stop-Writer 'LEDGER_REQUIRED' 'transaction requires a durable recovery ledger outside the protected parent'}
 Assert-OutsideParent $LedgerPath $dir 'LEDGER_INSIDE_PROTECTED_PARENT'
 if($AuthorizationPath-and-not$RequireReservation){Stop-Writer 'AUTHORIZATION_TARGET_MISMATCH' 'authorization applies only to the reservation claim'}
 if($AuthorizationPath-and-not$TransactionId){Stop-Writer 'AUTHORIZATION_TRANSACTION_MISMATCH' 'authorization requires the Local-issued transaction ID'}
 if(-not$TransactionId){$TransactionId=[Guid]::NewGuid().ToString('N')}
 if($TransactionId-notmatch'^[0-9A-Za-z-]{8,64}$'){Stop-Writer 'TRANSACTION_ID_INVALID' $TransactionId}
 try{$guard=Enter-Guard $Target -InjectAfterAcquire:($InjectFailure-eq'AfterAcquire') -AcquiredEvent $AcquiredEvent;$guardAcquired=$true;if($null-ne$RequiredParentReleaseEvent-and-not$RequiredParentReleaseEvent.WaitOne(0)){Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'peer acquired before release'};Wait-CrashBarrier 'AfterAcquireBeforeMutation' $CrashAt $CrashEvent
  if($RequireReservation){
   Assert-ReservedZeroByte -Path $Target -TestPolicy:$TestPolicy
   if($AuthorizationPath){Assert-WriterAuthorization $AuthorizationPath $TransactionId $Target 'RESPONSE'|Out-Null}
   Assert-ParentSiblingSet $dir @()
  }else{
   if(-not(Test-Path -LiteralPath $Target -PathType Leaf)){Stop-Writer 'SOURCE_UNAVAILABLE' 'copy-on-write replace requires an existing target'}
   Remove-OrphanTemps $dir
  }
  $prior=[IO.File]::ReadAllBytes($Target);$security=Get-SecurityState $Target;$prestateCaptured=$true
  $context=New-LedgerContext $LedgerPath $TransactionId $Target 'RESPONSE' (Get-OwnFileState $Target)
  if($RegistryPath){if($null-eq$PythonRuntime){Stop-Writer 'PYTHON_EXECUTABLE_UNAVAILABLE' 'registry validation requires resolved runtime'};$registryBytes=[IO.File]::ReadAllBytes($RegistryPath);$capture=Write-HardenedTemp $dir '.cvf-g4-capture-' $registryBytes -TestPolicy:$TestPolicy -Context $context -Role 'CAPTURE';$captureName=Split-Path -Leaf $capture;$validation=Invoke-PythonRuntime $PythonRuntime @($CheckerPath,'--registry',$capture);if($validation.exitCode-ne0){Stop-Writer 'SOURCE_SCHEMA_INVALID' ('exact captured registry bytes rejected inside guard: '+($validation.output-join"`n"))}}
  $temp=Write-HardenedTemp $dir '.cvf-g4-response-' $FinalBytes -TestPolicy:$TestPolicy -Context $context -Role 'CANDIDATE' -InjectAfterPlan:($InjectFailure-eq'AfterPlanBeforeCreate');$candidateName=Split-Path -Leaf $temp
  Wait-CrashBarrier 'AfterTempFlush' $CrashAt $CrashEvent;if($InjectFailure-eq'AfterTempFlush'){Stop-Writer 'ROLLBACK_INJECTED_AFTER_TEMP_FLUSH' 'self-test'}
  if($null-ne$ParentBarrierEvents){$ParentBarrierEvents.StartAttempt.Set()|Out-Null;if(-not$ParentBarrierEvents.Attempting.WaitOne(15000)){Stop-Writer 'CONCURRENCY_PEER_NOT_ATTEMPTING' 'ATTEMPTING not observed'};if($ParentBarrierEvents.Entered.WaitOne(0)){Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'peer entered while parent held guard'}}
  Wait-CrashBarrier 'BeforeReplace' $CrashAt $CrashEvent;if($InjectFailure-eq'BeforeReplace'){Stop-Writer 'ROLLBACK_INJECTED_BEFORE_REPLACE' 'self-test'}
  if($RequireReservation){Assert-ParentSiblingSet $dir @(@($candidateName,$captureName)|Where-Object{$_})}
  if($null-ne$InjectCompetitorBytes){[IO.File]::WriteAllBytes($Target,$InjectCompetitorBytes)}
  Add-LedgerRow $context $candidateName 'PRE_MOVE'
  [IO.File]::Move($temp,$Target,$true);$publishedByTransaction=$true
  Add-LedgerRow $context $candidateName 'PUBLISHED'
  if($InjectFailure-eq'AfterReplace'){Stop-Writer 'ROLLBACK_INJECTED_AFTER_REPLACE' 'self-test'};if(-not(Test-BytesEqual ([IO.File]::ReadAllBytes($Target)) $FinalBytes)){Stop-Writer 'HASH_TARGET_READBACK_MISMATCH' $Target};Assert-Security $Target -TestPolicy:$TestPolicy|Out-Null
  if($null-ne$ParentBarrierEvents){$ParentBarrierEvents.ParentRelease.Set()|Out-Null}
 }catch{$primary=$_;if($guardAcquired-and$prestateCaptured-and$publishedByTransaction-and$null-ne$prior){try{Restore-ExistingAtomic $Target $prior $security $context -TestPolicy:$TestPolicy}catch{Stop-Writer 'ROLLBACK_FAILED' ($primary.Exception.Message+' | '+$_.Exception.Message)}};if($null-ne$ParentBarrierEvents){$ParentBarrierEvents.ParentRelease.Set()|Out-Null};throw $primary
 }finally{
  if($null-ne$context){
   if($null-ne$captureName){Complete-LedgerTempRemoval $context $captureName 'RELEASED'}
   if($null-ne$candidateName-and-not$publishedByTransaction){Complete-LedgerTempRemoval $context $candidateName 'DISCARDED'}
  }
  Exit-Guard $guard
 }
}

function Assert-PrincipalAndPaths([string]$Root,[string]$Confirm){$id=[Security.Principal.WindowsIdentity]::GetCurrent();if($id.Name-cne$script:PartyBAccount-or$id.User.Value-cne$script:PartyBSid){Stop-Writer 'ACCESS_PRINCIPAL_MISMATCH' 'exact Party B account/SID required'};if($Confirm-cne$script:Confirmation){Stop-Writer 'ACCESS_CONFIRMATION_MISMATCH' 'exact confirmation required'};$r=Get-CanonicalPath $Root;$git=&git -C $r rev-parse --show-toplevel 2>$null;if($LASTEXITCODE-ne0-or(Get-CanonicalPath $git)-cne$r){Stop-Writer 'ACCESS_REPOSITORY_ROOT_INVALID' 'canonical Git root required'};[pscustomobject]@{root=$r;registry=Get-CanonicalPath(Join-Path $r $script:RegistryRelative);responses=Get-CanonicalPath(Join-Path $r $script:ResponseRelative);observations=Get-CanonicalPath(Join-Path $r $script:ObservationRelative);checker=Get-CanonicalPath(Join-Path $r 'governance/compat/check_acel_g1_issuer_registry.py');ledger=Get-CanonicalPath(Join-Path $r '.cvf/runtime/group4-recovery-ledger/RESPONSE_LEDGER.jsonl')}}
function Get-PreparedResponseLine($PythonRuntime,[string]$Checker,[string]$Registry,[string]$Responses,[string]$Observations,[string]$Request){$run=Invoke-PythonRuntime $PythonRuntime @($Checker,'--registry',$Registry,'--responses',$Responses,'--observation-log',$Observations,'--prepare-request',$Request);try{$payload=($run.output-join"`n"|ConvertFrom-Json)}catch{Stop-Writer 'LOOKUP_PREPARATION_FAILED' 'checker returned non-JSON output'};if($run.exitCode-ne0){$code=if($payload.taxonomyId){[string]$payload.taxonomyId}else{'LOOKUP_PREPARATION_FAILED'};Stop-Writer $code ([string]$payload.message)};$payload}
function Invoke-LookupAppendTransaction($Paths,[string]$Request,$PythonRuntime,[switch]$TestPolicy,$ParentBarrierEvents,[Threading.EventWaitHandle]$AcquiredEvent,[Threading.EventWaitHandle]$RequiredParentReleaseEvent,[ValidateSet('None','AfterAcquireBeforeMutation','AfterTempFlush','BeforeReplace')][string]$CrashAt='None',[Threading.EventWaitHandle]$CrashEvent,[string]$LedgerPath,[string]$TransactionId){
 $guard=$null;$context=$null;$dir=Split-Path -Parent $Paths.responses;$captureNames=[Collections.Generic.List[string]]::new();$candidateName=$null;$publishedByTransaction=$false;$prior=$null;$security=$null
 if(-not$LedgerPath){Stop-Writer 'LEDGER_REQUIRED' 'transaction requires a durable recovery ledger outside the protected parent'}
 Assert-OutsideParent $LedgerPath $dir 'LEDGER_INSIDE_PROTECTED_PARENT'
 if(-not$TransactionId){$TransactionId=[Guid]::NewGuid().ToString('N')}
 try{$guard=Enter-Guard $Paths.responses -AcquiredEvent $AcquiredEvent;if($null-ne$RequiredParentReleaseEvent-and-not$RequiredParentReleaseEvent.WaitOne(0)){Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'append peer acquired before release'};if(-not(Test-Path $Paths.responses)-or-not(Test-Path $Paths.registry)-or-not(Test-Path $Paths.observations)-or-not(Test-Path $Request)){Stop-Writer 'SOURCE_UNAVAILABLE' 'response, registry, observation, and request required'};$prior=[IO.File]::ReadAllBytes($Paths.responses);$security=Assert-Security $Paths.responses -TestPolicy:$TestPolicy;Wait-CrashBarrier 'AfterAcquireBeforeMutation' $CrashAt $CrashEvent;Remove-OrphanTemps $dir
  $context=New-LedgerContext $LedgerPath $TransactionId $Paths.responses 'RESPONSE' (Get-OwnFileState $Paths.responses)
  $registryCapture=Write-HardenedTemp $dir '.cvf-g4-capture-' ([IO.File]::ReadAllBytes($Paths.registry)) -TestPolicy:$TestPolicy -Context $context -Role 'CAPTURE';$captureNames.Add((Split-Path -Leaf $registryCapture))
  $responseCapture=Write-HardenedTemp $dir '.cvf-g4-capture-' $prior -TestPolicy:$TestPolicy -Context $context -Role 'CAPTURE';$captureNames.Add((Split-Path -Leaf $responseCapture))
  $observationCapture=Write-HardenedTemp $dir '.cvf-g4-capture-' ([IO.File]::ReadAllBytes($Paths.observations)) -TestPolicy:$TestPolicy -Context $context -Role 'CAPTURE';$captureNames.Add((Split-Path -Leaf $observationCapture))
  $requestCapture=Write-HardenedTemp $dir '.cvf-g4-capture-' ([IO.File]::ReadAllBytes($Request)) -TestPolicy:$TestPolicy -Context $context -Role 'CAPTURE';$captureNames.Add((Split-Path -Leaf $requestCapture))
  $prepared=Get-PreparedResponseLine $PythonRuntime $Paths.checker $registryCapture $responseCapture $observationCapture $requestCapture;if($prepared.kind-ceq'IDEMPOTENT'){return [pscustomobject]@{result='IDEMPOTENT';row=$prepared.row}};$line=[Convert]::FromBase64String([string]$prepared.lineBase64);$final=[byte[]]($prior+$line)
  $candidate=Write-HardenedTemp $dir '.cvf-g4-response-' $final -TestPolicy:$TestPolicy -Context $context -Role 'CANDIDATE';$candidateName=Split-Path -Leaf $candidate
  Wait-CrashBarrier 'AfterTempFlush' $CrashAt $CrashEvent
  $candidateCheck=Invoke-PythonRuntime $PythonRuntime @($Paths.checker,'--registry',$registryCapture,'--responses',$candidate,'--observation-log',$observationCapture,'--receipt-context');if($candidateCheck.exitCode-ne0){Stop-Writer 'CHAIN_VALIDATION_FAILED' ('candidate rejected: '+($candidateCheck.output-join"`n"))};if($null-ne$ParentBarrierEvents){$ParentBarrierEvents.StartAttempt.Set()|Out-Null;if(-not$ParentBarrierEvents.Attempting.WaitOne(15000)){Stop-Writer 'CONCURRENCY_PEER_NOT_ATTEMPTING' 'append peer did not attempt'};if($ParentBarrierEvents.Entered.WaitOne(0)){Stop-Writer 'CONCURRENCY_ENTERED_BEFORE_PARENT_RELEASE' 'append peer entered while parent held guard'}};Wait-CrashBarrier 'BeforeReplace' $CrashAt $CrashEvent
  Add-LedgerRow $context $candidateName 'PRE_MOVE'
  [IO.File]::Move($candidate,$Paths.responses,$true);$publishedByTransaction=$true
  Add-LedgerRow $context $candidateName 'PUBLISHED'
  if(-not(Test-BytesEqual ([IO.File]::ReadAllBytes($Paths.responses)) $final)){Stop-Writer 'HASH_TARGET_READBACK_MISMATCH' $Paths.responses};Assert-Security $Paths.responses -TestPolicy:$TestPolicy|Out-Null;$targetCheck=Invoke-PythonRuntime $PythonRuntime @($Paths.checker,'--registry',$registryCapture,'--responses',$Paths.responses,'--observation-log',$observationCapture,'--receipt-context');if($targetCheck.exitCode-ne0){Stop-Writer 'CHAIN_VALIDATION_FAILED' ('target rejected: '+($targetCheck.output-join"`n"))}
  if($null-ne$ParentBarrierEvents){$ParentBarrierEvents.ParentRelease.Set()|Out-Null};[pscustomobject]@{result='APPENDED_PENDING_LOCAL_VERIFICATION';row=$prepared.row;transactionId=$TransactionId}
 }catch{$primary=$_;if($publishedByTransaction){try{Restore-ExistingAtomic $Paths.responses $prior $security $context -TestPolicy:$TestPolicy}catch{Stop-Writer 'ROLLBACK_FAILED' ($primary.Exception.Message+' | '+$_.Exception.Message)}};if($null-ne$ParentBarrierEvents){$ParentBarrierEvents.ParentRelease.Set()|Out-Null};throw $primary
 }finally{
  if($null-ne$context){
   foreach($name in @($captureNames)){Complete-LedgerTempRemoval $context $name 'RELEASED'}
   if($null-ne$candidateName-and-not$publishedByTransaction){Complete-LedgerTempRemoval $context $candidateName 'DISCARDED'}
  }
  Exit-Guard $guard
 }
}

function Read-LedgerTransactionRows([string] $LedgerPath, [string] $TransactionId) {
    if (-not (Test-Path -LiteralPath $LedgerPath -PathType Leaf)) { return @() }
    return @([IO.File]::ReadAllLines($LedgerPath) | Where-Object { $_.Trim().Length -gt 0 } | ForEach-Object { $_ | ConvertFrom-Json } | Where-Object { $_.transactionId -ceq $TransactionId })
}

function New-PeerEvents([string]$Run){$m=[Threading.EventResetMode]::ManualReset;[pscustomobject]@{Ready=[Threading.EventWaitHandle]::new($false,$m,"Local\CVF_G4B_READY_$Run");StartAttempt=[Threading.EventWaitHandle]::new($false,$m,"Local\CVF_G4B_START_ATTEMPT_$Run");Attempting=[Threading.EventWaitHandle]::new($false,$m,"Local\CVF_G4B_ATTEMPTING_$Run");ParentRelease=[Threading.EventWaitHandle]::new($false,$m,"Local\CVF_G4B_PARENT_RELEASE_$Run");Entered=[Threading.EventWaitHandle]::new($false,$m,"Local\CVF_G4B_ENTERED_$Run");Complete=[Threading.EventWaitHandle]::new($false,$m,"Local\CVF_G4B_COMPLETE_$Run")}}
function Get-TestFixturePaths([string]$Root){$rootPath=Assert-DisposableFixtureRoot $Root;$p=[pscustomobject]@{root=$rootPath;registry=Join-Path $rootPath 'REGISTRY.json';responses=Join-Path $rootPath 'LOOKUP_RESPONSES.jsonl';observations=Join-Path $rootPath 'LOG.jsonl';request=Join-Path $rootPath 'REQUEST.json';ledger=Join-Path ($rootPath+'.ledger') 'LEDGER.jsonl';checker=Join-Path (Split-Path -Parent (Split-Path -Parent $script:ScriptPath)) 'governance/compat/check_acel_g1_issuer_registry.py'};foreach($path in @($p.registry,$p.responses,$p.observations,$p.request)){if(Test-Path -LiteralPath $path){$item=Get-Item -LiteralPath $path -Force;if($item.Attributes-band[IO.FileAttributes]::ReparsePoint-or$item.Length-gt1048576){Stop-Writer 'TEST_CONTAINMENT_VIOLATION' ('invalid fixture: '+$path)}}};$p}
function New-LookupFixture([string]$Root,[byte[]]$RegistryBytes){
 $p=Get-TestFixturePaths $Root;[IO.Directory]::CreateDirectory($p.root)|Out-Null;[IO.File]::WriteAllBytes($p.registry,$RegistryBytes);[IO.File]::WriteAllBytes($p.responses,[byte[]]::new(0));Set-ExactSecurity $p.responses -TestPolicy
 $snapshotHash=Get-Sha256Hex $RegistryBytes;$snapshotContent=[Convert]::ToBase64String($RegistryBytes).TrimEnd('=').Replace('+','-').Replace('/','_');$observed=[DateTime]::UtcNow.AddSeconds(-1).ToString('yyyy-MM-ddTHH:mm:ssZ');$snapshotId='snap-issuer-001'
 $preimage='{"authority":"ACEL_G1_DECISION_OWNER","domain":"cvf.observationLogEntry","observedAt":"'+$observed+'","observerIdentity":"'+$script:PartyBSid+'","priorEntryHashHex":null,"profile":"cvf.source-record-canonicalization@1","registryName":"issuer_registry","registrySnapshotVersion":1,"snapshotHashHex":"'+$snapshotHash+'","snapshotId":"'+$snapshotId+'"}'
 $entryHash=Get-Sha256Hex ([Text.Encoding]::UTF8.GetBytes($preimage));$record='{"authority":"ACEL_G1_DECISION_OWNER","entryHashHex":"'+$entryHash+'","observedAt":"'+$observed+'","observerIdentity":"'+$script:PartyBSid+'","priorEntryHashHex":null,"registryName":"issuer_registry","registrySnapshotVersion":1,"snapshotHashHex":"'+$snapshotHash+'","snapshotId":"'+$snapshotId+'","snapshot_content":"'+$snapshotContent+'"}'
 [IO.File]::WriteAllBytes($p.observations,[Text.Encoding]::UTF8.GetBytes($record+"`n"));$request='{"claimedIssuerHash":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","consumerIdentity":"consumer-test-001","issuerIdentity":"issuer-test-001","lookupId":"808e5a61-0b1c-4bdd-b505-2c2687496b9f","observedSnapshotId":"'+$snapshotId+'"}';[IO.File]::WriteAllBytes($p.request,[Text.Encoding]::UTF8.GetBytes($request));$p
}
function Invoke-PeerMode{$p=Get-TestFixturePaths $PeerFixtureRoot;$python=Resolve-PythonRuntime;$e=New-PeerEvents $PeerRunId;try{$e.Ready.Set()|Out-Null;if(-not$e.StartAttempt.WaitOne(15000)){exit 31};$e.Attempting.Set()|Out-Null;if($PeerExpectInitialize){try{Write-CopyOnWriteTransaction -Target $p.responses -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -AcquiredEvent $e.Entered -RequiredParentReleaseEvent $e.ParentRelease -LedgerPath $p.ledger;$e.Complete.Set()|Out-Null;exit 0}catch{exit 35}};$result=Invoke-LookupAppendTransaction $p $p.request $python -TestPolicy -AcquiredEvent $e.Entered -RequiredParentReleaseEvent $e.ParentRelease -LedgerPath $p.ledger;$expected=if($PeerExpectAppend){'APPENDED_PENDING_LOCAL_VERIFICATION'}else{'IDEMPOTENT'};if($result.result-cne$expected){exit 33};$e.Complete.Set()|Out-Null;exit 0}finally{@($e.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}}
function Invoke-CrashMode{$p=Get-TestFixturePaths $CrashFixtureRoot;$python=Resolve-PythonRuntime;$e=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4B_CRASH_$CrashRunId");try{Invoke-LookupAppendTransaction $p $p.request $python -TestPolicy -CrashAt $CrashPoint -CrashEvent $e -LedgerPath $p.ledger|Out-Null;exit 41}finally{$e.Dispose()}}
function Add-Test([string]$Id,[bool]$Passed,[string]$Detail){$script:Tests.Add([pscustomobject]@{id=$Id;passed=$Passed;detail=$Detail});if(-not$Passed){Stop-Writer 'SELF_TEST_FAILED' "${Id}: ${Detail}"}}
function Test-StrictJsonlFraming([byte[]]$Bytes){if($Bytes.Length-eq0){return $true};if($Bytes.Length-ge3-and$Bytes[0]-eq0xef-and$Bytes[1]-eq0xbb-and$Bytes[2]-eq0xbf){return $false};try{$text=[Text.UTF8Encoding]::new($false,$true).GetString($Bytes)}catch{return $false};if($text.Contains("`r")-or-not$text.EndsWith("`n")){return $false};$lines=$text.Substring(0,$text.Length-1)-split"`n";@($lines|Where-Object{$_.Length-eq0}).Count-eq0}

function Set-AdversarialSecurity([string]$Path,[ValidateSet('EXTRA_ALLOW','DENY','INHERITED','WRONG_OWNER','UNPROTECTED')][string]$Kind){
 $current=[Security.Principal.WindowsIdentity]::GetCurrent().User
 if($Kind-eq'INHERITED'){
  $directory=Split-Path -Parent $Path;$ds=[Security.AccessControl.DirectorySecurity]::new();$ds.SetOwner($current);$ds.SetAccessRuleProtection($true,$false);$ds.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new($current,[Security.AccessControl.FileSystemRights]::FullControl,[Security.AccessControl.InheritanceFlags]'ContainerInherit, ObjectInherit',[Security.AccessControl.PropagationFlags]::None,[Security.AccessControl.AccessControlType]::Allow));[IO.FileSystemAclExtensions]::SetAccessControl([IO.DirectoryInfo]::new($directory),$ds);$s=[Security.AccessControl.FileSecurity]::new();$s.SetOwner($current);$s.SetAccessRuleProtection($false,$false);[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($Path),$s);return
 }
 $state=Get-SecurityState $Path;$s=$state.raw
 switch($Kind){
  'EXTRA_ALLOW'{$s.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new($script:SystemSid),[Security.AccessControl.FileSystemRights]::Read,[Security.AccessControl.AccessControlType]::Allow))}
  'DENY'{$s.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new($script:SystemSid),[Security.AccessControl.FileSystemRights]::Read,[Security.AccessControl.AccessControlType]::Deny))}
  'WRONG_OWNER'{$s.SetOwner([Security.Principal.SecurityIdentifier]::new($script:AdministratorsSid))}
  'UNPROTECTED'{$s.SetAccessRuleProtection($false,$true)}
 }
 [IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($Path),$s)
}

function New-ReservedZeroByteFixture([string]$Path,[switch]$TestPolicy){$directory=Split-Path -Parent $Path;if(-not(Test-Path -LiteralPath $directory)){[IO.Directory]::CreateDirectory($directory)|Out-Null};[IO.File]::WriteAllBytes($Path,[byte[]]::new(0));Set-ExactSecurity $Path -TestPolicy:$TestPolicy}

function Invoke-SelfTest{
 $root=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4b-'+[Guid]::NewGuid().ToString('N'));[IO.Directory]::CreateDirectory($root)|Out-Null
 try{
  $python=Resolve-PythonRuntime;$registryBytes=[Text.Encoding]::UTF8.GetBytes('{"registrySnapshotId":"issuer-registry-snapshot-test-0001","registrySnapshotVersion":1,"rows":[{"canonicalContentBytesBase64":"eyJhdXRob3JpdHkiOiJBQ0VMX0cxX0RFQ0lTSU9OX09XTkVSIiwiaXNzdWVySWRlbnRpdHkiOiJpc3N1ZXItdGVzdC0wMDEiLCJwb2xpY3lWZXJzaW9uIjoxfQ","canonicalContentHashHex":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","correctedAt":null,"entryVersion":1,"issuerAttestedHash":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","issuerIdentity":"issuer-test-001","registeredAt":"2026-09-22T00:00:00Z","revokedAt":null,"status":"ACTIVE"}],"writeTimestamp":"2026-09-22T00:00:01Z"}')
  $ledger=Join-Path $root 'ledger/LEDGER.jsonl'

  # R2-02: own-target reservation claim, target-preserving atomic zero-byte initialize.
  $target=Join-Path $root 'source/LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $target -TestPolicy
  $txnInit='selftest-b-init-'+[Guid]::NewGuid().ToString('N')
  Write-CopyOnWriteTransaction -Target $target -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger -TransactionId $txnInit
  Add-Test 'T3D-C1-B-01' ((Test-Path $target)-and([IO.File]::ReadAllBytes($target).Length-eq0)) 'zero-byte reservation-claim initialization'
  # RV08: immutable non-empty temp binding across all phases.
  $initRows=@(Read-LedgerTransactionRows $ledger $txnInit)
  $rowKeys=@('schema','transactionId','sequence','phase','recordedAt','writerSid','writerProcessId','writerProcessStartUtcTicks','targetKind','targetName','targetPath','parentPath','parentFileId','targetPrestate','tempName','tempRole','expectedTempSha256','expectedTempSecurityDigest','tempFileId')|Sort-Object
  Add-Test 'T3D-C1-B-01-LEDGER-PHASES' ((($initRows|ForEach-Object phase)-join',')-ceq'TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE,PUBLISHED') 'init ledger phase sequence is PLANNED,FLUSHED,PRE_MOVE,PUBLISHED'
  Add-Test 'T3D-C1-B-01-LEDGER-SEQUENCE' ((($initRows|ForEach-Object sequence)-join',')-ceq'1,2,3,4') 'init ledger sequence is strictly 1..4'
  Add-Test 'T3D-C1-B-01-LEDGER-TEMPNAME' ((@($initRows|ForEach-Object tempName|Sort-Object -Unique).Count-eq1)-and([string]$initRows[0].tempName-match'^\.cvf-g4-response-[0-9a-f]{32}\.tmp$')-and([string]$initRows[3].tempName-ceq[string]$initRows[0].tempName)) 'PUBLISHED row carries the same non-empty temp name as TEMP_PLANNED'
  Add-Test 'T3D-C1-B-01-LEDGER-SCHEMA' ((@($initRows|Where-Object{((@($_.PSObject.Properties.Name)|Sort-Object)-join',')-cne($rowKeys-join',')}).Count-eq0)-and([string]$initRows[0].targetKind-ceq'RESPONSE')-and([string]$initRows[0].targetName-ceq'LOOKUP_RESPONSES.jsonl')) 'every init row uses the exact v2 field set and target binding'
  Add-Test 'T3D-C1-B-01-LEDGER-FILEID' (($null-eq$initRows[0].tempFileId)-and([string]$initRows[1].tempFileId-match'^0x[0-9a-f]+$')-and([string]$initRows[3].tempFileId-ceq[string]$initRows[1].tempFileId)) 'temp identity absent at planning and stable from flush onward'
  # RV07: capture and candidate are both bound before creation.
  $captureRoot=Join-Path $root 'capture-init';$captureTarget=Join-Path $captureRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $captureTarget -TestPolicy
  $captureRegistry=Join-Path $root 'capture-registry.json';[IO.File]::WriteAllBytes($captureRegistry,$registryBytes)
  $txnCapture='selftest-b-capture-'+[Guid]::NewGuid().ToString('N')
  Write-CopyOnWriteTransaction -Target $captureTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger -TransactionId $txnCapture -RegistryPath $captureRegistry -CheckerPath (Join-Path (Split-Path -Parent (Split-Path -Parent $script:ScriptPath)) 'governance/compat/check_acel_g1_issuer_registry.py') -PythonRuntime $python
  $captureRows=@(Read-LedgerTransactionRows $ledger $txnCapture)
  Add-Test 'T3D-C1-B-01-CAPTURE-BOUND' (((@($captureRows|Where-Object tempRole -ceq 'CAPTURE'|ForEach-Object phase))-join',')-ceq'TEMP_PLANNED,TEMP_FLUSHED,RELEASED') 'registry capture is PLANNED before creation, FLUSHED after hardening and RELEASED after use'
  Add-Test 'T3D-C1-B-01-CANDIDATE-BOUND' (((@($captureRows|Where-Object tempRole -ceq 'CANDIDATE'|ForEach-Object phase))-join',')-ceq'TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE,PUBLISHED') 'initialization candidate carries a complete bound phase sequence'
  Add-Test 'T3D-C1-B-01-CAPTURE-ORDER' (([string]$captureRows[0].phase-ceq'TEMP_PLANNED')-and([string]$captureRows[0].tempRole-ceq'CAPTURE')-and([string]$captureRows[1].phase-ceq'TEMP_FLUSHED')-and([string]$captureRows[1].tempName-ceq[string]$captureRows[0].tempName)) 'the first durable row precedes any capture file'
  $planRoot=Join-Path $root 'plan-only';$planTarget=Join-Path $planRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $planTarget -TestPolicy
  $txnPlan='selftest-b-plan-'+[Guid]::NewGuid().ToString('N')
  try{Write-CopyOnWriteTransaction -Target $planTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger -TransactionId $txnPlan -InjectFailure AfterPlanBeforeCreate;$planFailed=$false}catch{$planFailed=$_.Exception.Message-like'ROLLBACK_INJECTED_AFTER_PLAN:*'}
  $planRows=@(Read-LedgerTransactionRows $ledger $txnPlan)
  Add-Test 'T3D-C1-B-01-PLAN-BEFORE-CREATE' ($planFailed-and((($planRows|ForEach-Object phase)-join',')-ceq'TEMP_PLANNED,DISCARDED')-and-not(Test-Path (Join-Path $planRoot ([string]$planRows[0].tempName)))-and(@(Get-ChildItem $planRoot -Force).Count-eq1)) 'TEMP_PLANNED is durable while the temp does not yet exist; abort records DISCARDED'
  $orderRoot=Join-Path $root 'plan-order';$orderTarget=Join-Path $orderRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $orderTarget -TestPolicy
  $orderContext=New-LedgerContext $ledger ('selftest-b-order-'+[Guid]::NewGuid().ToString('N')) $orderTarget 'RESPONSE' (Get-OwnFileState $orderTarget)
  $preCreated='.cvf-g4-response-'+[Guid]::NewGuid().ToString('N')+'.tmp';$orderContext.temps[$preCreated]=[pscustomobject]@{role='CANDIDATE';expectedSha256='x';expectedSecurityDigest='x';fileId=$null;lastPhase=$null}
  [IO.File]::WriteAllBytes((Join-Path $orderRoot $preCreated),[byte[]](1))
  try{Add-LedgerRow $orderContext $preCreated 'TEMP_PLANNED';$orderRejected=$false}catch{$orderRejected=$_.Exception.Message-like'LEDGER_BINDING_AFTER_CREATION:*'}
  Add-Test 'T3D-C1-B-01-BINDING-AFTER-CREATE' $orderRejected 'a planning binding for an already-existing temp is refused'
  Remove-Item -LiteralPath (Join-Path $orderRoot $preCreated) -Force
  try{Add-LedgerRow $orderContext '' 'PUBLISHED';$emptyRejected=$false}catch{$emptyRejected=$_.Exception.Message-like'LEDGER_TEMP_BINDING_MISSING:*'}
  Add-Test 'T3D-C1-B-01-EMPTY-TEMPNAME' $emptyRejected 'an empty temp name can never be written to the ledger'
  $insideRoot=Join-Path $root 'inside-ledger';$insideTarget=Join-Path $insideRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $insideTarget -TestPolicy
  try{Write-CopyOnWriteTransaction -Target $insideTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath (Join-Path $insideRoot 'LEDGER.jsonl');$insideRejected=$false}catch{$insideRejected=$_.Exception.Message-like'LEDGER_INSIDE_PROTECTED_PARENT:*'}
  Add-Test 'T3D-C1-B-01-LEDGER-OUTSIDE-PARENT' $insideRejected 'a ledger inside the protected parent is refused before mutation'
  # RV11: the closed two-name shared parent.
  $sharedRoot=Join-Path $root 'shared';$sharedTarget=Join-Path $sharedRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $sharedTarget -TestPolicy
  $sharedPeer=Join-Path $sharedRoot 'REGISTRY.json';[IO.File]::WriteAllBytes($sharedPeer,$registryBytes);$sharedPeerId=Get-FileIdHex $sharedPeer;$sharedPeerHash=Get-Sha256Hex ([IO.File]::ReadAllBytes($sharedPeer))
  try{Write-CopyOnWriteTransaction -Target $sharedTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$sharedOk=$true}catch{$sharedOk=$false}
  Add-Test 'T3D-C1-B-01-SHARED-PARENT' ($sharedOk-and((Get-FileIdHex $sharedPeer)-ceq$sharedPeerId)-and((Get-Sha256Hex ([IO.File]::ReadAllBytes($sharedPeer)))-ceq$sharedPeerHash)) 'Party B initializes beside the published registry, which is unchanged (checked by the test harness, not the writer)'
  $thirdRoot=Join-Path $root 'third';$thirdTarget=Join-Path $thirdRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $thirdTarget -TestPolicy
  [IO.File]::WriteAllBytes((Join-Path $thirdRoot 'REGISTRY.json'),$registryBytes);$thirdSibling=Join-Path $thirdRoot 'unexpected.bin';[IO.File]::WriteAllBytes($thirdSibling,[Text.Encoding]::UTF8.GetBytes('preserve'))
  try{Write-CopyOnWriteTransaction -Target $thirdTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$thirdRejected=$false}catch{$thirdRejected=$_.Exception.Message-like'UNKNOWN_RESIDUE_PRESENT:*'}
  Add-Test 'T3D-C1-B-01-THIRD-SIBLING' ($thirdRejected-and(Test-Path $thirdSibling)-and(([IO.FileInfo]::new($thirdTarget)).Length-eq0)) 'an unknown third sibling beside both reservations blocks and is preserved'

  # R2-02 negative: absent reservation rejects.
  $absentTarget=Join-Path $root 'absent/LOOKUP_RESPONSES.jsonl'
  try{Write-CopyOnWriteTransaction -Target $absentTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$absentRejected=$false}catch{$absentRejected=$_.Exception.Message-like'RESERVATION_MISSING:*'}
  Add-Test 'T3D-C1-B-02-ABSENT' $absentRejected 'missing reservation rejects before mutation'

  # R2-02 negative: nonzero reservation rejects.
  $nonzeroTarget=Join-Path $root 'nonzero/LOOKUP_RESPONSES.jsonl';[IO.Directory]::CreateDirectory((Split-Path $nonzeroTarget))|Out-Null;[IO.File]::WriteAllBytes($nonzeroTarget,[Text.Encoding]::UTF8.GetBytes('not-empty'));Set-ExactSecurity $nonzeroTarget -TestPolicy
  try{Write-CopyOnWriteTransaction -Target $nonzeroTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$nonzeroRejected=$false}catch{$nonzeroRejected=$_.Exception.Message-like'RESERVATION_NONZERO:*'}
  Add-Test 'T3D-C1-B-02-NONZERO' ($nonzeroRejected-and(Test-BytesEqual ([IO.File]::ReadAllBytes($nonzeroTarget)) ([Text.Encoding]::UTF8.GetBytes('not-empty')))) 'nonzero reservation rejects and leaves bytes untouched'

  # Append path continues to use existing-target copy-on-write (post-initialization), unaffected by RequireReservation.
  $prefix=[Text.Encoding]::UTF8.GetBytes("{`"entry`":1}`n");Write-CopyOnWriteTransaction $target $prefix -TestPolicy -LedgerPath $ledger;$second=[Text.Encoding]::UTF8.GetBytes("{`"entry`":2}`n");$multi=[byte[]]($prefix+$second);Write-CopyOnWriteTransaction $target $multi -TestPolicy -LedgerPath $ledger;Add-Test 'T3D-C1-B-03' (Test-BytesEqual ([IO.File]::ReadAllBytes($target)[0..($prefix.Length-1)]) $prefix) 'prior bytes exact prefix on existing-target replace'

  # R2-04: unknown residue blocks ordinary publication.
  $residueTarget=Join-Path $root 'residue/LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $residueTarget -TestPolicy
  $residueDir=Split-Path -Parent $residueTarget;$staleTemp=Join-Path $residueDir ('.cvf-g4-response-'+[Guid]::NewGuid().ToString('N')+'.tmp');[IO.File]::WriteAllBytes($staleTemp,[Text.Encoding]::UTF8.GetBytes('stale'))
  try{Write-CopyOnWriteTransaction -Target $residueTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$residueBlocked=$false}catch{$residueBlocked=$_.Exception.Message-like'UNKNOWN_RESIDUE_PRESENT:*'}
  Add-Test 'T3D-C1-B-RESIDUE-BLOCKS' ($residueBlocked-and(Test-Path $staleTemp)) 'unknown stale temp is preserved and blocks initialization'
  Remove-Item -LiteralPath $staleTemp -Force

  $raceTarget=Join-Path $root 'race/LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $raceTarget -TestPolicy;$competitor=[Text.Encoding]::UTF8.GetBytes('competitor-owned-by-other-actor');try{Write-CopyOnWriteTransaction -Target $raceTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -InjectCompetitorBytes $competitor -LedgerPath $ledger;$raceOk=$true}catch{$raceOk=$false};Add-Test 'T3D-C1-B-INIT-RACE' ($raceOk-and(Test-BytesEqual ([IO.File]::ReadAllBytes($raceTarget)) ([byte[]]::new(0)))) 'own-target atomic replace under this writer''s own guard wins over a same-target write race (this is the intra-writer atomicity guarantee, not a cross-principal identity claim)'

  # RV02 negative: hardlinked reservation rejects (link count != 1) before mutation.
  $hardlinkRoot=Join-Path $root 'hardlink';[IO.Directory]::CreateDirectory($hardlinkRoot)|Out-Null;$hardlinkTarget=Join-Path $hardlinkRoot 'LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $hardlinkTarget -TestPolicy
  $hardlinkSupported=$true;try{New-Item -ItemType HardLink -Path (Join-Path $hardlinkRoot 'second-name') -Target $hardlinkTarget -ErrorAction Stop|Out-Null}catch{$hardlinkSupported=$false}
  if($hardlinkSupported){try{Write-CopyOnWriteTransaction -Target $hardlinkTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$hardlinkRejected=$false}catch{$hardlinkRejected=$_.Exception.Message-like'RESERVATION_LINK_COUNT_MISMATCH:*'};Add-Test 'T3D-C1-B-HARDLINK' ($hardlinkRejected-and(([IO.FileInfo]::new($hardlinkTarget)).Length-eq0)) 'hardlinked reservation (link count != 1) rejects before mutation'}else{Add-Test 'T3D-C1-B-HARDLINK' $true 'hardlink creation unsupported on this filesystem; RESERVATION_LINK_COUNT_MISMATCH branch verified by code inspection only'}

  # RV02 negative: cross-target identity (Party C's registry path) rejects.
  $crossRoot=Join-Path $root 'cross';[IO.Directory]::CreateDirectory($crossRoot)|Out-Null;$crossTarget=Join-Path $crossRoot 'REGISTRY.json';New-ReservedZeroByteFixture -Path $crossTarget -TestPolicy
  try{Write-CopyOnWriteTransaction -Target $crossTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$crossRejected=$false}catch{$crossRejected=$_.Exception.Message-like'TARGET_IDENTITY_MISMATCH:*'}
  Add-Test 'T3D-C1-B-CROSS-TARGET' ($crossRejected-and(([IO.FileInfo]::new($crossTarget)).Length-eq0)) 'writer rejects a cross-shaped target by literal identity before any mutation'

  # RV03 explicit case: failure after publication (AfterReplace) during a
  # reservation-claim initialization must restore the exact zero-byte
  # reservation content and security, not merely throw.
  $postReplaceTarget=Join-Path $root 'post-replace/LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $postReplaceTarget -TestPolicy
  $postReplacePreSecurity=Get-SecurityState $postReplaceTarget
  try{Write-CopyOnWriteTransaction -Target $postReplaceTarget -FinalBytes ([Text.Encoding]::UTF8.GetBytes('should-not-persist')) -InjectFailure AfterReplace -RequireReservation -TestPolicy -LedgerPath $ledger;$postReplaceFailed=$false}catch{$postReplaceFailed=$_.Exception.Message-like'ROLLBACK_INJECTED_AFTER_REPLACE:*'}
  $postReplacePostSecurity=Get-SecurityState $postReplaceTarget
  Add-Test 'T3D-C1-B-POST-REPLACE-ROLLBACK' ($postReplaceFailed-and(([IO.FileInfo]::new($postReplaceTarget)).Length-eq0)-and(Test-SecurityStateExact $postReplacePostSecurity $postReplacePreSecurity.ownerSid $postReplacePreSecurity.protectionState $postReplacePreSecurity.aces)) 'post-replacement failure during reservation-claim initialize restores exact zero-byte content and exact pre-transaction security descriptor'
  Add-Test 'T3D-C1-B-POST-REPLACE-NO-RESIDUE' (@(Get-ChildItem (Split-Path $postReplaceTarget) -Force -Filter '*.tmp').Count-eq0) 'no rollback-temp residue after restoration'

  # RV02 negative: unknown sibling in the reservation directory blocks initialization.
  $siblingTarget=Join-Path $root 'sibling/LOOKUP_RESPONSES.jsonl';New-ReservedZeroByteFixture -Path $siblingTarget -TestPolicy
  [IO.File]::WriteAllBytes((Join-Path $root 'sibling/unregistered.bin'),[Text.Encoding]::UTF8.GetBytes('preserve'))
  try{Write-CopyOnWriteTransaction -Target $siblingTarget -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger;$siblingRejected=$false}catch{$siblingRejected=$_.Exception.Message-like'UNKNOWN_RESIDUE_PRESENT:*'}
  Add-Test 'T3D-C1-B-SIBLING' ($siblingRejected-and(([IO.FileInfo]::new($siblingTarget)).Length-eq0)-and(Test-Path (Join-Path $root 'sibling/unregistered.bin'))) 'unknown sibling blocks reservation-claim initialization and is preserved untouched'

  foreach($point in @('AfterAcquire','AfterTempFlush','BeforeReplace','AfterReplace')){$before=[IO.File]::ReadAllBytes($target);$failure='none';try{Write-CopyOnWriteTransaction $target ([Text.Encoding]::UTF8.GetBytes('bad')) -InjectFailure $point -TestPolicy -LedgerPath $ledger;$failed=$false}catch{$failed=$true;$failure=$_.Exception.Message};Add-Test "T3D-C1-B-ROLLBACK-$point" ($failed-and(Test-BytesEqual ([IO.File]::ReadAllBytes($target)) $before)) ('atomic rollback preserves bytes; '+$failure)}
  $hardeningDir=Join-Path $root 'hardening';[IO.Directory]::CreateDirectory($hardeningDir)|Out-Null;try{Write-HardenedTemp $hardeningDir '.cvf-g4-response-' $prefix -TestPolicy -InjectHardeningFailure|Out-Null;$hardeningFailed=$false}catch{$hardeningFailed=$true};Add-Test 'T3D-C1-B-HARDEN-FAIL' ($hardeningFailed-and@(Get-ChildItem $hardeningDir -Force -Filter '*.tmp').Count-eq0) 'temp helper removes its own artifact when hardening fails'

  # R2-07: real second OS process for initialization; ENTERED must not precede PARENT_RELEASE.
  $initPeerRoot=Join-Path $root 'init-peer';$initPeerPaths=Get-TestFixturePaths $initPeerRoot;[IO.Directory]::CreateDirectory($initPeerPaths.root)|Out-Null;New-ReservedZeroByteFixture -Path $initPeerPaths.responses -TestPolicy
  $initRun=[Guid]::NewGuid().ToString('N');$initEvents=New-PeerEvents $initRun;$initPsi=[Diagnostics.ProcessStartInfo]::new();$initPsi.FileName=(Get-Command pwsh).Source;$initPsi.UseShellExecute=$false;$initPsi.CreateNoWindow=$true;foreach($a in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$initRun,'-PeerFixtureRoot',$initPeerRoot,'-PeerExpectInitialize')){$initPsi.ArgumentList.Add($a)};$initPeer=[Diagnostics.Process]::Start($initPsi)
  try{Add-Test 'T3D-C1-B-INIT-PEER-READY' ($initEvents.Ready.WaitOne(15000)) 'READY observed for real second-process initializer';$initParent=$null;try{Write-CopyOnWriteTransaction -Target $initPeerPaths.responses -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -ParentBarrierEvents $initEvents -LedgerPath $ledger;$initParent=$true}catch{$initParent=$false};Add-Test 'T3D-C1-B-INIT-PEER-PARENT' $initParent 'parent executed production reservation-claim initialize';Add-Test 'T3D-C1-B-INIT-PEER-ATTEMPTING' ($initEvents.Attempting.WaitOne(0)) 'ATTEMPTING observed while parent held guard';Add-Test 'T3D-C1-B-INIT-PEER-ENTERED' ($initEvents.Entered.WaitOne(15000)) 'ENTERED after release, never before';$initPeer.WaitForExit(15000)|Out-Null;Add-Test 'T3D-C1-B-INIT-PEER-EXIT' ($initPeer.HasExited-and$initPeer.ExitCode-eq0) 'real peer exited zero (RESERVATION_NONZERO on already-initialized target)'}finally{if(-not$initPeer.HasExited){$initPeer.Kill($true)};$initPeer.Dispose();@($initEvents.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}

  $appendRoot=Join-Path $root 'append-peer';$append=New-LookupFixture $appendRoot $registryBytes;$run=[Guid]::NewGuid().ToString('N');$events=New-PeerEvents $run;$psi=[Diagnostics.ProcessStartInfo]::new();$psi.FileName=(Get-Command pwsh).Source;$psi.UseShellExecute=$false;$psi.CreateNoWindow=$true;foreach($a in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$run,'-PeerFixtureRoot',$appendRoot)){$psi.ArgumentList.Add($a)};$peer=[Diagnostics.Process]::Start($psi)
  try{Add-Test 'T3D-C1-B-PEER-READY' ($events.Ready.WaitOne(15000)) 'READY';$parentResult=Invoke-LookupAppendTransaction $append $append.request $python -TestPolicy -ParentBarrierEvents $events -LedgerPath $ledger;Add-Test 'T3D-C1-B-PEER-PARENT' ($parentResult.result-ceq'APPENDED_PENDING_LOCAL_VERIFICATION') 'parent executed production append';Add-Test 'T3D-C1-B-PEER-ATTEMPTING' ($events.Attempting.WaitOne(0)) 'peer attempted production append';Add-Test 'T3D-C1-B-PEER-ENTERED' ($events.Entered.WaitOne(15000)) 'peer entered after release';Add-Test 'T3D-C1-B-PEER-COMPLETE' ($events.Complete.WaitOne(15000)) 'peer returned idempotent';$peer.WaitForExit(15000)|Out-Null;Add-Test 'T3D-C1-B-PEER-EXIT' ($peer.HasExited-and$peer.ExitCode-eq0) 'peer exit zero';$rows=@(([Text.Encoding]::UTF8.GetString([IO.File]::ReadAllBytes($append.responses))).TrimEnd("`n")-split"`n");Add-Test 'T3D-C1-B-PEER-ONCE' ($rows.Count-eq1) 'concurrent identical UUID leaves exactly one row'}finally{if(-not$peer.HasExited){$peer.Kill($true)};$peer.Dispose();@($events.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}

  $releaseRoot=Join-Path $root 'after-acquire-peer';$releasePaths=New-LookupFixture $releaseRoot $registryBytes;try{Write-CopyOnWriteTransaction $releasePaths.responses ([Text.Encoding]::UTF8.GetBytes('bad')) -InjectFailure AfterAcquire -TestPolicy -LedgerPath $ledger;$injected=$false}catch{$injected=$_.Exception.Message-like'ROLLBACK_INJECTED_AFTER_ACQUIRE:*'};$releaseRun=[Guid]::NewGuid().ToString('N');$releaseEvents=New-PeerEvents $releaseRun;$releasePsi=[Diagnostics.ProcessStartInfo]::new();$releasePsi.FileName=(Get-Command pwsh).Source;$releasePsi.UseShellExecute=$false;$releasePsi.CreateNoWindow=$true;foreach($a in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$releaseRun,'-PeerFixtureRoot',$releaseRoot,'-PeerExpectAppend')){$releasePsi.ArgumentList.Add($a)};$releasePeer=[Diagnostics.Process]::Start($releasePsi);try{Add-Test 'T3D-C1-B-AFTER-ACQUIRE-READY' ($injected-and$releaseEvents.Ready.WaitOne(15000)) 'second process ready after injected acquisition failure';$releaseEvents.ParentRelease.Set()|Out-Null;$releaseEvents.StartAttempt.Set()|Out-Null;Add-Test 'T3D-C1-B-AFTER-ACQUIRE-ENTERED' ($releaseEvents.Entered.WaitOne(15000)) 'second process acquired same-target guard';Add-Test 'T3D-C1-B-AFTER-ACQUIRE-COMPLETE' ($releaseEvents.Complete.WaitOne(15000)) 'second process completed production append';$releasePeer.WaitForExit(15000)|Out-Null;Add-Test 'T3D-C1-B-AFTER-ACQUIRE-EXIT' ($releasePeer.HasExited-and$releasePeer.ExitCode-eq0) 'same-target successor exited zero'}finally{if(-not$releasePeer.HasExited){$releasePeer.Kill($true)};$releasePeer.Dispose();@($releaseEvents.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}

  foreach($point in @('AfterAcquireBeforeMutation','AfterTempFlush','BeforeReplace')){$crashRoot=Join-Path $root ("append-crash-$point");$crashPaths=New-LookupFixture $crashRoot $registryBytes;$crashRun=[Guid]::NewGuid().ToString('N');$barrier=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4B_CRASH_$crashRun");$crashPsi=[Diagnostics.ProcessStartInfo]::new();$crashPsi.FileName=(Get-Command pwsh).Source;$crashPsi.UseShellExecute=$false;$crashPsi.CreateNoWindow=$true;foreach($a in @('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-CrashMode','-CrashRunId',$crashRun,'-CrashFixtureRoot',$crashRoot,'-CrashPoint',$point)){$crashPsi.ArgumentList.Add($a)};$crash=[Diagnostics.Process]::Start($crashPsi);try{Add-Test "T3D-C1-B-CRASH-$point-BARRIER" ($barrier.WaitOne(15000)) 'production append reached barrier';$crash.Kill($true);$crash.WaitForExit(15000)|Out-Null;Add-Test "T3D-C1-B-CRASH-$point-KILLED" $crash.HasExited 'append worker hard terminated';$ownedPatterns=@('.cvf-g4-response-*.tmp','.cvf-g4-capture-*.tmp');$hasOwnedTemp=@($ownedPatterns|ForEach-Object{Get-ChildItem $crashRoot -Force -Filter $_}).Count-gt0;if($hasOwnedTemp){try{Invoke-LookupAppendTransaction $crashPaths $crashPaths.request $python -TestPolicy -LedgerPath $ledger|Out-Null;$blocked=$false}catch{$blocked=$_.Exception.Message-like'UNKNOWN_RESIDUE_PRESENT:*'};Add-Test "T3D-C1-B-CRASH-$point-RESIDUE-BLOCKS" ($blocked-and(@($ownedPatterns|ForEach-Object{Get-ChildItem $crashRoot -Force -Filter $_}).Count-gt0)) 'ordinary successor fails closed on ledger-bound residue; only admin recovery may clear it';foreach($pattern in $ownedPatterns){foreach($residue in @(Get-ChildItem $crashRoot -Force -Filter $pattern)){Remove-Item -LiteralPath $residue.FullName -Force}};$recovered=Invoke-LookupAppendTransaction $crashPaths $crashPaths.request $python -TestPolicy -LedgerPath $ledger}else{$recovered=Invoke-LookupAppendTransaction $crashPaths $crashPaths.request $python -TestPolicy -LedgerPath $ledger};Add-Test "T3D-C1-B-CRASH-$point-RECOVER" ($recovered.result-ceq'APPENDED_PENDING_LOCAL_VERIFICATION') 'successor production append recovered after residue clearance';$count=@(([Text.Encoding]::UTF8.GetString([IO.File]::ReadAllBytes($crashPaths.responses))).TrimEnd("`n")-split"`n").Count;Add-Test "T3D-C1-B-CRASH-$point-ONCE" ($count-eq1) 'recovery leaves one complete row';Add-Test "T3D-C1-B-CRASH-$point-CLEAN" (@(Get-ChildItem $crashRoot -Force -Filter '*.tmp').Count-eq0) 'no residue after admin-equivalent clearance'}finally{if(-not$crash.HasExited){$crash.Kill($true)};$crash.Dispose();$barrier.Dispose()}}

  $testOwner=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value;foreach($kind in @('EXTRA_ALLOW','DENY','INHERITED','UNPROTECTED')){$caseDir=Join-Path $root ("descriptor-$kind");[IO.Directory]::CreateDirectory($caseDir)|Out-Null;$caseTarget=Join-Path $caseDir 'LOG.jsonl';[IO.File]::WriteAllBytes($caseTarget,$prefix);Set-ExactSecurity $caseTarget -TestPolicy;Set-AdversarialSecurity $caseTarget $kind;$captured=Get-SecurityState $caseTarget;$shapeValid=switch($kind){'EXTRA_ALLOW'{@($captured.aces).Count-gt1}'DENY'{@($captured.aces|Where-Object accessType -eq 1).Count-gt0}'INHERITED'{(-not$captured.protectionState)-and@($captured.aces|Where-Object isInherited).Count-gt0}'UNPROTECTED'{-not$captured.protectionState}};$failureMessage='none';try{Write-CopyOnWriteTransaction $caseTarget $multi -InjectFailure AfterReplace -TestPolicy -LedgerPath $ledger;$rolled=$false}catch{$failureMessage=$_.Exception.Message;$actual=Get-SecurityState $caseTarget;$rolled=$shapeValid-and(Test-BytesEqual ([IO.File]::ReadAllBytes($caseTarget)) $prefix)-and(Test-SecurityStateExact $actual $captured.ownerSid $captured.protectionState $captured.aces)};Add-Test "T3D-C1-B-DESCRIPTOR-$kind" $rolled ('atomic rollback restored actual adversarial descriptor and bytes; '+$failureMessage)}
  $ownerDir=Join-Path $root 'descriptor-WRONG_OWNER';[IO.Directory]::CreateDirectory($ownerDir)|Out-Null;$ownerTarget=Join-Path $ownerDir 'LOG.jsonl';[IO.File]::WriteAllBytes($ownerTarget,$prefix);Set-ExactSecurity $ownerTarget -TestPolicy;try{Set-AdversarialSecurity $ownerTarget WRONG_OWNER;$ownerDenied=$false;$ownerError='mutation unexpectedly succeeded'}catch{$ownerError=$_.Exception.Message;$ownerAfter=Get-SecurityState $ownerTarget;$ownerDenied=$ownerError-like'*security identifier is not allowed to be the owner*'-and$ownerAfter.ownerSid-ceq$testOwner};Add-Test 'T3D-C1-B-DESCRIPTOR-WRONG_OWNER-CAPABILITY' $ownerDenied ('current token cannot create a distinct-owner fixture; no rollback claim: '+$ownerError)

  $badRoot=Join-Path $root 'bad-security';$badPaths=New-LookupFixture $badRoot $registryBytes;Set-AdversarialSecurity $badPaths.responses EXTRA_ALLOW;$badBefore=[IO.File]::ReadAllBytes($badPaths.responses);$badState=Get-SecurityState $badPaths.responses;try{Invoke-LookupAppendTransaction $badPaths $badPaths.request $python -TestPolicy -LedgerPath $ledger|Out-Null;$badRejected=$false}catch{$badAfter=Get-SecurityState $badPaths.responses;$badRejected=$_.Exception.Message-like'SECURITY_STATE_MISMATCH:*'-and(Test-BytesEqual ([IO.File]::ReadAllBytes($badPaths.responses)) $badBefore)-and(Test-SecurityStateExact $badAfter $badState.ownerSid $badState.protectionState $badState.aces)};Add-Test 'T3D-C1-B-PRESTATE-SECURITY' $badRejected 'production append rejects widened descriptor before mutation'

  $expected=@(Get-ExpectedAceVector -TestPolicy);$owner=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value;$valid=[pscustomobject]@{ownerSid=$owner;protectionState=$true;aces=$expected};Add-Test 'T3D-C1-B-SEC-VALID' (Test-SecurityModel $valid $owner $expected) 'exact model accepted';$wrongOwnerModel=[pscustomobject]@{ownerSid=$script:AdministratorsSid;protectionState=$true;aces=$expected};Add-Test 'T3D-C1-B-SEC-WRONG-OWNER' (-not(Test-SecurityModel $wrongOwnerModel $owner $expected)) 'complete-state oracle rejects non-expected owner';Add-Test 'T3D-C1-B-FRAME-VALID' (Test-StrictJsonlFraming $prefix) 'valid LF accepted';Add-Test 'T3D-C1-B-FRAME-BOM' (-not(Test-StrictJsonlFraming ([byte[]](0xef,0xbb,0xbf)+$prefix))) 'BOM rejected';Add-Test 'T3D-C1-B-FRAME-CRLF' (-not(Test-StrictJsonlFraming ([Text.Encoding]::UTF8.GetBytes("{}`r`n")))) 'CRLF rejected';Add-Test 'T3D-C1-B-FRAME-BLANK' (-not(Test-StrictJsonlFraming ([Text.Encoding]::UTF8.GetBytes("{}`n`n")))) 'blank rejected';Add-Test 'T3D-C1-B-FRAME-PARTIAL' (-not(Test-StrictJsonlFraming ([Text.Encoding]::UTF8.GetBytes('{}')))) 'partial rejected';$checker=Join-Path (Split-Path -Parent (Split-Path -Parent $script:ScriptPath)) 'governance/compat/check_acel_g1_issuer_registry.py';$checkerRun=Invoke-PythonRuntime $python @($checker,'--self-test');Add-Test 'T3D-C1-B-CHECKER-TAXONOMY' ($checkerRun.exitCode-eq0-and($checkerRun.output-join"`n")-like'*"result": "PASS"*') 'executable checker taxonomy suite passed';try{Get-TestFixturePaths (Join-Path (Split-Path -Parent $root) 'outside')|Out-Null;$contained=$false}catch{$contained=$_.Exception.Message-like'TEST_CONTAINMENT_VIOLATION:*'};Add-Test 'T3D-C1-B-CONTAINMENT' $contained 'peer/crash fixture cannot escape disposable root';$junctionOutside=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4b-junction-target-'+[Guid]::NewGuid().ToString('N'));$junction=Join-Path $root 'nested-junction';[IO.Directory]::CreateDirectory($junctionOutside)|Out-Null;try{New-Item -ItemType Junction -Path $junction -Target $junctionOutside|Out-Null;try{Get-TestFixturePaths (Join-Path $junction 'fixture')|Out-Null;$nestedContained=$false}catch{$nestedContained=$_.Exception.Message-like'TEST_CONTAINMENT_VIOLATION:*'};Add-Test 'T3D-C1-B-NESTED-REPARSE' $nestedContained 'component walk rejects intermediate junction'}finally{if(Test-Path $junction){Remove-Item -LiteralPath $junction -Force};if(Test-Path $junctionOutside){Remove-Item -LiteralPath $junctionOutside -Force}};Add-Test 'T3D-C1-B-DEFAULT' ($PSCmdlet.ParameterSetName-eq'SelfTest') 'default mode self-test';[pscustomobject]@{result='PASS';tests=$script:Tests.Count;peerProtocol=@('READY','START_ATTEMPT','ATTEMPTING','PARENT_RELEASE','ENTERED','COMPLETE');sourceMutation=$false}|ConvertTo-Json -Compress
 }finally{if(Test-Path $root){Remove-Item -LiteralPath $root -Recurse -Force}}
}
if($PSCmdlet.ParameterSetName-eq'Peer'){Invoke-PeerMode}
if($PSCmdlet.ParameterSetName-eq'Crash'){Invoke-CrashMode}
if($PSCmdlet.ParameterSetName-eq'SelfTest'){Invoke-SelfTest;exit 0}
$paths=Assert-PrincipalAndPaths $RepositoryRoot $Confirmation
$python=Resolve-PythonRuntime $PythonExecutablePath
if($PSCmdlet.ParameterSetName-eq'Initialize'){if(-not(Test-Path $paths.registry)){Stop-Writer 'SOURCE_UNAVAILABLE' 'registry required'};Write-CopyOnWriteTransaction -Target $paths.responses -FinalBytes ([byte[]]::new(0)) -RequireReservation -RegistryPath $paths.registry -CheckerPath $paths.checker -PythonRuntime $python -LedgerPath $paths.ledger -TransactionId $TransactionId -AuthorizationPath $AuthorizationPath;[pscustomobject]@{result='RESPONSE_LOG_INITIALIZED_PENDING_LOCAL_POSTFLIGHT';path=$script:ResponseRelative;sha256=(Get-Sha256Hex ([byte[]]::new(0)));transactionId=$TransactionId}|ConvertTo-Json -Compress;exit 0}
$result=Invoke-LookupAppendTransaction $paths (Get-CanonicalPath $RequestJsonPath) $python -LedgerPath $paths.ledger;$result|ConvertTo-Json -Depth 8 -Compress
