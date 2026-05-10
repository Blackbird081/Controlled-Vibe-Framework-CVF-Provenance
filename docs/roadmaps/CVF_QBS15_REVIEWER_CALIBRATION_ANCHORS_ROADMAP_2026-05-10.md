# CVF QBS15 Reviewer Calibration Anchors Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Create a fixed reviewer calibration anchor set from R5/R6/R7 and prepare the
scoring script to use explicit calibration guidance in future runs.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS15-CP1 Build anchor generator | `COMPLETE` | `scripts/build_qbs_reviewer_calibration_anchors.py` creates the QBS15 anchor JSON from public R5/R6/R7 artifacts. |
| QBS15-CP2 Generate anchor set | `COMPLETE` | 20 anchors generated: 14 high-disagreement and 6 consensus references. |
| QBS15-CP3 Update reviewer scorer | `COMPLETE` | `score_qbs_model_assisted_reviewers.py` supports `--prompt-version` and `--calibration-anchors`. |
| QBS15-CP4 Publish public docs | `COMPLETE` | QBS15 anchor note and JSON linked from public benchmark docs. |
| QBS15-CP5 Validate and push | `COMPLETE` | Python compile, public-surface scan, scorer help, anchor generation, diff check, and secret scan passed; public commit pushed. |

## Evidence

Public commit:

`53462f7 Publish QBS reviewer calibration anchors`

Public artifacts:

- `scripts/build_qbs_reviewer_calibration_anchors.py`
- `docs/benchmark/qbs-1/reviewer-calibration-anchors-qbs15.md`
- `docs/benchmark/qbs-1/reviewer-calibration-anchors-qbs15.json`

Validation:

- Python compile for QBS scripts: PASS
- Anchor generation: PASS
- Scorer help output with new options: PASS
- Public-surface scan: PASS
- `git diff --check`: PASS
- Raw secret scan: PASS

## Closure Boundary

QBS-15 does not adjudicate anchors and does not create a new score. The anchor
set is a calibration/adjudication input only. R8 remains blocked until the
high-disagreement anchors are resolved and the reviewer plan is updated.
