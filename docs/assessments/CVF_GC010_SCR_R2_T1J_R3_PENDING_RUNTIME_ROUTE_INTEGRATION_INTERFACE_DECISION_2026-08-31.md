# CVF GC010 SCR-R2-T1J-R3 Assessment - Pending Runtime Route Integration Interface Decision

Memory class: governed-worker-assessment

docType: assessment

Status: COMPLETE_PENDING_REVIEW

Batch ID: GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION

Date: 2026-08-31

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_2026-08-31.md`

executionBaseHead: `1e8e186d5f4739dc18e1d7726c1fde7a65975b6d`

successorTrancheOpened: NO

Selected terminal: `PARTIAL_READY_REQUIRES_ONE_NAMED_IMPLEMENTATION_PRECONDITION`

## Purpose

Resolve the complete pending-runtime route-integration interface left open by corrected T1J-R2 in one bounded pass:
route ordering, immutable payload/policy-snapshot construction, SQLite lifecycle, and authorized crash recovery
together. Compare Candidates A-D as complete interfaces, answer fourteen mandatory questions, and select one terminal
without implementing anything.

## Target / Source

- T1J-R2 accepted assessment: `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`
- Execute route (full approval, enforcement, and gateway sections): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Approval PATCH route: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts`
- Approval store record shape: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts`
- Enforcement evaluation: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts`
- Web governance envelope: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- Pending-agent-execution core: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`
- Pending-agent-execution SQLite store: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts`
- Pending-agent-execution composition: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts`
- Local harness (only current caller pattern): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts`

## Scope / Methodology

Worker captured clean execution base `1e8e186d5f4739dc18e1d7726c1fde7a65975b6d` (confirmed by `git rev-parse HEAD`;
`git status --short --untracked-files=all` returned empty). Both output paths were confirmed absent before authoring.
Pre-implementation autorun gate passed before authoring.

Worker read the T1J-R3 baseline and work order, the accepted T1J-R2 assessment in full, and every source path named
in both packets' Source Verification Blocks, each read in full: `execute/route.ts` from the request-parse entry point
through the approval-resume validation block, the `enforcement.status` branches (`BLOCK`/`CLARIFY`/`NEEDS_APPROVAL`),
the pre-gateway construction of `guardContext`, and the `runExecuteRouteMandatoryGateway` call and its downstream
`guardResult`/provider-attempt sections; the approval PATCH route and `ApprovalRequestRecord`/`ApprovalRequestContext`/
`ApprovalRequestSnapshot` field definitions; the pending core's `GuardPolicySnapshot`/`PendingAgentExecutionImmutablePayload`
type definitions and validators; the SQLite store's constructor, `compareAndSwap`, and lifecycle; and the composition
module's bounded wrapper interface. All claims below are re-derived from this execution base rather than inherited
from T1J-R2's line citations without recomputation. This assessment makes zero source, test, package, script, or
session-state edits and zero provider/network/browser/credential/live calls.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Approval-resume validation runs first, immediately after body parse and auth, before `enforcement`/gateway | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 99-268 | `body.approvalId` block | `POST` | ACCEPT |
| `enforcement = evaluateEnforcement(...)` is a separate lightweight decision function, not `GuardRuntimeEngine`/`GuardPipelineResult`; `NEEDS_APPROVAL` is one of its four status values | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` lines 1-18; `execute/route.ts` line 416 | `EnforcementStatus`; `evaluateEnforcement` | enforcement module | ACCEPT |
| Approval issuance (`NEEDS_APPROVAL` branch, when no `approvalId` supplied) occurs before `guardContext` construction and before the real guard gateway call | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 416, 497-576, 578-605 | `evaluateEnforcement`; `guardContext`; `runExecuteRouteMandatoryGateway` | `POST` | ACCEPT |
| `guardContext` requires `resolvedExecutionRole.permissionRole`, which is only computed after role-permission gate checks that themselves occur after the `NEEDS_APPROVAL` branch in source order | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 382-406, 578-593 | `resolvedExecutionRole`; `guardContext` | `POST` | ACCEPT |
| `govEnvelope.policySnapshotId` is a random `pol-`-prefixed string, not a `GuardPolicySnapshot`-shaped object | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 25-97 | `WebGovernanceEnvelope.policySnapshotId`; `generatePolicySnapshotId` | web governance envelope | ACCEPT |
| `GuardPolicySnapshot` requires an exact `schemaVersion`, non-empty `rows[]` with hex64 `configDigest` per row, plus `phase`/`riskLevel`/`role`/`channel`/`controlMode`/`policySnapshotId`; no non-test route builder constructs this shape anywhere in the searched tree | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 238-326 | `GuardPolicySnapshot`; `validateGuardPolicySnapshot` | pending core | ACCEPT |
| `ApprovalRequestRecord`/`ApprovalRequestContext`/`ApprovalRequestSnapshot` carry only `policySnapshotId` (string) and no `originalGuardResult` or `GuardPolicySnapshot`-shaped field anywhere | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | lines 10-61 | `ApprovalRequestContext`; `ApprovalRequestSnapshot`; `ApprovalRequestRecord` | approval store | ACCEPT |
| Approval PATCH route mutates only `status`/`reviewedAt`/`reviewedBy`/`reviewComment`; it never touches `originalGuardResult`, `normalizedIntent`, or `policySnapshot` because none of those fields exist on the record it reads | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | lines 57-119 | `PATCH` | approval decision route | ACCEPT |
| Pending immutable payload requires `approvalId`, `approvalRequestHash`, `approvalRequestSnapshot`, `normalizedIntent`, `binding`, `originalGuardResult`, `environment`, `policySnapshot` together, with no partial construction path | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 367-376, 645-671 | `PendingAgentExecutionImmutablePayload`; in-memory-store `create` validation | pending core | ACCEPT |
| Claim/begin use CAS with a process-local, single-use, non-serializable grant | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 775-925; 939-970 | `ResumeAuthorityGrant`; `claimPendingExecution`; `beginPendingExecution` | pending core | ACCEPT |
| Explicit pre-start and ambiguous-executing recovery transitions exist with no current non-test caller anywhere in the route/CLI/MCP/Execution-Plane trees | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 987-994 | `abandonBeforeStart`; `resolveAmbiguousExecutingCrash` | pending core | ACCEPT |
| SQLite store requires a caller-supplied absolute path, has no default/env/global path, and exposes only an explicit, non-scheduled `close()` | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | lines 432-510 | constructor; `close` | SQLite store | ACCEPT |
| Only current caller pattern (local harness) supplies path and closes explicitly per bounded invocation | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts` | lines 1-136 | `dbPath`; `runtime.close()` | local harness | ACCEPT |
| T1J-R2 reviewer correction names the four-member interface cluster and keeps T1K parked | accepted assessment | `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md` | Independent Reviewer Correction | `ACCEPT_WITH_MATERIAL_CORRECTION` | T1J-R2 | ACCEPT |

