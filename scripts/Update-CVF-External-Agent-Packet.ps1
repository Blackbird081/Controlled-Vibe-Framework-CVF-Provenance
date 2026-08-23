<#
.SYNOPSIS
Refreshes the reusable CVF external-agent packet, prepares a repo-specific
task capsule, or validates a returned folder.

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode RefreshSnapshot

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode PrepareTask `
  -TaskId mcp-review-002 -Title 'Review MCP repository' `
  -Objective 'Create an absorption-ready source pack' `
  -WorkingMode SOURCE_PACK_PREPARATION `
  -SourceRepository 'https://github.com/modelcontextprotocol/modelcontextprotocol.git' `
  -SourceCommit '0000000000000000000000000000000000000000' `
  -OutputRoot 'D:\UNG DUNG AI\EXTERNAL_RETURNS\MCP_REVIEW_002'

.EXAMPLE
.\scripts\Update-CVF-External-Agent-Packet.ps1 -Mode ValidateReturn `
  -ReturnRoot 'D:\UNG DUNG AI\EXTERNAL_RETURNS\MCP_REVIEW_002'
#>
[CmdletBinding()]
param(
    [ValidateSet('RefreshSnapshot', 'PrepareTask', 'ValidateReturn')]
    [string]$Mode = 'RefreshSnapshot',
    [string]$PublicRepoPath = 'D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync',
    [string]$PacketRoot = 'D:\UNG DUNG AI\EXTERNAL_AGENT_READ',
    [string]$TaskId,
    [string]$Title,
    [string]$Objective,
    [ValidateSet('REVIEW_ONLY', 'DESIGN_ONLY', 'BUILD_NEW_REPOSITORY', 'EXTEND_SUPPLIED_REPOSITORY', 'SOURCE_PACK_PREPARATION')]
    [string]$WorkingMode = 'REVIEW_ONLY',
    [string]$SourceRepository,
    [string]$SourceCommit,
    [string]$OutputRoot,
    [string[]]$NonGoal = @(),
    [string]$ReturnRoot,
    [string]$Receipt
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$tool = Join-Path $repoRoot 'scripts\external_agent_packet.py'
$ownerIndex = Join-Path $repoRoot 'docs\reference\external_agent_review\CVF_EXTERNAL_AGENT_OWNER_SURFACE_INDEX.json'

if ($Mode -eq 'RefreshSnapshot') {
    & python $tool refresh-snapshot --public-repo $PublicRepoPath --packet-root $PacketRoot --owner-index-source $ownerIndex
} elseif ($Mode -eq 'PrepareTask') {
    foreach ($required in @('TaskId', 'Title', 'Objective', 'SourceRepository', 'SourceCommit', 'OutputRoot')) {
        if (-not (Get-Variable -Name $required -ValueOnly)) { throw "$required is required for PrepareTask" }
    }
    $arguments = @($tool, 'prepare-task', '--public-repo', $PublicRepoPath, '--packet-root', $PacketRoot,
        '--owner-index-source', $ownerIndex, '--task-id', $TaskId, '--title', $Title, '--objective', $Objective,
        '--working-mode', $WorkingMode, '--source-repository', $SourceRepository, '--source-commit', $SourceCommit,
        '--output-root', $OutputRoot)
    foreach ($item in $NonGoal) { $arguments += @('--non-goal', $item) }
    & python @arguments
} else {
    if (-not $ReturnRoot) { throw 'ReturnRoot is required for ValidateReturn' }
    $arguments = @($tool, 'validate-return', '--return-root', $ReturnRoot)
    if ($Receipt) { $arguments += @('--receipt', $Receipt) }
    & python @arguments
}

exit $LASTEXITCODE
