function Get-CvfWorkspaceOverlayCatalog {
    param([string]$RepoRoot)

    $catalogPath = Join-Path $RepoRoot "workspace_overlay_catalog.json"
    if (-not (Test-Path -LiteralPath $catalogPath -PathType Leaf)) {
        throw "Overlay catalog not found: $catalogPath"
    }

    $catalog = Get-Content -LiteralPath $catalogPath -Raw -Encoding utf8 | ConvertFrom-Json
    if (-not $catalog.artifacts) {
        throw "Overlay catalog missing artifacts array: $catalogPath"
    }

    return $catalog
}

function Get-CvfWorkspaceOverlayProfilesRoot {
    param([string]$RepoRoot)
    return (Join-Path $RepoRoot "workspace_overlay_profiles")
}

function Get-CvfWorkspaceOverlayProfilePath {
    param(
        [string]$RepoRoot,
        [string]$ProfileName
    )

    $profilesRoot = Get-CvfWorkspaceOverlayProfilesRoot -RepoRoot $RepoRoot
    return (Join-Path $profilesRoot "$ProfileName.json")
}

function Get-CvfWorkspaceOverlayProfileObject {
    param(
        [string]$RepoRoot,
        [string]$ProfileName
    )

    $profilePath = Get-CvfWorkspaceOverlayProfilePath -RepoRoot $RepoRoot -ProfileName $ProfileName
    if (-not (Test-Path -LiteralPath $profilePath -PathType Leaf)) {
        throw "Overlay profile not found: $profilePath"
    }

    $profile = Get-Content -LiteralPath $profilePath -Raw -Encoding utf8 | ConvertFrom-Json
    if (-not $profile.profileName) {
        throw "Overlay profile missing profileName: $profilePath"
    }

    return $profile
}

function Add-CvfOverlayUniqueString {
    param(
        [System.Collections.Generic.List[string]]$List,
        [string]$Value
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return
    }

    if (-not $List.Contains($Value)) {
        $null = $List.Add($Value)
    }
}