## Current Call-Order Table (As-Built, With Early Returns)

| Step | Line(s) | Action | Early-return conditions before this step |
| --- | --- | --- | --- |
| 1 | 99-110 | Parse request body | Invalid JSON (400) |
| 2 | 111-131 | Authenticate (session or service token) | Unauthorized (401) |
| 3 | 132-136 | Validate body is an object; normalize inputs | Invalid payload (400) |
| 4 | 140-148 | Build `govEnvelope` (random `envelopeId`/`policySnapshotId`) | none |
| 5 | 150-160 | Rate limit | Too many requests (429) |
| 6 | 162-171 | Validate required fields present | Missing fields (400) |
| 7 | 172-173 | Inline-knowledge-context bypass check | Blocked response |
| 8 | 174-183 | Resolve provider, build approval actor binding, snapshot, hash | none |
| 9 | 184-267 | **If `body.approvalId` present**: validate approval record (existence, hash-binding, actor-binding, expiry, `approved` status) | Approval not found/expired/mismatched/not-approved (404/409/403) |
| 10 | 269-329 | Resolve API keys, build prompt, DLP filter, safety workflow chain | Safety-blocked (400) |
| 11 | 330-344 | Legacy safety filters | Blocked (400) |
| 12 | 345-377 | Quota check | Quota exceeded (429) |
| 13 | 379-405 | Resolve execution role, actor-role gate | Role denied (403) |
| 14 | 406-432 | Resolve output class/role permission, build `enforcement` input | Output permission denied |
| 15 | 416 | `evaluateEnforcement(...)` computes `enforcement.status` | none |
| 16 | 434-465 | `enforcement.status === 'BLOCK'` | Blocked (per enforcement) |
| 17 | 466-496 | `enforcement.status === 'CLARIFY'` | Needs clarification (422) |
| 18 | 497-576 | `enforcement.status === 'NEEDS_APPROVAL'`: if `approvedRequestRecord` present, audit `APPROVAL_CONSUMED` and delete it (line 513); else **issue a new approval record** (`ApprovalStore.set`, line 521) and return `approvalId` (409) | Returns 409 either way (consume-then-continue, or issue-and-stop) |
| 19 | 578-593 | Build `guardContext` (requires `resolvedExecutionRole.permissionRole` from step 13) | none |
| 20 | 594-604 | `runExecuteRouteMandatoryGateway` (the real `GuardRuntimeEngine`/`GuardPipelineResult` boundary) | `gatewayOutcome.blockedResponse` |
| 21 | 605 onward | `guardResult` now exists; provider routing, `admitAndInvokeProvider` (801, 859), terminal response | Various provider-attempt outcomes |

**Key structural fact (answers Questions 1 and 2 together):** approval issuance (step 18) is driven by `enforcement`
(step 15, a separate lightweight policy function), not by the real guard gateway (step 20). `guardResult` (the actual
`GuardPipelineResult` from `GuardRuntimeEngine`) does not exist in scope until step 20, which runs strictly after
every approval-issuance and approval-resume-validation step. There is no current early return between step 18 (new
approval issued) and step 20 (real gateway) other than the approval-issuance response itself; a *resumed* request
(carrying `approvalId`) that already cleared step 9 proceeds through steps 10-20 exactly like a fresh request, so the
real gateway still runs exactly once per resumed request, same as today.

## Required-Field Provenance Table (`PendingAgentExecutionImmutablePayload`)

| Field | Current source owner | Lifecycle point available | Disposition |
| --- | --- | --- | --- |
| `approvalId` | `ApprovalStore`-generated ID (`execute/route.ts` line 517) | At approval issuance (step 18) | SOURCE_OWNED |
| `approvalRequestHash` | `computeApprovalRequestHash(approvalSnapshot)` (line 182) | Computed before step 9, reusable at step 18 | SOURCE_OWNED |
| `approvalRequestSnapshot` | `buildApprovalRequestSnapshot(body, provider, approvalActor)` (line 181) | Computed before step 9, reusable at step 18 | SOURCE_OWNED |
| `normalizedIntent` | No current builder; `body.intent`/`body.inputs` are raw request fields, not a `NormalizedIntent { action, targetFiles?, parameters? }`-shaped value | None | PROPOSED_ONLY (would require a new, currently nonexistent normalization function; this is a genuinely new field, not a renamed existing one) |
| `binding` (`ActorSessionRuntimeBinding`) | `approvalActor` (`buildApprovalActorBinding`, line 177) supplies `actor`; `sessionId`/`cwd`/`fileScope` have no current single owner in the approval-issuance branch (`fileScope` exists only via `rawBody.fileScope` read later, at line 586, for `guardContext`, not at step 18) | Partially available at step 18 (`actor` only); `sessionId`/`cwd` not populated anywhere in this route for a web request | PARTIALLY_SOURCE_OWNED (actor only); MISSING (`sessionId`, `cwd`) |
| `originalGuardResult` | `guardResult` (`GuardPipelineResult`), only exists after step 20 | Only after the real gateway runs, which is strictly after approval issuance (step 18) | MISSING_AT_ISSUANCE_TIME (structural: cannot exist before the gateway that produces it has run) |
| `environment` (`EnvironmentIdentity`) | No current builder in `execute/route.ts`; the type's `deploymentBoundary` field must be exactly `'single_process_non_production'` (`pending-agent-execution.ts` line 224-226), which is not a claim `execute/route.ts` can truthfully make for a production Next.js request handler | None | MISSING_AND_SEMANTICALLY_INCOMPATIBLE (the pending core's own validator rejects any other `deploymentBoundary` value; a route-composed caller cannot honestly supply this literal today) |
| `policySnapshot` (`GuardPolicySnapshot`) | No current non-test builder anywhere in the searched tree (`route/`, `lib/`) produces this shape; `govEnvelope.policySnapshotId` is a different, incompatible type (random string ID vs. a validated object with `rows[]`) | None | MISSING (field-by-field rejection recorded below, answers Question 4) |

**Question 4 field-by-field proof that `WebGovernanceEnvelope` is not equivalent to `GuardPolicySnapshot`:**

