# CVF Agent Work Order - AHB-T2-F2 Foundation Storage And Memory Learning Enforcement

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Batch ID: AHB-T2-F2

executionBaseHead: 46abc24e

## Dispatch Prompt Envelope

Worker prompt: Codex must close the mandatory enforcement gap found after
AHB-T2-F1. Verify whether foundation storage/layout and provider-memory-only
learning are guarded. If not, add bounded machine enforcement, focused tests,
active canonical standard routing, closure evidence, and session continuity.
Do not open AHB-T3, implement handoff-boundary unification, touch runtime
product code, run provider/live proof, or public-sync.

## Purpose

Convert two governance requirements from artifact-only or partially guarded
state into enforceable CVF controls:

- foundation refactors must include stable folder/index storage discipline;
- reusable lessons must not remain only in provider-specific memory.

## Scope / Target / Owner Boundary

Target: checker and reference-surface hardening.

Owner boundary: Codex owns implementation, review, commit, and closure in this
single-agent/multi-role batch.

Commit mode: `WORKER_MAY_COMMIT`

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Author | Codex | Add checker, active standard, tests, hook bindings, roadmap closure |
| Reviewer | Codex | Run focused gates and close with bounded evidence |
| Operator | Human operator | Redirect only if scope would exceed this work order |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Foundation storage rule to enforce |
| `governance/compat/check_finding_to_governance_learning.py` | Existing provider-memory-only learning guard |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-16 enforcement is mandatory before continuing | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_2026-06-16.md` | CLOSURE_SATISFIED |
| AHB-T2-F1 completion | `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` | PREDECESSOR_SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Foundation storage standard currently records machine-check candidate | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Machine Check Candidate | `Foundation Storage Layout Block` | foundation storage standard | ACCEPT |
| Provider-memory-only learning escape checker exists | `governance/compat/check_finding_to_governance_learning.py` | PROVIDER_MEMORY_ONLY_SIGNALS; provider_memory_only_learning_escape | `provider_memory_only_learning_escape` | finding-to-governance checker | ACCEPT |
| Autorun gate can host new checker | `governance/compat/run_agent_autorun_workflow_gate.py` | common commands | `_common_commands` | autorun workflow gate | ACCEPT |
| Local hook chain can host new checker | `governance/compat/run_local_governance_hook_chain.py` | hook check lists | `HOOK_CHAINS` | local hook chain | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or finding requirement | Work-order instruction | Final artifact or evidence | Disposition |
|---|---|---|---|
| AHB-T2-F1 checker gap must not stay artifact-only | add foundation storage checker | `check_foundation_storage_layout.py` | PASS |
| Provider-memory-only lessons must not remain local-only | verify existing guard and active standard | F2G checker plus active standard path | PASS |
| Future agents must hit the guard early | bind checker into autorun and hooks | autorun and local hook chain edits | PASS |
| AHB-T3 remains parked | update AHB roadmap only | AHB-T2-F2 closed; AHB-T3 candidate | PASS |

## Allowed Scope

- Add `governance/compat/check_foundation_storage_layout.py`.
- Add `governance/compat/test_check_foundation_storage_layout.py`.
- Update `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`.
- Add active stable `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`.
- Update `governance/compat/check_finding_to_governance_learning.py` to use the stable standard path.
- Update `AGENTS.md` to point future agents at the stable standard path.
- Update autorun and local hook chain bindings.
- Update AHB roadmap, GC-018, this work order, and completion review.
- Run focused tests and governance gates.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Storage class | Central foundation standards plus roadmap closure evidence |
| Index/front door | `docs/reference/foundation_storage/README.md`; `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`; AHB roadmap |
| Date policy | Stable-path retained for foundation-storage standard; dated active F2G standard restored because AGENTS/checker already name that canonical path |
| Archive disposition | N/A with reason: no historical file movement authorized |
| Deferred layout work | N/A with reason: checker and hook binding implemented in this batch |

## Pre-Flight Checks

Required before closure claim:

```powershell
pytest governance/compat/test_check_foundation_storage_layout.py governance/compat/test_check_finding_to_governance_learning.py -q
python governance/compat/check_foundation_storage_layout.py --base 46abc24e --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 46abc24e --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 46abc24e --head HEAD
git diff --check
```

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this work order authorizes governance
checker and governed markdown changes only. It does not edit CVF product
runtime routes, provider adapters, model registries, hardcoded provider
selection, or live-governance behavior. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
and `PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and bind a bounded foundation
storage/layout checker, with tests, so foundation refactor work orders and
stable `docs/reference/<family>/` folders are machine-checked.

Protected paths:

