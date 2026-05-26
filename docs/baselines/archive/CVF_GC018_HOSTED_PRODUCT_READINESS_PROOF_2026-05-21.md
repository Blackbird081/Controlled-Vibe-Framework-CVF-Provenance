# CVF GC-018 Hosted Product Readiness Proof

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_LOCAL_PRODUCTION_PROOF

docType: baseline

Date: 2026-05-21

---

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- `docs/reviews/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_COMPLETION_2026-05-21.md`
- `docs/reviews/CVF_CDH_D_VISION_ROUTE_WIRING_COMPLETION_2026-05-21.md`
- `docs/guides/CVF_DEPLOY_GUIDE.md`

---

## Purpose / Decision / Baseline

Decision: ACCEPTED for one bounded local production-mode proof.

The proof may use operator-supplied provider keys and service token from
approved local environment files. Raw key values must not be printed, copied
into evidence, or committed.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: Hosted Product Readiness Proof, limited to local
production-mode operation.

Accepted work:

- run `cvf-web` production build;
- start the built app with `npm run start` on a local port;
- call the existing `/api/execute` route with signed service-token headers and
  live provider execution;
- run the mandatory release gate;
- file completion evidence and continuity updates.

---

## Scope / Proposed Tranche

In scope:

- documentation artifacts for this tranche;
- local production build/start evidence;
- one live governed `/api/execute` proof;
- release gate output;
- active queue/state/handoff continuity.

Out of scope:

- source-code changes;
- new deploy target, tunnel, or public hosting action;
- public-sync update;
- provider runtime changes;
- persistence/database implementation;
- Maika child-data/photo/vision proof;
- kernel owner replacement or freeze release.

---

## Evidence / Required Evidence / Verification

Required evidence:

- `npm run build` PASS;
- `npm run start` reachable on local production-mode port;
- live `/api/execute` proof returns HTTP 200, `success=true`,
  decision `ALLOW`, `evidenceMode=live`, provider, model, receipt id, trace id;
- `python scripts/run_cvf_release_gate_bundle.py --json` PASS;
- secrets are redacted and not committed;
- governance checks pass.

---

## Claim Boundary

This GC-018 authorizes only a local production-mode proof. It does not close
hosted SaaS readiness, external deployment readiness, persistence readiness,
Maika readiness, broad provider stability, or any public product claim.
