param([string]$RepositoryRoot)
$ErrorActionPreference='Stop'
Set-StrictMode -Version Latest
$root=Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-local-review-'+[Guid]::NewGuid().ToString('N'))
[IO.Directory]::CreateDirectory($root)|Out-Null
$results=[Collections.Generic.List[object]]::new()
$script:LocalSid=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$script:SystemSid='S-1-5-18'
$script:AdministratorsSid='S-1-5-32-544'
foreach($role in @('c','b')) {
 & {
  param($role,$root,$results,$RepositoryRoot)
  $name=if($role-eq'c'){'acel_g1_party_c_group4_registry_writer.ps1'}else{'acel_g1_party_b_group4_lookup_response_writer.ps1'}
  $tokens=$null;$errors=$null
  $ast=[Management.Automation.Language.Parser]::ParseFile((Join-Path $RepositoryRoot ('scripts/'+$name)),[ref]$tokens,[ref]$errors)
  if($errors.Count){throw 'PARSE_ERROR'}
  foreach($f in $ast.EndBlock.Statements | Where-Object {$_ -is [Management.Automation.Language.FunctionDefinitionAst]}) { Invoke-Expression $f.Extent.Text }
   foreach($case in @('positive','shared-parent-positive','hardlink','unknown-sibling','post-replace-failure')) {
   if($role-eq'b'-and$case-eq'post-replace-failure'){continue}
   $dir=Join-Path $root ($role+'-'+$case);[IO.Directory]::CreateDirectory($dir)|Out-Null
   $target=Join-Path $dir $(if($role-eq'c'){'REGISTRY.json'}else{'LOOKUP_RESPONSES.jsonl'})
   [IO.File]::WriteAllBytes($target,[byte[]]::new(0));Set-ExactSecurity $target -TestPolicy|Out-Null
   $input=Join-Path $root ('input-'+$role+'-'+$case+'.json');[IO.File]::WriteAllText($input,'{"reviewer":true}')
   $ledger=Join-Path $root ('ledger-'+$role+'-'+$case+'.jsonl')
    if($case-eq'hardlink'){New-Item -ItemType HardLink -Path (Join-Path $dir 'second-name') -Target $target|Out-Null}
    if($case-eq'unknown-sibling'){[IO.File]::WriteAllText((Join-Path $dir 'unregistered.bin'),'preserve')}
    if($case-eq'shared-parent-positive'){
     $peer=Join-Path $dir $(if($role-eq'c'){'LOOKUP_RESPONSES.jsonl'}else{'REGISTRY.json'})
     [IO.File]::WriteAllBytes($peer,[byte[]]::new(0))
    }
   $caught=$null
   try {
    if($role-eq'c'){
     $args=@{InputPath=$input;TargetPath=$target;RequireReservation=$true;TestPolicy=$true;LedgerPath=$ledger}
     if($case-eq'post-replace-failure'){$args.InjectFailure='AfterMove'}
     Publish-RegistryTransaction @args|Out-Null
    }else{Write-CopyOnWriteTransaction -Target $target -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger}
   }catch{$caught=$_.Exception.Message}
   $len=([IO.FileInfo]::new($target)).Length
    $passed=if($case-in@('positive','shared-parent-positive')){$null-eq$caught}elseif($case-eq'post-replace-failure'){$null-ne$caught-and$len-eq0}else{$null-ne$caught-and$len-eq0}
   $results.Add([pscustomobject]@{id=($role+'-'+$case);requiredBehaviorSatisfied=$passed;exception=$caught;targetLength=$len})
  }
 } $role $root $results $RepositoryRoot
}
& {
 param($root,$results,$RepositoryRoot)
 $tokens=$null;$errors=$null
 $ast=[Management.Automation.Language.Parser]::ParseFile((Join-Path $RepositoryRoot 'scripts/acel_g1_group4_admin_recovery.ps1'),[ref]$tokens,[ref]$errors)
 foreach($f in $ast.EndBlock.Statements|Where-Object {$_ -is [Management.Automation.Language.FunctionDefinitionAst]}){Invoke-Expression $f.Extent.Text}
 foreach($case in @('missing-binding-control','unverified-binding','traversal-binding')) {
  $dir=Join-Path $root ('recovery-'+$case);[IO.Directory]::CreateDirectory($dir)|Out-Null
  $target=Join-Path $dir 'REGISTRY.json';[IO.File]::WriteAllBytes($target,[byte[]]::new(0))
  $tempName='.cvf-g4-registry-review.tmp'
  if($case-eq'traversal-binding'){$outside=Join-Path $root 'reviewer-owned-outside-source';[IO.Directory]::CreateDirectory($outside)|Out-Null;$tempName='../reviewer-owned-outside-source/.cvf-g4-registry-review.tmp'}
  $temp=[IO.Path]::GetFullPath((Join-Path $dir $tempName))
  if(-not$temp.StartsWith($root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){throw 'REVIEW_FIXTURE_ESCAPE'}
  [IO.File]::WriteAllText($temp,'reviewer-owned sentinel; no termination or identity evidence')
  $ledger=Join-Path $dir 'ledger.jsonl'
  $record=@{transactionId='review-txn';targetPath=$target;tempName=$tempName;writerSid='S-1-0-0';phase='TEMP_PLANNED'}
  [IO.File]::WriteAllText($ledger,($record|ConvertTo-Json -Compress)+[Environment]::NewLine)
  $caught=$null;$out=$null
  try{$id=if($case-eq'missing-binding-control'){'absent-txn'}else{'review-txn'};$out=Invoke-Recovery -LedgerPath $ledger -TransactionId $id}catch{$caught=$_.Exception.Message}
  $exists=Test-Path -LiteralPath $temp
  $results.Add([pscustomobject]@{id=('recovery-'+$case);requiredBehaviorSatisfied=($null-ne$caught-and$exists);exception=$caught;sentinelPreserved=$exists;result=$out})
 }

 # A syntactically complete but semantically unbound ledger row is not proof
 # that the named bytes were created by this transaction or that its writer
 # terminated. Recovery must preserve the reviewer-owned sentinel.
 $case='complete-but-unbound'
 $dir=Join-Path $root ('recovery-'+$case);[IO.Directory]::CreateDirectory($dir)|Out-Null
 $target=Join-Path $dir 'REGISTRY.json';[IO.File]::WriteAllBytes($target,[Text.Encoding]::UTF8.GetBytes('reviewer target prestate'))
 $tempName='.cvf-g4-registry-review-complete.tmp';$temp=Join-Path $dir $tempName
 $currentSid=[Security.Principal.WindowsIdentity]::GetCurrent().User.Value
 New-FixtureHardenedTemp $temp $currentSid ([Text.Encoding]::UTF8.GetBytes('reviewer sentinel not transaction-bound'))
 $ledger=Join-Path $dir 'ledger.jsonl'
 $record=@{schema='untrusted.noncontract.schema';transactionId='review-complete-unbound';writerSid=$currentSid;targetName='WRONG_TARGET.json';targetPath=$target;tempName=$tempName;phase='TEMP_PLANNED';recordedAt='not-a-timestamp'}
 [IO.File]::WriteAllText($ledger,($record|ConvertTo-Json -Compress)+[Environment]::NewLine)
 $caught=$null;$out=$null
 try{$out=Invoke-Recovery -LedgerPath $ledger -TransactionId 'review-complete-unbound' -TestPolicy}catch{$caught=$_.Exception.Message}
 $exists=Test-Path -LiteralPath $temp
 $results.Add([pscustomobject]@{id='recovery-complete-but-unbound';requiredBehaviorSatisfied=($null-ne$caught-and$exists);exception=$caught;sentinelPreserved=$exists;result=$out;missingBindings=@('contract schema','targetName/path agreement','target file identity','prestate hash','security digest','confirmed writer termination')})

 # A malformed row for another transaction must not whitelist an unknown
 # sibling during recovery of a valid transaction.
 $writer=Get-TerminatedWriterIdentity
 $fixture=New-RecoveryFixture $root 'recovery-malformed-other-binding' $writer -WithOtherReservation
 $unknown=Join-Path $fixture.parent 'unexpected.bin';[IO.File]::WriteAllText($unknown,'reviewer unknown sibling')
 $other=@{transactionId='unvalidated-other-transaction';tempName='unexpected.bin'}
 [IO.File]::AppendAllText($fixture.ledger,(($other|ConvertTo-Json -Compress)+[Environment]::NewLine))
 $caught=$null;$out=$null
 try{$out=Invoke-Recovery -LedgerPath $fixture.ledger -TransactionId $fixture.transactionId -TestPolicy}catch{$caught=$_.Exception.Message}
 $primaryPreserved=Test-Path -LiteralPath $fixture.temp;$unknownPreserved=Test-Path -LiteralPath $unknown
 $results.Add([pscustomobject]@{id='recovery-malformed-other-binding-does-not-whitelist';requiredBehaviorSatisfied=($null-ne$caught-and$primaryPreserved-and$unknownPreserved);exception=$caught;primaryResiduePreserved=$primaryPreserved;unknownSiblingPreserved=$unknownPreserved;result=$out})
} $root $results $RepositoryRoot
[pscustomobject]@{fixtureRoot=$root;realPrincipalExecuted=$false;productionSourceTouched=$false;cases=@($results.ToArray());failed=@($results|Where-Object {-not$_.requiredBehaviorSatisfied}).Count}|ConvertTo-Json -Depth 7
