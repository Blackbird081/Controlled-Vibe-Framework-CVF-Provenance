# CVF Fast Lane Audit — TM1 Truth Model Calibration

Memory class: REVIEW_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.truthModelCalibration.tm1.v1`

GC-018: `docs/baselines/CVF_GC018_TM1_TRUTH_MODEL_CALIBRATION_2026-05-31.md`

Risk class: R1 (additive calibration function, reuses existing contracts, no execution path change)

---

## Purpose

Fast Lane audit for TM1 Truth Model Calibration — implements LHW17 T3 Step 6
("Truth Model calibration begins"). Wires APE-1 A1-A6 as pre-flight gate before
calibration; builds TruthModel + TruthScore from PatternInsights using existing
contracts. TruthScore always PROVISIONAL. Gates Step 7 (Reputation Model).

## Target / Source Under Review

- New: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts`
- Modified: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` (+13 lines re-export)
- Tests: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/truth-model-calibration.test.ts`
- Existing: `truth.model.contract.ts`, `truth.score.contract.ts`, `adaptation-policy-engine.ts`

## Scope / Methodology

Fast Lane (R1). `runCalibrationSession()` = APE-1 preflight → TruthModelContract.build() → TruthScoreContract.score(). Returns typed `CalibrationSessionResult`. No route.ts change, no receipt-envelope extension, no new persistence.

## Findings / Position

| Gate | Result |
| --- | --- |
| APE-1 BLOCK → BLOCK disposition, no model built, truthModel=null | PASS |
| APE-1 ADVISORY → ADVISORY disposition, model built, truthScore present | PASS |
| APE-1 PASS → PASS disposition, model + score built | PASS |
| `isProvisional: true` always | PASS |
| `runtimeCalibrationAuthorized: false` always | PASS |
| Empty insights → INSUFFICIENT TruthScore | PASS |
| Deterministic: same input + same now() → same scoreHash | PASS |
| TypeScript check: PASS | PASS |
| Tests: 1644/1644 PASS (67 files, +13 TM1 tests) | PASS |
| GC-023: truth-model-calibration.ts (~100 lines, limit 1000) | PASS |
| GC-023: index.ts (956 lines, limit 1000) | PASS |
| No route.ts change | PASS |
| No receipt-envelope extension | PASS |
| No new persistence layer | PASS |
| No fixed TruthScore weighting doctrine | PASS |

Fast Lane verdict: **PASS**

## Risk / Corrective Action

No violations. TruthScore is provisional — no weighting doctrine activated. Step 7
(Reputation Model) requires a separate governed tranche. BLOCK/ADVISORY from APE-1
are advisory signals; callers are responsible for surfacing to operator.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| LHW17 T3 Step 6 now implemented | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | TM1 closes Step 6 gate | HANDLED |
| TruthScore provisional — no weighting doctrine | `RULE_GAP` | `DOCUMENTATION_ONLY_LEARNING` | `RULE_EXISTS` | Weighting doctrine requires LPF calibration proof session | DEFERRED |
| Step 7 Reputation wiring absent | `MACHINE_GATE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Separate TM2/RM1 tranche required | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A | No runtime execution, no provider call | N/A |

## Claim Boundary

TM1 implements a governed calibration session function. It does not activate
Truth Model runtime scoring, wire Reputation routing, or claim production readiness.
