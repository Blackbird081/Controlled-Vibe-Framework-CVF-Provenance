<#
.SYNOPSIS
    One-time elevated repair and verification for the ACEL G1 Group 3 log ACL.

.DESCRIPTION
    Verifies the Party B-created observation record and its exact pre-repair
    security state, changes only the DACL to add the exact Local reviewer SID
    as a read-only principal, verifies the independent Python checker before
    and after the change, and proves that the source bytes are unchanged.

    Any failure after mutation restores the captured pre-state DACL. The
    script never changes source content, owner, SACL, registry data, or any
    Group 1/2 source.
#>
[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$script:FailureDiagnosticPath = $null

trap {
    $failureMessage = $_.Exception.Message
    if ($null -ne $script:FailureDiagnosticPath) {
        try {
            $failurePayload = [ordered]@{
                schemaVersion = 'cvf.acel.g1.t3cC2LocalVerificationFailure.v1'
                disposition = 'FAILED_NO_ACCEPTANCE'
                message = $failureMessage
                scriptStackTrace = $_.ScriptStackTrace
                recordedAtUtc = [DateTime]::UtcNow.ToString('o')
                claimBoundary = 'diagnostic only; no source-establishment or repair-success claim'
            }
            [System.IO.File]::WriteAllText(
                $script:FailureDiagnosticPath,
                (($failurePayload | ConvertTo-Json -Depth 6) + [Environment]::NewLine),
                [System.Text.UTF8Encoding]::new($false))
        } catch { }
    }
    Write-Error $failureMessage
    exit 1
}

$script:PartyBSid = 'S-1-5-21-1644666849-912006174-747199667-1009'
$script:LocalSid = 'S-1-5-21-1644666849-912006174-747199667-1001'
$script:PartyASid = 'S-1-5-21-1644666849-912006174-747199667-1006'
$script:ExpectedSnapshotId = 'snap-9037220e94434acaa4909cb1cba2e2fc-eec908be7c0243d4'
$script:ExpectedSnapshotHash = '87594cdcf8a1e0c3c4b439434aeda39444ff54a432674d97403f1980c995d883'
$script:ExpectedEntryHash = 'a97f1066cc5fe33409eff6539c2ca68dcf72f794209c8de5df93a7f81dc6e1c3'

function Get-Sha256Hex {
    param([Parameter(Mandatory = $true)][byte[]] $Bytes)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([System.Convert]::ToHexString($sha.ComputeHash($Bytes))).ToLowerInvariant() }
    finally { $sha.Dispose() }
}

function Get-AceTuple {
    param([Parameter(Mandatory = $true)] $Rule)
    $sid = $Rule.IdentityReference.Translate(
        [System.Security.Principal.SecurityIdentifier]).Value
    return '{0}|{1}|{2}|{3}|{4}|{5}' -f $sid,
        ([int]$Rule.FileSystemRights), ([int]$Rule.AccessControlType),
        ([bool]$Rule.IsInherited), ([int]$Rule.InheritanceFlags),
        ([int]$Rule.PropagationFlags)
}

function Get-SecurityState {
    param([Parameter(Mandatory = $true)][string] $Path)
    $info = [System.IO.FileInfo]::new($Path)
    $ownerSecurity = [System.IO.FileSystemAclExtensions]::GetAccessControl(
        $info, [System.Security.AccessControl.AccessControlSections]::Owner)
    $accessSecurity = [System.IO.FileSystemAclExtensions]::GetAccessControl(
        $info, [System.Security.AccessControl.AccessControlSections]::Access)
    $rules = @($accessSecurity.GetAccessRules(
        $true, $true, [System.Security.Principal.SecurityIdentifier]))
    return [pscustomobject]@{
        OwnerSid = $ownerSecurity.GetOwner(
            [System.Security.Principal.SecurityIdentifier]).Value
        Protected = [bool]$accessSecurity.AreAccessRulesProtected
        AceTuples = @($rules | ForEach-Object { Get-AceTuple -Rule $_ } | Sort-Object)
        AccessSecurity = $accessSecurity
    }
}

