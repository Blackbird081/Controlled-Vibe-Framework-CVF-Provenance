<#
.SYNOPSIS
    Focused disposable-fixture test matrix for scripts\get_cvf_projection_map.ps1 (T1).

.DESCRIPTION
    Self-contained PowerShell test runner. It builds temporary disposable git
    repositories under $env:TEMP for every case, never touches the real
    public-sync clone, and cleans its own temp area in a `finally` block. It
    returns nonzero on any failed assertion.

    Run: powershell -NoProfile -ExecutionPolicy Bypass -File scripts\test_get_cvf_projection_map.ps1
#>

[CmdletBinding()]
param(
    [string]$GovernedReceiptPath
)

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$mapperPath = Join-Path $scriptRoot 'get_cvf_projection_map.ps1'

$testRunId = [guid]::NewGuid().ToString('N').Substring(0, 8)
$tempRoot = Join-Path $env:TEMP "cvf_proj_map_test_$testRunId"

$script:passCount = 0
$script:failCount = 0
$script:results = [System.Collections.Generic.List[string]]::new()

function Assert-True {
    param([bool]$Condition, [string]$CaseName, [string]$Detail = '')
    if ($Condition) {
        $script:passCount++
        $script:results.Add("PASS: $CaseName")
    } else {
        $script:failCount++
        $script:results.Add("FAIL: $CaseName -- $Detail")
    }
}

function New-DisposableGitRepo {
    param([string]$Path, [string]$OriginUrl)
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
    Push-Location $Path
    try {
        & git init -q 2>&1 | Out-Null
        & git config user.email 'test@example.invalid' 2>&1 | Out-Null
        & git config user.name 'CVF Test Fixture' 2>&1 | Out-Null
        if ($OriginUrl) {
            & git remote add origin $OriginUrl 2>&1 | Out-Null
        }
        'fixture' | Out-File -FilePath (Join-Path $Path 'README.md') -Encoding utf8
        & git add -A 2>&1 | Out-Null
        & git commit -q -m 'fixture init' 2>&1 | Out-Null
    } finally {
        Pop-Location
    }
}

function Invoke-Mapper {
    param(
        [string]$ProvenanceRoot,
        [string]$PublicSyncRoot,
        [string]$CvfWebRoot,
        [string]$PolicyPath,
        [string]$ReceiptOutputPath,
        [string]$WorkingDirectory
    )
    $argList = @(
        '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $mapperPath,
        '-ProvenanceRoot', $ProvenanceRoot,
        '-PublicSyncRoot', $PublicSyncRoot,
        '-CvfWebRoot', $CvfWebRoot,
        '-PolicyPath', $PolicyPath
    )
    if ($ReceiptOutputPath) {
        $argList += @('-ReceiptOutputPath', $ReceiptOutputPath)
    }
    $prevLocation = Get-Location
    if ($WorkingDirectory) { Set-Location $WorkingDirectory }
    try {
        $stdout = & powershell -NoProfile -ExecutionPolicy Bypass @argList 2>&1
        $exitCode = $LASTEXITCODE
    } finally {
        Set-Location $prevLocation
    }
    $stdoutText = ($stdout -join "`n")
    $json = $null
    try { $json = $stdoutText | ConvertFrom-Json } catch { $json = $null }
    return [pscustomobject]@{
        ExitCode = $exitCode
        StdoutText = $stdoutText
        Json = $json
    }
}

function New-BasePolicyFixture {
    param([string]$PublicRemote = 'https://example.invalid/public-sync.git', [string]$ProvenanceRemote = 'https://example.invalid/provenance-marker-repo.git')
    return [pscustomobject]@{
        schemaVersion = '1.0.0'
        sourceOfTruth = [pscustomobject]@{ path = 'scripts/cvf-public-sync.ps1'; note = 'fixture' }
        expectedRemotes = [pscustomobject]@{
            provenanceRemote = $ProvenanceRemote
            publicRemote = $PublicRemote
        }
        allowedTrees = @('AllowedTree')
        allowedRootFiles = @('README.md', 'ALLOWED_ROOT.txt')
        allowedScriptFiles = @()
        allowedWorkspaceTemplateFiles = @()
        allowedDocsPaths = @()
        mappedFiles = @(
            [pscustomobject]@{ source = 'MappedSource.txt'; destination = 'MappedDestination.txt' }
        )
        denyPatterns = @('DENY_ME', '\.env')
        denyExceptions = @()
        candidateActionEnum = @('COPY_CANDIDATE_ABSENT_TARGET', 'FLAG_SEMANTIC_REVIEW_CHANGED', 'SKIP_UNCHANGED', 'SKIP_DENIED', 'SKIP_NOT_ALLOWLISTED')
        semanticReviewBoundary = [pscustomobject]@{ note = 'fixture'; autoApproveForbidden = $true }
        cvfWebObservation = [pscustomobject]@{
            packageJsonPath = 'package.json'
            runtimeModulesPath = 'runtime-modules.ts'
            expectedSot3RegistryIds = @('cvf-refinery', 'cvf-truth-kernel', 'cvf-truth-flow')
        }
    }
}

