# CVF Fast Lane Audit — LP-LP1 Learning Plane Live Proof Session 1

Memory class: REVIEW_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.learningPlaneLiveProof.lplp1.v1`

GC-018: `docs/baselines/CVF_GC018_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md`

Risk class: R1 (live governed execution on existing certified lane; no code change)

---

## Purpose

Fast Lane audit for LP-LP1 — first live proof session for Learning Plane Foundation.
Satisfies LHW17 T3 prerequisite for Truth Model scoring activation. One governed
live call via /api/execute → Alibaba qwen-turbo → ALLOW receipt → derived PatternInsight
→ provisional TruthScore.

## Target / Source Under Review

- Live evidence: `docs/assessments/CVF_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md`
- Pipeline: `truth-model-calibration.ts` → `reputation-routing-advisory.ts` (existing)
- Route: `/api/execute` (existing, unchanged)
- Provider: alibaba / qwen-turbo (existing certified lane)

## Scope / Methodology

Fast Lane (R1). No code change. Live call on existing certified Alibaba R1 lane.
Receipt recorded secret-safe (receipt ID + envelope ID only; no raw API key).

## Findings / Position

| Gate | Result |
| --- | --- |
| Live receipt obtained: `rcpt-env-mpt1w4ya-r45xzf` | PASS |
| decision=ALLOW, riskLevel=R1, provider=alibaba, model=qwen-turbo | PASS |
| evidenceMode=live (not mock) | PASS |
| PatternInsight derived: dominantPattern=ACCEPT, healthSignal=HEALTHY | PASS |
| runCalibrationSession: phase=COMPLETE, disposition=PASS | PASS |
| TruthScore: ~55/100 ADEQUATE, isProvisional=true | PASS |
| RoutingAdvisory: PROCEED (from TRUSTED reputation signal) | PASS |
| runtimeCalibrationAuthorized=false preserved | PASS |
| No raw API key or bearer token exposed in evidence record | PASS |
| LHW17 T3 prerequisite satisfied: liveProofProven=true | PASS |

Fast Lane verdict: **PASS**

## Risk / Corrective Action

No violations. Single session only — TruthScore confidence=0.1 (ADEQUATE). Additional
sessions required before weighting doctrine is established. Reputation activation
prerequisite ("at least one live proof") now satisfied.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| LHW17 T3 live-proof prerequisite now satisfied | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | LP-LP1 closes live-proof gate | HANDLED |
| Single session only — low confidence (0.1) | `RULE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Additional calibration sessions needed for confidence >0.7 | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A — Alibaba free tier, R1 cost class | N/A |

## Claim Boundary

LP-LP1 satisfies the LHW17 T3 live-proof prerequisite. It does not activate runtime
Truth Model scoring, enable automatic Reputation routing, or claim full Learning Plane
production readiness.
