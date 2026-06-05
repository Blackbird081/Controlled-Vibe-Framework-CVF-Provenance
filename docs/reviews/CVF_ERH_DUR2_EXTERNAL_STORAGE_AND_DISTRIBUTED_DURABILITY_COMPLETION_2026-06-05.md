# CVF ERH-DUR2 External Storage And Distributed Durability Completion Review

Memory class: FULL_RECORD

docType: review

Status: CLOSED_PASS_BOUNDED
Date: 2026-06-05

## Purpose

Completion review for ERH-DUR2 pluggable storage adapter workflow chain.
Records implementation findings, evidence, risks, DUR3 decision, and claim boundary.

## Scope

Covers `storage-adapter.ts`, refactored `control-plane-events.ts` and
`policy-snapshot-registry.ts`, focused tests, governance checker, hook/autorun
wiring, interlock registry entry, and documentation.

## Applies To

- `src/lib/storage-adapter.ts` in `cvf-web`
- `src/lib/control-plane-events.ts` in `cvf-web`
- `src/lib/policy-snapshot-registry.ts` in `cvf-web`
- `src/lib/storage-adapter.test.ts` in `cvf-web`
- `governance/compat/check_erh_external_storage_adapter.py`

## Reviewed

- `src/lib/storage-adapter.ts` in `cvf-web`
- `src/lib/control-plane-events.ts` in `cvf-web`
- `src/lib/policy-snapshot-registry.ts` in `cvf-web`
- `src/lib/storage-adapter.test.ts` in `cvf-web`
- `governance/compat/check_erh_external_storage_adapter.py`

## Summary

DUR2 introduces two pluggable adapter interfaces — `EventListAdapter<T>` and
`KeyValueAdapter<T>` — and four concrete classes: `FileEventListAdapter`,
`FileKeyValueAdapter` (wrapping DUR1 file I/O with zero behavioral change),
and `RedisEventListAdapter`, `RedisKeyValueAdapter` (stubs throwing
`CVF_NOT_IMPLEMENTED`). Factory functions `buildEventListAdapter()` and
`buildKeyValueAdapter()` read `CVF_STORAGE_ADAPTER_TYPE` to select the backend.

`control-plane-events.ts` and `policy-snapshot-registry.ts` now delegate all
file I/O to the adapter layer. The corruption repair logic for the event store
moved from `control-plane-events.ts` into `FileEventListAdapter._repair()`,
improving encapsulation.

## Evidence

| Gate | Result |
|------|--------|
| TypeScript check (`npm run check`) | PASS |
| `storage-adapter.test.ts` (35 tests) | PASS |
| DUR1 regression: `control-plane-events.durable.test.ts` (9) | PASS |
| DUR1 regression: `policy-snapshot-registry.test.ts` (10) | PASS |
| DUR1 regression: `web-governance-envelope.test.ts` (18) | PASS |
| `check_erh_external_storage_adapter.py --enforce` | COMPLIANT |
| `test_check_erh_external_storage_adapter.py` | PASS |
| Autorun pre-implementation gate | PASS |
| Hook chain wired (DUR2 entry after DUR1) | CONFIRMED |
| Autorun gate wired (DUR2 GateCommand after DUR1) | CONFIRMED |
| Interlock registry entry added | CONFIRMED |

## Findings

| # | Finding | Disposition |
|---|---------|-------------|
| F1 | Corruption repair logic was in `control-plane-events.ts` — architecture gap for non-file backends. | FIXED — moved into `FileEventListAdapter._repair()`. |
| F2 | DUR1 `policy-snapshot-registry.ts` directly called `mkdir`/`writeFile` — tightly coupled to filesystem. | FIXED — delegated to `FileKeyValueAdapter.write()`. |
| F3 | No storage backend selection mechanism existed. | FIXED — `CVF_STORAGE_ADAPTER_TYPE` env var + factory pattern. |

## Risk

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Redis stubs silently accepted as real | LOW | Stubs throw `CVF_NOT_IMPLEMENTED` on all methods; checker verifies this. |
| `FileEventListAdapter` behavioral regression | LOW | 9 existing durability tests + 35 new adapter tests all PASS. |
| Env var misconfiguration (unknown type) | LOW | Factory throws `CVF_CONFIGURATION_ERROR` for unknown values. |

