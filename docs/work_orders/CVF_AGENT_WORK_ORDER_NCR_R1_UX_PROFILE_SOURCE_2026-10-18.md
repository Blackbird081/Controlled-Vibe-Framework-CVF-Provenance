# NCR R1 UX/Profile Source - Worker Work Order

Memory class: governed-work-order
docType: work_order
Status: DISPATCH_READY
Date: 2026-10-18
Batch ID: CVF-NCR-R1-UX-PROFILE-SOURCE-20261018
Inspection base: 8d39e708fed33ecbba5ce2e5e092738d4c4a3449
Commit mode: WORKER_MUST_NOT_COMMIT
rawMemoryReleased=false
providerExecutionAuthority: FORBIDDEN
Decision owner: LOCAL Root
Intended governed path: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT source implementation worker; Local Root reviews and commits.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; baseline `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`.
Commit mode: WORKER_MUST_NOT_COMMIT. executionBaseHead=actual clean released HEAD captured at start.
Current-time notes: one30min source task, no app/browser/provider or test.
Do-not-misread notes: exact4 worker; capabilities is display information, not authorization; old chains unchanged.
Required first actions: progressive startup, pair/required owners, bound pre-implementation PASS, return scaffold and current source pins.
Return contract: COMPLETE_PENDING_REVIEW only after actual mandatory proof and bound full return PASS; otherwise BLOCKED_WITH_REASON preserving failures.

## Purpose And Authority

Close the selected R1 mixed-language/profile-disclosure source gap for existing Work Transfer HTML. The finite worker result is a source-only presentation change plus a four-path evidence return, bounded by `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` section R1/R2 Exit And Gap Disposition and paired candidate GC-018 baseline. Local Root owns final source review and closure. No R1/R2 stage exit or actual effect admission follows automatically.

## Agent Roles

Dispatcher/closer: Local Root. Worker: one shared-workspace INTERNAL_AGENT. Reviewer: independent Local Root source reviewer, consuming worker evidence and doing a focused invariant/diff review. EXTERNAL_AGENT_CLI_MCP is not selected; no external model/CLI/MCP invocation. Future external research is advisory; Local retains private-CVF verification and decision.

## Locked Implementation Contract

Paired baseline section Locked Source Contract items 1-4 are normative. Implement vi/en UI copy using current `useLanguage` in exactly two component files. Translate user-visible job, criteria, link/reconcile, review, notice/error, Stop and status strings owned by those two files. New notices in touched components must react to language changes; HtmlDraftRecovery remains read-only with its existing vi/en table and retained notice behavior; keep user data and identifiers literal. Keep `jobDecisions === true` as the existing job-control enablement gate. Capture the exact `effectBoundary === 'LOCAL_SYNTHETIC'` enum as presentation state under the same scope/epoch checks and clear it with scope; pass it to the panel only when both fields are present. A missing/malformed enum retains the current job workflow and generic disclosure. For untyped general errors, use friendly localized UI fallback and optionally unchanged diagnostic detail; do not invent a full wire-error enum. The panel retains generic receipt/destination disclosure for fallback/standalone use. This is observed current profile, not a guarantee that future export POST configuration cannot change. Keep the existing auth, scope/epoch/expiry, journal, job/version/hash joins, write and decision logic within their locked semantics. No new generic helper unless Root separately admits it. Keep `ArtifactExportPanel.tsx` below 975 lines from current 883.

Selected pre-Build text must explain local HTML rendering, local synthetic draft storage, no governance receipt request, unverified/unaccepted draft, same-person synthetic review and local Stop/unknown result/cost limits. General fallback must not claim this profile. No provider/account chooser or fake control.

## Required Artifact Manifest

| Path | Action |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx` | MODIFY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | MODIFY |
| `docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md` | CREATE |
| `docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json` | CREATE |

Worker return path: `docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md`

Any need for a third source file, test edit, server/API/schema change or generated dependency mutation is a stop and consolidated finding, not silent scope expansion.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1 language/profile gap | current governed disposition | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | section R1/R2 Exit And Gap Disposition lines 42-50 | selected finite follow-through | roadmap Local disposition | ACCEPT |
| Capability contains local boundary | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.ts` | GET capabilities lines 82-88 | `jobDecisions; effectBoundary` | `jobRouteHandlers` | ACCEPT |
| Job component discards boundary and contains English copy | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx` | capability lines 68-73; UI lines 190-230 | `data; HtmlJobControls` | `HtmlJobControls` | ACCEPT |
| Recovery already has language table and remains read-only | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlDraftRecovery.tsx` | `COPY` and `setNotice`, lines 15-27, 51-123 | `useLanguage`, `notice` | `HtmlDraftRecovery` | ACCEPT |
| Generic disclosure and English Stop remain | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | preGenerateDisclosure and Stop UI, lines 660-690 | `LABELS`, `useLanguage`, `Stop locally` | `ArtifactExportPanel` | ACCEPT |
| Historic current-source browser proof is bounded | review evidence | `docs/reviews/CVF_NCR_R1_INTEGRATED_HTML_JOB_BROWSER_LOCAL_COMPLETION_REVIEW_2026-10-18.md` | completion/claim boundary | synthetic joined journey | Local reviewer | ACCEPT |

