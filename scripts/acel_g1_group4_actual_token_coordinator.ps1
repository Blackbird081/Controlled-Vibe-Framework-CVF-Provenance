<#
.SYNOPSIS
Local setup and command-packet coordinator for the Group 4 disposable proof.

.DESCRIPTION
Creates one strictly contained disposable root, the protected two-reservation
parent, Local-only control/evidence folders, and 22 hash-bound envelopes (the
eleven C0-R1 probe classes for both principals). It does not launch Party B or
Party C, handle credentials, touch the real Group 4 source, or issue a final
verdict. TestPolicy uses the current token and remains non-admissible as actual
token evidence.
#>
[CmdletBinding(DefaultParameterSetName='SelfTest')]
param(
    [Parameter(ParameterSetName='SelfTest')][switch]$SelfTest,
    [Parameter(ParameterSetName='Prepare',Mandatory=$true)][switch]$PrepareProof,
    [Parameter(ParameterSetName='Prepare',Mandatory=$true)][string]$DisposableRoot,
    [Parameter(ParameterSetName='Prepare',Mandatory=$true)][string]$RegistryPayloadSource,
    [Parameter(ParameterSetName='Prepare')][switch]$TestPolicy
)

Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$script:ScriptPath=$PSCommandPath
$script:RepoRoot=Split-Path -Parent (Split-Path -Parent $script:ScriptPath)
$script:ProbeScript=Join-Path $script:RepoRoot 'scripts/acel_g1_group4_actual_token_principal_probe.ps1'
$script:FinalizerScript=Join-Path $script:RepoRoot 'scripts/acel_g1_group4_actual_token_local_finalizer.ps1'
$script:RealSource=Join-Path $script:RepoRoot 'governance/sources/issuer_registry'
$script:LocalName='LAM-RUBY\DELL';$script:LocalSid='S-1-5-21-1644666849-912006174-747199667-1001'
$script:PartyBName='LAM-RUBY\cvf-g1-party-b';$script:PartyBSid='S-1-5-21-1644666849-912006174-747199667-1009'
$script:PartyCName='LAM-RUBY\cvf-g1-party-c';$script:PartyCSid='S-1-5-21-1644666849-912006174-747199667-1010'
$script:SystemSid='S-1-5-18';$script:AdministratorsSid='S-1-5-32-544'
$script:Actions=@('OWN_TARGET_PUBLICATION','CROSS_TARGET_MUTATION','OWNER_DACL_MUTATION','PARENT_MUTATION','ALLOWED_TEMP','REPARSE_JUNCTION','HARDLINK','SIBLING_DRIFT','SECURITY_DRIFT','CONCURRENCY','CRASH_ROLLBACK')
$script:Tests=[Collections.Generic.List[object]]::new()

