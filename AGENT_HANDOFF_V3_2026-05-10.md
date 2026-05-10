<!-- Memory class: SUMMARY_RECORD -->
# CVF Agent Handoff V3 - QBS Continuation

**Date:** 2026-05-10
**Status:** ACTIVE CONTINUATION HANDOFF
**Supersedes for new updates:** `AGENT_HANDOFF_V2_2026-05-09.md`
**Reason:** V2 exceeded the soft advisory size after QBS-9/QBS-10 continuation.

## Repository Boundary

This workspace is the private provenance/archive repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`

Public-facing CVF changes belong only in the sibling public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Before any public push, run `git remote -v` and confirm `origin` is:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Do not push public artifacts from this provenance workspace.

## Current QBS State

Latest public commit:

`57fd8c3 Improve QBS governed stop outputs`

Latest public push target:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Current public status:

`QBS10_REMEDIATION_COMPLETE_NO_NEW_SCORE`

QBS-9 remains the latest scored run. It completed model-assisted reviewer
scoring with agreement passing, but no public quality claim:

- Run: `qbs1-powered-single-provider-20260510-alibaba-r5`
- Provider/model: Alibaba/DashScope `qwen-turbo`
- Reviewer models: OpenAI `gpt-4o-mini` and DeepSeek `deepseek-chat`
- Agreement: PASS
- Median normalized quality delta `CFG-B` vs `CFG-A1`: `-0.25`
- Bootstrap 95% CI: `[-0.3125, -0.25]`
- Result: `QBS9_REVIEWER_SCORED_NO_PUBLIC_QBS_CLAIM`

QBS-10 root cause:

- Governance hard gates were mostly correct.
- `CFG-B` underperformed because governed non-ALLOW responses often produced
  empty or too-terse user-facing `output`.
- The worst negative deltas clustered in high-risk security, bypass/adversarial
  governance, and ambiguous non-coder prompt families.

QBS-10 remediation delivered:

- `/api/execute` now returns deterministic user-facing `output` for:
  - `BLOCK`
  - `CLARIFY`
  - `NEEDS_APPROVAL`
- `/api/qbs/front-door-clarification` now returns a fuller clarification packet
  instead of only the generic question.
- Public root-cause artifact:
  `docs/benchmark/qbs-1/quality-delta-root-cause-qbs10.md`
- Public README status updated to `QBS10_REMEDIATION_COMPLETE_NO_NEW_SCORE`.

## Validation Completed

In public-sync:

```bash
npm run test:run -- src/app/api/execute/route.qbs-hard-gates.test.ts src/app/api/qbs/front-door-clarification/route.test.ts src/lib/enforcement.qbs-hard-gates.test.ts src/lib/intent-router.qbs-f7.test.ts
npm run build
python scripts/check_public_surface.py
python -m py_compile scripts/run_qbs_powered_single_provider.py scripts/check_qbs_scored_run_readiness.py scripts/score_qbs_model_assisted_reviewers.py
git diff --check
```

Results:

- Targeted tests: `12 passed / 0 failed`
- Next build: PASS
- Public-surface scan: PASS
- Python compile: PASS
- Diff whitespace check: PASS
- Raw-key scan of touched files: no raw API key values found

## Claim Boundary

QBS-10 does not claim that CVF beats direct model baselines. It fixes the
identified output-quality defect and documents the remediation.

Any future score or L4/L5 public claim requires a new pre-registered run,
execution artifact, reviewer scoring, agreement check, and claim statement.

## Suggested Next Track

QBS-11 completed after this handoff was opened:

- Public pre-registration commit: `bdd7b9f Preregister QBS R6 remediation rerun`
- Public pre-registration tag:
  `qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r6`
- Tag SHA: `bdd7b9f07e932fb87d3eb929a05390debb7f4c68`
- Public scored artifact commit: `aaab722 Publish QBS R6 scored artifacts`
- Run: `qbs1-powered-single-provider-20260510-alibaba-r6`
- Live execution: 48 tasks x 3 repeats x 3 configs = 432 configuration executions
- Hard gates: PASS
- Reviewer scoring: OpenAI `gpt-4o-mini` + DeepSeek `deepseek-chat`
- Reviewer agreement: FAIL
  - quadratic-weighted Cohen kappa: `0.5043578866178171`
  - Spearman rho: `0.5987420572601858`
  - paired score count: `432`
- L4 result: FAIL
  - median normalized quality delta `CFG-B` vs `CFG-A1`: `-0.125`
  - bootstrap 95% CI: `[-0.25, 0.0]`
  - median normalized quality delta `CFG-B` vs `CFG-A0`: `-0.125`
  - median heavy/reject improvement `CFG-B` vs `CFG-A1`: `0.0`
- Public status:
  `QBS11_R6_REVIEWER_AGREEMENT_FAIL_NO_PUBLIC_QBS_CLAIM`

QBS-11 interpretation:

- QBS-10 remediation helped: high-risk and ambiguous prompt families improved
  materially versus QBS-9.
- Claim remains blocked because reviewer agreement did not clear the required
  gate and aggregate median delta is still negative.
- Public artifacts correctly make no L4/L5 claim.

Suggested next track, QBS-12 candidate:

1. Issue a fresh governed candidate/roadmap packet.
2. Analyze R6 reviewer disagreement at task/reviewer level.
3. Identify residual quality causes in normal planning, builder handoff,
   cost/provider selection, and negative-control families.
4. Decide whether to refine reviewer rubric calibration, CFG-B response
   completeness, or both.
5. Publish no new score claim unless a future pre-registered run passes hard
   gates, reviewer agreement, and claim-ladder thresholds.

Public artifacts should continue to avoid score language until scoring supports
it.

## QBS-12 Closed Continuation

QBS-12 completed after QBS-11:

- Public commit: `d44517c Remediate QBS reviewer disagreement drivers`
- Public status: `QBS12_REMEDIATION_COMPLETE_NO_NEW_SCORE`
- Public artifact:
  `docs/benchmark/qbs-1/reviewer-disagreement-remediation-qbs12.md`

R6 disagreement analysis:

- Reviewer disagreement was not isolated to `CFG-B`.
- Mean absolute reviewer quality difference:
  - `CFG-A0`: `0.722`
  - `CFG-A1`: `0.667`
  - `CFG-B`: `0.715`
- Largest family-level disagreement:
  `cost_quota_provider_selection`
- Residual `CFG-B` quality causes:
  - approval-gated security/incident outputs were correct but too generic;
  - provider/cost-selection outputs sometimes invented latency, accuracy,
    benchmark, cost, quota, version, or provider-ranking numbers;
  - simple low-risk transformations sometimes included too much meta-commentary.

QBS-12 remediation:

- `NEEDS_APPROVAL` output now includes deterministic pre-approval safe work.
- Security/incident-like approval requests now include a safe redaction plan and
  disclosure skeleton without exposing raw credentials, indicators, or account
  identifiers.
- Governed execution prompt now instructs the model to keep short
  transformations direct and to avoid unsupported provider benchmark numbers.
- Added targeted tests for these contracts.

Validation:

- Targeted tests: `15 passed / 0 failed`
- `npm run build`: PASS
- `python scripts/check_public_surface.py`: PASS
- `git diff --check`: PASS
- Raw secret scan: no raw key values found; only identifier false positives
  such as `configuredToken`.

QBS-12 claim boundary:

- No new QBS score.
- No L4/L5 claim.
- R6 score remains unchanged.

Suggested next track, QBS-13 candidate:

1. Fresh GC/roadmap.
2. Pre-register R7 after QBS-12 remediation.
3. Execute live run with redacted reviewer output retention.
4. Score with reviewers and publish no claim unless hard gates, reviewer
   agreement, and claim thresholds pass.
