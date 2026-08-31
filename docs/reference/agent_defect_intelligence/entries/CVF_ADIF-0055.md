# ADIF-0055 - Local Document Gates Pass While Semantic Problem Boundary Keeps Moving

Memory class: POINTER_RECORD

Status: ACTIVE

EPISTEMIC_PROCESS_NA_WITH_REASON: defect-record entry per the ADIF entry
template; it fixes a defect field template and cites canonical sources, and
does not itself make a new evidence-comparison or hypothesis-testing claim.

```text
defectId: ADIF-0055
title: Local document gates pass while semantic problem boundary keeps moving
defectCategory: GATE_TRIGGER_FRICTION
defectClass: PHASE_GATE_PLACEMENT_GAP
defectRole: worker; reviewer
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review
roles: worker; reviewer; closer; dispatcher
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: new or changed docs/work_orders/*.md; new or changed docs/reviews/*_WORKER_RETURN_*.md; docs/baselines/*.md declaring SCEC
detectionSignals: a successive decision packet narrows a prior remaining gap to one item while the reviewer's independent correction expands the same claim family's scope; repeated single-gap "PARTIAL_READY_REQUIRES_ONE_NAMED..." terminals across successive rounds without an integrated contract; a claim asserted as resolved in one round and rejected on the same evidence class in a later round
enforcementLevel: MACHINE_CHECKED
checkerBindings: governance/compat/check_semantic_convergence_control.py
promotionState: STANDARD_ADDED_AND_MACHINE_GATE_PLACED
supersedes: NONE
lastVerifiedCommit: PENDING_CURRENT_HARDENING_COMMIT
roadmapSeedId: NONE
```

## Purpose

Make discoverable, for future agents, the repeated defect the SCEC-T1
foundation answers: each packet in the GC-010 T1J-R1-through-R3 chain could
satisfy its own local document/structural gates while the declared semantic
problem boundary continued to move underneath it. Local gate compliance
measured document shape, not convergence of the underlying problem.

## Scope / Applies To

Applies to any CVF-governed baseline, work order, or worker return that is
part of a multi-round problem-decision chain: a successor packet that narrows
a prior packet's stated remaining gap, especially when a reviewer correction
subsequently expands scope or rejects a claim the worker treated as resolved.
Does not apply to single-round, non-chained decision packets, and does not
authorize inspection of private reasoning or reasoning traces.

## Bad Example

T1J-R2's worker return narrows the remaining decision to one connection-
lifecycle/storage-path gap and selects a partial-ready terminal. The reviewer
independently finds that route ordering and payload provenance (a different
claim family) were never actually resolved, expanding scope. T1J-R3's worker
return then asserts an exactly-once creation proof using
`ApprovalStore.delete()` as a single-winner barrier and again selects a
narrow partial-ready terminal, as if only one item remained. The reviewer
rejects that specific barrier a second time on the same claim family. Each
worker return individually satisfies its own required-headings and
Source-Verification-table document gates; nothing machine-observable flags
that the declared problem boundary kept moving, or that a fourth narrow
decision (T1J-R4) would repeat the pattern.

## Good Example

Every new or changed work order and worker return declares exactly one
Semantic Convergence Outcome block
with a stable `problemKey`, monotonic `chainOrdinal`, predecessor path/hash,
reconciled blocker-delta sets, and escalation counters. Once the counters
cross a fixed threshold (one reviewer scope expansion, two partial-ready
closures, or a repeated same-claim correction), `check_semantic_convergence_control.py`
fails closed on missing blocks, predecessor identity/ordinal/blocker/counter
resets, and any successor that stays narrow after escalation. Two consecutive
non-decreasing blocker transitions force `STOP_REASSESS_ARCHITECTURE` and
forbid another successor in the same problem chain. The checker validates
declared evidence shape; it does not judge engineering truth.

## Canonical Sources

- `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/baselines/CVF_GC018_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_2026-08-31.md`
- `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`
- `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md`

## Remediation

Bind a Semantic Convergence Outcome block to every new or changed governed
work order and worker return via
`governance/compat/build_dispatch_packet_scaffold.py` and
`governance/compat/build_worker_return_skeleton_scaffold.py` /
`governance/compat/run_worker_return_scaffold.py`. Run
`governance/compat/check_semantic_convergence_control.py` at the earliest
applicable autorun phase (bound into `_common_commands`) and in all three
local hook catalogs so an unjustified narrow successor after standing
escalation fails before it reaches a human reviewer. Reviewer judgment
remains authoritative on whether a claim is semantically correct; the checker
only enforces that declared escalation counters and successor-scope tokens
are internally consistent.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated governance implementation worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | SCEC-T1 semantic convergence foundation implementation, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed reads, checker/test authoring, `python -m unittest`, governance gates |
| Target paths | this entry; `docs/reference/agent_defect_intelligence/entries/README.md`; `docs/reference/semantic_convergence_control/`; `governance/compat/check_semantic_convergence_control.py` and its focused tests |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_2026-08-31.md` |
| Before status evidence | no SCEC standard, checker, or ADIF entry existed; GC-010 T1J chain's semantic-boundary drift was undetected by any machine gate |
| After status evidence | SCEC standard, fail-closed checker, historical replay fixture, and this entry are resolver-discoverable and gate-bound |
| Diff evidence | exact 21-path SCEC-T1 worker changed-set, per the worker return's changed-path manifest |
| Approval boundary | local governance learning and machine-check binding only; no GC-010 product/runtime, provider/live, or public-sync claim |
| Claim boundary | declared-evidence-shape defect record only; no semantic-truth-scoring or reasoning-trace-inspection claim |
| Agent type | worker |
| Invocation ID | `scec-t1-adif-0055-2026-08-31` |
| Expected manifest | this entry and the entries README index row |
| Actual changed set | this entry and the entries README index row |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence and governance-foundation
control detail. Public export, if ever desired, requires a separate reviewed
public-sync batch.

## Claim Boundary

This entry records a reusable defect and its machine enforcement. The SCEC
checker validates declared evidence shape (hashes, set algebra, schema
fields, dispositions) only; it does not inspect chain-of-thought, score prose
quality, or determine semantic truth. It does not claim all future
semantic-drift patterns are prevented, only that this specific escalation
class is now machine-observable.
