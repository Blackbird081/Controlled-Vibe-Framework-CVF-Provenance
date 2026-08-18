# CVF Agent Work Order - TPGR-R5 Shadow Command Applicability And Receipt Invalidation Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Batch ID: TPGR-R5

Dispatch base head: `dbaae72776ca6e50ae73a4e3baac327de1ef9ce5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated design worker

Reviewer/closer: CVF reviewer/orchestrator

Worker return path: `docs/reviews/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_WORKER_RETURN_2026-08-18.md`

## Dispatch Prompt Envelope

Role: delegated design worker for TPGR-R5.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

Current-time notes: artifact date is 2026-08-18; begin only from the clean
post-continuity HEAD supplied by the reviewer.

Do-not-misread notes: design only. Do not edit standards, checkers, registries,
catalogs, hooks, session state, source corpora, runtime, or public surfaces.
Do not skip any current gate; selective execution remains false.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired GC-018, this work order, all Required First Reads, and checker
sources named below before writing. Capture exact HEAD and clean status.

Return contract: create exactly the two authorized output files, run the full
worker-return gate, leave all work uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Design the smallest future-facing command-applicability and receipt-
invalidation contract for R4's accepted shadow interface. Reuse existing CVF
command and evidence owners by reference; do not build or propose a parallel
control plane.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker or contract defects directly. Return to the
reviewer only for source contradiction, forbidden-path need, or missing
authority that makes the two deliverables impossible. Do not ask for cosmetic
preferences.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| accepted R4 material | assessment and worker return committed at `dbdc0888e5c80cc507fb819d569a58083c2a533e` | RELEASED |
| R4 continuity | `CVF_SESSION/state/entries/tpgrR4ShadowInterfaceAndClaimVocabularyDesignClosed20260818.json`; `dbaae7277` | RELEASED |
| R5 design dispatch authority | standing operator authorization recorded in active continuity | RELEASED_DOCUMENTATION_ONLY |
| implementation/selective execution | no authority follows from the rows above | FORBIDDEN |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R5 --title "Shadow Command Applicability And Receipt Invalidation Design" --date 2026-08-18 --base dbaae72776ca6e50ae73a4e3baac327de1ef9ce5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact R5 authority, sources, two-path output manifest, design tables, hostile cases, gates, and return contract |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `commandApplicability`, `receiptOwnerRef`, `invalidationEvent`, `invalidationScope`, `recomputeFromNode`, `historicalDisposition` |
| claimBoundary | dispatch provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Returned defects | full resolver output inspected before authoring |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | source authority, exact paths, checker read-ahead, role separation, dependency graph audit, and no-commit evidence are explicit |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch-ready status, mandatory work-order structural groups, Source Verification columns, scaffold fields, no-commit terms, Task Governance Routing Manifest JSON, worker-return headings/fields, and public/delta evidence enums |
| gateRunPurpose | confirm authored shape against already-read checker source, not use failures as discovery |
| claimBoundary | structural conformance only; worker and reviewer must independently verify semantic correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R5 next-step authority | predecessor disposition | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | R5 Candidate Command/Receipt Invalidation Manifest; Final Disposition | assessment path | accepted R4 design | ACCEPT |
| independent R4 repair is binding | reviewer evidence | `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md` | Independent Reviewer Addendum | worker-return path | reviewer-accepted R4 evidence | ACCEPT |
| R4 field/token semantics | design input | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Shadow Interface Field Table; Exact Claim Vocabulary; corpus proof; upstream drift | assessment path | R4 design | ACCEPT |
| route floors and expiry | design input | `docs/assessments/CVF_TPGR_R3_ARCHETYPE_THRESHOLD_PROOF_DIVERGENCE_AND_ROLLBACK_FLOOR_DESIGN_2026-08-18.md` | Route Outcomes; Proof Floors; Dependency Invalidation Graph | assessment path | accepted R3 design | ACCEPT |
| canonical command owner | current implementation fact | `governance/compat/agent_autorun_command_catalog.py` | autorun command catalog definitions | `_common_commands` | autorun catalog | ACCEPT |
| shadow-only route | authority boundary | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock; Activation Rule | standard path | TPGR standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact four R5 paths | all returned false before authoring | PASS |
| namespace search | `rg -n "TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN" docs CVF_SESSION` returned no prior artifact | PASS |
| collision decision | exact namespace available | CREATE_NEW |

## Required First Reads

Read fully unless a targeted section is explicitly named:

1. paired R5 GC-018 baseline and this work order;
2. bootstrap read model, `CVF_SESSION_MEMORY.md`, and active handoff;
3. guard orientation and literal-format gotchas;
4. R4 assessment in full, including reviewer-repaired corpus proof, hostile
   cases, and R5 candidate manifest;
5. R4 worker return, including Independent Reviewer Addendum;
6. R3 assessment sections Route Outcomes, Proof Floors, Dependency
   Invalidation Graph, and A3/A4 worksheets;
7. TPGR routing standard sections Mandatory Classification, Mandatory
   Escalation, TPGR-T0 Legacy Full-Gate Interlock, Activation Rule;
8. `governance/compat/agent_autorun_command_catalog.py` in full;
9. applicable checker source for both worker outputs before writing them.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/assessments/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_2026-08-18.md` | create complete R5 documentation-only design |
| `docs/reviews/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_WORKER_RETURN_2026-08-18.md` | create full worker-return evidence packet |

