# Work Order — CDH-H Audit Memory Readout Hardening

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Surface audit-memory policy fields in route-level readout output, prove
`canReinject=false` remains binding after Phase 2.B changes, and prove
degraded-capture reason is visible in receipt output.

---

## Authority Chain

- CDH-H delta rebuttal:
  `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- CDH-H roadmap:
  `docs/roadmaps/CVF_CDH_H_AUDIT_MEMORY_READOUT_ROADMAP_2026-05-21.md`
- H2 prior closure:
  `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
- Phase 2.B memory tail:
  `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_CDH_H_AUDIT_MEMORY_READOUT_2026-05-21.md`

---

## Agent Roles

- Orchestrator: Codex files GC-018 and confirms scope.
- Reviewer: Codex reviews rebuttal boundary before implementation.
- Implementer: Codex adds/verifies readout fields and tests.
- Auditor: Codex verifies all tests pass and closes the packet.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`
- Route-level readout output (the field(s) that surface policy metadata).
- Test: `canReinject=false` binding after Phase 2.B memory tail changes.
- Test: degraded-capture reason visible in receipt output.
- `docs/baselines/CVF_GC018_CDH_H_AUDIT_MEMORY_READOUT_2026-05-21.md`
- `docs/reviews/CVF_CDH_H_AUDIT_MEMORY_READOUT_COMPLETION_2026-05-21.md`
- Active queue/state/handoff updates.

Out of scope:

- Memory reinjection of any kind.
- Persistent or archive memory.
- New memory tier semantics.
- Provider-side memory behavior.
- Adding `reinjectionAllowed` as a write gate.
- New capture semantics.
- Public-sync update.

---

## Required First Reads

- `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`
- `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`

---

## Pre-Flight Checks

- Confirm `canReinject: false` is present in `audit-memory-receipt.ts`.
- Confirm `reinjectionAllowed` is NOT present in `audit-memory-receipt.ts`
  as a write gate.
- Confirm `writesRequireReceipt` and `privacyFilters` are present in the
  `AuditMemoryReceipt` type.
- Check GC-023 line count for `audit-memory-receipt.ts` and `.test.ts`
  before adding lines.
- Run `python governance/compat/check_markdown_structural_completeness.py
  --base HEAD --head HEAD --enforce` — must be COMPLIANT before staging.

---

## Write Ownership

Permitted writes:

| File | Change |
| --- | --- |
| `docs/baselines/CVF_GC018_CDH_H_AUDIT_MEMORY_READOUT_2026-05-21.md` | New GC-018 baseline |
| `audit-memory-receipt.ts` | Readout field surfacing if not already present |
| `audit-memory-receipt.test.ts` | New tests for canReinject binding and degraded-capture |
| `docs/reviews/CVF_CDH_H_AUDIT_MEMORY_READOUT_COMPLETION_2026-05-21.md` | Completion review |
| `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` | Update cdh-h-delta status |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Update nextAllowedMove |
| `AGENT_HANDOFF_V10_2026-05-19.md` | GC-020 sync |

No other files may be modified.

---

## Execution Plan

1. File `CVF_GC018_CDH_H_AUDIT_MEMORY_READOUT_2026-05-21.md` (H-01).
2. Add or verify readout field surfacing for `writesRequireReceipt`,
   `privacyFilters`, receipt decision, and capture mode in route output (H-02).
3. Add test: `canReinject=false` binding is preserved after Phase 2.B
   memory tail adapter changes (H-03).
4. Add test: degraded-capture reason is visible in receipt output, no
   reinjection triggered (H-04).
5. Run test suite for affected extension (H-05).
6. File `CVF_CDH_H_AUDIT_MEMORY_READOUT_COMPLETION_2026-05-21.md` with
   evidence trace block (H-06).
7. Update active queue/state/handoff (H-07).
8. Run governance checks (H-08):
   `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce`
   `python governance/compat/check_governed_file_size.py --enforce`

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Policy fields visible in readout | Source path where `writesRequireReceipt`, `privacyFilters`, decision, and capture mode are surfaced |
| `canReinject=false` binding | Test file, test name, PASS result |
| Degraded-capture reason visible | Test file, test name, PASS result, reason string shown |
| No reinjection enabled | Confirmed absence of `reinjectionAllowed` as write gate in diff |
| `reinjectionAllowed` not added | Diff shows no such field |
| GC-023 compliance | Line count pre-flight and post-edit count both within limits |

---

## Acceptance Criteria

- [ ] GC-018 baseline filed.
- [ ] Readout fields surfaced: `writesRequireReceipt`, `privacyFilters`,
      receipt decision, capture mode.
- [ ] Test PASS: `canReinject=false` binding after Phase 2.B.
- [ ] Test PASS: degraded-capture reason visible.
- [ ] `reinjectionAllowed` not present as write gate.
- [ ] No new memory tier, reinjection, persistent memory.
- [ ] GC-023 line counts within limits.
- [ ] Governance checks exit 0.
- [ ] Completion review filed.
- [ ] Active queue `cdh-h-delta` status updated.

---

## Review Gate

Close only after H-08 governance checks exit 0, both new tests PASS, and
the evidence trace block is fully populated with source paths and test results.

---

## Closure Checklist

- [ ] GC-018 filed.
- [ ] Readout fields surfaced.
- [ ] `canReinject=false` test PASS.
- [ ] Degraded-capture test PASS.
- [ ] Completion review filed.
- [ ] Queue/state/handoff updated.
- [ ] Governance checks PASS.

---

## Return-To-Orchestrator Conditions

Return to Orchestrator (do not close) if:

- Adding readout fields requires changes to route.ts or a new route.
- `canReinject` default would need to change to make tests pass.
- GC-023 line count would be exceeded and no split strategy is clear.
- Any governance check exits non-zero.

---

## Operator Checkpoint

operator.checkpoint.waiver: documentation and test-only changes within the
existing session-memory path; no live provider call required; no route
changes; scope is bounded to the existing `audit-memory-receipt` surface.

---

## Claim Boundary

This work order closes only audit-memory policy readout observability and
degraded-capture proof. It does not prove memory reinjection, persistent
memory, archive memory, provider memory, new memory tiers, or any public
memory governance claim.
