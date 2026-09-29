# CVF Agent Work Order - ODVR-T1 Deterministic Local Composer

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-12

Batch ID: ODVR-T1-DISPATCH

dispatchBaseHead: `ef8702226`

executionBaseHead: `f3a9a7699`

closureBaseHead: `f3a9a7699`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: independent reviewer

## Dispatch Prompt Envelope

Role: delegated worker for ODVR-T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_2026-07-12.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture exact HEAD before editing and record it in the return.

Current-time notes: artifact date is 2026-07-12; refresh source paths, generated
state drift, and commit resolution from execution HEAD.

Do-not-misread notes: implement a local read-only projection, not a control
plane. Do not spawn subagents, commit, edit session state, add UI/Web routing,
call providers, publish, or absorb outside sources.

Required first actions: startup reads, HEAD/status capture, paired packet,
ODVR T0 contract/schema, relevant source and checker reads, ADIF query rerun,
then pre-implementation gate.

Return contract: leave all changes uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the narrowed T1 composer that deterministically projects canonical
session/material-decision evidence to T0-schema-valid JSON without mutation or
duplicating narrower MAO, MLW, and workspace summaries.

## Authority Chain

1. `AGENTS.md` and active session front doors.
2. Paired T1 baseline and this work order.
3. T0 completion review, active contract, and JSON Schema.
4. Current generated state and current runtime/read-model sources.
5. Canonical AHB contract and commit-steward standard.

## Agent Roles

- delegated worker: implementation, tests, evidence, worker return; no commit.
- independent reviewer: adversarial review, allowed repair, closer, commit owner.
- session-sync steward: separate continuity phase following material closure.

## Scope / Target / Owner Boundary

### Allowed deliverables

- `governance/compat/run_odvr_readout.py`
- `governance/compat/test_run_odvr_readout.py`
- `docs/reference/operator_decision_value_readout/README.md`
- `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_WORKER_RETURN_2026-07-12.md`

### Forbidden scope

No edit to generated/session state, T0 contract/schema, roadmap, baseline/work
order, MAO/MLW/workspace owners, Web/UI/routes, checker/hook/CI catalogs,
provider/API, public-sync, queue, registry, T2 proof, or outside-source intake.

## Write Ownership

Worker may change exactly the four allowed deliverables. Any required fifth
path returns to orchestrator.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T0 accepted contract | completion `REVIEWER_ACCEPTED_AFTER_REPAIR`; `2af788683` | SATISFIED |
| T0 schema invariants | four examples valid and four reviewer negatives rejected | SATISFIED |
| Session release | `ef8702226`; T1 packet authoring eligible | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id ODVR-T1 --title "Operator Decision And Value Readout Deterministic Local Composer" --date 2026-07-12 --base ef8702226 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: ODVR-T0 REVIEWER_ACCEPTED_AFTER_REPAIR at material commit 2af788683" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-backed T1 manifest, invariants, tests, and no-mutation controls |
| checkerReadAheadConfirmation | named checker sources read before authoring |
| docOnlyNewFields | none; output must conform to existing T0 schema |
| claimBoundary | dispatch provenance only |

## Required First Reads

Read startup/guard/literal-gotcha sequence, paired baseline/work order, ODVR
roadmap, T0 completion/contract/schema, active state generator and generated
state, canonical AHB ratification, commit steward, and relevant checker sources.

## Pre-Flight Checks

Capture HEAD/status, confirm clean post-sync HEAD, run `Test-Path` and semantic
`rg` for planned helper symbols, rerun ADIF, then run pre-implementation gate.

## Worker Autonomy / No-Question Rule

Repair allowed-scope test and gate failures. Return only for source
contradiction, forbidden-path need, or inability to implement T0 invariants
without guessing.

## Source Verification Block

Use the paired baseline table and independently refresh every source. No field
outside the T0 schema may be emitted. Treat all generated state as read-only.

## Negative Search And Collision Discipline

| Field | Evidence |
|---|---|
| Exact search command | `rg -n -i --glob '*.py' --glob '*.ts' --glob '*.md' --glob '*.json' -- 'run_odvr_readout|build_odvr_readout|ODVR' governance EXTENSIONS docs CVF_SESSION .private_reference` |
| Exact roots | governance, runtime source/tests, docs, JSON state, and private evidence |
| Same-token collisions | ODVR packet/reference/session occurrences are authoritative context; narrower readouts are non-authoritative for full T1 ownership |
| Planned path disposition | `run_odvr_readout.py` and focused test path are clear at dispatch; worker refreshes before editing |

