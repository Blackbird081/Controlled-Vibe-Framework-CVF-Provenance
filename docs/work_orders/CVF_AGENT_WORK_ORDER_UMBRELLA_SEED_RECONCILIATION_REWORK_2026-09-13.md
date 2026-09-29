# CVF Agent Work Order - Umbrella Seed And Historical Obligation Reconciliation

Memory class: governed-work-order
docType: work_order
Status: DISPATCH_READY
Date: 2026-09-13
Batch ID: UMBRELLA-SEED-RECONCILIATION-T1-REWORK-1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: 087234a8df215f740940c99e31b6621de892129d
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT evidence-repair worker; same workspace, operator relay.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md.
Paired authority: docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md.
Commit mode: WORKER_MUST_NOT_COMMIT. executionBaseHead: WORKER_MUST_CAPTURE_AT_START.
Required first actions: startup, this pair, consolidated F1-F4 review docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md; capture actual HEAD/status and pre-implementation.
Current-time notes: 2026-09-13; capture actual UTC start/end.
Do-not-misread notes: one REWORK of existing metadata evidence; no next-source intake.
Return contract: repair docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json; create docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_WORKER_RETURN_2026-09-13.md; preserve docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md unchanged; COMPLETE_PENDING_REVIEW with F1-F4 self-proof and gates, or precise blocker.

## Purpose

Repair all F1-F4 at docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md in one consolidated generation. Reuse valid membership and joins; complete required Local evidence/dispositions and produce an evidence-supported material next nomination. No new source intake or implementation.

## Authority Chain

Operator standing autonomous mandate -> original work order docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_2026-09-13.md -> consolidated reviewer decision docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md -> paired rework baseline docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md -> this packet. Original return remains immutable evidence. New packet repairs the same umbrella metadata task; old three-repo stopped chain remains distinct and unchanged.

## Agent Roles

