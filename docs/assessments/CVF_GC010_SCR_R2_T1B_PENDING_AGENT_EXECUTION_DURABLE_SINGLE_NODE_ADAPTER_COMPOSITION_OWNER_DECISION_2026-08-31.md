# CVF GC010 SCR-R2-T1B Pending Agent Execution Durable Single-Node Adapter And Composition Owner Decision

Memory class: governed-decision-assessment

docType: baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: GC010-SCR-R2-T1B

Date: 2026-08-31

Worker: delegated no-commit decision worker

executionBaseHead: `175b489aa`

## Purpose

Select the exact durable single-node storage boundary and exact future
composition owner for the accepted T1A pending-execution core
(`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`,
material `f55b80826`), or truthfully state why no safe boundary can be named
yet. This assessment answers the thirteen required decision questions from
the paired baseline
`docs/baselines/CVF_GC018_GC010_SCR_R2_T1B_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_ADAPTER_COMPOSITION_OWNER_DECISION_2026-08-31.md`
in order and selects exactly one terminal token. This tranche implements
nothing: no adapter, composition module, test, route, package, or dependency
change is created.

## Source / Predecessor Evidence

- Paired baseline: `docs/baselines/CVF_GC018_GC010_SCR_R2_T1B_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_ADAPTER_COMPOSITION_OWNER_DECISION_2026-08-31.md`.
- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1B_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_ADAPTER_COMPOSITION_OWNER_DECISION_2026-08-31.md`.
- T1A completion (`CLOSED_PASS_BOUNDED`, terminal `NON_PRODUCTION_CORE_ACCEPTED`):
  `docs/reviews/CVF_GC010_SCR_R2_T1A_PENDING_AGENT_EXECUTION_NON_PRODUCTION_CORE_IMPLEMENTATION_COMPLETION_2026-08-30.md`.
- T0B controlling contract (terminal `SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION`,
  with the Independent Reviewer Contract Correction controlling):
  `docs/assessments/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`.
- T1A material commit `f55b80826`; continuity `25e3b22ed`; T1B dispatch
  committed at `5eb3c882f`/`175b489aa`.
- executionBaseHead: `175b489aa` (captured fresh at worker start; `git status
  --short --untracked-files=all` was clean; both output paths were absent).

## Scope / Methodology

Fresh direct reads of the T1A implementation and every named candidate-owner
source at executionBaseHead `175b489aa`, plus the exact negative-search
command required by the work order's Verification Commands. No provider,
network, browser, credential, or runtime mutation occurred. No file outside
the two worker-owned output paths was written. The pre-implementation autorun
gate was run before authoring this artifact (see Command Evidence in the
paired worker return).

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1A already declares a linearizable `compareAndSwap(id, expectedVersion, expectedStatus, transition)` store contract and ships only a single-process in-memory implementation | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | `PendingAgentExecutionStore` interface lines 494-507; `InMemoryPendingAgentExecutionStore` lines 590-712; `claimPendingExecution` lines 860-897; `beginPendingExecution` lines 911-942 | store/claim/begin seams | cvf-web pending-execution core | ACCEPT |
| The controlling lifecycle is `CREATED -> CLAIMED -> EXECUTING` then exactly one truthful terminal, matching the T0B reviewer correction, not the worker's original `CONSUMED` state | runtime/schema | same file | `PendingAgentExecutionStatus` lines 330-340; `LEGAL_TRANSITION_FROM` lines 509-516 | lifecycle state machine | cvf-web pending-execution core | ACCEPT |
| Approval store's `Map.set` is last-writer-wins with no compare-and-swap, and `persist()` swallows write failures with `console.warn` only | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalStore.persist` lines 85-98; `override set` lines 100-104 | `ApprovalStore`; `persist` | approval owner | ACCEPT |
| Knowledge store uses write-to-temp-then-rename (atomic replacement of the whole file) but has no per-record version/status field and no conditional write | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `FileBackedKnowledgeStore._persist` lines 158-167 | file-backed store | knowledge owner | ACCEPT |
| SOT3 evidence store serializes appends only within one process via an in-memory promise chain (`appendQueue`); this is not a cross-process primitive | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | `appendQueue` field line 281; `append` lines 326-353 | process-local append queue | evidence owner | ACCEPT |
| MAO durable store validates/replays and atomically renames the whole snapshot file on every write; it has no lock or version predicate that resolves two concurrent cross-process writers to the same taskGraphId | runtime | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `MaoFileRunStore.appendEvent` lines 186-216; `atomicWriteJson` lines 443-462 | `MaoFileRunStore`; `atomicWriteJson` | MAO owner | ACCEPT |
| Generic SQLite capability already exists with WAL journal mode, `synchronous = NORMAL`, and `db.transaction(...)` support | runtime/dependency | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | `openSQLiteDatabase` lines 241-248; `withSQLiteDatabase` lines 250-257 | SQLite event/key-value adapters | generic storage owner | ACCEPT |
| Existing SQLite key-value write is an unconditional `INSERT ... ON CONFLICT(id) DO UPDATE` upsert with no `WHERE` predicate on prior version/status, so it is not compare-and-swap | runtime | same file | `SQLiteKeyValueAdapter.write` lines 357-366 | `ON CONFLICT ... DO UPDATE` | generic storage owner | ACCEPT |
| `better-sqlite3` and `@types/better-sqlite3` are already declared dependencies of `cvf-web`, not a new install | dependency | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `dependencies` line 22; `devDependencies` line 51 | `better-sqlite3`; types | cvf-web package | ACCEPT |
| `/api/execute`'s `POST` composes admission via `admitAndInvokeProvider` and is already a large, provider-calling route; this decision must not widen it | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `POST` line 99; `admitAndInvokeProvider` call sites lines 801, 859 | `POST`; `admitAndInvokeProvider` | execute route | ACCEPT |
| Approval `PATCH` decides approval status only, writes only `ApprovalRequestRecord` fields via `store.set`, and never touches a pending-execution store or claim primitive | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | `PATCH` lines 57-119; `store.set` line 101; `appendAuditEvent` lines 103-116 | `PATCH`; audit | approval decision route | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Both worker output paths absent at executionBaseHead `175b489aa` | `git status --short --untracked-files=all` was clean before authoring | ACCEPT |
| Proposed source names collision search | `rg -n "pending-agent-execution-sqlite-store\|pending-agent-execution-composition\|PendingAgentExecutionSqliteStore" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` returned zero hits (`rg` exit code 1) | ACCEPT |
| Existing-owner collision | approval store, knowledge store, SOT3 evidence store, MAO durable store, generic SQLite adapter, `/api/execute`, and approval `PATCH` were each read fresh and classified below rather than assumed compatible | ACCEPT |
| `better-sqlite3` dependency status | confirmed existing in `package.json` `dependencies`/`devDependencies`; this decision proposes no new install | ACCEPT |

