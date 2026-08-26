# CVF TPGR Tranche Value Admission Governance Roadmap

Memory class: governed-roadmap

Status: ACTIVE_TV1_DISPATCH_READY

docType: roadmap

Date: 2026-08-26

Roadmap base head: `85a2e5803604ee8cc5f487868133215dd83a3b0e`

## Authorization / Decision

The operator authorized a new foundational roadmap that prevents agent time,
latency, token, and quota waste caused by low-value tranche proliferation.
This roadmap extends the existing TPGR owner; it creates no parallel framework.

## Purpose

Add a pre-dispatch and continuation-value decision to task-proportional
governance. Risk continues to set the minimum governance posture. Marginal
value decides whether a proposed tranche starts, consolidates, parks, or stops.

## Scope / Target / Owner Boundary

| Lane | Existing owner | Bounded target |
| --- | --- | --- |
| TV1 | TPGR standard plus review-cost standard | documentation-only decision design and exact additive manifest |
| TV2 | same owners and their existing checker/router | minimal shadow-only implementation after independent TV1 acceptance |
| TV3 | same owners | bounded pilot on remediation plus one absorption/project case, followed by terminal disposition |

The first application scope is finding/remediation work. Absorption and
app/project delivery receive only one design/pilot comparison in TV3; they do
not open separate roadmaps here.

## Non-Goals

No selective gate execution, legacy suppression, P0 allowlist activation,
runtime/provider/live call, source-repository absorption, project build,
deployment, public sync, or automatic budget enforcement. TPGR-R8 remains
`HOLD_EMPTY_P0_ALLOWLIST_PENDING_OBSERVED_DUAL_RUN_EVIDENCE`.

## Governing Principle

`risk determines minimum governance; marginal value determines whether work starts or continues.`

Cost reduction can select `CONSOLIDATE`, `PARK_LOW_VALUE`, or
`STOP_NO_INCREMENTAL_VALUE`; it can never waive a risk-required guard.

## Work Plan And Successor Cap

| Order | Entry criteria | Required proof | Exit state |
| --- | --- | --- | --- |
| TV1 | operator authorization and R11 learning | source-verified schema, owner mapping, decision algorithm, hostile cases, migration/rollback and exact TV2 manifest | one accepted design disposition |
| TV2 | TV1 independently accepted with `PROCEED_TO_TV2_SHADOW_IMPLEMENTATION` | minimal standard/template/router/checker changes; shadow result only; legacy bundle unchanged | implement accepted shape or stop |
| TV3 | TV2 independently accepted and pilot evidence is worth its cost | two bounded comparisons, false-stop/false-continue analysis and terminal economics | close roadmap or explicitly park evidence collection |

Hard successor cap: three tranches total (`TV1`-`TV3`). No TV4 is authorized.
Any extra need must be independently justified as a new roadmap, not appended.

## Mandatory Admission Record

TV1 must design at least these fields: outcome/consumer, severity, evidence
state, independent root cause, marginal value, time/latency/token/quota
envelope, consolidation key, stop condition, successor cap, decision reason,
reviewer identity, and expiry/freshness.

Allowed decisions are exactly:

- `CONTINUE_HIGH_VALUE`
- `CONSOLIDATE`
- `PARK_LOW_VALUE`
- `STOP_NO_INCREMENTAL_VALUE`

Unknown or unsupported value cannot become `CONTINUE_HIGH_VALUE` merely because
work is available. P0/P1 risk routing and tranche-value admission remain
orthogonal decisions.

## Stop Conditions

Stop the roadmap early when the next tranche lacks an independent root cause,
has no named consumer/outcome, duplicates an existing owner, cannot state a
measurable stop condition, exceeds its approved envelope without new P0/P1
evidence, or yields only documentation churn. A serious new P0/P1 remains
eligible for a consolidated repair even when its economic return is unknown.

## Dispatch Boundary

Only TV1 documentation design is dispatched. TV2 and TV3 require independent
acceptance of their predecessor and an explicit value disposition. No
implementation path is writable under TV1.

## Acceptance Criteria

- one existing-owner additive design, not a parallel governance framework;
- risk floor can never be weakened by a value decision;
- remediation, absorption, and app/project applicability are separated;
- deterministic decisions, hostile cases, expiry, override and appeal path;
- explicit time/latency/token/quota evidence labels (`OBSERVED`,
  `HISTORICAL_BOUNDED`, `PROJECTED`, `UNKNOWN`);
- maximum three tranches and zero implicit successors;
- unchanged full legacy bundle and TPGR-R8 hold;
- no external effect.

## Verification / Evidence

Each tranche uses source read-ahead, exact manifest reconciliation, worker
no-commit proof, independent review, relevant fast/pre-commit gates, and a
separate continuity sync. TV2/TV3 cannot cite projected savings as observed.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| TPGR already owns risk-proportional routing | GOVERNANCE_RULE | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | Purpose and classification model | task governance route | TPGR standard | ACCEPT |
| review cost owner begins after work/review starts | GOVERNANCE_RULE | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | applicability and stop control | review-cost telemetry | review-cost standard | ACCEPT |
| pre-dispatch marginal-value gap is source-identified | REVIEW_EVIDENCE | `docs/reviews/CVF_EAFR_R11_FINAL_RECONCILIATION_TRANCHE_VALUE_AND_RFR_DECISION_WORKER_RETURN_2026-08-26.md` | Tranche Admission / Continuation Value Learning | recommended field set | accepted R11 return | ACCEPT |
| TPGR selective route remains held | REVIEW_EVIDENCE | `docs/assessments/CVF_TPGR_R8_P0_P1_ALLOWLIST_DECISION_DESIGN_2026-08-23.md` | Final Disposition | P0 0/6; P1 6/6 | accepted R8 design | ACCEPT |
| RFR demonstrates stop on no incremental value | REVIEW_EVIDENCE | `docs/reviews/CVF_RFR_FINAL_RECONCILIATION_AND_ROADMAP_CLOSURE_2026-08-26.md` | Findings / Position | RFR-FR3 | final RFR review | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_task_governance_route.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | roadmap status; Source Verification Block; Work Plan; successor cap; Stop Conditions; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-led roadmap and dispatch shape, not first discovery |
| claimBoundary | checker conformance does not implement tranche admission |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated. Dispatch impact: exact scope, checker
read-ahead, honest evidence labels, no-commit ownership, reusable-rule routing,
and independent review are mandatory. The paired work order records IDs.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundational governance roadmap; no public-sync receipt exists.

## Claim Boundary

This roadmap authorizes TV1 documentation design only. It does not implement a
tranche admission gate, reduce mandatory governance, activate selective
execution, resume TPGR-R9, or authorize any external effect.
