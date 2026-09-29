# CVF GC010 SCR-R2-T0A Agent Execution API Cross-Owner Contract Decision

Memory class: governed-decision-assessment

docType: baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: GC010-SCR-R2-T0A

Date: 2026-08-30

Worker: delegated no-commit decision worker

## Purpose

Decide one exact, source-compatible cross-owner contract for an isolated Web
Agent Execution API system chain, or state precisely why no such contract can
be adopted yet, without implementing any part of the chain. This assessment
answers the eighteen required decision questions from
`docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_2026-08-30.md`
and selects exactly one terminal token.

## Source / Predecessor Evidence

- Paired baseline: `docs/baselines/CVF_GC018_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_2026-08-30.md`.
- Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_2026-08-30.md`.
- Prior roadmap: `docs/roadmaps/CVF_GC010_SINGLE_CONSUMER_SYSTEM_CHAIN_PRODUCT_ROADMAP_2026-08-30.md` (T0 `CLOSED_PASS_BOUNDED`, `NO_VIABLE_CONSUMER_RETAIN_PARKED`).
- Prior decision completion: `docs/reviews/CVF_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_COMPLETION_2026-08-30.md`.
- executionBaseHead: `6d5f17548` (captured fresh at worker start; `git status --short` was clean).

## Scope / Methodology

Fresh direct reads of every named runtime/package/route source at
executionBaseHead, plus two exact `rg` searches over
`EXTENSIONS/CVF_GUARD_CONTRACT` and
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`. No provider, network,
browser, credential, or runtime mutation occurred. No file outside the two
worker-owned output paths was written.

## Current Runtime Freshness Verification

Commands run at executionBaseHead `6d5f17548`:

```
git rev-parse --short HEAD
rg -n "AgentExecutionRuntime|ApprovalExecutionBridge|admitAndInvokeProvider|appendAuditEvent" EXTENSIONS/CVF_GUARD_CONTRACT EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src -g "*.ts"
rg -n "agent-execution" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api EXTENSIONS/CVF_GUARD_CONTRACT/package.json EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts -g "*.ts" -g "*.json"
```

Classification of every non-test hit:

| Hit class | Disposition |
| --- | --- |
| `AgentExecutionRuntime` class definition and internal `approvalBridge?` field in `agent-execution-runtime.ts` | ACCEPT: only construction/definition site; no other file imports or constructs `AgentExecutionRuntime` |
| Two `ExecutionProvider` provider docstrings (`alibaba-dashscope-provider.ts`, `gemini-provider.ts`) that mention "Implements the `ExecutionProvider` interface from AgentExecutionRuntime" | ACCEPT: comment-only reference; neither file imports or wires `AgentExecutionRuntime` itself, and neither is a registered route caller |
| `ApprovalExecutionBridge`/`createApprovalExecutionBridge` in `approval-execution-bridge.ts` and re-exported from `src/index.ts` (lines 363-372) | ACCEPT: package-exported, but the bridge is not the same authority as the Web approval store; no cvf-web caller imports it |
| `admitAndInvokeProvider` used only inside `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (two call sites) | ACCEPT: confirms `/api/execute` is the sole owner of provider-attempt admission |
| `appendAuditEvent` used across many `cvf-web` route/lib files (approvals, execute, admin, etc.) | ACCEPT: confirms Web's durable audit owner is broadly reused; no agent-execution-specific caller exists |
| Second search for `agent-execution` across `cvf-web/src/app/api`, `CVF_GUARD_CONTRACT/package.json`, `CVF_GUARD_CONTRACT/src/index.ts` | ACCEPT: zero matches; no `agent-execution` route file, export entry, or package export exists at executionBaseHead |

No newly discovered owner requires reclassification. The dispatcher's Source
Verification Block claims (AER not package-exported; Web owns admission,
audit, and approval persistence; `/api/execute` is an independent accepted
chain) are all reconfirmed current.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| AER composes guard engine, provider, and an optional in-memory approval bridge | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `preCheck` (lines 188-228), `execute` (233-346), `run` (377-391), `runAwaitingApproval` (398-432) | `AgentExecutionRuntime` | Guard Contract runtime | ACCEPT |
| Approval bridge settles exactly once via an in-memory `Map`, no persistence | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/approval-execution-bridge.ts` | `request` (57-98), `settle`/`settleInternal` (100-144); `private readonly pending = new Map` (line 47) | `ApprovalExecutionBridge` | Guard Contract | ACCEPT |
| Web approval state is persistent (file-backed outside test) and exposed through GET/PATCH | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts`; `.../approvals/[id]/route.ts` | `FileBackedApprovalStore` (118-122), `createApprovalStore` (124-131); `GET`/`PATCH` handlers | approval record owner | cvf-web | ACCEPT |
| Web attempt helper pairs admission and invocation exactly once per candidate call | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` | `admitAndInvokeProvider` (352-379); `recordProviderCallStart` (161-175) | named function | cvf-web | ACCEPT |
| Web audit store is durable, retention-managed evidence owner | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | `appendAuditEvent` (143-156); `appendEvent`/`_eventAdapter.append` (116-132) | `appendAuditEvent` | cvf-web | ACCEPT |
| `/api/execute` is already an independent accepted chain that owns its own approval consumption, admission, and audit | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `POST` (99-964); approval consumption (183-268); admission (782-810, 859-864); audit (multiple sites) | `POST` | cvf-web | ACCEPT |
| AER has no active package export | package | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | `exports`/`files` fields (package.json 8-35); full barrel (index.ts 1-408) | absent export | Guard Contract package | ACCEPT |
| No `agent-execution` route, export, or package entry exists anywhere in current source | runtime/package | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/**`; `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | fresh `rg -n "agent-execution"` returned zero hits | absent route/export | none | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths | `test -f` returned absent for both the assessment and worker-return paths immediately before authoring | ACCEPT |
| Proposed route `POST /api/agent-execution` | fresh `rg -n "agent-execution"` across cvf-web `api`, Guard Contract `package.json`, and `src/index.ts` returned zero hits; the route does not exist | ACCEPT |
| Duplicate-chain boundary | `/api/execute/route.ts` was read in full and is untouched by this worker; no edit was made to it or its gateway/admission/reconciliation chain | ACCEPT |

## Candidate Comparison Contract

### Candidate 1: synchronous `POST /api/agent-execution` waiting on `ApprovalExecutionBridge`

| Field | Value |
| --- | --- |
| Trigger | a new route handler that constructs `AgentExecutionRuntime` per request and calls `runAwaitingApproval` |
| AER factory/export | none exists; would require a new factory and a new package export entry in `src/index.ts` and `package.json` |
| Engine owner | a freshly constructed `GuardRuntimeEngine` (via `createGuardEngine`), reused as-is |
| Approval creation | `ApprovalExecutionBridge.request` inside the same process |
| Approval decision/resume | a human reviewer would need a synchronous settlement call (`bridge.settle`) issued from a second concurrent request or admin action while the first HTTP request is still open |
| Provider adapter | a new `ExecutionProvider` implementation wired to the AER constructor, distinct from `admitAndInvokeProvider` |
| Attempt ledger | none; AER's `execute` calls `this.provider.execute` directly with no admission step, so this design would call a provider without prior attempt admission unless a new adapter layer is added |
| Durable audit | none; AER's `executionLog` is in-memory only and lost when the process/request ends |
| Response mapper | would need to be authored from scratch; no current mapper translates `ExecutionResult`/`ExecutionStatus` into an HTTP response |
| Cancellation/timeout/restart | `ApprovalExecutionBridge` supports timeout/abort via `AbortSignal`, but a Next.js request has its own timeout and no restart semantics; a pending approval that outlives the HTTP request has no bridge instance to resolve into, because the bridge is held in-memory in the request's closure and cannot be resolved by a separate `PATCH` call |
| Identity mapping | AER's `RuntimeConfig` accepts `sessionId`/`cwd`/`environment`/`agentId`, but nothing in Web session/service-token identity is currently mapped onto these fields |
| Duplication risk | HIGH: this design would stand up a second, parallel provider-attempt/audit/approval pipeline beside `/api/execute`'s, with no shared admission ledger or shared durable audit store unless explicitly wired in |
| Smallest future manifest | new route file, new AER factory/export, new `ExecutionProvider` adapter calling `admitAndInvokeProvider`, new response mapper, and a redesigned approval mechanism because the in-memory bridge cannot survive the HTTP request/response boundary |
| Verdict | REJECTED as currently specifiable: the in-memory bridge cannot resolve across two separate HTTP requests (submit, then approve), which is the normal human-approval shape; this design either blocks the HTTP connection open indefinitely waiting for an approval that has nowhere durable to be decided, or it silently reduces to "approve within the same request," which defeats the purpose of human-in-the-loop approval |

### Candidate 2: asynchronous submit/pending plus approval decision/resume using the Web approval store/API and an adapter into AER

| Field | Value |
| --- | --- |
| Trigger | a new `POST /api/agent-execution` route for submission, reusing the existing `GET`/`PATCH /api/approvals/[id]` handlers for the decision step |
| AER factory/export | none exists; would require a new factory and export, same gap as Candidate 1 |
| Engine owner | `createGuardEngine()` (existing factory in `src/index.ts`, lines 394-408), reused as-is |
| Approval creation | the existing `getApprovalStore().set(...)` persistence mechanism (`approvals/store.ts`), the same one `/api/execute` already uses at lines 521-549 of `route.ts` |
| Approval decision/resume | the existing `PATCH /api/approvals/[id]` handler remains decision-only. A separate authenticated resume request must present the approval id plus the identical bound execution payload; approval mutation must not itself start a provider call. |
| Provider adapter | a new `ExecutionProvider` implementation whose `execute` method internally calls `admitAndInvokeProvider` from `provider-attempt-admission.ts`, so admission and call-start accounting are reused rather than reinvented |
| Attempt ledger | `createProviderAttemptLedger` plus `admitAndInvokeProvider`, the same functions `/api/execute` already uses; a new call site, not a new mechanism |
| Durable audit | `appendAuditEvent` (`control-plane-events.ts`), the same durable, retention-managed store `/api/execute` and the approvals route already write to |
| Response mapper | must be newly authored to translate AER's `ExecutionStatus` (`PENDING`/`RUNNING`/`COMPLETED`/`FAILED`/`BLOCKED`/`NEEDS_APPROVAL`) into HTTP status/body without inventing a success claim; no current mapper exists for this |
| Cancellation/timeout/restart | resume happens through a separate fresh authenticated execution request after approval decision. `ApprovalExecutionBridge` is not used. Approval expiry is reusable, but restart-safety is not yet proved: the current approval store is file-backed outside tests yet its persistence method catches write failures, and its schema does not carry a complete pending AER execution or atomic execution claim. |
| Identity mapping | the existing actor-binding functions cover actor/org/team/auth mode only. A new bound pending-execution record must also preserve normalized intent, request/session/agent identity, cwd, environment, file scope, build authority, original guard decision, guard/policy fingerprint, approval id, and attempt/audit linkage. |
| Duplication risk | MEDIUM until a durable atomic claim exists. Reusing shared functions avoids duplicate mechanisms, but concurrent resume requests can still double-invoke unless one pending execution is claimed exactly once before provider admission. A raw call to public `execute(intent, synthesizedAllow)` is also an authority-bypass risk, not a valid no-duplication technique. |
| Smallest future manifest | (1) AER export/factory; (2) a bound pending-execution contract/store with explicit persistence-failure behavior; (3) an atomic claim/consume operation; (4) a safe resume-authority adapter that accepts a validated immutable approval artifact rather than a caller-supplied `ALLOW`; (5) a Web `ExecutionProvider` adapter calling `admitAndInvokeProvider`; (6) isolated submit and resume route handlers, while existing approval PATCH remains decision-only; (7) response/audit mapping; (8) focused concurrency, stale-binding, guard-fingerprint, persistence-failure, denial, timeout and terminal-audit tests. |
| Verdict | PARTIALLY VIABLE: the product boundary and reusable owners are nameable, but the durable pending-execution, safe resume-authority and atomic-claim interfaces do not exist. This is a bounded design direction, not implementation readiness. |

### Candidate 3: no safe cross-owner contract, retain parked

| Field | Value |
| --- | --- |
| Trigger | none; this candidate proposes no new trigger |
| AER factory/export | not created |
| Engine owner | not applicable |
| Approval creation | not applicable |
| Approval decision/resume | not applicable |
| Provider adapter | not applicable |
| Attempt ledger | not applicable |
| Durable audit | not applicable |
| Response mapper | not applicable |
| Cancellation/timeout/restart | not applicable |
| Identity mapping | not applicable |
| Duplication risk | NONE; nothing is built |
| Smallest future manifest | none; the historical four-fact reopen condition from the prior roadmap remains the controlling gate for any future attempt |
| Verdict | This candidate is the fallback if Candidate 2's bounded missing contract set cannot be closed coherently: AER export/factory, durable complete pending-execution binding, fail-closed persistence, atomic claim, safe resume authority, response mapping, and terminal audit wiring. Because those gaps are exactly nameable rather than open-ended, Candidate 3 is not selected, but none may be waved away as already solved. |

## Eighteen Required Decision Questions

**1. What user/product outcome justifies a separate Agent Execution API?**
The operator instruction and this committed T0A packet supply the product requirement: continue the system-chain program with an isolated programmatic Agent Execution API rather than modify the accepted template-oriented `/api/execute` chain. Current source does not yet prove adoption, UI demand, or runtime use, so the value claim remains a product hypothesis until a later bounded use proof. Operator intent is authority for the design question; it is not evidence that the route already exists.

**2. Is the registered route itself a sufficient trigger, and what request contract invokes it?**
No route is registered. Per the Mandatory Invariants ("a new export/factory without a registered trigger is not a consumer"), the absence of a registered `POST /api/agent-execution` route means no trigger currently exists. If one were created, its request contract would need at minimum: `intent`/`userInput` (mapped to `ParsedIntent` via `parseIntent`), an actor/session identity (mapped to `RuntimeConfig.agentId`/`sessionId`), and a `channel` value (`RuntimeConfig.channel` is typed `'web' | 'ide' | 'cli' | 'mcp' | 'api'`, so `'api'` is already a valid literal for this exact use case).

**3. Why must this remain distinct from `/api/execute`?**
`/api/execute` is explicitly out of scope for modification (work order Forbidden Scope: "any change to the accepted `/api/execute` chain"). It also encodes a different execution model (single-turn template prompt against `executeAI`/vision adapters) than AER's `parseIntent -> preCheck -> execute -> postCheck` pipeline, which is designed around a free-text `userInput` and a pluggable `ExecutionProvider`. Merging them would require reworking `/api/execute`'s accepted contract, which is forbidden. Keeping them distinct avoids double guard evaluation and double provider-attempt admission on the same request.

**4. Which exact factory constructs AER and where should it be exported?**
No factory exists today. `AgentExecutionRuntime`'s constructor (`agent-execution-runtime.ts`, lines 154-162) takes `(guardEngine, provider, config)` directly; there is no `createAgentExecutionRuntime(...)` helper analogous to `createGuardEngine` (`src/index.ts`, lines 394-408) or `createApprovalExecutionBridge` (`approval-execution-bridge.ts`, lines 172-176). A future factory would need to be added to `agent-execution-runtime.ts` and exported from `src/index.ts` plus given a `package.json` `exports` entry, matching the pattern already used for `./runtime/approval-execution-bridge`.

**5. Which current GuardRuntimeEngine configuration is reused?**
`createGuardEngine()` from `src/index.ts` (lines 394-408), which registers the full hardened default guard stack (`AiCommitGuard`, `PhaseGateGuard`, `RiskGateGuard`, `AuthorityGateGuard`, `BuildAuthorityGuard`, `MutationBudgetGuard`, `FileScopeGuard`, `ScopeGuard`, `AuditTrailGuard`). This is the same factory recommended for "both Web UI and MCP Server" per its own docstring, so no new engine configuration is needed.

**6. How is Web actor/role/phase/risk mapped into `RuntimeConfig`?**
No current mapping exists for AER specifically. `/api/execute` has its own adapter, `buildWebGuardContext` (`@/lib/guard-runtime-adapter`, used at `route.ts` line 578), which maps Web session/role into a `GuardRequestContext` for the mandatory gateway, not into `RuntimeConfig`. A new agent-execution route would need an analogous mapping function translating `session.role`/`session.userId`/`body.cvfPhase`/`body.cvfRiskLevel` into `RuntimeConfig.role`/`agentId`/`phase`/`riskLevel`/`sessionId`. This is a real, nameable gap, not an invented one.

**7. How are requestId, sessionId, agentId, approvalId, attempt index, audit event, and response linked?**
Partially resolvable from existing pieces, not fully wired: `preCheck` generates `requestId` internally (`agent-execution-runtime.ts` line 211, `exec-${Date.now()}-...`); `RuntimeConfig.sessionId`/`agentId` are settable at construction; the Web approval store's `id` field is the `approvalId` and is already bound to an actor via `submittedByActorId`/`submittedByAuthMode` (`approval-binding.ts`); `ProviderAttemptLedger.attempts[].attemptIndex` already exists in `provider-attempt-admission.ts`; `appendAuditEvent`'s `payload` field is a free-form `Record<string, unknown>` that can carry all of the above. No current code links AER's `requestId` to a Web `approvalId` or to a `ProviderAttemptLedger`; a new adapter would need to persist this linkage (for example, in an audit payload or a small pending-execution record keyed by `approvalId`).

**8. Can the in-memory bridge safely survive the HTTP approval lifecycle?**
No. `ApprovalExecutionBridge`'s `pending` map (`approval-execution-bridge.ts` line 47, `private readonly pending = new Map()`) is held in the JavaScript process's memory and is scoped to whatever object holds the `ApprovalExecutionBridge` instance. A Next.js API route handler returns its HTTP response before a human can review and decide on a separate request; nothing in the route lifecycle keeps a per-request bridge instance alive to receive a later `settle()` call from a different request context (and a module-scoped singleton bridge would not know which pending map entry belongs to which still-open HTTP connection, because the HTTP connection itself does not stay open across the approval wait in a synchronous design). This confirms Candidate 1 is not viable as specified.

**9. If not, what smallest adapter contract connects the Web approval store to AER without a second authority source?**
The smallest safe adapter does not use `ApprovalExecutionBridge` for the Web-facing flow. Submit performs the one planned guard evaluation and writes both (a) the existing Web approval record and (b) a separate immutable pending-execution record containing the normalized intent, complete identity/binding fields, original guard decision, and a guard/policy fingerprint. Approval PATCH remains decision-only. A later authenticated resume request must re-check actor, request hash, approval status/expiry and the recorded guard/policy fingerprint, then atomically claim the pending execution. Only a validated internal resume grant may reach AER/provider execution; a caller-supplied or synthesized `ALLOW` passed to public `execute()` is forbidden. If policy/guard fingerprints drift, persistence failed, binding changed, or the record was already claimed, resume fails closed before provider admission. `ApprovalExecutionBridge` remains limited to future same-process callers.

**10. Does submit/resume re-evaluate guards, and if so how is duplicate evaluation prevented?**
The design records one guard evaluation at submit and does not blindly run it again on resume. Resume instead validates the immutable original decision plus a current guard/policy fingerprint. Drift makes the approval stale and requires a fresh submission; it never converts stale evidence into `ALLOW`. This differs from the existing `/api/execute` flow, which recomputes enforcement on the resumed request before consuming approval and then still runs its mandatory gateway. Therefore `/api/execute` lines 498-513 are not evidence that raw enforcement can be skipped, and no future packet may cite them that way.

**11. How is approval bound to unchanged intent, cwd, environment, actor, and session?**
Two binding mechanisms exist and must be composed without declaring either complete. The bridge hash covers command, parameters, cwd, environment, actor and session but is in-memory. The Web snapshot/hash persists actor and request fields but does not cover every AER authority field or the guard decision/fingerprint. A future pending-execution schema must preserve the union of required fields under one versioned digest and re-verify it on resume. The current Web approval record alone is insufficient for this claim.

**12. Which `ExecutionProvider` adapter calls `admitAndInvokeProvider` exactly once?**
None exists today. `AgentExecutionRuntime.execute` (lines 233-346) calls `this.provider.execute(intent.action, intent.parameters)` directly with no admission step; the only current `ExecutionProvider` implementation is `DryRunProvider` (lines 139-144), which does not call `admitAndInvokeProvider` either. A future adapter's `execute` method would need to construct a `ProviderAttemptLedger` (via `createProviderAttemptLedger`) and call `admitAndInvokeProvider` internally, wrapping whatever real provider call it makes, so that AER's single call to `this.provider.execute` corresponds to exactly one admission-checked attempt.

**13. How are denied attempts guaranteed to start zero provider calls?**
By construction of `admitAndInvokeProvider` (`provider-attempt-admission.ts`, lines 352-379): admission is checked first (`admitProviderAttempt`), and only on `admission.admitted === true` does the function proceed to `recordProviderCallStart` and `params.invoke()`. A denied admission returns immediately via `params.onDenied(...)` without ever calling `invoke`. If a future `ExecutionProvider` adapter's `execute` method routes its real call through this exact function (as required by Q12), this invariant carries over automatically; it is not carried over automatically by AER itself, because AER's own `execute` method has no admission concept.

**14. How are thrown/rejected invocation, timeout, abort, cancellation, restart, and stale approval reconciled?**
- Thrown/rejected invocation: AER's `execute` already has a `try/catch` (lines 302-345) that produces a `FAILED` `ExecutionResult`; if the adapter's `execute` throws inside `admitAndInvokeProvider`'s own `try/catch` (lines 366-378), that inner catch already builds a `buildProviderInvocationErrorResponse`-shaped result, but AER's outer catch expects a thrown error from `this.provider.execute`, not a `NextResponse`, so the adapter must re-throw or return a value AER's catch can turn into `FAILED` - this composition detail is unresolved and belongs in the future T1 manifest.
- Timeout: `ApprovalExecutionBridge` has a `setTimeout`-based timeout (lines 79-81), but per Q8 this bridge is not used in the Web HTTP adapter; the Web-side timeout equivalent is the approval store's `expiresAt` field, already checked and converted to `status: 'expired'` in `/api/execute` (lines 240-253) - an agent-execution resume path must apply the same expiry check before calling `execute()`.
- Abort/cancellation: `ApprovalExecutionBridge.request` accepts an `AbortSignal` (lines 90-95); this is relevant only to a future non-HTTP (same-process) caller, not the Web HTTP adapter, which has no open connection to abort during the pending-approval window.
- Restart/persistence: the Web approval store is file-backed outside tests, but `persist()` catches write failures and the schema carries no atomic pending-execution claim. It is a reusable approval owner, not proof of durable exactly-once execution. A future store contract must fail closed on persistence/claim failure and prove restart/concurrency behavior.
- Stale approval: the existing hash/actor-binding checks in `approval-binding.ts` (already used by `/api/execute` at lines 196-238) must be re-run by the agent-execution resume path before calling `execute()`, exactly as `/api/execute` already does for its own approvals.

**15. Which durable audit events are appended for every terminal status?**
None are appended today for any AER-originated execution; `AgentExecutionRuntime.execute`/`executionLog` is purely in-memory (lines 152, 325, 343). A future adapter must call `appendAuditEvent` (`control-plane-events.ts`, lines 143-156, the same durable, SIEM-forwarding, retention-managed store `/api/execute` and the approvals route already use) at minimum for: `COMPLETED`, `FAILED`, `BLOCKED`, and `NEEDS_APPROVAL` terminal `ExecutionResult.status` values, plus the eventual resumed terminal outcome after approval decision. No current code does this; it is a named future-manifest item, not an existing owner.

**16. What HTTP status/body maps each AER terminal status without inventing success?**
No current mapper exists. A future response mapper would need, at minimum: `COMPLETED` -> 200 with `output`; `FAILED` -> 500 with `error`; `BLOCKED` -> 400 or 403 with `guardDecision.blockedBy`; `NEEDS_APPROVAL` -> 409 with `approvalId` (mirroring `/api/execute`'s existing 409 `NEEDS_APPROVAL` pattern at lines 550-573); `PENDING`/`RUNNING` are not currently produced by `execute()` (only by external log/status readers) and should not be mapped to an HTTP success code if ever surfaced. This mapper does not exist in source and must not be assumed solved.

**17. What is the exact smallest future T1 write and focused test manifest?**
The ultimate implementation manifest is bounded below, but the corrected review requires a fresh T0B contract/schema decision to freeze items 6-8 before any T1 implementation packet can open:

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` - add a `createAgentExecutionRuntime(...)` factory function (new code, no behavior change to the existing class).
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` - export the new factory and `AgentExecutionRuntime`/`RuntimeConfig`/`ExecutionResult`/`ExecutionProvider` types.
3. `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` - add an `exports`/`files` entry for the runtime module, matching the existing `./runtime/approval-execution-bridge` pattern.
4. A new cvf-web adapter file (for example, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/agent-execution-provider-adapter.ts`) implementing `ExecutionProvider` and internally calling `admitAndInvokeProvider`.
5. A new cvf-web route file (for example, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/agent-execution/route.ts`) for `POST` submit, reusing `buildApprovalActorBinding`/`computeApprovalRequestHash`/`getApprovalStore()` from the existing approvals module and `appendAuditEvent` from `control-plane-events.ts`.
6. A versioned pending-agent-execution record/store carrying the full binding, original guard decision and guard/policy fingerprint, with fail-closed persistence semantics.
7. An atomic claim/consume operation and a separate authenticated resume route/helper; the existing approval PATCH remains decision-only.
8. A safe internal resume-authority API that rejects raw/synthesized `ALLOW` and stale fingerprints before provider admission.
9. A new response-mapping helper translating `ExecutionResult`/`ExecutionStatus` to HTTP status/body per Q16.
10. Focused tests: one submit guard evaluation; stale guard/policy fingerprint fails closed; forged `ALLOW` is impossible/rejected; concurrent double resume yields one claim and at most one provider call; persistence failure starts zero calls; exactly-one admission per actual call; denied admission starts zero calls; durable audit for every terminal status; changed binding and expired approval cannot resume.

This manifest is complete only after a fresh T0B freezes the pending-record,
claim, and resume-authority contracts and a later operator-authorized T1 packet
reopens implementation. This assessment opens neither successor.

**18. Which terminal token is supported and what evidence defeats the alternatives?**
`PARTIAL_READY_REQUIRES_APPROVAL_ADAPTER` is supported. `READY_FOR_T1_ASYNC_AGENT_EXECUTION_CHAIN` is defeated because AER export/factory, complete bound pending-execution persistence, safe resume authorization, atomic claim/idempotency, response mapping and terminal audit wiring remain absent. Full parking is defeated because the operator-selected product boundary and reusable source owners are now exact enough for a bounded successor contract tranche. `BLOCKED_SOURCE_CONTRADICTION` is defeated because the corrected decision preserves every verified source fact. The token means architecture direction only, not implementation readiness.

## Findings / Position

Terminal decision: `PARTIAL_READY_REQUIRES_APPROVAL_ADAPTER`.

Candidate 2 (asynchronous submit/pending plus separate approval decision and
authenticated resume) is the only design that can reuse the existing guard,
approval, admission, audit and actor-binding owners without modifying
`/api/execute`. Its missing interfaces include AER export/factory, complete
pending-execution binding/persistence, safe resume authority, atomic claim,
response mapping and terminal audit wiring. A raw direct call to
`execute()` with a synthesized `ALLOW` is expressly rejected. These are
precise and small, not open-ended. `ApprovalExecutionBridge` is confirmed
unusable as the Web-facing approval authority because its `pending` map is
process-memory-only and cannot survive the HTTP submit/decide request
boundary (Q8-Q9). This tranche does not open T1; a fresh operator-authorized
work order is required to implement the manifest in Q17.

## Risk / Corrective Action

The primary risk is a future implementer treating `ApprovalExecutionBridge`
or the current Web approval record as sufficient for the Web HTTP lifecycle.
The former is process-memory-only; the latter lacks the complete AER binding,
guard/policy fingerprint, and atomic execution claim and does not prove
fail-closed persistence. The corrective action is to require a fresh T0B to
freeze the Q8-Q11 pending-record and safe-resume contracts before T1. The Web
approval store remains the approval-decision authority;
`ApprovalExecutionBridge` remains reserved for a future same-process non-HTTP
caller only.

A secondary risk is inventing a provider-attempt admission path that does not
route through `admitAndInvokeProvider`, which would create a second,
unreconciled attempt-counting mechanism beside `/api/execute`'s. The
corrective action is the Q12/Q17 requirement that any new `ExecutionProvider`
adapter's `execute` method internally calls `admitAndInvokeProvider`.

## Decision / Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Terminal token | `PARTIAL_READY_REQUIRES_APPROVAL_ADAPTER` |
| Reviewer consideration | authorized; does not open T1 |
| successorTrancheOpened | NO |
| Missing exact interfaces | AER factory/export; versioned pending-execution binding/store; fail-closed persistence; safe resume-authority adapter; atomic claim/idempotency; separate resume route; provider adapter; response mapper; terminal audit wiring |

## Mandatory Invariants Reconciliation

| Invariant | Status under Candidate 2 |
| --- | --- |
| One guard evaluation per logical execution, including resume | Satisfied by design only when submit records the decision and resume validates binding plus unchanged guard/policy fingerprint; stale evidence fails closed and raw synthesized `ALLOW` is forbidden |
| One approval authority and exactly-once settlement | Satisfied by design: Web approval store is the sole authority (Q9); `ApprovalExecutionBridge` is not used for this chain |
| Binding changes fail closed before provider invocation | Partially designed: existing actor/hash checks are reused, but a new union binding and guard/policy fingerprint are mandatory because the current snapshot is incomplete |
| One admission record before each actual provider call | Satisfied by design only if the future `ExecutionProvider` adapter calls `admitAndInvokeProvider` (Q12-Q13); AER itself does not do this today |
| Denied admission starts zero provider calls; admitted attempt starts at most one | Satisfied by `admitAndInvokeProvider`'s existing construction (Q13), if reused as required |
| Every terminal path has durable audit projection and truthful response | Not yet implemented; named as future-manifest items (Q15-Q16) |
| `/api/execute` is neither wrapped nor duplicated | Satisfied: no edit was made to `/api/execute/route.ts`; Candidate 2 reuses shared library functions, not the route itself |
| A new export/factory without a registered trigger is not a consumer | Satisfied: this assessment does not create any export, factory, or route |

## Evidence / Verification

- executionBaseHead `6d5f17548`; `git status --short` clean at worker start.
- Two exact `rg` searches reproduced above with full non-test hit classification.
- Full reads of `agent-execution-runtime.ts`, `approval-execution-bridge.ts`, `engine.ts` (partial, factory/registration section), `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`, `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`, `approvals/store.ts`, `approvals/[id]/route.ts`, `approvals/approval-binding.ts`, `provider-attempt-admission.ts`, `control-plane-events.ts`, and `execute/route.ts` in full.
- Zero provider/network/browser/credential calls were made while producing this assessment.
- This worker made no runtime, package, route, test, checker, workflow, or `/api/execute` edit.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `docs/assessments/` classified as `baseline` doc type by `_classify` in the structural completeness checker (path prefix match), requiring source/predecessor-evidence, decision/baseline/proposed-tranche, and evidence/verification section groups; `## Agent Operation Trace Block` required label set (`Actor` through `Deletion or rename disposition`); `## Delta Execution Claim Boundary Control Block` required field set and accepted enum tokens (`CLAIM_REJECTED`, `N/A with reason`, `CLAIM_REJECTED_NO_RECEIPT`, `CLAIM_REJECTED_NO_ACTION`); `## Public Export Disposition` allowed tokens (`EXPORTED`, `DEFERRED_PRIVATE_ONLY`, `BLOCKED_MISSING_PUBLIC_ARTIFACTS`) |
| gateRunPurpose | confirmation evidence after direct checker-source inspection, not first discovery |
| claimBoundary | shape and source-fact readiness only; this block makes no independent semantic-acceptance claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated no-commit decision worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | GC010-SCR-R2-T0A worker execution, 2026-08-30 |
| Working directory | repository root |
| Command or tool surface | direct file reads, `rg`, `git rev-parse`/`git status`, `test -f` |
| Target paths | all files listed in Evidence / Verification above, plus this assessment and the paired worker return |
| Allowed scope source | work order Worker Autonomy / No-Question Rule and Scope sections |
| Before status evidence | executionBaseHead `6d5f17548`; `git status --short` clean; both output paths absent |
| After status evidence | this assessment and the paired worker return created; no other path changed |
| Diff evidence | `git diff --name-status` (empty prior to authoring; two new untracked files after) |
| Approval boundary | decision-only; no runtime, route, package, test, checker, or workflow change |
| Claim boundary | architecture decision and gap analysis only; no runtime behavior, export, route, provider, or approval settlement is implemented or claimed |
| Agent type | delegated worker |
| Invocation ID | `gc010-scr-r2-t0a-worker-2026-08-30` |
| Expected manifest | `docs/assessments/CVF_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_2026-08-30.md`; `docs/reviews/CVF_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_WORKER_RETURN_2026-08-30.md` |
| Actual changed set | the same two paths; no other path was created, modified, or deleted |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred in this tranche |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only cross-owner contract decision; no runtime behavior |
| claimDisposition | CLAIM_REJECTED: no execution-control, governed-coding-control, interception, or runtime-enforcement claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is produced by this decision |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: only file reads, exact `rg`/`git` searches, and two documentation outputs occurred |
| invocationBoundary | no route, provider, or adapter is invoked, created, or registered |
| interceptionBoundary | no wrapper, proxy, or mandatory runtime control is implemented or proposed as already active |
| claimLanguage | proposed design, source-compatible decision, and named future-manifest gaps only |
| forbiddenExpansion | runtime/package/Web mutation, provider/live, public, deploy, production, and automatic T1 opening remain out of scope of this decision |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private decision-only system-chain dispatch; no public artifact,
runtime behavior, or release claim is authorized by this assessment.

## Claim Boundary

This assessment records a documentation-only architecture decision. It
selects `PARTIAL_READY_REQUIRES_APPROVAL_ADAPTER`, names the full missing
contract set (AER export/factory, bound pending persistence, safe resume
authority, atomic claim, provider adapter, response and audit), and states a future
manifest. It does not create an API, export `AgentExecutionRuntime`, connect
approval systems, call a provider, open T1, or claim live, public,
deployment, or production readiness. `successorTrancheOpened: NO`.
