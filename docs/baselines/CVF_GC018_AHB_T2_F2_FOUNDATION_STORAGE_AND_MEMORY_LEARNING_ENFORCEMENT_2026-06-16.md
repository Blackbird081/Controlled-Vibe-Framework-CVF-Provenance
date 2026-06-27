# CVF GC-018 - AHB-T2-F2 Foundation Storage And Memory Learning Enforcement

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-16

Batch ID: AHB-T2-F2

executionBaseHead: 46abc24e

## Purpose

Authorize and close the bounded enforcement hardening needed before AHB-T3:
foundation storage/layout must be machine-checked, and provider-memory-only
reusable lessons must remain tied to an active canonical Finding-To-Governance
standard.

## Scope / Target / Owner Boundary

Target: governance-control enforcement only.

Owner boundary: Codex-owned checker/template governance hardening. No AHB-T3
dispatch, runtime/source product mutation, provider/live proof, public-sync,
interlock registry edit, historical archive movement, or workspace build is
authorized.

## Source Authority

| Source | Path | Role |
|---|---|---|
| AHB-T2-F1 standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Required storage/index rule and prior machine-check candidate |
| AHB-T2-F1 completion | `docs/reviews/CVF_AHB_T2_F1_FOUNDATION_STORAGE_LAYOUT_REMEDIATION_COMPLETION_2026-06-16.md` | Recorded checker gap as bounded risk |
| Finding-To-Governance guard | `governance/compat/check_finding_to_governance_learning.py` | Existing machine guard for provider-memory-only learning escape |
| AGENTS.md authority boundary | `AGENTS.md` | Canonical CVF instruction that provider-local memory is not CVF authority |

## Decision

Proceed with a small enforcement batch:

- add `governance/compat/check_foundation_storage_layout.py`;
- add focused tests;
- bind the checker into autorun and local hook chains;
- update the foundation storage standard from candidate to machine-enforced;
- restore the Finding-To-Governance standard at its active canonical path.

## Closure Criteria

| Criterion | Evidence |
|---|---|
| Foundation storage/layout has a checker | `governance/compat/check_foundation_storage_layout.py` |
| Checker has regression tests | `governance/compat/test_check_foundation_storage_layout.py` |
| Checker is in autorun and local hook chains | `run_agent_autorun_workflow_gate.py`; `run_local_governance_hook_chain.py` |
| Provider-memory-only learning guard remains active | `check_finding_to_governance_learning.py` and active standard path |
| AHB-T3 remains parked | AHB roadmap records AHB-T2-F2 closure only |

## Evidence / Verification

Required evidence before closure:

```powershell
pytest governance/compat/test_check_foundation_storage_layout.py governance/compat/test_check_finding_to_governance_learning.py -q
python governance/compat/check_foundation_storage_layout.py --base 46abc24e --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 46abc24e --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 46abc24e --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 46abc24e --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 46abc24e --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 46abc24e --head HEAD
git diff --check
```

## Claim Boundary

This baseline authorizes only governance-control enforcement hardening. It does
not claim handoff-boundary unification, AHB-T3 checker implementation, runtime
governance behavior, live proof, public readiness, or public export.

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
