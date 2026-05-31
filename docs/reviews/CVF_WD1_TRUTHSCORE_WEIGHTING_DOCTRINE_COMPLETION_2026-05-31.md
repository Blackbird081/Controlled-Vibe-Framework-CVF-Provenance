# CVF WD1 — TruthScore Weighting Doctrine Completion

Memory class: COMPLETION_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.truthScoreWeightingDoctrine.wd1.v1`

GC-018: `docs/baselines/CVF_GC018_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_2026-05-31.md`

Fast Lane: `docs/reviews/CVF_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_FAST_LANE_2026-05-31.md`

---

## Purpose

Record completion of WD1 TruthScore Weighting Doctrine. Establishes canonical
equal-weight scoring and confidence gate (≥0.7) that lifts `isProvisional=true`
to `isProvisional=false`. Per 2026-04-12 decision s3.7 — calibration now complete.

## Target / Source Under Review

- New: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truthscore-weighting-doctrine.ts`
- Modified: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` (+12 lines)
- Tests: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/truthscore-weighting-doctrine.test.ts`

## Scope / Methodology

Fast Lane (R1). No live calls. No route.ts change. Doctrine from LP-LP2 calibration evidence.

## Findings / Position

| Gate | Result |
| --- | --- |
| DOCTRINE_APPLIED at confidence ≥ 0.7 | PASS |
| isProvisional=false when gate met | PASS |
| runtimeScoringAuthorized=false always | PASS |
| compositeScore=86/STRONG for 7-session model | PASS |
| Weights total = 100 (25×4) | PASS |
| TypeScript: PASS | PASS |
| Tests: 1677/1677 PASS (70 files, +12 WD1) | PASS |

## Risk / Corrective Action

No violations. Doctrine confirms existing scoring — no math change. Runtime wiring deferred.

## Deliverables

| Artifact | Status |
| --- | --- |
| `src/truthscore-weighting-doctrine.ts` — `applyWeightingDoctrine()` | DELIVERED |
| `src/index.ts` — re-export WD1 symbols | DELIVERED |
| `tests/truthscore-weighting-doctrine.test.ts` — 12 tests | DELIVERED |
| GC-018 baseline | DELIVERED |
| Fast Lane audit | DELIVERED |

## Doctrine Summary

```
WEIGHTING_DOCTRINE_VERSION:        cvf.truthScoreWeightingDoctrine.wd1.v1
WEIGHTING_DOCTRINE_CONFIDENCE_GATE: 0.7  (7+ calibration sessions)
WEIGHTING_DOCTRINE_WEIGHTS:
  confidence  → 25/100
  health      → 25/100
  trajectory  → 25/100
  pattern     → 25/100

applyWeightingDoctrine(model):
  confidence >= 0.7 → outcome=DOCTRINE_APPLIED, isProvisional=false
  confidence <  0.7 → outcome=CONFIDENCE_GATE_NOT_MET, isProvisional=true
  runtimeScoringAuthorized=false always
```

## LP Calibration Status — Final

```
LP-LP1:  confidence=0.1 — LHW17 T3 prerequisite SATISFIED
LP-LP2:  confidence=0.7 — TruthScore STRONG, gate eligible
WD1:     doctrine ESTABLISHED — isProvisional=false achievable at confidence ≥ 0.7
Next:    Runtime wiring tranche (separate GC-018) to activate scoring in route.ts
```

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| Weighting doctrine now established | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | WD1 lifts provisional gate | HANDLED |
| Runtime scoring not yet wired | `RULE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Separate tranche for route.ts integration | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A | No live execution | N/A |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY` — WD1 is a private provenance implementation tranche.

## Claim Boundary

WD1 establishes the weighting doctrine at advisory level. `isProvisional=false` is
now achievable. Runtime Truth Model scoring in route.ts requires a separate tranche.
