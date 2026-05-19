<!-- Memory class: FULL_RECORD -->
# CVF GC-018 - W151-T1 Authorization

> Date: 2026-05-08
> Tranche: W151-T1 - Trusted Form Test Maintainability Hardening
> Status: AUTHORIZED

## Decision

W151 is authorized as a narrow no-behavior-change test maintainability tranche
after W150.

## Scope Lock

Allowed:

- Split trusted-form activation coverage out of `form-routing.test.ts`.
- Convert repetitive activation tests to a data-driven matrix.
- Preserve tested prompts, expected template ids, and route behavior.
- Run targeted routing tests, lint/build, and release gate.

Not allowed:

- Add or remove trusted forms.
- Change activation regexes, wizard/form precedence, provider behavior, or
  governance policy.
- Create a new live value claim beyond W149.

## Exit Criteria

- Existing trusted-form routing behavior remains covered.
- `form-routing.test.ts` drops well below advisory size.
- New corpus activation test file is clear, bounded, and data-driven.
- Release gate remains PASS.
