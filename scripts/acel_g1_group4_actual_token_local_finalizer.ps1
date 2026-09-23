<#
.SYNOPSIS
Local-only adjudicator for the Group 4 disposable actual-token proof ledger.

.DESCRIPTION
Reads the coordinator manifest plus all 22 principal evidence records, verifies
their hashes/bindings, exact identities, outcomes, Local poststate and residue
inventory, then emits exactly PASS_ACTUAL_TOKEN_PROOF or
INCONCLUSIVE_OR_FAILED. Any TestPolicy evidence is categorically inadmissible
for PASS. The finalizer performs no writer action and accepts no credential.
#>
[CmdletBinding(DefaultParameterSetName='SelfTest')]
param(
    [Parameter(ParameterSetName='SelfTest')][switch]$SelfTest,
    [Parameter(ParameterSetName='Finalize',Mandatory=$true)][switch]$Finalize,
    [Parameter(ParameterSetName='Finalize',Mandatory=$true)][string]$ManifestPath,
    [Parameter(ParameterSetName='Finalize',Mandatory=$true)][string]$OutputPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$script:ScriptPath=$PSCommandPath
$script:RepoRoot=Split-Path -Parent (Split-Path -Parent $script:ScriptPath)
$script:RealSource=Join-Path $script:RepoRoot 'governance/sources/issuer_registry'
$script:LocalName='LAM-RUBY\DELL';$script:LocalSid='S-1-5-21-1644666849-912006174-747199667-1001'
$script:PartyBName='LAM-RUBY\cvf-g1-party-b';$script:PartyBSid='S-1-5-21-1644666849-912006174-747199667-1009'
$script:PartyCName='LAM-RUBY\cvf-g1-party-c';$script:PartyCSid='S-1-5-21-1644666849-912006174-747199667-1010'
$script:Actions=@('OWN_TARGET_PUBLICATION','CROSS_TARGET_MUTATION','OWNER_DACL_MUTATION','PARENT_MUTATION','ALLOWED_TEMP','REPARSE_JUNCTION','HARDLINK','SIBLING_DRIFT','SECURITY_DRIFT','CONCURRENCY','CRASH_ROLLBACK')
$script:Tests=[Collections.Generic.List[object]]::new()

function Stop-Finalizer([string]$Code,[string]$Message){throw [InvalidOperationException]::new("${Code}: ${Message}")}
function Get-CanonicalPath([string]$Path){[IO.Path]::GetFullPath($Path).TrimEnd([IO.Path]::DirectorySeparatorChar)}
function Get-Sha256Hex([byte[]]$Bytes){$sha=[Security.Cryptography.SHA256]::Create();try{([Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant()}finally{$sha.Dispose()}}
function Get-FileSha256([string]$Path){Get-Sha256Hex ([IO.File]::ReadAllBytes($Path))}
function Write-Utf8Json([string]$Path,$Value){[IO.Directory]::CreateDirectory((Split-Path -Parent $Path))|Out-Null;[IO.File]::WriteAllText($Path,($Value|ConvertTo-Json -Depth 18),[Text.UTF8Encoding]::new($false))}
function Add-Reason([Collections.Generic.List[string]]$Reasons,[string]$Reason){if(-not$Reasons.Contains($Reason)){$Reasons.Add($Reason)}}

function Assert-NoReparseTraversal([string]$BasePath,[string]$CandidatePath){$base=Get-CanonicalPath $BasePath;$candidate=Get-CanonicalPath $CandidatePath;$prefix=$base+[IO.Path]::DirectorySeparatorChar;if($candidate-cne$base-and-not$candidate.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Finalizer 'FINALIZER_CONTAINMENT_VIOLATION' $candidate};$current=$base;if(Test-Path -LiteralPath $current){if((Get-Item -LiteralPath $current -Force).Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Finalizer 'FINALIZER_REPARSE_REJECTED' $current}};if($candidate-cne$base){foreach($part in $candidate.Substring($prefix.Length)-split'[\\/]'){$current=Join-Path $current $part;if(Test-Path -LiteralPath $current){if((Get-Item -LiteralPath $current -Force).Attributes-band[IO.FileAttributes]::ReparsePoint){Stop-Finalizer 'FINALIZER_REPARSE_REJECTED' $current}}}}}
function Assert-DisposablePath([string]$Path,[bool]$IsTest){$temp=Get-CanonicalPath ([IO.Path]::GetTempPath());$full=Get-CanonicalPath $Path;$prefix=$temp+[IO.Path]::DirectorySeparatorChar;if(-not$full.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){Stop-Finalizer 'FINALIZER_CONTAINMENT_VIOLATION' $full};$leaf=(($full.Substring($prefix.Length))-split'[\\/]')[0];$pattern=if($IsTest){'cvf-g4-actual-token-test-*'}else{'cvf-g4-actual-token-*'};if($leaf-notlike$pattern-or(-not$IsTest-and$leaf-like'cvf-g4-actual-token-test-*')){Stop-Finalizer 'FINALIZER_CONTAINMENT_VIOLATION' $full};$root=Join-Path $temp $leaf;$real=Get-CanonicalPath $script:RealSource;if($full-ieq$real-or$full.StartsWith($real+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Stop-Finalizer 'PROBE_REAL_SOURCE_REACHED' $full};Assert-NoReparseTraversal $temp $root;Assert-NoReparseTraversal $root $full;return $full}
function Get-AceTuples($Acl){@($Acl.GetAccessRules($true,$true,[Security.Principal.SecurityIdentifier])|ForEach-Object{'{0}|{1}|{2}|{3}|{4}|{5}'-f$_.IdentityReference.Value,[int]$_.FileSystemRights,[int]$_.AccessControlType,[bool]$_.IsInherited,[int]$_.InheritanceFlags,[int]$_.PropagationFlags}|Sort-Object -CaseSensitive)}
function Get-SecurityTuple([string]$Path,[bool]$Directory){$sections=[Security.AccessControl.AccessControlSections]::Owner-bor[Security.AccessControl.AccessControlSections]::Access;$obj=if($Directory){[IO.DirectoryInfo]::new($Path)}else{[IO.FileInfo]::new($Path)};$acl=[IO.FileSystemAclExtensions]::GetAccessControl($obj,$sections);[ordered]@{ownerSid=$acl.GetOwner([Security.Principal.SecurityIdentifier]).Value;protectionState=[bool]$acl.AreAccessRulesProtected;aces=@(Get-AceTuples $acl)}}
function Get-LinkCount([string]$Path){$out=& fsutil hardlink list $Path 2>&1;if($LASTEXITCODE-ne0){return -1};@($out|Where-Object{$_.Trim().Length-gt0}).Count}
function Get-FileState([string]$Path){$info=[IO.FileInfo]::new($Path);[ordered]@{path=Get-CanonicalPath $Path;length=[int64]$info.Length;sha256=Get-FileSha256 $Path;linkCount=Get-LinkCount $Path;attributes=[int]$info.Attributes;reparse=[bool]($info.Attributes-band[IO.FileAttributes]::ReparsePoint);security=Get-SecurityTuple $Path $false}}
function Get-SecurityFingerprint($Security){if($null-eq$Security){return''};'{0}|{1}|{2}'-f[string]$Security.ownerSid,[bool]$Security.protectionState,(@($Security.aces)-join"`n")}
function Test-FileStateBinding($Expected,$Actual){if($null-eq$Expected-or$null-eq$Actual){return $false};return [string]$Expected.path-ceq[string]$Actual.path-and[int64]$Expected.length-eq[int64]$Actual.length-and[string]$Expected.sha256-ceq[string]$Actual.sha256-and[int]$Expected.linkCount-eq[int]$Actual.linkCount-and[bool]$Expected.reparse-eq[bool]$Actual.reparse-and(Get-SecurityFingerprint $Expected.security)-ceq(Get-SecurityFingerprint $Actual.security)}
function Get-Inventory($Parent){if($Parent-is[Collections.IDictionary]){if($Parent.Contains('inventory')){return @($Parent['inventory'])};if($Parent.Contains('children')){return @($Parent['children'])}};if($Parent.PSObject.Properties.Name-ccontains'inventory'){return @($Parent.inventory)};if($Parent.PSObject.Properties.Name-ccontains'children'){return @($Parent.children)};return @()}
function Test-FixtureBinding($Expected,$Actual){if($null-eq$Expected-or$null-eq$Actual){return $false};$parentOk=[string]$Expected.parent.path-ceq[string]$Actual.parent.path-and[bool]$Expected.parent.reparse-eq[bool]$Actual.parent.reparse-and(Get-SecurityFingerprint $Expected.parent.security)-ceq(Get-SecurityFingerprint $Actual.parent.security)-and(((Get-Inventory $Expected.parent)-join',')-ceq((Get-Inventory $Actual.parent)-join','));return $parentOk-and(Test-FileStateBinding $Expected.own $Actual.own)-and(Test-FileStateBinding $Expected.other $Actual.other)}
function Test-ProbeStateEqual($Left,$Right){(($Left|ConvertTo-Json -Depth 16 -Compress)-ceq($Right|ConvertTo-Json -Depth 16 -Compress))}
function Test-EvidencePostcondition($Evidence,$Manifest){if($Evidence.action-cne'OWN_TARGET_PUBLICATION'){return Test-ProbeStateEqual $Evidence.prestate $Evidence.poststate};$expectedHash=if($Evidence.role-ceq'PARTY_C'){[string]$Manifest.payloadSha256Hex}else{Get-Sha256Hex ([byte[]]::new(0))};return [string]$Evidence.poststate.own.sha256-ceq$expectedHash-and(Test-ProbeStateEqual $Evidence.prestate.other $Evidence.poststate.other)-and((Get-SecurityFingerprint $Evidence.prestate.parent.security)-ceq(Get-SecurityFingerprint $Evidence.poststate.parent.security))-and((@($Evidence.prestate.parent.children)-join',')-ceq(@($Evidence.poststate.parent.children)-join','))}
function Get-LiveFixtureState($Evidence){$parent=[string]$Evidence.poststate.parent.path;$isReparse=[bool]((Get-Item -LiteralPath $parent -Force).Attributes-band[IO.FileAttributes]::ReparsePoint);[ordered]@{parent=[ordered]@{path=$parent;reparse=$isReparse;security=Get-SecurityTuple $parent $true;inventory=if($isReparse){@()}else{@(Get-ChildItem -LiteralPath $parent -Force|ForEach-Object{$_.Name}|Sort-Object -CaseSensitive)}};own=Get-FileState ([string]$Evidence.poststate.own.path);other=Get-FileState ([string]$Evidence.poststate.other.path)}}

function Test-Manifest([string]$Path,[bool]$AllowSyntheticTestPolicy){
    $reasons=[Collections.Generic.List[string]]::new();$hashes=[Collections.Generic.List[object]]::new();$manifest=$null
    try{$manifest=Get-Content -LiteralPath $Path -Raw|ConvertFrom-Json}catch{Add-Reason $reasons 'MANIFEST_UNREADABLE';return [pscustomobject]@{manifest=$null;reasons=$reasons;evidenceHashes=$hashes}}
    if($manifest.schema-cne'cvf.g4.actualTokenProofManifest.v1'){Add-Reason $reasons 'MANIFEST_SCHEMA_INVALID'}
    $isTest=[bool]$manifest.testPolicy;if($isTest-and-not$AllowSyntheticTestPolicy){Add-Reason $reasons 'TEST_POLICY_EVIDENCE_INADMISSIBLE'}
    try{$root=Assert-DisposablePath ([string]$manifest.disposableRoot) $isTest;$manifestCanonical=Get-CanonicalPath $Path;if(-not$manifestCanonical.StartsWith($root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){Add-Reason $reasons 'MANIFEST_OUTSIDE_ROOT'}}catch{Add-Reason $reasons 'CONTAINMENT_OR_REPARSE_FAILURE';return [pscustomobject]@{manifest=$manifest;reasons=$reasons;evidenceHashes=$hashes}}
    if(@($manifest.matrix).Count-ne22){Add-Reason $reasons 'MATRIX_ROW_COUNT_INVALID'}
    $pairs=@($manifest.matrix|ForEach-Object{"$($_.role)|$($_.action)"});if(@($pairs|Sort-Object -Unique).Count-ne22){Add-Reason $reasons 'MATRIX_DUPLICATE_OR_MISSING'}
    foreach($role in @('PARTY_C','PARTY_B')){foreach($action in $script:Actions){if($pairs-cnotcontains"$role|$action"){Add-Reason $reasons "MATRIX_MISSING_${role}_${action}"}}}
    if(@($manifest.credentialFields).Count-ne0){Add-Reason $reasons 'CREDENTIAL_FIELD_PRESENT'}
    if(-not(Test-Path -LiteralPath ([string]$manifest.probeScriptPath)-PathType Leaf)-or(Get-FileSha256 ([string]$manifest.probeScriptPath))-cne[string]$manifest.probeScriptSha256Hex){Add-Reason $reasons 'PROBE_SCRIPT_HASH_MISMATCH'}
    foreach($row in @($manifest.matrix)){
        $pair="$($row.role)|$($row.action)";$envelopePath=[string]$row.envelopePath;$evidencePath=[string]$row.evidencePath
        try{$null=Assert-DisposablePath $envelopePath $isTest;$null=Assert-DisposablePath $evidencePath $isTest}catch{Add-Reason $reasons "PATH_INVALID_${pair}";continue}
        if(-not(Test-Path -LiteralPath $envelopePath -PathType Leaf)-or(Get-FileSha256 $envelopePath)-cne[string]$row.envelopeSha256Hex){Add-Reason $reasons "ENVELOPE_HASH_MISMATCH_${pair}";continue}
        if(-not(Test-Path -LiteralPath $evidencePath -PathType Leaf)){Add-Reason $reasons "EVIDENCE_MISSING_${pair}";continue}
        $evidenceHash=Get-FileSha256 $evidencePath;$hashes.Add([pscustomobject]@{role=[string]$row.role;action=[string]$row.action;path=$evidencePath;sha256Hex=$evidenceHash})
        try{$evidence=Get-Content -LiteralPath $evidencePath -Raw|ConvertFrom-Json}catch{Add-Reason $reasons "EVIDENCE_MALFORMED_${pair}";continue}
        if($evidence.schema-cne'cvf.g4.actualTokenProbeEvidence.v1'-or$evidence.role-cne$row.role-or$evidence.action-cne$row.action-or$evidence.runId-cne$manifest.runId){Add-Reason $reasons "EVIDENCE_BINDING_INVALID_${pair}"}
        if([bool]$evidence.testPolicy-ne$isTest-or[string]$evidence.envelopeBindingSha256Hex-cne[string](Get-Content -LiteralPath $envelopePath -Raw|ConvertFrom-Json).bindingSha256Hex){Add-Reason $reasons "EVIDENCE_ENVELOPE_BINDING_INVALID_${pair}"}
        if($evidence.disposition-cne'PASS'-or-not([bool]$evidence.postconditionsVerified)-or$evidence.expectedOutcome-cne$row.expectedOutcome-or$evidence.observedOutcome-cne$row.expectedOutcome){Add-Reason $reasons "EVIDENCE_OUTCOME_INVALID_${pair}"}
        if(-not(Test-FixtureBinding $row.fixturePrestate $evidence.prestate)){Add-Reason $reasons "EVIDENCE_PRESTATE_INVALID_${pair}"}
        if(-not(Test-EvidencePostcondition $evidence $manifest)){Add-Reason $reasons "EVIDENCE_POSTCONDITION_INVALID_${pair}"}
        try{$live=Get-LiveFixtureState $evidence;if(-not(Test-FixtureBinding ([ordered]@{parent=[ordered]@{path=[string]$evidence.poststate.parent.path;reparse=[bool]$evidence.poststate.parent.reparse;security=$evidence.poststate.parent.security;inventory=@($evidence.poststate.parent.children)};own=$evidence.poststate.own;other=$evidence.poststate.other}) $live)){Add-Reason $reasons "LIVE_POSTSTATE_MISMATCH_${pair}"}}catch{Add-Reason $reasons "LIVE_POSTSTATE_UNREADABLE_${pair}:$($_.Exception.GetType().Name):$($_.Exception.Message)"}
        $expectedName=if($isTest){[string]$evidence.token.name}elseif($row.role-ceq'PARTY_B'){$script:PartyBName}else{$script:PartyCName};$expectedSid=if($isTest){[string]$evidence.token.sid}elseif($row.role-ceq'PARTY_B'){$script:PartyBSid}else{$script:PartyCSid}
        if([string]$evidence.token.name-cne$expectedName-or[string]$evidence.token.sid-cne$expectedSid-or[bool]$evidence.token.isAdministrator){Add-Reason $reasons "TOKEN_INVALID_${pair}"}
    }
    return [pscustomobject]@{manifest=$manifest;reasons=$reasons;evidenceHashes=$hashes}
}

function Invoke-Finalize([string]$InputPath,[string]$ResultPath,[bool]$AllowSyntheticTestPolicy){
    $checked=Test-Manifest $InputPath $AllowSyntheticTestPolicy;$disposition=if($checked.reasons.Count-eq0){'PASS_ACTUAL_TOKEN_PROOF'}else{'INCONCLUSIVE_OR_FAILED'};$isActual=$false;if($null-ne$checked.manifest){$isActual=-not([bool]$checked.manifest.testPolicy)};$record=[ordered]@{schema='cvf.g4.actualTokenProofFinalVerdict.v1';disposition=$disposition;runId=if($null-ne$checked.manifest){[string]$checked.manifest.runId}else{$null};manifestPath=Get-CanonicalPath $InputPath;manifestSha256Hex=if(Test-Path -LiteralPath $InputPath){Get-FileSha256 $InputPath}else{$null};evidenceHashes=@($checked.evidenceHashes);reasons=@($checked.reasons);localFinalizer=[ordered]@{name=[Security.Principal.WindowsIdentity]::GetCurrent().Name;sid=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value};actualTokenProofClaimed=($disposition-ceq'PASS_ACTUAL_TOKEN_PROOF'-and$isActual);adjudicatedAtUtc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')};Write-Utf8Json $ResultPath $record;return [pscustomobject]$record
}

function Add-Test([string]$Id,[bool]$Passed,[string]$Detail){$script:Tests.Add([pscustomobject]@{id=$Id;passed=$Passed;detail=$Detail});if(-not$Passed){Stop-Finalizer 'FINALIZER_SELFTEST_FAILED' "${Id}: $Detail"}}
function New-SyntheticEvidence([string]$ManifestPath){$manifest=Get-Content -LiteralPath $ManifestPath -Raw|ConvertFrom-Json;foreach($row in $manifest.matrix){$envelope=Get-Content -LiteralPath ([string]$row.envelopePath)-Raw|ConvertFrom-Json;$record=[ordered]@{schema='cvf.g4.actualTokenProbeEvidence.v1';runId=[string]$manifest.runId;role=[string]$row.role;action=[string]$row.action;testPolicy=$true;token=[ordered]@{name=[string]$envelope.expectedAccountName;sid=[string]$envelope.expectedSid;isAdministrator=$false;groups=@()};expectedOutcome=[string]$row.expectedOutcome;observedOutcome=[string]$row.expectedOutcome;operationDetail='synthetic finalizer self-test only';prestate=[ordered]@{};poststate=[ordered]@{};postconditionsVerified=$true;disposition='PASS';envelopeBindingSha256Hex=[string]$envelope.bindingSha256Hex;recordedAtUtc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')};Write-Utf8Json ([string]$row.evidencePath) $record}}
function Invoke-SelfTest {
    $coordinator=Join-Path $script:RepoRoot 'scripts/acel_g1_group4_actual_token_coordinator.ps1';$inputRoot=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-finalizer-input-'+[Guid]::NewGuid().ToString('N'));$root=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-actual-token-test-'+[Guid]::NewGuid().ToString('N'));[IO.Directory]::CreateDirectory($inputRoot)|Out-Null;$payload=Join-Path $inputRoot 'payload.json';[IO.File]::WriteAllText($payload,'{"finalizer":"test"}')
    try{$raw=& pwsh -NoProfile -NonInteractive -File $coordinator -PrepareProof -DisposableRoot $root -RegistryPayloadSource $payload -TestPolicy 2>&1;if($LASTEXITCODE-ne0){Stop-Finalizer 'FINALIZER_FIXTURE_FAILED' ($raw-join"`n")};$packet=$raw|ConvertFrom-Json;$commands=Get-Content -LiteralPath $packet.commandPacketPath -Raw|ConvertFrom-Json;foreach($command in $commands.commands){$null=& $command.commandExecutable @($command.commandArguments);if($LASTEXITCODE-ne0){Stop-Finalizer 'FINALIZER_PROBE_COMMAND_FAILED' "$($command.role)/$($command.action)"}};$manifest=Get-Content -LiteralPath $packet.manifestPath -Raw|ConvertFrom-Json
        $passPath=Join-Path $root 'control/selftest-pass.json';$pass=Invoke-Finalize $packet.manifestPath $passPath $true;Add-Test 'G4-FINALIZER-STRUCTURAL-PASS' ($pass.disposition-ceq'PASS_ACTUAL_TOKEN_PROOF') 'complete synthetic ledger exercises positive adjudication logic'
        $publicPath=Join-Path $root 'control/selftest-public.json';$public=Invoke-Finalize $packet.manifestPath $publicPath $false;Add-Test 'G4-FINALIZER-TESTPOLICY-FAILS-CLOSED' ($public.disposition-ceq'INCONCLUSIVE_OR_FAILED'-and$public.reasons-ccontains'TEST_POLICY_EVIDENCE_INADMISSIBLE') 'test policy never becomes actual proof'
        $first=[string]$manifest.matrix[0].evidencePath;$saved=[IO.File]::ReadAllBytes($first);Remove-Item -LiteralPath $first -Force;$missing=Test-Manifest $packet.manifestPath $true;Add-Test 'G4-FINALIZER-MISSING-EVIDENCE' (@($missing.reasons|Where-Object{$_-like'EVIDENCE_MISSING_*'}).Count-eq1) 'missing row rejected';[IO.File]::WriteAllBytes($first,$saved)
        $record=Get-Content -LiteralPath $first -Raw|ConvertFrom-Json;$record.envelopeBindingSha256Hex='0'*64;Write-Utf8Json $first $record;$altered=Test-Manifest $packet.manifestPath $true;Add-Test 'G4-FINALIZER-ALTERED-EVIDENCE' (@($altered.reasons|Where-Object{$_-like'EVIDENCE_ENVELOPE_BINDING_INVALID_*'}).Count-eq1) 'altered binding rejected';[IO.File]::WriteAllBytes($first,$saved)
        $manifest.matrix[1].role=$manifest.matrix[0].role;$manifest.matrix[1].action=$manifest.matrix[0].action;$duplicatePath=Join-Path $root 'control/MANIFEST-DUPLICATE.json';Write-Utf8Json $duplicatePath $manifest;$duplicate=Test-Manifest $duplicatePath $true;Add-Test 'G4-FINALIZER-DUPLICATE' ($duplicate.reasons-ccontains'MATRIX_DUPLICATE_OR_MISSING') 'duplicate role/action rejected'
        $residue=Join-Path ([string]$manifest.matrix[0].fixturePrestate.parent.path) 'unknown.bin';[IO.File]::WriteAllBytes($residue,[byte[]](1));$dirty=Test-Manifest $packet.manifestPath $true;Add-Test 'G4-FINALIZER-RESIDUE' (@($dirty.reasons|Where-Object{$_-like'LIVE_POSTSTATE_MISMATCH_*'}).Count-ge1) ('unexpected residue rejected; reasons='+(@($dirty.reasons)-join','));Remove-Item -LiteralPath $residue -Force
        [pscustomobject]@{result='PASS';tests=$script:Tests.Count;publicTestPolicyDisposition='INCONCLUSIVE_OR_FAILED';allowedVerdicts=@('PASS_ACTUAL_TOKEN_PROOF','INCONCLUSIVE_OR_FAILED');realPrincipalClaimed=$false}|ConvertTo-Json -Compress
    }finally{foreach($path in @($root,$inputRoot)){if(Test-Path -LiteralPath $path){Remove-Item -LiteralPath $path -Recurse -Force}}}
}

if($PSCmdlet.ParameterSetName-ceq'Finalize'){Invoke-Finalize $ManifestPath $OutputPath $false|ConvertTo-Json -Depth 10 -Compress;exit 0}
Invoke-SelfTest
exit 0
