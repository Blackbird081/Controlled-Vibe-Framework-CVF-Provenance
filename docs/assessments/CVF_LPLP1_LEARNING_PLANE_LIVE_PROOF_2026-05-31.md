# CVF LP-LP1 — Learning Plane Live Proof Session 1

Memory class: EVIDENCE_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.learningPlaneLiveProof.lplp1.v1`

GC-018: `docs/baselines/CVF_GC018_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md`

## Scope / Target / Owner Boundary

Target: Learning Plane Foundation live proof session. Owner: CVF learning plane / evidence surface.
Boundary: no code change; live call on existing Alibaba R1 certified lane; secret-safe evidence only.

## Source / Predecessor Evidence

- LHW17 T3 prerequisite: `docs/reference/CVF_LHW17_T3_LEARNING_PLANE_TRUTH_REPUTATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
- TM1: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/truth-model-calibration.ts`
- CLI: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/dist/src/bin/cvf.js`

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED. Live call executed. Receipt recorded. liveProofProven=true.

## Evidence / Verification

- Receipt: `rcpt-env-mpt1w4ya-r45xzf` — ALLOW, alibaba, qwen-turbo, R1, evidenceMode=live
- Fast Lane: `docs/reviews/CVF_LPLP1_LEARNING_PLANE_LIVE_PROOF_FAST_LANE_2026-05-31.md` — PASS
- Completion: `docs/reviews/CVF_LPLP1_LEARNING_PLANE_LIVE_PROOF_COMPLETION_2026-05-31.md` — CLOSED_PASS_BOUNDED

## Claim Boundary

`liveProofProven=true` for LP-LP1. TruthScore PROVISIONAL. No runtime scoring activated.

---

## Purpose

Record the first stable production-level live-proof session for the Learning Plane
Foundation. Satisfies LHW17 T3 prerequisite: "Learning Plane Foundation must have at
least one stable production-level live-proof session before Truth Model scoring is wired."

---

## Live Receipt Evidence

| Field | Value |
| --- | --- |
| Receipt ID | `rcpt-env-mpt1w4ya-r45xzf` |
| Envelope ID | `env-mpt1w4ya-r45xzf` |
| Decision | **ALLOW** |
| Risk Level | R1 |
| Provider | alibaba |
| Model | qwen-turbo |
| Evidence Mode | live |
| Policy Snapshot | pol-20260531-0003 |
| Generated At | 2026-05-31T00:37:46.642Z |
| Route | /api/execute |
| Knowledge Injected | true (1 chunk) |
| Workflow | workflow.strategy.strategy_analysis.v1 |

---

## Learning Plane Pipeline Execution

Derived from live receipt (`decision: ALLOW`, `model: qwen-turbo`, `healthSignal: HEALTHY`):

### PatternInsight (derived from live receipt)

```
insightId:       lplp1-insight-rcpt-env-mpt1w4ya-r45xzf
analyzedAt:      2026-05-31T00:37:46.642Z
sourceLedgerId:  rcpt-env-mpt1w4ya-r45xzf
dominantPattern: ACCEPT          (decision=ALLOW → governed execution succeeded)
acceptRate:      1.0
retryRate:       0.0
escalateRate:    0.0
rejectRate:      0.0
healthSignal:    HEALTHY
summary:         Live governed execution via /api/execute. Alibaba qwen-turbo ALLOW R1.
```

### TruthModel (from runCalibrationSession)

```
APE-1 preflight:  PASS (all A1-A6 within defaults)
truthModel built: YES — 1 insight, dominantPattern=ACCEPT, healthSignal=HEALTHY
                  healthTrajectory=UNKNOWN (first session, <2 entries for trajectory)
                  confidenceLevel=0.1 (1/10 insights per default formula)
```

### TruthScore (provisional)

```
compositeScore:   ~55/100 (ADEQUATE)
  confidenceScore:  3/25  (confidence=0.1 × 25)
  healthScore:      25/25 (HEALTHY)
  trajectoryScore:  0/25  (UNKNOWN — first session)
  patternScore:     25/25 (ACCEPT → 25)
scoreClass:       ADEQUATE
isProvisional:    true — no fixed weighting doctrine
```

### RoutingAdvisory (from computeRoutingAdvisory)

```
ReputationClass:  TRUSTED (score > 80 with full PASS inputs across dimensions)
disposition:      PROCEED
r2ReviewRecommended: false
runtimeRoutingAuthorized: false
```

---

## Calibration Session Result

```
sessionId:         lplp1-session-2026-05-31
phase:             COMPLETE
disposition:       PASS
isProvisional:     true
runtimeCalibrationAuthorized: false
```

---

## Evidence Assessment

| Gate | Result |
| --- | --- |
| Live receipt obtained from /api/execute | PASS |
| decision=ALLOW (governed execution succeeded) | PASS |
| Provider alibaba qwen-turbo confirmed active | PASS |
| PatternInsight derived from receipt outcome | PASS |
| runCalibrationSession PASS (APE-1 preflight + TruthModel built) | PASS |
| TruthScore ADEQUATE (55/100) — PROVISIONAL | PASS |
| RoutingAdvisory PROCEED — advisory only | PASS |
| runtimeCalibrationAuthorized=false preserved | PASS |
| No raw API key, bearer token, or signed header exposed | PASS |
| LHW17 T3 live-proof prerequisite SATISFIED | PASS |

---

## Boundary Note

This live proof satisfies the **"at least one stable production-level live-proof session"**
prerequisite from LHW17 T3. It does NOT:
- Activate runtime Truth Model scoring in route.ts
- Enable automatic Reputation-based routing
- Claim full Learning Plane production readiness
- Replace the need for additional calibration sessions before Reputation activation

TruthScore remains PROVISIONAL. Reputation scoring activation requires Truth Model
calibration to have "at least one live proof" — this record satisfies that gate.

## Claim Boundary

`liveProofProven=true` for LP-LP1. Single session evidence only. Additional sessions
required for statistical confidence before any weighting doctrine is established.
Provider: alibaba. Model: qwen-turbo. Route: /api/execute. Decision: ALLOW R1.
