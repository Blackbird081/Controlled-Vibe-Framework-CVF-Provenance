# CVF MSEA R84 Lean Governance Follow-Through Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-07-10

Owner: Codex

## Authorization / Decision

The operator authorized the bounded Lean Governance Follow-Through after R83
closure. R84 converts one accepted R72 finding into behavior and stops after
one compact contract plus one checker lifecycle disposition.

## Purpose

Reduce recurring documentation-only worker-return format tax without weakening
source verification, command evidence, no-commit separation, claim boundaries,
or public/private repository controls.

## Scope / Methodology

R84 implements and proves `WORKER_RETURN_FAST_DOC_V1` for dispatch-authorized
`FAST_DOC_LANE` returns. It consolidates three always-not-applicable control
sections into one bounded disposition block and keeps the worker-return quality
checker blocking for all protected evidence.

## Non-Goals

R84 does not simplify every governed artifact, retire a checker, change hook
severity, or create a general risk router. It addresses one measured format
tax and then stops.

## Findings / Position

R72C provides source-backed eligibility and protected-control rules. R72B
classifies the worker-return quality checker as a consolidation candidate for
conditional sections and as blocking for evidence-bearing sections. This is
enough for one implementation pilot; it is not authority for global checker
demotion.

## Risk / Corrective Action

The main risk is worker self-selection into a lighter lane. The checker must
require explicit dispatch profile evidence. Any design that allows public-sync,
live, runtime, checker-authoring, or protected-control work into the lane fails
closed.

## Design Control Gate

Compact routing must fail closed unless the dispatch names the exact profile,
scope classification, no-commit mode, and prohibited-surface declarations.
Protected evidence remains identical to the full profile.

## Tranches

| Tranche | Objective | Exit evidence | Status |
|---|---|---|---|
| R84A | Ratify compact profile and eligibility | source-backed standard and dispatch contract | PASS |
| R84B | Implement checker and scaffold routing | focused tests for full and compact profiles | PASS |
| R84C | Measure value and regress protected controls | A/B shape metric and negative eligibility tests | PASS |
| R84D | Close or revert the pilot | bounded completion review and session sync | PASS |

## Work Plan

Commit the dispatch, implement the profile and tests, run A/B and negative
proof, then either close the bounded pilot or revert it under the fail
conditions.

## Acceptance Criteria

- compact eligibility is selected by dispatch, never by the worker alone;
- the three conditional headings may be replaced by one compact block;
- source/command evidence, trace, changed-set, claim-boundary, no-commit, and
  public-export requirements remain blocking;
- the full profile remains backward compatible;
- compact conditional-section format tax falls by at least 30 percent;
- no new checker, hook, public-sync artifact, or runtime behavior is added;
- R73F checker retirement remains parked.

## Verification / Evidence

Evidence consists of focused unit tests, generated full and compact scaffolds,
heading/line counts for the conditional controls, negative eligibility cases,
full autorun phases, git diffs, and exact commit ranges.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Status: INTEGRATED_EXECUTION_AUTHORIZED`; `FAST_DOC_LANE`; `WORKER_RETURN_FAST_DOC_V1`; `WORKER_MUST_NOT_COMMIT honored` |
| gateRunPurpose | confirmation before bounded R84 execution |
| claimBoundary | worker-return authoring and validation only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R84 is a private governance-control calibration; no public-sync
artifact is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Compact eligibility | `governance/compat/test_check_work_order_dispatch_quality_worker_return_contract.py` | focused unit-test PASS | PASS |
| Full compatibility | `governance/compat/fixtures/woas_r3_worker_return_skeleton_golden.md` | golden and legacy tests PASS | PASS |
| Protected controls | `governance/compat/test_check_worker_return_quality_gate.py` | negative cases PASS | PASS |
| Value threshold | completion review | 66.7 percent headings; 86.4 percent conditional lines | PASS |
| Completion review | `docs/reviews/CVF_MSEA_R84_LEAN_GOVERNANCE_FOLLOW_THROUGH_COMPLETION_REVIEW_2026-07-10.md` | `Status: REVIEWER_ACCEPTED_BOUNDED` | PASS |
| Work order status | N/A with reason: the dispatch packet remains immutable authority. | accepted completion review carries final execution disposition | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R84_LEAN_GOVERNANCE_FOLLOW_THROUGH_COMPLETION_REVIEW_2026-07-10.md` | `Status: REVIEWER_ACCEPTED_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generator drift check passes; registry content remains unchanged | PASS |
| Registry Markdown | `docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md` | GCI-017 is ACTIVE with consolidated pilot criteria | PASS |
| External evidence digest | N/A with reason: no external evidence is consumed. | local source and command evidence only | N/A with reason |
| System loop interlock | N/A with reason: R84 changes no runtime or system loop. | no interlock path in changed set | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md` | session-sync follows the committed material closure as a separate commit | N/A with reason |

## Claim Boundary

R84 does not authorize global checker demotion, checker retirement, runtime,
provider, live proof, public-sync, or product-use-case work.
