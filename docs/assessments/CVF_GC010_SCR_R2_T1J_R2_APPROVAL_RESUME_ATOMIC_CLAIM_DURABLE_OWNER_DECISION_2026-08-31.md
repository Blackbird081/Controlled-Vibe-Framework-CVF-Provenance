# CVF GC010 SCR-R2-T1J-R2 Assessment - Approval Resume Atomic Claim Durable Owner Decision

Memory class: governed-worker-assessment

docType: assessment

Status: COMPLETE_PENDING_REVIEW

Batch ID: GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION

Date: 2026-08-31

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`

executionBaseHead: `1f20225422166dc5161bfd3db50d3ae6788b27df`

successorTrancheOpened: NO

Selected terminal: `PARTIAL_READY_REQUIRES_FAILURE_RECOVERY_INTERFACE_DECISION`

## Purpose

Resolve the one bounded decision left open by accepted T1J-R1: select the smallest safe durable owner for atomic
approval-resume claim and recovery semantics, while `/api/execute` retains its existing single guard and
provider-admission pipeline. Compare four candidates, answer twelve mandatory questions, and select one terminal
without implementing, migrating, or wiring anything.

## Target / Source

- T1J-R1 accepted assessment: `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md`
- Approval store: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts`
- Execute route approval block: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Pending-agent-execution core: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`
- Pending-agent-execution SQLite store: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts`
- Pending-agent-execution composition: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts`
- Local harness (existing caller pattern for the pending runtime): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts`

## Scope / Methodology

Worker captured clean execution base `1f20225422166dc5161bfd3db50d3ae6788b27df` (confirmed by `git rev-parse HEAD`;
`git status --short --untracked-files=all` returned empty). Both output paths were confirmed absent before authoring.
Pre-implementation autorun gate passed before authoring.

