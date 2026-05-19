<!-- Memory class: FULL_RECORD -->
# CVF GC-018 - W150-T1 Authorization

> Date: 2026-05-08
> Tranche: W150-T1 - Trusted Form Router Maintainability Hardening
> Status: AUTHORIZED

## Decision

W150 is authorized as a narrow post-W149 hardening tranche.

## Scope Lock

Allowed:

- Split trusted-form corpus data from router behavior.
- Preserve the existing public import surface from `src/lib/form-routing.ts`.
- Add documentation proving no intended routing behavior change.
- Run targeted routing/type/lint/build verification.
- Run release gate if any closure claim touches routing/governance behavior.

Not allowed:

- Add new templates or activation patterns.
- Change wizard/form precedence.
- Change provider behavior, CVF ADD runtime behavior, or execution policy.
- Claim new live value beyond W149 evidence.

## Exit Criteria

- Existing routing tests remain green.
- Existing W149 corpus lock remains compatible.
- `form-routing.ts` is reduced to router API behavior, not the full corpus data.
- Closure packet records file-size posture and no-behavior-change boundary.
