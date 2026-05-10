# CVF QBS16 Anchor Adjudication Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Adjudicate the QBS15 high-disagreement reviewer calibration anchors and convert
the result into a bounded reviewer rubric addendum before any future QBS claim
run.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS16-CP1 Build adjudication script | `COMPLETE` | `scripts/adjudicate_qbs_calibration_anchors.py` reads QBS15 anchors, calls a live OpenAI-compatible adjudicator, and writes strict JSON adjudication output. |
| QBS16-CP2 Run third-model adjudication | `COMPLETE` | Alibaba/DashScope `qwen-turbo` adjudicated 14 high-disagreement anchors. |
| QBS16-CP3 Publish adjudication artifact | `COMPLETE` | `reviewer-calibration-adjudication-qbs16.json` records anchor-level decisions, quality scores, rework levels, and calibration issue summaries. |
| QBS16-CP4 Publish reviewer rubric addendum | `COMPLETE` | `reviewer-rubric-addendum-qbs16.md` documents clarified reviewer guidance for the highest-drift cases. |
| QBS16-CP5 Validate and push | `COMPLETE` | Python compile, public-surface scan, diff check, and raw secret scan passed; public commit pushed. |

## Evidence

Public commit:

`fe93f00 Publish QBS anchor adjudication`

Public artifacts:

- `scripts/adjudicate_qbs_calibration_anchors.py`
- `docs/benchmark/qbs-1/reviewer-anchor-adjudication-qbs16.md`
- `docs/benchmark/qbs-1/reviewer-calibration-adjudication-qbs16.json`
- `docs/benchmark/qbs-1/reviewer-rubric-addendum-qbs16.md`

Adjudicator:

- Provider/model: Alibaba/DashScope `qwen-turbo`
- Prompt version: `qbs16-anchor-adjudication-v1`
- Limitation: third-model adjudication fallback, not human gold-label review.

Key results:

- High-disagreement anchors adjudicated: `14`
- Mean adjudicated quality: `2.642857142857143`
- Decision counts: `deepseek_closer=11`, `openai_closer=0`,
  `both_reasonable=2`, `both_partly_wrong=1`
- Rework counts: `NONE=6`, `LIGHT=2`, `HEAVY=6`

Validation:

- Python compile for QBS scripts: PASS
- Public-surface scan: PASS
- `git diff --check`: PASS
- Raw secret scan: PASS

## Closure Boundary

QBS-16 creates no new QBS score and does not mutate historical R5/R6/R7
scores. It does not prove L4/L5 and does not authorize a public quality claim.
R8 remains blocked until a calibration-only check validates the revised
reviewer addendum and prompt against the QBS15/QBS16 anchors.
