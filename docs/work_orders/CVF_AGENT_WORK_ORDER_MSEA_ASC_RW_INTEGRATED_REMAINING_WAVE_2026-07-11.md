# CVF Agent Work Order MSEA-ASC-RW Integrated Remaining Wave

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: MSEA-ASC-RW

dispatchBaseHead: `107bece0e`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_TO_SET

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: one delegated worker executing ASC-T1 through ASC-T5 continuously.
Canonical packet: this file. Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: T0 is accepted at `9f8815fb7`.

Do-not-misread notes: phase checkpoints are evidence boundaries, not separate
review handoffs. Do not ask for review after T1/T2/T3/T4 unless blocked.

Required first actions: capture executionBaseHead/status, read T0 family and
roadmap, source-verify every protected T5 path before editing, run
pre-implementation, then execute phases in order.

Return contract: one final `COMPLETE_PENDING_REVIEW` worker return with five
terminal phase rows, or one honest `BLOCKED_WITH_REASON` when dependency-safe
continuation is impossible. No commit.

## Purpose

Complete the remaining as-built catalog roadmap in one governed worker run,
preserving truth-before-presentation and final independent review.

## Authority Chain

Operator batching authority -> MSEA-ASC roadmap -> accepted T0 contracts ->
paired ASC-RW GC-018 -> this work order -> one worker return -> reviewer/closer
final review.

## Agent Roles

- Worker: T1-T5 implementation and evidence; no commit.
- Reviewer/closer: independent semantic/negative review and material commit.
- Session-sync steward: continuity only after accepted closure.
- Operator: authorizes batching and resolves escalations.

## Scope / Target / Owner Boundary

Allowed owner families:

- `docs/reference/system_architecture_catalog/` including `entries/`, aggregate,
  README/front door, and existing T0 contracts when reconciliation is required;