Worker read the T1J-R2 baseline and work order, the accepted T1J-R1 assessment in full, and every source path named
in both packets, each read in full: the approval store's persistence implementation, the complete approval-resume
validation and consumption block inside `POST /api/execute`, the pending-agent-execution core's transition/CAS
functions (`applyPendingAgentExecutionTransition`, `claimPendingExecution`, `beginPendingExecution`,
`applyTerminalTransition`, `resolveAmbiguousExecutingCrash`, `abandonBeforeStart`, `expirePendingExecution`), the
SQLite store's `compareAndSwap` transaction implementation, and the composition module's bounded wrapper interface
and `dbPath` contract. Line citations were re-verified fresh at this execution base rather than inherited from T1J-R1
without recomputation (`rg` re-run against `route.ts` confirms identical line numbers, zero drift). This assessment
performs read-only source reconciliation; it makes zero source, test, package, script, or session-state edits and
zero provider/network/browser/credential/live calls.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `ApprovalStore` exposes independent Map get/set/delete plus whole-file persist; no CAS or lifecycle state machine | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | lines 63-137 | `ApprovalStore`; `FileBackedApprovalStore`; `persist` | approval store | ACCEPT |
| Execute route's approval-status check and later delete are two independent, non-atomic operations around one claimed provider call | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 184-267 (validation), 496-513 (consume), 801/859 (provider attempts) | `approvedRequestRecord`; `getApprovalStore().delete`; `admitAndInvokeProvider` | `POST` | ACCEPT (re-verified, zero line drift from T1J-R1) |
| Pending core's `claimPendingExecution` performs a true single-winner CAS claim (`CREATED` to `CLAIMED`) with an unforgeable, single-use `ResumeAuthorityGrant` | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 775-818 (grant), 888-925 (`claimPendingExecution`) | `ResumeAuthorityGrant`; `isAuthenticUnconsumedGrant`; `claimPendingExecution` | pending core | ACCEPT |
| `beginPendingExecution` consumes the grant exactly once (`VALID_GRANTS.delete`) before a second CAS to `EXECUTING`, closing the pre-provider-call window | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 939-970 | `beginPendingExecution` | pending core | ACCEPT |
| `applyTerminalTransition`/`resolveAmbiguousExecutingCrash`/`abandonBeforeStart` name explicit CAS-guarded terminal, ambiguous-crash, and pre-start-abandon transitions | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 972-998 | `applyTerminalTransition`; `resolveAmbiguousExecutingCrash`; `abandonBeforeStart`; `expirePendingExecution` | pending core | ACCEPT |
| SQLite store's `compareAndSwap` runs inside one `IMMEDIATE` transaction with a `WHERE record_version = ? AND status = ?` predicate; fails closed on corrupt/schema-mismatched rows | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | lines 646-743 | `compareAndSwap`; `runCas.immediate()` | SQLite store | ACCEPT |
| Composition's `buildPendingAgentExecutionRuntime` exposes only create/get/claim/begin/terminal/reconciliation; never a guard engine or provider call; requires a caller-supplied, non-empty, absolute `dbPath` with no default/env/global path anywhere in source | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | lines 110-224; `pending-agent-execution-sqlite-store.ts` lines 437-450 | `buildPendingAgentExecutionRuntime`; `PendingAgentExecutionComposedRuntime` | pending composition | ACCEPT |
| No current caller of the pending runtime uses a process-lifetime singleton or default storage path; the only existing caller (local harness) requires the caller to pass `dbPath` and to `close()` the store itself | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts` | lines 1-136 | `PendingAgentExecutionLocalHarnessInput.dbPath`; `runtime.close()` | local harness | ACCEPT |
| Approval store, by contrast, is a resolved-path, module-level, process-lifetime singleton constructed once at import | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | lines 124-137 | `createApprovalStore`; `getApprovalStore` | approval store | ACCEPT |
| T1J-R1 leaves durable claim ownership unresolved | accepted assessment | `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md` | Independent Reviewer Correction; Decision | `PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION` | T1J-R1 | ACCEPT |

## Required Candidate Comparison (4/4)

### Candidate 1: extend the existing approval store with an atomic claim, recovery, and terminal-state contract

| Field | Value |
| --- | --- |
| Classification | `NO_CURRENT_OWNER` |
| Creation owner | Existing: `ApprovalStore.set` at approval-issuance time inside `/api/execute` (line 521 in current route). No change needed here. |
| Claim owner | Proposed only: `ApprovalStore` would need a new method (for example `claimIfApproved(id)`) implementing the same read-check-write-inside-one-critical-section pattern `PendingAgentExecutionSqliteStore.compareAndSwap` already implements, but `ApprovalStore` today is a plain `Map` subclass with independent `get`/`set`/`delete` overrides and no transactional primitive of any kind (`store.ts` lines 63-116). |
| Begin/provider-attempt owner | Unchanged: `/api/execute`'s existing `admitAndInvokeProvider` calls (lines 801, 859), outside this candidate's scope |
| Terminal owner | Proposed only: would require adding terminal-state fields (`'claimed' \| 'consumed' \| 'crashed'`) to `ApprovalRequestRecord` and teaching `FileBackedApprovalStore.persist` to treat them meaningfully |
| Retry/recovery owner | Proposed only; would require designing crash-ambiguity handling (a `SUCCEEDED`-vs-`UNKNOWN_TERMINAL` distinction) from scratch, since `ApprovalStore` currently has no concept of an in-flight "begin executing" state at all |
| Audit owner | Existing `appendAuditEvent` call at consumption (line 500, `APPROVAL_CONSUMED`); unchanged |
| Storage-path/cleanup owner | Existing: `APPROVAL_STORE_PATH` env var or `process.cwd()/.data/approval-store.json` default (`store.ts` line 129); unchanged if this candidate is selected |
| Duplicate-boundary risk | NONE new: this candidate adds zero new guard/admission/provider boundary; it only proposes strengthening an existing store's internal atomicity |
| Value beyond current route | Would close the TOCTOU window using the store the route already imports, avoiding a second dependency, but requires designing and building a new CAS primitive from scratch inside `ApprovalStore` rather than reusing one that already exists and is already proven (below) |
| Smallest future manifest | Not proposed as ready in this tranche: reinventing a CAS/terminal-state machine inside `ApprovalStore` duplicates design and test surface that `pending-agent-execution.ts`'s transition graph, `LEGAL_TRANSITION_FROM` table, and `PendingAgentExecutionSqliteStore.compareAndSwap` already implement and have already been independently accepted (T1A-T1C) |

### Candidate 2: compose `buildPendingAgentExecutionRuntime` narrowly inside the existing `/api/execute` path, preserving the route's sole guard/provider owners

| Field | Value |
| --- | --- |
| Classification | `PROPOSED_NEW_OWNER_COMPATIBLE` (structurally compatible; one open interface decision remains, see below) |
| Creation owner | `/api/execute`'s existing `NEEDS_APPROVAL` branch (line ~517-546) would additionally call `runtime.create(...)` with the same `approvalId` already generated there, binding one pending-execution record to one approval record at the same creation instant. `computeRecordDigest`/`approvalRequestHash` binding (already used by both `ApprovalStore` and the pending core) prevents drift between the two records without needing a second identifier scheme (directly answers Question 5). |
| Claim owner | `runtime.claim(...)` (`claimPendingExecution`) replacing the route's current plain `approvalRecord.status !== 'approved'` check; this call already performs the drift/staleness checks (actor, hash, expiry, policy fingerprint) the route currently performs manually inline (lines 196-238), so composing it would consolidate rather than duplicate that validation logic |
| Guard owner | Unchanged: `/api/execute`'s existing single `runExecuteRouteMandatoryGateway` call remains the only guard boundary; the pending runtime has no guard call of its own (confirmed: `buildPendingAgentExecutionRuntime`'s interface exposes only `create`/`get`/`claim`/`begin`/`terminal`/`resolveAmbiguousExecutingCrash`/`abandonBeforeStart`/`expire`, never a `GuardRuntimeEngine` reference) |
| Provider/admission owner | Unchanged: `/api/execute`'s existing `admitAndInvokeProvider` calls remain the only provider-attempt admission boundary; `runtime.begin(...)` (`beginPendingExecution`) would be called immediately before the existing `admitAndInvokeProvider` call, and `runtime.terminal(...)` immediately after it resolves, without the pending runtime ever calling a provider itself |
| Durable owner | `PendingAgentExecutionSqliteStore`, for the claim/begin/terminal lifecycle only; `ApprovalStore` remains the durable owner of the approval decision itself (immutable once approved/rejected). These are two distinct facts (`the admin decided X` vs. `execution attempt N of approval X reached state Y`) that do not need one shared store to avoid duplication, because neither store's write path overlaps the other's (directly answers Question 8) |
| Response/failure owner | `/api/execute`'s existing response builder; `runtime.terminal(...)`'s result (`SUCCEEDED`/`FAILED`/`DENIED`/`UNKNOWN_TERMINAL`) would map onto the route's existing success/error response branches, not replace them |
| Exact call order (answers Question 7) | 1) `runExecuteRouteMandatoryGateway` (unchanged, exactly once); 2) on `NEEDS_APPROVAL` with no `approvalId`: existing `ApprovalStore.set` plus new `runtime.create(...)`; 3) on resume with `approvalId`: `runtime.claim(...)` in place of the current manual status/hash/actor/expiry checks; 4) `runtime.begin(grant, attemptIndex)` immediately before `admitAndInvokeProvider`; 5) `admitAndInvokeProvider` (unchanged, exactly once per attempt, including retry); 6) `runtime.terminal(...)` immediately after the provider outcome resolves, mapping to `SUCCEEDED`/`FAILED`/`DENIED`; 7) on any crash between step 4 and step 6 being observed on a later request, `resolveAmbiguousExecutingCrash` reports `UNKNOWN_TERMINAL` rather than silently allowing a second `begin` (the single-use `ResumeAuthorityGrant` cannot be replayed; a fresh claim on the same `pendingExecutionId` would fail with `ALREADY_CLAIMED_OR_TERMINAL` unless the record is still `CLAIMED`, in which case only an explicit `resolveAmbiguousExecutingCrash`/`abandonBeforeStart` call, not a bare retry, can move it forward) |
| Duplicate-boundary risk | NONE for guard/admission/provider (confirmed above: neither boundary is touched or duplicated); LOW-but-present for durable-approval-fact ownership if `create`/`claim` inputs are ever allowed to diverge from `ApprovalStore`'s own record without the hash-binding check being enforced on every call site, which is why Question 8's answer requires the drift checks to run on every claim, not only at creation |
| Open interface decision (why this is not fully ready) | No current source names: (a) who owns the SQLite `dbPath` for a route-composed runtime  -  every existing caller (the local harness) requires an explicit caller-supplied path and an explicit `close()` call per invocation, whereas `ApprovalStore` is a resolved-path, process-lifetime singleton constructed once at module load; a naive per-request `buildPendingAgentExecutionRuntime(dbPath)` call inside a Next.js route handler without a matching per-request `close()` (or a singleton-construction pattern that does not yet exist for this store) would leak `better-sqlite3` file handles under load; (b) which exact request/response lifecycle point calls `close()` on every code path, including thrown-error paths, so the connection is never leaked; (c) whether a module-level singleton (mirroring `ApprovalStore`'s own pattern) is safe given `PendingAgentExecutionSqliteStore`'s `IMMEDIATE`-transaction CAS is explicitly scoped to `single_node_multi_process_local_file`, not `single_process`, so a singleton is plausible but is not yet a source-backed decision |
| Value beyond current route | Real and specific: reuses an already-implemented, already-independently-accepted (T1A-T1C), transaction-level CAS and explicit ambiguous-crash-state machine instead of designing one from scratch (Candidate 1) or accepting the current route's non-atomic status-check-then-delete pattern (status quo) |
| Smallest future manifest | Deferred to a ready terminal; not authorized in this tranche because the storage-path/lifetime/connection-closure decision (open interface decision above) is not yet resolved by current source |

### Candidate 3: minimal consume-before-work operation without a durable execution lifecycle

| Field | Value |
| --- | --- |
| Classification | `EXISTING_SOURCE_INCOMPATIBLE` |
| Creation owner | None new; reuses `ApprovalStore` |
| Claim owner | Proposed: move the existing `getApprovalStore().delete(approvedRequestRecord.id)` call (currently at line 513, after the `APPROVAL_CONSUMED` audit and immediately before falling through to the guard/provider pipeline) earlier, to immediately after the `status !== 'approved'` check (currently at line 255), so the record is deleted before any further processing rather than after |
| Begin/provider-attempt owner | Unchanged: `admitAndInvokeProvider`, unaffected |
| Terminal owner | None; this candidate explicitly does not add a durable execution lifecycle |
| Retry/recovery owner (answers Question 3 for this candidate) | If the process fails after the earlier delete but before or during the provider call, the approval record is already gone. There is no durable record of "an execution was in flight for this now-deleted approval" anywhere. The user would see a generic execution failure with no path back to resume, because the approval that authorized the retry no longer exists and nothing records that the delete-then-fail happened. This is a real regression versus the current route's behavior, which (despite its narrow TOCTOU window) at least keeps the record until immediately before the pipeline runs, and versus Candidate 2, which has an explicit `UNKNOWN_TERMINAL`/`ABANDON_BEFORE_START` recovery path. |
| Crash ambiguity (answers Question 4 for this candidate) | Silent data loss: a crash after the earlier delete produces no distinguishable state between "execution succeeded", "execution failed", and "execution never started." This is the exact silent-replay/silent-loss risk the work order's Question 4 asks every candidate to name explicitly. |
| Duplicate-boundary risk | NONE new (no new boundary is introduced) but this is not a safety improvement; moving the delete earlier narrows the window in which *two concurrent requests* could both pass validation, but widens the window in which *a single request's own crash* loses all resumability |
| Value beyond current route | Narrows one specific race (concurrent double-claim) while introducing a different and arguably worse failure mode (crash-induced permanent loss of resumability). Net value is negative relative to the current route's already-audited, already-consumed-with-audit-trail pattern. |
| Smallest future manifest | Not proposed; rejected because it trades a narrow concurrency risk for an unbounded crash-loss risk without any compensating durable record |

### Candidate 4: retain formal T1 parked because no safe bounded owner can be selected

| Field | Value |
| --- | --- |
| Classification | `RETAIN_PARKED_WITH_REASON` |
| Reason | Not selected as the terminal outcome for this tranche, because Candidate 2 is a source-compatible, safety-improving design and is not rejected outright; it has exactly one remaining open interface decision (storage-path/lifetime ownership), which is a narrower and more specific gap than "no safe owner exists at all." Recorded for completeness of the mandatory four-way comparison. |

## Twelve Mandatory Decision Questions

**1. What atomicity does `ApprovalStore` provide today, and what does atomic file replacement not guarantee across concurrent callers or processes?**
`ApprovalStore.persist()` writes the entire in-memory `Map` to a temp file and atomically renames it over the target path (`store.ts` lines 85-98), which guarantees that any single `persist()` call either fully succeeds or is not observed at all (no partial/torn file). It does not guarantee anything about the *decision* to write: `get`/`set`/`delete` operate on the in-process `Map` with no locking, and multiple in-flight requests reading `approvalStore.get(id)`, deciding independently, and each calling `set`/`delete` can race with no serialization between the read and the write, because nothing sits between the status check and the mutation to prevent a second caller from making the same read-then-decide sequence before the first caller's write lands. Atomic file replacement protects the on-disk file's integrity; it does not provide compare-and-swap, mutual exclusion, or any transactional isolation between concurrent callers' read-decide-write sequences.

**2. What exact race exists from approval validation to deletion and provider admission?**
In `/api/execute`, the `status !== 'approved'` check happens at line 255; the `getApprovalStore().delete(approvedRequestRecord.id)` call happens at line 513, after an intervening `appendAuditEvent` call and the fall-through into the guard-evaluation and enforcement-decision logic. Between these two points, two concurrent requests carrying the same `approvalId` and passing all the same-body/hash/actor checks could both read `status === 'approved'` as true before either has called `delete`. Both would then proceed into the shared guard/provider pipeline, each generating its own audit event and its own provider-attempt admission for what is logically one approved authorization, meaning the single approval could authorize two live provider calls rather than the intended one.

**3. If approval is consumed before later validation/configuration/admission, how is a pre-provider failure retried or rolled back safely?**
In the current route (Candidate status quo / Candidate 3's earlier-delete variant), it is not: once the record is deleted, there is no durable trace to retry against, and the user must resubmit and get a fresh admin approval. In Candidate 2, the pending core's `claimPendingExecution` never deletes the approval record at all  -  the pending-execution record transitions `CREATED -> CLAIMED` via CAS (`pending-agent-execution.ts` lines 909-921), consuming a single-use `ResumeAuthorityGrant` (line 923). If `beginPendingExecution` fails its own CAS (for example another process already began this claim) or if a failure occurs before `admitAndInvokeProvider` is ever called, `abandonBeforeStart` (lines 987-990) provides an explicit, CAS-guarded `CLAIMED -> ABANDONED_BEFORE_START` transition that leaves a durable, auditable record distinct from "succeeded" or "failed after a real attempt," and the underlying `ApprovalStore` record is never deleted by this path, so a caller could still re-attempt the original approval flow with a fresh claim on a fresh pending-execution record if the product later chooses to support that.

**4. If a provider call starts but the process crashes before response/terminal persistence, which state prevents silent replay?**
In Candidate 2, the record sits in `EXECUTING` status (set by `beginPendingExecution`'s CAS, `CLAIMED -> EXECUTING`) until a `TERMINAL` transition (`SUCCEEDED`/`FAILED`/`DENIED`/`UNKNOWN_TERMINAL`) is applied via `applyTerminalTransition`, which itself requires `expectedStatus: 'EXECUTING'` (line 984). If the process crashes after `beginPendingExecution` succeeds but before a terminal transition is ever applied, the record remains durably `EXECUTING` in SQLite (WAL journal mode, `synchronous = FULL`, confirmed at `pending-agent-execution-sqlite-store.ts` lines 469-470) across a process restart. A later reader observing this state cannot silently retry, because `TERMINAL_STATES` (referenced by `applyPendingAgentExecutionTransition`, line 607) does not include `EXECUTING`, and the only legal transitions out of `EXECUTING` are terminal ones; `resolveAmbiguousExecutingCrash` (lines 992-994) exists specifically to move such a record to `UNKNOWN_TERMINAL` under explicit operator/recovery-path control, never automatically. In the current route (status quo) and in Candidate 3, no equivalent durable "an attempt was in flight" marker exists at all; a crash during the live provider call leaves nothing to distinguish "maybe it succeeded" from "definitely never happened," which is a real silent-replay risk today, independent of this tranche's outcome.

**5. What creation point and identifier bind an approval record to a pending execution without drift or two uncoordinated truths?**
The pending core's payload already carries `approvalId`, `approvalRequestHash`, and `approvalRequestSnapshot` (referenced throughout `pending-agent-execution.ts`, e.g. lines 665-671, 836-885), and `computeApprovalRequestHash` is the same function `/api/execute` already uses to bind the approval record to its originating request body (`approval-binding.ts`, cited in T1J-R1). In Candidate 2, the pending-execution record would be created at the same instant `/api/execute` creates the approval record (both inside the `NEEDS_APPROVAL` branch), using the same `approvalId` as the join key and the same hash as the drift check. `evaluateDriftChecks` (lines 846-885) independently re-verifies this binding on every `claim()` call (id match, hash match against both the stored snapshot and the current live snapshot, actor match, expiry, and policy-fingerprint match), so drift between the two records is actively detected and denied, not merely assumed absent.

**6. Can the existing approval store be extended with enough lifecycle state without rebuilding the pending core? Name exact states and CAS boundary.**
Technically yes, but not without substantially reimplementing what already exists. `ApprovalStore` would need at minimum: a `CAS`-capable mutation primitive (a critical section around read-decide-write, which its current `Map`-subclass `get`/`set`/`delete` overrides do not provide, see Question 1); new terminal states distinguishing "claimed-but-not-yet-attempted," "attempt-in-flight," and "attempt-resolved" (roughly mirroring `CLAIMED`/`EXECUTING`/terminal in the pending core's own `PendingAgentExecutionStatus` enum, `pending-agent-execution-sqlite-store.ts` lines 110-121); and an explicit ambiguous-crash-resolution transition (mirroring `resolveAmbiguousExecutingCrash`). This is Candidate 1, and it is classified `NO_CURRENT_OWNER` precisely because building it from scratch duplicates design, review, and test surface that the pending core already has and that has already been independently accepted (T1A-T1C), for no source-evidenced benefit over reusing that existing, proven CAS boundary.

**7. Can the pending runtime be composed inside `/api/execute` without a second guard, provider admission or route? Name exact call order.**
Yes; the exact call order is recorded in full under Candidate 2's "Exact call order (answers Question 7)" row above. In summary: guard runs exactly once (unchanged); the pending runtime's `create`/`claim`/`begin`/`terminal` calls wrap around the route's existing single `admitAndInvokeProvider` call rather than replacing or duplicating it; no second route and no second guard/provider boundary is introduced at any point in the flow.

**8. Does pending composition duplicate durable approval facts, or can immutable approval binding and mutable execution lifecycle have distinct owners?**
They can have distinct owners, and current source is already structured this way even outside this decision: `ApprovalStore` owns the immutable fact "an admin approved (or rejected) this specific request, by this actor, at this time" and never changes that fact once decided (the `PATCH` handler at `[id]/route.ts` only transitions `pending -> approved/rejected` once, guarded by `record.status !== 'pending'` returning 409). `PendingAgentExecutionSqliteStore` would own the separate, mutable fact "this specific resume attempt, bound to that approval by hash, reached this lifecycle state." Neither store's write path needs to write the other store's fields; the join is read-only (the pending core reads `ApprovalRequestRecord` via `ApprovalRecordLookup` purely to validate drift, never to mutate it). This is not duplication of the same fact in two places; it is two distinct facts with two distinct, non-overlapping owners.

**9. Where do `APPROVAL_CONSUMED`, begin, provider-attempt and terminal evidence occur, and what ordering is safe?**
In the current route, `APPROVAL_CONSUMED` audit fires at line 500, before the delete at line 513, before the guard/provider pipeline runs at all. In Candidate 2, the safe ordering is: (1) `claim()` succeeds (CAS-guarded, this is the true single-winner point, replacing the current unguarded status check); (2) `APPROVAL_CONSUMED` audit fires, now safely describing a fact that has already been atomically won rather than merely observed; (3) `begin()` succeeds (CAS-guarded, consumes the single-use grant); (4) `admitAndInvokeProvider` runs (unchanged, exactly once per attempt); (5) `terminal()` records the outcome. Moving the audit event to occur only after the CAS-guarded claim succeeds (rather than the current route's position, which occurs after a plain boolean check) removes the possibility of auditing "consumed" for a request that was not actually the sole winner of the resume race.

**10. Who owns SQLite path/configuration, runtime lifetime, connection closure, stale/expired cleanup and single-node process safety?**
This is the exact open interface decision that keeps this tranche from a fully-ready terminal. No current source names a default, environment-variable-resolved, or singleton-constructed path for `PendingAgentExecutionSqliteStore` the way `ApprovalStore.ts` names `APPROVAL_STORE_PATH`/`process.cwd()/.data/...` (store.ts line 129). The only existing caller (`pending-agent-execution-local-harness.ts`) requires the caller to supply `dbPath` explicitly and to call `runtime.close()` itself in a `finally` block (lines 122-133), a pattern designed for a bounded, single-invocation harness call, not for a stateless-per-HTTP-request Next.js route handler. Composing this into `/api/execute` without deciding whether to (a) open and close a connection per request (correctness-safe but has per-request filesystem/SQLite-open overhead and must close on every code path including thrown errors) or (b) construct a module-level singleton mirroring `ApprovalStore`'s pattern (matches the store's own `deploymentBoundary = 'single_node_multi_process_local_file'` claim, but is not yet a source-backed decision anywhere) would leave connection lifetime, stale-record cleanup (there is no current caller of `expirePendingExecution` from any route), and single-node process safety unresolved.

**11. What is the smallest exact future source/test manifest for each viable owner, including concurrency and crash-window negative tests?**
Deferred: this tranche selects `PARTIAL_READY_REQUIRES_FAILURE_RECOVERY_INTERFACE_DECISION`, not a ready terminal, so per the work order's Acceptance Criteria a smallest future implementation manifest is named only for a selected *ready* terminal. The single interface decision that must be resolved first (Question 10) is recorded precisely enough that a future T1K packet can consume it directly: decide connection-lifetime/singleton-vs-per-request ownership for `PendingAgentExecutionSqliteStore` when composed inside a Next.js route handler, and decide the storage-path resolution convention (env var, fixed relative path under `.data/`, or otherwise) before any implementation manifest can be written for Candidate 2.

**12. Which terminal is supported, and why is every alternative defeated?**
`PARTIAL_READY_REQUIRES_FAILURE_RECOVERY_INTERFACE_DECISION` is supported. `EXISTING_APPROVAL_STORE_ATOMIC_LIFECYCLE_OWNER_READY_FOR_T1K_DECISION` is defeated because Candidate 1 requires building a new CAS/terminal-state machine from scratch inside `ApprovalStore`, duplicating already-accepted, already-proven machinery in the pending core, and no current source names this as a smaller or safer path. `PENDING_RUNTIME_NARROW_IN_ROUTE_LIFECYCLE_OWNER_READY_FOR_T1K_DECISION` is defeated, narrowly: Candidate 2's guard/provider/duplication analysis is fully resolved and safe (Questions 2, 4, 5, 7, 8, 9 all have concrete, source-backed answers), but the storage-path/connection-lifetime ownership decision (Question 10) has no current source answer at all, which the work order's own Decision/Baseline section states explicitly disqualifies "ready" status: "An owner is not ready merely because it has atomic CAS; it must also define what happens when execution fails before provider admission... or must be retried without replaying effects"  -  the CAS/crash-recovery semantics are fully defined, but the connection-lifetime mechanics that make it safe to actually construct the store inside a route handler are not. `MINIMAL_ATOMIC_CONSUME_OWNER_READY_FOR_T1K_DECISION` is defeated because Candidate 3 trades a narrowed concurrency race for an unbounded crash-loss race, a net-negative trade with no compensating durable record. `NO_SAFE_DURABLE_OWNER_RETAIN_FORMAL_T1_PARKED` is defeated because a viable, nearly-ready candidate exists (Candidate 2); the gap is one specific, nameable interface decision, not an absence of any safe design. `BLOCKED_SOURCE_CONTRADICTION` is defeated because no binding packet fact was contradicted; this tranche's fresh re-verification confirms T1J-R2's baseline evidence rows without any drift.

## Crash-Window And Duplicate-Boundary Proof Table

| Failure window | Current route (status quo) | Candidate 2 (pending runtime composed in-route) |
| --- | --- | --- |
| Two concurrent resume requests, same `approvalId` | Both may pass the plain status check before either deletes; both may enter the guard/provider pipeline | Only one wins the CAS `CREATED -> CLAIMED` transition; the other receives `CAS_CONFLICT` and never reaches `begin()` or the provider call |
| Crash after claim/consume, before provider call starts | No durable marker distinguishes this from any other failure; approval is already deleted (status quo) or about to be (Candidate 3) | Record is durably `CLAIMED`; `abandonBeforeStart` provides an explicit, audited recovery transition distinct from a real attempt |
| Crash during a live provider call, before terminal persistence | No durable marker; silent-replay risk is real and unaddressed by any current candidate other than Candidate 2 | Record is durably `EXECUTING` across restart (WAL + `synchronous = FULL`); only `resolveAmbiguousExecutingCrash` (explicit, not automatic) can move it to `UNKNOWN_TERMINAL` |
| Guard evaluation duplicated | No risk (single pipeline) | No risk: pending runtime never calls a guard engine |
| Provider-attempt admission duplicated | No risk today (single pipeline); would become a risk only if a second pipeline were composed, which Candidate 2 explicitly avoids | No intrinsic duplicate in the pending runtime, but the route integration order remains undecided; the existing `admitAndInvokeProvider` boundary must remain the sole provider-attempt owner |

## Independent Reviewer Correction

Reviewer disposition: `ACCEPT_WITH_MATERIAL_CORRECTION`.

The selected terminal remains
`PARTIAL_READY_REQUIRES_FAILURE_RECOVERY_INTERFACE_DECISION`, and
`successorTrancheOpened: NO` remains correct. The worker's narrower claim that only SQLite path and connection
lifetime remain open is not accepted. Fresh source-order verification establishes the following additional members
of one consolidated integration-interface decision cluster:

1. Current `/api/execute` ordering is not the order asserted in Candidate 2. Approval validation occurs near the
   start of the handler; the `NEEDS_APPROVAL` branch creates the approval and returns `409` before the later
   `runExecuteRouteMandatoryGateway` call. Therefore a pending record cannot be created at the current approval
   creation point with a gateway-derived `originalGuardResult` unless the route order changes or another explicitly
   governed source for that field is selected.
2. `PendingAgentExecutionImmutablePayload` requires `originalGuardResult`, `environment`, and a distinct
   `GuardPolicySnapshot` in addition to approval identity/hash/snapshot data. No current non-test route-native adapter
   builds this complete payload or converts the route's current policy surfaces into that contract. Consequently,
   `runtime.create(...)` and `runtime.claim(...)` cannot yet simply replace the manual route checks as stated.
3. SQLite `dbPath`, construction lifetime, `close()` ownership, and stale-record cleanup remain genuinely unresolved,
   as the worker correctly found.
4. The source defines `abandonBeforeStart` and `resolveAmbiguousExecutingCrash`, but it does not assign the route or
   another production owner authority to invoke them after restart. A crash after `claim()` loses the in-memory
   `ResumeAuthorityGrant` while leaving durable `CLAIMED` state; a crash after `begin()` leaves `EXECUTING` state.
   Recovery is explicit and safe against silent replay, but its production invocation and authorization interface
   remain undecided.

These are not four successor tranches. They are one bounded T1J-R3 integration-interface decision that must select
the route ordering, payload/snapshot adapter owner, SQLite lifecycle owner, and recovery invocation owner together.
Candidate 2 remains the preferred direction because its CAS and lifecycle primitives are real and it introduces no
guard or provider call of its own. It is not yet ready for T1K implementation, because source-compatible composition
of those primitives into the current route has not been fully specified.

This correction supersedes conflicting statements in Candidate 2, Questions 5, 7, 10, 11, and 12, the risk section,
the Decision Basis, and the Epistemic Claim Update that describe Questions 2 through 9 as fully resolved, give the
proposed call order as already safe, or characterize connection lifetime as the only remaining gap. The worker's
candidate comparison and CAS/crash-window evidence remain accepted only within this corrected boundary.

## Risk / Corrective Action

1. **Risk of treating CAS existence as sufficient readiness.**
   A future reviewer could read Candidate 2's strong crash-recovery semantics and conclude it is fully ready.
   - *Mitigation:* This assessment explicitly separates the CAS/crash-recovery analysis (fully resolved, Questions
     2-9) from the connection-lifetime/storage-path analysis (unresolved, Question 10), and selects the terminal
     that reflects exactly that split rather than rounding up to full readiness.
2. **Risk of under-crediting Candidate 3's apparent simplicity.**
   Moving one line (the delete) earlier looks like the smallest possible fix.
   - *Mitigation:* This assessment names the specific silent-data-loss failure mode that earlier deletion introduces
     and shows it is a net-negative trade, not a smaller-is-safer simplification.
3. **Risk of a future implementer choosing a per-request `open`/`close` pattern without recognizing the overhead or
   choosing a singleton without recognizing it is not yet source-backed.**
   - *Mitigation:* Question 10 and the smallest-future-manifest note name both options explicitly so a future T1K
     packet inherits the exact decision surface rather than re-discovering it.

## Decision / Recommendation / Disposition

**Selected Terminal Token:** `PARTIAL_READY_REQUIRES_FAILURE_RECOVERY_INTERFACE_DECISION`

**successorTrancheOpened:** NO

**Basis:**
1. Candidate 2 (narrow in-route composition of the existing, already-accepted pending runtime) is structurally safe:
   it introduces no second guard or provider-admission boundary, its CAS-based claim closes the real TOCTOU race
   identified by T1J-R1, and its explicit `EXECUTING`/`UNKNOWN_TERMINAL`/`ABANDON_BEFORE_START` states answer the
   crash-window questions this work order specifically requires (Questions 3 and 4) with durable, source-backed
   evidence rather than assumption.
2. Candidates 1 and 3 are both defeated on their own terms: Candidate 1 duplicates already-accepted machinery for no
   evidenced benefit; Candidate 3 trades a narrowed race for an unbounded crash-loss risk.
3. One concrete, nameable interface decision remains unresolved by current source: who owns the SQLite connection's
   lifetime, storage-path resolution, and closure across a stateless-per-request route handler. This is not a design
   flaw in Candidate 2's safety properties; it is a missing configuration/lifecycle-ownership decision that current
   source simply does not make anywhere yet.
4. Per the work order's own standard ("An owner is not ready merely because it has atomic CAS"), this gap is
   sufficient to withhold a fully-ready terminal while still recording that the CAS/crash-recovery design itself is
   sound and does not need to be redesigned.
5. No implementation, migration, or route/store wiring is authorized by this terminal. A later T1K packet may resolve
   the connection-lifetime/storage-path decision and then propose an exact implementation manifest; that packet is
   not opened by this tranche.

## Evidence / Verification

- Pre-implementation autorun gate: PASS, before authoring (execution base `1f20225422166dc5161bfd3db50d3ae6788b27df`).
- Fresh execution base and clean initial status: PASS.
- Both output paths confirmed absent before authoring.
- All named source files in the work order's Source Verification Block read in full; `execute/route.ts` approval
  block line numbers re-verified with zero drift from T1J-R1's citations.
- Provider, network, browser, credential, and live calls: 0.
- Runtime, source, test, package, and checker mutations: 0.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | assessment docType; terminal token enum; successorTrancheOpened token; Source Verification ACCEPT disposition; AOT trace label set; terminal contract tokens |
| gateRunPurpose | post-read confirmation that literal shape is correct; gates confirm rather than reveal required tokens |
| claimBoundary | structural gate success does not substitute for reviewer semantic audit; external worker output is not CVF authority until independently accepted |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated operator-mediated external decision worker; provider identity not independently attested |
| Provider or surface | local private provenance workspace; no provider/API/network/browser call |
| Session or invocation | GC010-SCR-R2-T1J-R2 external worker, 2026-08-31 |
| Working directory | repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | governed reads; `git rev-parse HEAD`; `git status --short --untracked-files=all`; `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`; `rg` searches; `python governance/compat/run_worker_return_fast_gate.py` |
| Target paths | T1J-R1 assessment; `store.ts`; `execute/route.ts`; `pending-agent-execution.ts`; `pending-agent-execution-sqlite-store.ts`; `pending-agent-execution-composition.ts`; `pending-agent-execution-local-harness.ts` |
| Allowed scope source | committed T1J-R2 baseline/work order and active next-move authority at execution base `1f20225422166dc5161bfd3db50d3ae6788b27df` |
| Before status evidence | clean worktree at full HEAD `1f20225422166dc5161bfd3db50d3ae6788b27df`; both output paths absent |
| After status evidence | HEAD unchanged; both new documentation paths untracked and uncommitted |
| Diff evidence | `git diff --name-status` returns empty; `git status --short --untracked-files=all` shows exactly two new untracked documentation paths |
| Approval boundary | read-only source inspection and offline deterministic search only; no source/test edit, no provider/live/network call |
| Claim boundary | no source/test/package/script/session edit, route/store implementation, production, distributed, live, public, deploy or commit claim |
| Agent type | EXTERNAL_AGENT_CLI_MCP operator-mediated worker |
| Invocation ID | `gc010-scr-r2-t1j-r2-worker-2026-08-31` |
| Expected manifest | `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` |
| Actual changed set | `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | approval-resume atomic-claim durable-owner decision; read-only offline analysis |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: four candidates compared; twelve questions answered; crash-window and duplicate-boundary proof table recorded |
| receiptEvidence | CVF_RECEIPT_PRESENT: pre-implementation PASS; clean git status |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact two-path uncommitted documentation manifest; deterministic search outputs |
| invocationBoundary | read-only local source inspection and offline checks; one operator-mediated external worker invocation; zero provider/network/browser/credential/live calls |
| interceptionBoundary | no external interception, wrapper/proxy enforcement, runtime gate, or agent coding control was created |
| claimLanguage | T1J-R2 selects a durable-owner candidate or names the exact remaining interface decision; it does not implement, migrate, or wire any store or route |
| forbiddenExpansion | source/test/package/script/session edits; route/store implementation; provider/live; public sync; distributed; deployment; production; continuity update; commit; T1K/T2 successor dispatch |

