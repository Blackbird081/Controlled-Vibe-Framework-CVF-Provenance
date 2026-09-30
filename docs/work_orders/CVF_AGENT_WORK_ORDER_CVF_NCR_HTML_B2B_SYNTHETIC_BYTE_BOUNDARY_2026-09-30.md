# CVF Agent Work Order - NCR HTML B2b Synthetic Byte Boundary

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B2B-SYNTHETIC-BYTE-BOUNDARY

Dispatch base head: `e9395fb68`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md`

## Dispatch Prompt Envelope

Role: internal worker building an isolated synthetic decoded-string to UTF-8-byte handoff and contract; Local is reviewer/closer.

Canonical packet: this work order and `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Capture executionBaseHead and status at start. Do not edit before the bound pre-implementation gate passes.

Current-time notes: use synthetic strings and in-memory bytes only. No route call, browser automation, SQLite file, credential, provider, network or real data.

Do-not-misread notes: B2a already owns string identity. B2b owns a testable byte handoff; it does not decide acceptance. Do not hash JSON wire bytes, add an accept button or wire B2b into an active server/UI path.

Required first actions: read active continuity, this packet, paired baseline, D040 audit, B2a helper/contract, route/panel and named checker sources; capture HEAD and status; run the bound pre-implementation gate before edits.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, exact four-path changed set, focused tests, TypeScript, worker-return fast gate, no commit.

## Purpose

