param(
    [string]$CatalogPath = "",
    [string]$ProfilesRoot = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot "cvf_workspace_overlay_lib.ps1")
if ([string]::IsNullOrWhiteSpace($CatalogPath)) {
    $CatalogPath = Join-Path $repoRoot "workspace_overlay_catalog.json"
}
if ([string]::IsNullOrWhiteSpace($ProfilesRoot)) {
    $ProfilesRoot = Join-Path $repoRoot "workspace_overlay_profiles"
}

$allowedStability = @("high", "medium", "volatile")
$allowedReviewPolicy = @("manual-reviewed", "local-only")
$requiredArtifactFields = @("artifactId", "path", "artifactClass", "selectionTags", "stability", "reviewPolicy", "reason")

function Add-Result([System.Collections.ArrayList]$Results, [string]$Level, [string]$Message) {
    $null = $Results.Add([PSCustomObject]@{
        Level = $Level
        Message = $Message
    })
}

$results = [System.Collections.ArrayList]::new()
$catalog = Get-CvfWorkspaceOverlayCatalog -RepoRoot $repoRoot
if (-not $catalog.artifacts) {
    throw "Overlay catalog missing artifacts array: $CatalogPath"
}

$artifactIds = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$artifactPaths = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$tagSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)

foreach ($artifact in @($catalog.artifacts)) {
    foreach ($field in $requiredArtifactFields) {
        if (-not ($artifact.PSObject.Properties.Name -contains $field)) {
            Add-Result -Results $results -Level "FAIL" -Message "Artifact missing required field '$field': $($artifact | ConvertTo-Json -Compress)"
        }
    }

    if ([string]::IsNullOrWhiteSpace($artifact.artifactId)) {
        Add-Result -Results $results -Level "FAIL" -Message "Artifact has blank artifactId."
    }
    elseif (-not $artifactIds.Add($artifact.artifactId)) {
        Add-Result -Results $results -Level "FAIL" -Message "Duplicate artifactId: $($artifact.artifactId)"
    }

    if ([string]::IsNullOrWhiteSpace($artifact.path)) {
        Add-Result -Results $results -Level "FAIL" -Message "Artifact '$($artifact.artifactId)' has blank path."
    }
    else {
        if (-not $artifactPaths.Add($artifact.path)) {
            Add-Result -Results $results -Level "FAIL" -Message "Duplicate catalog path: $($artifact.path)"
        }
        $resolvedPath = Join-Path $repoRoot $artifact.path
        if (-not (Test-Path -LiteralPath $resolvedPath)) {
            Add-Result -Results $results -Level "FAIL" -Message "Catalog path not found for '$($artifact.artifactId)': $($artifact.path)"
        }
    }

    $artifactTags = @($artifact.selectionTags | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if ($artifactTags.Count -eq 0) {
        Add-Result -Results $results -Level "FAIL" -Message "Artifact '$($artifact.artifactId)' has no selectionTags."
    }
    foreach ($tag in $artifactTags) {
        $null = $tagSet.Add($tag)
    }

    if ($allowedStability -notcontains $artifact.stability) {
        Add-Result -Results $results -Level "FAIL" -Message "Artifact '$($artifact.artifactId)' has invalid stability '$($artifact.stability)'."
    }

    if ($allowedReviewPolicy -notcontains $artifact.reviewPolicy) {
        Add-Result -Results $results -Level "FAIL" -Message "Artifact '$($artifact.artifactId)' has invalid reviewPolicy '$($artifact.reviewPolicy)'."
    }

    $pathNormalized = [string]$artifact.path
    $isPremium = $artifactTags -contains "workspace-premium"
    $isLocal = $artifactTags -contains "workspace-provenance-local"
    $looksPrivate = $pathNormalized -like "CVF_SESSION*" -or
        $pathNormalized -eq "CVF_SESSION_MEMORY.md" -or
        $pathNormalized -like "AGENT_HANDOFF_V*.md"

    if ($isPremium -and $looksPrivate) {
        Add-Result -Results $results -Level "FAIL" -Message "Premium lane may not include private continuity surface: $($artifact.path)"
    }

    if ($isLocal -and $artifact.reviewPolicy -ne "local-only") {
        Add-Result -Results $results -Level "FAIL" -Message "Local provenance lane must use reviewPolicy=local-only: $($artifact.artifactId)"
    }

    if ($isPremium -and $artifact.reviewPolicy -eq "local-only") {
        Add-Result -Results $results -Level "FAIL" -Message "Premium lane may not use reviewPolicy=local-only: $($artifact.artifactId)"
    }
}

if (-not (Test-Path -LiteralPath $ProfilesRoot -PathType Container)) {
    throw "Overlay profiles root not found: $ProfilesRoot"
}

$profileFiles = Get-ChildItem -LiteralPath $ProfilesRoot -Filter "*.json" -File
$profileNames = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
foreach ($profileFile in $profileFiles) {
    $null = $profileNames.Add([System.IO.Path]::GetFileNameWithoutExtension($profileFile.Name))
}

foreach ($profileFile in $profileFiles) {
    $profile = Get-CvfWorkspaceOverlayProfileObject -RepoRoot $repoRoot -ProfileName ([System.IO.Path]::GetFileNameWithoutExtension($profileFile.Name))
    if ([string]::IsNullOrWhiteSpace($profile.profileName)) {
        Add-Result -Results $results -Level "FAIL" -Message "Profile missing profileName: $($profileFile.Name)"
        continue
    }

    $selectorCount = 0
    if (@($profile.includeSelectionTags | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }).Count -gt 0) { $selectorCount++ }
    if (@($profile.includeArtifactIds | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }).Count -gt 0) { $selectorCount++ }
    if (@($profile.includePaths | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }).Count -gt 0) { $selectorCount++ }
    $extendsCount = @($profile.extends | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }).Count
    if ($selectorCount -eq 0 -and $extendsCount -eq 0) {
        Add-Result -Results $results -Level "FAIL" -Message "Profile '$($profile.profileName)' has no selectors."
    }

    foreach ($parent in @($profile.extends | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        if (-not $profileNames.Contains($parent)) {
            Add-Result -Results $results -Level "FAIL" -Message "Profile '$($profile.profileName)' extends missing profile '$parent'."
        }
    }

    foreach ($artifactId in @($profile.includeArtifactIds | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        if (-not $artifactIds.Contains($artifactId)) {
            Add-Result -Results $results -Level "FAIL" -Message "Profile '$($profile.profileName)' references unknown artifactId '$artifactId'."
        }
    }

    foreach ($tag in @($profile.includeSelectionTags | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        if (-not $tagSet.Contains($tag)) {
            Add-Result -Results $results -Level "FAIL" -Message "Profile '$($profile.profileName)' references unknown selectionTag '$tag'."
        }
    }

    foreach ($path in @($profile.includePaths | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $path))) {
            Add-Result -Results $results -Level "FAIL" -Message "Profile '$($profile.profileName)' references missing path '$path'."
        }
    }
}

$fails = @($results | Where-Object { $_.Level -eq "FAIL" })
if ($fails.Count -eq 0) {
    Write-Host "[PASS] Overlay catalog and profiles are valid." -ForegroundColor Green
    Write-Host "Catalog:  $CatalogPath"
    Write-Host "Profiles: $ProfilesRoot"
    exit 0
}

foreach ($result in $results) {
    $color = if ($result.Level -eq "FAIL") { "Red" } else { "Yellow" }
    Write-Host "[$($result.Level)] $($result.Message)" -ForegroundColor $color
}

Write-Host ""
Write-Host "[FAIL] Overlay catalog validation failed with $($fails.Count) issue(s)." -ForegroundColor Red
exit 1
