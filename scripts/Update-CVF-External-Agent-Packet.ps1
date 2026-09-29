<#
.SYNOPSIS
Refreshes the reusable CVF external-agent packet, prepares a repo-specific
task capsule (live or offline), or validates a returned folder.

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode RefreshSnapshot

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode PrepareTask `
  -TaskId mcp-review-002 -Title 'Review MCP repository' `
  -Objective 'Create an absorption-ready source pack' `
  -WorkingMode SOURCE_PACK_PREPARATION `
  -SourceRepository 'https://github.com/modelcontextprotocol/modelcontextprotocol.git' `
  -SourceCommit '0000000000000000000000000000000000000000' `
  -SourceLicenseExpression 'MIT' `
  -SourceLicenseSource 'https://github.com/modelcontextprotocol/modelcontextprotocol/blob/0000000000000000000000000000000000000000/LICENSE' `
  -SourceImmutableReference 'https://github.com/modelcontextprotocol/modelcontextprotocol/blob/0000000000000000000000000000000000000000/README.md' `
  -OutputRoot 'D:\UNG DUNG AI\EXTERNAL_RETURNS\MCP_REVIEW_002'

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode PrepareTaskOffline `
  -PacketRoot 'D:\UNG DUNG AI\EXTERNAL_AGENT_READ' `
  -CvfPublicCommit '1111111111111111111111111111111111111111' `
  -ContextFile 'D:\UNG DUNG AI\context.json' `
  -TaskId coding-task-003 -Title 'Extend module X' `
  -Objective 'Add feature Y' `
  -WorkingMode EXTEND_SUPPLIED_REPOSITORY `
  -SourceRepository 'https://github.com/example/repo.git' `
  -SourceCommit '2222222222222222222222222222222222222222' `
  -OutputRoot 'D:\UNG DUNG AI\EXTERNAL_RETURNS\CODING_TASK_003'

