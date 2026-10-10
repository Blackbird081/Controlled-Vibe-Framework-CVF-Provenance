# CVF Agent Work Order - NCR Expense Browser Preview
Memory class: governed-worker-dispatch
docType: work_order
Status: CLOSED_PASS_BOUNDED
Date: 2026-10-10
Batch ID: CVF-NCR-EXPENSE-BROWSER-20261010
Dispatch base head: 665da5b2df3e1d2b81553a5c9567c7babb364459
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false
Preapproval-Feasibility: REQUIRED
Preapproval-Feasibility-Companion: docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.json

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT shared-workspace implementation worker; Local orchestrator/reviewer owns final disposition.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md; baseline docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md; frozen inputs docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json.
Commit mode: WORKER_MUST_NOT_COMMIT; capture actual clean released executionBaseHead.
Required first actions: BEFORE ANY file read, capture UTC and monotonic start in allowed ignored runtime; then startup, pair/input hashes, dispatch receipt and pre-implementation gate.
Current-time notes: operator manually transfers the order; no automated agent invocation.
Do-not-misread notes: independent browser UI proof; source R2/native/media/provider/public/deploy/P11 remain parked.
Return contract: docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md; docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json; COMPLETE_PENDING_REVIEW with two separately evidenced full bound return checks.
Exact workspace: D:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF; worker INTERNAL_AGENT regardless of provider/model.

## Purpose

Deliver a reusable offline browser preview of the accepted ExpenseList component and real Chromium interaction proof. Named gap: accepted unit fixture has no real-browser behavior/layout evidence or runnable preview. Reuse the unchanged component; do not recreate its filter, mount production routes or revise the storyboard. The useful outcome is an inspectable synthetic UI preview plus discriminating browser tests, not a model benchmark alone.

## Scope / Target / Owner Boundary

Standing operator autonomous isolated-test/continuation authority and manual worker transfer cover this finite private browser preview. Exactly two implementation scripts plus three metadata outputs. Accepted component/tests remain read-only; Local owns technical acceptance. Launch only installed headless Chromium against generated self-contained HTML, no server or external requests. No application-route, storyboard or AI-governance claim change.

## Allowed Paths

- `scripts/cvf_expense_fixture_preview.cjs`
- `scripts/test_cvf_expense_fixture_preview_browser.cjs`
- `docs/guides/CVF_EXPENSE_BROWSER_PREVIEW_README_2026-10-10.md`
- `docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json`
- `docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md`

Worker-owned entry/bundle/HTML/report/screenshots/logs/mutant copies and timer under `.cvf/runtime/cvf-expense-browser-worker-20261010/`; total30MiB, HTML2MiB, single text2MiB, screenshot3MiB. Mandatory gate-owned `.cvf/runtime/autorun-receipts/`, `.cvf/runtime/reviewer-fast/`, declared gate temporary files and test-owned caches remain authorized. No shared-cache cleanup/install. Timer creation before reads is the sole pre-implementation-gate write exception; it records only UTC/monotonic timestamps and no source or secret data.

## Forbidden Paths

Every tracked path outside the five-output manifest, including accepted ExpenseList/component tests, package/lockfiles, app routes, test config/setup, storyboard/design, governance/checkers and session surfaces. No provider/env/credential inspection or output, dependency installation, HTTP server/listener, external network, narration/recording/audio/video, native-source helper, source-R2 retry or public/deploy. Vite must use configFile:false and envFile:false; never serialize process.env or ambient config.

## Implementation Contract

