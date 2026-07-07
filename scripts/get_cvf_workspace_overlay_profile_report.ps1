param(
    [string]$ProfileName = "",
    [switch]$AsJson,
    [switch]$ShowFiles
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot "cvf_workspace_overlay_lib.ps1")

$profilesRoot = Get-CvfWorkspaceOverlayProfilesRoot -RepoRoot $repoRoot
if (-not (Test-Path -LiteralPath $profilesRoot -PathType Container)) {
    throw "Overlay profiles root not found: $profilesRoot"
}

$profileNames = @(Get-ChildItem -LiteralPath $profilesRoot -Filter "*.json" -File |
    Sort-Object Name |
    ForEach-Object { [System.IO.Path]::GetFileNameWithoutExtension($_.Name) })

if ([string]::IsNullOrWhiteSpace($ProfileName)) {
    $reports = @($profileNames | ForEach-Object {
        Get-CvfWorkspaceOverlayProfileReport -RepoRoot $repoRoot -ProfileName $_
    })

    if ($AsJson) {
        $reports | ConvertTo-Json -Depth 10
        exit 0
    }

    foreach ($report in $reports) {
        Write-Host "$($report.profileName) [$($report.resolvedPathCount) paths]" -ForegroundColor Cyan
        if ($report.description) {
            Write-Host "  $($report.description)"
        }
        if ($report.resolvedProfiles.Count -gt 1) {
            Write-Host "  chain: $($report.resolvedProfiles -join ' -> ')"
        }
    }
    exit 0
}

$selectedReport = Get-CvfWorkspaceOverlayProfileReport -RepoRoot $repoRoot -ProfileName $ProfileName
if ($AsJson) {
    $selectedReport | ConvertTo-Json -Depth 10
    exit 0
}

Write-Host "Profile:      $($selectedReport.profileName)" -ForegroundColor Cyan
Write-Host "Description:  $($selectedReport.description)"
Write-Host "Chain:        $($selectedReport.resolvedProfiles -join ' -> ')"
Write-Host "Path count:   $($selectedReport.resolvedPathCount)"
Write-Host "Classes:      $(([string]::Join(', ', @($selectedReport.counts.byArtifactClass.Keys | Sort-Object | ForEach-Object { '{0}={1}' -f $_, $selectedReport.counts.byArtifactClass[$_] }))))"
Write-Host "Stability:    $(([string]::Join(', ', @($selectedReport.counts.byStability.Keys | Sort-Object | ForEach-Object { '{0}={1}' -f $_, $selectedReport.counts.byStability[$_] }))))"
Write-Host "ReviewPolicy: $(([string]::Join(', ', @($selectedReport.counts.byReviewPolicy.Keys | Sort-Object | ForEach-Object { '{0}={1}' -f $_, $selectedReport.counts.byReviewPolicy[$_] }))))"

if ($ShowFiles) {
    Write-Host ""
    foreach ($artifact in @($selectedReport.resolvedArtifacts)) {
        $label = if ([string]::IsNullOrWhiteSpace($artifact.artifactId)) { $artifact.path } else { "$($artifact.artifactId): $($artifact.path)" }
        Write-Host "- $label"
    }
}
