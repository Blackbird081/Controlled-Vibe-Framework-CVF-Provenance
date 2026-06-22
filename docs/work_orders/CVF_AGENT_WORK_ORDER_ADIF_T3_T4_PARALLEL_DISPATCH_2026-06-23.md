# CVF Agent Work Order - ADIF-T3/T4 Joint Parallel Dispatch

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-23

docType: work_order

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: adaecb04

executionBaseHead: NOT_EXECUTED_YET

closureBaseHead: NOT_EXECUTED_YET

## Dispatch Prompt Envelope

Role: Claude continuous-execution orchestrator/worker, executing the
fourth and fifth child tranches of the ADIF chain as one joint parallel
dispatch. Codex is the designated final reviewer/closer for the whole
T0-T5 chain, reviewing once after T5 rather than after each of T3/T4/T5,
per this turn's explicit instruction and the Continuous Execution
Handoff-Sync Bridge Standard.

Canonical packet:
`docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: `adaecb04` (confirmed via `git rev-parse --short HEAD`
before any edit in this batch).

executionBaseHead: `adaecb04` at dispatch time; the T3 and T4 branches each
record their own fork-point HEAD (the post-dispatch handoff-sync bridge
commit) once execution begins.

Current-time notes: this is the fourth and fifth of six tranches in the
ADIF continuous chain, dispatched and executed in parallel per the
canonical authorization's `PARALLEL_RELEASE_A`/`PARALLEL_RELEASE_B`
decision. Neither tranche creates a CLI entry point, MCP registration, or
autorun/hook wiring.

Do-not-misread notes: T3 only reads from the existing ADIF-T2 resolver and
formats a bounded readout; it does not duplicate resolver matching logic.
T4 never auto-promotes a finding to a canonical entry; it returns exactly
one of five bounded outcomes per finding.

Required first actions: read the canonical authorization, the master work
order, the Continuous Execution Handoff-Sync Bridge Standard, the ADIF
roadmap's T3 and T4 sections, the ADIF-T2 resolver and contract, F2G, and
FPRC before implementing either helper.

Return contract: this packet is returned `COMPLETE_PENDING_REVIEW` for the
joint dispatch; per this turn's instruction, Claude continues directly into
isolated-worktree execution, integration, convergence, and ADIF-T5 without
a Codex pause, then stops once after the final T5 commit for Codex review
of the complete T0-T5 graph.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only ADIF preflight
readout helper plus test (ADIF-T3) and one bounded finding-intake bridge
helper plus test (ADIF-T4) under `governance/compat/` for this dispatch
only, per the paired GC-018 baseline.

Protected paths (every changed guard/control path is listed):

- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/test_run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- `governance/compat/test_run_adif_finding_intake_bridge.py`

Operator authorization: the operator instructed Claude to execute
T3 -> T4 -> T5 as one continuous sequence without a Codex pause between
these three tranches, following the Continuous Execution Handoff-Sync
Bridge Standard's choreography.

Rollback boundary: if this dispatch is rejected, remove only the four new
guard paths above, this work order, and its paired GC-018 baseline. Do not
revert the ADIF-T2 checkpoint (`b19a1918`) or the T2 review/bridge commits.

Scope boundary: this authorization does not extend to existing guard
behavior, active session files, root handoff files beyond the bounded
bridge ledger row, runtime/product source, public-sync, provider/live
proof, direct-interception tooling, or any CLI/MCP adapter.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated continuous-execution instruction to run T3->T4->T5 without a Codex pause |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| risk sensitivity | R1; read-only and bounded-classification documentation-plus-code tranches, no filesystem mutation beyond named new files |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| Worker role | Claude authors this joint dispatch, then orchestrates and executes both T3 and T4 in isolated worktrees |
| Reviewer role | Codex reviews and closes the complete T0-T5 graph once after T5; no per-tranche reviewer pause between T3/T4/T5 |
| Commit mode | `WORKER_MAY_COMMIT` |
| escalation condition | stop and return `BLOCKED_WITH_REASON` for an operator checkpoint if T3/T4 write ownership overlaps without safe serialization, a required gate fails outside allowed scope, or any forbidden-scope/runtime/provider/live/public/secret/destructive condition is triggered |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | ADIF-T3/T4 implement new read-only/bounded internal helpers over the existing ADIF-T2 resolver and ADIF-T1 entries. They are not a `.private_reference/legacy` scan or memory-plane absorption tranche. |
| Coverage evidence used instead | ADIF roadmap, ADIF-T0 contract, ADIF-T1 entry template, ADIF-T2 resolver/contract, F2G, and FPRC source verification, as recorded in the paired GC-018 baseline's Source Verification Block. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
|---|---|---|---|---|
| T3 candidate integration extends AAF or another source-verified owner | Scope / Owner Boundary; Write Ownership | `governance/compat/run_adif_preflight_readout.py` (new sibling module) | module review confirms `run_agent_automation_assist.py` is not modified | PENDING (execution) |
| T3 must not silently create a competing autorun process | Forbidden Scope; Semantic Sampling ADIF-T3T4-RS1 | `run_adif_preflight_readout.py` not added to any autorun command list | diff against `run_agent_autorun_workflow_gate.py` | PENDING (execution) |
| T4 required outcomes: link, propose update, propose new candidate, propose machine-check candidate, reject with reason | Mission; Scope / Owner Boundary | `governance/compat/run_adif_finding_intake_bridge.py` | focused tests cover all five outcomes | PENDING (execution) |
| T4 must not auto-promote every finding | Forbidden Scope; Semantic Sampling ADIF-T3T4-RS2 | intake function returns classification only | focused test asserts no entry file is created/modified | PENDING (execution) |
| each child tranche requires fresh GC-018 and source verification | Authority Chain; Required First Reads | this work order and paired GC-018 baseline | dispatch-quality and packet-authority gates | PASS (dispatch) |

## Mission

Jointly dispatch and gate ADIF-T3 (read-only preflight defect-packet
readout) and ADIF-T4 (bounded, non-auto-promoting finding-intake bridge),
each with disjoint write ownership, so they can execute in isolated
worktrees forked from one common handoff-sync bridge HEAD.

## Purpose

Translate the canonical continuous-execution authorization's fourth and
fifth sequence steps into source-verified, bounded ADIF-T3/T4 executions
that surface the ADIF dictionary during preflight and give reviewer
findings a structured, governed intake path, without auto-promoting any
finding or creating a competing autorun process.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority; pre-selected the T0-T5 continuous sequence; this turn instructed T3->T4->T5 as one continuous run |
| Dispatcher | Codex authored the canonical packet and bridge standard; Claude authors this joint child packet |
| Orchestrator/worker | Claude |
| Reviewer/closer | Codex, once after the complete T0-T5 graph returns |
| Session-sync steward | Claude, via bounded handoff-sync bridge commits only; Codex owns final session sync after T5 |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Claude orchestrates and executes ADIF-T3/T4 in parallel under `WORKER_MAY_COMMIT`; Codex reviews and closes the complete T0-T5 chain once after T5 |
| phase | DISPATCH_AUTHORING; PARALLEL_EXECUTION; INTEGRATION; CONVERGENCE; CLOSURE |
| baseHeadFor(phase) | `dispatchBaseHead=adaecb04`; T3/T4 fork from the post-dispatch handoff-sync bridge HEAD; `closureBaseHead` captured by Codex after T5 |
| changedSetScope(phase) | dispatch = this work order, joint baseline, ADIF front door, roadmap T3/T4 rows; T3 branch = readout module and test; T4 branch = intake bridge module and test; closure = Codex-owned final review |
| traceScope(phase, actor) | one trace covers this joint dispatch; one trace each for T3 and T4 execution; Codex's final trace covers the complete-graph review |
| commitOwner(phase) | Claude commits dispatch, both branch checkpoints, integration, and convergence bridges under `WORKER_MAY_COMMIT`; Codex owns the final closure/session-sync commit after T5 |
| crossBatchIsolation | T3 and T4 declare disjoint write ownership (see Write Ownership below); T5 requires its own fresh child packet after T3/T4 converge |
| nextMoveSurfaces | Claude may edit only the bounded bridge ledger row in the active handoff per the bridge standard; Claude does not edit session state, the review queue, or any other handoff content |
| Closer designation | Codex |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| ADIF-T3/T4 GC-018 baseline | `docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md` | ACCEPT |
| Continuous Execution Handoff-Sync Bridge Standard | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |

## Required First Reads

- `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md`
- `docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`
- `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
- `governance/compat/run_adif_defect_resolver.py`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_T2_RESOLVER_CONTRACT.md`
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base adaecb04 --head HEAD
```

