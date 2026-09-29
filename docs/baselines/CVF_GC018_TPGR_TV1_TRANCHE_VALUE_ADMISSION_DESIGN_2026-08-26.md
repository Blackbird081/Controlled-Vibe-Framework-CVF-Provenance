# CVF GC-018 Baseline - TPGR-TV1 Tranche Value Admission Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: TPGR-TV1

Dispatch base head: `85a2e5803604ee8cc5f487868133215dd83a3b0e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: current orchestrator/reviewer

Worker target: bounded documentation-only design worker

providerExecutionAuthority: FORBIDDEN

## Purpose

Design the smallest additive TPGR control that decides whether a proposed
tranche should start or continue based on independent value, cost envelope,
consolidation opportunity, and a hard stop/successor cap, while preserving the
risk-required governance floor.

## Scope

Read the current TPGR and review-cost owners plus accepted R11, TPGR-R8, and
RFR closure evidence. Create exactly one assessment and one worker return. Do
not edit a standard, template, checker, router, registry, roadmap, or runtime.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| operator foundational-learning authorization | operator messages on 2026-08-26 | ACCEPT |
| RFR terminal closure | `docs/reviews/CVF_RFR_FINAL_RECONCILIATION_AND_ROADMAP_CLOSURE_2026-08-26.md`; material `20bbb071c` | ACCEPT |
| R11 learning | accepted return at `820b677d8` | ACCEPT |
| TPGR-R8 hold | accepted material `859f851ac` | ACCEPT_AND_PRESERVE |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-TV1 --title "Tranche Value Admission Design" --date 2026-08-26 --base 85a2e5803604ee8cc5f487868133215dd83a3b0e --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus documentation design specialization |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | existing-owner boundary, design fields, successor cap and R8 hold interlock |
| checkerReadAheadConfirmation | dispatch, scaffold, source-verification and task-route checkers read |
| docOnlyNewFields | tranche-value record; consolidation key; successor cap |
| claimBoundary | dispatch baseline only; no implementation claim |

## Decision / Baseline / Proposed Tranche

Decision: dispatch TV1 only. Baseline: TPGR routes minimum governance by risk,
and review-cost control limits diminishing review after execution begins, but
neither is the canonical pre-dispatch owner for marginal tranche value.
Proposed tranche: decide the additive owner/schema/algorithm, hostile cases,
rollout, rollback, and exact optional TV2 manifest without implementation.

## Required Design Outcomes

The design must preserve the governing principle, define the four exact
decisions, cover remediation first, distinguish absorption and app/project
delivery, bind evidence labels and cost envelopes, define consolidation and
successor caps, and state when P0/P1 seriousness overrides economic
uncertainty without weakening governance.

## Evidence / Verification

Evidence comprises the five governed sources below, recomputed hashes in the
paired work order, clean/collision checks, ADIF disclosure, task-route shadow
result, pre-dispatch gates, and later exact-manifest worker/reviewer proof. No
provider, live, or runtime evidence is needed for this design.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| risk routing owner exists | GOVERNANCE_RULE | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Purpose | task governance route | TPGR standard | ACCEPT |
| diminishing-return owner exists | GOVERNANCE_RULE | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | applicability | review-cost control | review-cost standard | ACCEPT |
| pre-dispatch value gap and fields are documented | REVIEW_EVIDENCE | `docs/reviews/CVF_EAFR_R11_FINAL_RECONCILIATION_TRANCHE_VALUE_AND_RFR_DECISION_WORKER_RETURN_2026-08-26.md` | tranche-value learning | value record fields | accepted R11 return | ACCEPT |
| selective execution remains held | REVIEW_EVIDENCE | `docs/assessments/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md` | Final Disposition | P0/P1 decision | accepted R8 assessment | ACCEPT |
| no-value continuation should stop | REVIEW_EVIDENCE | `docs/reviews/CVF_RFR_FINAL_RECONCILIATION_AND_ROADMAP_CLOSURE_2026-08-26.md` | RFR-FR3 | stop disposition | RFR final review | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch status; exact paths; no-commit terms; Source Verification Block; trace/delta/public/claim blocks |
| gateRunPurpose | confirm source-verified packet shape before worker handoff |
| claimBoundary | checker conformance does not approve an implementation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated. Disclosed defectIds: ADIF-0001,
ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028,
ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: bounded named CVF sources; no corpus or external
repository absorption is claimed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - exact named governance sources only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; no public artifact or sync receipt exists.

## Claim Boundary

This baseline authorizes exactly two uncommitted TV1 documentation outputs. It
does not authorize TV2, owner edits, enforcement, selective routing, provider
use, absorption, project execution, deployment, public sync, or push.
