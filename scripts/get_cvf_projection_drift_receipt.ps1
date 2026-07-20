<#
.SYNOPSIS
    CVF Continuous Projection T1 read-only drift receipt (child-process
    wrapper over the accepted T0 mapper).

.DESCRIPTION
    Read-only, fail-closed drift receipt. It invokes the accepted mapper
    (scripts\get_cvf_projection_map.ps1) as a bounded child process with the
    same three-root and policy inputs, consumes its JSON output verbatim, and
    reports the frozen T0 three-root terminal contract (16 surfaces) plus a
    tracked-versus-ignored public-target split. It performs NO target
    mutation and duplicates none of the mapper's root/remote/dirty-root
    validation, allow/deny classification, or hash comparison; that behavior
    is fully delegated to the mapper child process and its exit code and
    structured error are propagated verbatim on failure.

    This script never copies, writes, or modifies any file inside
    ProvenanceRoot, PublicSyncRoot, or CvfWebRoot. The only filesystem write
    this script may perform is the JSON receipt at -ReceiptOutputPath, using
    the same path-containment discipline as the accepted mapper. If
    -ReceiptOutputPath is omitted, the receipt JSON is written to stdout only.

    Timeout semantics are fail-closed: if the mapper child process does not
    complete within -ScanTimeoutSeconds, only that child process is
    terminated, a structured RECEIPT_TIMEOUT_INCONCLUSIVE error is emitted,
    the script exits nonzero, and no success receipt rows and no receipt
    file are ever written for that run.

.PARAMETER ProvenanceRoot
    Path to the private provenance repository root. Passed through unchanged
    to the mapper child process.

.PARAMETER PublicSyncRoot
    Path to the public-sync repository root. Passed through unchanged to the
    mapper child process.

.PARAMETER CvfWebRoot
    Path to the cvf-web package root. Passed through unchanged to the mapper
    child process.

.PARAMETER PolicyPath
    Path to the JSON policy manifest. Passed through unchanged to the mapper
    child process.

.PARAMETER ReceiptOutputPath
    Optional. If supplied, the deterministic JSON receipt is also written to
    this path after a path-containment check against the current directory
    and against every read-only target root. If omitted, the receipt is
    written to stdout only.

.PARAMETER ScanTimeoutSeconds
    Optional. Integer bound on the mapper child process wall-clock duration.
    Default 60. Accepted range 1..3600. On timeout, only the mapper child
    process is terminated; this script itself always returns.

.OUTPUTS
    A single deterministic JSON object (the drift receipt) is always emitted
    to stdout as the last output of a successful run. On failure, a
    structured error envelope is emitted to stdout and the exit code is
    nonzero.

