# CVF Agent Work Order - ECC Cross-Harness Adapter Profile Intake

Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Date: 2026-09-15
Batch ID: ECC-ARCH-ABS-009-T0
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: f8fc0810c5f57bc3d475f9c6f0f1584008709a3c
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: N/A - pending worker return
providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: internal same-workspace source-intake worker; operator relay recipient is Claude.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ECC_ARCH_ABS_009_T0_2026-09-15.md`.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: WORKER_MUST_CAPTURE_AT_START.
Current-time notes: 2026-09-15; use the exact local pins below, not a moving branch.
Do-not-misread notes: evidence survey only; no code import, runtime adapter, hook work, WP-ARCH-006, provider/live or public action.
Required first actions: read startup/bootstrap/active handoff, guard orientation, literal gotchas, paired baseline, this packet and output checkers; capture full HEAD/status; verify dispatch ancestry; run pre-implementation before writing.
Return contract: create exactly the two owned outputs, run worker-return fast, leave all work uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Determine whether the pinned ECC fork/upstream pair contains independently
useful host-neutral adapter/profile semantics for `ARCH-F-023`, without
recreating current CVF owners or crossing the parked architecture boundary.

## Authority Chain And Roles

Operator continuation instruction -> AGENTS.md -> paired GC-018 -> this work
order -> external absorption/domain-funnel owners. Local is dispatcher,
reviewer, closer, decision owner and continuity steward. Claude is an
`INTERNAL_AGENT` worker because it operates in the shared private workspace.
External research is advisory only and has no role in this execution.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "ECC-ARCH-ABS-009-T0",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "EXTERNAL_ABSORPTION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [
    "docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json",
    "docs/reviews/CVF_ECC_ARCH_ABS_009_T0_WORKER_RETURN_2026-09-15.md",
    ".private_reference/source_mirrors/Blackbird081__everything-claude-code/",
    ".private_reference/source_mirrors/affaan-m__ECC/",
    "docs/baselines/CVF_GC018_ECC_ARCH_ABS_009_T0_2026-09-15.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_ECC_ARCH_ABS_009_T0_2026-09-15.md",
    "AGENT_HANDOFF_V60_2026-09-08.md"
  ],
  "claims": ["Initial source survey only; no absorption acceptance"],
  "requiredProof": ["Immutable source pins", "Terminal corpus ledger", "Fork/upstream delta", "Current-owner collision map"],
  "operatorCheckpoints": ["Local review before any successor"],
  "forbiddenEffects": ["Provider calls", "Upstream execution", "Dependency installation", "Runtime implementation", "Public writes", "Source import", "Worker commit"],
  "sourceEvidence": {"selectedFilesFullyRead": false, "corpusReceiptRef": null, "completenessClaimChanged": false},
  "initialIntakeAdmission": {
    "stage": "INITIAL_ACQUISITION_SURVEY",
    "plannedReceiptPath": "docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json",
    "acceptanceDisposition": "NO_ABSORPTION_ACCEPTANCE",
    "nextStageAuthority": "SEPARATE_REVIEWED_WORK_ORDER",
    "unknownEvidencePolicy": "PRESERVE_UNKNOWN"
  }
}
```

Routing metadata cannot release effects forbidden elsewhere in this packet.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "ecc-arch-abs-009-t0",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": ["wp-arch-003-parked"], "resolved": [],
    "retained": ["wp-arch-003-parked"],
    "new": ["bounded-ecc-source-evidence"],
    "reopened": [],
    "current": ["wp-arch-003-parked", "bounded-ecc-source-evidence"]
  },
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, bootstrap read model, named active handoff, this
packet, paired baseline, `docs/reference/guard_orientation/README.md`, literal
gotchas, domain-funnel method, external absorption chain/core standards,
corpus completeness/reconciliation standards, mirror README/INDEX, umbrella
reconciliation rows for `SKILL-SRC-004`/`ARCH-ABS-009`, three-repo Local review,
and WP-ARCH-003 parked roadmap. Do not read full session history by default.

## Source Identity And Frozen Pins

