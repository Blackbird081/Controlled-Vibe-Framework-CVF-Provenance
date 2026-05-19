<!-- Memory class: FULL_RECORD -->
# CVF GC-018 - WPR-4 Authorization

> Date: 2026-05-08
> Tranche: WPR-4 - Public RC Tag + Changelog Binding
> Status: AUTHORIZED

## Decision

WPR-4 is authorized as the release-candidate tag binding tranche after WPR-3
closed without unresolved blockers.

## Scope Lock

Allowed:

- Update `CHANGELOG.md` with `v4.0.0-rc.1`.
- Update the README version badge to the RC label.
- Create in-repo release notes for `v4.0.0-rc.1`.
- Update `AGENT_HANDOFF.md` with `RC1 TAGGED` state.
- Create annotated git tag `v4.0.0-rc.1` after verification.
- Push commits and the tag to `origin/main`.

Not allowed:

- Claim GA release.
- Publish a GitHub Release through an unavailable CLI/token path.
- Change runtime behavior, provider behavior, deploy config, or governance
  policy.
- Rewrite RC truth, live evidence, or known-limitations packets.

## Exit Criteria

- `CHANGELOG.md` contains a `v4.0.0-rc.1` entry.
- README version badge points to `4.0.0-rc.1`.
- Release notes draft exists in repo.
- Handoff says `RC1 TAGGED`.
- `git diff --check` passes.
- `python scripts/run_cvf_release_gate_bundle.py --json` passes.
- Annotated tag `v4.0.0-rc.1` exists.
