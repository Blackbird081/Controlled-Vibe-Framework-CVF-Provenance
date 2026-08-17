# CVF Agent Work Order - TPGR-R2G Generalized Absorption Routing Feasibility Assessment

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Batch ID: TPGR-R2G

Dispatch base head: `9e0dba8fff772675c202204a865a0dbf43e45e95`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated assessment worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md`

rawMemoryReleased=false

## Dispatch Prompt Envelope

Role: delegated external assessment worker for TPGR-R2G.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md`

Paired authority: `docs/baselines/CVF_GC018_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture current post-dispatch HEAD before any edit and
confirm the worktree is clean. Do not use the older dispatch-base anchor as
executionBaseHead.

Current-time notes: packet date is 2026-08-17.

Do-not-misread notes: this is a non-implementation feasibility assessment.
It does not authorize changes to standards, checkers, registries, catalogs,
hooks, source corpora, runtime, provider/live, public, deployment, production,
or selective gate execution.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, this packet, the R2G reconciliation, the named
authority sources, and checker source for both worker outputs before writing.

Return contract: leave exactly the two authorized outputs unstaged and
uncommitted. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Assess whether TPGR can route CVF's existing knowledge lifecycle across six
representative archetypes with bounded net value. Produce evidence and a
recommendation, not implementation or new governance authority.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R2G",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [
    "docs/baselines/",
    "docs/assessments/",
    "docs/reviews/"
  ],
  "claims": ["bounded TPGR and existing-lifecycle feasibility assessment"],
  "requiredProof": ["six-archetype evidence matrix", "cost separation", "source verification", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["rule, checker, registry, catalog or hook mutation", "new source intake or network access", "selective gate execution", "runtime, provider/live, public, deploy or production"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, profile `P2_BOUNDED`,
`selectiveExecutionAuthorized: false`, and
`legacyGateDisposition: RUN_FULL_LEGACY_BUNDLE`.

## Worker Autonomy / No-Question Rule

Proceed autonomously with source reads, local queries, documentation edits
inside the exact two-path manifest, and allowed-scope gate remediation. Return
to the orchestrator only for a source contradiction, dirty starting tree,
forbidden-path need, authority expansion, required network/source refresh, or
an unrepairable failure outside worker ownership.

## Authorization / Source

The operator approved generalized R2G through the `next` instruction after
reviewing the committed critique reconciliation. The paired baseline is the
complete execution authority.

## Authority Chain

1. frozen CVF doctrine and operating model;
2. `AGENTS.md`, active session state, and active handoff;
3. `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md`;
4. paired GC-018 baseline;
5. this work order.

Conflict rule: stop if a lower item appears to expand a higher authority.

## Agent Roles

- Dispatcher: CVF reviewer/orchestrator; owns this packet and commits.
- Worker: performs the assessment, writes exactly two files, does not stage or
  commit.
- Reviewer/closer: independently checks sources, calculations, claims, gates,
  and any bounded repairs before accepting or rejecting.
- Operator: required for R3+, scope expansion, authority changes, source
  acquisition, or any runtime/live/public/destructive action.

## Required First Reads

Read completely:

- `CVF_SESSION_MEMORY.md` and `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
- `AGENT_HANDOFF_V59_2026-08-11.md`;
- `docs/reference/guard_orientation/README.md`;
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
- paired baseline and this work order;
- `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md`;
- `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`;
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

