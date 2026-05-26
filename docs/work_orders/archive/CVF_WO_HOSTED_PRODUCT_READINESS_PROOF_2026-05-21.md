# Work Order - Hosted Product Readiness Proof

Memory class: FULL_RECORD

Status: CLOSED_LOCAL_PRODUCTION_PROOF

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Execute the bounded hosted/product-readiness proof accepted by GC-018 without
opening a deeper product tranche.

---

## Authority Chain

- Roadmap:
  `docs/roadmaps/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- GC-018:
  `docs/baselines/CVF_GC018_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- Deploy guide:
  `docs/guides/CVF_DEPLOY_GUIDE.md`
- Active state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Agent Roles

Codex performs all roles for this bounded tranche:

- Orchestrator: confirm the tranche is limited to proof, not implementation.
- Reviewer: reject broad hosted/product claims.
- Implementer: run build/start and live proof.
- Auditor: file evidence and run guards.

---

## Scope / Target / Owner Boundary

Allowed scope:

- `cvf-web` production build.
- `cvf-web` production-mode local server.
- Signed service-token `/api/execute` live proof.
- Mandatory release gate.
- Completion review and session continuity updates.

Forbidden scope:

- Source-code changes.
- New deployment target, public tunnel, Netlify/Vercel push, public-sync
  update, Dockerfile, database/persistence work, Maika proof, provider runtime
  change, UI/CLI/SSE change, kernel-owner replacement, or freeze release.

Risk ceiling: R2.

---

## Operator Checkpoint

Checkpoint source: operator approved the shallow next-roadmap workflow on
2026-05-21 and allowed API-key use. This permits live provider proof using
approved local environment variables only.

---

## Write Ownership

Owned by this work order:

- `docs/roadmaps/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- `docs/baselines/CVF_GC018_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- `docs/work_orders/CVF_WO_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- `docs/reviews/CVF_HOSTED_PRODUCT_READINESS_PROOF_COMPLETION_2026-05-21.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Not owned:

- application source files;
- provider runtime files;
- public-sync files;
- deployment platform configuration.

---

## Execution Plan

1. Run `npm run build` in `cvf-web`.
2. Start the built app with `npm run start` on a local production-mode port.
3. Send one signed service-token request to `/api/execute` using live Alibaba
   execution.
4. Record redacted response facts: HTTP status, success, decision,
   evidence mode, provider, model, receipt id, trace id.
5. Stop the local production server.
6. Run `python scripts/run_cvf_release_gate_bundle.py --json`.
7. File completion review and update continuity.
8. Run governance checks and commit.

---

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/roadmaps/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- `docs/baselines/CVF_GC018_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- `docs/guides/CVF_DEPLOY_GUIDE.md`
- `scripts/run_cvf_release_gate_bundle.py`

---

## Pre-Flight Checks

- Confirm approved local env contains live provider key aliases and
  `CVF_SERVICE_TOKEN` without printing values.
- Confirm no source-code files are required for the proof.
- Confirm the selected local production-mode port is free.
- Run markdown structural completeness before staging.

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Production build works | `npm run build` exits 0 |
| Production server is reachable | `npm run start` serves local port |
| Live governed product-like path works | `/api/execute` returns HTTP 200, success true, ALLOW, live evidence mode, receipt id, trace id |
| Mandatory release gate remains green | `python scripts/run_cvf_release_gate_bundle.py --json` PASS |
| Secrets are protected | no raw key/token printed or committed |

---

## Acceptance Criteria

- [x] Build PASS.
- [x] Production-mode server reachable.
- [x] Live `/api/execute` proof PASS.
- [x] Release gate PASS.
- [x] Completion packet filed.
- [x] Active queue/state/handoff synced.
- [x] Governance checks PASS.

---

## Review Gate

Close only if build, local production server reachability, live governed
receipt proof, mandatory release gate, and governance checks all pass. If any
proof requires source or deployment changes, return to Orchestrator instead.

---

## Closure Checklist

- [ ] Roadmap filed.
- [ ] GC-018 accepted.
- [ ] Work order filed.
- [ ] Production build run.
- [ ] Production server proof run.
- [ ] Live receipt captured.
- [ ] Release gate run.
- [ ] Completion review filed.
- [ ] Queue/state/handoff updated.

---

## Return-To-Orchestrator Conditions

Return instead of closing if:

- production build fails;
- production server cannot start;
- live proof returns non-200, mock evidence, missing receipt, or missing trace;
- release gate fails;
- any required proof would require source-code changes or public deployment.

---

## Claim Boundary

This work order closes only local production-mode product-readiness proof. It
does not authorize or prove hosted SaaS readiness, public deployment readiness,
persistence readiness, Maika readiness, or broad provider stability.
