# CVF Agent Work Order - NCR Expense Filter Fixture
Memory class: governed-worker-dispatch
docType: work_order
Status: READY
Date: 2026-10-09
Batch ID: CVF-NCR-EXPENSE-FIXTURE-20261009
Dispatch base head: d46cd676a367666bfe3abffbf25c54e327522fc0
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false
Preapproval-Feasibility: REQUIRED
Preapproval-Feasibility-Companion: docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.json

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT shared-workspace implementation worker; Local remains orchestrator/reviewer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md; baseline docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md; frozen inputs docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture the actual clean released HEAD before edits.
Current-time notes: operator transfers this order manually; no automated worker invocation.
Do-not-misread notes: independent unit fixture only; not source R2/native/media successor or live governance proof.
Required first actions: startup, pair and input pins; actual bound dispatch receipt and pre-implementation gate before writes.
Return contract: docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md and docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json; COMPLETE_PENDING_REVIEW only with required evidence and bound full return gate.
Exact workspace: D:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF. Worker is INTERNAL_AGENT regardless of model/provider; Local owns final technical disposition.

## Purpose

Implement the four expense-filter UI behaviors explicitly described in storyboard S05-S06 as a standalone React fixture and meaningful tests. No app wiring, API, model call, video asset or storyboard revision. The named value gap is that the expense behavior has no implementation/test in the inspected source regions; the accepted offline storyboard was presentation-only.

## Scope / Target / Owner Boundary

Operator standing autonomous isolated-test/continuation and manual worker transfer authority applies to this finite UI fixture. Exactly two implementation paths plus three guide/proof/return paths. Local owns technical acceptance; source R2 and effect holds remain untouched. No product route integration, HTML export change or source storyboard content acceptance is inferred.

## Allowed Paths

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx`
- `docs/guides/CVF_EXPENSE_FILTER_FIXTURE_README_2026-10-09.md`
- `docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json`
- `docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md`

Worker-authored fixtures, logs and mutation copies only under `.cvf/runtime/cvf-expense-filter-worker-20261009/`, total20MiB, individual text2MiB. Mandatory gate-owned `.cvf/runtime/autorun-receipts/`, `.cvf/runtime/reviewer-fast/`, declared gate temporary files and test-owned caches are authorized tool outputs, not additional implementation files. Do not install dependencies or clean shared caches.

## Forbidden Paths

All tracked paths outside the exact five-file manifest, including existing UI components, routing, package/lockfiles, test setup/config, source design, closed storyboard artifacts and all governance/session files. No private credential reads/output, no network/provider/server/recording/media/public/deploy, native helper or source-supervisor attempt. Test setup may perform its existing secret-safe environment loading; do not inspect or print its ambient values.

## Implementation Contract

1. Named export ExpenseList in EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx; props expenses are readonly records with id:string, date:string, label:string, amount:number. Optional exported pure filter helper stays in this file. No production mount/import elsewhere.
2. Native month input with accessible Vietnamese label, visible list/table and no-expenses message. Empty month shows all valid rows; YYYY-MM month filters by exact year/month. Invalid dates are always excluded without crashing. Preserve supplied order/IDs; do not mutate props.
3. Dates accepted only as actual Gregorian YYYY-MM-DD calendar dates. Reject malformed text, unpadded fields and nonexistent days; no locale parser or host timezone month inference. Leap-year behavior must be tested. No persistence, requests or new dependencies.
4. Primary fixture has exactly five manually authored synthetic rows: two February2026, two March2026, one invalid date. March shows two, April empty, cleared filter four valid rows, invalid row never crashes or appears. Additional negative cases transform this same fixture; record this interpretation of all/invalid, not a change to source wording.
5. Actual React rendering tests use existing Vitest/jsdom and testing-library, not only a helper or snapshots. Show synthetic/private fixture notice; use DESIGN.md tokens for simple accessible markup. Unit tests assert behavior/content/accessibility only; no browser/responsive or AI-governance claim.
6. Source caps component200, tests350, guide100, evidence300, return450 physical lines. No extra source split foreseeable; a sixth tracked path requires dispatcher amendment. Do not modify the accepted storyboard narration, badges or source claim status.

## Acceptance Criteria

Deliver all five outputs with concrete source-backed component, four render cases, date/year/leap negatives, no props mutation and at least two killed in-memory/disposable-source mutants: removed month filtering and accepting invalid dates. Every mutant starts from the passing unchanged baseline; keep worker source hashes unchanged after sweep. A finite NOT_EXECUTED test class is not PASS.

## Work-Order Fulfillment Manifest

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "COMPONENT",
      "mandatory": true,
      "expectedArtifacts": [
        "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx"
      ],
      "requiredProofIds": [
        "COMPONENT_CONTRACT"
      ]
    },
    {
      "requirementId": "TEST",
      "mandatory": true,
      "expectedArtifacts": [
        "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx"
      ],
      "requiredProofIds": [
        "FOUR_CASES_AND_MUTATIONS"
      ]
    },
    {
      "requirementId": "GUIDE",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/guides/CVF_EXPENSE_FILTER_FIXTURE_README_2026-10-09.md"
      ],
      "requiredProofIds": [
        "USAGE_LIMITS"
      ]
    },
    {
      "requirementId": "RETURN",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json",
        "docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md"
      ],
      "requiredProofIds": [
        "BOUND_FULL_RETURN_GATE"
      ]
    }
  ],
  "proofCatalog": [
    {
      "proofId": "COMPONENT_CONTRACT",
      "kind": "LOCAL_UI_ONLY",
      "locator": "docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json#componentContract"
    },
    {
      "proofId": "FOUR_CASES_AND_MUTATIONS",
      "kind": "LOCAL_UI_ONLY",
      "locator": "docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json#unitTestResults"
    },
    {
      "proofId": "USAGE_LIMITS",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json#guideVerification"
    },
    {
      "proofId": "BOUND_FULL_RETURN_GATE",
      "kind": "LOCAL_STATIC",
      "locator": "docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json#workerReturnGate"
    }
  ]
}
```

