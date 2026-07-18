<#
.SYNOPSIS
    CVF Projection Automation dry-run mapper (T1).

.DESCRIPTION
    Read-only, fail-closed inspection tool. It reports how the private
    provenance root WOULD map onto a public-sync root under the policy in
    scripts\cvf_projection_policy.json, and compares cvf-web package
    dependencies and runtime-module registry entries against that policy's
    expected SOT3 entries.

    This script performs NO target mutation. It never copies, writes, or
    modifies any file inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.
    It never edits scripts\cvf-public-sync.ps1 and never dot-sources or
    invokes it. The only filesystem write this script may perform is the
    JSON receipt at -ReceiptOutputPath, and only after that path passes a
    path-containment check against the current working directory. If
    -ReceiptOutputPath is omitted, the receipt JSON is written to stdout
    only and no file is created.

    Candidate actions are classification labels only:
      COPY_CANDIDATE_ABSENT_TARGET - allowlisted source file, absent at target.
      FLAG_SEMANTIC_REVIEW_CHANGED - allowlisted source file, byte-different at target.
      SKIP_UNCHANGED               - allowlisted source file, byte-identical at target.
      SKIP_DENIED                  - source file matches a deny pattern.
      SKIP_NOT_ALLOWLISTED         - source file matches no allow group.

    No candidate is ever applied, copied, or auto-approved by this script.

.PARAMETER ProvenanceRoot
    Path to the private provenance repository root. Must exist, must be a
    clean git worktree, and must have an 'origin' remote exactly equal to the
    expected provenance remote from the policy file.

.PARAMETER PublicSyncRoot
    Path to the public-sync repository root. Must exist, must be a clean git
    worktree, and must have an 'origin' remote equal to the policy file's
    exact public remote URL.

.PARAMETER CvfWebRoot
    Path to the cvf-web package root (normally
    EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web under ProvenanceRoot). Used
    only to read package.json and the runtime-modules.ts registry source
    text; never modified.

.PARAMETER PolicyPath
    Path to the JSON policy manifest (scripts\cvf_projection_policy.json).

.PARAMETER ReceiptOutputPath
    Optional. If supplied, the deterministic JSON receipt is also written to
    this path after a path-containment check against the current directory.
    If omitted, the receipt is written to stdout only.

.OUTPUTS
    A single deterministic JSON object (the receipt) is always emitted to
    stdout as the last output of a successful run.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\get_cvf_projection_map.ps1 `
      -ProvenanceRoot "D:\repo" -PublicSyncRoot "D:\repo-public-sync" `
      -CvfWebRoot "D:\repo\EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web" `
      -PolicyPath "D:\repo\scripts\cvf_projection_policy.json"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProvenanceRoot,

    [Parameter(Mandatory = $true)]
    [string]$PublicSyncRoot,

    [Parameter(Mandatory = $true)]
    [string]$CvfWebRoot,

    [Parameter(Mandatory = $true)]
    [string]$PolicyPath,

    [string]$ReceiptOutputPath
)

$ErrorActionPreference = 'Stop'

function New-MapperErrorMessage {
    param([string]$Code, [string]$Message)
    return "$Code`: $Message"
}

function Get-CanonicalPath {
    param([string]$Path)
    return [System.IO.Path]::GetFullPath($Path)
}

