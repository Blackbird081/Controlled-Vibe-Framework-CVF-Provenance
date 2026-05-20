# CVF Phase 2.B Memory Tail Adapters Migration Roadmap

Memory class: FULL_RECORD

Status: CLOSED_MEMORY_TAIL_ADAPTERS_MIGRATION

docType: roadmap

Date: 2026-05-21

---

## Status

This roadmap authorizes and records the final bounded Phase 2.B memory-tail
dependency tranche:

- `E-01 closed -> M-01`
- `M-04` standalone memory-gateway adapter

It is not a broad Phase 2.B bulk migration.

---

## Authorization / Decision

Authority chain:

- Phase 2.B migration plan:
  `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Prior receipt critical path closure:
  `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- Prior audit/trace/task receipt chain closure:
  `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`
- Prior identity/control-plane adapter closure:
  `docs/reviews/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`
- Prior safety/external-policy risk fanout closure:
  `docs/reviews/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_COMPLETION_2026-05-21.md`
- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Decision: close the two remaining memory-family rows through additive adapter
snapshots only.

---

## Purpose / Why This Tranche

Prior slices closed receipt, policy/risk, identity/control-plane, and most
memory receipt/audit rows. This tranche closes the remaining memory-tail rows
without introducing persistence, new memory tiers, reinjection behavior,
provider runtime, or live governance claims.

---

## Scope

In scope:

- `M-01`: working-memory adapter snapshot for existing
  `AgentGovernedSessionContract` receipts.
- `M-04`: controlled-memory-gateway adapter snapshot for existing capture,
  retrieve, and reinjection-result surfaces.
- Focused tests and completion evidence.
- Codex-only workflow role chain.

---

## Non-Goals

- No Claude review or Claude-authored work product.
- No persistent memory store.
- No new memory tier.
- No reinjection runtime expansion.
- No provider runtime call.
- No live governance proof claim.
- No Maika change.
- No database schema migration.
- No public catalog or public-sync claim update.
- No global freeze lift.
- No rows outside `M-01` and `M-04`.

---

## Work Plan

1. Add `M-01` working-memory adapter snapshot helper in
   `agent.governed.session.contract.ts`.
2. Export the `M-01` adapter through the continuation barrel.
3. Add `M-04` controlled-memory-gateway adapter snapshot and
   `WithAdapter` helpers.
4. Export the `M-04` adapter through Learning Plane index.
5. Add focused tests.
6. Run targeted/full package tests and type checks.
7. File completion review and update active session pointers.

---

## Acceptance Criteria

- Existing receipt, capture, retrieve, and reinject outputs remain unchanged.
- Adapters carry explicit version/source metadata.
- `M-01` reports working-memory posture without creating persistence.
- `M-04` reports memory gateway posture without creating a new memory tier.
- Completion review records no provider/Maika/persistent-memory/live-proof
  claim.

---

## Verification / Evidence

Required:

- `npm test -- --run tests/phase2b-memory-tail-adapters.test.ts` in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm test` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm test -- --run tests/phase2b-memory-tail-adapters.test.ts` in
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- `npm run check` in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- `npm test` in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- docs governance checks
- completion review with explicit bounded claim

---

## Claim Boundary

This roadmap may be cited only as authorization for `M-01` and `M-04` adapter
snapshot closure. It must not be cited as broad runtime coherence, live
governance proof, provider execution change, Maika change, persistent memory,
new memory tier, public catalog update, or global freeze release.
