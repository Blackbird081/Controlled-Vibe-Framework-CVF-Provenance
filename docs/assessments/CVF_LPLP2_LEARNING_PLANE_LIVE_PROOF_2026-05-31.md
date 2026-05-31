# CVF LP-LP2 — Learning Plane Live Proof Sessions 2-7

Memory class: EVIDENCE_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.learningPlaneLiveProof.lplp2.v1`

GC-018: `docs/baselines/CVF_GC018_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md` (parent)

## Purpose

Record 6 additional live proof sessions (S2-S7) for the Learning Plane Foundation.
Combined with LP-LP1 (session 1): 7 total insights → confidence=0.7 → TruthScore STRONG.
Target confidence threshold for weighting doctrine consideration now reached.

## Scope / Target / Owner Boundary

Target: Learning Plane Foundation calibration sessions 2-7. Owner: CVF learning plane / evidence surface.
Boundary: no code change; 6 additional live calls on existing Alibaba R1 certified lane; secret-safe evidence.

## Source / Predecessor Evidence

- LP-LP1: `docs/assessments/CVF_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md` (session 1, confidence=0.1)
- TM1: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts`
- CLI: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/dist/src/bin/cvf.js`

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED. 6 additional live calls executed. Combined with LP-LP1: 7 total insights. confidence=0.7 achieved.

## Live Receipt Evidence — Sessions 2-7

| Session | Receipt ID | Decision | Model | Provider |
| --- | --- | --- | --- | --- |
| S2 | `rcpt-env-mpt98mja-4s2n7i` | ALLOW | qwen-turbo | alibaba |
| S3 | `rcpt-env-mpt98uyt-tw7l6m` | ALLOW | qwen-turbo | alibaba |
| S4 | `rcpt-env-mpt994zn-tzj2a6` | ALLOW | qwen-turbo | alibaba |
| S5 | `rcpt-env-mpt99dc6-zanjkr` | ALLOW | qwen-turbo | alibaba |
| S6 | `rcpt-env-mpt99ohc-5iiqyi` | ALLOW | qwen-turbo | alibaba |
| S7 | `rcpt-env-mpt99yx9-51wat3` | ALLOW | qwen-turbo | alibaba |

All 6 sessions: decision=ALLOW, evidenceMode=live, riskLevel=R1.

---

## Cumulative Calibration Pipeline (LP-LP1 + LP-LP2)

### Total PatternInsights: 7 (sessions 1-7)

All 7 derived from live ALLOW receipts:
- `dominantPattern`: ACCEPT (all sessions)
- `healthSignal`: HEALTHY (all sessions)
- `acceptRate`: 1.0 (all sessions)

### TruthModel (7 insights)

```
totalInsightsProcessed: 7
dominantPattern:        ACCEPT
currentHealthSignal:    HEALTHY
healthTrajectory:       STABLE (7 HEALTHY entries — no degradation)
confidenceLevel:        0.7  (min(7/10, 1.0))
```

### TruthScore (7 insights — PROVISIONAL)

```
confidenceScore:   18/25  (round(0.7 × 25))
healthScore:       25/25  (HEALTHY)
trajectoryScore:   18/25  (STABLE)
patternScore:      25/25  (ACCEPT)
compositeScore:    86/100
scoreClass:        STRONG
isProvisional:     true   (no fixed weighting doctrine yet)
```

### RoutingAdvisory

```
reputationClass:         TRUSTED  (full PASS across all dimensions)
disposition:             PROCEED
r2ReviewRecommended:     false
runtimeRoutingAuthorized: false
```

---

## Evidence Assessment

| Gate | Result |
| --- | --- |
| 6 additional live receipts obtained (ALLOW × 6) | PASS |
| All 6: alibaba / qwen-turbo / R1 / evidenceMode=live | PASS |
| Total 7 insights cumulative (LP-LP1 + LP-LP2) | PASS |
| confidence=0.7 — target threshold reached | PASS |
| TruthScore 86/100 STRONG (PROVISIONAL) | PASS |
| RoutingAdvisory PROCEED (TRUSTED) | PASS |
| No raw API key or bearer token exposed | PASS |
| runtimeCalibrationAuthorized=false preserved | PASS |

---

## Weighting Doctrine Status

With confidence=0.7 (7 sessions), the TruthScore **STRONG** class is now eligible for
weighting doctrine consideration. However, per 2026-04-12 decision section 3.7:
"TruthScore deltas must remain provisional until LPF calibration is complete."

The weighting doctrine is still **PROVISIONAL**. Additional sessions and a separate
governed tranche are required before any fixed weighting is established.

---

## Claim Boundary

`liveProofProven=true` — 7 sessions total. TruthScore STRONG (PROVISIONAL).
confidence=0.7 reached. No runtime Truth Model scoring activated. No weighting
doctrine established. Separate governed tranche required to lift provisional status.

## Evidence / Verification

- LP-LP1 evidence: `docs/assessments/CVF_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md`
- LP-LP2 evidence: this record
- Fast Lane: `docs/reviews/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_FAST_LANE_2026-05-31.md`
- Completion: `docs/reviews/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_COMPLETION_2026-05-31.md`