function Assert-PathContainment {
    <# Mirrors the source-proven guard in
       scripts\update_cvf_workspace_public_core.ps1 (Assert-PathInsideWorkspace,
       lines 59-66): resolve both paths to absolute form and require the
       candidate to start with the container's prefix. Reused as read-only
       validation logic only; this script does not dot-source or call that
       script. #>
    param([string]$CandidatePath, [string]$ContainerPath)
    $resolvedCandidate = [System.IO.Path]::GetFullPath($CandidatePath)
    $resolvedContainer = [System.IO.Path]::GetFullPath($ContainerPath).TrimEnd('\') + '\'
    if (-not $resolvedCandidate.StartsWith($resolvedContainer, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "PATH_ESCAPE: '$resolvedCandidate' is not contained within '$resolvedContainer'"
    }
    return $resolvedCandidate
}

function Test-PathContained {
    param([string]$CandidatePath, [string]$ContainerPath)
    $resolvedCandidate = [System.IO.Path]::GetFullPath($CandidatePath)
    $resolvedContainer = [System.IO.Path]::GetFullPath($ContainerPath).TrimEnd('\') + '\'
    return $resolvedCandidate.StartsWith($resolvedContainer, [System.StringComparison]::OrdinalIgnoreCase)
}

function Get-Sha256Hex {
    param([byte[]]$Bytes)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $hash = $sha.ComputeHash($Bytes)
        return -join ($hash | ForEach-Object { $_.ToString('x2') })
    } finally {
        $sha.Dispose()
    }
}

function Get-Utf8Bytes {
    param([string]$Text)
    return [System.Text.Encoding]::UTF8.GetBytes($Text)
}

function Test-GitClean {
    param([string]$RepoRoot)
    $out = & git -C $RepoRoot status --porcelain 2>$null
    return [string]::IsNullOrWhiteSpace(($out -join "`n"))
}

function Get-GitOriginRemote {
    param([string]$RepoRoot)
    $remote = & git -C $RepoRoot remote get-url origin 2>$null
    if ($LASTEXITCODE -ne 0) { return $null }
    return ($remote | Select-Object -First 1)
}

function ConvertTo-RelativePath {
    param([string]$Root, [string]$FullPath)
    $rootFull = [System.IO.Path]::GetFullPath($Root).TrimEnd('\')
    $itemFull = [System.IO.Path]::GetFullPath($FullPath)
    $rel = $itemFull.Substring($rootFull.Length + 1)
    return ($rel -replace '\\', '/')
}

function Test-DenyMatch {
    param([string]$RelPath, [string[]]$DenyPatterns)
    foreach ($pattern in $DenyPatterns) {
        if ($RelPath -match $pattern) { return $true }
    }
    return $false
}

function Get-AllowGroupMatch {
    <# Returns the matched allow-group name, or $null if RelPath matches no
       allow group. Order mirrors cvf-public-sync.ps1 Get-AllowedFiles:
       root files, script files, workspace templates, allowed trees, docs
       sub-paths, then mapped-file sources are checked separately by the
       caller. #>
    param([string]$RelPath, [pscustomobject]$Policy)

    if ($Policy.allowedRootFiles -contains $RelPath) { return 'allowedRootFiles' }
    if ($Policy.allowedScriptFiles -contains $RelPath) { return 'allowedScriptFiles' }
    if ($Policy.allowedWorkspaceTemplateFiles -contains $RelPath) { return 'allowedWorkspaceTemplateFiles' }

    foreach ($tree in $Policy.allowedTrees) {
        $prefix = "$tree/"
        if ($RelPath -eq $tree -or $RelPath.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            return 'allowedTrees'
        }
    }

    foreach ($docPath in $Policy.allowedDocsPaths) {
        $prefix = "$docPath/"
        if ($RelPath -eq $docPath -or $RelPath.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            return 'allowedDocsPaths'
        }
    }

    return $null
}

function Get-CandidateRow {
    param(
        [string]$RelPath,
        [string]$SourceFull,
        [string]$TargetRoot,
        [string]$TargetRelOverride,
        [pscustomobject]$Policy,
        [string]$MatchedRule
    )

    $targetRel = if ($TargetRelOverride) { $TargetRelOverride } else { $RelPath }
    $targetFull = Join-Path $TargetRoot ($targetRel -replace '/', '\')

    if (Test-DenyMatch -RelPath $RelPath -DenyPatterns $Policy.denyPatterns) {
        return [pscustomobject]@{
            sourcePath           = $RelPath
            targetPath           = $targetRel
            candidateAction      = 'SKIP_DENIED'
            matchedAllowlistRule = $null
            matchedDenyPattern   = ($Policy.denyPatterns | Where-Object { $RelPath -match $_ } | Select-Object -First 1)
        }
    }

    if (-not (Test-Path -LiteralPath $targetFull -PathType Leaf)) {
        return [pscustomobject]@{
            sourcePath           = $RelPath
            targetPath           = $targetRel
            candidateAction      = 'COPY_CANDIDATE_ABSENT_TARGET'
            matchedAllowlistRule = $MatchedRule
            matchedDenyPattern   = $null
        }
    }

    $sourceBytes = [System.IO.File]::ReadAllBytes($SourceFull)
    $targetBytes = [System.IO.File]::ReadAllBytes($targetFull)
    $sourceHash = Get-Sha256Hex -Bytes $sourceBytes
    $targetHash = Get-Sha256Hex -Bytes $targetBytes

    if ($sourceHash -eq $targetHash) {
        return [pscustomobject]@{
            sourcePath           = $RelPath
            targetPath           = $targetRel
            candidateAction      = 'SKIP_UNCHANGED'
            matchedAllowlistRule = $MatchedRule
            matchedDenyPattern   = $null
        }
    }

    return [pscustomobject]@{
        sourcePath           = $RelPath
        targetPath           = $targetRel
        candidateAction      = 'FLAG_SEMANTIC_REVIEW_CHANGED'
        matchedAllowlistRule = $MatchedRule
        matchedDenyPattern   = $null
    }
}

function Get-PolicyParityReport {
    <# Parses current cvf-public-sync.ps1 text for its literal array
       assignments and compares the parsed values to the policy JSON, WITHOUT
       executing or dot-sourcing the script. #>
    param([string]$SyncScriptPath, [pscustomobject]$Policy)

    $groups = [ordered]@{
        allowedTrees                  = $Policy.allowedTrees
        allowedRootFiles              = $Policy.allowedRootFiles
        allowedScriptFiles            = $Policy.allowedScriptFiles
        allowedWorkspaceTemplateFiles = $Policy.allowedWorkspaceTemplateFiles
        allowedDocsPaths              = $Policy.allowedDocsPaths
        denyPatterns                  = $Policy.denyPatterns
    }

    $result = [ordered]@{}

    if (-not (Test-Path -LiteralPath $SyncScriptPath -PathType Leaf)) {
        foreach ($key in $groups.Keys) { $result[$key] = 'SOURCE_MISSING' }
        $result['publicRemote'] = 'SOURCE_MISSING'
        $result['mappedFiles'] = 'SOURCE_MISSING'
        return [pscustomobject]$result
    }

    $scriptText = Get-Content -LiteralPath $SyncScriptPath -Raw -Encoding utf8

    function Get-PsArrayValues {
        param([string]$Text, [string]$VarName)
        $pattern = "(?ms)\`$$VarName\s*=\s*@\((.*?)\r?\n\)"
        $m = [regex]::Match($Text, $pattern)
        if (-not $m.Success) { return @() }
        $body = $m.Groups[1].Value
        $lines = [regex]::Matches($body, "'([^']*)'|`"([^`"]*)`"")
        $values = @()
        foreach ($lm in $lines) {
            $val = if ($lm.Groups[1].Success) { $lm.Groups[1].Value } else { $lm.Groups[2].Value }
            if ($val -notmatch '^\s*#') { $values += $val }
        }
        return $values
    }

    $varMap = [ordered]@{
        allowedTrees                  = 'ALLOWED_TREES'
        allowedRootFiles              = 'ALLOWED_ROOT_FILES'
        allowedScriptFiles            = 'ALLOWED_SCRIPT_FILES'
        allowedWorkspaceTemplateFiles = 'ALLOWED_WORKSPACE_TEMPLATE_FILES'
        allowedDocsPaths              = 'ALLOWED_DOCS_PATHS'
        denyPatterns                  = 'DENY_PATTERNS'
    }

    foreach ($key in $groups.Keys) {
        $scriptValuesRaw = Get-PsArrayValues -Text $scriptText -VarName $varMap[$key]
        if ($key -eq 'denyPatterns') {
            $scriptValues = @($scriptValuesRaw | Sort-Object)
            $policyValues = @($groups[$key] | Sort-Object)
        } else {
            $scriptValues = @($scriptValuesRaw | ForEach-Object { $_ -replace '\\', '/' } | Sort-Object)
            $policyValues = @($groups[$key] | ForEach-Object { $_ -replace '\\', '/' } | Sort-Object)
        }
        $diff = if ($scriptValues.Count -eq 0 -and $policyValues.Count -eq 0) { @() } else { @(Compare-Object -ReferenceObject $policyValues -DifferenceObject $scriptValues -SyncWindow 0) }
        $result[$key] = if ($null -eq $diff -or @($diff).Count -eq 0) { 'MATCH' } else { 'MISMATCH' }
    }

    $remoteMatch = [regex]::Match($scriptText, "\`$PUBLIC_REMOTE\s*=\s*'([^']+)'")
    $result['publicRemote'] = if ($remoteMatch.Success -and $remoteMatch.Groups[1].Value -eq $Policy.expectedRemotes.publicRemote) { 'MATCH' } else { 'MISMATCH' }

    $mappedMatch = [regex]::Matches($scriptText, "Source\s*=\s*'([^']+)'\s*\r?\n\s*Destination\s*=\s*'([^']+)'")
    $scriptMapped = @()
    foreach ($mm in $mappedMatch) {
        $scriptMapped += "$($mm.Groups[1].Value -replace '\\','/')=>$($mm.Groups[2].Value -replace '\\','/')"
    }
    $policyMapped = @($Policy.mappedFiles | ForEach-Object { "$(($_.source -replace '\\','/'))=>$(($_.destination -replace '\\','/'))" })
    $scriptMapped = @($scriptMapped)
    $mappedDiff = if ($policyMapped.Count -eq 0 -and $scriptMapped.Count -eq 0) { @() } else { @(Compare-Object -ReferenceObject ($policyMapped | Sort-Object) -DifferenceObject ($scriptMapped | Sort-Object) -SyncWindow 0) }
    $result['mappedFiles'] = if ($null -eq $mappedDiff -or @($mappedDiff).Count -eq 0) { 'MATCH' } else { 'MISMATCH' }

    return [pscustomobject]$result
}

function Get-CvfWebObservation {
    param([pscustomobject]$Policy, [string]$CvfWebRootResolved)

    $pkgPath = Join-Path (Split-Path -Parent (Split-Path -Parent $CvfWebRootResolved)) ''
    $packageJsonFull = Join-Path $CvfWebRootResolved 'package.json'
    $registryFull = Join-Path $CvfWebRootResolved 'src\lib\server\runtime-modules.ts'

    $dependencies = @()
    if (Test-Path -LiteralPath $packageJsonFull -PathType Leaf) {
        $pkgJson = Get-Content -LiteralPath $packageJsonFull -Raw -Encoding utf8 | ConvertFrom-Json
        if ($pkgJson.dependencies) {
            $dependencies = @($pkgJson.dependencies.PSObject.Properties.Name | Sort-Object)
        }
    }

    $registryIds = @()
    if (Test-Path -LiteralPath $registryFull -PathType Leaf) {
        $registryText = Get-Content -LiteralPath $registryFull -Raw -Encoding utf8
        $idMatches = [regex]::Matches($registryText, "id:\s*'([^']+)'")
        foreach ($m in $idMatches) { $registryIds += $m.Groups[1].Value }
        $registryIds = @($registryIds | Sort-Object)
    }

    $expectedSot3 = $Policy.cvfWebObservation.expectedSot3RegistryIds | Sort-Object
    $observedSot3 = @($expectedSot3 | ForEach-Object {
        [pscustomobject]@{
            id                    = $_
            presentInDependencies = [bool]($dependencies -contains $_)
            presentInRegistry     = [bool]($registryIds -contains $_)
        }
    })

    $inconsistencies = @()
    foreach ($row in $observedSot3) {
        if ($row.presentInDependencies -and -not $row.presentInRegistry) {
            $inconsistencies += "SOT3_DEPENDENCY_PRESENT_REGISTRY_MISSING:$($row.id)"
        }
    }
    $inconsistencies = @($inconsistencies)

    return [pscustomobject]@{
        dependencyCount         = $dependencies.Count
        registryEntryCount      = $registryIds.Count
        sot3ObservedEntries     = $observedSot3
        semanticReviewFlags     = $inconsistencies
    }
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

$errors = [System.Collections.Generic.List[object]]::new()
$rootsValidated = [ordered]@{
    provenance = 'FAIL'
    publicSync = 'FAIL'
}

try {
    if (-not (Test-Path -LiteralPath $ProvenanceRoot -PathType Container)) {
        throw (New-MapperErrorMessage -Code 'MISSING_PROVENANCE_ROOT' -Message "Provenance root not found: $ProvenanceRoot")
    }
    if (-not (Test-Path -LiteralPath $PublicSyncRoot -PathType Container)) {
        throw (New-MapperErrorMessage -Code 'MISSING_PUBLIC_ROOT' -Message "Public-sync root not found: $PublicSyncRoot")
    }
    if (-not (Test-Path -LiteralPath $CvfWebRoot -PathType Container)) {
        throw (New-MapperErrorMessage -Code 'MISSING_CVF_WEB_ROOT' -Message "cvf-web root not found: $CvfWebRoot")
    }
    if (-not (Test-Path -LiteralPath $PolicyPath -PathType Leaf)) {
        throw (New-MapperErrorMessage -Code 'MISSING_POLICY' -Message "Policy file not found: $PolicyPath")
    }

    $provenanceRootResolved = Get-CanonicalPath -Path $ProvenanceRoot
    $publicSyncRootResolved = Get-CanonicalPath -Path $PublicSyncRoot
    $cvfWebRootResolved     = Get-CanonicalPath -Path $CvfWebRoot
    $policyResolved         = Get-CanonicalPath -Path $PolicyPath

    $policy = Get-Content -LiteralPath $policyResolved -Raw -Encoding utf8 | ConvertFrom-Json

    $provenanceRemote = Get-GitOriginRemote -RepoRoot $provenanceRootResolved
    if ($provenanceRemote -ne $policy.expectedRemotes.provenanceRemote) {
        throw (New-MapperErrorMessage -Code 'WRONG_PROVENANCE_REMOTE' -Message "Provenance origin remote does not match expected value. Found: $provenanceRemote")
    }
    $rootsValidated.provenance = 'PASS'

    $publicRemote = Get-GitOriginRemote -RepoRoot $publicSyncRootResolved
    if ($publicRemote -ne $policy.expectedRemotes.publicRemote) {
        throw (New-MapperErrorMessage -Code 'WRONG_PUBLIC_REMOTE' -Message "Public-sync origin remote does not match expected value. Found: $publicRemote")
    }
    $rootsValidated.publicSync = 'PASS'

    if (-not (Test-GitClean -RepoRoot $provenanceRootResolved)) {
        throw (New-MapperErrorMessage -Code 'DIRTY_PROVENANCE_ROOT' -Message 'Provenance root has uncommitted changes; refusing to map a dirty source.')
    }
    if (-not (Test-GitClean -RepoRoot $publicSyncRootResolved)) {
        throw (New-MapperErrorMessage -Code 'DIRTY_PUBLIC_ROOT' -Message 'Public-sync root has uncommitted changes; refusing to map onto a dirty target.')
    }

    $resolvedReceiptPath = $null
    if ($ReceiptOutputPath) {
        $cwdContainer = (Get-Location).ProviderPath
        $resolvedReceiptPath = Assert-PathContainment -CandidatePath $ReceiptOutputPath -ContainerPath $cwdContainer
        foreach ($readOnlyRoot in @($provenanceRootResolved, $publicSyncRootResolved, $cvfWebRootResolved)) {
            if (Test-PathContained -CandidatePath $resolvedReceiptPath -ContainerPath $readOnlyRoot) {
                throw (New-MapperErrorMessage -Code 'RECEIPT_TARGET_ROOT_FORBIDDEN' -Message "Receipt output must remain outside every read-only target root: $resolvedReceiptPath")
            }
        }
    }

    $candidates = [System.Collections.Generic.List[object]]::new()
    $deniedCount = 0
    $notAllowlistedCount = 0

    $mappedSourceSet = @{}
    foreach ($mapped in $policy.mappedFiles) {
        $mappedSourceSet[$mapped.source] = $mapped.destination
    }

    $allSourceRels = [System.Collections.Generic.List[string]]::new()

    foreach ($rel in $policy.allowedRootFiles) {
        $full = Join-Path $provenanceRootResolved ($rel -replace '/', '\')
        if (Test-Path -LiteralPath $full -PathType Leaf) { $allSourceRels.Add($rel) }
    }
    foreach ($rel in $policy.allowedScriptFiles) {
        $full = Join-Path $provenanceRootResolved ($rel -replace '/', '\')
        if (Test-Path -LiteralPath $full -PathType Leaf) { $allSourceRels.Add($rel) }
    }
    foreach ($rel in $policy.allowedWorkspaceTemplateFiles) {
        $full = Join-Path $provenanceRootResolved ($rel -replace '/', '\')
        if (Test-Path -LiteralPath $full -PathType Leaf) { $allSourceRels.Add($rel) }
    }
    foreach ($tree in $policy.allowedTrees) {
        $treeFull = Join-Path $provenanceRootResolved ($tree -replace '/', '\')
        if (Test-Path -LiteralPath $treeFull -PathType Container) {
            Get-ChildItem -LiteralPath $treeFull -Recurse -File | ForEach-Object {
                $rel = ConvertTo-RelativePath -Root $provenanceRootResolved -FullPath $_.FullName
                $allSourceRels.Add($rel)
            }
        }
    }
    foreach ($docPath in $policy.allowedDocsPaths) {
        $docFull = Join-Path $provenanceRootResolved ($docPath -replace '/', '\')
        if (Test-Path -LiteralPath $docFull -PathType Leaf) {
            $allSourceRels.Add($docPath)
        } elseif (Test-Path -LiteralPath $docFull -PathType Container) {
            Get-ChildItem -LiteralPath $docFull -Recurse -File | ForEach-Object {
                $rel = ConvertTo-RelativePath -Root $provenanceRootResolved -FullPath $_.FullName
                $allSourceRels.Add($rel)
            }
        }
    }

    # Also enumerate a bounded probe set for not-allowlisted / denied
    # classification: any file directly at provenance root not already
    # covered by allowedRootFiles.
    $rootProbe = Get-ChildItem -LiteralPath $provenanceRootResolved -File -Force |
        ForEach-Object { $_.Name } |
        Where-Object { $_ -notin $policy.allowedRootFiles }
    foreach ($rel in $rootProbe) { $allSourceRels.Add($rel) }

    $orderedSourceRels = $allSourceRels | Sort-Object -Unique

    foreach ($rel in $orderedSourceRels) {
        $sourceFull = Join-Path $provenanceRootResolved ($rel -replace '/', '\')
        if (-not (Test-Path -LiteralPath $sourceFull -PathType Leaf)) { continue }

        if (Test-DenyMatch -RelPath $rel -DenyPatterns $policy.denyPatterns) {
            $row = Get-CandidateRow -RelPath $rel -SourceFull $sourceFull -TargetRoot $publicSyncRootResolved -Policy $policy -MatchedRule $null
            $candidates.Add($row)
            $deniedCount++
            continue
        }

        $matchedRule = Get-AllowGroupMatch -RelPath $rel -Policy $policy
        if (-not $matchedRule) {
            $candidates.Add([pscustomobject]@{
                sourcePath           = $rel
                targetPath           = $rel
                candidateAction      = 'SKIP_NOT_ALLOWLISTED'
                matchedAllowlistRule = $null
                matchedDenyPattern   = $null
            })
            $notAllowlistedCount++
            continue
        }

        $row = Get-CandidateRow -RelPath $rel -SourceFull $sourceFull -TargetRoot $publicSyncRootResolved -Policy $policy -MatchedRule $matchedRule
        $candidates.Add($row)
    }

    foreach ($mapped in $policy.mappedFiles) {
        $sourceFull = Join-Path $provenanceRootResolved ($mapped.source -replace '/', '\')
        if (-not (Test-Path -LiteralPath $sourceFull -PathType Leaf)) { continue }
        $row = Get-CandidateRow -RelPath $mapped.source -SourceFull $sourceFull -TargetRoot $publicSyncRootResolved -TargetRelOverride $mapped.destination -Policy $policy -MatchedRule 'mappedFiles'
        $candidates.Add($row)
    }

    $orderedCandidates = @($candidates | Sort-Object -Property sourcePath, targetPath)

    $absentTargetCount = @($orderedCandidates | Where-Object { $_.candidateAction -eq 'COPY_CANDIDATE_ABSENT_TARGET' }).Count
    $semanticReviewCount = @($orderedCandidates | Where-Object { $_.candidateAction -eq 'FLAG_SEMANTIC_REVIEW_CHANGED' }).Count
    $unchangedCount = @($orderedCandidates | Where-Object { $_.candidateAction -eq 'SKIP_UNCHANGED' }).Count
    $deniedCount = @($orderedCandidates | Where-Object { $_.candidateAction -eq 'SKIP_DENIED' }).Count
    $notAllowlistedCount = @($orderedCandidates | Where-Object { $_.candidateAction -eq 'SKIP_NOT_ALLOWLISTED' }).Count

    $policyParity = Get-PolicyParityReport -SyncScriptPath (Join-Path $provenanceRootResolved 'scripts\cvf-public-sync.ps1') -Policy $policy
    $parityFailures = @($policyParity.PSObject.Properties | Where-Object { $_.Value -ne 'MATCH' })
    if ($parityFailures.Count -gt 0) {
        $failedGroups = ($parityFailures | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join ', '
        throw (New-MapperErrorMessage -Code 'POLICY_PARITY_FAILED' -Message "Projection policy does not match its source-of-truth script: $failedGroups")
    }
    $cvfWebObservation = Get-CvfWebObservation -Policy $policy -CvfWebRootResolved $cvfWebRootResolved

    $pathEscapeChecksRun = $orderedCandidates.Count + $(if ($ReceiptOutputPath) { 1 } else { 0 })
    foreach ($c in $orderedCandidates) {
        $null = Assert-PathContainment -CandidatePath (Join-Path $publicSyncRootResolved ($c.targetPath -replace '/', '\')) -ContainerPath $publicSyncRootResolved
    }

    $summary = [ordered]@{
        totalCandidates          = $orderedCandidates.Count
        copyCandidateAbsentCount = $absentTargetCount
        semanticReviewFlagCount  = $semanticReviewCount
        skipUnchangedCount       = $unchangedCount
        deniedPathCount          = $deniedCount
        notAllowlistedCount      = $notAllowlistedCount
    }
    $reconciledTotal = $absentTargetCount + $semanticReviewCount + $unchangedCount + $deniedCount + $notAllowlistedCount
    $summary['reconciliationMatch'] = ($reconciledTotal -eq $orderedCandidates.Count)

    $receiptBody = [ordered]@{
        schemaVersion              = $policy.schemaVersion
        sourceRoot                 = 'PROVENANCE_ROOT'
        targetRoot                 = 'PUBLIC_SYNC_ROOT'
        cvfWebRoot                 = 'CVF_WEB_ROOT'
        rootsValidated              = $rootsValidated
        policyParity                = $policyParity
        candidates                  = $orderedCandidates
        summary                     = $summary
        cvfWebObservation           = $cvfWebObservation
        pathEscapeChecksRun         = $pathEscapeChecksRun
        noTargetWriteConfirmation   = 'CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.'
        errors                      = @()
    }

    $canonicalJsonForHash = $receiptBody | ConvertTo-Json -Depth 20 -Compress
    $receiptId = Get-Sha256Hex -Bytes (Get-Utf8Bytes -Text $canonicalJsonForHash)

    $receipt = [ordered]@{
        receiptId = $receiptId
    }
    foreach ($key in $receiptBody.Keys) { $receipt[$key] = $receiptBody[$key] }

    $receiptJson = $receipt | ConvertTo-Json -Depth 20

    if ($ReceiptOutputPath) {
        $utf8NoBom = [System.Text.UTF8Encoding]::new($false)
        [System.IO.File]::WriteAllText($resolvedReceiptPath, $receiptJson, $utf8NoBom)
    }

    Write-Output $receiptJson
    exit 0
} catch {
    $err = $_.Exception
    $code = if ($err.Message -match '^[A-Z_]+:') { ($err.Message -split ':', 2)[0] } else { 'MAPPER_ERROR' }
    $failureEnvelope = [ordered]@{
        receiptId                 = $null
        schemaVersion              = '1.0.0'
        sourceRoot                 = 'PROVENANCE_ROOT'
        targetRoot                 = 'PUBLIC_SYNC_ROOT'
        cvfWebRoot                 = 'CVF_WEB_ROOT'
        rootsValidated              = $rootsValidated
        errors                      = @(
            [ordered]@{
                code    = $code
                message = $err.Message
            }
        )
        noTargetWriteConfirmation   = 'CONFIRMED_NO_TARGET_WRITE: this run performed zero filesystem writes inside ProvenanceRoot, PublicSyncRoot, or CvfWebRoot.'
    }
    $failureJson = $failureEnvelope | ConvertTo-Json -Depth 20
    Write-Output $failureJson
    exit 1
}
