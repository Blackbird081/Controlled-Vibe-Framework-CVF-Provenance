# CVF Agent Work Order - NCR HTML B2a Synthetic Acceptance Contract

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B2A-SYNTHETIC-CONTRACT

Dispatch base head: `f8790a475`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md`

## Dispatch Prompt Envelope

Role: internal worker building an isolated synthetic HTML artifact identity candidate and design contract; Local is reviewer/closer.

Canonical packet: this work order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Capture executionBaseHead and status at start. Do not edit before the bound pre-implementation gate passes.

Current-time notes: use synthetic strings and pure functions only. No route call, SQLite file, credential, provider, network or real data.

Do-not-misread notes: this is B2a, not durable acceptance. An evaluation ALLOW receipt is evidence only. Do not add an accept button or wire the candidate into an active server/UI path.

Required first actions: read active continuity, this packet, paired baseline, B2 audit, route/proof/panel and the named checker sources; capture HEAD and status; run the bound pre-implementation gate before edits.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, exact four-path changed set, focused tests, TypeScript, worker-return fast gate, no commit.

## Purpose

Produce a testable exact-byte identity contract for rendered HTML and a source-backed design for a later single-host, one-writer acceptance store. The candidate remains unconnected, so Profile A and Q001/Q004 remain open.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | 2026-09-30 approval of single-host direction and synthetic design/proof first | ACCEPT for B2a only; no real-data/effect grant |
| Current continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, operator Q001/B2 checkpoint | ACCEPT; B2a resolves only synthetic design/proof portion |
| NCR roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D034/D035/D037/Q001/Q004 | ACCEPT for conditional B2 boundary |
| Local audit | `docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md`, Decision | ACCEPT for source gap and no active B2 |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` | ACCEPT for exact scope, subject to committed release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route returns HTML while sourceHash covers source text only | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | buildHtml, POST | html, sourceHash | HTML export route | ACCEPT |
| Receipt helper submits excerpt, not exact rendered bytes | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | fetchGovernanceReceipt | fetchGovernanceReceipt | governance evaluation helper | ACCEPT |
| B1 panel already tracks displayed attempt/result | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | DisplayedResult, handleGenerate | displayed | Web consumer, read-only | ACCEPT |
| Existing single-node SQLite design is owned by pending execution | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | class and constructor | PendingAgentExecutionSqliteStore | other owner, design precedent only | ACCEPT |
| Web package has Vitest, TypeScript and better-sqlite3 dependency | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts and dependencies | better-sqlite3 | Web package | ACCEPT |
| D037 rejects active B2 without authority/storage selection | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D037/Q001/Q004 | B2 | NCR roadmap | ACCEPT |
| Local audit limits prior no-dispatch decision to active B2 | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md` | Decision / Disposition | REVIEW_COMPLETE_NO_DISPATCH | Local review | ACCEPT |

## Negative Search And Collision Discipline

Exact proposed B2a file paths did not exist at dispatch authoring; `rg -n "B2a|SYNTHETIC_ACCEPTANCE_CONTRACT" docs CVF_SESSION` returned no match before packet creation. The adjacent candidate file names are also new. Recheck HEAD/status and path collision before worker edits. Negative search is limited to named roots, not a full corpus claim.

## Current Runtime Freshness Verification

At dispatch base `f8790a475`, Local re-read the named route, receipt helper, B1 panel, pending-execution SQLite precedent, D037 and the B2 audit. `rg -n "html-artifact-acceptance-candidate" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` found no active or test import before packet authoring. This is a scoped search of one Web source tree; the worker repeats it at execution HEAD. The route currently returns HTML without an acceptance write, and the proposed candidate has no runtime claim.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B2A-SYNTHETIC-CONTRACT","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["isolated exact-byte HTML identity candidate"],"requiredProof":["UTF-8 exact-byte hash","changed rendered field changes identity","tamper rejection","receipt is evidence only","no active import","focused test and TypeScript"],"operatorCheckpoints":["Q001/Q004 real-data and store profile","real artifact acceptance","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","route or UI mutation","database write","provider call","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Earlier Web advisory is not private CVF proof |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | isolated candidate module and contract | pure synthetic identity; no active accept effect | source verification above and focused tests | no active adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2a interface | no ingress, auth, receipt, raw data or mutation grant | D037 and this bounded scope | external adapter deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace internal worker authors the exact candidate, tests, reference contract and pending return. Local reviews and commits. Operator retains Q001/Q004 data/effect decisions. This is not an external Web research assignment.

Allowed scope: create only `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts`, adjacent `html-artifact-acceptance-candidate.test.ts`, `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`, and `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md`.

Forbidden scope: route/proof/component/page imports, auth, governance ledger, SQLite/data files, package/lock/config, CI, README, roadmap, session state, provider/live, real data, public sync and deployment. Do not add a store implementation in this tranche. Risk ceiling: reversible isolated candidate.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | Local found no authoritative exact-HTML acceptance owner; operator approved synthetic design/proof |
| scope classification | bounded source-backed pure local candidate and design contract |
| risk sensitivity | misleading acceptance and exact-byte identity |
| selected role route | SINGLE_AGENT_MULTI_ROLE internal worker with distinct Local reviewer |
| role separation basis | worker cannot self-accept or authorize data/effect |
| escalation condition | active route, storage, auth or real-data need |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one internal worker creates candidate and pending evidence; Local reviews |
| actor | INTERNAL_AGENT worker |
| role set | implementer and evidence producer, not reviewer/closer |
| Role separation ledger | pending worker return followed by Local disposition |
| Evidence basis independent of memory | Git changed set, focused tests and Local byte-mutation probe |
| Stop boundary | worker cannot commit or authorize real-data/effect profile |
| Gate sequence | committed packet release, pre-implementation, focused tests, worker-return fast, Local reviewer-fast and pre-closure |
| Self-review boundary | worker test PASS is not independent acceptance |
| escalation condition | stop on active route, storage, auth, real-data or out-of-manifest need |

## Required First Reads

Read `AGENTS.md`, front door/bootstrap/active handoff, paired packet, B2 audit, route/proof/panel, existing SQLite precedent, guard orientation, literal-format gotchas, applicable output checkers. Capture HEAD and full `git status --short --untracked-files=all`.

## Worker Autonomy / No-Question Rule

Choose a small pure TypeScript API and synthetic fixtures within exact paths. Repair ordinary tests/checker findings without operator questions. If exact identity needs an active route change, persistence or authority expansion, return `BLOCKED_WITH_REASON` with the smallest dependency.

## Pre-Flight Checks

Start only after packet commit, exact-hash continuity and bound pre-dispatch gate. Record clean HEAD, verify three create paths absent, and run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` before editing.

