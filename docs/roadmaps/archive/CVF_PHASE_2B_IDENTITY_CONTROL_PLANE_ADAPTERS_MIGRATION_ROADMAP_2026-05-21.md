# CVF Phase 2.B Identity Control Plane Adapters Migration Roadmap

Memory class: FULL_RECORD

Status: CLOSED_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION

docType: roadmap

Date: 2026-05-21

---

## Status

This roadmap authorizes and records a grouped but bounded Phase 2.B dependency
tranche:

- `I-01 -> I-02 -> I-03 / I-07`
- `I-01 -> I-04 -> I-05`
- `I-03 -> I-06`

It is not a broad Phase 2.B bulk migration.

---

## Authorization / Decision

Authority chain:

- Phase 2.B migration plan:
  `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Prior receipt critical path closure:
  `docs/reviews/archive/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- Prior execution bridge receipt chain closure:
  `docs/reviews/archive/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`
- Prior audit/trace/task receipt chain closure:
  `docs/reviews/archive/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`
- Prior policy/risk adapter closure:
  `docs/reviews/archive/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_COMPLETION_2026-05-20.md`
- HN2.b owner map:
  `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Decision: run these chains together because all are identity/control-plane
adapter or barrel-export surfaces and all can close without role taxonomy,
provider execution, Maika, persistent memory-store, database schema, or
kernel-owner replacement.

---

## Purpose / Why This Tranche

The previous Phase 2.B slices established receipt and policy/risk adapter
anchors. This tranche adds the identity/control-plane adapter snapshots needed
to cite agent definition, design, orchestration, continuity, coordination, and
extension-bridge surfaces without claiming new runtime orchestration.

---

## Scope

In scope:

- `I-01`: agent definition boundary adapter snapshot.
- `I-02`: design-plan adapter snapshot.
- `I-03`: orchestration adapter snapshot.
- `I-04`: continuity checkpoint adapter snapshot.
- `I-05`: continuation barrel exports for continuity and agent-definition
  adapters.
- `I-06`: coordination barrel adapter snapshot.
- `I-07`: phase-governance extension-bridge adapter snapshot.
- Codex-only workflow role chain.

---

## Non-Goals

- No Claude review or Claude-authored work product.
- No new role taxonomy.
- No runtime actor/job queue.
- No provider runtime call.
- No Maika change.
- No persistent memory-store implementation.
- No live governance proof claim.
- No database schema migration.
- No kernel owner replacement.
- No global freeze lift.
- No public catalog claim.
- No rows outside the listed identity/control-plane chains.

---

## Work Plan

1. Add agent-definition adapter snapshot and optional `WithAdapter` helper.
2. Add design-plan adapter snapshot and optional `WithAdapter` helper.
3. Add orchestration adapter snapshot and optional `WithAdapter` helper.
4. Add continuity checkpoint adapter snapshot and validation wrapper.
5. Export continuity and agent-definition adapters through continuation barrel.
6. Add coordination barrel adapter snapshot tied to orchestration adapter
   evidence.
7. Add phase-governance extension-bridge adapter snapshot.
8. Add focused tests.
9. Run package tests/checks.
10. File completion review and update active session pointers.

---

## Acceptance Criteria

- Existing contract outputs remain unchanged.
- New adapters are additive snapshots with explicit version/source metadata.
- Barrel targets expose adapter contracts without introducing engines.
- Extension bridge adapter reports registry/workflow counts only and does not
  execute workflow steps.
- Completion review records no Claude participation and no role-taxonomy,
  provider/Maika/live-proof/global-freeze/public-catalog claim.

---

## Verification / Evidence

Required:

- `npm test -- --run tests/phase2b-identity-control-plane-adapters.test.ts`
  in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm test` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm test -- --run tests/extension.bridge.test.ts` in
  `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL`
- `npm run check` in `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL`
- `python governance/compat/check_docs_governance_compat.py`
- `python governance/compat/check_markdown_structural_completeness.py`

---

## Claim Boundary

This roadmap may be cited only as authorization for the listed
identity/control-plane adapter and barrel-export chains. It must not be cited
as broad Phase 2.B migration, live runtime proof, provider execution change,
Maika change, persistent memory, role taxonomy, Claude review, public catalog
update, kernel owner replacement, or global freeze release.