Actual dispatch rechecks these line locators and SHA256s at the committed base. They do not certify the proposed implementation.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap concern | Worker requirement | Evidence at return | Status |
| --- | --- | --- | --- |
| R1 Vietnamese and progressive disclosure | REQ-LANGUAGE | source diff and copy inventory in both languages | PLANNED |
| R1 selected profile/effect explanation | REQ-PROFILE | observed capabilities enum and panel fallback source inspection | PLANNED |
| R1 recovery/Stop/review honesty | REQ-LIMITS | exact notices and no logic/wire change diff | PLANNED |
| R2/W05 pre-live effect profile/config changes | no server/effect grant | Local later design admission | DEFERRED_WITH_REASON |
| Keyboard, small screen and non-coder comprehension | no test/run in this source packet | separately admitted user-role walkthrough | NOT_EVALUATED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-R1-UX-PROFILE-SOURCE-20261018
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

## Semantic Convergence Outcome

This new `ncr-r1-ux-profile-disclosure` problem is limited to the roadmap's language/disclosure delta. It is not a redefinition or reset of the spent source recovery, browser or parent chains. Its initial blocker is current-source mixed-language and generic selected-profile disclosure. Compiler/lint/source review may be `OTHER` / `NAMED_OBSERVABLE_PROOF` only for static source properties; no component or runtime behavior is proved by those tools. Worker return must bind actual work-order SHA256 and make any successor claim only from admissible evidence.

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"ncr-r1-ux-profile-disclosure","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["CURRENT_SOURCE_MIXED_LANGUAGE_AND_GENERIC_PROFILE_DISCLOSURE"],"reopened":[],"current":["CURRENT_SOURCE_MIXED_LANGUAGE_AND_GENERIC_PROFILE_DISCLOSURE"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

Root requires the canonical checker to evaluate this final actual work order as one eligible object before release. Zero-object PASS is insufficient. No historical source/browser budget is refreshed.

## Work-Order Acceptance Evidence Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-LANGUAGE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"requiredProofIds":["PROOF-REQ-LANGUAGE"]},{"requirementId":"REQ-PROFILE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"requiredProofIds":["PROOF-REQ-PROFILE"]},{"requirementId":"REQ-LIMITS","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"requiredProofIds":["PROOF-REQ-LIMITS"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md","docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json"],"requiredProofIds":["PROOF-REQ-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-REQ-LANGUAGE","kind":"SOURCE_INSPECTION","locator":"docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json#REQ-LANGUAGE"},{"proofId":"PROOF-REQ-PROFILE","kind":"SOURCE_INSPECTION","locator":"docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json#REQ-PROFILE"},{"proofId":"PROOF-REQ-LIMITS","kind":"SOURCE_INSPECTION","locator":"docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json#REQ-LIMITS"},{"proofId":"PROOF-REQ-RETURN","kind":"SOURCE_INSPECTION","locator":"docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json#REQ-RETURN"}]}
```

Proof IDs require actual source/diff identities, inspected strings and invariant evidence. Locator existence alone is not proof. Existing test files are read-only historical references; no test is added or run.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
returnTimeRecheck: REQUIRED_BEFORE_REPAIR
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | exact source pair and final-bound admission | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet and exact current6 | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker and exact current6 | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact4 worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | IMPLEMENTATION | worker | IMPLEMENTATION | installed tsc and scoped lint only; no test run | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | exact return/evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact4 final return | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact4 plus Local source review | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | bounded material closure | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | source invariants and pending UX evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | current6 after accepted source | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | committed material and continuity ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

`focused_checker_tests` is a framework gate identifier. Its selected worker evidence is static compiler/lint/source inspection only, with no test implementation or run. This gate binds the selected static proof only; no test execution is authorized. Closeability is validated on the actual final packet before release.

## Independent Review Probe Admission Contract

independentProbeRequired: NOT_APPLICABLE_WITH_REASON
independentProbeReason: UI copy and presentation-only prop on the exact two component files; no high-risk runtime effect or protected governance mutation is selected. Root independently reviews the diff/source and selected/fallback conditions, without an executable probe or test run in this scope.

## Budget / Tools / Temporary Resources

One worker source task, 30 minutes inclusive; at most two final worker-return gate attempts after all four files are prepared. Installed local `tsc --noEmit` and scoped ESLint may run at most twice each, with a second run only after a named in-scope source correction, with safe environment and `envDir=false` where supported; no package install, Next start, browser, provider, network, `.env`, private data or test run. Ignored scratch under `.cvf/runtime/ncr-r1-ux-profile-20261018` may hold safe intermediate notes. No recursive delete. A noncloseable source contradiction ends the lane with one consolidated finding; no automatic redispatch or fresh recovery budget.

## Forbidden Scope

Only the exact four worker paths are writable. `HtmlDraftRecovery.tsx` and all other source, test, server, API, i18n, guard, roadmap and continuity paths are read-only to the worker. No schema/auth/writer/provider/generic chooser/runtime change, test mutation/run, receipt request, external effect, production/public/deploy, nested delegation, stage or commit. Preserve user content, protocol enums, owner and hash joins exactly.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python -B governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md --max-return-lines 450 --max-return-bytes 64000`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
scaffoldPreparationCommand: `python -B governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md --title "NCR R1 UX Profile Source Worker Return" --check-shape`

