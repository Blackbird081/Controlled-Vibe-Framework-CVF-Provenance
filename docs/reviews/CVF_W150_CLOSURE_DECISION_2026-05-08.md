<!-- Memory class: FULL_RECORD -->
# CVF W150-T1 Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

W150 closes as a no-behavior-change maintainability tranche.

The trusted-form router API remains available from `src/lib/form-routing.ts`,
while the 40-form corpus data now lives in
`src/lib/trusted-form-corpus.ts`.

## What Changed

- `form-routing.ts` is reduced to routing behavior and public exports.
- `trusted-form-corpus.ts` owns `TrustedFormEntry` and `TRUSTED_FORM_MAP`.
- Existing consumers keep importing from `form-routing.ts`.
- No activation pattern, template id, label, wizard precedence, provider
  behavior, or governance execution policy was intentionally changed.

## File-Size Posture

| File | Lines After W150 | Posture |
|---|---:|---|
| `src/lib/form-routing.ts` | 56 | Router API only |
| `src/lib/trusted-form-corpus.ts` | 589 | Corpus data |
| `src/lib/form-routing.test.ts` | 731 | Under test-code advisory threshold |

## Verification

- `npx vitest run src/lib/form-routing.test.ts src/lib/intent-router.test.ts src/app/api/execute/route.test.ts`
  - PASS: 130/130
- `npx playwright test tests/e2e/w149-trusted-form-full-corpus-direct-api.live.spec.ts -g "CP1 corpus" --workers=1 --reporter=line`
  - PASS: 1/1 corpus compatibility
- `npm run lint`
  - PASS
- `npm run build`
  - PASS
- `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS: Web build, TypeScript guard contract, provider readiness, secrets
    scan, docs governance, UI mock Playwright, and live governance Playwright.

## Boundary

W150 does not create a new live usability claim. W149 remains the live value
baseline for the 40-form trusted-form corpus.
