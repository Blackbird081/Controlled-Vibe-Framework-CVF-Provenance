# CVF Agent Handoff V18 - Active Session Continuity

Memory class: POINTER_RECORD

Status: ACTIVE HANDOFF

Date opened: 2026-06-12

Supersedes:
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V17_2026-06-07.md`

## Purpose

This compact handoff records EXA-T1 closure, the next foundation move, and
parked operator checkpoints. Detailed history remains in governed completion
artifacts and archived handoffs.

## Scope / Target / Owner Boundary

Target: route the next bounded CVF foundation work after EXA-T1.

Owner boundary: this file is a pointer record. Runtime, tests, source maps,
reviews, and roadmap evidence remain in their governed owner paths.

## Startup Acknowledgment

Startup acknowledged: current mode=`exa_t2_scan_signal_route_decision_contracts_dispatched`; active handoff=`AGENT_HANDOFF_V18_2026-06-12.md`; next allowed move=Claude executes EXA-T2 under WORKER_MUST_NOT_COMMIT and returns uncommitted artifacts for Codex review; parked checkpoint=Policy_Local integration, EC activation/retrieval, T12, DEP2/Redis/receipt-anchor lanes remain parked.

## Current Mode

`exa_t2_scan_signal_route_decision_contracts_dispatched`

Current HEAD recorded for this handoff: `5ad40259`
(EXA-T2 scan signal and route decision contracts dispatch commit; this
dedicated session sync follows).

## Active Boundary

Active handoff: `AGENT_HANDOFF_V18_2026-06-12.md`.

Archived predecessor:
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V17_2026-06-07.md`.

This private provenance repository is not the public CVF front door.
Public-facing work remains restricted to the sibling public-sync clone and
requires separate authorization.

## Latest Continuity Note

EXA-T1 external extraction pattern absorption is
`CLOSED_PASS_BOUNDED`.

Material review commit: `6db11aed`.

Closure commit: `1509aa81`.

Reviewer-fast rescan gate placement hardening is `CLOSED_PASS_BOUNDED` at
material commit `aeb39903`.

Artifacts:

- completion:
  `docs/reviews/CVF_REVIEWER_FAST_RESCAN_GATE_PLACEMENT_HARDENING_COMPLETION_2026-06-12.md`;
- hook runner:
  `governance/compat/run_local_governance_hook_chain.py`;
- focused test:
  `governance/compat/test_run_local_governance_hook_chain.py`.

Result: `reviewer-fast` now runs 12 checks and includes
`rescan intelligence hardening`. Focused unittest passed. Reviewer-fast passed.
Full pre-commit governance chain passed.

Artifacts:

- roadmap:
  `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T1_DICH_TAI_LIEU_EXTRACTION_PATTERN_ABSORPTION_FOR_CLAUDE_2026-06-12.md`;
- source map:
  `docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md`;
- completion:
  `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md`.

Result:

- external source pinned to
  `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`;
- 1140 tracked files reconciled;
- current CVF owner surfaces were distinguished from new candidates;
- `DocumentScanSignals` and `ScanRouteDecision` were accepted only as
  deterministic EXA-T2 contract candidates;
- no external code, dependency, OCR runtime, provider call, Policy_Local
  mutation, or readiness claim was authorized.

Governance learning:

- `reviewer-fast` did not run the rescan intelligence checker;
- the missing rescan section appeared only at pre-commit;
- this is a phase-gate placement gap scheduled before EXA-T2 dispatch.

EXA-T2 scan signal and route decision contracts are `DISPATCHED` at commit
`5ad40259` from base `8376a31a`.

Artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_2026-06-12.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`.

Verification: reviewer-fast PASS 12/12; pre-dispatch autorun PASS; full
pre-commit governance chain PASS 37/37.

Worker boundary: Claude `WORKER_MUST_NOT_COMMIT`.

Result: EXA-T2 is authorized for deterministic `DocumentScanSignals` and
`ScanRouteDecision` contracts inside the CVF extraction foundation only. It
must reuse the current extraction quality, OCR language mapping,
storage-boundary, and scan-outcome-report owners.

## Latest Work / Changes

- Reviewed and corrected the EXA-T1 external corpus/source map.
- Closed EXA-T1 as bounded pattern absorption at material commit `6db11aed`.
- Reconciled accepted candidates against existing CVF extraction owners.
- Rotated V17 into the handoff archive because it reached 900 lines.
- Kept Policy_Local, OCR/provider execution, and readiness claims parked.
- Dispatched EXA-T2 at commit `5ad40259` with source-verified GC-018 and work
  order.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: perform the mandatory EXA-T1 closure
continuity sync and rotate the active handoff without changing governance
semantics.

Protected paths:

- `AGENTS.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: the operator requested external scan-layer knowledge
absorption before Policy_Local and returned the EXA-T1 worker packet for Codex
review. The mandatory closure-quality and governed-file maintainability rules
require synchronized front doors and handoff rotation.

Rollback boundary: revert only the V17-to-V18 routing changes and matching
EXA-T1 continuity markers if the rotation is incorrect. Do not revert the
material review commit `6db11aed` or unrelated history.

## Next Allowed Move

1. Claude executes EXA-T2 under `WORKER_MUST_NOT_COMMIT` from dispatch commit
   `5ad40259`.
2. Claude returns uncommitted source/test/registry artifacts and worker return
   packet for Codex review.
3. Keep Policy_Local as the downstream real use case after EXA-T2 foundation
   closure.

EXA-T2 must reuse the existing extraction quality, OCR language mapping,
storage-boundary, and scan-outcome-report owner surfaces. It must not create a
parallel quality/reporting system, invoke OCR/providers, import external code,
install dependencies, mutate Policy_Local, activate EC, change retrieval, or
claim readiness.

LHW24 remains the latest closed numbered LHW wave in the state registry.

## Parked Checkpoints

- Policy_Local integration: parked pending EXA-T2 foundation closure and fresh
  authorization.
- EC activation/retrieval: parked under existing metadata/operator evidence
  conditions.
- LPCI2-T12: forbidden until the separate EC-02 evidence path resolves on or
  after 2026-07-01 and eligibility is re-evaluated.
- DEP2 next-auth migration: `HARD_BLOCKED`.
- external receipt-anchor selection:
  `PARKED_PENDING_OPERATOR_DECISION`.
- live Redis proof: `PARKED_PENDING_CREDENTIALS`.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. `AGENT_HANDOFF_V18_2026-06-12.md`
5. Mandatory standards named in `AGENTS.md`

## Claim Boundary

This handoff is a routing and continuity artifact. It does not prove runtime
behavior, OCR quality, provider behavior, Policy_Local readiness, public
readiness, production readiness, hidden memory transfer, or autonomous
mutation.
