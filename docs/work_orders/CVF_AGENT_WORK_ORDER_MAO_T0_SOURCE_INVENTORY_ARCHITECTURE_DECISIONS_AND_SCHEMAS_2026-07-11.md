# CVF Agent Work Order - MAO-T0 Source Inventory, Architecture Decisions, And Schemas

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-11

Batch ID: MAO-T0-DISPATCH

dispatchBaseHead: `636f9639f`

executionBaseHead: `209a9b4b3`

closureBaseHead: `209a9b4b3`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex

## Dispatch Prompt Envelope

Role: delegated worker for MAO-T0.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T0_SOURCE_INVENTORY_ARCHITECTURE_DECISIONS_AND_SCHEMAS_2026-07-11.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture exact HEAD before any edit and record it in the worker return.

Current-time notes: artifact date is 2026-07-11; capture execution HEAD at start.

Do-not-misread notes: this is docs/schema contract work, not orchestration runtime implementation. Do not spawn subagents, call providers, commit, change session state, or touch public-sync.

Required first actions: complete startup reads, capture HEAD/status, read the paired baseline and checker sources, then source-verify before editing.

Return contract: create the named worker return, run required verification, leave all work uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce the MAO-T0 source inventory, overlap decisions, architecture contract,
schemas, lifecycle model, and threat/failure model needed before MAO-T1.

## Authority Chain

1. `AGENTS.md` and active session front doors.
2. Paired GC-018 baseline.
3. MAO roadmap and accepted critique reconciliation.
4. Active AHB and agent-workspace contracts.
5. Current runtime source for existing facts only.
6. Archived MA1/W2 artifacts as evidence history only.

## Agent Roles

- delegated worker: source verification, authoring, tests/validation, worker return; no commit.
- independent reviewer: designated closer, repair/acceptance decision, material commit.
- Session-sync steward: separate post-closure phase only.

## Scope / Target / Owner Boundary

### Allowed deliverables

- `docs/reference/multi_agent_orchestration/README.md`
- `docs/reference/multi_agent_orchestration/CVF_MAO_T0_SOURCE_INVENTORY_AND_OVERLAP_DECISIONS.md`
- `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`
- `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json`
- `docs/reviews/CVF_MAO_T0_SOURCE_INVENTORY_ARCHITECTURE_DECISIONS_AND_SCHEMAS_WORKER_RETURN_2026-07-11.md`

### Forbidden scope

No TypeScript/Python runtime, queue, scheduler, provider adapter implementation,
live call, UI, package lifecycle, checker/hook/CI wiring, generated workspace
state, active session state, roadmap mutation, ASC/R91 semantic change, public
sync, L4, R84, or R73F change.

## Write Ownership

Worker may change exactly the five allowed deliverables. Existing source and
governance files are read-only. Any required sixth path returns to orchestrator.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| Roadmap | `6a08a041e`; MAO roadmap PROPOSED | SATISFIED |
| Critique reconciliation | `d61c3c92c`; `INTERNAL_RECONCILIATION_ACCEPTED_WITH_T0_CAVEATS` | SATISFIED |
| Reopen audit | R94 terminal and R95 accepted in active state | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T0 --title "MAO Source Inventory Architecture Decisions And Schemas" --date 2026-07-11 --base a2907dbed --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | all placeholders replaced with MAO-T0 source-backed controls |
| checkerReadAheadConfirmation | named checker sources read before authoring |
| docOnlyNewFields | all new MAO fields must be listed in the contract's New Doc-Only Fields table |
| claimBoundary | dispatch provenance only |

## Required First Reads

Read startup sequence, guard orientation, literal gotchas, repository boundary,
paired baseline, this work order, MAO roadmap, reconciliation, AHB front door and
ratification, workspace front door/topology/taxonomy/runtime-expansion contract,
archived MA1 standard, W2-T9/W2-T14 plans, existing coordination/runtime sources,
provider router sources found by repo search, commit-steward standard, and ASC/gap
front doors before writing.

## Pre-Flight Checks

Capture `git rev-parse --short HEAD`, `git status --short`, confirm the five
allowed paths, verify no collision, and stop if HEAD is not the committed dispatch
HEAD supplied by the orchestrator handoff.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker failures directly by reading the failing checker.
Return only for source contradiction, forbidden-path need, or missing authority.