- `docs/reference/system_chain/gaps/` including README, entries, and generated index;
- `governance/compat/generate_as_built_system_catalog.py`;
- `governance/compat/check_as_built_system_catalog_drift.py`;
- focused tests named for those automation files;
- `governance/compat/local_governance_hook_catalog_pre_commit.py`;
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`;
- `governance/compat/local_governance_hook_catalog_pre_push.py`;
- `governance/compat/agent_autorun_command_catalog.py`;
- `.github/workflows/documentation-testing.yml`;
- `.github/workflows/as-built-system-catalog-freshness.yml` as a new T5 output;
- `docs/reviews/CVF_MSEA_ASC_RW_INTEGRATED_REMAINING_WAVE_WORKER_RETURN_2026-07-11.md`.

Forbidden: doctrine, R91 map/README/freshness checker/standard semantics,
runtime/product/Web/provider/public-sync/legacy/session/handoff/L4 promotion,
unrelated refactor, commit, push, secrets, or live proof.

## Pre-Flight Checks

1. Confirm `git status --short` is clean at dispatch base head before starting;
   if dirty, stop and report instead of executing.
2. Capture `executionBaseHead` from the actual current `HEAD` commit hash.
3. Confirm the ASC-T0 contract family (schema, topology decisions, worker
   return) is present and readable at the paths cited in Source Verification.
4. Confirm the dispatcher-verified protected T5 paths below still match their
   cited owners before editing; any drift is a stop condition, not authority
   to select another hook, CI, or weekly path.
5. Confirm no other in-progress dispatch batch occupies the working tree
   (GC-018/work-order pair not yet committed elsewhere).

## Write Ownership

Worker owns only the allowed families and must enumerate every final file in
the actual changed set. Reviewer owns closure and session sync.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| ASC-T0 | accepted worker return and T0 family | `9f8815fb7` | SATISFIED |
| batching decision | operator instruction | 2026-07-11 | SATISFIED |

## Required First Reads

1. startup front doors and active handoff;
2. paired ASC-RW baseline and this work order;
3. MSEA-ASC roadmap and critique classification;
4. all four T0 catalog-family files;
5. module inventory, governance control matrix, doctrine route and R91 map;
6. generated aggregate, parked-lane, autorun, commit-steward, and core-guard standards;
7. exact automation/hook/workflow sources named in Source Verification before
   T5 edits; no substitute owner may be selected by the worker.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy corpus is an inventory authority. Active
catalog records must cite current governed owners; legacy is evidence-only.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | prior Claude critique -> Codex classification -> T0 -> integrated wave |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | catalog reconciliation/admission records |
| Disposition | reuse only internally accepted findings |
| Claim boundary | external review remains advisory |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T1-T5 requirements | VALUE_SET | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | Work Plan | ASC-T1 through ASC-T5 | roadmap | ACCEPT |
| schema | EXISTS | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_SCHEMA.json` | root | cvf.as_built_system_catalog.schema.v0 | T0 | ACCEPT |
| topology | VALUE_SET | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md` | Decisions 1-3 | compact source; sibling freshness; dedicated front door | T0 | ACCEPT |
| local pre-commit catalog | EXISTS | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `build_pre_commit_commands` command list | system chain map freshness command entry | local pre-commit hook catalog | ACCEPT |
| local reviewer-fast catalog | EXISTS | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `build_reviewer_fast_commands` command list | system chain map freshness command entry | reviewer-fast hook catalog | ACCEPT |
| local pre-push catalog | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | pre-push command list | system chain map freshness command entry | local pre-push hook catalog | ACCEPT |
| autorun catalog | EXISTS | `governance/compat/agent_autorun_command_catalog.py` | pre-dispatch/pre-implementation command catalog | system chain map freshness command entry | agent autorun command catalog | ACCEPT |
| documentation CI owner | EXISTS | `.github/workflows/documentation-testing.yml` | system-chain-map-freshness job | Enforce system chain map freshness guard | documentation workflow | ACCEPT |

## New Doc/Implementation Fields And Paths

The two reserved T5 automation paths are new authorized output, not existing
source, and are therefore excluded from the Source Verification `ACCEPT` rows
above.

| Path | Disposition | Authorizing contract |
|---|---|---|
| `governance/compat/generate_as_built_system_catalog.py` | NEW_AUTHORIZED_OUTPUT | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md` Reserved future paths; Core Guard Self-Protection Authorization below |
| `governance/compat/check_as_built_system_catalog_drift.py` | NEW_AUTHORIZED_OUTPUT | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md` Reserved future paths; Core Guard Self-Protection Authorization below |
| `.github/workflows/as-built-system-catalog-freshness.yml` | NEW_AUTHORIZED_OUTPUT | T0 Decision 2 distinct weekly wiring without modifying the R91-owned weekly workflow |

## Current Runtime Freshness Verification

N/A with reason: catalog/governance metadata; no runtime claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_system_chain_map_freshness.py` |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; phase terminality; exact actual manifest; protected paths; closure fields; NEW_AUTHORIZED_OUTPUT; Scaffold Provenance Block fields |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | integrated-wave dispatch only |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | Execute ASC-T1-T5 continuously and return once. |
| Scope classification | BOUNDED_INTEGRATED_GOVERNED_WAVE |
| Risk sensitivity | R2 |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; one worker then independent reviewer/closer. |
| Role separation basis | worker no commit; reviewer/closer performs final review |
| Escalation condition | schema contradiction, authority expansion, R91 change, or forbidden scope |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> one integrated worker -> independent reviewer/closer -> session-sync steward |
| phase | dispatch-to-worker-to-final-review |
| baseHeadFor(phase) | dispatchBaseHead=107bece0e; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | allowed owner families only; exact files enumerated in final return |
| traceScope(phase, actor) | per-phase ledger plus final exact manifest and commands |
| commitOwner(phase) | worker none; reviewer material; steward session |
| crossBatchIsolation | clean worktree at executionBaseHead required; unrelated changes prohibited |
| nextMoveSurfaces | updated only after final accepted closure |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | reviewer/closer | governed repository | final acceptance/commit | negative tests, reconciliation, gates | ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | integrated worker | local tools | no commit or scope widening | phase ledger and final return | ALLOWED_BOUNDED_NO_COMMIT |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_ASC_RW_INTEGRATED_REMAINING_WAVE_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: accepted wave outputs under the allowed owner
families listed in Scope / Target / Owner Boundary, plus the completion
review itself and separate session sync.

closureOwner: reviewer/closer.

workerCommitPermission: FORBIDDEN

## Roadmap-to-Work-Order Trace Matrix

| Phase | Required terminal output |
|---|---|
| T1 | complete plane/module inventory or terminal exclusions |
| T2 | interface/edge graph with proof class, recency, visibility |
| T3 | gap entries, README, deterministic JSON index/generator |
| T4 | human front door/diagram linked by catalog edge IDs |
| T5 | scoped sibling freshness/admission generator/checker/tests/wiring |

## Work-Order Fulfillment Manifest

Final worker return must enumerate all files individually, counts by entity and
gap status, generated aggregate hash, graph edge counts by proof class, gap
README/index reconciliation, diagram edge-ID reconciliation, checker/test/wiring
evidence, and unchanged forbidden paths.

## Worker Return Packet Shape Contract

Worker return path:

`docs/reviews/CVF_MSEA_ASC_RW_INTEGRATED_REMAINING_WAVE_WORKER_RETURN_2026-07-11.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must contain the following standard sections, in addition to
the header fields required by contract profile above:

- Status
- executionBaseHead
- dispatchWorkOrder
- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Checker Source Read-Ahead Block
- Integrated Phase Ledger
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package
- Public Export Disposition
- Claim Boundary
- exact changed files
- command evidence
- `git status --short`
- no-commit statement

## Execution Plan

1. T1 inventory and schema validation.
2. T2 edge tracing; no file-existence promotion.
3. T3 gap terminalization and deterministic generation.
4. T4 human projection only from validated catalog IDs.
5. T5 protected implementation after fresh local source verification.
6. Run full reconciliation/gates and return once without commit.

## Evidence Requirements

Each phase must emit a terminal checkpoint ledger in the final worker return.
The following commands must be run, with output evidence recorded for each in
the worker return:

- JSON Schema validation with positive/negative fixtures;
- generator run twice for byte stability;
- aggregate/index drift checks;
- focused automation tests for the two new T5 files;
- `python governance/compat/check_system_chain_map_freshness.py`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- reviewer-fast gate;
- `git diff --check`;
- `git status --short`.

## Verification Commands

Run the following, recording output evidence for each in the worker return:

- JSON Schema validation with positive/negative fixtures;
- generator run twice for byte stability;
- aggregate/index drift checks;
- focused automation tests for the two new T5 files;
- `python governance/compat/check_system_chain_map_freshness.py`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- reviewer-fast gate;
- `git diff --check`;
- `git status --short`.

## Acceptance Criteria

- All active in-scope owners terminally cataloged or excluded with reason.
- Every edge has highest proven class, evidence recency, and visibility.
- Gap README/index/entries reconcile deterministically.
- Every diagram edge resolves to a catalog edge ID.
- Freshness sibling does not fingerprint or rewrite R91-owned artifacts.
- New/changed catalog sources trigger deterministic drift/admission checks.
- T1-T5 phase ledger terminal; exact changed set; no commit.

## Worker Autonomy / No-Question Rule

Repair allowed-scope defects and continue across phase-local issues when later
work remains truthful. Ask no routine questions. Stop only on authority/schema
contradiction or required forbidden expansion.

## Negative And Fail-Condition Scan

Fail on owner creation for diagram completeness, proof inflation, CI-only as
direct operator visibility, non-terminal gaps, free-text-only parked triggers,
aggregate-only edits, non-determinism, R91 semantic mutation, or false claims.

## Review Gate

One `COMPLETE_PENDING_REVIEW` at wave end. Reviewer/closer independently
recomputes representative inventory/edge/gap/generation/admission claims
before acceptance.

## Closure Checklist

- [x] T1-T5 each has a terminal phase disposition.
- [x] Every changed file is individually enumerated.
- [x] Catalog source records and generated aggregate reconcile.
- [x] Gap entries, README and JSON index reconcile.
- [x] Diagram/front-door edges resolve to catalog edge IDs.
- [x] Freshness/admission checker and focused tests pass.
- [x] R91-owned semantics remain unchanged.
- [x] Forbidden paths remain unchanged.
- [x] Worker did not commit.
- [x] Final status truthfully reflects dirty worktree.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only when the remaining dependency chain cannot
proceed without new authority. Record completed phase evidence even when blocked.

## Operator Checkpoint

No intermediate checkpoint. Final reviewer/closer review is mandatory.

## Foundation Storage Layout Block

| Surface | Path | Authority disposition |
|---|---|---|
| Catalog owner | `docs/reference/system_architecture_catalog/` | editable authority (compact source) |
| Compact catalog records | `docs/reference/system_architecture_catalog/entries/` | editable authority (compact source) |
| Catalog aggregate | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json` | generated output |
| Gap front door | `docs/reference/system_chain/gaps/README.md` | editable authority (compact source) |
| Gap source entries | `docs/reference/system_chain/gaps/entries/` | editable authority (compact source) |
| Gap index | `docs/reference/system_chain/gaps/CVF_SYSTEM_CHAIN_GAP_INDEX.json` | generated output |
| Generator | `governance/compat/generate_as_built_system_catalog.py` | new authorized output (T5) |
| Freshness/drift checker | `governance/compat/check_as_built_system_catalog_drift.py` | new authorized output (T5) |
| Worker return | `docs/reviews/CVF_MSEA_ASC_RW_INTEGRATED_REMAINING_WAVE_WORKER_RETURN_2026-07-11.md` | worker-authored deliverable |
| Completion review | `docs/reviews/CVF_MSEA_ASC_RW_INTEGRATED_REMAINING_WAVE_COMPLETION_2026-07-11.md` | reviewer-authored deliverable |

