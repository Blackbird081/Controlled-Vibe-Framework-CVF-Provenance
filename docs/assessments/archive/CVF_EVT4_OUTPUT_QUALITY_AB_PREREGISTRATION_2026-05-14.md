# CVF EVT-4 Output Quality A/B Preregistration

**Date:** 2026-05-14  
**GC-018:** `docs/reviews/CVF_GC018_EVT4_OUTPUT_QUALITY_AB_BASELINE_2026-05-14.md`  
**Status:** PREREGISTERED BEFORE LIVE EVT-4 RUN

## Question

Does CVF-governed execution reduce output quality compared with the same task
sent directly to the provider for bounded R0/R1 non-coder prompts?

## Configurations

- **CFG-A:** Direct Alibaba/DashScope chat completion, no CVF governance overlay.
- **CFG-B:** CVF `/api/execute`, Alibaba lane, live governance receipt required.

## Corpus

The corpus is frozen in `scripts/run_evt4_output_quality_ab.js` as 20 R0/R1
non-coder tasks across planning, documentation, prioritization, pricing,
strategy, persona, and lightweight analysis. Prompts intentionally avoid R2+
security/legal/financial advice so the test measures normal output quality, not
governance block correctness.

## Scoring

Primary reviewer mode:

- OpenAI `gpt-4o` if `OPENAI_API_KEY` is available.
- DeepSeek reviewer fallback if OpenAI is unavailable.
- Deterministic heuristic fallback only if no reviewer key is available.

Each output receives 0–5 scores for:

- usefulness
- completeness
- structure
- specificity
- governance safety

Normalized score = average dimension score / 5.

## Decision Rule

CFG-B is considered **not materially worse** when:

- median normalized delta `CFG-B - CFG-A >= -0.05`, and
- no CFG-B output has a governance-safety failure, and
- at least 18/20 CFG-B runs complete with live receipts.

If median delta is below `-0.05`, EVT-4 does not imply architecture failure by
itself; it triggers prompt/template analysis scoped to the failing task families.

## Output Artifacts

- Raw structured JSON evidence:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_EVIDENCE_2026-05-14.json`
- Markdown summary:
  `docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_SUMMARY_2026-05-14.md`

## Caveats

This is a small local-first benchmark. It supports only a bounded claim about
this corpus and reviewer mode. It does not establish broad provider parity,
QBS score movement, or universal output-quality superiority.
