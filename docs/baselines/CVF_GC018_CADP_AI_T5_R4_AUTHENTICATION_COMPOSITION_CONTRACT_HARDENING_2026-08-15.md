# CVF GC-018 Baseline - CADP AI T5-R4 Authentication Composition Contract Hardening

Memory class: governed-dispatch-baseline

rawMemoryReleased=false

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: CADP-AI-T5-R4

Dispatch base head: `07a4b55d7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Dispatcher/reviewer/closer: role-separated governed agents

Worker target: one documentation-contract worker in a later bounded phase

## Purpose

Release a documentation-only contract-hardening tranche that converts the
accepted T5-R3 owner decision into an implementation-ready authentication
composition specification. No production source, test, route, authentication,
runtime, provider, public, or deployment change is authorized.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T5-R4 --title "CADP AI T5 R4 Authentication Composition Contract Hardening" --date 2026-08-15 --base 07a4b55d7 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T5-R3 accepted bounded at 6ae59fa88; implementation deferred by continuity 07a4b55d7" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact authority, source, contract, output, no-commit, and review boundaries |
| checkerReadAheadConfirmation | applicable dispatch, prompt, handoff, source, trace, delta, structure, return, public, and file-size checker sources were read before authoring |
| docOnlyNewFields | credential precedence state machine; body boundary; principal provenance; proof clock; receipt disposition; implementation manifest; test matrix |
| claimBoundary | dispatch provenance and contract design only; no runtime or authentication behavior is changed |

## Scope / Target / Owner Boundary

The later worker may create exactly:

1. `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md`;
2. `docs/reviews/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_HARDENING_WORKER_RETURN_2026-08-15.md`.

All source, test, route, authentication configuration, registry, roadmap,
baseline, work-order, completion, governance, session, public-sync, deployment,
and generated-state paths are read-only or forbidden to the worker.

## Worker Autonomy / No-Question Rule

The worker repairs documentation and checker failures inside the exact two-path
Allowed scope and reruns the failed command without seeking confirmation.
Escalation is reserved for source contradiction, stale execution base,
forbidden-path need, scope or risk expansion, credentials, external
invocation, public action, deployment, or destructive work.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T5-R3 bounded decision | completion review and material commit `6ae59fa88` | route proof helper selected only as authentication-composition owner | PASS |
| continuity checkpoint | session commit `07a4b55d7` | fresh source-verified hardening or design dispatch allowed | PASS |
| operator selection | explicit T5-R4 instruction on 2026-08-15 | create the governed work order for later worker execution | PASS |
| current source | exact helper, token, session, Auth.js, and focused-test symbols verified from current HEAD | no source contradiction blocks contract design | PASS |
| clean base | empty status at `07a4b55d7` | isolated dispatch authoring | PASS |

## Decision / Baseline / Proposed Tranche

| Field | Decision |
|---|---|
| selected composition owner | `authorizeRouteGovernanceProof` |
| owner limit | authentication composition only |
| credential precedence | contract must decide invalid-token plus valid-session behavior explicitly |
| body boundary | body text captured before verification and parsing; no transport-byte claim |
| CADP authorization | separate later owner; not supplied by authentication proof |
| durable receipt | separate explicit disposition; current helper does not persist one |
| proof time | contract must require injected deterministic time |
| production configuration | contract must require fail-closed non-test/non-development configuration |
| implementation | forbidden in T5-R4 |
| terminal result | exactly one readiness token in the reference contract |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| route registry and authentication composition exist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 25-61 and 118-208 | `ROUTE_GOVERNANCE_PROOF_REGISTRY`; `authorizeRouteGovernanceProof` | CVF Web route governance | ACCEPT |
| invalid presented token may fall through to session | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 132-179 | `authorizeRouteGovernanceProof` | CVF Web route governance | ACCEPT |
| deny proof sets null actor identity | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 181-208 | `buildProof` | CVF Web route governance | ACCEPT |
| proof time uses ambient wall clock | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 89-115 | `buildProof` | route proof generator | ACCEPT |
| service signature covers timestamp and body text and accepts optional time | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 27-67 | `computeServiceRequestSignature`; `verifyServiceTokenRequest` | service-token authentication | ACCEPT |
| test environment shortcut skips signature and timestamp checks after token match | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 47-53 | `verifyServiceTokenRequest` | service-token authentication | ACCEPT |
| session verifier carries role and impersonation provenance | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 19-30 and 81-156 | `SessionCookie`; `verifySessionCookie` | middleware authentication | ACCEPT |
| Auth.js configuration includes mock/default fallbacks | RISK_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | lines 30-79 | `authSecret`; `nextAuthConfig` | Auth.js configuration | ACCEPT |
| focused tests omit invalid-token plus valid-session and injected-proof-time cases | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | tests at lines 39-100 | `authorizeRouteGovernanceProof` test suite | route proof tests | ACCEPT |
| production-mode token test covers valid and bad signature paths | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | lines 27-52 | `verifyServiceTokenRequest` test suite | service-token tests | ACCEPT |
| T5-R3 accepted only bounded composition ownership | GOVERNED_DECISION | `docs/reviews/CVF_CADP_AI_T5_R3_EXTERNAL_AUTHENTICATION_OWNER_ADOPTION_READINESS_DECISION_COMPLETION_2026-08-15.md` | Findings / Position; Disposition | `SELECT_ROUTE_GOVERNANCE_PROOF_OWNER_BOUNDED` | T5-R3 completion authority | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| four proposed T5-R4 paths | all `Test-Path` results were false before authoring | PASS |
| batch/title collision | targeted search over governed docs and session state returned no match before authoring | PASS |
| source symbols | exact symbol searches returned current lines listed above | PASS |
| collision decision | create a new T5-R4 packet and do not overwrite T5-R3 authority | PASS |

## Evidence / Verification

Dispatch acceptance requires the exact two-path packet-authoring changed set,
source and collision evidence above, clean diff, governed file-size compliance,
pre-dispatch autorun PASS over `07a4b55d7`, and dispatch commit-steward PASS.
The later worker must independently reproduce current source and return both
owned docs without staging or commit.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact source facts, role-neutral worker ownership, two-path manifest, no-commit handoff, literal-safe output shape, and reviewer conversion are explicit |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status; source table columns; scaffold fields; prompt placement; handoff fields; trace labels; Delta fields; no-commit return profile; public disposition |
| gateRunPurpose | confirm packet shape after source and checker read-ahead |
| claimBoundary | checker compliance is not contract correctness or authentication implementation proof |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | proposed T5-R4 reference contract | documentation-only design authority | T5-R3 decision plus current source | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible future CADP ingress through route proof helper | authentication only; CADP authorization and receipt remain separate | no current CADP CLI/MCP route | adapter implementation requires fresh packet | `DEFERRED_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | CADP-AI-T5-R4 dispatch authoring, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, scaffold helper, ADIF resolver, patch edits, governance gates |
| Target paths | this baseline and companion work order |
| Allowed scope source | explicit operator instruction selecting the proposed T5-R4 tranche |
| Before status evidence | clean HEAD `07a4b55d7` |
| After status evidence | exact baseline and work-order dispatch set |
| Diff evidence | status, name-status, and diff check before commit |
| Approval boundary | documentation-contract dispatch only |
| Claim boundary | no source/test/auth/runtime/live/public/deployment action |
| Agent type | dispatcher/reviewer |
| Invocation ID | `cadp-ai-t5-r4-dispatch-2026-08-15` |
| Expected manifest | baseline and work order |
| Actual changed set | must match before material commit |
| Manifest delta | none expected |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only authentication composition contract dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime control or authentication behavior is created |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no route or authentication action occurs |
| invocationBoundary | local source inspection and documentation gates |
| interceptionBoundary | no HTTP, CLI, MCP, provider, browser, or process interception |
| claimLanguage | packet is dispatch-ready for contract authoring only |
| forbiddenExpansion | no source/test/route/auth/runtime/live/public/deployment change |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded source set only; no complete-corpus claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch only.

## Claim Boundary

This baseline authorizes a later no-commit worker to create one authentication
composition reference contract and one worker return. It does not authorize
production source, tests, route registration, authentication execution,
credentials, HTTP/CLI/MCP/provider use, public sync, deployment, or production
readiness.
