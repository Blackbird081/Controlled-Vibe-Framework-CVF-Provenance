# CVF Hosted Product Readiness Proof Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_LOCAL_PRODUCTION_PROOF

docType: roadmap

Date: 2026-05-21

---

## Purpose

Define one shallow, high-signal product-readiness proof after CDH-D vision route
wiring closure.

This roadmap intentionally avoids a broad hosted-readiness program. It asks
only whether CVF can run through a production-mode web server and return a live
governance receipt from the existing `/api/execute` path.

---

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Post Phase 2.B publicization/readiness completion:
  `docs/reviews/CVF_POST_PHASE_2B_PUBLICIZATION_READINESS_COMPLETION_2026-05-21.md`
- Provider stability hardening completion:
  `docs/reviews/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_COMPLETION_2026-05-21.md`
- CDH-D vision route wiring completion:
  `docs/reviews/CVF_CDH_D_VISION_ROUTE_WIRING_COMPLETION_2026-05-21.md`
- Deploy guide:
  `docs/guides/CVF_DEPLOY_GUIDE.md`

---

## Authorization / Decision

Operator decision on 2026-05-21:

- continue the next roadmap;
- avoid deep, low-value tranches;
- allow API-key use for live proof.

Decision: proceed only with the smallest production-mode proof that can either
close a local product-readiness evidence gap or identify a blocker.

---

## Scope / Target / Owner Boundary

Target:

- HPR-01 local production build proof.
- HPR-02 local production server live `/api/execute` governance proof.
- HPR-03 service-token and live-key diagnostic boundary.
- HPR-04 mandatory release gate.

In scope:

- Use `npm run build` and `npm run start` from `cvf-web`.
- Load operator-supplied keys from approved local environment only.
- Call the existing `/api/execute` route with signed service-token headers.
- Record HTTP status, success flag, decision, evidence mode, provider, model,
  receipt id, trace id, and whether raw secrets were printed.

Out of scope:

- New deployment target, tunnel, Netlify/Vercel push, or public-sync update.
- Provider runtime changes, route changes, UI changes, CLI changes, SSE work,
  database/persistence work, Maika proof, child-data/photo proof, kernel-owner
  replacement, one-surface freeze release, or global freeze lift.

---

## Non-Goals

- Do not perform a public deployment.
- Do not claim hosted SaaS or multi-tenant readiness.
- Do not update public-sync.
- Do not modify application/runtime/provider source.
- Do not add persistence, database, Maika, UI, CLI, SSE, or provider features.
- Do not use this proof to lift any governance-kernel freeze.

---

## Agent Roles

Codex performs the bounded workflow roles:

- Orchestrator: open the roadmap and keep the proof shallow.
- Reviewer: reject broad hosted/product claims and verify predecessor evidence.
- Governance Owner: file GC-018 and work order before proof execution.
- Implementer: run production build/start and live receipt probe.
- Auditor: file completion, update continuity, and run guards.

---

## Work Plan

1. File GC-018 and work order.
2. Run `npm run build` in `cvf-web`.
3. Start `npm run start` on a local production-mode port.
4. Send one signed service-token live `/api/execute` request.
5. Run the mandatory release gate.
6. File completion evidence and update continuity.
7. Run governance checks and commit.

---

## Verification / Evidence

Evidence must include:

- build result;
- server reachability;
- live `/api/execute` response facts;
- release-gate result;
- confirmation that raw API keys and service token values were not printed or
  committed.

---

## Acceptance Criteria

- `npm run build` passes for `cvf-web`.
- `npm run start` serves the built app on a local production-mode port.
- A signed service-token call to `/api/execute` returns HTTP 200,
  `success=true`, decision `ALLOW`, `evidenceMode=live`, provider/model,
  receipt id, and trace id.
- `python scripts/run_cvf_release_gate_bundle.py --json` passes.
- No raw API key or service token is printed or committed.

---

## Claim Boundary

This roadmap can close only a local production-mode product-readiness proof.
It does not prove hosted SaaS readiness, public deployment readiness,
multi-tenant readiness, database persistence readiness, Maika readiness, broad
provider stability, or any freeze release.