| sourceId | role | URL | local mirror | frozen commit | tree | tracked files |
|---|---|---|---|---|---|---:|
| SKILL-SRC-004 | primary historical fork | `https://github.com/Blackbird081/everything-claude-code` | `.private_reference/source_mirrors/Blackbird081__everything-claude-code/` | `5064474d4d762dc9640234a41617cccb79185cec` | `9d448bb479cc1af55c488357556ac24d8cd932d2` | 3538 |
| ECC-UPSTREAM | canonical upstream comparator | `https://github.com/affaan-m/ECC` | `.private_reference/source_mirrors/affaan-m__ECC/` | `8321021c54d670126ce3b2969d5deb880b4b0c2a` | `a7489fb4da00fc7b4995df3a3c59c018d08a3807` | 3716 |

Both root LICENSE blobs have SHA-256
`326146379f01bb137c0a5d3c54770c1aa31076705c8b88a7f6b26a460f6221b2`
and identify MIT. This is inspection evidence, not legal clearance. Preserve
the two identities and never silently substitute upstream for fork evidence.

## Upstream Freshness Preflight

```json
[
  {
    "schemaVersion": "cvf.upstream-freshness.v1",
    "sourceUrl": "https://github.com/Blackbird081/everything-claude-code.git",
    "observedAt": "2026-09-15T02:26:32.8510192Z",
    "manifestFrozenAt": "2026-09-15T02:26:32.8510192Z",
    "defaultBranch": "refs/heads/main",
    "observedHead": "5064474d4d762dc9640234a41617cccb79185cec",
    "selectedPin": "5064474d4d762dc9640234a41617cccb79185cec",
    "previousPin": "5064474d4d762dc9640234a41617cccb79185cec",
    "selectionReason": "Use the immutable fork identity nominated by SKILL-SRC-004.",
    "deltaSummary": "Observed HEAD equals the selected pin.",
    "lsRemoteOutput": "ref: refs/heads/main\tHEAD\n5064474d4d762dc9640234a41617cccb79185cec\tHEAD\n"
  },
  {
    "schemaVersion": "cvf.upstream-freshness.v1",
    "sourceUrl": "https://github.com/affaan-m/ECC.git",
    "observedAt": "2026-09-15T02:26:32.8510192Z",
    "manifestFrozenAt": "2026-09-15T02:26:32.8510192Z",
    "defaultBranch": "refs/heads/main",
    "observedHead": "8321021c54d670126ce3b2969d5deb880b4b0c2a",
    "selectedPin": "8321021c54d670126ce3b2969d5deb880b4b0c2a",
    "previousPin": "8321021c54d670126ce3b2969d5deb880b4b0c2a",
    "selectionReason": "Use the canonical upstream comparator without replacing fork evidence.",
    "deltaSummary": "Observed HEAD equals the selected pin.",
    "lsRemoteOutput": "ref: refs/heads/main\tHEAD\n8321021c54d670126ce3b2969d5deb880b4b0c2a\tHEAD\n"
  }
]
```

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_THREE_REPO_PATTERN_COMPARISON_LOCAL_REVIEW_2026-09-13.md"
}
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Local nominated ARCH-ABS-009 next after rejecting duplicate MCP acquisition | `docs/reviews/CVF_THREE_REPO_PATTERN_COMPARISON_LOCAL_REVIEW_2026-09-13.md` | Selection result / Next Local action | lines 114-124 | Local comparison review | ACCEPT |
| ARCH-F-023 is an unresolved high-confidence ADAPT hypothesis | `docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json` | nextCandidates | `SKILL-SRC-004`; `ARCH-ABS-009` | umbrella reconciliation | ACCEPT |
| ARCH-F-024 is not new scope | `docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json` | ECC next-candidate rationale | `ARCH-F-024` existing/no-change | umbrella reconciliation | ACCEPT |
| WP-ARCH-003 cannot support implementation | `docs/roadmaps/CVF_WP_ARCH_003_ROOT_AUTHORITY_AND_PRINCIPAL_SCOPE_ARCHITECTURE_REASSESSMENT_ROADMAP_2026-09-08.md` | Status / Decision | `PARK_NO_TRUTHFUL_AUTHORITY_ROOT` | RABA roadmap | ACCEPT |
| Exact mirror pins are locally indexed | `.private_reference/source_mirrors/INDEX.md` | two ECC rows | URLs, commits, trees, license hashes | source mirror index | ACCEPT |

## Negative Search And Collision Discipline