## Write Ownership

Worker owns exactly four create paths and leaves them uncommitted. Local owns independent probe, any needed bounded repair, review, material commit and continuity.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | create | pure UTF-8 byte identity and verification, no I/O |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts` | create | discriminating synthetic positive/negative tests |
| `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` | create | future single-host contract and unresolved decisions, marked proposal |
| `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md` | create | exact changed set and gate evidence |

## Required Artifact Manifest

All four paths below are mandatory at handoff. They are planned create paths; no other worker deliverable is authorized. The worker must leave them pending and uncommitted.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | Yes | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts` | Yes | create |
| `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` | Yes | create |
| `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md` | Yes | create |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` | NOT_BINDING_REFERENCE_WITH_REASON: new candidate design contract, not an active-window binding reference |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-CANDIDATE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts"],"requiredProofIds":["PROOF-BYTES","PROOF-SEPARATION"]},{"requirementId":"REQ-TEST","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts"],"requiredProofIds":["PROOF-MUTATION","PROOF-RECEIPT"]},{"requirementId":"REQ-CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-BYTES","kind":"hash and verify exact UTF-8 rendered HTML bytes","locator":"html-artifact-acceptance-candidate.ts"},{"proofId":"PROOF-SEPARATION","kind":"attempt and receipt evidence cannot set accepted state","locator":"html-artifact-acceptance-candidate.ts"},{"proofId":"PROOF-MUTATION","kind":"different rendered bytes and one-byte tamper are rejected","locator":"html-artifact-acceptance-candidate.test.ts"},{"proofId":"PROOF-RECEIPT","kind":"synthetic ALLOW receipt leaves candidate unaccepted","locator":"html-artifact-acceptance-candidate.test.ts"},{"proofId":"PROOF-BOUNDARY","kind":"proposed store and operator decisions are clearly separated","locator":"docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md"},{"proofId":"PROOF-RETURN","kind":"focused test, TypeScript, worker-return fast gate and no-commit evidence","locator":"docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D034 | bind identity to exact rendered HTML bytes, not sourceHash | active route and durable acceptance |
| D035 | synthetic-only Profile A | real ledger Profile B/C |
| D037 and Q004 | specify proposed single-host, one-writer store and readback contract | actual store, backup and writer effect |
| Q001 | receipt is supporting evidence only | ALLOW is not artifact acceptance |

## Implementation Contract

Build a pure function that takes the exact returned HTML string plus explicit local version/attempt metadata and computes a SHA-256 over UTF-8 bytes. Preserve distinction among sourceHash, HTML hash, attempt ID and receipt ID. A candidate always remains `DRAFT_UNACCEPTED`. Verification uses the exact bytes, not a re-render from input fields. Do not expose an operation named or behaving as durable accept.

Tests must show identical bytes have stable identity; title, claim boundary or generated time changes in the HTML produce changed identity even when source text is unchanged; non-ASCII UTF-8 is deterministic; a single-byte mutation invalidates identity; and a receipt marked ALLOW cannot change acceptance state. The reference contract names proposed immutable version/store interfaces, transaction/readback and ambiguous-outcome behavior, but explicitly states these are not implemented.

## Execution Plan

1. Read named owners and output checkers; capture source and path collision status.
2. Write pure candidate module and focused synthetic tests with no route/import wiring.
3. Write the reference design contract with actor/store/write/recovery proposal and the open operator decisions.
4. Run focused Vitest, TypeScript, no-active-import search and worker-return fast gate; prepare pending return.

## Evidence Requirements

Worker return includes executionBaseHead, initial/final status, exact changed set, test counts/exit, TypeScript, import search, gate result and an acceptance-evidence-json block joining each proof ID to its actual path. No raw credentials or real data. A passing pure test is not durability or operator acceptance proof.

## Acceptance Criteria

- [ ] Exact returned HTML bytes, not source text or re-rendered input, determine candidate identity.
- [ ] Receipt and attempt IDs remain distinct supporting data; ALLOW alone never accepts.
- [ ] Synthetic mutation, alternate rendered field and UTF-8 cases pass.
- [ ] Contract marks proposed store, actor, transaction and recovery boundaries as future design with unresolved operator decisions.
- [ ] Candidate is unimported by active route/pages; only exact four-path manifest changes.
- [ ] Focused tests, TypeScript and worker-return fast gate pass without I/O or worker commit.

Fail conditions: active route/UI/auth import, disk or database mutation, real data/provider/network access, missing acceptance separation, unowned path, or worker commit.

## Review Gate

Implementation begins only after paired packet material commit, continuity exact-hash binding, bound pre-dispatch PASS and worker pre-implementation PASS. Local evaluates returned evidence, inspects no-active-import scope and runs one small independent byte-mutation probe if the proof is decision-changing. Required gate failures remain worker-owned within scope.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: FALSE_ARTIFACT_IDENTITY_OR_ACCEPTANCE

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local uses a newly chosen synthetic HTML byte pair with one changed rendered field, independent of worker fixtures.

positiveControl: identical UTF-8 bytes verify against one stable hash.

negativeMutationClasses: sourceHash used as artifact identity; one-byte HTML mutation passes; ALLOW receipt flips accepted state; active route import.

expectedInformationGain: distinguish true byte binding from an input-field or copy-only label.

rerunCostReason: one focused probe addresses the only synthetic identity risk without broad duplicate suite execution.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B2A-SYNTHETIC-CONTRACT
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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | candidate, test and contract | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2a-synthetic-acceptance","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - pure unconnected candidate has no durable write, cross-process lock, rollback or security mutation

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal candidate without external invocation

## Closure Checklist

Local verifies exact worker manifest, discriminating tests, reference contract boundary, worker return, review, material commit, continuity and clean pre-closure. Q001/Q004 remain open regardless of B2a result.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest run src/lib/html-artifact-acceptance-candidate.test.ts
npm run check
Set-Location ../../..
rg -n "html-artifact-acceptance-candidate" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts
git status --short --untracked-files=all
```

