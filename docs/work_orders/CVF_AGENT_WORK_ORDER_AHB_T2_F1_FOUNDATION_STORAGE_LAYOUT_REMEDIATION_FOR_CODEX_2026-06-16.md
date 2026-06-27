# CVF Agent Work Order - AHB-T2-F1 Foundation Storage Layout Remediation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Batch ID: AHB-T2-F1

## Dispatch Prompt Envelope

Worker prompt: Codex must execute the AHB-T2-F1 foundation storage/layout
remediation. Create the stable storage/index standard and folder front door,
update the operational index and AHB roadmap, close with evidence, and keep all
work documentation-only. Do not implement checkers, move historical files, touch
runtime/source/test/provider/public-sync paths, or open AHB-T3.

## Purpose

Promote the AHB-T2-F1 folder/index finding into governed CVF foundation
artifacts so future agents treat storage layout as part of governance refactor
work, not optional cleanup or provider-local memory.

## Scope / Target / Owner Boundary

Target: AHB-T2-F1 foundation storage/index remediation.

Owner boundary: Codex owns implementation, review, commit, and closure in this
single-agent/multi-role batch.

Commit mode: `WORKER_MAY_COMMIT`

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Author | Codex | Create standard, folder front door, index update, roadmap update |
| Reviewer | Codex | Run governance gates and close with bounded evidence |
| Operator | Human operator | Redirect only if scope would exceed this work order |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | Source AHB-T2-F1 finding |
| `docs/reference/work_order_template/README.md` | Stable local-view folder precedent |
| `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md` | Stable filename precedent |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-16 "tiep tuc nhu da ban" | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md` | CLOSURE_SATISFIED |
| AHB-T2 completion | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | PREDECESSOR_SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AHB-T2-F1 finding exists | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | Foundation Folder/Index Governance Finding | AHB-T2-F1 | AHB-T2 completion review | ACCEPT |
| Work-order template folder precedent exists | `docs/reference/work_order_template/README.md` | Purpose; Foundation File Naming Rule | `docs/reference/work_order_template/README.md` | work-order template family index | ACCEPT |
| CCLV-T1A adopted stable filenames for long-lived addenda | `docs/baselines/CVF_GC018_CCLV_T1A_WORK_ORDER_TEMPLATE_POINTER_REFACTOR_2026-06-16.md` | Operator Foundation Rule Addition | stable filenames without date suffixes | CCLV-T1A baseline | ACCEPT |
| Operational reference index exists | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Lookup Table | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | operational lookup front door | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or finding requirement | Work-order instruction | Final artifact or evidence | Disposition |
|---|---|---|---|
| AHB-T2-F1 must not remain memory-only | create stable standard and folder front door | `docs/reference/foundation_storage/` | PASS |
| Future agents need scanable context | update operational index | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | PASS |
| AHB-T3 must stay parked | update AHB roadmap without dispatching AHB-T3 | AHB roadmap note | PASS |

## Allowed Scope

- Create `docs/reference/foundation_storage/README.md`.
- Create `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`.
- Update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`.
- Update `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`.
- Create the GC-018 baseline, this work order, and completion review.
- Run governance gates and commit the material closure.

## Pre-Flight Checks

Required before closure claim:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 073407d3 --head HEAD --enforce
git diff --check
```

## Forbidden Scope

- No runtime/source/test/checker implementation.
- No historical file move, archive cleanup, or mass rename.
- No interlock registry edit.
- No public-sync or public catalog claim.
- No provider/API/live proof.
- No AHB-T3 dispatch, checker wiring, or agent-interaction workspace build.

## Write Ownership

| Path | Ownership |
|---|---|
| `docs/reference/foundation_storage/` | Codex may create stable folder and standard |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Codex may add one lookup row |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | Codex may add AHB-T2-F1 closure row/note |
| `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md` | Codex owns this baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_FOR_CODEX_2026-06-16.md` | Codex owns this work order |
| `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` | Codex owns closure |

## Execution Plan

1. Create the stable foundation storage folder front door.
2. Create the stable foundation storage/index standard.
3. Add one operational-index lookup row.
4. Add AHB-T2-F1 row and closure note to the AHB roadmap.
5. Run focused gates, then pre-closure autorun.
6. Commit material closure and perform session sync if next move changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/foundation_storage/README.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` |
| Storage class | Central foundation standard plus local folder front door |
| Index/front door | `docs/reference/foundation_storage/README.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` |
| Date policy | stable-path for durable standard and folder README; dated-path for GC-018, work order, roadmap, and completion evidence |
| Archive disposition | N/A with reason: no historical file movement authorized |
| Deferred layout work | checker implementation remains a future candidate |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Stable folder front door exists. |
| AC2 | Stable storage/index standard exists. |
| AC3 | Operational reference index routes foundation storage/layout work to the new folder. |
| AC4 | AHB roadmap records AHB-T2-F1 closure and keeps AHB-T3 future-only. |
| AC5 | Completion includes finding-to-governance disposition and machine-check candidate. |
| AC6 | AOT manifest matches the changed set. |
| AC7 | Pre-closure autorun gate passes on the material range. |

## Evidence Requirements

Evidence must include:

- changed set from `git diff --name-status 073407d3..HEAD`;
- focused structural, AOT, learning, and machine-closure checks;
- pre-closure autorun result;
- diff hygiene result;
- completion review with Machine Closure Package.

## Review Gate

Codex must reject or repair the batch before commit if any required gate fails
inside allowed scope. Operator escalation is required only if the repair would
move historical files, implement a checker, alter runtime/source/test behavior,
or open public-sync.

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this work order authorizes governed
markdown only. It does not edit runtime/source/test/checker/interlock/provider
or public-sync files.

## Closure Checklist

- [x] Stable folder front door created.
- [x] Stable standard created.
- [x] Operational index updated.
- [x] AHB roadmap updated.
- [x] Completion review authored.
- [x] Machine Closure Package present.
- [x] Forbidden scope untouched.

## Return-To-Orchestrator Conditions

Return status is `CLOSED_PASS_BOUNDED` after all acceptance criteria pass and the
material closure is committed. Return `BLOCKED` only if a required source
artifact is missing or a gate failure requires forbidden-scope remediation.

## Operator Checkpoint

No operator checkpoint is required unless remediation would require historical
file movement, checker implementation, public-sync, runtime/source/test edits,
or AHB-T3 dispatch.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_FOR_CODEX_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Foundation standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | `Status: ACTIVE_STANDARD` | PASS |
| Folder front door | `docs/reference/foundation_storage/README.md` | `Status: ACTIVE_INDEX` | PASS |
| Operational index | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | lookup row added | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T2-F1 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry edit authorized for AHB-T2-F1 documentation-only remediation | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for AHB-T2-F1 documentation-only remediation | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: AHB-T2-F1 does not edit the registry | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Verification Commands

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 073407d3 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 073407d3 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 073407d3 --head HEAD
git diff --check
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance work order. No public-sync batch is
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

This work order closes AHB-T2-F1 as bounded documentation-only governance
remediation. It does not implement a checker, move historical files, run live
proof, public-sync, or claim production/public readiness.