1. Builder scripts/cvf_expense_fixture_preview.cjs is a Node CommonJS CLI plus importable bounded helper. CLI: `node scripts/cvf_expense_fixture_preview.cjs --output .cvf/runtime/cvf-expense-browser-worker-20261010/expense-preview.html`. Resolve installed Vite/React/react-dom from the existing web node_modules, use browser IIFE bundling with configFile:false, envFile:false, write:false and production NODE_ENV literal. No install, app config/env load or server. Use a runtime-owned entry and existing JSX transform, no handwritten replacement of ExpenseList.
2. Bundle actual read-only EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx; its raw SHA is pinned in dispatch inputs. Browser root renders this named component with exactly five manually synthetic rows: two Feb2026, two Mar2026, one 05/03/2026 invalid row. Existing test fixture may inform data shape but must not be imported into browser oracle. Preserve displayed IDs/order; primary browser row expectations authored in test script.
3. Produce one standalone HTML with all runtime JS/CSS inline, no CDN/font/image/source-map imports or links. Escape closing script sequences in inline bundles. Use DESIGN.md token values for a small wrapper, system fonts, no invented success/governance badge. Existing component notice remains. Add concise Vietnamese text that this is private synthetic browser UI, not AI governance/application integration. Keep accepted storyboard and its historical badge/narration untouched.
4. Optional build helper arguments fixtureVariant=primary|calendar and sourceTextOverride are for test-only runtime negatives, not app features. Calendar variant transforms the same five rows to include a wrong-year March row and an impossible March32 row. Override must operate in memory or ignored copies, never change accepted tracked source. Ordinary CLI refuses source-pin drift before replacing existing output; failure preserves a preexisting output sentinel.
5. Browser test scripts/test_cvf_expense_fixture_preview_browser.cjs launches only installed Playwright Chromium, loads generated HTML with page.setContent or local file URL, and closes context/browser in finally. Block/report every external request; distinguish main file load from subresources. No HTTP listener. Treat page errors/console errors, skipped cases, missing readiness and timeout as failures, never PASS. Desktop1280x800 and mobile390x844 are the only profiles; use explicit waits for rendered rows, no timing sleeps as readiness proof.
6. Browser assertions: March2026 two exact rows; April empty message/table absent; clear filter four valid rows; malformed row absent/no errors; native input has Vietnamese accessible label and existing note. Calendar variant excludes wrong-year same-month and impossible date; preserve order/identity. Inspect input/note/table within viewport, no horizontal clipping at both profiles. Screenshots desktop/mobile primary March view for Local visual review, not media/storyboard assets.
7. Two browser mutants from pinned source: remove exact month predicate; bypass actual calendar-day validity. Browser assertions must fail for the corresponding behavior, not bundling/harness setup. Each starts from unchanged baseline; record tests collected/completed and assertion failure, exclude harness-invalid runs. Keep all accepted source hashes unchanged and restore ordinary passing preview after mutations.
8. Caps builder250/test350/guide100/evidence350/return450 physical lines. Generated primary HTML2MiB max. No extra tracked fixture/split, storage, real data, provider or runtime integration. Before coding inspect existing package/build API and checker shape; routine internal choices remain worker-owned.

## Acceptance Criteria

Five artifacts, unchanged accepted source pins, self-contained actual-component preview, concrete desktop/mobile browser interactions and calendar negatives, two genuine assertion-level browser mutant kills, no external requests or leaks, source-drift refusal preserving output sentinel, and full bound frozen-return confirmation. New browser proof is supplementary to accepted unit evidence; do not rerun the unit suite or claim application/AI-governance execution.

