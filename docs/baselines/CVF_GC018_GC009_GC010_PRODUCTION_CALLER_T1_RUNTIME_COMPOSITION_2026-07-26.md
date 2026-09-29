# CVF GC-018 GC-009/GC-010 Production Caller T1 Runtime Composition

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: GC009-GC010-PCALLER-T1

Date: 2026-07-26

Dispatch base head: `7275e9dc8`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded implementation tranche that adds the accepted
context-preserving mandatory-gateway interface, exposes it through the
guard-contract package, creates one cvf-web singleton and one route adapter,
and replaces the execute route's direct guard-engine evaluation with exactly
one mandatory-gateway evaluation before provider routing.

This tranche implements only the T1 production composition specified by the
independently closed T1I design. It does not run a live provider proof, close
GC-009 or GC-010, release T2-T4, add a new operator surface, or make a
production-readiness claim.

## Scope / Target / Owner Boundary

The no-commit implementation worker may modify or create exactly the runtime,
test, package, and worker-return paths listed in the companion work order.
The worker may not edit this baseline, the work order, the roadmap, completion
reviews, session state, handoffs, governance checkers, public-sync, or any
other path.

The reviewer/closer owns work-order status conversion, roadmap conversion,
completion review, continuity, and commits.

## Decision / Baseline / Proposed Tranche

T1 uses the accepted T1I design:

- add `MandatoryGateway.checkContext(context: GuardRequestContext)` while
  retaining the legacy `check` entry point;
- export the gateway through the canonical `cvf-guard-contract` package;
- create a cvf-web singleton configured with `enforceAll: true`,
  `hardBlock: true`, `hardEscalate: true`, `bypassActions: []`, and
  `defaultControlMode: 'governed'`;
- create a route adapter that accepts the canonical Web context, evaluates
  the gateway exactly once, persists a secret-safe gateway audit event, links
  its ID into the existing envelope, and returns both `GatewayResult` and the
  required `GuardPipelineResult`;
- replace the execute route's direct `guardEngine.evaluate` call with the
  adapter and fail closed before provider routing for BLOCK, ESCALATE,
  BYPASS, a missing pipeline result, or any disallowed result;
- extract enough route-local gateway work into the adapter that the active
  GC-023 owner `route.ts` is smaller after T1 than at dispatch base;
- add deterministic local tests only, with provider seams mocked.

## Evidence / Verification

Dispatch evidence is:

- T1I material closure `7b3cdc23a`;
- T1I continuity commit `7275e9dc8`;
- current runtime and package source cited below;
- the fresh ADIF resolver result;
- the exact three-path packet-author changed set;
- successful author, reviewer, pre-dispatch, and commit-steward gates.

