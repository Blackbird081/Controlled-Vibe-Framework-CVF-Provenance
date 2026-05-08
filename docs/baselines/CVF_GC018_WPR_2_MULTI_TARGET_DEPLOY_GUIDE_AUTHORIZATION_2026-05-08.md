<!-- Memory class: FULL_RECORD -->
# CVF GC-018 - WPR-2 Authorization

> Date: 2026-05-08
> Tranche: WPR-2 - Multi-Target Deploy Guide
> Status: AUTHORIZED

## Decision

WPR-2 is authorized as a documentation-only public-release packaging tranche.

## Scope Lock

Allowed:

- Create one canonical deploy guide for local, Netlify, Vercel, and Docker
  posture.
- Cross-link the guide from README and `docs/guides/README.md`.
- Reference existing deploy configs without changing them.
- Run docs hygiene and release gate verification.

Not allowed:

- Deploy CVF to any public host.
- Commit provider keys or create credential files.
- Change runtime behavior, provider routing, Next.js config, build scripts, or
  deployment config.
- Claim Docker is a supported canonical deploy target if no Dockerfile exists.

## Exit Criteria

- `docs/guides/CVF_DEPLOY_GUIDE.md` exists and is under 250 lines.
- Netlify and Vercel sections match current checked-in config files.
- README quick-run/new-machine surfaces point to the guide.
- `git diff --check` passes.
- `python scripts/run_cvf_release_gate_bundle.py --json` passes.
