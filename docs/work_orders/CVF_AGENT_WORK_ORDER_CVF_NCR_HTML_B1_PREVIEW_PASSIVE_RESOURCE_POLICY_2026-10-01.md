# CVF Agent Work Order - NCR HTML B1 Preview Passive Resource Policy

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B1-PREVIEW-RESOURCES

Dispatch base head: `86dae9fa218a34048ba1420e9644497e3be87bdc`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace INTERNAL_AGENT; reviewer/closer: Local

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md`

## Dispatch Prompt Envelope

Role: shared-workspace INTERNAL_AGENT implementer, Local reviews/closes. Canonical packet: this order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`. Commit mode: WORKER_MUST_NOT_COMMIT. executionBaseHead: capture clean released HEAD before edits.

Current-time notes: D063 and owner audit `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` admit distinct Preview packet. Print R2 accepted bounded; no Print successor or historical stash apply.

Do-not-misread notes: script blocking does not deny passive loads; policy text is not effective enforcement; derived Preview srcdoc is not canonical result.html. No production incident or universal safety claim.

Required first actions: read compact continuity, paired packet/audit/sources/checkers; capture clean HEAD/status; run bound pre-implementation PASS. Hash/path/authority collision returns BLOCKED_WITH_REASON.

Return contract: exactly seven named paths; COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON with control/negative/mutation, canonical/version, retained Print evidence and full worker-return gate; no commit.

## Purpose

Close Preview passive-resource gap within existing owner while preserving script/origin isolation, benign inline presentation and canonical output/version. Return bounded synthetic proof for Local review; Q001/Q004 remain OPEN.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator delegation | Local orchestrator authors bounded work orders; operator relays worker | ACCEPT for packet |
| Current continuity | AUTHOR_B1_PREVIEW_PASSIVE_RESOURCE_PACKET | ACCEPT authoring |
| Owner audit | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` at `9512b71c7` | ACCEPT ADAPT_EXISTING_OWNER |
| Roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` D063/D064 | ACCEPT distinct Preview lane |
| Print regression baseline | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_COMPLETENESS_R2_COMPLETION_2026-10-01.md` at `6251ca305` | ACCEPT bounded, no Print successor |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md` | ACCEPT subject to bound release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Distinct owner decision | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` | Decision / Disposition | ADAPT_EXISTING_OWNER | Local reviewer | ACCEPT |
| Direct Preview sink and input seams | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Preview; handleGenerate | srcDoc; initialResult; setDisplayed | ArtifactExportPanel | ACCEPT |
| Canonical actions | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | handleCopy; handleDownload; handlePrint | handleCopy; handleDownload; handlePrint | ArtifactExportPanel | ACCEPT |
| Producer escapes text | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | escapeHtml; buildHtml | escapeHtml | export route | ACCEPT |
| Existing script/origin control | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | FIXTURE_HTML | FIXTURE_HTML | Preview spec | ACCEPT |
| Print coupling | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | displayedHtml; observation validation | printedPayloadEqualsDisplayed | Print spec | ACCEPT |
| Preview registration | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-synthetic-sandbox-source.json` | scopePaths | artifact-export-preview-sandbox.spec.ts | GC-051 | ACCEPT |
| Print registration | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-browser-repair-source.json` | scopePaths | artifact-export-print-browser.spec.ts | GC-051 | ACCEPT |
| Packet admission | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D063 | ADAPT_EXISTING_OWNER | NCR roadmap | ACCEPT |

## Negative Search And Collision Discipline

At clean `86dae9fa218a34048ba1420e9644497e3be87bdc`, four source paths exist and three named task-output paths are absent. Explicit path checks only, no full corpus coverage. Reuse registered specs; historical accepted proofs read-only; no stash apply.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source implementation packet with explicit path collision checks only; no corpus completeness or all-files-read claim. Existing source audit receipt retains its PARTIAL selected-section boundary.

## Current Runtime Freshness Verification

Source audit and accepted Print evidence consumed without browser rerun during authoring; product unchanged. New policy behavior pending worker proof; production exploitability unproven.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B1-PREVIEW-RESOURCES","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"STATEFUL_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["one-profile synthetic Preview resource isolation and canonical identity"],"requiredProof":["PROOF-DENY-BEFORE-PARSE","PROOF-UNIT","PROOF-CANONICAL","PROOF-POSITIVE","PROOF-NEGATIVE","PROOF-MUTATION","PROOF-SANDBOX","PROOF-PRINT-REGRESSION","PROOF-BOUNDARY","PROOF-OBSERVATIONS","PROOF-RETURN"],"operatorCheckpoints":["Q001/Q004","actor/data/store","pilot/live","public sync","deployment"],"forbiddenEffects":["worker commit","route/provider/ledger/storage edit","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` |
| Chain map route | Local source-derived Preview adaptation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Local private-CVF review accepts worker evidence |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Preview component/specs | synthetic UI only | owner audit, pending proof | existing Web panel | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none | no ingress/mutation grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One worker implements/proves; Local reviews/commits; operator owns effects. Shared workspace INTERNAL_AGENT regardless of provider; no external research.

