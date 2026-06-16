# CVF GC-018 Authorization Baseline - AHB-T2-F1 Foundation Storage Layout Remediation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-16

Batch ID: AHB-T2-F1

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt to worker: execute the AHB-T2-F1 documentation-only foundation
storage/layout remediation. Promote the folder/index rule from AHB-T2-F1 into a
stable CVF-governed artifact, add a folder front door, update the operational
index, update the AHB roadmap, and close with bounded evidence. Do not implement
checkers, move historical files, public-sync, edit runtime/source/test files, or
claim production/public readiness.

## Purpose

Authorize a bounded remediation for AHB-T2-F1: foundation and governance
refactor work must include stable folder/index/storage layout review so future
agents can retrieve long-lived CVF rules from governed artifacts instead of
provider memory or dated one-off packets.

## Scope / Target / Owner Boundary

Target: foundation storage/index governance rule and front door.

Owner boundary: Codex owns this documentation-only implementation and closure.
No worker delegation is required. The batch may create a stable reference folder
and standard, update the operational index, update the AHB roadmap, and author a
completion review.

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-16 "tiep tuc nhu da ban" after AHB-T2 closure | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | AHB-T2-F1 remediation next |
| AHB-T2 completion | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | PREDECESSOR_SATISFIED |
| Work-order template folder precedent | `docs/reference/work_order_template/README.md` | SOURCE_INPUT |
| CCLV-T1A baseline | `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md` | SOURCE_INPUT |

## Source / Predecessor Evidence

| Source | Path | Role |
|---|---|---|
| AHB-T2-F1 finding | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | Root finding requiring promotion |
| Work-order template family index | `docs/reference/work_order_template/README.md` | Stable folder/index precedent |
| CCLV-T1A authorization | `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md` | Stable filename precedent |
| Operational reference index | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Cross-CVF lookup front door |

## Decision / Baseline / Proposed Tranche

Decision: close AHB-T2-F1 as a bounded documentation-control remediation.

Baseline: before this batch, the work-order template family had a stable local
folder, but CVF lacked a central foundation storage/index standard for all
durable governance refactor work.

Proposed tranche: create the central stable folder and standard, update the
operational reference index, record closure on the AHB roadmap, and leave
machine enforcement as a future candidate.

## Problem Statement

AHB-T2-F1 recorded that the stable folder/index rule was partially implemented
for `docs/reference/work_order_template/`, but not promoted as a general
cross-CVF foundation rule. That leaves future foundation refactors vulnerable to
date-sprawled durable files, missing folder front doors, and agent retrieval gaps.

## Authorized Changed Set

| Path | Action | Reason |
|---|---|---|
| `docs/reference/foundation_storage/README.md` | CREATE | stable folder front door for foundation storage/index rules |
| `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | CREATE | central standard for foundation file storage/index discipline |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | MODIFY | add operational lookup row for foundation storage/layout work |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | MODIFY | record AHB-T2-F1 closure and keep AHB-T3 candidate bounded |
| `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md` | CREATE | this authorization baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_FOR_CODEX_2026-06-16.md` | CREATE | Codex-owned work order and closure contract |
| `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` | CREATE | closure evidence |

## Forbidden Scope

- Do not move or archive historical files in this batch.
- Do not implement or wire a checker.
- Do not edit runtime, source, tests, interlock registry, provider config, or
  public-sync files.
- Do not open AHB-T3, build the agent-interaction workspace, or claim
  production/public readiness.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | A stable folder front door exists under `docs/reference/foundation_storage/README.md`. |
| AC2 | A central foundation storage/index standard exists under a stable path without a date suffix. |
| AC3 | The operational reference index points future agents to the new folder when foundation storage/layout is in scope. |
| AC4 | The AHB roadmap records AHB-T2-F1 closure and keeps AHB-T3 as future candidate only. |
| AC5 | Completion records the finding-to-governance disposition and future machine-check candidate. |
| AC6 | Changed set stays inside the authorized governed markdown scope. |
| AC7 | Pre-closure autorun gate passes on the material range before closure claim. |

## Evidence / Verification

Required commands:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 073407d3 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 073407d3 --head HEAD
git diff --check
```

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/foundation_storage/README.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` |
| Storage class | Central foundation standard plus local folder front door |
| Index/front door | `docs/reference/foundation_storage/README.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` |
| Date policy | stable-path for durable standard and folder README; dated paths retained for GC-018, work order, roadmap, and completion evidence |
| Archive disposition | N/A with reason: no historical file movement authorized |
| Deferred layout work | Machine-check implementation candidate only; no checker in this batch |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 AHB-T2-F1 foundation storage remediation |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `docs/reference/foundation_storage/README.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` |
| Allowed scope source | AHB-T2-F1 finding in `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` |
| Before status evidence | HEAD `073407d3`; worktree clean |
| After status evidence | AHB-T2-F1 material closure pending commit |
| Diff evidence | `git diff --name-status 073407d3..HEAD` |
| Approval boundary | documentation-only foundation storage/index remediation |
| Claim boundary | no runtime/provider/live/public/registry/checker implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-t2-f1-foundation-storage-layout-remediation-2026-06-16` |
| Expected manifest | `docs/reference/foundation_storage/README.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` |
| Actual changed set | `docs/reference/foundation_storage/README.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes and closes documentation-only foundation storage/index
remediation. It does not implement a checker, move historical files, run live
proof, public-sync, or claim production/public readiness.
