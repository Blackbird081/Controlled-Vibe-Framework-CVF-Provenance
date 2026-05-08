<!-- Memory class: FULL_RECORD -->
# CVF WPR-2 Multi-Target Deploy Guide Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

WPR-2 closes as a documentation-only public-release packaging tranche.

CVF now has one public deploy guide for local development, local production
build, Netlify, Vercel, Docker posture, environment variable handling, and
post-deploy verification.

## Updates

- `docs/guides/CVF_DEPLOY_GUIDE.md` created.
- `README.md` links the guide from Quick Run and New Machine setup surfaces.
- `docs/guides/README.md` lists the deploy guide in the guide index.

## Verification

- `docs/guides/CVF_DEPLOY_GUIDE.md`
  - PASS: 161 lines, under the WPR-2 250-line target.
- Existing deploy config represented:
  - Netlify: `netlify.toml` and package-local `netlify.toml`.
  - Vercel: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vercel.json`.
  - Docker: no Dockerfile exists, so Docker is recorded as non-canonical.
- `git diff --check`
  - PASS.
- `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS: Web build, TypeScript guard contract, provider readiness, secrets
    scan, docs governance, UI mock Playwright, and live governance Playwright.

## Boundary

WPR-2 changes no runtime behavior, provider routing, deployment config,
credential handling, build scripts, CI hooks, or release tag state.

WPR-3 remains the next recommended public-release packaging wave: public
exposure audit.