Return includes exact four-path manifest and Git status, source hashes/diff, language-copy inventory, selected/fallback proof, unchanged wire/auth/write invariants, static check results, acceptance proof IDs, SCEC successor and explicit pending component/walkthrough evidence. No executable UI or governance claim.

## Reviewer Closure Conversion

The worker finishes the bound full return gate on its exact four paths before Root adds closure artifacts. Root checks exact paths and final returned evidence, performs focused independent Local source review, decides ACCEPT_BOUNDED or consolidated blocker, then adds exactly one necessary Local completion review and the existing roadmap status update. Accepted closure material is worker four plus Root review one plus roadmap one (exact six); current6 is synchronized separately. No optional document, registry or guard change. Root does not turn static proof into R1 exit, user-role usability or actual effect readiness. Reviewer repair remains inside the exact source manifest; third repair round cannot auto-dispatch.

| Field | Value |
|---|---|
| completionReviewPath | docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-18.md |
| reviewerOwnedClosurePaths | docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-18.md; docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md; separate current6 |
| closureOwner | LOCAL Root |
| workerCommitPermission | FORBIDDEN |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`.

Returned 27; IDs: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006. Raw `.cvf/runtime/ncr-r1-ux-profile-20261018/planning/adif-dispatch.json` SHA256 `669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687`.

Impact: selected named source only; no corpus claim, provider memory authority, protected worker write, detached process, broad proof reuse or runtime promotion. Exact pair/worker/closure/current6 scopes, actual source fields, independent Local review and mandatory gate/raw-failure retention handle applicable items. No new guard selected.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_tables.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/run_adif_defect_resolver.py |
| literalTokensReviewed | exact4 worker and exact2 dispatch; exact6 closure material; separate current6; immutable pair; SOURCE_INSPECTION; existing jobDecisions enablement and LOCAL_SYNTHETIC presentation enum; full bound return; no source test mutation/run |
| gateRunPurpose | confirmation of consolidated source-only admission and exact schema/path/authority bindings before release; not product proof |
| claimBoundary | declarations and compiler/lint cannot establish UI behavior, effect admission or R1/R2 exit |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-R1-UX-PROFILE-SOURCE-20261018 --title "NCR R1 UX profile source" --date 2026-10-18 --base 8d39e708fed33ecbba5ce2e5e092738d4c4a3449 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key ncr-r1-ux-profile-disclosure --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| checkerReadAheadConfirmation | applicable checker sources and final schema/literal fields read before release; original candidate failure retained |
| manualEditsAfterScaffold | Exact source, proof, role, return and non-execution constraints |
| docOnlyNewFields | presentation-only selected profile prop |
| claimBoundary | Candidate only; no actual gate or worker release. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | NOT_APPLICABLE_WITH_REASON: current private source composition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | this source admission pair |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Local verifies private CVF; no external source promotion |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source/dependency reads only, no all-files claim.

## Knowledge System Reconciliation

- Knowledge task class: NON_KNOWLEDGE_SOURCE_IMPLEMENTATION
- Source manifest: Source Verification Block and exact four worker manifest
- Source manifest hash: NOT_APPLICABLE; no corpus manifest or map produced
- Enumeration safety: filesystem-backed explicit named-file reads
- Intake registry or ledger: no knowledge intake selected
- Authority assets: immutable accepted source, Local review, design and current continuity
- Derived views: no knowledge view produced
- Semantic region ledger: no mapping regions
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: NONE within zero-asset scope
- Cross-region links: NONE
- Drift check: source pins before edits and final hash reconciliation
- Rebuildability check: Git/source manifest and named commands
- Retrieval boundary: no retrieval-readiness assertion
- Adversarial verification: no map verification selected
- Knowledge-map verdict: PARTIAL

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: named local source correction, no corpus reassessment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY. No public-sync effect.

## Epistemic Process Block

Expected Result / Prediction: two component source edits can improve current selected-profile explanation without changing API or writes. Evidence Comparison: current components contain mixed language and generic disclosure; capabilities has the exact local enum but export resolves profile again. Contradiction Or Gap Disposition: copy remains conditional on observed capability; fallback stays generic; future effect configuration is R2/W05. Claim Update: dispatch candidate only; component behavior and noncoder comprehension remain untested.

## Claim Boundary

No source edit, executable test, UI run, provider/live proof, receipt, production/public/deploy or stage exit has occurred under this draft.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT Local dispatcher/reviewer; decision owner=LOCAL |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-r1-ux-profile-source-admission-20261018 |
| Working directory | repository root |
| Command or tool surface | named source analysis; two read-only planning aides; pair authoring and mandatory governance checks |
| Target paths | `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` |
| Allowed scope source | operator next and standing autonomous roadmap continuation; selected R1/R2 exit-gap disposition |
| Before status evidence | 8d39e708fed33ecbba5ce2e5e092738d4c4a3449; git status --short = clean; clean worktree before admission |
| After status evidence | exact2 source admission pair; source implementation awaits committed current6 and bound pre-dispatch PASS |
| Diff evidence | git diff --name-status; git diff --check; exact2 reconciliation |
| Approval boundary | source2 UI presentation plus return2 only; no protected worker path or effect |
| Claim boundary | source contract only; no source/runtime proof before execution |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-r1-ux-profile-source-admission-20261018 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` |
| Manifest delta | MATCH exact2 dispatch material; current6 separately |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | source-only R1 language and profile description |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: actual source/static evidence only at return |
| receiptEvidence | N/A with reason: no governance receipt selected |
| actionEvidence | N/A with reason: source edits have not begun |
| invocationBoundary | one INTERNAL_AGENT source task; mandatory gates; no app/browser/provider invocation |
| interceptionBoundary | no runtime interception or universal enforcement claim |
| claimLanguage | exact pins, source inspection and actual compiler/lint outputs only |
| forbiddenExpansion | server/schema/auth/writer/guard/test/runtime/real data/production/public/deploy |

