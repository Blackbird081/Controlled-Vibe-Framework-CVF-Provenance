# CVF Agent Work Order - RTAD-T6 External Agent MCP Workspace Absorption

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: work_order

## Dispatch Prompt Envelope

Prompt to worker:

Read the GC-018 packet first, then close a bounded CVF-owned absorption tranche.
Create stable reference context so external agents distinguish public/simple
workflow vocabulary from internal governed CVF workflow-chain authority. Absorb
useful MCP/workspace patterns from Foundry and the local external workspace
package without importing raw external code or treating external files as CVF
authority. Keep runtime, MCP implementation, provider calls, public-sync,
production readiness, and public readiness out of scope.

## Purpose

Close RTAD-T6 as a documentation/reference tranche that improves external-agent
review context and MCP/workspace foundation knowledge.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active next move | `CVF_SESSION/state/entries/nextAllowedMove.json` | ACCEPT |
| RTAD roadmap | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_2026-06-18.md` | ACCEPT |
| Agent Handoff Contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| Foundation storage | `docs/reference/foundation_storage/README.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Dispatcher | Codex |
| Worker | Codex |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex after material commit |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `docs/reference/external_agent_review/README.md`
- `docs/reference/mcp_gateway/README.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/foundation_storage/README.md`

## Pre-Flight Checks

| Check | Result |
|---|---|
| Startup state resolved | PASS |
| Raw external package classified as non-canonical | PASS |
| Scope excludes runtime implementation and public-sync | PASS |
| Dispatch prompt envelope appears first | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| routeToken | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Codex dispatcher/worker/reviewer/closer |
| phase | closure |
| dispatchBaseHead | `c5033df4` |
| executionBaseHead | `c5033df4` |
| closureBaseHead | `c5033df4` |
| baseHeadFor(phase) | `c5033df4` |
| changedSetScope(phase) | reference docs, GC-018, work order, completion, roadmap, GC-051 entries, `.gitignore` |
| traceScope(phase, actor) | exact material manifest in this work order and completion packet |
| commitOwner(phase) | Codex |
| crossBatchIsolation | no raw external package import; no public-sync; no runtime implementation |
| nextMoveSurfaces | session-sync after material commit |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | external package absorption and future workspace/MCP context only |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | stable reference files under `docs/reference/`; dated execution files under `docs/baselines`, `docs/work_orders`, and `docs/reviews` |
| Handoff fields | inherited from Agent Handoff Contract Control Block |
| State ownership | no workspace state source mutation |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | workspace runtime queues, workspace UI, runtime source, provider proof, public-sync, and registry edits are forbidden |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/foundation_storage/README.md` |
| stableFrontDoor | `docs/reference/external_agent_review/README.md` |
| stableFamilyFiles | `docs/reference/external_agent_review/`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` |
| datedExecutionFiles | GC-018, work order, completion |
| rawExternalPackage | ignored and not committed |
| indexUpdates | MCP, agent workspace, operational reference, RTAD roadmap, GC-051 |

## Source Verification

Source verification is inherited from:

`docs/baselines/CVF_GC018_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_2026-06-18.md`

## Execution Plan

1. Create stable external-agent review context front door and standards.
2. Create CVF-owned external package absorption map.
3. Update MCP and agent workspace front doors.
4. Update RTAD roadmap and GC-051 entries.
5. Keep copied raw external package ignored and uncommitted.
6. Run governance gates and commit bounded material.

## Write Ownership

Codex owns this bounded material commit and later session-sync commit. Raw
external package files remain local ignored input and are not commit-owned by
this work order.

## Evidence Requirements

| Evidence | Required |
|---|---|
| Source verification | GC-018 source verification table |
| External input classification | absorption map |
| Registry coverage | GC-051 source entries plus generated aggregate |
| Raw package boundary | `.gitignore` entry and clean status after commit |
| Closure gates | worker-return fast gate, pre-closure, pre-push/session-sync as applicable |

## Review Gate

Codex reviewer must confirm that the output is reference-only and does not
promote public/simple workflow labels into internal CVF authority.

## Closure Checklist

- [x] External-agent review context front door created.
- [x] Workflow-chain public review context created.
- [x] Package absorption map created.
- [x] MCP/workspace indexes updated.
- [x] Raw external package ignored.
- [x] GC-051 source entries created.

## Return-To-Orchestrator Conditions

Return to operator only if implementation, public-sync, provider live proof, or
raw package import becomes necessary. None became necessary in this tranche.

## Operator Checkpoint

Operator requested that CVF remain the origin, that useful external patterns be
absorbed selectively, and that existing package files be reused through CVF
rules rather than rewritten wholesale.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| RTAD-T6-AC1 | External-agent review context explains CVF source-of-truth and public/private boundary. |
| RTAD-T6-AC2 | Workflow-chain public review context rejects hard-coded public/simple lifecycle enum as internal authority. |
| RTAD-T6-AC3 | External workspace package has a CVF-owned absorption map. |
| RTAD-T6-AC4 | MCP/workspace front doors point to the absorbed local views. |
| RTAD-T6-AC5 | Raw external package is not committed. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_FOR_CODEX_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md` | RTAD-T6 row and closure note | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry exists for this reference family | no path required | BLOCKED with reason |
| External evidence digest | BLOCKED with reason: no external evidence digest path is authorized in this reference-only tranche | no path required | BLOCKED with reason |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path required | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit | N/A with reason |
| External raw package | `.gitignore` | package path ignored and not staged | PASS |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance reference absorption. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 RTAD-T6 external-agent MCP/workspace absorption |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, web/github inspection, local package smoke test, apply_patch |
| Target paths | `.gitignore`; `docs/reference/external_agent_review/`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; MCP/workspace front doors; RTAD roadmap; GC-018; work order; completion; GC-051 entries |
| Allowed scope source | operator request to handle external-agent context, Foundry audit, and local package absorption |
| Before status evidence | base `c5033df4` |
| After status evidence | RTAD-T6 material commit ready |
| Diff evidence | `git diff --name-status c5033df4..HEAD` |
| Approval boundary | bounded reference/absorption only |
| Claim boundary | no raw package import, MCP implementation, runtime execution, provider call, public-sync, production/public readiness |
| Agent type | Codex implementer/closer |
| Invocation ID | `rtad-t6-external-agent-mcp-workspace-absorption-2026-06-18` |
| Expected manifest | `.gitignore`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md`; `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/mcp_gateway/README.md`; `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/baselines/CVF_GC018_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_FOR_CODEX_2026-06-18.md`; `docs/reviews/CVF_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_COMPLETION_2026-06-18.md`; `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/rtad-t6-external-agent-mcp-workspace-absorption-completion.json`; `docs/corpus-intelligence/registry/entries/rtad-t6-external-agent-review-context-reference.json` |
| Actual changed set | `.gitignore`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md`; `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/mcp_gateway/README.md`; `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/baselines/CVF_GC018_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_FOR_CODEX_2026-06-18.md`; `docs/reviews/CVF_RTAD_T6_EXTERNAL_AGENT_MCP_WORKSPACE_ABSORPTION_COMPLETION_2026-06-18.md`; `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/rtad-t6-external-agent-mcp-workspace-absorption-completion.json`; `docs/corpus-intelligence/registry/entries/rtad-t6-external-agent-review-context-reference.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order is closed bounded as documentation/reference absorption. It
does not implement runtime behavior.
