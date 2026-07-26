# CVF Agent Work Order GC-009/GC-010 Production Caller T1 Runtime Composition

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_REDISPATCH_READY_R1_ROUTE_TEST_MOCK

Batch ID: GC009-GC010-PCALLER-T1

Date: 2026-07-26

Dispatch base head: `7275e9dc8`

Execution base head: `TO_BE_CAPTURED_BY_WORKER`

Closure base head: `TO_BE_CAPTURED_BY_REVIEWER`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Redispatch R1 original execution base head: `871251726`

## Dispatch Prompt Envelope

```text
Execute only:
docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_2026-07-26.md

Route: WORKER_MUST_NOT_COMMIT.

Before editing, capture:
git rev-parse --short HEAD
git status --short --untracked-files=all

The expected committed execution base is the reviewer-accepted dispatch
commit that contains this packet. Stop if HEAD differs from that committed
packet or if the worktree is not clean.

Implement only the exact writable manifest. Add the accepted
MandatoryGateway.checkContext interface, package export, cvf-web singleton,
route adapter, bounded execute-route replacement, and deterministic local
tests. Keep provider seams mocked. Do not run live provider, browser, CLI,
MCP, network, public-sync, push, deployment, or T2-T4 work.

Do not commit. Return the canonical worker-return artifact with exact changed
set, commands, results, route line-count delta, and one terminal disposition.

R1 continuation authority: retain the exact blocked T1 changed set created
from original execution base `871251726`. After this redispatch is committed,
capture the current committed HEAD as `redispatchAuthorityHead`. The retained
dirty worktree is expected only for the previously declared implementation
paths and blocked worker return. Replace the unused planned
`route.mandatory-gateway.test.ts` artifact with the existing `route.test.ts`.
Add a default resolved audit event to that suite, run all 31 tests, refresh
the worker return, rerun required gates, and stop without staging or
committing.
```

## Purpose

Implement the smallest source-verified T1 composition that makes the
mandatory gateway the execute route's sole guard-engine evaluation owner,
preserves the canonical Web context, fails closed before provider routing,
and links a secret-safe gateway audit event into the existing Web envelope.

## Authority Chain

1. Human authorization explicitly released fresh T1 packet authoring with
   T1I completion review `7b3cdc23a` as its predecessor evidence.
2. T0A material closure `0e97a0ace` identified the singleton owner direction.
3. T1I material closure `7b3cdc23a` accepted the exact interface and adapter
   contract.
4. This work order, after independent reviewer acceptance and commit, releases
   one no-commit implementation worker.
