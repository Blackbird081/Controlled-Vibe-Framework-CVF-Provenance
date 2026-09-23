<#
.SYNOPSIS
Distinct Administrator-only Group 4 hard-termination recovery operation
(C1-R2-05, C1-R2-06). Never an ordinary writer transaction.

.DESCRIPTION
Consumes the v2 recovery ledger that both writers append to before creating
any temp. For one named transaction it removes only temps whose complete
binding (exact schema, target/kind/path agreement, strict phase grammar,
monotonic timestamps, expected content hash, expected security digest and
recorded file identity) matches the residue exactly, and only after
independently confirming that the recorded writer process has terminated.
All mutation-sensitive checks run while holding the writer's transaction guard.
The target, the other reservation, the parent identity/security and the parent
inventory are captured before and after removal and must be invariant. Any
missing, ambiguous or contradictory evidence preserves every artifact.

Default invocation is a self-test against disposable fixtures.
#>
[CmdletBinding(DefaultParameterSetName = 'SelfTest')]
param(
    [Parameter(ParameterSetName = 'SelfTest')]
    [switch] $SelfTest,

    [Parameter(ParameterSetName = 'Recover', Mandatory = $true)]
    [switch] $ExecuteRecovery,
    [Parameter(ParameterSetName = 'Recover', Mandatory = $true)]
    [string[]] $LedgerPath,
    [Parameter(ParameterSetName = 'Recover', Mandatory = $true)]
    [string] $TransactionId,
    [Parameter(ParameterSetName = 'Recover', Mandatory = $true)]
    [string] $Confirmation
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:Confirmation = 'EXECUTE_ACEL_G1_GROUP4_ADMIN_RECOVERY_V1'
$script:ScriptPath = $PSCommandPath
$script:Tests = [System.Collections.Generic.List[object]]::new()

function Stop-Recovery([string] $Code, [string] $Message) {
    throw [System.InvalidOperationException]::new("${Code}: ${Message}")
}

function Get-CanonicalPath([string] $Path) {
    return [System.IO.Path]::GetFullPath($Path).TrimEnd([System.IO.Path]::DirectorySeparatorChar)
}

function Get-Sha256HexBytes([byte[]] $Bytes) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant() } finally { $sha.Dispose() }
}

function Get-TargetMutexName([string] $TargetPath) {
    $raw = [Text.Encoding]::UTF8.GetBytes((Get-CanonicalPath $TargetPath).ToUpperInvariant())
    $hex = Get-Sha256HexBytes $raw
    if ((Split-Path -Leaf $TargetPath) -ceq 'REGISTRY.json') { return 'Global\CVF_G4_REGISTRY_TXN_' + $hex.Substring(0, 48) }
    return 'Global\CVF_G4_RESPONSE_TXN_' + $hex.Substring(0, 48)
}

function Enter-RecoveryGuard([string] $TargetPath) {
    $created = $false
    $mutex = [System.Threading.Mutex]::new($false, (Get-TargetMutexName $TargetPath), [ref] $created)
    $acquired = $false
    try { $acquired = $mutex.WaitOne(15000) }
    catch [System.Threading.AbandonedMutexException] { $acquired = $true }
    if (-not $acquired) { $mutex.Dispose(); Stop-Recovery 'RECOVERY_GUARD_TIMEOUT' $TargetPath }
    return $mutex
}

function Exit-RecoveryGuard($Mutex) {
    if ($null -ne $Mutex) { try { $Mutex.ReleaseMutex() } finally { $Mutex.Dispose() } }
}

function Get-FileIdHex([string] $Path) {
    $output = & fsutil file queryfileid $Path 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Recovery 'RECOVERY_FILE_IDENTITY_UNAVAILABLE' $Path }
    $match = [regex]::Match(($output -join ' '), '0x[0-9a-fA-F]+')
    if (-not $match.Success) { Stop-Recovery 'RECOVERY_FILE_IDENTITY_UNAVAILABLE' $Path }
    return $match.Value.ToLowerInvariant()
}

function Get-HardLinkCount([string] $Path) {
    $output = & fsutil hardlink list $Path 2>&1
    if ($LASTEXITCODE -ne 0) { Stop-Recovery 'RECOVERY_RESIDUE_LINK_COUNT_UNAVAILABLE' $Path }
    return @($output | Where-Object { $_.Trim().Length -gt 0 }).Count
}

function Get-SecurityDigest($Security) {
    $owner = $Security.GetOwner([System.Security.Principal.SecurityIdentifier]).Value
    $tuples = @($Security.GetAccessRules($true, $true, [System.Security.Principal.SecurityIdentifier]) | ForEach-Object {
        '{0}|{1}|{2}|{3}|{4}|{5}' -f $_.IdentityReference.Value, [int]$_.FileSystemRights, [int]$_.AccessControlType, [bool]$_.IsInherited, [int]$_.InheritanceFlags, [int]$_.PropagationFlags
    })
    $text = 'owner=' + $owner + ';protected=' + ([bool]$Security.AreAccessRulesProtected).ToString() + ';aces=' + ($tuples -join "`n")
    return [pscustomobject]@{ ownerSid = $owner; protection = [bool]$Security.AreAccessRulesProtected; digest = Get-Sha256HexBytes ([Text.Encoding]::UTF8.GetBytes($text)) }
}

function Get-FileStateRecord([string] $Path) {
    $info = [System.IO.FileInfo]::new($Path)
    $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor [System.Security.AccessControl.AccessControlSections]::Access
    $security = Get-SecurityDigest ([System.IO.FileSystemAclExtensions]::GetAccessControl($info, $sections))
    return [pscustomobject]@{
        fileId = Get-FileIdHex $Path
        length = [int64]$info.Length
        sha256 = Get-Sha256HexBytes ([System.IO.File]::ReadAllBytes($Path))
        linkCount = [int](Get-HardLinkCount $Path)
        attributes = [int]$info.Attributes
        ownerSid = $security.ownerSid
        protection = $security.protection
        securityDigest = $security.digest
    }
}

function Format-FileState($State, [switch] $ExcludeFileId) {
    $fileId = if ($ExcludeFileId) { '*' } else { $State.fileId }
    return '{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}' -f $fileId, $State.length, $State.sha256, $State.linkCount, $State.attributes, $State.ownerSid, ([bool]$State.protection).ToString(), $State.securityDigest
}

