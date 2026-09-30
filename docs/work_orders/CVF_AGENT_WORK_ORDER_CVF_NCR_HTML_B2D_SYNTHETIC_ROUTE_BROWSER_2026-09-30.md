# CVF Agent Work Order - NCR HTML B2d Synthetic Route Browser

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER

Dispatch base head: `205a76790`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md`

## Dispatch Prompt Envelope

Role: internal worker creating test-only real-browser synthetic download proof and its bounded evidence; Local is reviewer/closer.

Canonical packet: this work order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Capture executionBaseHead and status at start. Do not edit before the bound pre-implementation gate passes.

Current-time notes: use only synthetic form fields and a fresh local test server with the test-only Node no-hop preload. The browser must call the actual export route without intercepting it. Set `NEXTAUTH_URL` empty before server startup, verify preload inheritance before the first export request, and fail closed if isolation cannot be proven. No provider, real data or authoritative store.

Do-not-misread notes: B2b owns an isolated Node-side byte identity. B2d observes what the existing route and panel produce and save for synthetic input. `sourceHash` hashes source text, not the rendered HTML, and browser JSON wire bytes are not artifact bytes. `NEXT_PUBLIC_CVF_MOCK_AI=1` does not disable the optional receipt hop. A mock browser test cannot prove AI governance behavior or artifact acceptance. Do not edit production code even if the test finds a defect.

Required first actions: read active continuity, this packet, paired baseline, D046 route/browser audit, export route and receipt helper, existing Playwright spec/mock config, panel, B2b helper/contract and named checker sources; capture HEAD and status; run the bound pre-implementation gate before edits.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, exact five-path changed set, no-hop preflight and attempt log, focused real-route browser result, saved-byte receipt, TypeScript/lint, worker-return fast gate, no commit.

## Purpose

Observe, in a real test browser, the exact bytes of an HTML file downloaded from the existing Artifacts panel after the actual export route builds HTML from synthetic input. Block and observe the optional server-side evaluate hop before network dispatch. Compare saved-file bytes to an independent oracle over the route's decoded `data.html` and B2b identity without changing production code. Profile A and Q001/Q004 stay open.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | 2026-09-30 approval of synthetic design/proof first and delegated Local work-order decisions | ACCEPT for B2d packet only; no real-data/effect grant |
| Current continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, next allowed move | ACCEPT; synthetic B2d packet only |
| NCR roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D045-D046/Q001/Q004 | ACCEPT for synthetic B2d proof only |
| Local audit | `docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md`, Decision | ACCEPT for source gap and bounded no-hop browser test |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md` | ACCEPT for exact scope, subject to committed release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route returns HTML while sourceHash covers source text only | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | buildHtml, POST | html, sourceHash | HTML export route | ACCEPT |
| Panel parses JSON and makes a Blob from the displayed HTML string | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handleGenerate`, `downloadHtml` | `response.json`, `Blob([html])` | Web consumer, read-only | ACCEPT |
| B2c intercepts export and therefore does not prove the real route/browser link | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts` | synthetic fulfillment | `api/artifacts/export` | prior saved-file proof | ACCEPT |
| Receipt helper returns before fetch if `NEXTAUTH_URL` is empty | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `resolveEvaluateUrl`, `fetchGovernanceReceipt` | `NOT_CONFIGURED`, `fetch` | receipt helper | ACCEPT |
| Mock Playwright config starts a local Web server | TEST_CONFIGURATION | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `NEXT_PUBLIC_CVF_MOCK_AI` | test harness | ACCEPT |
| Web package exposes Playwright, TypeScript and lint scripts | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts | `scripts` | Web package | ACCEPT |
| B2b computes identity over owned exact UTF-8 bytes | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | `createHtmlByteHandoff`, `verifyHtmlByteHandoff` | `copyBytes`, `identity` | isolated Node helper | ACCEPT |
| D046 permits synthetic route/browser packet authoring | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D045-D046/Q001/Q004 | B2d | NCR roadmap | ACCEPT |
| Local audit found an unproved route/browser link and optional server-side hop | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md` | Findings / Position; Decision / Disposition | route/browser boundary | Local review | ACCEPT |

## Negative Search And Collision Discipline

The five planned worker output paths were checked for collisions at dispatch authoring and were absent; existing production files and browser specs are read-only. Recheck HEAD/status and exact path collisions before worker edits. This is a named-path check, not a full corpus claim.

## Current Runtime Freshness Verification

At dispatch base `205a76790`, Local read the export route and receipt helper, panel, Playwright mock config, B2c proof, B2b helper, D046 and the B2d audit. B2c used an intercepted export response; five B2d outputs are planned new files. The worker repeats source and collision checks at execution HEAD. Packet authoring observed no real-route browser or file bytes.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"STATEFUL_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["synthetic un-intercepted route-to-browser saved-file byte proof under fail-closed no-hop harness"],"requiredProof":["pre-route no-hop preload and environment preflight","zero attempted server evaluate fetches and NOT_CONFIGURED response","real-route browser download event","saved-file SHA-256 and byte-length parity with decoded data.html oracle and B2b identity","same-length version discrimination","disposable file cleanup","focused Playwright and TypeScript"],"operatorCheckpoints":["Q001/Q004 real-data and store profile","real artifact acceptance","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","production route or UI mutation","authoritative database write","provider call","server governance evaluate call","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md` |
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
| `INTERNAL_AGENT` | no-hop preload, focused real-route browser test and synthetic receipt | local disposable saved-byte proof; no active accept effect | source verification above and pending Playwright observation | test adapter only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2d interface | no ingress, auth, receipt, raw data or mutation grant | D046 and this bounded scope | external adapter deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace internal worker authors a test-only no-hop preload, focused Playwright spec, synthetic proof receipt, reference contract and pending return. Local reviews and commits. Operator retains Q001/Q004 data/effect decisions. This is not an external Web research assignment.

