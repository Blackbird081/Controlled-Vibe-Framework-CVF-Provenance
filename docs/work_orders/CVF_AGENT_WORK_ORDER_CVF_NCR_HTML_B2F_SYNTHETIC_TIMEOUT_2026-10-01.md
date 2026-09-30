# CVF Agent Work Order - NCR HTML B2f Synthetic Timeout

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT

Dispatch base head: `b882d5d59`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md`

## Dispatch Prompt Envelope

Role: internal worker creating test-only real-browser timeout transport proof and its bounded evidence; Local is reviewer/closer.

Canonical packet: this work order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Capture executionBaseHead and status at start. Do not edit before the bound pre-implementation gate passes.

Current-time notes: use synthetic form fields and a fresh local Next test server. A test-only harness starts a delayed non-forwarding loopback HTTP stub first, binds `NEXTAUTH_URL` to that exact stub origin, `AUTH_URL` to fresh Next, sets a 1,000 ms receipt timeout and disables the Governance Engine. The browser calls the actual export route without intercepting it. If stub origin, auth, timeout inheritance or isolation preflight is uncertain, stop before export. No provider, real data or authoritative store.

Do-not-misread notes: B2e proved invalid/unavailable synthetic configured-hop failures. B2f covers only `TIMED_OUT` and ambiguous-outcome presentation. Abort does not prove that remote work stopped, no receipt does not imply safe retry, and a fabricated `PRESENT` is forbidden. `NEXT_PUBLIC_CVF_MOCK_AI=1` does not disable the receipt hop. The actual Next evaluate route and engine are forbidden destinations. Do not edit production code even if the test finds a defect.

Required first actions: read active continuity, this packet, paired baseline, D050 B2f branch-gap audit, B2e harness/spec as read-only precedent, export route/receipt helper, Next evaluate route, engine HTTP client, auth config, existing Playwright config, panel and named checker sources; capture HEAD and status; run the bound pre-implementation gate before edits.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, exact five-path changed set, loopback-stub preflight and secret-safe request ledger, focused real-route browser result, TypeScript/lint, worker-return fast gate, no commit.

## Purpose

Observe, in a real test browser, the actual export route's receipt POST reaching a delayed inert loopback stub and returning `TIMED_OUT` with the same attempt ID while the panel warns that processing may have occurred and the artifact remains draft. Do not call the real Next evaluate route or engine or change production code. Profile A and Q001/Q004 stay open.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | standing delegation of Local work-order decisions and the 2026-10-01 request to continue | ACCEPT for B2f packet only; no real-data/effect grant |
| Current continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, next allowed move | ACCEPT; synthetic B2f packet only |
| NCR roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D049-D050/Q001/Q004 | ACCEPT for timeout-only synthetic packet |
| Local audit | `docs/reviews/CVF_CVF_NCR_HTML_B2F_RECEIPT_BRANCH_GAP_AUDIT_2026-10-01.md`, Decision | ACCEPT for controlled timeout gap and delayed-stub test design |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md` | ACCEPT for exact scope, subject to committed release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Export route calls receipt helper and returns its status and attempt ID | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | final POST block | `fetchGovernanceReceipt`, `governanceReceiptAttemptId` | HTML export route | ACCEPT |
| Helper resolves `NEXTAUTH_URL` and POSTs to configured URL | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `resolveEvaluateUrl`, `fetchGovernanceReceipt` | `NEXTAUTH_URL`, `fetch` | receipt helper | ACCEPT |
| Actual Next evaluate route can forward to Governance Engine | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evaluate/route.ts` | POST | `governanceEvaluate` | forbidden destination | ACCEPT |
| Engine client may POST to configured engine, enabled unless false | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-engine.ts` | `getConfig`, `governanceEvaluate` | `GOVERNANCE_ENGINE_ENABLED` | forbidden downstream | ACCEPT |
| Helper bounds timeout and returns attempt ID after abort | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `proofTimeoutMs`, `fetchGovernanceReceipt` | `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS`, `TIMED_OUT` | receipt helper | ACCEPT |
| Direct route tests abort stubbed fetch to yield `TIMED_OUT` | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` | timeout case | `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS` | unit precedent | ACCEPT |
| Panel test renders fabricated timeout/attempt ID | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | timeout case | `governance-receipt-attempt-id` | UI precedent | ACCEPT |
| Panel warns that the service may still have processed the request | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | output labels | `receiptTimedOutNote` | panel, read-only | ACCEPT |
| Mock Playwright config starts a fresh local Web server | TEST_CONFIGURATION | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `reuseExistingServer` | test harness | ACCEPT |
| D050 permits timeout-only packet authoring | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D050/Q001/Q004 | B2f | NCR roadmap | ACCEPT |
| Local audit found an unproved controlled browser timeout chain | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B2F_RECEIPT_BRANCH_GAP_AUDIT_2026-10-01.md` | Findings / Position; Decision / Disposition | `TIMED_OUT` | Local review | ACCEPT |

