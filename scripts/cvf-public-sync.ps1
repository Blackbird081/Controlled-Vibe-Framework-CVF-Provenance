<#
.SYNOPSIS
    CVF Public Sync - Luong 2

.DESCRIPTION
    Sync allowed files from the governance repo to the public-sync repo,
    then push to GitHub. Uses an explicit allowlist - never copies internal
    governance artifacts (AGENT_HANDOFF, baselines, reviews, roadmaps).

    Usage:
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -DryRun
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -NoPush
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -NoCommit
        powershell -ExecutionPolicy Bypass -File scripts\cvf-public-sync.ps1 -WorkspaceKitOnly -NoCommit

    -DryRun : Show what would be copied/pushed without making changes
    -NoPush : Copy files and commit but do not push to GitHub
    -NoCommit : Copy files only; leave the public-sync worktree pending for review
    -WorkspaceKitOnly : Sync only the bounded public workspace reconciliation kit
#>

param(
    [switch]$DryRun,
    [switch]$NoPush,
    [switch]$NoCommit,
    [switch]$WorkspaceKitOnly
)

$ErrorActionPreference = 'Stop'

$GOVERNANCE_ROOT  = Split-Path -Parent $PSScriptRoot
$PUBLIC_SYNC_ROOT = 'D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync'
$PUBLIC_REMOTE    = 'https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git'

# Allowlist: directory trees that may be synced
$ALLOWED_TREES = @(
    'EXTENSIONS',
    'ECOSYSTEM',
    'governance',
    'v1.0',
    'v1.1',
    'tools',
    '.github',
    'App onboarding'
)

# Allowlist: root-level files that may be synced
$ALLOWED_ROOT_FILES = @(
    'ARCHITECTURE.md',
    'CHANGELOG.md',
    'CODEOWNERS',
    'CONTRIBUTING.md',
    'CONTRIBUTORS.md',
    'COST_AND_QUOTA.md',
    'GOVERNANCE.md',
    'LICENSE',
    'PROVIDERS.md',
    'PROVENANCE.md',
    'README.md',
    'SECURITY.md',
    'netlify.toml',
    'package.json',
    'package-lock.json'
)

# Allowlist: public-safe scripts only. Do not export the provenance operation
# scripts directory wholesale.
$ALLOWED_SCRIPT_FILES = @(
    'scripts\bootstrap_foundations.ps1',
    'scripts\bootstrap_foundations.sh',
    'scripts\check_cvf_workspace_agent_enforcement.ps1',
    'scripts\check_cvf_workspace_new_project_enforcement.ps1',
    'scripts\ingest_cvf_downstream_knowledge.ps1',
    'scripts\install_cvf_hooks.ps1',
    'scripts\install_cvf_workspace.ps1',
    'scripts\build_cvf_workspace_distribution.ps1',
    'scripts\get_cvf_workspace_status.ps1',
    'scripts\repair_cvf_workspace.ps1',
    'scripts\manage_cvf_workspace.ps1',
    'scripts\new-cvf-workspace.ps1',
    'scripts\lib\downstream_catalog\CvfDownstreamBootstrapContent.ps1',
    'scripts\lib\downstream_catalog\CvfDownstreamCatalogLib.ps1',
    'scripts\lib\downstream_catalog\CvfGoldenHarnessSupport.ps1',
    'scripts\lib\downstream_catalog\CvfWorkspaceDoctorLiveReadiness.ps1',
    'scripts\lib\downstream_catalog\manage_cvf_downstream_catalog.ps1',
    'scripts\lib\downstream_catalog\schemas\ARTIFACT_REGISTRY.schema.json',
    'scripts\lib\downstream_catalog\schemas\MODULE_REGISTRY.schema.json',
    'scripts\sync_cvf_workspace_public_profile.ps1',
    'scripts\test_cvf_golden_downstream_bootstrap.ps1',
    'scripts\update_cvf_workspace_public_core.ps1',
    'scripts\w114_cp7_multi_sample_downstream_proof.ps1',
    'scripts\write_cvf_workspace_web_evidence_bridge.ps1'
)