## Epistemic Process Block

### Expected Result / Prediction

The work order predicted that a durable owner should not be judged ready merely because it has atomic CAS; it must
also define pre-provider failure recovery, post-provider-call crash ambiguity, and storage/lifecycle ownership. It
warned specifically against assuming early deletion is safe or that the pending runtime necessarily requires a
second route.

### Evidence Comparison

Candidate 2's CAS and crash-recovery semantics were traced and found fully defined and source-backed (`CLAIMED`,
`EXECUTING`, `UNKNOWN_TERMINAL`, `ABANDONED_BEFORE_START` all have explicit, tested transition functions). Its
storage-path and connection-lifetime ownership was traced and found genuinely absent from current source. Candidate
3 (early deletion) was traced and found unsafe, matching the work order's explicit warning. No new route was
required for Candidate 2's guard/provider preservation, also matching the work order's framing.

### Contradiction Or Gap Disposition

No contradiction was found with T1J-R1's findings; this tranche extends rather than revises them. The gap this
tranche identifies (storage-path/connection-lifetime ownership) is a new, more specific finding than T1J-R1's general
"durable owner decision required" framing, narrowing the open question to one concrete configuration/lifecycle
decision rather than a broad design question.

### Claim Update

Narrowed. The atomic-claim design question is resolved: Candidate 2 is safe and source-compatible for guard/provider
preservation and crash-recovery semantics. The remaining open question is narrowly scoped to connection-lifetime and
storage-path ownership, not to the safety of the CAS/lifecycle design itself. No implementation is authorized. T2
remains held.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision-only reconciliation; no public artifact or export authority is included.

## Finding-To-Governance Learning Disposition

NOT_APPLICABLE_WITH_REASON: this tranche reconciles existing accepted T1J-R1 evidence and current source. No
recurring defect class was identified in this decision tranche.

## Claim Boundary

This assessment compares four durable-owner candidates for approval-resume atomic claim and recovery, answers twelve
mandatory questions, and selects one allowed terminal token. It does not close or edit the roadmap, implement or
migrate any store, wire any route, invoke a provider, emit production audit, prove distributed safety, sync public
artifacts, deploy, open production, commit, or authorize an automatic T1K or T2 successor tranche.
