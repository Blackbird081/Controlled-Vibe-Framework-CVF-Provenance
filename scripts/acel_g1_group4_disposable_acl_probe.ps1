<#
.SYNOPSIS
Local disposable verification and record harness for Group 4 reservation
tooling (C1-R2-08, C0-R1 Local preflight/postflight boundary).

.DESCRIPTION
Implements, for disposable roots only, the C0-R1 transaction-bound Local
boundary around a writer mutation:

  1. Local preflight: acquire the parent-scoped Local guard; verify the parent,
     the exact closed two-name reservation set, link counts and the writer's
     zero-byte reservation; capture complete parent and both target states in a
     Local-only preflight record bound to the transaction ID; hash that record
     into an authorization reference; issue a per-writer authorization view
     that contains only the writer's own-target fields.
  2. The writer (loaded from its own script) claims its reservation only if
     the view matches its transaction, parent identity, held guard and own
     target exactly.
  3. Local postflight: verify parent identity/security, the exact two-name
     inventory with no residue, exact invariance of the other target and the
     expected own-target poststate; record PASS or FAIL; release the guard.

It also exercises the distinct ledger-bound recovery against a real crashed
writer process. Every path is confined to %TEMP%\cvf-g4-probe-* or
%TEMP%\cvf-g4c-* and can never resolve to governance/sources/issuer_registry.
It never runs as Party B/C and makes no real-principal claim. Local preflight
for the real source parent is outside this tranche (operator checkpoint).
#>
[CmdletBinding()]
param(
    [switch] $SelfTest
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:ScriptPath = $PSCommandPath
$script:RepoRoot = Split-Path -Parent (Split-Path -Parent $script:ScriptPath)
$script:PartyCWriter = Join-Path $script:RepoRoot 'scripts/acel_g1_party_c_group4_registry_writer.ps1'
$script:PartyBWriter = Join-Path $script:RepoRoot 'scripts/acel_g1_party_b_group4_lookup_response_writer.ps1'
$script:RecoveryScript = Join-Path $script:RepoRoot 'scripts/acel_g1_group4_admin_recovery.ps1'
$script:RealSourceParent = Join-Path $script:RepoRoot 'governance/sources/issuer_registry'
$script:Tests = [System.Collections.Generic.List[object]]::new()
# Writer functions loaded under TestPolicy read these script-scope SIDs.
$script:LocalSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
$script:SystemSid = 'S-1-5-18'
$script:AdministratorsSid = 'S-1-5-32-544'

function Stop-Probe([string] $Code, [string] $Message) {
    throw [System.InvalidOperationException]::new("${Code}: ${Message}")
}

function Get-LocalCanonicalPath([string] $Path) {
    return [System.IO.Path]::GetFullPath($Path).TrimEnd([System.IO.Path]::DirectorySeparatorChar)
}

function Get-LocalSha256Hex([byte[]] $Bytes) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant() } finally { $sha.Dispose() }
}

