<!-- Memory class: FULL_RECORD -->
# CVF W149-T1 Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Claim Decision

W149 closes with a bounded live value claim:

> The expanded 40-template trusted-form front door is live-usable on the Alibaba
> lane under the W149 evidence matrix, with direct API and browser UI journeys
> both producing governed receipts for all 40 forms.

This does not claim perfect reliability, provider parity across the full corpus,
external tool execution, autonomous delegation, or any widening of CVF ADD
runtime behavior.

## Evidence Summary

| Checkpoint | Evidence | Result |
|---|---|---:|
| CP1 corpus lock | `docs/reviews/archive/CVF_W149_TRUSTED_FORM_FULL_CORPUS_LOCK_2026-05-08.md` | 40/40 locked |
| CP2 Alibaba direct API | `docs/reviews/CVF_W149_TRUSTED_FORM_DIRECT_API_ALIBABA_EVIDENCE_2026-05-08.{md,json}` | 40/40 accepted, 40/40 useful |
| CP3 Alibaba browser UI | `docs/reviews/CVF_W149_TRUSTED_FORM_UI_ALIBABA_EVIDENCE_2026-05-08.{md,json}` | 40/40 accepted with receipt |
| CP5 DeepSeek confirmatory | `docs/reviews/CVF_W149_TRUSTED_FORM_DEEPSEEK_CONFIRMATORY_EVIDENCE_2026-05-08.{md,json}` | 12/12 accepted, 12/12 useful |
| CP7 release gate | `python scripts/run_cvf_release_gate_bundle.py --json` | PASS |

## Fixes Delivered

- `src/app/api/execute/route.ts`: trusted-form development templates no longer
  require Skill Preflight solely because the template category is
  `development` or the generated trusted-form intent contains handoff/build
  wording. Explicit BUILD phase still requires Skill Preflight.
- `src/lib/form-routing.ts`: trusted-form membership is now exposed via
  `isTrustedFormTemplateId()`.
- W149 E2E harnesses now lock the 40-form corpus, run direct API and browser UI
  live matrices, capture HTTP diagnostics, and record evidence packets.
- `src/app/(dashboard)/home/page.tsx`: build-only TypeScript narrowing fix for
  history continuation output restoration.

## Verification

- `npx vitest run src/app/api/execute/route.test.ts src/lib/form-routing.test.ts src/lib/intent-router.test.ts`
  - PASS: 130/130
- `npx playwright test tests/e2e/w149-trusted-form-full-corpus-direct-api.live.spec.ts -g "CP2 Alibaba" --workers=1 --reporter=line`
  - PASS: 40/40
- `npx playwright test tests/e2e/w149-trusted-form-full-corpus-ui.live.spec.ts --workers=1 --reporter=line`
  - PASS: 40/40
- `npx playwright test tests/e2e/w149-trusted-form-full-corpus-direct-api.live.spec.ts -g "CP5 DeepSeek" --workers=1 --reporter=line`
  - PASS: 12/12
- `npm run lint`
  - PASS
- `npm run build`
  - PASS
- `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS: Web build, TypeScript guard contract, provider readiness, secrets
    scan, docs governance, UI mock Playwright, and live governance Playwright.

## Continuation

W149 does not require a continuation tranche for trusted-form live usability.
The next roadmap should move to a new operator-selected problem area, or to a
separate reliability/UX improvement tranche if future real traffic identifies a
new measured bottleneck.
