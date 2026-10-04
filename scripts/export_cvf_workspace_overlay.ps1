param(
    [Parameter(Mandatory = $true)]
    [string]$ProfileName,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$manifestFileName = "_cvf_overlay_export_manifest.json"

function Write-Info([string]$Message) { Write-Host "[INFO] $Message" -ForegroundColor Cyan }
function Write-Ok([string]$Message) { Write-Host "[OK]   $Message" -ForegroundColor Green }
. (Join-Path $PSScriptRoot "cvf_workspace_overlay_lib.ps1")

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

$outputResolved = Assert-NotRepoRoot -Path $OutputPath
$profile = Get-CvfWorkspaceOverlayProfileObject -RepoRoot $repoRoot -ProfileName $ProfileName
$report = Get-CvfWorkspaceOverlayProfileReport -RepoRoot $repoRoot -ProfileName $ProfileName
$includePaths = @($report.resolvedPaths)

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
    resolvedProfiles = @($report.resolvedProfiles)
    sourceRepoPath = $repoRoot
    sourceRepoHead = (git -C $repoRoot rev-parse --short HEAD).Trim()
    generatedAt = (Get-Date).ToString("s")
    files = @($exportedFiles | Sort-Object -Unique)
}

$manifestPath = Join-Path $outputResolved $manifestFileName
$manifest | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $manifestPath -Encoding utf8

Write-Ok "Overlay export complete: $manifestPath"
Write-Ok "Exported files: $($manifest.files.Count)"