The ledger is the canonical exact Required Artifact and Required Proof manifest. Required Proof Manifest Atomic Literal Discipline: one proofId per atomic requirement.

## Execution Plan

1. Capture UTC/monotonic start before startup/read/draft/write/gates; one60-minute total worker ceiling.
2. Verify frozen pins, tools, clean committed release and bound pre-implementation gate.
3. Implement the two files; run only the focused unit tests and two discriminating mutation classes; restore original submitted hashes.
4. Guide, evidence and checker-safe return scaffold; full bound return gate and frozen-return confirmation; stop for Local review. No installation, browser server or other suites.

## Verification Commands

Run from repository root: `python -B governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md --receipt-dir .cvf/runtime/cvf-expense-filter-worker-20261009/gates`.
Focused UI command from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`: `node node_modules/vitest/vitest.mjs run src/expenses/ExpenseList.test.tsx --reporter=verbose`. Use actual installed tools and unchanged test config/setup.
Required return: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`.
Record exact commands, working directory, exit, timing, tests/mutation results, all five file hashes/line counts and Git changed union. An unbound or individual checker is not the required full result.

## Worker Autonomy / No-Question Rule

Resolve routine markup/test/data choices and grouped in-scope repairs without another operator question. One manual worker assignment, one60-minute total ceiling including all reads/gates, zero tool-delegated subagent/external/provider invocation. At source/scope/tool contradiction or ceiling return one consolidated BLOCKED_WITH_REASON. Local target15-minute evidence review; model-cost assumptions unknown without actual tokens/bill. No automatic retry/successor.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-EXPENSE-FIXTURE-20261009
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
| baseHeadFor(phase) | dispatchBaseHead=d46cd676a367666bfe3abffbf25c54e327522fc0; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
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

completionReviewPath: docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_COMPLETION_2026-10-09.md
reviewerOwnedClosurePaths: completion/status and separately authorized continuity; workerCommitPermission: FORBIDDEN.
EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION; routine M5/M10/safety/M20. Consume valid focused tests/mutation receipts; one separate tiny date-boundary fixture only as specified. Preserve original submission and procedural deviations. Material commit, real-SHA continuity, clean split closure; no production/media/export acceptance.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
workerReturnPath: `docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md`
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
| Browser UI | not selected | no browser/session/server effect required |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named UI/design sources only; no complete repository scan claim.

## Knowledge System Applicability

- Knowledge-map verdict: NOT_APPLICABLE_WITH_REASON - no corpus-derived knowledge map; source trace covers only named UI/design inputs.

## Evidence Reuse And Encoding Plan

Reuse immutable design and prior accepted storyboard limits; no narrative/browser rerun. UTF-8 and existing localized component convention; short Vietnamese guide. Test/cost facts belong in evidence, no stale PASS UI badges. Original source claims remain historical; report only newly observed fixture behavior.

## Claim Boundary

