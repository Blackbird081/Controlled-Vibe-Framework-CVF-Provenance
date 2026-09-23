<#
.SYNOPSIS
Bounded Party B/Party C probe surface for the ACEL G1 Group 4 disposable-root proof.

.DESCRIPTION
The probe accepts one hash-bound envelope, verifies the exact current Windows
identity and a non-elevated token, confines every path to one
%TEMP%\cvf-g4-actual-token-* root, performs one allow/deny probe, and writes a
fact record. It never accepts or stores a password and never emits the final
Local verdict. TestPolicy is restricted to cvf-g4-actual-token-test-* roots and
is permanently marked as non-actual evidence.
#>
[CmdletBinding(DefaultParameterSetName='SelfTest')]
param(
    [Parameter(ParameterSetName='SelfTest')][switch]$SelfTest,
    [Parameter(ParameterSetName='Execute',Mandatory=$true)][switch]$ExecuteProbe,
    [Parameter(ParameterSetName='Execute',Mandatory=$true)][string]$EnvelopePath,
    [Parameter(ParameterSetName='Execute')][switch]$TestPolicy,
    [Parameter(ParameterSetName='Peer',Mandatory=$true)][switch]$PeerMode,
    [Parameter(ParameterSetName='Peer',Mandatory=$true)][string]$PeerRunId,
    [Parameter(ParameterSetName='Peer',Mandatory=$true)][string]$PeerTargetPath,
    [Parameter(ParameterSetName='Peer')][switch]$InjectAfterAcquire,
    [Parameter(ParameterSetName='Peer')][switch]$PeerTestPolicy,
    [Parameter(ParameterSetName='Crash',Mandatory=$true)][switch]$CrashMode,
    [Parameter(ParameterSetName='Crash',Mandatory=$true)][string]$CrashRunId,
    [Parameter(ParameterSetName='Crash',Mandatory=$true)][string]$CrashTargetPath,
    [Parameter(ParameterSetName='Crash')][switch]$CrashTestPolicy
)

Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$script:ScriptPath=$PSCommandPath
$script:RepoRoot=Split-Path -Parent (Split-Path -Parent $script:ScriptPath)
$script:RealSource=Join-Path $script:RepoRoot 'governance/sources/issuer_registry'
$script:PartyBName='LAM-RUBY\cvf-g1-party-b'
$script:PartyBSid='S-1-5-21-1644666849-912006174-747199667-1009'
$script:PartyCName='LAM-RUBY\cvf-g1-party-c'
$script:PartyCSid='S-1-5-21-1644666849-912006174-747199667-1010'
$script:LocalSid='S-1-5-21-1644666849-912006174-747199667-1001'
$script:SystemSid='S-1-5-18'
$script:AdministratorsSid='S-1-5-32-544'
$script:Actions=@('OWN_TARGET_PUBLICATION','CROSS_TARGET_MUTATION','OWNER_DACL_MUTATION','PARENT_MUTATION','ALLOWED_TEMP','REPARSE_JUNCTION','HARDLINK','SIBLING_DRIFT','SECURITY_DRIFT','CONCURRENCY','CRASH_ROLLBACK')
$script:Tests=[Collections.Generic.List[object]]::new()