.EXAMPLE
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\get_cvf_projection_drift_receipt.ps1 `
      -ProvenanceRoot "D:\repo" -PublicSyncRoot "D:\repo-public-sync" `
      -CvfWebRoot "D:\repo\EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web" `
      -PolicyPath "D:\repo\scripts\cvf_projection_policy.json"

.NOTES
    Invocation seams all use this same read-only command surface. Manual use
    runs it directly from a trusted checkout. CI captures stdout and treats a
    nonzero exit as a blocking inconclusive/failure result. A scheduled job
    may invoke the identical command under an external scheduler and retain
    the JSON receipt; T1 creates no scheduler, CI workflow, or apply authority.
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

    [string]$ReceiptOutputPath,

    [ValidateRange(1, 3600)]
    [int]$ScanTimeoutSeconds = 60,

    [string]$MapperPath
)

$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# Frozen T0 three-root terminal contract (16 surfaces). Source of truth:
# docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md
# Findings / Position terminal rows. This script never parses that governed
# Markdown ledger at runtime; the rows are transcribed here as an immutable,
# source-local array so the contract cannot silently drift from what the
# reviewer accepted.
# ---------------------------------------------------------------------------
function Get-FrozenT0ContractRows {
    return @(
        [ordered]@{
            surface        = 'mapped:AGENTS.md'
            semanticOwner  = 'provenance governance toolkit'
            projectionTarget = 'public-sync root file (policy mappedFiles[0])'
            evidenceClass  = 'source'
            audience       = @('developer', 'external_agent')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'mapped:public-core-continuation'
            semanticOwner  = 'provenance governance toolkit'
            projectionTarget = 'public-sync root file (policy mappedFiles[1])'
            evidenceClass  = 'source'
            audience       = @('developer', 'external_agent')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'mapped:scripts/install_cvf_workspace_root_wrappers.ps1'
            semanticOwner  = 'provenance scripts owner'
            projectionTarget = 'public-sync scripts/ (policy mappedFiles[2])'
            evidenceClass  = 'source'
            audience       = @('developer', 'external_agent')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'allowedRootFiles:byte-identical-eight'
            semanticOwner  = 'provenance root maintainers'
            projectionTarget = 'public-sync repository root'
            evidenceClass  = 'source'
            audience       = @('end_user', 'developer', 'external_agent')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'allowedRootFiles:target-only-six'
            semanticOwner  = 'no current provenance root source file found'
            projectionTarget = 'public-sync repository root'
            evidenceClass  = 'source'
            audience       = @('developer', 'external_agent', 'reviewer')
            driftDisposition = 'SOURCE_AUTHORITY_BLOCKED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'denied:docs/baselines'
            semanticOwner  = 'provenance-only, never a projection source'
            projectionTarget = 'NONE'
            evidenceClass  = 'source'
            audience       = @('reviewer')
            driftDisposition = 'SEMANTIC_REVIEW_REQUIRED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'Tracked policy drift and ignored local residue require separate reviewer triage.'
        },
        [ordered]@{
            surface        = 'denied:docs/reviews'
            semanticOwner  = 'provenance-only, never a projection source'
            projectionTarget = 'NONE'
            evidenceClass  = 'source'
            audience       = @('reviewer')
            driftDisposition = 'SEMANTIC_REVIEW_REQUIRED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'Tracked policy drift and ignored local residue require separate reviewer triage.'
        },
        [ordered]@{
            surface        = 'denied:docs/roadmaps'
            semanticOwner  = 'provenance-only, never a projection source'
            projectionTarget = 'NONE'
            evidenceClass  = 'source'
            audience       = @('reviewer')
            driftDisposition = 'SEMANTIC_REVIEW_REQUIRED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'Tracked policy drift and ignored local residue require separate reviewer triage.'
        },
        [ordered]@{
            surface        = 'denied:root-agent-handoffs'
            semanticOwner  = 'provenance-only, never a projection source'
            projectionTarget = 'NONE'
            evidenceClass  = 'source'
            audience       = @('reviewer')
            driftDisposition = 'SEMANTIC_REVIEW_REQUIRED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'Dated ignored handoff residue requires separate reviewer triage; mapped AGENT_HANDOFF.md is excluded.'
        },
        [ordered]@{
            surface        = 'allowedTrees'
            semanticOwner  = 'provenance root maintainers per-tree'
            projectionTarget = 'public-sync repository root (same relative paths)'
            evidenceClass  = 'source'
            audience       = @('developer', 'external_agent')
            driftDisposition = 'SEMANTIC_REVIEW_REQUIRED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'No per-file freshness claim is allowed until a bounded real-root receipt completes.'
        },
        [ordered]@{
            surface        = 'allowedDocsPaths'
            semanticOwner  = 'provenance docs maintainers'
            projectionTarget = 'public-sync docs/ allowed subset'
            evidenceClass  = 'source'
            audience       = @('end_user', 'developer', 'external_agent')
            driftDisposition = 'SEMANTIC_REVIEW_REQUIRED'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'No per-file freshness claim is allowed until a bounded real-root receipt completes.'
        },
        [ordered]@{
            surface        = 'denyPatterns'
            semanticOwner  = 'provenance policy owner (scripts/cvf_projection_policy.json)'
            projectionTarget = 'NONE'
            evidenceClass  = 'source'
            audience       = @('reviewer')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'cvfWeb:sot3-parity'
            semanticOwner  = 'cvf-web package maintainers'
            projectionTarget = 'not projected to public-sync; internal consistency check only'
            evidenceClass  = 'source'
            audience       = @('developer', 'reviewer')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'policy:sync-parity'
            semanticOwner  = 'provenance scripts owner (cvf-public-sync.ps1)'
            projectionTarget = 'not projected itself (deny-patterned)'
            evidenceClass  = 'source'
            audience       = @('developer', 'reviewer')
            driftDisposition = 'CURRENT'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'manual:technical-product-catalog'
            semanticOwner  = 'provenance root maintainers under the separate manual catalog verification discipline'
            projectionTarget = 'public-sync docs/reference/ (covered by allowedDocsPaths)'
            evidenceClass  = 'reviewer'
            audience       = @('end_user', 'developer', 'external_agent')
            driftDisposition = 'NOT_APPLICABLE_WITH_REASON'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = $null
        },
        [ordered]@{
            surface        = 'presentation:README'
            semanticOwner  = 'provenance README.md is semantic source; public-sync README.md receives curated content'
            projectionTarget = 'public-sync repository root'
            evidenceClass  = 'reviewer'
            audience       = @('end_user')
            driftDisposition = 'AUDIENCE_PRESENTATION_RISK'
            sourceHash     = $null
            targetHash     = $null
            reviewerNote   = 'Freshness does not establish end-user presentation quality; separate audience review remains required.'
        }
    )
}

function New-DriftReceiptErrorMessage {
    param([string]$Code, [string]$Message)
    return "$Code`: $Message"
}

