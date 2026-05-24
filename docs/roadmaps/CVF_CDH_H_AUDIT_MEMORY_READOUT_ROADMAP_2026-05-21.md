# CVF CDH-H Audit Memory Readout Hardening Roadmap

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: roadmap

Date: 2026-05-21

---

## Purpose

Surface audit-memory policy fields in route-level readout output, prove
`canReinject=false` remains binding after Phase 2.B changes, and prove
degraded-capture reason is visible in receipt output.

---

## Authorization

Authorized by:

- CDH-H delta rebuttal:
  `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- CDH delta meta-roadmap:
  `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- H2 prior closure:
  `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
- Phase 2.B memory tail adapters:
  `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`

This roadmap requires a fresh CDH-H GC-018 before implementation begins.

---

## Why

H2 closed the core policy-field surfacing delta: `AuditMemoryReceipt`
already includes `writesRequireReceipt` and `privacyFilters`. The no-
reinjection invariant is preserved (`canReinject: false`). Phase 2.B closed
the memory tail adapter chain.

The remaining gap is **readout observability**: the policy fields exist in
code but are not easily visible at the route-level audit output layer — an
operator reviewing a governed execution trace cannot trivially verify that
`writesRequireReceipt=true` or see which privacy filters were active. Without
route-level readout evidence, the policy metadata is invisible at the
accountability layer that external reviewers would inspect.

A second gap is **degraded-capture proof**: the existing code handles a
degraded capture path but there is no tested evidence that the degraded-
capture reason is surfaced in audit output.

---

## Scope

In scope:

- Surface `writesRequireReceipt`, `privacyFilters`, receipt decision, and
  capture mode in route-level audit/readout output.
- Add or verify a test proving `canReinject=false` remains binding after
  Phase 2.B memory tail adapter changes.
- Prove degraded-capture behavior in a test: degraded reason visible in
  receipt output, no reinjection enabled.
- Optional: one live route call showing the policy fields in the
  governance receipt output (if operator confirms live keys available).
- GC-018 baseline for this tranche.
- Completion review.

Out of scope:

- Memory reinjection of any kind.
- Persistent or archive memory.
- New memory tier semantics beyond the frozen 7-tier model.
- Provider-side memory behavior.
- Expanding `reinjectionAllowed` into a write gate.
- New capture semantics beyond the existing session-memory path.
- Public-sync update.

---

## Non-Goals

- Proving memory persistence to a database.
- Proving cross-session memory continuity.
- Adding new memory classes or tier IDs.
- Changing the `canReinject` default value.

---

## Work Plan

| Step | Artifact | Owner |
| --- | --- | --- |
| H-01 | File GC-018 baseline | Codex/Orchestrator |
| H-02 | Add/verify readout field surfacing for `writesRequireReceipt`, `privacyFilters`, receipt decision, capture mode in route output | Codex/Implementer |
| H-03 | Add test proving `canReinject=false` is preserved after Phase 2.B changes | Codex/Implementer |
| H-04 | Add test proving degraded-capture reason is visible in receipt output | Codex/Implementer |
| H-05 | (Optional) Live route call showing policy fields in governance receipt | Codex/Implementer |
| H-06 | File completion review with evidence trace block | Codex/Auditor |
| H-07 | Update active queue/state/handoff | Codex/Auditor |

---

## Acceptance Criteria

- [ ] GC-018 baseline filed.
- [ ] Route-level audit/readout surfaces `writesRequireReceipt`, `privacyFilters`,
      receipt decision, and capture mode.
- [ ] Test PASS: `canReinject=false` binding after Phase 2.B.
- [ ] Test PASS: degraded-capture reason visible in receipt output.
- [ ] `reinjectionAllowed` not added or used as write gate.
- [ ] Completion review filed with full evidence trace block.
- [ ] No new memory tier, reinjection, persistent memory, or public-sync.

---

## Verification / Evidence

All claims must be backed by:

- Test run output (file, test name, result).
- Source path where readout field is surfaced.
- Explicit confirmation that `canReinject=false` remains the default.
- Degraded-capture test: reason string visible, reinjection not triggered.

---

## Claim Boundary

This roadmap closes only audit-memory policy readout observability and
degraded-capture proof for the existing session-memory path. It does not
prove memory reinjection, persistent memory, archive memory, provider
memory, new memory tiers, or any public memory governance claim.