Only the test import may reference the candidate module. Verify gate syntax with --help. Do not install dependencies.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_COMPLETION_2026-09-30.md`

reviewerOwnedClosurePaths: completion review only if required by closure gate; otherwise Local records acceptance in worker return under review-cost guidance.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker creates exact manifest and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`f8790a475`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact four worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records synthetic identity, test and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/Q004, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact four-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused tests and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if exact-byte identity needs active route changes, if a design claim requires unowned storage/auth, if test dependencies are unavailable, or if a forbidden effect/path is needed. Give the narrowest amendment; do not silently broaden.

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
| claimBoundary | Static checks cannot prove synthetic candidate behavior or accept HTML |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2-SYNTHETIC-CONTRACT --title "NCR HTML B2 Synthetic Acceptance Contract" --date 2026-09-30 --base f8790a475 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed exact-byte contract, four-path worker manifest and operator boundary |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B2a packet authoring, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired B2a baseline, this work order and NCR roadmap D038 |
| Allowed scope source | operator approved synthetic design/proof; roadmap D037 |
| Before status evidence | clean worktree at `f8790a475` |
| After status evidence | paired packet and roadmap paths pending material commit; no worker edit |
| Diff evidence | exact three-path packet/roadmap set from Git status |
| Approval boundary | B2a packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b2a-synthetic-packet-20260930 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | isolated synthetic exact-byte identity candidate |
| claimDisposition | CLAIM_REJECTED: no implementation or active acceptance behavior claimed before worker evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: route receipt is read-only source context |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker focused tests pending |
| invocationBoundary | pure synthetic local tests only |
| interceptionBoundary | no direct interception or mandatory wrapper claimed |
| claimLanguage | source-identified B2a candidate, pending worker implementation and Local review |
| forbiddenExpansion | no route, ledger, database, provider, real data, artifact acceptance or public effect |

## Claim Boundary

This order authorizes only a pure, unconnected B2a identity candidate, focused tests and a proposed design contract after dispatch release. It does not authorize a durable writer, active acceptance, Q001/Q004 closure, Profile B/C, pilot/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Operator later selects real-data classification/source, accepting account and authority, artifact store/instance, writer profile, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect before any B2 durable writer or route action.
