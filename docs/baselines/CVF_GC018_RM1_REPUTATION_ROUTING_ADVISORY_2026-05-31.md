# CVF GC-018 Continuation Candidate
## RM1 — Reputation Routing Advisory (Step 7)

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent advisory: LHW17 T3 `cvf.learningPlaneTruthReputationAdvisory.lhw17.t3.v1` (Step 7)
Prerequisite gate: TM1 `cvf.truthModelCalibration.tm1.v1` (Step 6 — CLOSED_PASS_BOUNDED)

---

## Purpose

Authorize RM1: implement Reputation Routing Advisory as a governed advisory
function in `CVF_LEARNING_PLANE_FOUNDATION`. This is LHW17 T3 Step 7 —
"Reputation Model advisory signal wired." It gates Step 8 (Simulation Environment).

Per LHW17 T3: reputation score feeds into `resolveProviderForRole()` as an advisory
signal — not a hard gate — until calibration is proven stable. Reputation degradation
triggers an R2-level governance review, not an automatic capability reduction.
`CVF_ECO_v3.1_REPUTATION` is the owner surface (already exists as `ReputationSignalContract`).

## Scope / Target / Owner Boundary

Target: new `src/reputation-routing-advisory.ts` in `CVF_LEARNING_PLANE_FOUNDATION`.
Owner: CVF learning plane / reputation routing surface.
Boundary:
- New file only — no CLI change, no route.ts, no receipt-envelope extension
- Re-export in `src/index.ts`
- Tests in `tests/reputation-routing-advisory.test.ts`
- Returns typed `RoutingAdvisoryResult` with `PROCEED/CAUTION/DEFER` + rationale
- `UNTRUSTED` class → `DEFER` (advisory signal to prefer alternative provider or escalate)
- `runtimeRoutingAuthorized: false` always (advisory only, not hard gate)

## Source / Predecessor Evidence

- LHW17 T3 spec: `docs/reference/archive/CVF_LHW17_T3_LEARNING_PLANE_TRUTH_REPUTATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- TM1: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts`
- Reputation contract: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/reputation.signal.contract.ts`

---

## GC-018 Continuation Candidate

- Candidate ID: `gc018-rm1-reputation-routing-advisory-2026-05-31`
- Continuation class: IMPLEMENTATION
- Quality-first decision: EXPAND_NOW — Step 6 (TM1) closed; Step 7 is now unblocked
- Expected enforcement class: MACHINE_CHECK

### Authorization Boundary

- Authorized now: **YES**
- Contract: `cvf.reputationRoutingAdvisory.rm1.v1`
- Hard invariants: no CLI change; no route.ts change; `runtimeRoutingAuthorized: false` always; DEFER is advisory signal only; R2 review on degradation is advisory, not automatic

---

## Decision / Baseline

Decision: AUTHORIZED. Parent: LHW17 T3 Step 7 + TM1.

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/reputation-routing-advisory.ts` — new file
- Re-export in `src/index.ts`
- Tests in `tests/reputation-routing-advisory.test.ts`
- Fast Lane audit + completion review

## Evidence / Verification

- New file: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/reputation-routing-advisory.ts` — DELIVERED
- Tests: `tests/reputation-routing-advisory.test.ts` — 11 tests, 1655/1655 PASS (68 files)
- Fast Lane: `docs/reviews/CVF_RM1_REPUTATION_ROUTING_ADVISORY_FAST_LANE_2026-05-31.md` — PASS
- Completion: `docs/reviews/CVF_RM1_REPUTATION_ROUTING_ADVISORY_COMPLETION_2026-05-31.md` — CLOSED_PASS_BOUNDED

## Claim Boundary

RM1 implements a governed routing advisory function. It does not activate Reputation
runtime routing, change `resolveProviderForRole()` in the CLI, extend receipt envelopes,
or claim production readiness. Step 8 (Simulation Environment) requires a separate tranche.

---

*Authorized: 2026-05-31 | Operator sign-off in-session*