## Current Runtime Freshness Verification

Source identity at inspection HEAD `8d39e708fed33ecbba5ce2e5e092738d4c4a3449`; raw-byte named-file record `.cvf/runtime/ncr-r1-ux-profile-20261018/source-freshness.json` SHA256 `b6918cb9c9fb30b94c4c2899f238150cb539bd90aa7874e53ff03da5c8b2f0c2`. Selected source2 exists; return2 planned paths are unoccupied. No runtime was started; refresh identity if any source changes before release.

| Source file | SHA256 |
|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx | b5b3e2c84913f5bac67e805365431af2c5a461e3066f1fe635080db784dbbc2a |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx | 999f6710d4d9f18268c86f707be709f8e6aaddcb2d449656a3fa27c53f4cada8 |

## Negative Search And Collision Discipline

No negative owner-absence claim is selected. Both component owners and the server capability field exist at the stated source pins; Root checked named paths/symbols. User data and protocol strings are not translated. No repository-wide inference is made.

## Authority Chain

Frozen doctrine/operating model -> AGENTS/canonical standards -> current roadmap R1/R2 exit-gap disposition -> this fresh exact pair -> committed current6 and bound pre-dispatch PASS -> one source worker. Operator latest next and standing autonomous continuation cover this finite reversible source action. Prior source/browser grants stay spent and read-only.

## Intake Role Routing Decision