function Resolve-CvfWorkspaceOverlayProfileArtifactPaths {
    param(
        $Profile,
        $Catalog
    )

    $paths = [System.Collections.Generic.List[string]]::new()

    foreach ($item in @($Profile.includePaths | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        Add-CvfOverlayUniqueString -List $paths -Value $item
    }

    $artifactIds = @($Profile.includeArtifactIds | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if ($artifactIds.Count -gt 0) {
        foreach ($artifactId in $artifactIds) {
            $matches = @($Catalog.artifacts | Where-Object { $_.artifactId -eq $artifactId })
            if ($matches.Count -eq 0) {
                throw "Overlay catalog artifactId not found: $artifactId"
            }
            foreach ($entry in $matches) {
                Add-CvfOverlayUniqueString -List $paths -Value $entry.path
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
                    Add-CvfOverlayUniqueString -List $paths -Value $entry.path
                    break
                }
            }
        }
    }

    return $paths
}

function Resolve-CvfWorkspaceOverlayProfileNames {
    param(
        [string]$RepoRoot,
        [string]$ProfileName,
        [System.Collections.Generic.HashSet[string]]$Visited
    )

    if (-not $Visited.Add($ProfileName)) {
        throw "Overlay profile inheritance loop detected at profile: $ProfileName"
    }

    $profile = Get-CvfWorkspaceOverlayProfileObject -RepoRoot $RepoRoot -ProfileName $ProfileName
    $resolvedNames = [System.Collections.Generic.List[string]]::new()

    foreach ($parent in @($profile.extends | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        foreach ($item in Resolve-CvfWorkspaceOverlayProfileNames -RepoRoot $RepoRoot -ProfileName $parent -Visited $Visited) {
            Add-CvfOverlayUniqueString -List $resolvedNames -Value $item
        }
    }

    Add-CvfOverlayUniqueString -List $resolvedNames -Value $profile.profileName
    return @($resolvedNames)
}

function Resolve-CvfWorkspaceOverlayIncludePaths {
    param(
        [string]$RepoRoot,
        [string]$ProfileName,
        [System.Collections.Generic.HashSet[string]]$Visited
    )

    if (-not $Visited.Add($ProfileName)) {
        throw "Overlay profile inheritance loop detected at profile: $ProfileName"
    }

    $profile = Get-CvfWorkspaceOverlayProfileObject -RepoRoot $RepoRoot -ProfileName $ProfileName
    $catalog = Get-CvfWorkspaceOverlayCatalog -RepoRoot $RepoRoot
    $paths = [System.Collections.Generic.List[string]]::new()

    foreach ($parent in @($profile.extends | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        foreach ($item in Resolve-CvfWorkspaceOverlayIncludePaths -RepoRoot $RepoRoot -ProfileName $parent -Visited $Visited) {
            Add-CvfOverlayUniqueString -List $paths -Value $item
        }
    }

    foreach ($item in Resolve-CvfWorkspaceOverlayProfileArtifactPaths -Profile $profile -Catalog $catalog) {
        Add-CvfOverlayUniqueString -List $paths -Value $item
    }

    return @($paths | Sort-Object -Unique)
}

function Get-CvfWorkspaceOverlayProfileReport {
    param(
        [string]$RepoRoot,
        [string]$ProfileName
    )

    $profile = Get-CvfWorkspaceOverlayProfileObject -RepoRoot $RepoRoot -ProfileName $ProfileName
    $catalog = Get-CvfWorkspaceOverlayCatalog -RepoRoot $RepoRoot
    $pathVisited = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $nameVisited = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $resolvedPaths = @(Resolve-CvfWorkspaceOverlayIncludePaths -RepoRoot $RepoRoot -ProfileName $ProfileName -Visited $pathVisited)
    $resolvedProfiles = @(Resolve-CvfWorkspaceOverlayProfileNames -RepoRoot $RepoRoot -ProfileName $ProfileName -Visited $nameVisited)
    $artifactMap = @{}
    foreach ($entry in @($catalog.artifacts)) {
        $artifactMap[$entry.path] = $entry
    }

    $classCounts = @{}
    $stabilityCounts = @{}
    $reviewPolicyCounts = @{}
    $resolvedArtifacts = [System.Collections.ArrayList]::new()

    foreach ($path in $resolvedPaths) {
        if ($artifactMap.ContainsKey($path)) {
            $entry = $artifactMap[$path]
            $null = $resolvedArtifacts.Add([PSCustomObject]@{
                artifactId = $entry.artifactId
                path = $entry.path
                artifactClass = $entry.artifactClass
                stability = $entry.stability
                reviewPolicy = $entry.reviewPolicy
                selectionTags = @($entry.selectionTags)
                reason = $entry.reason
            })

            $classCounts[$entry.artifactClass] = 1 + [int]($classCounts[$entry.artifactClass])
            $stabilityCounts[$entry.stability] = 1 + [int]($stabilityCounts[$entry.stability])
            $reviewPolicyCounts[$entry.reviewPolicy] = 1 + [int]($reviewPolicyCounts[$entry.reviewPolicy])
        }
        else {
            $null = $resolvedArtifacts.Add([PSCustomObject]@{
                artifactId = ""
                path = $path
                artifactClass = "path-only"
                stability = "unknown"
                reviewPolicy = "unknown"
                selectionTags = @()
                reason = "Profile includes this path directly."
            })
        }
    }

    return [PSCustomObject]@{
        profileName = $profile.profileName
        description = $profile.description
        extends = @($profile.extends)
        includeSelectionTags = @($profile.includeSelectionTags)
        includeArtifactIds = @($profile.includeArtifactIds)
        includePaths = @($profile.includePaths)
        resolvedProfiles = $resolvedProfiles
        resolvedPathCount = $resolvedPaths.Count
        resolvedPaths = $resolvedPaths
        resolvedArtifacts = $resolvedArtifacts
        counts = [PSCustomObject]@{
            byArtifactClass = $classCounts
            byStability = $stabilityCounts
            byReviewPolicy = $reviewPolicyCounts
        }
    }
}
