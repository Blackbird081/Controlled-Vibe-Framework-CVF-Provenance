# CVF GC-018 - SOT3-RCS-T1 Review Cost Systemization

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Baseline ID: SOT3-RCS-T1-GC018

## Purpose

Authorize one bounded implementation tranche that converts the machine-safe
part of ADIF-0026 into a provider-neutral review-cost evidence contract and a
forward-only shape checker without automating semantic value judgment.

## Target / Source

Primary sources are ADIF-0026, the accepted SOT3-RAP-T0 completion review at
`d394b6018`, the Guard Orientation reviewer-return row, and existing checker
and hook-catalog conventions.

## Scope / Methodology

Implement one reference standard, one deterministic checker with focused
tests, wire it into the three local governance hook catalogs, index the
standard, and return without committing.

## Baseline Decision / Proposed Tranche

Release one `WORKER_MUST_NOT_COMMIT` implementation tranche for the exact
eight-path manifest below. Semantic review scoring remains rejected.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id SOT3-RCS-T1 --title "Review Cost Systemization" --date 2026-07-12 --base db99f4ebd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | bounded governance-checker baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Authored source verification, telemetry boundary, protected paths, and dependency release from current sources. |
| checkerReadAheadConfirmation | structural, dispatch-quality, scaffold, core-guard, handoff, and file-size checkers |
| docOnlyNewFields | review-cost declaration and stop-disposition vocabulary |
| claimBoundary | baseline authoring only; no checker implementation proof |

## Authorization / Decision

Operator continued after accepted T0. T0 dependency release evidence is
`docs/reviews/CVF_SOT3_RAP_T0_COMPLETION_REVIEW_2026-07-12.md` at
`d394b6018`, disposition `REVIEWER_ACCEPTED_BOUNDED`.

Decision: machine-enforce telemetry shape and round-three escalation only.
Reviewer-owned classification of independent root cause, dependent finding,
incremental value, and criticality remains semantic judgment.

## Non-Goals

- no SOT3 runtime, schemas, tests, packages, or Catalog/GAP mutation;
- no provider/live call or token accounting integration;
- no automatic semantic scoring or forced stop of critical reviews;
- no public-sync, Web/UI, or session-state mutation by the worker.

## Planned Artifact Manifest

| # | Path class | Purpose |
|---|---|---|
| 1 | `docs/reference/review_cost_control/README.md` | stable family front door |
| 2 | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | canonical shape and stop contract |
| 3 | `governance/compat/check_review_cost_control.py` | forward-only deterministic checker |
| 4 | `governance/compat/test_check_review_cost_control.py` | focused positive/negative tests |
| 5 | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast wiring |
| 6 | `governance/compat/local_governance_hook_catalog_pre_commit.py` | pre-commit wiring |
| 7 | `governance/compat/local_governance_hook_catalog_pre_push.py` | pre-push wiring |
| 8 | `docs/reviews/CVF_SOT3_RCS_T1_WORKER_RETURN_2026-07-12.md` | no-commit execution evidence |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| ADIF telemetry fields and stop rules exist | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Remediation | `reviewRoundCount`; `REVIEW_COST_ESCALATION_REQUIRED` | ADIF-0026 reviewer guidance | ACCEPT |
| T0 dependency is accepted | VALUE_SET | `docs/reviews/CVF_SOT3_RAP_T0_COMPLETION_REVIEW_2026-07-12.md` | Gate Result | `REVIEWER_ACCEPTED_BOUNDED` | SOT3-RAP-T0 completion review | ACCEPT |
| reviewer-fast catalog owns reviewer checker commands | EXISTS | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | catalog declaration | `REVIEWER_FAST_CHECKS` | local reviewer-fast catalog | ACCEPT |
| pre-commit catalog owns commit checker commands | EXISTS | `governance/compat/local_governance_hook_catalog_pre_commit.py` | catalog declaration | `PRE_COMMIT_CHECKS` | local pre-commit catalog | ACCEPT |
| pre-push catalog owns push checker commands | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | catalog declaration | `PRE_PUSH_CHECKS` | local pre-push catalog | ACCEPT |
| worker-experience checker provides narrow forward-only precedent | RUNTIME_BEHAVIOR | `governance/compat/check_worker_experience_retrospective.py` | eligibility and validation functions | `is_eligible_worker_return`; `diagnose` | worker-experience checker | ACCEPT |

## Machine-Enforceable Boundary

| Control | Machine disposition |
|---|---|
| required telemetry field presence | ENFORCE |
| integer-or-explicit-unavailable value shape | ENFORCE |
| round three escalation token | ENFORCE |
| allowed stop-disposition vocabulary | ENFORCE |
| whether a root cause is truly independent | REVIEWER_JUDGMENT |
| whether value delta is substantively high | REVIEWER_JUDGMENT |
| whether a critical contradiction warrants continuation | REVIEWER_JUDGMENT |

## Fail Conditions

- checker guesses semantic value or automatically closes a review;
- applicability is bare-substring based and self-triggers on standards/work orders;
- existing unchanged historical reviews are reopened;
- hook catalogs are edited without tests and core-guard authorization;
- worker commits or touches paths outside the manifest.

## Verification / Evidence

Focused tests, checker fixture runs, reviewer-fast, pre-commit-compatible hook
catalog validation, full worker-return fast gate, exact diff/status, and no
commit evidence are required.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; Planned Artifact Manifest; Core Guard Self-Protection Authorization; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch shape before implementation |
| claimBoundary | dispatch gates do not prove checker correctness or semantic review value |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Direct mandatory source: ADIF-0026.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening.

## Claim Boundary

This baseline authorizes a narrow review-cost evidence-shape checker. It does
not authorize semantic reviewer replacement, live quota accounting, or SOT3
runtime implementation.
