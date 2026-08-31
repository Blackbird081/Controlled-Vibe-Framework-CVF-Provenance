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
- `docs/baselines/CVF_GC018_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_2026-08-31.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_2026-08-31.md`
- `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_WORKER_RETURN_2026-08-31.md`

## Second Observed Instance - Mixed-Fence Active-Block Detection Miss

The SCEC-T1 foundation checker's own fenced-JSON discovery was itself a
second instance of this defect's broader class: a document/structural gate
(here, active-block extraction) can look correct in isolation while missing
the real semantic content underneath. `governance/compat/check_semantic_convergence_control.py`
originally extracted fenced JSON with one regex,
`` ```(?:json)?\s*\n(.*?)``` ``, applied over the whole document. A closing
fence also matches that same opening pattern, so when an earlier non-JSON
fenced block (for example a `powershell` block) appeared before one valid
active SCEC JSON block in a governed work order, the regex paired the
`powershell` block's own closing fence with the JSON block's opening fence as
if that combination were one match, consumed the wrong span, and never
reached the real JSON block. `find_active_blocks(...)` returned zero, and the
required-work-order gate then reported a false `MISSING_REQUIRED_SCEC_BLOCK`
violation on a work order that actually carried a valid block.

Prevention: replace regex fence-pairing with an explicit structural scanner
(`_iter_fenced_blocks`) that tracks a single outside/inside-fence state per
line. The first fence line encountered while outside a fence always opens a
block; the next fence line encountered while inside a fence always closes
that same block regardless of its own trailing language tag, and is never
reinterpreted as a new opener. This makes an ordinary closing fence
structurally impossible to pair as a later block's opening boundary, which a
single whole-document regex cannot guarantee. Regression coverage added: the
direct reproducer, a non-JSON fence after the active block, non-JSON fences
on both sides, multiple ordinary fenced blocks around the active block, an
untagged active JSON block preceded by a non-JSON fence, and confirmation
that quoted-marker immunity and malformed-active-candidate fail-closed
behavior are unchanged.

## Third Observed Instance - Unsupported Resolution Laundering

The SCEC-E1 effectiveness reconciliation (accepted with material correction
at `d504ac6e006f9d7f7cb5bd3d03cb5dbf9c5f41f5`) independently found that the
replay fixture and dispatch seed marked
`T1J_BLOCKER_ROUTE_ORDER_AND_PAYLOAD_PROVENANCE_UNDECIDED` resolved even
though accepted R3 evidence keeps audit/consume ordering undecided and
payload work blocking. Set algebra still validated because `resolved` and
`retained` remained disjoint and reconciled, so an unresolved blocker could
be laundered as `resolved` without binding that transition to any accepted
evidence. The correct accepted R2-to-R3 transition is 3 to 4 (three retained
plus the rejected exactly-once barrier as new), not 3 to 3.

Prevention: add a machine-checked per-resolved-blocker evidence binding
(`resolutionEvidence`) keyed exactly to `blockerDelta.resolved`. Each binding
carries an `evidenceClass` (`ACCEPTED_REVIEW` or `EXECUTABLE_PROOF`), a
normalized repository-relative `evidencePath`, an immutable `sha256`, a
non-empty `locator`, and an optional `claimId` linking an executable
resolution to a claim in the same block. The checker recomputes the
referenced file hash and fails closed on missing/extra/wrong bindings,
unsafe or unreadable paths, hash mismatch, empty locator, and invalid claim
links. Regression coverage includes positive accepted-review and
executable-proof bindings plus negative bypasses for every named failure
mode. Independent reviewer probing found one inheritance bypass: successor
validation initially checked the predecessor block without the evidence hash
resolver, so later evidence-target drift inherited trust silently. The
accepted implementation revalidates predecessor resolution-evidence hashes at
successor consumption time and carries a focused regression for that path.

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

## Agent Operation Trace Block - SCEC-T1-R1 Mixed-Fence Hardening

| Field | Evidence |
|---|---|
| Actor | delegated governance implementation worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | SCEC-T1-R1 mixed-fence active-block parser hardening, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed reads, direct reproducer probe, checker/test authoring, `python -m unittest`, governance gates |
| Target paths | this entry; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/test_check_semantic_convergence_control.py`; `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_WORKER_RETURN_2026-08-31.md` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_2026-08-31.md` |
| Before status evidence | `find_active_blocks(...)` returned `[]` for a governed work order carrying one non-JSON fenced block before one valid active SCEC JSON block, per the direct local reproducer |
| After status evidence | structural `_iter_fenced_blocks` scanner finds exactly one active block across the direct reproducer plus before/after/both-side and multiple-fence order variants; full focused suite passes |
| Diff evidence | exact four-path SCEC-T1-R1 worker changed-set, per this worker return's changed-set section |
| Approval boundary | local parser correctness repair and regression proof only; no semantic threshold, product/runtime, provider/live, or public claim |
| Claim boundary | declared-evidence-shape defect record only; no semantic-truth-scoring or reasoning-trace-inspection claim |
| Agent type | worker |
| Invocation ID | `scec-t1-r1-adif-0055-2026-08-31` |
| Expected manifest | this entry only, within the four-path SCEC-T1-R1 worker manifest |
| Actual changed set | this entry only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this tranche |

## Agent Operation Trace Block - SCEC-T1-R2 Resolution Evidence Binding

| Field | Evidence |
|---|---|
| Actor | delegated governance implementation worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | SCEC-T1-R2 blocker resolution evidence binding and historical replay correction, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed reads, checker/test/scaffold authoring, `python -m unittest`, governance gates |
| Target paths | this entry; `docs/reference/semantic_convergence_control/` standard; `governance/compat/check_semantic_convergence_control.py`; its focused tests; the replay fixture; both worker-return scaffold producers and the golden fixture |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R2_BLOCKER_RESOLUTION_EVIDENCE_BINDING_AND_HISTORICAL_REPLAY_CORRECTION_2026-08-31.md` |
| Before status evidence | `resolved` arrays could pass set algebra with no per-blocker evidence; the replay fixture resolved the still-open route-order/payload blocker |
| After status evidence | invariant 13 and the `resolutionEvidence` binding are machine-enforced; the corrected R3 reviewer node retains all three R2 blockers plus the rejected exactly-once barrier (current count 4) |
| Diff evidence | exact eleven-path SCEC-T1-R2 worker changed-set, per this worker return's changed-set section |
| Approval boundary | local governance checker/scaffold/test hardening only; no product/runtime, provider/live, or public-sync claim |
| Claim boundary | declared-evidence-shape defect record only; no semantic-truth-scoring or reasoning-trace-inspection claim |
| Agent type | worker |
| Invocation ID | `scec-t1-r2-adif-0055-2026-08-31` |
| Expected manifest | this entry only, within the eleven-path SCEC-T1-R2 worker manifest |
| Actual changed set | this entry only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this tranche |

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