Allowed scope: create only `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs`, `docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md`, `docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json`, and `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md`.

Forbidden scope: edits to existing route/proof/component/page/helper/test files, auth, governance ledger, SQLite/data files, package/lock/config, CI, README, roadmap, session state, provider/live, real data, public sync and deployment. Browser downloads may write only to disposable test locations outside the repository and must be cleaned. Do not add a store implementation. Risk ceiling: reversible synthetic UI/file proof.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | B2c is accepted bounded; D046 found no no-hop real-route/browser saved-file byte proof |
| scope classification | bounded test-only no-hop route/browser synthetic download proof |
| risk sensitivity | accidental server evaluate hop, wrong-version download or false byte proof |
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
| Evidence basis independent of memory | Git changed set, no-hop attempt log, route status, saved-file digest and Local independent browser/file probe |
| Stop boundary | worker cannot commit or authorize real-data/effect profile |
| Gate sequence | committed packet release, pre-implementation, focused Playwright, worker-return fast, Local reviewer-fast and pre-closure |
| Self-review boundary | worker test PASS is not independent acceptance |
| escalation condition | stop on active route, storage, auth, real-data or out-of-manifest need |

## Required First Reads

Read `AGENTS.md`, front door/bootstrap/active handoff, paired packet, D046 route/browser audit, export route and `proof.ts`, existing Playwright spec/mock config, B2b helper/reference, panel, `DESIGN.md`, guard orientation, literal-format gotchas and applicable output checkers. Capture HEAD and full `git status --short --untracked-files=all`.

## Worker Autonomy / No-Question Rule

Choose synthetic inputs and a focused Playwright test within the five paths. Repair ordinary test/checker findings without operator questions. If no-hop preflight cannot be established before calling the route, or the real browser exposes a production defect, preserve the observation and return `BLOCKED_WITH_REASON`; do not edit production code under this packet. Missing browser binaries or inability to clean disposable output are also blocked reasons; do not install dependencies silently.

## Pre-Flight Checks