function Get-DirectoryStateRecord([string] $Path) {
    $sections = [System.Security.AccessControl.AccessControlSections]::Owner -bor [System.Security.AccessControl.AccessControlSections]::Access
    $security = Get-SecurityDigest ([System.IO.FileSystemAclExtensions]::GetAccessControl([System.IO.DirectoryInfo]::new($Path), $sections))
    return [pscustomobject]@{ fileId = Get-FileIdHex $Path; securityDigest = $security.digest }
}

function Get-LedgerFieldNames {
    return @('schema','transactionId','sequence','phase','recordedAt','writerSid','writerProcessId','writerProcessStartUtcTicks','targetKind','targetName','targetPath','parentPath','parentFileId','targetPrestate','tempName','tempRole','expectedTempSha256','expectedTempSecurityDigest','tempFileId')
}

function Get-StateFieldNames {
    return @('fileId','length','sha256','linkCount','attributes','ownerSid','protection','securityDigest')
}

function Get-TempNamePattern([string] $TargetKind, [string] $Role) {
    $key = $TargetKind + '/' + $Role
    switch ($key) {
        'REGISTRY/CANDIDATE' { return '^\.cvf-g4-registry-[0-9a-f]{32}\.tmp$' }
        'REGISTRY/ROLLBACK' { return '^\.cvf-g4-registry-rollback-[0-9a-f]{32}\.tmp$' }
        'RESPONSE/CANDIDATE' { return '^\.cvf-g4-response-[0-9a-f]{32}\.tmp$' }
        'RESPONSE/CAPTURE' { return '^\.cvf-g4-capture-[0-9a-f]{32}\.tmp$' }
        'RESPONSE/ROLLBACK' { return '^\.cvf-g4-rollback-[0-9a-f]{32}\.tmp$' }
    }
    Stop-Recovery 'RECOVERY_LEDGER_ROLE_INVALID' $key
}

function Assert-LeafTempName([string] $TempName) {
    if ([string]::IsNullOrWhiteSpace($TempName)) { Stop-Recovery 'RECOVERY_LEDGER_TEMP_NAME_INVALID' '<empty>' }
    if ($TempName -match '[\\/:]' -or $TempName -eq '.' -or $TempName -eq '..') { Stop-Recovery 'RECOVERY_LEDGER_TEMP_NAME_INVALID' $TempName }
    foreach ($ch in $TempName.ToCharArray()) { if ([IO.Path]::GetInvalidFileNameChars() -contains $ch) { Stop-Recovery 'RECOVERY_LEDGER_TEMP_NAME_INVALID' $TempName } }
}

function Assert-ExactFieldSet($Object, [string[]] $Expected, [string] $Label) {
    if ($null -eq $Object -or $Object -isnot [System.Management.Automation.PSCustomObject]) { Stop-Recovery 'RECOVERY_LEDGER_ENTRY_INCOMPLETE' "${Label}: not an object" }
    $actual = (@($Object.PSObject.Properties.Name) | Sort-Object) -join ','
    $wanted = (@($Expected) | Sort-Object) -join ','
    if ($actual -cne $wanted) { Stop-Recovery 'RECOVERY_LEDGER_ENTRY_INCOMPLETE' "${Label}: fields [$actual] != [$wanted]" }
}

function Read-LedgerEntries([string[]] $LedgerPaths) {
    $entries = [System.Collections.Generic.List[object]]::new()
    foreach ($ledger in @($LedgerPaths)) {
        if (-not (Test-Path -LiteralPath $ledger -PathType Leaf)) { continue }
        foreach ($line in [System.IO.File]::ReadAllLines($ledger)) {
            if ($line.Trim().Length -eq 0) { continue }
            try { $parsed = $line | ConvertFrom-Json -DateKind String } catch { Stop-Recovery 'RECOVERY_LEDGER_ENTRY_MALFORMED' $line }
            $entries.Add([pscustomobject]@{ ledgerPath = (Get-CanonicalPath $ledger); row = $parsed; raw = $line })
        }
    }
    return @($entries.ToArray())
}