`Test-Path` returned false for this packet, paired baseline and planned return
before authoring. `rg -n "ECC-ARCH-ABS-009-T0|ECC Cross-Harness Adapter Profile
Intake" docs CVF_SESSION` returned no match. Broader ECC/ARCH-ABS-009 matches
are retained authority and backlog records; no existing accepted intake packet
or owner was replaced.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or backlog requirement | Work-order output | Verification |
|---|---|---|
| ARCH-ABS-009 / ARCH-F-023 independent admission | intake JSON and worker return | exact candidate/source join |
| preserve two ECC identities | source and delta matrices | independent pins and ledgers |
| exclude ARCH-F-024 | exclusions and candidate matrix | zero hook candidate |
| keep WP-ARCH-003 parked | claim boundary and stop conditions | zero runtime/architecture mutation |

## Intake Role Routing Decision

Intake summary: two-source bounded semantic survey. Route mode:
`MULTI_AGENT_MULTI_ROLE`; Claude is the internal worker and Local is the later
reviewer/closer. Risk sensitivity: P3 evidence work in a private repository.
Escalate only a source contradiction, forbidden effect or missing authority.

Escalation condition: source contradiction, forbidden effect, missing authority,
or a gate failure whose repair lies outside Write Ownership.

## Worker Autonomy / No-Question Rule

Repair allowed-scope evidence and formatting failures directly after reading
the failing checker. Do not ask about routine presentation choices. Return an
exact blocker instead of widening scope.

## Write Ownership

Worker owns exactly two create-only tracked paths:

- `docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json`
- `docs/reviews/CVF_ECC_ARCH_ABS_009_T0_WORKER_RETURN_2026-09-15.md`

Both mirror roots and all other repository paths are read-only. Local alone
may amend the packet/baseline, review disposition, commit or continuity state.

## Execution Plan

1. Capture exact HEAD/status, prove `dispatchBaseHead` ancestry, verify both
   mirror commits/trees/cleanliness and run pre-implementation.
2. Enumerate each frozen tree deterministically with `git ls-tree -r`; reconcile
   the stated totals and classify `.git`, generated, vendor and binary exclusions.
3. Produce a terminal per-path ledger. Perform bounded semantic reading focused
   on profiles, adapters, harness abstraction, configuration/command mapping,
   skill portability, tests/examples and their consumers/failure paths.
4. Produce explicit shared/fork-only/upstream-only deltas. Do not infer sameness
   from repository ancestry or count only path names as semantic evidence.
5. Map every plausible mechanism against existing CVF ASSF/package, CLI, MCP,
   profile and harness owners. Record producer, verifier, non-test consumer,
   missing link, operational benefit and collision evidence.
6. Assign each atomic candidate exactly one advisory disposition: `ADAPT`,
   `DEFER`, or `NO_NEW_VALUE`. Exclude hooks/installer layout/Claude-specific
   coupling and retain unknowns honestly.
7. Complete both outputs, run the required worker-return gate, verify HEAD is
   unchanged and return to Local without staging or committing.

