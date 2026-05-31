# CVF LP-LP2 — Learning Plane Live Proof Completion

Memory class: COMPLETION_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-31

Contract: `cvf.learningPlaneLiveProof.lplp2.v1`

GC-018: `docs/baselines/CVF_GC018_LPLP1_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md` (parent)

Fast Lane: `docs/reviews/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_FAST_LANE_2026-05-31.md`

---

## Purpose

Record completion of LP-LP2. 6 additional live sessions (S2-S7) added to LP-LP1 (S1).
Total 7 sessions → confidence=0.7 → TruthScore STRONG (PROVISIONAL). Confidence target
for weighting doctrine consideration reached.

## Target / Source Under Review

- Evidence: `docs/assessments/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md`
- Receipts: 6 × ALLOW alibaba/qwen-turbo/R1

## Scope / Methodology

Fast Lane (R1). No code change. 6 additional live governed sessions.

## Findings / Position

| Gate | Result |
| --- | --- |
| All 6 sessions: ALLOW × 6, alibaba, qwen-turbo, R1 | PASS |
| 7 total insights → confidence=0.7 | PASS |
| TruthScore 86/100 STRONG (PROVISIONAL) | PASS |
| RoutingAdvisory: PROCEED, r2Review=false | PASS |
| No runtime scoring activated | PASS |

## Risk / Corrective Action

No violations. Weighting doctrine PROVISIONAL — requires separate governed tranche.

## Deliverables

| Artifact | Status |
| --- | --- |
| 6 live receipts S2-S7 (all ALLOW) | DELIVERED |
| Evidence record: `docs/assessments/CVF_LPLP2_LEARNING_PLANE_LIVE_PROOF_2026-05-31.md` | DELIVERED |
| Fast Lane audit | DELIVERED |

## Calibration Milestone Summary

```
LP-LP1 (S1):  confidence=0.1 — first live proof, LHW17 T3 prerequisite satisfied
LP-LP2 (S2-S7): confidence=0.7 — STRONG TruthScore, weighting doctrine eligible
TruthScore:   86/100 STRONG (PROVISIONAL — isProvisional=true)
Next gate:    Separate governed tranche to establish weighting doctrine
              (removes isProvisional=true, activates fixed TruthScore weights)
```

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled |
| --- | --- | --- | --- | --- | --- |
| confidence=0.7 target reached | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` → `HANDLED` | LP-LP2 closes confidence target | HANDLED |
| Weighting doctrine PROVISIONAL | `RULE_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `DESIGN_REVIEW_REQUIRED` | Separate tranche for doctrine lift | DEFERRED |
| Runtime/provider/cost findings | N/A | `RUNTIME_BEHAVIOR_LEARNING` N/A | N/A | Alibaba R1, 6 calls | N/A |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY` — LP-LP2 is a private provenance live proof record.

## Claim Boundary

`confidence=0.7` reached. `TruthScore STRONG (PROVISIONAL)`. No runtime scoring
activated. No weighting doctrine established. Separate governed tranche required
to lift `isProvisional=true` and activate fixed TruthScore weighting.
