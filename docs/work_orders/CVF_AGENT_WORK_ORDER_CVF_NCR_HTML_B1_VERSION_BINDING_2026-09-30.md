# CVF Agent Work Order - NCR HTML B1 Version Binding

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B1-VERSION-BINDING

Dispatch base head: `44542a063`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md`

## Dispatch Prompt Envelope

Role: internal worker implementing the bounded HTML B1 consumer repair; Local is reviewer/closer.

Canonical packet: this work order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture current clean HEAD at worker start.

Current-time notes: use only synthetic test input and mocked fetch; no credential, ledger or provider invocation.

Do-not-misread notes: B1 binds UI result to submitted form version; it does not change route hash semantics or create durable artifact acceptance.

Required first actions: read active continuity, this packet, paired baseline, `DESIGN.md`, component/test and read-only route/proof sources; capture HEAD and status; run bound pre-implementation gate before editing.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, exact changed files, focused tests, TypeScript, worker-return fast gate, no worker commit, and source/version behavior evidence.

## Purpose

Repair the HTML review-packet consumer so its visible result, receipt, preview and output actions are bound to the form version submitted for that generation attempt. Preserve older output with clear version labeling when the form changes. Prevent a delayed or superseded response from masquerading as the current form's result.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | 2026-09-30 selection to prepare and hand off B1 work order | ACCEPT for bounded B1 packet; no Q001 effect choice |
| Active continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, Q001/R0 checkpoint | ACCEPT as parked real-ledger boundary; B1 independently selected by operator |
| NCR roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D034/D035 | ACCEPT for version-binding behavior and Profile A boundary |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md` | ACCEPT for exact worker scope, subject to committed release |
| UI design | `DESIGN.md`, operational state and copy rules | ACCEPT for readable stale-version state |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Result and form are separate states | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | lines 258-276 | `request`, `result`, `updateRequest` | HTML export panel | ACCEPT |
| Response is assigned without input-version binding | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | lines 279-299 | `handleGenerate`, `setResult` | HTML export panel | ACCEPT |
| Copy, download and print use current displayed result | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | lines 301-322 | `handleCopy`, `handleDownload`, `handlePrint` | HTML output actions | ACCEPT |
| Existing tests mock fetch and exercise result/receipt | TEST_OWNER | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | lines 28-214 | component test suite | focused Vitest owner | ACCEPT |
| Route builds HTML from fields but source hash covers content only | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | lines 288-362 | `POST`, `sourceHash`, `buildHtml` | server export route, read-only | ACCEPT |
| Receipt helper sends excerpt | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | lines 64-94 | `fetchGovernanceReceipt` | receipt helper, read-only | ACCEPT |
| Two pages consume export panel | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | lines 270-274 | `ArtifactExportPanel` | Work Transfer consumer, read-only | ACCEPT |
| B1 and B2 are separate | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D034, Work Plan | D034 | NCR roadmap | ACCEPT |

## Negative Search And Collision Discipline

The paired packet and worker-return paths were absent before authoring. `rg` search for the exact B1 batch found only roadmap B1 discussion and no prior B1 dispatch. No existing closed completion matches this tranche. Worker must recheck HEAD and path collision before edit.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B1-VERSION-BINDING","requestedProfile":"P2_BOUNDED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/","docs/reviews/","docs/baselines/","docs/work_orders/"],"claims":["HTML B1 source-identified consumer version-binding repair"],"requiredProof":["submit snapshot includes every request field","stale result disclosed on edited form","late and superseded response safety","copy/download/print version clarity","focused tests and TypeScript","worker-return fast gate"],"operatorCheckpoints":["Q001 real ledger","artifact acceptance","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","route/API mutation","ledger write","provider call","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Web advisory is not private CVF proof |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `ArtifactExportPanel` and focused test | Worker edits only two owned paths; Local closes | source verification above | Existing Web consumer only; no adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | No external CLI/MCP export in B1 | No ingress, auth, receipt, raw data or mutation grant | roadmap D034 and current component source | Any external adapter needs separate owner/authority | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace internal worker implements and reports; Local reviewer evaluates evidence, may repair bounded findings, and owns commits/closure. Web research is advisory and ended before this internal lane. Operator retains Q001/R0 and pilot/live decisions.

Allowed scope: edit only `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` and its adjacent `ArtifactExportPanel.test.tsx`; create only `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md`.

Forbidden scope: route/proof/API, parent pages, auth, governance, ledger, CI, configuration, README, roadmap, session state, provider/live calls, dependency installation, public sync, deployment, and any other path. If the existing component contract cannot satisfy an acceptance invariant, return the precise dependency instead of expanding.

