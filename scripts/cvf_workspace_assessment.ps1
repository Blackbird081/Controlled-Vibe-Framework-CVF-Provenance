function Test-CommitMatch([string]$Left, [string]$Right) {
    if ([string]::IsNullOrWhiteSpace($Left) -or [string]::IsNullOrWhiteSpace($Right)) {
        return $false
    }
    return $Left.StartsWith($Right, [System.StringComparison]::OrdinalIgnoreCase) -or
        $Right.StartsWith($Left, [System.StringComparison]::OrdinalIgnoreCase)
}

function Get-RemoteRelation([string]$Repository, [string]$LocalHead, [string]$RemoteHead) {
    if (Test-CommitMatch $LocalHead $RemoteHead) {
        return "CURRENT"
    }

    git -C $Repository cat-file -e "$RemoteHead`^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        return "REMOTE_UPDATE_OR_DIVERGENCE"
    }

    git -C $Repository merge-base --is-ancestor $RemoteHead $LocalHead 2>$null
    if ($LASTEXITCODE -eq 0) {
        return "LOCAL_AHEAD"
    }

    return "REMOTE_UPDATE_OR_DIVERGENCE"
}

function Get-WorkspaceAssessment([string]$Path) {
    $issues = [System.Collections.Generic.List[string]]::new()
    $updates = [System.Collections.Generic.List[string]]::new()
    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    if (-not (Test-Path -LiteralPath $corePath -PathType Container)) {
        $issues.Add("Hidden public core is missing.")
        return [pscustomobject]@{ Status = "REPAIR_REQUIRED"; Profile = "none"; Issues = @($issues); Updates = @() }
    }

    $coreRemote = (git -C $corePath remote get-url origin 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $coreRemote -ne $publicRemote) {
        $issues.Add("Hidden core remote is not the approved public repository.")
    }
    if (@(git -C $corePath status --porcelain).Count -gt 0) {
        $issues.Add("Hidden public core is dirty.")
    }

    $active = Get-ActiveProfile -Path $Path
    if ($null -eq $active) {
        $issues.Add("Active profile record is missing.")
    }

    $coreHead = (git -C $corePath rev-parse HEAD 2>$null).Trim()
    $publicLine = @(git ls-remote $publicRemote refs/heads/main 2>$null) | Select-Object -First 1
    $provenanceHead = (git -C $provenanceRoot rev-parse HEAD 2>$null).Trim()
    $provenanceLine = @(git ls-remote $provenanceRemote refs/heads/main 2>$null) | Select-Object -First 1
    if ([string]::IsNullOrWhiteSpace($publicLine) -or [string]::IsNullOrWhiteSpace($provenanceLine)) {
        $issues.Add("Remote update check could not be completed.")
    }
    else {
        $publicHead = ($publicLine -split "\s+")[0]
        $provenanceRemoteHead = ($provenanceLine -split "\s+")[0]
        if ((Get-RemoteRelation $corePath $coreHead $publicHead) -eq "REMOTE_UPDATE_OR_DIVERGENCE") {
            $updates.Add("Public core update is available.")
        }
        if ((Get-RemoteRelation $provenanceRoot $provenanceHead $provenanceRemoteHead) -eq "REMOTE_UPDATE_OR_DIVERGENCE") {
            $updates.Add("Provenance update is available.")
        }
    }

    if ($null -ne $active) {
        $packManifestPath = Join-Path $Path "CVF_RULE_PACKS\$($active.activeProfile)\RULE_PACK_MANIFEST.json"
        if (-not (Test-Path -LiteralPath $packManifestPath -PathType Leaf)) {
            $issues.Add("Active profile manifest is missing.")
        }
        else {
            $pack = Get-Content -LiteralPath $packManifestPath -Raw -Encoding utf8 | ConvertFrom-Json
            $packRoot = Split-Path -Parent $packManifestPath
            $sourceBase = if ($active.activeProfile -eq "operator-local") { $provenanceRoot } else { $corePath }
            foreach ($artifact in @($pack.artifacts)) {
                $artifactPath = if ($artifact.targetPath) {
                    Join-Path $Path $artifact.targetPath
                }
                else {
                    Join-Path $packRoot ("source\" + $artifact.sourcePath)
                }
                if (-not (Test-Path -LiteralPath $artifactPath -PathType Leaf)) {
                    if (-not (Test-Path -LiteralPath $artifactPath -PathType Container)) {
                        $issues.Add("Profile artifact is missing: $($artifact.sourcePath)")
                    }
                }
                elseif ($artifact.sha256) {
                    $hash = (Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant()
                    if ($hash -ne $artifact.sha256) {
                        $issues.Add("Profile artifact drift: $($artifact.sourcePath)")
                    }
                }
                $currentSource = Join-Path $sourceBase $artifact.sourcePath
                if (
                    $artifact.reviewPolicy -ne "local-only" -and
                    (Test-Path -LiteralPath $currentSource -PathType Leaf) -and
                    (Test-Path -LiteralPath $artifactPath -PathType Leaf)
                ) {
                    $sourceHash = (Get-FileHash -LiteralPath $currentSource -Algorithm SHA256).Hash
                    $targetHash = (Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash
                    if ($sourceHash -ne $targetHash) {
                        $updates.Add("Filtered profile source changed: $($artifact.sourcePath)")
                    }
                }
            }
        }
    }

    foreach ($required in @("WORKSPACE_RULES.md", "CVF_WORKSPACE_CLASSIFICATION_GUIDE.md", "AGENT_HANDOFF.md")) {
        if (-not (Test-Path -LiteralPath (Join-Path $Path $required) -PathType Leaf)) {
            $issues.Add("Required workspace file is missing: $required")
        }
    }

    $status = if ($issues.Count -gt 0) { "REPAIR_REQUIRED" } elseif ($updates.Count -gt 0) { "UPDATE_AVAILABLE" } else { "CURRENT" }
    return [pscustomobject]@{
        Status = $status
        Profile = if ($null -eq $active) { "none" } else { $active.activeProfile }
        Issues = @($issues)
        Updates = @($updates)
    }
}

function Write-WorkspaceAssessment($Assessment) {
    Write-Host ""
    Write-Host "Workspace status: $($Assessment.Status)" -ForegroundColor Cyan
    Write-Host "Active profile:   $($Assessment.Profile)"
    $Assessment.Updates | ForEach-Object { Write-Host "  [UPDATE] $_" -ForegroundColor Yellow }
    $Assessment.Issues | ForEach-Object { Write-Host "  [ISSUE]  $_" -ForegroundColor Red }
}

function Test-WorkspaceResult([string]$Path, [string]$Profile) {
    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    $remote = (git -C $corePath remote get-url origin).Trim()
    if ($remote -ne $publicRemote) {
        throw "Post-install hidden core remote mismatch: $remote"
    }

    $active = Get-ActiveProfile -Path $Path
    if ($null -eq $active -or $active.activeProfile -ne $Profile) {
        throw "Post-install active profile mismatch. Expected: $Profile"
    }

    foreach ($requiredRootFile in @(
        "WORKSPACE_RULES.md",
        "CVF_WORKSPACE_CLASSIFICATION_GUIDE.md",
        "CVF_WORKSPACE_MEMORY.md",
        "AGENT_HANDOFF.md",
        "New-CVF-Governed-Project.ps1",
        "Run-CVF-NewProject-Enforcement.ps1"
    )) {
        if (-not (Test-Path -LiteralPath (Join-Path $Path $requiredRootFile) -PathType Leaf)) {
            throw "Post-install workspace artifact is missing: $requiredRootFile"
        }
    }

    if ($Profile -ne "operator-local") {
        Invoke-CheckedPowerShell `
            -ScriptPath (Join-Path $Path "Manage-CVF-Workspace.ps1") `
            -Arguments @("-Action", "Status")
    }

    if (-not $SkipEnforcementGate) {
        Write-Step "Running workspace project-enforcement gate"
        Invoke-CheckedPowerShell -ScriptPath (Join-Path $Path "Run-CVF-NewProject-Enforcement.ps1")
    }

    $coreCommit = (git -C $corePath rev-parse --short HEAD).Trim()
    Write-Ok "Workspace ready"
    Write-Host "  Root:           $Path"
    Write-Host "  Profile:        $Profile"
    Write-Host "  Public core:    $coreCommit"
    Write-Host "  Classification: $(Join-Path $Path 'CVF_WORKSPACE_CLASSIFICATION_GUIDE.md')"
    Write-Host "  Next command:   .\New-CVF-Governed-Project.ps1 -ProjectName <name>"
}