Start only after packet commit, exact-hash continuity and bound pre-dispatch gate. Record clean HEAD, verify five create paths absent, and run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md` before editing.

## Write Ownership

Worker owns exactly five create paths and leaves them uncommitted. The existing panel, route, B2b helper and Playwright config/spec are read-only; importing the B2b helper in the new Node-side Playwright test is allowed. Local owns independent probe, review, material commit and continuity. Any production repair needs a separate packet.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts` | create | passive real-route response capture, browser download, saved-byte comparison and cleanup |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs` | create | fail-closed server-side evaluate-fetch blocker and external attempt log |
| `docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md` | create | browser/file proof boundary and limits, no store ratification |
| `docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json` | create | fixture, browser, saved-byte hash/length and cleanup evidence without raw HTML |
| `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md` | create | exact changed set and gate evidence |

## Required Artifact Manifest

All five paths below are mandatory at handoff. They are planned create paths; no other worker deliverable is authorized. The worker must leave them pending and uncommitted.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts` | Yes | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs` | Yes | create |
| `docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md` | Yes | create |
| `docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json` | Yes | create |
| `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md` | Yes | create |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md` | NOT_BINDING_REFERENCE_WITH_REASON: new synthetic browser-proof reference, not an active-window binding reference |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-NO-HOP","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs"],"requiredProofIds":["PROOF-ISOLATION"]},{"requirementId":"REQ-BROWSER","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts"],"requiredProofIds":["PROOF-DOWNLOAD","PROOF-VERSION"]},{"requirementId":"REQ-PROOF","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json"],"requiredProofIds":["PROOF-BYTES","PROOF-CLEANUP"]},{"requirementId":"REQ-CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-ISOLATION","kind":"pre-route fail-closed Node preload startup, empty NEXTAUTH_URL, zero attempted evaluate fetches and NOT_CONFIGURED route status","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs"},{"proofId":"PROOF-DOWNLOAD","kind":"un-intercepted real route response and observed real browser download","locator":"artifact-export-route-byte-download.spec.ts"},{"proofId":"PROOF-VERSION","kind":"saved file matches displayed B1 version after form change and differs for same-length title mutation","locator":"artifact-export-route-byte-download.spec.ts"},{"proofId":"PROOF-BYTES","kind":"saved-file byte SHA-256 and length match decoded route data.html oracle and B2b identity","locator":"docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json"},{"proofId":"PROOF-CLEANUP","kind":"disposable download path removed with no raw HTML committed","locator":"docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json"},{"proofId":"PROOF-BOUNDARY","kind":"browser/file proof scope without governance or store ratification","locator":"docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md"},{"proofId":"PROOF-RETURN","kind":"focused browser test, TypeScript/lint, worker-return fast gate and no-commit evidence","locator":"docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D042 | use B2b identity only as a Node-side oracle for the synthetic fixture | no production import of B2b into panel |
| D045 | preserve B2c saved-file byte identity discipline | no claim that the intercepted fixture reached the real route |
| D046 | isolate the optional receipt hop, observe the un-intercepted route response and compare actual saved-file bytes | no provider, print/clipboard or durable-store claim |
| D035, Q001 and Q004 | keep Profile A and store/effect decisions parked | no real ledger, accepting actor or durable writer |

## Implementation Contract

Create a test-only CommonJS preload and focused Playwright spec. The preload must be installed through `NODE_OPTIONS=--require <absolute preload path>` before the fresh Next test server starts, wrap global Node `fetch`, and synchronously record and throw on any attempted `/api/governance/evaluate` fetch before it reaches network. Record a startup marker and attempted-call count in a disposable log outside the repository; do not log headers, tokens or bodies. Set `NEXTAUTH_URL` to the empty string in the parent process before Playwright starts the server. Preflight that Next inherits this value and preload startup is observable. If either preflight is uncertain, return `BLOCKED_WITH_REASON` without issuing an export request. Keep the existing auth/browser test setup; no package/config/production change is authorized.