Compact catalog/gap source records (entries, README) are editable authority;
the aggregate JSON and gap index JSON are generated derived views rebuilt from
that authority by the T5 generator, not hand-edited.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-ASC-RW --title "Integrated Remaining Wave" --date 2026-07-11 --base 107bece0e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | all normative content authored/repaired manually against source-verified checker requirements after scaffold review |
| checkerReadAheadConfirmation | applicable `governance/compat/check_*.py` sources read before authoring; see Checker Source Read-Ahead Block |
| docOnlyNewFields | reserved T5 generator/checker paths recorded in New Doc/Implementation Fields And Paths table, not as Source Verification ACCEPT rows |
| claimBoundary | scaffold/text-generation provenance only; no runtime or automatic-invocation claim |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Actor | integrated worker (single delegated agent) |
| Provider or surface | local CLI/MCP execution surface assigned at dispatch |
| Session or invocation | worker to record actual session/invocation identifier at execution time |
| Working directory | repository root at `107bece0e` |
| Command or tool surface | local repository read/write tools; governance/compat checkers; no live provider calls |
| Target paths | allowed owner families listed in Scope / Target / Owner Boundary |
| Allowed scope source | this work order's Scope / Target / Owner Boundary and Write Ownership sections |
| Before status evidence | clean worktree at executionBaseHead required; worker records `git status --short` output before first edit |
| After status evidence | worker records `git status --short` output after final edit, before return |
| Diff evidence | worker records `git diff --stat` and per-file summary in the final return |
| Approval boundary | worker may not commit; reviewer/closer holds commit authority |
| Claim boundary | phase-ledger and exact-manifest evidence only; no runtime/provider claim |
| Agent type | single delegated worker agent (provider-neutral) |
| Invocation ID | worker to record actual invocation ID at execution time |
| Expected manifest | allowed owner families and exact T5 wiring paths enumerated above; exact created catalog/gap entry paths finalized in worker return |
| Actual changed set | worker to enumerate every changed file individually in the final return |
| Manifest delta | worker to record MATCH or itemized delta in the final return |
| Deletion or rename disposition | none expected; worker records N/A with reason if no deletion/rename occurs, or itemized disposition if one does |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | ASC-T1-T5 integrated architecture catalog wave |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT: no runtime receipt applies` |
| actionEvidence | `ACTION_EVIDENCE_PRESENT: inventory, edge graph, gap ledger, projection, deterministic generation, focused tests, wiring proof, and governance gates` |
| invocationBoundary | repository architecture/governance metadata only |
| interceptionBoundary | no provider/runtime/Web interception |
| claimLanguage | as-built catalog evidence, not universal runtime readiness |
| forbiddenExpansion | no doctrine, R91 semantics, runtime, public, provider, L4 promotion, session, commit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance integrated wave.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: T5 protected automation creation only,
scoped to the two reserved paths, their focused tests, the five exact existing
catalog/workflow owners source-verified above, and one exact new weekly path.

Protected paths:

- `governance/compat/generate_as_built_system_catalog.py`
- `governance/compat/check_as_built_system_catalog_drift.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `.github/workflows/documentation-testing.yml`
- `.github/workflows/as-built-system-catalog-freshness.yml`

T5 may create the two reserved automation paths, the exact new weekly workflow,
and focused tests, and may edit only the five exact existing owners listed
above. No other protected path is authorized. If any cited owner has drifted,
wiring is a terminal `BLOCKED_WITH_REASON` rather than a guessed substitute.

Operator authorization: integrated ASC remaining wave. Rollback boundary:
revert the ASC-RW protected diff only; R91 remains unchanged.

## Claim Boundary

This work order consolidates T1-T5 execution and removes intermediate review
ceremony. It does not weaken phase evidence, final independent review, or scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_ASC_RW_INTEGRATED_REMAINING_WAVE_COMPLETION_2026-07-11.md` | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Registry JSON | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json` | deterministic generated aggregate | PASS |
| Registry Markdown | `docs/reference/system_architecture_catalog/README.md` | stable-ID front door | PASS |
| External evidence digest | N/A with reason: no new external evidence | governed internal citations only | N/A with reason |
| System loop interlock | N/A with reason: no system-loop action | no invocation or bypass claim | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V41_2026-07-11.md` | closed mode and next move | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| T1-T5 terminality | five PASS rows | PASS |
| Catalog and gap determinism | repeated hashes match | PASS |
| Freshness ownership | ASC CURRENT; R91 CURRENT | PASS |