function Get-ExpectedTuples {
    param([Parameter(Mandatory = $true)][bool] $IncludeLocalRead)
    $allow = [int][System.Security.AccessControl.AccessControlType]::Allow
    $full = [int][System.Security.AccessControl.FileSystemRights]::FullControl
    $readRuleProbe = [System.Security.AccessControl.FileSystemAccessRule]::new(
        [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid),
        [System.Security.AccessControl.FileSystemRights]::Read,
        [System.Security.AccessControl.AccessControlType]::Allow)
    $read = [int]$readRuleProbe.FileSystemRights
    return @(
        foreach ($sid in @($script:PartyBSid, 'S-1-5-18', 'S-1-5-32-544')) {
            '{0}|{1}|{2}|False|0|0' -f $sid, $full, $allow
        }
        if ($IncludeLocalRead) {
            '{0}|{1}|{2}|False|0|0' -f $script:LocalSid, $read, $allow
        }
    ) | Sort-Object
}

function Assert-SecurityState {
    param(
        [Parameter(Mandatory = $true)] $State,
        [Parameter(Mandatory = $true)][bool] $IncludeLocalRead,
        [Parameter(Mandatory = $true)][string] $Stage
    )
    if ($State.OwnerSid -ne $script:PartyBSid) {
        throw "[$Stage] owner SID '$($State.OwnerSid)' is not Party B '$($script:PartyBSid)'"
    }
    if (-not $State.Protected) { throw "[$Stage] DACL is not protected" }
    $expected = @(Get-ExpectedTuples -IncludeLocalRead $IncludeLocalRead)
    if ($State.AceTuples.Count -ne $expected.Count) {
        throw ("[$Stage] expected $($expected.Count) ACEs but found $($State.AceTuples.Count); " +
            "actual tuples: $($State.AceTuples -join '; ')")
    }
    for ($index = 0; $index -lt $expected.Count; $index++) {
        if ($State.AceTuples[$index] -ne $expected[$index]) {
            throw "[$Stage] ACE mismatch at $index; expected '$($expected[$index])', found '$($State.AceTuples[$index])'"
        }
    }
}

function Invoke-IndependentChecker {
    param(
        [Parameter(Mandatory = $true)][string] $CheckerPath,
        [Parameter(Mandatory = $true)][string] $LogPath
    )
    $python = Get-Command python -ErrorAction Stop
    $output = @(& $python.Source $CheckerPath --log $LogPath `
        --expected-observer $script:PartyBSid `
        --registry-writer-sid $script:PartyASid 2>&1)
    if ($LASTEXITCODE -ne 0) {
        throw "independent checker rejected the observation log: $($output -join [Environment]::NewLine)"
    }
    $report = ($output -join [Environment]::NewLine) | ConvertFrom-Json
    if ($report.result -ne 'PASS' -or $report.entryCount -ne 1 -or
        $report.lastEntryHashHex -ne $script:ExpectedEntryHash) {
        throw 'independent checker output does not match the expected one-record ceremony product'
    }
    return ($output -join [Environment]::NewLine)
}

$principal = [System.Security.Principal.WindowsPrincipal]::new(
    [System.Security.Principal.WindowsIdentity]::GetCurrent())
$isAdministrator = $principal.IsInRole(
    [System.Security.Principal.WindowsBuiltInRole]::Administrator)

$repositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path
$logPath = Join-Path $repositoryRoot 'governance/sources/registry_observation_log/LOG.jsonl'
$registryPath = Join-Path $repositoryRoot 'governance/sources/verifier_key_registry/REGISTRY.json'
$checkerPath = Join-Path $repositoryRoot 'governance/compat/check_acel_g1_registry_observation_log.py'
$receiptPath = Join-Path $repositoryRoot 'docs/reviews/evidence/cvf-acel-g1-t3c-c2-local-verification-2026-09-22.json'
$script:FailureDiagnosticPath = Join-Path $repositoryRoot 'docs/reviews/evidence/cvf-acel-g1-t3c-c2-local-verification-failure-2026-09-22.json'
if (Test-Path -LiteralPath $script:FailureDiagnosticPath -PathType Leaf) {
    [System.IO.File]::Delete($script:FailureDiagnosticPath)
}