Forbidden paths: every other repository path. Do not stage or commit.

## Design Contract

The assessment must include all of the following:

1. Current owner map naming the single canonical command catalog and every
   existing receipt/evidence owner used; no second catalog or store.
2. A complete R4 invariant-to-command applicability matrix covering all eight
   interface fields, all eight claim tokens, no-promotion-by-aggregation,
   corpus semantic proof, uncertainty escalation, and upstream drift.
3. Applicability enum exactly `ALWAYS`, `CONDITIONAL`, or
   `NOT_APPLICABLE_WITH_REASON`. Each conditional row must state objective
   activation predicate, canonical command owner, required input/evidence,
   false-positive exclusion, failure route, and invalidation trigger.
4. A receipt ownership table for the six documentation-only candidates:
   `commandApplicability`, `receiptOwnerRef`, `invalidationEvent`,
   `invalidationScope`, `recomputeFromNode`, `historicalDisposition`.
5. Invalidation precedence: source identity, owner surface, schema/registry,
   checker semantics, command-catalog membership, and review authority.
   Earliest affected node controls; historical evidence remains immutable;
   current eligibility expires.
6. Re-earning rule: later claims become current only from fresh canonical-
   owner evidence after invalidation; no stale receipt revival and no worker
   declaration can restore eligibility.
7. False-positive boundary for descriptive prose, tables explaining tokens,
   archived history, code fences, quoted examples, and incomplete draft
   artifacts. Design exact detection surfaces without writing regex/code.
8. Cost proof: candidate routing must not add duplicate command discovery or
   replay on top of unavoidable Layer A evidence. Separate always-on legacy
   bundle cost from projected future selective value.
9. Hostile-case table, zero-edit R6 candidate manifest, and exactly one
   allowed final disposition.

This design must not implement any command, receipt, checker, registry field,
or selective route.

## Required Applicability Rows

At minimum, evaluate these command/evidence families without changing them:

- task route classification;
- worker-return structural/semantic evidence;
- corpus registration, ledger, blind-spot, knowledge-map reconciliation;
- claim vocabulary/no-aggregation detection candidate;
- upstream identity and selected-file hash comparison;
- owner/checker/catalog freshness;
- full legacy autorun bundle;
- non-applicable families with explicit reason.

Do not assume one command per field. Many-to-one reuse is preferred; any
one-to-many fan-out must justify why existing owner evidence cannot be reused.

## Required Hostile Cases

1. A worker marks a costly command `NOT_APPLICABLE_WITH_REASON` to obtain a
   lighter route.
2. A checker changes semantics but its filename and command row remain stable.
3. A command-catalog row is removed while an old receipt still cites it.
4. Upstream identity changes while selected file hashes remain stable.
5. A bare `NO_NEW_VALUE` ledger label is offered as corpus semantic proof.
6. Ten cluster receipts are aggregated into a corpus claim.
7. A historical archived document containing a claim token triggers current
   enforcement.
8. Descriptive prose or a code fence explaining a token is mistaken for an
   asserted claim.
9. A receipt has every field but its review authority changed.
10. A stale receipt is copied into a new artifact with a new timestamp.
11. One dependency fact is unknown and the worker declares low uncertainty.
12. Receipt invalidation cascades beyond the earliest affected scope and
    needlessly reopens unrelated evidence.

Every case must end in one deterministic route:
`FULL_LAYER_A_REQUIRED`, `ESCALATE_FOR_REVIEW`, or preservation of an
unaffected current sub-claim with an explicit reason. No case may silently
select `LIGHT_ROUTE_ALLOWED`.

## Allowed Final Dispositions