## Five Candidate Families Matrix

### Candidate 1: approval/knowledge file-backed stores

| Field | Value |
| --- | --- |
| Owner/path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` (`ApprovalStore`/`FileBackedApprovalStore`); `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` (`FileBackedKnowledgeStore`) |
| Interface fit | Neither exposes a `compareAndSwap(id, expectedVersion, expectedStatus, transition)`-shaped operation; both expose `Map`-style `set`/`upsert` semantics with no expected-prior-state precondition |
| Atomicity model | Whole-object last-writer-wins in memory (`Map.set`), whole-file temp-write-then-rename on disk; no per-record version field exists on either schema |
| Crash/error behavior | `ApprovalStore.persist()` swallows write failure with `console.warn` only (`store.ts` line 96) and never surfaces it to the caller; `FileBackedKnowledgeStore._persist()` does the same (`knowledge-store.ts` line 165) |
| Corruption behavior | `ApprovalStore.load()` clears the entire in-memory map on any parse failure (`store.ts` lines 74-82); `FileBackedKnowledgeStore._loadOrSeed()` silently falls back to defaults on parse failure |
| Process/node boundary | Single-process in-memory `Map` backed by best-effort file persistence; no cross-process read-modify-write protection |
| Dependency impact | None; reuses existing `node:fs` calls only |
| Composition fit | Would require overloading an unrelated schema (`ApprovalRequestRecord`/`KnowledgeCollectionDefinition`) with claim-state fields, conflating two authorities in one mutable object |
| Duplication risk | HIGH: mixing pending-execution claim state into the approval-decision or knowledge schema recreates exactly the authority-conflation risk the T0B assessment already rejected for Candidate 1 there |
| Disposition | `EXISTING_SOURCE_INCOMPATIBLE` |

### Candidate 2: SOT3/MAO atomic-file stores

| Field | Value |
| --- | --- |
| Owner/path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` (`Sot3ActivationEvidenceStore`); `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` (`MaoFileRunStore`) |
| Interface fit | SOT3's store is an append-only evidence ledger (`append`/`findByRecordId`); MAO's store is a single-task-graph replay/append store (`createRun`/`appendEvent`/`resumeRun`). Neither exposes a general keyed `compareAndSwap` over an arbitrary record ID with an expected-version/status precondition |
| Atomicity model | SOT3 serializes appends only via an in-process `Promise` chain (`appendQueue`, line 281) plus whole-file atomic rename; MAO validates/replays the whole snapshot and atomically renames the whole file on every append (`atomicWriteJson`, lines 443-462) |
| Crash/error behavior | SOT3 throws `Sot3EvidencePersistenceFailedError` on write/rename failure and leaves prior valid bytes unchanged (fail-closed, but process-local only); MAO's `atomicWriteJson` returns a typed failure and performs best-effort temp-file cleanup |
| Corruption behavior | SOT3 throws `Sot3EvidenceCorruptStoreError` on a per-record integrity failure; MAO's `loadAndReplay` rejects the whole run on any replay mismatch (`EVENT_REPLAY_REJECTED`) |
| Process/node boundary | Both are explicitly documented as process-local (SOT3's `appendQueue` docstring, lines 271-277) or single-caller-owned-root (MAO's file header, lines 1-17: "does not select a global/user/session/workspace path... Local execution-plane module only; no runtime caller"). Neither claims or provides cross-process mutual exclusion: two OS processes racing an atomic rename against the same path can each successfully replace the file in turn with no one-winner precondition check |
| Dependency impact | None |
| Composition fit | Both are purpose-built for their own domain (evidence ledger; MAO run graph) and are not general keyed record stores; retrofitting a claim primitive onto either duplicates the T0B-selected `PendingAgentExecutionRecord` domain into a foreign owner |
| Duplication risk | HIGH: a pending-execution claim bolted onto either store creates a second, incompatible schema/lifecycle owner alongside T1A's own `PendingAgentExecutionRecord` |
| Disposition | `EXISTING_SOURCE_INCOMPATIBLE` |

### Candidate 3: generic SQLite adapters (as-is)