Worker evidence must be recomputed from the worker's captured execution base.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition | Status |
|---|---|---|---|---|
| T0A owner-design closure | `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` | `0e97a0ace` | preferred cvf-web singleton sibling identified; interface change required | PASS |
| T1I interface-design closure | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md` | `7b3cdc23a` | `CLOSED_PASS_BOUNDED_INTERFACE_SPEC_READY_FOR_FRESH_T1_RUNTIME_PACKET` | PASS |
| Human authorization | explicit approval after continuity commit `7275e9dc8` | N/A with reason: conversation authority is recorded in this governed packet and the later continuity sync | explicitly authorizes a fresh source-verified T1 runtime packet; T2-T4 remain held | PASS |
| Gap registry state | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | current at dispatch base | remains `IMPLEMENTED_NOT_INVOCATION_PROVEN`; T1 is not closure proof | PASS |

This table releases packet authoring and, after reviewer acceptance and
commit, bounded T1 implementation only. It does not release T2-T4.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | N/A with reason: the accepted T1I baseline and work order are the same-lane checker-compliant scaffold source |
| generatedProfile | runtime implementation plus no-commit worker and held-successor profiles |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced documentation-only design scope with the T1I-accepted runtime, package, adapter, test, and GC-023 shrink scope |
| checkerReadAheadConfirmation | dispatch-quality, source-verification, manifest, prompt-envelope, handoff, operation-trace, file-size, and authority checkers reviewed before authoring |
| docOnlyNewFields | proposed file names and helper symbols below remain doc-only until the worker creates them |
| claimBoundary | packet provenance only; no runtime behavior has yet changed |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1I releases a fresh T1 packet checkpoint | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md` | Findings / Position; Claim Boundary | `INTERFACE_SPEC_READY_FOR_FRESH_T1_RUNTIME_PACKET` | T1I completion review | ACCEPT |
| Accepted sibling method and configuration | VALUE_SET | `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | Required Design Question Answers 1-4 | `checkContext`; `bypassActions` | T1I audit decision | ACCEPT |
| Current gateway has no context-preserving sibling | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 66-178 | `MandatoryGateway`; `check` | guard-contract runtime gateway | ACCEPT |
| Current gateway result contains optional pipeline result and nested evidence | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 36-49 | `GatewayResult`; `guardResult`; `evidence` | gateway result contract | ACCEPT |
| Current gateway bypass is substring based | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 95-107 | `bypassActions`; `check` | gateway configuration and evaluation | ACCEPT |
| Canonical Web context contains fourteen fields | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 93-110 | `GuardRequestContext` | guard-contract request schema | ACCEPT |
| Downstream route consumers require the pipeline result shape | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 578-935 | `guardResult` | execute POST route | ACCEPT |
| Route currently evaluates the shared engine directly | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 561-580 | `getSharedGuardEngine`; `guardEngine.evaluate` | execute POST route | ACCEPT |
| Existing Web builder creates the canonical context | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts` | lines 86-129 | `buildWebGuardContext` | Web guard runtime adapter | ACCEPT |
| Gateway is absent from package exports and files | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | package `exports` and `files`; barrel runtime exports | `exports`; `files`; named exports | guard-contract package surface | ACCEPT |
| Existing shared engine singleton is reusable by a sibling gateway singleton | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | full file | `getSharedGuardEngine`; `resetSharedGuardEngine` | cvf-web shared engine owner | ACCEPT |
| Audit persistence returns an event ID | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 96-152 | `appendAuditEvent` | control-plane event store | ACCEPT |
| Envelope supports audit-ID linkage | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 287-292 | `appendAuditEventToEnvelope` | Web governance envelope | ACCEPT |
| Receipt builder accepts a decision but no typed gateway summary | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 55-78, 241-280 | `buildEvidenceReceipt` | Web evidence receipt builder | ACCEPT |
| Execute route is an active GC-023 owner | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | `activeOwners` execute-route entry | `activeOwners`; `status` | governed file-size registry | ACCEPT |

## New Doc-Only Fields

| Proposed item | Documentation meaning | Runtime/source status |
|---|---|---|
| `getSharedMandatoryGateway` | cvf-web singleton accessor backed by `getSharedGuardEngine` and the accepted no-bypass config | DOC_ONLY_NEW until worker implementation |
| `resetSharedMandatoryGateway` | test-only singleton reset paired with the accessor | DOC_ONLY_NEW until worker implementation |
| `evaluateRouteMandatoryGateway` | async route adapter that evaluates once, persists and links gateway audit evidence, and returns gateway plus pipeline results | DOC_ONLY_NEW until worker implementation |
| `MANDATORY_GATEWAY_EVALUATED` | audit event type for the secret-safe gateway summary | DOC_ONLY_NEW until worker implementation |
| `route.mandatory-gateway.test.ts` | focused route-level no-provider fail-closed proof | DOC_ONLY_NEW until worker implementation |

## Current Runtime Freshness Verification

At dispatch base `7275e9dc8`, the gateway still exposes only `check`, the
package still omits the gateway, and the execute route still calls
`guardEngine.evaluate(guardContext)` directly. The route is 959 lines and is
an active GC-023 owner. The worker must recompute these facts at its own
execution base and stop if any is stale.

## Negative Search And Collision Discipline

