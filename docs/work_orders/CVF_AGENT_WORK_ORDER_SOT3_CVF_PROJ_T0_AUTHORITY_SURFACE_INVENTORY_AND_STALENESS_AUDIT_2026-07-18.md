# CVF Agent Work Order - SOT3 CVF Authority Surface Inventory And Staleness Audit

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-18

Work order ID: SOT3-CVF-PROJ-T0

dispatchBaseHead: `0eee70743`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated worker for SOT3-CVF-PROJ-T0.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_CVF_PROJ_T0_AUTHORITY_SURFACE_INVENTORY_AND_STALENESS_AUDIT_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse --short HEAD` before any edit and
require it to equal the committed dispatch HEAD supplied by the dispatcher.

Current-time notes: execute against the 2026-07-18 private provenance state.

Do-not-misread notes: this is a read-only architecture information audit. Do
not update architecture, catalogs, README, runtime, tests, generated
aggregates, registries, session state, handoff, public-sync, or provider state.

Required first actions: read startup state, active handoff, guard orientation,
literal-format gotchas, the paired roadmap and GC-018 baseline, this work
order, and the checker sources listed below.

Return contract: create exactly the two allowed review outputs, run the
required gates, leave them uncommitted and unstaged, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce an exact, source-backed ledger that tells later tranches which CVF
authority, architecture, workflow/navigation, product, and generated catalog
surfaces require SOT3 projection updates.

## Authority Chain

- Operator instruction: 2026-07-18 instruction to clean the workspace and
  create a worker work order for the CVF-wide SOT update.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V46_2026-07-17.md`.
- Roadmap: `docs/roadmaps/CVF_SOT3_CVF_AUTHORITY_SURFACE_AND_MASTER_ARCHITECTURE_PROJECTION_ROADMAP_2026-07-18.md`.
- GC-018: `docs/baselines/CVF_GC018_SOT3_CVF_PROJ_T0_AUTHORITY_SURFACE_INVENTORY_AND_STALENESS_AUDIT_2026-07-18.md`.
- Accepted implementation evidence: the three closed SOT3 roadmaps and source
  owners cited in the paired baseline.

Authority boundary: provider-specific memory, chat summaries, and sibling
application files are not CVF canonical authority. Use current CVF source and
accepted governed reviews for every factual disposition.

## Agent Roles

- Dispatcher: current orchestration role.
- Worker: one delegated worker role.
- Reviewer/closer: independent reviewer after worker return.
- Session-sync steward: reviewer/closer after material commit.
- Operator checkpoint: required only for scope expansion or a contradiction
  that cannot be resolved from governed source.

## Scope / Target / Owner Boundary

Allowed reads:

- all 15 seed surfaces in the paired baseline;
- `EXTENSIONS/CVF_REFINERY/src/`;
- `EXTENSIONS/CVF_TRUTH_KERNEL/src/`;
- `EXTENSIONS/CVF_TRUTH_FLOW/src/`;
- `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/`;
- SOT3 roadmap and completion-review evidence named in this packet;
- governance checker source required for the two worker outputs.

Allowed writes, exactly:

- `docs/reviews/CVF_SOT3_CVF_PROJ_T0_AUTHORITY_SURFACE_INVENTORY_AND_STALENESS_LEDGER_2026-07-18.md`
- `docs/reviews/CVF_SOT3_CVF_PROJ_T0_WORKER_RETURN_2026-07-18.md`

Forbidden scope:

- every other path;
- edits to any seed surface, runtime, test, checker, registry, generated
  aggregate, session file, handoff, roadmap, baseline, or this work order;
- staging, commit, branch, merge, reset, stash, cherry-pick, push, or publish;
- provider/live calls, secrets, browser/UI, queue/daemon, public-sync, or
  production actions;
- inventing later-tranche write scope not supported by a terminal ledger row.

Risk ceiling: R1 documentation-only read and review-output authoring.

## Write Ownership

