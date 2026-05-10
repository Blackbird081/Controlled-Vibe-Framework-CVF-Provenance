# CVF QBS11 Post-Remediation Rerun Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Run the QBS-1 powered single-provider benchmark again after QBS-10 remediation
and publish the result without overstating the claim.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS11-CP1 Create R6 pre-registration packet | `COMPLETE` | R6 preregistration, provider/model manifest, config prompt manifest, and reviewer plan published. |
| QBS11-CP2 Freeze R6 contract | `COMPLETE` | Tag `qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r6` pushed at `bdd7b9f07e932fb87d3eb929a05390debb7f4c68`. |
| QBS11-CP3 Execute live powered run | `COMPLETE` | 432 configuration executions completed on Alibaba/DashScope `qwen-turbo`; hard gates passed. |
| QBS11-CP4 Score reviewer outputs | `COMPLETE` | OpenAI `gpt-4o-mini` and DeepSeek `deepseek-chat` reviewers scored all task/config outputs. |
| QBS11-CP5 Evaluate claim ladder | `COMPLETE` | Reviewer agreement failed; L4 failed; no public score claim. |
| QBS11-CP6 Publish public artifacts | `COMPLETE` | R6 scored artifacts committed and pushed. |

## Evidence

Public commits:

- `bdd7b9f Preregister QBS R6 remediation rerun`
- `aaab722 Publish QBS R6 scored artifacts`

Public artifact path:

`docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r6/`

Key results:

- Hard gates: PASS
- Reviewer agreement: FAIL
- Quadratic-weighted Cohen kappa: `0.5043578866178171`
- Spearman rho: `0.5987420572601858`
- Median normalized quality delta `CFG-B` vs `CFG-A1`: `-0.125`
- Bootstrap 95% CI: `[-0.25, 0.0]`
- L4 pass: `false`

## Closure Boundary

QBS-11 improves the diagnostic picture but does not support a public QBS score
or L4/L5 claim. The next work should focus on reviewer disagreement and
remaining quality deficits before another pre-registered claim attempt.
