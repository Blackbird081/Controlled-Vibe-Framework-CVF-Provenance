param(
    [Parameter(Mandatory = $true)]
    [string]$WorkspaceRoot,

    [string]$ProfileName = "workspace-standard",

    [string]$CatalogPath = "workspace_overlay_catalog.json",

    [string]$ProfilesDir = "workspace_overlay_profiles",

    [string]$OutputDirName = "CVF_RULE_PACKS",

    [switch]$AllowProvenanceContinuity
)

$ErrorActionPreference = "Stop"

function Write-Info([string]$Message) {
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Ok([string]$Message) {
    Write-Host "[OK]   $Message" -ForegroundColor Green
}

function Read-JsonFile([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "JSON file not found: $Path"
    }
    return (Get-Content -LiteralPath $Path -Raw -Encoding utf8 | ConvertFrom-Json)
}

function Add-Unique([System.Collections.ArrayList]$List, [string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) {
        return
    }
    if (-not $List.Contains($Value)) {
        [void]$List.Add($Value)
    }
}

function Resolve-ProfileTags {
    param(
        [string]$Name,
        [string]$ProfileRoot,
        [System.Collections.ArrayList]$Visited
    )

    if ($Visited.Contains($Name)) {
        throw "Profile cycle detected at: $Name"
    }
    [void]$Visited.Add($Name)

    $profilePath = Join-Path $ProfileRoot "$Name.json"
    $profile = Read-JsonFile $profilePath
    $tags = [System.Collections.ArrayList]::new()

    if ($profile.extends) {
        foreach ($parent in @($profile.extends)) {
            $parentTags = Resolve-ProfileTags -Name $parent -ProfileRoot $ProfileRoot -Visited $Visited
            foreach ($tag in $parentTags) {
                Add-Unique $tags $tag
            }
        }
    }

    if ($profile.includeSelectionTags) {
        foreach ($tag in @($profile.includeSelectionTags)) {
            Add-Unique $tags $tag
        }
    }

    [void]$Visited.Remove($Name)
    return @($tags)
}

function Assert-ChildPath {
    param(
        [string]$Child,
        [string]$Parent,
        [string]$Label
    )

    $childFull = [System.IO.Path]::GetFullPath($Child)
    $parentFull = [System.IO.Path]::GetFullPath($Parent)
    if (-not $parentFull.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $parentFull = $parentFull + [System.IO.Path]::DirectorySeparatorChar
    }
    if (-not $childFull.StartsWith($parentFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "$Label resolved outside allowed root: $childFull"
    }
}

function Test-BlockedLocalOnlyArtifact {
    param($Artifact)

    $path = [string]$Artifact.path
    $reviewPolicy = [string]$Artifact.reviewPolicy
    $tags = @($Artifact.selectionTags)
    $blockedPrefixes = @(
        "CVF_SESSION",
        "CVF_SESSION_MEMORY.md",
        "AGENT_HANDOFF",
        ".private_reference",
        "Gop y CVF"
    )

    if ($reviewPolicy -eq "local-only") {
        return $true
    }
    foreach ($tag in $tags) {
        if ($tag -eq "workspace-provenance-local" -or $tag -eq "continuity-local") {
            return $true
        }
    }
    foreach ($prefix in $blockedPrefixes) {
        if ($path.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }
    }
    return $false
}

function Assert-NoSensitiveContent {
    param(
        [string]$SourcePath,
        [string]$RelativeSource
    )

    $denyTokens = @(
        "CVF_SESSION",
        ".private_reference",
        "provenance-local",
        "workspace-provenance-local",
        "private/generated MinerU",
        "Gop y CVF"
    )

    $filesToScan = @()
    if (Test-Path -LiteralPath $SourcePath -PathType Container) {
        $filesToScan = @(Get-ChildItem -LiteralPath $SourcePath -Recurse -File)
    }
    elseif (Test-Path -LiteralPath $SourcePath -PathType Leaf) {
        $filesToScan = @(Get-Item -LiteralPath $SourcePath)
    }

    foreach ($file in $filesToScan) {
        foreach ($token in $denyTokens) {
            $hit = Select-String -LiteralPath $file.FullName -Pattern $token -SimpleMatch -Quiet
            if ($hit) {
                throw "Sensitive token '$token' found in selected artifact '$RelativeSource'. Use -AllowProvenanceContinuity only for operator-local continuity packs, or remove this artifact from the profile."
            }
        }
    }
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$workspaceRootResolved = [System.IO.Path]::GetFullPath($WorkspaceRoot)
$catalogResolved = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $CatalogPath))
$profilesResolved = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $ProfilesDir))

if (-not (Test-Path -LiteralPath $workspaceRootResolved -PathType Container)) {
    throw "Workspace root not found: $workspaceRootResolved"
}
if (-not (Test-Path -LiteralPath $profilesResolved -PathType Container)) {
    throw "Profile directory not found: $profilesResolved"
}

$catalog = Read-JsonFile $catalogResolved
$selectionTags = Resolve-ProfileTags -Name $ProfileName -ProfileRoot $profilesResolved -Visited ([System.Collections.ArrayList]::new())
if ($selectionTags.Count -eq 0) {
    throw "Profile selected no tags: $ProfileName"
}

$selected = [System.Collections.ArrayList]::new()
foreach ($artifact in @($catalog.artifacts)) {
    $artifactTags = @($artifact.selectionTags)
    $matches = @($artifactTags | Where-Object { $selectionTags -contains $_ })
    if ($matches.Count -gt 0) {
        [void]$selected.Add($artifact)
    }
}

if ($selected.Count -eq 0) {
    throw "No artifacts selected for profile: $ProfileName"
}