foreach ($requiredPath in @($logPath, $registryPath, $checkerPath)) {
    if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
        throw "required path is absent: $requiredPath"
    }
}
if (Test-Path -LiteralPath $receiptPath) {
    throw "receipt already exists; refusing to overwrite: $receiptPath"
}

$logBytesBefore = [System.IO.File]::ReadAllBytes($logPath)
$logHashBefore = Get-Sha256Hex -Bytes $logBytesBefore
$logText = [System.Text.UTF8Encoding]::new($false, $true).GetString($logBytesBefore)
$lines = @($logText -split "`r?`n" | Where-Object { $_.Length -gt 0 })
if ($lines.Count -ne 1) { throw "expected exactly one nonblank observation line; found $($lines.Count)" }
$record = $lines[0] | ConvertFrom-Json
if ($record.snapshotId -ne $script:ExpectedSnapshotId -or
    $record.registryName -ne 'verifier_key_registry' -or
    $record.registrySnapshotVersion -ne 1 -or
    $record.snapshotHashHex -ne $script:ExpectedSnapshotHash -or
    $record.entryHashHex -ne $script:ExpectedEntryHash -or
    $record.observerIdentity -ne $script:PartyBSid) {
    throw 'stored observation fields do not match the operator-reported ceremony product'
}

$snapshotEncoded = [string]$record.snapshot_content
$padding = (4 - ($snapshotEncoded.Length % 4)) % 4
$snapshotBase64 = $snapshotEncoded.Replace('-', '+').Replace('_', '/') + ('=' * $padding)
$snapshotBytes = [System.Convert]::FromBase64String($snapshotBase64)
$registryBytes = [System.IO.File]::ReadAllBytes($registryPath)
if (-not [System.Linq.Enumerable]::SequenceEqual[byte]($snapshotBytes, $registryBytes)) {
    throw 'decoded snapshot_content is not byte-identical to the governed Group 1 registry'
}
if ((Get-Sha256Hex -Bytes $snapshotBytes) -ne $script:ExpectedSnapshotHash) {
    throw 'decoded snapshot_content SHA-256 does not match the expected snapshot hash'
}

$checkerBefore = Invoke-IndependentChecker -CheckerPath $checkerPath -LogPath $logPath
$stateBefore = Get-SecurityState -Path $logPath
$prestateAlreadyCompliant = $false
try {
    Assert-SecurityState -State $stateBefore -IncludeLocalRead $false -Stage 'PRESTATE'
} catch {
    $oldPolicyFailure = $_
    try {
        Assert-SecurityState -State $stateBefore -IncludeLocalRead $true -Stage 'PRESTATE_ALREADY_COMPLIANT'
        $prestateAlreadyCompliant = $true
    } catch {
        throw $oldPolicyFailure
    }
}
if (-not $prestateAlreadyCompliant -and -not $isAdministrator) {
    throw '[ELEVATION_REQUIRED] old three-ACE policy requires an elevated one-time DACL repair'
}

