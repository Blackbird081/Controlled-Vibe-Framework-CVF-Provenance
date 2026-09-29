# CVF GC010 SCR-R2-T1J-R1 Assessment - Approval Resume Product Caller Correction

Memory class: governed-worker-assessment

docType: assessment

Status: COMPLETE_PENDING_REVIEW

Batch ID: GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION

Date: 2026-08-31

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md`

executionBaseHead: `1d04a8fadd834bb67d0d70673354b6e09fd4337b`

successorTrancheOpened: NO

Selected terminal: `PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION`

## Purpose

Correct T1J's missed evidence about the approval UI (`ApprovalInbox`), the
approval-decision route (`PATCH /api/approvals/[id]`), and the approval-bound
resume primitive already present inside `POST /api/execute`. Determine whether
this concrete, registered product surface justifies an isolated
pending-execution/AER consumer, whether it instead proves that a pending-
execution consumer would be duplicative of `/api/execute`'s existing resume
primitive, whether one exact interface/owner decision remains, or whether no
source-backed caller exists at all.

## Target / Source

- T1J prior assessment (corrected here): `docs/assessments/CVF_GC010_SCR_R2_T1J_REGISTERED_PRODUCTION_INVOCATION_OWNER_AND_INVOKED_PATH_COMPOSITION_DECISION_2026-08-31.md`
- Approval inbox UI: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ApprovalInbox.tsx`
- Approval pages: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/admin/approvals/page.tsx`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/approvals/page.tsx`
- Approval decision route: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts`
- Approval store: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts`
- Execute route approval-resume block: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Processing screen: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`
- Pending-agent-execution core: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`
- Pending-agent-execution composition/store: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts`

## Scope / Methodology

Worker captured clean execution base `1d04a8fadd834bb67d0d70673354b6e09fd4337b`
(confirmed by `git rev-parse HEAD`; `git status --short --untracked-files=all`
returned empty). Both output paths were confirmed absent before authoring.
Pre-implementation autorun gate passed before authoring.

Worker read the T1J-R1 baseline and work order, the prior T1J assessment in
full (specifically its Questions 3 and 12, which are the rows this rework
corrects), and every source file named in the work order's Source
Verification Block, in full: `ApprovalInbox.tsx`, both approval pages, the
`PATCH`/`GET` approval-decision route, the approval store's persistence
implementation, the complete approval-resume validation block inside
`POST /api/execute`, `ProcessingScreen.tsx`'s execution and approval-submission
callbacks, and the pending-agent-execution core's `claimPendingExecution` and
drift-check logic. This assessment performs read-only source reconciliation;
it makes zero source, test, roadmap, or session-state edits and zero
provider/network/browser/credential/live calls.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `ApprovalInbox` is a registered, mounted production UI, not a stub | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ApprovalInbox.tsx` | lines 79-110, 293-299 | `loadRequests`; `handleAction`; `ApprovalInbox` | approval inbox component | ACCEPT |
| Two registered pages mount the inbox | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/admin/approvals/page.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/approvals/page.tsx` | full file | `ApprovalInbox` import/mount | admin and dashboard approval pages | ACCEPT |
| `PATCH /api/approvals/[id]` decides and audits but never triggers execution | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | lines 57-119 | `PATCH`; `APPROVAL_DECIDED` | approval decision route | ACCEPT |
| `POST /api/execute` implements approval-bound resume validation but does not provide atomic, exactly-once consumption | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 184-267 (validation), 482-512 (audit/delete) | `body.approvalId`; `approvalRecordMatchesActor`; `getApprovalStore().delete` | `POST` | ACCEPT_WITH_REVIEWER_CORRECTION: status read and deletion are separate operations, so concurrent requests can both pass validation |
| Approval store is already durable (file-backed with atomic write) outside test env, not in-memory-only | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | lines 63-137 | `ApprovalStore`; `FileBackedApprovalStore`; `persist()` | approval store | ACCEPT |
| `ProcessingScreen` stores the returned `approvalId` but its execute-request body never includes it on any subsequent call | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | lines 125, 159-174, 260 | `approvalRequestId`; `executeReal` request body | `ProcessingScreen` | ACCEPT |
| Pending-execution core provides claim-concurrency-safe (`CREATED`-status-gated) approval consumption with drift/staleness detection | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | lines 737, 834, 888-909 | `ApprovalRecordLookup`; `claimPendingExecution`; `evaluateDriftChecks` | pending execution core | ACCEPT |
| T1J's prior assessment concluded no product caller exists, missing this evidence | accepted assessment (corrected) | `docs/assessments/CVF_GC010_SCR_R2_T1J_REGISTERED_PRODUCTION_INVOCATION_OWNER_AND_INVOKED_PATH_COMPOSITION_DECISION_2026-08-31.md` | Questions 3 and 12 | no-caller finding | prior T1J | ACCEPT (superseded by this correction) |

## What T1J Missed, Precisely

T1J's Question 3 ("Is an isolated new route justified by a concrete product caller?") and Question 12 ("What product
caller or operator surface invokes the new trigger?") concluded no source-backed product caller existed, because the
searches performed were limited to `AgentExecutionRuntime`/`buildPendingAgentExecutionRuntime` construction sites and
route registrations, and did not trace the separately-named approval UI, the approval-decision route, or the
already-built approval-resume block inside `/api/execute`. That block is real, registered, and reachable today by any
authenticated approval-submitting user. T1J's conclusion that "no caller exists for a second agent-execution
endpoint" remains correct on its own narrow terms (nothing calls `buildPendingAgentExecutionRuntime` from any route),
but it did not test the separate, more specific question this rework answers: whether the approval-resume *user flow*
is itself a concrete product caller that would justify composing AER/pending-execution into the resume path.

## Traced End-To-End Flow (Current Source, No Inference)

1. User submits a template execution. `POST /api/execute` runs enforcement; on `NEEDS_APPROVAL` it auto-creates a
   durable, actor-bound, request-hash-bound approval record in the file-backed `ApprovalStore`
   (`route.ts` lines 515-546) and returns `approvalId` in the response body (line 559).
2. `ProcessingScreen.executeReal` receives that response, extracts `data.approvalId`, and stores it in
   `approvalRequestId` React state (line 260) and renders an "approval submitted" panel (lines 594-626). **No control
   in this component re-invokes `/api/execute` with that stored ID.** There is no "Retry" or "Resume" button wired to
   `executeReal` with `{ ...originalBody, approvalId: approvalRequestId }`.
3. Separately, an admin opens `/admin/approvals` or `/home/approvals` (dashboard), both of which mount
   `ApprovalInbox`. The admin clicks Approve/Reject, which `PATCH`es `/api/approvals/[id]` (`ApprovalInbox.tsx` line
   98). The `PATCH` handler (`route.ts` lines 57-119) flips `record.status` to `'approved'`/`'rejected'`, appends an
   `APPROVAL_DECIDED` audit event, and returns. **It does not call `/api/execute`, does not read `approvalRequestHash`
   against a live execution payload, and has no knowledge of the pending-agent-execution core.**
4. The only way the approved execution actually resumes today is a *new* client request to `POST /api/execute` that
   includes `approvalId` in its JSON body, reconstructing the exact same `templateId`/`templateName`/`inputs`/`intent`
   originally submitted (so `computeApprovalRequestHash` matches). No current UI component constructs and sends that
   request. The end-to-end resume is server-primitive-complete but UI-flow-incomplete.

## Required Candidate Comparison (4/4)

### Candidate 1: existing `/api/execute` approval-ID resubmission with smallest UI resume affordance, no AER/pending-runtime composition

| Field | Value |
| --- | --- |
| Classification | `EXISTING_SOURCE_COMPATIBLE` |
| Exact product caller | `ProcessingScreen` (or a new lightweight "Resume" control reachable from the approval-status panel / `ApprovalInbox` history row), re-invoking the existing `executeReal` request path |
| Request owner | `ProcessingScreen.executeReal`, extended to include `approvalId: approvalRequestId` in its POST body when present, and to re-run on an explicit user resume action rather than only on initial mount |
| Approval binding | Already fully implemented: `approvalRecordMatchesActor`, `requestHash` equality against `computeApprovalRequestHash`, expiry check, `status === 'approved'` check (`route.ts` lines 196-265) |
| Guard owner | The route's single existing `runExecuteRouteMandatoryGateway` boundary (line 594 in the T1J-cited freshness search); unchanged, exercised exactly once per request as today |
| Provider/admission owner | The route's single existing `admitAndInvokeProvider` boundary; unchanged |
| Durable owner | The already-durable, file-backed `ApprovalStore` (`FileBackedApprovalStore`, atomic write-rename) for the approval decision itself; the route's own existing reconciliation/receipt path for the execution outcome |
| Response/failure owner | The route's own existing response builder and diagnostic mapping; unchanged |
| Duplicate-boundary risk | NONE new. This candidate adds zero new guard, admission, provider, or audit boundary; it reuses the single existing pipeline exactly as `/api/execute` already does for a first-time (non-approval) request |
| Value beyond current route | Closes the missing caller behavior (UI never resubmits `approvalId`) while preserving the existing guard/provider pipeline; however, production-safe completion also requires an atomic consumption decision rather than only a client change |
| Smallest future manifest | One UI change in `ProcessingScreen.tsx` (and/or `ApprovalInbox.tsx`) plus a focused UI test, and one durable-owner decision selecting either atomic claim/CAS in the existing approval store or narrow composition of the pending runtime's already-implemented CAS lifecycle. No new route is justified by current evidence. |

### Candidate 2: isolated approval-resume route using `buildPendingAgentExecutionRuntime` and `PendingAgentExecutionSqliteStore`, invoked from the existing approval UI

| Field | Value |
| --- | --- |
| Classification | `NO_CURRENT_OWNER` |
| Exact product caller | Would require `ApprovalInbox` (or a new resume surface) to call a new route instead of, or in addition to, `PATCH /api/approvals/[id]` |
| Request owner | Proposed only: a new route importing `buildPendingAgentExecutionRuntime`, constructing a fresh `PendingAgentExecutionSqliteStore`-backed runtime, and driving `claim`/`begin`/`terminal` |
| Approval binding | Proposed: would reuse the pending core's `ApprovalRecordLookup` and `evaluateDriftChecks`, which duplicates (does not compose with) the validation already performed inline in `/api/execute`'s `body.approvalId` block  -  the two approval-validity checks are structurally parallel, not shared |
| Guard owner | Proposed only; would need its own guard boundary, since it must not call `runExecuteRouteMandatoryGateway` (that would duplicate GC-009's boundary for an unrelated route) |
| Provider/admission owner | Proposed only; would need its own admission boundary independent of `admitAndInvokeProvider`, or risk a second admission boundary running for what is logically the same approved request |
| Durable owner | `PendingAgentExecutionSqliteStore`, a second durable store distinct from the already-durable `FileBackedApprovalStore`; two durable stores would now separately track overlapping lifecycle state for the same logical approval |
| Response/failure owner | Proposed only |
| Duplicate-boundary risk | HIGH if implemented as a second route with its own guard/provider pipeline. The source does not prove that narrow lifecycle composition inside the existing route must duplicate guard or provider admission, so that narrower option remains part of the durable-owner decision. |
| Value beyond current route | The pending core's `claimPendingExecution` does add one real capability the current route lacks: `CREATED`-status-gated, single-claimant consumption of the approval-to-execution transition (see Anti-Duplication analysis below for the narrow TOCTOU window this closes). This value is real but narrow, and is achievable without a new route (see Candidate 1's future-manifest note and the Question 6 answer below) |
| Smallest future manifest | Not proposed. The isolated-route composition duplicates guard/admission/durable ownership for no caller need that Candidate 1 cannot already serve; its one genuine incremental capability (atomic claim) does not by itself justify a second pipeline |

### Candidate 3: approval-decision route (`PATCH /api/approvals/[id]`) directly triggers execution

| Field | Value |
| --- | --- |
| Classification | `EXISTING_SOURCE_INCOMPATIBLE` |
| Exact product caller | `ApprovalInbox.handleAction`, already registered and already calling this route |
| Request owner | Would require `PATCH /api/approvals/[id]` itself to reconstruct an `ExecutionRequest` and invoke the guard/provider pipeline synchronously inside the decision handler |
| Approval binding | The decision route currently has no access to the original execution request body beyond what `ApprovalRequestRecord.requestSnapshot`/`requestContext` stores; reconstructing a full `ExecutionRequest` from that snapshot is possible but was never designed for this route |
| Guard owner | Would require importing and invoking `runExecuteRouteMandatoryGateway` (or an equivalent) from inside an admin-decision handler, a second call site for the same boundary |
| Provider/admission owner | Would require importing `admitAndInvokeProvider` (or equivalent) into the decision route, meaning an admin's approve click directly triggers a real provider call synchronously inside the PATCH request/response cycle |
| Durable owner | Would fork receipt/audit ownership between the decision route and the execute route for what should be one logical resume |
| Response/failure owner | The PATCH response would now have to carry execution outcome (success/fail/output) in addition to approval-decision outcome, conflating two distinct response contracts |
| Duplicate-boundary risk | CRITICAL, and additionally unsafe by design: coupling an admin's approve/reject decision directly to synchronous provider execution removes the actor/session separation between "who approved this" and "who is charged/attributed for the provider call," and forces every admin decision click to block on a live provider round-trip. This is explicitly assessed as unsafe (see Question 8 below), independent of duplication concerns |
| Value beyond current route | None; this candidate makes the product worse (admin UX blocks on execution latency; actor-attribution semantics degrade) while adding no capability `/api/execute`'s own resume path lacks |
| Smallest future manifest | Not proposed; rejected on safety grounds, not merely on duplication grounds |

### Candidate 4: retain parked

| Field | Value |
| --- | --- |
| Classification | `RETAIN_PARKED_WITH_REASON` |
| Product caller | The mounted approval UI is real, but no implementation is authorized in this tranche |
| Reason | Formal T1 remains parked at a partial-ready decision boundary: a second route is rejected, while atomic claim ownership inside the existing route remains undecided |

## Ten Mandatory Decision Questions

**1. Which current UI initiates execution and which UI decides approval?**
`ProcessingScreen.executeReal` (invoked from the template-execution flow) initiates execution via `POST /api/execute`. `ApprovalInbox` (mounted at `/admin/approvals` and the dashboard `/approvals` page) decides approval via `PATCH /api/approvals/[id]`. These are two distinct, unconnected UI surfaces.

**2. Does any current UI resubmit `/api/execute` with the approved ID?**
No. `ProcessingScreen` stores `approvalRequestId` in state (line 125, set at line 260) but its `/api/execute` POST call site (`executeReal`, lines 159-174) never reads `approvalRequestId` back into the request body. The separate exported `useExecute` hook also POSTs to `/api/execute` without an approval ID, but current source has no non-test consumer of that hook. No inspected UI call site resubmits the approved ID. This is the exact missing behavior T1J did not evaluate.

**3. Does the existing execute route already provide the complete resume product behavior, or only a server-side primitive without caller completion?**
Only a server-side validation primitive without caller completion or atomic consumption. The validation block (lines 184-267: existence, hash-binding, actor-binding, expiry, `approved`-status check) is present, but the later audit/delete block (lines 496-513) is not a compare-and-swap boundary. What is missing is both a UI that constructs and sends the resume request and an explicit durable owner for safe single-claim consumption.

**4. What user/operator outcome is missing after approval today?**
After an admin approves a request in `ApprovalInbox`, the original submitting user has no UI path to actually resume their execution. The approval record sits in `'approved'` status in the durable store until it expires (24 hours) unless the user is somehow made to resend the exact original request body plus `approvalId` through some means outside the traced UI (e.g., manual API call). This is a real, product-relevant completion gap.

**5. Can that outcome be completed by a small existing-route UI change without creating an AER consumer?**
Yes. `ProcessingScreen` already has every value it needs (`approvalRequestId`, and the original `templateId`/`templateName`/`inputs`/`intent`/`executionOverrides` in its own props/closure) to construct and send `{ ...originalRequestBody, approvalId: approvalRequestId }` to the same `/api/execute` endpoint it already calls. No new route, adapter, or runtime import is required.

**6. What incremental product value would the pending runtime provide: durable recovery, claim/concurrency control, exactly-once terminal state, or none?**
Durable recovery for the *approval record itself* is already provided by the existing `FileBackedApprovalStore` (file-backed, atomic write-rename), so the pending runtime adds no new capability there. The one real incremental value is claim/concurrency control: `claimPendingExecution` gates on `record.state.status !== 'CREATED'` before allowing consumption, closing the narrow window in `/api/execute` between its early `status !== 'approved'` check (line 255) and its later `getApprovalStore().delete(...)` call (line 512), during which two concurrent resume requests carrying the same `approvalId` could both pass validation before either deletes the record. This is a real, narrow race-condition risk in the current route, not a hypothetical one. It does not by itself justify a second pipeline: the same protection can be added to the existing route by moving or duplicating the delete-as-lock earlier (an in-route fix), without adopting the pending runtime's separate store and lifecycle.

**7. If isolated composition is selected, name the exact caller, trigger, construction/import, guard, approval, provider/admission, durable store, response and failure owners.**
Not selected in this tranche (Candidate 2 rejected for readiness). If a future tranche found the narrow race-condition risk insufficiently addressable in-route, the exact owners would be: caller = a new resume-specific route or the existing `/api/execute` extended to construct `buildPendingAgentExecutionRuntime`; construction/import = `pending-agent-execution-composition.ts`; guard = would require a dedicated non-duplicating boundary decision (not resolved here); approval = pending core's `ApprovalRecordLookup`/`claimPendingExecution`; provider/admission = would require a dedicated non-duplicating boundary decision (not resolved here); durable store = `PendingAgentExecutionSqliteStore`; response/failure = not designed. This full topology is not authorized or needed by this tranche's findings.

**8. Would approval-route-triggered execution improperly couple an admin decision to provider effects or actor identity?**
Yes. Triggering execution synchronously from `PATCH /api/approvals/[id]` (Candidate 3) would force an admin's approve click to block on a live provider round-trip, and would conflate "who reviewed and approved this request" (the admin, `session.userId` in the PATCH handler) with "who is attributed for the provider call and its cost" (the original submitting user, tracked via `approvalActor`/`submittedByActorId` in `/api/execute`). The current design correctly keeps these separate: the PATCH route only ever touches `reviewedBy`/`reviewComment`, never `provider`/`model`/execution attribution.

**9. How is duplicate guard/admission/provider invocation prevented?**
In the selected Candidate 1, by construction: the resume request is just another call into the same single `POST /api/execute` handler that already owns exactly one `runExecuteRouteMandatoryGateway` call and exactly one `admitAndInvokeProvider` call per attempt (unchanged from T1J's freshness verification). No second boundary is introduced. The one identified residual risk (the narrow TOCTOU window between the status check and the delete, Question 6) exists in current source today regardless of this tranche's outcome, and its narrowest fix is moving the consumption/lock earlier in the same route  -  not composing a second pipeline.

**10. Which terminal is supported, and why is each alternative defeated?**
`PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION` is supported. A concrete product caller and resume interface are source-backed, but the current approval store exposes only independent `get`/`set`/`delete` operations and the route consumes approval after a non-atomic validation interval. The next decision must choose whether atomic claim belongs in the existing approval store/route or whether the already-built pending-runtime CAS lifecycle should be composed narrowly inside the existing route without adding a second guard/provider pipeline. `APPROVAL_RESUME_CALLER_READY_FOR_T1K_IMPLEMENTATION_DECISION` is premature until that ownership decision is made. `EXISTING_EXECUTE_RESUME_MAKES_AER_CONSUMER_DUPLICATIVE_RETAIN_PARKED` is defeated because narrow lifecycle composition has not been shown duplicative and supplies a real missing concurrency property. `NO_SOURCE_BACKED_CALLER_RETAIN_FORMAL_T1_PARKED` is defeated by the mounted approval UI and missing resume action. `BLOCKED_SOURCE_CONTRADICTION` is defeated because the source is consistent; it exposes an unresolved design choice rather than a contradiction.

## Anti-Duplication And Value-Beyond-Existing-Route Proof

| Risk/Value Question | Current-source evidence | Resolution |
| --- | --- | --- |
| Does a visible approval UI automatically justify AER/pending-execution? | `ApprovalInbox` only PATCHes approval status; it never calls `/api/execute` or any pending-execution symbol | No. The UI's existence proves a product need for *resume completion*, not for a second runtime |
| Does AER/pending-execution add guard value `/api/execute` lacks? | `/api/execute` owns the only real `GuardRuntimeEngine`-backed boundary (`runExecuteRouteMandatoryGateway`) on any invoked production path; the pending core never invokes a live guard engine itself | No incremental guard value |
| Does AER/pending-execution add provider/admission value `/api/execute` lacks? | `/api/execute` owns the only real `ExecutionProvider`-invoking, `admitAndInvokeProvider`-admitted boundary; the pending core has no provider call at all | No incremental provider/admission value |
| Does AER/pending-execution add durable value `/api/execute`'s approval path lacks? | `FileBackedApprovalStore` already persists approval records atomically to disk outside test env | No incremental durability value for the approval record itself |
| Does AER/pending-execution add any value at all? | `claimPendingExecution`'s `CREATED`-status gate closes a real, narrow TOCTOU window between `/api/execute`'s status check (line 255) and its delete (line 512) | Yes, one narrow concurrency-safety value exists, addressable in-route without adopting a second pipeline |
| Would composing AER/pending-execution into the resume path duplicate a boundary? | A separate route with its own guard/admission would duplicate boundaries; narrow claim/lifecycle composition inside `/api/execute` could retain the route's single guard and provider-admission owners | Separate-route duplication is proven; narrow in-route composition remains undecided |

## Risk / Corrective Action

1. **Risk of treating a real UI surface as automatic AER justification.**
   The presence of `ApprovalInbox` and its two mounted pages could be
   misread as proof that AER/pending-execution is needed.
   - *Mitigation:* This assessment traces the inbox's actual network calls
     (`GET /api/approvals`, `PATCH /api/approvals/[id]`) and shows neither
     touches AER, the pending-execution core, or `/api/execute`. The real
     gap is a client-side wiring omission on an already-complete server
     primitive.
2. **Risk of under-crediting the narrow concurrency gap found in `/api/execute`.**
   A future reviewer could dismiss the TOCTOU window between the approval
   status check and the store delete as immaterial.
   - *Mitigation:* This assessment names the exact two line ranges
     (line 255 check, line 512 delete) and states plainly that this is a
     real, narrow, addressable-in-route risk, not a fabricated one, while
     still concluding it does not justify a second pipeline.
3. **Risk of re-opening T1J's rejected Candidate 3 pattern under a different name.**
   A future proposal could reframe "approval-route-triggered execution" as
   safe if scoped narrowly.
   - *Mitigation:* Question 8's actor/attribution and latency-coupling
     analysis is recorded as a standing safety objection independent of the
     duplication analysis, so a narrower future proposal must still address
     it directly rather than relying on this tranche's silence.

## Decision / Recommendation / Disposition

**Selected Terminal Token:** `PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION`

**successorTrancheOpened:** NO

**Basis:**
1. A concrete, registered product caller and gap were found and are source-backed: users approved via `ApprovalInbox`
   have no UI path to resume execution, because `ProcessingScreen` never resubmits the stored `approvalId` to
   `/api/execute`.
2. `/api/execute` already owns approval validation and the single guard/provider pipeline, but its separated
   status-read and later delete do not establish exactly-once consumption under concurrency.
3. A second route with parallel guard/admission ownership would be duplicative. Current source does not establish
   that narrow pending-lifecycle composition inside the existing route would duplicate those boundaries.
4. The pending core's durable CAS claim is a real missing property. Simply deleting earlier is not an equivalent
   proven fix because a later pre-provider failure could consume the approval without a defined retry/rollback state.
5. Therefore one bounded durable-owner decision remains: extend the existing approval store with atomic claim and
   recovery semantics, or compose the pending runtime's lifecycle inside the existing route while retaining the
   route's guard/provider owners. No implementation successor opens automatically.

## Independent Reviewer Correction

The reviewer rejects the worker's `EXISTING_EXECUTE_RESUME_MAKES_AER_CONSUMER_DUPLICATIVE_RETAIN_PARKED` selection.
The worker correctly found the UI gap and TOCTOU race, but then contradicted that evidence by calling the route
"exactly-once-consumed" and by treating an early delete as an already-resolved substitute for CAS lifecycle. The
reviewer also corrected the absolute claim that no other component calls `/api/execute`: `useExecute.ts` contains a
second call site, although no current non-test source consumes that hook and it likewise sends no approval ID. The
accepted terminal is `PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION`; `successorTrancheOpened`
remains `NO`.

## Evidence / Verification

- Pre-implementation autorun gate: PASS, before authoring (execution base `1d04a8fadd834bb67d0d70673354b6e09fd4337b`).
- Fresh execution base and clean initial status: PASS.
- Both output paths confirmed absent before authoring.
- All named source files read in full: `ApprovalInbox.tsx`, both approval pages, `[id]/route.ts`, `store.ts`,
  `execute/route.ts` (approval blocks), `ProcessingScreen.tsx`, `pending-agent-execution.ts` (claim/drift logic).
- Provider, network, browser, credential, and live calls: 0.
- Runtime, source, test, package, and checker mutations: 0.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | assessment docType; terminal token enum; successorTrancheOpened token; Source Verification ACCEPT disposition; AOT trace label set; terminal contract tokens |
| gateRunPurpose | post-read confirmation that literal shape is correct; gates confirm rather than reveal required tokens |
| claimBoundary | structural gate success does not substitute for reviewer semantic audit; external worker output is not CVF authority until independently accepted |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated operator-mediated external decision worker; provider identity not independently attested |
| Provider or surface | local private provenance workspace; no provider/API/network/browser call |
| Session or invocation | GC010-SCR-R2-T1J-R1 external worker, 2026-08-31 |
| Working directory | repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | governed reads; `git rev-parse HEAD`; `git status --short --untracked-files=all`; `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`; `rg` searches; `python governance/compat/run_worker_return_fast_gate.py` |
| Target paths | `docs/assessments/CVF_GC010_SCR_R2_T1J_...2026-08-31.md`; `ApprovalInbox.tsx`; approval pages; `[id]/route.ts`; `store.ts`; `execute/route.ts`; `ProcessingScreen.tsx`; `pending-agent-execution.ts` |
| Allowed scope source | committed T1J-R1 baseline/work order and active next-move authority at execution base `1d04a8fadd834bb67d0d70673354b6e09fd4337b` |
| Before status evidence | clean worktree at full HEAD `1d04a8fadd834bb67d0d70673354b6e09fd4337b`; both output paths absent |
| After status evidence | HEAD unchanged; both new documentation paths untracked and uncommitted |
| Diff evidence | `git diff --name-status` returns empty; `git status --short --untracked-files=all` shows exactly two new untracked documentation paths |
| Approval boundary | read-only source inspection and offline deterministic search only; no source/test edit, no provider/live/network call |
| Claim boundary | no source/test/roadmap/session edit, route/package/provider/audit implementation, production, distributed, live, public, deploy or commit claim |
| Agent type | EXTERNAL_AGENT_CLI_MCP operator-mediated worker |
| Invocation ID | `gc010-scr-r2-t1j-r1-worker-2026-08-31` |
| Expected manifest | `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md` |
| Actual changed set | `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md`; `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | approval-resume product caller correction to T1J; read-only offline analysis |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: four candidates compared; ten questions answered; anti-duplication and value-beyond-existing-route proof recorded |
| receiptEvidence | CVF_RECEIPT_PRESENT: pre-implementation PASS; clean git status |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact two-path uncommitted documentation manifest; deterministic search outputs |
| invocationBoundary | read-only local source inspection and offline checks; one operator-mediated external worker invocation; zero provider/network/browser/credential/live calls |
| interceptionBoundary | no external interception, wrapper/proxy enforcement, runtime gate, or agent coding control was created |
| claimLanguage | T1J-R1 corrects T1J's missed evidence and selects a terminal; it does not implement, export, or register any topology |
| forbiddenExpansion | source/test/roadmap edits; package/export; route/provider/audit implementation; live; public sync; distributed; deployment; production; continuity update; commit; successor dispatch |