## Negative Search And Collision Discipline

The five planned worker output paths were checked for collisions at dispatch authoring and were absent; existing production files and browser specs are read-only. Recheck HEAD/status and exact path collisions before worker edits. This is a named-path check, not a full corpus claim.

## Current Runtime Freshness Verification

At dispatch base `b882d5d59`, Local read the export/receipt routes, unit/panel tests, B2e browser spec, Playwright config, D050 and the B2f audit. The existing B2e browser proof covers only `INVALID_RESPONSE`/`UNAVAILABLE`; five B2f outputs are planned new files. The worker repeats source and collision checks at execution HEAD. Packet authoring invoked no route or browser.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"STATEFUL_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["synthetic delayed loopback POST yields TIMED_OUT and ambiguous-outcome draft warning"],"requiredProof":["inert loopback listener and exact origin preflight before export","secret-safe stub request IDs/path/excerpt evidence and no forwarding","real export route browser response TIMED_OUT with matching attempt ID","panel draft and ambiguous-outcome warning text","unexpected request denial and disposable cleanup","focused Playwright and TypeScript"],"operatorCheckpoints":["Q001/Q004 real-data and store profile","real artifact acceptance","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","production route or UI mutation","actual Next governance evaluate route call","Governance Engine or provider call","authoritative database write","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B2F_RECEIPT_BRANCH_GAP_AUDIT_2026-10-01.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2F_RECEIPT_BRANCH_GAP_AUDIT_2026-10-01.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Earlier Web advisory is not private CVF proof |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | inert loopback harness, focused browser test and synthetic proof | local configured-hop transport/presentation only; no active accept effect | source verification above and pending Playwright observation | test adapter only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2f interface | no ingress, auth, receipt, raw data or mutation grant | D050 and this bounded scope | external adapter deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace internal worker authors an inert loopback harness, focused Playwright spec, synthetic proof receipt, reference contract and pending return. Local reviews and commits. Operator retains Q001/Q004 data/effect decisions. This is not external Web research.

Allowed scope: create only `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-timeout.spec.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs`, `docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md`, `docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json`, and `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md`.

Forbidden scope: edits to existing route/proof/component/page/helper/test files, auth, governance ledger, SQLite/data files, package/lock/config, CI, README, roadmap, session state, provider/live, real data, public sync and deployment. Test logs may write only to disposable locations outside the repository and must be cleaned. Do not add a store implementation. Risk ceiling: reversible synthetic transport/UI proof.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | B2e is accepted bounded; D050 found no controlled timeout status/attempt-ID browser proof |
| scope classification | bounded test-only delayed-loopback timeout transport and panel proof |
| risk sensitivity | accidental real evaluate/engine call, secret leak, or false remote-cancellation/retry claim |
| selected role route | SINGLE_AGENT_MULTI_ROLE internal worker with distinct Local reviewer |
| role separation basis | worker cannot self-accept or authorize data/effect |
| escalation condition | active route, storage, auth or real-data need |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one internal worker creates focused browser test and pending evidence; Local reviews |
| actor | INTERNAL_AGENT worker |
| role set | implementer and evidence producer, not reviewer/closer |
| Role separation ledger | pending worker return followed by Local disposition |
| Evidence basis independent of memory | Git changed set, inert stub request ledger, route/UI statuses and Local independent isolation probe |
| Stop boundary | worker cannot commit or authorize real-data/effect profile |
| Gate sequence | committed packet release, pre-implementation, focused Playwright, worker-return fast, Local reviewer-fast and pre-closure |
| Self-review boundary | worker test PASS is not independent acceptance |
| escalation condition | stop on active route, storage, auth, real-data or out-of-manifest need |

## Required First Reads

Read `AGENTS.md`, front door/bootstrap/active handoff, paired packet, D050 configured-hop audit, export route and `proof.ts`, Next evaluate route, engine client, auth source, existing Playwright spec/mock config, panel, `DESIGN.md`, guard orientation, literal-format gotchas and applicable output checkers. Capture HEAD and full `git status --short --untracked-files=all`.

## Worker Autonomy / No-Question Rule

