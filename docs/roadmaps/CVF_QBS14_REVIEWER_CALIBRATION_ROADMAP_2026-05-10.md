# CVF QBS14 Reviewer Calibration Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Analyze reviewer drift across R5/R6/R7 and decide whether QBS should rerun or
calibrate before another claim attempt.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS14-CP1 Build reviewer drift diagnostic | `COMPLETE` | `scripts/analyze_qbs_reviewer_drift.py` reads scored artifacts and emits cross-run diagnostics. |
| QBS14-CP2 Analyze R5/R6/R7 trend | `COMPLETE` | R7 did not improve agreement or median delta versus R6. |
| QBS14-CP3 Identify scoring instability | `COMPLETE` | Disagreement is present across direct baselines and `CFG-B`, with high drift in builder-handoff, cost/provider, and ambiguous prompts. |
| QBS14-CP4 Publish calibration plan | `COMPLETE` | Public plan requires anchor set, clarified rubric, and third adjudicator or human spot-check before future claim runs. |
| QBS14-CP5 Validate and push | `COMPLETE` | Python compile, public-surface scan, diff check, and secret scan passed; public commit pushed. |

## Evidence

Public commit:

`5fef21b Publish QBS reviewer drift analysis`

Public artifacts:

- `docs/benchmark/qbs-1/reviewer-calibration-plan-qbs14.md`
- `docs/benchmark/qbs-1/reviewer-drift-analysis-qbs14.json`
- `scripts/analyze_qbs_reviewer_drift.py`

Key results:

- R5 agreement: PASS, kappa `0.7138606707187487`, rho `0.7864500452029551`
- R6 agreement: FAIL, kappa `0.5043578866178171`, rho `0.5987420572601858`
- R7 agreement: FAIL, kappa `0.46363630803481326`, rho `0.5329992930685284`
- R6/R7 median `CFG-B - CFG-A1`: `-0.125`

## Closure Boundary

QBS-14 makes no public QBS score claim. It explicitly blocks another live claim
run until reviewer calibration and residual `CFG-B` output-quality work are
completed.
