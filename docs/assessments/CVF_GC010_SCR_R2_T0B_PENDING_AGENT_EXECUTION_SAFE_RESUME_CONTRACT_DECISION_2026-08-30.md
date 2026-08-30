# CVF GC010 SCR-R2-T0B Pending Agent Execution Safe Resume Contract Decision

Memory class: governed-decision-assessment

docType: baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: GC010-SCR-R2-T0B

Date: 2026-08-30

Worker: delegated no-commit decision worker

## Purpose

Freeze one exact, source-compatible schema, digest recipe, lifecycle state
machine, atomic claim operation, and internal resume-grant contract for a
durable "pending Agent Execution" record that sits between an approved human
decision and one future admitted provider attempt, or state precisely why no
such contract can be adopted yet. This assessment answers the eighteen
required decision questions from
`docs/baselines/CVF_GC018_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`
in order and selects exactly one terminal token. This tranche implements
nothing.

## Source / Predecessor Evidence

- Paired baseline: `docs/baselines/CVF_GC018_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`.
- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`.
- T0A assessment (accepted architecture direction only):
  `docs/assessments/CVF_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_2026-08-30.md`.
- T0A completion (`CLOSED_PASS_BOUNDED`, terminal `PARTIAL_READY_REQUIRES_APPROVAL_ADAPTER`):
  `docs/reviews/CVF_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_COMPLETION_2026-08-30.md`.
- T0A material commit `8119e3e51`; continuity sync `276fc4344`; T0B dispatch
  packet committed at `6017beaf2` and `3fcb0d418`.
- executionBaseHead: `3fcb0d418` (captured fresh at worker start; `git status --short --untracked-files=all` was clean).

## Scope / Methodology

Fresh direct reads of every named runtime/schema source at executionBaseHead,
plus the two exact `rg` searches over `EXTENSIONS/CVF_GUARD_CONTRACT` and
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` required by the work order's
"Current Runtime Freshness Verification" section. No provider, network,
browser, credential, or runtime mutation occurred. No file outside the two
worker-owned output paths was written.

## Current Runtime Freshness Verification

Commands run at executionBaseHead `3fcb0d418`:

```
git rev-parse --short HEAD
rg -n "ApprovalRequestRecord|computeApprovalRequestHash|buildApprovalActorBinding|AgentExecutionRuntime|admitAndInvokeProvider" EXTENSIONS/CVF_GUARD_CONTRACT EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src -g "*.ts"
rg -n "PendingAgentExecution|ResumeAuthorityGrant|claimPendingExecution|pending-agent-execution" EXTENSIONS/CVF_GUARD_CONTRACT EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src -g "*.ts"
```

Classification of every non-test hit from the first search (57 total hits,
including test files, all classified below):

| Hit class | Disposition |
| --- | --- |
| `AgentExecutionRuntime` class definition (`agent-execution-runtime.ts` line 148) and constructor call sites | ACCEPT: construction is used only inside test files (`agent-execution-runtime.test.ts`, `approval-execution-bridge.test.ts`, `gemini-provider.test.ts`, `alibaba-dashscope-provider.test.ts`); no non-test caller constructs `AgentExecutionRuntime` |
| `ExecutionProvider` docstring references in `gemini-provider.ts` and `alibaba-dashscope-provider.ts` | ACCEPT: comment-only reference ("Implements the `ExecutionProvider` interface from AgentExecutionRuntime"); neither file imports or wires `AgentExecutionRuntime` |
| `ApprovalRequestRecord` type usage across `approvals/store.ts`, `approvals/[id]/route.ts`, `approvals/route.ts`, `approvals/approval-binding.ts`, `execute/route.ts`, `execute/route-final-response.ts` | ACCEPT: confirms `ApprovalRequestRecord` remains the sole Web approval-decision schema; no pending-execution or claim field exists on it |
| `buildApprovalActorBinding`/`computeApprovalRequestHash` usage in `approval-binding.ts`, `approvals/route.ts`, `approvals/[id]/route.ts`, `execute/route.ts` | ACCEPT: confirms the actor/hash binding helpers are reused consistently but bind only the approval snapshot, not a full AER-authority binding |
| `admitAndInvokeProvider` used only in `execute/route.ts` (two call sites, lines 801 and 859) | ACCEPT: confirms `/api/execute` remains the sole caller; no agent-execution adapter exists yet |