| Field | Value |
| --- | --- |
| Owner/path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` (`SQLiteEventListAdapter`, `SQLiteKeyValueAdapter`) |
| Interface fit | `EventListAdapter`/`KeyValueAdapter` expose `append`/`writeAll`/`read`/`write` only; neither exposes a `compareAndSwap` with an expected-prior-state precondition, and `SQLiteKeyValueAdapter.write` takes no expected-version/status argument at all |
| Atomicity model | `openSQLiteDatabase` sets `journal_mode = WAL` and `synchronous = NORMAL` (lines 245-246); `SQLiteKeyValueAdapter.write` executes `INSERT ... ON CONFLICT(id) DO UPDATE SET item_json = excluded.item_json` (lines 360-364) with **no `WHERE` clause conditioning the update on a prior version or status value** -- this is ordinary upsert, not compare-and-swap, and the work order explicitly forbids presenting ordinary upsert as CAS proof |
| Crash/error behavior | `better-sqlite3` throws synchronously on `SQLITE_BUSY`/I-O failure; the adapter does not currently catch, retry, or map these into a typed failure result, and `busy_timeout` is not set (only `journal_mode`/`synchronous` are) |
| Corruption behavior | No schema-validation or digest-mismatch handling exists in either adapter; a malformed `item_json` blob is only discovered on `JSON.parse` at read time with no guard |
| Process/node boundary | Local single-node file (`.sqlite` file on the caller's filesystem); WAL mode does provide genuine cross-process file-level locking primitives at the SQLite engine level, but this adapter's own application code never uses a conditional `UPDATE ... WHERE version = ? AND status = ?` to build a one-winner CAS on top of that locking |
| Dependency impact | None; `better-sqlite3` is already a dependency (confirmed above) |
| Composition fit | The existing adapter is a generic capability, not a `PendingAgentExecutionRecord`-shaped schema; reusing it *as-is* (unmodified) cannot satisfy the T0B-mandated `compareAndSwap(pendingExecutionId, expectedVersion, expectedStatus, transition)` contract, because its only write primitive is unconditional upsert |
| Duplication risk | LOW if extended (see Candidate 5) but the *as-is, unmodified* adapter is unusable for this contract |
| Disposition | `EXISTING_SOURCE_INCOMPATIBLE` (as a direct, unmodified reuse target; it is the correct low-level SQLite capability to build upon, which is exactly Candidate 5) |

### Candidate 4: approval PATCH or `/api/execute` as direct composition owner

| Field | Value |
| --- | --- |
| Owner/path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` (`PATCH`); `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (`POST`) |
| Interface fit | `PATCH` only ever mutates `ApprovalRequestRecord` fields and calls `appendAuditEvent`; it never calls a claim/CAS primitive or a provider today. `/api/execute`'s `POST` already composes provider admission via `admitAndInvokeProvider` (lines 801, 859) |
| Atomicity model | N/A to this candidate's rejection; the defect is ownership, not atomicity |
| Crash/error behavior | N/A |
| Corruption behavior | N/A |
| Process/node boundary | Both are Next.js API route handlers running per-request in the same Node process as the rest of `cvf-web`; adding claim/composition logic here does not change the single-node boundary, but does change route authority |
| Dependency impact | None directly, but see composition fit |
| Composition fit | Making `PATCH` a composition owner would let "approval decided" and "execution claimed" collapse into one code path, which the T0B contract's Mandatory Invariant ("Approval PATCH starts zero provider calls and emits no executable grant") explicitly forbids. Making `/api/execute` the owner would require it to import and drive claim/CAS/version logic in a route the work order's own Source Verification Block flags as "already near its source-size ceiling" (T0B baseline) and that this T1B work order explicitly says "must not be widened by this decision" |
| Duplication risk | HIGH: erodes the approval-decision/execution-claim separation that both T0A and T0B established as the core safety property of this whole design |
| Disposition | `EXISTING_SOURCE_INCOMPATIBLE` |

### Candidate 5: new specialized server-only SQLite store plus new server-only composition module

| Field | Value |
| --- | --- |
| Owner/path | Proposed, not yet created: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` (class `PendingAgentExecutionSqliteStore`); `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` (function `buildPendingAgentExecutionRuntime`) |
| Interface fit | Would implement T1A's exact existing `PendingAgentExecutionStore` interface (`create`, `get`, `compareAndSwap`) from `pending-agent-execution.ts` lines 494-507. Existing claim/begin/terminal/drift functions remain unchanged; one bounded refactor exports a shared transition helper so both in-memory and SQLite stores use identical legality/application rules |
| Atomicity model | Built on the confirmed-existing `better-sqlite3` capability (Candidate 3), but adding a real conditional `UPDATE ... WHERE pending_execution_id = ? AND record_version = ? AND status = ?` inside a `db.transaction(...)` critical section. The transaction first decodes the row and applies one newly exported shared T1A transition helper, then persists that helper's result and checks `info.changes` for the one winner -- genuine linearizable CAS without duplicating T1A transition rules |
| Crash/error behavior | Uses `busy_timeout`, `synchronous = FULL`, and typed store errors. Because T1A's accepted synchronous interface returns a record from `create`/`get` rather than a result union, those two methods throw a typed `PendingAgentExecutionStoreError`; `compareAndSwap` may return a failed `CompareAndSwapResult`. The composition boundary catches typed store errors and returns zero grant authority. Create returns only after transaction commit and read-back |
| Corruption behavior | Uses `PRAGMA user_version = 1` as store-level schema metadata, retains a row-level schema constant, validates the complete decoded row, and recomputes the immutable digest. Unknown schema, malformed JSON/state, or digest mismatch fails closed without repair-on-read, deletion, or absent-row fallback |
| Process/node boundary | Single-node, multiple-OS-process: `better-sqlite3` opens a local file; WAL mode plus an explicit `busy_timeout` and the conditional `UPDATE ... WHERE` gives genuine mutual exclusion between multiple Node processes on the same host and filesystem. This is explicitly NOT a claim of cross-node, network-filesystem, or distributed-lock safety |
| Dependency impact | None: reuses the already-declared `better-sqlite3`/`@types/better-sqlite3` dependency; no `package.json` change |
| Composition fit | The new composition module would be the sole constructor of a wired `{ store, claim, begin, terminal }` runtime bundle for future callers, importing only from T1A's core (`pending-agent-execution.ts`) and the new SQLite store -- never from `execute/route.ts` or `approvals/[id]/route.ts`, and never calling `admitAndInvokeProvider` itself |
| Duplication risk | LOW BY DESIGN: it implements T1A's own interface rather than inventing a second schema, and keeps composition physically separate from both existing route owners |
| Disposition | `PROPOSED_NEW_OWNER_COMPATIBLE` |