| Path | Worker action | Reviewer action |
|---|---|---|
| authority-surface ledger | create uncommitted | verify, repair inside scope if needed, and own commit |
| worker return | create uncommitted | verify evidence and own commit |
| roadmap/baseline/work order | read only | reviewer may update closure state in a later reviewer-owned batch |
| session/handoff | forbidden to worker | session-sync steward only after accepted material closure |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| SOT3 absorption | accepted closure evidence in `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | ACCEPT |
| SOT3 activation | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; accepted bounded live status | ACCEPT |
| SOT3 downstream application | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md`; accepted T5 closure | ACCEPT |
| operator lane selection | 2026-07-18 instruction | ACCEPT |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`.
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
3. `AGENT_HANDOFF_V46_2026-07-17.md`.
4. `docs/reference/guard_orientation/README.md`.
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
6. the roadmap, GC-018 baseline, and this work order.
7. every seed surface before writing its ledger row.
8. checker sources named in Checker Source Read-Ahead Block as applied to each
   worker output.

## Pre-Flight Checks

Run before editing:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs/roadmaps/CVF_SOT3_CVF_AUTHORITY_SURFACE_AND_MASTER_ARCHITECTURE_PROJECTION_ROADMAP_2026-07-18.md'
Test-Path 'docs/baselines/CVF_GC018_SOT3_CVF_PROJ_T0_AUTHORITY_SURFACE_INVENTORY_AND_STALENESS_AUDIT_2026-07-18.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0eee70743 --head HEAD
```

Expected: the committed dispatch packet exists; worktree is clean; gate passes;
and execution base equals the dispatcher-supplied material commit HEAD.

Allowed-scope gate failures must be repaired and rerun. Escalate only when the
repair would exceed scope or change the claim boundary.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Refinery implementation | EXISTS | `EXTENSIONS/CVF_REFINERY/src/pipeline/engine.ts` | lines 23, 48, 86 | `RefineryEngine`; `REQUIRED_STAGE_CHAIN` | Refinery pipeline | ACCEPT |
| Kernel implementation | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | lines 49-55, 83 | `TruthKernel`; `evaluate` | Truth Kernel | ACCEPT |
| Flow implementation | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | class declaration and lifecycle methods | `DistributionEngine` | Truth Flow distribution | ACCEPT |
| vertical-slice implementation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/orchestrator.ts` | line 52 and composition body | `runThreeLayerScenario` | SOT3 vertical slice | ACCEPT |
| catalog stale claim | LITERAL_INVARIANT | `docs/reference/system_architecture_catalog/entries/interface.sot_three_layer_contract_chain.v1.json` | `claimBoundary`; `boundaryCaveat` | `cvf.asc.interface.sot_three_layer_contract_chain.v1` | as-built catalog | ACCEPT |
| bounded application proof | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` | status, decision, evidence summary | `SOT3_APP_T5_LIVE_PROOF_PASS` | T5 completion review | ACCEPT |

## New Doc-Only Fields

The ledger may introduce only these classification fields:

`surfacePath`, `surfaceClass`, `authorityRole`, `currentSot3Statement`,
`evidencePathOrSymbol`, `sot3Freshness`, `staleOrMissingDetail`,
`editDisposition`, `targetTranche`, `publicRisk`, and `reviewerNote`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| exact authority inventory | Required Inventory Method | ledger `surfacePath` rows | set comparison against 15 seed paths | PASS |
| stale claim detection | Source Verification; Required Inventory Method | `sot3Freshness`; `staleOrMissingDetail` | source/read-review comparison | PASS |
| tranche separation | Required Inventory Method | `targetTranche`; `editDisposition` | allowed enum and totals check | PASS |
| bounded claims | Claim Boundary | ledger and worker return | reviewer semantic read | PASS |
| no unauthorized edits | Write Ownership; Evidence Requirements | worker return changed set | `git status --short`; `git diff --name-status` | PASS |

## Required Inventory Method

Read each of the 15 seed surfaces in full. Create exactly one primary row per
seed. Do not group multiple files in one row.

For each row:

1. identify the surface class and current authority role;
2. quote or precisely locate its current SOT3 statement, or state that no SOT3
   navigation exists;
3. compare it with current package source and accepted governed evidence;
4. select one `sot3Freshness` value: `CURRENT`, `STALE`, `MISSING`, or
   `NO_CHANGE_WITH_REASON`;
5. select one `editDisposition`: `UPDATE`, `ADD_POINTER`,
   `REGENERATE_FROM_SOURCE`, `DEFER_WITH_REASON`, or `NO_CHANGE_WITH_REASON`;
6. assign T1, T2, T3, T4, or `NONE_WITH_REASON`;
7. state whether the later edit affects a public-facing claim.

Add a reconciliation summary with exact counts for every enum and prove the
sum equals 15. Additional evidence rows may follow, but they must not change
the seed denominator.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | capture execution base and clean status | worker return pre-flight block |
| 2 | read all seed surfaces and source owners | 15 terminal ledger rows |
| 3 | reconcile counts and tranche routing | ledger summary |
| 4 | create checker-safe worker return | exact changed-set and no-commit evidence |
| 5 | run gates and leave outputs unstaged | command/result table and final status |

