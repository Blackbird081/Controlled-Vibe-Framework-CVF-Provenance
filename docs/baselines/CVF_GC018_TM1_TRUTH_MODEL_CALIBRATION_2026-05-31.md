# CVF GC-018 Continuation Candidate
## TM1 — Truth Model Calibration (Step 6)

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent advisory: LHW17 T3 `cvf.learningPlaneTruthReputationAdvisory.lhw17.t3.v1` (Step 6)
Prerequisite gate: APE-1 `cvf.adaptationPolicyEngine.ape1.v1` (Step 5 — CLOSED_PASS_BOUNDED)

---

## Purpose

Authorize TM1: implement Truth Model Calibration as a governed calibration session function
in `CVF_LEARNING_PLANE_FOUNDATION`. This is LHW17 T3 Step 6 — "Truth Model calibration
begins." It gates Step 7 (Reputation Model advisory signal wired).

TM1 wires APE-1 A1-A6 policy checks as a pre-flight gate before any calibration cycle,
uses existing `TruthModelContract` + `TruthScoreContract` for scoring, and returns a
provisional `CalibrationSessionResult` with advisory disposition. No fixed TruthScore
weighting doctrine — provisional only per 2026-04-12 decision (section 3.7).

## Scope / Target / Owner Boundary

Target: new `src/truth-model-calibration.ts` in `CVF_LEARNING_PLANE_FOUNDATION`.
Owner: CVF learning plane / Truth Model calibration surface.
Boundary:
- New file only — no route.ts, no receipt-envelope extension, no persistence change
- Re-export in `src/index.ts`
- Tests in `tests/truth-model-calibration.test.ts`
- TruthScore remains PROVISIONAL (`isProvisional: true` always in this tranche)
- APE-1 gate must PASS before calibration proceeds
- `runtimeCalibrationAuthorized: false` on all results (advisory enforcement only)

## Source / Predecessor Evidence

- LHW17 T3 spec: `docs/reference/CVF_LHW17_T3_LEARNING_PLANE_TRUTH_REPUTATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- APE-1 gate: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/adaptation-policy-engine.ts`
- Truth score: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth.score.contract.ts`
- Truth model: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth.model.contract.ts`

---

## GC-018 Continuation Candidate

- Candidate ID: `gc018-tm1-truth-model-calibration-2026-05-31`
- Date: 2026-05-31
- Parent: LHW17 T3 Step 6 + APE-1 prerequisite
- Proposed scope: calibration session function + APE-1 gate integration + tests
- Continuation class: IMPLEMENTATION
- Quality-first decision: EXPAND_NOW — Step 5 (APE-1) closed; Step 6 is now unblocked
- Active-path impact: ADDITIVE — new file + re-export only
- Expected enforcement class: MACHINE_CHECK

### Depth Audit

- Risk reduction: 2 — closes Step 6 gate; enables Step 7 path
- Decision value: 2 — wires APE-1 A1-A6 as live pre-flight guard
- Machine enforceability: 2 — typed PASS/BLOCK/ADVISORY + provisional flag
- Operational efficiency: 2 — reuses existing contracts; zero new persistence
- Portfolio priority: 2 — operator-selected as next priority
- Total: 10/10
- Decision: **CONTINUE**

### Authorization Boundary

- Authorized now: **YES**
- Contract: `cvf.truthModelCalibration.tm1.v1`
- Hard invariants: no route.ts change; no receipt-envelope extension; `isProvisional: true` always; `runtimeCalibrationAuthorized: false` always; no fixed weighting doctrine

---

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.
Baseline: TM1 Truth Model Calibration. Parent: LHW17 T3 Step 6.

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts` — new file
- Re-export in `src/index.ts`
- Tests in `tests/truth-model-calibration.test.ts`
- Fast Lane audit + completion review

## Evidence / Verification

- New file: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts` — DELIVERED
- Tests: `tests/truth-model-calibration.test.ts` — 13 tests, 1644/1644 PASS (67 files)
- Fast Lane: `docs/reviews/CVF_TM1_TRUTH_MODEL_CALIBRATION_FAST_LANE_2026-05-31.md` — PASS
- Completion: `docs/reviews/CVF_TM1_TRUTH_MODEL_CALIBRATION_COMPLETION_2026-05-31.md` — CLOSED_PASS_BOUNDED

## Claim Boundary

TM1 implements a governed calibration session function. It does not activate
Truth Model runtime scoring, wire Reputation routing, change the execution path,
or claim production readiness. Step 7 (Reputation Model) requires a separate tranche.

---

*Authorized: 2026-05-31 | Operator sign-off in-session*
