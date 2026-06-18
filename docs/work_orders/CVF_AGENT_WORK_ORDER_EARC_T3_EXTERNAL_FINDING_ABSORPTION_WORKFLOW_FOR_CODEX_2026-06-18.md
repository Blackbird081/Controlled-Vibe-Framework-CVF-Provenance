# CVF Agent Work Order - EARC-T3 External Finding Absorption Workflow

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: work_order

## Dispatch Prompt Envelope

Prompt to worker:

Read the EARC roadmap, EARC-T1 reference packet material, and GC-018 first.
Define the stable workflow for classifying returned external-agent output into
CVF-owned dispositions: governed finding candidate, useful pattern, public
assumption/question, missing context, blocked readiness/runtime claim, or
rejected raw private-source request. Update the external-agent review front
door/template/checklist so future agents must use the workflow before acting on
external output. Keep public-sync, MCP implementation, provider/live calls,
workspace runtime mutation, raw package import, checker implementation, and
readiness claims out of scope.

## Purpose

Close EARC-T3 as a bounded reference/workflow tranche for absorbing
external-agent review output into CVF governance.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active next move | `CVF_SESSION/state/entries/nextAllowedMove.json` | ACCEPT |
| EARC roadmap | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_2026-06-18.md` | ACCEPT |
| External-agent review front door | `docs/reference/external_agent_review/README.md` | ACCEPT |
| Finding-to-governance standard | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | ACCEPT |
| Agent Handoff Contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |

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
- `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`
- `docs/baselines/CVF_GC018_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_2026-06-18.md`
- `docs/reference/external_agent_review/README.md`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `docs/reference/foundation_storage/README.md`

## Pre-Flight Checks

| Check | Result |
|---|---|
| Startup state resolved | PASS |
| EARC-T3 target shape verified from roadmap | PASS |
| EARC-T1 packet/template material exists | PASS |
| Finding-to-governance standard read for reusable external findings | PASS |
| Scope excludes public-sync, MCP/runtime, provider/live, raw package import, checker implementation, and readiness claims | PASS |
| Dispatch prompt envelope appears first | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Codex dispatcher/worker/reviewer/closer/session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| dispatchBaseHead | `3f0cebf1` |
| executionBaseHead | `3f0cebf1` |
| closureBaseHead | `3f0cebf1` |
| baseHeadFor(phase) | `3f0cebf1` for material; material commit for later session-sync |
| changedSetScope(phase) | EARC-T3 GC-018, work order, external-agent review workflow/reference updates, EARC roadmap, GC-051 registry entry, completion |
| traceScope(phase, actor) | exact material manifest in this work order and completion packet |
| commitOwner(phase) | Codex |
| crossBatchIsolation | clean worktree before EARC-T3; no public-sync, MCP/runtime/provider/raw-package/checker implementation work |
| nextMoveSurfaces | session-sync after material commit if next allowed move changes |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md` |
| Storage class | stable local-view foundation folder under `docs/reference/external_agent_review/` |
| Index/front door | `docs/reference/external_agent_review/README.md` |
| Date policy | stable filename without date suffix for durable workflow; dated GC-018/work order/completion for execution evidence |
| Archive disposition | N/A with reason: no superseded active file in this batch |
| Deferred layout work | N/A with reason: folder index is updated in this batch |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | external-output classification workflow only; no workspace build |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | stable external-agent review reference files; no workspace state source mutation |
| Handoff fields | inherited from Agent Handoff Contract Control Block |
| State ownership | N/A with reason: no workspace state, queue, inbox, dashboard, or runtime item is created |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | workspace runtime queues, workspace UI, runtime source, provider proof, public-sync, executable workspace behavior, and product-runtime registry edits are forbidden; the only registry edits allowed are GC-051 reference coverage entries listed in the material manifest |

## Source Verification

Source verification is recorded in:

`docs/baselines/CVF_GC018_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_2026-06-18.md`