## Current Runtime Freshness Verification

Re-run symbol/path searches at execution start. Verify generated-state drift
before composing. Selection must use highest eligible numeric `stateOrder`
whose object carries a resolvable `materialCommit` plus a governed artifact
path. Filesystem dates, mtimes, directory order, and handoff prose are forbidden
selection authority.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-read-model`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Worker rerun command: `python governance/compat/run_adif_defect_resolver.py --task-class runtime-read-model --role dispatcher --lifecycle-phase pre-dispatch --surface-selector governance/compat --risk-ceiling HIGH --max-results 20 --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, source verification, AHB, trace, CLI boundary, worker-return shape |
| gateRunPurpose | confirmatory evidence after source-backed authoring |
| claimBoundary | packet compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: bounded local deterministic projection over canonical CVF
state and governed material-decision evidence.

Scope classification: LOCAL_READ_ONLY_COMPOSER.

Risk sensitivity: MEDIUM because false selection/freshness could mislead the
operator even without mutation.

Escalation: source contradiction, forbidden path, or non-deterministic owner
selection.

## Agent Handoff Contract Control Block

Contract source: canonical contract, not archived handoff authority:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | executionBaseHead captured at start |
| changedSetScope(phase) | exactly four allowed deliverables |
| traceScope(phase, actor) | worker trace covers only worker changed set |
| commitOwner(phase) | nobody during execution; independent reviewer at CLOSURE |
| crossBatchIsolation | clean worktree and one batch only |
| Before status evidence | clean status at executionBaseHead |
| nextMoveSurfaces | worker must not edit; session steward owns following reviewer acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md`

reviewerOwnedClosurePaths: completion review, allowed repairs, baseline/work
order closure conversion, roadmap tranche disposition if supported, material
commit, and separate session sync.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap T1 requirement | Implementation/evidence |
|---|---|
| deterministic read-only composer | pure callable accepts injected state and repository evidence adapter |
| local CLI-readable JSON | `run_odvr_readout.py --json` writes JSON to stdout only |
| current/stale/missing/contradicted behavior | focused positive and negative tests |
| no duplicate narrow summaries | omit MAO/MLW/workspace summary payloads; link only through source anchors when consulted |
| no mutation | tests assert input/files unchanged and CLI has no write path |
| T0 schema conformity | validate emitted fixtures against the committed schema |

## Work-Order Fulfillment Manifest

Exactly four worker-owned outputs: helper, focused test, front-door update, and
worker return. No optional files.

## Required Artifact Manifest

| Path | Owner | Required disposition |
|---|---|---|
| `governance/compat/run_odvr_readout.py` | worker | implemented and reviewer accepted |
| `governance/compat/test_run_odvr_readout.py` | worker | 22 reviewer-expanded tests pass |
| `docs/reference/operator_decision_value_readout/README.md` | worker | local usage pointer updated |
| `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_WORKER_RETURN_2026-07-12.md` | worker | COMPLETE_PENDING_REVIEW converted by reviewer |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Return must include executionBaseHead, exact changed paths, tests/gates,
source/freshness evidence, unresolved dissent, claim boundary, and
`WORKER_MUST_NOT_COMMIT honored`.

## Implementation Contract

1. Expose a pure `build_odvr_readout`-equivalent callable with injected state,
   artifact reader, commit resolver, and generated-state freshness result.
2. Select the highest eligible numeric `stateOrder`; eligibility requires
   `materialCommit` plus one governed artifact path. Equal-order disagreement
   produces `CONTRADICTED` with both anchors.
3. A missing path or unresolved commit produces `MISSING_SOURCE`. A generated
   drift or recorded-status/artifact-status mismatch produces `STALE`.
4. Precedence is `MISSING_SOURCE`, then `CONTRADICTED`, then `STALE`, then
   `CURRENT`.
5. Extract only explicit governed `Status:` and `## Claim Boundary` content.
   Never infer a value verdict or reopen condition from arbitrary prose.
6. CLI loads only repository-local canonical paths, writes nothing, prints
   secret-safe JSON, and exits nonzero only for invocation/input failure; a
   valid MISSING_SOURCE/CONTRADICTED readout remains valid JSON output.

## Execution Plan

1. Build the pure injected composer and result helpers.
2. Add the local read-only CLI over canonical repository inputs.
3. Add focused positives, adversarial negatives, schema validation, and no-write proof.
4. Update the ODVR front door and create the checker-safe worker return.

## Verification Commands

