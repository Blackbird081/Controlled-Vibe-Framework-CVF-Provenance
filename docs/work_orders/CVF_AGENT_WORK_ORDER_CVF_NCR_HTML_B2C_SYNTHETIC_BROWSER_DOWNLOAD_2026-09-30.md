# CVF Agent Work Order - NCR HTML B2c Synthetic Browser Download

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD

Dispatch base head: `7be703a4d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md`

## Dispatch Prompt Envelope

Role: internal worker creating test-only real-browser synthetic download proof and its bounded evidence; Local is reviewer/closer.

Canonical packet: this work order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Capture executionBaseHead and status at start. Do not edit before the bound pre-implementation gate passes.

Current-time notes: use a synthetic intercepted export response, one real test browser and disposable downloaded files. No unmocked export route call, credential, provider, real data or authoritative store.

Do-not-misread notes: B2b owns an isolated Node-side byte identity. B2c observes what the existing panel actually saves for a synthetic displayed result. A mock browser test cannot prove AI governance behavior, production transport or artifact acceptance. Do not edit the panel even if the test finds a defect.

Required first actions: read active continuity, this packet, paired baseline, D043 audit, existing Playwright spec/mock config, panel, B2b helper/contract and named checker sources; capture HEAD and status; run the bound pre-implementation gate before edits.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, exact four-path changed set, focused real-browser result, saved-byte receipt, TypeScript/lint, worker-return fast gate, no commit.

## Purpose

Observe, in a real test browser, the exact bytes of an HTML file downloaded from the existing Artifacts panel when the export response is fully synthetic and intercepted. Compare saved-file bytes to an independent oracle and B2b identity without changing production code. Profile A and Q001/Q004 stay open.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | 2026-09-30 approval of synthetic design/proof first and delegated Local work-order decisions | ACCEPT for B2c packet only; no real-data/effect grant |
| Current continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, next allowed move | ACCEPT; synthetic B2c packet only |
| NCR roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D042-D043/Q001/Q004 | ACCEPT for synthetic B2c proof only |
| Local audit | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md`, Decision | ACCEPT for source gap and bounded browser test |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md` | ACCEPT for exact scope, subject to committed release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route returns HTML while sourceHash covers source text only | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | buildHtml, POST | html, sourceHash | HTML export route | ACCEPT |
| Panel parses JSON and makes a Blob from the displayed HTML string | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handleGenerate`, `downloadHtml` | `response.json`, `Blob([html])` | Web consumer, read-only | ACCEPT |
| Existing Playwright spec intercepts export and checks preview, not download bytes | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | first Artifacts case | `page.route`, preview | browser test precedent | ACCEPT |
| Mock Playwright config starts a local Web server | TEST_CONFIGURATION | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `NEXT_PUBLIC_CVF_MOCK_AI` | test harness | ACCEPT |
| Web package exposes Playwright, TypeScript and lint scripts | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts | `scripts` | Web package | ACCEPT |
| B2b computes identity over owned exact UTF-8 bytes | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | `createHtmlByteHandoff`, `verifyHtmlByteHandoff` | `copyBytes`, `identity` | isolated Node helper | ACCEPT |
| D043 permits synthetic browser-download packet authoring | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D042-D043/Q001/Q004 | B2c | NCR roadmap | ACCEPT |
| Local audit found saved-file proof missing and panel still unconnected to B2b | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md` | Findings / Position; Decision / Disposition | browser-file boundary | Local review | ACCEPT |

## Negative Search And Collision Discipline

The four planned worker output paths were checked for collisions at dispatch authoring and were absent; the existing panel, browser spec and B2b helper are read-only. Recheck HEAD/status and exact path collisions before worker edits. This is a named-path check, not a full corpus claim.

## Current Runtime Freshness Verification

