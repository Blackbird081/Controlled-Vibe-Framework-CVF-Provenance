# CVF GC-009/GC-010 Production Owner Design T0A Audit

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Batch ID: GC009-GC010-PCALLER-T0A

Date: 2026-07-25

executionBaseHead: `4b6c57d11`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_2026-07-25.md`

## Purpose

Define the smallest source-compatible future owner pattern for GC-009,
identify any interface changes required before implementation can be
dispatched, and give GC-010 a separate explicit lane disposition. This audit
is documentation-only and does not create a caller or release T1-T4.

## Target / Source

The target is the open production-caller gap
`cvf.asc.gap.gc009_gc010_no_production_caller.v1`. The primary source surfaces
are the canonical guard-contract gateway and agent runtime, the cvf-web shared
engine and execute route, the package export surface, the Web request adapter,
the Web receipt/audit seams, and the GC-023 registry.

## Scope / Methodology

At `executionBaseHead` `4b6c57d11`, the worker:

- read the paired GC-018, work order, accepted T0 audit and completion;
- read every source and checker required by the work order;
- reran the exact constructor/caller search under `EXTENSIONS/`;
- compared existing-singleton extension, a new sibling owner, route-local
  ownership, and MCP-local ownership;
- mapped the current Web guard request and result to `MandatoryGateway.check`;
- evaluated package surface, duplicate-evaluation, receipt, deterministic
  test, GC-010, GC-023, changed-set, and rollback constraints.

No provider, network, browser, CVF CLI/MCP, build, or test action was used.

## Findings / Position

Current source supports an exact preferred owner location, but not a
lossless implementation contract. The preferred documentation-only owner is:

| Field | Decision | Source status |
|---|---|---|
| `proposedOwnerModule` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | DOC_ONLY_NEW; absent and not created |
| `proposedOwnerTest` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.test.ts` | DOC_ONLY_NEW; absent and not created |
| `guardEvaluationDisposition` | REPLACE_DIRECT_EVALUATION | documentation design only |
| `gc010LaneDisposition` | SEPARATE_FRESH_PACKET | documentation design only |

The current `MandatoryGateway.check` interface cannot consume the route's
already-normalized `GuardRequestContext`. It generates a new request ID,
accepts only a subset of the canonical context fields, injects gateway
control-mode/default behavior, and applies a substring bypass list before
evaluation. A route integration that merely calls the current interface would
therefore either double-evaluate or change correlation/context semantics.

## Owner Candidate Comparison

| Candidate | Source-backed assessment | Decision |
|---|---|---|
| Extend `guard-engine-singleton.ts` | It currently owns only the cached `GuardRuntimeEngine` lifecycle and one test reset seam (`guard-engine-singleton.ts:13-32`). Adding gateway policy/configuration would couple two lifecycles and make reset behavior ambiguous. | REJECT as the direct gateway owner |
| New sibling `mandatory-gateway-singleton.ts` | It can consume `getSharedGuardEngine()` while retaining a separate gateway singleton/config/reset contract. The path is adjacent to the proven canonical engine owner without growing the execute route. | PREFERRED after the interface issue is resolved |
| Route-local owner | `route.ts` is 959 lines and is an active GC-023 owner. A handler-local instance would fragment lifecycle/audit state and route growth would require same-batch split or shrink evidence. | REJECT |
| MCP-local owner | The MCP family owns a different same-name `GuardRuntimeEngine`; the accepted T0 found no canonical gateway caller there. It is not the cvf-web execution owner. | REJECT |

## Required Design Question Answers

### 1. Exact GC-009 owner

The future owner should be the proposed sibling
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts`.
It should cache exactly one `MandatoryGateway` constructed from
`getSharedGuardEngine()` and expose a test-only reset paired with
`resetSharedGuardEngine()`.

This is preferable to extending `guard-engine-singleton.ts` because the
engine lifecycle remains canonical and independent from gateway configuration.
It is preferable to `route.ts` because the route is a 959-line active GC-023
owner and should orchestrate, not own another singleton. It is preferable to
the MCP-local engine because that engine is a distinct implementation and is
not the cvf-web production execution channel.

### 2. Package exports, files, and barrel changes

A future implementation using root-package named imports would require:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`: add named value exports
  `MandatoryGateway`, `createMandatoryGateway`, and
  `DEFAULT_GATEWAY_CONFIG`, plus type exports `GatewayConfig` and
  `GatewayResult`;
- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` `files`: add
  `src/runtime/mandatory-gateway.ts`;
- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` `exports`: no new subpath is
  required if the root `"."` export continues to resolve `src/index.ts`;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`: no dependency
  change is required because it already declares
  `"cvf-guard-contract": "file:../../CVF_GUARD_CONTRACT"`.

The current package and barrel omit the gateway. GC-010 exports are not part
of this future GC-009 slice.

### 3. Route evaluation and field mapping

The required choice is `REPLACE_DIRECT_EVALUATION`: remove the route's direct
`guardEngine.evaluate(guardContext)` call and make one gateway-owned
evaluation. Adapting the already-computed result would not call GC-009, while
calling `MandatoryGateway.check` after direct evaluation would duplicate it.

Required lossless input mapping:

| Current `GuardRequestContext` field | Current `MandatoryGateway.check` support | Required future handling |
|---|---|---|
| `requestId` | not accepted; gateway creates `gw-*` | preserve the exact incoming ID through a new context-preserving interface |
| `phase`, `riskLevel`, `role`, `agentId`, `action` | accepted | pass without re-defaulting |
| `targetFiles`, `fileScope`, `channel`, `metadata` | accepted | pass without mutation; preserve `userRole` and `ai_commit` metadata |
| `mutationCount`, `mutationBudget`, `scope`, `traceHash` | not accepted | preserve through the same canonical context interface, even if the current route does not populate every field |

Required result mapping:

| Gateway result | Route use |
|---|---|
| `guardResult` | remains the canonical `GuardPipelineResult` returned in route responses and passed downstream |
| `allowed=false`, `decision=BLOCK` | fail closed before provider routing |
| `allowed=false`, `decision=ESCALATE` | fail closed before provider routing with approval/escalation response handling |
| `allowed=true`, `decision=ALLOW` | continue exactly once |
| `decision=BYPASS` | forbidden for the execute route unless a later source-verified policy explicitly authorizes an exact bypass action |

The current interface cannot satisfy this mapping without semantic loss.
The future guard-contract interface must accept an already-built
`GuardRequestContext` and evaluate that exact object, or equivalently extend
`check` to cover every canonical field and preserve `requestId`. The route
owner must configure no execute-route bypasses.

### 4. Deterministic duplicate-evaluation prevention

The future route path must contain no call to `guardEngine.evaluate`.
The route builds one Web context, calls the gateway adapter once, and consumes
the returned `GatewayResult.guardResult`. The gateway context method contains
the only `engine.evaluate(context)` call.

Deterministic proof requires a spy engine assertion of exactly one evaluation
per ALLOW, BLOCK, and ESCALATE request plus a source assertion that the
route-integration path has no second `evaluate` call. A result-adaptation path
is rejected because it would not instantiate GC-009 as the evaluator.

### 5. Exact future tests

The smallest deterministic proof packet should cover:

| Future test path | Required proof |
|---|---|
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | extend the existing test to prove exact context/request-ID preservation, one evaluate call, ALLOW, hard BLOCK, hard ESCALATE, and execute-route bypass disabled |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.test.ts` | DOC_ONLY_NEW; singleton identity, shared-engine injection, configuration, and reset isolation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-mandatory-gateway.test.ts` | DOC_ONLY_NEW; route adapter returns ALLOW, fails closed for BLOCK and ESCALATE, makes zero provider calls in negative cases, and observes one engine evaluation |

All cases use deterministic fake/real guard fixtures and no provider key or
network access.

### 6. Gateway audit, receipt, and audit-event boundary

`MandatoryGateway` appends every `GatewayResult` only to its in-memory
`auditLog` (`mandatory-gateway.ts:69,105,118,178,195-197`). The execute route
uses a separate Web receipt builder and durable control-plane audit events:
`buildEvidenceReceipt` constructs `GovernanceEvidenceReceipt`
(`web-governance-envelope.ts:241-280`) and `appendAuditEvent` persists/forwards
the Web audit record (`control-plane-events.ts:140-152`).

The seams meet only through the nested `GatewayResult.guardResult`; they do
not currently share an audit store or receipt schema. A future adapter must
project a secret-safe gateway summary (`decision`, `allowed`, `bypassed`,
`controlMode`, `requestId`, `blockedBy`, `escalatedBy`) into the Web
enforcement trace/audit event while continuing to use the existing Web
receipt as the durable route receipt. The in-memory gateway log must not be
claimed as durable evidence. This projection requires a future source and
test decision; it is not implemented here.

### 7. GC-010 lane

`gc010LaneDisposition` is `SEPARATE_FRESH_PACKET`.
`AgentExecutionRuntime` owns a full asynchronous
parse/pre-check/provider-execute/post-check pipeline and its own in-memory
execution log (`agent-execution-runtime.ts:130-143,170-208,358-378`). It is
not a wrapper around `MandatoryGateway`, and adding it to the cvf-web route
would duplicate the route's provider pipeline.

The concrete release condition is a fresh GC-018/work order that identifies
a non-test provider-execution owner for `AgentExecutionRuntime`, maps its
provider and receipt contracts to that owner, and proves one guard evaluation
without composing it into the GC-009 Web gateway slice. Until that evidence
exists, GC-010 and T1-T4 remain HOLD.

### 8. Smallest future changed set, route-size handling, rollback, and failure

The smallest currently supportable future proposal is:

1. modify `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts`;
2. modify `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts`;
3. modify `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`;
4. modify `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`;
5. create the proposed owner module and proposed owner test;
6. create
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-guard-gateway.ts`;
7. create
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-mandatory-gateway.test.ts`;
8. modify
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
   only to delegate to the extracted route adapter.

The new `route-guard-gateway.ts` is same-directory split evidence for the
959-line active owner. The future packet must remeasure route size and satisfy
GC-023; it may not use the resolved 1001-line tombstone as a cap.

Rollback is atomic: restore the direct route evaluation and prior package
surface, delete only the three new source/test paths plus the owner test, and
revert the context-preserving gateway method/tests. There is no data
migration. The fail condition is any lost request/context field, more or less
than one evaluation, an execute-route bypass, provider invocation after BLOCK
or ESCALATE, non-durable audit evidence claimed as durable, or route-size gate
failure.

### 9. Terminal support

Current source supports the terminal disposition below because a preferred
owner and deterministic flow are identifiable, but the existing gateway
interface cannot preserve the route's canonical request context or provide
the required durable evidence adapter without a separately authorized
interface change.

## Decision / Disposition

`NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE`

This is a bounded design result. It does not release T1. A future packet may
be authored only after it source-verifies the exact context-preserving
gateway interface and receipt/audit projection described above.

## Negative Search And Collision Evidence

Command:

```powershell
rg -n "new MandatoryGateway|createMandatoryGateway\(|new AgentExecutionRuntime" EXTENSIONS --glob "!**/node_modules/**" --glob "!**/dist/**" --glob "!**/coverage/**"
```

Result: 16 matches. Fifteen are test construction sites; the remaining match
is the factory declaration/internal construction at
`mandatory-gateway.ts:219,223`. There are zero non-test callers. The command
returned search exit code 0 because matches exist.

The same-name `GuardRuntimeEngine` in the MCP server remains a separate
implementation and is not treated as the canonical package owner.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T0 accepted no current owner | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T0_COMPLETION_2026-07-25.md` | Findings / Position | `NOT_READY_MISSING_SOURCE_VERIFIED_OWNER` | T0 completion review | ACCEPT |
| Gap remains invocation-unproven | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `currentStatus`; `closeCondition` | `currentStatus`; `closeCondition` | system-chain gap entry | ACCEPT |
| Shared engine singleton lifecycle | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | lines 13-32 | `getSharedGuardEngine`; `resetSharedGuardEngine` | cvf-web singleton | ACCEPT |
| Web request normalization | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts` | lines 86-129 | `WebGuardInput`; `buildWebGuardContext` | Web guard adapter | ACCEPT |
| Existing direct evaluation | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 560-592 | `guardEngine.evaluate`; BLOCK response | execute POST route | ACCEPT |
| Gateway input and evaluation | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 80-180 | `check`; `engine.evaluate`; `GatewayResult` | `MandatoryGateway` | ACCEPT |
| Gateway in-memory audit | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 69, 105, 118, 178, 195-197 | `auditLog`; `getAuditLog` | `MandatoryGateway` | ACCEPT |
| Canonical context fields | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 93-110 | `GuardRequestContext` | guard-contract type | ACCEPT |
| Web receipt builder | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 55-78, 241-280 | `BuildGovernanceEvidenceReceiptInput`; `buildEvidenceReceipt` | Web evidence receipt | ACCEPT |
| Web audit event | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 140-152 | `appendAuditEvent` | control-plane event store | ACCEPT |
| Agent runtime is a separate provider pipeline | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | lines 130-143, 170-208, 358-378 | `AgentExecutionRuntime`; `preCheck`; `run` | agent runtime | ACCEPT |
| Package and barrel omit gateway | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | package lines 8-27; barrel full export surface | `exports`; `files`; named exports | guard-contract package | ACCEPT |
| cvf-web already depends on canonical package | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 26 | `cvf-guard-contract` | cvf-web package | ACCEPT |
| Route active owner and tombstone distinction | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | active owner lines 42-47; resolved tombstone lines 159-172 | `proactiveOwnerSurfaces`; `status`; `removalProcedure` | GC-023 registry | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Disposition |
|---|---|---|
| `proposedOwnerModule` | exact future GC-009 singleton owner path | DOC_ONLY_NEW |
| `proposedOwnerTest` | exact future singleton test path | DOC_ONLY_NEW |
| `guardEvaluationDisposition` | route evaluation design choice | DOC_ONLY_NEW |
| `gc010LaneDisposition` | separate GC-010 lane decision | DOC_ONLY_NEW |
| `route-guard-gateway.ts` | candidate future same-directory route split | DOC_ONLY_NEW |
| `route-mandatory-gateway.test.ts` | candidate future deterministic route proof | DOC_ONLY_NEW |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Current `check` changes request identity/context | keep the disposition not-ready until a canonical context-preserving method is source-verified |
| Route and gateway both evaluate | future route must replace direct evaluation and assert one engine call |
| Gateway substring bypass changes execute semantics | future execute owner uses no bypass actions; any bypass requires a separate policy decision |
| ESCALATE reaches provider execution | future route adapter fails closed before routing and proves zero provider calls |
| In-memory log overstated as durable receipt | project a bounded summary into existing Web audit/receipt seams and keep the in-memory boundary explicit |
| Route grows near GC-023 threshold | extract a same-directory route adapter and re-run the size guard |
| GC-010 conflated with GC-009 | retain `SEPARATE_FRESH_PACKET` and its concrete release condition |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | review structural headings; full worker-return headings; AOT fields; Delta fields and evidence tokens; exact no-commit literal; public export token |
| gateRunPurpose | confirm required output shape before authoring and support later worker-return fast-gate verification |
| claimBoundary | checker compliance evidence only; no implementation or closure claim |

## Epistemic Process Block

### Expected Result / Prediction

The paired baseline predicted that a future owner adjacent to the shared
singleton might be viable while GC-010 would remain separate.

### Evidence Comparison

The owner-location prediction is supported, and the GC-010 separation
prediction is supported. The readiness prediction is narrowed: current
`MandatoryGateway.check` cannot accept the exact Web context, preserve its
request ID/all canonical fields, disable execute-route bypass semantics
without configuration, or project durable gateway evidence through the
existing Web receipt/audit seam.

### Contradiction Or Gap Disposition

The source mismatch is not hidden. It changes the result from a ready owner
contract to a not-ready contract that requires a fresh source-verified
interface-change packet.

### Claim Update

The preferred owner location is confirmed as documentation design; GC-010 is
separated; implementation readiness is rejected until the interface and
receipt adapter are source-verified.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | no-commit documentation worker |
| Provider or surface | local workspace |
| Session or invocation | GC009-GC010-PCALLER-T0A worker execution, 2026-07-25 |
| Working directory | repository root |
| Command or tool surface | file reads; `rg`; git read-only checks; ADIF resolver; pre-implementation and worker-return gates |
| Target paths | this audit; companion worker return |
| Allowed scope source | committed T0A work order at execution base `4b6c57d11` |
| Before status evidence | HEAD `4b6c57d11`; `git status --short` empty |
| After status evidence | exactly this audit and companion worker return are untracked |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | documentation-only T0A execution |
| Claim boundary | repo-local trace; no OS/user attribution |
| Agent type | no-commit documentation worker |
| Invocation ID | `gc009-gc010-production-owner-design-t0a-worker-2026-07-25` |
| Expected manifest | this audit; companion worker return |
| Actual changed set | this audit; companion worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only future production-owner contract design |
| claimDisposition | CLAIM_REJECTED - no runtime enforcement behavior is implemented or claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no runtime receipt was generated |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source reads, exact caller search, and governance gates |
| invocationBoundary | governed local document authoring only |
| interceptionBoundary | no provider, browser, CLI, MCP, Web runtime, process, IDE, or filesystem interception claim |
| claimLanguage | identifies a preferred owner and blocking interface gap only |
| forbiddenExpansion | no T1 release, source/package/test/checker/session/public mutation, live proof, deploy, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance design audit; no public-sync authorization.

## Claim Boundary

This audit identifies a preferred documentation-only owner pattern and a
blocking interface mismatch. It does not establish a production caller,
change source/package/tests, prove runtime enforcement, authorize live proof,
or release T1-T4. GC-010 requires a separate fresh packet, and all provider,
CLI/MCP, public, deployment, and production actions remain parked.