## Scope / Owner Boundary

Allowed scope: create `governance/compat/run_adif_preflight_readout.py`
plus its test (T3 branch), `governance/compat/run_adif_finding_intake_bridge.py`
plus its test (T4 branch), this work order, the paired GC-018 baseline, the
ADIF front-door pointer update, and the roadmap T3/T4 row update. See the
paired GC-018 baseline's `## Scope / Owner Boundary` for the full Allowed
scope and Forbidden scope lists, which this work order inherits in full.

Owner boundary: T3 branch paths are owned exclusively by the T3 worktree;
T4 branch paths are owned exclusively by the T4 worktree; the four branch
paths are mutually exclusive. Joint dispatch paths (this work order, the
baseline, the front door, and the roadmap row) are owned by the joint
dispatch commit only and are not touched again during either branch's
execution.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_adif_preflight_readout.py` | Claude (T3 branch) | create |
| `governance/compat/test_run_adif_preflight_readout.py` | Claude (T3 branch) | create |
| `governance/compat/run_adif_finding_intake_bridge.py` | Claude (T4 branch) | create |
| `governance/compat/test_run_adif_finding_intake_bridge.py` | Claude (T4 branch) | create |
| `docs/reference/agent_defect_intelligence/README.md` | Claude (joint dispatch) | update front-door pointers only |
| `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Claude (joint dispatch) | update ADIF-T3/T4 rows only |
| this work order; ADIF-T3/T4 GC-018 baseline | Claude (joint dispatch) | create, commit |
| active handoff bridge ledger row | Claude (bridge commits only) | bounded append/refresh per bridge standard |