Read the named relevant sections, registry entries, tables, and evidence blocks
for the remaining authority and archetype sources in the Source Verification
Block and Archetype Work Matrix. This is a routing/cost assessment, not a new
semantic review of every underlying source file.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
```

Expected: executionBaseHead captured; clean start; pre-implementation and TPGR
shadow checks pass. Stop before editing on failure outside allowed remediation.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R2G --title "Generalized Absorption Routing Feasibility Assessment" --date 2026-08-17 --base 9e0dba8fff772675c202204a865a0dbf43e45e95 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact authority, manifests, archetypes, assessment schema, gates, and claim limits |
| checkerReadAheadConfirmation | dispatch, routing, ADIF, structural, trace, public-disposition, and worker-return checker sources read |
| docOnlyNewFields | archetype evidence posture; lifecycle node; inherited evidence; Layer A cost; TPGR overhead; projected closure; claim-token compatibility |
| claimBoundary | dispatch provenance only; no feasibility result or runtime behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: 22, not truncated.

| Defect IDs | Dispatch response |
| --- | --- |
| ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021 | exact bounded claims; CVF-only authority; no hidden completeness claim; role-true no-commit route; checker read-ahead; avoid marker collisions |
| ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052 | no aggregate claim beyond rows; no protected worker path; command help verified; no archive/continuity worker mutation |
| ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 | literal-safe boundaries; reusable findings routed; material/continuity split; fresh worker evidence; rejects remain visible; worker-return contract complete; cwd explicit; commands source-verified; source symbol cells are paths/symbols |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | first-section envelope; status; no-commit; authority chain; exact source table; ADIF disclosure; route manifest; trace labels; final manifest; worker-return scalar contract; public disposition |
| gateRunPurpose | confirm this source-reviewed work order is dispatchable before worker transfer |
| claimBoundary | authoring and dispatch-shape evidence only; no assessment outcome or implementation proof |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| generalized conditional graph and R2G deliverables | planning authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Conditional Lifecycle Route Graph; Generalized R2 Feasibility Assessment; R2 Deliverables And Exit | existing governed review path | R2G plan | ACCEPT |
| shadow interlock remains mandatory | routing fact | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock | `selectiveExecutionAuthorized` | TPGR T0 | ACCEPT |
| missing universal router is recorded | current gap | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Enforcement Gap | existing chain-map path | chain map | ACCEPT |
| lifecycle semantics stay in existing owners | authority fact | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core; Required Ledger Semantics | existing standard path | lifecycle core | ACCEPT |
| derived evidence reuse is cluster-based | evidence fact | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | Absorption Efficiency And Provenance Reuse | `semanticReviewUnit` | mixed-origin owner | ACCEPT |
| corpus and project registration rules exist | registry fact | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | Rule 1; Rule 5 | existing standard path | GC-051 | ACCEPT |
| A1-A6 primary artifacts exist | path fact | `docs/baselines/CVF_GC018_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | Archetype Evidence Map | six exact evidence paths | TPGR-R2G baseline | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| assessment path collision | `Test-Path docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` returned false | ACCEPT |
| worker-return path collision | `Test-Path docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md` returned false | ACCEPT |
| batch token search | `rg -n --fixed-strings "TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT" docs CVF_SESSION` returned no pre-existing match | ACCEPT |
| collision decision | create the exact two worker outputs only | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> delegated assessment worker -> independent reviewer/closer |
| phase | R2G non-implementation feasibility assessment |
| baseHeadFor(phase) | dispatchBaseHead=`9e0dba8fff772675c202204a865a0dbf43e45e95`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exactly one assessment and one worker return |
| traceScope(phase, actor) | worker records all reads, calculations, commands, edits, status, and diff; reviewer independently verifies |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns commit |
| crossBatchIsolation | no T15, R3+, RSPB implementation, or unrelated workspace mutation |
| nextMoveSurfaces | reviewer updates active handoff/session state only after accepted material commit |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | compare existing governed lifecycle evidence across six archetypes and measure routing feasibility |
| Scope classification | documentation-and-evidence-only bounded assessment |
| Risk sensitivity | MEDIUM: authority-sensitive design evidence, local reversible writes, independent review |
| Selected role route | routeMode=`MULTI_AGENT_SINGLE_ROLE`; dispatcher -> assessment worker -> reviewer/closer |
| Role separation basis | no-commit worker produces evidence; independent reviewer verifies and alone commits |
| Worker role | bounded evidence and cost assessor |
| Reviewer role | independent source, calculation, claim, and gate reviewer |
| Escalation condition | dirty start, source contradiction, forbidden-path need, authority expansion, new source refresh, or unrepairable gate failure |
| Source authority | CVF-governed standards, registries, audits, reviews, and code |
| Outside advisory role | critique input already reconciled; not canonical evidence by itself |
| Corpus action | no new registration, enumeration, ledger, or completeness claim |
| Semantic action | assess evidence requirements; do not re-adjudicate underlying source knowledge |
| Direct import | forbidden |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer reviewer disposition in a bounded completion artifact only if needed |
| reviewerOwnedClosurePaths | material acceptance/repair and later continuity surfaces |
| closureOwner | CVF reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | create complete R2G assessment |
| `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path, including standards, checkers,
registries, generated aggregates, catalogs, hooks, source corpora, handoff, and
session state.

## Worker Final Manifest Constraint

Final `git status --short --untracked-files=all` must show exactly the two
authorized untracked files. No modified, staged, deleted, renamed, or extra
path is allowed. If the start is dirty, stop without editing.

## Write Ownership

The worker owns content only in the exact two output files. Reviewer/closer
owns all material commits, repairs outside worker ownership, and continuity.

## Assessment Contract

The assessment must include:

- verified as-is Layer A owner map and universal-router gap;
- conditional lifecycle interface candidate referencing owners rather than
  copying their evidence models;
- one worksheet per A1-A6;
- claim-vocabulary compatibility and migration-cost assessment;
- canonical autorun command-universe count and minimal metadata feasibility;
- cost model separating Layer A work from TPGR overhead;
- observed/projected/unknown evidence labels;
- exact proposed authority-delta paths with zero current edits;
- stop-condition evaluation and one final allowed disposition.

## Archetype Work Matrix

| ID | Primary evidence | Required analysis |
| --- | --- | --- |
| A1 | `docs/audits/CVF_EAIC_KR_R1_CVF_23_07_EXTERNAL_REPOSITORY_INTAKE_AUDIT_2026-07-23.md` | first-intake controls and duplicate-ceremony risk |
| A2 | `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md` | mixed-origin local-first route and provenance reuse |
| A3 | `docs/reviews/CVF_RSPB_AI_T11_CAPABILITY_WORKSPACE_PROFILE_AND_BOOTSTRAP_POLICY_BUNDLE_VALIDATION_KERNEL_COMPLETION_2026-08-17.md` | accepted-cluster regression and actual ceremony cost |
| A4 | `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` | earliest-affected-node delta handling |
| A5 | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md` | small named advisory route without corpus ceremony |
| A6 | GC-051 Rule 5 and current `PROJECT_SOURCE` entries in `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | project-source use without CVF authority contamination |

Each worksheet records: input class, entry node, inherited evidence, semantic
scope, current controls, proposed TPGR route, always-on controls, conditional
controls, exact licensed claim, invalidation trigger, authority boundary,
Layer A cost, TPGR overhead, projected savings, uncertainty, and disposition.

## Measurement Protocol

1. Recompute registry entry count and populated-type distribution.
2. Recompute checker-shaped file count and canonical autorun-referenced
   checker count; retain `catalog-unwired` terminology.
3. Count active phase commands from the canonical autorun catalog, including
   non-checker commands.
4. Extract historical artifact/command/time evidence only where explicitly
   recorded; do not invent missing wall time.
5. Run the current pre-implementation gate once as required preflight and
   record its elapsed time as a current full-gate sample, not a universal
   benchmark.
6. Model proposed closure only from existing command groups and mark every
   unmapped command always-selected or unknown.
7. Estimate one-time metadata and recurring maintenance separately.
8. Never count required semantic reading as TPGR waste.

## Acceptance Criteria

- exact two-path worker manifest and no worker stage/commit;
- all six archetypes have complete worksheets;
- CVF owner sources and registry counts are independently recomputed;
- observed, projected, and unknown evidence are never conflated;
- small named input is not forced through corpus ceremony without evidence;
- first intake retains all necessary lifecycle controls;
- upstream delta preserves historical evidence and targets freshness impact;
- project-source use does not promote project material to CVF authority;
- proposed router/interface duplicates no manifest, ledger, or owner map;
- no selective execution or authority edit occurs;
- final disposition is exactly `PROCEED_TO_THRESHOLD_DESIGN`,
  `NARROW_TO_RECEIPT_REUSE_ONLY`, `REVISE_ARCHITECTURE`, or
  `STOP_TPGR_SECOND_UPGRADE`;
- worker-return fast gate and relevant governance gates pass.

## Execution Plan

1. Capture executionBaseHead and clean status; run pre-implementation gate.
2. Scaffold the worker return before long-form authoring.
3. Read authority and named archetype evidence proportionally to the asserted
   claims; record source sections.
4. Recompute machine counts and current full-gate sample.
5. Build A1-A6 worksheets, owner/interface analysis, cost model, claim-token
   compatibility, proposed delta manifest, and final disposition.
6. Complete worker return, run final gates, confirm exact two-path status, and
   return without staging or committing.

## Evidence Requirements

Record commands, cwd, exit status, counts, elapsed times when measured,
calculation formulas, source paths/sections, projection assumptions, unknowns,
executionBaseHead, final diff/status, and zero network/provider/live statement.

## Worker Output Checker Read-Ahead Mandate

Before writing the assessment and worker return, read the full checker source
applicable to their path, docType, and conditional terms. Assessment must use
baseline/evidence structural headings. Worker return must use the scaffold and
include its own checker-read-ahead, trace, delta boundary, public disposition,
external-intake routing, repeat-scan/corpus applicability, learning,
epistemic, status, changed files, retrospective, command evidence, and
no-commit sections.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

WORKER_EXPERIENCE_RETRO: REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md --title "CVF TPGR-R2G Generalized Absorption Routing Feasibility Assessment Worker Return" --profile WORKER_RETURN_FULL_GATE_V1
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

Do not run pre-commit because the worker must not stage or commit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated assessment worker |
| Provider or surface | operator-transferred external worker; repository-local evidence only |
| Session or invocation | TPGR-R2G assessment execution |
| Working directory | repository root |
| Command or tool surface | governed reads, PowerShell/Python queries, worker-return scaffold, governance gates, Git diagnostics |
| Target paths | exact assessment and worker-return paths |
| Allowed scope source | paired baseline and this work order |
| Before status evidence | clean worktree and captured executionBaseHead required |
| After status evidence | exactly two unstaged/untracked output paths |
| Diff evidence | `git diff --name-status` plus untracked-aware status |
| Approval boundary | assessment only; no implementation or authority mutation |
| Claim boundary | measured/projected feasibility evidence only |
| Agent type | external delegated worker |
| Invocation ID | worker records local invocation identifier or N/A with reason |
| Expected manifest | exact two output paths |
| Actual changed set | worker records final set |
| Manifest delta | zero required |
| Deletion or rename disposition | N/A with reason: forbidden |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only R2G feasibility and cost evidence |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION: no selective or runtime enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: existing governed receipts are read-only comparison inputs; no new runtime receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or outside-system action is authorized or observed |
| invocationBoundary | local read-only queries and exact two-file authoring |
| interceptionBoundary | no wrapper, proxy, hook, runtime gate, or agent-control interception |
| claimLanguage | distinguish observed, projected, unknown, and blocked |
| forbiddenExpansion | rule/checker/registry/catalog edits, new intake, runtime/provider/live/public/deploy/production |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | already reconciled critique -> bounded CVF feasibility assessment -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing TPGR and lifecycle owners |
| Disposition | COMPARISON_AND_COST_ASSESSMENT_ONLY |
| Claim boundary | no direct import, new corpus intake, or outside authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: this worker compares current governed artifacts and opens
  no repeat scan, source refresh, or corpus completeness update.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - archetypes are evidence samples,
  not a newly scanned corpus; no complete-corpus claim is authorized.

## Finding-To-Governance Learning Disposition

The worker must classify any reusable routing/cost defect using a valid defect
class, learning lane, disposition, and next action in the worker return. If no
new defect is found, use an explicit N/A-with-reason disposition. Do not edit
ADIF, standards, checkers, or hooks.

## Epistemic Process Block

Expected Result / Prediction: the existing lifecycle plus a thin TPGR
interface has bounded value on reuse routes without weakening first intake.

Evidence Comparison: compare A1-A6, current catalog evidence, actual full-gate
sample, and explicit projections.

Contradiction Or Gap Disposition: negative net value, duplicate evidence,
unmaintainable command mapping, or authority ambiguity narrows or stops the
upgrade.

Claim Update: return exactly one allowed R2G disposition; change no authority.

## Dual Agent Surface Matrix

| Surface | INTERNAL_AGENT | EXTERNAL_AGENT_CLI_MCP | Interface | Authority/risk boundary | Evidence | Adapter boundary |
| --- | --- | --- | --- | --- | --- | --- |
| dispatch | reviewer/orchestrator authors and commits | receives operator-transferred packet | Markdown baseline/work order | dispatch only | committed packet | no provider adapter required |
| assessment | reviewer independently verifies | writes exact two outputs without commit | governed files and local commands | no authority mutation | source and command trace | repository-local only |
| closure | reviewer repairs/accepts/commits | no commit authority | reviewer gate | separate-role acceptance | diff and rerun proof | no runtime adapter |

## Foundation Storage Layout Block

Outputs stay in existing `docs/assessments/` and `docs/reviews/` owners. No new
directory, package, schema, registry, generated aggregate, or runtime surface
is authorized.

## Review Gate

Worker handoff is not acceptance. Reviewer independently verifies all source
facts, counts, formulas, archetype dispositions, proposed path manifest,
claims, and gates. Reviewer alone decides repair, acceptance, commit, or return.

## Operator Checkpoint

No checkpoint is required for routine allowed-scope assessment work. Stop and
return for any proposed action beyond evidence authoring. R3 or implementation
requires a new explicit operator decision and new governed dispatch.

## Closure Checklist

- [ ] Worker captured post-dispatch executionBaseHead and clean start.
- [ ] Exactly two authorized output paths exist and remain unstaged.
- [ ] A1-A6 worksheets and cost separation are complete.
- [ ] Worker returned one allowed R2G disposition.
- [ ] Worker-return fast and reviewer-fast gates pass.
- [ ] Independent reviewer verified sources, counts, formulas, and claims.
- [ ] Reviewer/closer alone owns material and continuity commits.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this assessment compares existing governed
archetype evidence and changes no legacy coverage claim or coverage-index row.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private assessment dispatch; public-sync is not authorized.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for dirty start, missing authority source,
contradictory evidence that prevents bounded conclusions, forbidden-path need,
required network/source refresh, or unrepairable gate failure. Otherwise
return `COMPLETE_PENDING_REVIEW` with exact two-path evidence.

## Claim Boundary

This order authorizes only one uncommitted feasibility assessment and its
worker return. It authorizes no lifecycle or TPGR implementation, rule/checker/
registry/catalog/hook edit, source acquisition, selective execution, T15,
runtime, provider/live, public sync, deployment, destructive action, or
production claim.
