# CVF W135-T1 Post-AI Output Validation False-Positive Roadmap

> Authorization: `docs/baselines/CVF_GC018_W135_T1_POST_AI_OUTPUT_VALIDATION_FALSE_POSITIVE_AUTHORIZATION_2026-05-07.md`  
> Wave ID: W135  
> Status: CLOSED

## Problem

W134 proved the pre-AI HTTP 400 blocker is fixed, but Alibaba CP4 still showed a
post-AI `competitor_review` failure:

- enforcement: ALLOW
- provider path: reached
- HTTP status: 422
- output validation issue: `UNSAFE_CONTENT`

The likely root cause is a template/validator mismatch: the
`competitor_review` output template asks for `How to exploit`, while the output
validator treats the standalone word `exploit` as unsafe content.

## Checkpoints

| CP | Status | Work |
|---|---:|---|
| CP0 | COMPLETE | GC-018 authorization and scope lock |
| CP1 | COMPLETE | Confirmed exact template/validator mismatch |
| CP2 | COMPLETE | Replaced unsafe business wording in `competitor_review` output template |
| CP3 | COMPLETE | Made output validator context-aware for ambiguous security terms |
| CP4 | COMPLETE | Added targeted unit regression coverage |
| CP5 | COMPLETE | Live Alibaba `competitor_review` proof returned HTTP 200 / ALLOW |
| CP6 | COMPLETE | Published closure evidence |

## Evidence Rules

Evidence must keep API keys out of logs and commits. Live proof may record
provider, model, HTTP status, receipt decision, and output-validation metadata,
but not raw secrets.

## Closure Evidence

- Root-cause finding:
  `docs/reviews/CVF_W135_ROOT_CAUSE_FINDING_2026-05-07.md`
- Live Alibaba targeted evidence:
  `docs/reviews/CVF_W135_COMPETITOR_REVIEW_OUTPUT_VALIDATION_EVIDENCE_2026-05-07.json`
- Targeted live spec:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/w135-output-validation.live.spec.ts`
- Unit regression:
  `npx vitest run src/lib/output-validator.test.ts` — 32/32 passed
- Live proof:
  `npx playwright test tests/e2e/w135-output-validation.live.spec.ts --workers=1` — 1/1 passed
- Release gate:
  `docs/reviews/CVF_W135_RELEASE_GATE_RESULT_2026-05-07.md` — PASS

W135 closes the targeted post-AI `competitor_review` output-validation false
positive. It does not close the W134 execute-route timeout residuals.
