# CVF Agent Work Order - ERH-DUR2 External Storage And Distributed Durability For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-05

GC-018: `docs/baselines/CVF_GC018_ERH_DUR2_EXTERNAL_STORAGE_DISTRIBUTED_DURABILITY_2026-06-05.md`

dispatchBaseHead: `2ed85d65`

Assigned worker: Claude

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Implement ERH-DUR2: define a bounded, testable `StorageAdapter<T>` interface
contract to make the durable evidence and snapshot stores pluggable, then wrap
the existing DUR1 file-backed implementations in a `FileStorageAdapter` and
provide a `RedisStorageAdapter` stub that implements the same interface without
requiring a live Redis connection.

DUR1 moved event storage from OS temp to `.cvf/runtime` and made
`policySnapshotId` reconstructable. DUR2 extends that foundation with a clean
adapter seam: future Redis, PostgreSQL, or cloud-hosted backends can be slotted
in without bolted-on refactor.

Success means the existing DUR1 behavior is 100% unchanged when
`CVF_STORAGE_ADAPTER_TYPE` is absent or `file`, the adapter interface is
testable without any external backend, and a machine checker verifies the
workflow-chain markers.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-05: "DUR2, mở kiến trúc external storage/distributed durability bằng fresh GC-018" | ACCEPT |
| Fresh GC-018 | `docs/baselines/CVF_GC018_ERH_DUR2_EXTERNAL_STORAGE_DISTRIBUTED_DURABILITY_2026-06-05.md`; dispatchBaseHead=2ed85d65 | ACCEPT |
| DUR1 closure | `docs/reviews/CVF_ERH_DUR1_DURABLE_EVIDENCE_AND_POLICY_SNAPSHOT_COMPLETION_2026-06-05.md`; closureBaseHead=49e6725a | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`; DUR2 row `DISPATCH_READY` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; mode=`erh_dur2_external_storage_distributed_durability_dispatch_ready` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |

Authority boundary:

- This work order authorizes DUR2 only.
- Do not provision a live Redis or database instance, run database migrations,
  install new npm packages, touch auth/provider/rate-limiter code, public-sync,
  or make production-readiness claims.
- Do not commit or push.

## Scope / Target / Owner Boundary

Allowed scope:

- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts`:
  - define `StorageAdapter<T>` interface with at minimum `adapterType: string`,
    `append(item: T): Promise<void>`, `readAll(): Promise<T[]>`, and
    `deleteAll(): Promise<void>` surface (or equivalent split across
    `EventStoreAdapter<T>` + `SnapshotStoreAdapter<T>` if the access patterns
    require it — Claude must choose the cleanest design);
  - implement `FileStorageAdapter` (or `FileEventStoreAdapter` /
    `FileSnapshotStoreAdapter`) wrapping existing DUR1 file I/O logic;
  - implement `RedisStorageAdapter` stub (throws `CVF_NOT_IMPLEMENTED` error;
    must not silently swallow failures or corrupt existing file-backed data);
  - export `buildStorageAdapter()` factory that reads `CVF_STORAGE_ADAPTER_TYPE`
    env variable (default: `file`; unknown types throw bounded configuration
    error);
  - add `ERH_DUR2_MARKER` and `CVF_STORAGE_ADAPTER_VERSION` markers in header
    comment;
- update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts`:
  - import and use `buildStorageAdapter()` for the file I/O operations that back
    `readControlPlaneEvents`, `appendEvent`, and `writeEvents`;
  - all existing behavior must remain unchanged when `CVF_STORAGE_ADAPTER_TYPE`
    is absent or `file`;
  - preserve `CVF_CONTROL_PLANE_EVENTS_PATH` override;
  - preserve `ERH_DUR1_MARKER` and `CVF_DURABLE_EVIDENCE_VERSION` markers;
- update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts`:
  - import and use `buildStorageAdapter()` for the file I/O operations that back
    `persistPolicySnapshot` and `readPolicySnapshot`;
  - all existing behavior must remain unchanged when `CVF_STORAGE_ADAPTER_TYPE`
    is absent or `file`;
  - preserve `CVF_POLICY_SNAPSHOT_DIR` override;
  - preserve `CVF_POLICY_SNAPSHOT_REGISTRY_VERSION` and `ERH_DUR1_MARKER` markers;
- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.test.ts`:
  - test `FileStorageAdapter` append, readAll, deleteAll behavior;
  - test `RedisStorageAdapter` stub throws `CVF_NOT_IMPLEMENTED`;
  - test `buildStorageAdapter()` factory returns correct adapter by type;
  - test env override routes to correct adapter;
  - secret-safety assertions (adapter records must not carry raw prompts, output,
    secrets, API keys, or private memory);
- update existing tests only if DUR1-era snapshot/event test mocks need adapter
  wiring;
- create `governance/compat/check_erh_external_storage_adapter.py`;
- create `governance/compat/test_check_erh_external_storage_adapter.py`;
- update `governance/compat/run_local_governance_hook_chain.py`;
- update `governance/compat/run_agent_autorun_workflow_gate.py`;
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- create `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_WORKFLOW_CHAIN_2026-06-05.md`;
- create `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_LEDGER_2026-06-05.md`;
- create `docs/reviews/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_COMPLETION_2026-06-05.md`;
- update `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`
  (DUR2 row to `CLOSED_PASS_BOUNDED`);
- Codex reviewer may update `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
  `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF_V15_2026-05-29.md` only to
  record DUR2 dispatch or closure status.

Forbidden scope:

- package manifests, lockfiles (`package.json`, `package-lock.json`);
- live Redis instance, database provisioning, migration scripts, connection
  pooling, auth runtime, provider routing, rate limiter, public-sync clone,
  `.env*` secrets;
- broad `/api/execute` refactor;
- raw prompt/output/secret/private-memory persistence;
- live provider proof, hosted-readiness, production-readiness, public-readiness,
  production-grade distributed durability, or tamper-proof audit claims;
- DUR3 multi-instance consensus or distributed audit stream;
- commit or push.

