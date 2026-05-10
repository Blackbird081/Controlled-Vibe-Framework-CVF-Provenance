# CVF QBS18 Calibration Cleanup Rerun Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Clean the QBS15/QBS16 calibration reference, normalize rework labels, and rerun
the calibration-only reviewer agreement check without opening a new benchmark
claim run.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS18-CP1 Trace anchor/reference conflicts | `COMPLETE` | `QBS15-001` was confirmed as empty visible output in the R5 redacted reviewer bundle while QBS16 scored it as quality `4` and `NONE`. |
| QBS18-CP2 Build cleaned reference | `COMPLETE` | `scripts/build_qbs18_calibration_reference.py` generated `reviewer-calibration-reference-qbs18.json` without mutating QBS15/QBS16. |
| QBS18-CP3 Normalize rework rubric | `COMPLETE` | `reviewer-rework-rubric-normalization-qbs18.md` defines `REJECT`, `HEAVY`, `LIGHT`, and `NONE` semantics. |
| QBS18-CP4 Rerun calibration-only check | `COMPLETE` | OpenAI `gpt-4o-mini` and DeepSeek `deepseek-chat` rerun passed against the cleaned reference. |
| QBS18-CP5 Publish and validate | `COMPLETE` | Python compile, public-surface scan, diff check, and raw secret scan passed; public commit pushed. |

## Evidence

Public commit:

`59d4a06 Publish QBS18 calibration cleanup rerun`

Public artifacts:

- `scripts/build_qbs18_calibration_reference.py`
- `docs/benchmark/qbs-1/reviewer-calibration-cleanup-and-rerun-qbs18.md`
- `docs/benchmark/qbs-1/reviewer-calibration-reference-qbs18.json`
- `docs/benchmark/qbs-1/reviewer-calibration-agreement-qbs18-rerun.json`
- `docs/benchmark/qbs-1/reviewer-rework-rubric-normalization-qbs18.md`

Key cleanup results:

- Cleaned reference count: `14`
- `correct_empty_visible_output_and_normalize_rework`: `1`
- `normalize_rework_label`: `1`
- `unchanged`: `12`

Rerun results:

- Overall status: `PASS`
- Weighted kappa: `0.9046321525885559`
- Spearman rho: `0.9219234991142461`
- OpenAI reviewer-vs-reference: `PASS`
  - quality-within-one: `1.0`
  - rework-match: `0.6428571428571429`
- DeepSeek reviewer-vs-reference: `PASS`
  - quality-within-one: `1.0`
  - rework-match: `0.7857142857142857`

Validation:

- Python compile for QBS scripts: PASS
- Public-surface scan: PASS
- `git diff --check`: PASS
- Raw secret scan: PASS

## Closure Boundary

QBS-18 passes the calibration-only reviewer-plan gate but does not publish a
QBS score. It does not prove L4/L5, family-level performance, or provider
parity.

The next track may freeze the reviewer plan and pre-register a future R8 claim
run that cites the QBS18 cleaned reference and prompt lineage.
