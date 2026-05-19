<!-- Memory class: FULL_RECORD -->
# CVF Static CI Gate Roadmap

**Date:** 2026-05-08  
**Track:** RC2 Pre-GA / CI1  
**Status:** CLOSED DELIVERED  
**Authorization:** `docs/baselines/CVF_GC018_RC2_CI1_STATIC_CI_GUARDRAILS_CANDIDATE_2026-05-08.md`

## Purpose

Install a non-secret static CI lane before post-RC2 non-coder regression
evidence is collected.

## Scope

### CI1.0 — Design

Define the static gate:

- no provider secrets;
- no live provider calls;
- no release-quality governance claim;
- build/type/static governance protection only.

Artifact:

`docs/reviews/CVF_STATIC_CI_GATE_DESIGN_2026-05-08.md`

### CI1.1 — Implementation

Deliver:

- `scripts/run_cvf_static_ci_gate.py`;
- `.github/workflows/cvf-static-ci.yml`;
- static gate evidence artifact.

Checks:

- Web build;
- Web TypeScript check;
- repository secrets scan;
- docs governance compatibility;
- targeted static governance/unit tests.

Artifact:

`docs/reviews/CVF_STATIC_CI_GATE_EVIDENCE_2026-05-08.md`

## Stop Rules

Stop if:

- a check requires a live provider key;
- the gate calls `scripts/run_cvf_release_gate_bundle.py` default live mode;
- raw secret values would be printed;
- CI wording implies live governance proof;
- the implementation modifies runtime behavior outside static gate plumbing.

## Exit Claim

Allowed:

> CVF has a default static CI lane that protects build, type, secret-scan, docs,
> and static/unit checks without requiring provider secrets.

Forbidden:

- CI proves live governance.
- PRs run release-quality proof.
- R1/R2 regression is complete.

## Closure

CI1 is delivered.

Evidence:

`docs/reviews/CVF_STATIC_CI_GATE_EVIDENCE_2026-05-08.md`