Private standalone unit UI fixture only; two implementation paths and three metadata artifacts, not an actual two-file-only governance run. No app integration, E2E workflow, CVF AI-governance behavior, real ledger, browser/print/paper, media/live/public claim. Source R2/counters and native/provider/media holds unchanged. Tokens/bill unknown; no Haiku-versus-Sonnet superiority or savings claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Four behaviors and source boundaries | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06; Claim Boundary | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06; Claim Boundary | ACCEPT |
| Prior UI lacks expense proof | docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_COMPLETION_2026-10-09.md | Scope / Methodology; Claim Boundary | docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_COMPLETION_2026-10-09.md | Scope / Methodology; Claim Boundary | ACCEPT |
| Existing unit tooling | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts | test environment/setup/include | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts | test environment/setup/include | ACCEPT |
| Source/effect isolation | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts | provider-execution fetch guard; secret-safe environment setup | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts | provider-execution fetch guard; secret-safe environment setup | ACCEPT |
| UI contract | canonical UI contract DESIGN.md | theme and tokens | DESIGN.md | theme and tokens | ACCEPT |
| Forward control | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_task_governance_route.py |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; Source Verification Block; COMPLETE_PENDING_REVIEW; CLOSEABLE; gateId; mutationSurface; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source-verified packet structure, not first discovery |
| claimBoundary | no worker implementation or media execution proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`expense-filter-fixture`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class expense-filter-fixture --role dispatcher --lifecycle-phase pre-dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Targeted filename search in EXTENSIONS/scripts/review evidence found no ExpenseList/expense demo fixture. This is not corpus absence/completeness proof. All exact new packet/worker paths checked absent. Existing Print/navigation E2E tests inspected; no duplicate rerun selected. Independent storyboard unit-fixture identity; source-R2 STOP is not renamed or reset.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-NCR-EXPENSE-FIXTURE-20261009",
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
    "docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.json",
    "docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx",
    "docs/guides/CVF_EXPENSE_FILTER_FIXTURE_README_2026-10-09.md",
    "docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json",
    "docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md"
  ],
  "claims": [
    "PRIVATE_UNIT_UI_FIXTURE_ONLY",
    "SOURCE_R2_STOP_RETAINED"
  ],
  "requiredProof": [
    "COMPONENT_CONTRACT",
    "FOUR_CASES_AND_MUTATIONS",
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
| Operator2026-10-09: continue; manual transfer to Claude; Local orchestrator/reviewer | ACCEPT |
| Paired GC-018 baseline docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md | ACCEPT |
| Accepted behavior design and pinned unit config/setup docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json | ACCEPT |
| Source R2 terminal restrictions | ACCEPT; retained boundary |

## Agent Roles

Dispatcher prepares and releases; shared-workspace worker implements; separate Local reviewer evaluates evidence; Local closer commits; session-sync steward updates continuity. Operator manually transfers the order; no automated worker/provider invocation.

## Required First Reads

Startup front door/bootstrap/current handoff progressively; docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md; this order; docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json; named design S05/S06; DESIGN.md; existing unit config/setup; relevant checker literals before output authoring. No full history or unrelated source corpus read. Capture timer first.

## Pre-Flight Checks

All frozen source hashes match, output paths absent, installed Vitest/testing-library available, actual clean committed bound release PASS and pre-implementation PASS. No writes before those checks; source drift fails closed. Packet contradictions are handled by the dispatcher before release.

## Write Ownership

Worker owns five exact outputs and bounded ignored test logs/copies. Dispatcher owns four packet/input paths; reviewer owns final acceptance/status; steward owns generated continuity. Mandatory gate-owned output roots declared above. No dispatcher mutation while worker is active.

## Evidence Requirements

docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json records componentContract, unitTestResults, guideVerification, workerReturnGate: exact four scenario counts, malformed/calendar/leap/year cases, immutability, mutant identities/results, commands/exit/time, input and output hashes/lines, source/metadata counts and limits. Return contains executionBaseHead, Git union, acceptance-evidence-json and complete bound gate. Record first failures and grouped self-repairs honestly; token/quota usage NOT_AVAILABLE_WITH_REASON if no meter. Never fabricate committed file status.

## Review Gate

Review coherent four-case requirements, source/metadata scope and discriminating tests. Local authors one independent year/month/calendar-boundary fixture; do not import worker test oracle or repeat whole package suites. Unit fixture proof is not end-to-end governed execution or final storyboard acceptance.

## Closure Checklist

Exact scope, required artifacts and proof contents; full return gate; Local semantic review; no old STOP reset; material commit followed by real-SHA continuity; verify split committed ranges. Runtime and public approval remain separate.

## Return-To-Orchestrator Conditions

COMPLETE_PENDING_REVIEW only when all five paths, four proof IDs and bound full gate succeed. Otherwise one BLOCKED_WITH_REASON with grouped missing evidence; no self-extension or redispatch. Future media/operator content checkpoints do not block this honestly complete isolated unit fixture.

## Operator Checkpoint

No new operator preference needed for admitted isolated UI unit development. Operator manually transfers order; Local dispatch/review. App wiring, live demo/recording, source/native, rights/install, media/provider/public/deploy/P11 remain parked. A code/test fixture is not approval to change storyboard claims.

## Foundation Storage Layout Block

Reuse existing component/test, guides and reviews/evidence roots; no new system/standard/index/daemon. Five exact paths within component200/test350/guide100/evidence300/return450 caps. A sixth tracked path or source split requires dispatcher amendment before creation.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
reviewerDecisionOwner: LOCAL
independentProbeRiskClass: BOUNDED_LOCAL_VALIDATOR
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
implementationOracleSeparation: separate Local date fixture/oracle derived from S06, not worker expectations
positiveControl: March2026 exact-year/month rows with a separate fixture
negativeMutationClasses: invalid calendar date and wrong-year same-month row
expectedInformationGain: distinguish calendar validation and exact filtering from forgiving Date parsing
rerunCostReason: one tiny independent fixture; no duplicate broad suite

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | expense-filter-dispatch-20261009 |
| Working directory | repository root |
| Command or tool surface | targeted requirement/tool/overlap reads; scaffold; pinned packet; canonical feasibility and authoring checks |
| Target paths | `docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.json`; `docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json` |
| Allowed scope source | operator continue; standing autonomous isolated tests and manual worker handoff; Local reviewer |
| Before status evidence | clean HEAD d46cd676a367666bfe3abffbf25c54e327522fc0; five outputs absent |
| After status evidence | four packet artifacts only; worker not invoked and implementation pending |
| Diff evidence | git status --short; git diff --check; exact staged manifest |
| Approval boundary | standalone unit fixture only |
| Claim boundary | dispatch packet only, no implementation acceptance |
| Agent type | INTERNAL_AGENT |
| Invocation ID | expense-filter-dispatch-20261009 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.json`; `docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.json`; `docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | expense unit fixture dispatch |
| claimDisposition | CLAIM_REJECTED: no source/runtime production acceptance |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: new worker not run |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no media/provider action |
| invocationBoundary | Local packet only; operator transfers worker |
| interceptionBoundary | no OS/native containment implemented |
| claimLanguage | private prototype only |
| forbiddenExpansion | source retry, media, install/provider/public |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-storyboard-expense-filter-unit-fixture","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

Independent expense unit-fixture identity only; source C1/R2 blockers, counters and STOP remain untouched.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-EXPENSE-FIXTURE-20261009 --title "NCR Expense Filter Fixture" --date 2026-10-09 --base d46cd676a367666bfe3abffbf25c54e327522fc0 --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard/no-commit worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | reuse verified prior packet role/closeability contracts; replace all task-specific scope, ledger, source and fixture sections |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | NONE |
| claimBoundary | authoring provenance only |

## Current Runtime Freshness Verification

Existing installed Vitest binary and package/config/setup paths observed without install. Worker rechecks exact pinned source and tool availability. No upstream version, runtime provider or browser support claim. No fixture produced by dispatcher.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md |
| Chain map route | accepted S05-S06 requirements -> unit fixture |
| Matching local-view guard | N/A with reason: no external intake |
| Owner surface | accepted storyboard |
| Disposition | ADAPT pure unit UI behavior |
| Claim boundary | no external absorption or source successor |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON - no new absorption capability/corpus or legacy coverage claim.

## Export Surface Decision

Private provenance worktree only; local kit handoff, no public/export runtime.

## Tool / Classifier Block Recovery Contract

toolClassifierBlockRecoveryApplicability: NOT_APPLICABLE_WITH_REASON - local offline UI only; no blocked provider/media effect authorized.

## Required Artifact Manifest

| Path | Required at handoff |
|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | YES |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | YES |
| docs/guides/CVF_EXPENSE_FILTER_FIXTURE_README_2026-10-09.md | YES |
| docs/reviews/evidence/cvf-expense-filter-worker-2026-10-09.json | YES |
| docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md | YES |

Worker return path: docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_WORKER_RETURN_2026-10-09.md

## Intake Role Routing Decision

Intake summary: realize the four documented expense UI behaviors as a standalone unit fixture.
Scope classification: two implementation and three metadata paths; no app/runtime integration.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Escalation condition: source/tool/authority contradiction, extra path or effect; return grouped BLOCKED_WITH_REASON.
MULTI_AGENT_MULTI_ROLE: Local dispatcher -> manually transferred shared-workspace worker -> independent Local reviewer/closer. No automated provider/CLI/MCP agent invocation.

## Dated Owner Dependency Discovery

Frozen source input rows bind exact raw hashes observed2026-10-09. No external dependency acquisition, source-R2 reopening or full corpus assertion.

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
      "action": "Use S05-S06 phase-specific UI requirements and exact fixture identity; verify bound feasibility/return route before dispatch; retain old STOP and separate two implementation paths from metadata.",
      "verificationPlan": "Canonical actual-order binding positive and in-memory missing-plan negative; explicit feasibility with one canonical object; review actual returned four-case tests and procedure/cost separately."
    }
  ]
}
```

Prior bounded application remains recorded; this is a new task plan, not proof of its application.
