# CVF Agent Work Order - EARC-T3A External Return Absorption Pilot

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: work_order

## Dispatch Prompt Envelope

Prompt to worker:

Read the EARC-T3 absorption workflow, the workspace-layer absorption map, and
the copied workspace-layer package references first. Run one bounded absorption
pilot using the package as external advisory input. Produce a dated absorption
review packet with the Required Absorption Table, update the existing
absorption map only with CVF-owned conclusions, update roadmap and GC-051
coverage, and decide whether a future checker tranche is now ready. Do not
import raw package files, implement MCP/workspace runtime, run providers,
public-sync, mutate workspace runtime state, add the checker, or claim
readiness.

## Purpose

Close EARC-T3A as the first real external-return absorption pilot after
EARC-T3.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active next move | `CVF_SESSION/state/entries/nextAllowedMove.json` | ACCEPT |
| EARC roadmap | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md` | ACCEPT |
| EARC-T3 workflow | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | ACCEPT |
| Workspace package absorption map | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | ACCEPT |
| Root lifecycle registry | `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | ACCEPT |

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
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
- `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`
- `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md`

## Pre-Flight Checks

| Check | Result |
|---|---|
| Startup state resolved | PASS |
| External package remains frozen internal reference | PASS |
| EARC-T3 required absorption table identified | PASS |
| Scope excludes public-sync, MCP/runtime, provider/live, raw package import, checker implementation, and readiness claims | PASS |
| Dispatch prompt envelope appears first | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | Codex dispatcher/worker/reviewer/closer/session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| dispatchBaseHead | `0f6d54e8` |
| executionBaseHead | `0f6d54e8` |
| closureBaseHead | `0f6d54e8` |
| baseHeadFor(phase) | `0f6d54e8` for material; material commit for later session-sync |
| changedSetScope(phase) | EARC-T3A GC-018, work order, absorption review packet, workspace absorption map, EARC roadmap, GC-051 registry entry, aggregate |
| traceScope(phase, actor) | exact material manifest in this work order and absorption review packet |
| commitOwner(phase) | Codex |
| crossBatchIsolation | clean worktree before EARC-T3A; no public-sync, MCP/runtime/provider/raw-package/checker implementation work |
| nextMoveSurfaces | session-sync after material commit if next allowed move changes |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` |
| Storage class | existing stable local-view absorption map under `docs/reference/agent_workspace/` |
| Index/front door | `docs/reference/agent_workspace/README.md`; existing map remains indexed through agent workspace local view |
| Date policy | stable absorption map updated in place; dated GC-018/work order/review for execution evidence |
| Archive disposition | N/A with reason: no superseded active file in this batch |
| Deferred layout work | N/A with reason: this pilot updates the existing indexed map only |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | absorption pilot only; no workspace build |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | stable absorption-map update plus dated review evidence |
| Handoff fields | inherited from Agent Handoff Contract Control Block |
| State ownership | N/A with reason: no workspace state, queue, inbox, dashboard, or runtime item is created |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | workspace runtime queues, workspace UI, runtime source, provider proof, public-sync, executable workspace behavior, raw package import, and product-runtime registry edits are forbidden; the only registry edits allowed are GC-051 coverage entries listed in the material manifest |

## Source Verification

Source verification is recorded in:

`docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md`

## Execution Plan

1. Classify selected package claims through the EARC-T3 required absorption
   table.
2. Author the dated absorption review packet.
3. Update the existing workspace package absorption map with pilot results.
4. Update the EARC roadmap and GC-051 registry coverage.
5. Run gates and commit material.
6. Sync session continuity if next-move surfaces change.

## Write Ownership

Codex owns the bounded material commit and later session-sync commit. The raw
external package, public-sync clone, runtime source, provider keys, MCP
implementation, checker implementation, and workspace runtime state are not
owned by this work order.

## Evidence Requirements

| Evidence | Required |
|---|---|
| Required Absorption Table | present in the absorption review packet |
| CVF-owned source verification | GC-018 source verification table |
| Absorption map update | existing stable map updated with pilot result |
| Registry coverage | GC-051 source entry plus generated aggregate |
| Closure gates | worker-return fast gate, commit steward preflight, pre-closure, pre-push/session-sync as applicable |

## Review Gate

Codex reviewer must confirm that the pilot consumes external package material
as advisory input only, preserves CVF as authority, and does not make runtime
or readiness claims.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| EARC-T3A-AC1 | Dated absorption review packet exists and includes the Required Absorption Table. |
| EARC-T3A-AC2 | External package items are split into atomic observations with CVF dispositions. |
| EARC-T3A-AC3 | Existing absorption map records the pilot outcome. |
| EARC-T3A-AC4 | Future checker readiness is decided without implementing the checker. |
| EARC-T3A-AC5 | No public-sync, MCP implementation, provider call, workspace runtime mutation, raw package import, checker implementation, or readiness claim is introduced. |

## Closure Checklist

- [x] GC-018 source verification authored.
- [x] Absorption review packet authored.
- [x] Workspace-layer absorption map updated.
- [x] Roadmap tranche state updated.
- [x] GC-051 entry added and aggregate regenerated.
- [x] Checker follow-up decision recorded.

## Return-To-Orchestrator Conditions

Return to operator only if public-sync, MCP implementation, provider/live proof,
workspace runtime mutation, raw package import, checker implementation, or
readiness claims become necessary. None became necessary in this tranche.

## Operator Checkpoint

Operator explicitly agreed to EARC-T3A and directed Codex to perform the
absorption. No authorization was given for public-sync, MCP implementation,
provider/live calls, workspace runtime mutation, raw package import, production
readiness, release readiness, public readiness, external-facing readiness, or
checker implementation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Primary absorption review | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | EARC-T3A row and closure note | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | Required Absorption Table plus External Artifact Hash Manifest; representative sha256 `a267edd4f9702daa1047034520f3e24b0c7321b17d1451a858b12a2845b7cd82` | PASS |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit | N/A with reason |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance absorption pilot. Public-facing versions require
separate public-sync authorization.

## External Artifact Hash Manifest

| External artifact | sha256 |
|---|---|
| workspace-layer package README | `a267edd4f9702daa1047034520f3e24b0c7321b17d1451a858b12a2845b7cd82` |
| workspace-layer package MCP API document | `b3897e04801b6fdadf70c0ca46be579e3e64149eef40b74778fb4942d6cff3d7` |
| workspace-layer package MCP contract | `545ca7842f447c5de5f17ca0788e05b29748770bb450d808a9bd6e30b4297e93` |
| workspace-layer package state projection contract | `52b458d57fc443cf579196db5517811718bdf84e2ad6b84896c92cbc1e182956` |
| workspace-layer package workflow schema | `4b74d469effcafe1d0cc2993e4479f4f9431cda3c62963084df860f07cb8a9b5` |
| workspace-layer package smoke-result JSON | `1900be01745d5568c4040108938fc8b79a0b7eb6248a4805253578eecb41de6f` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 EARC-T3A external return absorption pilot |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | EARC-T3A GC-018; work order; absorption review packet; completion review; workspace-layer absorption map; EARC roadmap; GC-051 registry entry and aggregate |
| Allowed scope source | operator authorization after EARC-T3 closure and GC-018 |
| Before status evidence | base `0f6d54e8`; clean worktree |
| After status evidence | EARC-T3A material closure pending commit |
| Diff evidence | `git diff --name-status 0f6d54e8..HEAD` |
| Approval boundary | bounded reference absorption pilot only |
| Claim boundary | no public-sync, MCP implementation, provider/live call, workspace runtime mutation, raw package import, checker implementation, readiness claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `earc-t3a-external-return-absorption-pilot-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_FOR_CODEX_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_COMPLETION_2026-06-18.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3a-external-return-absorption-pilot.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_FOR_CODEX_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_COMPLETION_2026-06-18.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3a-external-return-absorption-pilot.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order closes a reference absorption pilot only. It does not implement
runtime behavior, add a checker, import raw package files, or publish
public-facing material.
