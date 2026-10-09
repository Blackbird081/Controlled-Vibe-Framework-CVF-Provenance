# CVF Agent Work Order - NCR Offline Preview Delivery
Memory class: governed-worker-dispatch
docType: work_order
Status: READY
Date: 2026-10-09
Batch ID: CVF-NCR-OFFLINE-PREVIEW-20261009
Dispatch base head: e93ad0075c2868ebc476c43a0324256fb6c6d4a0
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false
Preapproval-Feasibility: REQUIRED
Preapproval-Feasibility-Companion: docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.json

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT shared-workspace implementation worker; Local remains independent orchestrator/reviewer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; baseline docs/baselines/CVF_GC018_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; frozen inputs docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture actual committed clean released HEAD before any worker edits.
Current-time notes: operator manually transfers this packet to Claude in this workspace; no automated invocation by dispatcher.
Do-not-misread notes: implement only durable offline HTML preview and its tests; source R2 attempt is spent and source/native/TTS/MP4/provider/public lanes stay parked.
Required first actions: read startup, complete pair and pinned inputs; verify source hashes, actual bound pre-dispatch receipt and clean released HEAD; pass pre-implementation before writing.
Return contract: docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md and docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json; COMPLETE_PENDING_REVIEW only with complete acceptance evidence and bound full return gate, otherwise one BLOCKED_WITH_REASON.

Exact workspace: D:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF.
Worker is INTERNAL_AGENT regardless of provider/model. Local owns final technical disposition.

## Purpose

Make the selected ten-scene browser preview reproducible and durable. Deliver a deterministic source-to-HTML builder, the usable offline preview, discriminating static/browser tests, a short usage guide and a pending-review return. Reuse the already tested prototype; do not rebuild the CVF narrative or repeat the full source audit.

## Scope / Target / Owner Boundary

Operator has selected continued local test work and manual transfer to Claude. Worker implements the seven exact artifacts; Local orchestrator prepares/releases the packet, then independently reviews returned evidence and owns closure/commit. This UI package is independent of stopped C1/source-supervisor chains. Its finite consumer is the operator opening an offline storyboard before future media-production admission.

## Allowed Paths

- `scripts/cvf_storyboard_preview.py`
- `scripts/test_cvf_storyboard_preview.py`
- `scripts/test_cvf_storyboard_preview_browser.cjs`
- `docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html`
- `docs/guides/CVF_STORYBOARD_PREVIEW_README_2026-10-09.md`
- `docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json`
- `docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md`

## Forbidden Paths

Every other tracked path is read-only, including this pair, frozen inputs, accepted design, core product source, roadmap, governance/checkers/hooks, dependency/lock files, session state/handoff, credentials and source mirrors. No sibling R2 root reads/imports/executes/mutations. No audio, MP4, TTS, FFmpeg, installation, remote fonts/assets, provider, server/listener, public push or deploy.

Worker-authored ignored fixtures, screenshots and logs are confined to `.cvf/runtime/cvf-offline-preview-worker-20261009/` (20 MiB total, 2 MiB per textual receipt). Trusted canonical gates may emit their own receipts/caches under `.cvf/runtime/autorun-receipts/`, `.cvf/runtime/reviewer-fast/`, `.pytest_cache/`, Python `__pycache__/`, and gate-declared temporary fixtures; declare observed paths and do not hand-edit gate receipts. Existing Playwright/Chromium may create tool-owned ephemeral browser profiles in OS TEMP; close only owned browser instances. No package/browser download, installed-tool mutation or shared-cache cleanup. Tests create small synthetic fixtures only within their owned runtime root; no recursive cleanup outside a verified resolved owned path.

## Implementation Contract