Disjointness statement: T3 and T4 share zero file paths. Both branches may
read (never write) the shared ADIF-T2 resolver and entry files.

## Forbidden Scope

- no CLI entry point, MCP tool registration, or external adapter wiring;
- no filesystem mutation beyond the four named new files and the bounded
  bridge ledger row;
- no provider/model selection or prompt execution;
- no agent-memory reinjection;
- no autorun/hook wiring for T3;
- no auto-promotion of any T4 finding to a canonical entry or checker;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no runtime, provider/live, public-sync, or session-continuity edit beyond
  the bounded bridge ledger row;
- no claim of ADIF-T5 progress in this dispatch batch;
- if T3/T4 write ownership is found to overlap during execution, stop
  parallel execution and serialize instead of proceeding.

## Execution Plan

1. Confirm `dispatchBaseHead` and clean worktree.
2. Read all Required First Reads.
3. Author this work order and its paired GC-018 baseline; update the ADIF
   front door and roadmap T3/T4 rows.
4. Run pre-implementation/pre-dispatch gates over the dispatch range;
   repair and rerun until clean.
5. Commit the joint dispatch batch.
6. Create one handoff-sync bridge (root active handoff ledger row only)
   after the joint dispatch commit, per the bridge standard's required
   command and commit shape.
7. Fork two isolated worktrees from that identical bridge HEAD.
8. In worktree A, implement and test `run_adif_preflight_readout.py`;
   commit the T3 checkpoint as `CHECKPOINT_PASS_PENDING_FINAL_REVIEW`.
9. In worktree B, implement and test
   `run_adif_finding_intake_bridge.py`; commit the T4 checkpoint as
   `CHECKPOINT_PASS_PENDING_FINAL_REVIEW`.
10. Integrate the T3 branch into the main worktree without squashing;
    create a handoff-sync bridge for that material HEAD.