- `PROCEED_TO_R6_SHADOW_REPLAY_AND_MIGRATION_DESIGN`
- `REVISE_R5_COMMAND_RECEIPT_DESIGN`
- `NARROW_TO_RECEIPT_INVALIDATION_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Acceptance Criteria

- exact two-path worker output manifest and no commit;
- every R4 invariant and token reconciles to the applicability matrix;
- one canonical command catalog, zero new store/catalog/lifecycle/router;
- applicability cannot be worker-selected as final;
- semantic checker change invalidates a receipt even when command text is
  stable;
- stale receipt cannot revive through copying or timestamp change;
- false-positive boundaries are explicit and testable later;
- all 12 hostile cases fail closed without widening invalidation scope;
- current legacy bundle remains mandatory;
- zero-edit R6 manifest and one allowed disposition;
- required gates pass and reviewer independently accepts.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | external no-commit design worker -> independent reviewer/closer -> session-sync steward |
| phase | R5 documentation-only design execution |
| baseHeadFor(phase) | dispatchBaseHead=`dbaae72776ca6e50ae73a4e3baac327de1ef9ce5`; executionBaseHead=worker captures clean post-continuity HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly two worker outputs |
| traceScope(phase, actor) | worker records reads, commands, status, actual manifest; reviewer records independent semantic and gate evidence |
| commitOwner(phase) | reviewer/closer only; worker commit forbidden |
| crossBatchIsolation | no R6+, T15, RSPB, runtime, or public work |
| nextMoveSurfaces | reviewer owns active continuity only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_COMPLETION_2026-08-18.md` (optional reviewer-owned path; prefer an Independent Reviewer Addendum unless distinct closure evidence becomes necessary) |
| reviewerOwnedClosurePaths | the exact two worker outputs; active continuity only in a separate commit after acceptance |
| closureOwner | CVF reviewer/orchestrator |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing either output, read applicable checker source for its docType,
path family, and triggered evidence classes. The assessment must satisfy
baseline structural groups. The worker return must derive required headings,
trace labels, delta evidence tokens, external-intake disposition, corpus,
epistemic, public-export, status, no-commit, and every other mandatory
hardening literal from checker source.

Do not use gate failures as a substitute for this read-ahead.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN_WORKER_RETURN_2026-08-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections include Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Checker Source Read-Ahead Block, Agent
Operation Trace Block, Delta Execution Claim Boundary Control Block, Public
Export Disposition, External Knowledge Intake Routing, every checker-required
hardening block, Corpus Completeness And Report Integrity, Finding-To-Governance
Learning Disposition, Epistemic Process Block, Claim Boundary, git status,
Changed Files, Command Evidence, and No-Commit Statement.

## Verification Commands

Run from repository root after authoring both outputs:

```powershell
python governance/compat/check_task_governance_route.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --check
git status --short --untracked-files=all
```

No individual checker run substitutes for the full fast gate. Record exact
results and actual untracked paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated design worker, then independent reviewer/closer |
| Provider or surface | operator-transferred external worker; local private provenance workspace |
| Session or invocation | TPGR-R5 design, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, local git inspection, Python governance commands, file authoring |
| Target paths | exact two output paths in fulfillment manifest |
| Allowed scope source | paired R5 baseline and this work order |
| Before status evidence | clean worktree and captured executionBaseHead required before edits |
| After status evidence | exactly two untracked output paths |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` for untracked additions |
| Approval boundary | documentation-only R5 design |
| Claim boundary | no implementation, selective execution, source intake, or external effect |
| Agent type | external delegated worker |
| Invocation ID | `tpgr-r5-worker-execution-2026-08-18` |
| Expected manifest | exact two output paths |
| Actual changed set | worker fills from actual status |
| Manifest delta | must be MATCH or return blocked |
| Deletion or rename disposition | N/A with reason unless actual evidence differs, which blocks completion |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R5 documentation-only command-applicability and receipt-invalidation design |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or selective-command behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two governed design artifacts and local verification commands only |
| invocationBoundary | local reads, authoring, and governance checks |
| interceptionBoundary | no wrapper, proxy, runtime gate, CLI/MCP adapter, or agent coding control |
| claimLanguage | candidate documentation-only semantics, not implemented behavior |
| forbiddenExpansion | no standard/checker/registry/catalog/hook edits, source intake, R6+, T15, runtime/provider/live/public/deploy/production action |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | prior critique is already reconciled through R2G/R3/R4; R5 uses only accepted CVF artifacts as authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | TPGR standard and existing R3/R4 design evidence |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no new outside input, corpus registration, direct import, or external authority promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this work order designs command applicability and
receipt invalidation from existing committed R3/R4 evidence and opens no repeat
scan, source refresh, or corpus completeness update.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: no corpus is
scanned and no completeness claim changes; R4 semantic-proof rules are design
inputs only.

## Finding-To-Governance Learning Disposition

Worker must disclose any new repeated defect pattern. Otherwise use
N/A_WITH_REASON and explain why the result is task-local. Runtime/provider/
cost learning is N/A because those effects are forbidden.

## Epistemic Process Block

Expected Result / Prediction: existing command and evidence owners can support
a small future shadow receipt without duplicate command discovery or a new
store.

Evidence Comparison: compare every R4 field/token invariant, R3 invalidation
node, current autorun catalog owner, and all 12 hostile cases.

Contradiction Or Gap Disposition: duplicate catalogs/stores, worker-selected
applicability, stale receipt revival, semantic false positives, or negative
net control value require revision, narrowing, or stop.

Claim Update: one allowed R5 disposition only; no active authority changes.

## Foundation Storage Layout Block

N/A with reason: R5 must not create storage. Any proposed persistence surface
is a stop-condition finding, not an allowed output.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | documentation-only design over committed governed sources; no runtime, provider, live-proof, adapter, or selective-execution behavior is claimed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design work; no public-sync authority.

## Claim Boundary

This work order authorizes only two documentation outputs. It does not
authorize implementation, command omission, receipt persistence, standard or
checker mutation, source intake, R6-R9, T15, runtime, provider/live, public
sync, deployment, production, or destructive action.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "TPGR-R5",
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
  "pathFamilies": ["docs/baselines/", "docs/assessments/", "docs/reviews/"],
  "claims": ["bounded shadow command applicability and receipt invalidation design"],
  "requiredProof": ["R4 invariant matrix", "single command owner", "invalidation precedence", "12 hostile cases", "full legacy gate"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["protected mutation", "new intake", "selective execution", "runtime or external effects"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: accepted design evidence only; no corpus claim",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P2_BOUNDED`, selective execution false,