if (-not $AllowProvenanceContinuity) {
    $blocked = @($selected | Where-Object { Test-BlockedLocalOnlyArtifact $_ })
    if ($blocked.Count -gt 0) {
        $blockedList = ($blocked | ForEach-Object { "$($_.artifactId) -> $($_.path)" }) -join "; "
        throw "Profile selects local-only provenance continuity artifacts. Re-run with -AllowProvenanceContinuity only for operator-local use. Blocked: $blockedList"
    }
}

$outputRoot = Join-Path $workspaceRootResolved $OutputDirName
$profileRoot = Join-Path $outputRoot $ProfileName
$sourceRoot = Join-Path $profileRoot "source"
Assert-ChildPath -Child $profileRoot -Parent $workspaceRootResolved -Label "profile output"

if (Test-Path -LiteralPath $profileRoot) {
    $profileRootFull = [System.IO.Path]::GetFullPath($profileRoot)
    $outputRootFull = [System.IO.Path]::GetFullPath($outputRoot)
    if (-not $outputRootFull.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $outputRootFull = $outputRootFull + [System.IO.Path]::DirectorySeparatorChar
    }
    if (-not $profileRootFull.StartsWith($outputRootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to remove profile output outside pack root: $profileRootFull"
    }
    Remove-Item -LiteralPath $profileRoot -Recurse -Force
}

New-Item -ItemType Directory -Path $sourceRoot -Force | Out-Null

$copied = [System.Collections.ArrayList]::new()
foreach ($artifact in $selected) {
    $relativeSource = [string]$artifact.path
    $sourcePath = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $relativeSource))
    Assert-ChildPath -Child $sourcePath -Parent $repoRoot -Label "artifact source"
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Selected artifact source not found: $relativeSource"
    }
    if (-not $AllowProvenanceContinuity) {
        Assert-NoSensitiveContent -SourcePath $sourcePath -RelativeSource $relativeSource
    }

    $targetPath = Join-Path $sourceRoot $relativeSource
    $targetParent = Split-Path -Parent $targetPath
    New-Item -ItemType Directory -Path $targetParent -Force | Out-Null

    if (Test-Path -LiteralPath $sourcePath -PathType Container) {
        Copy-Item -LiteralPath $sourcePath -Destination $targetPath -Recurse -Force
    }
    else {
        Copy-Item -LiteralPath $sourcePath -Destination $targetPath -Force
    }

    [void]$copied.Add([ordered]@{
        artifactId = $artifact.artifactId
        sourcePath = $relativeSource
        targetPath = $targetPath.Substring($workspaceRootResolved.Length).TrimStart("\", "/")
        artifactClass = $artifact.artifactClass
        selectionTags = @($artifact.selectionTags)
        reviewPolicy = $artifact.reviewPolicy
    })
}

$sourceCommit = (git -C $repoRoot rev-parse --short HEAD).Trim()
$manifest = [ordered]@{
    schemaVersion = "1.0"
    profileName = $ProfileName
    sourceRepository = "Controlled-Vibe-Framework-CVF-Provenance"
    sourceCommit = $sourceCommit
    generatedAt = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
    workspaceRoot = $workspaceRootResolved
    allowProvenanceContinuity = [bool]$AllowProvenanceContinuity
    selectionTags = @($selectionTags)
    artifactCount = $copied.Count
    artifacts = @($copied)
}

$manifestPath = Join-Path $profileRoot "RULE_PACK_MANIFEST.json"
$manifest | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $manifestPath -Encoding utf8

$readmePath = Join-Path $profileRoot "README.md"
$readme = @"
# CVF Workspace Rule Pack: $ProfileName

Generated from provenance commit $sourceCommit.

This pack is a curated workspace copy. It does not make the workspace root a
CVF provenance repository and does not replace project-level AGENTS.md,
.cvf/manifest.json, or .cvf/policy.json.

## Selected Tags

$($selectionTags | ForEach-Object { "- $_" } | Out-String)
## Contents

See RULE_PACK_MANIFEST.json for the exact copied artifact list.
"@
Set-Content -LiteralPath $readmePath -Value $readme -Encoding utf8

$activeManifest = [ordered]@{
    schemaVersion = "1.0"
    activeProfile = $ProfileName
    activeProfilePath = (Join-Path $OutputDirName "$ProfileName\RULE_PACK_MANIFEST.json")
    sourceCommit = $sourceCommit
    artifactCount = $copied.Count
    updatedAt = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
}
$activeManifestPath = Join-Path $outputRoot "ACTIVE_RULE_PACK.json"
$activeManifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $activeManifestPath -Encoding utf8

$workspaceGuidePath = Join-Path $workspaceRootResolved "CVF_WORKSPACE_RULE_PACKS.md"
$workspaceGuide = @"
# CVF Workspace Rule Packs

Active profile: $ProfileName

Source commit: $sourceCommit

Rule packs are curated copies from the provenance repository into this local
workspace. Use them as local guidance for downstream projects. Do not treat
this folder as a public export or a full provenance mirror.

## Commands

Refresh this pack from the provenance repository:

~~~powershell
powershell -ExecutionPolicy Bypass -File "<provenance-root>\scripts\sync_cvf_workspace_rule_pack.ps1" -WorkspaceRoot "$workspaceRootResolved" -ProfileName "$ProfileName"
~~~

## Files

- $OutputDirName\ACTIVE_RULE_PACK.json
- $OutputDirName\$ProfileName\RULE_PACK_MANIFEST.json
- $OutputDirName\$ProfileName\source\
"@
Set-Content -LiteralPath $workspaceGuidePath -Value $workspaceGuide -Encoding utf8

Write-Ok "Applied profile '$ProfileName' to workspace: $workspaceRootResolved"
Write-Ok "Copied artifacts: $($copied.Count)"
Write-Ok "Manifest: $manifestPath"
