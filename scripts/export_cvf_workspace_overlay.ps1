param(
    [Parameter(Mandatory = $true)]
    [string]$ProfileName,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$profilesRoot = Join-Path $repoRoot "workspace_overlay_profiles"
$catalogPath = Join-Path $repoRoot "workspace_overlay_catalog.json"
$manifestFileName = "_cvf_overlay_export_manifest.json"

function Write-Info([string]$Message) { Write-Host "[INFO] $Message" -ForegroundColor Cyan }
function Write-Ok([string]$Message) { Write-Host "[OK]   $Message" -ForegroundColor Green }

function Get-ProfilePath([string]$Name) {
    return Join-Path $profilesRoot "$Name.json"
}

function Get-ProfileObject([string]$Name) {
    $profilePath = Get-ProfilePath -Name $Name
    if (-not (Test-Path -LiteralPath $profilePath -PathType Leaf)) {
        throw "Overlay profile not found: $profilePath"
    }
    $profile = Get-Content -LiteralPath $profilePath -Raw -Encoding utf8 | ConvertFrom-Json
    if (-not $profile.profileName) {
        throw "Overlay profile missing profileName: $profilePath"
    }
    return $profile
}

function Get-OverlayCatalog() {
    if (-not (Test-Path -LiteralPath $catalogPath -PathType Leaf)) {
        throw "Overlay catalog not found: $catalogPath"
    }
    $catalog = Get-Content -LiteralPath $catalogPath -Raw -Encoding utf8 | ConvertFrom-Json
    if (-not $catalog.artifacts) {
        throw "Overlay catalog missing artifacts array: $catalogPath"
    }
    return $catalog
}

function Add-UniqueString([System.Collections.Generic.List[string]]$List, [string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) {
        return
    }
    if (-not $List.Contains($Value)) {
        $null = $List.Add($Value)
    }
}

function Resolve-ProfileArtifactPaths($Profile, $Catalog) {
    $paths = [System.Collections.Generic.List[string]]::new()

    foreach ($item in @($Profile.includePaths)) {
        Add-UniqueString -List $paths -Value $item
    }

    $artifactIds = @($Profile.includeArtifactIds | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if ($artifactIds.Count -gt 0) {
        foreach ($artifactId in $artifactIds) {
            $match = @($Catalog.artifacts | Where-Object { $_.artifactId -eq $artifactId })
            if ($match.Count -eq 0) {
                throw "Overlay catalog artifactId not found: $artifactId"
            }
            foreach ($entry in $match) {
                Add-UniqueString -List $paths -Value $entry.path
            }
        }
    }

    $selectionTags = @($Profile.includeSelectionTags | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if ($selectionTags.Count -gt 0) {
        foreach ($entry in @($Catalog.artifacts)) {
            $entryTags = @($entry.selectionTags)
            if ($entryTags.Count -eq 0) {
                continue
            }
            foreach ($tag in $selectionTags) {
                if ($entryTags -contains $tag) {
                    Add-UniqueString -List $paths -Value $entry.path
                    break
                }
            }
        }
    }

    return $paths
}

function Resolve-IncludePaths([string]$Name, [System.Collections.Generic.HashSet[string]]$Visited) {
    if (-not $Visited.Add($Name)) {
        throw "Overlay profile inheritance loop detected at profile: $Name"
    }

    $profile = Get-ProfileObject -Name $Name
    $catalog = Get-OverlayCatalog
    $paths = [System.Collections.Generic.List[string]]::new()

    if ($profile.extends) {
        foreach ($parent in @($profile.extends)) {
            foreach ($item in Resolve-IncludePaths -Name $parent -Visited $Visited) {
                Add-UniqueString -List $paths -Value $item
            }
        }
    }

    foreach ($item in Resolve-ProfileArtifactPaths -Profile $profile -Catalog $catalog) {
        Add-UniqueString -List $paths -Value $item
    }

    return @($paths | Sort-Object -Unique)
}

function Assert-NotRepoRoot([string]$Path) {
    $resolved = [System.IO.Path]::GetFullPath($Path)
    $repoResolved = [System.IO.Path]::GetFullPath($repoRoot)
    if ($resolved -eq $repoResolved) {
        throw "Refusing to export overlay into the provenance repo root."
    }
    return $resolved
}

function Reset-OutputDirectory([string]$Path) {
    if (Test-Path -LiteralPath $Path -PathType Container) {
        if (-not $Force) {
            throw "Output path already exists. Re-run with -Force to replace it: $Path"
        }
        Remove-Item -LiteralPath $Path -Recurse -Force
    }
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
}

function Copy-SourcePath([string]$RelativePath, [string]$DestinationRoot) {
    $sourcePath = Join-Path $repoRoot $RelativePath
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Overlay include path not found: $RelativePath"
    }

    $copiedFiles = [System.Collections.Generic.List[string]]::new()

    if (Test-Path -LiteralPath $sourcePath -PathType Leaf) {
        $destinationPath = Join-Path $DestinationRoot $RelativePath
        $destinationDir = Split-Path -Parent $destinationPath
        if (-not (Test-Path -LiteralPath $destinationDir -PathType Container)) {
            New-Item -ItemType Directory -Path $destinationDir -Force | Out-Null
        }
        Copy-Item -LiteralPath $sourcePath -Destination $destinationPath -Force
        $null = $copiedFiles.Add($RelativePath)
        return $copiedFiles
    }

    $sourceRootNormalized = [System.IO.Path]::GetFullPath($sourcePath).TrimEnd("\")
    $files = Get-ChildItem -LiteralPath $sourcePath -Recurse -File
    foreach ($file in $files) {
        $fullPath = [System.IO.Path]::GetFullPath($file.FullName)
        $relativeFile = $fullPath.Substring($repoRoot.Length + 1)
        $destinationPath = Join-Path $DestinationRoot $relativeFile
        $destinationDir = Split-Path -Parent $destinationPath
        if (-not (Test-Path -LiteralPath $destinationDir -PathType Container)) {
            New-Item -ItemType Directory -Path $destinationDir -Force | Out-Null
        }
        Copy-Item -LiteralPath $file.FullName -Destination $destinationPath -Force
        $null = $copiedFiles.Add($relativeFile)
    }

    return $copiedFiles
}

if (-not (Test-Path -LiteralPath $profilesRoot -PathType Container)) {
    throw "Overlay profiles folder not found: $profilesRoot"
}

$outputResolved = Assert-NotRepoRoot -Path $OutputPath
$profile = Get-ProfileObject -Name $ProfileName
$visited = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$includePaths = Resolve-IncludePaths -Name $ProfileName -Visited $visited

Write-Info "Profile:       $($profile.profileName)"
Write-Info "Output path:   $outputResolved"
Write-Info "Include paths: $($includePaths.Count)"

Reset-OutputDirectory -Path $outputResolved

$exportedFiles = [System.Collections.Generic.List[string]]::new()
foreach ($relativePath in $includePaths) {
    foreach ($copiedFile in Copy-SourcePath -RelativePath $relativePath -DestinationRoot $outputResolved) {
        $null = $exportedFiles.Add($copiedFile)
    }
    Write-Info "Included: $relativePath"
}

$manifest = [ordered]@{
    profileName = $profile.profileName
    extends = @($profile.extends)
    description = $profile.description
    includeSelectionTags = @($profile.includeSelectionTags)
    includeArtifactIds = @($profile.includeArtifactIds)
    sourceRepoPath = $repoRoot
    sourceRepoHead = (git -C $repoRoot rev-parse --short HEAD).Trim()
    generatedAt = (Get-Date).ToString("s")
    files = @($exportedFiles | Sort-Object -Unique)
}

$manifestPath = Join-Path $outputResolved $manifestFileName
$manifest | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $manifestPath -Encoding utf8

Write-Ok "Overlay export complete: $manifestPath"
Write-Ok "Exported files: $($manifest.files.Count)"
