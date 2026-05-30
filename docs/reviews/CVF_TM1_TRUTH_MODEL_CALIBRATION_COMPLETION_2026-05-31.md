# CVF TM1 — Truth Model Calibration Completion

Memory class: COMPLETION_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.truthModelCalibration.tm1.v1`

GC-018: `docs/baselines/CVF_GC018_TM1_TRUTH_MODEL_CALIBRATION_2026-05-31.md`

Fast Lane: `docs/reviews/CVF_TM1_TRUTH_MODEL_CALIBRATION_FAST_LANE_2026-05-31.md`

---

## Purpose

Record completion of TM1 Truth Model Calibration. Implements LHW17 T3 Step 6
("Truth Model calibration begins"). Wires APE-1 A1-A6 as pre-flight gate; builds
provisional TruthModel + TruthScore from PatternInsights. Gates Step 7 (Reputation Model).

## Target / Source Under Review

- New: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts`
- Modified: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` (+13 lines re-export)
- Tests: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/truth-model-calibration.test.ts`

## Scope / Methodology

Fast Lane (R1). Additive calibration session function. No route.ts change. No new persistence.

## Findings / Position

| Gate | Result |
| --- | --- |
| BLOCK on APE-1 preflight failure; truthModel=null | PASS |
| ADVISORY when APE-1 advisory-only; model+score present | PASS |
| PASS when all APE-1 checks pass | PASS |
| `isProvisional: true` always | PASS |
| `runtimeCalibrationAuthorized: false` always | PASS |
| Empty insights → INSUFFICIENT score (not error) | PASS |
| Deterministic hash with injected clock | PASS |
| TypeScript: PASS | PASS |
| Tests: 1644/1644 PASS (67 files, +13 TM1 tests) | PASS |

## Risk / Corrective Action

No violations. TruthScore provisional only — no weighting doctrine. Step 7 requires separate tranche.

## Deliverables

| Artifact | Status |
| --- | --- |
| `src/truth-model-calibration.ts` — `runCalibrationSession()` | DELIVERED |
| `src/index.ts` — re-export TM1 symbols | DELIVERED |
| `tests/truth-model-calibration.test.ts` — 13 tests | DELIVERED |
| GC-018 baseline | DELIVERED |
| Fast Lane audit | DELIVERED |

## Behaviour Summary

`runCalibrationSession(input)`:
1. Runs `checkAdaptationPolicy(input.adaptationPolicyInput)` — APE-1 A1-A6 preflight
2. If BLOCK → returns `{ disposition: "BLOCK", phase: "PREFLIGHT_CHECK", truthModel: null, truthScore: null }`
3. If PASS/ADVISORY → builds `TruthModel` via `TruthModelContract.build(insights)`
4. Scores via `TruthScoreContract.score(model)` → provisional `TruthScore`
5. Returns `{ disposition, phase: "COMPLETE", truthModel, truthScore, isProvisional: true }`

## LHW17 T3 Activation Order Status

```
Step 1-4: CLOSED (LHW17 T3 advisory + prior tranches)
Step 5:   APE-1 CLOSED — Adaptation Policy implemented
Step 6:   THIS TRANCHE — Truth Model calibration begins ← TM1 CLOSED
Step 7:   FUTURE — Reputation Model advisory signal wired
Step 8:   FUTURE — Simulation Environment validated
```

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| LHW17 T3 Step 6 now implemented | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | TM1 closes Step 6 | HANDLED |
| TruthScore weighting doctrine absent | `RULE_GAP` | `DOCUMENTATION_ONLY_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Requires LPF live-proof calibration session | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A | No runtime execution | N/A |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY` — TM1 is a private provenance implementation tranche.

## Claim Boundary

TM1 implements a governed calibration session. It does not activate Truth Model runtime
scoring, Reputation routing, or claim production readiness. Steps 7-8 require separate tranches.
