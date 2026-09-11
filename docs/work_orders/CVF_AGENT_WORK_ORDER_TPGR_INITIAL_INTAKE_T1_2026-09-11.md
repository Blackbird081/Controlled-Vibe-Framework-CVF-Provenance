# CVF Agent Work Order - TPGR Initial Intake Admission
Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Date: 2026-09-11
Batch ID: TPGR-INITIAL-INTAKE-T1
dispatchBaseHead: 00f8e1bd1
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: NOT_EXECUTED_YET
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchSurface: INTERNAL_AGENT
providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: internal implementation worker for TPGR-INITIAL-INTAKE-T1.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_INITIAL_INTAKE_T1_2026-09-11.md`.
Paired authority: `docs/baselines/CVF_GC018_TPGR_INITIAL_INTAKE_T1_2026-09-11.md`.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: WORKER_MUST_CAPTURE_AT_START.
Current-time notes: 2026-09-11, source-verified against 00f8e1bd1.
Do-not-misread notes: amend admission only; the three-repo pilot remains unopened.
Required first actions: read startup surfaces, guard orientation, literal gotchas, this packet, paired baseline, checker/source owners; capture exact HEAD/status and pass pre-implementation.
Return contract: six-path uncommitted delta, required gates, COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON. No network or provider use.

## Purpose

Remove the evidence-bootstrap contradiction for initial source acquisition and bounded survey without weakening evidence requirements for selected absorption, semantic completeness or runtime acceptance. Implement the narrow additive contract below in the existing TPGR owner.

## Authority Chain

Operator agreement on 2026-09-11 -> AGENTS.md and current active handoff -> paired GC-018 -> this packet -> existing TPGR standard/schema/router. The user authorized the amendment; returned Web research is context, not authority. Standalone operator-authorized defect repair; no parent roadmap.

## Intake Role Routing Decision

Intake summary: operator-authorized repair of initial-intake evidence admission in the existing TPGR owner.
Route mode: MULTI_AGENT_MULTI_ROLE.
Internal worker implements; independent Local reviewer accepts/repairs; Local closer commits.
Risk sensitivity: P3_ELEVATED governance-machine surface. No external invocation.
Scope classification: bounded local deterministic validation maintenance.
Escalation condition: manifest expansion, source contradiction, or forbidden effects.

## Agent Roles

Dispatcher/reviewer/closer: Local orchestrator. Worker: operator-selected internal agent in same VS Code workspace. External Web agent: no execution role.

## Required First Reads

Read startup front door/bootstrap/active handoff, paired GC-018, this work order, guard orientation/literal gotchas, TPGR canonical standard, current router/schema/test sources, and applicable checker sources below. Read the domain-funnel method for initial-survey versus acceptance boundaries; no upstream research is required.

## Pre-Flight Checks

Capture HEAD/status; require clean staging and no pre-existing worker-path delta; prove dispatch anchor ancestry; run pre-implementation before editing. Worker does not edit dispatcher-owned packet/continuity paths.

## Write Ownership

Exactly the six Required Artifact Manifest targets. All other paths frozen. Dispatcher may update only packet/continuity before lane transfer; no simultaneous mutations.

## Required Admission Contract

Implement one optional top-level `initialIntakeAdmission` object on the existing manifest version. Omission preserves existing behavior and existing receipt fields exactly. This record is independent of `trancheValue`; do not extend value-admission scope.

The object has exactly these keys; reject extras, missing fields, wrong types and unknown values:

| Field | Required value |
|---|---|
| stage | INITIAL_ACQUISITION_SURVEY |
| plannedReceiptPath | one normalized repo-relative .json or .md output under docs/audits/ or docs/reviews/, maximum 256 characters, no traversal, drive, backslash, control character or empty segment |
| acceptanceDisposition | NO_ABSORPTION_ACCEPTANCE |
| nextStageAuthority | SEPARATE_REVIEWED_WORK_ORDER |
| unknownEvidencePolicy | PRESERVE_UNKNOWN |

plannedReceiptPath is a planned output, not existing evidence. Its existence is not required at dispatch. Never copy it into corpusReceiptRef or convert a future path into a prior receipt. It must fall within a declared path family. Source evidence remains truthful: selectedFilesFullyRead=false and completenessClaimChanged=false; corpusReceiptRef may be null or a nonblank real prior reference retained for reuse. No new interpretation of old historical evidence is permitted.

Admission is valid only when all of these hold:

- taskKind=EXTERNAL_ABSORPTION.
- authorityImpact is NONE or USES_EXISTING_OWNER.
- externalEffect is NONE, LOCAL_REVERSIBLE or NETWORK_READ.
- dataSensitivity is PUBLIC or PRIVATE_REPO.
- reversibility is READ_ONLY or GIT_REVERSIBLE.
- sourceScale is NAMED_FILES, BOUNDED_CLUSTER or CORPUS.
- delegation is SINGLE_ROLE or MULTI_ROLE_NO_COMMIT.
- novelty is KNOWN_PATTERN or OWNER_COMPOSITION.
- no trancheValue record is present.
- requested risk profile is at least P3_ELEVATED; all existing higher risk minimums remain immutable.

Initial-stage path families must be confined to docs/audits, docs/reviews,
docs/work_orders, docs/baselines, .private_reference/source_mirrors, or the
explicit continuity metadata paths CVF_SESSION, CVF_SESSION_MEMORY.md and
AGENT_HANDOFF_V60_2026-09-08.md. Prefix checks must be segment-aware. Reject
broader roots such as docs or .private_reference and any product-source,
governance-code, hook, scripts, SDK or public-workflow family. Continuity paths
are dispatcher-owned; declaration does not authorize worker mutation of them.
Do not create a registry-wide exception for those paths.

For this explicit valid initial stage only, permit the otherwise missing initial full-read confirmation or prior corpus receipt. Do not modify the old selected-read/corpus rejection rules when the optional object is absent. Invalid initial stage must reject, not fall back to a more permissive interpretation.

Successful initial receipts explicitly carry `initialIntakeDisposition: INITIAL_EVIDENCE_COLLECTION_ONLY` and `absorptionAcceptanceAuthorized: false`. Preserve `selectiveExecutionAuthorized: false`, `legacyGateDisposition: RUN_FULL_LEGACY_BUNDLE`, and force SOURCE_PROVENANCE and CORPUS_ACCOUNTING into the selected bundle explanation regardless of sourceScale.

The initial stage permits only source identity/acquisition, immutable pinning, freshness/license evidence, inventory and bounded representative reading. The planned receipt must later record actual read depth, source/manifest/ledger evidence, exclusions, unknowns and next decision. It cannot certify complete absorption, whole-repository semantic reading, final novelty/NO_NEW_VALUE, or authorize integration. Named observations and follow-up recommendations remain advisory until reviewer acceptance under a separate selected-absorption work order.

This is a declaration validator, not a natural-language semantic verifier or process sandbox. The schema/router cannot prove source truth, prevent arbitrary shell operations, or establish that proposed receipts will be produced. Keep that limitation explicit in the standard and worker return.

## Test And Acceptance Matrix

| Case | Expected result |
|---|---|
| Old selected-file task without full-read evidence | existing rejection unchanged |
| Old corpus task without receipt | existing rejection unchanged |
| Old valid manifests without new object | identical routing output; no new receipt fields |
| Explicit initial stage for each source scale with missing initial evidence | ROUTED_SHADOW, P3 or higher, source/corpus bundles, no acceptance |
| Initial record malformed, null, boolean, extra/missing keys or unknown enum | REJECTED_ESCALATED, full fallback |
| Unsafe planned output or output outside declared path families | rejection |
| Product/code/protected path family or broad-root/prefix-collision family | rejection even with otherwise valid initial classification |
| Future planned output absent from disk | allowed only as a planned initial-stage output |
| Full-read or completeness claim true with initial stage | rejection; no blend of acquisition and acceptance |
| Blank prior receipt value | rejection in the initial object path |
| Runtime/live/public/destructive task or effect, secret/credential sensitivity, authority change, new interface/authority, worker commit delegation | rejection |
| Initial record combined with trancheValue | rejection |
| P0/P1/P2 self-downgrade | rejection |
| Malformed ordinary manifest plus valid-looking initial object | rejection; no validation short circuit |
| Active work-order checker integration | explicit new object accepted; malformed object rejected; changed-set coverage retained |
| Schema/router parity | closed record and field types/enums agree; executable tests for schema structure without installing dependencies |

Do not satisfy a test by asserting only status or matching an error substring. For positive initial cases check classification, profile minimum, bundles, full-gate interlock, acceptance flag and deterministic repeat output. For old-valid cases compare the full baseline receipt. Run all pre-existing router and checker tests, not only new tests.

## Execution Plan

1. Read startup/authority/checker sources, capture executionBaseHead and status; run pre-implementation.
2. Reproduce the two original rejections using missing initial evidence; record command and actual output.
3. Implement the additive closed schema, router validation/routing and standard wording in the existing owners; add tests.
4. Confirm ordinary absorption still requires evidence and that initial receipts cannot claim acceptance.
5. Run focused suites and worker-return fast gate; reconcile the exact manifest and leave staging empty.
6. Return COMPLETE_PENDING_REVIEW. Local reviewer independently evaluates this implementation before any new pilot packet.

## Required Artifact Manifest

| Path | Required worker action | Owner |
|---|---|---|
| governance/compat/route_task_governance.py | additive validation/routing only | worker |
| governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json | optional closed initialIntakeAdmission object | worker |
| governance/compat/test_route_task_governance.py | positive/negative/legacy-equivalence coverage | worker |
| governance/compat/test_check_task_governance_route.py | active work-order integration coverage | worker |
| docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md | canonical initial-stage contract and limitations | worker |
| docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md | source-backed return, full command evidence and no-commit statement | worker |

## Work-Order Fulfillment Manifest

Exactly the six targets above. Dispatcher owns the completed single-entry TPGR registration in the active-window registry; worker must not change it. No new helper module, other registry change, checker source change, hook/catalog/template edit, broad file split, or generated aggregate mutation is planned or authorized. The worker may select internal implementation details within these paths. If size limits require a split, return the concrete path/topology need to the reviewer; do not invent new ownership.

## Dated Owner Dependency Discovery

| Owned dated reference path | Classification | Registry evidence | Disposition |
|---|---|---|---|
| docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md | BINDING_REFERENCE_ACTIVE_WINDOW | Dispatcher added this existing canonical standard to governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json before dispatch | ACCEPT |

This is necessary dependency maintenance within the approved admission amendment. No unrelated active-window entry may be changed.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing TPGR standard, router, schema and tests |
| Storage decision | enrich existing owners; no new source module/folder |
| Existing aggregate impact | one narrowly scoped active-window registration |
| Generated state impact | none by worker |
| Durable governance boundary | deterministic metadata only; no runtime service |

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW after all in-scope gates pass, or BLOCKED_WITH_REASON with exact evidence for source contradiction, forbidden-path need or missing authority. Routine allowed-scope repairs belong to worker.

## Evidence Requirements

Capture old rejection behavior before edits, focused test counts and outputs, schema/router parity evidence, exact before/after git status, executionBaseHead and diff. Tests are hermetic metadata-validation tests, not provider or AI-governance proof. No release-gate provider bundle may be invoked.

## Acceptance Criteria

All matrix cases covered with executable evidence; existing suites pass; proposed standard reflects actual implementation; no claim of runtime enforcement; full legacy gates retained; exact six-path worker delta and empty staging; independent Local review still required.

## Forbidden Scope And Stop Conditions

No upstream clone/fetch/research, repo absorption, runtime code, provider/API/network/credentials, dependency install, registry expansion, CI/hooks, public sync, push, deployment or worker commit. Stop BLOCKED_WITH_REASON for missing authority, source contradiction, forbidden-path need or inability to pass a required gate inside this manifest.

Pilot selection remains Agentgateway, QM and DeepSeek Harness. Reuse EARA-AGW-T1 and DSH-WRA-R1 evidence when the later pilot opens; do not repeat unchanged source work. This background is not worker permission to start that pilot.

## Review Gate

Independent Local reviewer evaluates the returned implementation and evidence under EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Review malformed-input handling, old-receipt equivalence, evidence-stage separation and output-path containment before release. Apply MFRP P4-C1 routine M5/M10/safety/M20 cadence; no broad duplicate rerun without contradiction, expected information gain and cost reason.

## Closure Checklist

- [ ] original rejection reproduced before edit
- [ ] additive schema/router/standard contract aligned
- [ ] positive, adversarial, legacy and checker tests pass
- [ ] worker-return fast gate passes
- [ ] six-path delta reconciled and staging empty
- [ ] independent Local reviewer acceptance recorded

## Operator Checkpoint

SATISFIED: operator agreed on 2026-09-11 to narrowly supplement initial-intake admission, with evidence controls and runtime boundary unchanged. Future source survey dispatch remains reviewer-owned and is not opened here.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current selected-file route rejects missing full-read confirmation | LOCAL_SOURCE | governance/compat/route_task_governance.py | route_manifest contradiction checks | route_manifest | TPGR router | ACCEPT |
| Current corpus route requires prior receipt | LOCAL_SOURCE | governance/compat/route_task_governance.py | route_manifest contradiction checks | corpusReceiptRef | TPGR router | ACCEPT |
| Source evidence currently has three closed keys | LOCAL_SCHEMA | governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json | sourceEvidence | selectedFilesFullyRead | manifest v1 | ACCEPT |
| Existing regressions preserve selected-read and prior-receipt rules | LOCAL_TEST | governance/compat/test_route_task_governance.py | selected and corpus tests | test_corpus_requires_receipt_and_selects_accounting | deterministic router tests | ACCEPT |
| Work-order activation uses router | LOCAL_SOURCE | governance/compat/check_task_governance_route.py | evaluate | route_manifest | changed active work-order checker | ACCEPT |
| Initial survey precedes selected conversion | LOCAL_STANDARD | docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md | Two-Step Operating Agreement And Proportional Depth | Initial survey for every acquired repository | method 1.2 | ACCEPT |
| Current standard requires independent review of router/schema changes | LOCAL_STANDARD | docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md | Rollback | independent review | TPGR standard | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_task_governance_route.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_worker_return_quality_gate.py; governance/compat/check_markdown_structural_completeness.py |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Required Artifact Manifest; WORKER_MUST_NOT_COMMIT; sourceEvidence; closeabilityContractVersion; Self-declared worker-return artifact |
| gateRunPurpose | confirmation of source-verified dispatch and output contracts, not first discovery |
| claimBoundary | dispatch read-ahead does not certify worker implementation or source value |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id TPGR-INITIAL-INTAKE-T1 --title "Initial Intake Admission" --date 2026-09-11 --base 00f8e1bd1 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout |
| generatedProfile | protected-governance-path plus internal no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added closed additive admission contract, negative tests, exact six-path worker scope and independent reviewer boundary; reused existing closeability graph shape. |
| checkerReadAheadConfirmation | Listed checker constants, source keys, routing rejection branches and source-backed tests read before authoring. |
| docOnlyNewFields | initialIntakeAdmission proposed contract; plannedReceiptPath; admission claim boundary |
| claimBoundary | authoring provenance only; proposed machine fields are not currently implemented |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-machine-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class governance-machine-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.

Returned defect count: 0. Returned defects: NONE_RETURNED. Disclosed defectIds: none.
Dispatch impact: no matching active resolver item; all named guard obligations remain.

## Current Runtime Freshness Verification

Current local source inspected on 2026-09-11: route_manifest in governance/compat/route_task_governance.py rejects missing selected-file full-read confirmation and missing corpusReceiptRef. Source/schema/tests were read at 00f8e1bd1. This is a metadata predicate observation, not an absence claim about a runtime capability. The two deterministic rejection diagnostics are recorded in Evidence / Verification or the paired baseline.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned baseline and work-order paths | Test-Path on each exact path returned False before authoring | NEW_PATHS_CONFIRMED |
| Packet identifier | search roots: docs/work_orders and docs/baselines; command: rg -n -g '*.md' --fixed-strings 'TPGR-INITIAL-INTAKE-T1' docs/work_orders docs/baselines; query TPGR-INITIAL-INTAKE-T1; zero matches, exit 1 before authoring | NO_COLLISION |
| Existing owner | route_task_governance.py, manifest schema and TPGR standard already own routing | ENRICH_EXISTING_OWNER |

## Core Guard Self-Protection Authorization

Operator authorization: 2026-09-11 explicit agreement to supplement initial-intake admission without weakening evidence or opening runtime authority.

Authorized guard-maintenance scope: amend only the existing TPGR source-evidence admission contract, manifest schema, router and focused tests in the worker manifest. Preserve existing hook/catalog semantics, all legacy gates, old-manifest behavior and unrelated value-admission logic. Worker return must repeat this authorization for its changed set.

Protected worker paths:
- governance/compat/route_task_governance.py
- governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json
- governance/compat/test_route_task_governance.py
- governance/compat/test_check_task_governance_route.py
Dispatcher-owned protected path:
- governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json (single binding-reference entry for TPGR standard, added before dispatch; worker read-only)

Canonical standard owner:
- docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md

Rollback boundary: remove only the newly introduced additive admission feature and its tests if rejected; preserve all historical work and legacy rejection behavior. Do not reset, restore unrelated files, change hooks or reinterpret old receipts.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | TPGR manifest/router and this internal work order | deterministic admission metadata only; independent review, no worker commit | current source and required regression proof | internal direct Python caller, not runtime interception | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no new external adapter | advisory research cannot activate initial intake or accept values | operator relay is content transport only | no CLI/MCP/provider adapter implementation authorized | N/A_WITH_REASON |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: TPGR-INITIAL-INTAKE-T1
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

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "tpgr-initial-intake-admission",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [
      "initial-intake-evidence-bootstrap-gap"
    ],
    "reopened": [],
    "current": [
      "initial-intake-evidence-bootstrap-gap"
    ]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "legacy-and-initial-admission-contract",
      "claimClass": "SCHEMA_COMPATIBILITY",
      "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
      "evidenceRef": "governance/compat/test_route_task_governance.py"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-INITIAL-INTAKE-T1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NONE",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "governance/compat/route_task_governance.py",
    "governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json",
    "governance/compat/test_route_task_governance.py",
    "governance/compat/test_check_task_governance_route.py",
    "governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json",
    "docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md",
    "docs/baselines/CVF_GC018_TPGR_INITIAL_INTAKE_T1_2026-09-11.md",
    "docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md",
    "AGENT_HANDOFF_V60_2026-09-08.md",
    "CVF_SESSION",
    "CVF_SESSION_MEMORY.md"
  ],
  "claims": [
    "deterministic initial-intake admission metadata only"
  ],
  "requiredProof": [
    "focused positive and adversarial routing tests",
    "schema and checker compatibility",
    "legacy receipt equivalence"
  ],
  "operatorCheckpoints": [
    "pilot source acquisition",
    "runtime or public effect",
    "scope expansion"
  ],
  "forbiddenEffects": [
    "worker commit",
    "network",
    "provider calls",
    "source acquisition",
    "runtime implementation",
    "legacy gate suppression"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

This maintenance task has sourceScale NONE because it processes no absorption corpus. It does not use the proposed initial-intake field to authorize its own implementation.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker failures directly and rerun the applicable gate.
Ask no routine preference questions. Stop only for a source contradiction,
missing pinned source, forbidden-path need, or missing authority that prevents
honest completion.
## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher/reviewer/closer; operator-selected internal worker |
| phase | worker implementation then independent Local review |
| baseHeadFor(phase) | dispatchBaseHead=00f8e1bd1; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=NOT_EXECUTED_YET |
| changedSetScope(phase) | worker exactly six manifest paths; reviewer may repair same paths |
| traceScope(phase, actor) | full worker command/status/diff and manifest evidence |
| commitOwner(phase) | worker forbidden; Local closer |
| crossBatchIsolation | dispatcher packet and continuity frozen during worker lane |
| nextMoveSurfaces | return -> Local review -> material/continuity commit -> separate pilot dispatch |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: operator-selected internal worker
laneOwnedPaths: exactly six Required Artifact Manifest paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: worker terminal return, exact manifest reconciliation and empty staging

Clean worktree required at lane handoff. Dispatcher commits only dispatch material and continuity before the operator transfers this packet. Worker captures actual execution HEAD, not dispatchBaseHead as a substitute. Dispatcher will not modify worker-owned paths while the lane is active.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_COMPLETION_2026-09-11.md` (optional; prefer reviewer decision in the named worker return) |
| reviewerOwnedClosurePaths | six worker paths, this work order and paired baseline status; separate active continuity sync |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead=00f8e1bd1; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=NOT_EXECUTED_YET. Worker must record actual start HEAD and prove dispatch anchor ancestry. Reviewer sets closureBaseHead from worker start evidence, commits material before separate continuity, and verifies homogeneous committed ranges. No future SHA prediction.