function Stop-Coordinator([string]$Code,[string]$Message){throw [InvalidOperationException]::new("${Code}: ${Message}")}
function Get-CanonicalPath([string]$Path){[IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar)}
function Get-Sha256Hex([byte[]]$Bytes){$sha=[Security.Cryptography.SHA256]::Create();try{([Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant()}finally{$sha.Dispose()}}
function Get-FileSha256([string]$Path){Get-Sha256Hex ([IO.File]::ReadAllBytes($Path))}
function Write-Utf8Json([string]$Path,$Value){[IO.File]::WriteAllText($Path,($Value|ConvertTo-Json -Depth 16),[Text.UTF8Encoding]::new($false))}

function Assert-NoReparseTraversal([string]$BasePath,[string]$CandidatePath){
    $base=Get-CanonicalPath $BasePath;$candidate=Get-CanonicalPath $CandidatePath;$prefix=$base+[IO.Path]::DirectorySeparatorChar
    if($candidate-cne$base-and-not$candidate.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Coordinator 'COORDINATOR_CONTAINMENT_VIOLATION' $candidate}
    $current=$base;if(Test-Path -LiteralPath $current){if((Get-Item -LiteralPath $current -Force).Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Coordinator 'COORDINATOR_REPARSE_REJECTED' $current}}
    if($candidate-cne$base){foreach($part in $candidate.Substring($prefix.Length)-split'[\\/]'){$current=Join-Path $current $part;if(Test-Path -LiteralPath $current){if((Get-Item -LiteralPath $current -Force).Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Coordinator 'COORDINATOR_REPARSE_REJECTED' $current}}}}
}
function Assert-DisposableRoot([string]$Path,[bool]$IsTest,[bool]$MustBeAbsent){
    $temp=Get-CanonicalPath ([IO.Path]::GetTempPath());$full=Get-CanonicalPath $Path;$prefix=$temp+[IO.Path]::DirectorySeparatorChar
    if(-not$full.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Coordinator 'COORDINATOR_CONTAINMENT_VIOLATION' $full}
    $relative=$full.Substring($prefix.Length);if($relative.Contains([IO.Path]::DirectorySeparatorChar)){Stop-Coordinator 'COORDINATOR_ROOT_NOT_DIRECT_CHILD' $full}
    $pattern=if($IsTest){'cvf-g4-actual-token-test-*'}else{'cvf-g4-actual-token-*'}
    if($relative-notlike$pattern-or(-not$IsTest-and$relative-like'cvf-g4-actual-token-test-*')){Stop-Coordinator 'COORDINATOR_ROOT_NAME_INVALID' $relative}
    $repo=Get-CanonicalPath $script:RepoRoot;$real=Get-CanonicalPath $script:RealSource;$userProfilePath=Get-CanonicalPath ([Environment]::GetFolderPath('UserProfile'))
    foreach($forbidden in @($repo,$real)){if($full-ieq$forbidden-or$full.StartsWith($forbidden+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)-or$forbidden.StartsWith($full+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Coordinator 'PROBE_REAL_SOURCE_REACHED' $full}}
    if($full-ieq$userProfilePath-or$userProfilePath.StartsWith($full+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Coordinator 'COORDINATOR_CONTAINMENT_VIOLATION' $full}
    Assert-NoReparseTraversal $temp $full;if($MustBeAbsent-and(Test-Path -LiteralPath $full)){Stop-Coordinator 'COORDINATOR_AMBIGUOUS_PRESTATE' $full};return $full
}
function Assert-PayloadSource([string]$Path,[string]$Root){
    $full=Get-CanonicalPath $Path;if(-not(Test-Path -LiteralPath $full -PathType Leaf)){Stop-Coordinator 'COORDINATOR_PAYLOAD_MISSING' $full};$item=Get-Item -LiteralPath $full -Force
    if($item.Attributes-band[IO.FileAttributes]::ReparsePoint-or$item.Length-le0-or$item.Length-gt1048576){Stop-Coordinator 'COORDINATOR_PAYLOAD_INVALID' $full}
    $real=Get-CanonicalPath $script:RealSource;if($full-ieq$real-or$full.StartsWith($real+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Coordinator 'PROBE_REAL_SOURCE_REACHED' $full};if($full.StartsWith($Root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Coordinator 'COORDINATOR_PAYLOAD_INSIDE_NEW_ROOT' $full};return $full
}
function Assert-LocalSetupToken([bool]$IsTest){
    $identity=[Security.Principal.WindowsIdentity]::GetCurrent();if($IsTest){return [ordered]@{name=$identity.Name;sid=$identity.User.Value;testPolicy=$true}}
    $principal=[Security.Principal.WindowsPrincipal]::new($identity);if(-not$principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)){Stop-Coordinator 'COORDINATOR_ADMIN_REQUIRED' $identity.Name}
    if($identity.Name-cne$script:LocalName-or$identity.User.Value-cne$script:LocalSid){Stop-Coordinator 'COORDINATOR_LOCAL_IDENTITY_MISMATCH' "$($identity.Name)/$($identity.User.Value)"};return [ordered]@{name=$identity.Name;sid=$identity.User.Value;testPolicy=$false}
}
function Add-Ace($Security,[string]$Sid,[Security.AccessControl.FileSystemRights]$Rights){$Security.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new($Sid),$Rights,[Security.AccessControl.InheritanceFlags]::None,[Security.AccessControl.PropagationFlags]::None,[Security.AccessControl.AccessControlType]::Allow))}
function Set-ParentSecurity([string]$Path,[bool]$IsTest){
    $acl=[Security.AccessControl.DirectorySecurity]::new();$acl.SetAccessRuleProtection($true,$false)
    if($IsTest){$sid=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value;$acl.SetOwner([Security.Principal.SecurityIdentifier]::new($sid));Add-Ace $acl $sid ([Security.AccessControl.FileSystemRights]::FullControl)}else{$acl.SetOwner([Security.Principal.SecurityIdentifier]::new($script:AdministratorsSid));Add-Ace $acl $script:SystemSid ([Security.AccessControl.FileSystemRights]::FullControl);Add-Ace $acl $script:AdministratorsSid ([Security.AccessControl.FileSystemRights]::FullControl);$partyRights=[Security.AccessControl.FileSystemRights]::ReadAndExecute-bor[Security.AccessControl.FileSystemRights]::CreateFiles-bor[Security.AccessControl.FileSystemRights]::Synchronize;Add-Ace $acl $script:PartyCSid $partyRights;Add-Ace $acl $script:PartyBSid $partyRights;$localRights=[Security.AccessControl.FileSystemRights]::ReadAndExecute-bor[Security.AccessControl.FileSystemRights]::Synchronize;Add-Ace $acl $script:LocalSid $localRights}
    [IO.FileSystemAclExtensions]::SetAccessControl([IO.DirectoryInfo]::new($Path),$acl)
}
function Set-ReservationSecurity([string]$Path,[string]$OwnerSid,[bool]$IsTest){
    $acl=[Security.AccessControl.FileSecurity]::new();$acl.SetAccessRuleProtection($true,$false);$owner=if($IsTest){[Security.Principal.WindowsIdentity]::GetCurrent().User.Value}else{$OwnerSid};$ownerIdentity=[Security.Principal.SecurityIdentifier]::new($owner);$acl.SetOwner($ownerIdentity);$acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new($ownerIdentity,[Security.AccessControl.FileSystemRights]::FullControl,[Security.AccessControl.AccessControlType]::Allow))
    if(-not$IsTest){foreach($entry in @(@($script:SystemSid,[Security.AccessControl.FileSystemRights]::FullControl),@($script:AdministratorsSid,[Security.AccessControl.FileSystemRights]::FullControl),@($script:LocalSid,[Security.AccessControl.FileSystemRights]::Read))){$acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new([string]$entry[0]),[Security.AccessControl.FileSystemRights]$entry[1],[Security.AccessControl.AccessControlType]::Allow))}}
    [IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($Path),$acl)
}
function Set-ActualDirectorySecurity([string]$Path,[bool]$AllowCreateFiles){
    $acl=[Security.AccessControl.DirectorySecurity]::new();$acl.SetAccessRuleProtection($true,$false);$acl.SetOwner([Security.Principal.SecurityIdentifier]::new($script:AdministratorsSid));Add-Ace $acl $script:SystemSid ([Security.AccessControl.FileSystemRights]::FullControl);Add-Ace $acl $script:AdministratorsSid ([Security.AccessControl.FileSystemRights]::FullControl);Add-Ace $acl $script:LocalSid ([Security.AccessControl.FileSystemRights]::FullControl);$rights=[Security.AccessControl.FileSystemRights]::ReadAndExecute-bor[Security.AccessControl.FileSystemRights]::Synchronize;if($AllowCreateFiles){$rights=$rights-bor[Security.AccessControl.FileSystemRights]::CreateFiles};Add-Ace $acl $script:PartyBSid $rights;Add-Ace $acl $script:PartyCSid $rights;[IO.FileSystemAclExtensions]::SetAccessControl([IO.DirectoryInfo]::new($Path),$acl)
}
function Set-ActualControlFileSecurity([string]$Path,[string]$PrincipalSid,[bool]$Writable){
    $acl=[Security.AccessControl.FileSecurity]::new();$acl.SetAccessRuleProtection($true,$false);$acl.SetOwner([Security.Principal.SecurityIdentifier]::new($script:AdministratorsSid));Add-Ace $acl $script:SystemSid ([Security.AccessControl.FileSystemRights]::FullControl);Add-Ace $acl $script:AdministratorsSid ([Security.AccessControl.FileSystemRights]::FullControl);Add-Ace $acl $script:LocalSid ([Security.AccessControl.FileSystemRights]::FullControl);Add-Ace $acl $PrincipalSid $(if($Writable){[Security.AccessControl.FileSystemRights]::FullControl}else{[Security.AccessControl.FileSystemRights]::Read});[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($Path),$acl)
}
function Grant-TestCleanupAccess([string]$Root){
    $verified=Assert-DisposableRoot $Root $true $false;$sid=[Security.Principal.WindowsIdentity]::GetCurrent().User
    foreach($file in @(Get-ChildItem -LiteralPath $verified -File -Force -Recurse)){$acl=[Security.AccessControl.FileSecurity]::new();$acl.SetAccessRuleProtection($true,$false);$acl.SetOwner($sid);$acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new($sid,[Security.AccessControl.FileSystemRights]::FullControl,[Security.AccessControl.AccessControlType]::Allow));[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($file.FullName),$acl)}
    $dirs=@(Get-ChildItem -LiteralPath $verified -Directory -Force -Recurse|Sort-Object{$_.FullName.Length}-Descending)+@(Get-Item -LiteralPath $verified -Force);foreach($dir in $dirs){$acl=[Security.AccessControl.DirectorySecurity]::new();$acl.SetAccessRuleProtection($true,$false);$acl.SetOwner($sid);$acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new($sid,[Security.AccessControl.FileSystemRights]::FullControl,[Security.AccessControl.InheritanceFlags]::None,[Security.AccessControl.PropagationFlags]::None,[Security.AccessControl.AccessControlType]::Allow));[IO.FileSystemAclExtensions]::SetAccessControl([IO.DirectoryInfo]::new($dir.FullName),$acl)}
}
function Get-SecurityTuple([string]$Path,[bool]$Directory){$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$obj=if($Directory){[IO.DirectoryInfo]::new($Path)}else{[IO.FileInfo]::new($Path)};$acl=[IO.FileSystemAclExtensions]::GetAccessControl($obj,$sections);[ordered]@{ownerSid=$acl.GetOwner([Security.Principal.SecurityIdentifier]).Value;protectionState=[bool]$acl.AreAccessRulesProtected;aces=@($acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier])|ForEach-Object{'{0}|{1}|{2}|{3}|{4}|{5}'-f$_.IdentityReference.Value,[int]$_.FileSystemRights,[int]$_.AccessControlType,[bool]$_.IsInherited,[int]$_.InheritanceFlags,[int]$_.PropagationFlags}|Sort-Object -CaseSensitive)}}
function Get-FileState([string]$Path){$info=[IO.FileInfo]::new($Path);$links=& fsutil hardlink list $Path 2>&1;if($LASTEXITCODE-ne0){Stop-Coordinator 'COORDINATOR_LINK_COUNT_UNAVAILABLE' $Path};[ordered]@{path=Get-CanonicalPath $Path;length=[int64]$info.Length;sha256=Get-FileSha256 $Path;linkCount=@($links|Where-Object{$_.Trim().Length-gt0}).Count;attributes=[int]$info.Attributes;reparse=[bool]($info.Attributes-band[IO.FileAttributes]::ReparsePoint);security=Get-SecurityTuple $Path $false}}
function Get-FixtureState([string]$Parent,[string]$Own,[string]$Other){$parentItem=Get-Item -LiteralPath $Parent -Force;$isReparse=[bool]($parentItem.Attributes-band[IO.FileAttributes]::ReparsePoint);[ordered]@{parent=[ordered]@{path=Get-CanonicalPath $Parent;reparse=$isReparse;security=Get-SecurityTuple $Parent $true;inventory=if($isReparse){@()}else{@(Get-ChildItem -LiteralPath $Parent -Force|ForEach-Object{$_.Name}|Sort-Object -CaseSensitive)}};own=Get-FileState $Own;other=Get-FileState $Other}}
function Add-SecurityDrift([string]$Path){$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$acl=[IO.FileSystemAclExtensions]::GetAccessControl([IO.FileInfo]::new($Path),$sections);$acl.AddAccessRule([Security.AccessControl.FileSystemAccessRule]::new([Security.Principal.SecurityIdentifier]::new('S-1-1-0'),[Security.AccessControl.FileSystemRights]::Read,[Security.AccessControl.AccessControlType]::Allow));[IO.FileSystemAclExtensions]::SetAccessControl([IO.FileInfo]::new($Path),$acl)}