## Epistemic Process Block

### Expected Result / Prediction

The work order's rework envelope predicted that the missed approval UI and resume-path evidence could either justify
an isolated pending-execution consumer, prove such a consumer duplicative of the existing route, leave one interface
decision open, or leave no caller at all  -  and specifically warned against both defaulting to "UI exists therefore
AER has value" and against repeating T1J's no-caller conclusion without addressing the named evidence.

### Evidence Comparison

- A concrete product caller and gap were found (Question 4): confirmed, ruling out the "no caller" branch.
- AER/pending-execution's guard, provider/admission, and approval-durability value were each traced and found absent
  or already provided by the existing route/store: confirmed.
- One narrow, real incremental value (claim-concurrency safety) was found. Whether it is owned by an extended
  approval store or narrow pending-runtime composition is not resolved by current source.
- Approval-decision-route-triggered execution (Candidate 3) was found unsafe on actor-attribution and latency-coupling
  grounds, independent of duplication: confirmed and extends the prediction.

The actual evidence matches the prediction's partial-ready branch: the resume interface is concrete, while durable
claim ownership remains a bounded open decision.

### Contradiction Or Gap Disposition

No contradiction was found between this tranche and T1J's prior route/pipeline findings (guard, admission, and
provider ownership on `/api/execute` are unchanged and reconfirmed). The correction is additive: T1J's conclusion
that no caller exists for a *new AER/pending-execution-invoking route* remains valid; this tranche adds the separate,
previously untested finding that a real caller exists for *resume completion on the existing route*. Whether that
route should compose the pending lifecycle narrowly is the remaining decision.

### Claim Update

Updated by reviewer. The approval-resume product need is source-backed, but formal T1 is not yet satisfied because
the safe single-claim durable owner has not been selected. No AER/pending-execution topology or implementation is
authorized automatically. T2 remains held.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision-only reconciliation; no public artifact or export authority is included.

## Finding-To-Governance Learning Disposition

Defect class: WORKER_EXECUTION_ERROR (prior T1J tranche)

Learning lane: DOCUMENTATION_ONLY_LEARNING

Disposition: RULE_EXISTS

Reason: T1J's freshness-verification searches were scoped to construction-site and route-registration symbols and did
not extend to separately-named UI and approval-decision surfaces named in a prior accepted assessment (T1I's own
Source Verification Block already named `ProcessingScreen`/approval binding evidence). The existing source-verification
and freshness-recomputation rules already require tracing every named evidence surface; no new standard is justified
by this single occurrence.

## Claim Boundary

This assessment corrects T1J's missed approval-UI and resume-primitive evidence, compares four candidates against
that evidence, and selects one allowed terminal token. It does not close or edit the roadmap, register a production
trigger, wire a route, invoke a provider, emit production audit, prove distributed safety, sync public artifacts,
deploy, open production, commit, or authorize an automatic successor tranche.
