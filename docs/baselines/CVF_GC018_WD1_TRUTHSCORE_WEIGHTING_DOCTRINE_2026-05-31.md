# CVF GC-018 Continuation Candidate
## WD1 — TruthScore Weighting Doctrine

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent advisory: LP-LP2 `cvf.learningPlaneLiveProof.lplp2.v1` (confidence=0.7, TruthScore STRONG)
Prerequisite: LP-LP1 + LP-LP2 — 7 live sessions, all ALLOW, confidence=0.7

---

## Purpose

Authorize WD1: establish the TruthScore Weighting Doctrine — a governed set of
weight constants and a `applyWeightingDoctrine()` function that lifts `isProvisional=true`
to `isProvisional=false` once calibration confidence meets the threshold.

Per 2026-04-12 decision section 3.7: "TruthScore deltas must remain provisional (no
fixed weighting doctrine) until LPF calibration is complete." LP-LP2 reached
confidence=0.7 with 7 ALLOW sessions → calibration is now sufficiently complete to
establish an initial weighting doctrine.

The doctrine codifies the existing 4-dimension scoring as the canonical weights,
adds a confidence gate (minimum 0.7 to lift provisional status), and provides an
`applyWeightingDoctrine()` function that returns a non-provisional `TruthScore`
when the gate is met.

## Scope / Target / Owner Boundary

Target: new `src/truthscore-weighting-doctrine.ts` in `CVF_LEARNING_PLANE_FOUNDATION`.
Owner: CVF learning plane / TruthScore weighting surface.
Boundary:
- New file only — no route.ts, no receipt-envelope, no persistence change
- Re-export in `src/index.ts`
- Tests in `tests/truthscore-weighting-doctrine.test.ts`
- `isProvisional` on output: `false` only when confidence ≥ 0.7 AND calibration complete
- `runtimeScoringAuthorized: false` always (advisory doctrine only)

## Source / Predecessor Evidence

- LP-LP2: `docs/assessments/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md` (confidence=0.7)
- TM1: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts`
- TruthScore contract: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth.score.contract.ts`
- 2026-04-12 decision s3.7: provisional until calibration complete

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED. Baseline: WD1 TruthScore Weighting Doctrine. Parent: LP-LP2.

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truthscore-weighting-doctrine.ts` — new file
- Re-export in `src/index.ts`
- Tests in `tests/truthscore-weighting-doctrine.test.ts`
- Fast Lane + completion review

## Evidence / Verification

- New file: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truthscore-weighting-doctrine.ts` — DELIVERED
- Tests: `tests/truthscore-weighting-doctrine.test.ts` — 12 tests, 1677/1677 PASS (70 files)
- Fast Lane: `docs/reviews/CVF_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_FAST_LANE_2026-05-31.md` — PASS
- Completion: `docs/reviews/CVF_WD1_TRUTHSCORE_WEIGHTING_DOCTRINE_COMPLETION_2026-05-31.md` — CLOSED_PASS_BOUNDED

## Authorization Boundary

- Contract: `cvf.truthScoreWeightingDoctrine.wd1.v1`
- Hard invariants: confidence gate ≥ 0.7 required to lift provisional; `runtimeScoringAuthorized: false` always; no route.ts change

## Claim Boundary

WD1 establishes the weighting doctrine at advisory level. It does not activate
runtime Truth Model scoring in route.ts or claim production readiness.

---

*Authorized: 2026-05-31 | Operator sign-off in-session*
