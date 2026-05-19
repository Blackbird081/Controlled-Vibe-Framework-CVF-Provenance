# CVF QBS17 Calibration-Only Check Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Run a calibration-only reviewer agreement check against the QBS15/QBS16 anchor
set using the QBS16 rubric addendum, without opening a new live benchmark claim
run.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS17-CP1 Build calibration checker | `COMPLETE` | `scripts/check_qbs_reviewer_calibration_agreement.py` scores anchor batches with live reviewers and computes reviewer agreement plus reviewer-vs-reference alignment. |
| QBS17-CP2 Run live reviewer check | `COMPLETE` | OpenAI `gpt-4o-mini` and DeepSeek `deepseek-chat` scored 14 high-disagreement anchors. |
| QBS17-CP3 Publish calibration artifact | `COMPLETE` | `reviewer-calibration-agreement-qbs17.json` records scores, usage, gates, largest deltas, and issue summaries. |
| QBS17-CP4 Publish public report | `COMPLETE` | `reviewer-calibration-agreement-qbs17.md` documents the fail/no-score result and next blocker. |
| QBS17-CP5 Validate and push | `COMPLETE` | Python compile, public-surface scan, diff check, and raw secret scan passed; public commit pushed. |

## Evidence

Public commit:

`ccfee10 Publish QBS calibration-only agreement check`

Public artifacts:

- `scripts/check_qbs_reviewer_calibration_agreement.py`
- `docs/benchmark/qbs-1/reviewer-calibration-agreement-qbs17.md`
- `docs/benchmark/qbs-1/reviewer-calibration-agreement-qbs17.json`

Key results:

- Overall status: `FAIL`
- Anchors checked: `14`
- Inter-reviewer agreement: `PASS`
- Weighted kappa: `0.7365591397849462`
- Spearman rho: `0.7935131868283122`
- OpenAI reviewer-vs-reference: `FAIL`
  - quality-within-one: `0.7857142857142857`
  - rework-match: `0.42857142857142855`
- DeepSeek reviewer-vs-reference: `FAIL`
  - quality-within-one: `0.9285714285714286`
  - rework-match: `0.35714285714285715`

Validation:

- Python compile for QBS scripts: PASS
- Public-surface scan: PASS
- `git diff --check`: PASS
- Raw secret scan: PASS

## Closure Boundary

QBS-17 restores reviewer-to-reviewer agreement on the anchor set but does not
validate the QBS16 model-adjudicated reference as sufficient for R8. It creates
no QBS score and does not unlock L4/L5 or any family-level claim.

R8 remains blocked until a later tranche audits anchor/reference conflicts and
normalizes the rework-label rubric.
