# CVF Work Order — Delta D2 MCP Write/Submit Tools

Memory class: FULL_RECORD

Status: DEMAND_GATED

docType: work_order

Date: 2026-05-29

---

## Purpose

Add `cvf_submit_review_receipt` and `cvf_advance_pipeline_stage` write-path
tools to the MCP server — closing the gap where Reviewer/Closure Gate agents
must bypass the governance control plane to submit receipts.

Per `.private_reference/legacy/CVF 28.05/CLI & MCP.md` design intent:
"Reviewer không tự viết file báo cáo, mà nó phải gọi Tool
`cvf_submit_review_receipt()` qua MCP. MCP Server sẽ đứng sau kiểm tra xem
báo cáo có đúng chuẩn Markdown luật không."

**DEMAND_GATED.** Operator must explicitly authorize D2 after D1 CLOSED_PASS.
D2 is a write-path implementation — security review required before dispatch.

## Authority Chain

- Delta roadmap: `docs/roadmaps/CVF_DELTA_CLI_MCP_WIREIN_ROADMAP_2026-05-29.md`
- Delta GC-018: `docs/baselines/CVF_GC018_DELTA_CLI_MCP_WIREIN_2026-05-29.md`
- MCP server: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` (551 lines, 14 tools)
- EL-1 source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
  — `advancePipelineStage()` line 257, `PipelineChainState` line 173
- **D1 gate: `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS**

## Agent Roles

Implementer adds two MCP tools. Security Reviewer checks input validation,
audit trail, caller authentication boundary, and write-path risks. Auditor
confirms D1 gate and advisory-only posture for `cvf_advance_pipeline_stage`.
No self-review.

## Scope

**Allowed (after authorization):**

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` (add 2 tools)
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/` supporting modules if needed
- MCP test files
- `docs/reviews/CVF_DELTA_D2_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_DELTA_D2_MCP_WRITE_SUBMIT_TOOLS_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `route.ts`, sandboxed execution, process spawning, public-sync.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
   — confirm 14 existing tools; confirm current line count
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
   — confirm `advancePipelineStage()` at line 257; confirm `PipelineStageResult` at line 133
5. `docs/reviews/CVF_DELTA_D1_PIPELINE_CHAIN_READOUT_COMPLETION_2026-05-29.md`
   — confirm D1 CLOSED_PASS

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `advancePipelineStage()` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 257 | `advancePipelineStage` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| `PipelineStageResult` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 133 | `PipelineStageResult` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| `PipelineChainState` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 173 | `PipelineChainState` | `pipeline-chain-orchestrator.ts` | ACCEPT |
| MCP server tool count | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | 14 `server.tool()` calls | 14 existing tools | MCP server | ACCEPT |

New tools (write-path, require security review):

| New MCP tool | Write risk | Input validation required | Audit trail |
| --- | --- | --- | --- |
| `cvf_submit_review_receipt` | Writes to governance store | Receipt schema validation; caller role check | Per-submission audit entry |
| `cvf_advance_pipeline_stage` | Updates pipeline state | `PipelineStageResult` schema; valid transition check | Per-advance audit entry |

## Pre-Flight

- [ ] D1 CLOSED_PASS confirmed
- [ ] Security review completed and documented
- [ ] `advancePipelineStage()` confirmed at pipeline-chain-orchestrator.ts line 257
- [ ] MCP server current line count confirmed
- [ ] Write-path audit store location identified

## Write Ownership

Implementer owns all new and modified files. Only files in Allowed list may
be touched. `route.ts` and non-MCP app files are off-limits.

## Execution Plan

1. Read all required first reads; confirm D1 gate.
2. Complete security review document for write-path tools.
3. Implement `cvf_submit_review_receipt` with input validation + audit entry.
4. Implement `cvf_advance_pipeline_stage` with `PipelineStageResult` validation.
5. Write tests for both tools.
6. Run full MCP test suite — all PASS.
7. Run TypeScript check.
8. Run governance gates.
9. Update session continuity.
10. Commit.
11. Write Fast Lane audit + completion review with D3 gate answer.

## Evidence Requirements

- Security review document completed before implementation
- `cvf_submit_review_receipt`: validates receipt schema; creates audit entry
- `cvf_advance_pipeline_stage`: validates `PipelineStageResult`; returns updated state
- All existing 14 MCP tests still PASS
- New tool tests PASS
- TypeScript PASS
- No process spawning in either tool

## Acceptance Criteria

- [ ] D1 CLOSED_PASS confirmed
- [ ] Security review completed and documented before implementation
- [ ] `cvf_submit_review_receipt` tool: validates receipt schema; writes to audit store; creates audit entry
- [ ] `cvf_advance_pipeline_stage` tool: validates `PipelineStageResult`; calls `advancePipelineStage()`; returns updated state
- [ ] All existing 14 MCP tests still PASS
- [ ] New tests PASS for both tools
- [ ] TypeScript PASS
- [ ] No process spawning in either tool
- [ ] D3 gate answer in completion review

## Review Gate

D1 confirmed; security review documented; both tools validated; no process
spawning; all tests PASS; TypeScript PASS.

## Closure Checklist

- [ ] D1 CLOSED_PASS confirmed
- [ ] Security review completed
- [ ] Both tools implemented with input validation + audit trail
- [ ] All tests PASS
- [ ] TypeScript PASS
- [ ] Fast Lane audit PASS
- [ ] Session continuity updated
- [ ] Completion review with D3 gate answer written

## Return-To-Orchestrator Conditions

Stop if: D1 not confirmed; security review cannot be completed; write-path
validation cannot be bounded; tests fail.

## D3 Gate Output

Was the MCP → CLI bridge gap confirmed during D2?

**Expected YES:** D2 write tools exist, but agents still cannot invoke CLI
execution stages through MCP. `cvf_invoke_cli_stage` connecting `runCli()` to
MCP does not exist. D3 closes that gap — but requires sandbox boundary design
first.

## Operator Checkpoint

DEMAND_GATED — operator must authorize D2 explicitly after D1 closes.
Security review document must accompany authorization.

## Claim Boundary

D2 produces two MCP write tools. It does not claim sandboxed terminal execution,
MCP → CLI bridge, production readiness, hosted readiness, or public release
readiness.