| `GuardPolicySnapshot` field | `WebGovernanceEnvelope` equivalent | Compatible? |
| --- | --- | --- |
| `schemaVersion: 'cvf.guardPolicySnapshot.pendingExecution.v1'` | none | NO |
| `rows: GuardPolicySnapshotRow[]` (non-empty, each with hex64 `configDigest`) | none | NO |
| `phase` | `body.cvfPhase` is available as a raw string, but is not assembled into a `GuardPolicySnapshotRow`-bearing object | NO (raw field only, not the required object) |
| `riskLevel` | `body.cvfRiskLevel` similarly available as a raw string only | NO |
| `role`, `channel`, `controlMode` | none | NO |
| `policySnapshotId` | `govEnvelope.policySnapshotId` exists but is a random `pol-`-prefixed string generated per request, not derived from any guard configuration digest | STRING_PRESENT_BUT_SEMANTICALLY_DIFFERENT |

No field in `WebGovernanceEnvelope` satisfies `GuardPolicySnapshot`'s schema; the two are rejected as equivalent, not
merely "different names for the same data."

## Required Candidate Comparison (Complete Interfaces, A-D)

### Candidate A: move the mandatory gateway before approval creation

| Field | Value |
| --- | --- |
| Source compatibility | `EXISTING_SOURCE_INCOMPATIBLE` for a same-tranche decision; would require reordering the route's own step sequence |
| Creation identity | Would create one pending record at the (moved-earlier) approval-issuance point, now armed with a real `guardResult` |
| Payload owner | Once moved, `originalGuardResult` would be source-owned (the just-computed `guardResult`). `policySnapshot` (`GuardPolicySnapshot`) would still have no builder: moving the gateway earlier does not create the missing `GuardPolicySnapshotRow[]`/hex64-digest structure, because `runExecuteRouteMandatoryGateway`'s own output (`GuardPipelineResult`) is not shown by any current source citation to already be, or to trivially convert to, this shape. `normalizedIntent`, `environment.deploymentBoundary`, and `binding.sessionId`/`cwd` remain unbuilt regardless of gateway position (Question 5 below). |
| Gateway owner | Moved earlier, but still called exactly once (Question 5 requires proving denial/quota/approval/audit/provider-attempt semantics are unchanged) |
| Approval owner | `ApprovalStore`, unchanged in write pattern, only its position in the route shifts |
| Claim/begin/provider/terminal order | Unaffected structurally; same as Candidate B's proposed order (see below) once a payload exists |
| SQLite owner | Same open question as identified in T1J-R2: no current source names connection-lifetime/path ownership for a route-composed store |
| Recovery owner | Same as Candidate B/T1J-R2: `abandonBeforeStart`/`resolveAmbiguousExecutingCrash` exist but have no current caller |
| Audit owner | `appendAuditEvent('APPROVAL_CONSUMED', ...)`, unchanged in principle |
| Failure windows | Reordering the gateway earlier changes when quota/safety/role-gate/rate-limit checks run relative to guard evaluation; the work order's Question 5 requires proving this reordering does not change denial, quota, approval, audit, or provider-attempt semantics, and no current source demonstrates this is safe: quota check (step 12) and role-permission checks (step 13-14) currently run *after* provider/prompt construction but *before* enforcement, and moving the gateway to run before all of these would change the observable order of a BLOCK-vs-quota-exceeded-vs-role-denied response for the same malformed/risky request, which is an externally observable behavior change this tranche cannot verify is safe from documentation alone |
| Duplicate-boundary risk | LOW for guard/provider duplication itself (still exactly one gateway call, one admission boundary), but MEDIUM for behavioral drift in which check "wins" first for a request that would previously have failed quota/role/safety before ever reaching approval logic |
| Value beyond current route | Would close the `originalGuardResult` gap, but does not close the `policySnapshot`/`normalizedIntent`/`environment`/`binding.sessionId,cwd` gaps, and introduces an unverified reordering risk the current route does not have |
| Smallest future manifest | Not proposed as ready: this candidate resolves at most one of the four required interface members (payload's `originalGuardResult` field only) while leaving the `GuardPolicySnapshot` builder, `normalizedIntent` builder, `environment`/`binding` completion, SQLite lifecycle, and recovery authority all still open, and adds a new, unverified reordering risk the other candidates do not have |

### Candidate B: preserve current approval-return ordering, create the pending record at approved-resume time (after the gateway)

| Field | Value |
| --- | --- |
| Source compatibility | `PROPOSED_NEW_OWNER_COMPATIBLE`; does not require reordering any existing check |
| Creation identity (answers Question 6) | The pending record would be created at step 21 (after the gateway succeeds, i.e., after `guardResult` exists and after `admitAndInvokeProvider` is about to run, or immediately before it), using `approvedRequestRecord.id` (the existing `approvalId`) as the `pendingExecutionId`. `PendingAgentExecutionSqliteStore.create` enforces a `PRIMARY KEY` on `pending_execution_id` (`pending-agent-execution-sqlite-store.ts` line 126, `CREATE_TABLE_SQL`) inside its own `transaction()` (lines 562-602), and the `UNIQUE constraint failed` path is explicitly caught and converted to a typed `IO_FAILURE` (lines 581-586) rather than silently succeeding twice. Because `approvalId` is deleted from `ApprovalStore` exactly once (existing line 513, unchanged in this candidate) before this creation point, and the SQLite primary-key constraint independently rejects a second `create` call with the same ID even if two concurrent resume requests both raced past the earlier delete, exactly-once creation is proven by two independent mechanisms (the existing delete-based single-winner pattern from T1J-R2's own analysis, plus a fresh, source-backed unique-constraint defense this tranche adds), not by only one of them. |
| Payload owner | `originalGuardResult` = `guardResult` (now available at step 21, after the gateway). `approvalId`/`approvalRequestHash`/`approvalRequestSnapshot` = existing values, unchanged. `normalizedIntent`, `environment` (with the required literal `deploymentBoundary`), and `binding.sessionId`/`binding.cwd` remain unbuilt by any current source (same gap as Candidate A; this gap is independent of route ordering) |
| Gateway owner | Unchanged: exactly one `runExecuteRouteMandatoryGateway` call, at its current position; no reordering risk |
| Approval owner | `ApprovalStore`, unchanged: validated at step 9, consumed (deleted) at step 18 exactly as today |
| Claim/begin/provider/terminal order (answers Question 11) | 1) `runtime.create(...)` immediately after the gateway succeeds and immediately before the provider-attempt call; 2) `runtime.claim(...)` (or a combined create+claim if the caller is also the sole authorized claimant, which the single-winner analysis above supports treating as effectively immediate); 3) `APPROVAL_CONSUMED` audit (already exists, unchanged position); 4) `runtime.begin(grant, attemptIndex)` immediately before `admitAndInvokeProvider`; 5) `admitAndInvokeProvider` (unchanged, exactly once per attempt including retry); 6) `runtime.terminal(...)` immediately after the provider outcome resolves |
| SQLite owner | Same open question as T1J-R2: no current source names connection-lifetime/path ownership for a route-composed store (Question 8, unresolved) |
| Recovery owner (answers Questions 9 and 10) | `CLAIMED`-with-no-in-memory-grant after restart: no current source names an authenticated caller authorized to invoke `abandonBeforeStart`; the function exists and is CAS-guarded, but nothing in `execute/route.ts`, any CLI/MCP tree, or any scheduled job calls it. `EXECUTING`-after-restart: same gap for `resolveAmbiguousExecutingCrash`. Both functions are `NO_CURRENT_OWNER` for invocation authority, distinct from the CAS mechanism itself being sound (T1J-R2 already established the mechanism is sound; this tranche additionally confirms no caller exists for either recovery function anywhere in the current route/CLI/MCP/Execution-Plane trees) |
| Audit owner | `APPROVAL_CONSUMED` (existing, unchanged); a new terminal-outcome audit event is not currently emitted by any pending-core-aware caller (the local harness does not call `appendAuditEvent`) |
| Failure windows (crash matrix, see below) | Fully mapped; see Crash-Window Recovery Matrix |
| Duplicate-boundary risk | NONE for guard/provider (unchanged single boundaries, confirmed by the call-order table); NONE for duplicate creation (two independent mechanisms proven above) |
| Value beyond current route | Closes the `originalGuardResult` gap without any reordering risk; provides atomic claim/crash-recovery mechanics T1J-R2 already found valuable; requires zero change to existing quota/safety/role/rate-limit/approval-validation ordering |
| Smallest future manifest (only if selected ready) | Not selected ready in this tranche: two required interface members remain unresolved (SQLite connection-lifetime ownership, Question 8; recovery invocation authority, Questions 9-10) even though route ordering and payload provenance for `originalGuardResult`/`approvalId`/`approvalRequestHash`/`approvalRequestSnapshot` are now fully resolved. `normalizedIntent`/`environment`/`binding.sessionId,cwd` remain genuinely new fields requiring new, currently nonexistent builders regardless of which candidate is chosen. |