## Work-Order Fulfillment Manifest

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "BUILD",
      "mandatory": true,
      "expectedArtifacts": [
        "scripts/cvf_expense_fixture_preview.cjs"
      ],
      "requiredProofIds": [
        "SOURCE_BOUND_PREVIEW"
      ]
    },
    {
      "requirementId": "BROWSER",
      "mandatory": true,
      "expectedArtifacts": [
        "scripts/test_cvf_expense_fixture_preview_browser.cjs"
      ],
      "requiredProofIds": [
        "BROWSER_CASES_AND_MUTANTS"
      ]
    },
    {
      "requirementId": "GUIDE",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/guides/CVF_EXPENSE_BROWSER_PREVIEW_README_2026-10-10.md"
      ],
      "requiredProofIds": [
        "USAGE_LIMITS"
      ]
    },
    {
      "requirementId": "RETURN",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json",
        "docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md"
      ],
      "requiredProofIds": [
        "BOUND_FULL_RETURN_GATE"
      ]
    }
  ],
  "proofCatalog": [
    {
      "proofId": "SOURCE_BOUND_PREVIEW",
      "kind": "LOCAL_UI_ONLY",
      "locator": "docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json#previewBuild"
    },
    {
      "proofId": "BROWSER_CASES_AND_MUTANTS",
      "kind": "LOCAL_UI_ONLY",
      "locator": "docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json#browserTestResults"
    },
    {
      "proofId": "USAGE_LIMITS",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json#guideVerification"
    },
    {
      "proofId": "BOUND_FULL_RETURN_GATE",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json#workerReturnGate"
    }
  ]
}
```

Canonical Required Artifact and Proof manifest; one atomic proofId per requirement.

## Execution Plan

1. Capture UTC/monotonic FIRST, before first read, in allowed timer file; total one90-minute worker ceiling includes startup, reads, coding, browser and all gates.
2. Startup; verify pair/pins/tooling/clean release; bound pre-implementation gate before any other write.
3. Build actual-component preview; browser cases, calendar variant and two mutants; pin/screenshot/log all results; no duplicate unit suite.
4. Guide/evidence/return; full bound gate. Freeze all five final bytes and record hashes in ignored manifest; rerun full bound gate with separate confirmation log; verify five hashes still match. Final elapsed ends after confirmation and hash check. Do not then rewrite frozen tracked files.

## Verification Commands

From repository root: `python -B governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md --receipt-dir .cvf/runtime/cvf-expense-browser-worker-20261010/gates`.
Build: `node scripts/cvf_expense_fixture_preview.cjs --output .cvf/runtime/cvf-expense-browser-worker-20261010/expense-preview.html`.
Focused browser proof: `node scripts/test_cvf_expense_fixture_preview_browser.cjs`; emits bounded runtime reports/logs/screenshots and includes two mutants.
Syntax checks: `node --check scripts/cvf_expense_fixture_preview.cjs`; `node --check scripts/test_cvf_expense_fixture_preview_browser.cjs`.
Full return and separate frozen confirmation: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`.
No unit/full app suites, global tsc, installs or browser server; record commands/exit/timing/actual assertion counts and final five-path Git union.

## Worker Autonomy / No-Question Rule

Resolve routine bundler/markup/test choices and grouped repairs without another operator question. One manually transferred assignment, one90-minute TOTAL ceiling, no tool-delegated subagent/external/provider invocation. At pin/tool/source/scope contradiction or ceiling return one consolidated BLOCKED_WITH_REASON. Full worker elapsed must include first read and postrecord confirmation; unknown pre-read or end time is not within-budget proof. Local review target15 minutes; actual usage/bill unknown unless supplied. No automatic retry/successor.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-EXPENSE-BROWSER-20261010
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
| baseHeadFor(phase) | dispatchBaseHead=665da5b2df3e1d2b81553a5c9567c7babb364459; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact five worker paths; dispatcher pair and inputs separately owned |
| traceScope(phase, actor) | each actor records own commands and evidence |
| commitOwner(phase) | Local closer; WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no unrelated dirty files or stopped-chain redispatch |
| nextMoveSurfaces | current front door, active handoff and generated state steward-only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: operator-transferred shared-workspace implementation worker after committed release; Local reviewer after worker lane release
laneOwnedPaths: exact five-path acceptance ledger
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
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | five allowed paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | five allowed paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity,pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker proof/return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | WORKER_RETURN | worker | WORKER_RETURN | worker proof/return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | REVIEW | reviewer | REVIEW | five allowed paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | PRE_MATERIAL_COMMIT | reviewed five paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | POST_MATERIAL | reviewer | REVIEW | Local completion review | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | source continuity and generated views | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL_CLOSURE | reviewed material/continuity ranges | EXACT_PATHS | Local-closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Graph describes required owners and sequence; passed authoring checks are not worker execution proof.