Budget: 90 minutes total; at most 30 semantically read files per source plus
owner evidence needed for collision checks. Stop when the decision is supported
or the budget is exhausted; record all unread regions. No automatic second pass.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json` | create machine-readable identities, manifests, terminal ledger, read-depth, delta, owner/candidate and reconciliation evidence |
| `docs/reviews/CVF_ECC_ARCH_ABS_009_T0_WORKER_RETURN_2026-09-15.md` | create human review packet with status, findings, risks, commands, exact changed set and no-commit proof |

JSON must include `schemaVersion`, `taskId`, `executionBaseHead`, `sources`,
`manifest`, `processingLedger`, `reconciliation`, `semanticReads`, `deltaMatrix`,
`ownerCollisionMatrix`, `candidates`, `exclusions`, `unknowns`, `gateEvidence`
and `claimBoundary`. Counts must be derived from arrays, not prose.

## Acceptance And Stop Conditions

Accept the return only when both identities and pins reconcile; manifest equals
terminal ledger plus declared exclusions; mapped/deferred/unmapped totals
reconcile; each conclusion cites exact pin/path/symbol and actual read depth;
current-owner searches are bounded and reproducible; no candidate depends on
ARCH-F-024 or the parked authority root; exact changed set is two files; gates
pass; HEAD is unchanged.

Stop with `BLOCKED_WITH_REASON` on identity/pin/tree mismatch, dirty mirror,
unreadable required source, packet contradiction, forbidden mutation need,
failed outside-authority gate, or inability to produce truthful reconciliation.
One source blocker does not authorize identity substitution.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ECC_ARCH_ABS_009_T0_WORKER_RETURN_2026-09-15.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Public Export Disposition; Return-Time
Closeability Recheck; executionBaseHead; git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Knowledge System
Reconciliation; Finding-To-Governance Learning Disposition; Epistemic Process
Block; Machine Closure Package. Use `N/A with reason` only where truthful.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED
dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ECC-ARCH-ABS-009-T0
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
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | this packet and paired baseline | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | frozen packet and baseline | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V60_2026-09-08.md material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | frozen Write Ownership only | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_identity_license | WORKER_RETURN | worker | IMPLEMENTATION | two worker outputs; source identity evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| inventory_depth_value | WORKER_RETURN | worker | IMPLEMENTATION | two worker outputs; inventory and value evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | source_identity_license |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | two worker outputs; deterministic validation | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, inventory_depth_value |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure only | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact reviewed material set | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact reviewed material set | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer disposition in worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | paired baseline Local continuity authorization | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | exact reviewed material set | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: Local until committed dispatch continuity; then worker until pending return

laneOwnedPaths: exact two create-only paths in Write Ownership

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: committed packet plus continuity SHA; worker verifies clean state before accepting lane

beforeStatusEvidence: clean worktree at HEAD `f8fc0810c5f57bc3d475f9c6f0f1584008709a3c`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | internal intake worker returns evidence; Local separately reviews/closes |
| phase | WORKER_EXECUTION_AND_RETURN |
| baseHeadFor(phase) | dispatchBaseHead above; worker captures executionBaseHead; reviewer sets closureBaseHead |
| changedSetScope(phase) | exactly two create-only outputs |
| traceScope(phase, actor) | worker records commands, pins, status and manifest delta |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local closer owns commits |
| crossBatchIsolation | no unrelated changes; stop on pre-existing dirty state |
| nextMoveSurfaces | worker return to Local only; no successor dispatch |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_ECC_ARCH_ABS_009_T0_COMPLETION_REVIEW_2026-09-15.md`

reviewerOwnedClosurePaths: completion review, worker outputs, packet status and explicitly authorized continuity only.

closureOwner: Local reviewer/closer