The browser must submit only synthetic form values to the actual `/api/artifacts/export` route. Do not `page.route`, fulfill, mock or otherwise intercept that endpoint. Passively capture its response and require a successful JSON result with `governanceReceiptStatus: NOT_CONFIGURED`, no receipt and no evaluate attempt in the preload log. If an evaluate attempt is logged, the preload must have blocked it and the test must fail. Build an independent Node `Buffer.from(data.html, 'utf8')` oracle from the decoded route result, then compare the B2b identity for the same HTML string. After the UI displays the result, edit the form without rebuilding and assert the preview remains the earlier version. Click Download HTML, await the real download event, save outside the repository, read the file as bytes, and compare length and SHA-256 to the oracle. A second synthetic input with a same-length title change must yield an equal byte length but different digest; any wrong-version file fails. Do not equate `sourceHash` or JSON wire bytes with artifact bytes. Record browser/profile, route status, filename, byte hashes, preload log summary, cleanup and failures without raw HTML or credentials. The reference states this local synthetic browser/profile's scope and limits.

## Execution Plan

1. Read named owners and output checkers; capture source and path collision status.
2. Write the no-hop preload and focused synthetic Playwright spec without production-code edits.
3. Run the isolated server/preload preflight before the first export request. Only on PASS, run the spec with the mock Playwright config; capture route status, zero attempted evaluate calls, saved-file bytes and cleanup. On any isolation/browser/file failure, stop and return BLOCKED with the observation.
4. Write the proof JSON, bounded reference and pending return; run TypeScript, targeted lint and worker-return fast gate.

## Evidence Requirements

Worker return includes executionBaseHead, initial/final status, exact changed set, pre-route isolation command/result, preload startup/attempt counts, observed route status, browser version/profile, focused Playwright counts/exit, saved-file hashes/length, cleanup, TypeScript/lint, gate result and an acceptance-evidence-json block joining each proof ID to its actual path. No raw credentials or real data. A passing synthetic browser-file test is not governance behavior, durability or operator acceptance proof.

## Acceptance Criteria

- [ ] Before the first export request, fresh server inheritance of empty `NEXTAUTH_URL` and active fail-closed preload is evidenced; any attempted server-side evaluate fetch is blocked and recorded.
- [ ] Focused Playwright uses a real test browser and un-intercepted real export route with synthetic inputs; response is `NOT_CONFIGURED`, attempted evaluate count is zero and no provider is called.
- [ ] A real download event and saved-file readback match independent UTF-8 byte oracle from decoded route `data.html` and B2b identity for the exact displayed result.
- [ ] Same-length changed title yields a different digest, and changing the form without rebuilding does not change the downloaded displayed version.
- [ ] Same-length title substitution compares bytes, not only preview text; filename and cleanup are recorded.
- [ ] Reference and proof JSON state tested browser/profile and unproven boundaries; exact five-path manifest only.
- [ ] Focused Playwright, TypeScript/lint and worker-return fast gate pass without production code edit or worker commit.

Fail conditions: preflight uncertainty, evaluate attempt, route status other than `NOT_CONFIGURED`, browser interception of export, no browser/download event, saved-byte mismatch, wrong displayed version, incomplete cleanup, production route/UI/auth edit, authoritative database write, real data/provider call, hash over JSON envelope or sourceHash, text-only readback substituted for bytes, unowned path, or worker commit.

## Review Gate

Implementation begins only after paired packet material commit, continuity exact-hash binding, bound pre-dispatch PASS and worker pre-implementation PASS. Local evaluates no-hop and browser/file evidence, verifies the exact five-path scope and runs one independent saved-byte probe or recomputation. Required gate failures remain worker-owned within scope; an observed production defect needs a separate Local decision.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: FALSE_BROWSER_SAVED_BYTE_PROOF

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local independently verifies preload no-hop evidence and recomputes actual saved-file bytes and SHA-256 from a reviewer-owned real-route browser run, separate from worker self-report.

positiveControl: un-intercepted route returns `NOT_CONFIGURED` with zero attempted evaluate calls; a real downloaded file matches decoded route HTML's independent byte oracle and B2b identity.

negativeMutationClasses: preload absent or evaluate attempt overlooked; intercepted export mistaken for real route; same-length wrong-version file accepted; text-only readback substitutes for saved bytes; download event absent; cleanup omitted; production path edited.

expectedInformationGain: distinguish actual real-route saved-file bytes from preview text or a digest computed solely on a fixture string, while proving the receipt hop did not execute.