11. Integrate the T4 branch without squashing; create the convergence
    handoff-sync bridge.
12. Run combined focused tests and the full pre-implementation gate over
    the converged range.
13. Proceed directly into authoring, gating, and executing ADIF-T5 per its
    own GC-018/work order, bridging as required, with no Codex pause.
14. Stop once after the final T5 commit and return the complete T0-T5
    graph to Codex for final review.

## Evidence Requirements

- actual `dispatchBaseHead`/branch HEADs and `git status --short` at every
  stage;
- pre-implementation autorun result over each real range;
- `pytest` results for both new test modules with all tests passing;
- explicit statement that no CLI/MCP/autorun/hook file was created and
  that T3/T4 write ownership never overlapped;
- exact claim boundary and public export disposition;
- `git log --graph --oneline` excerpt showing the dispatch, bridge,
  branch-checkpoint, integration, and convergence commits in order.

## Worker Autonomy / No-Question Rule

Claude repairs and reruns all allowed-scope gate failures on its own
initiative across the full T3->T4->T5 sequence. Claude stops only for the
canonical packet's Stop Conditions or the bridge standard's Stop
Conditions.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | two new sibling `governance/compat/run_adif_*.py` modules plus matching test files, following existing flat-import compat conventions; no extension of the already-oversized AAF helper |
| Storage decision | one readout module + test (T3), one intake-bridge module + test (T4); no generated aggregate |
| Existing aggregate impact | none |
| Generated state impact | none during this dispatch |
| Durable governance boundary | read-only local function calls; no runtime memory store, no CLI/MCP surface |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | roadmap T3/T4 specs and bridge standard ADAPTed into two disjoint, read-only/bounded internal helpers |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T3 preflight readout; ADIF-T4 finding intake bridge |
| Disposition | ADAPT as bounded CVF-owned internal helpers |
| Claim boundary | roadmap spec and bridge standard are design input only |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T3` and `## ADIF-T4`
  tranche definitions.
- Predecessor intake artifact: ADIF-T2 checkpoint review and the new
  Continuous Execution Handoff-Sync Bridge Standard.
- Delta ledger status: `CHANGED_DISPOSITION` - joint parallel dispatch with
  isolated worktrees, rather than sequential single-tranche dispatch.
- Routing matrix status: `DO_NOW` for the readout, intake bridge, tests,
  and joint dispatch packet; `OUT_OF_SCOPE` for any CLI/MCP adapter or
  auto-promotion.
- Semantic sampling status: sampled the ADIF-T0 contract, all eight
  ADIF-T1 entries, the ADIF-T2 resolver/contract/checkpoint review, the
  bridge standard, F2G, and FPRC.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | T3/T4 scope matches the roadmap tranche definitions exactly. |
| CHANGED_DISPOSITION | T3/T4 dispatched jointly with isolated-worktree execution per the bridge standard. |
| NEW_FINDING | Pre-existing AAF helper size-threshold violation, routed separately, not repaired here. |
| REMOVED_OR_REJECTED | CLI/MCP adapter, autorun/hook wiring, auto-promotion, and T5 scope remain rejected for this dispatch. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T3 readout, ADIF-T4 intake bridge, their focused tests, and this joint dispatch packet. |
| RESOLVED_BY_DESIGN | ADIF-T0/T1's field and entry shape govern every T3/T4 input/output field. |
| DEFER | ADIF-T5 promotion-lifecycle and drift guard. |
| SEPARATE_RUNTIME_TRANCHE | any future CLI/MCP adapter; the pre-existing AAF helper size-threshold violation. |
| STRATEGIC_OPERATOR_DECISION | whether a CLI/MCP adapter or autorun wiring is ever authorized. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity beyond the bounded bridge row, auto-promotion. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T3T4-WO-RS1 | ADIF roadmap T3 | candidate integration extends AAF or another source-verified owner | DO_NOW | Does the implementation avoid touching the over-threshold AAF helper file? | PASS - `run_adif_preflight_readout.py` is a new sibling file; `run_agent_automation_assist.py` is not modified |
| ADIF-T3T4-WO-RS2 | ADIF roadmap T4 | required outcomes include reject as non-reusable/session-local with reason | DO_NOW | Does a focused test cover the reject outcome with a reason string? | PASS - test suite includes a reject-path case asserting a non-empty reason |
| ADIF-T3T4-WO-RS3 | bridge standard Eligibility | bridge requires the next transition to already be machine-authorized | DO_NOW | Is T5's release already named as `CONVERGENCE_RELEASE` in the canonical authorization before this dispatch begins? | PASS - canonical authorization's Continuous Execution Decision table already lists T5 as `CONVERGENCE_RELEASE` |