function Write-PolicyFixture {
    param([string]$Path, [pscustomobject]$Policy)
    ($Policy | ConvertTo-Json -Depth 20) | Out-File -FilePath $Path -Encoding utf8
}

function Write-SyncScriptFixture {
    param([string]$ProvenanceRoot, [pscustomobject]$Policy)
    $scriptsDir = Join-Path $ProvenanceRoot 'scripts'
    New-Item -ItemType Directory -Path $scriptsDir -Force | Out-Null

    function Format-PsArray([object[]]$Values) {
        $lines = @($Values | ForEach-Object { "    '$($_ -replace "'", "''")'" })
        return "@(`r`n$($lines -join ",`r`n")`r`n)"
    }

    $mappedBlocks = @($Policy.mappedFiles | ForEach-Object {
        "    @{`r`n        Source      = '$($_.source)'`r`n        Destination = '$($_.destination)'`r`n    }"
    })
    $content = @(
        "`$PUBLIC_REMOTE = '$($Policy.expectedRemotes.publicRemote)'"
        "`$ALLOWED_TREES = $(Format-PsArray $Policy.allowedTrees)"
        "`$ALLOWED_ROOT_FILES = $(Format-PsArray $Policy.allowedRootFiles)"
        "`$ALLOWED_SCRIPT_FILES = $(Format-PsArray $Policy.allowedScriptFiles)"
        "`$ALLOWED_WORKSPACE_TEMPLATE_FILES = $(Format-PsArray $Policy.allowedWorkspaceTemplateFiles)"
        "`$ALLOWED_DOCS_PATHS = $(Format-PsArray $Policy.allowedDocsPaths)"
        "`$DENY_PATTERNS = $(Format-PsArray $Policy.denyPatterns)"
        "`$DENY_EXCEPTIONS = $(Format-PsArray $Policy.denyExceptions)"
        "`$MAPPED_FILES = @(`r`n$($mappedBlocks -join ",`r`n")`r`n)"
    ) -join "`r`n`r`n"
    [System.IO.File]::WriteAllText((Join-Path $scriptsDir 'cvf-public-sync.ps1'), $content, [System.Text.Encoding]::UTF8)
}

try {
    New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

    # -----------------------------------------------------------------
    # Case 1: help/parameter contract
    # -----------------------------------------------------------------
    $help = Get-Help $mapperPath -Full
    Assert-True ($null -ne $help.Synopsis -and $help.Synopsis.Trim().Length -gt 0) 'help_parameter_contract_synopsis' 'missing synopsis'
    $paramNames = $help.Parameters.Parameter | ForEach-Object { $_.Name }
    $expectedParams = @('ProvenanceRoot', 'PublicSyncRoot', 'CvfWebRoot', 'PolicyPath', 'ReceiptOutputPath')
    $missingParams = $expectedParams | Where-Object { $_ -notin $paramNames }
    Assert-True ($missingParams.Count -eq 0) 'help_parameter_contract_params' "missing: $($missingParams -join ',')"

    # -----------------------------------------------------------------
    # Case 2: policy parity by parsing current sync-script assignments
    # (parses the REAL repo's cvf-public-sync.ps1 without executing it)
    # -----------------------------------------------------------------
    $realProvenanceRoot = (Resolve-Path (Join-Path $scriptRoot '..')).ProviderPath
    $realPublicSyncScript = Join-Path $realProvenanceRoot 'scripts\cvf-public-sync.ps1'
    $realPolicyPath = Join-Path $realProvenanceRoot 'scripts\cvf_projection_policy.json'
    Assert-True (Test-Path -LiteralPath $realPublicSyncScript -PathType Leaf) 'policy_parity_source_script_exists' 'cvf-public-sync.ps1 not found'
    $realPolicy = Get-Content -LiteralPath $realPolicyPath -Raw -Encoding utf8 | ConvertFrom-Json
    $syncScriptText = Get-Content -LiteralPath $realPublicSyncScript -Raw -Encoding utf8
    $treesMatch = [regex]::Match($syncScriptText, "(?ms)\`$ALLOWED_TREES\s*=\s*@\((.*?)\r?\n\)")
    $parsedTrees = @()
    if ($treesMatch.Success) {
        [regex]::Matches($treesMatch.Groups[1].Value, "'([^']+)'") | ForEach-Object { $parsedTrees += $_.Groups[1].Value }
    }
    $policyTrees = $realPolicy.allowedTrees
    $treesDiff = Compare-Object -ReferenceObject ($policyTrees | Sort-Object) -DifferenceObject ($parsedTrees | Sort-Object) -SyncWindow 0
    Assert-True (@($treesDiff).Count -eq 0) 'policy_parity_allowed_trees' "diff: $($treesDiff | Out-String)"
    $remoteMatch = [regex]::Match($syncScriptText, "\`$PUBLIC_REMOTE\s*=\s*'([^']+)'")
    Assert-True ($remoteMatch.Success -and $remoteMatch.Groups[1].Value -eq $realPolicy.expectedRemotes.publicRemote) 'policy_parity_public_remote' 'public remote mismatch'
    $realOrigin = (& git -C $realProvenanceRoot remote get-url origin 2>$null | Select-Object -First 1)
    Assert-True ($realOrigin -eq $realPolicy.expectedRemotes.provenanceRemote) 'policy_parity_provenance_remote' "expected exact provenance remote, found: $realOrigin"

    $realGroupMap = [ordered]@{
        allowedTrees = 'ALLOWED_TREES'
        allowedRootFiles = 'ALLOWED_ROOT_FILES'
        allowedScriptFiles = 'ALLOWED_SCRIPT_FILES'
        allowedWorkspaceTemplateFiles = 'ALLOWED_WORKSPACE_TEMPLATE_FILES'
        allowedDocsPaths = 'ALLOWED_DOCS_PATHS'
        denyPatterns = 'DENY_PATTERNS'
        denyExceptions = 'DENY_EXCEPTIONS'
    }
    foreach ($entry in $realGroupMap.GetEnumerator()) {
        $groupMatch = [regex]::Match($syncScriptText, "(?ms)\`$$($entry.Value)\s*=\s*@\((.*?)\r?\n\)")
        $parsed = @()
        if ($groupMatch.Success) {
            [regex]::Matches($groupMatch.Groups[1].Value, "'([^']*)'") | ForEach-Object { $parsed += $_.Groups[1].Value }
        }
        $expected = @($realPolicy.($entry.Key))
        if ($entry.Key -ne 'denyPatterns') {
            $parsed = @($parsed | ForEach-Object { $_ -replace '\\', '/' })
            $expected = @($expected | ForEach-Object { $_ -replace '\\', '/' })
        }
        $groupDiff = @(Compare-Object -ReferenceObject ($expected | Sort-Object) -DifferenceObject ($parsed | Sort-Object) -SyncWindow 0)
        Assert-True ($groupMatch.Success -and $groupDiff.Count -eq 0) "policy_parity_real_$($entry.Key)" ($groupDiff | Out-String)
    }

    $realMappedMatches = [regex]::Matches($syncScriptText, "Source\s*=\s*'([^']+)'\s*\r?\n\s*Destination\s*=\s*'([^']+)'")
    $realScriptMapped = @($realMappedMatches | ForEach-Object { "$(($_.Groups[1].Value -replace '\\','/'))=>$(($_.Groups[2].Value -replace '\\','/'))" })
    $realPolicyMapped = @($realPolicy.mappedFiles | ForEach-Object { "$($_.source)=>$($_.destination)" })
    $realMappedDiff = @(Compare-Object -ReferenceObject ($realPolicyMapped | Sort-Object) -DifferenceObject ($realScriptMapped | Sort-Object) -SyncWindow 0)
    Assert-True ($realMappedDiff.Count -eq 0) 'policy_parity_real_mappedFiles' ($realMappedDiff | Out-String)
    # Confirm this test never dot-sources or executes cvf-public-sync.ps1:
    # only text-pattern parsing above; no '. $realPublicSyncScript' or invocation exists in this file.

    # -----------------------------------------------------------------
    # Shared fixture roots for negative + positive cases
    # -----------------------------------------------------------------
    $provRoot = Join-Path $tempRoot 'provenance'
    $pubRoot = Join-Path $tempRoot 'public'
    $cvfWebRoot = Join-Path $tempRoot 'cvfweb'
    New-DisposableGitRepo -Path $provRoot -OriginUrl 'https://example.invalid/provenance-marker-repo.git'
    New-DisposableGitRepo -Path $pubRoot -OriginUrl 'https://example.invalid/public-sync.git'
    New-Item -ItemType Directory -Path $cvfWebRoot -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $cvfWebRoot 'src\lib\server') -Force | Out-Null
    @'
{
  "name": "fixture-cvf-web",
  "version": "0.0.0-fixture",
  "dependencies": {
    "cvf-refinery": "file:../CVF_REFINERY",
    "cvf-truth-kernel": "file:../CVF_TRUTH_KERNEL",
    "cvf-truth-flow": "file:../CVF_TRUTH_FLOW"
  }
}
'@ | Out-File -FilePath (Join-Path $cvfWebRoot 'package.json') -Encoding utf8
    @"
const MODULES = [
    { id: 'cvf-refinery', name: 'CVF Refinery' },
    { id: 'cvf-truth-kernel', name: 'CVF Truth Kernel' },
    { id: 'cvf-truth-flow', name: 'CVF Truth Flow' },
];
"@ | Out-File -FilePath (Join-Path $cvfWebRoot 'src\lib\server\runtime-modules.ts') -Encoding utf8

    $policyPath = Join-Path $tempRoot 'policy.json'
    $basePolicy = New-BasePolicyFixture
    Write-PolicyFixture -Path $policyPath -Policy $basePolicy
    Write-SyncScriptFixture -ProvenanceRoot $provRoot -Policy $basePolicy
    & git -C $provRoot add -A 2>&1 | Out-Null
    & git -C $provRoot commit -q -m 'add parity source fixture' 2>&1 | Out-Null

    # -----------------------------------------------------------------
    # Case 3: missing provenance root
    # -----------------------------------------------------------------
    $missingProv = Join-Path $tempRoot 'does_not_exist_provenance'
    $r3 = Invoke-Mapper -ProvenanceRoot $missingProv -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r3.ExitCode -ne 0 -and $r3.Json.errors[0].code -eq 'MISSING_PROVENANCE_ROOT') 'missing_provenance_root' $r3.StdoutText

    # -----------------------------------------------------------------
    # Case 4: missing public root
    # -----------------------------------------------------------------
    $missingPub = Join-Path $tempRoot 'does_not_exist_public'
    $r4 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $missingPub -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r4.ExitCode -ne 0 -and $r4.Json.errors[0].code -eq 'MISSING_PUBLIC_ROOT') 'missing_public_root' $r4.StdoutText

    $missingCvfWeb = Join-Path $tempRoot 'does_not_exist_cvf_web'
    $r4b = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $missingCvfWeb -PolicyPath $policyPath
    Assert-True ($r4b.ExitCode -ne 0 -and $r4b.Json.errors[0].code -eq 'MISSING_CVF_WEB_ROOT') 'missing_cvf_web_root' $r4b.StdoutText

    # -----------------------------------------------------------------
    # Case 5: wrong provenance remote
    # -----------------------------------------------------------------
    $wrongProvRoot = Join-Path $tempRoot 'provenance_wrong_remote'
    New-DisposableGitRepo -Path $wrongProvRoot -OriginUrl 'https://example.invalid/totally-unrelated.git'
    $r5 = Invoke-Mapper -ProvenanceRoot $wrongProvRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r5.ExitCode -ne 0 -and $r5.Json.errors[0].code -eq 'WRONG_PROVENANCE_REMOTE') 'wrong_provenance_remote' $r5.StdoutText

    $spoofedProvRoot = Join-Path $tempRoot 'provenance_spoofed_remote'
    New-DisposableGitRepo -Path $spoofedProvRoot -OriginUrl 'https://evil.example.invalid/https://example.invalid/provenance-marker-repo.git'
    $r5b = Invoke-Mapper -ProvenanceRoot $spoofedProvRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r5b.ExitCode -ne 0 -and $r5b.Json.errors[0].code -eq 'WRONG_PROVENANCE_REMOTE') 'provenance_remote_substring_spoof_rejected' $r5b.StdoutText

    # -----------------------------------------------------------------
    # Case 6: wrong public remote
    # -----------------------------------------------------------------
    $wrongPubRoot = Join-Path $tempRoot 'public_wrong_remote'
    New-DisposableGitRepo -Path $wrongPubRoot -OriginUrl 'https://example.invalid/totally-unrelated-public.git'
    $r6 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $wrongPubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r6.ExitCode -ne 0 -and $r6.Json.errors[0].code -eq 'WRONG_PUBLIC_REMOTE') 'wrong_public_remote' $r6.StdoutText

    # -----------------------------------------------------------------
    # Case 7: dirty provenance root
    # -----------------------------------------------------------------
    $dirtyProvRoot = Join-Path $tempRoot 'provenance_dirty'
    New-DisposableGitRepo -Path $dirtyProvRoot -OriginUrl 'https://example.invalid/provenance-marker-repo.git'
    'dirt' | Out-File -FilePath (Join-Path $dirtyProvRoot 'DIRTY.txt') -Encoding utf8
    $r7 = Invoke-Mapper -ProvenanceRoot $dirtyProvRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r7.ExitCode -ne 0 -and $r7.Json.errors[0].code -eq 'DIRTY_PROVENANCE_ROOT') 'dirty_provenance_root' $r7.StdoutText

    # -----------------------------------------------------------------
    # Case 8: dirty public root
    # -----------------------------------------------------------------
    $dirtyPubRoot = Join-Path $tempRoot 'public_dirty'
    New-DisposableGitRepo -Path $dirtyPubRoot -OriginUrl 'https://example.invalid/public-sync.git'
    'dirt' | Out-File -FilePath (Join-Path $dirtyPubRoot 'DIRTY.txt') -Encoding utf8
    $r8 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $dirtyPubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r8.ExitCode -ne 0 -and $r8.Json.errors[0].code -eq 'DIRTY_PUBLIC_ROOT') 'dirty_public_root' $r8.StdoutText

    $missingParityRoot = Join-Path $tempRoot 'provenance_missing_parity_source'
    New-DisposableGitRepo -Path $missingParityRoot -OriginUrl 'https://example.invalid/provenance-marker-repo.git'
    $r8b = Invoke-Mapper -ProvenanceRoot $missingParityRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($r8b.ExitCode -ne 0 -and $r8b.Json.errors[0].code -eq 'POLICY_PARITY_FAILED') 'policy_parity_source_missing_fails_closed' $r8b.StdoutText

    $mismatchPolicyPath = Join-Path $tempRoot 'policy_mismatch.json'
    $mismatchPolicy = New-BasePolicyFixture
    $mismatchPolicy.allowedTrees = @('AllowedTree', 'UnexpectedTree')
    Write-PolicyFixture -Path $mismatchPolicyPath -Policy $mismatchPolicy
    $r8c = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $mismatchPolicyPath
    Assert-True ($r8c.ExitCode -ne 0 -and $r8c.Json.errors[0].code -eq 'POLICY_PARITY_FAILED') 'policy_parity_mismatch_fails_closed' $r8c.StdoutText

    # -----------------------------------------------------------------
    # Case 9: candidate destination path escape
    # (deny/allow classification never lets a targetPath leave PublicSyncRoot;
    #  verified by direct unit call to the mapper's containment guard pattern
    #  via a crafted policy mapped-file destination using .. traversal)
    # -----------------------------------------------------------------
    $escapePolicyPath = Join-Path $tempRoot 'policy_escape.json'
    $escapePolicy = New-BasePolicyFixture
    $escapePolicy.mappedFiles = @(
        [pscustomobject]@{ source = 'MappedSource.txt'; destination = '..\..\escaped.txt' }
    )
    Write-PolicyFixture -Path $escapePolicyPath -Policy $escapePolicy
    Write-SyncScriptFixture -ProvenanceRoot $provRoot -Policy $escapePolicy
    'mapped source content' | Out-File -FilePath (Join-Path $provRoot 'MappedSource.txt') -Encoding utf8
    & git -C $provRoot add -A 2>&1 | Out-Null
    & git -C $provRoot commit -q -m 'add mapped source' 2>&1 | Out-Null
    $r9 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $escapePolicyPath
    Assert-True ($r9.ExitCode -ne 0 -and $r9.Json.errors[0].code -eq 'PATH_ESCAPE') 'candidate_destination_path_escape' $r9.StdoutText
    Write-SyncScriptFixture -ProvenanceRoot $provRoot -Policy $basePolicy
    & git -C $provRoot add -A 2>&1 | Out-Null
    & git -C $provRoot commit -q -m 'restore parity source fixture' 2>&1 | Out-Null

    # -----------------------------------------------------------------
    # Case 10: receipt output path escape
    # -----------------------------------------------------------------
    $workDir = Join-Path $tempRoot 'workdir_for_escape'
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null
    $escapedReceiptPath = Join-Path $tempRoot 'escaped_receipt.json'
    $r10 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath '..\escaped_receipt.json' -WorkingDirectory $workDir
    Assert-True ($r10.ExitCode -ne 0 -and $r10.Json.errors[0].message -match 'PATH_ESCAPE') 'receipt_output_path_escape' $r10.StdoutText
    Assert-True (-not (Test-Path -LiteralPath $escapedReceiptPath)) 'receipt_output_path_escape_no_file_written' 'escaped receipt file was written'

    $receiptInsideTarget = Join-Path $provRoot 'receipt_forbidden.json'
    $r10b = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath 'receipt_forbidden.json' -WorkingDirectory $provRoot
    Assert-True ($r10b.ExitCode -ne 0 -and $r10b.Json.errors[0].code -eq 'RECEIPT_TARGET_ROOT_FORBIDDEN') 'receipt_inside_target_root_rejected' $r10b.StdoutText
    Assert-True (-not (Test-Path -LiteralPath $receiptInsideTarget)) 'receipt_inside_target_root_no_file_written' 'forbidden receipt file was written'

    # -----------------------------------------------------------------
    # Fixture for positive classification cases: reset provenance/public
    # to clean state with controlled allow/mapped/deny/unallowlisted files.
    # -----------------------------------------------------------------
    'allowed root content v1' | Out-File -FilePath (Join-Path $provRoot 'ALLOWED_ROOT.txt') -Encoding utf8
    New-Item -ItemType Directory -Path (Join-Path $provRoot 'AllowedTree') -Force | Out-Null
    'tree file content' | Out-File -FilePath (Join-Path $provRoot 'AllowedTree\inner.txt') -Encoding utf8
    'denied content' | Out-File -FilePath (Join-Path $provRoot 'DENY_ME_file.txt') -Encoding utf8
    'unlisted content' | Out-File -FilePath (Join-Path $provRoot 'UNLISTED_ROOT_FILE.txt') -Encoding utf8
    & git -C $provRoot add -A 2>&1 | Out-Null
    & git -C $provRoot commit -q -m 'add classification fixtures' 2>&1 | Out-Null

    'mapped destination existing but different' | Out-File -FilePath (Join-Path $pubRoot 'MappedDestination.txt') -Encoding utf8
    & git -C $pubRoot add -A 2>&1 | Out-Null
    & git -C $pubRoot commit -q -m 'seed mapped destination' 2>&1 | Out-Null

    $rPositive = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    $nonMatchingParity = @($rPositive.Json.policyParity.PSObject.Properties | Where-Object { $_.Value -ne 'MATCH' })
    Assert-True ($rPositive.ExitCode -eq 0 -and $nonMatchingParity.Count -eq 0) 'policy_parity_all_groups_match' ($rPositive.StdoutText)
    Assert-True ($rPositive.Json.pathEscapeChecksRun -eq $rPositive.Json.candidates.Count) 'path_escape_count_without_receipt_reconciles' ($rPositive.StdoutText)

    # -----------------------------------------------------------------
    # Case 11: absent-target candidate
    # -----------------------------------------------------------------
    $absentRow = $rPositive.Json.candidates | Where-Object { $_.sourcePath -eq 'ALLOWED_ROOT.txt' }
    Assert-True ($null -ne $absentRow -and $absentRow.candidateAction -eq 'COPY_CANDIDATE_ABSENT_TARGET') 'absent_target_candidate' ($rPositive.StdoutText)

    # -----------------------------------------------------------------
    # Case 12: changed-content semantic-review flag (mapped file differs)
    # -----------------------------------------------------------------
    $changedRow = $rPositive.Json.candidates | Where-Object { $_.sourcePath -eq 'MappedSource.txt' }
    Assert-True ($null -ne $changedRow -and $changedRow.candidateAction -eq 'FLAG_SEMANTIC_REVIEW_CHANGED') 'changed_content_semantic_review_flag' ($rPositive.StdoutText)

    # -----------------------------------------------------------------
    # Case 13: unchanged skip
    # -----------------------------------------------------------------
    'byte identical readme' | Out-File -FilePath (Join-Path $provRoot 'README.md') -Encoding utf8 -NoNewline
    & git -C $provRoot add -A 2>&1 | Out-Null
    & git -C $provRoot commit -q -m 'stabilize readme' 2>&1 | Out-Null
    'byte identical readme' | Out-File -FilePath (Join-Path $pubRoot 'README.md') -Encoding utf8 -NoNewline
    & git -C $pubRoot add -A 2>&1 | Out-Null
    & git -C $pubRoot commit -q -m 'stabilize readme' 2>&1 | Out-Null
    $rUnchanged = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    $unchangedRow = $rUnchanged.Json.candidates | Where-Object { $_.sourcePath -eq 'README.md' }
    Assert-True ($null -ne $unchangedRow -and $unchangedRow.candidateAction -eq 'SKIP_UNCHANGED') 'unchanged_skip' ($rUnchanged.StdoutText)

    # -----------------------------------------------------------------
    # Case 14: mapped export destination
    # -----------------------------------------------------------------
    Assert-True ($null -ne $changedRow -and $changedRow.targetPath -eq 'MappedDestination.txt') 'mapped_export_destination' ($rPositive.StdoutText)

    # -----------------------------------------------------------------
    # Case 15: deny and not-allowlisted dispositions
    # -----------------------------------------------------------------
    $denyRow = $rPositive.Json.candidates | Where-Object { $_.sourcePath -eq 'DENY_ME_file.txt' }
    Assert-True ($null -ne $denyRow -and $denyRow.candidateAction -eq 'SKIP_DENIED') 'deny_disposition' ($rPositive.StdoutText)
    $notAllowRow = $rPositive.Json.candidates | Where-Object { $_.sourcePath -eq 'UNLISTED_ROOT_FILE.txt' }
    Assert-True ($null -ne $notAllowRow -and $notAllowRow.candidateAction -eq 'SKIP_NOT_ALLOWLISTED') 'not_allowlisted_disposition' ($rPositive.StdoutText)

    # -----------------------------------------------------------------
    # Case 16: all three current SOT3 registry entries observed
    # -----------------------------------------------------------------
    $sot3Rows = $rPositive.Json.cvfWebObservation.sot3ObservedEntries
    $allThreePresent = ($sot3Rows | Where-Object { $_.presentInDependencies -and $_.presentInRegistry }).Count -eq 3
    Assert-True $allThreePresent 'sot3_registry_entries_observed' ($sot3Rows | ConvertTo-Json -Compress)

    # -----------------------------------------------------------------
    # Case 17: two identical runs produce byte-identical JSON and receipt ID
    # -----------------------------------------------------------------
    $rRun1 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    $rRun2 = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($rRun1.StdoutText -eq $rRun2.StdoutText) 'deterministic_repeated_run_byte_identical' 'stdout differed between runs'
    Assert-True ($rRun1.Json.receiptId -eq $rRun2.Json.receiptId -and $rRun1.Json.receiptId) 'deterministic_repeated_run_receipt_id' 'receiptId differed or empty'

    # -----------------------------------------------------------------
    # Case 18: no target filesystem or git-status change before/after
    # -----------------------------------------------------------------
    $provStatusBefore = (& git -C $provRoot status --porcelain) -join "`n"
    $pubStatusBefore = (& git -C $pubRoot status --porcelain) -join "`n"
    $provFilesBefore = Get-ChildItem -LiteralPath $provRoot -Recurse -File | ForEach-Object { $_.FullName } | Sort-Object
    $pubFilesBefore = Get-ChildItem -LiteralPath $pubRoot -Recurse -File | ForEach-Object { $_.FullName } | Sort-Object
    $null = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    $provStatusAfter = (& git -C $provRoot status --porcelain) -join "`n"
    $pubStatusAfter = (& git -C $pubRoot status --porcelain) -join "`n"
    $provFilesAfter = Get-ChildItem -LiteralPath $provRoot -Recurse -File | ForEach-Object { $_.FullName } | Sort-Object
    $pubFilesAfter = Get-ChildItem -LiteralPath $pubRoot -Recurse -File | ForEach-Object { $_.FullName } | Sort-Object
    Assert-True ($provStatusBefore -eq $provStatusAfter) 'no_target_git_status_change_provenance' 'provenance git status changed'
    Assert-True ($pubStatusBefore -eq $pubStatusAfter) 'no_target_git_status_change_public' 'public-sync git status changed'
    $provFilesDiff = Compare-Object -ReferenceObject $provFilesBefore -DifferenceObject $provFilesAfter -SyncWindow 0
    $pubFilesDiff = Compare-Object -ReferenceObject $pubFilesBefore -DifferenceObject $pubFilesAfter -SyncWindow 0
    Assert-True (@($provFilesDiff).Count -eq 0) 'no_target_filesystem_change_provenance' ($provFilesDiff | Out-String)
    Assert-True (@($pubFilesDiff).Count -eq 0) 'no_target_filesystem_change_public' ($pubFilesDiff | Out-String)

    # -----------------------------------------------------------------
    # Case 19: secret-like fixture value is not emitted
    # -----------------------------------------------------------------
    $secretMarker = 'SECRET_TOKEN_zK9x7QpL3vN8'
    "$secretMarker=do-not-leak" | Out-File -FilePath (Join-Path $provRoot '.env.fixture.txt') -Encoding utf8
    & git -C $provRoot add -A 2>&1 | Out-Null
    & git -C $provRoot commit -q -m 'add secret-like fixture' 2>&1 | Out-Null
    $rSecret = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath
    Assert-True ($rSecret.StdoutText -notmatch [regex]::Escape($secretMarker)) 'secret_like_fixture_value_not_emitted' 'secret marker leaked into output'

    # -----------------------------------------------------------------
    # Case 20 (bonus): explicit ReceiptOutputPath writes exactly one file
    # inside the working directory, and its content matches stdout JSON.
    # -----------------------------------------------------------------
    $receiptWorkDir = Join-Path $tempRoot 'receipt_workdir'
    New-Item -ItemType Directory -Path $receiptWorkDir -Force | Out-Null
    $receiptRelPath = 'receipt_out.json'
    $rReceipt = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath $receiptRelPath -WorkingDirectory $receiptWorkDir
    $receiptFileFull = Join-Path $receiptWorkDir $receiptRelPath
    $receiptExists = Test-Path -LiteralPath $receiptFileFull -PathType Leaf
    Assert-True $receiptExists 'receipt_output_path_file_written' $rReceipt.StdoutText
    $contentMatches = $false
    if ($receiptExists) {
        $receiptFileText = Get-Content -LiteralPath $receiptFileFull -Raw -Encoding utf8
        $normalizedFile = $receiptFileText.Trim() -replace "`r`n", "`n"
        $normalizedStdout = $rReceipt.StdoutText.Trim() -replace "`r`n", "`n"
        $contentMatches = $normalizedFile -eq $normalizedStdout
    }
    if ($receiptExists -and -not $contentMatches) {
        Write-Host "DIAG file length: $($normalizedFile.Length) stdout length: $($normalizedStdout.Length)"
        $minLen = [Math]::Min($normalizedFile.Length, $normalizedStdout.Length)
        for ($i = 0; $i -lt $minLen; $i++) {
            if ($normalizedFile[$i] -ne $normalizedStdout[$i]) {
                Write-Host "DIAG first diff at index $i : file='$($normalizedFile.Substring([Math]::Max(0,$i-20), [Math]::Min(40, $normalizedFile.Length-[Math]::Max(0,$i-20))))' stdout='$($normalizedStdout.Substring([Math]::Max(0,$i-20), [Math]::Min(40, $normalizedStdout.Length-[Math]::Max(0,$i-20))))'"
                break
            }
        }
    }
    Assert-True $contentMatches 'receipt_output_path_content_matches_stdout' 'receipt file content differs from stdout'

    if ($GovernedReceiptPath) {
        $governedRoot = (Resolve-Path (Join-Path $scriptRoot '..')).ProviderPath
        $governedRun = Invoke-Mapper -ProvenanceRoot $provRoot -PublicSyncRoot $pubRoot -CvfWebRoot $cvfWebRoot -PolicyPath $policyPath -ReceiptOutputPath $GovernedReceiptPath -WorkingDirectory $governedRoot
        Assert-True ($governedRun.ExitCode -eq 0) 'governed_receipt_generated' $governedRun.StdoutText
        Assert-True (Test-Path -LiteralPath $GovernedReceiptPath -PathType Leaf) 'governed_receipt_path_exists' 'governed receipt was not written'
    }

    # -----------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------
    Write-Host ''
    Write-Host '=== CVF Projection Mapper Focused Test Matrix ===' -ForegroundColor Cyan
    $script:results | ForEach-Object {
        if ($_ -like 'PASS:*') { Write-Host $_ -ForegroundColor Green } else { Write-Host $_ -ForegroundColor Red }
    }
    Write-Host ''
    Write-Host "TOTAL: $($script:passCount + $script:failCount)  PASS: $($script:passCount)  FAIL: $($script:failCount)" -ForegroundColor Cyan

    if ($script:failCount -gt 0) {
        exit 1
    }
    exit 0
} finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