Choose synthetic inputs and a focused Playwright test within the five paths. Repair ordinary test/checker findings without operator questions. If the inert stub/origin/engine-disabled preflight or browser auth cannot be established before export, preserve the observation and return `BLOCKED_WITH_REASON`; do not point `NEXTAUTH_URL` at the real Next server or edit production code. Missing browser binaries or inability to clean disposable output also block; do not install dependencies silently.

## Pre-Flight Checks

Start only after packet commit, exact-hash continuity and bound pre-dispatch gate. Record clean HEAD, verify five create paths absent, and run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md` before editing.

## Write Ownership

Worker owns exactly five create paths and leaves them uncommitted. Existing panel, routes, auth, receipt helper, engine client and Playwright config/spec are read-only. Local owns independent probe, review, material commit and continuity. Any production repair needs a separate packet.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-timeout.spec.ts` | create | real export `TIMED_OUT`, matching attempt ID, draft and ambiguous-outcome warning assertions |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs` | create | start/stop inert loopback stub and fresh test server with fail-closed preflight |
| `docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md` | create | synthetic transport/presentation boundary, no governance/store ratification |
| `docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json` | create | secret-safe stub request/route/UI and cleanup evidence, no raw body |
| `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md` | create | exact changed set and gate evidence |

## Required Artifact Manifest

All five paths below are mandatory at handoff. They are planned create paths; no other worker deliverable is authorized. The worker must leave them pending and uncommitted.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-timeout.spec.ts` | Yes | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs` | Yes | create |
| `docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md` | Yes | create |
| `docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json` | Yes | create |
| `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md` | Yes | create |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md` | NOT_BINDING_REFERENCE_WITH_REASON: new synthetic transport-proof reference, not an active-window binding reference |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-LOOPBACK","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs"],"requiredProofIds":["PROOF-ISOLATION"]},{"requirementId":"REQ-BROWSER","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-timeout.spec.ts"],"requiredProofIds":["PROOF-REQUEST","PROOF-UI"]},{"requirementId":"REQ-PROOF","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json"],"requiredProofIds":["PROOF-RECEIPT","PROOF-CLEANUP"]},{"requirementId":"REQ-CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-ISOLATION","kind":"loopback-only non-forwarding stub and exact configured origin proven before export","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs"},{"proofId":"PROOF-REQUEST","kind":"actual export route sends expected secret-safe receipt POST metadata to inert stub","locator":"artifact-export-loopback-timeout.spec.ts"},{"proofId":"PROOF-UI","kind":"TIMED_OUT status, attempt ID and ambiguous-outcome warning shown while artifact stays draft","locator":"artifact-export-loopback-timeout.spec.ts"},{"proofId":"PROOF-BOUNDARY","kind":"no real evaluate/engine/provider call and no acceptance claim","locator":"docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md"},{"proofId":"PROOF-RECEIPT","kind":"secret-safe delayed stub request/timeout proof with no real evaluate/engine/provider call","locator":"docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json"},{"proofId":"PROOF-CLEANUP","kind":"inert stub and disposable outputs stopped/removed","locator":"docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json"},{"proofId":"PROOF-RETURN","kind":"focused browser test, TypeScript/lint, worker-return fast gate and no-commit evidence","locator":"docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D049 | use B2e inert loopback design as read-only isolation precedent | do not edit B2e accepted test/proof paths or infer timeout from its invalid/unavailable replies |
| D050 | delay the configured receipt POST at an inert stub and observe `TIMED_OUT`, attempt ID and ambiguous warning | no actual Next evaluate/engine/provider, fabricated `PRESENT`, retry-safety or governance claim |
| D035, Q001 and Q004 | keep Profile A and store/effect decisions parked | no real ledger, accepting actor or durable writer |

## Implementation Contract

Create a test-only CommonJS harness and focused Playwright spec. The harness must bind an HTTP listener to `127.0.0.1` on an ephemeral port before a fresh Next test server starts, set the child server's `NEXTAUTH_URL` to the exact stub origin, `AUTH_URL` to the fresh Next origin, `GOVERNANCE_ENGINE_ENABLED=false`, a dead engine URL, synthetic service token and `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS=1000`. Prove these inherited values and browser auth before any export request; do not log token values. The stub must never forward. Accept only the one expected receipt POST path and artifact ID, record secret-safe request/artifact IDs and receive time, delay its reply beyond the configured timeout with a bounded deterministic margin, and reject unexpected requests. The harness must track the late reply/disconnect as observation only and clean timers, listener, server and disposable output. If preflight, isolation, timeout inheritance or authentication is uncertain, return `BLOCKED_WITH_REASON` before export. No production auth/config/package edit or actual evaluate/engine destination is authorized.

