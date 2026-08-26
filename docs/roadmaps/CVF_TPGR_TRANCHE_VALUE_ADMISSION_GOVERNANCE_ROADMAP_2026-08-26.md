# CVF TPGR Tranche Value Admission Governance Roadmap

Memory class: governed-roadmap

Status: CLOSED_PASS_BOUNDED

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

## Tranche Successor Authority

```json
{
  "schemaVersion": "cvf.trancheSuccessorAuthority.v1",
  "roadmapId": "TPGR-TV",
  "declaredCap": 3,
  "authorizedOrdinals": [1, 2, 3],
  "currentAuthorizedOrdinal": 3,
  "noTv4": true,
  "authorityDisposition": "TV3_COMPLETED_ROADMAP_CLOSED_NO_SUCCESSOR"
}
```

This committed roadmap block is the authority source for TV3 cap and ordinal
validation. A candidate record may reference it but may not redefine it. TV3
is the final authorized ordinal; the array defines the hard ceiling and no TV4
or implicit successor exists.

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

TV1 is independently accepted at `5084910ce`; TV2 is independently accepted
with bounded reviewer repairs at `227f3d950`. TV3 is independently accepted
with one bounded evidence-label repair at material commit `3b3f944ff`. Its two
comparisons both match their accepted historical outcomes with zero observed
false stops and zero observed false continues. The terminal disposition is
`CLOSE_ROADMAP_BOUNDED`. No TV4 exists.

## Terminal Closure

Disposition: `CLOSE_ROADMAP_BOUNDED`.

The terminal worker return is
`docs/reviews/CVF_TPGR_TV3_TERMINAL_TWO_COMPARISON_PILOT_WORKER_RETURN_2026-08-26.md`,
materially committed at `3b3f944ff110245d91502c8e21e65b1b88faabe3`
with SHA-256
`c8faae810c7a9ca93f7c8747c61172706e488cf54c93fa06308452967bc3dd66`.
Independent review corrected C1 from `OBSERVED` to `HISTORICAL_BOUNDED`
because EAFR-R12 had already repaired the current source, then reproduced the
same `CONSOLIDATE` result. C2 remains comparison-only and activates no
absorption, app, or project class. Focused tests passed 43/43,
worker-return/reviewer-fast passed 66/66, material pre-commit passed 87/87,
and provider/live call count was zero.

The roadmap delivered its bounded design, shadow implementation, and terminal
two-case calibration. Further remediation findings require a separately
justified new roadmap; they cannot be appended as TV4.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A with reason: immutable terminal dispatch evidence is not mutated in the roadmap-only closure batch | its one-return execution contract completed at material `3b3f944ff` | N/A with reason: roadmap-only closure ownership |
| Completion or reviewer artifact | `docs/reviews/CVF_TPGR_TV3_TERMINAL_TWO_COMPARISON_PILOT_WORKER_RETURN_2026-08-26.md` | Independent Reviewer Addendum: `REVIEWER_ACCEPTED_WITH_BOUNDED_REPAIR` | PASS |
| Roadmap state | this roadmap | top-level `Status: CLOSED_PASS_BOUNDED` | PASS |
| Terminal worker/reviewer artifact | `docs/reviews/CVF_TPGR_TV3_TERMINAL_TWO_COMPARISON_PILOT_WORKER_RETURN_2026-08-26.md` | material `3b3f944ff`; SHA-256 `c8faae810c7a9ca93f7c8747c61172706e488cf54c93fa06308452967bc3dd66` | PASS |
| Comparison contract | terminal worker/reviewer artifact | exactly C1 remediation and C2 absorption/project boundary; both `MATCH` | PASS |
| Error counts | terminal worker/reviewer artifact comparison table | false-stop 0; false-continue 0 | PASS |
| Hard cap | this roadmap `Tranche Successor Authority` block | ordinal 3 of cap 3; `noTv4: true` | PASS |
| External effects | terminal worker/reviewer artifact command and claim evidence | zero provider/live/network/store/public/deploy effects | PASS |
| Registry JSON | N/A with reason: TV3 creates or changes no registry | exact one-file material commit `3b3f944ff` contains only the reviewer-accepted return | PASS |
| Registry Markdown | N/A with reason: TV3 creates or changes no registry | exact one-file material commit `3b3f944ff` contains only the reviewer-accepted return | PASS |
| External evidence digest | N/A with reason: no external input was introduced | eight pinned committed local-input SHA-256 values independently matched | N/A with reason: no external artifact |
| System loop interlock | this roadmap hard cap and claim boundary | ordinal 3 of cap 3; TV4 and every external-effect lane remain forbidden | PASS |
| Session continuity | active bootstrap, front door, state sources/aggregate and handoff | separate post-closure continuity batch required | N/A with reason: separate post-closure batch |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| terminal disposition | exactly `CLOSE_ROADMAP_BOUNDED` or `PARK_EVIDENCE_COLLECTION` | `CLOSE_ROADMAP_BOUNDED` | PASS |
| comparison count | exactly two pinned comparisons | C1 remediation plus C2 absorption/project boundary | PASS |
| false-decision counts | false-stop 0 and false-continue 0 | 0 and 0 | PASS |
| evaluator receipt | verified authority and non-authoritative shadow result | committed cap 3/ordinal 3; C1 `CONSOLIDATE`; authoritative flag false | PASS |
| class activation | none for absorption/app/project | C2 documentary mapping only | PASS |
| external effects | zero | zero provider/live/network/store/public/deploy calls or writes | PASS |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO; the zero-call statement is execution evidence, not a claim that provider runtime or registries are absent |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | CURRENT_SOURCE_BOUNDARY_READ |
| currentOwnerAccounting | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` exist and remain outside this documentation-only closure |
| reason | TV3 compares committed governance decisions and makes no runtime behavior, provider-routing, or production-readiness claim |
| requiredFutureAction | any future runtime/provider behavior claim requires separate authority and the mandatory real-provider live proof |

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

This closed roadmap records the terminal TV3 comparison-only pass. It does not
reduce mandatory governance, activate selective execution, resume TPGR-R9,
modify implementation owners, authorize any external effect, or authorize a
TV4 or implicit successor.