## Evidence Requirements

- command-backed execution base and git status;
- 15/15 exact seed row set comparison;
- source paths and symbols for every runtime-correction claim;
- accepted review paths for every live/bounded claim;
- final `git diff --name-status` and `git status --short` showing exactly the
  two allowed outputs and nothing staged;
- worker-return fast-gate PASS;
- file-size guard PASS or unrelated pre-existing advisories disclosed.

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_SOT3_CVF_PROJ_T0_AUTHORITY_SURFACE_INVENTORY_AND_STALENESS_LEDGER_2026-07-18.md` | create exact 15-row terminal ledger and reconciliation |
| `docs/reviews/CVF_SOT3_CVF_PROJ_T0_WORKER_RETURN_2026-07-18.md` | create full checker-safe no-commit return |

## Acceptance Criteria

- 15/15 seed rows exist with no duplicate or missing path.
- all freshness and edit dispositions use the permitted terminal enums.
- the contract-only/no-runtime catalog contradiction routes to T1.
- later architecture, workflow/navigation, and product/readme work route to
  separate tranches.
- every factual runtime statement cites current CVF source.
- exactly two allowed outputs are untracked, nothing is staged, and HEAD is
  unchanged.
- all required gates pass.

## Review Gate

The reviewer must independently recompute the seed set, inspect every `STALE`
and `MISSING` row, verify the totals, and confirm no later-tranche edit was
performed. Fast-gate PASS alone is not acceptance.

## Closure Checklist

- [ ] 15 seed rows independently reconciled;
- [ ] stale/no-runtime contradiction independently confirmed;
- [ ] target-tranche routing accepted or repaired;
- [ ] exact two-path changed set confirmed;
- [ ] no stage or commit by worker confirmed;
- [ ] reviewer-fast and commit-steward gates pass;
- [ ] roadmap T0 state updated only by reviewer if accepted;
- [ ] session state synchronized separately after material commit.

## Stop Conditions

Return `BLOCKED_WITH_REASON` when:

- a seed path is missing or unreadable;
- source and accepted review evidence materially contradict each other;
- completion requires editing outside the two allowed outputs;
- pre-implementation or worker-return gates cannot pass inside allowed scope;
- the worktree is not clean at start or includes another batch;
- a provider/live, secret, public, production, runtime, generated aggregate,
  registry, session, or handoff mutation would be required.

## Return-To-Orchestrator Conditions

Return only `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, with the exact
execution base, changed set, stage state, gate results, and claim boundary.

## Worker Autonomy / No-Question Rule

Proceed autonomously with non-destructive reads, the two allowed writes,
format remediation inside those outputs, and repeated allowed-scope gate runs.
Do not ask the operator routine formatting or checker questions. Escalate only
for a stop condition.

## Operator Checkpoint

No routine checkpoint is required during T0. Return to the operator only if a
stop condition proves that the exact seed set or claim boundary must change.
T1 remains parked until independent reviewer acceptance and a fresh packet.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | operator request to audit and route CVF-wide SOT3 architecture and workflow information updates |
| scope classification | bounded internal documentation audit with exactly two allowed worker outputs |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| dispatcher role | authors and commits the bounded packet |
| worker role | reads canonical sources and creates two uncommitted review outputs |
| reviewer role | independently recomputes, repairs within scope, and owns closure |
| session-sync role | protected continuity steward after material acceptance |
| risk sensitivity | documentation audit; source/runtime mutation, public action, and provider/live use are prohibited |
| routing decision | `WORKER_MUST_NOT_COMMIT` |
| public route | `DEFERRED_PRIVATE_ONLY` |
| escalation condition | missing seed, source contradiction, foreign worktree change, forbidden-path need, or scope expansion |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-design`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture-design --role dispatcher --lifecycle-phase pre-dispatch --surface-selector sot-three-layer --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T0 ledger and worker return | read-only planning evidence; no runtime or action authority | exact seed/source evidence | internal review artifact only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external interface in T0 | no CLI/MCP, authentication, mutation, or public support | no adapter evidence or authorization | separate future adapter packet required | `DEFERRED_WITH_REASON` |

## Worker Output Checker Read-Ahead Mandate

Before writing either review artifact, derive its exact required headings,
table labels, trace labels, delta-boundary fields, conditional N/A sections,
no-commit evidence, and enum literals from current checker source. Do not use
the dispatch packet as a substitute for reading the output checkers.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher authors and commits packet; delegated worker audits without commit; independent reviewer/closer accepts and commits; session-sync steward updates continuity |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`0eee70743`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer sets from worker execution base |
| changedSetScope(phase) | dispatch exact three governed packet paths; execution exact two review outputs; closure reviewer-owned packet and accepted outputs; session sync protected continuity only |
| traceScope(phase, actor) | each actor records its own command, path, diff, and boundary evidence |
| commitOwner(phase) | dispatcher owns dispatch commit; worker commit forbidden; reviewer/closer owns material closure; session-sync steward owns separate continuity commit |
| crossBatchIsolation | dispatch starts from clean worktree at HEAD `0eee70743`; worker must also start clean and stop on any foreign change |
| nextMoveSurfaces | worker must not edit; reviewer/closer and session-sync steward update only after accepted material closure |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_CVF_PROJ_T0_COMPLETION_REVIEW_2026-07-18.md`

