<!-- Memory class: FULL_RECORD -->
# CVF Static CI Gate Evidence

**Date:** 2026-05-08  
**Track:** RC2 Pre-GA / CI1  
**Status:** CLOSED DELIVERED  
**Authorization:** `docs/baselines/CVF_GC018_RC2_CI1_STATIC_CI_GUARDRAILS_CANDIDATE_2026-05-08.md`

## Delivered

CI1 adds a non-secret static gate:

- local runner: `scripts/run_cvf_static_ci_gate.py`;
- GitHub workflow: `.github/workflows/cvf-static-ci.yml`;
- design artifact: `docs/reviews/CVF_STATIC_CI_GATE_DESIGN_2026-05-08.md`;
- roadmap: `docs/roadmaps/archive/CVF_STATIC_CI_GATE_ROADMAP_2026-05-08.md`.

## Local Verification

Command:

```bash
python scripts/run_cvf_static_ci_gate.py --json
```

Result:

```json
{
  "date": "2026-05-08",
  "gate": "cvf_static_ci_gate",
  "live_provider_use": false,
  "gate_result": "PASS",
  "checks": [
    {
      "name": "Web build (npm run build)",
      "status": "PASS",
      "message": "Build succeeded"
    },
    {
      "name": "Web TypeScript check",
      "status": "PASS",
      "message": "Web TypeScript check clean"
    },
    {
      "name": "Secrets scan",
      "status": "PASS",
      "message": "No secret patterns detected"
    },
    {
      "name": "Docs governance compatibility",
      "status": "PASS",
      "message": "Docs governance compatibility passed",
      "detail": ["range=HEAD..HEAD"]
    },
    {
      "name": "Static governance/unit tests",
      "status": "PASS",
      "message": "Static governance/unit tests passed",
      "detail": ["42 passed"]
    }
  ]
}
```

## CI Boundary

The workflow does not require provider secrets and does not run live provider
calls. It installs local dependencies, then runs:

```bash
python scripts/run_cvf_static_ci_gate.py --json
```

This is not a substitute for:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

## Exit Claim

Allowed:

> CVF has a default static CI lane that protects build, type, secret-scan, docs,
> and static/unit checks without requiring provider secrets.

Still forbidden:

- CI1 proves live governance.
- PR checks are release-quality proof.
- Post-RC2 non-coder no-regression is proven.
- CI1 by itself proves Web-triggered full live release gate behavior.
- CVF is GA-ready.
