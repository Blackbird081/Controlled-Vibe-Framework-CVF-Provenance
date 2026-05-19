# CVF F-1 Output Quality Parity Closure — Not Met

Date: 2026-05-15

## Decision

Close F-1 as `not met, evidence-backed`.

Do not continue broad prompt, template, model, token-budget, or rerun-based
attempts to force parity on the current EVT-4 corpus.

## Closure Evidence

Final stop-rule rebaseline:

- Evidence:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FINAL_STOP_RULE_REBASELINE_EVIDENCE_2026-05-15.json`
- Summary:
  `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FINAL_STOP_RULE_REBASELINE_SUMMARY_2026-05-15.md`

Result:

- Provider/model: DeepSeek `deepseek-v4-pro`.
- CFG-A: direct provider API.
- CFG-B: governed `/api/execute`.
- Completed: `20/20`.
- CFG-B live receipts: `20/20`.
- Safety failures: `0`.
- Median normalized delta: `-0.08`.
- Registered decision rule: `CFG-B - CFG-A >= -0.05`.
- Decision rule met: `false`.

## What Was Proven

CVF preserved live governance evidence and safety on the frozen EVT-4 R0/R1
corpus, but the governed path still carried a measurable output-quality tax
against direct provider output.

This is a useful product boundary, not a runtime governance failure.

## Retained Improvements

- Lean governed system prompt.
- DeepSeek `deepseek-v4-pro` trusted non-coder cap at `3072`.
- EVT-4 runner bounded CFG-A direct-empty retry.
- EVT-4 runner task filter and richer CFG-B failure diagnostics.

## Rejected Paths

- 4096-token DeepSeek cap: rejected due to timeout instability.
- Runtime two-pass expansion: rejected by prior evidence.
- Broad family-contract R2: rejected because it worsened the retained signal.
- Repeated full reruns hoping reviewer variance closes the gap.

## Required Future Posture

Future work may use EVT-4 as a regression benchmark after meaningful product
changes, but F-1 must not be reopened as a micro-tuning loop without fresh
explicit human authorization and a new review/roadmap packet.

