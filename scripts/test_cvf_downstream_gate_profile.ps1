# CVF-DGIP-T1 hermetic golden harness for the portable downstream gate profile.
#
# Offline and disposable: a local fresh clone (public-main anchor) plus the DECLARED candidate overlay
# (worktree files, identity-checked byte-for-byte), real bootstrap runs, then positive controls,
# deliberate truth-surface drifts, status/claim/role/REWORK negatives, tamper/override attempts,
# preservation + idempotency, LF/CRLF variants, and failure propagation through the project runner,
# the generated PR command, the Core doctor and the workspace aggregate. No provider call, no network
# (a dead git proxy is forced), no install, no write outside harness-created temp roots, no bytecode.
param([string]$EvidencePath = "")
$ErrorActionPreference = "Stop"
$env:PYTHONDONTWRITEBYTECODE = "1"
$env:GIT_CONFIG_COUNT = "1"; $env:GIT_CONFIG_KEY_0 = "http.proxy"; $env:GIT_CONFIG_VALUE_0 = "http://127.0.0.1:9"
$script:results = [System.Collections.Generic.List[object]]::new()
$script:tempRoots = [System.Collections.Generic.List[string]]::new()
$script:negatives = [System.Collections.Generic.List[object]]::new()
function Add-Result {
    param([string]$Ac, [string]$Name, [bool]$Pass, [string]$Detail = "")
    $script:results.Add([PSCustomObject]@{ Ac = $Ac; Name = $Name; Pass = $Pass; Detail = $Detail })
    Write-Host ("[{0}] {1} : {2}" -f $(if ($Pass) { "PASS" } else { "FAIL" }), $Ac, $Name) -ForegroundColor $(if ($Pass) { "Green" } else { "Red" })
    if (-not $Pass -and $Detail) { Write-Host "        -> $Detail" -ForegroundColor Yellow }
}
function New-TempDirectory([string]$Prefix) {
    $dir = Join-Path ([System.IO.Path]::GetTempPath()) "$Prefix-$([Guid]::NewGuid().ToString('N').Substring(0,10))"
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
    $script:tempRoots.Add($dir)
    return $dir
}
. (Join-Path $PSScriptRoot "lib\downstream_catalog\CvfGoldenHarnessSupport.ps1")
. (Join-Path $PSScriptRoot "lib\downstream_catalog\CvfDownstreamCatalogLib.ps1")
. (Join-Path $PSScriptRoot "lib\downstream_governance\CvfDownstreamGateProfile.ps1")
$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot ".."))
$bootstrapScript = Join-Path $repoRoot "scripts\new-cvf-workspace.ps1"
$python = Resolve-CvfPython
$git = @("-c", "user.email=downstream@local", "-c", "user.name=Downstream Probe")
function Get-Text([string]$Path) { return [System.IO.File]::ReadAllText($Path) }
function Test-SameBytes([string]$A, [string]$B) { return (Get-FileHash -LiteralPath $A -Algorithm SHA256).Hash -eq (Get-FileHash -LiteralPath $B -Algorithm SHA256).Hash }
function Set-Json([string]$Path, [scriptblock]$Edit) {
    $j = Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
    & $Edit $j
    [System.IO.File]::WriteAllText($Path, ($j | ConvertTo-Json -Depth 8), (New-Object System.Text.UTF8Encoding($false)))
}
function Edit-Text([string]$Path, [string]$Old, [string]$New) {
    [System.IO.File]::WriteAllText($Path, (Get-Text $Path).Replace($Old, $New), (New-Object System.Text.UTF8Encoding($false)))
}
try {
    Add-Result "DGIP-ENV" "Python 3 is available for the portable runner" ($null -ne $python) "$python"
    $proxyProbe = (git ls-remote https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git 2>&1 | Out-String)
    Add-Result "DGIP-OFFLINE" "Offline guard blocks git network access (no fetch can succeed)" ($LASTEXITCODE -ne 0) $proxyProbe.Trim()
    # --- Candidate identity -------------------------------------------------------------------
    $candidate = Get-CvfDgCandidateSet -RepoRoot $repoRoot
    $changedFromHead = @($candidate | Where-Object { $_.DiffersFromHead })
    Add-Result "DGIP-IDENT" "Declared candidate set found in the worktree ($($candidate.Count) files; $($changedFromHead.Count) differ from HEAD)" ($candidate.Count -ge 30 -and $changedFromHead.Count -eq $candidate.Count) ($candidate | Where-Object { -not $_.DiffersFromHead } | ForEach-Object { $_.Path }) -join ", "
    $workspaceA = New-TempDirectory "cvf-golden-dgip-a"
    $coreA = Join-Path $workspaceA ".Controlled-Vibe-Framework-CVF"
    $mismatch = New-CvfDgCandidateCore -SourceRepoPath $repoRoot -DestCorePath $coreA -CandidateSet $candidate
    Add-Result "DGIP-IDENT" "Every candidate file in the hermetic core is byte-identical to the worktree candidate" ($mismatch.Count -eq 0) (($mismatch | ForEach-Object { $_.Path }) -join ", ")
    $coreRunner = Join-Path $coreA "scripts\lib\downstream_governance\cvf_downstream_gate_runner.py"
    $doctor = Join-Path $coreA "scripts\check_cvf_workspace_agent_enforcement.ps1"
    $aggregate = Join-Path $coreA "scripts\check_cvf_workspace_new_project_enforcement.ps1"
    $projectName = "GateProbe"
    $projectA = Join-Path $workspaceA $projectName
    New-Item -ItemType Directory -Path $projectA -Force | Out-Null
    git -C $projectA init --quiet
    git -C $projectA @git commit --quiet --allow-empty -m "empty downstream repository" | Out-Null
    # --- Fresh bootstrap, positive controls ---------------------------------------------------
    $first = Invoke-CvfBootstrap -WorkspaceRoot $workspaceA -ProjectName $projectName -BootstrapScriptPath $bootstrapScript
    Add-Result "DGIP-BOOT" "Fresh bootstrap exits 0 and reports FRESH_INSTALLED" (($first.ExitCode -eq 0) -and ($first.Output -match "gate profile status: FRESH_INSTALLED")) $first.Output
    $gateFiles = @(".cvf\gate-profile.lock.json", ".github\workflows\cvf-downstream-gates.yml", "scripts\cvf_gates\cvf_downstream_gate_runner.py",
        "scripts\cvf_gates\cvf_downstream_gate_profile.json", "scripts\cvf_gates\check_gate_to_role_closeability.py", "scripts\cvf_gates\git-pre-commit.template")
    $absent = @($gateFiles | Where-Object { -not (Test-Path -LiteralPath (Join-Path $projectA $_)) })
    Add-Result "DGIP-BOOT" "Bootstrap installs the pinned runner, profile, closeability checker, CI workflow and hook template" ($absent.Count -eq 0) ($absent -join ", ")
    $manifest = Get-Content -LiteralPath (Join-Path $projectA ".cvf\manifest.json") -Raw | ConvertFrom-Json
    Add-Result "DGIP-BOOT" "Manifest carries the gate-profile marker and requiredDocs; .gitignore ignores .cvf/runtime/" `
        (($manifest.downstreamGateProfile -eq $Script:CvfGateProfileId) -and ($manifest.requiredDocs -contains ".cvf/gate-profile.lock.json") -and ((Get-Text (Join-Path $projectA ".gitignore")) -match [regex]::Escape(".cvf/runtime/")))
    $memoryText = Get-Text (Join-Path $projectA "CVF_SESSION_MEMORY.md")
    Add-Result "DGIP-CONT" "Initial memory carries machine-comparable truth (contract, mode, phase, handoff)" `
        (($memoryText -match "## Current Truth") -and ($memoryText -match "- Contract: cvf.downstreamContinuityContract@1.0.0") -and ($memoryText -match "- Current mode: INTAKE") -and ($memoryText -match "- Active phase: INTAKE") -and ($memoryText -match "- Active handoff: CVF_SESSION/handoffs/AGENT_HANDOFF_V1_"))
    $projectRunner = Join-Path $projectA "scripts\cvf_gates\cvf_downstream_gate_runner.py"
    $phases = @("bootstrap", "pre-dispatch", "worker-return", "reviewer-fast", "pre-commit", "pr-ci")
    $lock = Get-Content -LiteralPath (Join-Path $projectA ".cvf\gate-profile.lock.json") -Raw | ConvertFrom-Json
    $baseSha = (git -C $projectA rev-parse HEAD | Out-String).Trim()
    $env:CVF_DG_BASE = $baseSha
    $pinArgs = @("--expect-profile-sha256", $lock.profileSha256, "--expect-runner-sha256", $lock.runnerSha256, "--expect-bundle-sha256", $lock.bundleSha256)
    foreach ($phase in $phases) {
        $range = if ($phase -eq "pr-ci") { @("--base", $baseSha, "--head", "HEAD") } else { @() }
        $own = Invoke-CvfDgRunner -Python $python -Runner $projectRunner -Arguments (@("run", "--phase", $phase, "--project-root", $projectA) + $range + $(if ($phase -eq "pr-ci") { $pinArgs } else { @() }))
        $trusted = Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments (@("run", "--phase", $phase, "--project-root", $projectA, "--trusted") + $range)
        Add-Result "DGIP-POS" "Positive control phase ${phase}: project runner and trusted Core runner both PASS" (($own.ExitCode -eq 0) -and ($trusted.ExitCode -eq 0)) "$($own.Output) $($trusted.Output)"
    }
    $doctorClean = Invoke-CvfDoctor -ProjectPath $projectA -CoreDoctorPath $doctor
    Add-Result "DGIP-DOCTOR" "Doctor passes the pristine project, reports GATE_COVERAGE and makes no blanket readiness claim" `
        (($doctorClean.ExitCode -eq 0) -and ($doctorClean.Output -match "GATE_COVERAGE:") -and ($doctorClean.Output -match "hostedCiObserved=false") -and ($doctorClean.Output -notmatch "agent-enforcement-ready")) $doctorClean.Output
    $coverage = (Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("coverage", "--project-root", $projectA, "--json")).Output | ConvertFrom-Json
    $states = @($coverage.phases.PSObject.Properties | ForEach-Object { $_.Value.PSObject.Properties | ForEach-Object { $_.Value.state } } | Sort-Object -Unique)
    Add-Result "DGIP-COV" "Coverage separates INSTALLED/INVOKED and never invents PROVEN_HERMETIC or hosted CI" `
        (($states -contains "INVOKED") -and ($states -notcontains "PROVEN_HERMETIC") -and (-not $coverage.hostedCiObserved)) ($states -join ",")
    $independentProfile = Get-CvfDgLfSha256 (Join-Path $projectA "scripts\cvf_gates\cvf_downstream_gate_profile.json")
    $independentRunner = Get-CvfDgLfSha256 $projectRunner
    $independentBundle = Get-CvfDgBundleSha256 (Join-Path $projectA "scripts\cvf_gates")
    Add-Result "DGIP-PIN" "Lock pins (profile, runner, bundle) equal independently computed LF-normalised hashes and the candidate files" `
        (($lock.profileSha256 -eq $independentProfile) -and ($lock.runnerSha256 -eq $independentRunner) -and ($lock.bundleSha256 -eq $independentBundle) -and ($independentRunner -eq (@($candidate | Where-Object { $_.Path -eq "scripts/lib/downstream_governance/cvf_downstream_gate_runner.py" })[0].LfSha256))) "$independentProfile $independentRunner $independentBundle"
    $prCommand = Get-CvfDgPrCommand -WorkflowPath (Join-Path $projectA ".github\workflows\cvf-downstream-gates.yml") -Python $python
    Add-Result "DGIP-CI" "Generated PR workflow carries the runner command with the profile, runner and bundle pins and an env-bound base (static evidence only)" `
        (($null -ne $prCommand) -and (($prCommand -join " ") -match $lock.profileSha256) -and (($prCommand -join " ") -match $lock.runnerSha256) -and (($prCommand -join " ") -match $lock.bundleSha256) -and (($prCommand -join " ") -match "--base-from-env CVF_DG_BASE")) ($prCommand -join " ")
    $prClean = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $projectA
    Add-Result "DGIP-CI" "The extracted PR command passes on the pristine project (actual local invocation, not hosted CI)" ($prClean.ExitCode -eq 0) $prClean.Output
    # --- Idempotency and preservation ---------------------------------------------------------
    $snapshot = @("CVF_SESSION_MEMORY.md", "CVF_SESSION\ACTIVE_SESSION_STATE.json", "IMPLEMENTATION_STATUS.json", ".cvf\gate-profile.lock.json", "AGENTS.md", ".github\workflows\cvf-downstream-gates.yml") |
        ForEach-Object { [PSCustomObject]@{ Rel = $_; Hash = (Get-FileHash -LiteralPath (Join-Path $projectA $_) -Algorithm SHA256).Hash } }
    git -C $projectA add -A | Out-Null
    git -C $projectA @git commit --quiet -m "first bootstrap" | Out-Null
    $second = Invoke-CvfBootstrap -WorkspaceRoot $workspaceA -ProjectName $projectName -BootstrapScriptPath $bootstrapScript
    $diff = (git -C $projectA status --porcelain | Out-String).Trim()
    $unchanged = @($snapshot | Where-Object { (Get-FileHash -LiteralPath (Join-Path $projectA $_.Rel) -Algorithm SHA256).Hash -ne $_.Hash })
    Add-Result "DGIP-IDEM" "Second bootstrap is idempotent: ALREADY_INSTALLED, no tracked diff, project/lock/CI bytes identical" `
        (($second.ExitCode -eq 0) -and ($second.Output -match "gate profile status: ALREADY_INSTALLED") -and [string]::IsNullOrWhiteSpace($diff) -and ($unchanged.Count -eq 0)) "exit=$($second.ExitCode) diff=$diff changed=$(($unchanged | ForEach-Object { $_.Rel }) -join ',')"
    $pyc = @(Get-ChildItem -LiteralPath $projectA, $coreA -Recurse -Force -Include "*.pyc", "__pycache__" -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\\.git\\' })
    Add-Result "DGIP-BYTECODE" "No bytecode or __pycache__ appears in the project or hermetic core after all runs" ($pyc.Count -eq 0) (($pyc | Select-Object -First 3 | ForEach-Object { $_.FullName }) -join ", ")
    # --- Negative mutations ---------------------------------------------------------------------
    function Test-GateMutation {
        param([string]$Name, [string]$Control, [scriptblock]$Mutate, [string]$ExpectInRunner, [string[]]$Phases = @("pr-ci"), [string]$ExpectInDoctor = "", [string[]]$ExtraArgs = @(), [string]$ExpectInPr = "")
        $copy = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label $Name
        & $Mutate $copy
        $failures = @()
        foreach ($phase in $Phases) {
            if ($phase -eq "pr-ci") { $r = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $copy; $expect = if ($ExpectInPr) { $ExpectInPr } else { $ExpectInRunner } }
            else { $r = Invoke-CvfDgRunner -Python $python -Runner (Join-Path $copy "scripts\cvf_gates\cvf_downstream_gate_runner.py") -Arguments (@("run", "--phase", $phase, "--project-root", $copy) + $ExtraArgs); $expect = $ExpectInRunner }
            if (-not (($r.ExitCode -ne 0) -and ($r.Output -match [regex]::Escape($expect)))) { $failures += "${phase}: exit=$($r.ExitCode) $($r.Output)" }
        }
        Add-Result "DGIP-NEG" "$Name -> $Control fails in phases [$($Phases -join ',')] with $ExpectInRunner" ($failures.Count -eq 0) ($failures -join " | ")
        $doctorOk = $true
        if ($ExpectInDoctor) {
            $d = Invoke-CvfDoctor -ProjectPath $copy -CoreDoctorPath $doctor
            $doctorOk = ($d.ExitCode -ne 0) -and ($d.Output -match [regex]::Escape($ExpectInDoctor))
            Add-Result "DGIP-NEG" "$Name -> Core doctor fails with $ExpectInDoctor" $doctorOk $d.Output
        }
        $script:negatives.Add([PSCustomObject]@{ Name = $Name; Control = $Control; Phases = $Phases; Passed = (($failures.Count -eq 0) -and $doctorOk) })
        Remove-CvfHermeticDirectory -Path $copy | Out-Null
    }
    $allPhases = $phases
    $sf = "CVF_SESSION\ACTIVE_SESSION_STATE.json"
    Test-GateMutation -Name "state-mode-drift" -Control "CVF-DG-CONT-01" -Phases $allPhases -ExpectInRunner "SURFACE_MISMATCH" -ExpectInDoctor "CVF-DG-CONT-01" -Mutate { param($p) Set-Json (Join-Path $p $sf) { param($j) $j.currentMode = "BUILD" } }
    Test-GateMutation -Name "memory-phase-drift" -Control "CVF-DG-CONT-01" -ExpectInRunner "CVF_SESSION_MEMORY.md#Active phase" -ExpectInDoctor "CVF-DG-CONT-01" -Mutate { param($p) Edit-Text (Join-Path $p "CVF_SESSION_MEMORY.md") "- Active phase: INTAKE" "- Active phase: WORK_ORDER" }
    Test-GateMutation -Name "handoff-mode-drift" -Control "CVF-DG-CONT-01" -ExpectInRunner "Current mode" -Mutate { param($p) $h = (Get-ChildItem (Join-Path $p "CVF_SESSION\handoffs") -Filter "AGENT_HANDOFF_V1_*.md")[0].FullName; Edit-Text $h "- Current mode: INTAKE" "- Current mode: REVIEW" }
    Test-GateMutation -Name "implementation-phase-drift" -Control "CVF-DG-CONT-01" -ExpectInRunner "IMPLEMENTATION_STATUS.json#/currentPhase" -Mutate { param($p) Set-Json (Join-Path $p "IMPLEMENTATION_STATUS.json") { param($j) $j.currentPhase = "SPEC" } }
    Test-GateMutation -Name "review-pending-stale-memory" -Control "CVF-DG-CONT-01" -ExpectInRunner "SURFACE_MISMATCH" -ExpectInDoctor "CVF-DG-CONT-01" -Mutate {
        param($p)
        Set-Json (Join-Path $p $sf) { param($j) $j.currentMode = "REVIEW_PENDING"; $j.activePhase = "REVIEW" }
        $h = (Get-ChildItem (Join-Path $p "CVF_SESSION\handoffs") -Filter "AGENT_HANDOFF_V1_*.md")[0].FullName
        Edit-Text $h "- Current mode: INTAKE" "- Current mode: REVIEW_PENDING"; Edit-Text $h "- Active phase: INTAKE" "- Active phase: REVIEW"
    }
    Test-GateMutation -Name "unknown-state-field" -Control "CVF-DG-CONT-01" -ExpectInRunner "UNKNOWN_FIELD" -Mutate { param($p) Set-Json (Join-Path $p $sf) { param($j) $j | Add-Member -NotePropertyName "rogueField" -NotePropertyValue 1 -Force } }
    $packetPhases = @("pre-dispatch", "worker-return", "reviewer-fast", "pre-commit", "pr-ci")
    $reviewPhases = @("worker-return", "reviewer-fast", "pre-commit", "pr-ci")
    function New-Packet([string]$Project, [string]$Rel, [string]$Body) { $f = Join-Path $Project $Rel; New-Item -ItemType Directory -Path (Split-Path -Parent $f) -Force | Out-Null; [System.IO.File]::WriteAllText($f, $Body, (New-Object System.Text.UTF8Encoding($false))) }
    $wo = "docs/work_orders/CVF_AGENT_WORK_ORDER_PROBE.md"
    $statusCases = @(
        @{ Name = "inline-issue-suffix-status"; Body = "Status: DISPATCH_READY - issue #12`n"; Code = "status_malformed" },
        @{ Name = "unknown-status"; Body = "Status: DISPATCH_RDY`n"; Code = "status_unknown" },
        @{ Name = "blank-status"; Body = "Status:`n"; Code = "status_blank" },
        @{ Name = "duplicate-status"; Body = "Status: HOLD`nStatus: HOLD`n"; Code = "status_duplicate" },
        @{ Name = "active-without-contract"; Body = "Status: DISPATCH_READY (issue #12)`n"; Code = "contract_missing" }
    )
    foreach ($case in $statusCases) {
        $body = $case.Body
        Test-GateMutation -Name $case.Name -Control "CVF-DG-APPL-01" -Phases $packetPhases -ExpectInRunner $case.Code -Mutate ({ param($p) New-Packet $p $wo $body }.GetNewClosure())
    }
    $rework = { param($p, $over) $f = @{ dispatchKind = "REWORK"; reviewerLocalRepairBoundary = "SCOPE_OR_AUTHORITY_EXPANSION"; reviewerLocalRepairBasis = "Finding F1 in the CI workflow needs a deploy path outside the work order"; unchangedObjective = "YES"; unchangedDesign = "YES"; unchangedPaths = "NO"; unchangedAuthority = "YES"; unchangedEffects = "YES"; unchangedCommitOwner = "YES"; evidenceDetermined = "YES"; focusedVerification = "rerun the focused workflow test" }; foreach ($k in $over.Keys) { $f[$k] = $over[$k] }; New-Packet $p "docs/work_orders/CVF_AGENT_WORK_ORDER_REWORK.md" ("Status: HOLD`n" + (($f.GetEnumerator() | Sort-Object Name | ForEach-Object { "$($_.Key): $($_.Value)" }) -join "`n") + "`n") }
    Test-GateMutation -Name "unjustified-rework-deterministic-one-line-repair" -Control "CVF-DG-ROUTE-01" -Phases @("pre-dispatch", "reviewer-fast", "pr-ci") -ExpectInRunner "REWORK_UNJUSTIFIED_REVIEWER_LOCAL_AVAILABLE" -Mutate { param($p) & $rework $p @{ unchangedPaths = "YES" } }
    Test-GateMutation -Name "rework-invalid-boundary" -Control "CVF-DG-ROUTE-01" -Phases @("pre-dispatch") -ExpectInRunner "REWORK_BOUNDARY_INVALID" -Mutate { param($p) & $rework $p @{ reviewerLocalRepairBoundary = "BECAUSE" } }
    $roleDoc = { param($p, $body) New-Packet $p "docs/reviews/CVF_PROBE_REVIEW.md" $body }
    Test-GateMutation -Name "r2-worker-self-review" -Control "CVF-DG-ROLE-01" -Phases $reviewPhases -ExpectInRunner "SELF_REVIEW" -Mutate { param($p) & $roleDoc $p "Risk: R2`nWorker: Agent-A`nReviewer: agent-a`n" }
    Test-GateMutation -Name "r1-lowercase-risk-self-review-f03" -Control "CVF-DG-ROLE-01" -Phases $reviewPhases -ExpectInRunner "RISK_INVALID" -Mutate { param($p) & $roleDoc $p "Risk: r2`nWorker: Agent-A`nReviewer: Agent-A`n" }
    Test-GateMutation -Name "role-bearing-review-without-risk-f03" -Control "CVF-DG-ROLE-01" -Phases $reviewPhases -ExpectInRunner "RISK_MISSING" -Mutate { param($p) & $roleDoc $p "Worker: Agent-A`nReviewer: Agent-A`n" }
    Test-GateMutation -Name "unsupported-proven-claim" -Control "CVF-DG-CLAIM-01" -Phases $reviewPhases -ExpectInRunner "UNSUPPORTED_CLAIM" -Mutate { param($p) & $roleDoc $p "Gate claim: CVF-DG-CONT-01=PROVEN_HERMETIC`n" }
    Test-GateMutation -Name "claim-with-trailing-text-f04" -Control "CVF-DG-CLAIM-01" -Phases $reviewPhases -ExpectInRunner "CLAIM_MALFORMED" -Mutate { param($p) & $roleDoc $p "Gate claim: CVF-DG-CONT-01=PROVEN_HERMETIC because trust me`n" }
    Test-GateMutation -Name "blanket-enforcement-claim" -Control "CVF-DG-CLAIM-01" -Phases @("reviewer-fast", "pr-ci") -ExpectInRunner "BROAD_CLAIM_PHRASE" -Mutate { param($p) & $roleDoc $p "The workspace is agent-enforcement-ready.`n" }
    Test-GateMutation -Name "handoff-active-and-archived-f05" -Control "CVF-DG-CONT-01" -Phases $allPhases -ExpectInRunner "HANDOFF_STATUS_INVALID" -ExpectInDoctor "CVF-DG-CONT-01" -Mutate { param($p) $h = (Get-ChildItem (Join-Path $p "CVF_SESSION\handoffs") -Filter "AGENT_HANDOFF_V1_*.md")[0].FullName; Edit-Text $h "Status: ACTIVE" "Status: ACTIVE`nStatus: ARCHIVED" }
    Test-GateMutation -Name "active-work-order-is-draft-f06" -Control "CVF-DG-CONT-01" -Phases $allPhases -ExpectInRunner "ACTIVE_WORK_ORDER_NOT_ACTIVE" -ExpectInDoctor "CVF-DG-CONT-01" -Mutate {
        param($p)
        New-Packet $p "docs/work_orders/CVF_AGENT_WORK_ORDER_DRAFT.md" "Status: DRAFT`n"
        Set-Json (Join-Path $p "IMPLEMENTATION_STATUS.json") { param($j) $j.activeWorkOrders = @("docs/work_orders/CVF_AGENT_WORK_ORDER_DRAFT.md") }
    }
    $gatesRel = "scripts\cvf_gates"
    Test-GateMutation -Name "tampered-routing-module" -Control "CVF-DG-INST-01" -Phases $allPhases -ExpectInRunner "FILE_TAMPERED" -ExpectInPr "BUNDLE_PIN_MISMATCH" -ExpectInDoctor "FILE_TAMPERED" -Mutate { param($p) Add-Content -LiteralPath (Join-Path $p "$gatesRel\cvf_dg_routing.py") -Value "# noop" }
    Test-GateMutation -Name "empty-runner-modules" -Control "CVF-DG-INST-01" -Phases @("pr-ci") -ExpectInRunner "BLOCKED_INVALID_INPUT" -ExpectInPr "BUNDLE_PIN_MISMATCH" -ExpectInDoctor "FILE_EMPTY" -Mutate { param($p) Set-Content -LiteralPath (Join-Path $p "$gatesRel\cvf_dg_continuity.py") -Value "" -NoNewline }
    Test-GateMutation -Name "missing-profile" -Control "CVF-DG-INST-01" -Phases @("pr-ci") -ExpectInRunner "BLOCKED_INVALID_INPUT" -ExpectInPr "BUNDLE_PIN_MISMATCH" -ExpectInDoctor "FILE_MISSING" -Mutate { param($p) Remove-Item -LiteralPath (Join-Path $p "$gatesRel\cvf_downstream_gate_profile.json") -Force }
    Test-GateMutation -Name "unexpected-shadow-file-f02" -Control "CVF-DG-INST-01" -Phases @("bootstrap", "pr-ci") -ExpectInRunner "UNEXPECTED_FILE" -ExpectInPr "BUNDLE_PIN_MISMATCH" -ExpectInDoctor "UNEXPECTED_FILE" -Mutate { param($p) New-Packet $p "$($gatesRel.Replace('\', '/'))/sitecustomize.py" "raise SystemExit(0)`n" }
    Test-GateMutation -Name "noop-project-override" -Control "CVF-DG-INST-01" -Phases @("worker-return") -ExpectInRunner "OVERRIDE_REFUSED" -ExpectInDoctor "OVERRIDE_REFUSED" -Mutate { param($p) New-Packet $p ".cvf/gate-profile.local.json" '{"additionalControls":[{"id":"CVF-DG-CONT-01","phases":["worker-return"],"command":["python","-c","pass"]}]}' }
    Test-GateMutation -Name "replaced-runner-fails-ci-pin" -Control "CVF-DG-INST-01" -Phases @("pr-ci") -ExpectInRunner "RUNNER_PIN_MISMATCH" -Mutate {
        param($p)
        $rp = Join-Path $p "$gatesRel\cvf_downstream_gate_runner.py"
        Add-Content -LiteralPath $rp -Value "# noop"
        Set-Json (Join-Path $p ".cvf\gate-profile.lock.json") { param($j) $j.files.'cvf_downstream_gate_runner.py' = Get-CvfDgLfSha256 $rp; $j.runnerSha256 = Get-CvfDgLfSha256 $rp }
    }
    # Consistent edit of a module AND its lock pin: the project's own lock-only check cannot see it
    # (documented trust boundary); the Core doctor compares against the trusted Core source.
    $noop = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "consistent-noop-edit"
    $noopModule = Join-Path $noop "$gatesRel\cvf_dg_continuity.py"
    Add-Content -LiteralPath $noopModule -Value "# noop"
    $noopBundle = Get-CvfDgBundleSha256 (Join-Path $noop $gatesRel)
    Set-Json (Join-Path $noop ".cvf\gate-profile.lock.json") { param($j) $j.files.'cvf_dg_continuity.py' = Get-CvfDgLfSha256 $noopModule; $j.bundleSha256 = $noopBundle }
    $noopOwn = Invoke-CvfDgRunner -Python $python -Runner (Join-Path $noop "$gatesRel\cvf_downstream_gate_runner.py") -Arguments @("run", "--phase", "bootstrap", "--project-root", $noop)
    $noopPr = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $noop
    $noopDoctor = Invoke-CvfDoctor -ProjectPath $noop -CoreDoctorPath $doctor
    $noopCaught = ($noopDoctor.ExitCode -ne 0) -and ($noopDoctor.Output -match "TRUSTED_MISMATCH") -and ($noopPr.ExitCode -ne 0) -and ($noopPr.Output -match "BUNDLE_PIN_MISMATCH")
    Add-Result "DGIP-NEG" "F02 consistent module+lock edit: lock-only check passes (stated limit), but the pinned PR command refuses on actual bytes (BUNDLE_PIN_MISMATCH) and the Core doctor on the trusted source (TRUSTED_MISMATCH)" (($noopOwn.ExitCode -eq 0) -and $noopCaught) "$($noopPr.Output) $($noopDoctor.Output)"
    $script:negatives.Add([PSCustomObject]@{ Name = "consistent-noop-edit"; Control = "CVF-DG-INST-01"; Phases = @("bootstrap", "pr-ci"); Passed = $noopCaught })
    Remove-CvfHermeticDirectory -Path $noop | Out-Null
    # F01: a CLEAN committed checkout (nothing dirty, nothing untracked) must still have its candidates discovered
    # from the PR range, and a missing/unresolvable range must refuse instead of passing on an empty discovery.
    $clean = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "f01-clean-commit"
    $preSha = (git -C $clean rev-parse HEAD | Out-String).Trim()
    New-Packet $clean "docs/work_orders/CVF_AGENT_WORK_ORDER_F01.md" "Status: DISPATCH_READY - issue #1`n"
    New-Packet $clean "docs/reviews/CVF_F01_REVIEW.md" "Risk: R2`nWorker: Agent-A`nReviewer: agent-a`nGate claim: CVF-DG-CONT-01=PROVEN_HERMETIC trailing`n"
    git -C $clean add -A | Out-Null
    git -C $clean @git commit --quiet -m "candidate packets" | Out-Null
    $cleanStatus = (git -C $clean status --porcelain | Out-String).Trim()
    $env:CVF_DG_BASE = $preSha
    $f01 = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $clean
    Remove-Item Env:\CVF_DG_BASE
    $f01Missing = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $clean
    $env:CVF_DG_BASE = ("f" * 40)
    $f01Unresolved = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $clean
    $env:CVF_DG_BASE = (git -C $clean rev-parse HEAD | Out-String).Trim()
    $f01Pristine = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $clean
    $env:CVF_DG_BASE = $baseSha
    $f01Ok = [string]::IsNullOrEmpty($cleanStatus) -and ($f01.ExitCode -ne 0) -and ($f01.Output -match "status_malformed") -and ($f01.Output -match "SELF_REVIEW") -and ($f01.Output -match "CLAIM_MALFORMED") -and ($f01.Output -match "RANGE_RESOLVED")
    Add-Result "DGIP-NEG" "F01 clean committed checkout: the generated PR command binds the PR range, finds the malformed order, self-review and claim and refuses" $f01Ok "status=[$cleanStatus] $($f01.Output)"
    Add-Result "DGIP-NEG" "F01 missing or unresolvable base refuses (RANGE_BASE_MISSING / RANGE_BASE_UNRESOLVED); a pristine range passes with an explicit RANGE_EMPTY_CHECKED disposition" `
        (($f01Missing.ExitCode -ne 0) -and ($f01Missing.Output -match "RANGE_BASE_MISSING") -and ($f01Unresolved.ExitCode -ne 0) -and ($f01Unresolved.Output -match "RANGE_BASE_UNRESOLVED") -and ($f01Pristine.ExitCode -eq 0) -and ($f01Pristine.Output -match "RANGE_EMPTY_CHECKED")) "$($f01Missing.Output) $($f01Unresolved.Output) $($f01Pristine.Output)"
    $script:negatives.Add([PSCustomObject]@{ Name = "clean-committed-range"; Control = "CVF-DG-RANGE-01"; Phases = @("pr-ci"); Passed = ($f01Ok -and ($f01Missing.ExitCode -ne 0) -and ($f01Unresolved.ExitCode -ne 0)) })
    $script:negatives.Add([PSCustomObject]@{ Name = "clean-committed-range-candidates"; Control = "CVF-DG-APPL-01"; Phases = @("pr-ci"); Passed = $f01Ok })
    Remove-CvfHermeticDirectory -Path $clean | Out-Null
    # Environment override of a mandatory gate is refused.
    $env:CVF_DG_SKIP = "1"
    $envRun = Invoke-CvfDgRunner -Python $python -Runner $projectRunner -Arguments @("run", "--phase", "pre-commit", "--project-root", $projectA)
    Remove-Item Env:\CVF_DG_SKIP
    Add-Result "DGIP-NEG" "CVF_DG_SKIP environment override is refused (non-zero, OVERRIDE_REFUSED)" (($envRun.ExitCode -ne 0) -and ($envRun.Output -match "OVERRIDE_REFUSED")) $envRun.Output
    # Justified REWORK (real boundary change) is still permitted; a project-local LOCAL-* control runs alongside the mandatory ones.
    $okCopy = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "rework-justified"
    & $rework $okCopy @{}
    New-Packet $okCopy ".cvf/gate-profile.local.json" '{"additionalControls":[{"id":"LOCAL-probe","phases":["pre-dispatch"],"command":["python","-c","raise SystemExit(0)"]}]}'
    $okRun = Invoke-CvfDgRunner -Python $python -Runner (Join-Path $okCopy "$gatesRel\cvf_downstream_gate_runner.py") -Arguments @("run", "--phase", "pre-dispatch", "--project-root", $okCopy)
    Add-Result "DGIP-POS" "Justified REWORK passes; an added LOCAL-* control runs alongside the mandatory controls" (($okRun.ExitCode -eq 0) -and ($okRun.Output -match "LOCAL-probe") -and ($okRun.Output -match "CVF-DG-ROUTE-01")) $okRun.Output
    Remove-CvfHermeticDirectory -Path $okCopy | Out-Null
    # --- Line-ending checkout variants -------------------------------------------------------------
    foreach ($ending in @("CRLF", "LF")) {
        $variant = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "variant$ending"
        Convert-CvfDgLineEndings -Root $variant -To $ending
        $vDoctor = Invoke-CvfDoctor -ProjectPath $variant -CoreDoctorPath $doctor
        $vPr = Invoke-CvfDgRunner -Python $python -Runner $prCommand[1] -Arguments $prCommand[2..($prCommand.Count - 1)] -WorkingDirectory $variant
        Add-Result "DGIP-EOL" "$ending checkout variant: Core doctor and the pinned PR command still PASS (LF-normalised identity)" (($vDoctor.ExitCode -eq 0) -and ($vPr.ExitCode -eq 0)) "$($vDoctor.Output) $($vPr.Output)"
        Remove-CvfHermeticDirectory -Path $variant | Out-Null
    }
    $script:notExecuted = @([PSCustomObject]@{ Id = "DGIP-LINUX"; Status = "NOT_EXECUTED_PLATFORM_UNAVAILABLE"; Reason = "no Linux runtime is available in this session (wsl lists only the docker-desktop internal distro; no install attempted); Linux checkout, hosted CI and cross-OS behavior remain unproven" })
    Write-Host "[SKIP] DGIP-LINUX : NOT_EXECUTED_PLATFORM_UNAVAILABLE (cross-OS and hosted rollout unproven)" -ForegroundColor Yellow
    # --- Workspace aggregate propagation ------------------------------------------------------------
    Set-Content -LiteralPath (Join-Path $workspaceA "WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json") -Value '{"schemaVersion":"1.0","legacyProjects":[]}' -Encoding utf8
    function Invoke-Aggregate {
        $previous = $ErrorActionPreference; $ErrorActionPreference = "Continue"
        try { $o = powershell -ExecutionPolicy Bypass -File $aggregate -WorkspaceRoot $workspaceA -AllowOfflinePinnedCore 2>&1 | Out-String; return [PSCustomObject]@{ ExitCode = $LASTEXITCODE; Output = $o } }
        finally { $ErrorActionPreference = $previous }
    }
    $aggClean = Invoke-Aggregate
    Add-Result "DGIP-AGG" "Workspace aggregate passes the clean project and prints gate coverage with a scope disclaimer" (($aggClean.ExitCode -eq 0) -and ($aggClean.Output -match "ENFORCED_PASS") -and ($aggClean.Output -match "GATE_COVERAGE") -and ($aggClean.Output -match "not claimed")) $aggClean.Output
    $mutant = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "aggmutant"
    Set-Json (Join-Path $mutant $sf) { param($j) $j.activePhase = "DESIGN" }
    $aggBad = Invoke-Aggregate
    $aggCaught = ($aggBad.ExitCode -ne 0) -and ($aggBad.Output -match "ENFORCED_FAIL")
    Add-Result "DGIP-AGG" "A mandatory gate failure propagates through the doctor to the aggregate (ENFORCED_FAIL, non-zero exit, control named)" ($aggCaught -and ($aggBad.Output -match "CVF-DG-CONT-01")) $aggBad.Output
    Remove-CvfHermeticDirectory -Path $mutant | Out-Null
    $script:negatives.Add([PSCustomObject]@{ Name = "aggregate-propagation"; Control = "CVF-DG-CONT-01"; Phases = @("bootstrap"); Passed = $aggCaught })
    # --- Pre-existing (legacy) project: explicit gap, no rewrite, deliberate adoption ---------------
    $legacyName = "OldProject"
    $legacy = Join-Path $workspaceA $legacyName
    foreach ($d in @("CVF_SESSION\handoffs", "docs")) { New-Item -ItemType Directory -Path (Join-Path $legacy $d) -Force | Out-Null }
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    $oldHandoffRel = "CVF_SESSION/handoffs/AGENT_HANDOFF_V1_$(Get-Date -Format yyyy-MM-dd).md"
    $oldState = @{ schemaVersion = "1.0"; projectName = $legacyName; currentMode = "BUILD"; activePhase = "BUILD"; phaseModel = @("INTAKE", "DESIGN", "SPEC", "WORK_ORDER", "BUILD", "REVIEW", "FREEZE"); activeHandoff = $oldHandoffRel; nextAllowedMove = "Old move."; parkedOperatorCheckpoint = $null; activeRole = "ORCHESTRATOR"; roleRoute = "SINGLE_AGENT_MULTI_ROLE_ALLOWED"; updatedAt = "2026-01-01" }
    $oldImpl = @{ schemaVersion = "1.0"; projectName = $legacyName; overallStatus = "BOOTSTRAPPED"; currentPhase = "BUILD"; completedCapabilities = @(); activeWorkOrders = @(); knownLimitations = @("x"); evidence = @(); updatedAt = "2026-01-01" }
    [System.IO.File]::WriteAllText((Join-Path $legacy "CVF_SESSION_MEMORY.md"), "# Project Session Memory`r`n`r`nOLD PROJECT-OWNED MEMORY.`r`nActive state: CVF_SESSION/ACTIVE_SESSION_STATE.json`r`n", $utf8)
    [System.IO.File]::WriteAllText((Join-Path $legacy "CVF_SESSION\ACTIVE_SESSION_STATE.json"), ($oldState | ConvertTo-Json -Depth 5), $utf8)
    [System.IO.File]::WriteAllText((Join-Path $legacy $oldHandoffRel.Replace('/', '\')), "# Agent Handoff V1`r`n`r`nStatus: ACTIVE`r`n`r`n## Current State`r`n`r`n- Current mode: BUILD`r`n- Active phase: BUILD`r`n- Active role: ORCHESTRATOR`r`n- Next allowed move: Different old wording.`r`n", $utf8)
    [System.IO.File]::WriteAllText((Join-Path $legacy "IMPLEMENTATION_STATUS.json"), ($oldImpl | ConvertTo-Json -Depth 5), $utf8)
    [System.IO.File]::WriteAllText((Join-Path $legacy "AGENTS.md"), "# PROJECT OWNED AGENTS`r`nKeep this.`n", $utf8)
    $ownedRel = @("CVF_SESSION_MEMORY.md", "CVF_SESSION\ACTIVE_SESSION_STATE.json", $oldHandoffRel.Replace('/', '\'), "IMPLEMENTATION_STATUS.json")
    $ownedBefore = $ownedRel | ForEach-Object { [PSCustomObject]@{ Rel = $_; Hash = (Get-FileHash -LiteralPath (Join-Path $legacy $_) -Algorithm SHA256).Hash } }
    $legacyBoot = Invoke-CvfBootstrap -WorkspaceRoot $workspaceA -ProjectName $legacyName -BootstrapScriptPath $bootstrapScript
    $changedOwned = @($ownedBefore | Where-Object { (Get-FileHash -LiteralPath (Join-Path $legacy $_.Rel) -Algorithm SHA256).Hash -ne $_.Hash })
    Add-Result "DGIP-MIG" "Pre-existing project: bootstrap exits 0, reports MIGRATION_REQUIRED_SKIPPED, installs no gate file, rewrites no project-owned surface" `
        (($legacyBoot.ExitCode -eq 0) -and ($legacyBoot.Output -match "gate profile status: MIGRATION_REQUIRED_SKIPPED") -and (-not (Test-Path -LiteralPath (Join-Path $legacy "scripts\cvf_gates"))) -and ($changedOwned.Count -eq 0)) $legacyBoot.Output
    $legacyManifest = Get-Content -LiteralPath (Join-Path $legacy ".cvf\manifest.json") -Raw | ConvertFrom-Json
    $legacyDoctor = Invoke-CvfDoctor -ProjectPath $legacy -CoreDoctorPath $doctor
    Add-Result "DGIP-MIG" "Doctor gives the legacy project an explicit migration gap (WARN GATE_PROFILE_NOT_INSTALLED, NOT_INSTALLED coverage) and no readiness claim" `
        (($legacyDoctor.ExitCode -eq 0) -and (-not ($legacyManifest.PSObject.Properties.Name -contains "downstreamGateProfile")) -and ($legacyDoctor.Output -match "GATE_PROFILE_NOT_INSTALLED") -and ($legacyDoctor.Output -match "GATE_COVERAGE: NOT_INSTALLED") -and ($legacyDoctor.Output -notmatch "agent-enforcement-ready")) $legacyDoctor.Output
    $previousEap = $ErrorActionPreference; $ErrorActionPreference = "Continue"
    $explicit = powershell -ExecutionPolicy Bypass -File $bootstrapScript -WorkspaceRoot $workspaceA -ProjectName $legacyName -InstallGateProfile 2>&1 | Out-String
    $explicitExit = $LASTEXITCODE
    $ErrorActionPreference = $previousEap
    $changedOwned = @($ownedBefore | Where-Object { (Get-FileHash -LiteralPath (Join-Path $legacy $_.Rel) -Algorithm SHA256).Hash -ne $_.Hash })
    $afterExplicit = Invoke-CvfDoctor -ProjectPath $legacy -CoreDoctorPath $doctor
    Add-Result "DGIP-MIG" "Explicit -InstallGateProfile installs tooling only; project-owned surfaces stay byte-identical; unmigrated continuity is a blocking MIGRATION_REQUIRED, not a pass" `
        (($explicitExit -eq 0) -and ($explicit -match "gate profile status: FRESH_INSTALLED") -and ($changedOwned.Count -eq 0) -and ($afterExplicit.ExitCode -ne 0) -and ($afterExplicit.Output -match "BLOCKED_MIGRATION_REQUIRED")) "$explicit $($afterExplicit.Output)"
    Set-Json (Join-Path $legacy "CVF_SESSION\ACTIVE_SESSION_STATE.json") { param($j) $j | Add-Member -NotePropertyName "continuityContract" -NotePropertyValue "cvf.downstreamContinuityContract@1.0.0" -Force; $j.nextAllowedMove = "Different old wording." }
    Add-Content -LiteralPath (Join-Path $legacy "CVF_SESSION_MEMORY.md") -Value "`r`n## Current Truth`r`n`r`n- Contract: cvf.downstreamContinuityContract@1.0.0`r`n- Current mode: BUILD`r`n- Active phase: BUILD`r`n- Active handoff: $oldHandoffRel`r`n"
    $adopted = Invoke-CvfDoctor -ProjectPath $legacy -CoreDoctorPath $doctor
    Add-Result "DGIP-MIG" "After the owner deliberately adopts the contract (no automatic alignment) the doctor passes" ($adopted.ExitCode -eq 0) $adopted.Output
    # --- Finding intake: deterministic, explicit, no overwrite --------------------------------------
    $intakeProject = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "intakeprobe"
    $findingPath = Join-Path (New-TempDirectory "cvf-golden-dgip-input") "finding.json"
    $finding = Get-Content -LiteralPath (Join-Path $repoRoot "docs\reference\downstream_gate_profile\DOWNSTREAM_FINDING_INTAKE_TEMPLATE.json") -Raw | ConvertFrom-Json
    $finding.findingId = "FND-GOLD-001"; $finding.title = "Continuity drift passes the doctor"; $finding.sourceProject = "Disposable Probe"; $finding.sourceSha = ("b" * 40)
    $finding.observed = "doctor passed while memory disagreed"; $finding.expected = "drift blocks the doctor"; $finding.candidateControl = "CVF-DG-CONT-01"; $finding.claimLimits = "synthetic hermetic fixture only"
    $finding.negativeEvidence = @(@{ locator = "docs/reviews/x.md#L1"; description = "manual alignment recorded" })
    $finding.chainJoins = @(@{ join = "template to executable"; gap = "no runner"; earliestControlPoint = "bootstrap" })
    [System.IO.File]::WriteAllText($findingPath, ($finding | ConvertTo-Json -Depth 6), $utf8)
    $i1 = Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("intake", "--project-root", $intakeProject, "--finding", $findingPath)
    $target = Join-Path $intakeProject "docs\learning_intake\FND-GOLD-001.intake.json"
    $hashOne = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash
    $i2 = Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("intake", "--project-root", $intakeProject, "--finding", $findingPath)
    $valid = Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("validate-intake", "--record", $target)
    # F07: delete/alter mandatory metadata and RECOMPUTE the content digest; the full schema must still refuse.
    $resignPath = Join-Path (New-TempDirectory "cvf-golden-dgip-resign") "resign.py"
    Set-Content -LiteralPath $resignPath -Encoding ascii -Value @(
        "import json, sys", "sys.path.insert(0, sys.argv[1])", "import cvf_dg_common as c",
        "r = json.load(open(sys.argv[2], encoding='utf-8'))", "r.pop('schemaVersion'); r['profileId'] = 'other'; r['parentOwner'] = 'elsewhere.md'",
        "body = {k: v for k, v in r.items() if k != 'contentSha256'}", "r['contentSha256'] = c.content_sha256(c.canonical_json(body).encode('utf-8'))",
        "json.dump(r, open(sys.argv[3], 'w', encoding='utf-8'))")
    $mutatedRecord = Join-Path (Split-Path -Parent $resignPath) "mutated.intake.json"
    & $python -B $resignPath (Join-Path $coreA "scripts\lib\downstream_governance") $target $mutatedRecord
    $f07 = Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("validate-intake", "--record", $mutatedRecord)
    Add-Result "DGIP-INTAKE" "F07 a record with deleted/altered mandatory metadata and a recomputed digest is refused (MISSING_FIELD, exit non-zero)" (($f07.ExitCode -ne 0) -and ($f07.Output -match "MISSING_FIELD") -and ($f07.Output -match "INTAKE_RECORD: INVALID")) $f07.Output
    $finding.sourceSha = "bad"
    [System.IO.File]::WriteAllText($findingPath, ($finding | ConvertTo-Json -Depth 6), $utf8)
    $i3 = Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("intake", "--project-root", $intakeProject, "--finding", $findingPath)
    Add-Result "DGIP-INTAKE" "Intake is deterministic and idempotent, validates, is not parent acceptance, and refuses an invalid finding" `
        (($i1.ExitCode -eq 0) -and ($i2.ExitCode -eq 0) -and ($hashOne -eq (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash) -and ($valid.Output -match "INTAKE_RECORD: VALID") -and ((Get-Text $target) -match "NOT_ACCEPTED_GENERATION_ONLY") -and ($i3.ExitCode -ne 0)) "$($i1.Output)$($i3.Output)"
    Remove-CvfHermeticDirectory -Path $intakeProject | Out-Null
    # --- Proof receipt (only from assertions that actually passed) and PROVEN_HERMETIC coverage ------
    $controlsProof = [ordered]@{}
    foreach ($id in @("CVF-DG-INST-01", "CVF-DG-CONT-01", "CVF-DG-APPL-01", "CVF-DG-ROUTE-01", "CVF-DG-ROLE-01", "CVF-DG-CLAIM-01")) {
        $good = @($script:negatives | Where-Object { $_.Control -eq $id -and $_.Passed })
        if ($good.Count -gt 0) { $controlsProof[$id] = [ordered]@{ phases = @($good | ForEach-Object { $_.Phases } | Sort-Object -Unique); negativeCases = @($good | ForEach-Object { $_.Name }) } }
    }
    $proof = [ordered]@{ schemaVersion = "cvf.downstreamGateProofReceipt@1.0.0"; profileSha256 = $lock.profileSha256; runnerSha256 = $lock.runnerSha256; bundleSha256 = $lock.bundleSha256; controls = $controlsProof }
    $proofPath = Join-Path (New-TempDirectory "cvf-golden-dgip-proof") "proof.json"
    [System.IO.File]::WriteAllText($proofPath, ($proof | ConvertTo-Json -Depth 6), $utf8)
    $proven = (Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("coverage", "--project-root", $projectA, "--proof-receipt", $proofPath, "--json")).Output | ConvertFrom-Json
    $provenCells = @($proven.phases.PSObject.Properties | ForEach-Object { $row = $_; $row.Value.PSObject.Properties | Where-Object { $_.Value.state -eq "PROVEN_HERMETIC" } | ForEach-Object { "$($row.Name):$($_.Name)" } })
    $expectedCells = @($controlsProof.Keys | ForEach-Object { $c = $_; $controlsProof[$c].phases | ForEach-Object { "${_}:$c" } })
    Add-Result "DGIP-COV" "PROVEN_HERMETIC appears exactly for the control/phase cells whose negative mutation passed in this run" (($provenCells.Count -gt 0) -and (@($provenCells | Where-Object { $expectedCells -notcontains $_ }).Count -eq 0) -and (@($expectedCells | Where-Object { $provenCells -notcontains $_ }).Count -eq 0)) "proven=$($provenCells.Count) expected=$($expectedCells.Count)"
    $proof.bundleSha256 = ("0" * 64)
    [System.IO.File]::WriteAllText($proofPath, ($proof | ConvertTo-Json -Depth 6), $utf8)
    $stale = (Invoke-CvfDgRunner -Python $python -Runner $coreRunner -Arguments @("coverage", "--project-root", $projectA, "--proof-receipt", $proofPath, "--json")).Output | ConvertFrom-Json
    Add-Result "DGIP-COV" "A proof receipt bound to a different bundle identity grants no PROVEN_HERMETIC" (@($stale.phases.PSObject.Properties | ForEach-Object { $_.Value.PSObject.Properties | Where-Object { $_.Value.state -eq "PROVEN_HERMETIC" } }).Count -eq 0)
    # --- Claim wording of the bridge receipt and the rule pack (copying is not invoking) -----------
    $bridgeProject = Copy-DisposableProject -SourceProjectPath $projectA -WorkspaceRoot $workspaceA -Label "bridgeprobe"
    $previousEap = $ErrorActionPreference; $ErrorActionPreference = "Continue"
    powershell -ExecutionPolicy Bypass -File (Join-Path $coreA "scripts\write_cvf_workspace_web_evidence_bridge.ps1") -ProjectPath $bridgeProject 2>&1 | Out-Null
    $ErrorActionPreference = $previousEap
    $receiptFile = @(Get-ChildItem -LiteralPath (Join-Path $bridgeProject "docs") -Filter "CVF_WORKSPACE_WEB_EVIDENCE_BRIDGE_*.md")
    $receiptText = if ($receiptFile.Count -gt 0) { Get-Text $receiptFile[0].FullName } else { "" }
    Add-Result "DGIP-CLAIM" "Bridge receipt makes only scoped doctor claims, no blanket readiness, and carries the gate coverage line" `
        (($receiptFile.Count -eq 1) -and ($receiptText -notmatch "agent-enforcement-ready") -and ($receiptText -match "scoped statement") -and ($receiptText -match "GATE_COVERAGE")) $receiptText
    Remove-CvfHermeticDirectory -Path $bridgeProject | Out-Null
    $packWorkspace = New-TempDirectory "cvf-golden-dgip-pack"
    $previousEap = $ErrorActionPreference; $ErrorActionPreference = "Continue"
    $packOut = powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\sync_cvf_workspace_rule_pack.ps1") -WorkspaceRoot $packWorkspace -ProfileName operator-local -AllowProvenanceContinuity 2>&1 | Out-String
    $packExit = $LASTEXITCODE
    $ErrorActionPreference = $previousEap
    $packManifest = Join-Path $packWorkspace "CVF_RULE_PACKS\operator-local\RULE_PACK_MANIFEST.json"
    Add-Result "DGIP-CLAIM" "Rule-pack manifest and guide state COPIED_NOT_INVOKED (copying a checker is not invoking it)" `
        (($packExit -eq 0) -and (Test-Path -LiteralPath $packManifest) -and ((Get-Text $packManifest) -match "COPIED_NOT_INVOKED") -and ((Get-Text (Join-Path $packWorkspace "CVF_WORKSPACE_RULE_PACKS.md")) -match "Copying a checker")) $packOut
    # --- Size guard ---------------------------------------------------------------------------------
    $sized = @($candidate | Where-Object { $_.Path -match '\.(ps1|py)$' } | Where-Object { ([System.IO.File]::ReadAllLines((Join-Path $repoRoot ($_.Path -replace '/', '\')))).Count -gt 600 })
    Add-Result "DGIP-SIZE" "No candidate script/test exceeds the 600-line project guard" ($sized.Count -eq 0) (($sized | ForEach-Object { $_.Path }) -join ", ")
    if ($EvidencePath) {
        $pythonVersion = (& $python --version 2>&1 | Out-String).Trim()
        $evidence = [ordered]@{ schemaVersion = "cvf.dgipHarnessRun@1"; python = $pythonVersion; candidate = $candidate; lockPins = [ordered]@{ profileSha256 = $lock.profileSha256; runnerSha256 = $lock.runnerSha256; bundleSha256 = $lock.bundleSha256 }
            negatives = @($script:negatives); notExecuted = $script:notExecuted; proofReceipt = $proof; provenCells = $provenCells; results = @($script:results) }
        [System.IO.File]::WriteAllText($EvidencePath, ($evidence | ConvertTo-Json -Depth 8), $utf8)
    }
}
finally {
    foreach ($dir in $script:tempRoots) {
        if (-not (Remove-CvfHermeticDirectory -Path $dir)) { Write-Host "[WARN] Could not remove hermetic temp directory: $dir" -ForegroundColor Yellow }
    }
    $residue = @($script:tempRoots | Where-Object { Test-Path -LiteralPath $_ })
    Add-Result "DGIP-CLEAN" "No hermetic temp directory residue remains after cleanup" ($residue.Count -eq 0) ($residue -join ", ")
}
Write-Host ""
Write-Host "CVF Downstream Gate Profile Golden Harness - Summary" -ForegroundColor Cyan
$failed = @($script:results | Where-Object { -not $_.Pass })
Write-Host ("  {0}/{1} assertions passed; not executed: {2}" -f ($script:results.Count - $failed.Count), $script:results.Count, $(if ($script:notExecuted) { ($script:notExecuted | ForEach-Object { "$($_.Id)=$($_.Status)" }) -join "," } else { "none" }))
if ($failed.Count -gt 0) {
    Write-Host "  FAILED:" -ForegroundColor Red
    foreach ($f in $failed) { Write-Host ("   - [{0}] {1}: {2}" -f $f.Ac, $f.Name, $f.Detail) -ForegroundColor Red }
    exit 1
}
Write-Host "  RESULT: PASS" -ForegroundColor Green
exit 0