At dispatch base `7be703a4d`, Local re-read the panel, existing Playwright spec/mock config, B2b helper, D043 and the B2c audit. The existing spec has no download event or saved-file digest assertion; the four B2c outputs are planned new files. The worker repeats source and collision checks at execution HEAD. Packet authoring observed no actual browser or file bytes.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"STATEFUL_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["synthetic real-browser saved-file byte proof for displayed HTML"],"requiredProof":["browser download event","saved-file SHA-256 and byte-length parity with independent oracle and B2b identity","same-length version discrimination","BOM newline and Unicode byte cases","disposable file cleanup","focused Playwright and TypeScript"],"operatorCheckpoints":["Q001/Q004 real-data and store profile","real artifact acceptance","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","production route or UI mutation","authoritative database write","provider call","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md` |
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
| `INTERNAL_AGENT` | focused real-browser test and synthetic receipt | local disposable saved-byte proof; no active accept effect | source verification above and pending Playwright observation | test adapter only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2c interface | no ingress, auth, receipt, raw data or mutation grant | D043 and this bounded scope | external adapter deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace internal worker authors a new focused Playwright spec, synthetic proof receipt, reference contract and pending return. Local reviews and commits. Operator retains Q001/Q004 data/effect decisions. This is not an external Web research assignment.

Allowed scope: create only `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts`, `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md`, `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json`, and `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md`.

Forbidden scope: edits to existing route/proof/component/page/helper/test files, auth, governance ledger, SQLite/data files, package/lock/config, CI, README, roadmap, session state, provider/live, real data, public sync and deployment. Browser downloads may write only to disposable test locations outside the repository and must be cleaned. Do not add a store implementation. Risk ceiling: reversible synthetic UI/file proof.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | B2b is accepted bounded; D043 found no saved-file byte proof in existing browser tests |
| scope classification | bounded test-only real-browser synthetic download proof |
| risk sensitivity | wrong-version download, text-only false proof or missing browser download |
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
| Evidence basis independent of memory | Git changed set, saved-file digest receipt and Local independent browser/file probe |
| Stop boundary | worker cannot commit or authorize real-data/effect profile |
| Gate sequence | committed packet release, pre-implementation, focused Playwright, worker-return fast, Local reviewer-fast and pre-closure |
| Self-review boundary | worker test PASS is not independent acceptance |
| escalation condition | stop on active route, storage, auth, real-data or out-of-manifest need |

## Required First Reads

Read `AGENTS.md`, front door/bootstrap/active handoff, paired packet, D043 audit, existing Playwright spec/mock config, B2b helper/reference, panel, `DESIGN.md`, guard orientation, literal-format gotchas and applicable output checkers. Capture HEAD and full `git status --short --untracked-files=all`.

## Worker Autonomy / No-Question Rule

Choose exact synthetic fixtures and a focused Playwright test within the four paths. Repair ordinary test/checker findings without operator questions. If the real browser exposes a panel defect, preserve the failing observation and return `BLOCKED_WITH_REASON`; do not edit the panel under this packet. Missing browser binaries or inability to clean disposable output are also blocked reasons; do not install dependencies silently.

## Pre-Flight Checks

Start only after packet commit, exact-hash continuity and bound pre-dispatch gate. Record clean HEAD, verify four create paths absent, and run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md` before editing.

## Write Ownership

