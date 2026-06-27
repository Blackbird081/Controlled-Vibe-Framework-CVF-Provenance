# CVF GC-018 Authorization Baseline - FPRC-T1 Finding Root Cause And Memory Escape Guard

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_DISPATCH

docType: baseline

Date: 2026-06-16

Batch ID: FPRC-T1

## Purpose

Authorize a bounded FPRC-T1 governance-foundation tranche. FPRC-T1 must define
root-cause grouping for finding propagation and add a provider-memory learning
escape control so reusable lessons cannot close only in provider-specific
memory.

## Decision / Baseline / Proposed Tranche

Decision: authorize FPRC-T1 as the immediate worker tranche before CCLV-T2
resumes.

Baseline: current finding-learning enforcement is owned by
`governance/compat/check_finding_to_governance_learning.py`; current authoring
guidance is owned by
`docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`.

Proposed tranche: add the FPRC standard, update the authoring addendum, extend
the finding-learning checker for provider-memory-only learning escape, and add
focused tests.

## Scope / Target / Owner Boundary

Allowed:

- add a governed FPRC reference standard;
- update the work-order authoring hardening addendum with FPRC authoring rules;
- update the finding-to-governance learning checker and focused tests for
  provider-memory-only lesson escape;
- author a completion review;
- update FPRC roadmap closure state if evidence passes.

Forbidden:

- hard global hook broadening beyond existing finding-to-governance checker
  surfaces;
- historical artifact migration;
- editing provider-specific memory files;
- runtime behavior changes outside `governance/compat`;
- public-sync, live proof, credential use, or legacy absorption.

Risk ceiling: R1 governance guard hardening.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPRC roadmap exists | `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` | Tranche Plan | `FPRC-T1` | FPRC roadmap | ACCEPT |
| Existing finding-learning checker owns learning disposition enforcement | `governance/compat/check_finding_to_governance_learning.py` | module constants and `_validate_finding_doc` | `_validate_finding_doc` | finding-to-governance checker | ACCEPT |
| Existing finding-learning test module exists | `governance/compat/test_check_finding_to_governance_learning.py` | test module | `test_valid_finding_doc_passes` | pytest test module | ACCEPT |
| Work-order authoring addendum exists | `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | Purpose / Scope | `CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | reference addendum | ACCEPT |
| CCLV-T2 is paused by operator override | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | CCLV-T2 Pause Record | `CCLV-T2` | CCLV roadmap | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Owner |
|---|---|---|
| `Root Cause To Propagated Findings` | Standard section/table for grouping one root defect and its symptoms | FPRC-T1 standard |
| `Provider Memory Learning Escape Guard` | Rule requiring governed learning disposition when a reusable lesson is recorded in provider-specific memory | FPRC-T1 standard |
| `Boundary-Prose Trigger Discipline` | Rule separating out-of-scope/N/A prose from positive evidence-class claims | FPRC-T1 standard |

## Current Runtime Freshness Verification

This tranche is a governance checker/documentation tranche. The only executable
owner in scope is `governance/compat/check_finding_to_governance_learning.py`.
Runtime product source, provider adapters, public-sync, live proof, and legacy
absorption are outside this authorization.

Verification commands:

```powershell
Test-Path governance/compat/check_finding_to_governance_learning.py
Test-Path governance/compat/test_check_finding_to_governance_learning.py
Test-Path docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md
```

## Legacy Absorption Coverage Index Disposition

Disposition: NOT_APPLICABLE_WITH_REASON

Reason: FPRC-T1 is a governance guard-hardening tranche based on current CVF
workflow findings. It does not absorb, scan, or classify legacy knowledge.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: FPRC-T1 may update the finding-to-governance
checker and its focused tests to catch provider-memory-only learning escape.

Protected paths:

- governance/compat/check_finding_to_governance_learning.py
- governance/compat/test_check_finding_to_governance_learning.py

Operator authorization: operator prioritized FPRC-T1 because CCLV-T2 could
repeat the two newly observed guard gaps.

Rollback boundary: if rejected, revert only FPRC-T1 guard/doc artifacts and the
FPRC/CCLV priority updates. Do not revert prior CCLV-T1, CCLV-T1A, CCLV-T2
dispatch, or session-sync commits.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | FPRC standard defines root finding, propagated symptom, evidence replication, stale sync, and reviewer repair side-effect roles. |
| AC2 | FPRC standard defines Provider Memory Learning Escape Guard. |
| AC3 | FPRC standard defines Boundary-Prose Trigger Discipline for N/A/out-of-scope prose. |
| AC4 | Work-order authoring addendum carries the new FPRC guidance. |
| AC5 | Finding-learning checker has focused coverage for provider-memory-only lesson escape. |
| AC6 | Focused tests pass. |
| AC7 | CCLV-T2 remains paused until FPRC-T1 is reviewed and committed. |

## Evidence / Verification

Worker evidence must include:

- focused pytest for `governance/compat/test_check_finding_to_governance_learning.py`;
- checker self-run for `governance/compat/check_finding_to_governance_learning.py`;
- worker-return fast gate with the focused pytest target;
- `git diff --check`;
- completion review with Root Cause To Propagated Findings, Machine Closure
  Package, Finding-To-Governance Learning Disposition, Public Export
  Disposition, and Agent Operation Trace Block.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance baseline. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 FPRC-T1 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md` |
| Allowed scope source | operator priority override for FPRC-T1 before CCLV-T2 |
| Before status evidence | base `aa977426` |
| After status evidence | GC-018 authored; pending material commit |
| Diff evidence | `git diff --name-status`; dispatch gates |
| Approval boundary | GC-018 and dispatch only |
| Claim boundary | governance guard authorization only |
| Expected manifest | `docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md`; `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` |
| Actual changed set | docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md; docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md; docs/work_orders/CVF_AGENT_WORK_ORDER_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_FOR_CLAUDE_2026-06-16.md; docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md; docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes FPRC-T1 governance hardening only. It does not prove
the worker implementation, public readiness, production readiness, runtime
behavior, provider behavior, live proof, or historical migration.