function Get-EnvelopeBinding($Envelope){$fields=@('schema','runId','role','action','expectedAccountName','expectedSid','disposableRoot','protectedParent','ownTarget','otherTarget','evidencePath','payloadPath','expectedOutcome','testPolicy','issuedAtUtc');$values=[Collections.Generic.List[string]]::new();foreach($field in $fields){$value=$Envelope.$field;if($value-is[bool]){$values.Add($value.ToString().ToLowerInvariant())}elseif($value-is[datetime]){$values.Add($value.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffZ'))}else{$values.Add([string]$value)}};Get-Sha256Hex ([Text.Encoding]::UTF8.GetBytes(($values.ToArray()-join"`n")))}
function Get-ExpectedOutcome([string]$Action){switch($Action){'OWN_TARGET_PUBLICATION'{'ALLOWED'}'ALLOWED_TEMP'{'ALLOWED'}'CONCURRENCY'{'ALLOWED'}'CROSS_TARGET_MUTATION'{'DENIED'}'OWNER_DACL_MUTATION'{'DENIED'}'PARENT_MUTATION'{'DENIED'}default{'REJECTED'}}}
function New-Envelope([string]$RunId,[string]$Role,[string]$Action,[string]$Root,[string]$Parent,[string]$Payload,[bool]$IsTest){
    $isB=$Role-ceq'PARTY_B';$own=Join-Path $Parent $(if($isB){'LOOKUP_RESPONSES.jsonl'}else{'REGISTRY.json'});$other=Join-Path $Parent $(if($isB){'REGISTRY.json'}else{'LOOKUP_RESPONSES.jsonl'});$name=if($IsTest){[Security.Principal.WindowsIdentity]::GetCurrent().Name}elseif($isB){$script:PartyBName}else{$script:PartyCName};$sid=if($IsTest){[Security.Principal.WindowsIdentity]::GetCurrent().User.Value}elseif($isB){$script:PartyBSid}else{$script:PartyCSid}
    $record=[ordered]@{schema='cvf.g4.actualTokenProbeEnvelope.v1';runId=$RunId;role=$Role;action=$Action;expectedAccountName=$name;expectedSid=$sid;disposableRoot=$Root;protectedParent=$Parent;ownTarget=$own;otherTarget=$other;evidencePath=Join-Path $Root "evidence/$Role-$Action.json";payloadPath=if($Action-ceq'OWN_TARGET_PUBLICATION'-and-not$isB){$Payload}else{''};expectedOutcome=Get-ExpectedOutcome $Action;testPolicy=$IsTest;issuedAtUtc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ');bindingSha256Hex=''};$obj=[pscustomobject]$record;$obj.bindingSha256Hex=Get-EnvelopeBinding $obj;return $obj
}

function New-ProofPacket([string]$RequestedRoot,[string]$PayloadSource,[bool]$IsTest){
    $root=Assert-DisposableRoot $RequestedRoot $IsTest $true;$payloadInput=Assert-PayloadSource $PayloadSource $root;$setupToken=Assert-LocalSetupToken $IsTest;$runId=[Guid]::NewGuid().ToString('N')
    [IO.Directory]::CreateDirectory($root)|Out-Null
    try{$control=Join-Path $root 'control';$envelopes=Join-Path $control 'envelopes';$evidence=Join-Path $root 'evidence';$ledger=Join-Path $root 'ledger';$scenarios=Join-Path $root 'scenarios';foreach($path in @($envelopes,$evidence,$ledger,$scenarios)){[IO.Directory]::CreateDirectory($path)|Out-Null}
        $payload=Join-Path $control 'registry-payload.json';[IO.File]::Copy($payloadInput,$payload,$false)
        if(-not$IsTest){foreach($path in @($root,$control,$envelopes,$evidence,$ledger,$scenarios)){Set-ActualDirectorySecurity $path $false};Set-ActualControlFileSecurity $payload $script:PartyCSid $false}
        $rows=[Collections.Generic.List[object]]::new();foreach($role in @('PARTY_C','PARTY_B')){foreach($action in $script:Actions){
            $fixture=Join-Path $scenarios "$role-$action";[IO.Directory]::CreateDirectory($fixture)|Out-Null;$parent=Join-Path $fixture 'issuer_registry';$realParent=$parent
            if($action-ceq'REPARSE_JUNCTION'){$realParent=Join-Path $fixture 'real_parent';[IO.Directory]::CreateDirectory($realParent)|Out-Null}else{[IO.Directory]::CreateDirectory($parent)|Out-Null}
            $registry=Join-Path $realParent 'REGISTRY.json';$responses=Join-Path $realParent 'LOOKUP_RESPONSES.jsonl';[IO.File]::WriteAllBytes($registry,[byte[]]::new(0));[IO.File]::WriteAllBytes($responses,[byte[]]::new(0));if(-not$IsTest){Set-ParentSecurity $realParent $false;Set-ReservationSecurity $registry $script:PartyCSid $false;Set-ReservationSecurity $responses $script:PartyBSid $false;Set-ActualDirectorySecurity $fixture $false}
            if($action-ceq'REPARSE_JUNCTION'){New-Item -ItemType Junction -Path $parent -Target $realParent|Out-Null}
            $isB=$role-ceq'PARTY_B';$own=if($isB){$responses}else{$registry}
            if($action-ceq'HARDLINK'){$alias=Join-Path $realParent ".adversary-hardlink-$role";$out=& fsutil hardlink create $alias $own 2>&1;if($LASTEXITCODE-ne0){Stop-Coordinator 'COORDINATOR_HARDLINK_FIXTURE_FAILED' ($out-join' ')}}
            if($action-ceq'SIBLING_DRIFT'){[IO.File]::WriteAllBytes((Join-Path $realParent '.adversary-sibling.bin'),[byte[]](1,2,3))}
            if($action-ceq'SECURITY_DRIFT'){Add-SecurityDrift $own}
            $envelope=New-Envelope $runId $role $action $root $parent $payload $IsTest;$envelopePath=Join-Path $envelopes "$role-$action.json";Write-Utf8Json $envelopePath $envelope;$principalSid=if($isB){$script:PartyBSid}else{$script:PartyCSid};if(-not$IsTest){Set-ActualControlFileSecurity $envelopePath $principalSid $false;[IO.File]::WriteAllBytes([string]$envelope.evidencePath,[byte[]]::new(0));Set-ActualControlFileSecurity ([string]$envelope.evidencePath) $principalSid $true}
            $arguments=@('-NoProfile','-NonInteractive','-File',$script:ProbeScript,'-ExecuteProbe','-EnvelopePath',$envelopePath);if($IsTest){$arguments+='-TestPolicy'};$rows.Add([pscustomobject]@{role=$role;action=$action;expectedOutcome=$envelope.expectedOutcome;envelopePath=$envelopePath;envelopeSha256Hex=Get-FileSha256 $envelopePath;evidencePath=$envelope.evidencePath;fixturePrestate=Get-FixtureState $parent ([string]$envelope.ownTarget) ([string]$envelope.otherTarget);commandExecutable=(Get-Command pwsh).Source;commandArguments=$arguments})}}
        $manifest=[ordered]@{schema='cvf.g4.actualTokenProofManifest.v1';runId=$runId;testPolicy=$IsTest;disposableRoot=$root;setupToken=$setupToken;principalConstants=[ordered]@{localName=$script:LocalName;localSid=$script:LocalSid;partyBName=$script:PartyBName;partyBSid=$script:PartyBSid;partyCName=$script:PartyCName;partyCSid=$script:PartyCSid};probeScriptPath=$script:ProbeScript;probeScriptSha256Hex=Get-FileSha256 $script:ProbeScript;finalizerScriptPath=$script:FinalizerScript;payloadPath=$payload;payloadSha256Hex=Get-FileSha256 $payload;matrix=@($rows);credentialFields=@();actualTokenProofClaimed=$false;createdAtUtc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')}
        $manifestPath=Join-Path $control 'MANIFEST.json';Write-Utf8Json $manifestPath $manifest;$commandPacket=[ordered]@{schema='cvf.g4.actualTokenCommandPacket.v1';runId=$runId;manifestPath=$manifestPath;instructions=@('Open a non-elevated shell already running as the envelope principal.','Run only the matching role commands; each command owns an isolated Local-prepared scenario.','Stop after the first nonzero exit or unexpected outcome.','Do not disclose or persist any password.','Return to Local for finalization; a principal cannot self-certify PASS.');commands=@($rows);finalizerCommand=[ordered]@{executable=(Get-Command pwsh).Source;arguments=@('-NoProfile','-NonInteractive','-File',$script:FinalizerScript,'-Finalize','-ManifestPath',$manifestPath,'-OutputPath',(Join-Path $control 'FINAL_VERDICT.json'))};passwordRequiredFromAgent=$false;principalProcessLaunched=$false}
        $commandPath=Join-Path $control 'COMMAND_PACKET.json';Write-Utf8Json $commandPath $commandPacket
        return [pscustomobject]@{disposition='DISPOSABLE_PACKET_PREPARED_NO_PRINCIPAL_EXECUTION';runId=$runId;root=$root;manifestPath=$manifestPath;commandPacketPath=$commandPath;matrixRows=$rows.Count;testPolicy=$IsTest;principalProcessLaunched=$false;realSourceReached=$false}
    }catch{if(Test-Path -LiteralPath $root){Remove-Item -LiteralPath $root -Recurse -Force};throw}
}

function Add-Test([string]$Id,[bool]$Passed,[string]$Detail){$script:Tests.Add([pscustomobject]@{id=$Id;passed=$Passed;detail=$Detail});if(-not$Passed){Stop-Coordinator 'COORDINATOR_SELFTEST_FAILED' "${Id}: $Detail"}}
function Invoke-SelfTest {
    $inputRoot=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-actual-token-input-'+[Guid]::NewGuid().ToString('N'));$root=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-actual-token-test-'+[Guid]::NewGuid().ToString('N'));[IO.Directory]::CreateDirectory($inputRoot)|Out-Null;$payload=Join-Path $inputRoot 'payload.json';[IO.File]::WriteAllText($payload,'{"fresh":"hermetic-current-token-only"}')
    try{$packet=New-ProofPacket $root $payload $true;$manifest=Get-Content -LiteralPath $packet.manifestPath -Raw|ConvertFrom-Json;Add-Test 'G4-COORDINATOR-MATRIX-22' ($packet.matrixRows-eq22-and@($manifest.matrix).Count-eq22) 'eleven classes planned for each of two roles';Add-Test 'G4-COORDINATOR-UNIQUE' (@($manifest.matrix|ForEach-Object{"$($_.role)|$($_.action)"}|Sort-Object -Unique).Count-eq22) 'role/action pairs unique';Add-Test 'G4-COORDINATOR-TESTPOLICY' ($manifest.testPolicy-and-not$manifest.actualTokenProofClaimed) 'hermetic packet cannot claim actual proof';Add-Test 'G4-COORDINATOR-NO-CREDENTIALS' (@($manifest.credentialFields).Count-eq0-and-not((Get-Content $packet.commandPacketPath -Raw)-match'(?i)password\s*[:=]')) 'no credential field or value';Add-Test 'G4-COORDINATOR-PRESTATE' (@($manifest.matrix|Where-Object{-not$_.fixturePrestate.own-or-not$_.fixturePrestate.other}).Count-eq0) 'all 22 isolated fixture prestates captured';$allHashes=$true;foreach($row in $manifest.matrix){if((Get-FileSha256 ([string]$row.envelopePath))-cne[string]$row.envelopeSha256Hex){$allHashes=$false}};Add-Test 'G4-COORDINATOR-ENVELOPE-HASHES' $allHashes 'all envelope file hashes exact'
        $out=& pwsh -NoProfile -NonInteractive -File $script:ProbeScript -SelfTest 2>&1;$probeOk=$LASTEXITCODE-eq0-and(($out-join"`n")-match'"result":"PASS"');Add-Test 'G4-COORDINATOR-REAL-CHILD-PROBE' $probeOk 'real child process exercises barrier and failure cleanup'
        try{Assert-DisposableRoot $script:RepoRoot $true $false|Out-Null;$blocked=$false}catch{$blocked=$true};Add-Test 'G4-COORDINATOR-REPO-REJECTED' $blocked 'repository root rejected'
        try{Assert-DisposableRoot $root $true $true|Out-Null;$blocked=$false}catch{$blocked=$_.Exception.Message-like'COORDINATOR_AMBIGUOUS_PRESTATE:*'};Add-Test 'G4-COORDINATOR-PREEXISTING-REJECTED' $blocked 'pre-existing root rejected'
        [pscustomobject]@{result='PASS';tests=$script:Tests.Count;matrixRows=22;testPolicyOnly=$true;principalProcessLaunched=$false;realSourceReached=$false}|ConvertTo-Json -Compress
    }finally{if(Test-Path -LiteralPath $root){Remove-Item -LiteralPath $root -Recurse -Force};if(Test-Path -LiteralPath $inputRoot){Remove-Item -LiteralPath $inputRoot -Recurse -Force}}
}

if($PSCmdlet.ParameterSetName-ceq'Prepare'){New-ProofPacket $DisposableRoot $RegistryPayloadSource ([bool]$TestPolicy)|ConvertTo-Json -Depth 8 -Compress;exit 0}
Invoke-SelfTest
exit 0