Second search (`PendingAgentExecution\|ResumeAuthorityGrant\|claimPendingExecution\|pending-agent-execution`) returned **zero hits** across both extension roots (`rg` exit code 1 = no matches). No pending-execution record, resume grant, claim function, or route file exists anywhere in current source. This reconfirms T0A's finding (Q8/Q9 of the T0A assessment) and the work order's own Negative Search prediction; no newly discovered owner requires reclassification of this contract.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Approval record lacks complete pending execution and claim state | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalRequestRecord` (lines 37-61) | approval record | cvf-web | ACCEPT |
| File-backed persistence catches write failures, non-atomically, with no claim primitive | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `FileBackedApprovalStore.persist` (lines 85-98) | approval persistence | cvf-web | ACCEPT |
| Approval actor/request hash helpers exist but cover only the approval snapshot, not a full AER-authority digest | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | `buildApprovalActorBinding` (lines 45-69); `computeApprovalRequestHash` (lines 95-99) | approval binding | cvf-web | ACCEPT |
| Approval PATCH decides state and is not a provider execution endpoint; it never calls `execute()` or a provider | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | `PATCH` (lines 57-119) | decision handler | cvf-web | ACCEPT |
| AER execution receives a caller-provided guard result; `execute()` performs no admission check itself | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `execute(intent, guardResult)` (lines 233-346) | public execution method | Guard Contract | ACCEPT |
| Provider admission owner exists separately and is called only from `/api/execute` | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` | `admitAndInvokeProvider` (lines 352-379) | attempt admission | cvf-web | ACCEPT |
| Durable audit store is shared, retention-managed, and used by both the approval route and `/api/execute` | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | `appendAuditEvent` (lines 143-156) | durable audit owner | cvf-web | ACCEPT |
| No `PendingAgentExecution`/`ResumeAuthorityGrant`/`claimPendingExecution`/`pending-agent-execution` symbol exists anywhere in current source | runtime/schema | `EXTENSIONS/CVF_GUARD_CONTRACT/**`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/**` | fresh `rg` returned zero hits | absent schema/store/function | none | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Two planned output paths | absent at executionBaseHead `3fcb0d418` before authoring (confirmed by pre-flight `git status --short --untracked-files=all` showing clean tree) | ACCEPT |
| Proposed schema/claim/grant symbols (`PendingAgentExecution`, `ResumeAuthorityGrant`, `claimPendingExecution`) | fresh `rg` search returned zero hits across both extension roots; no existing owner collides with this decision | ACCEPT |
| Existing-chain collision | approval PATCH (`approvals/[id]/route.ts`) and `/api/execute` (`execute/route.ts`) remain untouched, read-only boundaries; no edit was made to either | ACCEPT |
| `ApprovalExecutionBridge` in-memory bridge | confirmed (per T0A Q8, reconfirmed here) process-memory-only via `private readonly pending = new Map()`; cannot survive the HTTP submit/decide request boundary and is excluded from this contract | ACCEPT |

## Candidate Comparison Contract

### Candidate 1: extend `ApprovalRequestRecord` into execution storage and authority

| Field | Value |
| --- | --- |
| Schema owner | `approvals/store.ts` `ApprovalRequestRecord` interface, extended in place |
| Immutable/mutable fields | Would require overloading the same interface with both approval-decision fields (`status`, `reviewedAt`, `reviewedBy`) and execution-claim fields (a hypothetical `executionClaimId`, `executionStatus`); no current field separation exists to keep these two authorities apart, so "immutable" cannot be enforced per-concern without a second schema |
| Persistence semantics | Same `FileBackedApprovalStore.persist()` (lines 85-98): non-atomic (`writeFileSync` to `.tmp` then `renameSync`), catches write failures only with a `console.warn`, never surfaces failure to the caller, and returns `void` |
| State machine | The existing `ApprovalStatus` union (`'pending' \| 'approved' \| 'rejected' \| 'expired'`) has no execution-claim states (no `CLAIMED`, `EXECUTING`, `CONSUMED`); adding them conflates decision lifecycle with execution lifecycle in one enum |
| Claim operation | None exists; `store.set(key, value)` (line 100) is a last-writer-wins `Map.set` with no compare-and-swap or precondition check, so two concurrent PATCH-like writes race with no atomic winner |
| Concurrency/restart behavior | `ApprovalStore extends Map`; two near-simultaneous `set()` calls each fully overwrite prior state in-process with no version check; `persist()` failure is swallowed, so a failed write leaves the in-memory map and the on-disk file silently diverged after restart |
| Approval binding | Reuses `buildApprovalActorBinding`/`computeApprovalRequestHash`, but these only ever validated an approval-decision snapshot, not a full AER binding (intent, session, cwd, environment, guard/policy fingerprint) |
| Fingerprint handling | None exists on `ApprovalRequestRecord`; would need new fields bolted onto the same object used for `GET`/`PATCH` responses, which already return `record` fields directly to callers (`route.ts` line 118, `{ success: true, data: updatedRecord }`), risking accidental exposure of internal claim state to approval API consumers |
| Grant construction/consumption | No separation between "approval decided" and "execution authorized"; `PATCH`'s `store.set(id, updatedRecord)` (line 101) would become the same code path that could, if extended carelessly, imply execution authority is the same act as approval decision - this directly violates Mandatory Invariant 1 ("Approval PATCH starts zero provider calls") if the extension is not carefully firewalled, and the boundary is easy to erode over time because it is the same object and the same store |
| Attempt/audit correlation | Reuses `appendAuditEvent`, but has no `attemptIndex`/`claimId` field to correlate a specific resume attempt to a specific provider call |
| Duplication risk | HIGH: mixing decision authority and execution-claim authority in one mutable record makes it structurally easy for a future edit to treat `status: 'approved'` as sufficient execution authority, exactly the authority-laundering risk the T0A completion review flagged |
| Future manifest | Would require: new claim-state fields on `ApprovalRequestRecord`; a new atomic claim helper operating on the approval store; careful re-auditing of every existing `GET`/`PATCH` response shape to avoid leaking claim internals; a rewritten `ApprovalStatus` union or a parallel claim-status field, either of which changes the approval store's existing accepted shape |
| Verdict | REJECTED: extending the existing approval-decision schema does not achieve invariant 4 (immutable except through named atomic transitions) or invariant 6 (claim yields at most one executable winner) without first splitting decision authority from execution-claim authority into two schemas - at which point this candidate degenerates into Candidate 2 with extra migration risk on the existing accepted `/api/approvals` contract |

### Candidate 2: keep approval decision separate and add a dedicated versioned pending-execution record/store plus atomic claim and internal resume grant

| Field | Value |
| --- | --- |
| Schema owner | a new, separate schema/store module (for example, a hypothetical `pending-agent-execution-store.ts`), never created by this tranche; `ApprovalRequestRecord` and `approvals/store.ts` remain completely unmodified |
| Immutable/mutable fields | Immutable at create time: `pendingExecutionId`, `schemaVersion`, `approvalId`, `requestId`, normalized intent/actor/session/cwd/environment/fileScope/buildAuthority fields, the original `guardDecision` snapshot, the `guardPolicyFingerprint`, and the canonical record digest. Mutable only through named transitions: `status`, `claimId`, `claimedAt`, `claimedBy`, `attemptIndex`, `consumedAt` |
| Persistence semantics | A new store must prove durable, fail-closed create (write success acknowledged only after a verified durable write, e.g. write-to-temp plus atomic rename plus a read-back or fsync confirmation, not `FileBackedApprovalStore`'s current swallow-on-failure pattern) |
| State machine | A dedicated lifecycle distinct from `ApprovalStatus`: `CREATED -> CLAIMED -> CONSUMED`, with `EXPIRED` and `STALE` as terminal non-executable states reachable from `CREATED` or `CLAIMED` |
| Claim operation | A new atomic claim/consume primitive (a compare-and-swap style transition, for example an atomic file rename or a single-writer in-process mutex plus a persisted claim marker) that admits at most one winner per `pendingExecutionId` |
| Concurrency/restart behavior | Must be specified so that two concurrent resume requests race on the same atomic primitive and exactly one observes success; a process restart must be able to reconcile an `CLAIMED`-but-never-`CONSUMED` record without a second provider call (see Q10) |
| Approval binding | Composes the existing `approvalRecordMatchesActor`/`computeApprovalRequestHash` checks (reused, not reinvented) plus new checks against the pending-execution record's own stored actor/session/cwd/environment fields |
| Fingerprint handling | A new `guardPolicyFingerprint` field captured at create time and revalidated bit-for-bit at claim time; any drift is stale (Mandatory Invariant 7) |
| Grant construction/consumption | A branded, opaque, single-use internal grant type returned only by the claim primitive on success; never constructible by a route handler or caller directly; consumed exactly once by the one future `ExecutionProvider` adapter that calls `admitAndInvokeProvider` |
| Attempt/audit correlation | New fields `pendingExecutionId`, `claimId`, `requestId`, `attemptIndex` correlate cleanly to the existing `ProviderAttemptLedger.attempts[].attemptIndex` (`provider-attempt-admission.ts` lines 56-63) and to `appendAuditEvent`'s free-form `payload` |
| Duplication risk | LOW BY DESIGN: because approval-decision authority (`ApprovalRequestRecord`) and execution-claim authority (the new record) are two separate schemas owned by two separate stores, a caller cannot conflate "approved" with "claimed", and the atomic claim primitive is the only path to a grant |
| Future manifest | (1) a versioned pending-execution schema/store file with fail-closed persistence; (2) an atomic claim/consume primitive; (3) a branded internal resume-grant type consumed only by a future `ExecutionProvider` adapter; (4) a resume route/helper that revalidates approval + fingerprint + binding before calling the claim primitive; (5) focused negative tests per Q17 |
| Verdict | SELECTED: this is the only candidate that satisfies all nine Mandatory Contract Invariants without eroding the existing accepted `/api/approvals` and `/api/execute` contracts. It is a contract decision, not an implementation - no file in this list is created by this tranche |

### Candidate 3: adopt no safe contract and retain parked

| Field | Value |
| --- | --- |
| Schema owner | not applicable; nothing is created |
| Immutable/mutable fields | not applicable |
| Persistence semantics | not applicable |
| State machine | not applicable |
| Claim operation | not applicable |
| Concurrency/restart behavior | not applicable |
| Approval binding | not applicable |
| Fingerprint handling | not applicable |
| Grant construction/consumption | not applicable |
| Attempt/audit correlation | not applicable |
| Duplication risk | NONE; nothing is built |
| Future manifest | none; the T0A-established four-gap manifest (AER export/factory, pending-execution binding/store, safe resume authority, atomic claim, response mapping, audit wiring) remains the controlling reopen gate |
| Verdict | NOT SELECTED: Candidate 2's schema, state machine, claim, and grant boundary are exactly nameable from current source (this assessment names every field, state, and transition below), so full parking is not required. Candidate 3 remains the correct fallback only if Candidate 2's contract could not be stated coherently, which is not the case here |

## Eighteen Required Decision Questions

**1. What is the schema name and `schemaVersion`?**
Schema name: `PendingAgentExecutionRecord`. `schemaVersion`: `"cvf.pendingAgentExecution.v1"` (string literal, matching the existing convention on `ProviderAttemptLedger.schemaVersion: 'cvf.providerAttemptLedger.v1'` in `provider-attempt-admission.ts` line 66 and `ProviderAttemptReconciliation.schemaVersion: 'cvf.providerAttemptReconciliation.v1'` line 178).

**2. Which normalized intent, actor, session, cwd, environment, file-scope, build-authority, guard decision, fingerprint, approval, attempt and audit fields are mandatory?**
Mandatory fields on `PendingAgentExecutionRecord`:
- `pendingExecutionId: string` (server-generated, unique per record)
- `schemaVersion: 'cvf.pendingAgentExecution.v1'`
- `approvalId: string` (foreign key into `ApprovalRequestRecord.id`)
- `requestId: string` (AER's `GuardRequestContext.requestId`, matching the format at `agent-execution-runtime.ts` line 211, `exec-${Date.now()}-...`)
- `normalizedIntent: { action: string; targetFiles?: string[]; parameters?: Record<string, unknown> }` (from `ParsedIntent`, excluding `confidence` since confidence is not authority-bearing)
- `actorBinding: ApprovalActorBinding` (reused type from `approval-binding.ts` lines 8-13: `actorId`, `actorOrgId`, `actorTeamId`, `actorAuthMode`)
- `sessionId: string` (maps to `RuntimeConfig.sessionId`)
- `cwd: string` (maps to `RuntimeConfig.cwd`)
- `environment: Record<string, string>` (maps to `RuntimeConfig.environment`, non-secret only)
- `fileScope: string[] | undefined` (maps to `RuntimeConfig.fileScope`)
- `buildAuthority: BuildAuthorityEvidence | undefined` (maps to `RuntimeConfig.buildAuthority`)
- `originalGuardDecision: GuardPipelineResult` (the exact `GuardPipelineResult` returned by `preCheck` at submit time, stored verbatim)
- `guardPolicyFingerprint: string` (a new sha256 digest of the guard engine's active rule/policy configuration at submit time; no current source computes this field, so it is a named future-manifest item, not an existing owner)
- `status: PendingAgentExecutionStatus` (see Q5)
- `claimId: string | null` (set only on successful claim)
- `claimedAt: string | null` (ISO 8601, set only on successful claim)
- `claimedBy: ApprovalActorBinding | null` (the actor who performed the resume/claim; may differ in identity checks from `actorBinding` only when policy explicitly allows delegated resume, which this contract does not permit - see Q11)
- `attemptIndex: number | null` (correlates to `ProviderAttemptLedger.attempts[].attemptIndex` once a provider call is admitted)
- `createdAt: string` (ISO 8601)
- `consumedAt: string | null`
- `recordDigest: string` (see Q3)

**3. What exact bytes/normalization form the canonical record digest?**
The canonical digest follows the existing pattern in `computeApprovalRequestHash` (`approval-binding.ts` lines 95-99: `createHash('sha256').update(JSON.stringify(snapshot)).digest('hex')`), extended to a union binding object. The digest input is a plain object containing exactly the immutable fields from Q2 in this fixed key order: `schemaVersion`, `approvalId`, `requestId`, `normalizedIntent` (with `parameters` deep-sorted by key, reusing the `sortStringRecord`-style sort pattern from `approval-binding.ts` lines 34-43, generalized to nested objects), `actorBinding` (all four sub-fields in their declared order), `sessionId`, `cwd`, `environment` (key-sorted), `fileScope` (array, order-preserved since file scope order can be authority-bearing), `buildAuthority`, `originalGuardDecision.finalDecision`, and `guardPolicyFingerprint`. The digest is `createHash('sha256').update(JSON.stringify(orderedObject)).digest('hex')`, stored as `recordDigest`. Mutable fields (`status`, `claimId`, `claimedAt`, `claimedBy`, `attemptIndex`, `consumedAt`) are never included in the digest input, because including a mutable field would make the "unchanged since create" comparison at claim time self-invalidating.

**4. Which fields are immutable and which transition metadata may change?**
Immutable after create (protected by `recordDigest`): `pendingExecutionId`, `schemaVersion`, `approvalId`, `requestId`, `normalizedIntent`, `actorBinding`, `sessionId`, `cwd`, `environment`, `fileScope`, `buildAuthority`, `originalGuardDecision`, `guardPolicyFingerprint`, `createdAt`, `recordDigest`. Mutable only through the named transitions in Q5: `status`, `claimId`, `claimedAt`, `claimedBy`, `attemptIndex`, `consumedAt`. Any write that would change an immutable field must be rejected by the store layer as a defensive-programming error, analogous to how `recordProviderCallStart` (`provider-attempt-admission.ts` lines 161-175) treats a double call as a no-op-plus-warning rather than silently succeeding.

**5. What are all lifecycle states and legal transitions?**
`PendingAgentExecutionStatus = 'CREATED' | 'CLAIMED' | 'CONSUMED' | 'EXPIRED' | 'STALE' | 'ABANDONED'`.

Legal transitions:
- `CREATED -> CLAIMED`: only via the atomic claim operation (Q8), only when the approval is `'approved'` and unexpired (per `approvals/store.ts` `ApprovalStatus`), the actor/hash/binding/fingerprint checks in Q11-Q12 all pass, and no other claim has already succeeded for this `pendingExecutionId`.
- `CLAIMED -> CONSUMED`: only by the single component named in Q15 (the future `ExecutionProvider` adapter), exactly once, immediately after `admitAndInvokeProvider` (or the admission-denied path) resolves for the attempt tied to `claimId`.
- `CREATED -> EXPIRED`: when the linked `ApprovalRequestRecord.expiresAt` has passed, mirroring the exact check `/api/execute` already performs (`route.ts` lines 240-253).
- `CREATED -> STALE` or `CLAIMED -> STALE`: when `recordDigest` recomputed from current binding does not match the stored `recordDigest`, or `guardPolicyFingerprint` recomputed from the current guard engine configuration does not match the stored value (Q13).
- `CLAIMED -> ABANDONED`: reconciliation-only transition (Q10) when a claim has been held past a defined abandonment window without reaching `CONSUMED`; this transition never re-opens the record to a fresh `CLAIMED` state for the same `claimId` and never permits a second provider call for the same `attemptIndex`.
- No transition ever returns a record from `CONSUMED`, `EXPIRED`, `STALE`, or `ABANDONED` back to `CREATED` or `CLAIMED`. All four are terminal-for-resume states; a genuinely new attempt requires a brand-new `pendingExecutionId` created from a fresh submit, not a resurrected old record.

**6. What persisted evidence proves create success before returning pending?**
Create is acknowledged to the caller only after: (a) the record is written to durable storage using a write-to-temp-then-atomic-rename sequence (the same `writeFileSync(tmpPath, ...)` + `renameSync(tmpPath, filePath)` pattern already used in `FileBackedApprovalStore.persist()`, `store.ts` lines 90-94, but unlike that function, failure must propagate to the caller rather than being swallowed by a `console.warn`), and (b) a read-back of the just-written record from the store confirms `recordDigest` matches the value computed before the write. Only after both (a) and (b) succeed does the create path return `status: 'CREATED'` with the generated `pendingExecutionId`. Any failure in (a) or (b) fails closed: the caller receives an explicit create-failure result, and no `pendingExecutionId` is returned as valid.

**7. How do write, fsync/replace, parse, corruption and restart failures fail closed?**
- Write failure (temp-file write throws): create fails closed; no record exists; caller receives an explicit error, unlike `FileBackedApprovalStore.persist()`'s current silent `console.warn` (`store.ts` line 96).
- Fsync/replace failure (`renameSync` throws or the read-back in Q6 does not match): treated identically to write failure; the record is never considered `CREATED`.
- Parse failure on load (mirroring `ApprovalStore.load()`'s `catch { super.clear(); }` at `store.ts` lines 74-82, which currently silently discards ALL records on any parse error): the pending-execution store must not adopt this blanket-clear behavior. A parse failure on the whole file must fail the store to a `LOAD_FAILED` state that blocks all claim operations until repaired, rather than silently resetting to empty (which would silently erase legitimate `CLAIMED` records and could not be distinguished from "no pending executions exist").
- Corruption of a single record (valid JSON file, but one record fails schema validation): that one record is marked `STALE` on load with a recorded reason; other valid records are unaffected.
- Restart: on process restart, every `CLAIMED` record's claim age is checked against the abandonment window (Q10) before any new claim attempt is admitted for that record.

**8. What is the atomic claim operation, precondition and success receipt?**
Atomic claim operation: `claimPendingExecution(pendingExecutionId, claimContext) -> ClaimResult`. Precondition (all must hold, checked inside one atomic critical section, not as separate sequential checks that could interleave with a concurrent claim): (a) record exists and `status === 'CREATED'`; (b) linked `ApprovalRequestRecord.status === 'approved'` and unexpired (Q11); (c) `approvalRecordMatchesActor`-equivalent check passes between `claimContext.actor` and the record's stored `actorBinding` (Q11); (d) recomputed `recordDigest` matches stored `recordDigest` (Q13); (e) recomputed `guardPolicyFingerprint` matches stored value (Q13). The atomic primitive itself is a single-writer compare-and-swap: the claim function must perform its precondition check and its `status` write inside one non-yielding critical section (analogous to `RateLimitStore.consume`'s synchronous read-increment-write pattern cited in `provider-attempt-admission.ts` lines 42-49) so that two concurrent callers cannot both observe `status === 'CREATED'` before either write lands. Success receipt: a branded, opaque `ResumeAuthorityGrant` object (Q14) containing `pendingExecutionId`, `claimId` (freshly generated), `attemptIndex: null` (populated later by the ledger), and the frozen `normalizedIntent`/binding fields needed to construct the provider call - nothing more.

**9. How do concurrent resume requests yield at most one winner?**
Because the claim precondition-check-and-write happens inside one atomic critical section (Q8), only the first caller to reach that section while `status === 'CREATED'` observes the precondition as true; every other concurrent caller either sees `status === 'CLAIMED'` (or later) and is rejected with a `ClaimResult.ok: false, reason: 'ALREADY_CLAIMED'`, or - if the underlying storage cannot guarantee true single-writer atomicity across process boundaries - the claim primitive must use a storage-level compare-and-swap (e.g., an atomic rename of a claim-marker file keyed by `pendingExecutionId`, where only one renamer can succeed) so that cross-process concurrency is resolved the same way. No claim implementation may rely on a check-then-write pattern with an await between the check and the write, because that reintroduces the race this invariant forbids.

**10. How are abandoned/expired claims reconciled without duplicate execution?**
A `CLAIMED` record that has not reached `CONSUMED` within a defined abandonment window (a fixed duration, e.g. matching the existing approval `expiresAt` horizon semantics) transitions to `ABANDONED` via a reconciliation pass (run at store load / restart, and optionally on a periodic sweep). `ABANDONED` is terminal for that `claimId`: it never re-admits a claim for the same `pendingExecutionId`, and it never triggers a provider call, because no component may call `admitAndInvokeProvider` from a reconciliation pass - reconciliation only updates state and audit records via `appendAuditEvent`. If a legitimately new attempt is needed after abandonment, the caller must submit a brand-new `PendingAgentExecutionRecord` through the normal create path (Q6), which produces a new `pendingExecutionId` and a new `recordDigest`, not a reopened old one. This guarantees that even if the original provider call from an abandoned claim was in an unknown state (in flight, succeeded silently, or failed), reconciliation itself never fires a second call for the same `claimId`.

**11. What validates approval actor, status, expiry and request hash?**
Reused directly, unmodified, from `approval-binding.ts` and `approvals/store.ts`: `approvalRecordMatchesActor` (lines 116-133) validates actor identity/org/team/auth-mode match; the approval record's own `status === 'approved'` field (checked the same way `/api/execute` checks it at `route.ts` line 255); the same expiry check `/api/execute` performs at `route.ts` lines 240-253 (`new Date(approvalRecord.expiresAt).getTime() <= Date.now()`); and `computeApprovalRequestHash` compared against `approvalRecord.requestHash`, exactly as `/api/execute` does at `route.ts` line 229. The pending-execution claim operation must re-run all four checks at claim time (not only at create time), because approval state can change (be revoked, expire, or be re-decided) between submit and resume.

**12. What validates complete AER binding and guard/policy fingerprint?**
The claim operation recomputes `recordDigest` (Q3) from the pending-execution record's own stored immutable fields and the claim-time restated intent/binding presented by the resume caller, and rejects the claim if they differ (this catches any drift in intent, actor, session, cwd, environment, file scope, or build authority). Separately, it recomputes `guardPolicyFingerprint` from the currently active guard engine configuration (the same `createGuardEngine()` factory from `src/index.ts` lines 394-408 that `GuardRuntimeEngine.evaluate` would use) and rejects the claim if it differs from the value stored at create time. These are two independent checks: binding drift and policy drift are different failure classes and must both be named explicitly rather than folded into one generic "hash mismatch."

**13. What exact stale disposition applies on drift?**
Any drift detected in Q11 or Q12 - changed actor, changed request hash, expired/non-approved approval status, changed `recordDigest`, or changed `guardPolicyFingerprint` - produces `status: 'STALE'` on the pending-execution record and a `ClaimResult.ok: false, reason: 'STALE_<DRIFT_CLASS>'` (for example `STALE_BINDING_CHANGED`, `STALE_POLICY_FINGERPRINT_CHANGED`, `STALE_APPROVAL_EXPIRED`, `STALE_APPROVAL_NOT_MATCHING`). `STALE` is terminal and non-executable; it is never silently treated as approval, and the caller must resubmit a fresh request (a new `pendingExecutionId`) rather than retry the same claim.

**14. What makes the internal resume grant non-caller-constructible?**
`ResumeAuthorityGrant` is a TypeScript nominal/branded type (for example, carrying a non-exported unique symbol brand field, following the standard TypeScript branding pattern), whose only constructor is a private/module-internal function invoked exclusively from inside the successful branch of `claimPendingExecution`'s atomic critical section. No exported factory, no public constructor, and no plain-object literal matching its public shape is sufficient to satisfy its type outside that module, because the brand field's type is not constructible from outside the module that declares it. This is the same "no caller-supplied or synthesized `ALLOW`" principle the T0A completion review already required for `execute(intent, guardResult)` (`agent-execution-runtime.ts` line 233), generalized to this new type: nothing may hand-construct a `ResumeAuthorityGrant` object literal and have it type-check or be accepted by the consumer in Q15.

**15. Which component may consume that grant and how is single use enforced?**
Only the future `ExecutionProvider` adapter (named in the T0A Q12/Q17 future manifest, not created by this tranche) may consume a `ResumeAuthorityGrant`; it is the sole caller permitted to pass the grant into a function that ultimately invokes `admitAndInvokeProvider`. Single use is enforced at two layers: (a) the grant's `claimId` is marked `CONSUMED` (Q5) by the adapter's wrapper, in the same atomic-write style as the claim operation itself, immediately upon successful or failed provider-invocation attempt, so a second presentation of the same grant object finds `status !== 'CLAIMED'` and is rejected; and (b) the grant object itself carries no serializable representation that could be reconstructed and replayed after process exit - it is a live, in-memory-only handle for the duration of one resume request, analogous to how `ApprovalExecutionBridge`'s bridge instance (confirmed process-memory-only per T0A Q8) cannot survive a request boundary, except here that same non-durability property is deliberately exploited as a security property (a grant cannot outlive the request that earned it) rather than being a limitation.

**16. How are approvalId, pendingExecutionId, claimId, requestId, attempt index, audit event and response correlated?**
`PendingAgentExecutionRecord.approvalId` links to `ApprovalRequestRecord.id`. `PendingAgentExecutionRecord.pendingExecutionId` is the record's own primary key. `PendingAgentExecutionRecord.requestId` is AER's `GuardRequestContext.requestId` format, generated at submit/preCheck time. `claimId` is generated fresh by the atomic claim operation and stored on the record once `CLAIMED`. `attemptIndex` is populated from `ProviderAttemptLedger.attempts[].attemptIndex` (`provider-attempt-admission.ts` line 57) once the future `ExecutionProvider` adapter's call is admitted. Every `appendAuditEvent` call in this flow (submit-create, claim-success, claim-denied, stale, consumed, abandoned) must carry a `payload` containing all five identifiers (`approvalId`, `pendingExecutionId`, `claimId`, `requestId`, `attemptIndex`) so a single audit query can reconstruct the full chain, mirroring how `approvals/[id]/route.ts`'s `PATCH` already includes `approvalId`/`templateId` in its `APPROVAL_DECIDED` audit payload (lines 111-115). The final HTTP response (not designed by this tranche; named in T0A Q16) must echo the same identifiers so a client can correlate its own request to the audit trail.

**17. Which negative cases must future focused tests prove?**
1. Concurrent double claim on the same `pendingExecutionId` yields exactly one `ok: true` and every other caller receives `ALREADY_CLAIMED`.
2. A claim attempt against a `STALE` binding (changed intent/actor/session/cwd/environment) is rejected with `STALE_BINDING_CHANGED` and starts zero provider calls.
3. A claim attempt against a changed `guardPolicyFingerprint` is rejected with `STALE_POLICY_FINGERPRINT_CHANGED` and starts zero provider calls.
4. A claim attempt against an expired or non-`approved` linked `ApprovalRequestRecord` is rejected and starts zero provider calls.
5. A forged/hand-constructed object matching `ResumeAuthorityGrant`'s public shape is rejected by the consumer (type-level and, where reachable at runtime via untyped JS callers, a runtime brand check) as a defensive-programming test.
6. A create-path write failure (simulated fsync/rename failure) never returns an acknowledged `pendingExecutionId`, and no orphaned partial record is claimable afterward.
7. A single-record parse/corruption failure on load marks only that record `STALE` and does not clear or corrupt sibling records.
8. A whole-file parse failure on load blocks all claims (`LOAD_FAILED`) rather than silently resetting to an empty store.
9. Process restart correctly ages a `CLAIMED` record past the abandonment window into `ABANDONED` without ever admitting a second claim or a second provider call for the same `pendingExecutionId`.
10. A successfully consumed grant (`status: 'CONSUMED'`) cannot be claimed or consumed a second time even if presented again in the same process lifetime.
11. Exactly one `admitAndInvokeProvider` call occurs per successful claim-to-consumption path, verified via `ProviderAttemptLedger.providerCallCount`.
12. Every terminal disposition (`CONSUMED`, `STALE`, `ABANDONED`, `EXPIRED`) produces a durable `appendAuditEvent` carrying all five correlation identifiers from Q16.

**18. Is the contract ready for a later T1 packet, requires another decision, or must remain parked?**
`SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION`, subject to the controlling
Independent Reviewer Contract Correction below. The worker's original digest,
CAS, runtime-brand and terminal-state details are superseded where they
conflict with that correction. This does not open T1.

## Independent Reviewer Contract Correction

Reviewer disposition: `REVIEWER_ACCEPTED_WITH_BOUNDED_SEMANTIC_REPAIR`.

Candidate 2 and the terminal token are retained, but the following corrected
contract is controlling for any later T1 packet:

1. `PendingAgentExecutionRecord` stores the complete immutable authority
   payload, including `pendingExecutionId`, `createdAt`, the exact linked
   `approvalRequestHash`, the complete normalized `ApprovalRequestSnapshot`,
   normalized intent, actor/session/runtime binding, complete original guard
   result, and a versioned `GuardPolicySnapshot`. Environment values must be
   allowlisted identity metadata; arbitrary process environment and secrets
   are rejected.
2. `recordDigest` is lowercase SHA-256 over UTF-8 RFC-8785/JCS canonical JSON
   of every immutable authority field. JSON-incompatible values, duplicate or
   unsupported representations, non-finite numbers, and undefined-bearing
   objects fail create. Arrays preserve order. Mutable transition fields are
   excluded. The worker's partial digest over only
   `originalGuardDecision.finalDecision` is superseded.
3. `guardPolicyFingerprint` is the digest of the versioned
   `GuardPolicySnapshot`, not an unspecified digest of an in-memory engine.
   The snapshot must include ordered guard identifiers and versions, relevant
   normalized configuration digests, phase/risk/role/channel/control mode, and
   any policy snapshot identifier. If current source cannot produce this
   deterministically, T1 remains blocked at implementation time.
4. The store contract exposes a linearizable
   `compareAndSwap(pendingExecutionId, expectedVersion, expectedStatus,
   transition)` operation. A synchronous in-process critical section and
   ordinary rename are not cross-process CAS. Each production-capable adapter
   must prove its atomicity over its declared deployment boundary. A local
   filesystem adapter may be non-production only and must use an exclusive
   create/lock primitive plus durable transition evidence; silent fallback is
   forbidden.
5. The controlling lifecycle is `CREATED -> CLAIMED -> EXECUTING`, then exactly
   one truthful terminal: `SUCCEEDED`, `FAILED`, `DENIED`, or
   `UNKNOWN_TERMINAL`. `CREATED` may become `EXPIRED` or `STALE`; `CLAIMED`
   may become `ABANDONED_BEFORE_START`. A crash or timeout after durable
   `EXECUTING` can only become `UNKNOWN_TERMINAL`, never retryable. Every
   terminal is non-executable. The worker's single `CONSUMED` state is
   superseded because it hid provider outcome and the ambiguous-start window.
6. Approval validation uses the authenticated actor plus the stored approval
   snapshot/hash. The resume request supplies only the pending identifier and
   authentication context; it does not restate authority-bearing intent.
   Claim verifies the linked record is approved/unexpired, actor-bound,
   `requestHash === approvalRequestHash`, and that recomputing the stored
   snapshot hash yields that same value.
7. A TypeScript brand alone is not runtime authority. The grant is a
   module-private runtime capability registered in a module-private `WeakSet`
   (or stronger equivalent), never serialized or returned by HTTP. Only a
   co-located consumer can validate it. Consumption deletes the capability
   and durably CAS-transitions `CLAIMED -> EXECUTING` before provider admission;
   failure to persist that transition starts zero provider calls.
8. After `EXECUTING` is durable, the consumer calls
   `admitAndInvokeProvider` exactly once. Admission denial ends `DENIED` with
   zero provider calls. Resolved success/failure ends `SUCCEEDED`/`FAILED`.
   Crash, timeout, or lost acknowledgement after call start ends or reconciles
   only to `UNKNOWN_TERMINAL`; no automatic replay is authorized. This is an
   at-most-once-start safety contract, not an exactly-once provider-result
   claim.
9. `attemptIndex` must be allocated and persisted before `EXECUTING`; every
   transition and HTTP/audit projection carries `approvalId`,
   `pendingExecutionId`, `claimId`, `requestId`, `attemptIndex`, `recordVersion`
   and terminal reason. Missing identifiers use an explicit null/not-yet-
   allocated representation rather than invented values.
10. Future tests must additionally prove: cross-process CAS behavior over the
    adapter's declared boundary; digest sensitivity to every immutable field;
    rejection of secret/non-allowlisted environment data; runtime rejection of
    structurally forged grants; atomic pre-admission capability consumption;
    crash before and after durable `EXECUTING`; no replay from
    `UNKNOWN_TERMINAL`; and truthful distinct terminal audit/response mapping.

With these corrections the contract is exact enough for a later T1 packet to
be considered. T1 must implement the contract as one bounded non-production
slice first; production/distributed readiness remains separately blocked.

## Findings / Position

Terminal decision: `SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION`.

Candidate 2 (a dedicated, versioned `PendingAgentExecutionRecord` schema and
store, fully separate from `ApprovalRequestRecord`, with linearizable CAS and
a runtime-held, single-use, internally-constructed `ResumeAuthorityGrant`) is
the only candidate that satisfies all nine
Mandatory Contract Invariants without modifying the existing accepted
`/api/approvals` or `/api/execute` contracts. Candidate 1 (extending
`ApprovalRequestRecord`) was rejected because it structurally conflates
approval-decision authority with execution-claim authority in one mutable
object and one enum, which is exactly the authority-laundering risk the T0A
completion review already flagged for the `execute()`/`ALLOW` boundary.
Candidate 3 (retain parked) was not selected because Candidate 2's schema,
digest, state machine, claim operation, and grant boundary are all exactly
nameable from current source plus the controlling reviewer correction. Storage
adapter atomicity and deterministic policy-snapshot production remain mandatory
T1 implementation gates, not assumed existing behavior.

The fresh negative search confirms zero existing owner for
`PendingAgentExecution`, `ResumeAuthorityGrant`, `claimPendingExecution`, or
`pending-agent-execution` anywhere in current source, so this contract does
not collide with or duplicate any existing mechanism. `ApprovalExecutionBridge`
remains confirmed (per T0A, reconfirmed here) as unusable for the Web HTTP
approval lifecycle because its `pending` Map is process-memory-only; this
contract does not use it.

## Risk / Corrective Action

The primary risk is a future T1 implementer treating this contract's schema
names as already-existing source, when in fact `PendingAgentExecutionRecord`,
`ResumeAuthorityGrant`, and `claimPendingExecution` are proposed names with
zero current source backing (confirmed by the fresh negative search above).
The corrective action is that any future T1 work order must state explicitly
that these are new files/types to be created, not existing owners to be
imported.

A secondary risk is a future implementation computing `guardPolicyFingerprint`
inconsistently between create time and claim time (for example, if the guard
engine's rule set is mutable at runtime and two different processes hold
different in-memory configurations). The corrective action named in Q17's
test 3 requires an explicit focused test proving that a changed fingerprint
is detected and fails closed, not merely assumed stable.

A tertiary risk is a future implementer reusing `FileBackedApprovalStore`'s
current silent-failure `persist()` pattern (`store.ts` line 96,
`console.warn` only) for the new pending-execution store. The corrective
action is Q6/Q7's explicit requirement that create-success acknowledgment
requires a verified durable write plus read-back, and that write/fsync
failures must propagate to the caller rather than being swallowed.

Independent review also found four semantic defects in the original worker
contract: an incomplete/self-contradictory digest, a non-linearizable rename/
in-process claim proposal, compile-time branding presented as runtime
authority, and a `CONSUMED` state that erased provider outcome and ambiguous
start. The controlling correction above repairs all four before closure.

## Decision / Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Terminal token | `SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION` |
| Reviewer consideration | authorized; does not open T1 |
| successorTrancheOpened | NO |
| T0A direction | CONFIRMED and narrowed: Candidate 2 (async submit/pending plus separate approval decision and authenticated resume) remains the correct architecture; this tranche narrows it from an architecture direction into an exact schema/state-machine/claim/grant contract |
| Selected candidate | Candidate 2: dedicated versioned pending-execution record/store plus atomic claim and internal resume grant |
| New schema name | `PendingAgentExecutionRecord`, `schemaVersion: 'cvf.pendingAgentExecution.v1'` |
| New grant type name | `ResumeAuthorityGrant` (module-private runtime capability, WeakSet-or-stronger validation, single-use) |
| Safety claim | at-most-once provider start; ambiguous post-start outcome becomes `UNKNOWN_TERMINAL`, never replay |

## Mandatory Invariants Reconciliation

The Independent Reviewer Contract Correction is controlling for this table.
Earlier Q5-Q15 text is retained as worker-decision history only where it uses
`CONSUMED`, an in-process critical section/ordinary rename, or TypeScript
branding as the enforcement mechanism.

| Invariant | Status under Candidate 2 |
| --- | --- |
| Approval PATCH starts zero provider calls and emits no executable grant | Satisfied: `approvals/[id]/route.ts` `PATCH` (lines 57-119) is untouched by this decision; it writes only `ApprovalRequestRecord` fields and never touches the pending-execution store or the claim primitive |
| Approval status alone never authorizes execution | Satisfied by design: the claim operation (Q8) requires the atomic claim to succeed in addition to `status === 'approved'`; approval status is one of five preconditions, not a sufficient one |
| Caller-supplied or synthesized `ALLOW` is forbidden | Satisfied after reviewer correction: the resume surface accepts only the pending identifier plus authenticated caller context, while a module-private runtime capability validated through a private `WeakSet` (or stronger mechanism) is created only after successful durable claim |
| Create is acknowledged only after durable success; uncertainty fails closed | Satisfied by design: Q6/Q7 require a verified write-plus-read-back before returning `CREATED`, unlike the existing `FileBackedApprovalStore.persist()` swallow-on-failure pattern |
| Claim is atomic and yields at most one executable winner | Satisfied after reviewer correction: the store contract requires a linearizable versioned compare-and-swap; an in-process critical section or ordinary rename is explicitly insufficient for cross-process safety |
| No lease/retry rule may permit duplicate provider invocation after ambiguous execution start | Satisfied after reviewer correction: `CLAIMED -> ABANDONED_BEFORE_START` is allowed only before durable provider-start admission; after `EXECUTING`, ambiguity becomes non-retryable `UNKNOWN_TERMINAL` and never authorizes replay |
| Any actor, digest, binding, approval, expiry, guard or policy drift is stale and non-executable | Satisfied by design: Q11-Q13's five-precondition drift check and `STALE_*` disposition family |
| Grant construction is internal, opaque and single-use | Satisfied after reviewer correction: TypeScript branding is compile-time defense only; runtime membership is private and consumption removes the capability before a durable `CLAIMED -> EXECUTING` CAS |
| Future provider invocation still routes through exactly one `admitAndInvokeProvider` call | Satisfied after reviewer correction: after the durable `EXECUTING` transition, exactly one adapter path may call `admitAndInvokeProvider`; the result is recorded as `SUCCEEDED`, `FAILED`, `DENIED`, or `UNKNOWN_TERMINAL`, supporting at-most-once provider start rather than exactly-once result |

## Evidence / Verification

- executionBaseHead `3fcb0d418`; `git status --short --untracked-files=all` clean at worker start.
- Two exact `rg` searches reproduced above with full non-test hit classification; second search returned zero hits (confirmed via `rg` exit code 1).
- Full reads of `agent-execution-runtime.ts`, `store.ts` (approvals), `approval-binding.ts`, `approvals/[id]/route.ts`, `execute/route.ts`, `provider-attempt-admission.ts`, `control-plane-events.ts` in full, plus T0A assessment and T0A completion in full.
- Zero provider/network/browser/credential calls were made while producing this assessment.
- This worker made no runtime, package, route, test, checker, workflow, `/api/execute`, or approval-PATCH edit.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `docs/assessments/` classified as `baseline` doc type by `_classify` in the structural completeness checker (path prefix match), requiring source/predecessor-evidence, decision/baseline/proposed-tranche, and evidence/verification section groups; the Agent-Operation-Trace-Block section's required label set (`Actor` through `Deletion or rename disposition`); the Delta-Execution-Claim-Boundary-Control-Block section's required field set and accepted enum tokens (`CLAIM_REJECTED`, `N/A with reason`, `CLAIM_REJECTED_NO_RECEIPT`, `CLAIM_REJECTED_NO_ACTION`); the Public-Export-Disposition section's allowed tokens (`EXPORTED`, `DEFERRED_PRIVATE_ONLY`, `BLOCKED_MISSING_PUBLIC_ARTIFACTS`); the Checker-Source-Read-Ahead-Block section's required fields (`applicableCheckersRead`, `literalTokensReviewed`, `gateRunPurpose`, `claimBoundary`) from `check_governed_artifact_checker_read_ahead.py` |
| gateRunPurpose | confirmation evidence after direct checker-source inspection; checker constants were read and reviewed before this artifact was authored |
| claimBoundary | shape and source-fact readiness only; this block makes no independent semantic-acceptance claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit decision worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | GC010-SCR-R2-T0B worker execution, 2026-08-30 |
| Working directory | repository root |
| Command or tool surface | direct file reads, `rg`, `git rev-parse`/`git status` |
| Target paths | all files listed in Evidence / Verification above, plus this assessment and the paired worker return |
| Allowed scope source | work order Worker Autonomy / No-Question Rule and Scope sections |
| Before status evidence | executionBaseHead `3fcb0d418`; `git status --short --untracked-files=all` clean; both output paths absent |
| After status evidence | this assessment and the paired worker return created; no other path changed |
| Diff evidence | `git diff --name-status` (empty prior to authoring; two new untracked files after) |
| Approval boundary | decision-only; no runtime, route, package, test, checker, or workflow change |
| Claim boundary | architecture/schema decision and contract specification only; no runtime behavior, export, route, provider, store, or grant is implemented or claimed |
| Agent type | delegated worker |
| Invocation ID | `gc010-scr-r2-t0b-worker-2026-08-30` |
| Expected manifest | `docs/assessments/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`; `docs/reviews/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_WORKER_RETURN_2026-08-30.md` |
| Actual changed set | the same two paths; no other path was created, modified, or deleted |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this tranche |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only pending-execution safe-resume contract decision; no runtime behavior |
| claimDisposition | CLAIM_REJECTED: no execution-control, governed-coding-control, interception, or runtime-enforcement claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is produced by this decision |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: only file reads, exact `rg`/`git` searches, and two documentation outputs occurred |
| invocationBoundary | no route, provider, store, or adapter is invoked, created, or registered |
| interceptionBoundary | no wrapper, proxy, or mandatory runtime control is implemented or proposed as already active |
| claimLanguage | proposed schema/state-machine/claim/grant contract and named future-manifest gaps only |
| forbiddenExpansion | runtime/package/Web mutation, provider/live, public, deploy, production, and automatic T1 opening remain out of scope of this decision |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private decision-only system-chain dispatch; no public artifact,
runtime behavior, or release claim is authorized by this assessment.

## Claim Boundary

This assessment records a documentation-only contract decision. It selects
`SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION`, names the exact
`PendingAgentExecutionRecord` schema, canonical digest, lifecycle state
machine, atomic claim operation, and `ResumeAuthorityGrant` boundary, and
states a future negative-test manifest. It does not create a store, route,
claim primitive, resume grant, AER export, or provider adapter, call a
provider, open T1, or claim live, public, deployment, or production
readiness. `successorTrancheOpened: NO`.