Allowed: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md`.

Forbidden: route/auth/config/package/lock/engine/ledger/storage/README/roadmap/governance/continuity edits; historical proof overwrite; extra tracked output; provider calls, real data, public sync/deployment, worker commit.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | Preview passive loads despite script sandbox |
| scope classification | distinct initial Preview assignment |
| risk sensitivity | inert control or post-parse policy falsely passes |
| selected role route | SINGLE_AGENT_MULTI_ROLE worker; distinct Local reviewer |
| role separation basis | worker cannot accept or authorize effects |
| escalation condition | safe design requires forbidden paths |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | implementer/evidence producer then distinct Local review |
| actor | INTERNAL_AGENT worker |
| role set | implementer, evidence producer; not closer |
| Role separation ledger | pending return then reviewer disposition |
| Evidence basis independent of memory | committed audit, source, browser receipts, Git status |
| Stop boundary | no worker commit or effect choice |
| Gate sequence | release, pre-implementation, focused checks, full return gate, reviewer gate |
| Self-review boundary | static PASS cannot prove browser denial |
| escalation condition | coherent in-scope mechanism unavailable |

## Required First Reads

AGENTS.md, bootstrap/front door/active handoff, paired packet, `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md`, accepted Print R2 completion, panel/unit/both specs, export route read-only, DESIGN.md, orientation/literal gotchas and output-artifact checker sources. Selected source regions only.

## Worker Autonomy / No-Question Rule

Choose coherent outcome-preserving mechanism and repair in-scope gate failures autonomously. Return unavailable proof/out-of-scope architecture to Local as blocked; no routine operator questions or silent authority extension.

## Pre-Flight Checks

Begin only after paired material commit, exact-hash continuity and bound pre-dispatch PASS. Capture clean executionBaseHead/status; run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md` before edits. Verify four source paths and three absent output paths; no stash apply.

## Write Ownership