## Reviewer Closure Conversion

completionReviewPath: docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_COMPLETION_2026-10-10.md
reviewerOwnedClosurePaths: completion/status and separately authorized continuity; workerCommitPermission: FORBIDDEN.
EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION; routine M5/M10/safety/M20. Consume valid browser/mutant receipts and two pinned screenshots. Local independent probe is one alternate fixture with wrong-year/impossible dates plus one source-drift sentinel refusal; no duplicate broad suite. Preserve original return and timer/process deviations. Material commit and its actual committed proof BEFORE real-SHA continuity; then clean continuity proof separately. No retrospective worker-history repair or media/export admission.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
workerReturnPath: `docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md`
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
| EXTERNAL_AGENT_CLI_MCP | detached research/execution | not selected; ceiling0, no adapter admission |
| Browser UI | installed local headless Chromium | selected synthetic offline UI only, no server/network/provider |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named UI/design sources only; no complete repository scan claim.

## Knowledge System Applicability

- Knowledge-map verdict: NOT_APPLICABLE_WITH_REASON - no corpus-derived knowledge map; source trace covers only named UI/design inputs.

## Evidence Reuse And Encoding Plan

Consume accepted unit12/12 and mutant2/2 evidence within its original scope; no duplicate unit rerun. New proof measures browser transport/interaction/layout only. UTF-8; Text Encoding Exception markers for Vietnamese labels. Tokens/bill and model identity remain qualified. Read known return literal tokens before writing; use current scaffold and disclosure of first failures.

## Claim Boundary