## Mandatory Decision Questions (Thirteen, In Baseline Order)

**1. Which exact adapter class and repo-relative source path own persistence?**
`PendingAgentExecutionSqliteStore`, proposed at
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts`.
It implements T1A's existing `PendingAgentExecutionStore` interface
(`create`, `get`, `compareAndSwap`) verbatim; it is not created by this
tranche. Confirmed absent by the negative search above.

**2. Which exact composition function/module and path own future construction and orchestration without becoming a route or provider caller?**
`buildPendingAgentExecutionRuntime`, proposed at
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts`.
It may import only from `pending-agent-execution.ts` (T1A core) and
`pending-agent-execution-sqlite-store.ts` (this tranche's proposed store).
Forbidden imports: `src/app/api/execute/route.ts`, `src/app/api/approvals/[id]/route.ts`,
`src/lib/provider-attempt-admission.ts`, or any provider-invocation module.
It must never call `admitAndInvokeProvider` and must never be imported by
either forbidden route file. Not created by this tranche.

**3. What single-node process model is supported, and what distributed/network filesystem claims remain forbidden?**
Supported: multiple independent Node.js OS processes on **one physical or
virtual host**, all opening the same local `better-sqlite3` file path with
WAL journal mode and an explicit `busy_timeout`. Forbidden: any claim of
correctness over a network filesystem (NFS/SMB/cloud-mounted volume), any
multi-host/distributed-lock claim, and any claim that this adapter alone
proves cross-node safety. `better-sqlite3` is a synchronous, single-file,
single-host native binding; it has no network protocol and no cluster
coordination primitive.

**4. What SQLite/file schema stores immutable payload, digest, status, version, claim metadata, attempt index, request correlation, and terminal reason?**
One table, `pending_agent_execution` (schema version
`'cvf.pendingAgentExecutionSqlite.v1'`):

| Column | Type | Notes |
| --- | --- | --- |
| `pending_execution_id` | `TEXT PRIMARY KEY` | matches T1A's `pendingExecutionId` |
| `schema_version` | `TEXT NOT NULL` | literal `'cvf.pendingAgentExecutionSqlite.v1'` |
| `created_at` | `TEXT NOT NULL` | ISO 8601, immutable |
| `payload_json` | `TEXT NOT NULL` | canonical JSON of T1A's `PendingAgentExecutionImmutablePayload`, immutable |
| `guard_policy_fingerprint` | `TEXT NOT NULL` | lowercase 64-hex, immutable |
| `record_digest` | `TEXT NOT NULL` | lowercase 64-hex, immutable, matches T1A's `computeRecordDigest` |
| `status` | `TEXT NOT NULL` | one of T1A's `PendingAgentExecutionStatus` values; mutable only via CAS |
| `record_version` | `INTEGER NOT NULL DEFAULT 0` | monotonically incremented by each successful CAS; the CAS version field |
| `claim_id` | `TEXT` | nullable; set only on successful `CLAIM` transition |
| `claimed_at` | `TEXT` | nullable ISO 8601 |
| `claimed_by_json` | `TEXT` | nullable JSON of `ApprovalActorBinding` |
| `attempt_index` | `INTEGER` | nullable; set only on `BEGIN_EXECUTING` |
| `request_id` | `TEXT` | nullable; set on `CLAIM` |
| `terminal_reason` | `TEXT` | nullable; set on any terminal-producing transition |
| `terminal_at` | `TEXT` | nullable ISO 8601 |

Constraints: `PRIMARY KEY (pending_execution_id)`; `CHECK (record_version >= 0)`;
`CHECK (status IN ('CREATED','CLAIMED','EXECUTING','SUCCEEDED','FAILED','DENIED','EXPIRED','STALE','ABANDONED_BEFORE_START','UNKNOWN_TERMINAL'))`;
an index `CREATE INDEX IF NOT EXISTS idx_pending_agent_execution_status ON pending_agent_execution(status)`
to support future reconciliation sweeps scanning `CLAIMED` rows. Schema
identity is owned at store level by `PRAGMA user_version = 1`, set only when
the store creates a new schema. An existing non-empty database whose
`user_version` is not exactly `1` fails store-open closed; the row-level
`schema_version` constant is defense in depth. No automatic migration occurs.

**5. What create transaction proves uniqueness and durable read-back?**
`create` executes inside one `db.transaction(...)`: (a) `INSERT INTO
pending_agent_execution (...) VALUES (...)` with no `ON CONFLICT` clause, so
a duplicate `pending_execution_id` throws a SQLite `UNIQUE` constraint
violation and the transaction rolls back atomically (uniqueness proof); (b)
immediately inside the same transaction, `SELECT record_digest FROM
pending_agent_execution WHERE pending_execution_id = ?` reads back the just
-written row; (c) the read-back `record_digest` is compared byte-for-byte to
the value computed before the write. Only if (a), (b), and (c) all succeed
does the transaction commit. With `synchronous = FULL`, `create` returns the
`CREATED` record only after that commit completes; it does not acknowledge
from the pre-commit read-back. Any failure at any step fails closed with no
partial row (SQLite transactions are all-or-nothing).

**6. What exact conditional CAS predicate produces one winner across Node processes on the same host?**
```sql
UPDATE pending_agent_execution
SET status = @nextStatus,
    record_version = record_version + 1,
    claim_id = @claimId,
    claimed_at = @claimedAt,
    claimed_by_json = @claimedByJson,
    request_id = @requestId,
    attempt_index = @attemptIndex,
    terminal_reason = @terminalReason,
    terminal_at = @terminalAt
WHERE pending_execution_id = @pendingExecutionId
  AND record_version = @expectedVersion
  AND status = @expectedStatus;
```
Executed via a prepared statement's `.run(params)` inside a
`db.transaction(...)` wrapper. Before this statement, the same transaction
selects and decodes the current row and invokes the shared T1A transition
helper selected in Question 10; all `SET` values come from that helper's
validated result. The one-winner predicate is the returned
`changes` count: exactly one racing process observes `info.changes === 1`
(its expected `record_version`/`status` pair still matched at UPDATE time);
every other process's identical UPDATE observes `info.changes === 0` because
the row's `record_version`/`status` already advanced, and that process must
re-`SELECT` and report `CAS_CONFLICT` rather than retry blindly. This is the
same three-column WHERE-predicate-plus-changed-row-count pattern the T0B
contract requires and the work order explicitly forbids substituting with
rename or unconditional upsert; unlike `SQLiteKeyValueAdapter.write`'s
`ON CONFLICT ... DO UPDATE` (no WHERE clause at all), this statement's WHERE
clause is the entire correctness mechanism.

**7. What journal, synchronous, busy-timeout, transaction, and error settings are required, and which failures return zero grant authority?**
`journal_mode = WAL`; `synchronous = FULL` (stronger than the generic
adapter's `NORMAL`, because T0B requires acknowledgement only after durable
success); a new required
`busy_timeout = 5000` pragma (not currently set by `storage-adapter.ts` and
must be added by this proposed store, since a claim CAS retried without a
busy timeout can spuriously fail under concurrent load); every multi-
statement operation (`create`, `compareAndSwap`) runs inside exactly one
`db.transaction(...)` call so partial writes are impossible. Failure mapping:
a thrown `SQLITE_BUSY` (timeout exceeded), any I/O exception, or any
constraint violation fails closed. T1A's accepted synchronous interface is
preserved exactly: `create` and `get` throw a typed
`PendingAgentExecutionStoreError` (`BUSY_TIMEOUT`, `IO_FAILURE`,
`CORRUPT_ROW`, or `SCHEMA_MISMATCH`) because their signatures do not admit a
result union; `compareAndSwap` returns `{ ok: false, reason, record: null }`
when safely representable, otherwise throws the same typed error. The future
composition wrapper catches these errors and returns no grant or execution
authority. There is no blind retry.

**8. How are corrupt, partially migrated, unknown-schema, and digest-mismatched rows handled without repair-on-read or silent fallback?**
At store-open, `PRAGMA user_version` must be exactly `1` for an existing
schema; `0` is accepted only for a genuinely new empty database being created
by this store. Every `get` then validates the row-level `schema_version`, all
required columns, status enum, non-negative integer version/attempt fields,
canonical timestamps, nullable-state invariants, and both JSON columns.
`payload_json` is normalized with T1A's exported validators and
`record_digest` is recomputed. Any unknown/partial schema, malformed JSON or
state, or digest mismatch throws the typed fail-closed store error and makes
the row non-executable; it is never returned as valid, silently skipped,
treated as absent, repaired, migrated, or deleted. No behavior may resemble
`FileBackedApprovalStore.load()`'s whole-store `clear()` on parse failure.

**9. How do `CLAIMED`, `EXECUTING`, crash-before-start, and ambiguous-after-start recovery preserve T0B/T1A semantics?**
Unchanged from T1A's already-implemented, reviewer-corrected lifecycle
(`pending-agent-execution.ts` lines 330-340, 509-516): `CLAIMED` may only
advance to `EXECUTING` via `beginPendingExecution`'s CAS, or terminate via
`ABANDON_BEFORE_START` (crash-before-start, reconciliation-only, never
re-admits a second claim for the same `pendingExecutionId`). Once `EXECUTING`
is durably persisted (a successful CAS row in the SQLite table, not merely an
in-memory grant), a crash or timeout can only resolve to `UNKNOWN_TERMINAL`
via `resolveAmbiguousExecutingCrash`, never back to a retryable state and
never to a second provider call. The lifecycle remains owned by T1A. The
later implementation must first expose and reuse one shared pure transition
helper from that core, as Question 10 specifies, so both stores apply the
same legality and identity rules while SQLite adds durable CAS.

**10. Which T1A core symbols may the adapter import, and how is duplicate state validation avoided?**
Fresh source review found that T1A's transition helpers are currently private:
`LEGAL_TRANSITION_FROM` (line 509), `applyTransition` (line 539), and
`validateTransitionIdentity` (line 576). Therefore a later implementation
must make one bounded T1A core change before adding the SQLite store: export a
single pure `applyPendingAgentExecutionTransition` helper that returns the
same `CompareAndSwapResult` semantics, and refactor
`InMemoryPendingAgentExecutionStore.compareAndSwap` to call it. The SQLite
store must call that same helper after decoding the selected row and before
its conditional update. It may otherwise import only T1A record/transition
types, `canonicalizeToJson`, `computeRecordDigest`,
`computeGuardPolicyFingerprint`, `validateEnvironmentIdentity`, and
`validateGuardPolicySnapshot`. Store-owned row decoding validates persistence
representation; the shared helper remains the sole owner of transition
legality and claim/attempt identity rules. `claimPendingExecution`,
`beginPendingExecution`, terminal/reconciliation functions, and drift checks
remain in T1A and are not reimplemented.

**11. Why are the four non-selected candidate families unsafe or owner-wrong?**
Candidate 1 (approval/knowledge stores) conflates approval-decision and
execution-claim authority in one mutable schema with no CAS primitive at
all -- rejected for the same reason the T0B assessment already rejected
extending `ApprovalRequestRecord`. Candidate 2 (SOT3/MAO atomic-file stores)
provides only process-local serialization or whole-file atomic rename, never
a cross-process one-winner precondition check, and is purpose-built for a
different domain (evidence ledger; MAO task-graph replay). Candidate 3
(generic SQLite adapters, as-is) has genuine WAL/transaction infrastructure
but its only write primitive is unconditional `ON CONFLICT ... DO UPDATE`
upsert with no `WHERE` predicate on prior state, so it cannot express CAS
without modification -- this is exactly the "ordinary SQLite upsert is not
CAS proof" trap the work order names explicitly. Candidate 4 (approval PATCH
or `/api/execute` as composition owner) would erode the approval-decision/
execution-claim separation that is the core safety property established in
T0A/T0B, and would additionally violate this work order's explicit
prohibition on widening `/api/execute`.