Local owns dispatch, independent review, commit and continuity. Worker owns only the two output files. External agent findings are advisory; no new external research invocation.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "UMBRELLA-SEED-RECONCILIATION-T1-REWORK-1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md",
    "docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md",
    "docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json",
    "docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_WORKER_RETURN_2026-09-13.md",
    "docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json",
    "docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_COMPLETION_2026-09-13.md",
    "CVF_SESSION/",
    "CVF_SESSION_MEMORY.md",
    "AGENT_HANDOFF_V60_2026-09-08.md",
    "docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md",
    "docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_WORKER_RETURN_2026-09-13.md"
  ],
  "claims": [
    "Historical metadata reconciliation only"
  ],
  "requiredProof": [
    "Input hashes",
    "54 unique seed IDs and 68 unique obligation IDs",
    "Scoped Local acceptance evidence",
    "Unresolved and next-action accounting"
  ],
  "operatorCheckpoints": [
    "Separate implementation and acquisition authority"
  ],
  "forbiddenEffects": [
    "Worker commit",
    "Source execution",
    "Network",
    "Provider calls",
    "Public writes"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": "docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json",
    "completenessClaimChanged": false
  }
}
```

## Scope / Target / Owner Boundary

Allowed: read the seven exact local inputs in docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json; inspect ZIP entries as data without extracting/executing the validator; targeted governed acceptance lookup under docs/ and CVF_SESSION/state/entries. Source mirrors/INDEX are discovery pointers only.
Worker writes only docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json and docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_WORKER_RETURN_2026-09-13.md.
Forbidden: all other writes, staging, commit, source-mirror mutation, full
upstream semantic scan, network/fetch/clone, credentials, provider/live/public/deploy.
Local closure may additionally write docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_COMPLETION_2026-09-13.md, this pair and the baseline's exact continuity paths.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Original required evidence | docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_2026-09-13.md | Execution Plan and Acceptance Criteria | metadata dispositions and joins | Existing dispatch | ACCEPT |
| Consolidated F1-F4 | docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md | Findings / Position | Finding digest 5869948b2b1c860f0675658d45a58ff90a8e30392704eeb08b39ace8cc6ec237 | Local reviewer | ACCEPT |
| Receipt-bound input | docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json | sourceRecords and historicalObligationRows | Exact decoded strings | Provenance receipt | ACCEPT |
| MCP source binding | docs/audits/CVF_MCP_KAR_T0_ABSORPTION_AUDIT_2026-08-23.md | line 208 | official URL / exact pin | Existing MCP intake | ACCEPT |

## Input Identity And Evidence Boundaries

The receipt binds ZIP SHA256 66d47f56c92bdd747ed0294fdc00d7d8d2fcc69bc0a0b1e4e92b71b33b7bc795 and seven matching member digests.
Seed records have 54 unique IDs, 40 Git locator rows but 39 distinct URL strings;
the two ECC-related IDs must not be silently merged. Fourteen rows are non-Git
or unresolved. Seed remains SEED_ONLY_NOT_FRESHNESS_AUTHORITY.
The standalone backlog has 68 unique IDs, including three XD-prefixed IDs.
Its SHA256 is 2ac5d5432c14fb58d697a3f28899a43ec6d90a82aa11ff1a4597573cc8dcbae0.
That standalone file is not bound by the ZIP manifest: record provenance as
operator-local historical candidate until cross-links corroborate it. Five domain
ledgers were hash-read, not semantically reviewed by dispatcher. Do not inherit
external NOT_STARTED as Local status. Preserve raw historical artifacts unchanged.

## Required First Reads

AGENTS.md startup surfaces; this work order and docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md; docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json; six-mirror triage; applicable worker-return checker sources.

## Pre-Flight Checks

Capture HEAD/branch and git status including untracked files. Verify currentAuthority matches this committed pair; stop on another active worker or unexpected worktree changes. Verify exact input hashes and run pre-implementation before writing outputs.

## Write Ownership

Allowed scope: docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json; docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_WORKER_RETURN_2026-09-13.md.
Worker must not edit authority, receipt, SOT, prior recovery artifacts, mirrors or external files.
Local owns docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_COMPLETION_2026-09-13.md and paired continuity. No concurrent mutation while worker lane is active.

## Execution Plan

1. Read the F1-F4 finding set at docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md; verify digest 5869948b2b1c860f0675658d45a58ff90a8e30392704eeb08b39ace8cc6ec237.
2. Repair receipt-bound values and prove all-field equality; preserve original IDs/rows. Do not recreate valid joins without a named contradiction.
3. Complete per-source and per-obligation dispositions, actual bounded canonical lookup evidence, hashes and many-to-many provenance as already required by the original contract. Group searches are allowed with explicit covered IDs; no fabricated absence.
4. Consume reviewer MCP identity evidence; correct ECC mechanisms/corroboration, scope negative claims, and select a real remaining-value nomination. No separate packet for a basic lookup already in scope.
5. Reconcile read-depth/value/unknown counts and the chain to THIS work order's exact hash. Worker cannot self-accept resolution; derive counters and escalation honestly. Preserve original return unchanged.
6. Run focused F1-F4 checks and worker-return fast; return new self-proof with exact audit hash, actual changed set and Local-owned next action.

## Evidence Requirements

Audit JSON must contain executionBaseHead, inputHashes, sourceRows,
historicalObligationRows, joinEdges, localEvidence, searchLedger, reconciliation,
nextCandidates and programContinuation. Each unresolved search records scope,
query and result; absence within a search is not global absence. Every input row
has one metadata disposition, and every join references existing IDs.
Keep 54 source records separate from 68 obligation records and 39 unique URLs.
Record which files were fully read, section-read, metadata-only or hash-only.
The return cites docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json, actual changed set, gates, dates and no-commit status.

## Acceptance Criteria

All original metadata criteria plus all F1-F4 check clauses pass. 54 source and 68 obligation rows each have one allowed metadata state and evidence/search links. Unknown value is not NO_NEW_VALUE. Reviewer acceptance and SCEC resolution may not be self-issued. Original return unchanged; exact two owned outputs. Any outside-scope need is returned to Local.

## Review Gate
Local accepts the source-identification, ownership and initial-metadata reconciliation design.
Pre-dispatch PASS is required before worker lane transfer. Worker returns
COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON, never closure or a commit.
Reviewer consumes evidence by capability cluster under MFRP M5/M10/safety/M20;
EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Reruns require a named
contradiction, expected information gain and cost reason. Selected absorption
requires a separate reviewed work order; no automatic successor.

## Gate-To-Role Closeability Contract
closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET
returnTimeRecheck: REQUIRED_BEFORE_REPAIR

This is the released lifecycle graph for the bounded metadata reconciliation. Mandatory
gate IDs follow `docs/reference/CVF_GATE_TO_ROLE_CLOSEABILITY_MACHINE_STANDARD.md`.
Protected continuity remains Local-only under the paired authorization; worker cannot amend it.

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | this packet and paired baseline | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | same frozen authorization packet; release dependency table | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V60_2026-09-08.md material-SHA marker plus paired baseline exact seven Local continuity paths and currentAuthority fingerprints | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | frozen Write Ownership only; outside-scope failure returns to Local | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_identity_license | WORKER_RETURN | worker | IMPLEMENTATION | two evidence outputs; read-only input identity; step 1 | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| inventory_depth_value | WORKER_RETURN | worker | IMPLEMENTATION | two evidence outputs; steps 2-4 | EXACT_PATHS | closer | MATERIAL_COMMIT | source_identity_license |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | two evidence outputs; focused manifest/hash/reconciliation validation, no upstream tests | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, inventory_depth_value |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure only; no ADIF owner mutation | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | two evidence outputs; step 6 | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | released material paths and reviewer disposition in return | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact reviewed material set | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local-only completionReviewPath and disposition in named return | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | paired baseline exact Local continuity authorization | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact reviewed material set; corrective material only within released authority | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Pre-implementation must pass before any steps 1-6 evidence mutation.
Inventory hashes and semantic depth are different proofs. Terminal review and
material commit precede dedicated continuity; clean split-range closure follows
continuity. No future commit SHA is guessed. Every return rechecks blockers
before repair; unknown ownership forbids worker redispatch.

## Review Dispatch Convergence And Invocation Budget Control
Review-Dispatch Convergence Control: REQUIRED
dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: UMBRELLA-SEED-RECONCILIATION-T1
reviewRoundCount: 1
priorFindingSetDigest: 5869948b2b1c860f0675658d45a58ff90a8e30392704eeb08b39ace8cc6ec237
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: UMBRELLA-SEED-EVIDENCE-INTEGRITY
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

Initial dispatch contract reviewed; worker operates autonomously inside its exact scope.

## Verification Commands
Local pre-dispatch:
`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch`.
Worker before mutation:
`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`.
Worker return:
`python governance/compat/run_worker_return_fast_gate.py`.
`git diff --check` and `git status --short --untracked-files=all`.
Focused proof is deterministic ID/hash/join/ledger reconciliation;
no upstream tests or AI governance runtime claims. Full legacy bundles remain
mandatory. Local commits accepted material then separate continuity, and runs
clean committed-range pre-closure separately for each range.

## Closure Checklist
- Local accepts a bounded metadata reconciliation only after its required evidence and gates.
- Worker leaves evidence uncommitted; reviewer owns acceptance and closer owns commit.
- Continuity changes, if authorized, are separate from material evidence commits.
- Selected absorption and any implementation require a separate reviewed work order.

## Return-To-Orchestrator Conditions

Return COMPLETE_PENDING_REVIEW with final evidence and gate results, or BLOCKED_WITH_REASON with an exact unowned blocker. Missing source-specific acceptance does not block independent joins; input hash mismatch blocks only use of that input. Do not ask the operator for routine read order or say next.

## Dual Agent Surface Matrix
| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | This historical metadata contract | Same-workspace, no worker commit; initial metadata reconciliation only | Operator request and active next move | N/A with reason: document-only intake contract | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | Existing external nomination input | Advisory only; no new call | Domain-funnel method | No CLI/MCP adapter or execution release | DEFERRED_WITH_REASON |

## Evidence Reuse And Encoding Plan
verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: docs/reviews/CVF_MULTI_REPO_ACCEPTANCE_HISTORY_TRIAGE_2026-09-13.md
priorVerificationAnchor: 4899ce2e947968b6615005e3827bace5d47182e1; reuse only scoped acceptance facts
freshRecomputeRequired: exact input hashes and selected Local acceptance evidence; no upstream freshness action
unicodePathHandling: literal paths and UTF-8-safe readers; preserve Windows path spelling
extractedTextAuthority: exact external bytes control historical membership; governed Local acceptance controls CVF status

## Checker Source Read-Ahead Block
| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| conditionalTriggersReviewed | work_order structure, active dispatch lifecycle, historical metadata versus current acceptance |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; PARTIAL; required work_order heading families |
| gateRunPurpose | Confirmation and evidence of the prepared document; not first discovery or source certification |
| claimBoundary | Document read-ahead only; no runtime or source-value claim |
| disposition | Source and contract review complete; pre-dispatch governs worker release |

## Agent Handoff Contract Control Block
Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local author/reviewer/closer; internal worker |
| phase | initial metadata reconciliation then independent review |
| baseHeadFor(phase) | preparation anchor f5bfdffdda4041ce7277026b3ec83dae89eff43d; worker captures execution HEAD at start |
| changedSetScope(phase) | Two dispatch-document paths in current trace; worker two output paths |
| traceScope(phase, actor) | Exact command, hash and changed-set evidence |
| commitOwner(phase) | Local closer; worker forbidden |
| crossBatchIsolation | No active metadata worker; no concurrent mutation |
| nextMoveSurfaces | This packet and baseline; independent release review before intake |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: internal metadata worker after committed dispatch and continuity
laneOwnedPaths: exactly the two tracked worker output paths; mirrors read-only
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return and exact changed-set reconciliation

## Reviewer Closure Conversion
| Field | Value |
|---|---|
| completionReviewPath | docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_COMPLETION_2026-09-13.md (Local reviewer only; create at return) |
| reviewerOwnedClosurePaths | Exact two worker outputs, named completionReviewPath, this work order and paired baseline; continuity is separately authorized |
| closureOwner | Local reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## ADIF Defect Registry Disclosure
Resolver query: taskClass=`external-absorption`, role=`reviewer`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption --role reviewer --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.
Returned defect count: 0. Returned defects: NONE_RETURNED.
Disclosed defectIds: none. Truncated: false.
Disposition: no matching registry item; mandatory guards still apply.

## Worker Autonomy / No-Question Rule
Repair gate failures inside Allowed scope and rerun. Do not ask for preference on routine evidence formatting. Return precise outside-scope blockers to Local; do not expand authority.

## Architecture Readiness Admission
Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON
Reason: internal source metadata reconciliation only; no external invocation or runtime integration.

## Worker Return Packet Shape Contract
workerReturnPath: docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_WORKER_RETURN_2026-09-13.md
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Commit Mode And Base-Anchor Lifecycle
dispatchBaseHead: 087234a8df215f740940c99e31b6621de892129d
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: N/A - pending review
Commit mode: WORKER_MUST_NOT_COMMIT
Worker Pending-Return Gate: worker-return fast PASS on final owned evidence; committed-range pre-closure is Local-owned after material and continuity commits.

## Commit Prompt Readiness
Worker must not stage/commit. Local closer alone commits reviewed material and separate continuity; no push.

## Epistemic Process Block

Expected Result / Prediction: external historical NOT_STARTED rows may already have scoped Local acceptance.
Evidence Comparison: join exact input rows to canonical acceptance and retain mismatches.
Contradiction Or Gap Disposition: unresolved identity/pin/owner remains explicit.
Claim Update: metadata reconciliation only; no current source or implementation proof.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/dispatcher |
| Provider or surface | internal workspace |
| Session or invocation | umbrella-seed-review-20260913 |
| Working directory | private provenance root |
| Command or tool surface | targeted JSON comparisons and canonical reads, reviewer-return preflight |
| Target paths | docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md; docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md |
| Allowed scope source | Original Reviewer Closure Conversion and standing operator mandate |
| Before status evidence | HEAD 087234a8df215f740940c99e31b6621de892129d; worktree clean after review continuity commit; original two outputs are now committed historical evidence |
| After status evidence | Two rework dispatch paths; no worker repair yet |
| Diff evidence | git status --short --untracked-files=all |
| Approval boundary | Consolidated internal evidence repair only |
| Claim boundary | No absorption, runtime or public acceptance |
| Agent type | reviewer/dispatcher |
| Invocation ID | umbrella-seed-review-20260913 |
| Expected manifest | docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md; docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md |
| Actual changed set | docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md; docs/baselines/CVF_GC018_UMBRELLA_SEED_RECONCILIATION_REWORK_2026-09-13.md |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block
| Field | Disposition |
|---|---|
| claimScope | Intake work-order preparation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no source intake executed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: paired draft documents and isolated material-range gate evidence |
| invocationBoundary | Local governed document authoring |
| interceptionBoundary | No process, filesystem, Git or provider interception claim |
| claimLanguage | Defines metadata joins and evidence requirements |
| forbiddenExpansion | No source acceptance, implementation, provider/live/public/deployment |

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: historical metadata and acceptance lookup only; no source-code intake. Input identity is bound by the local receipt. Enumeration is 54 seed and 68 backlog records; read-depth remains separate from membership. Existing domain-funnel method owns future value conversion. No external script execution.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external-agent returned output |
| Chain map route | historical metadata comparison then Local nomination review |
| Matching local-view guard | governance/compat/check_task_governance_route.py |
| Owner surface | docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md |
| Disposition | COMPARISON_ONLY_NO_ABSORPTION |
| Claim boundary | No source execution or value conversion in this dispatch |

## Overlap And Novelty Classification

CONFIRMED_EXISTING: reuse existing domain-funnel and acceptance owners. New payload availability enables historical joins; no new architecture or source-value decision.

## Mandatory Blind-Spot Control Block

Audit unknown/deferred groups by domain and scoped acceptance. Do not mark whole source complete from one child closure, merge ECC source IDs by URL, omit three XD obligations, or equate file enumeration with semantic review. No whole-source scan is authorized.

## Corpus Completeness And Report Integrity

- Corpus task class: metadata reconciliation preparation.
- Corpus root: exact inputs listed in docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json.
- Snapshot time: receipt checkedAtUtc.
- Enumeration command: filesystem-backed direct file reads and ZIP member listing.
- Manifest artifact or inline manifest: receipt inputs and packageEntries.
- Manifest hash: per-input SHA256 values in receipt; no aggregate corpus claim.
- Processing ledger artifact or inline ledger: receipt readDepth; worker audit planned.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=7; ledger_terminal=2; exclusions=0; unresolved=5 for local input processing: ZIP/backlog metadata parsed, five domain ledgers hash-only pending semantic read. 54 source IDs, 68 historical obligation IDs, seven local input files; different units never added. Source semantic corpus is excluded.
- Unresolved files: 5 domain-ledger content reads; semantic Local mappings are worker work.
- Declared exclusions: current upstream source contents, network freshness and runtime.
- Unreadable or unsupported files: none encountered during metadata reads.
- Aggregation check: unique IDs independently parsed; current disposition pending.
- Drift check: rehash before and after worker reads.
- Output traceability: receipt to planned audit and return.
- Adversarial verification: membership does not imply absorption.
- Corpus verdict: PARTIAL - metadata preparation only.

## Knowledge System Reconciliation

- Knowledge task class: Historical metadata join planning
- Source manifest: docs/audits/CVF_UMBRELLA_SEED_PROVENANCE_RECEIPT_2026-09-13.json
- Source manifest hash: Per-input hashes in receipt; aggregate not claimed
- Enumeration safety: filesystem-backed direct file reads; no source execution
- Intake registry or ledger: Receipt sourceRecords and historicalObligationRows; worker audit pending
- Authority assets: AGENTS.md and existing Local acceptance review owners
- Derived views: Planned worker audit only
- Semantic region ledger: Not produced; metadata IDs are not source semantic regions
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0 for semantic regions processed by dispatcher; 54 source IDs and 68 obligation IDs to join separately
- Orphan or unmapped assets: Local mappings unresolved until worker return
- Cross-region links: Future many-to-many joins by preserved IDs
- Drift check: Rehash all inputs before and after worker reads
- Rebuildability check: Exact input hashes and queries in worker audit
- Retrieval boundary: Historical metadata only; no runtime knowledge retrieval
- Adversarial verification: Reject whole-source completion inferred from child acceptance
- Knowledge-map verdict: PARTIAL

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json | Yes | Historical joins and next nomination |
| docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_REWORK_WORKER_RETURN_2026-09-13.md | Yes | Pending worker evidence |

## Work-Order Fulfillment Manifest

Exact two worker outputs in Required Artifact Manifest; all input and authority paths read-only. Required Proof Manifest Atomic Literal Discipline: proof tokens are individual assertions, not bundled status substitutions.
rawMemoryReleased=false

## Operator Checkpoint

Routine metadata work proceeds autonomously within this packet. Implementation, acquisition, network research and source execution need a separate reviewed packet. No request for the operator to remember the next repository.

## Program Continuation

Local owns acceptance and next packet in the same review cycle. This task must produce usable source/obligation membership and a supported nomination; it must not restart the stopped three-repo scan. Existing six-mirror acceptance is reused. Historical external seed is neither exhaustive current inventory nor current upstream authority; fresh source/version work is separately scoped after nomination.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "umbrella-seed-membership-reconciliation",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/work_orders/CVF_AGENT_WORK_ORDER_UMBRELLA_SEED_RECONCILIATION_2026-09-13.md",
    "sha256": "fbff5bb507c9fd7ede808235d255587764ef107a3a94902058a91126d6524c21"
  },
  "blockerDelta": {
    "prior": [
      "historical-membership-acceptance-joins-unverified"
    ],
    "resolved": [],
    "retained": [
      "historical-membership-acceptance-joins-unverified"
    ],
    "new": [
      "receipt-string-fidelity",
      "per-row-local-evidence",
      "nomination-and-read-depth-integrity"
    ],
    "reopened": [],
    "current": [
      "historical-membership-acceptance-joins-unverified",
      "receipt-string-fidelity",
      "per-row-local-evidence",
      "nomination-and-read-depth-integrity"
    ]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 1
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

Predecessor is the original governing dispatch, not the worker INITIAL echo. One real successor generation, no blocker resolution claimed. Worker return must bind this rework packet and derive the next counters; original three-repo chain remains stopped and separate.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id UMBRELLA-SEED-RECONCILIATION-T1 --title "Umbrella Seed Provenance And Historical Obligation Reconciliation" --date 2026-09-13 --base f5bfdffdda4041ce7277026b3ec83dae89eff43d --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Adapted existing intake lifecycle after generating the generic-worker-dispatch scaffold; replaced source, ownership, evidence and continuation contracts |
| checkerReadAheadConfirmation | Source shape, gate-to-role, lifecycle, intake, routing and handoff requirements reviewed |
| docOnlyNewFields | Doc-only provenance receipt fields; no runtime schema authority |
| claimBoundary | Generation provenance only; no source-read or runtime claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY: private provenance metadata only; no public export.

## Claim Boundary

Local historical reconciliation preparation only. No source freshness, current global backlog closure, runtime, provider, live, public, deployment, whole-repository completion or implementation authority.


## Foundation Storage Layout Block

Use existing docs/baselines, docs/work_orders, docs/audits and docs/reviews
families; no new foundation owner or folder. Existing source-mirror INDEX
remains the control-plane owner. No layout migration or registry split.


## Intake Role Routing Decision

Intake summary: bounded historical metadata reconciliation.
Route mode: MULTI_AGENT_MULTI_ROLE.
Risk sensitivity: P3_ELEVATED source provenance; internal worker, Local reviewer.
Scope classification: initial evidence only.
Escalation condition: forbidden effect or unowned repair.


## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: historical metadata only; no legacy payload conversion or coverage-index closure.

## Review Cost And Evidence Reuse

Worker budget: one consolidated metadata pass, up to 120 minutes; report unknowns with exact searches instead of extending into source scans. Local review uses M5/M10/safety/M20 and EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Any repeated read or rerun must name contradiction, information gain and cost. Budget is a ceiling, not an instruction to consume it.

## Consolidated Draft Review Disposition

REWORK generation 1; root cluster UMBRELLA-SEED-EVIDENCE-INTEGRITY. Contract/schema/path/authority/string fidelity/hash/trace/semantic nomination/lifecycle audit completed before repair. Single F1-F4 set at docs/reviews/CVF_UMBRELLA_SEED_RECONCILIATION_COMPLETION_2026-09-13.md; digest 5869948b2b1c860f0675658d45a58ff90a8e30392704eeb08b39ace8cc6ec237. Regression checks are the check clauses; no drip redispatch.

Metadata-only output contract: Required Artifact Manifest is binding for the next worker return. Existing audit was preserved as rejected historical evidence in prior review commit 82bd8cd882266c3b580974cd41ef46ce35d0799e, not produced by the new repair worker. No delegated runtime/source implementation is in scope.

Review material anchor: 82bd8cd882266c3b580974cd41ef46ce35d0799e. Reviewer decision F1-F4 is committed before this dispatch. Final original-return packaging hash is in that review; worker preserves it unchanged.
