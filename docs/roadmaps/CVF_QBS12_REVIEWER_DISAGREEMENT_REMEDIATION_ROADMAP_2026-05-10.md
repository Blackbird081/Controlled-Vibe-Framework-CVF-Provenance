# CVF QBS12 Reviewer Disagreement Remediation Roadmap

Date: 2026-05-10

Status: `CLOSED_COMPLETE_NO_PUBLIC_QBS_CLAIM`

## Objective

Analyze why QBS-11 R6 failed reviewer agreement and remediate the clearest
residual quality defects without making a new score claim.

## Work Packages

| Work Package | Status | Result |
|---|---|---|
| QBS12-CP1 Analyze R6 reviewer disagreement | `COMPLETE` | Disagreement found across all configs, not only `CFG-B`; largest family-level disagreement in `cost_quota_provider_selection`. |
| QBS12-CP2 Identify residual quality drivers | `COMPLETE` | Generic approval-gated security output, unsupported provider benchmark numbers, and meta-commentary on simple transformations identified. |
| QBS12-CP3 Remediate approval-gated output | `COMPLETE` | `NEEDS_APPROVAL` now includes deterministic pre-approval safe work, with incident redaction plan and disclosure skeleton where relevant. |
| QBS12-CP4 Remediate governed prompt contract | `COMPLETE` | Prompt now instructs direct output for short transformations and forbids invented provider benchmark numbers. |
| QBS12-CP5 Add focused tests | `COMPLETE` | Tests cover approval-gated security preparation and prompt-contract constraints. |
| QBS12-CP6 Publish public no-score note | `COMPLETE` | Public QBS12 remediation note added. |
| QBS12-CP7 Validate and push | `COMPLETE` | Tests/build/public-surface/diff checks passed; public commit pushed. |

## Evidence

Public commit:

`d44517c Remediate QBS reviewer disagreement drivers`

Public artifact:

`docs/benchmark/qbs-1/reviewer-disagreement-remediation-qbs12.md`

Validation:

- `npm run test:run -- src/app/api/execute/route.qbs-hard-gates.test.ts src/app/api/qbs/front-door-clarification/route.test.ts src/lib/execute-prompt-contract.test.ts src/lib/enforcement.qbs-hard-gates.test.ts src/lib/intent-router.qbs-f7.test.ts` -> `15 passed / 0 failed`
- `npm run build` -> PASS
- `python scripts/check_public_surface.py` -> PASS
- `git diff --check` -> PASS

## Closure Boundary

QBS-12 does not create a new benchmark score. It prepares the code and public
methodology surface for a future pre-registered rerun. Any QBS-13/R7 claim
attempt must be separately frozen, executed, scored, and agreement-checked.