$ALLOWED_WORKSPACE_TEMPLATE_FILES = @(
    'workspace_templates\CVF_WORKSPACE_MEMORY_TEMPLATE.md',
    'workspace_templates\AGENT_HANDOFF_TEMPLATE.md'
)

# Mapped exports keep private provenance root files private while still
# publishing a public-safe root front door.
$MAPPED_FILES = @(
    @{
        Source      = 'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_AGENTS.md'
        Destination = 'AGENTS.md'
    },
    @{
        Source      = 'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_CONTINUATION.md'
        Destination = 'AGENT_HANDOFF.md'
    },
    @{
        Source      = 'scripts\install_cvf_workspace_root_wrappers_public.ps1'
        Destination = 'scripts\install_cvf_workspace_root_wrappers.ps1'
    }
)

$WORKSPACE_KIT_FILES = @(
    'docs\GET_STARTED.md',
    'docs\guides\CVF_WORKSPACE_CLASSIFICATION_AND_USAGE_GUIDE.md',
    'docs\reference\CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_DESIGN_2026-07-23.md',
    'docs\reference\CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_LEARNING_INTAKE_2026-07-23.md',
    'docs\reference\CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_SPEC_2026-07-23.md',
    'docs\reference\CVF_NEW_MACHINE_SETUP_CHECKLIST.md',
    'docs\reference\CVF_W114_PUBLIC_EVIDENCE_PACKET_2026-04-23.md',
    'docs\reference\CVF_WORKSPACE_RULES.md',
    'docs\reference\CVF_WORKSPACE_PROFILE_TIERS.md',
    'docs\reference\CVF_WORKSPACE_PAID_USER_AUTHORING_GUIDE.md',
    'docs\reference\CVF_WORKSPACE_PAID_USER_SAFE_ONBOARDING_FLOW.md',
    'docs\reference\CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md',
    'docs\reference\CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md',
    'docs\reference\workspace_distribution\README.md',
    'docs\reference\workspace_distribution\CVF_WORKSPACE_DISTRIBUTION_MANIFEST.json',
    'governance\toolkit\05_OPERATION\CVF_DOWNSTREAM_AGENTS_TEMPLATE.md',
    'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_AGENTS.md',
    'governance\toolkit\05_OPERATION\CVF_PUBLIC_CORE_CONTINUATION.md',
    'governance\toolkit\05_OPERATION\CVF_WORKSPACE_ISOLATION_GUARD.md',
    'governance\toolkit\05_OPERATION\downstream_catalog\CVF_DOWNSTREAM_CATALOG_GUARD.md'
) + $ALLOWED_WORKSPACE_TEMPLATE_FILES + $ALLOWED_SCRIPT_FILES

# Allowlist: docs/ sub-paths that may be synced
# baselines/, reviews/, roadmaps/ are intentionally absent
$ALLOWED_DOCS_PATHS = @(
    'docs\GET_STARTED.md',
    'docs\CHEAT_SHEET.md',
    'docs\CVF_ARCHITECTURE_DECISIONS.md',
    'docs\CVF_CORE_KNOWLEDGE_BASE.md',
    'docs\EXPORT_MANIFEST.md',
    'docs\concepts',
    'docs\guides',
    'docs\reference',
    'docs\benchmark'
)