Risk ceiling: R1 reversible component/test change with synthetic mocked inputs.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | Local source verification found a version-binding gap in the existing HTML consumer |
| scope classification | bounded reversible Web UI component and focused tests |
| risk sensitivity | stale result/receipt presentation and response ordering |
| selected role route | SINGLE_AGENT_MULTI_ROLE internal worker followed by distinct Local reviewer/closer |
| role separation basis | worker tests its implementation but cannot self-accept or close Q001/R0 |
| escalation condition | API/caller change or effect outside three-path manifest |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one internal worker implements and writes pending evidence; Local reviews |
| actor | INTERNAL_AGENT worker |
| role set | implementer and evidence producer, not reviewer/closer |
| Role separation ledger | pending worker return, then Local review and disposition |
| Evidence basis independent of memory | Git changed set, focused tests and Local interaction oracle |
| Gate sequence | committed packet release, pre-implementation, focused tests, worker-return fast, Local review |
| Self-review boundary | worker test PASS is not independent acceptance |
| escalation condition | out-of-manifest dependency, source contradiction or external effect |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, bootstrap and active handoff; this order and paired baseline; `DESIGN.md`; the two owned files; read-only export route/proof and the two page consumers; guard orientation and literal-format gotchas; applicable worker-return checker source. Capture `executionBaseHead` and full `git status --short --untracked-files=all` before edits.

## Worker Autonomy / No-Question Rule

Worker chooses a small component-local attempt/version mechanism and clear localized UI wording. Repair within the exact three-path manifest without routine operator questions. If a required behavior needs route changes, new durable state, secrets, real data, or a new effect, stop with `BLOCKED_WITH_REASON`; do not self-authorize that expansion.

## Pre-Flight Checks

Start only on clean committed dispatch frontier after the packet, continuity and bound release gate pass. Record HEAD and verify both edit paths exist and return path is absent. Run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md` before edits. Use mocked fetch only.

## Write Ownership

Worker owns exactly the component, its focused test, and pending return. The return remains uncommitted. Local owns any independent probe, completion disposition and commits. No other actor should mutate these paths during the worker lane.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | edit | submitted snapshot, result provenance and stale state |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | edit | discriminating behavioral tests |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md` | create | full gate evidence and exact changed set |

## Required Artifact Manifest

The exact three worker paths below are mandatory at handoff. Both component paths exist at dispatch; the return path is a planned create path. The worker must leave all three pending and uncommitted. No other path is an authorized deliverable.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Yes | edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | Yes | edit |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md` | Yes | create when worker executes |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-COMPONENT","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"requiredProofIds":["PROOF-SNAPSHOT","PROOF-STALE","PROOF-ORDER"]},{"requirementId":"REQ-TEST","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"],"requiredProofIds":["PROOF-STALE","PROOF-ORDER","PROOF-ACTIONS"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-SNAPSHOT","kind":"full submitted request snapshot bound to local attempt","locator":"ArtifactExportPanel.tsx"},{"proofId":"PROOF-STALE","kind":"edited form keeps old result visibly versioned","locator":"ArtifactExportPanel.test.tsx"},{"proofId":"PROOF-ORDER","kind":"late and superseded responses cannot replace newer result","locator":"ArtifactExportPanel.test.tsx"},{"proofId":"PROOF-ACTIONS","kind":"copy download print act on labeled displayed version","locator":"ArtifactExportPanel.test.tsx"},{"proofId":"PROOF-RETURN","kind":"focused tests TypeScript and worker-return fast gate with no-commit evidence","locator":"docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D034 HTML B1 | submit snapshot; attempt/result binding; stale disclosure; delayed response tests | no durable acceptance or route rewrite |
| D035 Profile A | synthetic component tests only | real ledger Profile B/C and pilot effect remain parked |
| Q001 | leave receipt as evidence for submitted version | no artifact approval or cutover claim |

## Implementation Contract

Snapshot all seven request fields at submit. Distinguish submitted version from current editable form by comparing the full normalized request, not only `sourceContent` or the server's source hash. Present generated output and receipt as one coherent result for the submitted version. Preserve previous result across edits, but visibly mark it as from earlier inputs before preview, copy, download or print can be mistaken for the new form. Keep existing `DRAFT_UNACCEPTED` and receipt boundaries truthful. A later attempt supersedes an earlier attempt; its response cannot be overwritten by older success/error/finally events. An `initialResult` with no request snapshot has unknown source-version relationship and must be labeled conservatively. Callback handling must not falsely present superseded output as the current generation.

Do not add an acceptance control or claim that `sourceHash` binds full rendered HTML. Avoid storing raw form content beyond existing component lifetime. Preserve keyboard and screen-reader discoverability for the stale-version notice, and provide English/Vietnamese copy consistent with the existing UI.

## Execution Plan

1. Inspect the exact component contract, test setup, and read-only callers; record any contradiction before edits.
2. Implement the smallest component-local version/attempt binding and UI notice.
3. Add focused tests for unchanged content with changed title/boundary, edits during pending fetch, late/out-of-order attempt resolution, `initialResult`, and labeled copy/download/print actions. Mock fetch and browser APIs; do not call the route.
4. Run focused Vitest, TypeScript, worker-return fast gate; inspect exact changed set and prepare pending return. Repair allowed-scope failures before handoff.

## Evidence Requirements

Evidence Trace Block: claim, command, result, key path and verdict for each acceptance invariant. Include `executionBaseHead`, initial/final `git status --short --untracked-files=all`, changed-path diff, focused test count, TypeScript result, worker gate exit, and zero external/provider calls. Show the payloads and request snapshots in tests using synthetic values, with no raw credential or real ledger content.

## Acceptance Criteria

- [ ] Full-input changes, including title and claim boundary without source-content change, create an explicit stale-result state.
- [ ] Pending edits cannot relabel the returned receipt or HTML as the edited form.
- [ ] Superseded success/error/finally cannot replace newer selected output or dismiss its state.
- [ ] Copy/download/print use the displayed older version and its notice remains visible.
- [ ] `initialResult` provenance is conservative; existing draft/ALLOW distinction remains.
- [ ] Only the exact three-path manifest changes, focused tests and TypeScript pass, and worker-return fast gate passes.

Fail conditions: an API/schema/parent-page change is needed; a receipt is represented as artifact approval; a source-content-only comparison misses another field; response ordering remains ambiguous; a test uses live route/provider data; any forbidden path changes; or the worker commits.

## Review Gate

Implementation begins only after paired packet material commit, continuity exact-hash binding, bound pre-dispatch PASS and worker pre-implementation PASS. Local reviewer evaluates the pending return, runs a bounded independent interaction probe if a decision-changing gap remains, and owns the final disposition. A failed required gate remains worker-owned for repair inside allowed scope; reviewer does not accept a self-reported pass in place of output.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: STALE_RECEIPT_AND_VERSION_PRESENTATION

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local reviewer constructs its own synthetic form-edit and delayed-response oracle after the worker return, independent of worker fixture expectations.

positiveControl: submitted version A stays labeled A after title or boundary changes; a fresh B result is labeled B.

negativeMutationClasses: sourceContent-only equality; old response overwrites new; stale receipt shown as current; initialResult silently trusted.

expectedInformationGain: distinguish actual consumer state binding from copy-only labels or source-hash-only comparison.

rerunCostReason: one focused independent interaction probe is proportional to the user-visible stale-receipt risk; no broad suite duplication.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B1-VERSION-BINDING
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
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet and source review | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | component and focused test | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b1-version-binding","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Closure Checklist

Local verifies exact worker manifest, discriminating tests, return evidence, review disposition, material commit, continuity sync, and clean committed-range pre-closure. Q001/R0 remains open regardless of B1 result.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to the exact changed set.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. Include explicit N/A with reason for every non-applicable conditional block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest run src/components/ArtifactExportPanel.test.tsx
npm run check
Set-Location ../../..
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx
git status --short --untracked-files=all
```