5. Codex remains reviewer/closer and commit owner.
6. T2-T4 remain held.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | N/A with reason: the accepted same-lane T1I work order is the starting scaffold |
| generatedProfile | runtime implementation, no-commit worker, held successors |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced design questions with exact writable runtime paths, implementation instructions, deterministic tests, and GC-023 shrink proof |
| checkerReadAheadConfirmation | dispatch, handoff, authority, manifest, source-verification, operation-trace, worker-return, and file-size checker contracts reviewed |
| docOnlyNewFields | new symbols and files are isolated in `## New Doc-Only Fields` until implemented |
| claimBoundary | scaffold provenance only |

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition | Status |
|---|---|---|---|---|
| T0A | `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` | `0e97a0ace` | preferred singleton owner; interface gap | PASS |
| T1I | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md` | `7b3cdc23a` | `CLOSED_PASS_BOUNDED_INTERFACE_SPEC_READY_FOR_FRESH_T1_RUNTIME_PACKET` | PASS |
| Human authorization | approval after `7275e9dc8` | N/A with reason: recorded in this governed packet | fresh T1 runtime packet authorized; T2-T4 held | PASS |
| Dispatch packet | this baseline and work order | reviewer-accepted packet pending material commit | worker starts only from the committed dispatch base | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | bounded T1 mandatory-gateway runtime composition |
| scopeClassification | runtime, package surface, and deterministic local tests |
| riskSensitivity | R1 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | Codex dispatcher; one no-commit implementation worker; Codex reviewer/closer |
| escalationCondition | stale source, extra writable path, live proof, T2-T4, new surface, checker, session, or public need |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| packet author | Codex | source verification and draft packet |
| reviewer/dispatcher | Codex | repair, gates, material commit, worker dispatch |
| implementation worker | one documentation-and-code worker | exact manifest implementation and worker return; no commit |
| reviewer/closer | Codex | independent diff/source/test review, bounded repair if authorized, closure, commit, continuity |
| commit owner | Codex | all material and session-sync commits |

## Scope

### Allowed implementation

- add the accepted `checkContext` sibling without changing canonical context
  or gateway-result schemas;
- preserve legacy `check` behavior and make it delegate through one evaluation
  path where practical;
- expose the gateway through the guard-contract root and runtime subpath;
- add a cvf-web gateway singleton backed by the existing shared engine;
- add an async route adapter with injection seams for deterministic tests;
- persist `MANDATORY_GATEWAY_EVALUATED`, append the returned event ID to the
  current envelope, and return both gateway and pipeline results;
- replace the route's direct engine evaluation with the adapter;
- fail closed before provider routing for every non-allowed decision and for
  an absent pipeline result;
- include gateway decision receipt evidence on direct gateway-denied
  responses while preserving later response-specific receipt decisions;
- shrink `route.ts` below its 959-line dispatch-base count;
- add deterministic local tests with no real provider call.

### Explicitly excluded

- live providers, keys, network, browser, CLI, MCP, deployment, push, or
  public-sync;
- receipt-schema, canonical context, or gateway-result schema expansion;
- new UI, API route, operator surface, checker, registry, session, roadmap, or
  completion-review edits by the worker;
- GC-010 live proof or T2-T4 execution;
- unrelated refactor, formatting, dependency install, or lockfile update.

## Write Ownership

### Worker-owned writable paths

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`
4. `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.test.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
11. `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_WORKER_RETURN_2026-07-26.md`

### Reviewer-owned closure paths

- this work order;
- `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`;
- `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md`;
- active session and handoff surfaces in a separate session-sync commit.

## Required First Reads

The worker must fully read:

1. this work order;
2. the companion GC-018 baseline;
3. the T1I audit and completion review;
4. `docs/reference/guard_orientation/README.md`;
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
6. `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`;
7. `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`;
8. `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`;
9. `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`;
10. every source and test path in the Source Verification Block.

## Pre-Flight Checks

Before editing:

1. capture `executionBaseHead`;
2. require clean `git status --short --untracked-files=all`;
3. confirm this work order is committed and dispatch-ready;
4. recompute the 959-line route baseline;
5. for initial execution, confirm `checkContext`, new helper files, and worker
   return do not yet exist; for R1 continuation, confirm the retained changed
   set exactly matches the blocked worker return;
6. confirm the route still has one direct `guardEngine.evaluate`;
7. confirm package exports still omit mandatory gateway;
8. run pre-implementation autorun using the captured base and current HEAD;
9. stop on any stale source or unexpected changed path.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1I ready token | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md` | Findings / Position | `INTERFACE_SPEC_READY_FOR_FRESH_T1_RUNTIME_PACKET` | T1I completion review | ACCEPT |
| Exact sibling method design | VALUE_SET | `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | Required Design Question Answers 1-2 | `checkContext` | T1I audit | ACCEPT |
| Exact gateway config | VALUE_SET | `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | Required Design Question Answer 4 | `bypassActions`; `enforceAll`; `hardBlock`; `hardEscalate`; `defaultControlMode` | T1I audit | ACCEPT |
| Existing gateway entry point and result shape | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 36-49, 66-178 | `MandatoryGateway`; `GatewayResult`; `check` | runtime gateway | ACCEPT |
| Existing pipeline result shape | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 127-137 | `GuardPipelineResult` | guard-contract schema | ACCEPT |
| Canonical request context | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 93-110 | `GuardRequestContext` | guard-contract schema | ACCEPT |
| Shared engine singleton | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | full file | `getSharedGuardEngine`; `resetSharedGuardEngine` | cvf-web runtime owner | ACCEPT |
| Current package omission requires the writable package correction | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | `exports`; `files`; runtime helper exports | `exports`; `files`; named exports | guard-contract package | REJECT |
| Web context builder | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts` | lines 86-129 | `buildWebGuardContext` | Web guard adapter | ACCEPT |
| Direct route evaluation must be replaced by the writable adapter call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 561-580 | `getSharedGuardEngine`; `guardEngine.evaluate` | execute POST route | REJECT |
| Downstream pipeline-result consumers | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 580-935 | `guardResult` | execute POST route | ACCEPT |
| Durable audit append | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 96-152 | `appendAuditEvent` | control-plane event store | ACCEPT |
| Envelope audit linkage | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 287-292 | `appendAuditEventToEnvelope` | Web governance envelope | ACCEPT |
| Receipt decision projection | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 55-78, 241-280 | `buildEvidenceReceipt` | Web evidence receipt | ACCEPT |
| Active route owner | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | `activeOwners` execute-route entry | `activeOwners`; `status` | file-size registry | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `getSharedMandatoryGateway` | configured singleton accessor | DOC_ONLY_NEW before implementation |
| `resetSharedMandatoryGateway` | test reset seam | DOC_ONLY_NEW before implementation |
| `evaluateRouteMandatoryGateway` | exactly-once gateway and audit adapter | DOC_ONLY_NEW before implementation |
| `MANDATORY_GATEWAY_EVALUATED` | durable audit event type | DOC_ONLY_NEW before implementation |
| `route.test.ts` mock default | existing route suite becomes the route-level integration proof by returning a deterministic audit event ID | EXISTS; writable only under R1 redispatch |

## Implementation Contract

### Guard-contract method

Add:

```ts
checkContext(context: GuardRequestContext): GatewayResult
```

It must use the exact context object. Every branch must set nested
`evidence.requestId`. Evaluation-required branches call
`this.engine.evaluate(context)` exactly once. Legacy `check` may normalize its
partial input and delegate, but its public behavior must remain covered.

### Package surface

Export `MandatoryGateway`, `GatewayConfig`, `GatewayResult`, and
`DEFAULT_GATEWAY_CONFIG` from the root barrel. Add the runtime subpath export
and published file entry in `package.json`. Do not change dependencies,
version, or lockfiles.

### Singleton

The singleton must use `getSharedGuardEngine()` and exactly:

```ts
{
  enforceAll: true,
  hardBlock: true,
  hardEscalate: true,
  bypassActions: [],
  defaultControlMode: 'governed',
}
```

Defaults for phase, risk, and role remain owned by the canonical gateway
unless source requires explicit values. Provide a test-only reset.

### Route adapter

`evaluateRouteMandatoryGateway` must:

1. accept the already-built `GuardRequestContext`, current
   `WebGovernanceEnvelope`, and audit actor/target fields;
2. accept an injectable gateway for tests and default to the singleton;
3. call `checkContext` exactly once;
4. append one `MANDATORY_GATEWAY_EVALUATED` event with the seven T1I-specified
   gateway fields in `payload`;
5. append the returned audit ID to the same envelope;
6. return `gatewayResult` and `guardResult`;
7. mark a missing `guardResult`, BYPASS, BLOCK, ESCALATE, or any
   `allowed: false` result as fail-closed before provider routing.

Do not stringify the gateway summary into a trace string and do not call the
engine directly from the adapter.

### Execute route

Remove the `getSharedGuardEngine` import and every direct
`guardEngine.evaluate` call. Build the canonical context as today, call the
adapter once, retain the returned pipeline result as `guardResult` for
downstream compatibility, and return before provider routing on all
fail-closed outcomes. Direct gateway-denied responses must include the current
envelope and a receipt whose decision is the gateway decision. Later
response-specific receipts may retain their existing decision semantics
because the full gateway projection is linked through the audit ID.

The route must finish below 959 lines. Extraction is required; prose
compression or registry edits are forbidden.

## Terminal Disposition Enum

The worker must return exactly one:

- `COMPLETE_PENDING_REVIEW`
- `BLOCKED_STALE_EXECUTION_BASE`
- `BLOCKED_SOURCE_DRIFT`
- `BLOCKED_TEST_FAILURE`
- `BLOCKED_SCOPE_EXPANSION_REQUIRED`

Only `COMPLETE_PENDING_REVIEW` may accompany a closure recommendation.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Required evidence |
|---|---|---|
| accepted owner contract | method, package, singleton sections | source diff and focused tests |
| exactly-one evaluation | adapter and route sections | spy count plus negative direct-symbol search |
| fail-closed before provider | route contract | BLOCK, ESCALATE, BYPASS/missing-result tests with provider count zero |
| receipt/audit projection | adapter contract | seven-field payload, event ID in envelope, denied receipt decision |
| smallest changed set | exact writable manifest | no path outside manifest |
| GC-023 maintainability | route extraction | final line count below 959 and file-size gate |
| keep T2-T4 held | exclusions and claim boundary | no live proof or successor mutation |

## Design Control Carry-Forward

The worker must not:

- replace the accepted sibling method with an overload;
- flatten nested gateway evidence;
- treat the gateway's in-memory audit log as durable;
- allow ESCALATE or BYPASS to reach routing/provider;
- expand receipt schemas to carry the full gateway summary;
- import the MCP-local engine;
- use the resolved route-size tombstone as an active exception.

## Worker Autonomy / No-Question Rule

Repair in-scope compile, lint, type, and deterministic-test defects directly.
Resolve in-scope implementation details directly. Stop only on a
return-to-orchestrator condition.

## Work-Order Fulfillment Manifest

The work order is fulfilled only when every writable runtime/test path that
the implementation needs is present in the actual changed set, every changed
path is allowed, all required proof passes, and the worker return is complete.

## Required Artifact Manifest

| Artifact class | Required path | Owner | Required state |
|---|---|---|---|
| guard implementation | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | worker | modified |
| guard tests | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | worker | modified |
| package barrel | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | worker | modified |
| package manifest | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | worker | modified |
| gateway singleton | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | worker | new |
| singleton tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.test.ts` | worker | new |
| route adapter | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | worker | new |
| adapter tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.test.ts` | worker | new |
| route integration | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | worker | modified and smaller |
| route proof and regression fix | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | worker | modified under R1; default `appendAuditEvent` resolution and all 31 tests PASS |
| worker return | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_WORKER_RETURN_2026-07-26.md` | worker | new |