The browser submits only synthetic form values through the real `/api/artifacts/export` route without `page.route`, fulfill, mock or intercept of that endpoint. Passively capture HTTP 200 and `TIMED_OUT`, a route attempt ID equal to the stub's request ID, no receipt and `DRAFT_UNACCEPTED`. Verify the panel displays the same ID and the exact warning that the service may still have processed the request and an operator should check before retry. The stub must have received the POST before route timeout observation; an aborted client connection or late response does not prove remote cancellation, rollback or retry safety. Record browser/profile, secret-safe timing/metadata, route/UI status, isolation, late-reply/disconnect observation and cleanup. No `PRESENT` fixture or real governance claim is allowed.

## Execution Plan

1. Read named owners and output checkers; capture source and path collision status.
2. Write the inert loopback harness and focused synthetic Playwright spec without production-code edits.
3. Bind the delayed loopback listener and preflight fresh server origin, disabled engine, 1,000 ms timeout, synthetic token, browser auth and no-forwarding behavior before export. Only on PASS, run one timeout case; capture stub receive time, route timeout status, UI warning, late reply/disconnect and cleanup. On any isolation/auth/browser failure, stop and return BLOCKED with the observation.
4. Write the proof JSON, bounded reference and pending return; run TypeScript, targeted lint and worker-return fast gate.

## Evidence Requirements

Worker return includes executionBaseHead, initial/final status, exact changed set, pre-export isolation command/result, bound stub origin and non-forwarding evidence, inherited timeout, expected/unexpected request counts, secret-safe request/attempt IDs and receive/timeout/late-reply observations, route/UI status and warning, browser version/profile, focused Playwright counts/exit, cleanup, TypeScript/lint, gate result and an acceptance-evidence-json block joining each proof ID to its actual path. No raw credentials, bodies or real data. A passing synthetic timeout test is not remote rollback, retry safety, governance behavior, durability or operator acceptance proof.

## Acceptance Criteria

- [ ] Before export, loopback-only listener, exact `NEXTAUTH_URL`/`AUTH_URL`, disabled engine, synthetic token, 1,000 ms timeout and browser auth are evidenced; the stub has no forwarding behavior.
- [ ] Focused Playwright uses a real browser and un-intercepted export route with synthetic inputs; exactly one expected receipt POST reaches the delayed stub before timeout, with no actual evaluate route, engine or provider call.
- [ ] Route returns `TIMED_OUT`, matching attempt/stub request ID, absent receipt and `DRAFT_UNACCEPTED`; panel shows same ID and ambiguous-outcome/operator-check wording without approval affordance.
- [ ] Late reply/disconnect is recorded as observation only; no cancellation, rollback or safe-retry claim appears. Unexpected stub requests fail closed.
- [ ] Secret-safe timing/request metadata, browser/profile and disposal of listener, server, timers and external test outputs are recorded.
- [ ] Reference and proof JSON state tested browser/profile and unproven boundaries; exact five-path manifest only.
- [ ] Focused Playwright, TypeScript/lint and worker-return fast gate pass without production code edit or worker commit.

Fail conditions: preflight, auth/origin or timeout inheritance uncertainty; actual evaluate/engine/provider call; non-loopback or forwarding stub; unexpected request not rejected; missing stub receive event; route status/attempt mismatch; missing ambiguous-outcome warning; browser interception of export; fabricated `PRESENT`; false rollback/retry claim; secret exposure; incomplete cleanup; production route/UI/auth edit; authoritative database write; real data; unowned path; or worker commit.

## Review Gate

Implementation begins only after paired packet material commit, continuity exact-hash binding, bound pre-dispatch PASS and worker pre-implementation PASS. Local evaluates isolation and browser/route/UI evidence, verifies the exact five-path scope and runs one independent focused probe when the worker claims completion. Required gate failures remain worker-owned within scope; an observed production defect needs a separate Local decision.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: FALSE_TIMEOUT_REMOTE_CANCELLATION_PROOF

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local inspects the delayed stub and timeout configuration, then independently runs one fresh browser/export timeout probe; Local evaluates timing/status/attempt-ID and ambiguous warning separately from worker self-report.

positiveControl: un-intercepted export route returns `TIMED_OUT` and matching attempt ID after stub receive; panel remains draft and warns processing may have occurred.

negativeMutationClasses: listener not bound before export; timeout env not inherited; `NEXTAUTH_URL` points at Next or another destination; stub forwards; unexpected request accepted; route response fabricated in browser; no stub receive event; attempt ID mismatch; warning implies safe retry; cleanup omitted; production path edited.