1. Fully read frozen sources and prototype as data; verify raw source digests before writes. The selected original design is the narrative authority. Prior content/browser proof is scoped evidence, not a final media acceptance. Current sources are already chosen; no outside repository research or absorption.
2. Implement a Python standard-library builder at `scripts/cvf_storyboard_preview.py` with explicit source/input-manifest/output arguments. Default invocation builds `docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html` from the pinned source using the dispatch input manifest. Produce UTF-8 HTML deterministically, with no timestamps or ambient environment-dependent bytes. Validate source digest, exactly S01-S10, five scene fields, unique IDs, contiguous 0-240 second schedule and declared claim IDs; fail closed before replacing output on invalid input.
3. Keep the original narration and original on-screen text exact after HTML decoding. Preview summaries may reuse the frozen prototype cards but must be labeled presentation summaries; original on-screen content remains accessible per scene. Every S05-S08 scene carries the complete illustration badge even when shown alone. No fabricated expense-code execution/test result; no claims beyond documentary source limits. Encode data safely: source strings containing HTML, closing script tags or event markup cannot create executable DOM.
4. Self-contained offline HTML, local system fonts, no remote resource/URL, provider call or storage writer. Desktop stage is 16:9; mobile adapts to readable vertical layout. Provide ten scene buttons, previous/next, play/pause, seek, reset, keyboard access, 240-second browser timeline, end-stop and replay, and pause when the page is hidden. No browser speech synthesis or recording. Derived source SHA and package/test status must be truthful, not stale review labels.
5. Build discriminating standard-library tests at `scripts/test_cvf_storyboard_preview.py` for valid source/repeatable output, missing/duplicate/reordered scene, field omission, timeline gap/overlap, bad claim join, source drift, and unsafe text injection. Malformed input must not overwrite an existing output. Use synthetic fixtures only; never modify frozen inputs or canonical source to create negatives.
6. Implement Playwright tests at `scripts/test_cvf_storyboard_preview_browser.cjs` using the existing package named in frozen inputs, with owned-browser cleanup in finally and a finite per-test timeout. Test all ten scenes in desktop1440x1050/mobile390x844: exact narration and source-screen content, per-scene badges, active selection, controls, keyboard, seek boundaries, stable pause, hidden-page pause, end/replay, accessibility names, zero HTTP requests/errors and no horizontal/clipped text. Browser virtual clock is allowed only to verify pure UI timer behavior and must not be reported as measured real narration/video duration.
7. Short guide `docs/guides/CVF_STORYBOARD_PREVIEW_README_2026-10-09.md` states build/open/test commands, source/hash provenance, layout adaptation, estimated timing, private/UI-only status and excluded media lanes. Keep existing prototype evidence and sources read-only; no new roadmap, runtime daemon or acceptance system.
8. Evidence `docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json` and return `docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md` contain actual commands/exits/assertions, elapsed time, source/output/test hashes, executionBaseHead, exact Git changed union, limits and cleanup. Copy the dispatcher ledger IDs into acceptance-evidence-json; do not redefine requirements. Include one consolidated negative-class sweep. Complete only after the bound full return gate; do not stage/commit or update reviewer/state surfaces.

## Acceptance Criteria

Seven exact artifacts are Git-observed; deterministic build is source-pinned; all ten narration/on-screen fields preserved; four standalone illustration badges visible; navigation/timer/seek/keyboard and both viewports tested; parser/injection/invalid-input negatives fail safely; actual evidence and bound full gate support COMPLETE_PENDING_REVIEW. The prototype is a reuse input, not a ready-made implementation acceptance oracle. Audio/video/provider/live-governance and old source custody acceptance are excluded.