## Forbidden Path Manifest

- `CVF_SESSION/`
- `AGENT_HANDOFF_V52_2026-07-25.md`
- `CVF_SESSION_MEMORY.md`
- `governance/compat/`
- `docs/baselines/`
- `docs/roadmaps/`
- this work order
- all completion-review paths
- public-sync clone
- all package lockfiles
- every path not listed in the writable manifest

## Forbidden Filesystem State At Dispatch

- worker output already present, except the exact R1 retained blocked return
  declared at original execution base `871251726`;
- uncommitted packet-author changes;
- a staged path;
- a changed path outside the packet-author manifest;
- HEAD not equal to the committed reviewer dispatch;
- direct route evaluation already removed by an unreviewed change.

## Required Proof Manifest

| Proof | Required result |
|---|---|
| guard focused tests | PASS |
| guard typecheck | PASS |
| cvf-web singleton, adapter, and existing route tests | PASS, including 31/31 in `route.test.ts` |
| cvf-web typecheck | PASS |
| negative direct-evaluate search | zero `guardEngine.evaluate` in route and new adapter |
| exactly-one evaluation | one engine call with same context object |
| fail-closed provider boundary | zero provider calls for BLOCK, ESCALATE, BYPASS, and missing pipeline result |
| audit projection | all seven fields plus linked event ID |
| route maintainability | final route line count less than 959; file-size guard PASS |
| changed set | exact subset of writable manifest plus required worker return |
| diff hygiene | `git diff --check` PASS |
| worker-return fast gate | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | packet roles and cvf-web route | exact no-commit manifest | diffs, tests, audit linkage | route adapter | `IMPLEMENTATION_AUTHORIZED` |
| `EXTERNAL_AGENT_CLI_MCP` | not in scope | no invocation or adapter authority | N/A with reason: no CLI/MCP work | none | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external knowledge input |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | canonical CVF source only |

