# CVF Work Order: O4 Release Gate E2E Selector Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: O4

Roadmap: `docs/roadmaps/CVF_POST_AIF_OPERATIONALIZATION_ROADMAP_2026-05-24.md`

---

## Purpose

Harden stale Playwright release-gate selectors exposed during the Post-AIF
operationalization full release-gate run. The failure was in UI selector
stability, not LPF runtime behavior.

---

## Authorization

O4 is corrective QA work under the operator-authorized Post-AIF
operationalization workflow. It changes tests only and does not require a
separate GC-018.

---

## Authority Chain

Operator -> Codex QA -> Codex Release Manager.

---

## Agent Roles

- QA: inspect release-gate failure artifacts and harden selectors.
- Release Manager: rerun targeted/full gates and record evidence.

---

## Owner / Source

Owner: Codex as QA and Release Manager.

Source:

- `python scripts/run_cvf_release_gate_bundle.py --json` initial E2E failures.
- Error contexts under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/test-results/`.

---

## Required First Reads

- `scripts/run_cvf_release_gate_bundle.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/admin-rbac.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/noncoder-governance-live.spec.ts`

---

## Pre-Flight Checks

- Confirm failures are selector/test-harness issues, not LPF runtime changes.
- Confirm no UI source files need modification.
- Confirm live governance assertions remain intact.

---

## Write Ownership

Codex owns only the two Playwright spec updates and O4 closure docs.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/noncoder-governance-live.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/admin-rbac.spec.ts`

Out of scope:

- UI redesign.
- Runtime route/provider behavior.
- Governance receipt or policy changes.
- Public-sync, hosted readiness, production readiness, or freeze release.

---

## Execution Plan

1. Replace stale structural selector for the template gallery with a semantic
   role/text selector for the current governed template button.
2. Make the admin FinOps assertion wait for route settling and accept the
   existing heading/text variants.
3. Rerun targeted `--e2e` and `--e2e-live` release-gate modes.
4. Rerun full release gate.

---

## Evidence Requirements

- `--e2e` release-gate mode passes.
- `--e2e-live` release-gate mode passes.
- Full release gate passes.

---

## Acceptance Criteria

- [x] No UI/runtime behavior changes.
- [x] Targeted mock E2E release-gate mode PASS.
- [x] Targeted live E2E release-gate mode PASS.
- [x] Full release gate PASS.

---

## Risk / Corrective Action

Risk: selectors become too broad. Corrective action: selectors remain scoped to
existing visible role/text landmarks and do not bypass governance assertions.

---

## Review Gate

O4 can close only if targeted and full release-gate commands pass.

---

## Closure Checklist

- [x] Selector updates complete.
- [x] `--e2e` PASS.
- [x] `--e2e-live` PASS.
- [x] Full release gate PASS.

---

## Return-To-Orchestrator Conditions

Return if a selector fix would require UI/runtime behavior changes.

---

## Operator Checkpoint

Operator authorization was provided in-session on 2026-05-24 for Codex to
create and execute the roadmap/work orders.

---

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS.

---

## Claim Boundary

O4 proves release-gate selector stability only. It does not prove new UI
behavior, provider stability, hosted readiness, production readiness, or freeze
release.