This mode makes zero network or Git-remote calls; -CvfPublicCommit is an
operator-pinned commit, not live-verified against public origin/main.

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode ValidateReturn `
  -ReturnRoot 'D:\UNG DUNG AI\EXTERNAL_RETURNS\MCP_REVIEW_002'

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode ValidateDetachedReturn `
  -ReturnRoot 'D:\UNG DUNG AI\EXTERNAL_RETURNS\CODING_TASK_003' `
  -TaskCapsule 'D:\UNG DUNG AI\EXTERNAL_AGENT_READ\CVF_EXTERNAL_AGENT_TASK_CAPSULE.json'
#>
[CmdletBinding()]
param(
    [ValidateSet('RefreshSnapshot', 'PrepareTask', 'PrepareTaskOffline', 'ValidateReturn', 'ValidateDetachedReturn')]
    [string]$Mode = 'RefreshSnapshot',
    [string]$PublicRepoPath = 'D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync',
    [string]$PacketRoot = 'D:\UNG DUNG AI\EXTERNAL_AGENT_READ',
    [string]$TaskId,
    [string]$Title,
    [string]$Objective,
    [ValidateSet('REVIEW_ONLY', 'DESIGN_ONLY', 'BUILD_NEW_REPOSITORY', 'EXTEND_SUPPLIED_REPOSITORY', 'SOURCE_PACK_PREPARATION', 'DETACHED_IMPLEMENTATION_PROPOSAL')]
    [string]$WorkingMode = 'REVIEW_ONLY',
    [ValidateSet('SHARED_WORKSPACE_DELEGATED_WORKER', 'DETACHED_EXTERNAL_AGENT')]
    [string]$ExecutionClass,
    [string]$SourceRepository,
    [string]$SourceCommit,
    [string]$SourceLicenseExpression,
    [string]$SourceLicenseSource,
    [string[]]$SourceImmutableReference = @(),
    [string]$OutputRoot,
    [string[]]$NonGoal = @(),
    [string]$ContextFile,
    [string]$CvfPublicCommit,
    [string]$ReturnRoot,
    [string]$TaskCapsule,
    [string]$Receipt
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$tool = Join-Path $repoRoot 'scripts\external_agent_packet.py'
$sourceCapsuleTool = Join-Path $repoRoot 'scripts\external_agent_source_capsule.py'
$ownerIndex = Join-Path $repoRoot 'docs\reference\external_agent_review\CVF_EXTERNAL_AGENT_OWNER_SURFACE_INDEX.json'

if ($Mode -eq 'RefreshSnapshot') {
    & python $tool refresh-snapshot --public-repo $PublicRepoPath --packet-root $PacketRoot --owner-index-source $ownerIndex
} elseif ($Mode -eq 'PrepareTask') {
    foreach ($required in @('TaskId', 'Title', 'Objective', 'SourceRepository', 'SourceCommit', 'OutputRoot')) {
        if (-not (Get-Variable -Name $required -ValueOnly)) { throw "$required is required for PrepareTask" }
    }
    $selectedTool = if ($WorkingMode -eq 'SOURCE_PACK_PREPARATION') { $sourceCapsuleTool } else { $tool }
    $arguments = @($selectedTool, 'prepare-task', '--public-repo', $PublicRepoPath, '--packet-root', $PacketRoot,
        '--owner-index-source', $ownerIndex, '--task-id', $TaskId, '--title', $Title, '--objective', $Objective,
        '--working-mode', $WorkingMode, '--source-repository', $SourceRepository, '--source-commit', $SourceCommit,
        '--output-root', $OutputRoot)
    if ($WorkingMode -eq 'SOURCE_PACK_PREPARATION') {
        foreach ($required in @('SourceLicenseExpression', 'SourceLicenseSource')) {
            if (-not (Get-Variable -Name $required -ValueOnly)) { throw "$required is required for SOURCE_PACK_PREPARATION" }
        }
        if ($SourceImmutableReference.Count -eq 0) { throw 'SourceImmutableReference is required for SOURCE_PACK_PREPARATION' }
        $arguments += @('--source-license-expression', $SourceLicenseExpression, '--source-license-source', $SourceLicenseSource)
        foreach ($item in $SourceImmutableReference) { $arguments += @('--source-immutable-reference', $item) }
    }
    if ($WorkingMode -eq 'DETACHED_IMPLEMENTATION_PROPOSAL') {
        if (-not $ExecutionClass) { throw 'ExecutionClass is required for DETACHED_IMPLEMENTATION_PROPOSAL' }
        $arguments += @('--execution-class', $ExecutionClass)
    }
    foreach ($item in $NonGoal) { $arguments += @('--non-goal', $item) }
    if ($ContextFile) { $arguments += @('--context-file', $ContextFile) }
    & python @arguments
} elseif ($Mode -eq 'PrepareTaskOffline') {
    foreach ($required in @('PacketRoot', 'CvfPublicCommit', 'ContextFile', 'TaskId', 'Title', 'Objective', 'SourceRepository', 'SourceCommit', 'OutputRoot')) {
        if (-not (Get-Variable -Name $required -ValueOnly)) { throw "$required is required for PrepareTaskOffline" }
    }
    $selectedTool = if ($WorkingMode -eq 'SOURCE_PACK_PREPARATION') { $sourceCapsuleTool } else { $tool }
    $arguments = @($selectedTool, 'create-capsule-offline', '--packet-root', $PacketRoot,
        '--cvf-public-commit', $CvfPublicCommit, '--context-file', $ContextFile,
        '--task-id', $TaskId, '--title', $Title, '--objective', $Objective,
        '--working-mode', $WorkingMode, '--source-repository', $SourceRepository, '--source-commit', $SourceCommit,
        '--output-root', $OutputRoot)
    if ($WorkingMode -eq 'SOURCE_PACK_PREPARATION') {
        foreach ($required in @('SourceLicenseExpression', 'SourceLicenseSource')) {
            if (-not (Get-Variable -Name $required -ValueOnly)) { throw "$required is required for SOURCE_PACK_PREPARATION" }
        }
        if ($SourceImmutableReference.Count -eq 0) { throw 'SourceImmutableReference is required for SOURCE_PACK_PREPARATION' }
        $arguments += @('--source-license-expression', $SourceLicenseExpression, '--source-license-source', $SourceLicenseSource)
        foreach ($item in $SourceImmutableReference) { $arguments += @('--source-immutable-reference', $item) }
    }
    if ($WorkingMode -eq 'DETACHED_IMPLEMENTATION_PROPOSAL') {
        if (-not $ExecutionClass) { throw 'ExecutionClass is required for DETACHED_IMPLEMENTATION_PROPOSAL' }
        $arguments += @('--execution-class', $ExecutionClass)
    }
    foreach ($item in $NonGoal) { $arguments += @('--non-goal', $item) }
    & python @arguments
} elseif ($Mode -eq 'ValidateDetachedReturn') {
    if (-not $ReturnRoot) { throw 'ReturnRoot is required for ValidateDetachedReturn' }
    if (-not $TaskCapsule) { throw 'TaskCapsule is required for ValidateDetachedReturn' }
    $arguments = @($tool, 'validate-detached-return', '--return-root', $ReturnRoot, '--task-capsule', $TaskCapsule)
    if ($Receipt) { $arguments += @('--receipt', $Receipt) }
    & python @arguments
} else {
    if (-not $ReturnRoot) { throw 'ReturnRoot is required for ValidateReturn' }
    $arguments = @($tool, 'validate-return', '--return-root', $ReturnRoot)
    if ($Receipt) { $arguments += @('--receipt', $Receipt) }
    & python @arguments
}

exit $LASTEXITCODE
