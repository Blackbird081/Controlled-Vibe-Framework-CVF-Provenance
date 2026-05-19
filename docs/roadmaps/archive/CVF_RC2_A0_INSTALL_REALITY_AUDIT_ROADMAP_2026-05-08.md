<!-- Memory class: FULL_RECORD -->
# CVF RC2-A0 Install Reality Audit Roadmap

> Authorization: `docs/baselines/CVF_GC018_RC2_A0_INSTALL_REALITY_AUDIT_AUTHORIZATION_2026-05-08.md`
> Track: RC2 Foundation / A — Install Productization
> Status: CLOSED DELIVERED

## Purpose

Classify what a fresh Windows clone actually needs before CVF can offer a
guided first-run path.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and A0 scope lock |
| CP1 | Create clean Windows fresh clone probe |
| CP2 | Record dependency, env, port, and writable-state readiness |
| CP3 | Classify findings as `BLOCKER`, `WARNING`, `OPTIONAL`, or `DEFERRED_PLATFORM` |
| CP4 | Publish audit and closure decision |

## Exit Criteria

- Fresh clone path recorded.
- Node/npm/Python readiness recorded.
- `cvf-web` package and lockfile readiness recorded.
- Provider-key and env-template status recorded without raw secrets.
- A1/A2 follow-up blockers are explicit.

## Closure Result

RC2-A0 closed on 2026-05-08.

Audit:
`docs/reviews/CVF_RC2_INSTALL_REALITY_AUDIT_2026-05-08.md`

Closure:
`docs/reviews/CVF_RC2_A0_INSTALL_REALITY_AUDIT_CLOSURE_DECISION_2026-05-08.md`