Seven worker paths only; specs already GC-051 registered, registry read-only. Local owns release/review/commit/continuity. No foreseeable split within size budgets; return blocked rather than create eighth path.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | revise existing | Preview boundary |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | revise existing | canonical/provenance units |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | revise existing | resource and sandbox browser controls |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | revise existing | canonical fixture comparison and retained R2 regression |
| `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md` | create task-specific | policy/tradeoffs/untested contexts |
| `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json` | create task-specific | secret-safe observations and gates |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md` | create task-specific | pending review exact scope and gate join |

## Required Artifact Manifest

Exactly seven mandatory worker paths; four existing sources and three new task outputs. No eighth path or historical proof overwrite.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Yes | revise existing |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | Yes | revise existing |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | Yes | revise existing |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | Yes | revise existing |
| `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md` | Yes | create new |
| `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json` | Yes | create new |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md` | Yes | create new |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md` | NOT_BINDING_REFERENCE_WITH_REASON: synthetic proof, not standard |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-1","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"requiredProofIds":["PROOF-DENY-BEFORE-PARSE"]},{"requirementId":"REQ-2","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"],"requiredProofIds":["PROOF-UNIT","PROOF-CANONICAL"]},{"requirementId":"REQ-3","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"],"requiredProofIds":["PROOF-POSITIVE","PROOF-NEGATIVE","PROOF-MUTATION","PROOF-SANDBOX"]},{"requirementId":"REQ-4","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"],"requiredProofIds":["PROOF-PRINT-REGRESSION"]},{"requirementId":"REQ-5","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-6","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json"],"requiredProofIds":["PROOF-OBSERVATIONS"]},{"requirementId":"REQ-7","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-DENY-BEFORE-PARSE","kind":"effective policy before early payload resources","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"},{"proofId":"PROOF-UNIT","kind":"canonical identity/provenance regressions","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"},{"proofId":"PROOF-CANONICAL","kind":"exact Copy/Download canonical bytes","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"},{"proofId":"PROOF-POSITIVE","kind":"passive same/off-origin positive hits","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"},{"proofId":"PROOF-NEGATIVE","kind":"actual Preview zero hits and visible inline render","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"},{"proofId":"PROOF-MUTATION","kind":"policy-only removal discriminated","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"},{"proofId":"PROOF-SANDBOX","kind":"empty sandbox opaque origin blocked script","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"},{"proofId":"PROOF-PRINT-REGRESSION","kind":"canonical fixture/version native Print origin short-long output and existing mutations","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"},{"proofId":"PROOF-BOUNDARY","kind":"resource choices rendering limits untested contexts","locator":"docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md"},{"proofId":"PROOF-OBSERVATIONS","kind":"profile hit counts controls and gates","locator":"docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json"},{"proofId":"PROOF-RETURN","kind":"exact scope full gate no commit","locator":"docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md"}]}
```

## Implementation Contract

Harden only the existing Preview renderer. No mechanism is pre-approved. Establish effective resource denial before any payload parsing/loading, including early resource markup before a head, duplicate heads and payload-supplied permissive policy. Preserve canonical result.html unchanged. A Preview-only derived render document may differ; distinguish it from canonical source rather than replacing exported bytes with the wrapper.

Retain empty sandbox, opaque origin, blocked payload script and existing form/top-navigation/opener restrictions. Preserve visible benign text/headings and inline CSS from the default producer. Deny same-origin and off-origin passive network resources: images/srcset, link stylesheets, CSS @import/background/font and nested iframe/object/embed resource paths relevant to the selected policy. Declare data/blob behavior and rendering losses explicitly; prove any allowed data image with real decode/visibility assertions, otherwise state blocked/unproven. Payload meta/CSS cannot reopen network authority. This is presentation isolation, not universal sanitization or durable acceptance.

Positive control: a disposable context with the existing empty sandbox and no resource-denial policy must generate passive hits without scripts. Include same-origin controlled endpoints and an intercepted off-origin synthetic destination. Install interception before payload insertion; fulfill/abort locally, never forward fixture traffic. Positive image/CSS/font fixtures must actually load enough to trigger downstream dependencies. Record expected/observed hit classes. Reset counters, drive actual product Preview before any Print click, and require zero controlled hits plus visible benign text and inline style. Mutation removes only the chosen resource policy while retaining script sandbox; restored passive hits must fail the same negative oracle. Observe all pages/frames. No blanket same-origin exemption; normal Next/auth harness exceptions must be exact route/purpose bounded. Unknown fixture requests fail.

Keep Copy, Download and Print bound to displayed.result.html and its submitted snapshot. Assert exact copied/downloaded/printed HTML equals known canonical response fixture even when Preview srcdoc differs; do not remove or weaken stale-version assertions. Cover unsaved edits, latest-response supersession, failure preserving previous result and initialResult unknown provenance in focused units, with actual browser displayed-version/Print binding. Retain all existing Print R2 native invocation, isolation, short/120-row completeness and mutation assertions. No Print sizing/CSP/lifecycle redesign or new Print successor.

If a coherent design or oracle requires forbidden paths, return BLOCKED_WITH_REASON with narrowest design conflict; no automatic scope extension.

## Execution Plan