Worker owns exactly four create paths and leaves them uncommitted. The existing panel, route, B2b helper and Playwright config/spec are read-only; importing the B2b helper in the new Node-side Playwright test is allowed. Local owns independent probe, review, material commit and continuity. Any panel repair needs a separate packet.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts` | create | intercepted synthetic response, real browser download, saved-byte comparison and cleanup |
| `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md` | create | browser/file proof boundary and limits, no store ratification |
| `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json` | create | fixture, browser, saved-byte hash/length and cleanup evidence without raw HTML |
| `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md` | create | exact changed set and gate evidence |

## Required Artifact Manifest

All four paths below are mandatory at handoff. They are planned create paths; no other worker deliverable is authorized. The worker must leave them pending and uncommitted.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts` | Yes | create |
| `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md` | Yes | create |
| `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json` | Yes | create |
| `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md` | Yes | create |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md` | NOT_BINDING_REFERENCE_WITH_REASON: new synthetic browser-proof reference, not an active-window binding reference |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-BROWSER","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts"],"requiredProofIds":["PROOF-DOWNLOAD","PROOF-VERSION"]},{"requirementId":"REQ-PROOF","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json"],"requiredProofIds":["PROOF-BYTES","PROOF-CLEANUP"]},{"requirementId":"REQ-CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-DOWNLOAD","kind":"intercepted synthetic response and observed real browser download","locator":"artifact-export-byte-download.spec.ts"},{"proofId":"PROOF-VERSION","kind":"saved file matches displayed B1 version after form change and differs for same-length title mutation","locator":"artifact-export-byte-download.spec.ts"},{"proofId":"PROOF-BYTES","kind":"saved-file byte SHA-256 and length match independent oracle and B2b identity","locator":"docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json"},{"proofId":"PROOF-CLEANUP","kind":"disposable download path removed with no raw HTML committed","locator":"docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json"},{"proofId":"PROOF-BOUNDARY","kind":"browser/file proof scope without governance or store ratification","locator":"docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md"},{"proofId":"PROOF-RETURN","kind":"focused browser test, TypeScript/lint, worker-return fast gate and no-commit evidence","locator":"docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D042 | use B2b identity only as a Node-side oracle for the synthetic fixture | no production import of B2b into panel |
| D043 | observe real browser download and compare actual saved-file bytes for the displayed version | no production route/proxy, print/clipboard, or durable-store claim |
| D035, Q001 and Q004 | keep Profile A and store/effect decisions parked | no real ledger, accepting actor or durable writer |

## Implementation Contract

Create a focused Playwright spec using the real Artifacts panel and a `page.route` synthetic fulfillment for the export endpoint. The fixture must contain exact, well-formed HTML strings with a same-byte-length title substitution and distinctive UTF-8 cases (BOM, CRLF/LF and non-ASCII). Do not call the real export handler or a provider. Keep the existing auth/browser test setup; if it is unavailable, return a precise blocked finding rather than installing dependencies or weakening the browser requirement.

Build the fixture oracle independently of the panel and B2b helper, then compute B2b's Node-side identity for parity. After the UI displays a result, edit the form without rebuilding and assert the preview still shows the earlier version. Click Download HTML, await Playwright's real download event, save to a disposable test directory, read the saved file as bytes, and compare length and SHA-256. A second fixture differing in a same-length title must have a different digest; a wrong-version file is a failure. Use byte arrays for BOM/newline/Unicode assertions; reading text alone is insufficient. Record actual browser/profile, filename, observed hashes, cleanup and any failures in the proof JSON and return. Do not commit raw HTML/downloaded files. The reference explains precisely what this browser/profile proves and what remains unproven, including production network, print/clipboard, other browsers and durable acceptance.

## Execution Plan

1. Read named owners and output checkers; capture source and path collision status.
2. Write the focused synthetic Playwright spec without production-code edits.
3. Run the spec once with the mock Playwright config; capture exact saved-file bytes, observed status and cleanup. If the browser/file proof fails, stop and return BLOCKED with the failing observation.
4. Write the proof JSON, bounded reference and pending return; run TypeScript, targeted lint and worker-return fast gate.

## Evidence Requirements

Worker return includes executionBaseHead, initial/final status, exact changed set, browser version/profile, focused Playwright counts/exit, saved-file hashes/length, cleanup, TypeScript/lint, gate result and an acceptance-evidence-json block joining each proof ID to its actual path. No raw credentials or real data. A passing synthetic browser-file test is not production network, governance behavior, durability or operator acceptance proof.

## Acceptance Criteria

- [ ] Focused Playwright uses a real test browser and intercepted synthetic export response; no provider or real export route call.
- [ ] A real download event and saved-file readback match independent UTF-8 byte oracle and B2b identity for exact displayed fixture.
- [ ] Same-length changed title yields a different digest, and changing the form without rebuilding does not change the downloaded displayed version.
- [ ] BOM, CRLF/LF and non-ASCII cases are compared as bytes; filename and cleanup are recorded.
- [ ] Reference and proof JSON state tested browser/profile and unproven boundaries; exact four-path manifest only.
- [ ] Focused Playwright, TypeScript/lint and worker-return fast gate pass without production code edit or worker commit.

Fail conditions: no browser/download event, saved-byte mismatch, wrong displayed version, incomplete cleanup, production route/UI/auth edit, authoritative database write, real data/provider call, hash over JSON envelope or sourceHash, text-only readback substituted for bytes, unowned path, or worker commit.

## Review Gate

Implementation begins only after paired packet material commit, continuity exact-hash binding, bound pre-dispatch PASS and worker pre-implementation PASS. Local evaluates returned browser/file evidence, verifies the exact four-path scope and runs one independent saved-byte probe or recomputation with a distinct fixture. Required gate failures remain worker-owned within scope; an observed panel defect is a separate Local R1 decision.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: FALSE_BROWSER_SAVED_BYTE_PROOF

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local uses a distinct synthetic HTML fixture or independently recomputes actual saved-file bytes and SHA-256 from a reviewer-owned browser run, separate from worker self-report.

positiveControl: a real downloaded file matches the displayed fixture's independent byte oracle and B2b identity.

negativeMutationClasses: same-length wrong-version file accepted; text-only readback substitutes for saved bytes; download event absent; cleanup omitted; production path edited.

expectedInformationGain: distinguish actual saved-file bytes from preview text or a digest computed solely on the fixture string.

rerunCostReason: one focused reviewer browser/file probe addresses the saved-byte claim without repeating broad suites.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD
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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | Playwright spec, proof JSON and contract | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2c-synthetic-browser-download","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - disposable browser-test download is not an authoritative durable write or rollback transaction; no cross-process lock, ownership or security mutation is authorized

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal browser-file test without external invocation

## Closure Checklist

Local verifies exact worker manifest, discriminating browser saved-byte proof, cleanup, reference boundary, worker return, review, material commit, continuity and clean pre-closure. Q001/Q004 remain open regardless of B2c result.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx playwright test tests/e2e/artifact-export-byte-download.spec.ts --config playwright.config.mock.ts
npm run check
npx eslint --max-warnings=0 tests/e2e/artifact-export-byte-download.spec.ts
Set-Location ../../..
git diff --name-status 7be703a4d --
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md
git status --short --untracked-files=all
```