### Candidate C: create the pending record inside the approval `PATCH` transition

| Field | Value |
| --- | --- |
| Source compatibility | `EXISTING_SOURCE_INCOMPATIBLE` |
| Creation identity | Would create the record at `PATCH /api/approvals/[id]` time, using the path parameter `id` as `approvalId` |
| Payload owner (answers Question 7) | Rejected field by field: the `PATCH` handler reads only `ApprovalRequestRecord` (`[id]/route.ts` lines 66-73), whose type (`store.ts` lines 37-61) carries `requestContext?: ApprovalRequestContext` (fields: `templateName`, `intent`, `cvfPhase`, `cvfRiskLevel`, `provider`, `model`, `policySnapshotId`, `envelopeId` -- a **string** ID, not an object) and `requestSnapshot?: ApprovalRequestSnapshot` (fields: `templateId`, `templateName`, `intent`, `inputs?`, `provider?`, `model?`, `cvfPhase?`, `cvfRiskLevel?`, `knowledgeCollectionId?`, actor fields -- no `originalGuardResult`, no `GuardPolicySnapshot`-shaped field, no `normalizedIntent`, no `environment`). None of the four hardest-to-source payload fields (`normalizedIntent`, `originalGuardResult`, `environment`, `policySnapshot`) exist anywhere on the record this route boundary can read. This is not a recomputation-drift risk to be mitigated; the data is structurally absent from the type the PATCH handler has access to. |
| Gateway owner | Would require importing `runExecuteRouteMandatoryGateway` into an admin-decision handler, a second call site for a boundary otherwise owned exclusively by `/api/execute`, and one this tranche's own baseline explicitly excludes: the baseline's Candidate C definition requires proving the PATCH boundary already possesses every required input "without inventing or weakening evidence," which the field-by-field rejection above shows it cannot |
| Approval owner | `PATCH` route, unchanged for the approval-decision fact itself |
| Claim/begin/provider/terminal order | Not reachable: without `originalGuardResult`/`policySnapshot`/`normalizedIntent`/`environment`, no valid `PendingAgentExecutionImmutablePayload` can be constructed at this boundary, so `create()` itself would fail validation (`pending-agent-execution.ts` lines 645-671, in-memory store; equivalent validation in the SQLite store's `create`) |
| SQLite owner | N/A; rejected before reaching this question |
| Recovery owner | N/A; rejected before reaching this question |
| Audit owner | N/A; rejected before reaching this question |
| Failure windows | N/A; rejected before reaching this question |
| Duplicate-boundary risk | CRITICAL if attempted anyway: would require the PATCH route to either invent placeholder values for the missing fields (violating the pending core's own fail-closed validation intent) or import a second, independent guard-evaluation call, duplicating `/api/execute`'s exclusive guard/provider ownership from an unrelated admin-decision endpoint |
| Value beyond current route | None; this candidate is structurally defeated by missing data, not by a value judgment |
| Smallest future manifest | Not proposed; rejected outright per the baseline's own instruction to "prove that boundary possesses every immutable payload and policy-snapshot input without inventing or weakening evidence," which this assessment shows it does not |

### Candidate D: retain formal T1 parked because no bounded source-compatible interface can own all required inputs and recovery transitions safely

| Field | Value |
| --- | --- |
| Classification | Not selected as the terminal outcome, but closely related to the selected terminal: recorded for completeness of the mandatory four-way comparison |
| Reason not selected outright | Candidate B resolves two of the four required interface members completely (route ordering with zero reordering risk; full provenance proof for `originalGuardResult`/`approvalId`/`approvalRequestHash`/`approvalRequestSnapshot`, plus a structural, source-backed exactly-once-creation proof) and narrows the other two to two specifically named, still-open items (SQLite connection lifetime; recovery invocation authority) rather than leaving the entire interface undecided. A fully parked terminal would discard this narrowing without cause. |

## Crash-Window Recovery Matrix

| Failure point | Durable state after crash | Current source recovery owner | Disposition |
| --- | --- | --- | --- |
| Before `create()` | `ApprovalStore` record remains `'approved'` (if Candidate B's create has not yet run) or has already been deleted by the existing consume step (line 513) depending on exact ordering chosen | User must resubmit; no pending record exists to recover | Acceptable: identical to current-route behavior before any pending-runtime composition |
| After `create()`, before `claim()` | Pending record durably `CREATED` (SQLite, `synchronous = FULL`) | No current caller invokes `expirePendingExecution` or any cleanup on a stale `CREATED` record from any route/CLI/MCP path | `NO_CURRENT_OWNER` for cleanup, though the record itself is not ambiguous (a fresh `claim()` attempt is well-defined and safe per T1J-R2's CAS analysis) |
| After `claim()`, before `begin()` | Pending record durably `CLAIMED`; in-memory `ResumeAuthorityGrant` is lost on process crash (grants are process-local, non-serializable, per `pending-agent-execution.ts` lines 775-818) | `abandonBeforeStart` exists and is CAS-guarded (`LEGAL_TRANSITION_FROM.ABANDON_BEFORE_START = ['CLAIMED']`), but no current route, CLI, MCP, or scheduled-job caller invokes it | `NO_CURRENT_OWNER` for invocation authority (answers Question 9); this is the concrete, named gap that keeps the terminal from full readiness |
| After `begin()`, before provider call starts | Pending record durably `EXECUTING` | Same `resolveAmbiguousExecutingCrash` gap as `CLAIMED` above | `NO_CURRENT_OWNER` for invocation authority |
| During a live provider call, before response returns | Pending record durably `EXECUTING`; provider side effect state is unknown to CVF | `resolveAmbiguousExecutingCrash` is the only source-backed path to a terminal `UNKNOWN_TERMINAL` state, and it has no current caller | `NO_CURRENT_OWNER` for invocation authority (answers Question 10) |
| After provider response, before `terminal()` write | Pending record durably `EXECUTING`; provider response was received in-process but not yet persisted | Same gap; `resolveAmbiguousExecutingCrash` is the only correct recovery path and has no caller | `NO_CURRENT_OWNER` for invocation authority |
| After `terminal()` write | Pending record durably in a terminal status (`SUCCEEDED`/`FAILED`/`DENIED`/`UNKNOWN_TERMINAL`) | `TERMINAL_STATUSES` makes this immutable (`pending-agent-execution.ts` line 344-352, `TERMINAL_STATE_IMMUTABLE` guard in `applyPendingAgentExecutionTransition` line 607-609) | Safe by construction; no recovery action possible or needed |

**Answer to Question 9 and 10 together:** recovery is neither automatic, route-triggered, startup-triggered, nor
operator-triggered today, because no current source path calls `abandonBeforeStart` or
`resolveAmbiguousExecutingCrash` at all. The CAS mechanism these functions rely on is sound (T1J-R2's finding,
reconfirmed here), but "the mechanism exists" is explicitly distinguished from "an authorized caller exists" per
this work order's own fail condition: "recovery APIs are treated as production-owned merely because they exist."

## Question 13: Exact Negative And Concurrency Tests That Would Defeat Each Risk

| Risk | Test that would defeat it if it failed |
| --- | --- |
| Duplicate `create()` under concurrent approved resumes | Two concurrent `POST /api/execute` calls with the same valid `approvalId` after both have passed the approval-validation block; assert exactly one `create()` succeeds and the other observes `UNIQUE constraint failed` (converted to `IO_FAILURE`) or finds the `ApprovalStore` record already deleted |
| Duplicate `claim()` (grant issued twice for the same pending execution) | Two concurrent `claim()` calls on the same `pendingExecutionId`; assert exactly one receives `ok: true` with a grant and the other receives `CAS_CONFLICT` (T1J-R2 already covers this; re-asserted here as part of the complete interface) |
| Grant replay (a consumed grant reused for a second `begin()`) | Call `begin()` twice with the same `ResumeAuthorityGrant` object; assert the second call returns `FORGED_OR_CONSUMED_GRANT` (`isAuthenticUnconsumedGrant` checks `VALID_GRANTS`, which `beginPendingExecution` deletes from on first use, `pending-agent-execution.ts` lines 944-950) |
| Premature recovery (an operator or job calling `abandonBeforeStart`/`resolveAmbiguousExecutingCrash` on a record that is not actually stuck) | Attempt `abandonBeforeStart` on a record still legitimately `CLAIMED` by an in-flight, non-crashed request; assert the CAS `expectedVersion`/`expectedStatus` predicate prevents state corruption even if invoked incorrectly (mechanism-level safety); separately, assert that no current source path invokes either function automatically, so this risk is currently unrealized only because no caller exists (not because a safe caller has been built and tested) |
| Provider replay after an ambiguous crash | Simulate `EXECUTING` with no terminal write, then attempt a second `admitAndInvokeProvider`-driven attempt against the same `pendingExecutionId`/`claimId`; assert the route-level design (once a route caller exists) must check `record.state.status` and refuse to `begin()` again on an already-`EXECUTING` record rather than silently retrying (this specific negative test cannot be written today because no route caller exists to test; it is named here as the exact focused test a future T1K manifest must include) |

## Fourteen Mandatory Decision Questions

**1. What is the exact current call order from request parse through approval creation/resume, gateway, provider admission, and response?**
Recorded in full in the Current Call-Order Table above (21 steps, with every early-return condition named).

**2. Which current early returns prevent a gateway-derived `originalGuardResult` from existing at initial approval creation?**
Not an early return in the blocking sense, but a strict sequencing fact: approval issuance (step 18) is driven by `enforcement.status === 'NEEDS_APPROVAL'` (step 15-18), and `guardContext`/`runExecuteRouteMandatoryGateway` (steps 19-20, which produce `guardResult`) are constructed and called only afterward, because `guardContext` requires `resolvedExecutionRole.permissionRole` which is itself computed at step 13, and the route's own source order places the entire `enforcement`/approval-issuance block before the gateway call unconditionally. `guardResult` therefore cannot exist at approval-issuance time under the current route structure regardless of any early return; it is a strict ordering fact, not a conditional early exit.

**3. For each immutable pending payload field, which exact current owner supplies it and at what lifecycle point?**
Recorded in full in the Required-Field Provenance Table above.

**4. Is any current route-native `GuardPolicySnapshot` builder semantically identical to the pending schema? Prove or reject field by field.**
Rejected field by field; see the dedicated proof table above. No current route-native builder produces this shape.

**5. Can Candidate A move the gateway earlier without changing denial, quota, approval, audit, or provider-attempt semantics?**
Not proven safe by current source. Moving the gateway earlier would change the relative order in which quota exceedance, role-permission denial, actor-role-gate denial, and safety-filter blocking are evaluated against real guard denial for the same request, and no current source demonstrates these checks are order-independent in their externally observable response codes/bodies. This is recorded as an unresolved risk specific to Candidate A, not a defeat of the pending runtime's design.

**6. Can Candidate B create exactly one pending record during concurrent resumes, and what deterministic identity/unique constraint/CAS proves it?**
Yes, proven by two independent mechanisms: (a) the existing `ApprovalStore.delete` at line 513 already provides a single-winner pattern per T1J-R2's analysis; (b) `PendingAgentExecutionSqliteStore.create`'s `PRIMARY KEY` constraint on `pending_execution_id` (using the existing `approvalId` as the identity) independently rejects a second `create` call with the same ID inside its own transaction, converting the failure to a typed, non-silent `IO_FAILURE`. Full citation and reasoning recorded under Candidate B's "Creation identity" row.

**7. Can Candidate C's approval PATCH boundary access trustworthy normalized intent, original guard result, environment, and policy snapshot without recomputation drift?**
No. Rejected field by field in Candidate C's row above: none of these four fields exist anywhere on `ApprovalRequestRecord`, `ApprovalRequestContext`, or `ApprovalRequestSnapshot`, the only types the PATCH handler can read.

**8. Who owns SQLite path resolution, construction, close, process exit, contention, and expired-record cleanup?**
No current source names this owner for a route-composed runtime. This is the single most consequential open item carried forward unchanged from T1J-R2: every existing caller (the local harness) uses an explicit caller-supplied path and an explicit, invocation-scoped `close()`, a pattern not designed for a stateless-per-HTTP-request Next.js route handler. No module-level singleton, environment-variable convention, or default path exists anywhere in the composition or store modules (confirmed by re-search at this execution base, unchanged from T1J-R2's finding).

**9. After restart with durable `CLAIMED` but no in-memory grant, which authenticated owner may abandon or recreate work without replay?**
No current source names one. `abandonBeforeStart` exists and is CAS-guarded, but has zero non-test callers anywhere in `execute/route.ts`, the CLI tree, the MCP tree, or the Execution Plane Foundation tree (re-confirmed at this execution base). This is `NO_CURRENT_OWNER` for invocation authority, not a defect in the transition function itself.

**10. After restart with `EXECUTING`, which owner may resolve ambiguity, using what evidence and audit record?**
Same answer as Question 9, for `resolveAmbiguousExecutingCrash`: the function exists, is CAS-guarded (requires `expectedStatus: 'EXECUTING'`), and produces an auditable `UNKNOWN_TERMINAL` terminal state, but has zero current callers. No audit-event emission (`appendAuditEvent`) is wired to either recovery function anywhere in current source.

**11. Where do `APPROVAL_CONSUMED`, claim, begin, provider-attempt admission, and terminal evidence occur in the proposed order?**
Recorded in full under Candidate B's "Claim/begin/provider/terminal order" row: `create` -> `claim` -> `APPROVAL_CONSUMED` audit (existing position, unchanged) -> `begin` -> `admitAndInvokeProvider` (existing, unchanged) -> `terminal`.

**12. Does the proposed interface retain exactly one mandatory gateway and one provider-attempt admission owner?**
Yes, for Candidate B: the call-order table and Candidate B's row both confirm the existing single `runExecuteRouteMandatoryGateway` call and the existing single `admitAndInvokeProvider`-per-attempt pattern are unchanged in position and count. The pending runtime's own interface (confirmed by direct inspection of `PendingAgentExecutionComposedRuntime` in the composition module) never itself calls a guard engine or a provider.

**13. What exact negative and concurrency tests would defeat duplicate create, duplicate claim, grant replay, premature recovery, and provider replay?**
Recorded in full in the dedicated table above.

**14. Which terminal is supported, why is every alternative defeated, and what remains parked?**
`PARTIAL_READY_REQUIRES_ONE_NAMED_IMPLEMENTATION_PRECONDITION` is supported. `ROUTE_PRE_GATEWAY_PENDING_CREATION_INTERFACE_READY_FOR_T1K_DECISION` (Candidate A) is defeated because it introduces an unverified reordering risk (Question 5) on top of leaving three of four payload fields (`normalizedIntent`, `environment`, `policySnapshot`) still unbuilt, resolving strictly less than Candidate B while adding new risk. `RESUME_TIME_DETERMINISTIC_PENDING_CREATION_INTERFACE_READY_FOR_T1K_DECISION` (Candidate B) is the closest to ready and is not selected as fully ready only because two named interface members remain genuinely open in current source: SQLite connection-lifetime/path ownership (Question 8) and recovery invocation authority (Questions 9-10). Per the work order's own fail condition ("recovery APIs are treated as production-owned merely because they exist" and "connection lifetime is omitted"), these two gaps are sufficient to withhold full readiness even though route ordering, exactly-once creation, and three of the four payload fields (`approvalId`, `approvalRequestHash`, `approvalRequestSnapshot`, plus `originalGuardResult` once positioned after the gateway) are now fully resolved. `APPROVAL_PATCH_PENDING_CREATION_INTERFACE_READY_FOR_T1K_DECISION` (Candidate C) is defeated outright by the field-by-field data-absence proof (Question 7). `NO_SAFE_INTEGRATION_INTERFACE_RETAIN_FORMAL_T1_PARKED` (Candidate D) is defeated because Candidate B is not merely "not unsafe" but affirmatively resolves the majority of the required interface with source-backed proof, leaving a narrowly named remainder rather than an absence of any viable design. `BLOCKED_SOURCE_CONTRADICTION` is defeated because no binding packet fact was contradicted by this tranche's fresh re-verification; all T1J-R2 and baseline Source Verification rows are reconfirmed with zero drift. **What remains parked:** SQLite connection-lifetime/path ownership; recovery invocation authority for `abandonBeforeStart`/`resolveAmbiguousExecutingCrash`; the still-entirely-unbuilt `normalizedIntent` construction function; the `environment.deploymentBoundary` literal-compatibility gap for a production route context; and all implementation, T1K, T2, provider/live, and public/deploy authority.

## Named Implementation Precondition (For The Selected Partial-Ready Terminal)

Per the work order's terminal contract, a partial-ready terminal must name the one precondition (or, here, the small
named cluster) that blocks full readiness, without authorizing implementation:

1. **SQLite connection-lifetime and storage-path ownership decision** (Question 8): decide whether a route-composed
   `PendingAgentExecutionSqliteStore` is constructed per-request-with-explicit-close, or via a module-level singleton
   pattern (mirroring `ApprovalStore`'s own `createApprovalStore()`/`getApprovalStore()` pattern), and decide the
   storage-path resolution convention (environment variable, fixed relative path under `.data/`, or otherwise).
2. **Recovery invocation authority decision** (Questions 9-10): decide which authenticated surface (a startup
   reconciliation pass, an operator-triggered admin action, a scheduled job, or a route-level check-before-act) is
   authorized to call `abandonBeforeStart` for a stale `CLAIMED` record and `resolveAmbiguousExecutingCrash` for a
   stale `EXECUTING` record after a process restart, and what audit evidence that call must produce.

Both items are narrowly scoped, source-backed, and do not require redesigning the CAS/lifecycle mechanism itself,
which T1J-R2 and this tranche both confirm is sound. `normalizedIntent` construction and `environment` literal
compatibility remain additional, separately named open builder gaps that any future T1K manifest must also resolve,
but are not elevated to blocking preconditions here because they are net-new field construction (no existing source
claims to already solve them), whereas the two named preconditions above are genuine lifecycle/authority decisions
with no current source answer at all.

## Independent Reviewer Correction

Reviewer disposition: `ACCEPT_WITH_MATERIAL_CORRECTION`.

The selected terminal remains
`PARTIAL_READY_REQUIRES_ONE_NAMED_IMPLEMENTATION_PRECONDITION`, and
`successorTrancheOpened: NO` remains correct. The worker's Candidate B safety proof and its enumeration of the
remaining precondition are materially corrected as follows:

1. `ApprovalStore.delete()` is not a single-winner mechanism. T1J-R1 and T1J-R2 already established that two
   concurrent requests can both retain an approved in-memory record reference before either delete occurs. The
   SQLite primary key can reject a second create only if every caller uses the same deterministic
   `pendingExecutionId = approvalId`; it is the sole proposed duplicate-create barrier, not a second independent
   barrier. The route adapter must treat duplicate-create conflict as a fail-closed no-provider outcome.
2. The worker's proposed order is internally inconsistent. Current `APPROVAL_CONSUMED` audit and delete occur before
   the mandatory gateway. A pending `create()` positioned after the gateway cannot also precede that audit while
   leaving the audit at its unchanged source position. The accepted direction must explicitly move the consume audit
   to after successful deterministic create/claim, or explain a different atomic ordering; current source does
   neither.
3. Candidate B lacks more than SQLite and recovery owners. Current source has no route-native builders for
   `normalizedIntent`, full actor/session/runtime `binding`, or `GuardPolicySnapshot`. More importantly,
   `validateEnvironmentIdentity` accepts only
   `deploymentBoundary: single_process_non_production`; representing a product route honestly therefore requires an
   explicit environment contract extension, not merely construction of an existing valid object. These missing and
   incompatible payload fields are blocking interface members under the work order and cannot be demoted because
   they would be net-new code.
4. SQLite path/construction/close/cleanup ownership and authenticated recovery invocation for stale `CLAIMED` and
   ambiguous `EXECUTING` records remain open exactly as the worker found.

The one named implementation precondition is therefore:

`ACCEPTED_ROUTE_NATIVE_PRODUCTION_PENDING_EXECUTION_COMPOSITION_OWNER_CONTRACT`

That single owner contract must define, as one atomic interface: deterministic approval-bound record identity and
duplicate-create handling; complete immutable payload and policy-snapshot provenance; a truthful production-capable
environment schema; exact consume/create/claim/begin/provider/terminal audit order; SQLite path, lifetime, close and
cleanup ownership; and authenticated restart recovery with fail-closed provider replay behavior.

Candidate B remains the preferred architectural direction because it preserves the current gateway position and
reuses the accepted CAS core. It is not yet a source-compatible or implementation-ready interface. No additional
single-gap decision tranche may claim closure by resolving only one member of the owner contract above.

This correction supersedes all conflicting statements that call delete a single-winner, claim two independent
duplicate-create mechanisms, state the proposed audit order is unchanged, classify route ordering or payload
provenance as fully resolved, or list only SQLite lifecycle and recovery authority as blocking preconditions.

## Risk / Corrective Action

1. **Risk of treating Candidate B's strong creation-identity and ordering proof as sufficient for full readiness.**
   A future reviewer could read the exactly-once-creation proof and the unchanged-gateway-position proof and round up
   to a ready terminal.
   - *Mitigation:* This assessment explicitly separates "route ordering and payload provenance are resolved" from
     "SQLite lifecycle and recovery authority are resolved," and the terminal selection reflects only the former.
2. **Risk of treating `normalizedIntent`/`environment` gaps as smaller than they are.**
   These could be mistaken for simple field renames or pass-through mappings.
   - *Mitigation:* The provenance table explicitly marks both as requiring wholly new, currently nonexistent builder
     functions, not renamed existing values, and the `environment.deploymentBoundary` literal-compatibility issue is
     named as a semantic incompatibility, not a naming gap.
3. **Risk of a future implementer invoking `abandonBeforeStart`/`resolveAmbiguousExecutingCrash` without an
   authorization design, assuming their mere existence is sufficient authority.**
   - *Mitigation:* The Named Implementation Precondition section states this explicitly as a decision that must be
     made, separate from the mechanism's own soundness.

## Decision / Recommendation / Disposition

**Selected Terminal Token:** `PARTIAL_READY_REQUIRES_ONE_NAMED_IMPLEMENTATION_PRECONDITION`

**successorTrancheOpened:** NO

**Basis:**
1. Candidate B (resume-time deterministic pending creation, preserving current route ordering) is the only candidate
   that resolves route ordering with zero reordering risk, provides a two-mechanism, source-backed exactly-once
   creation proof, and closes the `originalGuardResult` payload gap by construction (created after the gateway runs).
2. Candidates A and C are both defeated on source-backed grounds specific to each: A introduces an unverified
   reordering risk while resolving strictly less of the payload than B; C is structurally impossible because the PATCH
   boundary lacks every hard-to-source payload field.
3. Two named, narrowly scoped interface members remain genuinely undecided by current source: SQLite connection-
   lifetime/path ownership, and recovery invocation authority for the two existing but uncalled recovery transition
   functions. Per the work order's own fail conditions, these gaps are sufficient to withhold full readiness.
4. `normalizedIntent` construction and `environment` literal-compatibility are additional open builder gaps recorded
   for completeness but not elevated to blocking preconditions, since they represent net-new construction work rather
   than an undecided ownership/authority question.
5. No implementation, route reordering, schema/store edit, runtime construction, or provider/live work is authorized
   by this terminal. A later T1K packet may resolve the two named preconditions and then propose an exact
   implementation manifest; that packet is not opened by this tranche.

## Evidence / Verification

- Pre-implementation autorun gate: PASS, before authoring (execution base `1e8e186d5f4739dc18e1d7726c1fde7a65975b6d`).
- Fresh execution base and clean initial status: PASS.
- Both output paths confirmed absent before authoring.
- All named source files in both packets' Source Verification Blocks read in full; `execute/route.ts` re-traced end
  to end from request parse through the provider-attempt admission block.
- Zero non-test `GuardPolicySnapshot`-shaped or `normalizedIntent`-shaped builder found anywhere in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`.
- Zero non-test caller of `abandonBeforeStart`/`resolveAmbiguousExecutingCrash` found anywhere in `execute/route.ts`,
  CLI, MCP, or Execution Plane Foundation trees.
- Provider, network, browser, credential, and live calls: 0.
- Runtime, source, test, package, and checker mutations: 0.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | assessment docType; terminal token enum; successorTrancheOpened token; Source Verification ACCEPT disposition; AOT trace label set; terminal contract tokens |
| gateRunPurpose | post-read confirmation that literal shape is correct; gates confirm rather than reveal required tokens |
| claimBoundary | structural gate success does not substitute for reviewer semantic audit; external worker output is not CVF authority until independently accepted |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated operator-mediated external decision worker; provider identity not independently attested |
| Provider or surface | local private provenance workspace; no provider/API/network/browser call |
| Session or invocation | GC010-SCR-R2-T1J-R3 external worker, 2026-08-31 |
| Working directory | repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | governed reads; `git rev-parse HEAD`; `git status --short --untracked-files=all`; `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`; `rg` searches; `python governance/compat/run_worker_return_fast_gate.py` |
| Target paths | T1J-R2 assessment; `execute/route.ts`; `[id]/route.ts`; `approvals/store.ts`; `enforcement.ts`; `web-governance-envelope.ts`; `pending-agent-execution.ts`; `pending-agent-execution-sqlite-store.ts`; `pending-agent-execution-composition.ts`; `pending-agent-execution-local-harness.ts` |
| Allowed scope source | committed T1J-R3 baseline/work order and active next-move authority at execution base `1e8e186d5f4739dc18e1d7726c1fde7a65975b6d` |
| Before status evidence | clean worktree at full HEAD `1e8e186d5f4739dc18e1d7726c1fde7a65975b6d`; both output paths absent |
| After status evidence | HEAD unchanged; both new documentation paths untracked and uncommitted |
| Diff evidence | `git diff --name-status` returns empty; `git status --short --untracked-files=all` shows exactly two new untracked documentation paths |
| Approval boundary | read-only source inspection and offline deterministic search only; no source/test edit, no provider/live/network call |
| Claim boundary | no source/test/package/script/session edit, route/store implementation, production, distributed, live, public, deploy or commit claim |
| Agent type | EXTERNAL_AGENT_CLI_MCP operator-mediated worker |
| Invocation ID | `gc010-scr-r2-t1j-r3-worker-2026-08-31` |
| Expected manifest | `docs/assessments/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` |
| Actual changed set | `docs/assessments/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | pending-runtime route-integration interface decision; read-only offline analysis |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: four candidates compared as complete interfaces; fourteen questions answered; call-order, payload-provenance, and crash-recovery matrices recorded |
| receiptEvidence | CVF_RECEIPT_PRESENT: pre-implementation PASS; clean git status |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact two-path uncommitted documentation manifest; deterministic search outputs |
| invocationBoundary | read-only local source inspection and offline checks; one operator-mediated external worker invocation; zero provider/network/browser/credential/live calls |
| interceptionBoundary | no external interception, wrapper/proxy enforcement, runtime gate, or agent coding control was created |
| claimLanguage | T1J-R3 selects a partial-ready integration interface and names its exact remaining preconditions; it does not implement, reorder, or wire any route or store |
| forbiddenExpansion | source/test/package/script/session edits; route/store implementation; provider/live; public sync; distributed; deployment; production; continuity update; commit; T1K/T2 successor dispatch |

## Epistemic Process Block

### Expected Result / Prediction

The work order predicted that a worker answer resolving only one or two of the four required interface members
(route ordering, payload provenance, SQLite lifecycle, restart recovery) must select a partial or parked terminal,
and warned against treating recovery APIs as production-owned merely because they exist, against omitting connection
lifetime, and against assuming Candidate B's ordering preservation alone proves complete readiness.

### Evidence Comparison

Route ordering and creation-identity uniqueness (two of the four members) were traced and found fully resolved for
Candidate B with two independent, source-backed mechanisms. Payload provenance was traced field by field and found
mostly resolved for existing fields but genuinely open for `normalizedIntent`/`environment`/`policySnapshot`
construction. SQLite lifecycle ownership and recovery invocation authority (the remaining two members) were traced
and found to have zero current source answer, matching the work order's explicit warning not to treat recovery APIs
as owned merely because they exist.

### Contradiction Or Gap Disposition

No contradiction was found with T1J-R2's findings; this tranche extends them into a complete four-member interface
decision. The gap this tranche identifies and narrows (specifically: which two named items, not a general "durable
owner decision," block full readiness) is more precise than T1J-R2's framing, consistent with this tranche's mandate
to resolve the complete cluster in one pass rather than reopen single-gap loops.

### Claim Update

Narrowed further. Route ordering and creation-identity uniqueness are now fully resolved with source-backed proof.
SQLite lifecycle ownership and recovery invocation authority remain the two specific, named open items. No
implementation is authorized. T2 remains held.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_2026-08-31.md` | `Status: DISPATCH_READY` | PASS |
| Worker return | `docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md` | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Baseline state | `docs/baselines/CVF_GC018_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_2026-08-31.md` | `Status: READY_FOR_DISPATCH` | PASS |
| Exact two-path manifest | this assessment and its paired worker return | `git status --short --untracked-files=all` shows exactly these two untracked paths | PASS |
| Terminal and successor flag | this document's Decision section | `PARTIAL_READY_REQUIRES_ONE_NAMED_IMPLEMENTATION_PRECONDITION`; `successorTrancheOpened: NO` | PASS |
| Reviewer closure | N/A with reason: reviewer closure is a separate, independent action not performed by this worker | pending independent review | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision-only reconciliation; no public artifact or export authority is included.

## Finding-To-Governance Learning Disposition

NOT_APPLICABLE_WITH_REASON: this tranche reconciles existing accepted T1J-R2 evidence and current source into a
complete four-member interface decision. No recurring defect class was identified in this decision tranche.

## Claim Boundary

This assessment compares four pending-runtime route-integration candidates as complete interfaces, answers fourteen
mandatory questions, and selects one allowed terminal token. It does not close or edit the roadmap, reorder or
implement any route, construct or migrate any store, invoke a provider, emit production audit, prove distributed
safety, sync public artifacts, deploy, open production, commit, or authorize an automatic T1K or T2 successor
tranche.