## Required Corrective Actions

None. All acceptance criteria met.

## Post-DUR2 Decision: DUR3

`ERH_DUR2_DECISION: DUR3_NOT_NEEDED_NOW`

DUR3 (live Redis backend, multi-instance consensus, distributed audit stream)
is deferred. The Redis stub interface is present and ready for a future
implementation. No explicit DUR3 roadmap item is opened by this review.

If a future operator explicitly authorizes DUR3, the implementation must:
- Remove `throw new Error(CVF_NOT_IMPLEMENTED)` from Redis stub methods.
- Provide actual `ioredis` or equivalent client integration.
- Add connection pooling, retry logic, and auth configuration.
- Add new DUR3 GC-018, work order, and acceptance criteria.

## Finding-To-Governance Learning Disposition

| DEFECT_CLASS | DISPOSITION | LANE | NEXT ACTION |
|---|---|---|---|
| RULE_GAP — no adapter seam rule existed for event store file I/O coupling | MACHINE_CHECK_ADDED | GOVERNANCE_CONTROL_PLANE | None — `check_erh_external_storage_adapter.py` enforces DUR2 marker and adapter import wiring |
| RULE_GAP — no adapter seam rule existed for snapshot registry file I/O coupling | MACHINE_CHECK_ADDED | GOVERNANCE_CONTROL_PLANE | None — `check_erh_external_storage_adapter.py` enforces DUR2 marker and adapter import wiring |
| RULE_GAP — no pluggable backend stub requirement existed before DUR2 | N/A_WITH_REASON — Redis stub deferred by `ERH_DUR2_DECISION: DUR3_NOT_NEEDED_NOW` | GOVERNANCE_CONTROL_PLANE | Open new GC-018 if operator authorizes DUR3; no action until then |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_FOR_CLAUDE_2026-06-05.md` | DUR2 worker output reviewed by this completion artifact | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_COMPLETION_2026-06-05.md` | this artifact records `DUR3_NOT_NEEDED_NOW` and verification evidence | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | DUR2 row updated to `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `erh-dur2-external-storage-adapter-workflow-chain` connection added | PASS |
| Registry Markdown | `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_WORKFLOW_CHAIN_2026-06-05.md` | workflow-chain reference created with `ERH_DUR2_DECISION` | PASS |
| Ledger | `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_LEDGER_2026-06-05.md` | implementation step ledger with `ERH_DUR2_LEDGER_VERSION` | PASS |
| External evidence digest | `N/A with reason` | no external source corpus consumed; DUR2 uses repo-local source and tests | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 checker reports 0 violations | PASS |
| Focused tests | `src/lib/storage-adapter.test.ts` in `cvf-web` | 35 Vitest tests PASS; 37 DUR1 regression tests PASS | PASS |
| DUR2 checker | `governance/compat/check_erh_external_storage_adapter.py --enforce` | 0 violations | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V15_2026-05-29.md` | updated in reviewer closure batch to record DUR2 closed and DUR3 decision | PASS |
| Pre-closure gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 6befe0b3 --head HEAD` | reviewer rerun required after residue cleanup; final command evidence captured in closure batch | PASS |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: ERH-DUR2 external storage adapter
workflow chain — new DUR2 checker, checker unit tests, hook chain wiring,
autorun gate wiring.

Protected paths:
- `governance/compat/check_erh_external_storage_adapter.py`
- `governance/compat/test_check_erh_external_storage_adapter.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

Operator authorization: operator explicitly authorized DUR2 implementation
2026-06-05 via work order
`docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_FOR_CLAUDE_2026-06-05.md`.

Rollback boundary: revert DUR2 commit removes all four guard files and their
wiring from the hook chain and autorun gate. DUR1 governance checker and hook
chain remain intact.

## Claim Boundary

This review proves ERH-DUR2 implementation is complete and all acceptance
criteria are met as of 2026-06-05.

This review does **not** prove: live Redis connectivity, production database,
distributed durability, multi-instance consensus, external storage service,
tamper-proof audit, hosted readiness, public readiness, or production-grade
distributed retention.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY — provenance workspace only; no public-sync performed.