# Denylist: explicit patterns checked at copy time (defense-in-depth)
$DENY_PATTERNS = @(
    '^AGENT_HANDOFF',
    '^docs[/\\]baselines[/\\]',
    '^docs[/\\]reviews[/\\]',
    '^docs[/\\]roadmaps[/\\]',
    '^docs[/\\]reference[/\\]archive[/\\]',
    '^docs[/\\]reference[/\\]CVF_EXTERNAL_AGENT_ROUND_TRIP_PUBLIC_SYNC_RECORD_',
    '^docs[/\\]reference[/\\]external_agent_invocation_control[/\\]',
    '^docs[/\\]reference[/\\]CVF_MSEA_R72_R84_T0_GOVERNANCE_LOAD_EFFECTIVENESS_EVIDENCE_LEDGER_2026-07-22\.md$',
    '^docs[/\\]reference[/\\]agent_workspace[/\\]CVF_WORKSPACE_LAYER_V041_SEMANTIC_ABSORPTION_LEDGER\.md$',
    '^docs[/\\]reference[/\\]external_agent_review[/\\](?:README|CVF_EXTERNAL_ABSORPTION_CORE_STANDARD|CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP)\.md$',
    '^governance[/\\]capability-grants[/\\]cadp-ai-t2a-owner-binding-grant\.v[12]\.json$',
    '^EXTENSIONS[/\\]CVF_GUARD_CONTRACT[/\\]src[/\\]contracts[/\\](?:repository-capability-owner\.source|capability-owner-binding\.contract)(?:\.test)?\.ts$',
    '^EXTENSIONS[/\\]CVF_GUARD_CONTRACT[/\\]src[/\\]contracts[/\\](?:assf-capability-preflight|cadp-|capability-|controlled-acquisition)[^/\\]*\.ts$',
    '^EXTENSIONS[/\\]CVF_GUARD_CONTRACT[/\\]src[/\\]contracts[/\\](?:index|contracts\.phase1r\.test|contracts\.phase2b-runtime-coherence\.test)\.ts$',
    '^EXTENSIONS[/\\]CVF_GUARD_CONTRACT[/\\]src[/\\](?:index|package\.boundary\.test)\.ts$',
    '^EXTENSIONS[/\\]CVF_EXECUTION_PLANE_FOUNDATION[/\\](?:src[/\\](?:index|cadp\.capability\.consumer\.contract)|tests[/\\]cadp\.capability\.consumer\.contract\.test)\.ts$',
    '^EXTENSIONS[/\\]CVF_MODEL_GATEWAY[/\\](?:src[/\\](?:index|cadp\.constraint\.projection\.contract)|tests[/\\]cadp\.constraint\.projection\.contract\.test)\.ts$',
    '^EXTENSIONS[/\\](?:CVF_EXECUTION_PLANE_FOUNDATION|CVF_MODEL_GATEWAY)[/\\]tests[/\\]cadp\.package\.root\.exports\.test\.ts$',
    '^EXTENSIONS[/\\]CVF_v1\.6_AGENT_PLATFORM[/\\]cvf-web[/\\]src[/\\]lib[/\\]cadp-(?:authentication-policy|authorization)(?:\.test)?\.ts$',
    '^EXTENSIONS[/\\]CVF_LEARNING_PLANE_FOUNDATION[/\\](?:src[/\\](?:index|capability-learning-candidate-projection)|tests[/\\]capability-learning-candidate-projection\.test)\.ts$',
    '^governance[/\\]compat[/\\](?:test_)?check_cadp_authority_boundary_drift\.py$',
    '^governance[/\\]compat[/\\]fixtures[/\\]cadp_authority_boundary_contract\.v1\.json$',
    '^docs[/\\]reference[/\\]system_architecture_catalog[/\\]entries[/\\]interface\.cadp_capability_admission_distribution_profile\.v1\.json$',
    '^governance[/\\]compat[/\\](?:test_)?check_mixed_origin_derived_synthesis_absorption\.py$',
    '^governance[/\\]compat[/\\](?:agent_autorun_command_catalog|local_governance_hook_catalog_(?:pre_commit|pre_push|reviewer_fast))\.py$',
    '^docs[/\\]reference[/\\](?:CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19|guard_orientation[/\\]README)\.md$',
    '^docs[/\\]reference[/\\]CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_BUILD_EVIDENCE_2026-07-23\.md$',
    '^docs[/\\]reference[/\\]CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_INDEPENDENT_REVIEW_2026-07-23\.md$',
    '^docs[/\\]reference[/\\]CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_INDEPENDENT_REVIEW_FINDINGS_2026-07-23\.md$',
    '^docs[/\\]reference[/\\]CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_WORK_ORDER_2026-07-23\.md$',
    '^docs[/\\]reference[/\\]CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_WORK_ORDER_AMENDMENT_1_2026-07-23\.md$',
    # Internal operation scripts - provenance repo only
    'scripts[/\\]cvf-provenance-push\.ps1$',
    'scripts[/\\]cvf-public-sync\.ps1$',
    '\.env$',
    '\.env\.local$',
    '\.env\.[^e]',
    '[/\\]node_modules[/\\]',
    '[/\\]\.next[/\\]',
    '[/\\]\.next-',
    '[/\\]coverage[/\\]',
    '[/\\]test-results[/\\]',
    '[/\\]playwright-report[/\\]',
    '[/\\]__pycache__[/\\]',
    '[/\\]\.data[/\\]',
    '(^|[/\\])\.cvf[/\\](runtime|config)([/\\]|$)',
    '\.jsonl$',
    'RAW',
    'HANDOFF',
    '\.tsbuildinfo$',
    '\.pyc$',
    '\.log$',
    '\.tmp$'
)