## Agent Handoff Contract Control Block

Contract source:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
|---|---|
| route | `WORKER_MUST_NOT_COMMIT` |
| rolePattern | `MULTI_AGENT_MULTI_ROLE` |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`7275e9dc8`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | dispatch: baseline, work order, roadmap; execution: exact worker writable manifest; closure: reviewer-owned closure paths; session-sync: continuity only |
| traceScope(phase, actor) | each actor records its own phase trace and exact changed set |
| commitOwner(phase) | worker must not commit; Codex owns material dispatch, material closure, and separate continuity commits |
| crossBatchIsolation | no unrelated change may share the worker or closure batch |
| nextMoveSurfaces | reviewer updates session state and active handoff only after material commit, in a separate session-sync commit |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | T1 changes current guard-contract and cvf-web runtime owners; it does not scan or absorb `.private_reference/legacy`. |
| Coverage evidence used instead | T0A and T1I accepted reviews plus current runtime source verification. |

## Evidence Reuse And Encoding Plan

verificationMode: `RECOMPUTE_REQUIRED`

recomputeReason: T0A and T1I release the design and dependency facts, but the
worker must recompute current runtime symbols, route line count, changed set,
tests, and gate results at its own execution base.

unicodePathHandling: literal ASCII repo-local paths only

extractedTextAuthority: N/A with reason: no extracted document text is used.