## Source Verification Block

Use the paired baseline table. Add a complete source inventory in the T0 output
with one row per existing owner/symbol and an allowed source disposition. New schema fields belong in a separate New Doc-Only
Fields table and must not be presented as existing runtime facts.

## Negative Search And Collision Discipline

Run `Test-Path` for planned outputs and `rg` for MAO contract/schema names.
Record every collision and authority disposition in the inventory.

## Current Runtime Freshness Verification

Re-run repo-wide searches at execution start. Explicitly prove the zero non-test
caller status of `MultiAgentRuntime`, the absence of closer tokens in the
commit-steward standard, the AHB closer owner, concrete provider-router paths,
and the absence of a MAO-specific ADIF defect baseline.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-contract`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/check_agent_workspace_runtime_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, source verification, AHB block, workspace block, reviewer closure conversion, worker return contract |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | packet compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: bounded documentation/schema foundation with no runtime mutation.

Scope classification: DOCS_SCHEMA_CONTRACT_ONLY.

Risk sensitivity: MEDIUM because authority and lifecycle schemas affect later runtime work.

Escalation condition: source contradiction, forbidden path, or unresolved authority owner.

## Agent Handoff Contract Control Block

Contract source: canonical contract, not archive:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | executionBaseHead captured by worker at start |
| changedSetScope(phase) | exactly five allowed deliverables |
| traceScope(phase, actor) | delegated worker execution trace covers only worker changed set |
| commitOwner(phase) | nobody during execution; Codex at CLOSURE |
| crossBatchIsolation | one batch in this clean worktree; Before status evidence: clean worktree |
| Before status evidence | clean worktree at dispatchBaseHead |
| nextMoveSurfaces | worker must not edit; session-sync steward owns after reviewer acceptance |

## Agent Workspace Design Control Block

Contract sources, active and not archive: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` and
`docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`.

| Field | Value |
|---|---|
| Workspace purpose | analyze relationship only; no workspace build |
| Contract source | active AHB and workspace topology/runtime-expansion contracts |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | N/A with reason: no workspace state or runtime storage created |
| Handoff fields | route, rolePattern, phase, base heads, changed set, trace, commit owner |
| State ownership | MAO event ledger decision is doc-only; existing workspace generated state remains projection owner |
| Guard owner | existing workspace design/runtime-boundary guards |
| Build boundary | documentation/schema only; no runtime source, provider proof, public-sync, registry edits, runtime queue, or generated workspace state mutation |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MAO_T0_SOURCE_INVENTORY_ARCHITECTURE_DECISIONS_AND_SCHEMAS_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: completion review, allowed repairs to worker outputs,
baseline/work-order closure conversion, roadmap status only if closure evidence
supports it, and separate session-sync paths after material commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap T0 requirement | Worker output |
|---|---|
| source inventory and overlap | source inventory/overlap decisions document |
| architecture decisions and active front door | README plus foundation contract |
| task graph/event/receipt/capability/authority/read-model schemas | JSON Schema and contract tables |
| lifecycle/state transitions | contract transition matrix |
| storage/retention and threat/failure model | contract decisions and negative model |
| three reconciliation caveats | explicit compatibility/authority/ADIF caveat sections |

## Work-Order Fulfillment Manifest

Exactly five worker-owned outputs. Four material reference/schema artifacts plus
one worker return. No optional files.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must state `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`,
executionBaseHead, exact changed paths, source-verification summary, commands and
results, unresolved dissent, claim boundary, and explicit `WORKER_MUST_NOT_COMMIT` confirmation.

## Execution Plan

1. Inventory current owners and historical overlaps.
2. Record REUSE/ADAPT/REJECT decisions and the three critique caveats.
3. Define immutable authority graph, event/receipt ledger, generated read model,
   role resolver ownership, provider-neutral port, lifecycle and closer boundary.
4. Define JSON Schema with explicit new fields, invariants, terminal propagation,
   retry/cancel/idempotency, budget and receipt shapes.
5. Validate schema and cross-document references; write worker return.

## Verification Commands