and `RUN_FULL_LEGACY_BUNDLE`.

## Authority Chain

Frozen doctrine -> `AGENTS.md` and active continuity -> accepted R3/R4 ->
paired R5 baseline -> this work order. Stop on conflict or expansion.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | provides standing authorization and transfers committed work order |
| worker | reads, designs exactly two outputs, runs gates, does not commit |
| reviewer/closer | independently audits semantics, repairs allowed scope, runs gates, commits accepted material |
| session-sync steward | updates active continuity separately after acceptance |

## Pre-Flight Checks

Worker must confirm exact HEAD, clean worktree, both output paths absent, paired
baseline/work order hashes readable, all required sources present, and no
forbidden path change before the first edit.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | no new intake; accepted governed R3/R4 design evidence only |
| Scope classification | documentation-only bounded command/receipt design |
| Risk sensitivity | MEDIUM, authority-sensitive and Git-reversible |
| Selected role route | routeMode=`MULTI_AGENT_SINGLE_ROLE`; dispatcher -> worker -> reviewer/closer |
| Role separation basis | worker cannot commit; reviewer independently verifies owners, applicability, invalidation, and hostile outcomes |
| Worker role | command-applicability and receipt-invalidation designer |
| Reviewer role | source, dependency graph, false-positive, cost, path, and gate reviewer |
| Escalation condition | dirty start, source contradiction, missing owner, forbidden path, new storage need, external effect, or unrepairable gate failure |
| Source authority | CVF-governed sources only; prior critique only through accepted reconciliation |
| Corpus action | none |
| Direct import | forbidden |

## Write Ownership

Worker owns only the two fulfillment-manifest outputs while uncommitted.
Reviewer owns bounded corrections and material commit. Session-sync steward
owns only active continuity after accepted material.

## Execution Plan

1. Capture clean execution base and read every required source/checker.
2. Scaffold the worker return before long-form drafting.
3. Build the complete dependency and applicability matrix before prose.
4. Author assessment, then complete worker return with actual evidence.
5. Run route check, worker-return fast gate, full pre-implementation, diff
   hygiene, and final status.
6. Return without stage/commit.

## Evidence Requirements

Provide source-section citations, exact table reconciliation counts, command
owner evidence, deterministic hostile outcomes, no-current-edit proof, exact
status, command results, and no-commit statement. Self-report is not acceptance.

## Review Gate

Reviewer independently verifies every owner, all R4 field/token rows, all
hostile cases, applicability/invalidation precedence, exact paths, and gates.

## Operator Checkpoint

No checkpoint inside this bounded R5 design. Implementation, protected
mutation, selective execution, new intake, R6+, or external effects require a
later governed boundary.

## Closure Checklist

- [ ] Execution-base worktree status captured.
- [ ] Exactly two uncommitted outputs.
- [ ] Complete R4 invariant/applicability reconciliation.
- [ ] Single canonical command owner and zero new storage.
- [ ] Invalidation and re-earning rules fail closed.
- [ ] Twelve hostile cases resolved deterministically.
- [ ] Zero-edit R6 manifest and one allowed disposition.
- [ ] Full gates pass; reviewer alone commits.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all checklist items pass. Return
`BLOCKED_WITH_REASON` for source contradiction, forbidden-path dependency,
unresolved stop condition, non-matching manifest, or gate failure that cannot
be repaired inside the two allowed paths.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: R5 does not reopen a legacy absorption row or
claim new corpus coverage; it designs routing over already accepted R3/R4
evidence. Existing legacy and absorption controls remain unchanged.