Risk ceiling: R2. Escalate before external backend, package install, auth/rate-
limit/provider edits, public-sync, live proof, or claim-boundary expansion.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | authored DUR2 dispatch packet; reviews Claude output |
| Worker | Claude | implement DUR2 within Allowed scope under `WORKER_MUST_NOT_COMMIT` |
| Reviewer | Codex or human | verify diff, tests, gates, claim boundary, residuals |
| Human authorization required for | public-sync, push, live Redis/DB, package changes, provider/live proof, secrets | not included in DUR2 |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_DUR2_EXTERNAL_STORAGE_DISTRIBUTED_DURABILITY_2026-06-05.md` | tranche authority and source verification |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | DUR1 event store owner; DUR2 must wrap not replace its file I/O |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | DUR1 snapshot registry owner; DUR2 must wrap not replace its file I/O |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | envelope policySnapshotId re-export; verify DUR2 adapter wiring is compatible |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 workflow-chain registration pattern; see DUR1 entry as template |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | Claude captures execution base before editing |
| `git status --short` | Claude records existing worktree state |
| `Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts \| Measure-Object -Line` | current count recorded; expected ≈320 |
| `Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts \| Measure-Object -Line` | current count recorded; expected ≈89 |
| `Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts \| Measure-Object -Line` | route count recorded; broad route edit forbidden; expected 874 |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2ed85d65 --head HEAD` | PASS before implementation |

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `control-plane-events.ts` uses DUR1 durable local path after DUR1 | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 92-96 | `getStorePath` — `path.join(process.cwd(), '.cvf', 'runtime', 'control-plane-events.json')` | `getStorePath` | ACCEPT |
| `CVF_CONTROL_PLANE_EVENTS_PATH` env override still present | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 93-95 | `CVF_CONTROL_PLANE_EVENTS_PATH` | `getStorePath` | ACCEPT |
| `control-plane-events.ts` line count at dispatch base | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | full file | `control-plane-events.ts` | GC-023 file-size guard | ACCEPT — 320 lines |
| `policy-snapshot-registry.ts` uses DUR1 durable local path | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | lines 36-40 | `getSnapshotDir` — `path.join(process.cwd(), '.cvf', 'runtime', 'policy-snapshots')` | `getSnapshotDir` | ACCEPT |
| `CVF_POLICY_SNAPSHOT_DIR` env override still present | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | lines 37-39 | `CVF_POLICY_SNAPSHOT_DIR` | `getSnapshotDir` | ACCEPT |
| `buildPolicySnapshot` export exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | line 42 | `buildPolicySnapshot` | policy snapshot registry | ACCEPT |
| `persistPolicySnapshot` export exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | line 53 | `persistPolicySnapshot` | policy snapshot registry | ACCEPT |
| `readPolicySnapshot` export exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | line 68 | `readPolicySnapshot` | policy snapshot registry | ACCEPT |
| `generatePolicySnapshotId` export exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | line 81 | `generatePolicySnapshotId` | policy snapshot registry | ACCEPT |
| `policy-snapshot-registry.ts` line count at dispatch base | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | full file | `policy-snapshot-registry.ts` | GC-023 file-size guard | ACCEPT — 89 lines |
| No `StorageAdapter` interface exists in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `StorageAdapter` → no results | `StorageAdapter` | n/a | ACCEPT — confirmed absent |
| No `CVF_STORAGE_ADAPTER_TYPE` env variable exists in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `CVF_STORAGE_ADAPTER_TYPE` → no results | `CVF_STORAGE_ADAPTER_TYPE` | n/a | ACCEPT — confirmed absent |
| No `FileStorageAdapter` class exists in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `FileStorageAdapter` → no results | `FileStorageAdapter` | n/a | ACCEPT — confirmed absent |
| No `RedisStorageAdapter` class exists in current codebase | ABSENCE_VERIFIED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/` | grep `RedisStorageAdapter` → no results | `RedisStorageAdapter` | n/a | ACCEPT — confirmed absent |
| `web-governance-envelope.ts` line count at dispatch base | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | full file | `web-governance-envelope.ts` | GC-023 file-size guard | ACCEPT — 246 lines |
| `route.ts` line count at dispatch base | LINE_COUNT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | full file | `POST` | GC-023 hard limit 1000 | ACCEPT — 874 lines |

## New Doc-Only Fields

| New field or marker | Purpose | Not sourced from runtime? | Runtime claim blocked? |
| --- | --- | --- | --- |
| `ERH_DUR2_MARKER` | Machine marker that DUR2 storage adapter interface is installed | Yes | Yes — checker marker only until implemented |
| `CVF_STORAGE_ADAPTER_VERSION` | Version marker for the pluggable storage adapter contract | Yes | Yes — no external backend claim |
| `ERH_DUR2_LEDGER_VERSION` | Ledger marker for DUR2 evidence and residuals | Yes | Yes — documentation/checker marker |

Note: `CVF_STORAGE_ADAPTER_TYPE` is a new runtime env variable (not doc-only)
to be created by this work order. It is absence-verified above.

## Current Runtime Freshness Verification

| Runtime fact | Fresh evidence | Disposition |
| --- | --- | --- |
| `control-plane-events.ts` uses DUR1 `.cvf/runtime` default | source read at dispatchBaseHead `2ed85d65`, lines 92-96 | ACCEPT |
| `CVF_CONTROL_PLANE_EVENTS_PATH` override present | source read at dispatchBaseHead `2ed85d65`, lines 93-95 | ACCEPT |
| `policy-snapshot-registry.ts` uses DUR1 `.cvf/runtime/policy-snapshots` default | source read at dispatchBaseHead `2ed85d65`, lines 36-40 | ACCEPT |
| `CVF_POLICY_SNAPSHOT_DIR` override present | source read at dispatchBaseHead `2ed85d65`, lines 37-39 | ACCEPT |
| No `StorageAdapter` in current codebase | grep confirmed at dispatchBaseHead `2ed85d65` | ACCEPT |
| No `CVF_STORAGE_ADAPTER_TYPE` in current codebase | grep confirmed at dispatchBaseHead `2ed85d65` | ACCEPT |
| `control-plane-events.ts` line count is 320 | measured at dispatchBaseHead `2ed85d65` | ACCEPT |
| `policy-snapshot-registry.ts` line count is 89 | measured at dispatchBaseHead `2ed85d65` | ACCEPT |
| `route.ts` line count is 874 | measured at dispatchBaseHead `2ed85d65` | ACCEPT |
| `web-governance-envelope.ts` line count is 246 | measured at dispatchBaseHead `2ed85d65` | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or predecessor requirement | DUR2 output | Evidence | Status |
| --- | --- | --- | --- |
| ERH-RS1 section 4.4 external storage gap — no pluggable adapter after DUR1 | Split adapter contract: `EventListAdapter<T>` plus `KeyValueAdapter<T>`; `FileEventListAdapter`, `FileKeyValueAdapter`, `RedisEventListAdapter`, and `RedisKeyValueAdapter` | `storage-adapter.ts`; `check_erh_external_storage_adapter.py --enforce` PASS | PASS |
| GC-018 requirement: `CVF_STORAGE_ADAPTER_TYPE` env factory switch | `buildEventListAdapter()` and `buildKeyValueAdapter()` read `CVF_STORAGE_ADAPTER_TYPE`; default to `file`; `redis` returns throwing stub | `storage-adapter.test.ts`; focused Vitest PASS | PASS |
| DUR1 backward compatibility requirement | existing `appendAuditEvent`, `readAuditEvents`, `persistPolicySnapshot`, `readPolicySnapshot`, `generatePolicySnapshotId` behavior unchanged with default `file` adapter | DUR1 regression focused Vitest PASS: `control-plane-events.durable.test.ts`, `policy-snapshot-registry.test.ts`, `web-governance-envelope.test.ts` | PASS |
| Avoid overclaiming production/distributed durability | Completion review records `ERH_DUR2_DECISION: DUR3_NOT_NEEDED_NOW`; no live Redis/DB claim | `docs/reviews/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_COMPLETION_2026-06-05.md` | PASS |

Reviewer verified every trace row against source and focused test evidence in
the DUR2 closure batch.

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.test.ts` | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | bounded update — use adapter; preserve all existing exports and behavior |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.ts` | bounded update — use adapter; preserve all existing exports and behavior |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.durable.test.ts` | update only if adapter wiring changes test mock requirements |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/policy-snapshot-registry.test.ts` | update only if adapter wiring changes test mock requirements |
| `governance/compat/check_erh_external_storage_adapter.py` | create |
| `governance/compat/test_check_erh_external_storage_adapter.py` | create |
| `governance/compat/run_local_governance_hook_chain.py` | update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | update |
| `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_WORKFLOW_CHAIN_2026-06-05.md` | create |
| `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_LEDGER_2026-06-05.md` | create |
| `docs/reviews/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_COMPLETION_2026-06-05.md` | create |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update DUR2 row to `CLOSED_PASS_BOUNDED` |

Forbidden paths: package manifests, lockfiles, auth runtime, provider router,
rate limiter, public-sync clone, `.env*`, `route.ts` broad refactor, unrelated
source files.

## Worker Autonomy / No-Question Rule

Claude must fix allowed-scope machine-gate failures directly and rerun the gate.
Do not ask the operator whether to repair an allowed-scope guard failure.

Escalate only for scope expansion, external backend, package install, claim-
boundary changes, public-sync, live/provider proof, secrets/quota,
auth/rate-limit/provider edits, forbidden paths, or destructive/irreversible
actions.

## Execution Plan

| Step | Action | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | Capture execution base/status and run pre-implementation gate | base evidence | gate failure outside Allowed scope |
| 2 | Create `storage-adapter.ts` with interface, `FileStorageAdapter`, `RedisStorageAdapter` stub, and `buildStorageAdapter()` factory | pluggable adapter contract | adapter silently breaks DUR1 file behavior; `RedisStorageAdapter` swallows failures |
| 3 | Refactor `control-plane-events.ts` to use adapter; preserve all existing exports | DUR1 + DUR2 event store | any existing caller breaks with default `file` adapter |
| 4 | Refactor `policy-snapshot-registry.ts` to use adapter; preserve all existing exports | DUR1 + DUR2 snapshot registry | any existing caller breaks with default `file` adapter |
| 5 | Create `storage-adapter.test.ts`; update DUR1 tests only if mock wiring changes | adapter tests PASS | raw prompt/output/secret stored in test fixture |
| 6 | Create DUR2 checker, checker tests, hook/autorun wiring, GC-052 entry | machine workflow gate | checker cannot be bounded to source markers |
| 7 | Create workflow reference, ledger, completion review; update ERH roadmap | review-ready packet | completion overclaims production/Redis/distributed durability |
| 8 | Run focused tests, TypeScript check, build, all governance gates | all PASS or classified failure | failure outside Allowed scope |

## DUR2 Behavior Requirements

| Requirement | Required behavior |
| --- | --- |
| `StorageAdapter<T>` interface | defines `adapterType: string` plus at minimum the append/readAll/deleteAll or equivalent write/read surface needed by both event store and snapshot registry |
| `FileStorageAdapter` backward compat | default adapter wraps DUR1 file I/O; all callers unchanged; `.cvf/runtime` paths preserved |
| `RedisStorageAdapter` stub | implements `StorageAdapter<T>`; throws `CVF_NOT_IMPLEMENTED` error with message referencing `CVF_STORAGE_ADAPTER_TYPE=redis` is a stub; must never silently corrupt file-backed data |
| `buildStorageAdapter()` factory | reads `CVF_STORAGE_ADAPTER_TYPE`; returns `FileStorageAdapter` for `file` or absent; throws bounded `CVF_CONFIGURATION_ERROR` for unknown types; never returns a partially-initialized adapter |
| `CVF_STORAGE_ADAPTER_TYPE` env | new env variable; default absent/`file`; `redis` returns stub; no other values accepted without escalation |
| Backward compatibility | all existing DUR1 behavior (append, read, CSV export, corruption repair, snapshot persist/read, SIEM forward) must remain source-compatible with no code change in callers outside `control-plane-events.ts` and `policy-snapshot-registry.ts` |
| Secret and content safety | adapter records must not include raw prompts, raw AI output, API keys, provider secrets, or private memory payloads |
| Bounded claim | DUR2 claims pluggable adapter interface contract only; no live Redis connection, production database, distributed instances, multi-instance consensus, or tamper-proof audit |

## Acceptance Criteria

- `storage-adapter.ts` exists with `StorageAdapter<T>` (or split) interface,
  `FileStorageAdapter`, `RedisStorageAdapter` stub, and `buildStorageAdapter()`.
- `CVF_STORAGE_ADAPTER_TYPE` env variable is wired through `buildStorageAdapter()`.
- `control-plane-events.ts` and `policy-snapshot-registry.ts` use the adapter;
  existing DUR1 behavior unchanged with default `file` adapter.
- `RedisStorageAdapter` throws `CVF_NOT_IMPLEMENTED` and does not silently
  corrupt file-backed data.
- Focused adapter tests pass.
- All existing DUR1 tests continue to pass.
- DUR2 checker and checker tests pass, wired into local hook and autorun gate.
- GC-052 interlock contains a DUR2 workflow-chain connection with bounded claim.
- Completion review records DUR3 residual decision and does not claim live Redis,
  production database, distributed, hosted, public, or tamper-proof durability.

## Post-DUR2 Decision Rules

Completion review must include one residual decision:

| Verdict | Use when |
| --- | --- |
| `DUR3_READY` | DUR2 passes and source-visible need remains for multi-instance consensus or distributed audit stream |
| `DUR3_HOLD` | DUR2 evidence is insufficient or next step requires a live infrastructure architecture decision |
| `DUR3_NOT_NEEDED_NOW` | DUR2 closes the currently handleable adapter interface gap; multi-instance/distributed remains documented strategic residual |

DUR3 implementation is forbidden in this work order.

## Evidence Requirements

| Evidence | Path or command | Required |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | Yes |
| Worktree start state | `git status --short` | Yes |
| File counts before edit | four `Measure-Object -Line` commands in Pre-Flight Checks | Yes |
| TypeScript check | `npm run check` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` | Yes |
| Focused adapter tests | `npx vitest run src/lib/storage-adapter.test.ts` | Yes |
| Focused DUR1 regression | `npx vitest run src/lib/control-plane-events.durable.test.ts src/lib/policy-snapshot-registry.test.ts src/lib/web-governance-envelope.test.ts` | Yes |
| Build | `npm run build` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` | Yes |
| DUR2 checker | `python governance/compat/check_erh_external_storage_adapter.py --enforce` | Yes |
| Checker tests | `python -m pytest governance/compat/test_check_erh_external_storage_adapter.py` | Yes |
| Autorun pre-closure | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD` | Yes |
| Allowed-path proof | `git diff --name-status <executionBaseHead> HEAD` | Yes |
| Closure worktree state | `git status --short` | Yes |