Scope classification: bounded existing-owner UI copy/presentation source correction.
Intake summary: actual source2 mixed-language/generic-profile gap; no new authority or runtime owner.
Risk sensitivity: source-only/static; protected sources and effects remain outside worker scope.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Escalation condition: one consolidated source/scope contradiction to Local; routine details resolved within contract.

## Required First Reads And Source-to-Requirement Mapping

Read bootstrap, CVF_SESSION_MEMORY.md and named active handoff; both external/local role methods; guard orientation/literal gotchas/lifecycle Outcome-Bound rule; work-order template and execution SOP; this complete pair and its source/read map; DESIGN.md; applicable output checker sources before authoring. Both source files are fully read before edits. Read HtmlDraftRecovery, useHtmlBuildAttempts, html-job-api, export route and language owner only to protect declared interfaces.

Language -> existing useLanguage/LABELS and job JSX; profile -> authenticated capabilities effectBoundary and selected panel prop; invariant -> existing owner/epoch/expiry/journal/hash/POST/GET conditions. Existing tests only map future proof; no test read becomes current execution evidence.

## Write Ownership

Worker exact4 Required Artifact Manifest plus owned ignored `.cvf/runtime/ncr-r1-ux-profile-20261018/worker`. Root owns pair2 and separate current6. After worker final bound gate, Root adds review `docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-18.md` and roadmap `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` for exact6 material; current6 separately. No generated registry or source dependency mutation selected.

## Pre-Flight Checks

Root validates actual source pins, pair hashes, SCEC object count and declared closeability; commits pair then current6; runs bound pre-dispatch PASS on clean HEAD before release. Worker captures clean actual executionBaseHead and immutable pair hashes, runs bound pre-implementation PASS, then edits exact source2 and return2 only. Source or lane collision blocks edits.

## Execution Plan

Implement only locked language and observed-profile presentation delta. Preserve selectors, literal request/wire values, editable content and write/attempt guards; use render-time translation for new notices. Record copy/invariant inventory and raw hashes. Run installed compiler and scoped lint under sanitized environment, at most two runs each with any second run limited to a named source correction, complete required return/evidence, then full bound return gate at most2 attempts. No tests or app/server/browser. Terminal gate result ends worker lane; Root consumes evidence without duplicate suites.

## Evidence Requirements

Raw stdout/stderr/exit code and duration for actual commands; raw-byte final source hashes, exact changed4, pair pins, language-copy inventory, missing/malformed-boundary fallback source branches, untouched auth/write/journal conditions, original failures, pending component/walkthrough evidence. Build/Save/review selectors and protocol values stay literal. No checksum/shape-only substitution for source review.

## Acceptance Criteria

REQ-LANGUAGE: owned control/status/notice/error/accessible copy uses current vi/en labels without translating user data. REQ-PROFILE: only the exact server-observed enum with jobDecisions true selects local-profile description; missing enum retains enablement/generic warning; fallback/standalone untouched. REQ-LIMITS: draft/review/Stop claims and source invariants remain bounded. REQ-RETURN: actual compiler/lint, exact4, original failures, full bound return and pending UI evidence. These criteria close this source package only, not R1 or R2 exits.

## Review Gate

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Local reads actual source diff/branches and sealed raw evidence, checks the whole bounded dependency class once, runs reviewer-fast on final staged closure, and returns one consolidated finding if required. No executable independent probe is selected for source-only UI copy; no source test/component/walkthrough claim. Read current P4 state; routine M5/M10/safety/M20 only.

## Closure Checklist

Worker exact4 and final bound full gate first; Root Local review plus existing roadmap1 then exact6 material commit; separate exact current6 generated sync; actual nonempty split closure ranges. Source package accepted only with stated limits and real gate outputs. No new source successor or stage promotion.

## Return-To-Orchestrator Conditions

Return one consolidated blocker for third-source/helper/test/schema/auth/writer need, missing authority, unexpected source drift, size cap, time budget or two failed final gate attempts. No automatic retry/refill or nested worker. Root may correct bounded documentary defects from evidence within existing authority; source expansion requires fresh scoped admission.

## Worker Autonomy / No-Question Rule

Resolve routine in-scope source/copy choices. Do not ask operator for mechanical repairs. Hold only the dependent action when contract or authority is missing; retain original failures and notify Local once.

## Work-Order Fulfillment Manifest

Required worker union exact4; requirements and proof IDs are dispatcher-owned in the acceptance ledger. Worker returns actual artifact actions/hashes and command evidence, not a redefined expected set. Root closure adds Local review/roadmap only after worker gate; no worker re-run for Root metadata.