reviewerOwnedClosurePaths: the two worker outputs; this roadmap; paired GC-018
and work order; optional completion review only when needed; protected session
surfaces only in a separate session-sync commit.

closureOwner: independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_CVF_PROJ_T0_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Claim Boundary, Checker Source
Read-Ahead Block, git status evidence, Changed Files, No-Commit Statement,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, and conditional N/A-with-reason sections required by
the current worker-return checker.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0eee70743 --head HEAD
python governance/compat/run_agent_automation_assist.py --base 0eee70743 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Role:; Canonical packet:; Commit mode:; executionBaseHead; Current-time notes:; Do-not-misread notes:; Required first actions:; Return contract:; Authority Chain; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Execution Plan; Evidence Requirements; Planned Worker Fulfillment Manifest; Acceptance Criteria; Review Gate; Closure Checklist; Stop Conditions; Worker Autonomy / No-Question Rule; Dual Agent Surface Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; COMPLETE_PENDING_REVIEW; BLOCKED_WITH_REASON; WORKER_MUST_NOT_COMMIT; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and dispatch evidence after checker-source read-ahead, not first discovery |
| claimBoundary | structural dispatch and output-shape evidence only; semantic ledger acceptance remains reviewer-owned |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-CVF-PROJ-T0 --title "SOT3 CVF Authority Surface Inventory And Staleness Audit" --date 2026-07-18 --base 0eee70743 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact authority, source, manifest, handoff, evidence, and return contracts |
| checkerReadAheadConfirmation | checker paths and literal families recorded above |
| docOnlyNewFields | ledger classification fields named in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-CVF-PROJ-T0 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, rg, apply_patch, governance gates |
| Target paths | roadmap; GC-018 baseline; this work order |
| Allowed scope source | operator instruction dated 2026-07-18 |
| Before status evidence | clean worktree at HEAD `0eee70743`; tracked workspace overlay catalog verified unchanged |
| After status evidence | exact dispatch packet pending gates and commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | T0 read-only authority-surface audit dispatch only |
| Claim boundary | no source/runtime/test/provider/live/public/push/production/session mutation |
| Agent type | dispatcher |
| Invocation ID | `sot3-cvf-proj-t0-dispatch-2026-07-18` |
| Expected manifest | roadmap; GC-018 baseline; work order |
| Actual changed set | exact three-path dispatch set before commit |
| Manifest delta | MATCH expected after pre-commit verification |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | read-only authority-surface inventory and staleness routing |
| claimDisposition | N/A with reason: no runtime execution-control or enforcement behavior is implemented |
| receiptEvidence | N/A with reason: prior review evidence is read only and no runtime receipt is created |
| actionEvidence | N/A with reason: audit authoring is not runtime action evidence |
| invocationBoundary | exact T0 worker packet |
| interceptionBoundary | no IDE, shell, filesystem, provider, or agent-action interception claim |
| claimLanguage | audit, classify, reconcile, and route only |
| forbiddenExpansion | runtime/source/test mutation, provider/live, public-sync, push, production, browser/UI, queue/daemon, and universal SOT3 claims |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance audit packet. No public-safe export or
public-sync action is authorized.

## Claim Boundary

This work order authorizes exactly one no-commit T0 worker audit and exactly
two review outputs. It does not authorize later-tranche document edits,
generated catalog changes, runtime/provider/live work, public-sync, push,
production, or universal SOT3 claims.