Live proof: N/A with reason. DUR2 adds an adapter interface contract and stub;
no live Redis connection, provider call, or external backend is required.

## Review Gate

Reviewer must verify:

- `WORKER_MUST_NOT_COMMIT` was honored;
- changed files stay within Allowed scope;
- `FileStorageAdapter` preserves all DUR1 file I/O behavior;
- `RedisStorageAdapter` throws `CVF_NOT_IMPLEMENTED` and does not silently
  corrupt file-backed data;
- `buildStorageAdapter()` factory correctly routes `file` and throws on unknown;
- all existing DUR1 focused tests still pass;
- no package manifest, lockfile, auth, provider, or rate-limit changes;
- checker and adapter tests pass;
- completion review records DUR3 residual decision and does not claim live Redis,
  production database, distributed, hosted, public, or tamper-proof durability.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_FOR_CLAUDE_2026-06-05.md` | Status: `CLOSED_PASS_BOUNDED` after worker output reviewed | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_COMPLETION_2026-06-05.md` | completion review records DUR3_NOT_NEEDED_NOW and all verification gates | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | DUR2 row updated to CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | erh-dur2-external-storage-adapter-workflow-chain connection added | PASS |
| Registry Markdown | `docs/reference/CVF_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_WORKFLOW_CHAIN_2026-06-05.md` | workflow-chain reference created with ERH_DUR2_DECISION | PASS |
| External evidence digest | N/A with reason | no external source corpus consumed; DUR2 uses repo-local source and tests | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | GC-052 checker reports 0 violations | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V15_2026-05-29.md` | updated in reviewer closure batch to record DUR2 closed and DUR3 decision | PASS |

## Closure Checklist

Worker must mark each item in the completion review as checked, N/A with reason,
or BLOCKED with return-to-orchestrator action:

- pre-implementation autorun gate run with captured execution base;
- source diff limited to Allowed scope;
- no package, lockfile, auth, provider, rate-limit, public-sync, `.env*`, or
  unrelated file changes;
- no raw prompt, raw output, secret, API key, or private memory persistence;
- TypeScript check, focused adapter tests, DUR1 regression tests, build,
  checker, checker tests, and pre-closure autorun evidence recorded;
- `git status --short` and `git diff --name-status <executionBaseHead> HEAD`
  evidence recorded;
- DUR3 residual decision recorded.

## Operator Checkpoint

No operator input is required for allowed-scope implementation or remediation.

Return to operator only if DUR2 needs a live Redis/DB instance, package
installs, auth/rate-limit/provider edits, public-sync, live/provider proof,
secrets/quota, claim-boundary expansion, forbidden paths, destructive action,
or an external storage architecture decision.

## Failure Conditions

Return to Orchestrator if:

- package, lockfile, auth, rate-limit, provider, public-sync, `.env*`, or
  unrelated files require edits;
- `FileStorageAdapter` cannot wrap DUR1 file logic without breaking callers;
- `RedisStorageAdapter` stub requires a live Redis connection to pass tests;
- `buildStorageAdapter()` factory cannot default to `file` without a runtime
  change to existing callers;
- any adapter record would store raw prompt, raw output, secret, API key, or
  private memory payload;
- DUR1 focused tests fail after the refactor;
- `route.ts` would require changes beyond what is allowed;
- completion artifact claims hosted, public, production, distributed, or
  tamper-proof durability.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Codex reviewer may update
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, and
`AGENT_HANDOFF_V15_2026-05-29.md` to record DUR2 dispatch or reviewed closure
status.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Operator authorization: 2026-06-05 operator explicitly opened DUR2 with
"DUR2, mở kiến trúc external storage/distributed durability bằng fresh GC-018".

Rollback boundary: if continuity sync is wrong, restore only the DUR2
continuity text or active-state keys. Do not revert DUR2 source, checker,
roadmap, work-order, review, GC-018, or historical handoff content.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason — this work order dispatches runtime
  interface hardening; it is not a corpus scan or inventory task
- Corpus root: N/A with reason
- Snapshot time: N/A with reason
- Enumeration command: `rg --files --hidden --no-ignore docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DUR2_EXTERNAL_STORAGE_AND_DISTRIBUTED_DURABILITY_FOR_CLAUDE_2026-06-05.md`
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
| No pluggable storage adapter interface exists after DUR1 — any future Redis/DB backend requires bolted-on refactor | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `WORKFLOW_CHAIN_REQUIRED` | DUR2 `StorageAdapter<T>` interface contract and `FileStorageAdapter` wrap |
| `CVF_STORAGE_ADAPTER_TYPE` env switch absent — backend selection always implicit after DUR1 | `RUNTIME_SIGNAL_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | DUR2 `buildStorageAdapter()` factory + DUR2 checker |
| Redis/external backend path is undefined and untestable after DUR1 | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `MACHINE_CHECK_CANDIDATE` | DUR2 `RedisStorageAdapter` stub + interface-boundary test |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ERH-DUR2 is private provenance runtime interface hardening and dispatch
planning. Public-facing external storage or distributed durability claims require
a later public-sync work order after DUR2 is reviewed and claim boundaries are
accepted.

Next action: keep DUR3 external backend/distributed durability separate unless
the operator explicitly authorizes a fresh GC-018. The operator may authorize a
bounded public-sync summary later if claim boundaries are acceptable.

## Claim Boundary

This work order authorizes bounded pluggable storage adapter interface contract
hardening only. It does not authorize live Redis connectivity, external database
provisioning, distributed durability, multi-instance consensus, production-grade
audit storage, hosted freshness, live governance proof, production readiness,
public readiness, or complete remediation of every external-review durability
gap. DUR3 is not authorized.