function Assert-LocalDisposablePath([string] $Path) {
    $tempRoot = Get-LocalCanonicalPath ([IO.Path]::GetTempPath())
    $full = Get-LocalCanonicalPath $Path
    if (-not $full.StartsWith($tempRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $full }
    $first = (($full.Substring($tempRoot.Length + 1)) -split '[\\/]')[0]
    if ($first -notlike 'cvf-g4-probe-*' -and $first -notlike 'cvf-g4c-*') { Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' $full }
    $real = Get-LocalCanonicalPath $script:RealSourceParent
    if ($full -ieq $real -or $full.StartsWith($real + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { Stop-Probe 'PROBE_REAL_SOURCE_REACHED' $full }
    $current = $tempRoot
    foreach ($part in $full.Substring($tempRoot.Length + 1) -split '[\\/]') {
        $current = Join-Path $current $part
        if ((Test-Path -LiteralPath $current) -and ((Get-Item -LiteralPath $current -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { Stop-Probe 'PROBE_CONTAINMENT_VIOLATION' ('reparse traversal: ' + $current) }
    }
}

function Get-LocalFileId([string] $Path) {
    $output = & fsutil file queryfileid $Path 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Probe 'LOCAL_FILE_IDENTITY_UNAVAILABLE' $Path }
    return ([regex]::Match(($output -join ' '), '0x[0-9a-fA-F]+')).Value.ToLowerInvariant()
}

function Get-LocalLinkCount([string] $Path) {
    $output = & fsutil hardlink list $Path 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Probe 'LOCAL_LINK_COUNT_UNAVAILABLE' $Path }
    return @($output | Where-Object { $_.Trim().Length -gt 0 }).Count
}

function Get-LocalSecurityDigest($Security) {
    $owner = $Security.GetOwner([System.Security.Principal.SecurityIdentifier]).Value
    $tuples = @($Security.GetAccessRules($true, $true, [System.Security.Principal.SecurityIdentifier]) | ForEach-Object {
        '{0}|{1}|{2}|{3}|{4}|{5}' -f $_.IdentityReference.Value, [int]$_.FileSystemRights, [int]$_.AccessControlType, [bool]$_.IsInherited, [int]$_.InheritanceFlags, [int]$_.PropagationFlags
    })
    $text = 'owner=' + $owner + ';protected=' + ([bool]$Security.AreAccessRulesProtected).ToString() + ';aces=' + ($tuples -join "`n")
    return [pscustomobject]@{ ownerSid = $owner; protection = [bool]$Security.AreAccessRulesProtected; digest = Get-LocalSha256Hex ([Text.Encoding]::UTF8.GetBytes($text)) }
}

# Local may read both reservations; writers never receive the other one.
function Get-LocalFileState([string] $Path) {
    $info = [System.IO.FileInfo]::new($Path)
    $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor [System.Security.AccessControl.AccessControlSections]::Access
    $security = Get-LocalSecurityDigest ([System.IO.FileSystemAclExtensions]::GetAccessControl($info, $sections))
    return [ordered]@{
        fileId = Get-LocalFileId $Path
        length = [int64]$info.Length
        sha256 = Get-LocalSha256Hex ([System.IO.File]::ReadAllBytes($Path))
        linkCount = [int](Get-LocalLinkCount $Path)
        attributes = [int]$info.Attributes
        ownerSid = $security.ownerSid
        protection = $security.protection
        securityDigest = $security.digest
    }
}

function Format-LocalFileState($State) {
    return '{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}' -f $State.fileId, $State.length, $State.sha256, $State.linkCount, $State.attributes, $State.ownerSid, ([bool]$State.protection).ToString(), $State.securityDigest
}

function Get-LocalDirectoryState([string] $Path) {
    $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor [System.Security.AccessControl.AccessControlSections]::Access
    $security = Get-LocalSecurityDigest ([System.IO.FileSystemAclExtensions]::GetAccessControl([System.IO.DirectoryInfo]::new($Path), $sections))
    return [ordered]@{ fileId = Get-LocalFileId $Path; securityDigest = $security.digest }
}

function Get-LocalParentGuardName([string] $ParentPath) {
    $raw = [Text.Encoding]::UTF8.GetBytes((Get-LocalCanonicalPath $ParentPath).ToUpperInvariant())
    return 'Global\CVF_G4_PARENT_GUARD_' + (Get-LocalSha256Hex $raw).Substring(0, 48)
}

function Get-LocalTargetName([string] $Kind) {
    if ($Kind -ceq 'REGISTRY') { return 'REGISTRY.json' }
    if ($Kind -ceq 'RESPONSE') { return 'LOOKUP_RESPONSES.jsonl' }
    Stop-Probe 'LOCAL_PREFLIGHT_KIND_INVALID' $Kind
}

function Assert-LocalInventory([string] $ParentPath, [string] $Code) {
    $items = @(Get-ChildItem -LiteralPath $ParentPath -Force)
    $names = (@($items | ForEach-Object Name) | Sort-Object) -join ','
    if ($names -cne 'LOOKUP_RESPONSES.jsonl,REGISTRY.json') { Stop-Probe $Code "inventory [$names]" }
    foreach ($item in $items) {
        if ($item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { Stop-Probe $Code $item.FullName }
    }
    return @('LOOKUP_RESPONSES.jsonl', 'REGISTRY.json')
}

function New-LocalReservation([string] $Path) {
    [System.IO.File]::WriteAllBytes($Path, [byte[]]::new(0))
    $owner = [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid)
    $security = [System.Security.AccessControl.FileSecurity]::new()
    $security.SetAccessRuleProtection($true, $false)
    $security.SetOwner($owner)
    $security.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new($owner, [System.Security.AccessControl.FileSystemRights]::FullControl, [System.Security.AccessControl.AccessControlType]::Allow))
    [System.IO.FileSystemAclExtensions]::SetAccessControl([System.IO.FileInfo]::new($Path), $security)
}

function Invoke-LocalPreflight([string] $ParentPath, [string] $WriterKind, [string] $TransactionId, [string] $RecordDirectory, [string] $ExpectedOwnSecurityDigest) {
    $parent = Get-LocalCanonicalPath $ParentPath
    Assert-LocalDisposablePath $parent
    $records = Get-LocalCanonicalPath $RecordDirectory
    Assert-LocalDisposablePath $records
    if ($records -ieq $parent -or $records.StartsWith($parent + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { Stop-Probe 'LOCAL_RECORD_INSIDE_PROTECTED_PARENT' $records }
    if (-not (Test-Path -LiteralPath $parent -PathType Container)) { Stop-Probe 'LOCAL_PREFLIGHT_PARENT_MISSING' $parent }
    $guardName = Get-LocalParentGuardName $parent
    $guard = [System.Threading.Mutex]::new($false, $guardName)
    $held = $false
    try { $held = $guard.WaitOne(0) } catch [System.Threading.AbandonedMutexException] { $held = $true }
    if (-not $held) { $guard.Dispose(); Stop-Probe 'LOCAL_PREFLIGHT_GUARD_BUSY' $guardName }
    try {
        $siblings = Assert-LocalInventory $parent 'LOCAL_PREFLIGHT_SIBLING_SET'
        $targetName = Get-LocalTargetName $WriterKind
        $states = [ordered]@{}
        foreach ($kind in @('REGISTRY', 'RESPONSE')) {
            $path = Join-Path $parent (Get-LocalTargetName $kind)
            $state = Get-LocalFileState $path
            if ($state.linkCount -ne 1) { Stop-Probe 'LOCAL_PREFLIGHT_LINK_COUNT' $path }
            $states[$kind] = $state
        }
        $own = $states[$WriterKind]
        if ($own.length -ne 0 -or $own.securityDigest -cne $ExpectedOwnSecurityDigest) { Stop-Probe 'LOCAL_PREFLIGHT_TARGET_NOT_RESERVED' $targetName }
        $parentState = Get-LocalDirectoryState $parent
        [System.IO.Directory]::CreateDirectory($records) | Out-Null
        $record = [ordered]@{
            schema = 'cvf.g4.localPreflightRecord.v1'; transactionId = $TransactionId; writerKind = $WriterKind
            parentPath = $parent; parentFileId = $parentState.fileId; parentSecurityDigest = $parentState.securityDigest
            siblingSet = $siblings; targets = $states; guardName = $guardName
            issuedAt = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')
        }
        $recordPath = Join-Path $records ("preflight-$TransactionId.json")
        [System.IO.File]::WriteAllText($recordPath, ($record | ConvertTo-Json -Depth 6 -Compress))
        $authorizationRef = Get-LocalSha256Hex ([System.IO.File]::ReadAllBytes($recordPath))
        $view = [ordered]@{
            schema = 'cvf.g4.localWriterAuthorization.v1'; transactionId = $TransactionId; authorizationRef = $authorizationRef
            status = 'PREFLIGHT_PASSED'; parentPath = $parent; parentFileId = $parentState.fileId; guardName = $guardName
            targetKind = $WriterKind; targetName = $targetName; ownTarget = $own
            issuedAt = $record.issuedAt
        }
        $authorizationPath = Join-Path $records ("authorization-$WriterKind-$TransactionId.json")
        [System.IO.File]::WriteAllText($authorizationPath, ($view | ConvertTo-Json -Depth 6 -Compress))
        return [pscustomobject]@{
            transactionId = $TransactionId; writerKind = $WriterKind; parentPath = $parent; recordDirectory = $records
            recordPath = $recordPath; authorizationPath = $authorizationPath; authorizationRef = $authorizationRef
            record = $record; guard = $guard
        }
    } catch {
        try { $guard.ReleaseMutex() } catch {}
        $guard.Dispose()
        throw
    }
}

function Close-LocalPreflight($Preflight) {
    if ($null -ne $Preflight.guard) {
        try { $Preflight.guard.ReleaseMutex() } catch {}
        $Preflight.guard.Dispose()
        $Preflight.guard = $null
    }
}

function Invoke-LocalPostflight($Preflight, [string] $ExpectedOwnSha256) {
    $verdict = 'PASS'; $reason = $null; $ownAfter = $null; $otherAfter = $null; $parentAfter = $null; $inventory = $null
    try {
        try {
            $parentAfter = Get-LocalDirectoryState $Preflight.parentPath
            if ($parentAfter.fileId -cne $Preflight.record.parentFileId -or $parentAfter.securityDigest -cne $Preflight.record.parentSecurityDigest) { Stop-Probe 'LOCAL_POSTFLIGHT_PARENT_DRIFT' $Preflight.parentPath }
            $inventory = Assert-LocalInventory $Preflight.parentPath 'LOCAL_POSTFLIGHT_RESIDUE'
            $otherKind = if ($Preflight.writerKind -ceq 'REGISTRY') { 'RESPONSE' } else { 'REGISTRY' }
            $otherAfter = Get-LocalFileState (Join-Path $Preflight.parentPath (Get-LocalTargetName $otherKind))
            if ((Format-LocalFileState $otherAfter) -cne (Format-LocalFileState $Preflight.record.targets[$otherKind])) { Stop-Probe 'LOCAL_POSTFLIGHT_OTHER_TARGET_DRIFT' $otherKind }
            $ownBefore = $Preflight.record.targets[$Preflight.writerKind]
            $ownAfter = Get-LocalFileState (Join-Path $Preflight.parentPath (Get-LocalTargetName $Preflight.writerKind))
            if ($ownAfter.sha256 -cne $ExpectedOwnSha256 -or $ownAfter.linkCount -ne 1 -or $ownAfter.securityDigest -cne $ownBefore.securityDigest -or $ownAfter.ownerSid -cne $ownBefore.ownerSid -or $ownAfter.protection -ne $ownBefore.protection) { Stop-Probe 'LOCAL_POSTFLIGHT_OWN_TARGET_MISMATCH' $Preflight.writerKind }
        } catch { $verdict = 'FAIL'; $reason = $_.Exception.Message }
        $postflight = [ordered]@{
            schema = 'cvf.g4.localPostflightRecord.v1'; transactionId = $Preflight.transactionId; authorizationRef = $Preflight.authorizationRef
            verdict = $verdict; reason = $reason; parentPoststate = $parentAfter; inventory = $inventory
            ownTargetPoststate = $ownAfter; otherTargetPoststate = $otherAfter; checkedAt = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')
        }
        $postflightPath = Join-Path $Preflight.recordDirectory ("postflight-$($Preflight.transactionId).json")
        [System.IO.File]::WriteAllText($postflightPath, ($postflight | ConvertTo-Json -Depth 6 -Compress))
        if ($verdict -cne 'PASS') { throw [System.InvalidOperationException]::new($reason) }
        return [pscustomobject]@{ verdict = $verdict; path = $postflightPath; record = $postflight }
    } finally { Close-LocalPreflight $Preflight }
}

function Get-FunctionDefinitions([string] $Path) {
    $tokens = $null; $errors = $null
    $ast = [System.Management.Automation.Language.Parser]::ParseFile($Path, [ref] $tokens, [ref] $errors)
    if ($errors.Count) { Stop-Probe 'PROBE_PARSE_ERROR' $Path }
    return @($ast.EndBlock.Statements | Where-Object { $_ -is [System.Management.Automation.Language.FunctionDefinitionAst] } | ForEach-Object { $_.Extent.Text })
}

function Add-Test([string] $Id, [bool] $Passed, [string] $Detail) {
    $script:Tests.Add([pscustomobject]@{ id = $Id; passed = $Passed; detail = $Detail })
    if (-not $Passed) { Stop-Probe 'PROBE_ASSERTION_FAILED' "${Id}: ${Detail}" }
}

function New-LocalParent([string] $Root, [string] $Name) {
    $parent = Join-Path $Root $Name
    [System.IO.Directory]::CreateDirectory($parent) | Out-Null
    New-LocalReservation (Join-Path $parent 'REGISTRY.json')
    New-LocalReservation (Join-Path $parent 'LOOKUP_RESPONSES.jsonl')
    return $parent
}

function Invoke-DisposableProbe {
    $root = Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-probe-' + [Guid]::NewGuid().ToString('N'))
    $crashRoot = Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4c-' + [Guid]::NewGuid().ToString('N'))
    Assert-LocalDisposablePath $root; Assert-LocalDisposablePath $crashRoot
    [System.IO.Directory]::CreateDirectory($root) | Out-Null
    [System.IO.Directory]::CreateDirectory($crashRoot) | Out-Null
    try {
        $records = Join-Path $root 'local-records'
        $ledger = Join-Path $root 'ledger/LEDGER.jsonl'
        $inputPath = Join-Path $root 'input.json'
        $inputBytes = [Text.Encoding]::UTF8.GetBytes('{"probe":"registry bytes"}')
        [System.IO.File]::WriteAllBytes($inputPath, $inputBytes)
        $probeReservation = Join-Path $root 'digest-probe.json'; New-LocalReservation $probeReservation
        $reservedDigest = (Get-LocalFileState $probeReservation).securityDigest

        # Containment of the harness itself.
        try { Assert-LocalDisposablePath (Join-Path $script:RealSourceParent 'REGISTRY.json'); $blocked = $false } catch { $blocked = $_.Exception.Message -like 'PROBE_*' }
        Add-Test 'PROBE-CONTAINMENT-REAL-SOURCE' $blocked 'the harness refuses the real Group 4 source path'
        $escape = Join-Path $root ('..' + [IO.Path]::DirectorySeparatorChar + 'escape-probe')
        & pwsh -NoProfile -NonInteractive -File $script:PartyCWriter -PeerMode -PeerRunId ([Guid]::NewGuid().ToString('N')) -PeerTargetPath $escape -PeerInputPath $escape -PeerLedgerPath $escape 2>&1 | Out-Null
        Add-Test 'PROBE-PARTY-C-ESCAPE-BLOCKED' ($LASTEXITCODE -ne 0) 'Party C peer mode rejects a path outside the disposable root'

        # RV10: complete Local preflight -> Party C claim -> Local postflight.
        & {
            foreach ($definition in Get-FunctionDefinitions $script:PartyCWriter) { Invoke-Expression $definition }
            $parent = New-LocalParent $root 'shared'
            $txn = 'local-c-' + [Guid]::NewGuid().ToString('N')
            $pre = Invoke-LocalPreflight $parent 'REGISTRY' $txn $records $reservedDigest
            $view = Get-Content -LiteralPath $pre.authorizationPath -Raw
            $viewObject = $view | ConvertFrom-Json
            Add-Test 'PROBE-RV10-C-VIEW-OWN-ONLY' (((@($viewObject.PSObject.Properties.Name) | Sort-Object) -join ',') -ceq 'authorizationRef,guardName,issuedAt,ownTarget,parentFileId,parentPath,schema,status,targetKind,targetName,transactionId' -and -not $view.Contains([string]$pre.record.targets['RESPONSE'].fileId)) 'Party C view carries only its own target and no response identity, bytes or security'
            Add-Test 'PROBE-RV10-C-REF-BINDS-RECORD' ($pre.authorizationRef -ceq (Get-LocalSha256Hex ([System.IO.File]::ReadAllBytes($pre.recordPath)))) 'authorization reference is the hash of the Local preflight record'
            Publish-RegistryTransaction -InputPath $inputPath -TargetPath (Join-Path $parent 'REGISTRY.json') -TestPolicy -LedgerPath $ledger -RequireReservation -TransactionId $txn -AuthorizationPath $pre.authorizationPath | Out-Null
            $post = Invoke-LocalPostflight $pre (Get-LocalSha256Hex $inputBytes)
            Add-Test 'PROBE-RV10-C-POSTFLIGHT' ($post.verdict -ceq 'PASS' -and (Test-Path $post.path)) 'Local postflight records PASS: parent, two-name inventory, response invariance and registry poststate'
            $rows = @([System.IO.File]::ReadAllLines($ledger) | ForEach-Object { $_ | ConvertFrom-Json } | Where-Object { $_.transactionId -ceq $txn })
            Add-Test 'PROBE-RV10-C-LEDGER-BOUND' ((($rows | ForEach-Object phase) -join ',') -ceq 'TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE,PUBLISHED' -and [string]$rows[0].parentFileId -ceq [string]$pre.record.parentFileId) 'writer ledger shares the Local transaction ID and parent identity'
            $script:SharedParent = $parent
        }

        # RV10: Party B initialization on the same shared parent after Party C.
        & {
            foreach ($definition in Get-FunctionDefinitions $script:PartyBWriter) { Invoke-Expression $definition }
            $parent = $script:SharedParent
            $txn = 'local-b-' + [Guid]::NewGuid().ToString('N')
            $pre = Invoke-LocalPreflight $parent 'RESPONSE' $txn $records $reservedDigest
            $view = Get-Content -LiteralPath $pre.authorizationPath -Raw
            Add-Test 'PROBE-RV10-B-VIEW-OWN-ONLY' (-not $view.Contains([string]$pre.record.targets['REGISTRY'].sha256) -and -not $view.Contains([string]$pre.record.targets['REGISTRY'].fileId)) 'Party B view carries no registry identity or content hash and grants no registry authority'
            Write-CopyOnWriteTransaction -Target (Join-Path $parent 'LOOKUP_RESPONSES.jsonl') -FinalBytes ([byte[]]::new(0)) -RequireReservation -TestPolicy -LedgerPath $ledger -TransactionId $txn -AuthorizationPath $pre.authorizationPath
            $post = Invoke-LocalPostflight $pre (Get-LocalSha256Hex ([byte[]]::new(0)))
            Add-Test 'PROBE-RV10-B-POSTFLIGHT' ($post.verdict -ceq 'PASS') 'Local postflight records PASS and proves the published registry unchanged'
        }

        # RV10 negatives for the writer-side authorization check.
        & {
            foreach ($definition in Get-FunctionDefinitions $script:PartyCWriter) { Invoke-Expression $definition }
            $cases = @('wrong-transaction', 'disclosure', 'guard-absent', 'own-drift')
            foreach ($case in $cases) {
                $parent = New-LocalParent $root ('neg-' + $case)
                $target = Join-Path $parent 'REGISTRY.json'
                $txn = 'local-neg-' + [Guid]::NewGuid().ToString('N')
                $pre = Invoke-LocalPreflight $parent 'REGISTRY' $txn $records $reservedDigest
                $useTxn = $txn
                $expected = ''
                switch ($case) {
                    'wrong-transaction' { $useTxn = 'local-other-' + [Guid]::NewGuid().ToString('N'); $expected = 'AUTHORIZATION_TRANSACTION_MISMATCH' }
                    'disclosure' {
                        $view = Get-Content -LiteralPath $pre.authorizationPath -Raw | ConvertFrom-Json
                        $view | Add-Member -NotePropertyName otherTarget -NotePropertyValue $pre.record.targets['RESPONSE']
                        [System.IO.File]::WriteAllText($pre.authorizationPath, ($view | ConvertTo-Json -Depth 6 -Compress))
                        $expected = 'AUTHORIZATION_FIELD_SET_INVALID'
                    }
                    'guard-absent' { Close-LocalPreflight $pre; $expected = 'AUTHORIZATION_GUARD_ABSENT' }
                    'own-drift' { [System.IO.File]::SetAttributes($target, [System.IO.FileAttributes]::Archive -bor [System.IO.FileAttributes]::NotContentIndexed); $expected = 'AUTHORIZATION_OWN_TARGET_DRIFT' }
                }
                $before = Get-LocalFileState $target
                try { Publish-RegistryTransaction -InputPath $inputPath -TargetPath $target -TestPolicy -LedgerPath $ledger -RequireReservation -TransactionId $useTxn -AuthorizationPath $pre.authorizationPath | Out-Null; $rejected = $false } catch { $rejected = $_.Exception.Message -like "${expected}:*" }
                $after = Get-LocalFileState $target
                Close-LocalPreflight $pre
                Add-Test ('PROBE-RV10-NEG-' + $case.ToUpperInvariant()) ($rejected -and (Format-LocalFileState $after) -ceq (Format-LocalFileState $before) -and (@(Get-ChildItem -LiteralPath $parent -Force).Count -eq 2)) "writer rejects ($expected) before any mutation"
            }

            # Postflight detects other-target drift during the guarded window.
            $parent = New-LocalParent $root 'neg-other-drift'
            $txn = 'local-drift-' + [Guid]::NewGuid().ToString('N')
            $pre = Invoke-LocalPreflight $parent 'REGISTRY' $txn $records $reservedDigest
            Publish-RegistryTransaction -InputPath $inputPath -TargetPath (Join-Path $parent 'REGISTRY.json') -TestPolicy -LedgerPath $ledger -RequireReservation -TransactionId $txn -AuthorizationPath $pre.authorizationPath | Out-Null
            [System.IO.File]::WriteAllText((Join-Path $parent 'LOOKUP_RESPONSES.jsonl'), 'concurrent drift')
            try { Invoke-LocalPostflight $pre (Get-LocalSha256Hex $inputBytes) | Out-Null; $detected = $false } catch { $detected = $_.Exception.Message -like 'LOCAL_POSTFLIGHT_OTHER_TARGET_DRIFT:*' }
            $failRecord = Get-Content -LiteralPath (Join-Path $records "postflight-$txn.json") -Raw | ConvertFrom-Json
            Add-Test 'PROBE-RV10-POSTFLIGHT-OTHER-DRIFT' ($detected -and $failRecord.verdict -ceq 'FAIL') 'postflight records FAIL when the other reservation changed'
        }

        # RV11 / RV10: Local preflight enforces the exact closed two-name set.
        $third = New-LocalParent $root 'neg-third'
        $thirdFile = Join-Path $third 'unexpected.bin'; [System.IO.File]::WriteAllText($thirdFile, 'preserve')
        try { Invoke-LocalPreflight $third 'REGISTRY' ('local-third-' + [Guid]::NewGuid().ToString('N')) $records $reservedDigest | Out-Null; $thirdRejected = $false } catch { $thirdRejected = $_.Exception.Message -like 'LOCAL_PREFLIGHT_SIBLING_SET:*' }
        $guardProbe = [System.Threading.Mutex]::new($false, (Get-LocalParentGuardName $third)); $released = $guardProbe.WaitOne(0); if ($released) { $guardProbe.ReleaseMutex() }; $guardProbe.Dispose()
        Add-Test 'PROBE-RV11-PREFLIGHT-THIRD-SIBLING' ($thirdRejected -and (Test-Path $thirdFile) -and $released) 'an unknown third sibling fails preflight, is preserved, and the guard is released'
        $missing = Join-Path $root 'neg-missing-peer'; [System.IO.Directory]::CreateDirectory($missing) | Out-Null; New-LocalReservation (Join-Path $missing 'REGISTRY.json')
        try { Invoke-LocalPreflight $missing 'REGISTRY' ('local-missing-' + [Guid]::NewGuid().ToString('N')) $records $reservedDigest | Out-Null; $missingRejected = $false } catch { $missingRejected = $_.Exception.Message -like 'LOCAL_PREFLIGHT_SIBLING_SET:*' }
        Add-Test 'PROBE-RV11-PREFLIGHT-MISSING-PEER' $missingRejected 'a parent without both reservations fails preflight'

        # RV06/RV09: a real crashed Party C writer, recovered only after termination.
        $crashParent = Join-Path $crashRoot 'source'; [System.IO.Directory]::CreateDirectory($crashParent) | Out-Null
        $crashTarget = Join-Path $crashParent 'REGISTRY.json'; New-LocalReservation $crashTarget
        $crashInput = Join-Path $crashRoot 'input.json'
        $registryVector = [Text.Encoding]::UTF8.GetBytes('{"registrySnapshotId":"issuer-registry-snapshot-test-0001","registrySnapshotVersion":1,"rows":[{"canonicalContentBytesBase64":"eyJhdXRob3JpdHkiOiJBQ0VMX0cxX0RFQ0lTSU9OX09XTkVSIiwiaXNzdWVySWRlbnRpdHkiOiJpc3N1ZXItdGVzdC0wMDEiLCJwb2xpY3lWZXJzaW9uIjoxfQ","canonicalContentHashHex":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","correctedAt":null,"entryVersion":1,"issuerAttestedHash":"db76dcc22fcec9cc566c5b449b0aaa8eabdb657d157c62cba626aba8b26d12ca","issuerIdentity":"issuer-test-001","registeredAt":"2026-09-22T00:00:00Z","revokedAt":null,"status":"ACTIVE"}],"writeTimestamp":"2026-09-22T00:00:01Z"}')
        [System.IO.File]::WriteAllBytes($crashInput, $registryVector)
        $crashLedger = Join-Path $crashRoot 'ledger/LEDGER.jsonl'
        $crashTargetBefore = Get-LocalFileState $crashTarget
        $run = [Guid]::NewGuid().ToString('N')
        $barrier = [System.Threading.EventWaitHandle]::new($false, [System.Threading.EventResetMode]::ManualReset, "Local\CVF_G4C_CRASH_$run")
        $psi = [System.Diagnostics.ProcessStartInfo]::new(); $psi.FileName = (Get-Command pwsh).Source; $psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
        foreach ($argument in @('-NoProfile','-NonInteractive','-File',$script:PartyCWriter,'-CrashMode','-CrashRunId',$run,'-CrashTargetPath',$crashTarget,'-CrashInputPath',$crashInput,'-CrashLedgerPath',$crashLedger,'-CrashPoint','AfterTempFlush')) { $psi.ArgumentList.Add($argument) }
        $crash = [System.Diagnostics.Process]::Start($psi)
        try {
            Add-Test 'PROBE-RV06-CRASH-BARRIER' ($barrier.WaitOne(30000)) 'writer child reached the post-flush crash barrier'
            $crashTxn = [string](([System.IO.File]::ReadAllLines($crashLedger)[0] | ConvertFrom-Json).transactionId)
            $residue = @(Get-ChildItem -LiteralPath $crashParent -Force -Filter '.cvf-g4-registry-*.tmp')
            & {
                foreach ($definition in Get-FunctionDefinitions $script:RecoveryScript) { Invoke-Expression $definition }
                try { Invoke-Recovery -LedgerPath $crashLedger -TransactionId $crashTxn -TestPolicy | Out-Null; $aliveRejected = $false } catch { $aliveRejected = $_.Exception.Message -like 'RECOVERY_WRITER_NOT_TERMINATED:*' }
                Add-Test 'PROBE-RV06-ALIVE-WRITER-PRESERVED' ($aliveRejected -and $residue.Count -eq 1 -and (Test-Path -LiteralPath $residue[0].FullName)) 'recovery refuses while the recorded writer instance is alive; residue preserved'
                $crash.Kill($true); $crash.WaitForExit(15000) | Out-Null
                $result = Invoke-Recovery -LedgerPath $crashLedger -TransactionId $crashTxn -TestPolicy
                Add-Test 'PROBE-RV06-RECOVERED-AFTER-TERMINATION' ($result.result -ceq 'RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED' -and -not (Test-Path -LiteralPath $residue[0].FullName) -and $result.writerTermination -like 'TERMINATED*') 'after independent termination evidence the exactly bound residue is removed'
                Add-Test 'PROBE-RV09-TARGET-EXACT' ((Format-LocalFileState (Get-LocalFileState $crashTarget)) -ceq (Format-LocalFileState $crashTargetBefore)) 'target identity, bytes, link count, attributes and complete security are unchanged by recovery'
                $phases = (@([System.IO.File]::ReadAllLines($crashLedger) | ForEach-Object { ($_ | ConvertFrom-Json).phase }) -join ',')
                Add-Test 'PROBE-RV09-LEDGER-RECOVERED' ($phases -ceq 'TEMP_PLANNED,TEMP_FLUSHED,RECOVERED') 'the crashed binding ends with a terminal RECOVERED row'
            }
            & {
                foreach ($definition in Get-FunctionDefinitions $script:PartyCWriter) { Invoke-Expression $definition }
                Publish-RegistryTransaction -InputPath $crashInput -TargetPath $crashTarget -TestPolicy -LedgerPath $crashLedger -RequireReservation | Out-Null
                Add-Test 'PROBE-RV09-CLAIMABLE-AFTER-RECOVERY' ((Get-LocalSha256Hex ([System.IO.File]::ReadAllBytes($crashTarget))) -ceq (Get-LocalSha256Hex $registryVector)) 'the reservation is claimable again after verified recovery'
            }
        } finally {
            if (-not $crash.HasExited) { $crash.Kill($true) }
            $crash.Dispose(); $barrier.Dispose()
        }

        [pscustomobject]@{
            result = 'PASS'
            tests = $script:Tests.Count
            realSourceReached = $false
            realPrincipalClaimed = $false
            harnessRole = 'LOCAL_DISPOSABLE_VERIFICATION_NOT_REVIEWER_INDEPENDENT'
        } | ConvertTo-Json -Compress
    } finally {
        foreach ($path in @($root, $crashRoot)) { if (Test-Path -LiteralPath $path) { Remove-Item -LiteralPath $path -Recurse -Force } }
    }
}

Invoke-DisposableProbe
exit 0