- JSON parse and Draft schema self-validation using available local tooling.
- `rg` source/collision searches recorded in evidence.
- `python governance/compat/check_agent_workspace_runtime_boundary.py --enforce`
- `python governance/compat/check_governed_file_size.py --enforce`
- `git diff --check`
- `python governance/compat/run_worker_return_fast_gate.py`
- applicable pre-implementation autorun gate on the real execution range.

## Acceptance Criteria

- Four material outputs and one worker return exist, no extra paths.
- Every existing fact is source-verified; every new field is doc-only new.
- All roadmap architecture decisions are resolved without placeholder language.
- Three critique caveats are folded exactly with calibrated evidence weight.
- Task lifecycle, roles, reviewer isolation, revision, closer, recovery, receipts,
  budgets, human checkpoints, projection, freshness, and catalog admission are
  machine-testable contract statements.
- No runtime/provider/queue/public/session mutation or production claim occurs.

## Evidence Requirements

Command-backed source searches, JSON/schema validation, exact changed-set proof,
gate results, and explicit N/A with reason for non-applicable proof.

## Negative And Fail-Condition Scan

Fail on provider hardcoding, worker-as-reviewer authority, multiple closers,
automatic commit, workspace-as-runtime-truth, unlimited retry/revision/fan-out,
missing terminal propagation, guessed source field, archive promotion, or any
changed path outside the fulfillment manifest.

## Review Gate

Codex independently re-runs source searches, validates schema semantics and
negative cases, classifies worker dissent, repairs only within allowed scope,
and alone decides acceptance/commit.

## Closure Checklist

- [x] Exactly five worker outputs reviewed.
- [x] Every source fact and new field classified.
- [x] Schema and negative cases validated.
- [x] No forbidden path or runtime claim present.
- [x] Worker return fast gate passes.
- [x] Reviewer authors completion review and owns commit.

## Return-To-Orchestrator Conditions

Return only for source contradiction, missing canonical authority, required
forbidden path, or a schema decision whose alternatives materially change MAO
architecture beyond the roadmap decisions.

## Operator Checkpoint

N/A with reason: operator authorized creation of this MAO-T0 work order; no
runtime or public checkpoint is crossed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local private provenance repository |
| Session or invocation | MAO-T0 execution |
| Working directory | repository root |
| Command or tool surface | read/search/edit/local validation only |
| Target paths | five allowed deliverables |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | clean worktree; `git status --short` empty at executionBaseHead |
| After status evidence | uncommitted worker outputs plus return |
| Diff evidence | git status and diff name-status |
| Approval boundary | no commit; reviewer acceptance required |
| Claim boundary | T0 docs/schema only |
| Agent type | worker |
| Invocation ID | mao-t0-delegated-worker-2026-07-11 |
| Expected manifest | five allowed deliverables |
| Actual changed set | worker records at return |
| Manifest delta | worker records MATCH or BLOCKED |
| Deletion or rename disposition | N/A with reason: none authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T0 contract/schema work.

## Claim Boundary

This work order authorizes the delegated worker to produce MAO-T0 documentation and schemas
without committing. It does not authorize runtime implementation, provider/live
proof, agent spawning, queue/scheduler, UI, package, checker/hook, session state,
public-sync, ASC/R91 semantic, L4, R84, R73F, or production-readiness work.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation root | `docs/reference/multi_agent_orchestration/` |
| Stable front door | `docs/reference/multi_agent_orchestration/README.md` |
| Durable source files | inventory/decision Markdown, contract Markdown, JSON Schema |
| Generated aggregate | N/A with reason: T0 defines schema only and creates no aggregate |
| Generator/checker | N/A with reason: no generator or checker authorized |
| Index update | README indexes all three sibling T0 artifacts |
| Public boundary | provenance only; no public-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | critique reconciliation | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | PROPOSED | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate current; no T0 registration required | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | current companion retained | PASS |
| External evidence digest | critique reconciliation | sha256 `E7392BC13A7F56E8647E94D091B5F76BB8EA3D67ACCF4245EE0E150A5354726D` | PASS |
| System loop interlock | R91/ASC freshness | CURRENT | PASS |
| Session continuity | active front doors | dispatch authoring current | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | Evidence field | Required value | Observed value | Status |
|---|---|---|---|---|---|
| MAO-T0-Q1 | reconciliation | verdict | accepted with T0 caveats | accepted with T0 caveats | PASS |
