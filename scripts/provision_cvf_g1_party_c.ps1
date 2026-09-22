<#
.SYNOPSIS
    Provision or check the dedicated ACEL G1 Party C local principal.

.DESCRIPTION
    Default/check mode is read-only. Execute mode requires elevation, an exact
    confirmation phrase and a password entered as SecureString. It creates one
    standard local account, enforces password-required and bounded expiry,
    rejects Administrators membership and writes a secret-free receipt.
    A failure after creation removes only the newly created account.
#>
[CmdletBinding(DefaultParameterSetName = 'Check')]
param(
    [Parameter(ParameterSetName = 'Check')][switch] $Check,
    [Parameter(Mandatory = $true, ParameterSetName = 'Execute')][switch] $ExecuteProvision
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:AccountName = 'cvf-g1-party-c'
$script:Description = 'CVF G1 Party C dedicated issuer registry authority'
$script:ConfirmationPhrase = 'CREATE CVF G1 PARTY C'
$script:ForbiddenSids = @(
    'S-1-5-21-1644666849-912006174-747199667-1001',
    'S-1-5-21-1644666849-912006174-747199667-1006',
    'S-1-5-21-1644666849-912006174-747199667-1008',
    'S-1-5-21-1644666849-912006174-747199667-1009'
)

function Get-PartyCState {
    $user = Get-LocalUser -Name $script:AccountName -ErrorAction SilentlyContinue
    if ($null -eq $user) { return $null }
    $adminSids = @(Get-LocalGroupMember -Group 'Administrators' -ErrorAction Stop |
        ForEach-Object { $_.SID.Value })
    return [pscustomobject]@{
        Name = $user.Name
        Enabled = [bool]$user.Enabled
        PasswordRequired = [bool]$user.PasswordRequired
        Sid = $user.SID.Value
        AccountExpires = $user.AccountExpires
        Description = $user.Description
        IsAdministrator = $adminSids -contains $user.SID.Value
    }
}
function Assert-PartyCState {
    param([Parameter(Mandatory = $true)] $State)
    if ($State.Name -cne $script:AccountName) { throw '[PARTY_C_NAME_MISMATCH] account name mismatch' }
    if (-not $State.Enabled) { throw '[PARTY_C_DISABLED] account is disabled' }
    if (-not $State.PasswordRequired) { throw '[PARTY_C_PASSWORD_NOT_REQUIRED] password-required flag is false' }
    if ($State.IsAdministrator) { throw '[PARTY_C_ADMIN_FORBIDDEN] Party C must be a standard non-admin account' }
    if ($script:ForbiddenSids -contains $State.Sid) { throw '[PARTY_C_IDENTITY_COLLISION] SID collides with Local, Party A, Approver or Party B' }
    if ($State.Description -cne $script:Description) { throw '[PARTY_C_DESCRIPTION_MISMATCH] account description mismatch' }
    if ($null -eq $State.AccountExpires -or $State.AccountExpires -le (Get-Date) -or
        $State.AccountExpires -gt (Get-Date).AddDays(31)) {
        throw '[PARTY_C_EXPIRY_INVALID] account expiry is absent, expired or outside the bounded window'
    }
}

$repositoryRoot = (Resolve-Path -LiteralPath (Split-Path -Path $PSScriptRoot -Parent)).Path
$receiptPath = Join-Path $repositoryRoot 'docs/reviews/evidence/cvf-acel-g1-t3d-party-c-provisioning-operator-result-2026-09-22.json'
$failurePath = Join-Path $repositoryRoot 'docs/reviews/evidence/cvf-acel-g1-t3d-party-c-provisioning-failure-2026-09-22.json'
$script:CreationOccurred = $false
$script:RollbackAttempted = $false
$script:RollbackSucceeded = $false

trap {
    $failureRecord = $_
    $accountExistsAfterFailure = $null -ne (
        Get-LocalUser -Name $script:AccountName -ErrorAction SilentlyContinue)
    $failureReceipt = [ordered]@{
        schemaVersion = 'cvf.acel.g1.partyCProvisioningFailure.v1'
        disposition = 'PARTY_C_PROVISIONING_FAILED_NO_RETRY_PENDING_LOCAL_DIAGNOSIS'
        failedAtUtc = [DateTime]::UtcNow.ToString('o')
        errorMessage = $failureRecord.Exception.Message
        fullyQualifiedErrorId = $failureRecord.FullyQualifiedErrorId
        accountCreationOccurred = $script:CreationOccurred
        rollbackAttempted = $script:RollbackAttempted
        rollbackSucceeded = $script:RollbackSucceeded
        accountExistsAfterFailure = $accountExistsAfterFailure
        successReceiptExistsAfterFailure = Test-Path -LiteralPath $receiptPath -PathType Leaf
        secretMaterialRecorded = $false
        claimBoundary = 'secret-free failed-attempt diagnostic only; retry requires Local diagnosis'
    }
    try {
        [System.IO.File]::WriteAllText(
            $failurePath, (($failureReceipt | ConvertTo-Json -Depth 6) + [Environment]::NewLine),
            [System.Text.UTF8Encoding]::new($false))
        Write-Host "Failure diagnostic: $failurePath" -ForegroundColor Yellow
    } catch {
        Write-Warning "Could not persist the secret-free failure diagnostic: $($_.Exception.Message)"
    }
    Write-Error -Message $failureRecord.Exception.Message -ErrorAction Continue
    exit 1
}

if ($PSCmdlet.ParameterSetName -eq 'Check') {
    $state = Get-PartyCState
    if ($null -eq $state) {
        Write-Host 'READY_TO_PROVISION_CVF_G1_PARTY_C'
        Write-Host "  account : $env:COMPUTERNAME\$($script:AccountName)"
        Write-Host '  posture : standard local account; password required; 30-day expiry'
        exit 0
    }
    Assert-PartyCState -State $state
    Write-Host 'PARTY_C_ALREADY_PROVISIONED_PENDING_LOCAL_VERIFICATION'
    Write-Host "  account : $env:COMPUTERNAME\$($state.Name)"
    Write-Host "  sid     : $($state.Sid)"
    exit 0
}

Remove-Item -LiteralPath $failurePath -Force -ErrorAction SilentlyContinue

$principal = [System.Security.Principal.WindowsPrincipal]::new(
    [System.Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
    throw '[ELEVATION_REQUIRED] execute provisioning from an elevated PowerShell session'
}
if ($null -ne (Get-PartyCState)) {
    throw '[PARTY_C_ALREADY_EXISTS] refusing to mutate an existing account'
}
if (Test-Path -LiteralPath $receiptPath -PathType Leaf) {
    throw '[RECEIPT_ALREADY_EXISTS] refusing to overwrite an existing provisioning result'
}

Write-Host "About to create the dedicated standard local account '$env:COMPUTERNAME\$($script:AccountName)'."
Write-Host "Type exactly: $($script:ConfirmationPhrase)"
$confirmation = Read-Host 'Confirmation'
if ($confirmation -cne $script:ConfirmationPhrase) {
    throw '[CONFIRMATION_MISMATCH] provisioning cancelled before mutation'
}

$password = Read-Host "Password for $($script:AccountName)" -AsSecureString
$created = $false
try {
    $expiry = (Get-Date).AddDays(30)
    New-LocalUser -Name $script:AccountName -Password $password `
        -Description $script:Description -AccountExpires $expiry | Out-Null
    $created = $true
    $script:CreationOccurred = $true
    Remove-Variable password -ErrorAction SilentlyContinue

    & net.exe user $script:AccountName /passwordreq:yes | Out-Null
    if ($LASTEXITCODE -ne 0) { throw '[PASSWORD_REQUIRED_ENFORCEMENT_FAILED] net user returned nonzero' }

    $state = Get-PartyCState
    if ($null -eq $state) { throw '[PARTY_C_NOT_FOUND_AFTER_CREATE] created account is not readable' }
    Assert-PartyCState -State $state

    $receipt = [ordered]@{
        schemaVersion = 'cvf.acel.g1.partyCProvisioningResult.v1'
        disposition = 'PARTY_C_PRINCIPAL_CREATED_PENDING_LOCAL_VERIFICATION'
        principalName = "$env:COMPUTERNAME\$($state.Name)"
        principalSid = $state.Sid
        enabled = $state.Enabled
        passwordRequired = $state.PasswordRequired
        isAdministrator = $state.IsAdministrator
        accountExpires = $state.AccountExpires.ToUniversalTime().ToString('o')
        description = $state.Description
        createdAtUtc = [DateTime]::UtcNow.ToString('o')
        secretMaterialRecorded = $false
        claimBoundary = 'principal provisioning result only; no issuer registry, lookup response, observation, consumer binding or admission claim'
    }
    [System.IO.File]::WriteAllText(
        $receiptPath, (($receipt | ConvertTo-Json -Depth 6) + [Environment]::NewLine),
        [System.Text.UTF8Encoding]::new($false))
    Remove-Item -LiteralPath $failurePath -Force -ErrorAction SilentlyContinue

    Write-Host 'PARTY_C_PRINCIPAL_CREATED_PENDING_LOCAL_VERIFICATION'
    Write-Host "  account : $($receipt.principalName)"
    Write-Host "  sid     : $($receipt.principalSid)"
    Write-Host "  receipt : $receiptPath"
} catch {
    Remove-Variable password -ErrorAction SilentlyContinue
    if ($created) {
        $script:RollbackAttempted = $true
        try {
            Remove-LocalUser -Name $script:AccountName -ErrorAction Stop
            $script:RollbackSucceeded = $true
        } catch {
            throw "[PARTY_C_ROLLBACK_FAILED] account creation failed and rollback also failed: $($_.Exception.Message)"
        }
    }
    throw
}