# Validates every row of one transaction against the exact v2 contract and
# returns the per-temp bindings. Anything missing, extra, ambiguous or out of
# order fails closed before any file is touched.
function Get-TransactionBinding([string[]] $LedgerPaths, [string] $TransactionId) {
    $all = @(Read-LedgerEntries $LedgerPaths)
    $entries = @($all | Where-Object { ($_.row.PSObject.Properties.Name -contains 'transactionId') -and [string]$_.row.transactionId -ceq $TransactionId })
    if ($entries.Count -eq 0) { Stop-Recovery 'RECOVERY_LEDGER_BINDING_ABSENT' $TransactionId }
    $ledgers = @($entries | ForEach-Object ledgerPath | Sort-Object -Unique)
    if ($ledgers.Count -ne 1) { Stop-Recovery 'RECOVERY_LEDGER_BINDING_AMBIGUOUS' 'transaction appears in more than one ledger' }
    $now = [DateTime]::UtcNow
    $previousTime = [DateTime]::MinValue
    $expectedSequence = 1
    foreach ($entry in $entries) {
        $row = $entry.row
        Assert-ExactFieldSet $row (Get-LedgerFieldNames) 'ledger row'
        Assert-ExactFieldSet $row.targetPrestate (Get-StateFieldNames) 'targetPrestate'
        if ([string]$row.schema -cne 'cvf.g4.recoveryLedger.v2') { Stop-Recovery 'RECOVERY_LEDGER_SCHEMA_INVALID' ([string]$row.schema) }
        if ($row.sequence -isnot [long] -and $row.sequence -isnot [int]) { Stop-Recovery 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID' 'sequence type' }
        if ([int64]$row.sequence -ne $expectedSequence) { Stop-Recovery 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID' "sequence $($row.sequence) expected $expectedSequence" }
        $expectedSequence++
        $recorded = [DateTime]::MinValue
        if ([string]$row.recordedAt -notmatch '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$' -or -not [DateTime]::TryParseExact([string]$row.recordedAt, 'yyyy-MM-ddTHH:mm:ss.fffZ', [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::AdjustToUniversal -bor [Globalization.DateTimeStyles]::AssumeUniversal, [ref] $recorded)) {
            Stop-Recovery 'RECOVERY_LEDGER_TIMESTAMP_INVALID' ([string]$row.recordedAt)
        }
        if ($recorded -gt $now.AddMinutes(5) -or $recorded -lt $previousTime) { Stop-Recovery 'RECOVERY_LEDGER_TIMESTAMP_INVALID' ([string]$row.recordedAt) }
        $previousTime = $recorded
        if ([string]$row.writerSid -notmatch '^S-1-[0-9-]+$' -or [int64]$row.writerProcessId -le 0 -or [int64]$row.writerProcessStartUtcTicks -le 0) { Stop-Recovery 'RECOVERY_LEDGER_WRITER_IDENTITY_INVALID' $TransactionId }
        $targetName = switch ([string]$row.targetKind) { 'REGISTRY' { 'REGISTRY.json' } 'RESPONSE' { 'LOOKUP_RESPONSES.jsonl' } default { $null } }
        if ($null -eq $targetName) { Stop-Recovery 'RECOVERY_LEDGER_TARGET_MISMATCH' ([string]$row.targetKind) }
        $targetPath = [string]$row.targetPath
        if (-not [IO.Path]::IsPathFullyQualified($targetPath) -or (Get-CanonicalPath $targetPath) -cne $targetPath) { Stop-Recovery 'RECOVERY_LEDGER_TARGET_MISMATCH' $targetPath }
        if ([string]$row.targetName -cne $targetName -or (Split-Path -Leaf $targetPath) -cne $targetName) { Stop-Recovery 'RECOVERY_LEDGER_TARGET_MISMATCH' ([string]$row.targetName) }
        if ([string]$row.parentPath -cne (Get-CanonicalPath (Split-Path -Parent $targetPath))) { Stop-Recovery 'RECOVERY_LEDGER_TARGET_MISMATCH' ([string]$row.parentPath) }
        if ([string]$row.parentFileId -notmatch '^0x[0-9a-f]+$' -or [string]$row.targetPrestate.fileId -notmatch '^0x[0-9a-f]+$') { Stop-Recovery 'RECOVERY_LEDGER_IDENTITY_INVALID' $TransactionId }
        foreach ($hash in @([string]$row.expectedTempSha256, [string]$row.expectedTempSecurityDigest, [string]$row.targetPrestate.sha256, [string]$row.targetPrestate.securityDigest)) {
            if ($hash -notmatch '^[0-9a-f]{64}$') { Stop-Recovery 'RECOVERY_LEDGER_HASH_INVALID' $TransactionId }
        }
        Assert-LeafTempName ([string]$row.tempName)
        if ([string]$row.tempName -notmatch (Get-TempNamePattern ([string]$row.targetKind) ([string]$row.tempRole))) { Stop-Recovery 'RECOVERY_LEDGER_TEMP_NAME_INVALID' ([string]$row.tempName) }
        if ($null -ne $row.tempFileId -and [string]$row.tempFileId -notmatch '^0x[0-9a-f]+$') { Stop-Recovery 'RECOVERY_LEDGER_IDENTITY_INVALID' 'tempFileId' }
    }
    $constantFields = @('writerSid','writerProcessId','writerProcessStartUtcTicks','targetKind','targetName','targetPath','parentPath','parentFileId')
    $first = $entries[0].row
    foreach ($entry in $entries) {
        foreach ($field in $constantFields) { if ([string]$entry.row.$field -cne [string]$first.$field) { Stop-Recovery 'RECOVERY_LEDGER_BINDING_AMBIGUOUS' $field } }
        if ((Format-FileState $entry.row.targetPrestate) -cne (Format-FileState $first.targetPrestate)) { Stop-Recovery 'RECOVERY_LEDGER_BINDING_AMBIGUOUS' 'targetPrestate' }
    }
    $temps = [ordered]@{}
    foreach ($entry in $entries) {
        $name = [string]$entry.row.tempName
        if (-not $temps.Contains($name)) { $temps[$name] = [System.Collections.Generic.List[object]]::new() }
        $temps[$name].Add($entry.row)
    }
    $bindings = [System.Collections.Generic.List[object]]::new()
    foreach ($name in $temps.Keys) {
        $rows = @($temps[$name])
        foreach ($field in @('tempRole','expectedTempSha256','expectedTempSecurityDigest')) {
            if (@($rows | ForEach-Object { [string]$_.$field } | Sort-Object -Unique).Count -ne 1) { Stop-Recovery 'RECOVERY_LEDGER_BINDING_AMBIGUOUS' "$name $field" }
        }
        $role = [string]$rows[0].tempRole
        $phases = (@($rows | ForEach-Object { [string]$_.phase }) -join ',')
        $valid = ($phases -match '^TEMP_PLANNED(,TEMP_FLUSHED)?(,(DISCARDED|RECOVERED))?$') -or
            ($role -cne 'CAPTURE' -and $phases -match '^TEMP_PLANNED,TEMP_FLUSHED,PRE_MOVE(,(PUBLISHED|DISCARDED|RECOVERED))?$') -or
            ($role -ceq 'CAPTURE' -and $phases -ceq 'TEMP_PLANNED,TEMP_FLUSHED,RELEASED')
        if (-not $valid) { Stop-Recovery 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID' "$name $phases" }
        if ($null -ne $rows[0].tempFileId) { Stop-Recovery 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID' "$name tempFileId recorded before creation" }
        $fileIds = @($rows | Where-Object { $null -ne $_.tempFileId } | ForEach-Object { [string]$_.tempFileId } | Sort-Object -Unique)
        if ($fileIds.Count -gt 1) { Stop-Recovery 'RECOVERY_LEDGER_BINDING_AMBIGUOUS' "$name tempFileId" }
        if ($phases -match 'TEMP_FLUSHED' -and $fileIds.Count -ne 1) { Stop-Recovery 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID' "$name flushed without identity" }
        $bindings.Add([pscustomobject]@{
            tempName = $name; role = $role; phases = $phases; lastPhase = [string]$rows[-1].phase
            expectedSha256 = [string]$rows[0].expectedTempSha256; expectedSecurityDigest = [string]$rows[0].expectedTempSecurityDigest
            tempFileId = if ($fileIds.Count -eq 1) { $fileIds[0] } else { $null }
        })
    }
    return [pscustomobject]@{
        transactionId = $TransactionId; ledgerPath = $ledgers[0]; lastSequence = $expectedSequence - 1; lastTime = $previousTime
        first = $first; targetPath = [string]$first.targetPath; parentPath = [string]$first.parentPath; parentFileId = [string]$first.parentFileId
        targetKind = [string]$first.targetKind; prestate = $first.targetPrestate
        writerProcessId = [int]$first.writerProcessId; writerProcessStartUtcTicks = [int64]$first.writerProcessStartUtcTicks
        temps = @($bindings.ToArray()); allEntries = $all
    }
}

# Independently checkable termination evidence: the exact recorded process
# instance (PID plus start time) must no longer exist.
function Assert-WriterTerminated([int] $ProcessId, [int64] $StartTicks) {
    $process = $null
    try { $process = [System.Diagnostics.Process]::GetProcessById($ProcessId) } catch [System.ArgumentException] { return 'TERMINATED' }
    try {
        try { $ticks = [int64]$process.StartTime.ToUniversalTime().Ticks } catch { Stop-Recovery 'RECOVERY_WRITER_TERMINATION_UNVERIFIABLE' "pid $ProcessId" }
        if ($ticks -eq $StartTicks) { Stop-Recovery 'RECOVERY_WRITER_NOT_TERMINATED' "pid $ProcessId is still running" }
        return 'TERMINATED_PID_REUSED'
    } finally { $process.Dispose() }
}

function Get-OtherReservationPath([string] $TargetPath) {
    $other = if ((Split-Path -Leaf $TargetPath) -ceq 'REGISTRY.json') { 'LOOKUP_RESPONSES.jsonl' } else { 'REGISTRY.json' }
    return Join-Path (Split-Path -Parent $TargetPath) $other
}

function Get-ParentInventory([string] $ParentPath) {
    return @(Get-ChildItem -LiteralPath $ParentPath -Force | ForEach-Object {
        [pscustomobject]@{ name = $_.Name; isContainer = [bool]$_.PSIsContainer; isReparse = [bool]($_.Attributes -band [IO.FileAttributes]::ReparsePoint) }
    })
}

function Invoke-Recovery([string[]] $LedgerPath, [string] $TransactionId, [switch] $TestPolicy) {
    $binding = Get-TransactionBinding $LedgerPath $TransactionId
    $candidates = @($binding.temps | Where-Object { @('TEMP_PLANNED','TEMP_FLUSHED','PRE_MOVE') -contains $_.lastPhase })
    if ($candidates.Count -eq 0) {
        if (@($binding.temps | Where-Object { $_.phases -match 'PUBLISHED' }).Count -gt 0) { Stop-Recovery 'RECOVERY_TRANSACTION_ALREADY_PUBLISHED' $TransactionId }
        Stop-Recovery 'RECOVERY_NOTHING_TO_RECOVER' $TransactionId
    }
    $termination = Assert-WriterTerminated $binding.writerProcessId $binding.writerProcessStartUtcTicks
    $parentPrefix = $binding.parentPath + [IO.Path]::DirectorySeparatorChar
    foreach ($candidate in $candidates) {
        $candidatePath = Get-CanonicalPath (Join-Path $binding.parentPath $candidate.tempName)
        if (-not $candidatePath.StartsWith($parentPrefix, [StringComparison]::OrdinalIgnoreCase)) { Stop-Recovery 'RECOVERY_RESIDUE_CONTAINMENT_VIOLATION' $candidatePath }
    }
    # Every other transaction ID appearing anywhere in the provided ledgers
    # must be independently validated by the exact same schema/identity/hash/
    # phase-sequence/ambiguity contract as the primary transaction before any
    # of its temp names can be recognized as known residue. A malformed,
    # incomplete, contradictory or ambiguous other-transaction row must never
    # whitelist a sibling; it must fail the whole recovery closed instead of
    # being silently skipped, because an attacker-controlled malformed row is
    # exactly the case this validation exists to catch.
    $otherTransactionIds = @($binding.allEntries | Where-Object { ($_.row.PSObject.Properties.Name -contains 'transactionId') -and [string]$_.row.transactionId -cne $TransactionId } | ForEach-Object { [string]$_.row.transactionId } | Sort-Object -Unique)
    $otherBound = [System.Collections.Generic.List[string]]::new()
    foreach ($otherId in $otherTransactionIds) {
        $otherBinding = Get-TransactionBinding $LedgerPath $otherId
        foreach ($otherTemp in @($otherBinding.temps | Where-Object { @('TEMP_PLANNED','TEMP_FLUSHED','PRE_MOVE') -contains $_.lastPhase })) {
            $otherBound.Add($otherTemp.tempName)
        }
    }
    $otherBound = @($otherBound | Sort-Object -Unique)
    $guard = Enter-RecoveryGuard $binding.targetPath
    try {
        if (-not (Test-Path -LiteralPath $binding.parentPath -PathType Container)) { Stop-Recovery 'RECOVERY_PARENT_MISMATCH' $binding.parentPath }
        if ((Get-Item -LiteralPath $binding.parentPath -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) { Stop-Recovery 'RECOVERY_PARENT_MISMATCH' 'reparse parent' }
        $parentBefore = Get-DirectoryStateRecord $binding.parentPath
        if ($parentBefore.fileId -cne $binding.parentFileId) { Stop-Recovery 'RECOVERY_PARENT_MISMATCH' $binding.parentPath }
        $reservations = @('REGISTRY.json', 'LOOKUP_RESPONSES.jsonl')
        $candidateNames = @($candidates | ForEach-Object tempName)
        foreach ($item in @(Get-ParentInventory $binding.parentPath)) {
            if ($item.isReparse) { Stop-Recovery 'RECOVERY_UNKNOWN_SIBLING' $item.name }
            if ($reservations -ccontains $item.name -and -not $item.isContainer) { continue }
            if ($candidateNames -ccontains $item.name -or $otherBound -ccontains $item.name) { continue }
            Stop-Recovery 'RECOVERY_UNKNOWN_SIBLING' $item.name
        }
        if (-not (Test-Path -LiteralPath $binding.targetPath -PathType Leaf)) { Stop-Recovery 'RECOVERY_TARGET_STATE_INDETERMINATE' 'target missing' }
        $targetBefore = Get-FileStateRecord $binding.targetPath
        $otherPath = Get-OtherReservationPath $binding.targetPath
        $otherBefore = if (Test-Path -LiteralPath $otherPath -PathType Leaf) { Get-FileStateRecord $otherPath } else { $null }
        # Acceptable target states: exact prestate (including identity) when
        # nothing was published, or the exact poststate of a published temp.
        $published = @($binding.temps | Where-Object { $_.phases -match 'PUBLISHED' })
        $targetMatches = if ($published.Count -eq 0) { (Format-FileState $targetBefore) -ceq (Format-FileState $binding.prestate) } else { $false }
        foreach ($temp in @($published + @($candidates | Where-Object lastPhase -ceq 'PRE_MOVE'))) {
            if ($targetBefore.fileId -ceq $temp.tempFileId -and $targetBefore.sha256 -ceq $temp.expectedSha256 -and $targetBefore.securityDigest -ceq $temp.expectedSecurityDigest -and $targetBefore.linkCount -eq 1) { $targetMatches = $true }
        }
        if (-not $targetMatches) { Stop-Recovery 'RECOVERY_TARGET_STATE_INDETERMINATE' $binding.targetPath }
        $removals = [System.Collections.Generic.List[string]]::new()
        foreach ($candidate in $candidates) {
            $path = Join-Path $binding.parentPath $candidate.tempName
            if (-not (Test-Path -LiteralPath $path)) {
                if ($candidate.lastPhase -ceq 'TEMP_FLUSHED') { Stop-Recovery 'RECOVERY_TARGET_STATE_INDETERMINATE' "flushed temp vanished: $($candidate.tempName)" }
                if ($candidate.lastPhase -ceq 'PRE_MOVE' -and $targetBefore.fileId -cne $candidate.tempFileId) { Stop-Recovery 'RECOVERY_TARGET_STATE_INDETERMINATE' "pre-move temp vanished without publication: $($candidate.tempName)" }
                continue
            }
            $item = Get-Item -LiteralPath $path -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { Stop-Recovery 'RECOVERY_RESIDUE_REPARSE_POINT' $path }
            if ($item.PSIsContainer) { Stop-Recovery 'RECOVERY_RESIDUE_NOT_A_FILE' $path }
            $residue = Get-FileStateRecord $path
            if ($residue.linkCount -ne 1) { Stop-Recovery 'RECOVERY_RESIDUE_LINK_COUNT_MISMATCH' $path }
            if ($null -ne $candidate.tempFileId -and $residue.fileId -cne $candidate.tempFileId) { Stop-Recovery 'RECOVERY_RESIDUE_IDENTITY_MISMATCH' $path }
            if ($residue.sha256 -cne $candidate.expectedSha256) { Stop-Recovery 'RECOVERY_RESIDUE_CONTENT_MISMATCH' $path }
            if ($residue.securityDigest -cne $candidate.expectedSecurityDigest) { Stop-Recovery 'RECOVERY_RESIDUE_SECURITY_MISMATCH' $path }
            if ($candidate.lastPhase -ceq 'PRE_MOVE' -and $published.Count -eq 0 -and (Format-FileState $targetBefore) -cne (Format-FileState $binding.prestate)) { Stop-Recovery 'RECOVERY_TARGET_STATE_INDETERMINATE' $binding.targetPath }
            $removals.Add($path)
        }
        foreach ($path in $removals) { Remove-Item -LiteralPath $path -Force }
        # Postflight: exact invariance of target, other reservation and parent;
        # no removed residue remains.
        $targetAfter = Get-FileStateRecord $binding.targetPath
        if ((Format-FileState $targetAfter) -cne (Format-FileState $targetBefore)) { Stop-Recovery 'RECOVERY_NON_TARGET_STATE_CHANGED' $binding.targetPath }
        $otherAfter = if (Test-Path -LiteralPath $otherPath -PathType Leaf) { Get-FileStateRecord $otherPath } else { $null }
        if (($null -eq $otherBefore) -ne ($null -eq $otherAfter) -or ($null -ne $otherBefore -and (Format-FileState $otherAfter) -cne (Format-FileState $otherBefore))) { Stop-Recovery 'RECOVERY_NON_TARGET_STATE_CHANGED' $otherPath }
        $parentAfter = Get-DirectoryStateRecord $binding.parentPath
        if ($parentAfter.fileId -cne $parentBefore.fileId -or $parentAfter.securityDigest -cne $parentBefore.securityDigest) { Stop-Recovery 'RECOVERY_NON_TARGET_STATE_CHANGED' $binding.parentPath }
        $inventoryAfter = @(Get-ParentInventory $binding.parentPath | ForEach-Object name)
        foreach ($name in $candidateNames) { if ($inventoryAfter -ccontains $name) { Stop-Recovery 'RECOVERY_POSTSTATE_RESIDUE_REMAINS' $name } }
        # Terminal RECOVERED rows reuse the exact binding so a rerun sees no candidate.
        $sequence = $binding.lastSequence
        foreach ($candidate in $candidates) {
            $sequence++
            $timestamp = [DateTime]::UtcNow; if ($timestamp -lt $binding.lastTime) { $timestamp = $binding.lastTime }
            $row = [ordered]@{}
            foreach ($field in Get-LedgerFieldNames) { $row[$field] = $binding.first.$field }
            $row.sequence = $sequence; $row.phase = 'RECOVERED'; $row.recordedAt = $timestamp.ToString('yyyy-MM-ddTHH:mm:ss.fffZ')
            $row.tempName = $candidate.tempName; $row.tempRole = $candidate.role; $row.expectedTempSha256 = $candidate.expectedSha256
            $row.expectedTempSecurityDigest = $candidate.expectedSecurityDigest; $row.tempFileId = $candidate.tempFileId
            [System.IO.File]::AppendAllText($binding.ledgerPath, (($row | ConvertTo-Json -Compress -Depth 6) + "`n"))
        }
        return [pscustomobject]@{
            result = if ($removals.Count -gt 0) { 'RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED' } else { 'RECOVERY_NO_RESIDUE_FOUND' }
            transactionId = $TransactionId
            writerTermination = $termination
            removed = @($removals.ToArray())
            targetPoststate = $targetAfter
            otherReservationPoststate = $otherAfter
            parentPoststate = $parentAfter
            inventory = $inventoryAfter
        }
    } finally { Exit-RecoveryGuard $guard }
}

function Add-Test([string] $Id, [bool] $Passed, [string] $Detail) {
    $script:Tests.Add([pscustomobject]@{ id = $Id; passed = $Passed; detail = $Detail })
    if (-not $Passed) { Stop-Recovery 'SELF_TEST_FAILED' "${Id}: ${Detail}" }
}

function New-FixtureHardenedTemp([string] $Path, [string] $OwnerSid, [byte[]] $Bytes) {
    [System.IO.File]::WriteAllBytes($Path, $Bytes)
    $security = [System.Security.AccessControl.FileSecurity]::new()
    $security.SetAccessRuleProtection($true, $false)
    $security.SetOwner([System.Security.Principal.SecurityIdentifier]::new($OwnerSid))
    $security.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
        [System.Security.Principal.SecurityIdentifier]::new($OwnerSid),
        [System.Security.AccessControl.FileSystemRights]::FullControl,
        [System.Security.AccessControl.AccessControlType]::Allow))
    [System.IO.FileSystemAclExtensions]::SetAccessControl([System.IO.FileInfo]::new($Path), $security)
}

function Get-TerminatedWriterIdentity {
    $process = Start-Process -FilePath (Get-Command pwsh).Source -ArgumentList '-NoProfile','-NonInteractive','-Command','exit 0' -PassThru -WindowStyle Hidden
    $process.WaitForExit()
    return [pscustomobject]@{ processId = [int]$process.Id; startTicks = [int64]$process.StartTime.ToUniversalTime().Ticks }
}

# Builds a realistic crashed-writer fixture: reserved target, hardened temp
# residue, and a v2 ledger whose binding matches both exactly.
function New-RecoveryFixture([string] $Root, [string] $Name, $Writer, [switch] $WithOtherReservation, [string[]] $Phases = @('TEMP_PLANNED','TEMP_FLUSHED')) {
    $parent = Join-Path $Root $Name
    [System.IO.Directory]::CreateDirectory($parent) | Out-Null
    $currentSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    $target = Join-Path $parent 'REGISTRY.json'
    New-FixtureHardenedTemp $target $currentSid ([byte[]]::new(0))
    if ($WithOtherReservation) { [System.IO.File]::WriteAllBytes((Join-Path $parent 'LOOKUP_RESPONSES.jsonl'), [byte[]]::new(0)) }
    $tempName = '.cvf-g4-registry-' + [Guid]::NewGuid().ToString('N') + '.tmp'
    $tempPath = Join-Path $parent $tempName
    $bytes = [Text.Encoding]::UTF8.GetBytes('{"fixture":"candidate registry bytes"}')
    New-FixtureHardenedTemp $tempPath $currentSid $bytes
    $tempState = Get-FileStateRecord $tempPath
    $ledger = Join-Path $Root ($Name + '.ledger.jsonl')
    $transactionId = 'fixture-' + [Guid]::NewGuid().ToString('N')
    $prestate = Get-FileStateRecord $target
    $sequence = 0
    foreach ($phase in $Phases) {
        $sequence++
        $row = [ordered]@{
            schema = 'cvf.g4.recoveryLedger.v2'; transactionId = $transactionId; sequence = $sequence; phase = $phase
            recordedAt = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ss.fffZ'); writerSid = $currentSid
            writerProcessId = $Writer.processId; writerProcessStartUtcTicks = $Writer.startTicks
            targetKind = 'REGISTRY'; targetName = 'REGISTRY.json'; targetPath = Get-CanonicalPath $target
            parentPath = Get-CanonicalPath $parent; parentFileId = Get-FileIdHex $parent
            targetPrestate = [ordered]@{ fileId = $prestate.fileId; length = $prestate.length; sha256 = $prestate.sha256; linkCount = $prestate.linkCount; attributes = $prestate.attributes; ownerSid = $prestate.ownerSid; protection = $prestate.protection; securityDigest = $prestate.securityDigest }
            tempName = $tempName; tempRole = 'CANDIDATE'; expectedTempSha256 = $tempState.sha256; expectedTempSecurityDigest = $tempState.securityDigest
            tempFileId = if ($phase -ceq 'TEMP_PLANNED') { $null } else { $tempState.fileId }
        }
        [System.IO.File]::AppendAllText($ledger, (($row | ConvertTo-Json -Compress -Depth 6) + "`n"))
    }
    return [pscustomobject]@{ parent = $parent; target = $target; temp = $tempPath; tempName = $tempName; ledger = $ledger; transactionId = $transactionId; bytes = $bytes }
}

function Set-FixtureLedgerField($Fixture, [int] $RowIndex, [string] $Field, $Value) {
    $lines = @([System.IO.File]::ReadAllLines($Fixture.ledger))
    $row = $lines[$RowIndex] | ConvertFrom-Json -DateKind String
    if ($Field -ceq '<remove>') { $row.PSObject.Properties.Remove($Value) } elseif ($row.PSObject.Properties.Name -contains $Field) { $row.$Field = $Value } else { $row | Add-Member -NotePropertyName $Field -NotePropertyValue $Value }
    $lines[$RowIndex] = $row | ConvertTo-Json -Compress -Depth 6
    [System.IO.File]::WriteAllLines($Fixture.ledger, $lines)
}

function Test-RecoveryRejected($Fixture, [string] $ExpectedCode, [string[]] $Ledgers) {
    if (-not $Ledgers) { $Ledgers = @($Fixture.ledger) }
    try { Invoke-Recovery -LedgerPath $Ledgers -TransactionId $Fixture.transactionId -TestPolicy | Out-Null; return $false }
    catch { $message = $_.Exception.Message; $ok = ($message -like "${ExpectedCode}:*") -and (Test-Path -LiteralPath $Fixture.temp); return $ok }
}

function Invoke-SelfTest {
    $root = Join-Path ([IO.Path]::GetTempPath()) ('cvf-g4-recovery-' + [Guid]::NewGuid().ToString('N'))
    [System.IO.Directory]::CreateDirectory($root) | Out-Null
    try {
        $dead = Get-TerminatedWriterIdentity
        $currentSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value

        # Positive: exact binding, terminated writer, exact residue.
        $fixture = New-RecoveryFixture $root 'positive' $dead -WithOtherReservation
        $otherBefore = Get-FileStateRecord (Join-Path $fixture.parent 'LOOKUP_RESPONSES.jsonl')
        $targetBefore = Get-FileStateRecord $fixture.target
        $result = Invoke-Recovery -LedgerPath $fixture.ledger -TransactionId $fixture.transactionId -TestPolicy
        Add-Test 'RECOVERY-01-REMOVED' ($result.result -ceq 'RECOVERY_RESIDUE_REMOVED_LEDGER_VERIFIED' -and -not (Test-Path $fixture.temp)) 'exactly bound residue of a terminated writer is removed'
        Add-Test 'RECOVERY-01-TARGET-EXACT' ((Format-FileState $result.targetPoststate) -ceq (Format-FileState $targetBefore)) 'target poststate equals prestate in identity, bytes, link count, attributes and complete security digest'
        Add-Test 'RECOVERY-01-OTHER-EXACT' ((Format-FileState $result.otherReservationPoststate) -ceq (Format-FileState $otherBefore)) 'other reservation is invariant'
        Add-Test 'RECOVERY-01-INVENTORY' ((@($result.inventory | Sort-Object) -join ',') -ceq 'LOOKUP_RESPONSES.jsonl,REGISTRY.json') 'final parent inventory is exactly the two reservations'
        $recoveredPhases = (@([System.IO.File]::ReadAllLines($fixture.ledger) | ForEach-Object { ($_ | ConvertFrom-Json).phase }) -join ',')
        Add-Test 'RECOVERY-01-RECORDED' ($recoveredPhases -ceq 'TEMP_PLANNED,TEMP_FLUSHED,RECOVERED') 'recovery appends a terminal RECOVERED row with the same binding'
        try { Invoke-Recovery -LedgerPath $fixture.ledger -TransactionId $fixture.transactionId -TestPolicy | Out-Null; $rerun = $false } catch { $rerun = $_.Exception.Message -like 'RECOVERY_NOTHING_TO_RECOVER:*' }
        Add-Test 'RECOVERY-01-IDEMPOTENT' $rerun 'a recovered transaction is not recovered again'

        $f = New-RecoveryFixture $root 'absent-binding' $dead
        try { Invoke-Recovery -LedgerPath $f.ledger -TransactionId 'absent-txn' -TestPolicy | Out-Null; $ok = $false } catch { $ok = ($_.Exception.Message -like 'RECOVERY_LEDGER_BINDING_ABSENT:*') -and (Test-Path $f.temp) }
        Add-Test 'RECOVERY-02-ABSENT-REJECTED' $ok 'no binding: artifact preserved'

        $f = New-RecoveryFixture $root 'wrong-schema' $dead; Set-FixtureLedgerField $f 0 'schema' 'untrusted.noncontract.schema'
        Add-Test 'RECOVERY-03-WRONG-SCHEMA' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_SCHEMA_INVALID') 'non-contract schema rejected; residue preserved'

        $f = New-RecoveryFixture $root 'target-name' $dead; Set-FixtureLedgerField $f 0 'targetName' 'WRONG_TARGET.json'
        Add-Test 'RECOVERY-04-TARGETNAME-MISMATCH' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_TARGET_MISMATCH') 'targetName disagreeing with target path leaf/kind rejected'

        $f = New-RecoveryFixture $root 'timestamp' $dead; Set-FixtureLedgerField $f 0 'recordedAt' 'not-a-timestamp'
        Add-Test 'RECOVERY-05-TIMESTAMP' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_TIMESTAMP_INVALID') 'invalid timestamp rejected'

        $f = New-RecoveryFixture $root 'phase-order' $dead -Phases @('TEMP_FLUSHED','TEMP_PLANNED')
        Add-Test 'RECOVERY-06-PHASE-SEQUENCE' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID') 'out-of-order phase grammar rejected'

        $f = New-RecoveryFixture $root 'sequence-gap' $dead; Set-FixtureLedgerField $f 1 'sequence' 5
        Add-Test 'RECOVERY-06-SEQUENCE-GAP' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID') 'non-contiguous sequence rejected'

        $alive = [pscustomobject]@{ processId = $PID; startTicks = [int64][System.Diagnostics.Process]::GetCurrentProcess().StartTime.ToUniversalTime().Ticks }
        $f = New-RecoveryFixture $root 'alive-writer' $alive
        Add-Test 'RECOVERY-07-WRITER-ALIVE' (Test-RecoveryRejected $f 'RECOVERY_WRITER_NOT_TERMINATED') 'a running writer instance blocks cleanup; residue preserved'

        $f = New-RecoveryFixture $root 'content' $dead; [System.IO.File]::AppendAllText($f.temp, 'tampered')
        Add-Test 'RECOVERY-08-CONTENT-MISMATCH' (Test-RecoveryRejected $f 'RECOVERY_RESIDUE_CONTENT_MISMATCH') 'residue bytes differing from the bound hash are preserved'

        $f = New-RecoveryFixture $root 'ace' $dead
        $sec = [System.IO.FileSystemAclExtensions]::GetAccessControl([System.IO.FileInfo]::new($f.temp))
        $sec.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new([System.Security.Principal.SecurityIdentifier]::new('S-1-5-18'), [System.Security.AccessControl.FileSystemRights]::Read, [System.Security.AccessControl.AccessControlType]::Allow))
        [System.IO.FileSystemAclExtensions]::SetAccessControl([System.IO.FileInfo]::new($f.temp), $sec)
        Add-Test 'RECOVERY-09-COMPLETE-ACE-MISMATCH' (Test-RecoveryRejected $f 'RECOVERY_RESIDUE_SECURITY_MISMATCH') 'same owner and protection but an extra ACE is rejected by the complete security digest'

        $f = New-RecoveryFixture $root 'target-drift' $dead; [System.IO.File]::WriteAllText($f.target, 'drift')
        Add-Test 'RECOVERY-10-TARGET-DRIFT' (Test-RecoveryRejected $f 'RECOVERY_TARGET_STATE_INDETERMINATE') 'target differing from the bound prestate blocks cleanup'

        $f = New-RecoveryFixture $root 'tempname-change' $dead; Set-FixtureLedgerField $f 1 'tempName' ('.cvf-g4-registry-' + [Guid]::NewGuid().ToString('N') + '.tmp')
        Add-Test 'RECOVERY-11-TEMPNAME-CHANGED' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_PHASE_SEQUENCE_INVALID') 'a temp name changing across phases breaks the phase grammar and is rejected'

        $f = New-RecoveryFixture $root 'tempname-empty' $dead; Set-FixtureLedgerField $f 1 'tempName' ''
        Add-Test 'RECOVERY-11-TEMPNAME-EMPTY' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_TEMP_NAME_INVALID') 'an empty temp name is rejected'

        $f = New-RecoveryFixture $root 'traversal' $dead; Set-FixtureLedgerField $f 0 'tempName' '../outside/.cvf-g4-registry-review.tmp'
        Add-Test 'RECOVERY-12-TRAVERSAL' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_TEMP_NAME_INVALID') 'traversal temp name rejected before path resolution'

        $f = New-RecoveryFixture $root 'missing-field' $dead; Set-FixtureLedgerField $f 0 '<remove>' 'writerProcessId'
        Add-Test 'RECOVERY-13-MISSING-FIELD' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_ENTRY_INCOMPLETE') 'missing termination-evidence field rejected'

        $f = New-RecoveryFixture $root 'extra-field' $dead; Set-FixtureLedgerField $f 0 'unexpected' 'x'
        Add-Test 'RECOVERY-13-EXTRA-FIELD' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_ENTRY_INCOMPLETE') 'unknown extra field rejected'

        $f = New-RecoveryFixture $root 'published' $dead -Phases @('TEMP_PLANNED','TEMP_FLUSHED','PRE_MOVE','PUBLISHED')
        Add-Test 'RECOVERY-14-PUBLISHED' (Test-RecoveryRejected $f 'RECOVERY_TRANSACTION_ALREADY_PUBLISHED') 'a published transaction is not a recovery candidate'

        $f = New-RecoveryFixture $root 'unknown-sibling' $dead; $third = Join-Path $f.parent 'unexpected.bin'; [System.IO.File]::WriteAllText($third, 'preserve')
        Add-Test 'RECOVERY-15-UNKNOWN-SIBLING' ((Test-RecoveryRejected $f 'RECOVERY_UNKNOWN_SIBLING') -and (Test-Path $third)) 'an unknown sibling blocks cleanup; both are preserved'

        $f = New-RecoveryFixture $root 'hardlink' $dead
        $linked = $true; try { New-Item -ItemType HardLink -Path (Join-Path $root 'hardlink-second-name.tmp') -Target $f.temp -ErrorAction Stop | Out-Null } catch { $linked = $false }
        Add-Test 'RECOVERY-16-HARDLINK' ((-not $linked) -or (Test-RecoveryRejected $f 'RECOVERY_RESIDUE_LINK_COUNT_MISMATCH')) 'hardlinked residue is rejected'

        $f = New-RecoveryFixture $root 'identity' $dead
        Remove-Item -LiteralPath $f.temp -Force; New-FixtureHardenedTemp $f.temp $currentSid $f.bytes
        Add-Test 'RECOVERY-17-IDENTITY-MISMATCH' (Test-RecoveryRejected $f 'RECOVERY_RESIDUE_IDENTITY_MISMATCH') 'a same-named, same-content replacement with a different file identity is preserved'

        $f = New-RecoveryFixture $root 'complete-but-unbound' $dead
        $unbound = [ordered]@{ schema='untrusted.noncontract.schema'; transactionId=$f.transactionId; writerSid=$currentSid; targetName='WRONG_TARGET.json'; targetPath=$f.target; tempName=$f.tempName; phase='TEMP_PLANNED'; recordedAt='not-a-timestamp' }
        [System.IO.File]::WriteAllText($f.ledger, (($unbound | ConvertTo-Json -Compress) + "`n"))
        Add-Test 'RECOVERY-18-COMPLETE-BUT-UNBOUND' (Test-RecoveryRejected $f 'RECOVERY_LEDGER_ENTRY_INCOMPLETE') 'a syntactically complete but semantically unbound row never authorizes deletion'

        # RV12: a malformed row for a DIFFERENT transaction ID must never
        # whitelist an unknown sibling during recovery of a valid primary
        # transaction. The primary transaction's own residue, the unrelated
        # unknown sibling, the target, the other reservation and the parent
        # must all be preserved unchanged, and no RECOVERED row may be
        # appended for either transaction.
        $f = New-RecoveryFixture $root 'malformed-other-binding' $dead -WithOtherReservation
        $unknown = Join-Path $f.parent 'unexpected.bin'; [System.IO.File]::WriteAllText($unknown, 'reviewer unknown sibling')
        $otherRow = [ordered]@{ transactionId = 'unvalidated-other-transaction'; tempName = 'unexpected.bin' }
        [System.IO.File]::AppendAllText($f.ledger, (($otherRow | ConvertTo-Json -Compress) + "`n"))
        $targetBefore = Get-FileStateRecord $f.target
        $otherReservationBefore = Get-FileStateRecord (Join-Path $f.parent 'LOOKUP_RESPONSES.jsonl')
        $parentBefore = Get-DirectoryStateRecord $f.parent
        try { Invoke-Recovery -LedgerPath $f.ledger -TransactionId $f.transactionId -TestPolicy | Out-Null; $rejected = $false } catch { $rejected = $_.Exception.Message -like 'RECOVERY_LEDGER_ENTRY_INCOMPLETE:*' }
        $primaryPreserved = Test-Path -LiteralPath $f.temp
        $unknownPreserved = Test-Path -LiteralPath $unknown
        $targetUnchanged = (Format-FileState (Get-FileStateRecord $f.target)) -ceq (Format-FileState $targetBefore)
        $otherReservationUnchanged = (Format-FileState (Get-FileStateRecord (Join-Path $f.parent 'LOOKUP_RESPONSES.jsonl'))) -ceq (Format-FileState $otherReservationBefore)
        $parentAfter = Get-DirectoryStateRecord $f.parent
        $parentUnchanged = $parentAfter.fileId -ceq $parentBefore.fileId -and $parentAfter.securityDigest -ceq $parentBefore.securityDigest
        $noRecovered = -not (@([System.IO.File]::ReadAllLines($f.ledger) | ForEach-Object { $parsed = $_ | ConvertFrom-Json; if ($parsed.PSObject.Properties.Name -contains 'phase') { [string]$parsed.phase } }) -contains 'RECOVERED')
        Add-Test 'RECOVERY-19-MALFORMED-OTHER-BINDING' ($rejected -and $primaryPreserved -and $unknownPreserved -and $targetUnchanged -and $otherReservationUnchanged -and $parentUnchanged -and $noRecovered) 'a malformed other-transaction row fails recovery closed instead of whitelisting its named sibling; primary residue, unknown sibling, target, other reservation and parent are all preserved, and no RECOVERED row is appended'

        Add-Test 'RECOVERY-20-DEFAULT' ($PSCmdlet.ParameterSetName -eq 'SelfTest') 'default mode is self-test'
        [pscustomobject]@{ result='PASS'; tests=$script:Tests.Count; sourceMutation=$false } | ConvertTo-Json -Compress
    } finally {
        if (Test-Path -LiteralPath $root) { Remove-Item -LiteralPath $root -Recurse -Force }
    }
}

if ($PSCmdlet.ParameterSetName -eq 'SelfTest') { Invoke-SelfTest; exit 0 }

if ($Confirmation -cne $script:Confirmation) { Stop-Recovery 'ACCESS_CONFIRMATION_MISMATCH' 'exact confirmation literal required' }
$identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$isAdmin = (New-Object Security.Principal.WindowsPrincipal $identity).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) { Stop-Recovery 'ACCESS_PRINCIPAL_MISMATCH' 'recovery requires an Administrator-elevated context' }
$result = Invoke-Recovery -LedgerPath @($LedgerPath | ForEach-Object { Get-CanonicalPath $_ }) -TransactionId $TransactionId
$result | ConvertTo-Json -Compress -Depth 6