$daclMutated = $false
try {
    if (-not $prestateAlreadyCompliant) {
        $newSecurity = [System.Security.AccessControl.FileSecurity]::new()
        $newSecurity.SetAccessRuleProtection($true, $false)
        foreach ($sid in @($script:PartyBSid, 'S-1-5-18', 'S-1-5-32-544')) {
            $newSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
                [System.Security.Principal.SecurityIdentifier]::new($sid),
                [System.Security.AccessControl.FileSystemRights]::FullControl,
                [System.Security.AccessControl.AccessControlType]::Allow))
        }
        $newSecurity.AddAccessRule([System.Security.AccessControl.FileSystemAccessRule]::new(
            [System.Security.Principal.SecurityIdentifier]::new($script:LocalSid),
            [System.Security.AccessControl.FileSystemRights]::Read,
            [System.Security.AccessControl.AccessControlType]::Allow))

        [System.IO.FileSystemAclExtensions]::SetAccessControl(
            [System.IO.FileInfo]::new($logPath), $newSecurity)
        $daclMutated = $true
    }

    $stateAfter = Get-SecurityState -Path $logPath
    Assert-SecurityState -State $stateAfter -IncludeLocalRead $true -Stage 'POSTSTATE'
    $checkerAfter = Invoke-IndependentChecker -CheckerPath $checkerPath -LogPath $logPath
    $logBytesAfter = [System.IO.File]::ReadAllBytes($logPath)
    $logHashAfter = Get-Sha256Hex -Bytes $logBytesAfter
    if ($logHashAfter -ne $logHashBefore -or
        -not [System.Linq.Enumerable]::SequenceEqual[byte]($logBytesBefore, $logBytesAfter)) {
        throw 'source bytes changed during the DACL-only repair'
    }

    $receipt = [ordered]@{
        schemaVersion = 'cvf.acel.g1.t3cC2LocalVerificationReceipt.v1'
        disposition = 'LOCAL_VERIFICATION_PASS'
        sourcePath = 'governance/sources/registry_observation_log/LOG.jsonl'
        snapshotId = $script:ExpectedSnapshotId
        snapshotHashHex = $script:ExpectedSnapshotHash
        entryHashHex = $script:ExpectedEntryHash
        observerIdentity = $script:PartyBSid
        fileSha256Before = $logHashBefore
        fileSha256After = $logHashAfter
        sourceBytesUnchanged = $true
        sourceCheckerBefore = 'PASS'
        sourceCheckerAfter = 'PASS'
        daclMutationPerformed = $daclMutated
        ownerSid = $stateAfter.OwnerSid
        daclProtected = $stateAfter.Protected
        aceTuples = @($stateAfter.AceTuples)
        executedAtUtc = [DateTime]::UtcNow.ToString('o')
        claimBoundary = 'Group 3 artifact and Local-read ACL verified; no establishment, admission, T3E wiring, provider, deployment or public-export claim'
    }
    $receiptJson = $receipt | ConvertTo-Json -Depth 8
    [System.IO.File]::WriteAllText(
        $receiptPath, $receiptJson + [Environment]::NewLine,
        [System.Text.UTF8Encoding]::new($false))
    if (Test-Path -LiteralPath $script:FailureDiagnosticPath -PathType Leaf) {
        [System.IO.File]::Delete($script:FailureDiagnosticPath)
    }

    Write-Host 'T3C_C2_LOCAL_VERIFICATION_AND_ACL_REPAIR_PASS'
    Write-Host "  logSha256 : $logHashAfter"
    Write-Host "  receipt   : $receiptPath"
    if ($daclMutated) {
        Write-Host '  mutation  : DACL only; source bytes unchanged'
    } else {
        Write-Host '  mutation  : none; DACL was already compliant and source bytes are unchanged'
    }
} catch {
    if ($daclMutated) {
        try {
            if (Test-Path -LiteralPath $receiptPath -PathType Leaf) {
                [System.IO.File]::Delete($receiptPath)
            }
            [System.IO.FileSystemAclExtensions]::SetAccessControl(
                [System.IO.FileInfo]::new($logPath), $stateBefore.AccessSecurity)
            $restored = Get-SecurityState -Path $logPath
            Assert-SecurityState -State $restored -IncludeLocalRead $false -Stage 'ROLLBACK'
        } catch {
            throw "[ACL_REPAIR_ROLLBACK_FAILED] original error and rollback failure: $($_.Exception.Message)"
        }
    }
    throw
}