Produce a testable handoff from a decoded HTML string to defensively owned UTF-8 bytes, binding actual handed-off bytes to the existing B2a identity. This remains unconnected, so Profile A and Q001/Q004 stay open.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | 2026-09-30 approval of synthetic design/proof first and delegated Local work-order decisions | ACCEPT for B2b packet only; no real-data/effect grant |
| Current continuity | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, next allowed move | ACCEPT; synthetic B2b packet only |
| NCR roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D039-D040/Q001/Q004 | ACCEPT for conditional B2b boundary |
| Local audit | `docs/reviews/CVF_CVF_NCR_HTML_B2_BYTE_TRANSPORT_AUDIT_2026-09-30.md`, Decision | ACCEPT for source gap and synthetic next step |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md` | ACCEPT for exact scope, subject to committed release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route returns HTML while sourceHash covers source text only | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | buildHtml, POST | html, sourceHash | HTML export route | ACCEPT |
| Panel parses JSON and makes a Blob from the displayed HTML string | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handleGenerate`, `downloadHtml` | `response.json`, `Blob([html])` | Web consumer, read-only | ACCEPT |
| B2a computes UTF-8 HTML identity and rejects lone surrogates | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | `utf8Bytes`, `computeHtmlBytesIdentity` | B2a identity | existing pure helper | ACCEPT |
| Web package supports Vitest and TypeScript | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts | `scripts` | Web package | ACCEPT |
| D040 allows an in-memory B2b handoff only | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D039-D040/Q001/Q004 | B2b | NCR roadmap | ACCEPT |
| Local audit distinguishes JSON envelope and artifact bytes | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B2_BYTE_TRANSPORT_AUDIT_2026-09-30.md` | Findings / Position; Decision / Disposition | byte owner | Local review | ACCEPT |

## Negative Search And Collision Discipline

The four planned worker output paths were checked for collisions at dispatch authoring and were absent; the B2a helper and test already exist and are read-only. Recheck HEAD/status and exact path collisions before worker edits. This is a named-path check, not a full corpus claim.

## Current Runtime Freshness Verification

At dispatch base `e9395fb68`, Local re-read the route, panel, B2a helper/tests, D040 and the byte-transport audit. A scoped Web-source search found the B2a test import but no route/panel import of B2a; B2b paths are planned new files. The worker repeats the source and collision checks at execution HEAD. No actual JSON wire, browser or file bytes were observed.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B2B-SYNTHETIC-BYTE-BOUNDARY","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["isolated decoded-HTML-string to owned UTF-8-byte handoff"],"requiredProof":["B2a digest and byte-length parity","defensive byte copy","synthetic JSON and Blob roundtrip","same-length and Unicode mutation rejection","no active import","focused test and TypeScript"],"operatorCheckpoints":["Q001/Q004 real-data and store profile","real artifact acceptance","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","route or UI mutation","database write","provider call","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B2_BYTE_TRANSPORT_AUDIT_2026-09-30.md","completenessClaimChanged":false}}
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
| `INTERNAL_AGENT` | isolated B2b handoff module and contract | pure synthetic byte boundary; no active accept effect | source verification above and focused tests | no active adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2b interface | no ingress, auth, receipt, raw data or mutation grant | D040 and this bounded scope | external adapter deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace internal worker authors the exact byte-handoff module, tests, reference contract and pending return. Local reviews and commits. Operator retains Q001/Q004 data/effect decisions. This is not an external Web research assignment.

Allowed scope: create only `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts`, adjacent `html-artifact-byte-handoff.test.ts`, `docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`, and `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md`.

Forbidden scope: route/proof/component/page imports, auth, governance ledger, SQLite/data files, package/lock/config, CI, README, roadmap, session state, provider/live, real data, public sync and deployment. Do not add a store implementation in this tranche. Risk ceiling: reversible isolated candidate.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | Local accepted B2a helper and D040 found no byte custody join; operator approved synthetic proof first |
| scope classification | bounded source-backed pure local handoff and contract |
| risk sensitivity | byte mismatch hidden by text-only roundtrip or ambiguous custody |
| selected role route | SINGLE_AGENT_MULTI_ROLE internal worker with distinct Local reviewer |
| role separation basis | worker cannot self-accept or authorize data/effect |
| escalation condition | active route, storage, auth or real-data need |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one internal worker creates B2b handoff and pending evidence; Local reviews |
| actor | INTERNAL_AGENT worker |
| role set | implementer and evidence producer, not reviewer/closer |
| Role separation ledger | pending worker return followed by Local disposition |
| Evidence basis independent of memory | Git changed set, focused tests and Local byte-mutation probe |
| Stop boundary | worker cannot commit or authorize real-data/effect profile |
| Gate sequence | committed packet release, pre-implementation, focused tests, worker-return fast, Local reviewer-fast and pre-closure |
| Self-review boundary | worker test PASS is not independent acceptance |
| escalation condition | stop on active route, storage, auth, real-data or out-of-manifest need |

## Required First Reads

Read `AGENTS.md`, front door/bootstrap/active handoff, paired packet, D040 audit, B2a helper/test/contract, route/panel, guard orientation, literal-format gotchas and applicable output checkers. Capture HEAD and full `git status --short --untracked-files=all`.

## Worker Autonomy / No-Question Rule

Choose a small pure TypeScript API and synthetic fixtures within exact paths. Repair ordinary tests/checker findings without operator questions. If the handoff needs an active route change, persistence or authority expansion, return `BLOCKED_WITH_REASON` with the smallest dependency.

## Pre-Flight Checks

Start only after packet commit, exact-hash continuity and bound pre-dispatch gate. Record clean HEAD, verify four create paths absent, and run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md` before editing.

## Write Ownership