1. Verify clean authority/collisions and bound pre-implementation PASS.
2. Implement coherent Preview policy and resource controls; retain canonical identity and Print design.
3. Run both specs/unit/type/lint; strengthen Print comparison to canonical fixture without dropping R2 assertions.
4. Create three task-specific outputs and evidence join; full return gate PASS, hand back pending/no commit.

## Evidence Requirements

Capture clean executionBaseHead, seven changed paths, interception ordering, browser/profile, expected/observed resource classes, positive/actual-before-Print-negative/policy-only-mutation, inline render/data choices, sandbox regression, exact canonical bytes/version/provenance and retained Print regressions. Secret-safe command/result/path receipts and full worker gate. Synthetic fixtures allowed; no real HTML, cookie values, tokens or credentials.

## Acceptance Criteria

- [ ] Bound clean pre-implementation PASS before edits; exact seven paths; no worker commit.
- [ ] Executable empty-sandbox resource-positive control records same/off-origin image/style/CSS import/font/nested-resource hits; counters reset before actual Preview.
- [ ] Actual Preview before Print has zero controlled/unexplained hits, effective deny-before-payload under early-markup adversary, empty sandbox/opaque origin/blocked script and visible benign inline content/style.
- [ ] Policy-only removal mutation retains sandbox and makes negative oracle fail with passive hits.
- [ ] Canonical Copy/Download/Print bytes/version remain correct; derived Preview is distinguished; unsaved edits/superseded responses/prior-result failure/initialResult provenance covered.
- [ ] Existing Preview/Print and unit/type/lint checks PASS with all accepted R2 regressions retained; new proof/return disclose policy/resource choices, rendering limits and untested contexts.
- [ ] Full worker-return gate PASS with acceptance-evidence-json join and exact changed set including new return; no historical proof overwrite or effects.

Fail closed on inert control, post-parse policy, actual Preview request, ineffective mutation, missing benign render, stale/corrupted canonical output, weakened Print proof, unknown request or unauthorized path.

## Review Gate

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Consume valid evidence; audit policy ordering/canonical binding; one admitted distinct-fixture Preview probe for false-denial risk only. No broad duplicate Print suite/per-row review. Apply active MFRP M5/M10/safety/M20.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: FALSE_PREVIEW_RESOURCE_DENIAL
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: distinct early-resource fixture in actual Preview before Print; reuse valid worker Print regressions.
positiveControl: empty sandbox without resource policy produces intercepted same/off-origin passive hits.
negativeMutationClasses: actual request; post-parse policy; mutation inert; corrupt canonical version; benign render missing.
expectedInformationGain: effective early denial versus inert fixture or wrapper-only claim.
rerunCostReason: one bounded critical Preview probe, no duplicated Print suite.
reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B1-PREVIEW-RESOURCES
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