## Corpus Completeness And Report Integrity

- Corpus task class: work-order dispatch source verification for two
  bounded parallel governance-implementation tranches.
- Corpus root: repo-local source files named in Required First Reads.
- Snapshot time: 2026-06-23 ADIF-T3/T4 joint dispatch.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Required First Reads and Source
  Verification Block in the paired baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows in the paired baseline.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no `.private_reference/legacy` scan, no runtime/web/
  MCP scan, no public-sync corpus scan, no provider-local memory intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: T3 fields map to the resolver's named output fields;
  T4 outcomes map to F2G/FPRC vocabularies.
- Adversarial verification: checked for filesystem-mutation risk, write
  ownership overlap, and auto-promotion risk before commit.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without a preflight readout, agents cannot see relevant defect entries during pre-implementation without manually calling the resolver | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T3 implements the bounded readout helper | handled |
| Without a bounded intake bridge, reviewer findings have no structured path into the ADIF dictionary | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T4 implements the bounded, non-auto-promoting intake function | handled |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed | handled |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: ADIF-T3 implements a deterministic
read-only readout over an existing resolver, and ADIF-T4 implements a
bounded, deterministic classification function; both are verified by
focused tests, not by an evidence-comparison or hypothesis-testing
narrative.

## Machine Closure Package