## Commit Prompt Readiness

Only Local closer may stage and commit after independent evidence review and required gates. No push. Reviewer may repair only authorized worker paths and closure artifacts; forbidden-path repair needs renewed scope.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | reviewer | PRE_DISPATCH | paired baseline, work order and one active-window registration | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline, work order and one active-window registration | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V60_2026-09-08.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact six-path Required Artifact Manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | exact Required Artifact Manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact Required Artifact Manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return and exact manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact material paths and reviewer repair | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact material paths and reviewer repair | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker return reviewer disposition or separate completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact material paths | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Return-Time Closeability Recheck: REQUIRED_BEFORE_REPAIR. Worker must report
whether every mandatory gate is passable without touching forbidden paths.
## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_INITIAL_INTAKE_T1_WORKER_RETURN_2026-09-11.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary; git status --short; Changed Files; Command Evidence; No-Commit Statement; Return-Time Closeability Recheck; Semantic Convergence Outcome.

Conditional section names: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. Use N/A with reason where genuinely inapplicable.

Required markers: Self-declared worker-return artifact: yes; Responds to work order:; dispatchWorkOrder; executionBaseHead; WORKER_MUST_NOT_COMMIT honored. Record actual pending paths, invocation counts and cost as UNKNOWN if unavailable. Never claim clean status while the return is untracked.

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read its applicable checker source and derive exact field/heading/enum requirements. Dispatch checklist is not a substitute. Standard additions require reference shape; worker return requires all quality/trace/delta/epistemic/closeability fields. Reproduce this packet's core guard authorization in the worker return for the worker changed set.