## Execution Plan

1. Create the stable external-agent finding absorption workflow.
2. Update the external-agent review folder README, packet template, and
   authoring checklist to require the workflow after external review.
3. Update EARC roadmap tranche status and closure note.
4. Add GC-051 registry source entry and regenerate aggregate.
5. Author completion packet and run gates.
6. Commit material, then sync session continuity if the next move changes.

## Write Ownership

Codex owns the bounded material commit and the later session-sync commit. Raw
external package files, public-sync clone, runtime source, provider keys, MCP
implementation, checker implementation, and workspace runtime state are not
owned by this work order.

## Evidence Requirements

| Evidence | Required |
|---|---|
| Source verification | GC-018 source verification table |
| Stable workflow | `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` |
| Stable front door | README indexes and routes to the workflow |
| Registry coverage | GC-051 source entry plus generated aggregate |
| Closure gates | worker-return fast gate, commit steward preflight, pre-closure, pre-push/session-sync as applicable |

## Review Gate

Codex reviewer must confirm that EARC-T3 classifies external output before CVF
acts on it and does not make external-agent commentary canonical by itself.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| EARC-T3-AC1 | Stable external-agent finding absorption workflow exists. |
| EARC-T3-AC2 | Workflow maps returned external output to CVF-owned dispositions and next actions. |
| EARC-T3-AC3 | README/template/checklist point future agents to the workflow. |
| EARC-T3-AC4 | Completion records machine-check follow-up without implementing a checker in this tranche. |
| EARC-T3-AC5 | No public-sync, MCP implementation, provider call, workspace runtime mutation, raw package import, checker implementation, or readiness claim is introduced. |

## Closure Checklist

- [x] GC-018 source verification authored.
- [x] Absorption workflow authored.
- [x] Folder front door updated.
- [x] Packet template and checklist updated.
- [x] Roadmap tranche state updated.
- [x] GC-051 entry added and aggregate regenerated.
- [x] Completion packet authored.

## Return-To-Orchestrator Conditions

Return to operator only if public-sync, MCP implementation, provider/live proof,
workspace runtime mutation, raw package import, checker implementation, or
readiness claims become necessary. None became necessary in this tranche.

## Operator Checkpoint

Operator asked Codex to proceed to the next foundation tranche. No additional
authorization was given for public-sync, MCP implementation, provider/live
calls, workspace runtime mutation, raw package import, production readiness,
release readiness, public readiness, external-facing readiness, or checker
implementation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | EARC-T3 row and closure note | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | BLOCKED with reason: no external review output was processed in this tranche | no path changed | BLOCKED with reason |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit | N/A with reason |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance workflow tranche. Public-facing versions require
separate public-sync authorization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 EARC-T3 external finding absorption workflow |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | EARC-T3 GC-018; work order; external-agent review workflow/reference updates; EARC roadmap; GC-051 registry entry and aggregate; completion |
| Allowed scope source | EARC roadmap `## T3 Target Shape` and operator request to proceed |
| Before status evidence | base `3f0cebf1`; clean worktree |
| After status evidence | EARC-T3 material closure pending commit |
| Diff evidence | `git diff --name-status 3f0cebf1..HEAD` |
| Approval boundary | bounded reference/workflow foundation only |
| Claim boundary | no public-sync, MCP implementation, provider/live call, workspace runtime mutation, raw package import, checker implementation, readiness claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `earc-t3-external-finding-absorption-workflow-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_FOR_CODEX_2026-06-18.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3-external-finding-absorption-workflow.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_COMPLETION_2026-06-18.md` |
| Actual changed set | `docs/baselines/CVF_GC018_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_FOR_CODEX_2026-06-18.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3-external-finding-absorption-workflow.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_COMPLETION_2026-06-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order closes a reference/workflow tranche only. It does not implement
runtime behavior, add a checker, or publish public-facing material.
