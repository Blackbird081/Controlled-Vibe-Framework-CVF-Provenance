# CVF Agent Work Order - ADIF-T4 Reviewer Finding Intake Bridge

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-06-23

docType: work_order

closureBaseHead: NOT_EXECUTED_YET

## Dispatch Prompt Envelope

Role: Claude continuous-execution orchestrator/worker, executing the T4
evidence branch of the joint ADIF-T3/T4 dispatch, forked from the
handoff-sync bridge HEAD.

Canonical packet:
`docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: `617b041f` (the ADIF-T3/T4 joint dispatch handoff-sync
bridge HEAD).

executionBaseHead: `f8f82a8e` (the T3-branch-integration handoff-sync
bridge HEAD; T4 is serialized after T3 in the single working directory
per the operator's worktree-fallback decision, with both branches
verified to share zero file paths).

Current-time notes: this is the T4 evidence branch only. Same
worktree-fallback condition as T3: real OS-level isolation via
`EnterWorktree` failed on this machine; serialized execution with disjoint
write ownership substitutes for filesystem-level isolation, per operator
decision already recorded in the T3 branch work order.

Do-not-misread notes: this checkpoint covers only the two T4 paths listed
below. The classification function never writes, modifies, or promotes
any ADIF entry file; it returns a bounded classification only.

Required first actions: none beyond the joint dispatch's Required First
Reads, already completed before the T3/T4 branches began.

Return contract: this branch returns `COMPLETE_PENDING_REVIEW`; per the
operator's continuous-execution instruction, Claude continues directly
into convergence and then ADIF-T5 without a Codex pause.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one bounded, non-auto-promoting
finding-intake bridge helper plus its focused test under
`governance/compat/`, per the ADIF-T3/T4 joint GC-018 baseline's Allowed
scope (ADIF-T4 branch).

Protected paths (every changed guard/control path is listed):

- `governance/compat/run_adif_finding_intake_bridge.py`
- `governance/compat/test_run_adif_finding_intake_bridge.py`

Operator authorization: the operator pre-selected the T0-T5 continuous
sequence and instructed Claude to execute T3->T4->T5 continuously without
a Codex pause, per the joint GC-018 baseline and the Continuous Execution
Handoff-Sync Bridge Standard.

Rollback boundary: if this T4 branch is rejected, remove only the two
named paths above and this work order. Do not revert the ADIF-T3/T4 joint
dispatch commit (`af56db7c`), its handoff-sync bridge (`617b041f`), or the
T3 branch checkpoint (`41b026a6`) or its handoff-sync bridge (`f8f82a8e`).

Scope boundary: this authorization does not extend to existing guard
behavior, active session files, root handoff files, runtime/product
source, public-sync, provider/live proof, direct-interception tooling, or
any CLI/MCP adapter.

## Scope / Owner Boundary

Allowed scope: create `governance/compat/run_adif_finding_intake_bridge.py`
and `governance/compat/test_run_adif_finding_intake_bridge.py` only, per
the joint GC-018 baseline's T4 Allowed scope. Forbidden scope is identical
to the joint baseline's Forbidden scope for ADIF-T3/T4, including: never
auto-promote any finding to a canonical entry or checker.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_adif_finding_intake_bridge.py` | Claude (T4 branch) | create |
| `governance/compat/test_run_adif_finding_intake_bridge.py` | Claude (T4 branch) | create |
| this work order | Claude (T4 branch) | create, commit |