The worker verifies the appropriate worker gate syntax against its `--help` before running; no network/dependency installation is authorized. If local dependencies are unavailable, return an honest blocked result rather than installing them.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_COMPLETION_2026-09-30.md`

reviewerOwnedClosurePaths: completion review only if required by the closure gate; otherwise Local records acceptance in the worker return under existing review-cost guidance.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker changes exact manifest and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`44542a063`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact three worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records snapshots, attempt ordering, tests and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/R0, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact three-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused tests and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if version identity cannot be made truthful within the component, the callback or initial-result contract needs an unowned change, a test requires a live route/provider, or a forbidden path/effect is needed. Report the narrowest proposed amendment. Do not silently drop a result or convert a receipt into artifact approval.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | source ACCEPT rows, first-section envelope, exact acceptance-ledger-json, closeability graph, return gate fields |
| gateRunPurpose | Confirm packet shape and authority before release |
| claimBoundary | Static checks cannot prove implementation or grant pilot effect |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-HTML-B1-VERSION-BINDING --title "HTML B1 Version Binding" --date 2026-09-30 --base 44542a063 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B1 scope, exact three-path ledger and worker contract |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope and structural checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B1 packet authoring, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, author-fast and pre-dispatch gates, Git |
| Target paths | paired B1 baseline and this work order |
| Allowed scope source | operator selected B1 work-order authoring; roadmap D034 |
| Before status evidence | clean worktree at `44542a063` |
| After status evidence | paired packet paths pending material commit; no worker edit |
| Diff evidence | exact two-path packet changed set from Git status |
| Approval boundary | B1 packet only; worker execution follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b1-version-binding-packet-20260930 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_VERSION_BINDING_2026-09-30.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | UI result-to-submitted-input association candidate only |
| claimDisposition | CLAIM_REJECTED: no enforcement or runtime behavior claimed before implementation evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: existing route receipt semantics are read-only source context |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker focused tests pending |
| invocationBoundary | mocked fetch in focused test only |
| interceptionBoundary | no direct interception or mandatory wrapper claimed |
| claimLanguage | source-identified B1 repair, pending worker execution and review |
| forbiddenExpansion | no API, ledger, provider, public or artifact-acceptance expansion |

## Claim Boundary

This order authorizes only the B1 UI component/test repair after dispatch release. It does not authorize B2, real ledger Profile B/C, pilot effect, provider/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

The operator still decides authoritative real ledger/copy access, backup/key custody, retention, RPO/RTO, P08, cost, artifact acceptance and pilot/live. These do not block B1's synthetic component proof and are not answered by it.
