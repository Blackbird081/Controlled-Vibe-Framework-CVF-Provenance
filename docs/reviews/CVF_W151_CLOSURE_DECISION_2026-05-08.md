<!-- Memory class: FULL_RECORD -->
# CVF W151-T1 Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

W151 closes as a no-behavior-change test maintainability tranche.

Trusted-form activation coverage is now data-driven in
`src/lib/trusted-form-corpus.test.ts`, while `src/lib/form-routing.test.ts`
focuses on router behavior, wizard non-overlap, flag posture, and
`routeIntent()` integration.

## What Changed

- `form-routing.test.ts` reduced from 731 lines to 153 lines.
- New `trusted-form-corpus.test.ts` holds the 40-form EN/VN activation matrix.
- Activation coverage remains explicit for every trusted form and language lane.
- No trusted-form ids, activation regexes, wizard precedence, provider behavior,
  or governance policy were intentionally changed.

## Verification

- `npx vitest run src/lib/form-routing.test.ts src/lib/trusted-form-corpus.test.ts src/lib/intent-router.test.ts src/app/api/execute/route.test.ts`
  - PASS: 131/131
- `npm run lint`
  - PASS
- `npm run build`
  - PASS
- `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS: Web build, TypeScript guard contract, provider readiness, secrets
    scan, docs governance, UI mock Playwright, and live governance Playwright.

## Boundary

W151 does not create a new live usability claim. W149 remains the live value
baseline for the 40-form trusted-form corpus, and W150 remains the router/corpus
source split baseline.
