# CVF EVT-4 Provider Model Screening Summary

Date: 2026-05-15

Scope: F-1 model-lane screening for the frozen EVT-4 output-quality corpus.
CFG-A is direct provider API. CFG-B is governed `/api/execute` with live
governance receipt. Reviewer mode was `openai:gpt-4o`.

## Result

F-1 is not closed. The best full-corpus lane was DeepSeek `deepseek-v4-pro`,
but its full 20-pair rebaseline finished at median normalized delta `-0.08`,
below the preregistered closure threshold `>= -0.05`.

## Provider Screening

| Provider | Model | Run | Completed | Receipts | Safety failures | Median delta | Decision |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| OpenAI | `gpt-5.4-mini` | two-pass sample 5 | 5/5 | 5/5 final, 5/5 expansion pairs | 0 | -0.16 | Not selected |
| Alibaba | `qwen3.6-plus` | latest smoke 2 | 2/2 | 2/2 | 0 | -0.16 | Not selected |
| DeepSeek | `deepseek-v4-pro` | full rebaseline 20 | 20/20 | 20/20 | 0 | -0.08 | Best lane, not closed |
| DeepSeek | `deepseek-v4-pro` | two-pass sample 5 | 5/5 | 5/5 final, 5/5 expansion pairs | 0 | -0.16 | Two-pass rejected |

## Code Changes Kept

- EVT-4 runner can now screen `alibaba`, `deepseek`, and `openai` lanes.
- OpenAI GPT-5-family chat calls use `max_completion_tokens`.
- EVT-4 runner passes a bounded provider timeout override for slow model
  rebaselines.
- Canonical governed system prompt is language-adaptive instead of forcing
  Vietnamese for English input.
- `/api/execute` now validates successful-but-empty provider output and
  retries/blocks it instead of returning an empty successful response.

## Boundary

DeepSeek `deepseek-v4-pro` is the recommended next F-1 lane, but the full
evidence does not satisfy F-1 closure. Model choice alone is insufficient.
Further work should target prompt depth and template-family behavior on the
negative full-corpus lanes, especially EVT4-02 through EVT4-05, EVT4-09,
EVT4-12, EVT4-14, EVT4-15, and EVT4-18.

## Evidence

- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FULL_REBASELINE_R2_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_FULL_REBASELINE_R2_SUMMARY_2026-05-15.md`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_TWO_PASS_SAMPLE5_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_DEEPSEEK_V4_PRO_TWO_PASS_SAMPLE5_SUMMARY_2026-05-15.md`
- `docs/assessments/CVF_EVT4_OPENAI_MINI_TWO_PASS_SAMPLE5_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_OPENAI_MINI_TWO_PASS_SAMPLE5_SUMMARY_2026-05-15.md`
- `docs/assessments/CVF_EVT4_QWEN36_PLUS_RESPONSE_LANGUAGE_SMOKE_EVIDENCE_2026-05-15.json`
- `docs/assessments/CVF_EVT4_QWEN36_PLUS_RESPONSE_LANGUAGE_SMOKE_SUMMARY_2026-05-15.md`

## Verification

- `npx vitest run src/app/api/execute/route.test.ts src/lib/execute-prompt-contract.test.ts src/lib/ai-providers.test.ts src/lib/ai/providers.test.ts`
  PASS (103/103).
- `python scripts/run_cvf_release_gate_bundle.py --json` PASS.