Prior governed reviews are dependency authority only. They do not substitute
for fresh source and test verification. Encoding is UTF-8 with ASCII-authored
prose under the repository symbol discipline.

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: NOT_APPLICABLE_WITH_REASON
- Target lifecycle state: NOT_APPLICABLE_WITH_REASON
- Prior phase evidence: N/A with reason: this work changes a TypeScript package export, not an ASSF package-skill lifecycle.
- Next forbidden skip: no skill certification, truth-packet, adapter, or live-proof claim may be inferred.
- Runtime/provider proof: forbidden in T1; deterministic local tests only.
- Claim boundary: package-skill productionization is not part of this tranche.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md` |
| reviewerOwnedClosurePaths | this work order; companion roadmap; completion review; later session-sync surfaces |
| workerReturnAdmission | worker return is evidence, not closure; reviewer independently verifies source, diff, tests, and claims |
| repairAuthority | reviewer may repair in-scope runtime/test/doc defects without expanding writable scope; material repairs must be documented |
| blockedConversion | any required extra path, failing test, stale source, unlinked audit event, provider reachability, or route growth |
| commitConversion | reviewer commits material closure first and session continuity separately |

## Execution Plan

1. Read and source-verify all required surfaces.
2. Run pre-implementation at the captured execution base.
3. Implement and test `checkContext`.
4. Export the gateway without dependency or lockfile changes.
5. Implement and test the singleton.
6. Implement and test the injectable route adapter.
7. Replace route evaluation and use the existing route suite as integration
   proof. Under R1, add
   `appendAuditEventMock.mockResolvedValue({ id: 'audit-test-id' })` in its
   reset/setup path and do not change production code to mask the mock gap.
8. Run typechecks, focused tests, negative searches, line-count proof, and
   file-size enforcement.
9. Run worker-return and reviewer-fast preparation gates.
10. Create the worker return and stop without staging or committing.

## Evidence Requirements

The worker return must include:

- execution base and initial clean status;
- exact name-status output;
- before/after route line counts;
- package export diff;
- focused test and typecheck commands with counts/results;
- `route.test.ts` result `31/31 PASS` after the one-line mock default;
- negative direct-evaluate search;
- exactly-one and same-object evidence;
- all fail-closed zero-provider assertions;
- audit payload and envelope-link assertion;
- no-live/no-network/no-browser/no-CLI/MCP statement;
- final status and terminal disposition.

## Epistemic Process Block

### Expected Result / Prediction

The accepted design should compose without schema expansion and should reduce
the execute route by extracting gateway and audit work.

### Evidence Comparison

The worker compares actual source, tests, and line counts against that
prediction after implementation.

### Contradiction Or Gap Disposition

Any schema expansion, extra writable path, route growth, missing pipeline
result behavior, or provider call on fail-closed cases blocks the return.

### Claim Update

The worker may claim only implementation pending review, never closure or
production readiness.

## Acceptance Criteria

- [ ] `checkContext` preserves the exact fourteen-field context object.
- [ ] Gateway engine evaluation is exactly once.
- [ ] Legacy `check` tests remain passing.
- [ ] Root and runtime package exports resolve.
- [ ] Singleton configuration exactly matches the accepted no-bypass values.
- [ ] Adapter emits and links one durable gateway audit event.
- [ ] Adapter returns both gateway and pipeline results.
- [ ] BLOCK, ESCALATE, BYPASS, missing pipeline result, and disallowed outcomes
      stop before routing/provider.
- [ ] Direct gateway-denied response receipt uses the gateway decision.
- [ ] Route and adapter contain no direct engine evaluation.
- [ ] Route finishes below 959 lines.
- [ ] All focused tests, all 31 existing route tests, and both typechecks pass.
- [ ] Actual changed set stays inside the writable manifest.
- [ ] Worker did not stage or commit.
- [ ] T2-T4 remain held.

## Review Gate

Codex must inspect the complete diff, recompute source facts, run the
reviewer-fast gate, verify route line count and package surface, and decide
closure. Worker success language is not acceptance evidence.

## Operator Checkpoint

N/A with reason: this packet defines complete worker authority. A new schema,
writable path, live proof, public action, or successor release is outside this
work order and requires return-to-orchestrator disposition.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_WORKER_RETURN_2026-07-26.md`