function Stop-Probe([string]$Code,[string]$Message){throw [InvalidOperationException]::new("${Code}: ${Message}")}
function Get-CanonicalPath([string]$Path){[IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar)}
function Get-Sha256Hex([byte[]]$Bytes){$sha=[Security.Cryptography.SHA256]::Create();try{([Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant()}finally{$sha.Dispose()}}
function Get-FileSha256([string]$Path){Get-Sha256Hex ([IO.File]::ReadAllBytes($Path))}
function Get-MutexName([string]$Target){'Global\CVF_G4_ACTUAL_PROBE_'+(Get-Sha256Hex ([Text.Encoding]::UTF8.GetBytes((Get-CanonicalPath $Target).ToUpperInvariant()))).Substring(0,48)}

function Assert-NoReparseTraversal([string]$BasePath,[string]$CandidatePath){
    $base=Get-CanonicalPath $BasePath;$candidate=Get-CanonicalPath $CandidatePath
    $prefix=$base+[IO.Path]::DirectorySeparatorChar
    if($candidate-cne$base-and-not$candidate.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $candidate}
    $current=$base
    if(Test-Path -LiteralPath $current){if((Get-Item -LiteralPath $current -Force).Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Probe 'PROBE_REPARSE_REJECTED' $current}}
    if($candidate-cne$base){foreach($part in $candidate.Substring($prefix.Length)-split'[\\/]'){$current=Join-Path $current $part;if(Test-Path -LiteralPath $current){if((Get-Item -LiteralPath $current -Force).Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Probe 'PROBE_REPARSE_REJECTED' $current}}}}
}

function Assert-DisposablePath([string]$Path,[bool]$IsTest){
    $temp=Get-CanonicalPath ([IO.Path]::GetTempPath());$full=Get-CanonicalPath $Path;$prefix=$temp+[IO.Path]::DirectorySeparatorChar
    if(-not$full.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $full}
    $leaf=(($full.Substring($prefix.Length))-split'[\\/]')[0]
    $pattern=if($IsTest){'cvf-g4-actual-token-test-*'}else{'cvf-g4-actual-token-*'}
    if($leaf-notlike$pattern-or(-not$IsTest-and$leaf-like'cvf-g4-actual-token-test-*')){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $full}
    $real=Get-CanonicalPath $script:RealSource;$repo=Get-CanonicalPath $script:RepoRoot;$userProfilePath=Get-CanonicalPath ([Environment]::GetFolderPath('UserProfile'))
    foreach($forbidden in @($real,$repo)){if($full-ieq$forbidden-or$full.StartsWith($forbidden+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)-or$forbidden.StartsWith($full+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_REAL_SOURCE_REACHED' $full}}
    if($full-ieq$userProfilePath-or$userProfilePath.StartsWith($full+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_REAL_SOURCE_REACHED' $full}
    $root=Join-Path $temp $leaf;Assert-NoReparseTraversal $temp $root;Assert-NoReparseTraversal $root $full
    return $full
}
function Assert-DisposableLexicalPath([string]$Path,[bool]$IsTest){
    $temp=Get-CanonicalPath ([IO.Path]::GetTempPath());$full=Get-CanonicalPath $Path;$prefix=$temp+[IO.Path]::DirectorySeparatorChar
    if(-not$full.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $full}
    $leaf=(($full.Substring($prefix.Length))-split'[\\/]')[0];$pattern=if($IsTest){'cvf-g4-actual-token-test-*'}else{'cvf-g4-actual-token-*'}
    if($leaf-notlike$pattern-or(-not$IsTest-and$leaf-like'cvf-g4-actual-token-test-*')){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $full}
    $root=Join-Path $temp $leaf;$repo=Get-CanonicalPath $script:RepoRoot;$real=Get-CanonicalPath $script:RealSource
    foreach($forbidden in @($repo,$real)){if($full-ieq$forbidden-or$full.StartsWith($forbidden+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)-or$forbidden.StartsWith($full+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_REAL_SOURCE_REACHED' $full}}
    Assert-NoReparseTraversal $temp $root;return $full
}

function Get-AceTuples($Security){@($Security.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier])|ForEach-Object{'{0}|{1}|{2}|{3}|{4}|{5}'-f$_.IdentityReference.Value,[int]$_.FileSystemRights,[int]$_.AccessControlType,[bool]$_.IsInherited,[int]$_.InheritanceFlags,[int]$_.PropagationFlags}|Sort-Object -CaseSensitive)}
function Get-SecurityState([string]$Path,[bool]$Directory){
    try{$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$obj=if($Directory){[IO.DirectoryInfo]::new($Path)}else{[IO.FileInfo]::new($Path)};$acl=[IO.FileSystemAclExtensions]::GetAccessControl($obj,$sections);[ordered]@{readable=$true;ownerSid=$acl.GetOwner([Security.Principal.SecurityIdentifier]).Value;protectionState=[bool]$acl.AreAccessRulesProtected;aces=@(Get-AceTuples $acl)}}catch{[ordered]@{readable=$false;error=$_.Exception.GetType().FullName}}
}
function Get-HardLinkCount([string]$Path){$out=& fsutil hardlink list $Path 2>&1;if($LASTEXITCODE-ne0){return -1};@($out|Where-Object{$_.Trim().Length-gt0}).Count}
function Test-ExpectedReservationSecurity([string]$Path,[string]$Role,[bool]$IsTest){
    $state=Get-SecurityState $Path $false;if(-not$state.readable-or-not$state.protectionState){return $false};$full=[int][Security.AccessControl.FileSystemRights]::FullControl
    if($IsTest){$sid=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value;$expected=@("$sid|$full|0|False|0|0")}
    else{$owner=if($Role-ceq'PARTY_B'){$script:PartyBSid}else{$script:PartyCSid};$probe=[Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new($script:LocalSid),[Security.AccessControl.FileSystemRights]::Read,[Security.AccessControl.AccessControlType]::Allow);$read=[int]$probe.FileSystemRights;$expected=@("$owner|$full|0|False|0|0","$script:SystemSid|$full|0|False|0|0","$script:AdministratorsSid|$full|0|False|0|0","$script:LocalSid|$read|0|False|0|0")|Sort-Object -CaseSensitive;if($state.ownerSid-cne$owner){return $false}}
    return (($state.aces-join"`n")-ceq($expected-join"`n"))
}
function Get-PathState([string]$Path){
    $full=Get-CanonicalPath $Path
    if(-not(Test-Path -LiteralPath $full)){return [ordered]@{path=$full;exists=$false}}
    $item=Get-Item -LiteralPath $full -Force;$isDir=[bool]$item.PSIsContainer
    $state=[ordered]@{path=$full;exists=$true;isDirectory=$isDir;attributes=[int]$item.Attributes;reparse=[bool]($item.Attributes-band[IO.FileAttributes]::ReparsePoint);security=Get-SecurityState $full $isDir}
    if(-not$isDir){$state.length=[int64]$item.Length;$state.sha256=Get-FileSha256 $full;$state.linkCount=Get-HardLinkCount $full}
    elseif($state.reparse){$state.children=@()}
    else{$state.children=@(Get-ChildItem -LiteralPath $full -Force|ForEach-Object{$_.Name}|Sort-Object -CaseSensitive)}
    return $state
}

function Get-EnvelopeBinding($Envelope){
    $fields=@('schema','runId','role','action','expectedAccountName','expectedSid','disposableRoot','protectedParent','ownTarget','otherTarget','evidencePath','payloadPath','expectedOutcome','testPolicy','issuedAtUtc')
    $values=[Collections.Generic.List[string]]::new()
    foreach($field in $fields){if($Envelope.PSObject.Properties.Name-cnotcontains$field){Stop-Probe 'PROBE_ENVELOPE_FIELD_SET_INVALID' $field};$value=$Envelope.$field;if($value-is[bool]){$values.Add($value.ToString().ToLowerInvariant())}elseif($value-is[datetime]){$values.Add($value.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffZ'))}else{$values.Add([string]$value)}}
    return Get-Sha256Hex ([Text.Encoding]::UTF8.GetBytes(($values.ToArray()-join"`n")))
}

function Assert-Envelope($Envelope,[bool]$IsTest){
    $expected=@('schema','runId','role','action','expectedAccountName','expectedSid','disposableRoot','protectedParent','ownTarget','otherTarget','evidencePath','payloadPath','expectedOutcome','testPolicy','issuedAtUtc','bindingSha256Hex')|Sort-Object
    $actual=@($Envelope.PSObject.Properties.Name)|Sort-Object
    if(($actual-join',')-cne($expected-join',')){Stop-Probe 'PROBE_ENVELOPE_FIELD_SET_INVALID' ($actual-join',')}
    if($Envelope.schema-cne'cvf.g4.actualTokenProbeEnvelope.v1'){Stop-Probe 'PROBE_ENVELOPE_SCHEMA_INVALID' ([string]$Envelope.schema)}
    if($Envelope.role-cnotin@('PARTY_B','PARTY_C')-or$script:Actions-cnotcontains[string]$Envelope.action){Stop-Probe 'PROBE_ROLE_OR_ACTION_INVALID' "$($Envelope.role)/$($Envelope.action)"}
    if([bool]$Envelope.testPolicy-ne$IsTest){Stop-Probe 'PROBE_TEST_POLICY_MISMATCH' ([string]$Envelope.testPolicy)}
    $computedBinding=Get-EnvelopeBinding $Envelope
    if([string]$Envelope.bindingSha256Hex-cne$computedBinding){Stop-Probe 'PROBE_ENVELOPE_HASH_MISMATCH' ("$($Envelope.runId): $($Envelope.bindingSha256Hex) != $computedBinding")}
    $root=Assert-DisposablePath ([string]$Envelope.disposableRoot) $IsTest
    foreach($field in @('protectedParent','ownTarget','otherTarget','evidencePath')){$resolved=if($Envelope.action-ceq'REPARSE_JUNCTION'-and$field-cne'evidencePath'){Assert-DisposableLexicalPath ([string]$Envelope.$field) $IsTest}else{Assert-DisposablePath ([string]$Envelope.$field) $IsTest};if(-not$resolved.StartsWith($root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $resolved}}
    if([string]$Envelope.payloadPath){$resolved=Assert-DisposablePath ([string]$Envelope.payloadPath) $IsTest;if(-not$resolved.StartsWith($root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $resolved}}
}

function Get-TokenFacts {
    $identity=[Security.Principal.WindowsIdentity]::GetCurrent();$principal=[Security.Principal.WindowsPrincipal]::new($identity)
    [ordered]@{name=$identity.Name;sid=$identity.User.Value;isAdministrator=$principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator);groups=@($identity.Groups|ForEach-Object{$_.Value}|Sort-Object -Unique)}
}
function Assert-Token($Envelope,[bool]$IsTest){
    $facts=Get-TokenFacts
    if($facts.name-cne[string]$Envelope.expectedAccountName-or$facts.sid-cne[string]$Envelope.expectedSid){Stop-Probe 'PROBE_PRINCIPAL_MISMATCH' "$($facts.name)/$($facts.sid)"}
    if(-not$IsTest){$expectedName=if($Envelope.role-ceq'PARTY_B'){$script:PartyBName}else{$script:PartyCName};$expectedSid=if($Envelope.role-ceq'PARTY_B'){$script:PartyBSid}else{$script:PartyCSid};if($facts.name-cne$expectedName-or$facts.sid-cne$expectedSid){Stop-Probe 'PROBE_PRINCIPAL_MISMATCH' 'verified principal constants differ'}}
    if($facts.isAdministrator){Stop-Probe 'PROBE_ELEVATED_TOKEN_REJECTED' $facts.name}
    return $facts
}

function Enter-Guard([string]$Target,[bool]$Inject){$m=$null;$held=$false;try{$m=[Threading.Mutex]::new($false,(Get-MutexName $Target));try{$held=$m.WaitOne(15000)}catch [Threading.AbandonedMutexException]{$held=$true};if(-not$held){Stop-Probe 'PROBE_CONCURRENCY_TIMEOUT' $Target};if($Inject){Stop-Probe 'PROBE_INJECTED_AFTER_ACQUIRE' $Target};return $m}catch{if($null-ne$m){if($held){try{$m.ReleaseMutex()}catch{}};$m.Dispose()};throw}}
function Exit-Guard($Mutex){if($null-ne$Mutex){try{$Mutex.ReleaseMutex()}finally{$Mutex.Dispose()}}}
function New-PeerEvents([string]$RunId){[pscustomobject]@{Ready=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${RunId}_READY");Start=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${RunId}_START");Attempting=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${RunId}_ATTEMPTING");Entered=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${RunId}_ENTERED");Complete=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${RunId}_COMPLETE")}}
function Start-SameTokenChild([string[]]$Arguments){$psi=[Diagnostics.ProcessStartInfo]::new();$psi.FileName=(Get-Command pwsh).Source;$psi.UseShellExecute=$false;$psi.CreateNoWindow=$true;foreach($arg in $Arguments){$psi.ArgumentList.Add($arg)};[Diagnostics.Process]::Start($psi)}
function Invoke-RealPeerBarrier([string]$Target,[bool]$IsTest){
    $run=[Guid]::NewGuid().ToString('N');$events=New-PeerEvents $run;$held=Enter-Guard $Target $false;$peer=$null
    try{$childArgs=@('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-PeerMode','-PeerRunId',$run,'-PeerTargetPath',$Target);if($IsTest){$childArgs+='-PeerTestPolicy'};$peer=Start-SameTokenChild $childArgs;if(-not$events.Ready.WaitOne(15000)){Stop-Probe 'PROBE_PEER_TIMEOUT' 'READY'};$events.Start.Set()|Out-Null;if(-not$events.Attempting.WaitOne(15000)){Stop-Probe 'PROBE_PEER_TIMEOUT' 'ATTEMPTING'};if($events.Entered.WaitOne(250)){Stop-Probe 'PROBE_PEER_EARLY_ENTRY' $Target};Exit-Guard $held;$held=$null;if(-not$events.Entered.WaitOne(15000)-or-not$events.Complete.WaitOne(15000)){Stop-Probe 'PROBE_PEER_TIMEOUT' 'ENTERED/COMPLETE'};$peer.WaitForExit(15000)|Out-Null;if(-not$peer.HasExited-or$peer.ExitCode-ne0){Stop-Probe 'PROBE_PEER_FAILED' ([string]$peer.ExitCode)};return [ordered]@{observed='ALLOWED';detail='READY,START_ATTEMPT,ATTEMPTING,PARENT_RELEASE,ENTERED,COMPLETE'}}finally{if($null-ne$held){Exit-Guard $held};if($null-ne$peer){if(-not$peer.HasExited){$peer.Kill($true)};$peer.Dispose()};@($events.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}
}
function Invoke-HardTerminationProbe([string]$Target,[bool]$IsTest){
    $run=[Guid]::NewGuid().ToString('N');$event=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${run}_CRASH_ACQUIRED");$child=$null
    try{$childArgs=@('-NoProfile','-NonInteractive','-File',$script:ScriptPath,'-CrashMode','-CrashRunId',$run,'-CrashTargetPath',$Target);if($IsTest){$childArgs+='-CrashTestPolicy'};$child=Start-SameTokenChild $childArgs;if(-not$event.WaitOne(15000)){Stop-Probe 'PROBE_CRASH_TIMEOUT' 'ACQUIRED'};$child.Kill($true);$child.WaitForExit(15000)|Out-Null;$successor=Enter-Guard $Target $false;try{return [ordered]@{observed='REJECTED';detail='real child hard-terminated after acquire; successor acquired abandoned guard'}}finally{Exit-Guard $successor}}finally{if($null-ne$child){if(-not$child.HasExited){$child.Kill($true)};$child.Dispose()};$event.Dispose()}
}
function Invoke-DenialMatrix([object[]]$Attempts){$denials=[Collections.Generic.List[string]]::new();foreach($attempt in $Attempts){try{& $attempt.operation;return [ordered]@{observed='UNEXPECTED_SUCCESS';detail=([string]$attempt.name+' succeeded')}}catch{$denials.Add(([string]$attempt.name+'='+$_.Exception.GetType().FullName))}};return [ordered]@{observed='DENIED';detail=($denials.ToArray()-join';')}}

function Invoke-BoundedOperation($Envelope,[bool]$IsTest){
    $action=[string]$Envelope.action;$own=[string]$Envelope.ownTarget;$other=[string]$Envelope.otherTarget;$parent=[string]$Envelope.protectedParent
    switch($action){
        'OWN_TARGET_PUBLICATION' {
            if(-not(Test-Path -LiteralPath $own -PathType Leaf)){Stop-Probe 'PROBE_RESERVATION_MISSING' $own}
            [byte[]]$bytes=[byte[]]@();if([string]$Envelope.payloadPath){$bytes=[IO.File]::ReadAllBytes([string]$Envelope.payloadPath)}
            $temp=Join-Path $parent ('.cvf-g4-actual-'+[Guid]::NewGuid().ToString('N')+'.tmp');$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$acl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.FileInfo]::new($own),$sections)
            try{$stream=[IO.File]::Open($temp,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None);try{$stream.Write($bytes,0,$bytes.Length);$stream.Flush($true)}finally{$stream.Dispose()};[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($temp),$acl);[IO.File]::Move($temp,$own,$true);return [ordered]@{observed='ALLOWED';detail='own target atomically replaced'}}finally{if(Test-Path -LiteralPath $temp){Remove-Item -LiteralPath $temp -Force}}
        }
        'ALLOWED_TEMP' {$temp=Join-Path $parent ('.cvf-g4-actual-'+[Guid]::NewGuid().ToString('N')+'.tmp');try{[IO.File]::WriteAllBytes($temp,[byte[]](1,2,3));$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$ownAcl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.FileInfo]::new($own),$sections);[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($temp),$ownAcl);return [ordered]@{observed='ALLOWED';detail='unique temp created, hardened and removed'}}finally{if(Test-Path -LiteralPath $temp){Remove-Item -LiteralPath $temp -Force}}}
        'REPARSE_JUNCTION' {try{Assert-NoReparseTraversal ([string]$Envelope.disposableRoot) $parent;Stop-Probe 'PROBE_EXPECTED_REPARSE_NOT_PRESENT' $parent}catch{if($_.Exception.Message-like'PROBE_REPARSE_REJECTED:*'){return [ordered]@{observed='REJECTED';detail='reparse component rejected before mutation'}};throw}}
        'HARDLINK' {if((Get-HardLinkCount $own)-ne1){return [ordered]@{observed='REJECTED';detail='link count is not one'}};Stop-Probe 'PROBE_EXPECTED_HARDLINK_NOT_PRESENT' $own}
        'SIBLING_DRIFT' {$allowed=@('REGISTRY.json','LOOKUP_RESPONSES.jsonl');$unknown=@(Get-ChildItem -LiteralPath $parent -Force|Where-Object{$allowed-cnotcontains$_.Name});if($unknown.Count-gt0){return [ordered]@{observed='REJECTED';detail='unexpected sibling preserved'}};Stop-Probe 'PROBE_EXPECTED_SIBLING_DRIFT_NOT_PRESENT' $parent}
        'SECURITY_DRIFT' {if(-not(Test-ExpectedReservationSecurity $own ([string]$Envelope.role) $IsTest)){return [ordered]@{observed='REJECTED';detail='owner/protection/complete ACE vector drift rejected'}};Stop-Probe 'PROBE_EXPECTED_SECURITY_DRIFT_NOT_PRESENT' $own}
        'CONCURRENCY' {return Invoke-RealPeerBarrier $own $IsTest}
        'CRASH_ROLLBACK' {return Invoke-HardTerminationProbe $own $IsTest}
        'CROSS_TARGET_MUTATION' {if($IsTest){return [ordered]@{observed='DENIED';detail='test-policy denial sentinel: overwrite,rename,delete,replace'}};$renamed=$other+'.forbidden';$replacement=Join-Path $parent ('.cvf-g4-cross-'+[Guid]::NewGuid().ToString('N')+'.tmp');$attempts=@([pscustomobject]@{name='overwrite';operation={[IO.File]::WriteAllBytes($other,[byte[]](88))}},[pscustomobject]@{name='rename';operation={[IO.File]::Move($other,$renamed)}},[pscustomobject]@{name='delete';operation={[IO.File]::Delete($other)}},[pscustomobject]@{name='replace';operation={try{[IO.File]::WriteAllBytes($replacement,[byte[]](88));[IO.File]::Replace($replacement,$other,$null,$true)}finally{if(Test-Path -LiteralPath $replacement){Remove-Item -LiteralPath $replacement -Force}}}});return Invoke-DenialMatrix $attempts}
        'OWNER_DACL_MUTATION' {if($IsTest){return [ordered]@{observed='DENIED';detail='test-policy denial sentinel: dacl,owner'}};$attempts=@([pscustomobject]@{name='dacl';operation={$acl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.FileInfo]::new($other));$acl.SetAccessRuleProtection($true,$false);[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($other),$acl)}},[pscustomobject]@{name='owner';operation={$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$acl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.FileInfo]::new($other),$sections);$acl.SetOwner([Security.Principal.WindowsIdentity]::GetCurrent().User);[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($other),$acl)}});return Invoke-DenialMatrix $attempts}
        'PARENT_MUTATION' {if($IsTest){return [ordered]@{observed='DENIED';detail='test-policy denial sentinel: child-directory,dacl,owner,rename'}};$candidate=Join-Path $parent ('forbidden-dir-'+[Guid]::NewGuid().ToString('N'));$renamed=$parent+'.forbidden';$attempts=@([pscustomobject]@{name='child-directory';operation={[IO.Directory]::CreateDirectory($candidate)|Out-Null}},[pscustomobject]@{name='dacl';operation={$acl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.DirectoryInfo]::new($parent));$acl.SetAccessRuleProtection($true,$false);[IO.FileSystemAclExtensions]::SetAccessControl([IO.DirectoryInfo]::new($parent),$acl)}},[pscustomobject]@{name='owner';operation={$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$acl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.DirectoryInfo]::new($parent),$sections);$acl.SetOwner([Security.Principal.WindowsIdentity]::GetCurrent().User);[IO.FileSystemAclExtensions]::SetAccessControl([IO.DirectoryInfo]::new($parent),$acl)}},[pscustomobject]@{name='rename';operation={[IO.Directory]::Move($parent,$renamed)}});return Invoke-DenialMatrix $attempts}
        default {Stop-Probe 'PROBE_ROLE_OR_ACTION_INVALID' $action}
    }
}

function Test-StateEqual($Left,$Right){(($Left|ConvertTo-Json -Depth 14 -Compress)-ceq($Right|ConvertTo-Json -Depth 14 -Compress))}
function Test-OperationPostconditions($Envelope,$Before,$After,$Operation){
    if([string]$Operation.observed-cne[string]$Envelope.expectedOutcome){return $false}
    if($Envelope.action-ceq'OWN_TARGET_PUBLICATION'){$expectedHash=if([string]$Envelope.payloadPath){Get-FileSha256 ([string]$Envelope.payloadPath)}else{Get-Sha256Hex ([byte[]]::new(0))};return $After.own.exists-and$After.own.sha256-ceq$expectedHash-and(Test-StateEqual $Before.other $After.other)-and(($Before.parent.security|ConvertTo-Json -Depth 8 -Compress)-ceq($After.parent.security|ConvertTo-Json -Depth 8 -Compress))-and(($After.parent.children-join',')-ceq($Before.parent.children-join','))}
    return (Test-StateEqual $Before $After)
}
function Write-Evidence($Envelope,$Token,$Before,$After,$Operation,[bool]$IsTest,[string]$Disposition,[string]$ErrorCode,[bool]$PostconditionsVerified){
    $record=[ordered]@{schema='cvf.g4.actualTokenProbeEvidence.v1';runId=[string]$Envelope.runId;role=[string]$Envelope.role;action=[string]$Envelope.action;testPolicy=$IsTest;token=$Token;expectedOutcome=[string]$Envelope.expectedOutcome;observedOutcome=if($null-ne$Operation){[string]$Operation.observed}else{'ERROR'};operationDetail=if($null-ne$Operation){[string]$Operation.detail}else{$ErrorCode};prestate=$Before;poststate=$After;postconditionsVerified=$PostconditionsVerified;disposition=$Disposition;envelopeBindingSha256Hex=[string]$Envelope.bindingSha256Hex;recordedAtUtc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')}
    $path=Get-CanonicalPath ([string]$Envelope.evidencePath);[IO.Directory]::CreateDirectory((Split-Path -Parent $path))|Out-Null
    [IO.File]::WriteAllText($path,($record|ConvertTo-Json -Depth 12 -Compress),[Text.UTF8Encoding]::new($false));return $record
}

function Invoke-Probe([string]$Path,[bool]$IsTest){
    $envelope=Get-Content -LiteralPath $Path -Raw|ConvertFrom-Json;Assert-Envelope $envelope $IsTest;$token=Assert-Token $envelope $IsTest
    $before=[ordered]@{parent=Get-PathState ([string]$envelope.protectedParent);own=Get-PathState ([string]$envelope.ownTarget);other=Get-PathState ([string]$envelope.otherTarget)};$operation=$null
    try{$operation=Invoke-BoundedOperation $envelope $IsTest;$after=[ordered]@{parent=Get-PathState ([string]$envelope.protectedParent);own=Get-PathState ([string]$envelope.ownTarget);other=Get-PathState ([string]$envelope.otherTarget)};$postOk=Test-OperationPostconditions $envelope $before $after $operation;$pass=([string]$operation.observed-ceq[string]$envelope.expectedOutcome)-and$postOk;$record=Write-Evidence $envelope $token $before $after $operation $IsTest $(if($pass){'PASS'}else{'FAIL'}) $(if($pass){$null}else{'PROBE_OUTCOME_OR_POSTCONDITION_MISMATCH'}) $postOk;if(-not$pass){Stop-Probe 'PROBE_OUTCOME_OR_POSTCONDITION_MISMATCH' "$($operation.observed) / post=$postOk"};return $record}catch{$after=[ordered]@{parent=Get-PathState ([string]$envelope.protectedParent);own=Get-PathState ([string]$envelope.ownTarget);other=Get-PathState ([string]$envelope.otherTarget)};if($null-eq$operation){Write-Evidence $envelope $token $before $after $null $IsTest 'FAIL' $_.Exception.Message $false|Out-Null};throw}
}

function Add-Test([string]$Id,[bool]$Passed,[string]$Detail){$script:Tests.Add([pscustomobject]@{id=$Id;passed=$Passed;detail=$Detail});if(-not$Passed){Stop-Probe 'PROBE_SELFTEST_FAILED' "${Id}: $Detail"}}
function New-TestEnvelope([string]$Root,[string]$Action,[string]$Expected){
    $identity=[Security.Principal.WindowsIdentity]::GetCurrent();$parent=Join-Path $Root 'source';$record=[ordered]@{schema='cvf.g4.actualTokenProbeEnvelope.v1';runId=[Guid]::NewGuid().ToString('N');role='PARTY_C';action=$Action;expectedAccountName=$identity.Name;expectedSid=$identity.User.Value;disposableRoot=$Root;protectedParent=$parent;ownTarget=Join-Path $parent 'REGISTRY.json';otherTarget=Join-Path $parent 'LOOKUP_RESPONSES.jsonl';evidencePath=Join-Path $Root "evidence/$Action.json";payloadPath='';expectedOutcome=$Expected;testPolicy=$true;issuedAtUtc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ');bindingSha256Hex=''};$obj=[pscustomobject]$record;$obj.bindingSha256Hex=Get-EnvelopeBinding $obj;return $obj
}
function Invoke-SelfTest {
    $root=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-actual-token-test-'+[Guid]::NewGuid().ToString('N'));[IO.Directory]::CreateDirectory((Join-Path $root 'source'))|Out-Null
    try{[IO.File]::WriteAllBytes((Join-Path $root 'source/REGISTRY.json'),[byte[]]::new(0));[IO.File]::WriteAllBytes((Join-Path $root 'source/LOOKUP_RESPONSES.jsonl'),[byte[]]::new(0));$envelope=New-TestEnvelope $root 'ALLOWED_TEMP' 'ALLOWED';$path=Join-Path $root 'envelope.json';[IO.File]::WriteAllText($path,($envelope|ConvertTo-Json -Depth 8 -Compress));$record=Invoke-Probe $path $true;Add-Test 'G4-PRINCIPAL-TESTPOLICY-PASS' ($record.disposition-ceq'PASS'-and$record.testPolicy) 'current-token evidence is permanently marked test policy'
        $tampered=$envelope.PSObject.Copy();$tampered.action='OWN_TARGET_PUBLICATION';try{Assert-Envelope $tampered $true;$rejected=$false}catch{$rejected=$_.Exception.Message-like'PROBE_ENVELOPE_HASH_MISMATCH:*'};Add-Test 'G4-PRINCIPAL-HASH-BINDING' $rejected 'tampered envelope rejected'
        $wrong=$envelope.PSObject.Copy();$wrong.expectedSid='S-1-0-0';$wrong.bindingSha256Hex=Get-EnvelopeBinding $wrong;try{Assert-Token $wrong $true|Out-Null;$rejected=$false}catch{$rejected=$_.Exception.Message-like'PROBE_PRINCIPAL_MISMATCH:*'};Add-Test 'G4-PRINCIPAL-IDENTITY' $rejected 'wrong SID rejected'
        try{Assert-DisposablePath $script:RealSource $true|Out-Null;$rejected=$false}catch{$rejected=$_.Exception.Message-like'PROBE_*'};Add-Test 'G4-PRINCIPAL-REAL-SOURCE' $rejected 'real source rejected'
        $failure=New-TestEnvelope $root 'CRASH_ROLLBACK' 'REJECTED';$failurePath=Join-Path $root 'failure.json';[IO.File]::WriteAllText($failurePath,($failure|ConvertTo-Json -Depth 8 -Compress));$failureRecord=Invoke-Probe $failurePath $true;Add-Test 'G4-PRINCIPAL-INJECT-RELEASE' ($failureRecord.disposition-ceq'PASS') 'after-acquire injection releases guard'
        $successor=Enter-Guard ([string]$failure.ownTarget) $false;Add-Test 'G4-PRINCIPAL-SUCCESSOR-ACQUIRE' ($null-ne$successor) 'successor acquires after injected failure';Exit-Guard $successor
        $peerResult=Invoke-RealPeerBarrier ([string]$failure.ownTarget) $true;Add-Test 'G4-PRINCIPAL-REAL-CHILD' ($peerResult.observed-ceq'ALLOWED'-and$peerResult.detail-like'READY,*COMPLETE') 'real second pwsh process is blocked before parent release and then enters'
        [pscustomobject]@{result='PASS';tests=$script:Tests.Count;testPolicyOnly=$true;realPrincipalClaimed=$false;peerProtocol=@('READY','START_ATTEMPT','ATTEMPTING','PARENT_RELEASE','ENTERED','COMPLETE')}|ConvertTo-Json -Compress
    }finally{if(Test-Path -LiteralPath $root){Remove-Item -LiteralPath $root -Recurse -Force}}
}

if($PSCmdlet.ParameterSetName-ceq'Peer'){$target=Assert-DisposablePath $PeerTargetPath ([bool]$PeerTestPolicy);$events=New-PeerEvents $PeerRunId;try{$events.Ready.Set()|Out-Null;if(-not$events.Start.WaitOne(15000)){exit 51};$events.Attempting.Set()|Out-Null;$mutex=Enter-Guard $target ([bool]$InjectAfterAcquire);try{$events.Entered.Set()|Out-Null;$events.Complete.Set()|Out-Null}finally{Exit-Guard $mutex};exit 0}finally{@($events.psobject.Properties.Value)|ForEach-Object{$_.Dispose()}}}
if($PSCmdlet.ParameterSetName-ceq'Crash'){$target=Assert-DisposablePath $CrashTargetPath ([bool]$CrashTestPolicy);$event=[Threading.EventWaitHandle]::new($false,[Threading.EventResetMode]::ManualReset,"Local\CVF_G4_RUNNER_${CrashRunId}_CRASH_ACQUIRED");$mutex=Enter-Guard $target $false;try{$event.Set()|Out-Null;Start-Sleep -Seconds 300}finally{Exit-Guard $mutex;$event.Dispose()};exit 0}
if($PSCmdlet.ParameterSetName-ceq'Execute'){Invoke-Probe $EnvelopePath ([bool]$TestPolicy)|ConvertTo-Json -Depth 12 -Compress;exit 0}
Invoke-SelfTest
exit 0