Private actual-component browser UI preview only; two new scripts plus three metadata files, not a two-file-only governed execution. No application-route integration, AI-governance behavior, actual ledger/provider, media, production readiness, source-R2 recovery/public/deploy/P11 claim. Original unit timing/process deviations retained. Next worker preference is operator-reported Haiku5.5/Max metadata, not normative or a savings claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Accepted component | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList; filterExpensesByMonth | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList; filterExpensesByMonth | ACCEPT |
| Read-only existing test fixture | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | FIXTURE; render cases | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | FIXTURE; render cases | ACCEPT |
| Accepted unit result and limitations | docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_COMPLETION_2026-10-09.md | Findings / Position; Claim Boundary | docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_COMPLETION_2026-10-09.md | Findings / Position; Claim Boundary | ACCEPT |
| Behavior intent | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | ACCEPT |
| UI contract | canonical UI contract DESIGN.md | theme and tokens | DESIGN.md | theme and tokens | ACCEPT |
| Existing browser method | scripts/test_cvf_storyboard_preview_browser.cjs | withPage; Chromium; screenshot | scripts/test_cvf_storyboard_preview_browser.cjs | withPage; Chromium; screenshot | ACCEPT |
| Forward learning | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | ACCEPT |
| Existing dependencies | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | react; @playwright/test; vitest | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | react; @playwright/test; vitest | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_task_governance_route.py |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; Source Verification Block; COMPLETE_PENDING_REVIEW; CLOSEABLE; gateId; mutationSurface; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source-verified packet structure, not first discovery |
| claimBoundary | no worker implementation or media execution proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`expense-browser-preview`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class expense-browser-preview --role dispatcher --lifecycle-phase pre-dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Targeted rg in scripts and accepted expenses directory found only the new accepted unit fixture, no actual-component browser preview/helper. Prior storyboard browser suite covers a different static projection; no duplicate rerun selected. This is not repository-wide absence/completeness proof. Exact nine packet/worker paths checked absent. Existing source-R2 key and STOP unchanged; new finite UI outcome has a separate INITIAL identity.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-NCR-EXPENSE-BROWSER-20261010",
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
    "docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.json",
    "docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json",
    "scripts/cvf_expense_fixture_preview.cjs",
    "scripts/test_cvf_expense_fixture_preview_browser.cjs",
    "docs/guides/CVF_EXPENSE_BROWSER_PREVIEW_README_2026-10-10.md",
    "docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json",
    "docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md"
  ],
  "claims": [
    "PRIVATE_BROWSER_UI_PREVIEW_ONLY",
    "SOURCE_R2_STOP_RETAINED"
  ],
  "requiredProof": [
    "SOURCE_BOUND_PREVIEW",
    "BROWSER_CASES_AND_MUTANTS",
    "USAGE_LIMITS",
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
| Operator2026-10-10 continue; prior autonomous isolated tests/manual transfer and Local reviewer role | ACCEPT |
| Paired GC-018 baseline docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md | ACCEPT |
| Accepted unit and browser capability pins docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json | ACCEPT |
| Source R2 and all effect holds | ACCEPT; retained |

## Agent Roles

Dispatcher prepares and releases; shared-workspace worker implements; separate Local reviewer evaluates evidence; Local closer commits; session-sync steward updates continuity. Operator manually transfers the order; no automated worker/provider invocation.

## Required First Reads

FIRST capture timer in allowed runtime, before this work order or any source read; then progressive startup, docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md, this order, docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json, accepted component/test/completion, S05-S06, DESIGN.md, existing browser script and relevant checker literals. Installed Vite/React API only as needed; no full history or ambient .env reads.

## Pre-Flight Checks

All frozen pins match; five worker outputs absent; installed Vite/React/ReactDOM/Playwright resolve from web node_modules and Chromium executable exists; no install needed. Actual clean committed bound pre-dispatch PASS and pre-implementation PASS required before implementation writes. Generic dependency bundling verified by dispatcher, not task execution. Source drift fails closed; packet contradiction routes to Local.

## Write Ownership

Worker owns five exact outputs plus bounded runtime preview/screenshots/reports/mutants and pre-read timer. Dispatcher owns four packet/input paths; Local reviewer owns acceptance/status; steward owns generated continuity. No dispatcher mutation while worker lane active. Tool-owned mandatory gate roots authorized independently of worker runtime caps.

## Evidence Requirements

docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json records previewBuild, browserTestResults, guideVerification, workerReturnGate; source/tool hashes, HTML hash/bytes, two viewport scenarios, exact expected/observed IDs and calendar outcomes, screenshots+hashes, all request/error counts, mutation identities and valid discriminating failures, source restoration, five output caps and Git union. Record timer start-before-read, end-after-confirmation, complete elapsed, first failures and grouped repairs. Full return gate then separate frozen confirmation log and final hash manifest; no post-confirmation tracked rewrites. Unknown usage is NOT_AVAILABLE_WITH_REASON. Never certify absent history.

## Review Gate

Local evaluates unchanged source bindings, ordinary/negative browser outcomes, two killed mutants, screenshot/layout evidence, no requests/errors, and start/final time provenance. No per-row duplicate suite; one separate alternate fixture and source-drift sentinel only. Technical output, procedure quality and model/billing assessment remain separate. Resolve ordinary decisions locally, no repeat operator confirmation.

## Closure Checklist

Worker no commit; exact five outputs; source pins unchanged; two scripts syntax valid; primary self-contained preview and focused browser proof; discriminating mutants; two screenshots; bounded guide; full gate and frozen confirmation. Local accepts/rejects; closer commits material, obtains actual material-range proof at that HEAD, then steward real-SHA continuity and its own verified committed range proof. No combined range or historical fingerprint promotion.

## Return-To-Orchestrator Conditions

COMPLETE_PENDING_REVIEW only when all five paths, four proof IDs and bound full gate succeed. Otherwise one BLOCKED_WITH_REASON with grouped missing evidence; no self-extension or redispatch. Future media/operator content checkpoints do not block this honestly complete isolated browser fixture.

## Operator Checkpoint

No new operator checkpoint for this bounded private synthetic browser proof under standing isolated-test authority. Final storyboard content, source/native/provider/media/real-data/public/deploy/P11 remain independent parked checkpoints. No repeat consent requested for routine implementation choices.

## Foundation Storage Layout Block

Reuse scripts, guides and reviews/evidence; no new runtime daemon/system/registry or package. Five outputs within builder250/test350/guide100/evidence350/return450; generated HTML and media-like screenshots stay ignored runtime with caps. Sixth tracked path or foreseeable split requires dispatcher amendment before creation.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
reviewerDecisionOwner: LOCAL
independentProbeRiskClass: BOUNDED_LOCAL_VALIDATOR
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
implementationOracleSeparation: Local-authored alternate five-row fixture/expected IDs, no import of worker test oracle
positiveControl: actual component displays exact March2026 rows from separate fixture
negativeMutationClasses: impossible calendar and same-month wrong-year row; changed-source pin refusal preserves sentinel
expectedInformationGain: distinguish authentic browser rendering/source identity from a rewritten/static lookalike
rerunCostReason: one tiny alternate fixture plus source-drift refusal, consume original suite/screenshots

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private shared CVF workspace |
| Session or invocation | expense-browser-dispatch-20261010 |
| Working directory | repository root |
| Command or tool surface | targeted overlap/source checks, generic bundler capability, scaffold, exact pins and feasibility |
| Target paths | `docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.json`; `docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json` |
| Allowed scope source | operator continue, isolated tests and manual worker transfer; Local reviewer |
| Before status evidence | clean HEAD 665da5b2df3e1d2b81553a5c9567c7babb364459; five outputs absent |
| After status evidence | four packet paths only; actual worker task not run |
| Diff evidence | git status --short; exact staged manifest; git diff --check |
| Approval boundary | standalone browser UI packet |
| Claim boundary | no component/browser implementation acceptance |
| Agent type | INTERNAL_AGENT |
| Invocation ID | expense-browser-dispatch-20261010 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.json`; `docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.json`; `docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | expense browser preview dispatch |
| claimDisposition | CLAIM_REJECTED: no source/runtime production acceptance |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: new worker not run |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no media/provider action |
| invocationBoundary | Local packet only; operator transfers worker |
| interceptionBoundary | no OS/native containment implemented |
| claimLanguage | private prototype only |
| forbiddenExpansion | source retry, media, install/provider/public |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-expense-actual-component-browser-preview","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

New INITIAL browser UI outcome; not a source-R2 successor, retry or counter reset.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-EXPENSE-BROWSER-20261010 --title "NCR Expense Browser Preview" --date 2026-10-10 --base 665da5b2df3e1d2b81553a5c9567c7babb364459 --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard/no-commit worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | verified prior packet boilerplate reused; all task-specific scope/source/ledger/probe/timing/browser contracts replaced |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | NONE |
| claimBoundary | authoring only |

## Current Runtime Freshness Verification

Installed React19.2.3, TypeScript5.9.3, Vite build API and Playwright Chromium executable observed locally. Generic React/ReactDOM dependency IIFE build189372 bytes PASS with config/env loading disabled; no accepted component import, browser launch or task preview. First virtual-entry capability attempt failed resolution; absolute ignored generic entry fixed it. Not an upstream/current availability claim. Worker must recheck pinned tooling and actual launch outcomes.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_COMPLETION_2026-10-09.md |
| Chain map route | accepted unit component -> independent browser UI proof |
| Matching local-view guard | N/A with reason: no external intake |
| Owner surface | accepted unit fixture and S05-S06 requirements |
| Disposition | ADAPT existing component for private preview |
| Claim boundary | no external absorption or source successor |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON - no new absorption capability/corpus or legacy coverage claim.

## Export Surface Decision

Private ignored runtime preview and five governed worker outputs only; no public catalog/export claim or public-sync effect.

## Tool / Classifier Block Recovery Contract

toolClassifierBlockRecoveryApplicability: NOT_APPLICABLE_WITH_REASON - local offline UI only; no blocked provider/media effect authorized.

## Required Artifact Manifest

| Path | Required at handoff |
|---|---|
| scripts/cvf_expense_fixture_preview.cjs | YES |
| scripts/test_cvf_expense_fixture_preview_browser.cjs | YES |
| docs/guides/CVF_EXPENSE_BROWSER_PREVIEW_README_2026-10-10.md | YES |
| docs/reviews/evidence/cvf-expense-browser-worker-2026-10-10.json | YES |
| docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md | YES |

Worker return path: docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_WORKER_RETURN_2026-10-10.md

## Intake Role Routing Decision

Intake summary: standalone preview and native-browser proof of accepted component.
Scope classification: two implementation scripts plus three metadata, no app integration.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Escalation condition: source/tool/scope contradiction, extra path/effect, or elapsed ceiling; grouped BLOCKED_WITH_REASON.
MULTI_AGENT_MULTI_ROLE: Local dispatcher -> manually transferred shared-workspace worker -> independent Local reviewer/closer. No automated CLI/MCP/provider invocation.

## Dated Owner Dependency Discovery

Named component/design/tool inputs frozen2026-10-10; read-only accepted fixture and browser helper reused. Installed tool package metadata pins are execution aids, not canonical source authority; governed package/dependency contract and actual capability observation stay separate. No dependency acquisition or repository-wide enumeration claim.

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
      "action": "Verify actual-component offline browser scope and pinned tooling before release; retain accepted unit evidence and stopped source lanes; require timer before first read and separate frozen final confirmation.",
      "verificationPlan": "Actual-order binding positive/missing-plan negative; exact canonical feasibility and clean committed bound dispatch; review fresh browser behavior separately from unit/process/model cost."
    }
  ]
}
```

Prior bounded application preserved; new plan is not application evidence.


## Local Closure Receipt

CLOSED_PASS_BOUNDED: five original browser-preview artifacts accepted; independent alternate fixture/sentinel PASS; historical timer/read deviations and inherited touch target limitation retained.
Completion evidence: docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_COMPLETION_2026-10-10.md; docs/reviews/evidence/cvf-expense-browser-local-review-2026-10-10.json.
No redispatch; original return preserved.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| BUILD | actual pinned component, standalone offline HTML | pins and primary/calendar hashes MATCH; independent builder transport PASS | PASS |
| BROWSER | profiles, calendar negatives, meaningful mutants | worker 5 ordinary records PASS; 2 assertion kills; Local alternate fixture PASS | PASS |
| GUIDE | usage and limits | commands/source binding inspected; dark-only and touch-target limitation explicit | PASS |
| RETURN | full bound gate, frozen bytes, no commit | three draft failures then PASS; separate frozen confirmation COMPLIANT; five raw hashes MATCH | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md | CLOSED_PASS_BOUNDED; no redispatch | PASS |
| Completion or reviewer artifact | docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_COMPLETION_2026-10-10.md | five frozen worker outputs accepted, limitations retained | PASS |
| Roadmap state | existing NCR/video owners | no new successor or production admission | N/A with reason: standalone work order |
| Registry JSON | docs/reviews/evidence/cvf-expense-browser-local-review-2026-10-10.json; docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json | hashes; independent executable probe; model ledger | PASS |
| Registry Markdown | docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_COMPLETION_2026-10-10.md | five disclosed findings and model observations | PASS |
| External evidence digest | docs/reviews/evidence/cvf-expense-browser-local-review-2026-10-10.json | internal worker result only | N/A with reason: no external research |
| System loop interlock | source R2 and C1 STOP owners retained | no retry/reset/effect | PASS |
| Session continuity | AGENT_HANDOFF_V63_2026-09-18.md; generated bootstrap/state | closed raw pin, then actual material SHA | PASS |