- `governance/compat/check_foundation_storage_layout.py`
- `governance/compat/test_check_foundation_storage_layout.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `AGENTS.md`

Operator authorization: operator stated this enforcement is mandatory before
continuing.

Rollback boundary: revert only the AHB-T2-F2 checker, tests, hook bindings, and
matching docs if this batch fails; do not alter unrelated guards, runtime, or
AHB-T3.

## Execution Plan

1. Inspect the current F2G and foundation storage controls.
2. Add the foundation storage/layout checker.
3. Add focused checker tests.
4. Restore the active F2G standard path and update foundation storage standard
   machine-enforcement status.
5. Bind the checker into autorun and local hook chains.
6. Update AHB roadmap and closure artifacts.
7. Run focused tests, focused gates, pre-closure autorun, and diff hygiene.

## Forbidden Scope

- No AHB-T3 unified handoff-boundary checker implementation.
- No runtime/product source mutation.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No historical file movement or archive cleanup.
- No agent-interaction workspace build.

## Write Ownership

| Path | Ownership |
|---|---|
| `governance/compat/check_foundation_storage_layout.py` | Codex may add checker |
| `governance/compat/test_check_foundation_storage_layout.py` | Codex may add focused tests |
| `governance/compat/check_finding_to_governance_learning.py` | Codex may update standard path constant only |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Codex may add checker binding |
| `governance/compat/run_local_governance_hook_chain.py` | Codex may add checker binding |
| `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Codex may update machine-enforcement status |
| `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Codex may restore active canonical standard |
| `AGENTS.md` | Codex may update the F2G standard pointer only |
| AHB-T2-F2 baseline, work order, completion, and AHB roadmap | Codex owns closure evidence |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Foundation storage/layout checker exists. |
| AC2 | Checker catches missing stable folder README and missing work-order storage block. |
| AC3 | Checker is bound into autorun and local hooks. |
| AC4 | Finding-To-Governance active standard path exists and documents provider-memory-only boundary. |
| AC5 | Focused tests pass. |
| AC6 | Pre-closure autorun gate passes. |
| AC7 | AHB-T3 remains candidate-only. |

## Evidence Requirements

Evidence must include:

- focused pytest output for the foundation storage and F2G checker suites;
- foundation storage checker output on `46abc24e..HEAD`;
- F2G checker output on `46abc24e..HEAD`;
- markdown structural, AOT, machine closure, and pre-closure autorun results;
- `git diff --check`;
- committed changed-set evidence.

## Review Gate

Codex must reject or repair the batch before commit if any required gate fails
inside allowed scope. Operator escalation is required only if remediation would
open AHB-T3, move historical files, touch runtime/product source, public-sync,
or run provider/live proof.

## Closure Checklist

- [x] Foundation storage checker added.
- [x] Foundation storage checker tests added.
- [x] F2G active standard restored.
- [x] Foundation storage standard updated to machine-enforced.
- [x] Autorun and local hook chains updated.
- [x] AHB roadmap updated.
- [x] Completion review authored.
- [x] AHB-T3 remains candidate-only.

## Return-To-Orchestrator Conditions

Return status is `CLOSED_PASS_BOUNDED` after all acceptance criteria pass and
the material closure is committed. Return `BLOCKED` only if a required source
artifact is missing or a gate failure requires forbidden-scope remediation.

## Operator Checkpoint

No operator checkpoint is required unless remediation would require AHB-T3
dispatch, runtime/source edits, public-sync, provider/live proof, interlock
registry edits, or historical archive movement.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_FOR_CODEX_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Foundation checker | `governance/compat/check_foundation_storage_layout.py` | file exists and gate passes | PASS |
| Foundation checker tests | `governance/compat/test_check_foundation_storage_layout.py` | focused pytest passes | PASS |
| F2G active standard | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | file exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T2-F2 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry edit authorized for AHB-T2-F2 governance-control enforcement | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry edit authorized for AHB-T2-F2 governance-control enforcement | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED`; `STANDARD_UPDATED`; `RULE_EXISTS` |
| Next control action | Run pre-closure and session sync, then keep AHB-T3 gated behind fresh GC-018 |
| Worker blame | `N/A_WITH_REASON`: this was a control-plane enforcement gap, not individual worker blame |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance enforcement. No public-sync batch is
authorized.

## Claim Boundary

This work order closes only AHB-T2-F2 enforcement hardening. It does not
implement AHB-T3, alter runtime behavior, run live proof, public-sync, or claim
production/public readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 AHB-T2-F2 enforcement hardening |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_2026-06-16.md`; `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_FOR_CODEX_2026-06-16.md`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_check_foundation_storage_layout.py` |
| Allowed scope source | operator instruction that enforcement is mandatory before continuing |
| Before status evidence | HEAD `46abc24e`; worktree clean |
| After status evidence | AHB-T2-F2 material closure pending commit |
| Diff evidence | `git diff --name-status 46abc24e..HEAD` |
| Approval boundary | bounded governance-control enforcement hardening |
| Claim boundary | no runtime/provider/live/public/AHB-T3 implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-t2-f2-foundation-storage-memory-learning-enforcement-2026-06-16` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_2026-06-16.md`; `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_FOR_CODEX_2026-06-16.md`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_check_foundation_storage_layout.py` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_2026-06-16.md`; `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`; `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md`; `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_FOR_CODEX_2026-06-16.md`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_check_foundation_storage_layout.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