- `python -m unittest governance.compat.test_run_odvr_readout -v`
- JSON Schema validation for CURRENT/STALE/MISSING_SOURCE/CONTRADICTED outputs.
- negatives for equal-order conflict, unresolved commit, absent artifact,
  status mismatch, generator drift, malformed stateOrder, missing material
  commit, no eligible entry, and no-write behavior.
- CLI smoke using current repository state with secrets scan.
- `python governance/compat/run_worker_return_fast_gate.py`
- `python governance/compat/check_governed_file_size.py --enforce`
- `git diff --check`
- pre-implementation autorun on real range.

## Acceptance Criteria

- Exactly four allowed outputs, no extra path.
- Deterministic output for identical injected inputs.
- Output validates against T0 schema.
- Selection and freshness follow the reviewer-corrected contract exactly.
- All negative states retain required evidence anchors.
- No MAO/MLW/workspace payload duplication.
- No file/state mutation, provider call, UI route, public action, or value claim.
- Required worker-return fast gate passes before return.

## Evidence Requirements

Exact HEAD/status, source/collision searches, focused unittest results, four
schema-state proofs, CLI smoke JSON, no-write evidence, secrets scan, exact
changed-set evidence, and required governance gates.

## Negative And Fail-Condition Scan

Fail on filesystem-date selection, silent precedence, inferred free-prose
verdict, missing evidence anchor, schema-invalid output, nondeterminism, state
write, broad scanner, UI/provider/public work, extra path, or skipped fast gate.

## Review Gate

The independent reviewer reruns tests, adds adversarial fixtures, checks no-
write behavior, validates current CLI JSON, inspects secret safety, and alone
decides acceptance and commit.

## Return-To-Orchestrator Conditions

Return only for canonical-source contradiction, forbidden-path need, inability
to meet schema invariants deterministically, or required authority expansion.

## Operator Checkpoint

N/A with reason: operator authorized this T1 work order; no UI, provider,
public, state-mutation, or outside-source checkpoint is crossed.

## Closure Checklist

- [x] Exact four-output manifest reviewed.
- [x] Positive and negative tests pass.
- [x] T0 schema validation passes.
- [x] No mutation or duplicate-owner behavior exists.
- [x] Worker-return fast gate passes.
- [x] Reviewer completion and material commit prepared.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local private provenance repository |
| Session or invocation | ODVR-T1 execution |
| Working directory | repository root |
| Command or tool surface | read/search/edit/local Python tests only |
| Target paths | four allowed deliverables |
| Allowed scope source | paired baseline and this work order |
| Before status evidence | clean worktree at executionBaseHead |
| After status evidence | uncommitted worker outputs plus return |
| Diff evidence | status and diff name-status |
| Approval boundary | no commit; reviewer acceptance required |
| Claim boundary | local read-only T1 only |
| Agent type | worker |
| Invocation ID | odvr-t1-delegated-worker-2026-07-12 |
| Expected manifest | four allowed deliverables |
| Actual changed set | worker records at return |
| Manifest delta | worker records MATCH or BLOCKED |
| Deletion or rename disposition | N/A with reason: none |

## MCP / CLI Adapter Boundary

The CLI is a local read-only presentation adapter over the pure composer. It
does not expose MCP, network, provider, shell execution, write, approval,
dispatch, or autonomous action authority.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation root | `docs/reference/operator_decision_value_readout/` plus local helper under `governance/compat/` |
| Stable front door | `docs/reference/operator_decision_value_readout/README.md` |
| Durable source files | T0 contract/schema remain unchanged; T1 helper is local read-only implementation |
| Generated aggregate | N/A with reason: T1 creates no stored aggregate |
| Generator/checker | helper is manually invoked and not wired as a blocking checker |
| Index update | existing README gains T1 helper/test usage pointer |
| Public boundary | provenance only; no public-sync |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local implementation dispatch; no public artifact authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Baseline | `docs/baselines/CVF_GC018_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_2026-07-12.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md` | `Status: REVIEWER_ACCEPTED_AFTER_REPAIR` | PASS |
| Roadmap state | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | `PROPOSED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no mutation; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no mutation required | PASS |
| External evidence digest | N/A with reason: internal local implementation | no external evidence | N/A with reason |
| System loop interlock | current ODVR contract and schema | deterministic read-only boundary retained | PASS |
| Session continuity | separate session-sync after material commit | not part of material batch | N/A with reason |

## Claim Boundary

This work order authorizes the exact T1 helper/test/front-door/return manifest
without worker commit. It does not authorize UI, Web route, provider/live,
state mutation, autonomous selection, agent dispatch, public-sync, T2 value
proof, outside-source intake, or production readiness.
