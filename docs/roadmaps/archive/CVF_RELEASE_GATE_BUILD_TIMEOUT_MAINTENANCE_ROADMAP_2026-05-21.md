# CVF Release Gate Build Timeout Maintenance Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_TIMEOUT_MAINTENANCE

docType: roadmap

Date: 2026-05-21

---

## Purpose

Close the narrow timeout blocker discovered by the Hosted Product Readiness
Proof without opening a broader readiness tranche.

The prior proof showed that `npm run build` passed directly but the release
gate runner failed its build subcheck at the hard-coded 300s timeout. This
roadmap authorizes only aligning the release-gate build timeout with observed
Next.js production build duration.

---

## Authority Chain

- Hosted readiness completion:
  `docs/reviews/CVF_HOSTED_PRODUCT_READINESS_PROOF_COMPLETION_2026-05-21.md`
- Hosted readiness work order:
  `docs/work_orders/CVF_WO_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- Release gate runner:
  `scripts/run_cvf_release_gate_bundle.py`
- Active state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Authorization / Decision

Operator decision on 2026-05-21:

- handle the small release-gate timeout maintenance before considering any new
  tranche;
- keep the work compact;
- commit the result.

Decision: proceed with a tiny maintenance tranche limited to the release-gate
web build timeout.

---

## Scope / Target / Owner Boundary

In scope:

- update only the `Web build (npm run build)` timeout in
  `scripts/run_cvf_release_gate_bundle.py`;
- rerun `python scripts/run_cvf_release_gate_bundle.py --json`;
- file completion and active continuity updates.

Out of scope:

- changing provider checks, Playwright checks, governance semantics, app
  source, route behavior, deployment config, public-sync, persistence/database,
  Maika proof, hosted SaaS claim, or freeze release.

---

## Non-Goals

- Do not make builds faster.
- Do not weaken release-gate requirements.
- Do not convert failures into warnings.
- Do not add a new readiness claim unless the unchanged gate passes.

---

## Work Plan

1. File GC-018 and work order.
2. Change only the release-gate web build timeout from 300s to 900s.
3. Run the full release gate bundle with live provider evidence.
4. File completion with evidence.
5. Update queue/state/handoff.
6. Run governance checks and commit.

---

## Verification / Evidence

Required evidence:

- diff shows only the intended timeout change in the runner;
- `python scripts/run_cvf_release_gate_bundle.py --json` returns PASS;
- no raw secrets are printed;
- governance checks pass.

---

## Acceptance Criteria

- Web build subcheck timeout is raised from 300s to 900s.
- Full release gate returns PASS.
- No release-gate requirement is weakened or converted to a warning.
- Completion packet records the exact result.

---

## Claim Boundary

This roadmap can close only release-gate timeout maintenance and may unblock
the previously returned local production-mode readiness proof. It does not
prove external hosted SaaS readiness, public deployment readiness,
multi-tenant readiness, persistence readiness, Maika readiness, broad provider
stability, or freeze release.