## Verification Commands

Before edits: capture `git rev-parse HEAD`, `git status --short`, ancestry and run:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Before return:

```powershell
python -m pytest governance/compat/test_route_task_governance.py governance/compat/test_check_task_governance_route.py -q
git diff --check
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

Use the exact captured execution base for worker delta/range evidence. No individual checker substitution for the required fast gate.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON
Reason: internal governed validator maintenance; no external invocation or runtime integration.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator method requirement -> existing TPGR metadata owner -> internal implementation review |
| Matching local-view guard | governance/compat/check_task_governance_route.py |
| Owner surface | existing TPGR standard/schema/router |
| Disposition | ADAPT the operator-approved admission requirement; no source-value acceptance |
| Claim boundary | routing maintenance only, no source acquisition or absorption execution |

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: this packet changes a routing metadata owner; it neither acquires nor absorbs an external source. Future intake tasks need their own entry control.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: no repository survey or source-value decision is performed in this maintenance tranche.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus processed; deterministic routing metadata and tests only.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy source payload is inspected or promoted.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | local VS Code workspace |
| Session or invocation | TPGR-INITIAL-INTAKE-T1 dispatch, 2026-09-11 |
| Working directory | repository root |
| Command or tool surface | read-only Git/search, deterministic router diagnostics, apply_patch |
| Target paths | paired baseline, work order and one active-window registration |
| Allowed scope source | operator agreement of 2026-09-11 |
| Before status evidence | clean worktree at 00f8e1bd1 before dispatch authoring; empty staging |
| After status evidence | two dispatcher-owned packets plus one bounded active-window registration; no worker implementation performed |
| Diff evidence | git diff --name-status; git status --short |
| Approval boundary | exact admission amendment worker dispatch only |
| Claim boundary | no implemented behavior or pilot survey claim |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | tpgr-initial-intake-t1-dispatch |
| Expected manifest | paired baseline, work order and one active-window registration |
| Actual changed set | paired baseline, work order and one active-window registration before separate continuity |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic admission metadata implementation dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement claimed |
| receiptEvidence | N/A with reason: routing diagnostics only, not runtime receipts |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: authoring and source inspection only |
| invocationBoundary | internal workspace; no provider or external execution |
| interceptionBoundary | no interception, wrapper or sandbox claim |
| claimLanguage | proposed bounded admission contract, implementation pending |
| forbiddenExpansion | no runtime, provider, public, package, MCP or pilot execution |

## Claim Boundary

This is internal deterministic governance-metadata maintenance, not AI governance runtime proof. No source repository acquisition, research, source-value disposition, corpus completion, implementation of a repo candidate, provider/live call, credential access, package install, CLI/MCP adapter, public sync, push or deployment is authorized. The future three-repo pilot is not dispatched by this packet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private internal admission implementation and review; no public export.
