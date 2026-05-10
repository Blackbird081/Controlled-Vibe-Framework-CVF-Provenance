# CVF QBS13 Post-QBS12 Rerun Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Run the QBS-1 powered single-provider benchmark after QBS-12 remediation and
publish the result without overstating the claim.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS13-CP1 Create R7 pre-registration packet | `COMPLETE` | R7 preregistration, provider/model manifest, config prompt manifest, and reviewer plan published. |
| QBS13-CP2 Freeze R7 contract | `COMPLETE` | Tag `qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r7` pushed at `556edd368ed4d0e45b6f88d915be4c4b6fd1d4b3`. |
| QBS13-CP3 Execute live powered run | `COMPLETE` | 432 configuration executions completed on Alibaba/DashScope `qwen-turbo`; hard gates passed. |
| QBS13-CP4 Score reviewer outputs | `COMPLETE` | OpenAI `gpt-4o-mini` and DeepSeek `deepseek-chat` reviewers scored all task/config outputs. |
| QBS13-CP5 Evaluate claim ladder | `COMPLETE` | Reviewer agreement failed; L4 failed; no public score claim. |
| QBS13-CP6 Publish public artifacts | `COMPLETE` | R7 scored artifacts committed and pushed. |

## Evidence

Public commits:

- `556edd3 Preregister QBS R7 remediation rerun`
- `e66c556 Publish QBS R7 scored artifacts`

Public artifact path:

`docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r7/`

Key results:

- Hard gates: PASS
- Reviewer agreement: FAIL
- Quadratic-weighted Cohen kappa: `0.46363630803481326`
- Spearman rho: `0.5329992930685284`
- Median normalized quality delta `CFG-B` vs `CFG-A1`: `-0.125`
- Bootstrap 95% CI: `[-0.25, 0.0]`
- L4 pass: `false`

## Closure Boundary

QBS-13 does not support a public QBS score or L4/L5 claim. Because reviewer
agreement worsened versus R6 and the median delta did not improve, the next
work should stop live reruns and focus on scoring-method calibration plus
residual CFG-B output quality.