# Narrow public-safe exceptions for names that intentionally contain a
# blocked token. Keep this list aligned with the public-surface manifest;
# runtime state and receipt streams are never exceptions here.
$DENY_EXCEPTIONS = @(
    'workspace_templates\AGENT_HANDOFF_TEMPLATE.md',
    'EXTENSIONS\CVF_GUARD_CONTRACT\src\runtime\agent-handoff.ts',
    'EXTENSIONS\CVF_GUARD_CONTRACT\src\runtime\agent-handoff.test.ts',
    'EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\src\lib\agent-handoff-validator.ts',
    'EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\src\lib\agent-handoff-validator.test.ts',
    'EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\src\app\api\execute\route.web-build-handoff.alibaba.live.test.ts',
    'EXTENSIONS\CVF_v1.6_AGENT_PLATFORM\cvf-web\src\lib\spec-export-portable-handoff.ts',
    'EXTENSIONS\CVF_CONTROL_PLANE_FOUNDATION\src\agent.handoff.contract.ts',
    'EXTENSIONS\CVF_CONTROL_PLANE_FOUNDATION\tests\agent.handoff.contract.test.ts',
    'EXTENSIONS\CVF_v1.2.1_EXTERNAL_INTEGRATION\models\external-skill.raw.ts',
    'EXTENSIONS\CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS\product_ux\claude_design_handoff.skill.md',
    'governance\compat\check_agent_handoff_guard_compat.py',
    'governance\compat\test_check_agent_handoff_guard_compat.py',
    'governance\toolkit\05_OPERATION\CVF_AGENT_HANDOFF_GUARD.md',
    'governance\toolkit\05_OPERATION\CVF_AGENT_HANDOFF_TRANSITION_GUARD.md',
    'docs\reference\CVF_AGENT_HANDOFF_TEMPLATE.md',
    'docs\reference\CVF_ADR_AGENT_HANDOFF_CONTRACT_RELATIONSHIP_2026-05-17.md'
)

# -----------------------------------------------------------------------

function Test-Denied {
    param([string]$RelPath)
    $normalized = $RelPath -replace '/', '\'
    if ($normalized -in $DENY_EXCEPTIONS) { return $false }
    foreach ($pattern in $DENY_PATTERNS) {
        if ($RelPath -match $pattern) { return $true }
    }

    # A governed artifact that explicitly declares a non-export disposition is
    # private by contract even when it sits below an otherwise allowed tree.
    # Limit the search to the artifact's own disposition section so standards
    # and templates that merely document the vocabulary remain exportable.
    $sourcePath = Join-Path $GOVERNANCE_ROOT $RelPath
    if ($RelPath -match '\.md$' -and (Test-Path $sourcePath -PathType Leaf)) {
        $content = Get-Content -LiteralPath $sourcePath -Raw
        $sectionPattern = '(?ms)^## Public Export Disposition\s*\r?\n(?<body>.*?)(?=^##\s|\z)'
        $section = [regex]::Match($content, $sectionPattern)
        if ($section.Success -and
            $section.Groups['body'].Value -match '(?m)^\s*(?:Disposition:\s*)?`?(?:DEFERRED_PRIVATE_ONLY|BLOCKED_MISSING_PUBLIC_ARTIFACTS)`?\s*$') {
            return $true
        }
    }

    return $false
}

