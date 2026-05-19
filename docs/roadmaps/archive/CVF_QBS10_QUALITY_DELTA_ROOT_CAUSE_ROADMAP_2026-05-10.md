# CVF QBS10 Quality Delta Root-Cause Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE`

## Objective

Determine why QBS-9 did not support an L4/L5 public quality claim, remediate
the highest-impact defect, and preserve claim boundaries.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS10-CP1 Inspect QBS-9 reviewer score drivers | `COMPLETE` | Worst deltas identified in high-risk safety, bypass/adversarial, and ambiguous non-coder families. |
| QBS10-CP2 Identify root cause | `COMPLETE` | Correct non-ALLOW decisions lacked useful primary `output` text. |
| QBS10-CP3 Remediate `/api/execute` non-ALLOW outputs | `COMPLETE` | Deterministic `BLOCK`, `CLARIFY`, and `NEEDS_APPROVAL` output guidance added. |
| QBS10-CP4 Remediate front-door clarification output | `COMPLETE` | Weak-confidence route now returns fuller clarification packet. |
| QBS10-CP5 Add targeted tests | `COMPLETE` | Route tests cover block, clarify, approval, and front-door clarification output. |
| QBS10-CP6 Publish public documentation | `COMPLETE` | Public QBS docs updated with no-score remediation status. |
| QBS10-CP7 Validate and push | `COMPLETE` | Targeted tests, build, public-surface scan, Python compile, and diff check passed; public commit pushed. |

## Evidence

Public commit:

`57fd8c3 Improve QBS governed stop outputs`

Public root-cause artifact:

`docs/benchmark/qbs-1/quality-delta-root-cause-qbs10.md`

Validation:

- `npm run test:run -- src/app/api/execute/route.qbs-hard-gates.test.ts src/app/api/qbs/front-door-clarification/route.test.ts src/lib/enforcement.qbs-hard-gates.test.ts src/lib/intent-router.qbs-f7.test.ts` -> `12 passed / 0 failed`
- `npm run build` -> PASS
- `python scripts/check_public_surface.py` -> PASS
- `python -m py_compile scripts/run_qbs_powered_single_provider.py scripts/check_qbs_scored_run_readiness.py scripts/score_qbs_model_assisted_reviewers.py` -> PASS
- `git diff --check` -> PASS

## Boundary

QBS-10 does not create a new QBS score. It only remediates the non-ALLOW
user-facing output quality defect found after QBS-9 reviewer scoring.

The next scored attempt requires fresh pre-registration and should be treated
as QBS-11 or later.
