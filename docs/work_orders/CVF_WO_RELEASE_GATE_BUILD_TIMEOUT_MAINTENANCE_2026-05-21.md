# Work Order - Release Gate Build Timeout Maintenance

Memory class: FULL_RECORD

Status: CLOSED_TIMEOUT_MAINTENANCE

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Fix the narrow release-gate build timeout blocker discovered by the hosted
product readiness proof.

---

## Authority Chain

- Roadmap:
  `docs/roadmaps/CVF_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_ROADMAP_2026-05-21.md`
- GC-018:
  `docs/baselines/CVF_GC018_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_2026-05-21.md`
- Hosted readiness completion:
  `docs/reviews/CVF_HOSTED_PRODUCT_READINESS_PROOF_COMPLETION_2026-05-21.md`
- Active state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Agent Roles

Codex performs all roles for this bounded maintenance tranche:

- Orchestrator: keep scope limited to timeout maintenance.
- Reviewer: reject broad release-gate or readiness changes.
- Implementer: patch the timeout and rerun the gate.
- Auditor: file evidence, update continuity, and commit.

---

## Scope / Target / Owner Boundary

Allowed scope:

- `scripts/run_cvf_release_gate_bundle.py` web build timeout only.
- Completion review and active continuity updates.

Forbidden scope:

- app source, provider source, route behavior, test expectation changes,
  deployment config, public-sync, persistence/database, Maika proof, hosted
  SaaS claim, or freeze release.

Risk ceiling: R1.

---

## Operator Checkpoint

Checkpoint source: operator request on 2026-05-21 to handle the tiny timeout
tranche before considering any new tranche.

---

## Write Ownership

Owned by this work order:

- `scripts/run_cvf_release_gate_bundle.py`
- `docs/roadmaps/CVF_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_ROADMAP_2026-05-21.md`
- `docs/baselines/CVF_GC018_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_2026-05-21.md`
- `docs/work_orders/CVF_WO_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_2026-05-21.md`
- `docs/reviews/CVF_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_COMPLETION_2026-05-21.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V11_2026-05-21.md`

---

## Required First Reads

- `docs/reviews/CVF_HOSTED_PRODUCT_READINESS_PROOF_COMPLETION_2026-05-21.md`
- `scripts/run_cvf_release_gate_bundle.py`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Pre-Flight Checks

- Confirm the failure was a timeout, not a build error.
- Confirm direct `npm run build` previously passed.
- Confirm no source-code change is needed.

---

## Execution Plan

1. Change the web build timeout in `check_web_build()` from 300s to 900s.
2. Run `python scripts/run_cvf_release_gate_bundle.py --json`.
3. File completion review.
4. Update active queue/state/handoff.
5. Run governance checks and commit.

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Timeout blocker fixed | release gate `Web build` subcheck PASS |
| Gate remains strict | full release gate PASS, not warning-only |
| Scope stayed narrow | diff only changes build timeout plus docs/session continuity |
| Secrets protected | no raw key/token printed or committed |

---

## Acceptance Criteria

- [x] Timeout changed from 300s to 900s for web build subcheck.
- [x] Full release gate PASS.
- [x] Completion review filed.
- [x] Queue/state/handoff synced.
- [ ] Governance checks PASS.

---

## Review Gate

Close only if the full release gate returns PASS and the diff does not include
runtime, provider, route, deployment, public-sync, or product-scope changes.

---

## Closure Checklist

- [x] GC-018 filed.
- [x] Work order filed.
- [x] Timeout patched.
- [x] Release gate rerun.
- [x] Completion packet filed.
- [x] Continuity updated.
- [ ] Commit created.

---

## Return-To-Orchestrator Conditions

Return instead of closing if:

- release gate still fails after the timeout maintenance;
- the failure requires source-code or product-scope changes;
- the timeout change would mask an actual build failure.

---

## Claim Boundary

This work order closes only release-gate timeout maintenance. It does not
prove hosted SaaS readiness, public deployment readiness, persistence
readiness, Maika readiness, broad provider stability, or freeze release.