function Get-AllowedFiles {
    $files = [System.Collections.Generic.List[string]]::new()

    # Root-level files
    foreach ($f in $ALLOWED_ROOT_FILES) {
        $full = Join-Path $GOVERNANCE_ROOT $f
        if (Test-Path $full -PathType Leaf) { $files.Add($f) }
    }

    # Public-safe scripts
    foreach ($scriptPath in $ALLOWED_SCRIPT_FILES) {
        $full = Join-Path $GOVERNANCE_ROOT $scriptPath
        if (Test-Path $full -PathType Leaf) { $files.Add($scriptPath) }
    }

    foreach ($templatePath in $ALLOWED_WORKSPACE_TEMPLATE_FILES) {
        $full = Join-Path $GOVERNANCE_ROOT $templatePath
        if (Test-Path $full -PathType Leaf) { $files.Add($templatePath) }
    }

    # Allowed directory trees
    foreach ($tree in $ALLOWED_TREES) {
        $treeRoot = Join-Path $GOVERNANCE_ROOT $tree
        if (-not (Test-Path $treeRoot)) { continue }
        Get-ChildItem -Recurse -File $treeRoot | ForEach-Object {
            $rel = $_.FullName.Substring($GOVERNANCE_ROOT.Length + 1)
            if (-not (Test-Denied $rel)) { $files.Add($rel) }
        }
    }

    # docs/ sub-paths
    foreach ($docPath in $ALLOWED_DOCS_PATHS) {
        $full = Join-Path $GOVERNANCE_ROOT $docPath
        if (-not (Test-Path $full)) { continue }
        if (Test-Path $full -PathType Leaf) {
            if (-not (Test-Denied $docPath)) { $files.Add($docPath) }
        } else {
            Get-ChildItem -Recurse -File $full | ForEach-Object {
                $rel = $_.FullName.Substring($GOVERNANCE_ROOT.Length + 1)
                if (-not (Test-Denied $rel)) { $files.Add($rel) }
            }
        }
    }

    return ($files | Sort-Object -Unique)
}

# -----------------------------------------------------------------------

# Validate governance repo
if (-not (Test-Path $GOVERNANCE_ROOT)) {
    Write-Host "[ABORT] Governance repo not found: $GOVERNANCE_ROOT" -ForegroundColor Red
    exit 1
}

# Validate public-sync repo
if (-not (Test-Path $PUBLIC_SYNC_ROOT)) {
    Write-Host "[ABORT] Public-sync repo not found: $PUBLIC_SYNC_ROOT" -ForegroundColor Red
    exit 1
}

# Validate public-sync remote URL
$pubRemote = git -C $PUBLIC_SYNC_ROOT remote get-url origin 2>$null
if ($pubRemote -ne $PUBLIC_REMOTE) {
    Write-Host '[ABORT] Public-sync repo origin does not match expected URL.' -ForegroundColor Red
    Write-Host "        Expected : $PUBLIC_REMOTE"
    Write-Host "        Found    : $pubRemote"
    exit 1
}

# -----------------------------------------------------------------------

Write-Host ''
Write-Host 'CVF Public Sync' -ForegroundColor Cyan
Write-Host '===============' -ForegroundColor Cyan
Write-Host "  From : $GOVERNANCE_ROOT"
Write-Host "  To   : $PUBLIC_SYNC_ROOT"
if ($DryRun) { Write-Host '  Mode : DRY RUN' -ForegroundColor Yellow }
if ($NoPush) { Write-Host '  Push : DISABLED (-NoPush)' -ForegroundColor Yellow }
Write-Host ''

