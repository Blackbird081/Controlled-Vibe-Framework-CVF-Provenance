<!-- Memory class: FULL_RECORD -->
# CVF WPR-2 Multi-Target Deploy Guide Roadmap

> Authorization: `docs/baselines/CVF_GC018_WPR_2_MULTI_TARGET_DEPLOY_GUIDE_AUTHORIZATION_2026-05-08.md`
> Wave ID: WPR-2
> Status: CLOSED DELIVERED

## Purpose

CVF has local, Netlify, and Vercel deploy hints, but they are scattered across
README and package-specific config files. WPR-2 creates one public guide so
community users know how to run or host the web app without leaking keys or
mistaking UI mock checks for governance proof.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and docs-only scope lock |
| CP1 | Inspect checked-in deploy configs |
| CP2 | Create deploy guide |
| CP3 | Cross-link public guide surfaces |
| CP4 | Verify guide size, diff hygiene, and release gate |
| CP5 | Closure decision and commit |

## Claim Boundary

WPR-2 may claim that CVF has a canonical public deploy guide. It does not claim
that CVF has been deployed by this tranche, that Docker is canonical, or that a
hosted instance proves governance behavior without live provider evidence.

## Exit Criteria

- Guide remains under 250 lines.
- Existing Netlify/Vercel config is represented accurately.
- Release gate remains PASS.

## Closure Result

WPR-2 closed on 2026-05-08. The deploy guide exists, README and guides index
link to it, current Netlify/Vercel config values are represented, Docker is
correctly marked non-canonical, `git diff --check` passed, and the release gate
passed.

Closure decision:
`docs/reviews/CVF_WPR_2_MULTI_TARGET_DEPLOY_GUIDE_CLOSURE_DECISION_2026-05-08.md`.