**12. What smallest future implementation/test manifest is authorized for later consideration, with no route/provider/audit integration?**
1. Modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`
   only to export the shared pure transition helper described in Question 10
   and refactor the existing in-memory store to use it without behavior drift.
2. Extend `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.test.ts`
   with parity regressions proving the shared helper preserves all current
   in-memory transition outcomes.
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts`
   -- the `PendingAgentExecutionSqliteStore` class implementing T1A's
   `PendingAgentExecutionStore` interface, taking an explicit caller-supplied
   database file path (see Foundation Storage Layout below) with no default.
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts`
   -- the `buildPendingAgentExecutionRuntime` composition function, importing
   only from (1), (3), and T1A's core, never from a route file.
5. A focused Vitest file (e.g.
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.test.ts`)
   proving, at minimum, every negative case in this list: concurrent CAS race
   yields exactly one winner and the loser observes `CAS_CONFLICT`
   (`info.changes === 0`); a UNIQUE-violation on duplicate `create` never
   returns an acknowledged ID; a simulated `SQLITE_BUSY` under `busy_timeout`
   exhaustion yields a typed store failure and zero grant authority at the
   composition boundary; a digest-mismatched row fails closed without repair-
   on-read; a store re-opened with a mismatched `PRAGMA user_version` or row
   `schema_version` fails closed;
   process-restart reconciliation ages a `CLAIMED` row into
   `ABANDONED_BEFORE_START` without a second provider call being possible
   (no provider is called by the test -- this proves the state transition
   only). All tests use a temporary directory-backed database path (e.g.
   `node:fs.mkdtempSync`) and never a shared/global path.
