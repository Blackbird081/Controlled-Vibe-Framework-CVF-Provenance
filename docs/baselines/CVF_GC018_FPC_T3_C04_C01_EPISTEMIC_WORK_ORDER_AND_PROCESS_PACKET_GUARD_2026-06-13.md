# CVF GC-018 - FPC-T3-C04+C01 Epistemic Work-Order And Process Packet Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `0101eddf`

sourceAuthority:
`docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

## Purpose

Authorize the next bounded FPC foundation implementation tranche: pair
FPC-T3-C04, a work-order template epistemic block, with FPC-T3-C01, a
deterministic epistemic process packet checker.

The goal is to catch the recurring failure mode where a guard appears to pass
but did not verify the intended evidence block. The implementation must improve
pre-dispatch and reviewer-fast evidence quality without turning every small
agent action into a high-latency checkpoint.

## Scope / Target / Owner Boundary

Target:

- add a bounded epistemic block to the canonical work-order template for
  high-evidence governed work;
- implement a structural checker for evidence-heavy worker-return and
  completion packets;
- wire the checker into the earliest useful local governance gate without
  broadening runtime/provider scope;
- add deterministic tests, including false-positive and not-applicable cases.

Owner boundary:

- Codex owns this GC-018, the work order, dispatch review, final acceptance,
  commit, and any session continuity update.
- Claude owns only allowed implementation artifacts under
  `WORKER_MUST_NOT_COMMIT`.
- Claude must not edit session state, active handoff, front door, public-sync,
  runtime/provider code, OS audit setup, endpoint telemetry, or downstream
  use-case surfaces.

## Decision / Baseline / Proposed Tranche

Decision: open the FPC-T3-C04+C01 implementation tranche because FPC-T3 ranked
C01 as the highest priority machine-check candidate and C04 as the paired
template anchor.

Baseline:

- current dispatch base: `0101eddf`;
- FPC-T3 coverage closure commit: `c1fd85d3`;
- AOT-T2-C01+C02 closure state: `CLOSED_PASS_BOUNDED`;
- FPC-T3 accepted next move: open FPC-T3-C04 plus FPC-T3-C01 through a fresh
  source-verified work order.

Proposed tranche:

- update `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` with a
  narrow epistemic block for high-evidence work orders;
- create `governance/compat/check_epistemic_process_packet.py`;
- add focused tests under `governance/compat/`;
- wire the checker into `governance/compat/run_local_governance_hook_chain.py`
  at reviewer-fast or an equally early local hook phase;
- ensure `governance/compat/run_worker_return_fast_gate.py` runs the checker
  through reviewer-fast once the hook-chain wiring exists;
- keep `EPISTEMIC_PROCESS_NA_WITH_REASON` available for mechanical or
  low-evidence work with a required reason.
- allow a narrow AOT checker false-positive repair only if the new template
  section or worker-return manifest ordering causes this tranche to fail the
  existing Agent Operation Trace gate.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| FPC-T3 coverage plan closed | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` recommends C04+C01 as the first implementation tranche | ACCEPT |
