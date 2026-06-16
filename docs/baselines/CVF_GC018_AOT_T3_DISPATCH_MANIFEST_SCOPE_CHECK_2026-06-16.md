# CVF GC-018 Authorization Baseline - AOT-T3 Dispatch Manifest Scope Check

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-16

Batch ID: AOT-T3

rawMemoryReleased: false

## Purpose

Authorize a bounded machine-check cleanup for B12: dispatch Agent Operation
Trace manifests must describe the dispatch changed set, while future execution
deliverables belong in ownership or expected-deliverable sections.

## Authorization Decision

Operator selected AOT-T3 on 2026-06-16 as the faster cleanup before any AHB-T2
contract ratification.

Decision: Codex may implement AOT-T3 as a standalone `WORKER_MAY_COMMIT`
tranche. AHB-T2 remains unopened.

## Baseline Decision

AOT-T3 may modify:

- `governance/compat/check_agent_operation_trace.py`;
- `governance/compat/test_check_agent_operation_trace.py`;
- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
- `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`;
- `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`;
- this GC-018 baseline;
- the matching work order;
- the matching completion review.

No AHB-T2 ratification, public-sync, runtime/product behavior change, external
API usage, or interlock registry edit is authorized.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| B12 dispatch manifest scope discipline exists | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | `## Dispatch Manifest Scope Discipline` | `B12` | finding propagation standard | ACCEPT |
| AOT checker owns manifest comparison | `governance/compat/check_agent_operation_trace.py` | `_check_manifest_delta` | `Expected manifest`; `Actual changed set`; `Manifest delta` | AOT checker | ACCEPT |
| AOT focused tests cover manifest behavior | `governance/compat/test_check_agent_operation_trace.py` | `AgentOperationTraceTests` | `MISSING_DELIVERABLE`; `UNAUTHORIZED_ADDITION` | unittest module | ACCEPT |
| AOT standard owns manifest field semantics | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | `### Expected Manifest And Manifest Delta (AOT-T2-C01)` | `Expected manifest` | AOT standard | ACCEPT |
| AOT-T3 is queued as a separate machine-check follow-up | `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` | `## Cross-Lane Queued Follow-Up: AOT-T3` | `AOT-T3` | finding propagation roadmap | ACCEPT |

## Authorized Scope

Authorized:

- add a dispatch-work-order scope check to the AOT manifest comparison;
- keep future execution paths valid in `Write Ownership`, expected-deliverable,
  and required-artifact sections;
- fail a dispatch work order when the trace `Expected manifest` itself lists a
  future execution path;
- add focused regressions for pass and fail cases;
- update the AOT standard and roadmaps;
- create a completion review with gate evidence.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: patch the existing AOT checker, focused AOT
tests, and AOT standard to enforce B12 dispatch manifest scope discipline. No
hook-chain rewiring, broad parser rewrite, or runtime/product mutation is
authorized.

Protected paths:

- governance/compat/check_agent_operation_trace.py
- governance/compat/test_check_agent_operation_trace.py
- docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md

Operator authorization: operator selected AOT-T3 on 2026-06-16 after agreeing
it was the faster cleanup before AHB-T2.

Rollback boundary: if rejected, revert only the AOT-T3 checker, test, standard,
roadmap, work-order, GC-018, and completion changes. Do not revert AHB-T1,
AHB-T1A, PLCS, or FPRC closure history.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Future execution paths listed in work-order ownership sections do not count as dispatch manifest paths. |
| AC2 | A dispatch work-order trace `Expected manifest` that lists a future execution path fails with `DISPATCH_SCOPE_VIOLATION`. |
| AC3 | Existing AOT-T2 manifest `MATCH`, `MISSING_DELIVERABLE`, and `UNAUTHORIZED_ADDITION` behavior remains covered by tests. |
| AC4 | AOT standard documents the dispatch manifest scope rule. |
| AC5 | Finding-propagation and AHB roadmaps record AOT-T3 as shipped standalone while AHB-T2 remains unopened. |
| AC6 | Completion review records gates and bounded claim boundary. |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: AOT-T3 changes governance checker/test
code and governance Markdown only. It does not change CVF product runtime,
model routing, provider adapter behavior, public-sync content, live governance
behavior, or interlock registry data.

## Evidence / Verification

Required focused checks:

- `python -m unittest governance.compat.test_check_agent_operation_trace`
- `python governance/compat/check_agent_operation_trace.py --base e509aa4d --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base e509aa4d --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base e509aa4d --head HEAD --enforce`

## Rescan Intelligence Hardening

- Original source artifact: PLCS-T3 B12 promotion in finding-propagation
  standard and roadmap.
- Predecessor intake artifact: PLCS-T3 completion and AHB-T1/AHB-T1A sequencing
  notes.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: DO_NOW for AOT-T3 only; AHB-T2 remains separate.
- Semantic sampling status: focused AOT dispatch-scope tests.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | AOT-T3 disposition |
|---|---|
| `UNCHANGED_FROM_INTAKE` | B12 remains a dispatch manifest scope defect. |
| `CHANGED_DISPOSITION` | AOT-T3 moves from queued machine-check candidate to closed checker hardening. |
| `NEW_FINDING` | None. |
| `REMOVED_OR_REJECTED` | B11 remains documentation-only guidance; AHB-T2 remains unopened. |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
|---|---|---|
| RESOLVED_BY_DESIGN | B12 dispatch manifest scope | checker/test/standard update |
| DOCUMENTATION_ONLY | B11 boundary prose trigger guidance | existing standard/addendum guidance remains sufficient |
| SEPARATE_RUNTIME_TRANCHE | Product runtime or live-governance behavior | not part of this checker cleanup |
| STRATEGIC_OPERATOR_DECISION | AHB-T2 contract ratification | not opened by AOT-T3 |
| OUT_OF_SCOPE | Runtime/product/public-sync/provider behavior | explicitly forbidden |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AOT-T3-B1 | B12 standard | future deliverables belong outside dispatch manifest | ownership-only paths | Could ownership paths falsely become manifest paths? | PASS |
| AOT-T3-B2 | B12 standard | future deliverables in dispatch manifest are defects | Expected manifest violation | Could a future path hide inside Expected manifest? | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

AOT-T3 closes the B12 dispatch manifest scope machine-check cleanup. It does
not ratify AHB-T2, implement a unified handoff contract checker, alter runtime
or provider behavior, edit public-sync content, or claim production/public
readiness.
