<!-- Memory class: FULL_RECORD -->
# CVF RC2-A2 Guided First-Run Setup Roadmap

> Authorization: `docs/baselines/CVF_GC018_RC2_A2_GUIDED_FIRST_RUN_SETUP_AUTHORIZATION_2026-05-08.md`
> Track: RC2 Foundation / A — Install Productization
> Status: CLOSED DELIVERED

## Purpose

Provide a guided first-run path that connects fresh clone readiness, env setup,
dependency guidance, provider readiness, Web start instructions, and first
governed-run guidance.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and A2 scope lock |
| CP1 | Add `scripts/cvf_setup.py` orchestrator |
| CP2 | Add short "5-minute RC setup" guide |
| CP3 | Link guide from README and guides index |
| CP4 | Verify setup paths on configured Windows workspace |
| CP5 | Publish closure and handoff sync |

## Exit Criteria

- Setup script can produce JSON and human-readable guidance.
- Setup script can create `.env.local` from `.env.example` when requested.
- Setup script can optionally run dependency install.
- Setup script delegates provider readiness to A1 provider check.
- Guide keeps live governance proof boundary explicit.

## Closure Result

RC2-A2 closed on 2026-05-08.

Closure:
`docs/reviews/CVF_RC2_A2_GUIDED_FIRST_RUN_SETUP_CLOSURE_DECISION_2026-05-08.md`