Before canonical packet creation, the new T1 batch ID and file paths had no
matches. The proposed helper names appear only in this packet and the accepted
T1I design until implementation. `GuardRuntimeEngine` references must resolve
to `cvf-guard-contract`; the MCP-local same-name class is not an acceptable
source or owner.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50`

Returned defects (20): ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044,
ADIF-0045, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031,
ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Dispatch impact: exact manifests prevent aggregate authority expansion;
package export work is writable because source rejects its current omission;
durable projection receives explicit negative tests; no value or type is
placed in a source-verification symbol cell.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | exact status token; Source Verification columns; Required Artifact Manifest; Agent Handoff Contract rows; GC-023 active-owner evidence; ASCII-only prose |
| gateRunPurpose | confirm the already reviewed source-backed dispatch shape and record gate output as evidence before worker release |
| claimBoundary | checker preparation only; PASS will be recorded only after execution |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | implement the accepted T1I gateway interface and minimal cvf-web production composition |
| scopeClassification | bounded runtime and deterministic local-test tranche |
| riskSensitivity | R1 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | Codex reviewer/dispatcher releases; one no-commit implementation worker executes; Codex reviewer/closer accepts and commits |
| escalationCondition | any live provider, new surface, checker, session, public, T2, T3, or T4 requirement |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | dispatcher, implementation worker, reviewer/closer | exact writable manifest and no-commit route | source diff, local tests, worker return | governed repository workflow | `IMPLEMENTATION_AUTHORIZED` |
| `EXTERNAL_AGENT_CLI_MCP` | not used by T1 | no invocation or adapter authority | N/A with reason: T1 is cvf-web runtime composition only | none | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: canonical CVF source and accepted reviews are sufficient |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and companion work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | provider-local memory and conversation are not source authority |

## Epistemic Process Block

### Expected Result / Prediction

The accepted T1I contract should fit the current source with one package
export, two guard-contract edits, two new cvf-web helpers, one bounded route
replacement, and deterministic tests.

### Evidence Comparison

Current source confirms the method, package, singleton, route, audit, envelope,
and test seams. It also adds one constraint: downstream route behavior needs
the underlying `GuardPipelineResult`, so the adapter must return it and fail
closed if it is unexpectedly absent.

### Contradiction Or Gap Disposition

Any inability to preserve downstream pipeline-result behavior, shrink the
active route owner, or prove zero provider calls on fail-closed branches
blocks closure and returns the packet to the reviewer.

### Claim Update

Packet authoring is source-supported. Runtime readiness remains contingent on
worker execution and independent closure.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex packet author and reviewer/dispatcher |
| Provider or surface | local Codex workspace |
| Session or invocation | GC009-GC010-PCALLER-T1 packet authoring, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, git read-only checks, ADIF resolver, `apply_patch`, autorun gates |
| Target paths | this baseline; companion work order; companion roadmap |
| Allowed scope source | explicit human authorization after T1I continuity commit `7275e9dc8` |
| Before status evidence | HEAD `7275e9dc8`; clean worktree |
| After status evidence | exact three-path packet-author changed set pending review |
| Diff evidence | `git status --short`; `git diff --name-status`; `git diff --check` |
| Approval boundary | packet authoring and dispatch review only; worker implementation starts only after committed dispatch |
| Claim boundary | repo-local trace only; no runtime execution claim |
| Agent type | reviewer/dispatcher |
| Invocation ID | `gc009-gc010-production-caller-t1-packet-2026-07-26` |
| Expected manifest | this baseline; companion work order; companion roadmap |
| Actual changed set | same three paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | source-verified T1 runtime implementation dispatch packet |
| claimDisposition | CLAIM_REJECTED - packet authoring does not implement or execute runtime behavior |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no runtime receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source verification and dispatch gates |
| invocationBoundary | governed local document authoring only |
| interceptionBoundary | no provider, browser, CLI, MCP, or runtime interception claim |
| claimLanguage | authorizes bounded implementation only after committed reviewer acceptance |
| forbiddenExpansion | no live proof, T2-T4, new surface, checker, session, public-sync, push, deployment, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation packet; no public-sync authority.

## Claim Boundary

This baseline authorizes only the exact T1 implementation and local
deterministic proof described here after reviewer acceptance and commit. It
does not itself change runtime behavior, prove invocation, close GC-009 or
GC-010, or release T2-T4.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Work order status | companion T1 work order | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future T1 completion review | absent before worker execution | N/A with reason: independent closure remains pending |
| Dependency release | T1I completion review | material commit `7b3cdc23a`; interface spec ready | PASS |
| Roadmap state | companion roadmap | T1 dispatch-ready; T2-T4 held | PASS |
| Worker outputs | runtime/test paths and worker return | absent before dispatch | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no corpus packet created | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no corpus entry required | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | N/A with reason |
| System loop interlock | GC-009/GC-010 gap entry | remains `IMPLEMENTED_NOT_INVOCATION_PROVEN` | PASS |
| Session continuity | separate session-sync commit | follows the material dispatch commit | N/A with reason: not a baseline-owned mutation |
| Public export | this baseline | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required assertion | Dispatch evidence | Expected result | Status |
|---|---|---|---|
| T1I predecessor is independently closed | completion review at `7b3cdc23a` | exact ready token | PASS |
| Source symbols exist and omissions are explicit | Source Verification Block | no guessed runtime field | PASS |
| Writable manifest covers every behavior change | companion work order | exact runtime, package, test, and return paths | PASS |
| Successor holds remain | roadmap and Claim Boundary | T2-T4 held | PASS |
| No worker executed before dispatch | git status and absent worker return | no implementation output | PASS |