Write-Host 'Collecting allowed files...' -ForegroundColor Yellow
$allowedFiles = Get-AllowedFiles
if ($WorkspaceKitOnly) {
    $allowedFiles = @($allowedFiles | Where-Object { $_ -in $WORKSPACE_KIT_FILES })
}
Write-Host "  $($allowedFiles.Count) files in allowlist."
Write-Host ''

if ($DryRun) {
    Write-Host 'Files that would be synced (first 50):' -ForegroundColor Yellow
    $allowedFiles | Select-Object -First 50 | ForEach-Object { Write-Host "  + $_" }
    if ($allowedFiles.Count -gt 50) {
        Write-Host "  ... and $($allowedFiles.Count - 50) more"
    }
    Write-Host ''
    Write-Host 'Mapped exports:' -ForegroundColor Yellow
    foreach ($mapping in $MAPPED_FILES) {
        Write-Host "  + $($mapping.Source) -> $($mapping.Destination)"
    }
    Write-Host ''
    Write-Host 'DRY RUN complete. No changes made.' -ForegroundColor Cyan
    exit 0
}

# Copy files
Write-Host 'Copying files...' -ForegroundColor Yellow
$copied  = 0
$denied  = 0

foreach ($rel in $allowedFiles) {
    $src = Join-Path $GOVERNANCE_ROOT $rel
    $dst = Join-Path $PUBLIC_SYNC_ROOT $rel

    if (Test-Denied $rel) {
        Write-Host "  [DENIED] $rel" -ForegroundColor Red
        $denied++
        continue
    }

    $dstDir = Split-Path $dst -Parent
    if (-not (Test-Path $dstDir)) {
        New-Item -ItemType Directory -Force $dstDir | Out-Null
    }
    Copy-Item -Force $src $dst
    $copied++
}

foreach ($mapping in $MAPPED_FILES) {
    $src = Join-Path $GOVERNANCE_ROOT $mapping.Source
    $dst = Join-Path $PUBLIC_SYNC_ROOT $mapping.Destination
    if (-not (Test-Path $src -PathType Leaf)) {
        throw "Mapped public export source not found: $src"
    }
    $dstDir = Split-Path $dst -Parent
    if (-not (Test-Path $dstDir)) {
        New-Item -ItemType Directory -Force $dstDir | Out-Null
    }
    Copy-Item -Force $src $dst
    $copied++
}