rerunCostReason: one focused reviewer browser/file probe addresses the saved-byte claim without repeating broad suites.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER
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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | no-hop preload, Playwright spec, proof JSON and contract | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2d-synthetic-route-browser","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - disposable browser-test download and no-hop log are not authoritative durable writes or rollback transactions; no cross-process lock, ownership or security mutation is authorized

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal no-hop route/browser test without external invocation

## Closure Checklist

Local verifies exact worker manifest, no-hop preflight/attempt evidence, discriminating real-route browser saved-byte proof, cleanup, reference boundary, worker return, review, material commit, continuity and clean pre-closure. Q001/Q004 remain open regardless of B2d result.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
$env:CVF_PLAYWRIGHT_PORT='3000'
$env:PLAYWRIGHT_BASE_URL='http://localhost:3000'
$env:NEXTAUTH_URL=''
$env:CVF_B2D_NO_HOP_LOG=<absolute-disposable-path-outside-repository>
$env:NODE_OPTIONS='--require <absolute-path-to-b2d-no-hop-preload.cjs>'
# Verify blank NEXTAUTH_URL survives Next env loading, preload startup is recorded,
# and the fresh Next server inherits the preload before requesting export.
npx playwright test tests/e2e/artifact-export-route-byte-download.spec.ts --config playwright.config.mock.ts
npm run check
npx eslint --max-warnings=0 tests/e2e/artifact-export-route-byte-download.spec.ts tests/e2e/support/b2d-no-hop-preload.cjs
Set-Location ../../..
git diff --name-status 205a76790 --
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md
git status --short --untracked-files=all
```

The angle-bracket values above are placeholders, not a command to copy verbatim. Use resolved absolute paths and restore environment variables after the run. Only the new Node-side Playwright test may import the B2b helper; no production import is authorized. Verify gate syntax with --help. Do not install dependencies.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_COMPLETION_2026-09-30.md`

reviewerOwnedClosurePaths: completion review only if required by closure gate; otherwise Local records acceptance in worker return under review-cost guidance.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker creates exact manifest and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`205a76790`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact five worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records no-hop preflight, real-route browser download, saved-file bytes, cleanup and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/Q004, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact five-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused Playwright and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before calling export if no-hop preflight cannot be proven. Also block if an evaluate attempt occurs, route status is not `NOT_CONFIGURED`, browser download or saved-byte comparison fails, test/browser dependencies are unavailable, cleanup fails, production repair is needed, or a forbidden effect/path is required. Give the narrowest amendment and observed evidence; do not silently broaden.

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
| claimBoundary | Static checks cannot prove no-hop isolation or browser saved-file bytes or accept HTML |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER --title "NCR HTML B2d Synthetic Route Browser" --date 2026-09-30 --base 205a76790 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2d no-hop route/browser proof contract, five-path worker manifest and operator boundary |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B2d packet authoring, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired B2d baseline and this work order |
| Allowed scope source | delegated Local dispatch; roadmap D046 |
| Before status evidence | clean worktree at `205a76790` |
| After status evidence | paired packet paths pending material commit; no worker edit |
| Diff evidence | exact two-path packet set from Git status |
| Approval boundary | B2d packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b2d-route-browser-packet-20260930 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_2026-09-30.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | synthetic no-hop real-route/browser downloaded-file byte proof packet |
| claimDisposition | CLAIM_REJECTED: no implementation or active acceptance behavior claimed before worker evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker browser-file receipt is pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker browser test is pending |
| invocationBoundary | synthetic local server/browser/test processes only |
| interceptionBoundary | test-only Node fetch wrapper blocks server-side evaluate; export route must not be browser-intercepted |
| claimLanguage | source-identified B2d route/browser and receipt-hop proof gap, pending worker test and Local review |
| forbiddenExpansion | no route, ledger, database, provider, real data, artifact acceptance or public effect |

## Claim Boundary

This order authorizes only a no-hop synthetic real-route/browser download test, proof receipt and reference contract after dispatch release. It does not authorize production edits, a durable writer, active acceptance, Q001/Q004 closure, Profile B/C, pilot/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Operator later selects real-data classification/source, accepting account and authority, artifact store/instance, writer profile, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect before any B2 durable writer or route action.
