# CVF GC-018 - ERH-DUR2 External Storage And Distributed Durability

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `2ed85d65`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize ERH-DUR2 as the next external-review hardening tranche after DUR1.

DUR1 closed the bounded local durability gap: the control-plane event store
default now uses `.cvf/runtime` and each `policySnapshotId` maps to a persisted
local snapshot record. DUR1 explicitly deferred external database, Redis,
distributed instances, and production-grade durability as a strategic residual
requiring a separate operator storage architecture decision.

The operator has now opened DUR2. DUR2 targets the remaining external-storage
and distributed-durability architecture gap:

1. The current file-backed event store and file-backed snapshot registry have
   no pluggable adapter interface. Any future Redis, PostgreSQL, or cloud-hosted
   backend must be bolted on rather than slotted in.
2. There is no `StorageAdapter` interface contract that maps the `append` / `read`
   / `list` / `delete` surface across storage backends.
3. `CVF_STORAGE_ADAPTER_TYPE` env override does not exist; backend selection is
   always implicit (file-only after DUR1).

DUR2 targets: define a bounded, testable `StorageAdapter<T>` interface contract,
wrap DUR1 file backends in a `FileStorageAdapter` implementation, create a
`RedisStorageAdapter` stub (no live Redis required — interface boundary only),
and wire a `CVF_STORAGE_ADAPTER_TYPE` env switch. External live Redis/DB
infrastructure is NOT required for DUR2 tests or governance proofs.

## Scope / Target / Owner Boundary

Target runtime surfaces:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts`
  (new — `StorageAdapter<T>` interface + `FileStorageAdapter` + `RedisStorageAdapter`
  stub + `buildStorageAdapter()` factory)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts`
  (refactor `getStorePath` to delegate to `buildStorageAdapter()` when
  `CVF_STORAGE_ADAPTER_TYPE` is set; file adapter remains default)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts`
  (same refactor — use storage adapter for snapshot persist/read)
- bounded helper, test, checker, and reference artifacts named by the DUR2
  work order.

Authorized outputs:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_FOR_CLAUDE_2026-06-05.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.test.ts`
- `governance/compat/check_erh_external_storage_adapter.py`
- `governance/compat/test_check_erh_external_storage_adapter.py`
- `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_WORKFLOW_CHAIN_2026-06-05.md`
- `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_LEDGER_2026-06-05.md`
- `docs/reviews/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_COMPLETION_2026-06-05.md`
- ERH roadmap row for DUR2; GC-052 interlock entry for DUR2.

Out of scope:

- Live Redis or PostgreSQL instance, external database provisioning, cloud
  storage backend, any migration script or schema change;
- package manifest or lockfile changes (no new npm/pip packages);
- auth runtime, provider routing, rate limiter, `.env*` secrets, raw prompt or
  raw AI output persistence;
- live provider proof, hosted-readiness, production-readiness, public-readiness,
  production-grade distributed durability, or tamper-proof audit claims;
- public-sync, push to remote, or any change to public repository;
- DUR3 (multi-instance consensus, distributed audit stream) — remains blocked
  until DUR2 closes and operator authorizes.

Risk ceiling: R2 runtime interface hardening. Escalate before any live external
backend, package install, auth/provider change, public-sync, live proof, or
claim-boundary expansion.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05: "DUR2, mở kiến trúc external storage/distributed durability bằng fresh GC-018" | ACCEPT |
| DUR1 closure | `docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md`; `DUR2_NOT_NEEDED_NOW` overridden by explicit operator DUR2 authorization | ACCEPT |
| DUR1 residual documented | DUR1 completion review Risk table: "External DB/Redis/distributed runtime retention"; ledger step 16; finding disposition `DEFERRED_EXTERNAL_STORAGE` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| ERH-RS1 external review source | `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md` (section 4.4 external storage residual) | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |

## Decision / Baseline

Decision: authorize Claude to implement DUR2 storage adapter interface contract
under `WORKER_MUST_NOT_COMMIT`.

Baseline facts (source-verified at `2ed85d65`):

- DUR1 closed: `control-plane-events.ts` default path is
  `process.cwd()/.cvf/runtime/control-plane-events.json`; `CVF_CONTROL_PLANE_EVENTS_PATH`
  override preserved; `ERH_DUR1_MARKER` present.
- `policy-snapshot-registry.ts` owns `generatePolicySnapshotId` and persists
  bounded records under `.cvf/runtime/policy-snapshots/`; `CVF_POLICY_SNAPSHOT_DIR`
  override preserved.
- No `StorageAdapter` interface exists in the codebase.
- No `CVF_STORAGE_ADAPTER_TYPE` env variable exists.
- No Redis, database, or external storage adapter code exists.
- `control-plane-events.ts` current line count: ~372; `policy-snapshot-registry.ts`
  current line count: ~93; `/api/execute/route.ts`: 874 (hard limit 1000).

## Source Verification Block