workerCommitPermission: FORBIDDEN

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
git merge-base --is-ancestor f8fc0810c5f57bc3d475f9c6f0f1584008709a3c HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short
```

Do not run upstream commands, package managers, hooks, tests, scripts, CLIs or
MCP servers. Reading Git objects and text files is allowed.

## Source-Intake Decision Packet Fields

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Negative search performed | exact packet and owner collision searches required |
| Disposition | worker advisory ADAPT/DEFER/NO_NEW_VALUE; Local final decision |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned local source -> internal survey -> Local disposition |
| Matching local-view guard | `governance/compat/check_task_governance_route.py` |
| Owner surface | domain-funnel absorption method |
| Disposition | INITIAL_EVIDENCE_COLLECTION_ONLY |
| Claim boundary | no absorption acceptance |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | the two exact mirrors and pins in this packet |
| Enumeration command | pinned `git ls-tree -r` per source |
| Manifest artifact or inline manifest | `docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json` planned output |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json` planned terminal ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md` plus planned ownerCollisionMatrix |
| Unresolved items | all source semantics before worker execution |
| Absorption maturity | NO_RUNTIME_VALUE_WITH_REASON |
| Named runtime consumer | N/A with reason: intake only |
| Integration evidence | N/A with reason: forbidden |
| Use proof | N/A with reason: upstream execution forbidden |
| Operator checkpoint | SATISFIED_FOR_INITIAL_SURVEY_ONLY |
| Absorption completion status | NO_RUNTIME_VALUE_WITH_REASON |
| Completion claim boundary | survey preparation only |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded source intake preparation.
- Corpus root: the two exact mirror roots and pins in Source Identity.
- Snapshot time: `2026-09-15T02:26:32.8510192Z`.
- Enumeration command: worker must use `rg --files --hidden --no-ignore` for filesystem evidence and reconcile with pinned `git ls-tree -r`.
- Manifest artifact or inline manifest: `docs/audits/CVF_ECC_ARCH_ABS_009_T0_INTAKE_2026-09-15.json`, planned and not yet produced.
- Manifest hash: NOT_PRODUCED at dispatch; worker must compute it.
- Processing ledger artifact or inline ledger: same planned JSON terminal ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=0; unresolved=0 for executed rows at dispatch; worker must replace with derived totals.
- Unresolved files: 0 executed rows; full source totals remain pending.
- Declared exclusions: Git metadata, binaries, generated/vendor payload only where evidenced.
- Unreadable or unsupported files: not assessed at dispatch; worker must list them.
- Aggregation check: pending worker output; required before return.
- Drift check: remote HEAD equals each selected pin at snapshot; worker rechecks local pins.
- Output traceability: planned JSON plus worker return.
- Adversarial verification: reject path-count-only semantic completeness and silent source merging.
- Corpus verdict: PARTIAL - preparation only; no completeness claim.

## Mandatory Blind-Spot Control Block

Worker must inspect operational value beyond the named hypothesis, while staying
within the bounded read budget, and explicitly record unread regions. Search
profiles, adapters, commands/configuration, tests/examples, consumers, failure
paths, fixtures and integration documentation. No whole-repo value conclusion
may be inferred from the external shortlist.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION

| Field | Value |
|---|---|
| Source type | two pinned external repository mirrors |
| Upstream or source-mirror disposition | read-only clean ignored mirrors at exact pins |
| Enumeration or manifest plan | filesystem plus Git-tree reconciliation in planned JSON |
| Per-file terminal-ledger plan | every manifest row receives one allowed terminal status |
| Owner or overlap route | existing CVF owner evidence plus Local review |
| Value-disposition route | worker advisory; Local decides ADAPT/DEFER/NO_NEW_VALUE |
| Claim boundary | no absorption acceptance, import or runtime conversion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| ARCH-F-023 hypothesis | unassessed | RUNTIME_CANDIDATE | current profile/harness owners | source survey | no runtime authority |
| ARCH-F-024 hooks | already existing | NO_PACKAGE_OR_RUNTIME_VALUE | existing hooks | exclude | no hook change |
| existing intake method | existing governance value | DOCTRINE_ADAPTED | domain-funnel method | reuse without new owner | no doctrine change |
| package possibility | unassessed | PACKAGE_CANDIDATE | ASSF package owners | classify only | no install/promotion |
| checker possibility | unassessed | CHECKER_CANDIDATE | governance checker owners | classify only | no checker mutation |
| foreign code | none selected | REJECT_DIRECT_IMPORT | existing intake boundary | pattern review only | no import |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| hook enforcement | `governance/compat/run_local_governance_hook_chain.py` | CONFIRMED_EXISTING | none admitted | exclude |
| adapter/profile semantics | `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md` | ENRICH_EXISTING | possible host-neutral portability, unverified until intake | inspect before final classification |

## Foundation Storage Layout Block

Use existing `docs/audits` and `docs/reviews` families only. No new foundation
folder, registry, runtime owner, index mutation, relocation or file split.

## Pre-Flight Checks

At dispatch authoring the worktree was clean at the full dispatch base, planned
paths were absent, mirrors were indexed at exact clean pins, and remote HEADs
were observed. Pre-dispatch must pass before relay. Worker recaptures the actual
execution base and stops on unrelated dirty state or ancestry failure.

## Evidence Requirements

Require exact pins, tree and license hashes; command/cwd/result/timestamps;
derived manifest and terminal-ledger totals; actual semantic read depth;
fork/upstream delta; owner searches and collision evidence; candidate producer,
verifier and non-test consumer; unknowns/exclusions; and exact gate/status proof.
`Knowledge System Reconciliation` must show mapped + deferred + unmapped equals
candidate total. No all-files-read or whole-repository absorption claim.

## Acceptance Criteria

The Acceptance And Stop Conditions above are binding and exhaustive. Local
accepts only evidence, never a worker self-declared source disposition.

## Review Gate

Worker returns `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`. Local applies
`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`; reruns require a named
contradiction, expected information gain and cost reason.

## Closure Checklist

- Exactly two worker-owned paths changed and HEAD unchanged.
- Corpus, knowledge and candidate totals reconcile.
- Reviewer-fast and pre-commit precede Local material commit.
- Continuity is a distinct Local-only commit; no successor opens automatically.

## Return-To-Orchestrator Conditions

Return exact evidence, command results, full execution base, current status,
manifest delta and no-commit statement. A truthful blocker is an acceptable
return; incomplete evidence is not completion.

## Operator Checkpoint

The operator authorized this bounded intake by instructing Local to continue
as orchestrator/reviewer and relay to Claude. Any absorption, implementation,
architecture reopening, provider/live or public action requires a later packet.

## MCP/CLI Adapter Boundary

| Field | Value |
|---|---|
| Adapter scope | source semantics comparison only; no MCP/CLI activation or wrapper |
| No-runtime-overclaim | This packet does not claim the adapter executes, intercepts, or wraps any runtime command. |

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: source-intake evidence only; the parked architecture owner explicitly
prevents this packet from becoming an architecture or runtime tranche.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.
Returned defect count: 0. Returned defects: NONE_RETURNED. Truncated: false.
Dispatch impact: none; existing gates remain mandatory.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; reviewer-fast source-intake bindings |
| literalTokensReviewed | exact headings/columns, status tokens, gate IDs, no-commit and worker-return profile fields |
| gateRunPurpose | confirm/evidence the completed dispatch packet before relay |
| claimBoundary | form verification only; no upstream value claim |

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead: f8fc0810c5f57bc3d475f9c6f0f1584008709a3c
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: N/A - pending worker return
Commit mode: WORKER_MUST_NOT_COMMIT
Worker stages and commits nothing. Local owns material and continuity commits.

## Work-Order Fulfillment Manifest

The Required Artifact Manifest and Write Ownership are exhaustive. Ignored
mirrors are read-only evidence roots, not changed-set members. No optional file.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a new two-source bounded intake, not a
legacy foundation absorption or whole-system completion claim.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: source-intake evidence only.
Target lifecycle state: unchanged; no package candidate is promoted.
Prior phase evidence: umbrella reconciliation and mirror index only.
Next forbidden skip: package creation, activation, UAT or certification.
Runtime/provider proof: none authorized.
Claim boundary: required classification vocabulary only; no package, skill or
lifecycle state is created or changed.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id ECC-ARCH-ABS-009-T0 --title "ECC Cross-Harness Adapter Profile Intake" --date 2026-09-15 --base f8fc0810c --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --include-worker-return-skeleton --stdout` |
| generatedProfile | source-intake plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source identities, boundaries, outputs, lifecycle graph and evidence contract |
| checkerReadAheadConfirmation | listed above |
| docOnlyNewFields | JSON output fields listed in artifact manifest |
| claimBoundary | scaffold provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | Codex local private workspace |
| Session or invocation | ECC-ARCH-ABS-009-T0 dispatch authoring 2026-09-15 |
| Working directory | repository root at dispatch base |
| Command or tool surface | governed reads, rg, Git read-only checks, scaffold helper, apply_patch and gates |
| Target paths | this packet and paired baseline |
| Allowed scope source | operator instruction to continue as orchestrator/reviewer |
| Before status evidence | clean worktree and empty staging at `f8fc0810c`; all planned paths absent |
| After status evidence | exactly paired dispatch documents pending validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded internal intake only |
| Claim boundary | no worker execution or source decision yet |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | `ecc-arch-abs-009-t0-dispatch-2026-09-15` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | NONE at authoring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | dispatch documentation for source intake |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no upstream/runtime action |
| invocationBoundary | local authoring and governance validation only |
| interceptionBoundary | no wrapper, proxy, runtime gate or hook activation |
| claimLanguage | packet is ready for manual relay after Local gate/commit |
| forbiddenExpansion | runtime/provider/live/public/package/MCP/CLI/architecture implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private source-intake packet; no public artifact requested.

## Claim Boundary

This work order authorizes only the two-output, read-only survey at exact pins.
It does not accept or import source value, reopen parked architecture, create
WP-ARCH-006, implement profiles/adapters/hooks, or authorize external effects.