expectedInformationGain: distinguish an actual route-to-stub timeout and ambiguous panel presentation from fabricated unit/jsdom behavior without inferring remote cancellation.

rerunCostReason: one focused reviewer timeout/browser probe addresses the timing and UI claim without repeating broad suites.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet and audit | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | delayed loopback harness, timeout Playwright spec, proof JSON and contract | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted worker paths and Local probe | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2f-synthetic-timeout","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - disposable loopback listener and test log are not authoritative durable writes or rollback transactions; no cross-process lock, ownership or security mutation is authorized

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal loopback route/browser test without external invocation

## Closure Checklist

Local verifies exact worker manifest, delayed loopback preflight/non-forwarding, real-route receipt POST before timeout, `TIMED_OUT` and attempt-ID join, ambiguous warning, late-response/cleanup observations, reference boundary, worker return, review, material commit, continuity and clean pre-closure. Q001/Q004 remain open regardless of B2f result.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
# Run the test-owned harness documented in the created CommonJS file. It binds
# 127.0.0.1:0 before spawning Playwright/fresh Next and injects only its own
# ephemeral origin, disabled engine and synthetic/absent service-token values.
# Check the harness CLI and isolation preflight before issuing export.
node tests/e2e/support/b2f-loopback-timeout-harness.cjs --help
node tests/e2e/support/b2f-loopback-timeout-harness.cjs
npm run check
npx eslint --max-warnings=0 tests/e2e/artifact-export-loopback-timeout.spec.ts tests/e2e/support/b2f-loopback-timeout-harness.cjs
Set-Location ../../..
git diff --name-status b882d5d59 --
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md
git status --short --untracked-files=all
```

The harness CLI is worker-defined within its owned path; its no-argument invocation above is the expected interface, and the worker must document any exact bounded argument. Use resolved paths and restore environment variables after the run. No production import of test helpers is authorized. Verify gate syntax with --help. Do not install dependencies.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_COMPLETION_2026-10-01.md`

reviewerOwnedClosurePaths: completion review only if required by closure gate; otherwise Local records acceptance in worker return under review-cost guidance.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker creates exact manifest and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`b882d5d59`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact five worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records delayed-loopback preflight, receipt POST, browser timeout/attempt ID, ambiguous warning, late response, cleanup and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/Q004, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact five-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused Playwright and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before calling export if loopback-only listener, exact origin/timeout/synthetic-token inheritance, disabled engine, auth compatibility or non-forwarding preflight cannot be proven. Also block if no stub request precedes the timeout, an actual evaluate/engine/provider call occurs, route/UI status or attempt ID mismatches, ambiguous warning is missing, test/browser dependencies are unavailable, cleanup fails, production repair is needed, or a forbidden effect/path is required. Give the narrowest amendment and observed evidence; do not silently broaden.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove timeout timing, remote cancellation, browser UI behavior or accept HTML |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT --title "NCR HTML B2f Synthetic Timeout" --date 2026-10-01 --base b882d5d59 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2f delayed-loopback timeout and ambiguous-outcome contract, five-path worker manifest and operator boundary |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B2f packet authoring, 2026-10-01 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired B2f baseline and this work order |
| Allowed scope source | delegated Local dispatch; roadmap D050 |
| Before status evidence | clean worktree at `b882d5d59` |
| After status evidence | paired packet paths pending material commit; no worker edit |
| Diff evidence | exact two-path packet set from Git status |
| Approval boundary | B2f packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b2f-timeout-packet-20261001 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_2026-10-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | synthetic configured receipt timeout/panel proof packet |
| claimDisposition | CLAIM_REJECTED: no implementation or active acceptance behavior claimed before worker evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker synthetic loopback evidence is pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker browser test is pending |
| invocationBoundary | synthetic local server/browser/test processes only |
| interceptionBoundary | test-only inert loopback stub contains the configured server-side receipt POST; export route must not be browser-intercepted |
| claimLanguage | source-identified B2f timeout/ambiguous-outcome browser gap, pending worker test and Local review |
| forbiddenExpansion | no route, ledger, database, provider, real data, artifact acceptance or public effect |

## Claim Boundary

This order authorizes only a configured-hop synthetic real-route/browser timeout and panel test against a delayed inert loopback stub, proof receipt and reference contract after dispatch release. It does not authorize fabricated `PRESENT`, remote-cancellation or retry-safety claims, actual Next evaluate route, engine/provider calls, production edits, a durable writer, active acceptance, Q001/Q004 closure, Profile B/C, pilot/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Operator later selects real-data classification/source, accepting account and authority, artifact store/instance, writer profile, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect before any B2 durable writer or route action.
