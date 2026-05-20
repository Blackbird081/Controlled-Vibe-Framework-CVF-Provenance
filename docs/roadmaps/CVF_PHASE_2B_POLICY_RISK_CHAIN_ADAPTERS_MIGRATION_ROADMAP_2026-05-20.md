# CVF Phase 2.B Policy Risk Chain Adapters Migration Roadmap

Memory class: FULL_RECORD

Status: CLOSED_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION

docType: roadmap

Date: 2026-05-20

---

## Status

This roadmap authorizes and records a grouped but bounded Phase 2.B dependency
tranche:

- `P-01 -> P-06 -> P-05`
- `P-01 -> P-02 + P-03 -> P-04`
- `R-02 -> R-03 -> R-13 / R-14`

It is not a broad Phase 2.B bulk migration.

---

## Authorization / Decision

Authority chain:

- Phase 2.B migration plan:
  `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Prior receipt critical path closure:
  `docs/reviews/CVF_PHASE_2B_RECEIPT_CRITICAL_PATH_MIGRATION_COMPLETION_2026-05-20.md`
- Prior execution bridge receipt chain closure:
  `docs/reviews/CVF_PHASE_2B_EXECUTION_BRIDGE_RECEIPT_CHAIN_MIGRATION_COMPLETION_2026-05-20.md`
- Prior audit/trace/task receipt chain closure:
  `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`
- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

Decision: run these chains together because all are bounded policy or risk
adapter/snapshot surfaces and all can close without provider execution, Maika,
persistent memory-store, database schema, or kernel-owner replacement.

---

## Purpose / Why This Tranche

The previous Phase 2.B slices established receipt-envelope and audit/trace/task
wrappers. This tranche moves the remaining requested policy/risk chains from
static plan rows to typed adapter snapshots so downstream rows can cite stable
contract evidence without claiming live runtime governance behavior.

---

## Scope

In scope:

- `P-01`: governance engine policy-result adapter snapshot.
- `P-02`: governance engine API response adapter marker/helper.
- `P-03`: governance engine orchestrator summary adapter snapshot.
- `P-04`: local governance-engine main execution summary adapter.
- `P-06`: model-gateway routing-policy contract snapshot.
- `P-05`: model-gateway index exports for routing-policy snapshot contract.
- `R-02`: safety-runtime risk-engine CVF risk-level adapter snapshot.
- `R-03`: contamination risk-detector adapter snapshot.
- `R-13`: risk-propagation adapter snapshot.
- `R-14`: contamination risk-scorer adapter snapshot.
- Codex-only workflow role chain.

---

## Non-Goals

- No Claude review or Claude-authored work product.
- No provider runtime call.
- No Maika change.
- No persistent memory-store implementation.
- No live governance proof claim.
- No database schema migration.
- No kernel owner replacement.
- No global freeze lift.
- No public catalog claim.
- No rows outside the listed policy/risk chains.

---

## Work Plan

1. Add governance-engine policy-result adapter snapshot and tests.
2. Add API response adapter marker/helper without changing endpoint behavior.
3. Add orchestrator summary adapter and main local execution summary adapter.
4. Add model-gateway routing-policy contract snapshot and package exports.
5. Add safety-runtime risk-engine CVF risk-level adapter snapshot.
6. Add contamination risk detector, risk propagation, and risk scorer adapter
   snapshots.
7. Add focused tests.
8. Run package tests/checks and TypeScript compile checks.
9. Run docs gates.
10. File completion review and update active session pointers.

---

## Acceptance Criteria

- Existing policy/risk decisions remain unchanged.
- New adapters return additive snapshots and do not replace canonical engines.
- Routing-policy snapshot exposes decision metadata without provider fallback
  execution.
- Safety-runtime adapters preserve existing detector/scorer/propagation return
  values.
- Completion review records no Claude participation and no provider/Maika/live
  proof/global-freeze/public-catalog claim.

---

## Verification / Evidence

Required:

- `python -m pytest tests/test_phase2b_policy_chains.py` in
  `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core`
- `npm test` and `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`
- TypeScript compile checks for touched Safety Runtime policy and kernel
  surfaces.
- `python governance/compat/check_docs_governance_compat.py`
- `python governance/compat/check_markdown_structural_completeness.py`

---

## Claim Boundary

This roadmap may be cited only as authorization for the listed policy and risk
adapter/snapshot chains. It must not be cited as broad Phase 2.B migration,
live runtime proof, provider execution change, Maika change, persistent memory,
Claude review, public catalog update, kernel owner replacement, or global
freeze release.
