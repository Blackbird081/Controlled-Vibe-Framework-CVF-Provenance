# CVF GC-009/GC-010 Production Caller T1 Interface Design Audit

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-07-25

Batch ID: GC009-GC010-PCALLER-T1I

executionBaseHead: `2956af3e4`

contextPreservingMethodName: `checkContext`

receiptAdapterShape: full `GatewayResult` summary in the durable audit payload,
with the currently representable decision projected into the Web evidence
receipt.

## Purpose

Specify, without implementation, the smallest source-backed interface and Web
adapter contract that lets a future execute-route composition evaluate one
already-built `GuardRequestContext` exactly once through `MandatoryGateway`,
fail closed without bypass, and project a secret-safe result into the existing
Web receipt and durable audit seams.

## Scope / Target / Owner Boundary

This audit answers the eight design questions in the committed T1I work order.
It changes no source, runtime, test, package, checker, session, roadmap,
provider, public, or deployment surface. The proposed method, adapter, owner,
and tests remain documentation-only. T1 runtime composition and T2-T4 remain
`HOLD_*`.

## Source Inventory

| File | Action | Source fact used |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | FULL_READ | active mode, next move, and parked checkpoints |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | FULL_READ | compact current routing |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | SOURCE_VERIFIED | active handoff and T1I dispatch state |
| `AGENT_HANDOFF_V52_2026-07-25.md` | FULL_READ | active handoff boundary |
| `docs/reference/guard_orientation/README.md` | FULL_READ | worker and governed-artifact guard map |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal and worker-return shape controls |
| `docs/baselines/CVF_GC018_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | FULL_READ | T1I authority and documentation-only scope |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | FULL_READ | worker contract and eight questions |
| `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | FULL_READ | T1I/T1-T4 lifecycle state |
| `docs/audits/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_2026-07-25.md` | FULL_READ | accepted preferred-owner and interface-gap findings |
| `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` | FULL_READ | independent T0A acceptance and corrective actions |
| `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | FULL_READ | paired gap status and close condition |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | FULL_READ | current gateway config, method, result, and audit behavior |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | FULL_READ | canonical request and pipeline-result fields |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | SOURCE_VERIFIED | engine preserves `context.requestId` and stores the passed context |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | SOURCE_VERIFIED | current co-located gateway test seam |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | SOURCE_VERIFIED | current direct evaluation and pre-provider ordering |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts` | FULL_READ | exact Web context builder output |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | FULL_READ | receipt input and construction seam |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | SOURCE_VERIFIED | Web receipt and governance-trace field set |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | FULL_READ | durable audit event shape and storage path |
| `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | FULL_READ | active owner and resolved tombstone distinction |
| checker paths named by the work order | SOURCE_VERIFIED | output headings, read-ahead fields, trace fields, no-commit proof, and ASCII discipline |

## Current Source Facts

| Fact | Source evidence | Disposition |
|---|---|---|
| `GatewayResult` stores `requestId`, `blockedBy`, and `escalatedBy` only under optional `evidence` | `mandatory-gateway.ts:36-49,163-176` | ACCEPT |
| Current `check` accepts a narrower request and creates a new ID | `mandatory-gateway.ts:80-90,122-137` | ACCEPT |
| Current gateway bypass uses substring matching | `mandatory-gateway.ts:95-107` | ACCEPT |
| Current gateway calls the engine once on its locally built context | `mandatory-gateway.ts:139-140` | ACCEPT |
| Engine result copies `context.requestId` and its audit entry stores the same context object | `engine.ts:82-136` | ACCEPT |
| Canonical context has fourteen fields including mutation, scope, and trace fields absent from current `check` input | `types.ts:93-110` | ACCEPT |
| Web builder returns the canonical context before route evaluation | `guard-runtime-adapter.ts:86-129`; `route.ts:562-578` | ACCEPT |
| Execute route currently calls the shared engine directly | `route.ts:561,578` | ACCEPT |
| `buildEvidenceReceipt` constructs and returns a receipt object | `web-governance-envelope.ts:241-280` | ACCEPT |
| `buildEvidenceReceipt` has no typed gateway request-ID, allowed, bypassed, control-mode, blocked-by, or escalated-by fields | `web-governance-envelope.ts:55-78`; `ai/types.ts:131-157` | ACCEPT |
| `appendAuditEvent` persists a `UnifiedAuditEvent` whose payload accepts a record | `control-plane-events.ts:28-39,96-152` | ACCEPT |
| Execute route is an active GC-023 owner | file-size registry `activeOwners`, lines 42-47 | ACCEPT |
| The prior 1001-line route exception is `RESOLVED` and supplies no usable cap | file-size registry exception entry, lines 159-172 | ACCEPT |

## Proposed Doc-Only Interface Contract

The exact public sibling method is:

```ts
checkContext(context: GuardRequestContext): GatewayResult
```

Its required behavior is:

1. receive the already-built context by reference;
2. derive `controlMode` for the result without modifying or rebuilding
   `context` or `context.metadata`;
3. apply the configured enforcement and bypass decisions;
4. when evaluation is required, call
   `this.engine.evaluate(context)` exactly once with that same object;
5. return `evidence.requestId` for every branch, using `context.requestId`
   when no pipeline result exists and the pipeline result request ID when it
   does;
6. preserve current decision, hard-block, hard-escalate, and in-memory gateway
   audit behavior.

The existing `check(request)` remains as the convenience/backward-compatible
entry point. It may build its current context and delegate once to
`checkContext(context)`. The new sibling is preferred over replacing `check`
or overloading it because the two input contracts have different semantics:
one normalizes a partial request, while the other promises exact context
preservation. A distinct method makes that boundary statically visible and
does not make a structurally compatible partial object ambiguous.

No `GuardRequestContext` or `GatewayResult` type extension is required for
this method. Both types already contain every input and output field needed.

## Required Design Question Answers

### 1. Exact context-preserving method

Add the doc-only sibling signature
`checkContext(context: GuardRequestContext): GatewayResult` to
`MandatoryGateway`. It must pass the exact `context` object to
`engine.evaluate`, with no spread, default assignment, request-ID generation,
field omission, or metadata rewrite. The engine already copies
`context.requestId` into its result and stores the supplied context
(`engine.ts:120-136`). The gateway result must keep the nested evidence shape:
`evidence.requestId`, `evidence.blockedBy`, and `evidence.escalatedBy`.

For BYPASS or disabled-enforcement branches that do not produce a
`GuardPipelineResult`, `evidence.requestId` must still equal
`context.requestId`; the other two nested fields remain absent. This closes
the current branch-specific request-ID loss without inventing top-level
`GatewayResult` fields.

### 2. Replace, overload, or sibling

Add a sibling method. Do not replace `check`, because current callers and its
test use the partial convenience request. Do not overload `check`, because
`GuardRequestContext` is structurally compatible with the partial request and
an overload would obscure whether defaults and ID generation are allowed.
The explicit sibling name makes the no-normalization contract inspectable.

The existing `check` may delegate to the sibling only after building its
current normalized context. That refactor preserves the legacy boundary while
keeping evaluation logic in one implementation path.

### 3. Exactly-one evaluation mechanism

The future route must replace, not supplement, the direct line
`guardEngine.evaluate(guardContext)` with exactly:

```ts
const gatewayResult = mandatoryGateway.checkContext(guardContext);
```

The future route adapter receives `MandatoryGateway`, not
`GuardRuntimeEngine`; therefore it has no direct evaluation capability. The
future singleton may construct both objects internally, but must export only
the gateway to the route adapter. The route file must contain no
`guardEngine.evaluate` call after composition.

Deterministic proof is a shared engine spy asserting one call per route
request and `toHaveBeenCalledWith(guardContext)`. A negative static assertion
must reject `guardEngine.evaluate` in the future route and route-adapter
changed set. This is source-verifiable ownership, not a convention.

### 4. Exact no-bypass configuration

The future execute-route singleton must construct the gateway with:

```ts
{
  enforceAll: true,
  hardBlock: true,
  hardEscalate: true,
  bypassActions: [],
  defaultControlMode: 'governed',
}
```

The exact bypass requirement is `bypassActions: []`. `enforceAll: true`
prevents the separate disabled-enforcement allow branch. Both hard flags make
BLOCK and ESCALATE return `allowed: false`. The empty array makes the current
substring bypass predicate false for every execute action. The future test
must use an action containing each current default substring and prove none
returns `BYPASS`.

### 5. Receipt and audit projection

The proposed route adapter must project fields as follows:

| Gateway source field | `buildEvidenceReceipt` input/output | `appendAuditEvent` field | Loss status |
|---|---|---|---|
| `decision` | `decision` -> receipt `decision` | `outcome` and `payload.gatewayDecision` | represented directly in both |
| `allowed` | no native typed receipt field | `payload.gatewayAllowed` | lossless only in durable audit |
| `bypassed` | no native typed receipt field | `payload.gatewayBypassed` | lossless only in durable audit |
| `controlMode` | no native typed receipt field | `payload.gatewayControlMode` | lossless only in durable audit |
| `evidence.requestId` | no native typed receipt field | `payload.gatewayRequestId` | lossless only in durable audit |
| `evidence.blockedBy` | no native typed receipt field | `payload.gatewayBlockedBy`, omitted when undefined | lossless only in durable audit |
| `evidence.escalatedBy` | no native typed receipt field | `payload.gatewayEscalatedBy`, omitted when undefined | lossless only in durable audit |

The audit event shape is:

```ts
{
  eventType: 'MANDATORY_GATEWAY_EVALUATED',
  actorId,
  actorRole,
  targetResource,
  action: guardContext.action,
  riskLevel: guardContext.riskLevel,
  phase: guardContext.phase,
  outcome: gatewayResult.decision,
  payload: {
    gatewayDecision: gatewayResult.decision,
    gatewayAllowed: gatewayResult.allowed,
    gatewayBypassed: gatewayResult.bypassed,
    gatewayControlMode: gatewayResult.controlMode,
    gatewayRequestId: gatewayResult.evidence?.requestId,
    gatewayBlockedBy: gatewayResult.evidence?.blockedBy,
    gatewayEscalatedBy: gatewayResult.evidence?.escalatedBy,
  },
}
```

After `appendAuditEvent` returns, its ID must be added to the existing envelope
with `appendAuditEventToEnvelope`; the response can then carry the existing
envelope plus the receipt built with `decision: gatewayResult.decision`.

Current source cannot put the six non-decision gateway fields into
`GovernanceEvidenceReceipt` as typed, standalone fields without changing its
schema and builder input. Packing them into trace summary strings would not
be a lossless typed projection and is rejected. The combined adapter is
lossless because the durable audit payload retains all seven fields and its
ID is linked through the envelope. `buildEvidenceReceipt` only constructs the
receipt object; durable storage is provided by `appendAuditEvent` through the
event storage adapter.

### 6. Exact future deterministic tests

| Required proof | Deterministic assertion |
|---|---|
| Context and request-ID preservation | construct a context containing all fourteen canonical fields; assert engine spy called once with the same object reference; assert nested `result.evidence.requestId` equals the supplied ID; assert the stored engine audit context is the same object |
| Exactly one evaluation | route-adapter test issues one request, expects the shared engine spy count to equal one, and verifies no direct-evaluate symbol remains in the route/adapter changed set |
| No bypass reaches execution | configure the execute gateway with `bypassActions: []`; use actions containing `health-check`, `ping`, `version`, and `openapi`; assert none returns `BYPASS`, each evaluates once, and provider seam count follows only `allowed` |
| BLOCK fail closed | engine returns BLOCK; assert gateway `allowed` is false, response occurs before routing/provider, provider spy count is zero, and durable audit payload contains `gatewayBlockedBy` |
| ESCALATE fail closed | engine returns ESCALATE; assert gateway `allowed` is false, response occurs before routing/provider, provider spy count is zero, and durable audit payload contains `gatewayEscalatedBy` |
| Projection completeness | table-drive ALLOW/BLOCK/ESCALATE results and deep-equal all seven projected audit payload fields; assert receipt decision equals gateway decision and envelope contains the returned audit ID |

The provider seam is a local spy only. No live call is needed or authorized.

### 7. Interface-change files versus later runtime files

Interface change itself:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts`;
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts`.

`EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` is not required because current
`GuardRequestContext` and nested `GatewayResult.evidence` already carry the
needed fields.

Separate future T1 runtime composition:

- proposed same-directory Web singleton;
- proposed route guard adapter and its test;
- execute route replacement and its focused route test.

Any future receipt-schema extension would be a separately source-verified Web
contract change. It is not required for the bounded combined projection
specified here because the durable audit payload carries the full summary.
The execute route remains an active GC-023 owner at lines 42-47 of the
registry; the lines 159-172 exception is only a resolved non-usable
tombstone. Therefore any T1 route edit must include same-domain extraction or
shrink evidence and cannot rely on the old 1001-line record.

### 8. Terminal disposition

`INTERFACE_SPEC_READY_FOR_FRESH_T1_RUNTIME_PACKET`

Current source supports the exact sibling signature, no-bypass configuration,
single-evaluation ownership, complete durable audit projection, bounded
receipt projection, and deterministic proof plan. This token authorizes only
a future packet-authoring checkpoint. It does not authorize T1 implementation
or release T2-T4.

## Findings / Position

The T0A interface blocker is resolved at specification level. The design does
not require extending the canonical context type, does not overload the
legacy convenience method, and does not misstate the receipt builder as
durable storage. The one bounded loss boundary is explicit: a standalone
current Web receipt represents only the decision, while the linked durable
audit record represents the full gateway summary.

## Risk / Corrective Action

| Risk | Corrective action required in any fresh T1 packet |
|---|---|
| Context silently rebuilt | require same-object engine assertion for `checkContext` |
| Route and gateway both evaluate | adapter receives gateway only; direct route evaluation removed; exact one-call test |
| Substring bypass survives | exact `bypassActions: []` plus four substring regression cases |
| ESCALATE reaches provider | gate on `gatewayResult.allowed` before routing/provider and prove zero provider calls |
| Receipt called durable | identify receipt as constructed response evidence and audit event as durable storage |
| Nested evidence flattened incorrectly | retain `GatewayResult.evidence.requestId`, `.blockedBy`, and `.escalatedBy` source shape |
| Route grows against GC-023 | honor active-owner split/shrink rule; do not use resolved tombstone |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Final evidence | Status |
|---|---|---|
| Resolve context-preserving method | questions 1-2 | PASS |
| Prevent duplicate evaluation | questions 3 and 6 | PASS |
| Disable execute bypass | questions 4 and 6 | PASS |
| Bound receipt/audit projection | question 5 | PASS |
| Separate interface and runtime files | question 7 | PASS |
| Keep later tranches held | question 8 and Claim Boundary | PASS |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `Status: COMPLETE_PENDING_REVIEW`; exact terminal enum; review/audit structural headings; Agent Operation Trace row labels; Delta evidence tokens; ASCII-only prose |
| gateRunPurpose | confirm the completed audit shape and claim boundaries after source verification; checker execution is evidence, not discovery |
| claimBoundary | checker-shape preparation only; independent reviewer acceptance remains pending |

## Epistemic Process Block

### Expected Result / Prediction

The packet predicted that current source could support one lossless
context-preserving method and one bounded receipt/audit adapter.

### Evidence Comparison

The method prediction is confirmed. The adapter prediction is narrowed:
current receipt types directly carry only the gateway decision, while the
existing durable audit payload can carry the full secret-safe summary.

### Contradiction Or Gap Disposition

No blocking contradiction remains because the combined projection is
lossless and explicitly linked through the envelope. A claim that the
standalone receipt carries all gateway fields is rejected.

### Claim Update

The interface specification is ready for independent review and, if accepted,
a fresh T1 runtime packet-authoring checkpoint.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Receipt construction and durable audit persistence are distinct existing seams | `RULE_GAP` | GOVERNANCE_CONTROL_PLANE | `N/A_WITH_REASON` | no new ADIF entry: ADIF-0029 already governs durable evidence projection drift |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | no-commit documentation worker |
| Provider or surface | local provenance workspace |
| Session or invocation | GC009-GC010-PCALLER-T1I worker execution, 2026-07-25 |
| Working directory | repository root |
| Command or tool surface | governed file reads; bounded `rg`; git read-only checks; ADIF resolver; autorun and worker-return gates; `apply_patch` |
| Target paths | this audit and canonical T1I worker return |
| Allowed scope source | committed T1I work order at execution base `2956af3e4` |
| Before status evidence | HEAD `2956af3e4`; `git status --short` empty |
| After status evidence | exactly two worker-owned untracked paths |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | documentation-only interface and adapter specification |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | no-commit documentation worker |
| Invocation ID | `gc009-gc010-production-caller-t1i-worker-2026-07-25` |
| Expected manifest | this audit and canonical T1I worker return |
| Actual changed set | this audit and canonical T1I worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only future gateway interface and Web projection design |
| claimDisposition | CLAIM_REJECTED - no runtime enforcement or production caller is implemented |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no runtime receipt was generated |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source reads, source mapping, and governance gates |
| invocationBoundary | local governed document editing only |
| interceptionBoundary | no provider, browser, CLI, MCP, process, runtime, or filesystem interception claim |
| claimLanguage | specifies a future method and adapter for separate authorization |
| forbiddenExpansion | no T1 implementation, source/test/package/checker/session/public mutation, live proof, push, deploy, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance design audit; no public-sync authority.

## Claim Boundary

This audit specifies a doc-only interface and adapter contract and selects the
interface-spec-ready disposition. It does not implement or release T1, does
not prove a production caller, does not close the paired GC-009/GC-010 gap,
and leaves T2-T4 in `HOLD_*`. GC-010 remains a separate fresh-packet lane.
