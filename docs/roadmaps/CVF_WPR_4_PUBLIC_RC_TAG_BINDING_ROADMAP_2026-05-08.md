<!-- Memory class: FULL_RECORD -->
# CVF WPR-4 Public RC Tag Binding Roadmap

> Authorization: `docs/baselines/CVF_GC018_WPR_4_PUBLIC_RC_TAG_BINDING_AUTHORIZATION_2026-05-08.md`
> Wave ID: WPR-4
> Status: CLOSED DELIVERED

## Purpose

CVF has RC truth packets and WPR-1 through WPR-3 public-release packaging
artifacts, but the repository still needs a concrete git tag so community users
can identify the exact release-candidate revision.

## Checkpoints

| CP | Work |
|---|---|
| CP0 | GC-018 authorization and tag-binding scope lock |
| CP1 | Update changelog and README badge |
| CP2 | Create release notes draft |
| CP3 | Update handoff to RC1 tagged posture |
| CP4 | Verify diff hygiene and release gate |
| CP5 | Commit, create annotated tag, and push commit/tag |

## Claim Boundary

WPR-4 may claim `v4.0.0-rc.1` is a release candidate tag. It may not claim GA,
provider parity, universal skill trust, or a hosted GitHub Release unless that
publication is performed by a valid operator/CLI path.

## Exit Criteria

- Changelog, README badge, release notes, and handoff are synchronized.
- Release gate remains PASS.
- Annotated tag exists.

## Closure Result

WPR-4 closed on 2026-05-08. Changelog, README badge, release notes draft, and
handoff are synchronized to `v4.0.0-rc.1`; `git diff --check` passed; release
gate passed; annotated tag creation is part of the final commit/tag step.

Closure decision:
`docs/reviews/CVF_WPR_4_PUBLIC_RC_TAG_BINDING_CLOSURE_DECISION_2026-05-08.md`.