# Project the Guard Contract barrel from its canonical source while removing
# only export statements whose referenced contract module is intentionally
# absent from the public projection. This preserves public runtime exports
# (including the mandatory gateway) without leaking private capability grants.
$guardIndexSource = Join-Path $GOVERNANCE_ROOT 'EXTENSIONS\CVF_GUARD_CONTRACT\src\index.ts'
$guardIndexDestination = Join-Path $PUBLIC_SYNC_ROOT 'EXTENSIONS\CVF_GUARD_CONTRACT\src\index.ts'
$guardIndexContent = Get-Content -LiteralPath $guardIndexSource -Raw
$missingGuardModules = [System.Collections.Generic.List[string]]::new()
$guardExportPattern = "(?ms)^export(?:\s+type)?\s*\{.*?\}\s+from\s+'(?<module>\./contracts/[^']+)';\s*\r?\n"
$guardIndexProjected = [regex]::Replace($guardIndexContent, $guardExportPattern, {
    param($match)
    $module = $match.Groups['module'].Value
    $relativeModule = ($module.Substring(2) -replace '/', '\') + '.ts'
    $publicModule = Join-Path (Split-Path $guardIndexDestination -Parent) $relativeModule
    if (-not (Test-Path $publicModule -PathType Leaf)) {
        $missingGuardModules.Add($module)
        return ''
    }
    return $match.Value
})
if ($missingGuardModules.Count -eq 0) {
    throw 'Expected at least one private/deferred Guard Contract module to be removed from the public barrel.'
}
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($guardIndexDestination, $guardIndexProjected, $utf8NoBom)
$copied++
Write-Host "Projected public Guard Contract barrel; removed $($missingGuardModules.Count) absent module export blocks." -ForegroundColor Yellow

# Rebuild generated catalog output from the public projection's own compact
# entries. The provenance aggregate may include private/deferred entries that
# this allowlist correctly omits, so copying that aggregate verbatim would
# leave the public projection internally inconsistent.
$catalogGenerator = Join-Path $PUBLIC_SYNC_ROOT 'governance\compat\generate_as_built_system_catalog.py'
if (-not (Test-Path $catalogGenerator -PathType Leaf)) {
    throw "Public catalog generator not found: $catalogGenerator"
}
Write-Host 'Regenerating public as-built catalog aggregate...' -ForegroundColor Yellow
& python $catalogGenerator --target catalog --json
if ($LASTEXITCODE -ne 0) {
    throw "Public catalog aggregate generation failed with exit code $LASTEXITCODE"
}

Write-Host "  Copied : $copied"
Write-Host "  Denied : $denied"
Write-Host ''

# Commit
Set-Location $PUBLIC_SYNC_ROOT

$gitStatus = git status --porcelain
if (-not $gitStatus) {
    Write-Host 'No changes detected in public-sync repo. Nothing to commit.' -ForegroundColor Yellow
    exit 0
}

if ($NoCommit) {
    Write-Host 'Public-sync worktree updated. Skipping commit and push (-NoCommit).' -ForegroundColor Yellow
    Write-Host "Review pending changes in: $PUBLIC_SYNC_ROOT" -ForegroundColor Yellow
    exit 0
}

# Fail closed before `git add -A`: tests and local tooling may leave runtime,
# receipt, cache, or evidence files in the public worktree. Only files owned by
# this exact projection are eligible for staging.
$authorizedPending = [System.Collections.Generic.HashSet[string]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)
foreach ($path in $allowedFiles) {
    [void]$authorizedPending.Add(($path -replace '/', '\'))
}
foreach ($mapping in $MAPPED_FILES) {
    [void]$authorizedPending.Add(($mapping.Destination -replace '/', '\'))
}
[void]$authorizedPending.Add('EXTENSIONS\CVF_GUARD_CONTRACT\src\index.ts')
[void]$authorizedPending.Add('docs\reference\system_architecture_catalog\CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json')

$pendingPaths = @(
    git diff --name-only
    git diff --cached --name-only
    git ls-files --others --exclude-standard
) | Where-Object { $_ } | Sort-Object -Unique
$unexpectedPending = @(
    $pendingPaths | Where-Object {
        -not $authorizedPending.Contains(($_ -replace '/', '\'))
    }
)
if ($unexpectedPending.Count -gt 0) {
    throw "Public-sync worktree contains paths not owned by this projection: $($unexpectedPending -join ', ')"
}

$govHead = git -C $GOVERNANCE_ROOT rev-parse --short HEAD
$govMsg  = git -C $GOVERNANCE_ROOT log -1 --pretty=%s

Write-Host 'Staging changes...' -ForegroundColor Yellow
git add -A
foreach ($mapping in $MAPPED_FILES) {
    git add -f -- $mapping.Destination
}

$commitMsg = @"
sync: public surface update from governance@$govHead

Source: $govHead - $govMsg

Synced via cvf-public-sync.ps1 allowlist.
Internal artifacts excluded: AGENT_HANDOFF, baselines, reviews, roadmaps.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
"@

Write-Host 'Committing...' -ForegroundColor Yellow
git commit -m $commitMsg
Write-Host ''

# Push
if (-not $NoPush) {
    Write-Host "Pushing to $PUBLIC_REMOTE ..." -ForegroundColor Yellow
    git push origin main
    Write-Host ''
    Write-Host 'Public sync complete.' -ForegroundColor Green
} else {
    Write-Host 'Committed locally. Skipping push (-NoPush).' -ForegroundColor Yellow
    Write-Host "Run 'git push origin main' in $PUBLIC_SYNC_ROOT when ready." -ForegroundColor Yellow
}

Write-Host ''