Independent Preview problem, not a reset/successor of Print. INITIAL sentinel fields are machine-required; worker self-proof names B1_PREVIEW_PASSIVE_RESOURCE_GAP with generation zero.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired Preview packet and roadmap | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | seven-path worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted worker paths and Local probe | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Exact continuity surface: active handoff, CVF_SESSION_MEMORY.md, CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json, CVF_SESSION/state/entries/nextAllowedMove.json and two generated active-state/bootstrap JSON surfaces. Exact dispatcher material: paired packet and roadmap. Worker has no access to these mutation lanes; reviewer closure is the named completion review. Any tracked independent probe requires explicit Local admission at return.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b1-preview-passive-resource-policy","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["B1_PREVIEW_PASSIVE_RESOURCE_GAP"],"reopened":[],"current":["B1_PREVIEW_PASSIVE_RESOURCE_GAP"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - synthetic UI presentation and tests authorize no authoritative transaction, process lock, ownership or security configuration mutation

## Foundation Storage Layout Block

N/A with reason: no durable foundation/index/storage owner created, moved or split.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal Chromium UI without external invocation

## Closure Checklist

Verify exact scope, browser resource/sandbox/canonical controls, retained Print, limitations, return/reviewer gates and material commit; continuity separately. Q001/Q004 OPEN.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx playwright test tests/e2e/artifact-export-preview-sandbox.spec.ts tests/e2e/artifact-export-print-browser.spec.ts --config playwright.config.mock.ts
npx vitest run src/components/ArtifactExportPanel.test.tsx
npm run check
npx eslint --max-warnings=0 src/components/ArtifactExportPanel.tsx src/components/ArtifactExportPanel.test.tsx tests/e2e/artifact-export-preview-sandbox.spec.ts tests/e2e/artifact-export-print-browser.spec.ts
Set-Location ../../..
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md
```

Existing runtime NEXTAUTH_URL/AUTH_URL port overrides allowed; no config edit/dependency install. System pdftotext may be selected via CVF_PDFTOTEXT_PATH; missing extraction returns diagnostic/blocked. Restore incidental tracked test-results state. Disposable PDFs/logs outside tracked outputs. Mock mode UI-only; no AI/governance behavior claim.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_COMPLETION_2026-10-01.md`
reviewerOwnedClosurePaths: named completion review, accepted worker paths, roadmap if required and separately authorized continuity; no worker closure access.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct reviewer |
| rolePattern | seven-path worker then Local review/commit |
| phase | release before implementation |
| baseHeadFor(phase) | dispatchBaseHead=`86dae9fa218a34048ba1420e9644497e3be87bdc`; executionBaseHead=clean released HEAD; closureBaseHead=Local at return |
| changedSetScope(phase) | exact seven worker paths; packet dispatcher-owned |
| traceScope(phase, actor) | resource/order/canonical observations and exact diff |
| commitOwner(phase) | Local closer; worker forbidden |
| crossBatchIsolation | Q001/Q004, durable B2, P11, effects/public/deploy parked |
| nextMoveSurfaces | committed packet, hash-bound continuity, release gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: none until bound release PASS
laneOwnedPaths: exact seven-path acceptance ledger
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: pending worker return, exact diff and full return gate

## Return-To-Orchestrator Conditions

BLOCKED_WITH_REASON for authority/collision mismatch, unavailable browser/extraction, inert controls, failing resource/canonical/Print evidence, unexpected requests or forbidden path need. Observed evidence plus smallest amendment; no automatic successor.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove Preview resource enforcement |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PREVIEW-RESOURCES --title "NCR HTML B1 Preview Passive Resource Policy" --date 2026-10-01 --base 86dae9fa218a34048ba1420e9644497e3be87bdc --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-html-b1-preview-passive-resource-policy --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Preview resource outcomes, seven-path manifest and canonical identity |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Acceptance evidence |
|---|---|---|
| D063/D064 in `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | Preview denial/canonical identity | actual resource controls/mutation and both specs |
| D062 | retain accepted Print limits/behavior | existing native/origin/output/version assertions |
| Q001/Q004 | OPEN/effects parked | exact scope, no effects |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B1 packet authoring, 2026-10-01 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired Preview baseline, this work order and NCR roadmap D064 |
| Allowed scope source | delegated Local dispatch; roadmap D063 and Preview owner audit |
| Before status evidence | clean worktree at `86dae9fa218a34048ba1420e9644497e3be87bdc` |
| After status evidence | paired packet and roadmap paths pending material commit; no worker edit |
| Diff evidence | exact three-path packet/roadmap set from Git status |
| Approval boundary | B1 packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b1-preview-resource-packet-20261001 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | synthetic Preview policy packet |
| claimDisposition | CLAIM_REJECTED: no implementation proven before evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker receipt pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker test pending |
| invocationBoundary | local synthetic browser/test process |
| interceptionBoundary | fulfill/abort synthetic resources, no forwarding |
| claimLanguage | existing sink gap pending bounded proof |
| forbiddenExpansion | no route/auth/storage/provider/real/public effects |

## Claim Boundary

Synthetic Preview denial and canonical identity only after release/review. No production incident, universal safety/all resource-browser support, paper/dialog/accessibility, provider governance, durable acceptance, Q001/Q004 exit, public sync or deployment. Print R2 limits retained.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Actor/data/store/writer, keys/backup/retention/RPO-RTO, cost and pilot/live effects operator-owned. No choice needed for synthetic scope.