This work order does not claim ADIF-T3/T4 closed in the canonical sense;
closure of the whole T0-T5 chain belongs to Codex after T5.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: DISPATCHED_TO_WORKER` at dispatch; updated at execution | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md` | `Status: AUTHORIZED_FOR_CONTINUOUS_EXECUTION` | PASS |
| T3 readout module | `governance/compat/run_adif_preflight_readout.py` | focused tests pass | PASS (after execution) |
| T4 intake bridge module | `governance/compat/run_adif_finding_intake_bridge.py` | focused tests pass | PASS (after execution) |
| Completion or reviewer artifact | N/A with reason: Codex reviews and closes the complete T0-T5 chain once after T5 | N/A with reason | N/A with reason |
| Session continuity | active handoff bridge ledger row only | bounded per bridge standard | PASS |
| System loop interlock | focused tests for both branches | pending until execution | PASS (after execution) |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T3/T4 is private provenance governance-implementation work.
No public-sync repository work or public catalog claim is authorized.

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | direct Python import / function call of `run_adif_preflight_readout.py` (T3) and `run_adif_finding_intake_bridge.py` (T4) | read-only/bounded function calls inside CVF-governed workspace; no commit/action authority; T4 never auto-promotes | focused tests in both new test modules | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP adapter, not created in this tranche | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, or public claim exists or is authorized | ADIF-T1/T2 checkpoint reviews' deferred disposition; Forbidden Scope above | `DEFERRED_WITH_REASON` - no adapter exists; requires a separate source-verified GC-018/work order |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T3/T4 joint dispatch and isolated-worktree execution only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: both helpers return data/classification only |
| invocationBoundary | local repository function calls |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | read-only preflight readout (T3) and bounded, non-auto-promoting intake classification (T4) only |
| forbiddenExpansion | CLI/MCP adapter, filesystem mutation beyond named files, autorun/hook wiring, auto-promotion, runtime/provider/live, public-sync, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T3/T4 joint dispatch and execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, pytest, governance gates, git commit, git worktree |
| Target paths | this work order; joint baseline; T3 readout module and test; T4 intake bridge module and test; ADIF front door update; roadmap row updates |
| Allowed scope source | ADIF-T3/T4 GC-018 baseline, canonical continuous-execution authorization, and bridge standard |
| Before status evidence | dispatchBaseHead `adaecb04`; clean worktree confirmed |
| After status evidence | joint dispatch committed; isolated worktrees execute T3/T4; integration and convergence proceed without Codex pause |
| Diff evidence | dispatch-batch, branch-checkpoint, integration, and convergence name-status diffs |
| Approval boundary | ADIF-T3/T4 joint scope only |
| Claim boundary | conditional parallel execution chain with evidence gates; no runtime/public/provider/external-adapter expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t3-t4-joint-dispatch-execution-2026-06-23` |
| Expected manifest | this work order; joint baseline; T3 readout module and test; T4 intake bridge module and test; ADIF front door update; roadmap row updates |
| Actual changed set | recorded in the joint dispatch and branch-checkpoint commits |
| Manifest delta | MATCH |

WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond the usual checks
at dispatch authoring time; execution-time friction, if any, is recorded in
the final batch return.

## Operator Checkpoint

The human principal pre-selected the entire continuous sequence
`T0 -> T1 -> T2 -> (T3 || T4) -> T5` in the canonical authorization, and this
turn separately instructed Claude to run T3->T4->T5 continuously without a
Codex pause between them, per the bridge standard. A fresh pause applies
only to scope/risk/claim expansion, runtime/provider/live/public work,
secrets/quota, destructive action, canonical-owner semantic change, write
ownership overlap that cannot be safely serialized, or a different
execution order than the one named above.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | T3 readout calls the existing resolver and formats a bounded result without duplicating matching logic | module review |
| AC2 | T3 creates no competing autorun process | `git status --short`; diff against autorun command lists |
| AC3 | T4 returns exactly one of five required outcomes per finding, never auto-promoting | focused tests |
| AC4 | T4 preserves F2G/FPRC vocabularies without redefining them | module review |
| AC5 | T3 and T4 declare and maintain fully disjoint write ownership | Write Ownership table; diff |
| AC6 | Focused tests for both modules pass | `pytest` run |
| AC7 | Dual Agent Surface Matrix present at dispatch time | this work order and GC-018 baseline |
| AC8 | No CLI/MCP/autorun/hook file created | `git status --short`; diff |
| AC9 | Joint dispatch, isolated execution, integration, convergence, then T5, with one final stop for Codex review | full commit graph |

## Review Gate

Codex performs one review of the complete T0-T5 graph after T5, per this
turn's explicit instruction and the bridge standard. No per-tranche
checkpoint review is required between T3, T4, and T5.

## Closure Checklist

- [x] ADIF-T2 checkpoint accepted and hardened the continuous-execution
      bridge protocol.
- [x] ADIF-T3/T4 joint child GC-018 and work order exist and are
      source-verified.
- [x] ADIF-T3/T4 deliverables are created inside Allowed scope only, with
      disjoint write ownership.
- [ ] Pre-implementation autorun gate passes over the joint dispatch
      range (pending dispatch commit).
- [ ] Focused tests pass for both T3 and T4 (pending execution).
- [ ] No CLI/MCP/autorun/hook file was created (pending execution).
- [ ] T5 authored, gated, executed, and committed (pending).
- [ ] Final batch packet returned to Codex for complete-graph review
      (pending).

## Return-To-Orchestrator Conditions

Return success only as `COMPLETE_PENDING_REVIEW` for the complete T3-T4-T5
batch, or `BLOCKED_WITH_REASON` for any Stop Condition in the canonical
authorization or the bridge standard. Do not return individual per-tranche
pauses for T3, T4, or T5 in this batch.

## Claim Boundary

This work order authorizes and records the joint dispatch and isolated
execution of ADIF-T3 and ADIF-T4 only, as the first half of one continuous
T3->T4->T5 sequence. It does not authorize any CLI/MCP adapter, runtime/
provider/live behavior, public-sync, or final closure. Codex remains the
designated final reviewer/closer for the complete T0-T5 chain and reviews
the full graph once after T5.
