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

QBS-11 candidate:

1. Issue a fresh governed candidate/roadmap packet.
2. Pre-register a new QBS-1 powered rerun after QBS-10 remediation.
3. Execute live provider run with redacted output retention.
4. Score with model-assisted reviewers and agreement metrics.
5. Publish no claim unless the claim ladder thresholds pass.

Public artifacts should continue to avoid score language until scoring supports
it.
