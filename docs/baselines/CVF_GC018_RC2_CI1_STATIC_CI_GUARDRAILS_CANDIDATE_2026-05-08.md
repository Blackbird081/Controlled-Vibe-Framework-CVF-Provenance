<!-- Memory class: FULL_RECORD -->
# CVF GC-018 — RC2 CI1 Static CI Guardrails Candidate

**Date:** 2026-05-08  
**Track:** RC2 Pre-GA / CI1  
**Status:** AUTHORIZED FOR IMPLEMENTATION  
**Source roadmap:** `docs/roadmaps/CVF_RC2_PRE_GA_VALIDATION_AND_C5_READINESS_ROADMAP_V2_2026-05-08.md`

## Decision

Authorize CI1 implementation: a default static CI gate that requires no live
provider key and makes no live governance claim.

## Scope

Allowed:

- add a static CI workflow;
- add a local static gate runner script;
- run Web build;
- run Web TypeScript check;
- run repository secrets scan;
- run docs governance compatibility check;
- run static/unit governance checks already available in `cvf-web`;
- file design and evidence artifacts.

Forbidden:

- live provider calls;
- full release gate execution;
- Web-triggered release gate implementation;
- C5.2+ runtime work;
- R1/R2 non-coder regression claims;
- any CI claim that PR checks prove live governance.

## Exit Claim

Allowed after closure:

> CVF has a default static CI lane that protects build, type, secret-scan, docs,
> and static/unit governance checks without requiring provider secrets.

Still forbidden:

- CI proves live governance.
- Post-RC2 non-coder no-regression is proven.
- Web can trigger the full live release gate.
- CVF is GA-ready.