## Verification Commands

Only after bound release: `python -B governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`. App cwd: direct installed `node node_modules/typescript/bin/tsc --noEmit --incremental false`; direct installed ESLint bin exact source2; child environment includes OS path/temp variables only, NODE_ENV=development, no inherited CVF/provider/secret variables and no env loader. Use no package manager. Then `git diff --check` and the exact full requiredGate. Compiler/lint are static checks, not UI/test execution.

Final command: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md --max-return-lines 450 --max-return-bytes 64000`.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: existing language/capability owners; no design owner or executable boundary added.

## Local Transaction Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - Git-reversible UI source text and return metadata only; no durable store/lock/ACL/rollback operation.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Root dispatcher/reviewer/closer; one separate INTERNAL_AGENT implementation worker |
| phase | DISPATCH -> IMPLEMENTATION -> WORKER_RETURN -> REVIEW -> FREEZE |
| baseHeadFor(phase) | dispatchBaseHead=8d39e708fed33ecbba5ce2e5e092738d4c4a3449; executionBaseHead=actual clean released HEAD captured at start; closureBaseHead=actual dispatch continuity commit |
| changedSetScope(phase) | Root exact2 dispatch; separate current6; worker exact4; Root exact6 material; separate current6 actual-SHA continuity |
| traceScope(phase, actor) | worker exact4 and owned ignored scratch only; Root pair/review/roadmap/continuity |
| commitOwner(phase) | worker WORKER_MUST_NOT_COMMIT; Local Root commits |
| crossBatchIsolation | old browser/source actor grants remain spent; distinct UX-only source issue |
| nextMoveSurfaces | bootstrap, compact front door, active handoff; aggregate targeted only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: INTERNAL_AGENT worker only after committed release
laneOwnedPaths: exact4 Required Artifact Manifest plus owned ignored worker root
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return, exact4 reconciliation and stage empty

## Worker Output Checker Read-Ahead Mandate

Before first write, inspect worker-return/full gate, operation trace, acceptance ledger, independent probe, coordination and structural predicates for each output path. Apply Worker Preparation Reminder and exact literal gotchas. Do not rely on provider-memory authority or run broad historical suites.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-R1-UX-PROFILE-SOURCE-20261018","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md","docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md","docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-18.md","docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION_MEMORY.md","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/state/entries/nextAllowedMove.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx","docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md","docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json"],"claims":["source-only vi/en and observed-profile presentation"],"requiredProof":["source diff and copy inventory","static compiler and scoped lint","full bound return","independent Local source review"],"operatorCheckpoints":["app/browser","provider/live","real-data writer/custody","production/public/deploy"],"forbiddenEffects":["test mutation/run","server/schema/auth/writer change","network/provider/app/browser","worker stage/commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","completenessClaimChanged":false}}
```

## Baseline Binding

Baseline `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` SHA256 `28a2385af4b5585e524a7167c381da5ab3127af13c63b2563097f3b0d1eb089c`. Frozen at committed release; return pins both pair raw hashes. Baseline and work order remain immutable after release; result belongs in Local review/current continuity.

## Operator Checkpoint

Standing operator next/autonomous orchestration covers this finite source action. No repeated permission is required for exact source2/return2. App/browser, provider/live, real-data writer/custody, production/public/deploy remain action-specific checkpoints; no such effect is released here.

## Foundation Storage Layout Block

Reuse existing dated baseline, work-order, review and evidence folders. Worker ignored logs stay in its owned task root. No governance owner/file relocation, new registry, durable runtime store or generic helper is selected.

## Learning Application Plan

```learning-application-plan-json
{
  "schemaVersion": "cvf.learningApplicationPlan@1.0.0",
  "bindings": [
    {
      "findingId": "NCR-LEARNING-APPLICATION-OBSERVABILITY",
      "control": {
        "path": "governance/compat/learning_application_binding.py",
        "sha256": "84068b6f197c19404a23daa643266d7f9ed334f313cd2d8bbe2f2e6d37d7b7b8"
      },
      "action": "One finite source2 UI outcome; exact4 worker and exact6 closure; consume sealed evidence; Root consolidates documentary repairs; preserve original failure and costs.",
      "verificationPlan": "Record actual worker and Local preparation/review duration, original candidate failures and source/static acceptance; no effectiveness or APPLIED claim before measured outcome."
    }
  ]
}
```

Plan only; no effectiveness or APPLIED claim.

