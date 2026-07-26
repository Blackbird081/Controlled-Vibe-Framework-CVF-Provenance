# CVF GC-018 Baseline - GC009 GC010 Production Caller T2 Deterministic Invocation Proof

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: GC009-GC010-PCALLER-T2

Dispatch base head: `14434bf58`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer/dispatcher/closer: Codex

Worker target: one documentation-and-test worker

## Purpose

Release the roadmap's bounded T2 proof after independent T1 closure. T2 may add
one focused deterministic route-level test suite and its worker return. It must
prove that the real T1 composition admits an ALLOW request to the existing
provider-call seam and fails closed before that seam for a real gateway BLOCK.

## Scope / Target / Owner Boundary

This is a test-and-evidence tranche. The worker may create:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.mandatory-gateway-invocation.test.ts`;
2. `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_WORKER_RETURN_2026-07-26.md`.

The worker must not modify runtime source, the existing 1153-line
`route.test.ts`, package metadata, governance checkers, session state, the
roadmap, this baseline, or the work order. Provider execution remains mocked;
no network or live-provider call is authorized.

## Decision / Baseline / Proposed Tranche

| Field | Decision |
|---|---|
| T1 predecessor | independently closed at material commit `29e7d6956` |
| continuity checkpoint | `14434bf58` |
| T2 implementation class | focused deterministic route-level test plus governed worker return |
| positive proof | actual POST route, actual T1 gateway composition, actual guard engine, mocked provider seam called exactly once |
| negative proof | actual POST route, actual T1 gateway composition, source-backed gateway BLOCK, mocked provider seam called zero times |
| receipt/audit proof | `MANDATORY_GATEWAY_EVALUATED` event and response evidence receipt agree with each decision |
| live proof | forbidden |
| runtime mutation | forbidden |
| later tranches | T3-T4 and GC-010 remain held |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC009-GC010-PCALLER-T2 --title "GC009 GC010 Production Caller T2 Deterministic Invocation Proof" --date 2026-07-26 --base 14434bf58 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1 bounded closure at material commit 29e7d6956 and continuity commit 14434bf58" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus `WORKER_MUST_NOT_COMMIT` profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with current T1 closure evidence, exact test contract, manifests, source facts, and bounded no-live claim |
| checkerReadAheadConfirmation | dispatch-quality, dispatch tables, prompt envelope, handoff boundary, governed file size, worker-return quality, operation trace, and packet authority/encoding checker sources |
| docOnlyNewFields | batch and artifact names only; no runtime field is introduced |
| claimBoundary | dispatch authoring provenance only; no T2 execution or behavior claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T1 independent closure | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md`; material commit `29e7d6956` | completion status must be closed bounded and T1 tests/gates accepted | PASS |
| continuity refresh | `CVF_SESSION/state/entries/gc009Gc010ProductionCallerT1RuntimeCompositionClosure20260726.json`; commit `14434bf58` | next move must require explicit human selection of a fresh T2 packet | PASS |
| operator release | explicit operator message `Dong y` after Codex recommended T2 first | authority is recorded in this governed packet; no provider-local file is source authority | PASS |
| clean dispatch base | `git status --short` empty at `14434bf58` before packet authoring | packet authoring must begin from an isolated clean base | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1 closed bounded and T2 stayed held | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md` | Findings / Position; Claim Boundary | `CLOSED_PASS_BOUNDED_GC009_COMPOSED` | T1 completion review | ACCEPT |
| Roadmap defines deterministic positive and fail-closed negative T2 proof | VALUE_SET | `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | T2 - Positive And Fail-Closed Negative Invocation Proof | `T2` | roadmap tranche contract | ACCEPT |
| Execute route invokes the T1 wrapper before provider routing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 560-590 | `runExecuteRouteMandatoryGateway` | execute POST route | ACCEPT |
| Existing execution seam is the provider adapter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 771-778 | `executeAI` | execute POST route | ACCEPT |
| T1 wrapper defaults to the real shared mandatory gateway | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 43-47, 111-122 | `evaluateRouteMandatoryGateway`; `runExecuteRouteMandatoryGateway` | route gateway adapter | ACCEPT |
| T1 wrapper returns a 400 fail-closed response before continuation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 124-146 | `blockedResponse` | route gateway adapter | ACCEPT |
| Gateway singleton uses the shared real engine and no bypass actions | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | lines 20-33 | `getSharedMandatoryGateway` | cvf-web gateway singleton | ACCEPT |
| Test reset seams exist for engine and gateway isolation | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` | reset functions | `resetSharedGuardEngine`; `resetSharedMandatoryGateway` | cvf-web singleton test seams | ACCEPT |
| Explicit request action flows into the guard context | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-route-guards.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `resolveGuardAction`; lines 561-576 | `action` | execute guard context builder | ACCEPT |
| `delete_governance` is not allowed for OPERATOR and therefore yields a deterministic authority BLOCK | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `AUTHORITY_MATRIX`; `AuthorityGateGuard.evaluate` | `delete_governance` | authority gate | ACCEPT |
| Audit adapter emits the seven-field gateway event and links its ID | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 49-75 | `MANDATORY_GATEWAY_EVALUATED` | route gateway adapter | ACCEPT |
| Existing route suite supplies stable mock/reset patterns | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | lines 1-120 | `beforeEach` | execute route test suite | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `GC009-GC010-PCALLER-T2` | governed T2 batch identifier | DOC_ONLY_NEW |
| `route.mandatory-gateway-invocation.test.ts` | focused deterministic test filename | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

| Check | Current evidence | Disposition |
|---|---|---|
| HEAD | `14434bf58` before authoring | PASS |
| route line count | 955 | PASS |
| existing route test line count | 1153; excluded from worker writes | PASS |
| T1 invocation location | `route.ts` calls `runExecuteRouteMandatoryGateway` before provider routing | PASS |
| provider seam location | `route.ts` calls `executeAI` after the T1 wrapper | PASS |
| no-live boundary | focused tests use a fake key and mocked `executeAI` | PASS |

## Evidence / Verification

Packet acceptance requires an exact three-path packet-author diff, clean
`git diff --check`, dispatch-packet author gate PASS, pre-dispatch autorun
PASS over the packet-author range, and commit-steward PASS before commit.
Worker execution evidence is separately defined by the companion work order
and is not created by this baseline.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Four proposed paths | `Test-Path` returned false for the baseline, work order, worker return, and focused test before authoring | PASS |
| Exact T2 artifact tokens | `rg -n "GC009-GC010-PCALLER-T2|DETERMINISTIC_INVOCATION_PROOF|mandatory-gateway-invocation" docs CVF_SESSION EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute` returned no match before authoring | PASS |
| Collision decision | use the fresh T2 names in this packet; do not reuse the T1 abandoned focused-test name without the T2 suffix semantics | PASS |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`,
`ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`,
`ADIF-0044`, `ADIF-0045`, `ADIF-0007`, `ADIF-0016`, `ADIF-0017`,
`ADIF-0024`, `ADIF-0031`, `ADIF-0039`, `ADIF-0043`, `ADIF-0049`,
`ADIF-0006`.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 20 |
| Disclosed defectIds | all 20 IDs listed above |
| Dispatch impact | exact manifests, current source lines, checker read-ahead, worker-return gate, test reset isolation, no-live boundary, and no-commit closure conversion are explicit |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | exact status token; Source Verification columns; manifest headings; no-commit handoff rows; ASCII-only prose |
| gateRunPurpose | confirm dispatch shape after source review and before worker release |
| claimBoundary | checker preparation only; gate PASS does not prove T2 behavior |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | add deterministic route-level proof for the already composed GC-009 gateway edge |
| scopeClassification | bounded test and evidence tranche |
| riskSensitivity | R1 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | Codex authors and dispatches; one no-commit worker executes; Codex independently reviews, closes, and commits |
| escalationCondition | any runtime mutation, live provider, browser, CLI/MCP, new operator surface, GC-010, T3-T4, session, public, push, or deployment need |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | dispatcher, test worker, reviewer/closer | exact two-path worker manifest and no-commit route | focused route tests and worker return | governed repository workflow | `TEST_EXECUTION_AUTHORIZED` |
| `EXTERNAL_AGENT_CLI_MCP` | not used | no adapter or invocation authority | N/A with reason: T2 is local deterministic proof | none | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime source verification and deterministic local proof |
| Matching local-view guard | N/A with reason: no external artifact is absorbed |
| Owner surface | this GC-018 and companion work order |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for T2 behavior until independent closure |
| Claim boundary | no external-source completeness claim |

