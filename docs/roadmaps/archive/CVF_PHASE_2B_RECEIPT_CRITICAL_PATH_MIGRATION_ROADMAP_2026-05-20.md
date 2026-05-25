# CVF Phase 2.B Receipt Critical Path Migration Roadmap

Memory class: FULL_RECORD

Status: READY_FOR_GC018

docType: roadmap

Date: 2026-05-20

---

## Status

This roadmap authorizes a bounded dependency-chain slice for four locked Phase
2.B rows:

`E-01 -> E-02 -> E-04 -> M-08`

It is not a broad Phase 2.B bulk migration.

---

## Authorization / Decision

Authority chain:

- Phase 2.B migration plan:
  `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Decision: run one grouped critical-path slice because the four rows are directly
dependent, preserve the same receipt-envelope contract, and do not replace a
frozen kernel owner.

---

## Purpose / Why This Tranche

The locked Phase 2.B plan names the receipt path as operationally critical:

`E-01 -> E-02 -> E-04 -> M-08`

This tranche wires those four surfaces to the canonical Phase 1.R
`Receipt<TPayload>` envelope while preserving legacy receipt payload shapes.

---

## Scope

In scope:

- `E-01`: `cpf-agent-governed-session-contract`
- `E-02`: `cpf-gateway-consumer-contract`
- `E-04`: `model-gateway-gateway-receipt`
- `M-08`: `model-gateway-gateway-receipt-receipt`
- contract-only helper in `receipt-envelope.contract.ts` if needed
- focused unit tests and package-level checks

Allowed files:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/gateway.consumer.contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`
- focused tests adjacent to those surfaces

---

## Non-Goals

- No provider runtime change.
- No Maika change.
- No memory store or persistence implementation.
- No broad runtime coherence claim.
- No global freeze lift.
- No change to existing receipt payload field names.
- No rows outside `E-01`, `E-02`, `E-04`, and `M-08`.

---

## Work Plan

1. Add or reuse a canonical helper for `Receipt<TPayload>` envelope creation.
2. Add E-01 envelope wrapper for `AgentExecutionAuditReceipt`.
3. Add E-02 envelope wrapper for `GatewayConsumptionReceipt`.
4. Add E-04 envelope wrapper for `GatewayReceipt`.
5. Add M-08 receipt-memory record wrapper for gateway receipt envelopes.
6. Add focused tests.
7. Run package tests/checks and docs checks.
8. File completion review.

---

## Acceptance Criteria

- Existing receipt payloads remain unchanged.
- New wrappers use `schemaVersion: "1.R.0"`.
- Wrapper payload is typed, never `any`.
- M-08 marks gateway receipt envelope as receipt-tier immutable memory record
  without adding a storage backend.
- Package-level tests/checks pass for touched packages.
- Completion review records no provider/Maika/live-proof/global-freeze claim.

---

## Verification / Evidence

Required:

- `npm test` and `npm run check` in `EXTENSIONS/CVF_GUARD_CONTRACT`
- `npm test` and `npm run check` in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`
- `npm test` and `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`
- `python governance/compat/check_docs_governance_compat.py`
- `python governance/compat/check_markdown_structural_completeness.py`

---

## Claim Boundary

This roadmap may be cited only as authorization for the four-row receipt
critical path. It must not be cited as broad Phase 2.B migration, live runtime
proof, provider execution change, Maika change, persistent memory, or global
freeze release.