Only the new Node-side Playwright test may import the B2b helper; no production import is authorized. Verify gate syntax with --help. Do not install dependencies.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_COMPLETION_2026-09-30.md`

reviewerOwnedClosurePaths: completion review only if required by closure gate; otherwise Local records acceptance in worker return under review-cost guidance.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker creates exact manifest and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`7be703a4d`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact four worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records synthetic browser download, saved-file bytes, cleanup and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/Q004, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact four-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused Playwright and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if browser download or saved-byte comparison fails, test/browser dependencies are unavailable, cleanup fails, panel repair is needed, or a forbidden effect/path is required. Give the narrowest amendment and observed evidence; do not silently broaden.

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
| claimBoundary | Static checks cannot prove browser saved-file bytes or accept HTML |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD --title "NCR HTML B2c Synthetic Browser Download" --date 2026-09-30 --base 7be703a4d --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2c browser-file proof contract, four-path worker manifest and operator boundary |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B2c packet authoring, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired B2c baseline, this work order and NCR roadmap D044 |
| Allowed scope source | delegated Local dispatch; roadmap D043 |
| Before status evidence | clean worktree at `7be703a4d` |
| After status evidence | paired packet and roadmap paths pending material commit; no worker edit |
| Diff evidence | exact three-path packet/roadmap set from Git status |
| Approval boundary | B2c packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b2c-byte-packet-20260930 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | synthetic real-browser downloaded-file byte proof packet |
| claimDisposition | CLAIM_REJECTED: no implementation or active acceptance behavior claimed before worker evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker browser-file receipt is pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker browser test is pending |
| invocationBoundary | synthetic local browser/test process only |
| interceptionBoundary | no direct interception or mandatory wrapper claimed |
| claimLanguage | source-identified B2c saved-byte proof gap, pending worker browser test and Local review |
| forbiddenExpansion | no route, ledger, database, provider, real data, artifact acceptance or public effect |

## Claim Boundary

This order authorizes only a synthetic real-browser download test, proof receipt and reference contract after dispatch release. It does not authorize panel/route edits, a durable writer, active acceptance, Q001/Q004 closure, Profile B/C, pilot/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Operator later selects real-data classification/source, accepting account and authority, artifact store/instance, writer profile, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect before any B2 durable writer or route action.