function Get-CanonicalPath {
    param([string]$Path)
    return [System.IO.Path]::GetFullPath($Path)
}

function Assert-PathContainment {
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

function ConvertTo-RelativePath {
    param([string]$Root, [string]$FullPath)
    $rootFull = [System.IO.Path]::GetFullPath($Root).TrimEnd('\')
    $itemFull = [System.IO.Path]::GetFullPath($FullPath)
    if (-not $itemFull.StartsWith($rootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $itemFull -replace '\\', '/'
    }
    $rel = $itemFull.Substring($rootFull.Length + 1)
    return ($rel -replace '\\', '/')
}

function Test-GitTrackedPath {
    <# Returns $true only if RelativePath is tracked by git in RepoRoot.
       'git ls-files --error-unmatch' writes a normal, expected stderr line
       for the common untracked case; with the script-wide
       $ErrorActionPreference = 'Stop', that non-zero-exit native call can
       surface as a terminating error even though it is not exceptional
       here. The check is scoped to a local 'Continue' preference so an
       untracked or ignored path is treated as ordinary read-only
       information, not a script failure. #>
    param([string]$RepoRoot, [string]$RelativePath)
    $prevPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $tracked = & git -C $RepoRoot ls-files --error-unmatch -- $RelativePath 2>$null
        return ($LASTEXITCODE -eq 0 -and $tracked)
    } finally {
        $ErrorActionPreference = $prevPreference
    }
}

function Test-GitIgnoredPath {
    <# Returns true only when git itself confirms that RelativePath is
       ignored. A merely untracked path must never be labeled residue. #>
    param([string]$RepoRoot, [string]$RelativePath)
    $prevPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        & git -C $RepoRoot check-ignore --quiet -- $RelativePath 2>$null
        return ($LASTEXITCODE -eq 0)
    } finally {
        $ErrorActionPreference = $prevPreference
    }
}

function Get-PublicTargetState {
    <# Reports tracked-versus-ignored counts for the deny-patterned doc
       classes and dated AGENT_HANDOFF root files as two explicit, disjoint
       sets, so tracked policy drift is never conflated with ignored local
       clone residue (the exact T0 reviewer-repaired finding). Read-only:
       only 'git ls-files' and 'git check-ignore' are invoked; no root state
       is modified. #>
    param([string]$PublicSyncRootResolved)

    $probePaths = @('docs/baselines', 'docs/reviews', 'docs/roadmaps')
    $trackedDenied = New-Object System.Collections.Generic.List[string]
    $ignoredResidue = New-Object System.Collections.Generic.List[string]

    foreach ($probe in $probePaths) {
        $probeFull = Join-Path $PublicSyncRootResolved ($probe -replace '/', '\')
        if (-not (Test-Path -LiteralPath $probeFull -PathType Container)) { continue }
        $files = Get-ChildItem -LiteralPath $probeFull -Recurse -File -ErrorAction SilentlyContinue
        foreach ($f in $files) {
            $rel = ConvertTo-RelativePath -Root $PublicSyncRootResolved -FullPath $f.FullName
            if (Test-GitTrackedPath -RepoRoot $PublicSyncRootResolved -RelativePath $rel) {
                $trackedDenied.Add($rel)
            } elseif (Test-GitIgnoredPath -RepoRoot $PublicSyncRootResolved -RelativePath $rel) {
                $ignoredResidue.Add($rel)
            } else {
                throw (New-DriftReceiptErrorMessage -Code 'PUBLIC_TARGET_STATE_UNCLASSIFIED' -Message "Denied path is neither tracked nor ignored: $rel")
            }
        }
    }

    $rootFiles = Get-ChildItem -LiteralPath $PublicSyncRootResolved -File -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^AGENT_HANDOFF' -and $_.Name -ne 'AGENT_HANDOFF.md' }
    foreach ($f in $rootFiles) {
        $rel = ConvertTo-RelativePath -Root $PublicSyncRootResolved -FullPath $f.FullName
        if (Test-GitTrackedPath -RepoRoot $PublicSyncRootResolved -RelativePath $rel) {
            $trackedDenied.Add($rel)
        } elseif (Test-GitIgnoredPath -RepoRoot $PublicSyncRootResolved -RelativePath $rel) {
            $ignoredResidue.Add($rel)
        } else {
            throw (New-DriftReceiptErrorMessage -Code 'PUBLIC_TARGET_STATE_UNCLASSIFIED' -Message "Denied path is neither tracked nor ignored: $rel")
        }
    }

    $trackedSorted = @($trackedDenied | Sort-Object -Unique)
    $ignoredSorted = @($ignoredResidue | Sort-Object -Unique)

    return [ordered]@{
        trackedDeniedPaths   = $trackedSorted
        trackedDeniedCount   = $trackedSorted.Count
        ignoredResiduePaths  = $ignoredSorted
        ignoredResidueCount  = $ignoredSorted.Count
    }
}

function Set-LiveMapperDispositions {
    <# Applies only mapper-owned freshness signals to the frozen contract.
       Ownership, audience, evidence class, target-only source authority, and
       presentation-review decisions remain frozen reviewer inputs. #>
    param([object[]]$Rows, [object[]]$MapperCandidates)

    function Get-CandidateDisposition([object[]]$Candidates) {
        if (@($Candidates).Count -eq 0) { return $null }
        if (@($Candidates | Where-Object { $_.candidateAction -eq 'COPY_CANDIDATE_ABSENT_TARGET' }).Count -gt 0) {
            return 'MISSING_TARGET'
        }
        if (@($Candidates | Where-Object { $_.candidateAction -eq 'FLAG_SEMANTIC_REVIEW_CHANGED' }).Count -gt 0) {
            return 'STALE_TARGET'
        }
        if (@($Candidates | Where-Object { $_.candidateAction -ne 'SKIP_UNCHANGED' }).Count -eq 0) {
            return 'CURRENT'
        }
        return $null
    }

    $normalizedCandidates = @($MapperCandidates | ForEach-Object {
        [pscustomobject]@{
            sourcePath = ($_.sourcePath -replace '\\', '/')
            candidateAction = $_.candidateAction
            matchedAllowlistRule = $_.matchedAllowlistRule
        }
    })
    $mappedSources = @{
        'mapped:AGENTS.md' = 'governance/toolkit/05_OPERATION/CVF_PUBLIC_CORE_AGENTS.md'
        'mapped:public-core-continuation' = 'governance/toolkit/05_OPERATION/CVF_PUBLIC_CORE_CONTINUATION.md'
        'mapped:scripts/install_cvf_workspace_root_wrappers.ps1' = 'scripts/install_cvf_workspace_root_wrappers_public.ps1'
    }
    $byteIdenticalRootFiles = @('ARCHITECTURE.md', 'SECURITY.md', 'CHANGELOG.md', 'CONTRIBUTORS.md', 'LICENSE', 'netlify.toml', 'package.json', 'package-lock.json')

    foreach ($row in $Rows) {
        $matching = @()
        if ($mappedSources.ContainsKey($row.surface)) {
            $expectedSource = $mappedSources[$row.surface]
            $matching = @($normalizedCandidates | Where-Object { $_.sourcePath -ceq $expectedSource })
        } elseif ($row.surface -eq 'allowedRootFiles:byte-identical-eight') {
            $matching = @($normalizedCandidates | Where-Object { $byteIdenticalRootFiles -ccontains $_.sourcePath })
        } elseif ($row.surface -eq 'allowedTrees') {
            $matching = @($normalizedCandidates | Where-Object { $_.matchedAllowlistRule -eq 'allowedTrees' })
        } elseif ($row.surface -eq 'allowedDocsPaths') {
            $matching = @($normalizedCandidates | Where-Object { $_.matchedAllowlistRule -eq 'allowedDocsPaths' })
        }

        $liveDisposition = Get-CandidateDisposition -Candidates $matching
        if ($liveDisposition) {
            $row.driftDisposition = $liveDisposition
            $row.reviewerNote = $null
        }
    }
}

function Stop-ProcessTree {
    <# Kills a process and its full descendant tree. Windows PowerShell
       5.1 runs on .NET Framework, whose System.Diagnostics.Process has no
       Kill(bool entireProcessTree) overload (that overload was added in
       .NET Core 3.0+); calling it there is a silent no-op under a broad
       try/catch, which lets a timed-out child (and any of its own
       children) keep running to completion. taskkill /T /F is used
       instead because it works identically under both runtimes. #>
    param([int]$ProcessId)
    try {
        & taskkill /PID $ProcessId /T /F 2>&1 | Out-Null
    } catch { }
}

function Invoke-MapperChildProcess {
    <# Invokes the accepted mapper as a bounded child process. Never
       duplicates or weakens mapper validation; consumes its JSON output
       verbatim. Fail-closed on timeout: only the child process is killed,
       no partial receipt row is ever emitted, and no receipt file is
       written for that run. #>
    param(
        [string]$MapperScriptPath,
        [string]$ProvenanceRoot,
        [string]$PublicSyncRoot,
        [string]$CvfWebRoot,
        [string]$PolicyPath,
        [int]$TimeoutSeconds
    )

    $argList = @(
        '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $MapperScriptPath,
        '-ProvenanceRoot', $ProvenanceRoot,
        '-PublicSyncRoot', $PublicSyncRoot,
        '-CvfWebRoot', $CvfWebRoot,
        '-PolicyPath', $PolicyPath
    )

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = 'powershell'
    if ($psi.PSObject.Properties.Match('ArgumentList').Count -gt 0 -and $null -ne $psi.ArgumentList) {
        foreach ($a in $argList) { $psi.ArgumentList.Add($a) }
    } else {
        # Windows PowerShell 5.1's ProcessStartInfo has no ArgumentList
        # collection (added in .NET Core 2.1+); fall back to a single
        # escaped Arguments string so paths containing spaces still pass
        # through as one argument each.
        $psi.Arguments = ($argList | ForEach-Object {
            '"' + ($_ -replace '"', '""') + '"'
        }) -join ' '
    }
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true

    $proc = New-Object System.Diagnostics.Process
    $proc.StartInfo = $psi

    try {
        $null = $proc.Start()
        $stdoutTask = $proc.StandardOutput.ReadToEndAsync()
        $stderrTask = $proc.StandardError.ReadToEndAsync()
        $completed = $proc.WaitForExit($TimeoutSeconds * 1000)

        if (-not $completed) {
            Stop-ProcessTree -ProcessId $proc.Id
            # Confirm the OS has actually reaped the child (and released its
            # stdout/stderr pipe handles) before returning. Without this, the
            # still-pending ReadToEndAsync tasks can keep this script's own
            # process alive in the background well past the caller's return,
            # which shows up as a much longer wall-clock time to an outer
            # caller that waits on this script's own process exit (for
            # example PowerShell's `&` call operator).
            try { $proc.WaitForExit(5000) | Out-Null } catch { }
            return [ordered]@{
                TimedOut = $true
                ExitCode = $null
                StdoutText = ''
                Json = $null
            }
        }

        # Process has exited, so its stdout/stderr pipes are closed and the
        # in-flight ReadToEndAsync tasks are already complete or complete
        # immediately. GetAwaiter().GetResult() blocks only long enough to
        # drain the already-closed stream; it does not reintroduce the
        # read/exit deadlock that a naive WaitForExit-then-ReadToEnd order
        # would risk on a large-output child.
        $exitCode = $proc.ExitCode
        $stdoutText = $stdoutTask.GetAwaiter().GetResult()
        $json = $null
        try { $json = $stdoutText | ConvertFrom-Json } catch { $json = $null }
        return [ordered]@{
            TimedOut = $false
            ExitCode = $exitCode
            StdoutText = $stdoutText
            Json = $json
        }
    } finally {
        if (-not $proc.HasExited) { Stop-ProcessTree -ProcessId $proc.Id }
        $proc.Dispose()
    }
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

try {
    if (-not $MapperPath) {
        $MapperPath = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'get_cvf_projection_map.ps1'
    }
    if (-not (Test-Path -LiteralPath $MapperPath -PathType Leaf)) {
        throw (New-DriftReceiptErrorMessage -Code 'MISSING_MAPPER_SCRIPT' -Message "Mapper script not found: $MapperPath")
    }
    if (-not (Test-Path -LiteralPath $ProvenanceRoot -PathType Container)) {
        throw (New-DriftReceiptErrorMessage -Code 'MISSING_PROVENANCE_ROOT' -Message "Provenance root not found: $ProvenanceRoot")
    }
    if (-not (Test-Path -LiteralPath $PublicSyncRoot -PathType Container)) {
        throw (New-DriftReceiptErrorMessage -Code 'MISSING_PUBLIC_ROOT' -Message "Public-sync root not found: $PublicSyncRoot")
    }

    $provenanceRootResolved = Get-CanonicalPath -Path $ProvenanceRoot
    $publicSyncRootResolved = Get-CanonicalPath -Path $PublicSyncRoot
    $cvfWebRootResolved     = Get-CanonicalPath -Path $CvfWebRoot

    $resolvedReceiptPath = $null
    if ($ReceiptOutputPath) {
        $cwdContainer = (Get-Location).ProviderPath
        $resolvedReceiptPath = Assert-PathContainment -CandidatePath $ReceiptOutputPath -ContainerPath $cwdContainer
        foreach ($readOnlyRoot in @($provenanceRootResolved, $publicSyncRootResolved, $cvfWebRootResolved)) {
            if (Test-PathContained -CandidatePath $resolvedReceiptPath -ContainerPath $readOnlyRoot) {
                throw (New-DriftReceiptErrorMessage -Code 'RECEIPT_TARGET_ROOT_FORBIDDEN' -Message "Receipt output must remain outside every read-only target root: $resolvedReceiptPath")
            }
        }
    }

    $mapperResult = Invoke-MapperChildProcess -MapperScriptPath $MapperPath `
        -ProvenanceRoot $ProvenanceRoot -PublicSyncRoot $PublicSyncRoot -CvfWebRoot $CvfWebRoot -PolicyPath $PolicyPath `
        -TimeoutSeconds $ScanTimeoutSeconds

    if ($mapperResult.TimedOut) {
        throw (New-DriftReceiptErrorMessage -Code 'RECEIPT_TIMEOUT_INCONCLUSIVE' -Message "Mapper child process did not complete within $ScanTimeoutSeconds seconds; terminated child, emitted no success receipt.")
    }

    if ($mapperResult.ExitCode -ne 0) {
        $childCode = 'MAPPER_CHILD_ERROR'
        $childMessage = $mapperResult.StdoutText
        if ($mapperResult.Json -and $mapperResult.Json.errors -and @($mapperResult.Json.errors).Count -gt 0) {
            $childCode = $mapperResult.Json.errors[0].code
            $childMessage = $mapperResult.Json.errors[0].message
        }
        throw (New-DriftReceiptErrorMessage -Code $childCode -Message "Mapper child process failed: $childMessage")
    }

    if (-not $mapperResult.Json) {
        throw (New-DriftReceiptErrorMessage -Code 'MAPPER_CHILD_OUTPUT_UNPARSEABLE' -Message 'Mapper child process exit was zero but stdout did not parse as JSON.')
    }

    $publicTargetState = Get-PublicTargetState -PublicSyncRootResolved $publicSyncRootResolved

    $unsortedRows = @(Get-FrozenT0ContractRows)
    Set-LiveMapperDispositions -Rows $unsortedRows -MapperCandidates @($mapperResult.Json.candidates)
    $rowBySurface = @{}
    foreach ($row in $unsortedRows) { $rowBySurface[$row.surface] = $row }
    $surfaceNames = [string[]]@($rowBySurface.Keys)
    [System.Array]::Sort($surfaceNames, [System.StringComparer]::Ordinal)
    $rows = @($surfaceNames | ForEach-Object { $rowBySurface[$_] })

    $byDisposition = [ordered]@{}
    foreach ($row in $rows) {
        $key = $row.driftDisposition
        if (-not $byDisposition.Contains($key)) { $byDisposition[$key] = 0 }
        $byDisposition[$key] = $byDisposition[$key] + 1
    }
    $reconciledTotal = 0
    foreach ($v in $byDisposition.Values) { $reconciledTotal += $v }

    $receiptBody = [ordered]@{
        schemaVersion              = '1.0.0'
        generatedAtLogical         = 'T0-2026-07-20'
        sourceRoot                 = 'PROVENANCE_ROOT'
        targetRoot                 = 'PUBLIC_SYNC_ROOT'
        cvfWebRoot                 = 'CVF_WEB_ROOT'
        rootsObserved               = $mapperResult.Json.rootsValidated
        rows                        = $rows
        publicTargetState           = $publicTargetState
        summary                     = [ordered]@{
            rowCount            = $rows.Count
            byDisposition       = $byDisposition
            reconciliationMatch = ($reconciledTotal -eq $rows.Count)
        }
        mapperReceiptId             = $mapperResult.Json.receiptId
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
    $code = if ($err.Message -match '^[A-Z_]+:') { ($err.Message -split ':', 2)[0] } else { 'DRIFT_RECEIPT_ERROR' }
    $failureEnvelope = [ordered]@{
        receiptId                 = $null
        schemaVersion              = '1.0.0'
        sourceRoot                 = 'PROVENANCE_ROOT'
        targetRoot                 = 'PUBLIC_SYNC_ROOT'
        cvfWebRoot                 = 'CVF_WEB_ROOT'
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