## Work-Order Fulfillment Manifest

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "BUILD",
      "mandatory": true,
      "expectedArtifacts": [
        "scripts/cvf_storyboard_preview.py"
      ],
      "requiredProofIds": [
        "DETERMINISTIC_SOURCE_PROJECTION"
      ]
    },
    {
      "requirementId": "STATIC",
      "mandatory": true,
      "expectedArtifacts": [
        "scripts/test_cvf_storyboard_preview.py"
      ],
      "requiredProofIds": [
        "PARSER_AND_INJECTION_NEGATIVES"
      ]
    },
    {
      "requirementId": "BROWSER",
      "mandatory": true,
      "expectedArtifacts": [
        "scripts/test_cvf_storyboard_preview_browser.cjs",
        "docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html"
      ],
      "requiredProofIds": [
        "CONTROLS_AND_RESPONSIVE_UI"
      ]
    },
    {
      "requirementId": "GUIDE",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/guides/CVF_STORYBOARD_PREVIEW_README_2026-10-09.md"
      ],
      "requiredProofIds": [
        "USAGE_AND_LIMITS"
      ]
    },
    {
      "requirementId": "RETURN",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json",
        "docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md"
      ],
      "requiredProofIds": [
        "BOUND_FULL_RETURN_GATE"
      ]
    }
  ],
  "proofCatalog": [
    {
      "proofId": "DETERMINISTIC_SOURCE_PROJECTION",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json#builderValidation"
    },
    {
      "proofId": "PARSER_AND_INJECTION_NEGATIVES",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json#staticTestResults"
    },
    {
      "proofId": "CONTROLS_AND_RESPONSIVE_UI",
      "kind": "LOCAL_UI_ONLY",
      "locator": "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json#browserTestResults"
    },
    {
      "proofId": "USAGE_AND_LIMITS",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json#guideVerification"
    },
    {
      "proofId": "BOUND_FULL_RETURN_GATE",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json#workerReturnGate"
    }
  ]
}
```

The ledger is the canonical exact Required Artifact and Required Proof manifest. Required Proof Manifest Atomic Literal Discipline: one proofId per atomic requirement; no alternate self-selected oracle.

## Execution Plan

1. Read complete packet, verify bound committed release/inputs and gate-owned receipt authority.
2. Reuse prototype presentation; implement deterministic source projection plus focused negative tests.
3. Generate durable preview; run static and browser UI tests; inspect screenshots.
4. Write guide and proof/acceptance return; run the exact bound full return gate; stop for Local review.

## Verification Commands

```text
python -B governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md --receipt-dir .cvf/runtime/cvf-offline-preview-worker-20261009/gates
python -B -m unittest discover -s scripts -p test_cvf_storyboard_preview.py
python -B scripts/cvf_storyboard_preview.py
node scripts/test_cvf_storyboard_preview_browser.cjs
python -B governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md
git diff --check
git status --short
```
The builder default is specified above; documented explicit arguments remain available. Record command logs and output hashes before claiming success. These are content/UI tests, not CVF live governance proof; no provider release-bundle run is requested.

## Worker Autonomy / No-Question Rule

Resolve routine implementation/layout/testing choices and grouped same-scope defects independently. One worker invocation with a 90-minute total ceiling including startup, reads, preparation, writes and gates; no subagent/external/provider invocation by tools. Return one consolidated blocker set at the ceiling or an actual authority/source/tool contradiction. Routine allowed-scope repairs do not require operator confirmation; no hidden overtime or successor. Target Local evidence review15 minutes; token/session cost UNKNOWN without a meter, not a zero-cost assertion.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-OFFLINE-PREVIEW-20261009
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

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON
Reason: shared-workspace internal worker; external architecture invocation is absent.
High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - no locking, durable transaction, ownership/DACL or rollback implementation.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> implementation worker -> independent Local reviewer/closer -> session-sync steward |
| phase | dispatch then bounded offline UI implementation |
| baseHeadFor(phase) | dispatchBaseHead=e93ad0075c2868ebc476c43a0324256fb6c6d4a0; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact seven worker paths; dispatcher pair and inputs separately owned |
| traceScope(phase, actor) | each actor records own commands and evidence |
| commitOwner(phase) | Local closer; WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no unrelated dirty files or stopped-chain redispatch |
| nextMoveSurfaces | current front door, active handoff and generated state steward-only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: operator-transferred shared-workspace implementation worker after committed release; Local reviewer after worker lane release
laneOwnedPaths: exact seven-path acceptance ledger
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: exact worker diff/evidence and full return gate before Local review

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
returnTimeRecheck: REQUIRED_BEFORE_REPAIR
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | packet baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | packet baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker and source continuity | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | seven allowed paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | seven allowed paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity,pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker proof/return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | WORKER_RETURN | worker | WORKER_RETURN | worker proof/return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | REVIEW | reviewer | REVIEW | seven allowed paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | PRE_MATERIAL_COMMIT | reviewed seven paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | POST_MATERIAL | reviewer | REVIEW | Local completion review | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | source continuity and generated views | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL_CLOSURE | reviewed material/continuity ranges | EXACT_PATHS | Local-closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Graph describes required owners and sequence; passed authoring checks are not worker execution proof.

## Reviewer Closure Conversion

completionReviewPath: docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_COMPLETION_2026-10-09.md
reviewerOwnedClosurePaths: completion review, packet status and separately authorized continuity.
closureOwner: Local orchestrator/reviewer/closer; workerCommitPermission: FORBIDDEN.
Use EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION; routine M5/M10/safety/M20. One small independent source-drift or escaping probe only if required below. Preserve original worker evidence and any process deviation. Material commit, real-SHA continuity, then clean split-range closure; no media/public acceptance inferred.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
workerReturnPath: `docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md`
Required sections: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Return-Time Closeability Recheck; Epistemic Process Block; acceptance-evidence-json.
Create the checker-safe return skeleton with the existing run_worker_return_scaffold.py before filling it; conform to the committed ledger and preserve meaningful commands/evidence. Read the canonical return quality/closeability checker before writing. Record invocation counts and cost availability. Complete requires CLOSEABLE and outsideAuthorityBlockers: NONE; otherwise BLOCKED_WITH_REASON with no automatic redispatch. A gate passed without the active order is supplementary, never the required result.

## Commit Mode And Base-Anchor Lifecycle

WORKER_MUST_NOT_COMMIT. Planning base is not the actual execution anchor. Committed packet and synchronized authority must precede worker edits. Reviewer alone commits accepted material; steward then records real SHA and generates continuity; split committed closure follows clean continuity. No fabricated future hashes.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dual Agent Surface Matrix

| Surface | Role | Disposition |
|---|---|---|
| INTERNAL_AGENT | manually transferred worker and independent Local reviewer | selected; shared workspace |
| EXTERNAL_AGENT_CLI_MCP | detached research/execution | not selected; ceiling0 |
| Browser UI | installed local Chromium | permitted pure UI tests only |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named UI/design sources only; no complete repository scan claim.

## Knowledge System Applicability

- Knowledge-map verdict: NOT_APPLICABLE_WITH_REASON - no corpus-derived knowledge map; source trace covers only named UI/design inputs.

## Evidence Reuse And Encoding Plan

Rehash named inputs once at execution start; consume prior semantic/content/browser proof without duplicate whole-repository review. The maintained implementation requires its own focused delta tests. ASCII governance prose and Python/CJS test code; Vietnamese source/UI text may retain diacritics as explicit quoted-source/UI encoding exception. Do not use provider memory as CVF authority.

## Claim Boundary

Only a private source-pinned offline UI prototype is admitted. It does not create a custom media-render pipeline, admit HyperFrames/VieNeu/FFmpeg, execute the illustrative expense app, resolve source R2/custody/STOP obligations, or prove provider/live CVF governance. Browser-timer simulation is not measured four-minute narration/audio/video. Initial identity below tracks durable UI packaging alone; old stopped problem identities/counters remain untouched.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Ten-scene narrative | source fact | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | Outline; Scene Handoff; Claim Boundary | S01-S10 | accepted documentary design | ACCEPT |
| Prior content defects and selection | observation | docs/reviews/evidence/cvf-offline-preview-content-test-2026-10-09.json | findingsBeforeRepair; terminalReview | PASS_LOCAL_STORYBOARD_TEST | bounded content receipt | ACCEPT |
| Prototype controls and browser evidence | observation | docs/reviews/evidence/cvf-offline-preview-ui-test-2026-10-09.json | browser; visualInspection | PASS_OFFLINE_UI_PREVIEW | pure UI evidence | ACCEPT |
| UI reuse input | source fact | docs/reviews/evidence/cvf-offline-preview-prototype-2026-10-09.html | stage; controls; render | offline preview HTML | bounded prototype, not production | ACCEPT |
| Freeze constraints | authority boundary | docs/reviews/CVF_NCR_C1_S1_CONSOLIDATED_REPAIR_COMPLETION_2026-10-09.md | Decision; Claim Boundary | retained R2 result | Local source disposition | ACCEPT |
| Required learning application | contract | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Forward Application Control | real dispatch and returned-result review | existing F2G control | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_task_governance_route.py |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; Source Verification Block; COMPLETE_PENDING_REVIEW; CLOSEABLE; gateId; mutationSurface; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source-verified packet structure, not first discovery |
| claimBoundary | no worker implementation or media execution proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`video-offline-preview`, role=`dispatcher`, lifecyclePhase=`dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class video-offline-preview --role dispatcher --lifecycle-phase dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Before authoring, rg -n 'NCR_OFFLINE_PREVIEW_DELIVERY|CVF-NCR-OFFLINE-PREVIEW-20261009' docs CVF_SESSION returned exit1, no matches. Exact packet and worker paths checked absent. Existing design and tested prototype are reused; new durable packaging has distinct output/cost/consumer boundaries and is not a source-R2 successor or repository-wide inventory.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-NCR-OFFLINE-PREVIEW-20261009",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [
    "docs/baselines/CVF_GC018_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.json",
    "docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json",
    "docs/reviews/evidence/cvf-offline-preview-prototype-2026-10-09.html",
    "docs/reviews/evidence/cvf-offline-preview-content-test-2026-10-09.json",
    "docs/reviews/evidence/cvf-offline-preview-ui-test-2026-10-09.json",
    "scripts/cvf_storyboard_preview.py",
    "scripts/test_cvf_storyboard_preview.py",
    "scripts/test_cvf_storyboard_preview_browser.cjs",
    "docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html",
    "docs/guides/CVF_STORYBOARD_PREVIEW_README_2026-10-09.md",
    "docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json",
    "docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md"
  ],
  "claims": [
    "PRIVATE_OFFLINE_UI_ONLY",
    "SOURCE_R2_STOP_RETAINED"
  ],
  "requiredProof": [
    "DETERMINISTIC_SOURCE_PROJECTION",
    "PARSER_AND_INJECTION_NEGATIVES",
    "CONTROLS_AND_RESPONSIVE_UI",
    "BOUND_FULL_RETURN_GATE"
  ],
  "operatorCheckpoints": [
    "RUNTIME_ENVELOPE_AND_RIGHTS_ADMISSION_BEFORE_INSTALL_OR_MEDIA"
  ],
  "forbiddenEffects": [
    "NETWORK_ACCESS",
    "INSTALL",
    "MODEL_DOWNLOAD",
    "PROVIDER_CALL",
    "MEDIA_EXECUTION",
    "PUBLIC_WRITE",
    "DEPLOYMENT",
    "REAL_DATA_MUTATION"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

SHADOW_FULL_GATE_FALLBACK; full legacy bundles remain mandatory.

## Authority Chain

| Source | Disposition |
|---|---|
| Operator2026-10-09: continue; manual transfer to Claude; Local orchestrator/reviewer | ACCEPT |
| Paired GC-018 baseline docs/baselines/CVF_GC018_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md | ACCEPT |
| Accepted design and frozen local prototype evidence docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json | ACCEPT |
| Source R2 terminal restrictions | ACCEPT; retained boundary |

## Agent Roles

Dispatcher prepares and releases; shared-workspace worker implements; separate Local reviewer evaluates evidence; Local closer commits; session-sync steward updates continuity. Operator manually transfers the order; no automated worker/provider invocation.

## Required First Reads

AGENTS.md, bootstrap/front door/active handoff; complete paired baseline/order/frozen inputs; original design, prototype HTML and both local test receipts; DESIGN.md; guard orientation/literal gotchas; lifecycle Technical Feasibility and Execution-Surface And Total-Cost Feasibility; learning Forward Application Control; acceptance-ledger, closeability, worker-return and encoding owners. Consume only named inputs; no provider memory authority or external research.

## Pre-Flight Checks

Clean released HEAD; packet/source hashes; committed current-authority bindings; release and pre-implementation gates; no unrelated changes. Record actual executionBaseHead and command results. Reject drift before writes rather than adapting frozen sources silently.

## Write Ownership

Worker owns exactly seven allowed artifacts and bounded ignored test output. Dispatcher owns this pair, feasibility companion and frozen inputs. Local reviewer owns final completion/status; steward owns source continuity and generated views. No dispatcher mutations while worker lane is active; release evidence is complete worker diff/return plus bound gate.

## Evidence Requirements

docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json records all five canonical proof IDs, observed commands/exits, source/hash joins, source integrity, negative mutations, deterministic repeated-byte comparison, browser controls/viewport/zero-HTTP tests, screenshots and cleanup. Return includes executionBaseHead, Git exact union, acceptance-evidence-json and bound gate. Frozen screenshot paths in prior receipts are historical runtime locators; do not reclassify them as current output proof.

## Review Gate

Evaluate evidence and integrated UI/source limitations; no duplicate full narrative/source audit. An independent tiny malformed/escaping fixture is admitted only to separate a safe projection from executable source injection; do not alter worker outputs solely to make the review look independent. Prototype proof alone cannot accept the new builder.

## Closure Checklist

Exact scope, required artifacts and proof contents; full return gate; Local semantic review; no old STOP reset; material commit followed by real-SHA continuity; clean split-range closure. Runtime and public approval remain separate.

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW when all offline UI requirements and gates are satisfied. Return BLOCKED_WITH_REASON for packet/source contradictions, forbidden-scope needs, unavailable required gates or time ceiling. Provide one consolidated missing-evidence ledger and no automatic retry/successor. Unresolved future media rights/budgets alone do not block an honestly complete offline preview package.

## Operator Checkpoint

No preference checkpoint for this admitted private UI package. Operator manually hands off to worker; Local releases/reviews. Source/native supervisor, download/install, TTS/real voice/MP4, provider/live, public or deploy effects stay parked. Return after finite UI delivery; do not extend into media production.

## Foundation Storage Layout Block

Use existing scripts, guides, reviews/evidence roots. No new storage/index/standard/daemon or foundational directory. Seven exact small files are bounded to 250 Python/CJS lines each, HTML300, guide120, evidence350, return450; split is not foreseeable within this budget. If a split is needed, report BLOCKED_WITH_REASON for dispatcher amendment before creating an eighth artifact.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
reviewerDecisionOwner: LOCAL
independentProbeRiskClass: BOUNDED_LOCAL_VALIDATOR
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
implementationOracleSeparation: Local authors one tiny malformed/escaping fixture from contract, not worker test expectations.
positiveControl: valid pinned source projects exact narration with deterministic bytes
negativeMutationClasses: altered source digest or embedded closing script markup
expectedInformationGain: rule out silent drift/executable injection at source-to-HTML boundary
rerunCostReason: one narrow fixture/command, not a duplicate browser suite or broad source audit

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | offline-preview-dispatch-20261009 |
| Working directory | private CVF repository root |
| Command or tool surface | named source reads; scaffold; ADIF; structural/feasibility gates |
| Target paths | docs/baselines/CVF_GC018_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-prototype-2026-10-09.html; docs/reviews/evidence/cvf-offline-preview-content-test-2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-ui-test-2026-10-09.json |
| Allowed scope source | operator2026-10-09 manual worker transfer instruction |
| Before status evidence | clean HEAD e93ad0075c2868ebc476c43a0324256fb6c6d4a0; main ahead2; existing ignored prototype only |
| After status evidence | seven new dispatcher paths; worker not invoked |
| Diff evidence | git status --short; git diff --check; exact staged manifest |
| Approval boundary | local offline UI package; no media/provider/public effect |
| Claim boundary | packet authoring only; implementation pending |
| Agent type | INTERNAL_AGENT orchestrator/reviewer |
| Invocation ID | offline-preview-dispatch-20261009 |
| Expected manifest | docs/baselines/CVF_GC018_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-prototype-2026-10-09.html; docs/reviews/evidence/cvf-offline-preview-content-test-2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-ui-test-2026-10-09.json |
| Actual changed set | docs/baselines/CVF_GC018_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.md; docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_OFFLINE_PREVIEW_DELIVERY_2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-dispatch-inputs-2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-prototype-2026-10-09.html; docs/reviews/evidence/cvf-offline-preview-content-test-2026-10-09.json; docs/reviews/evidence/cvf-offline-preview-ui-test-2026-10-09.json |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | offline UI dispatch |
| claimDisposition | CLAIM_REJECTED: no source/runtime production acceptance |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: new worker not run |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no media/provider action |
| invocationBoundary | Local packet only; operator transfers worker |
| interceptionBoundary | no OS/native containment implemented |
| claimLanguage | private prototype only |
| forbiddenExpansion | source retry, media, install/provider/public |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-offline-storyboard-durable-ui-package","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

Independent UI packaging identity only; not a renamed C1 source/metadata chain and not clearance of their obligations.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-OFFLINE-PREVIEW-20261009 --title "NCR Offline Preview Delivery" --date 2026-10-09 --base e93ad0075c2868ebc476c43a0324256fb6c6d4a0 --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact UI scope/ledger; source pins; prototype reuse; learning and gate-owned receipt boundaries; reusable canonical contracts from previous no-commit packet |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | NONE; existing contracts reused |
| claimBoundary | authoring provenance only |

## Current Runtime Freshness Verification

Existing Chromium 145.0.7632.6 and Playwright package were used for the prior bounded UI tests; frozen receipt pins identify that evidence. Worker checks availability without install before writes. No current-upstream/package/license or media readiness claim. All seven worker outputs are absent before dispatch authoring.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md |
| Chain map route | accepted design and local prototype -> maintained UI package |
| Matching local-view guard | N/A with reason: no external intake |
| Owner surface | accepted storyboard |
| Disposition | ADAPT bounded local presentation |
| Claim boundary | no repository absorption/source-relay reopening |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON - no new absorption capability/corpus or legacy coverage claim.

## Export Surface Decision

Private provenance worktree only; local kit handoff, no public/export runtime.

## Tool / Classifier Block Recovery Contract

toolClassifierBlockRecoveryApplicability: NOT_APPLICABLE_WITH_REASON - local offline UI only; no blocked provider/media effect authorized.

## Required Artifact Manifest

| Path | Required at handoff |
|---|---|
| scripts/cvf_storyboard_preview.py | YES |
| scripts/test_cvf_storyboard_preview.py | YES |
| scripts/test_cvf_storyboard_preview_browser.cjs | YES |
| docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html | YES |
| docs/guides/CVF_STORYBOARD_PREVIEW_README_2026-10-09.md | YES |
| docs/reviews/evidence/cvf-storyboard-preview-worker-2026-10-09.json | YES |
| docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md | YES |

Worker return path: docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_WORKER_RETURN_2026-10-09.md

## Intake Role Routing Decision

Intake summary: maintain the tested offline storyboard as a reproducible private UI package.
Scope classification: seven exact local implementation/evidence paths; no media or source-supervisor execution.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Escalation condition: source drift, required gate/tool unavailable, extra path or new effects; return consolidated BLOCKED_WITH_REASON.

MULTI_AGENT_MULTI_ROLE: Local orchestrator/dispatcher -> manually transferred shared-workspace worker -> independent Local reviewer/closer. Selected implementation is a seven-file private offline UI package. No automated provider/CLI/MCP worker invocation; no media/source-runtime release inferred from actor/model or this packet.

## Dated Owner Dependency Discovery

Frozen sources in dispatch input JSON bind exact paths/raw hashes and observation date. There is no external-source acquisition, dated-owner search or full corpus assertion; source R2 terminal disposition is a limit only, not a dependency that this UI package can resolve.


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
      "action": "Before release verify phase-correct input/transport and trusted gate output authority; bind exact current packet to feasibility and full return route; preserve old source STOP. Review returned work separately from process deviations.",
      "verificationPlan": "Run canonical validate_changed on this actual work order and an in-memory negative with its binding removed; capture bound explicit feasibility with canonical object count1. On actual worker return verify the admitted commands, gate receipts, elapsed budget and disclosure; only then assess project application with typed evidence."
    }
  ]
}
```

Plan is a dispatch obligation, not APPLIED project evidence. First real worker dispatch plus returned-result review is the required observation boundary.