Disjointness statement: T4 shares zero file paths with the T3 branch
(`governance/compat/run_adif_preflight_readout.py`,
`governance/compat/test_run_adif_preflight_readout.py`, and the T3 work
order).

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Joint ADIF-T3/T4 GC-018 baseline | `docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md` | ACCEPT |
| Joint ADIF-T3/T4 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md` | ACCEPT |
| Handoff-sync bridge after joint dispatch | `617b041f` | ACCEPT |
| T3 branch checkpoint | `41b026a6` | ACCEPT |
| T3-branch-integration handoff-sync bridge | `f8f82a8e` | ACCEPT |
| Continuous Execution Handoff-Sync Bridge Standard | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | ACCEPT |

## Required First Reads

Inherited in full from the joint ADIF-T3/T4 GC-018 baseline's Required
First Reads, already completed before this branch began:
`docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python -m pytest governance/compat/test_run_adif_finding_intake_bridge.py -v
```

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one new sibling `governance/compat/run_adif_finding_intake_bridge.py` module plus matching test file, following existing flat-import compat conventions |
| Storage decision | one intake-bridge module, one test module; no generated aggregate; no relocation or refactor of any existing file |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | bounded, read-only classification function over the existing ADIF-T2 resolver's entry loader; no entry file write, no CLI/MCP surface |

## Mission

Implement the ADIF-T4 bounded, non-auto-promoting finding-intake bridge
function and its focused tests, per the joint GC-018 baseline.

## Purpose

Give reviewer findings and worker friction items a structured, governed
classification path into one of five bounded outcomes, preserving F2G
disposition and FPRC defectRole vocabularies, without ever auto-promoting
a finding into a canonical entry or checker.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority; pre-selected the T0-T5 continuous sequence |
| Dispatcher | Claude authored the joint T3/T4 GC-018 baseline and this T4 branch packet |
| Orchestrator/worker | Claude |
| Reviewer/closer | Codex, once after the complete T0-T5 graph returns |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Claude orchestrates and executes the T4 branch under `WORKER_MAY_COMMIT`; Codex reviews and closes the complete T0-T5 chain once after T5 |
| phase | EXECUTION |
| baseHeadFor(phase) | `executionBaseHead=f8f82a8e` (T3-branch-integration bridge HEAD, serialized) |
| changedSetScope(phase) | T4 branch = intake bridge module, intake bridge test, this work order |
| traceScope(phase, actor) | one trace covers this T4 branch checkpoint |
| commitOwner(phase) | Claude commits this T4 checkpoint under `WORKER_MAY_COMMIT` |
| crossBatchIsolation | T4 declares zero shared paths with T3; both converge into the same branch without overlap |
| nextMoveSurfaces | Claude continues directly into convergence and ADIF-T5 without a Codex pause |
| Closer designation | Codex |

## Execution Plan

1. Confirm `executionBaseHead` and clean worktree.
2. Implement `run_adif_finding_intake_bridge.py` with the five bounded
   outcomes.
3. Implement `test_run_adif_finding_intake_bridge.py` with focused
   coverage of all five outcomes plus the no-mutation guarantee.
4. Run focused tests; confirm all pass.
5. Run real-range pre-implementation gate; repair and rerun until clean.
6. Commit the T4 branch checkpoint; continue directly into convergence.

## Evidence Requirements

- `python -m pytest governance/compat/test_run_adif_finding_intake_bridge.py -v`
  result with all 10 tests passing;
- explicit statement that no ADIF entry file was created, modified, or
  promoted by this module;
- exact claim boundary and public export disposition.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Returns exactly one of five required outcomes per finding | `test_all_five_outcomes_are_distinct_and_in_valid_set` |
| AC2 | Never auto-promotes; no entry file mutation | `test_classification_never_mutates_entries_directory` |
| AC3 | Reject outcome always carries a non-empty reason | `test_session_local_finding_is_rejected_with_reason`; `test_unknown_defect_id_is_rejected_pending_source_verification` |
| AC4 | Preserves F2G/FPRC vocabularies without redefining them | module review (no new canonical enum defined) |
| AC5 | Focused tests pass | `pytest` run: 10/10 |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Without a bounded intake bridge, reviewer findings had no structured, non-auto-promoting path into the ADIF dictionary | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T4 implements the bounded classification function |

Runtime/provider/cost learning lane: N/A_WITH_REASON - no runtime,
provider, or cost behavior is executed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-implementation work. No public-sync
repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T4 branch execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | file write tool, pytest, governance gates, git commit |
| Target paths | this work order; intake bridge module; intake bridge test |
| Allowed scope source | joint ADIF-T3/T4 GC-018 baseline's T4 Allowed scope |
| Before status evidence | executionBaseHead `f8f82a8e`; clean worktree confirmed |
| After status evidence | T4 branch checkpoint committed; execution continues into convergence and ADIF-T5 |
| Diff evidence | T4-branch-only name-status and committed diff |
| Approval boundary | ADIF-T4 branch scope only |
| Claim boundary | bounded, non-auto-promoting classification helper; no runtime/public/provider/external-adapter expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t4-branch-execution-2026-06-23` |
| Expected manifest | this work order; intake bridge module; intake bridge test |
| Actual changed set | this work order; intake bridge module; intake bridge test |
| Manifest delta | MATCH |

## Review Gate

Codex reviews the T4 branch as part of the complete T0-T5 graph review
once after T5. No per-branch reviewer pause is required, per this turn's
explicit instruction and the Continuous Execution Handoff-Sync Bridge
Standard.

## Closure Checklist

- [x] T4 intake bridge module and test created inside Allowed scope only.
- [x] Focused tests pass (10/10).
- [x] No ADIF entry file created, modified, or promoted.
- [x] Core Guard Self-Protection Authorization block present for both
      protected paths.
- [ ] Codex review of the complete T0-T5 graph after T5 (pending; not
      owned by this branch packet).

## Return-To-Orchestrator Conditions

Return success as `COMPLETE_PENDING_REVIEW` for this T4 branch and
continue directly into convergence and ADIF-T5. Return
`BLOCKED_WITH_REASON` for any Stop Condition in the canonical authorization
or the bridge standard.

## Operator Checkpoint

The human principal pre-selected the entire continuous sequence and this
turn separately instructed Claude to run T3->T4->T5 continuously without a
Codex pause. A fresh pause applies only to scope/risk/claim expansion,
runtime/provider/live/public work, secrets/quota, destructive action,
canonical-owner semantic change, write ownership overlap that cannot be
safely serialized, or a different execution order than the one named
above.

## Claim Boundary

This work order records only the ADIF-T4 branch checkpoint. It does not
authorize ADIF-T5 implementation, any CLI/MCP adapter, or final closure.
Codex remains the designated final reviewer/closer for the complete T0-T5
chain.
