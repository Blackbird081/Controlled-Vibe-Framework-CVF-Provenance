# CVF Agent Work Order - CCG-1 Corpus Completeness And Report Integrity Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-01

## Purpose

Implement the general corpus-completeness and report-integrity guard authorized
by the operator and CCG-1 GC-018 packet.

## Scope / Target / Owner Boundary

Allowed scope:

- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `governance/toolkit/05_OPERATION/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD.md`
- `governance/compat/check_corpus_completeness_report_integrity.py`
- `governance/compat/test_check_corpus_completeness_report_integrity.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `.github/workflows/documentation-testing.yml`
- `AGENTS.md`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `CLAUDE.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `CVF_SESSION_MEMORY.md`
- `README.md`
- `docs/CVF_CORE_KNOWLEDGE_BASE.md`
- `docs/INDEX.md`
- `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- `docs/baselines/CVF_GC018_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_2026-06-01.md`
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `docs/reference/README.md`
- `docs/roadmaps/CVF_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_ROADMAP_2026-06-01.md`
- `docs/work_orders/CVF_WO_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_2026-06-01.md`
- `docs/reviews/CVF_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_COMPLETION_2026-06-01.md`
- `governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`

Forbidden scope:

- legacy concept absorption or implementation;
- runtime provider, prompt, route, receipt, memory, or Learning Plane changes;
- public-sync changes;
- destructive operations.

Risk ceiling: R1 repository governance hardening.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 explicit request to implement the generalized guard | ACCEPT |
| CCG-1 roadmap | `docs/roadmaps/CVF_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_ROADMAP_2026-06-01.md` | ACCEPT |
| Fresh CCG-1 GC-018 | `docs/baselines/CVF_GC018_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_2026-06-01.md` | ACCEPT |
| Legacy failure evidence | `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Convert operator instruction into bounded guard tranche | No Legacy absorption |
| Implementer | Add checker, tests, wiring, and docs corrections | Allowed files only |
| Reviewer | Run machine gates and reject paper-only enforcement claims | No public/runtime expansion |

## Required First Reads

- `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `.github/workflows/documentation-testing.yml`

## Pre-Flight Checks

Captured batch base:

```text
baseHead=fe29b4d6
```

Commands:

```powershell
git rev-parse --short HEAD
python governance/compat/check_active_session_state.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fe29b4d6 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base fe29b4d6 --head HEAD
```

The pre-existing handoff HEAD drift from `fe29b4d6` is an allowed continuity
remediation item in this batch. Repair and rerun instead of asking the operator.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Autorun bundle function exists | `EXISTS` | `governance/compat/run_agent_autorun_workflow_gate.py` | autorun source | `_common_commands` | Autorun wrapper | ACCEPT |
| Local hook map exists | `EXISTS` | `governance/compat/run_local_governance_hook_chain.py` | hook source | `HOOK_CHAINS` | Local hook chain | ACCEPT |
| Documentation CI workflow exists | `EXISTS` | `.github/workflows/documentation-testing.yml` | workflow source | `knowledge-absorption-priority-guard` | Documentation workflow | ACCEPT |
| Specialized filesystem listing rule exists | `EXISTS` | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Gate 1 sub-rule | `FILESYSTEM_LISTING_REQUIRED` | Blind-spot standard | ACCEPT |
| Specialized completeness cross-check exists | `EXISTS` | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Gate 7 sub-rule | `COMPLETENESS_CROSS_CHECK` | Blind-spot standard | ACCEPT |

## New Doc-Only Fields

| Proposed field or symbol | Intended owner | Purpose | Source status |
| --- | --- | --- | --- |
| `Corpus Completeness And Report Integrity` | corpus-derived artifact | Evidence block header | DOC_ONLY_NEW |
| `COMPLETE_VERIFIED` | corpus verdict vocabulary | Zero-unresolved completion claim | DOC_ONLY_NEW |
| `check_corpus_completeness_report_integrity.py` | compat layer | Machine validator | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence required |
| --- | --- | --- |
| General corpus standard | Add reference standard and `GC-047` guard | File existence + guard authoring PASS |
| Machine enforcement | Implement checker and tests | Focused pytest PASS |
| Earliest applicable gate wiring | Update autorun, hooks, CI | Checker binding PASS |
| Agent routing | Update AGENTS, CLAUDE, GC-018 template | Marker scan PASS |
| Legacy audit correction | Recount and patch audit | Filesystem command evidence |
| Continuity repair | Update state/front door/handoff | Active-session gate PASS |

## Write Ownership

Only the allowed governance, documentation, checker, test, and continuity
surfaces may change. Archive cleanup and Legacy content edits are out of scope.

## Execution Plan

1. Add general standard and `GC-047` guard.
2. Add checker and focused tests.
3. Wire checker into autorun, local hooks, and documentation CI.
4. Update routing docs and the GC-018 template.
5. Correct the legacy audit count claim and record the governance-learning
   disposition.
6. Run focused and governance checks.
7. File completion review, commit implementation, sync handoff, and verify a
   clean worktree.

## Evidence Requirements

- `git diff --name-status fe29b4d6 HEAD`
- `python -m pytest governance/compat/test_check_corpus_completeness_report_integrity.py -q`
- `python governance/compat/check_corpus_completeness_report_integrity.py --base fe29b4d6 --head HEAD --enforce`
- `python governance/compat/check_guard_registry.py --enforce`
- `python governance/compat/check_guard_authoring_standard.py --base fe29b4d6 --head HEAD --enforce`
- `python governance/compat/check_governed_file_size.py --enforce`
- `python governance/compat/check_active_session_state.py --enforce`

## Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| Standard and `GC-047` exist | PASS |
| Checker rejects missing evidence blocks when an output asserts corpus completion | PASS |
| Checker rejects unresolved `COMPLETE_VERIFIED` claims | PASS |
| Checker accepts bounded partial verdicts | PASS |
| Checker is bound to autorun, hooks, and CI | PASS |
| Pointer and audit corrections are command-backed | PASS |
| Continuity is clean after sync | PASS |

## Review Gate

Reject closure if the checker is documentation-only, if hooks/CI/autorun omit
it, if audit counts remain mixed across file classes, or if the result claims
semantic understanding rather than evidence discipline.

## Closure Checklist

| Item | Resolution |
| --- | --- |
| Fresh GC-018 filed | PASS |
| Operator authorization captured | PASS |
| Source Verification Block completed | PASS |
| Checker and tests implemented | PASS |
| Hook, CI, autorun bindings verified | PASS |
| Audit and continuity remediation verified | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return if implementation requires runtime behavior changes, public-sync,
destructive operations, or Legacy concept absorption.

## Operator Checkpoint

SATISFIED. Operator explicitly authorized implementation on 2026-06-01.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening only. Public-sync is outside
this work order.

## Claim Boundary

This work order authorizes corpus-evidence governance hardening only. It does
not authorize Legacy concept implementation or prove perfect semantic
understanding.

## Closure Diff Gate

| Surface | Evidence | Resolution |
| --- | --- | --- |
| Allowed changed-file scope | `git diff --name-status fe29b4d6 f078fe91` | PASS |
| Standard, guard, checker, tests | committed implementation diff | PASS |
| Hook, CI, autorun bindings | corpus checker binding scan | PASS |
| Audit correction | filesystem recount evidence in Legacy audit | PASS |
| Continuity sync | active-session compatibility gate | PASS |

## Closure Decision

Decision: `CLOSED_PASS_BOUNDED`.

Completion review:

`docs/reviews/CVF_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_COMPLETION_2026-06-01.md`
