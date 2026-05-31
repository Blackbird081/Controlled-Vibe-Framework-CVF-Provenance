# CVF Fast Lane Audit — WD1 TruthScore Weighting Doctrine

Memory class: REVIEW_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.truthScoreWeightingDoctrine.wd1.v1`

GC-018: `docs/baselines/CVF_GC018_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_2026-05-31.md`

Risk class: R1 (additive doctrine function, no route.ts change, no live execution)

---

## Purpose

Fast Lane audit for WD1 TruthScore Weighting Doctrine. Establishes canonical
equal-weight scoring (25/25/25/25) and a confidence gate (≥0.7) that lifts
`isProvisional=true` → `isProvisional=false`. Derived from LP-LP1+LP-LP2
calibration (7 ALLOW sessions, confidence=0.7, TruthScore STRONG).

## Target / Source Under Review

- New: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truthscore-weighting-doctrine.ts`
- Modified: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` (+12 lines re-export)
- Tests: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/truthscore-weighting-doctrine.test.ts`

## Scope / Methodology

Fast Lane (R1). Additive doctrine function wrapping `TruthScoreContract`. No live
calls required. No route.ts change. Confidence gate derived from LP-LP2 evidence.

## Findings / Position

| Gate | Result |
| --- | --- |
| DOCTRINE_APPLIED when confidence ≥ 0.7 (7+ insights) | PASS |
| CONFIDENCE_GATE_NOT_MET when confidence < 0.7 | PASS |
| isProvisional=false only when gate met | PASS |
| isProvisional=true preserved when gate not met | PASS |
| Exact boundary: 7 insights → confidence=0.7 → APPLIED | PASS |
| Just below: 6 insights → confidence=0.6 → NOT_MET | PASS |
| runtimeScoringAuthorized=false always | PASS |
| compositeScore=86 (STRONG) for 7 ACCEPT/HEALTHY sessions | PASS |
| WEIGHTING_DOCTRINE_WEIGHTS total = 100 | PASS |
| TypeScript check: PASS | PASS |
| Tests: 1677/1677 PASS (70 files, +12 WD1) | PASS |
| GC-023: truthscore-weighting-doctrine.ts (~110 lines, limit 1000) | PASS |
| No route.ts change | PASS |

Fast Lane verdict: **PASS**

## Risk / Corrective Action

No violations. `applyWeightingDoctrine()` confirms the existing TruthScoreContract
dimension scoring as canonical — it does not change the scoring math, only codifies
it as doctrine and lifts the provisional flag when confidence is met.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| isProvisional=true lifted after confidence=0.7 | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | WD1 codifies doctrine and lifts provisional gate | HANDLED |
| Runtime Truth Model scoring still absent | `RULE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Separate tranche to wire doctrine into route.ts | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A | No live execution in this tranche | N/A |

## Claim Boundary

WD1 establishes the weighting doctrine at advisory level. `isProvisional=false` is
now achievable when confidence ≥ 0.7. No runtime scoring activated in route.ts.