## Epistemic Process Block

### Expected Result / Prediction

The real T1 gateway chain should produce ALLOW for an authorized OPERATOR
analysis request and BLOCK for the explicit unauthorized
`delete_governance` action. Only the ALLOW case should call mocked `executeAI`.

### Evidence Comparison

Worker must compare actual response, provider-call count, gateway audit
payload, request ID, and receipt decision with that prediction.

### Contradiction Or Gap Disposition

Any different gateway decision, missing audit link, provider call on denial, or
need to mock the gateway is `BLOCKED_SOURCE_DRIFT` or
`BLOCKED_SCOPE_EXPANSION_REQUIRED`.

### Claim Update

Only reviewer-accepted test evidence may advance T2; packet readiness alone
does not.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex packet author and reviewer/dispatcher |
| Provider or surface | local Codex workspace |
| Session or invocation | GC009-GC010-PCALLER-T2 packet authoring, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, git checks, scaffold helper, ADIF resolver, patch edits, workflow gates |
| Target paths | this baseline; companion work order; companion roadmap |
| Allowed scope source | explicit operator T2 selection backed by material commit `29e7d6956` and continuity commit `14434bf58` |
| Before status evidence | clean worktree at `14434bf58` |
| After status evidence | exact packet-author changed set |
| Diff evidence | `git status --short`; `git diff --name-status`; `git diff --check` |
| Approval boundary | packet authoring, review, commit, and dispatch only |
| Claim boundary | no worker test execution or runtime behavior claim |
| Agent type | reviewer/dispatcher |
| Invocation ID | `gc009-gc010-production-caller-t2-baseline-2026-07-26` |
| Expected manifest | this baseline; companion work order; companion roadmap |
| Actual changed set | must match expected manifest before packet commit |
| Manifest delta | none expected |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic proof packet for one already-existing GC-009 route composition |
| claimDisposition | `CLAIM_REJECTED`: packet authoring is not invocation evidence |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: none at dispatch; worker must collect deterministic response receipt assertions |
| actionEvidence | `CLAIM_REJECTED_NO_ACTION`: none at dispatch; worker must prove mocked provider seam counts |
| invocationBoundary | local Vitest POST invocation only |
| interceptionBoundary | no external-agent interception, wrapper, proxy, or arbitrary process control |
| claimLanguage | T2 test-and-evidence packet is dispatch-ready |
| forbiddenExpansion | no live provider, runtime source mutation, GC-010, T3-T4, public-sync, push, deployment, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this private provenance dispatch packet has no corresponding
public-sync artifact and makes no public catalog claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Work order status | companion T2 work order | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future T2 completion review | absent before worker execution | N/A with reason: independent closure remains pending |
| Dependency release | T1 completion review | material commit `29e7d6956`; continuity commit `14434bf58` | PASS |
| Roadmap state | companion roadmap | T2 dispatch-ready; T3-T4 held | PASS |
| Worker outputs | focused test and worker return | absent before dispatch | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no corpus packet created | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no corpus entry required | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | N/A with reason |
| System loop interlock | GC-009/GC-010 gap entry | remains `IMPLEMENTED_NOT_INVOCATION_PROVEN` pending T2 acceptance and GC-010 | PASS |
| Session continuity | separate session-sync commit | follows material packet commit | N/A with reason: not baseline-owned |
| Public export | this baseline | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required assertion | Dispatch evidence | Required value | Observed value | Status |
|---|---|---|---|---|
| T1 predecessor closure | T1 completion review and commits | `CLOSED_PASS_BOUNDED_GC009_COMPOSED` | `CLOSED_PASS_BOUNDED_GC009_COMPOSED` | PASS |
| T2 dependency release | dependency table | all rows PASS | all rows PASS | PASS |
| Worker writable scope | companion work order manifest | exactly two paths | exactly two paths | PASS |
| Runtime mutation authority | Scope / Target / Owner Boundary | forbidden | forbidden | PASS |
| Live-provider authority | Decision table and Claim Boundary | forbidden | forbidden | PASS |
| T3-T4 and GC-010 state | roadmap and Claim Boundary | held | held | PASS |

## Claim Boundary

This baseline releases only the exact test-and-evidence T2 work order. It does
not prove T2, authorize runtime changes or live governance proof, instantiate
GC-010, release T3-T4, modify session state, or authorize public export.