Worker owns exactly four create paths and leaves them uncommitted. The existing B2a module is read-only, with import allowed from B2b only. Local owns independent probe, any needed bounded repair, review, material commit and continuity.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | create | pure owned-byte handoff and verification using existing B2a identity, no I/O |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.test.ts` | create | independent byte oracle, synthetic JSON/Blob roundtrips and hostile mutation cases |
| `docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md` | create | byte custody/encoding boundary and limits, no store ratification |
| `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md` | create | exact changed set and gate evidence |

## Required Artifact Manifest

All four paths below are mandatory at handoff. They are planned create paths; no other worker deliverable is authorized. The worker must leave them pending and uncommitted.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | Yes | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.test.ts` | Yes | create |
| `docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md` | Yes | create |
| `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md` | Yes | create |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md` | NOT_BINDING_REFERENCE_WITH_REASON: new isolated byte-boundary reference, not an active-window binding reference |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-HANDOFF","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts"],"requiredProofIds":["PROOF-BYTE-OWNER","PROOF-B2A-PARITY"]},{"requirementId":"REQ-TEST","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.test.ts"],"requiredProofIds":["PROOF-ROUNDTRIP","PROOF-MUTATION"]},{"requirementId":"REQ-CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-BYTE-OWNER","kind":"decode-once UTF-8 bytes with defensive copy and actual-byte verification","locator":"html-artifact-byte-handoff.ts"},{"proofId":"PROOF-B2A-PARITY","kind":"digest and length agree with existing B2a identity","locator":"html-artifact-byte-handoff.ts"},{"proofId":"PROOF-ROUNDTRIP","kind":"independent JSON parse and in-memory Blob byte roundtrip","locator":"html-artifact-byte-handoff.test.ts"},{"proofId":"PROOF-MUTATION","kind":"same-length, Unicode, newline, BOM, malformed string and post-handoff mutation cases","locator":"html-artifact-byte-handoff.test.ts"},{"proofId":"PROOF-BOUNDARY","kind":"byte ownership and transport limits without store ratification","locator":"docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md"},{"proofId":"PROOF-RETURN","kind":"focused test, TypeScript, worker-return fast gate and no-commit evidence","locator":"docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D039 | reuse B2a identity algorithm and draft-only candidate state | no change to B2a helper or live route |
| D040 | bind decoded HTML string to owned UTF-8 bytes and verify the actual byte handoff | no browser/network/file custody claim |
| D035, Q001 and Q004 | keep Profile A and store/effect decisions parked | no real ledger, accepting actor or durable writer |

## Implementation Contract

Build a pure function that takes an exact decoded HTML string, rejects malformed Unicode as B2a does, and produces a defensively owned UTF-8 byte snapshot plus B2a-compatible digest and length. Verification must take the byte snapshot as input and recompute from those bytes; it must not trust a hash of a retained string while different bytes are passed onward. Prevent caller mutation of an input or returned byte array from silently changing the verified handoff: defensive copies at custody boundaries or an equivalent explicit immutable-byte contract with tests are required. If a B2a candidate is carried, it remains `DRAFT_UNACCEPTED`; sourceHash, attempt and receipt are separate supporting fields. Do not create another identity algorithm or an accept operation.

Tests must use an independent byte/hash oracle, not call the function under test to compute expected values. Include a synthetic JSON `stringify`/`parse` envelope and prove the decoded HTML artifact bytes agree with the B2b handoff while the JSON envelope bytes are not the identity. Use an in-memory `Blob([html], {type:'text/html;charset=utf-8'})` and compare `arrayBuffer()` bytes, not just read-as-text. Include non-ASCII and supplementary Unicode, NFC/NFD, CRLF/LF, leading BOM, same-byte-length title mutation, lone surrogate rejection, and post-handoff mutation. The reference contract names the first byte owner and the next unproven browser/file boundary; it must not repeat B2a's unratified durable-store proposal as a new decision.

## Execution Plan

1. Read named owners and output checkers; capture source and path collision status.
2. Write pure handoff module and focused synthetic tests with no route/import wiring.
3. Write the byte-boundary reference with custody and roundtrip limits; cite B2a for future-store proposals without ratifying them.
4. Run focused Vitest, TypeScript, no-active-import search and worker-return fast gate; prepare pending return.

## Evidence Requirements

Worker return includes executionBaseHead, initial/final status, exact changed set, test counts/exit, TypeScript, import search, gate result and an acceptance-evidence-json block joining each proof ID to its actual path. No raw credentials or real data. A passing in-memory test is not network-wire, saved-file, real-browser, durability or operator acceptance proof.

## Acceptance Criteria

- [ ] Decoded HTML string produces owned UTF-8 bytes with B2a-compatible digest and length; verification recomputes from actual bytes.
- [ ] Independent JSON-decoded string and in-memory Blob byte roundtrips pass without treating JSON envelope bytes as artifact bytes.
- [ ] Same-length byte mutation, Unicode normalization difference, CRLF/LF, BOM, malformed Unicode and byte aliasing fail or differ as specified.
- [ ] No duplicate acceptance state or identity algorithm; receipt and attempt IDs cannot promote `DRAFT_UNACCEPTED`.
- [ ] Reference identifies byte owner and unproven browser/file boundary; B2b is unimported by active route/pages; exact four-path manifest only.
- [ ] Focused tests, TypeScript and worker-return fast gate pass without route, disk or worker commit.

Fail conditions: active route/UI/auth import, disk or database mutation, real data/provider/network access, hash over JSON envelope or sourceHash, verification that ignores handed-off bytes, unowned path, or worker commit.

## Review Gate

Implementation begins only after paired packet material commit, continuity exact-hash binding, bound pre-dispatch PASS and worker pre-implementation PASS. Local evaluates returned evidence, inspects no-active-import scope and runs one independent same-length mutation against the handed-off bytes. Required gate failures remain worker-owned within scope.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: FALSE_BYTE_CUSTODY_OR_IDENTITY

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local uses a newly chosen synthetic same-length HTML byte pair and independent SHA-256 oracle, separate from worker fixtures.

positiveControl: a copied byte snapshot verifies against the B2a identity.

negativeMutationClasses: same-length byte mutation passes; string hash substitutes for handed-off byte check; returned array alias mutates custody; active route import.

expectedInformationGain: distinguish verification of handed-off bytes from a digest computed on a separate string.

rerunCostReason: one focused probe addresses byte custody risk without broad duplicate suite execution.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B2B-SYNTHETIC-BYTE-BOUNDARY
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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | handoff, test and contract | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2b-synthetic-byte-boundary","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - pure in-memory handoff has no durable write, cross-process lock, rollback or security mutation

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal handoff without external invocation

## Closure Checklist

Local verifies exact worker manifest, discriminating byte tests, reference boundary, worker return, review, material commit, continuity and clean pre-closure. Q001/Q004 remain open regardless of B2b result.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.test.ts`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest run src/lib/html-artifact-byte-handoff.test.ts
npm run check
Set-Location ../../..
rg -n "html-artifact-byte-handoff" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.test.ts
git status --short --untracked-files=all
```

Only the B2b test may import the handoff module; the handoff module may import B2a. Verify gate syntax with --help. Do not install dependencies.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_COMPLETION_2026-09-30.md`

