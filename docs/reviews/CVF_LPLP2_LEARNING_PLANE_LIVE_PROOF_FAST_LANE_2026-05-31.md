# CVF Fast Lane Audit — LP-LP2 Learning Plane Live Proof Sessions 2-7

Memory class: REVIEW_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.learningPlaneLiveProof.lplp2.v1`

GC-018: `docs/baselines/CVF_GC018_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md` (parent)

Risk class: R1 (live governed execution, existing certified lane, no code change)

---

## Purpose

Fast Lane audit for LP-LP2 — 6 additional live proof sessions to reach confidence=0.7.
Combined with LP-LP1 (session 1), total = 7 sessions → confidence=0.7 → TruthScore STRONG.
TruthScore remains PROVISIONAL — no weighting doctrine established.

## Target / Source Under Review

- Evidence: `docs/assessments/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md`
- Pipeline: `truth-model-calibration.ts` → `reputation-routing-advisory.ts` (existing)
- Provider: alibaba / qwen-turbo R1 (6 × ALLOW)

## Scope / Methodology

Fast Lane (R1). No code change. 6 live calls on existing Alibaba R1 certified lane.
All receipts recorded secret-safe.

## Findings / Position

| Gate | Result |
| --- | --- |
| 6 ALLOW receipts: S2-S7 all alibaba/qwen-turbo/R1 | PASS |
| 7 total insights cumulative (LP-LP1 + LP-LP2) | PASS |
| confidence=0.7 (7/10) — target threshold reached | PASS |
| TruthScore: 86/100 STRONG (PROVISIONAL, isProvisional=true) | PASS |
| RoutingAdvisory: PROCEED (TRUSTED class) | PASS |
| No raw API key or bearer token in evidence record | PASS |
| runtimeCalibrationAuthorized=false preserved | PASS |
| No runtime Truth Model scoring activated | PASS |

Fast Lane verdict: **PASS**

## Risk / Corrective Action

No violations. TruthScore STRONG but PROVISIONAL — weighting doctrine requires separate
governed tranche per 2026-04-12 decision s3.7. No fixed doctrine established here.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| confidence=0.7 threshold reached | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | LP-LP2 reaches confidence target | HANDLED |
| Weighting doctrine still PROVISIONAL | `RULE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Separate tranche to lift provisional status | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A — Alibaba R1, 6 calls | N/A |

## Claim Boundary

LP-LP2 reaches confidence=0.7 with TruthScore STRONG. TruthScore PROVISIONAL.
No weighting doctrine established. No runtime scoring activated.