This manifest authorizes no route, no provider-admission wiring, and no
audit-emission integration; those remain separately gated per Question 13.

**13. What separate evidence would be required before a production consumer, cross-node store, route, provider admission, or audit integration opens?**
- **Route reopen gate:** a fresh, separately authorized work order naming
  the exact HTTP surface, request/response schema, and authentication model
  that would call `buildPendingAgentExecutionRuntime`; this T1B decision
  authorizes no route.
- **Provider admission reopen gate:** fresh evidence that the composition
  module's `EXECUTING`-transition consumer calls `admitAndInvokeProvider`
  exactly once per successful claim-to-consumption path, verified via
  `ProviderAttemptLedger.providerCallCount`, plus the full negative-test
  manifest from the T0B assessment's Q17 (concurrent double claim, stale
  binding, stale policy fingerprint, expired/non-approved approval, forged
  grant, write failure, corruption, restart-abandonment, double-consumption,
  exactly-one-provider-call, terminal-audit-completeness).
- **Audit integration reopen gate:** evidence that every lifecycle transition
  emits `appendAuditEvent` carrying `approvalId`, `pendingExecutionId`,
  `claimId`, `requestId`, `attemptIndex`, and `recordVersion`, matching T0B
  Q16/Q9's correlation contract.
- **Production/cross-node reopen gate:** a separate, explicitly authorized
  tranche naming a distributed or networked storage backend (this decision
  makes zero claim beyond one host's local filesystem) plus live-provider
  proof; this T1B decision explicitly excludes and does not imply that
  authority.

## Decision / Baseline / Proposed Tranche

Terminal token: **`SPECIALIZED_SQLITE_SINGLE_NODE_ADAPTER_AND_COMPOSITION_OWNER_SELECTED`**

Not selected:

- `EXISTING_OWNER_REUSE_SELECTED` -- NOT SELECTED. Every existing storage
  owner examined (approval store, knowledge store, SOT3 evidence store, MAO
  durable store, and the generic SQLite adapter as currently written) either
  lacks any compare-and-swap primitive or exposes only unconditional upsert;
  none can satisfy the T0B-mandated `compareAndSwap(pendingExecutionId,
  expectedVersion, expectedStatus, transition)` contract without being
  extended into what is functionally Candidate 5.
- `NO_SAFE_DURABLE_COMPOSITION_RETAIN_PARKED` -- NOT SELECTED. A safe boundary
  is exactly nameable from current source: `better-sqlite3` is a confirmed
  existing dependency with WAL/transaction support, T1A's
  `PendingAgentExecutionStore` interface is already durable-storage-shaped
  (it was designed for exactly this seam), and the exact table schema, CAS
  predicate, and reopen gates are all stated above without inventing any
  currently-absent capability. Parking would be correct only if no
  source-backed boundary could be stated, which is not the case here.

## Frozen Future-Manifest Details

- **Exact future adapter class/path:** `PendingAgentExecutionSqliteStore` at
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts`.
- **Exact future composition owner function/path and forbidden imports:**
  `buildPendingAgentExecutionRuntime` at
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts`;
  forbidden imports: `src/app/api/execute/route.ts`,
  `src/app/api/approvals/[id]/route.ts`,
  `src/lib/provider-attempt-admission.ts`, and any provider client module.
- **Exact SQLite table/index/constraint and schema version:** table
  `pending_agent_execution`, schema version
  `'cvf.pendingAgentExecutionSqlite.v1'`, `PRAGMA user_version = 1`,
  `PRIMARY KEY (pending_execution_id)`, version/status checks, index
  `idx_pending_agent_execution_status` on `status` -- full column list in
  Question 4 above.
- **Create and CAS transaction pseudocode, including the one-winner
  predicate:** given in Questions 5 and 6 above (`INSERT` + read-back inside
  one transaction for create; `UPDATE ... WHERE pending_execution_id = ? AND
  record_version = ? AND status = ?` with `changes === 1` as the one-winner
  predicate for CAS).
- **`journal_mode`, `synchronous`, `busy_timeout`, transaction mode, and
  `SQLITE_BUSY`/I-O/corruption failure mapping:** `WAL` / `FULL` / `5000`ms
  / one `db.transaction(...)` per operation / typed store errors or failed
  CAS results, caught at composition so they never return a grant -- given in
  full in Question 7.
- **Row validation/read-back and T1A digest verification:** create requires
  a same-transaction read-back digest match followed by a `FULL` synchronous
  commit before acknowledgement (Question 5); every `get` validates the full
  persistence row and recomputes `record_digest` (Question 8).
- **Crash reconciliation for pre-start and post-start windows:** pre-start
  (`CLAIMED` never reaching `EXECUTING`) reconciles to
  `ABANDONED_BEFORE_START` via T1A's existing `abandonBeforeStart`; post-start
  (`EXECUTING` durably persisted, then crash/timeout) reconciles only to
  `UNKNOWN_TERMINAL` via T1A's existing `resolveAmbiguousExecutingCrash` --
  both reused unmodified (Question 9).
- **Explicit single-node multi-process boundary and distributed
  exclusions:** one host, multiple Node processes, one local file; explicitly
  excludes network filesystems, multi-host, and any distributed-lock claim
  (Question 3).
- **Smallest later implementation manifest with focused tests:** given in
  full in Question 12 (one bounded T1A core/helper refactor and parity-test
  update, store file, composition file, and focused SQLite test file).
- **Separate reopen gates for route, provider admission, audit, and
  production:** given in full in Question 13.

## Foundation Storage Layout Block

Decision-only; no file, directory, or database is created by this tranche.
Any later implementation's SQLite path must be an explicit caller-supplied
constructor argument to `PendingAgentExecutionSqliteStore` (for example,
`new PendingAgentExecutionSqliteStore(dbPath)`), never a default, global,
user-home, repository-root, or implicit environment-variable-derived path.
Tests must use a temporary directory (`node:fs.mkdtempSync` or equivalent)
for their database file and must never write to a shared or repository path.
The store constructor must fail closed (throw or return a typed failure) if
`dbPath` is missing, empty, or not a string, mirroring
`MaoFileRunStore`'s existing constructor guard
(`durable.run.store.ts` lines 114-119).

## Evidence / Verification

Required evidence for this decision is: a fresh execution base and clean
pre-authoring status (`175b489aa`); exact source reads of every file in the
Source Verification Block above; the exact negative-search command and its
zero-hit result; the complete five-family classification matrix; all
thirteen ordered baseline questions answered with source citations; exactly
one selected terminal token with the other two explicitly marked not
selected; the exact two-file worker output diff; the worker-return fast
gate; and a zero external/provider call statement. All of these are recorded
above (Source Verification Block, Negative Search And Collision Discipline,
Five Candidate Families Matrix, Mandatory Decision Questions,
Decision / Baseline / Proposed Tranche) and in the paired worker return's
Command Evidence section.

## Independent Reviewer Contract Correction

The selected terminal and Candidate 5 owner direction are retained, but this
section controls over conflicting worker-authored wording elsewhere in the
original return. Fresh review found one root-cause cluster: the proposed
adapter contract assumed transition helpers and typed failure results that
the accepted synchronous T1A interface does not currently expose.

The controlling corrections are:

1. SQLite uses `WAL`, `synchronous = FULL`, and `busy_timeout = 5000`; create
   acknowledges only after the transaction commit completes.
2. `PRAGMA user_version = 1` owns store-level schema identity; the row-level
   schema constant remains defense in depth. Unknown or partial schema and any
   malformed/digest-invalid row fail closed without repair or absent fallback.
3. `create`/`get` preserve T1A's synchronous signatures and therefore throw a
   typed store error; CAS may return a failed `CompareAndSwapResult`. The
   composition boundary catches failures and creates zero grant authority.
4. Because T1A's legality/application helpers are private today, the future
   implementation must export one shared pure transition helper and refactor
   the in-memory store to use it before the SQLite store reuses it. This is a
   bounded core parity refactor, not permission to change lifecycle semantics.
5. The smallest truthful future manifest is the five paths in Question 12.
   No implementation path is authorized by this closed decision itself.

## Findings / Position

Terminal decision:
`SPECIALIZED_SQLITE_SINGLE_NODE_ADAPTER_AND_COMPOSITION_OWNER_SELECTED`.

T1A's `PendingAgentExecutionStore` interface was already designed around a
`compareAndSwap(pendingExecutionId, expectedVersion, expectedStatus,
transition)` contract -- the T0B reviewer correction explicitly required this
shape and T1A's accepted implementation delivers it for the single-process
case. The only remaining question was whether a durable, cross-process
backend for that same interface already exists in this codebase. It does
not: every existing candidate either has no compare-and-swap primitive
(approval/knowledge/SOT3/MAO) or has only unconditional upsert
(the generic SQLite key-value adapter's `ON CONFLICT ... DO UPDATE`, which
this assessment explicitly does not accept as CAS proof). `better-sqlite3`
is, however, a confirmed existing dependency with genuine WAL-mode
cross-process file locking at the engine level; building one specialized
store that implements T1A's own interface with a real conditional
`UPDATE ... WHERE record_version = ? AND status = ?` predicate is the
correct, minimal path once T1A exposes one shared transition helper for both
the in-memory and SQLite stores; no route, provider, or audit authority is
opened by naming it.

## Risk / Corrective Action

The primary risk is a future implementer treating `SQLiteKeyValueAdapter`'s
existing unconditional upsert, or a plain atomic file rename, as sufficient
proof of cross-process CAS. The corrective action is that this assessment
names the exact conditional `UPDATE ... WHERE pending_execution_id = ? AND
record_version = ? AND status = ?` predicate and the `changes === 1`
one-winner check as the only acceptable mechanism, and explicitly rejects
rename/mutex/upsert as substitutes, per the work order's own prohibition.

A secondary risk is a future implementer skipping the `busy_timeout` pragma
(not set by the existing adapter) and hitting spurious `SQLITE_BUSY` failures
under concurrent claim attempts. The corrective action is Question 7's
explicit requirement to add `busy_timeout = 5000`, surface a typed store
failure matching the synchronous interface, and catch it at composition with
zero grant authority.

A tertiary risk is a future implementer reimplementing T1A transition
legality inside the new SQLite store. Fresh review confirmed those helpers are
currently private, so Question 10 and the future manifest now require one
shared exported transition helper used by both stores, while persistence-row
decoding remains store-owned.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private decision-only system-chain dispatch; no public artifact,
runtime behavior, or release claim is authorized by this assessment. No
public-sync boundary is crossed by this documentation-only decision.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | source-table columns and dispositions (`EXISTING_SOURCE_COMPATIBLE`, `EXISTING_SOURCE_INCOMPATIBLE`, `PROPOSED_NEW_OWNER_COMPATIBLE`, `NO_CURRENT_OWNER`); Agent-Operation-Trace-Block required label set; Delta-Execution-Claim-Boundary required field set and accepted enum tokens (`CLAIM_REJECTED`, `CLAIM_REJECTED_NO_RECEIPT`, `CLAIM_REJECTED_NO_ACTION`); Public-Export-Disposition allowed tokens (`EXPORTED`, `DEFERRED_PRIVATE_ONLY`, `BLOCKED_MISSING_PUBLIC_ARTIFACTS`); Checker-Source-Read-Ahead-Block required fields (`applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, `claimBoundary`); the three allowed terminal tokens for this decision |
| gateRunPurpose | confirmation evidence after direct checker-source inspection; checker constants were read and reviewed before this artifact was authored, not discovered via gate failure |
| claimBoundary | shape and source-fact readiness only; this block makes no independent semantic-acceptance claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit decision worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | GC010-SCR-R2-T1B worker execution, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | direct file reads, `rg`, `git rev-parse`/`git status`, `python governance/compat/run_agent_autorun_workflow_gate.py` |
| Target paths | all files listed in Source Verification Block above, plus this assessment and the paired worker return |
| Allowed scope source | work order Worker Autonomy / No-Question Rule and Scope sections |
| Before status evidence | executionBaseHead `175b489aa`; `git status --short --untracked-files=all` clean; both output paths absent |
| After status evidence | this assessment and the paired worker return created; no other path changed |
| Diff evidence | `git diff --name-status` |
| Approval boundary | decision-only; no runtime, route, package, test, checker, or workflow change |
| Claim boundary | architecture/schema decision and contract specification only; no runtime behavior, export, route, provider, store, or grant is implemented or claimed |
| Agent type | delegated worker |
| Invocation ID | `gc010-scr-r2-t1b-worker-2026-08-31` |
| Expected manifest | `docs/assessments/CVF_GC010_SCR_R2_T1B_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_ADAPTER_COMPOSITION_OWNER_DECISION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1B_PENDING_AGENT_EXECUTION_DURABLE_SINGLE_NODE_ADAPTER_COMPOSITION_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` |
| Actual changed set | the same two paths; no other path was created, modified, or deleted |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this tranche |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only durable single-node adapter and composition owner decision; no runtime behavior |
| claimDisposition | CLAIM_REJECTED: no execution-control, governed-coding-control, interception, or runtime-enforcement claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is produced by this decision |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: only file reads, exact `rg`/`git` searches, one autorun gate run, and two documentation outputs occurred |
| invocationBoundary | no route, provider, store, or adapter is invoked, created, or registered |
| interceptionBoundary | no wrapper, proxy, or mandatory runtime control is implemented or proposed as already active |
| claimLanguage | proposed schema/table/CAS/composition contract and named future-manifest gaps only |
| forbiddenExpansion | runtime/package/Web mutation, provider/live, public, deploy, production, and automatic T1C opening remain out of scope of this decision |

## Claim Boundary

This assessment records a documentation-only durable single-node adapter and
composition owner decision. It selects
`SPECIALIZED_SQLITE_SINGLE_NODE_ADAPTER_AND_COMPOSITION_OWNER_SELECTED`,
names the exact `PendingAgentExecutionSqliteStore` class/path,
`buildPendingAgentExecutionRuntime` composition function/path, SQLite
schema, CAS transaction, and pragma settings, and states a future negative-
test manifest. It does not create a store, route, claim primitive, resume
grant, AER export, or provider adapter, call a provider, open a T1C
implementation tranche, or claim live, public, deployment, or production
readiness. `successorTrancheOpened: NO`.