reviewerOwnedClosurePaths: completion review only if required by closure gate; otherwise Local records acceptance in worker return under review-cost guidance.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker creates exact manifest and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`e9395fb68`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact four worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records synthetic byte custody, test and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/Q004, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact four-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused tests and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if byte handoff needs active route changes, if a claim requires unowned storage/auth, if test dependencies are unavailable, or if a forbidden effect/path is needed. Give the narrowest amendment; do not silently broaden.

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
| claimBoundary | Static checks cannot prove synthetic byte custody or accept HTML |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2B-SYNTHETIC-BYTE-BOUNDARY --title "NCR HTML B2b Synthetic Byte Boundary" --date 2026-09-30 --base e9395fb68 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2b byte contract, four-path worker manifest and operator boundary |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B2b packet authoring, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired B2b baseline, this work order and NCR roadmap D041 |
| Allowed scope source | delegated Local dispatch; roadmap D040 |
| Before status evidence | clean worktree at `e9395fb68` |
| After status evidence | paired packet and roadmap paths pending material commit; no worker edit |
| Diff evidence | exact three-path packet/roadmap set from Git status |
| Approval boundary | B2b packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b2b-byte-packet-20260930 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | isolated synthetic decoded-string to owned-byte handoff |
| claimDisposition | CLAIM_REJECTED: no implementation or active acceptance behavior claimed before worker evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: route receipt is read-only source context |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker focused tests pending |
| invocationBoundary | pure synthetic local tests only |
| interceptionBoundary | no direct interception or mandatory wrapper claimed |
| claimLanguage | source-identified B2b byte handoff, pending worker implementation and Local review |
| forbiddenExpansion | no route, ledger, database, provider, real data, artifact acceptance or public effect |

## Claim Boundary

This order authorizes only a pure, unconnected B2b byte handoff, focused tests and reference contract after dispatch release. It does not authorize a durable writer, active acceptance, Q001/Q004 closure, Profile B/C, pilot/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Operator later selects real-data classification/source, accepting account and authority, artifact store/instance, writer profile, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect before any B2 durable writer or route action.