```text
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: python governance/compat/run_worker_return_fast_gate.py
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
requiredEvidenceTerms: executionBaseHead; git status --short
conditionalDispositionRule: include each conditional section with evidence when applicable, otherwise record N/A with reason
```

The worker return must contain:

- `Status: COMPLETE_PENDING_REVIEW` or the selected blocked token;
- execution-base and clean-start evidence;
- Source Verification refresh;
- Work-Order Fulfillment Manifest;
- Required Artifact Manifest reconciliation;
- proof table;
- exact changed-set table;
- route-size table;
- Epistemic Process Block;
- External Knowledge Intake Routing;
- Corpus Completeness And Report Integrity with a valid N/A verdict;
- Rescan Intelligence Hardening;
- Finding-To-Governance Learning Disposition;
- Agent Operation Trace Block;
- Delta Execution Claim Boundary Control Block;
- Public Export Disposition;
- Claim Boundary;
- no staging/commit evidence.

## Verification Commands

Run from repository root unless the command changes directory explicitly:

```powershell
git status --short --untracked-files=all
git diff --name-status
git diff --check
(Get-Content EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts).Count
rg -n "guardEngine\.evaluate|getSharedGuardEngine" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts
Push-Location EXTENSIONS/CVF_GUARD_CONTRACT; npm test -- src/runtime/mandatory-gateway.test.ts; npm run check; Pop-Location
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web; npm run test:run -- src/lib/mandatory-gateway-singleton.test.ts src/lib/route-guard-gateway.test.ts src/app/api/execute/route.test.ts; npm run check; Pop-Location
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py --work-order docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_2026-07-26.md --worker-return docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_WORKER_RETURN_2026-07-26.md
```

The Vitest command signatures were verified against local `npx vitest --help`;
the worker must preserve equivalent non-live filters.

## Closure Checklist

- [ ] Worker return admitted only after independent review.
- [ ] Every acceptance item resolved PASS, N/A with reason, or BLOCKED.
- [ ] Roadmap-to-work-order diff reconciled.
- [ ] No open checkbox remains in a closed artifact.
- [ ] No stale HOLD release claim exists.
- [ ] File and no-live claims have command evidence.
- [ ] Completion review records repairs and test results.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return with the matching blocked token if:

- committed execution base is stale or dirty;
- any required source symbol changed incompatibly;
- a writable path outside the manifest is required;
- route cannot shrink below 959 lines;
- package export requires a lockfile or dependency change;
- tests or typechecks cannot pass in scope;
- any fail-closed branch can reach provider routing;
- durable audit linkage cannot be proven;
- live proof, T2-T4, new surface, checker, session, or public action is needed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50`

Returned defects (20): ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044,
ADIF-0045, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031,
ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Dispatch controls include exact manifests, steward-first commit separation,
explicit durable projection tests, automation-assist worker-return terms,
verified command signatures, and symbol-only source-verification cells.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `WORKER_MUST_NOT_COMMIT`; exact manifest headings; Source Verification columns; Agent Handoff rows; `completionReviewPath`; `reviewerOwnedClosurePaths`; ASCII-only prose |
| gateRunPurpose | confirm the already reviewed worker-executable packet shape and record the gate result as dispatch evidence |
| claimBoundary | gate compliance does not prove implementation |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex packet author and reviewer/dispatcher |
| Provider or surface | local Codex workspace |
| Session or invocation | GC009-GC010-PCALLER-T1 work-order authoring, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, git checks, ADIF resolver, `apply_patch`, workflow gates |
| Target paths | this work order; companion roadmap; system-chain map fingerprint refresh for the clean HEAD package barrel |
| Allowed scope source | explicit human authorization backed by T1I material closure `7b3cdc23a` |
| Before status evidence | reviewer redispatch at HEAD `871251726`; blocked implementation preserved separately while packet gates run on a clean worktree |
| After status evidence | exact three-path reviewer redispatch and mandatory fingerprint-maintenance set |
| Diff evidence | `git status --short`; `git diff --name-status`; `git diff --check` |
| Approval boundary | packet authoring, review, commit, and dispatch only |
| Claim boundary | no worker implementation or runtime behavior yet |
| Agent type | reviewer/dispatcher |
| Invocation ID | `gc009-gc010-production-caller-t1-work-order-2026-07-26` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_2026-07-26.md`; `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`; `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_2026-07-26.md`; `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`; `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded T1 implementation dispatch |
| claimDisposition | CLAIM_REJECTED - work-order authoring is not runtime execution |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source verification and gates |
| invocationBoundary | local governed document workflow |
| interceptionBoundary | no provider, browser, CLI, MCP, process, or runtime interception claim |
| claimLanguage | releases one no-commit worker only after committed reviewer acceptance |
| forbiddenExpansion | no live proof, T2-T4, new surface, checker, session, public, push, deployment, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime work order; no public-sync authority.

## Claim Boundary

This work order authorizes one bounded no-commit T1 implementation after
reviewer acceptance and commit. It does not claim that implementation has
occurred, does not prove invocation, does not close GC-009 or GC-010, and
does not release T2-T4.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: REVIEWER_ACCEPTED_REDISPATCH_READY_R1_ROUTE_TEST_MOCK` | PASS |
| Completion or reviewer artifact | future T1 completion review | absent before worker execution | N/A with reason: independent closure remains pending |
| Baseline status | companion baseline | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| T1I dependency | T1I completion review | material commit `7b3cdc23a` | PASS |
| Worker output | canonical worker return | absent before dispatch | PASS |
| Roadmap state | companion roadmap | T1 dispatch-ready; T2-T4 held | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no corpus packet created | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no corpus entry required | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | N/A with reason |
| System loop interlock | GC-009/GC-010 gap entry | remains `IMPLEMENTED_NOT_INVOCATION_PROVEN` | PASS |
| Session continuity | separate session-sync commit | follows material dispatch commit | N/A with reason: not worker-owned |
| Public export | this work order | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required assertion | Evidence source | Expected result | Status |
|---|---|---|---|
| Source facts are current | Source Verification Block | all existing claims ACCEPT or corrected REJECT | PASS |
| Dependency is released | Dependency Release Evidence | T1I ready plus operator authority | PASS |
| Writable scope is exhaustive | Required Artifact Manifest | every behavior-changing path listed | PASS |
| Worker has not executed | clean worktree and absent worker return | no runtime output | PASS |
| Dispatch gates pass | author/reviewer/pre-dispatch receipts | author-fast PASS; full pre-dispatch and commit steward required before commit | PASS |
| T2-T4 remain held | roadmap and Claim Boundary | no successor release | PASS |