| FPC-T2-C05 registry viability depends on C01 | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` records FPC-T3-C01 as the hard prerequisite for C05 | ACCEPT |
| Work-order template is the owner surface for C04 | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` is the canonical work-order template | ACCEPT |
| Reviewer-fast hook chain exists | `governance/compat/run_local_governance_hook_chain.py` owns `REVIEWER_FAST_CHECKS` and `HOOK_CHAINS` | ACCEPT |
| Worker-return fast gate delegates to reviewer-fast | `governance/compat/run_worker_return_fast_gate.py` owns `build_commands` and invokes reviewer-fast | ACCEPT |
| Protected-path carrier required | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` section 7A and `governance/compat/check_work_order_dispatch_quality.py` require a Core Guard Self-Protection Authorization block for `governance/compat/*.py` work | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: FPC-T3 recommends C04+C01 as first implementation tranche | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | line 316 | `Recommended First Implementation Tranche` | FPC-T3 coverage plan | ACCEPT |
| EXISTS: C01 is the hard prerequisite in the FPC-T3 chain | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | line 321 | `FPC-T3-C01` | FPC-T3 coverage plan | ACCEPT |
| EXISTS: C04 is the work-order template epistemic block candidate | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | line 276 | `FPC-T3-C04` | FPC-T3 coverage plan | ACCEPT |
| EXISTS: C01 requires structural sections and not semantic correctness | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | line 367 | `check_epistemic_process_packet.py` | FPC-T1 audit matrix | ACCEPT |
| EXISTS: FPC-T2-C05 requires C01 before registry entry | `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | line 497 | `FPC-T2-C05` | FPC-T2 decision matrix | ACCEPT |
| EXISTS: source verification is required for dispatch work orders | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 344 | `Source Verification Block` | canonical work-order template | ACCEPT |
| EXISTS: roadmap-derived work orders require trace matrix | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 506 | `Roadmap-To-Work-Order Trace Matrix` | canonical work-order template | ACCEPT |
| EXISTS: protected-path authorization carrier is required | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 868 | `Protected-Path Authorization Carrier` | canonical work-order template | ACCEPT |
| EXISTS: reviewer-fast hook chain owner | `governance/compat/run_local_governance_hook_chain.py` | line 24 | `REVIEWER_FAST_CHECKS` | local governance hook chain | ACCEPT |
| EXISTS: hook-chain map owner | `governance/compat/run_local_governance_hook_chain.py` | line 90 | `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| EXISTS: worker-return fast gate command builder | `governance/compat/run_worker_return_fast_gate.py` | line 28 | `build_commands` | worker-return fast gate | ACCEPT |
| EXISTS: protected path detector for dispatch quality | `governance/compat/check_work_order_dispatch_quality.py` | line 447 | `_is_protected_authorization_path` | dispatch quality checker | ACCEPT |
| EXISTS: protected carrier validator for dispatch quality | `governance/compat/check_work_order_dispatch_quality.py` | line 467 | `_validate_protected_path_authorization_carrier` | dispatch quality checker | ACCEPT |
| EXISTS: trace block requirement for agent execution evidence | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 54 | `Agent Operation Trace Block` | AOT standard | ACCEPT |
| EXISTS: trace checker enforces required labels | `governance/compat/check_agent_operation_trace.py` | line 27 | `TRACE_REQUIRED_LABELS` | agent operation trace checker | ACCEPT |
| EXISTS: trace artifact classifier owns reference-template trace eligibility | `governance/compat/check_agent_operation_trace.py` | line 154 | `is_trace_artifact` | agent operation trace checker | ACCEPT |
| EXISTS: trace violation scanner owns manifest-delta candidate selection | `governance/compat/check_agent_operation_trace.py` | line 347 | `find_trace_violations` | agent operation trace checker | ACCEPT |

## Current Runtime Freshness Verification

| Source fact | Verification command or evidence | Disposition |
| --- | --- | --- |
| `check_epistemic_process_packet.py` is not an implemented runtime checker yet | `rg -n "check_epistemic_process_packet" governance docs EXTENSIONS scripts` shows planning-document references only and no current `governance/compat/check_epistemic_process_packet.py` file | ACCEPT |
| The implementation target is a new governance checker plus narrow AOT false-positive repair, not a runtime/provider route | Allowed artifact set is limited to `docs/reference/` template, `governance/compat/` checker/tests/hook wrappers/AOT trace-boundary repair, and worker return | ACCEPT |
| No provider API, OCR, retrieval, public-sync, OS audit, endpoint telemetry, or external app mutation is authorized | Forbidden Scope in paired work order | ACCEPT |

## New Doc-Only Fields

The work-order template change may introduce these doc-only field labels for
high-evidence governed work orders:

| Field | Purpose |
| --- | --- |
| `Epistemic Process Applicability` | declares whether the work order is high-evidence, evidence-light, or mechanical |
| `Expected Result / Prediction` | records the expected outcome the worker must compare against actual evidence |
| `Evidence Comparison Requirement` | states how actual evidence must be compared to the expected result |
| `Contradiction Handling Requirement` | requires contrary evidence to produce a claim update, exception, or checkpoint |
| `Claim Update Requirement` | requires the worker return or completion to record whether the claim changed |
| `EPISTEMIC_PROCESS_NA_WITH_REASON` | allowed escape for mechanical or low-evidence work, with an explicit reason |

These are template/checker fields only. They are not runtime receipt fields,
provider fields, registry fields, or session-state fields.

## Negative Search And Collision Discipline

Before implementation, Claude must run:

```powershell
rg -n "check_epistemic_process_packet|EPISTEMIC_PROCESS_NA_WITH_REASON|Epistemic Process Applicability|Expected Result / Prediction|Contradiction Handling Requirement" governance docs EXTENSIONS scripts
```

Required disposition:

- occurrences in FPC planning documents are planning authority only;
- no existing `.py` implementation of `check_epistemic_process_packet.py` may
  be treated as present unless a current file exists under `governance/compat/`;
- same-token occurrences in historical reviews must be recorded as collisions,
  not implementation evidence.

## Evidence / Verification

Dispatch verification required before handoff:

- `python governance/compat/check_agent_operation_trace.py --base 0101eddf --head HEAD --enforce`;
- `python governance/compat/check_work_order_dispatch_quality.py --base 0101eddf --head HEAD --enforce`;
- `git diff --check`;
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`.

Worker verification required before return:

- focused pytest for the new checker and touched hook/fast-gate tests;
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_epistemic_process_packet.py`;
- worker-return Agent Operation Trace Block with expected manifest, actual
  changed set, and manifest delta;
- `git diff --check`.

Closure verification is reviewer-owned and must use a real committed range
after Codex accepts the worker return. Codex reviewer accepted the narrow AOT
trace-boundary repair because the new template section exposed two false
positives in the existing trace checker: canonical `_TEMPLATE_` files carrying
worker-instruction vocabulary, and manifest-delta selection preferring dispatch
work orders over worker returns. This acceptance does not authorize broader
AOT hardening.

## Claim Boundary

This GC-018 authorizes a bounded governance-control implementation. It proves
only structural packet completeness when the later checker passes. It does not
prove semantic truth, reasoning quality, provider quality, public readiness,
runtime behavior, OS-level user attribution, endpoint telemetry, or autonomous
mutation safety.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control dispatch. Public-sync is not
authorized by this tranche.

rawMemoryReleased=false
