# CVF GC-018 Baseline - Autorun Active Work Order Lane Binding R1

Memory class: governed-dispatch-baseline

docType: baseline

Status: AUTHORIZED_FOR_DISPATCH

Batch ID: CVF-AUTORUN-ACTIVE-WORK-ORDER-LANE-BINDING-R1

Dispatch base head: `40f7bbba71a959541bd424f147028b358a6b7f02`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize one bounded repair of the autorun aggregate so a pre-implementation
caller may bind the current work order to the already implemented
changed-lane independent-probe contract. The repair must keep every unbound
and every non-pre-implementation aggregate invocation broad and fail closed.

## Scope / Target / Owner Boundary

Scope is the existing autorun standard, aggregate runner, command catalog,
focused runner tests and one worker return. Local owns dispatch, independent
review, commit and continuity. The INTERNAL_AGENT worker owns only the first
five material paths listed below and has no commit authority.

## Source / Predecessor Evidence

The predecessor evidence is the reproducible HRLTP-T2 pre-implementation
84/85 result, the current autorun role rule, the existing checker lane-binding
CLI, and the existing fast-gate forwarding implementation. No external source
or provider output is used.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | dispatch status; protected paths; exact gate IDs; active-work-order binding; corpus verdict |
| gateRunPurpose | confirmation after source read-ahead, not first discovery |
| claimBoundary | dispatch baseline only; no implementation result is claimed |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-guard-authoring`, role=`INTERNAL_AGENT`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "governance-guard-authoring" --role INTERNAL_AGENT --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no registered defect changes this bounded repair |

## Learning Trigger And Root Cause

The committed HRLTP-T2 worker correctly stopped before editing when its
required pre-implementation aggregate passed 84 of 85 commands but the broad
independent-probe admission command rejected three older worker returns among
thirteen intentionally parked untracked paths. Direct invocation with
`--changed-lane-only --active-work-order` passed, reported all three findings
as out of lane, and kept the current dispatch's declared untracked return in
the failing lane.

The checker already owns the safe semantics. The aggregate runner cannot pass
the active-work-order context into its common command catalog. This is a
composition gap, not authority to suppress a gate, hide parked evidence, edit
historical returns, or waive the failed aggregate.

## Architecture Decision

Add an optional aggregate `--active-work-order` binding with these invariants:

1. it is accepted only for `pre-implementation`;
2. it adds `--changed-lane-only --active-work-order <exact path>` only to the
   unique independent-probe admission command;
3. the default command and all other phases remain broad;
4. a missing, invalid or ambiguous binding still fails through the existing
   checker contract;
5. the active untracked worker return remains in the failing lane;
6. parked out-of-lane findings remain visible in successful aggregate output;
7. the bound command argv changes command-manifest and receipt identity; and
8. no checker semantics or receipt schema changes.

## Decision / Baseline / Proposed Tranche

Authorize exactly one no-commit maintenance tranche implementing the opt-in
binding above. After Local acceptance, HRLTP-T2 resumes from a fresh captured
execution base; no other successor or runtime authority follows.

## Exact Material Manifest

| Path | Owner | Action |
| --- | --- | --- |
| `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | worker | document the opt-in pre-implementation binding and broad defaults |
| `governance/compat/run_agent_autorun_workflow_gate.py` | worker | accept, phase-check and forward the binding; expose successful parked diagnostics |
| `governance/compat/agent_autorun_command_catalog.py` | worker | parameterize only the unique independent-probe command |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | worker | add forwarding, phase, visibility and receipt-identity regressions |
| `docs/reviews/CVF_AUTORUN_ACTIVE_WORK_ORDER_LANE_BINDING_R1_WORKER_RETURN_2026-09-23.md` | worker | return exact no-commit evidence |
| `docs/reviews/CVF_AUTORUN_ACTIVE_WORK_ORDER_LANE_BINDING_R1_COMPLETION_2026-09-23.md` | Local reviewer | record independent review and terminal disposition |

Worker owns exactly the first five paths. The sixth path is reviewer-only.

## Required Evidence

- default `_common_commands` remains broad and contains one probe command;
- a bound pre-implementation plan contains one probe command with the exact
  two lane arguments and no other command receives them;
- the same binding is rejected at pre-dispatch, pre-closure and pre-push;
- an invalid active return fails while parked findings remain diagnosed but
  nonblocking;
- successful parallel output preserves known parked-finding diagnostics;
- changing or removing the active binding changes receipt reuse identity;
- all existing runner and independent-probe tests pass; and
- the thirteen parked paths remain byte-identical and unstaged.

## Authority And Claim Boundary

This baseline authorizes repository-local guard composition only. It does not
authorize hiding or moving parked files, weakening the broad checker, changing
independent-probe semantics, changing a receipt schema, executing HRLTP-T2
implementation inside this repair, using credentials or alternate principals,
performing ACEL/source/provider/live/runtime/public/deployment action, or
committing as worker.

## Verification Boundary

Acceptance requires focused runner and existing checker suites, one successful
bound pre-implementation aggregate, exact-path reconciliation, unchanged
parked hashes, an empty index and a distinct Local adversarial probe. Static
PASS proves command composition only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private control-plane repair with no public-sync authorization.