| Claimed item | Verification class | Source file | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- |
| `control-plane-events.ts` uses `.cvf/runtime` default after DUR1 | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | `getStorePath` — `'.cvf', 'runtime'` path | ACCEPT |
| `policy-snapshot-registry.ts` persists snapshots under `.cvf/runtime/policy-snapshots` | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | `getSnapshotDir` | ACCEPT |
| No `StorageAdapter` interface in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `StorageAdapter` → no results | ACCEPT |
| No `CVF_STORAGE_ADAPTER_TYPE` env override in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `CVF_STORAGE_ADAPTER_TYPE` → no results | ACCEPT |
| No Redis or external DB adapter in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `redis\|ioredis\|pg\|prisma` → no results | ACCEPT |

## New Doc-Only Fields

| New field or marker | Purpose | Not sourced from runtime? | Runtime claim blocked? |
| --- | --- | --- | --- |
| `ERH_DUR2_MARKER` | Machine marker that DUR2 storage adapter interface is installed | Yes | Yes — checker marker only |
| `CVF_STORAGE_ADAPTER_VERSION` | Version marker for the pluggable storage adapter contract | Yes | Yes — no external backend claim |
| `ERH_DUR2_LEDGER_VERSION` | Ledger marker for DUR2 evidence and residuals | Yes | Yes — documentation/checker marker |
| `CVF_STORAGE_ADAPTER_TYPE` | Runtime env: `file` (default) \| `redis` (stub, no live required) | No — this IS a new env var | Yes — stub only; no live Redis connection |

## Behavior Requirements

| Requirement | Required behavior |
| --- | --- |
| StorageAdapter interface | `StorageAdapter<T>` must define `append(key, item)`, `readAll(key)`, `deleteAll(key)`, and `adapterType` property |
| FileStorageAdapter | Must wrap existing DUR1 file-backed logic; backward-compatible with all existing `appendAuditEvent`, `readAuditEvents`, `appendCostEvent`, `readCostEvents`, CSV export, and corruption-repair callers |
| RedisStorageAdapter stub | Must implement `StorageAdapter<T>` interface; must throw `NOT_IMPLEMENTED` until a live Redis URL is configured; must never silently fail in a way that corrupts existing file-backed data |
| Factory env switch | `buildStorageAdapter(type)` reads `CVF_STORAGE_ADAPTER_TYPE`; default is `file`; unknown types throw a bounded configuration error |
| Backward compatibility | All existing event-store and snapshot-registry behavior remains unchanged when `CVF_STORAGE_ADAPTER_TYPE` is absent or `file` |
| Secret and content safety | Adapter implementations must not persist raw prompts, raw AI outputs, secrets, API keys, or private memory payloads |
| Checker coverage | DUR2 machine checker must verify `ERH_DUR2_MARKER`, `StorageAdapter` interface export, `FileStorageAdapter` export, `RedisStorageAdapter` export, `buildStorageAdapter` export, `CVF_STORAGE_ADAPTER_TYPE` env reference, backward-compat callers unmodified, and docs |

## Evidence / Verification

Dispatch verification:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 2ed85d65 --head HEAD
```

Worker verification must use the Claude-captured execution base.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason — GC-018 dispatch baseline, not a corpus scan
- Corpus root: N/A with reason
- Snapshot time: N/A with reason
- Enumeration command: `rg --files --hidden --no-ignore docs/baselines/CVF_GC018_ERH_DUR2_EXTERNAL_STORAGE_DISTRIBUTED_DURABILITY_2026-06-05.md`
- Manifest artifact or inline manifest: N/A with reason
- Manifest hash: N/A with reason
- Processing ledger artifact or inline ledger: N/A with reason
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason
- Drift check: N/A with reason
- Output traceability: N/A with reason
- Adversarial verification: N/A with reason
- Corpus verdict: COMPLETE_VERIFIED

No corpus completeness claim is made.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| No pluggable storage adapter interface exists after DUR1 | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `WORKFLOW_CHAIN_REQUIRED` | DUR2 `StorageAdapter<T>` interface contract |
| Redis/external backend cannot be slotted in without bolted-on refactor | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `WORKFLOW_CHAIN_REQUIRED` | DUR2 `RedisStorageAdapter` stub + factory env switch |
| `CVF_STORAGE_ADAPTER_TYPE` env does not exist | `RUNTIME_SIGNAL_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | DUR2 checker verifies env reference |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-DUR2 is private provenance runtime interface hardening and dispatch
planning. Public-facing distributed durability claims require a later
public-sync work order after DUR2 implementation is reviewed and claim
boundaries are accepted.

Next action: author DUR2 work order, then dispatch to worker under
`WORKER_MUST_NOT_COMMIT`.

## Claim Boundary

This GC-018 authorizes bounded pluggable storage adapter interface contract
hardening only. It does not claim live Redis connectivity, external database,
distributed instances, production-grade audit durability, hosted freshness,
live governance proof, production readiness, public readiness, or complete
remediation of every external-review durability gap. DUR3 (multi-instance
consensus, distributed audit stream) is not authorized.
