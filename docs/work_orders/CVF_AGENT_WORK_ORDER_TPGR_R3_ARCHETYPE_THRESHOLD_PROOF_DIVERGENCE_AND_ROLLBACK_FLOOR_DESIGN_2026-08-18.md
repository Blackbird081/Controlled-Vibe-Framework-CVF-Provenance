# CVF Agent Work Order - TPGR-R3 Archetype Threshold, Proof, Divergence, And Rollback Floor Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Batch ID: TPGR-R3

Dispatch base head: `e6f6f4916b8eec27e0a4877e98b325f993b4552e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated design worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md`

## Dispatch Prompt Envelope

Role: delegated design worker for TPGR-R3.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: artifact date is 2026-08-18; capture actual execution base
and require a clean worktree before any edit.

Do-not-misread notes: this is threshold design only. It does not authorize
R4-R9, implementation, selective execution, protected governance edits,
source intake, runtime, provider/live, public, deployment, or production.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, and every source/read-ahead checker
named below before authoring either output.

Return contract: write exactly the two authorized outputs, run required gates,
leave all changes unstaged and uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce a source-backed, testable R3 design for archetype-specific proof,
cost, divergence, freshness, anti-self-downgrade, and rollback floors. Return
design evidence and a disposition, not implementation.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R3",
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
  "claims": ["bounded archetype-specific threshold design"],
  "requiredProof": ["A1-A6 threshold matrix", "anti-self-downgrade rules", "freshness invalidation", "rollback floors", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["standard, checker, registry, catalog or hook mutation", "new source intake or network access", "selective gate execution", "runtime, provider/live, public, deploy or production"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: R3 uses committed R2G design evidence, not a new corpus claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, profile `P2_BOUNDED`,
`selectiveExecutionAuthorized: false`, and
`legacyGateDisposition: RUN_FULL_LEGACY_BUNDLE`.

## Worker Autonomy / No-Question Rule

Proceed autonomously with governed reads, local read-only calculations,
two-file authoring, and allowed-scope shape repairs. Return only for dirty
start, source contradiction, forbidden-path need, authority expansion,
required network/source refresh, or an unrepairable out-of-scope failure.

## Authorization / Source

The operator explicitly authorized
`AUTHORIZE_FRESH_R3_THRESHOLD_DESIGN_DISPATCH`. The paired GC-018 baseline is
the complete bounded execution authority.

## Authority Chain

1. frozen CVF doctrine and operating model;
2. `AGENTS.md`, active session state, and active handoff;
3. generalized TPGR reconciliation and accepted R2G assessment;
4. paired GC-018 baseline;
5. this work order.

Conflict rule: stop if a lower item expands a higher authority.

## Agent Roles

- Dispatcher: authors and commits the packet.
- Worker: designs thresholds, writes exactly two outputs, and does not stage or
  commit.
- Reviewer/closer: independently checks sources, logic, hostile cases,
  calculations, gates, and bounded repairs before disposition.
- Operator: required for R4+, implementation, protected governance mutation,
  or any runtime/live/public/destructive expansion.

## Required First Reads

Read completely:

- `CVF_SESSION_MEMORY.md`;
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
- `AGENT_HANDOFF_V59_2026-08-11.md`;
- `docs/reference/guard_orientation/README.md`;
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
- paired baseline and this work order;
- `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md`;
- `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md`;
- `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md`;
- `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`;
- `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md`.

Read only the targeted owner sections named by R2G for Layer A; source corpora
remain outside this design task's scope.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
```

Expected: captured execution base, clean start, full pre-implementation PASS,
and TPGR shadow route `COMPLIANT`. Stop before editing on other results.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R3 --title "Archetype Threshold Proof Divergence And Rollback Floor Design" --date 2026-08-18 --base accd005c1786f1e5e3d1950c706ba5f117424f32 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact R3 authority, threshold matrices, failure rules, output paths, roles, and gates |
| checkerReadAheadConfirmation | dispatch, routing, ADIF, structural, trace, public-disposition, and worker-return checker sources reviewed |
| docOnlyNewFields | route outcome; proof floor; cost ceiling; divergence tolerance; freshness dependency; rollback safe route; fact assertion owner |
| claimBoundary | dispatch authoring provenance only; no implementation claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: 22, not truncated.

Disclosed defectIds: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`,
`ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`,
`ADIF-0044`, `ADIF-0045`, `ADIF-0051`, `ADIF-0052`, `ADIF-0007`,
`ADIF-0016`, `ADIF-0017`, `ADIF-0024`, `ADIF-0031`, `ADIF-0039`,
`ADIF-0043`, `ADIF-0049`, `ADIF-0006`.

Dispatch impact: exact paths and sources; no provider memory authority; no
aggregate overclaim; checker read-ahead before drafting; worker no-commit;
hostile metadata and stale-receipt cases; separate material/continuity commits.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch envelope; status; commit mode; authority chain; source table; ADIF disclosure; route manifest; trace labels; fulfillment manifest; worker-return contract; public disposition |
| gateRunPurpose | confirmation of source-reviewed packet shape before release |
| claimBoundary | dispatch checker conformance only; no threshold correctness proof |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R3 stage definition | planning authority | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Revised Delivery Sequence | `R3` | generalized TPGR plan | ACCEPT |
| R2G passes into threshold design only | closure authority | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | Final Disposition; Claim Boundary | `PROCEED_TO_THRESHOLD_DESIGN` | R2G assessment | ACCEPT |
| six archetypes and evidence uncertainty | predecessor evidence | `docs/assessments/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | A1-A6 Worksheets; Observed / Projected / Unknown Evidence Summary | `A1-A6` | R2G evidence model | ACCEPT |
| current route is shadow-only | routing authority | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock | `selectiveExecutionAuthorized` | TPGR standard | ACCEPT |
| external critique identified self-downgrade and stale-receipt risks | advisory evidence already reconciled | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_EXTERNAL_CRITIQUE_2026-08-17.md` | strongest failure modes | `decisionUncertainty` | critique input | ACCEPT |
| final corrected checker evidence | review evidence | `docs/reviews/CVF_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_WORKER_RETURN_2026-08-17.md` | Independent Reviewer Addendum | direct checker invocation count | reviewer addendum | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| all four intended R3 paths | `Test-Path` returned false before authoring | ACCEPT |
| batch token search | `rg -n "TPGR-R3|ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR"` over active governed roots returned no match | ACCEPT |
| collision decision | create paired dispatch files now; reserve exact two worker output paths | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> delegated design worker -> independent reviewer/closer |
| phase | R3 documentation-only threshold design |
| baseHeadFor(phase) | dispatchBaseHead=`e6f6f4916b8eec27e0a4877e98b325f993b4552e`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exactly one assessment and one worker return |
| traceScope(phase, actor) | worker records reads, design derivation, hostile cases, commands, edits, status, and diff; reviewer independently verifies |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns commit |
| crossBatchIsolation | no R4-R9, T15, RSPB implementation, protected governance mutation, or unrelated workspace change |
| nextMoveSurfaces | reviewer updates continuity only after accepted material commit |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | no new intake; design thresholds from committed CVF evidence |
| Scope classification | documentation-only bounded threshold design |
| Risk sensitivity | MEDIUM: authority-sensitive design with local reversible writes and independent review |
| Selected role route | routeMode=`MULTI_AGENT_SINGLE_ROLE`; dispatcher -> design worker -> reviewer/closer |
| Role separation basis | no-commit worker designs; reviewer independently verifies and commits |
| Worker role | bounded threshold and hostile-case designer |
| Reviewer role | source, logic, anti-self-downgrade, freshness, rollback, and gate reviewer |
| Escalation condition | dirty start, contradiction, unowned fact, forbidden path, network need, or unrepairable gate failure |
| Source authority | CVF-governed standards, reviews, assessment, and code only |
| Outside advisory role | already reconciled critique is risk input, not authority |
| Corpus action | none |
| Semantic action | design proof floors; do not re-adjudicate source corpora |
| Direct import | forbidden |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_COMPLETION_2026-08-18.md` (optional reviewer-owned artifact; create only if the worker return cannot carry bounded acceptance evidence) |
| reviewerOwnedClosurePaths | material acceptance/repair and later continuity surfaces |
| closureOwner | CVF reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | create complete R3 design assessment |
| `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path, including standards, checkers,
registries, generated aggregates, catalogs, hooks, corpora, and continuity.

## Worker Final Manifest Constraint

Final untracked-aware status must show exactly the two authorized output files.
No modified, staged, deleted, renamed, or additional path is allowed. Stop on
a dirty starting tree.

## Write Ownership

Worker owns only the exact two output files. Reviewer/closer owns repairs,
material commits, and continuity.

## Design Contract

The assessment must include:

- one canonical fact-owner map; no second truth store;
- A1-A6 threshold worksheets;
- the three route outcomes and deterministic precedence;
- proof floors and evidence-expiry rules;
- per-archetype TPGR cost ceilings and maintenance assumptions;
- divergence tolerances and fail-closed escalation;
- rollback triggers and restored safe route;
- assertion ownership preventing worker self-downgrade;
- stale-receipt handling for source/schema/checker/catalog changes;
- hostile examples and a decision table for missing/malformed/conflicting data;
- R4 candidate delta manifest with zero current edits;
- one final allowed disposition.

## Archetype Threshold Matrix

| ID | Required design focus | Default fail-closed posture |
| --- | --- | --- |
| A1 new upstream corpus | retain first-intake manifest, ledger, and authority controls; bound routing-only overhead | `FULL_LAYER_A_REQUIRED` |
| A2 mixed-origin local synthesis | preserve dual-origin separation and cluster-scoped semantic claims | `FULL_LAYER_A_REQUIRED` until reusable receipts and owner mapping are current |
| A3 accepted-corpus cluster | admit light route only with current accepted receipts and exact named scope | `ESCALATE_FOR_REVIEW` on any owner/hash/freshness ambiguity |
| A4 upstream delta | find earliest affected node and preserve unrelated history | `FULL_LAYER_A_REQUIRED` for affected delta scope |
| A5 small named advisory item | avoid corpus ceremony while retaining source verification and authority boundary | `ESCALATE_FOR_REVIEW` on authority or reuse ambiguity |
| A6 downstream project source | preserve PROJECT_SOURCE registration and prevent CVF authority promotion | `FULL_LAYER_A_REQUIRED` when project corpus scanning is claimed |

Each worksheet must record: objective facts, fact owner, worker-assertable
fields, non-worker-assertable fields, route outcome, proof floor, cost ceiling,
divergence tolerance, escalation trigger, freshness dependencies, invalidation
node, rollback trigger, safe restored route, hostile example, evidence class,
and unresolved uncertainty.

## Threshold Precedence And Fail-Closed Rules

1. Authority/materiality and external-effect escalation overrides file count,
   reversibility, and worker cost preference.
2. Missing or contradictory owner facts cannot select `LIGHT_ROUTE_ALLOWED`.
3. `decisionUncertainty` is derived from evidence conflicts or reviewer-owned
   policy, never accepted as a worker-controlled downgrade input.
4. Any relevant source/schema/checker/catalog change expires current route
   eligibility from the earliest affected dependency node; historical receipt
   evidence remains immutable.
5. Cost thresholds cannot omit required semantic reading or always-on Layer A
   controls from the denominator.
6. A route with unknown maintenance cost cannot claim positive net value; it
   must remain projected and carry an escalation or measurement requirement.

## Hostile Test Design Matrix

At minimum, design expected outcomes for:

- one-file input with material doctrine authority impact;
- many-file corpus with complete structural receipts but no semantic receipt;
- worker declares low uncertainty while owner evidence conflicts;
- current receipt generated before a relevant checker hardening;
- unrelated checker change that must not invalidate the receipt;
- reused cluster with source hash drift;
- mixed-origin cluster whose provenance edge is missing;
- project source presented as CVF canonical authority;
- cost estimate excludes required semantic reading;
- light-route metadata is missing, malformed, unknown, or contradictory.

## Measurement Protocol

1. Use R2G A1-A6 evidence as the predecessor dataset; no new corpus scan.
2. Identify every threshold input's canonical owner and update trigger.
3. Separate one-time design cost, per-task routing cost, recurring maintenance,
   escalation cost, and unavoidable Layer A cost.
4. Express numeric thresholds only when evidence supports a number; otherwise
   define a measurement requirement and fail-closed interim route.
5. Distinguish direct checker command references from wrapper or indirect use;
   use corrected R2G evidence: 193 files, 80 command rows, 79 direct checker
   invocations, one wrapper, 114 not directly referenced.
6. Do not claim equivalence, false-negative rate, or production savings without
   replay/canary evidence; those remain R6-R7 concerns.
7. Produce a dependency invalidation graph sufficient to decide relevant
   versus unrelated checker/catalog changes without enumerating all 193 files.

## Acceptance Criteria

- exact two-path manifest and no worker stage/commit;
- A1-A6 worksheets complete with deterministic route precedence;
- no worker-controlled self-downgrade path;
- missing, malformed, stale, or contradictory evidence fails closed;
- proof floors never replace Layer A semantic owners;
- receipt invalidation is dependency-scoped, not globally stale or blindly current;
- thresholds with inadequate numeric evidence remain explicit measurement gates;
- rollback restores the full safe route and retains historical receipts;
- no second registry, lifecycle, command catalog, or truth store is proposed;
- no standard/checker/registry/catalog/hook edit occurs;
- final disposition is exactly `PROCEED_TO_R4_SHADOW_INTERFACE_DESIGN`,
  `REVISE_R3_THRESHOLDS`, `NARROW_TO_RECEIPT_REUSE_ONLY`, or
  `STOP_TPGR_SECOND_UPGRADE`;
- worker-return fast and reviewer-fast gates pass.

## Execution Plan

1. Capture clean execution base and run pre-implementation checks.
2. Scaffold worker return before long-form authoring.
3. Read all R3/R2G authorities and targeted Layer A owner sections.
4. Build fact-owner, A1-A6 threshold, hostile-case, freshness dependency, and
   rollback matrices.
5. Reconcile cost evidence and unknowns without inventing numeric certainty.
6. Produce R4 zero-edit candidate manifest and one allowed disposition.
7. Complete worker return, gates, exact status, and no-commit handoff.

## Evidence Requirements

Every threshold must cite its evidence owner and state whether it is observed,
projected, unknown, or a proposed design invariant. Every numeric value must
show a source or formula. Every light-route candidate must include a hostile
counterexample and rollback path.

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for its path family, docType,
and conditional content. The assessment must satisfy baseline/assessment
structure; the return must satisfy review, worker-return, trace, delta,
epistemic, public-disposition, and no-commit shapes.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Section-name lists must omit heading prefixes; actual headings belong only in
the real output artifact.

## Verification Commands

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_WORKER_RETURN_2026-08-18.md --title "CVF TPGR-R3 Archetype Threshold Proof Divergence And Rollback Floor Design Worker Return" --profile WORKER_RETURN_FULL_GATE_V1
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
| Actor | delegated design worker |
| Provider or surface | operator-transferred external worker; repository-local evidence only |
| Session or invocation | TPGR-R3 design execution |
| Working directory | repository root |
| Command or tool surface | governed reads, local queries, scaffold, gates, and Git diagnostics |
| Target paths | exact assessment and worker-return paths |
| Allowed scope source | paired baseline and this work order |
| Before status evidence | clean worktree and captured executionBaseHead required |
| After status evidence | exactly two unstaged/untracked output paths |
| Diff evidence | `git diff --name-status` plus untracked-aware status |
| Approval boundary | threshold design only; no implementation or authority mutation |
| Claim boundary | proposed design and evidence classification only |
| Agent type | external delegated worker |
| Invocation ID | worker records identifier or N/A with reason |
| Expected manifest | exact two output paths |
| Actual changed set | worker records final set |
| Manifest delta | zero required |
| Deletion or rename disposition | N/A with reason: forbidden |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | documentation-only R3 threshold design |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION: no selective or runtime enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: existing receipts are read-only design inputs; no new runtime receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or outside-system action is authorized or observed |
| invocationBoundary | local reads, calculations, and exact two-file authoring |
| interceptionBoundary | no wrapper, proxy, hook, runtime gate, or agent-control interception |
| claimLanguage | distinguish observed, projected, unknown, proposed, and blocked |
| forbiddenExpansion | R4-R9, protected edits, new intake, selective execution, runtime/provider/live/public/deploy/production |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | reconciled critique -> accepted R2G -> bounded R3 design |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard and existing Layer A owners |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no direct import, new corpus intake, or outside authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: no repeat scan, source refresh, or completeness update.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - committed archetype evidence is
  a design fixture; no new corpus or complete-scan claim is opened.

## Finding-To-Governance Learning Disposition

Classify any reusable threshold/control defect with a valid defect class,
learning lane, disposition, and next action. If none is found, use explicit
N/A-with-reason. Do not edit ADIF, standards, checkers, or hooks.

## Epistemic Process Block

Expected Result / Prediction: archetype-specific thresholds can prevent unsafe
self-downgrade while retaining bounded cheap routes.

Evidence Comparison: compare proposed floors to R2G evidence, Layer A owners,
current TPGR classification, and hostile stale/contradictory cases.

Contradiction Or Gap Disposition: ambiguous ownership, stale eligibility,
negative net value, or untestable thresholds require revision or stop.

Claim Update: return one allowed R3 disposition and change no authority.

## Dual Agent Surface Matrix

| Surface | INTERNAL_AGENT | EXTERNAL_AGENT_CLI_MCP | Interface | Authority/risk boundary | Evidence | Adapter boundary |
| --- | --- | --- | --- | --- | --- | --- |
| dispatch | reviewer/orchestrator authors and commits | receives operator-transferred packet | baseline/work order | dispatch only | committed packet | no provider adapter required |
| design | reviewer independently verifies | writes exact two outputs without commit | governed files and local commands | no authority mutation | source, formulas, hostile cases | repository-local only |
| closure | reviewer repairs/accepts/commits | no commit authority | reviewer gates | separate-role acceptance | diff and rerun proof | no runtime adapter |

## Foundation Storage Layout Block

Outputs stay in existing `docs/assessments/` and `docs/reviews/` owners. No new
directory, schema, registry, generated aggregate, package, or runtime surface.

## Review Gate

Worker return is not acceptance. Reviewer independently verifies sources,
fact ownership, precedence, formulas, hostile cases, freshness dependencies,
rollback behavior, output manifest, and gates before deciding disposition.

## Operator Checkpoint

No checkpoint is required inside allowed design work. Any R4 opening,
implementation, protected edit, selective execution, or external effect
requires a new explicit operator decision and governed dispatch.

## Closure Checklist

- [ ] Worker captured post-dispatch executionBaseHead and clean start.
- [ ] Exactly two authorized outputs remain unstaged.
- [ ] A1-A6 threshold and hostile-case matrices are complete.
- [ ] No self-downgrade or stale-receipt light route exists.
- [ ] Costs, unknowns, divergence, and rollback floors are explicit.
- [ ] Worker returned one allowed R3 disposition.
- [ ] Worker-return fast and reviewer-fast gates pass.
- [ ] Reviewer independently verified and alone owns commits.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: R3 designs routing thresholds and changes no
legacy coverage claim or coverage-index row.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; public-sync is not authorized.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for dirty start, missing/contradictory authority,
unowned threshold input, forbidden-path need, source refresh/network need, or
unrepairable gate failure. Otherwise return `COMPLETE_PENDING_REVIEW`.

## Claim Boundary

This order authorizes only one uncommitted R3 threshold design assessment and
its worker return. It authorizes no R4-R9 work, implementation, standard/
checker/registry/catalog/hook edit, source acquisition, selective execution,
T15, runtime, provider/live, public sync, deployment, destructive action, or
production claim.
