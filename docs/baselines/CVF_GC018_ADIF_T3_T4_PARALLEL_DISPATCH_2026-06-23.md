# CVF GC-018 - ADIF-T3/T4 Joint Parallel Dispatch

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: gc018_baseline

dispatchBaseHead: adaecb04

executionBaseHead: 617b041f

closureBaseHead: c08f810e

Commit mode: `WORKER_MAY_COMMIT`

Batch ID: ADIF-T3-T4-JOINT-DISPATCH

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only ADIF preflight
readout helper plus test (ADIF-T3) and one bounded finding-intake bridge
helper plus test (ADIF-T4) under `governance/compat/` for this dispatch
only, per the canonical continuous-execution authorization's
`PARALLEL_RELEASE_A`/`PARALLEL_RELEASE_B` decision.

Protected paths (every changed guard/control path is listed):

- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/test_run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- `governance/compat/test_run_adif_finding_intake_bridge.py`

Operator authorization: the operator pre-selected the T0-T5 continuous
sequence in the canonical authorization and this turn explicitly instructed
Claude to execute T3->T4->T5 as one continuous sequence without a Codex
pause between these three tranches, per the Continuous Execution
Handoff-Sync Bridge Standard.

Rollback boundary: if this dispatch is rejected, remove only the four new
guard paths above, this baseline, and its paired work order. Do not revert
the ADIF-T2 checkpoint (`b19a1918`) or the T2 review/bridge commits
(`07000fd6`, `4527c55a`, `dfaae2e7`, `adaecb04`).

Scope boundary: this authorization does not extend to existing guard
behavior, active session files, root handoff files beyond the bounded
bridge ledger row, runtime/product source, public-sync, provider/live
proof, direct-interception tooling, or any CLI/MCP adapter.

## Purpose

Jointly author and gate the ADIF-T3 (Early Preflight Integration) and
ADIF-T4 (Reviewer Finding Intake And De-Dup Bridge) child tranches as one
dispatch batch, per the canonical authorization's Parallel Fork And
Convergence Protocol. Both tranches fork from the same accepted ADIF-T2
checkpoint and must declare disjoint write ownership so they can execute
in isolated worktrees without overlap.

This baseline is authorized under, and subordinate to, the canonical
continuous-execution packet, the Continuous Execution Handoff-Sync Bridge
Standard, and the accepted ADIF-T2 checkpoint review. It does not waive
that packet's Stop Conditions or Codex final-review requirement after T5.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| Master work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CONTINUOUS_EXECUTION_T0_T5_FOR_CLAUDE_2026-06-22.md` | ACCEPT |
| Continuous Execution Handoff-Sync Bridge Standard | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | ACCEPT |
| ADIF-T2 checkpoint commit | `b19a1918` | ACCEPT |
| ADIF-T2 checkpoint accept/harden commits | `07000fd6`; `4527c55a`; `dfaae2e7`; `adaecb04` | ACCEPT - HEAD continuity restored before T3/T4 dispatch |
| ADIF-T0 owner-reconciliation contract | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | ACCEPT |
| ADIF entry template and eight seed entries | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | ACCEPT |
| ADIF-T2 resolver and contract | `governance/compat/run_adif_defect_resolver.py`; `docs/reference/agent_defect_intelligence/CVF_ADIF_T2_RESOLVER_CONTRACT.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | ACCEPT |
| Finding-To-Governance Learning Trigger Standard | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | ACCEPT |
| Finding Propagation And Root-Cause Grouping Standard | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF-T3 prerequisite, candidate integration, and no-competing-autorun constraint | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T3 - Early Preflight Integration | T3 tranche definition | ADIF roadmap | VALUE_SET | ACCEPT |
| ADIF-T4 prerequisite, output, and required-outcomes list (link, propose update, propose new candidate, propose machine-check candidate, reject) | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T4 - Reviewer Finding Intake And De-Dup Bridge | T4 required outcomes list | ADIF roadmap | VALUE_SET | ACCEPT |
| Resolver function and packet shape T3/T4 may call | `governance/compat/run_adif_defect_resolver.py` | `resolve_defect_packet`; `DefectPacket`; `load_entries` | `resolve_defect_packet` | ADIF-T2 resolver | EXISTS | ACCEPT |
| Existing flat-import test pattern with `sys.modules` registration before `exec_module` | `governance/compat/test_run_adif_defect_resolver.py` | module-loading preamble | `MODULE` | ADIF-T2 resolver test | EXISTS | ACCEPT |
| Bridge standard's exact write boundary (root active handoff named by session state only) and required command shape | `docs/reference/CVF_CONTINUOUS_EXECUTION_HANDOFF_SYNC_BRIDGE_STANDARD_2026-06-23.md` | Exact Write Boundary; Required Command And Commit Shape | `HANDOFF_SYNC_BRIDGE_PASS` | Bridge standard | VALUE_SET | ACCEPT |
| Active handoff file currently named by session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `activeHandoff` field | `activeHandoff` | active session state | EXISTS | ACCEPT |
| F2G `Disposition` enum (`RULE_EXISTS`, `RULE_ADDED`, `MACHINE_CHECK_ADDED`, `MACHINE_CHECK_CANDIDATE`, `TEMPLATE_UPDATED`, `STANDARD_UPDATED`, `STANDARD_ADDED`, `PHASE_GATE_PLACEMENT_GAP`, `DESIGN_REVIEW_REQUIRED`, `RUNTIME_LEARNING_CANDIDATE`) | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Disposition enum section | Disposition enum list | F2G standard | VALUE_SET | ACCEPT |
| FPRC `defectRole` enum (`ROOT_CAUSE`, `PROPAGATED_SYMPTOM`, `EVIDENCE_REPLICATION`, `STALE_SYNC`, `REVIEWER_REPAIR_SIDE_EFFECT`) | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | Defect Role Field table | `defectRole` value table | FPRC standard | VALUE_SET | ACCEPT |
| Eight ADIF entries with stable `defectId` values and `lifecycleState` | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | fenced field block in each file | `defectId`; `lifecycleState` | ADIF-T1 seed entries | EXISTS | ACCEPT |

## Scope / Owner Boundary

Allowed scope (ADIF-T3, disjoint branch):

- create `governance/compat/run_adif_preflight_readout.py` - a read-only
  function that calls `resolve_defect_packet` with caller-supplied or
  pre-implementation-context-derived task class/role/phase/selector and
  formats a bounded human-readable readout, mirroring the AAF helper's
  `*ReadoutItem`/`_build_*_readout` shape without modifying
  `run_agent_automation_assist.py` (already over the Python automation
  hard size threshold; see Current Runtime Freshness Verification);
- create `governance/compat/test_run_adif_preflight_readout.py`;
- create local checkpoint commit for the T3 branch only.

Allowed scope (ADIF-T4, disjoint branch):

- create `governance/compat/run_adif_finding_intake_bridge.py` - a bounded,
  read-only intake function that takes a structured finding description and
  returns exactly one of the five required outcomes (link to existing
  entry, propose update to existing entry, propose new guidance-only
  candidate, propose machine-check candidate through F2G, reject as
  non-reusable/session-local with reason), never auto-promoting;
- create `governance/compat/test_run_adif_finding_intake_bridge.py`;
- create local checkpoint commit for the T4 branch only.

Joint allowed scope:

- create this baseline and its paired work order;
- create the bounded handoff-sync bridge commits required by the
  Continuous Execution Handoff-Sync Bridge Standard (root active handoff
  file only, ledger-row edit only).

Forbidden scope (both tranches):

- no CLI entry point, MCP tool registration, or external adapter wiring;
- no filesystem mutation beyond the named new files and the bounded bridge
  ledger row;
- no provider/model selection or prompt execution;
- no agent-memory reinjection;
- no autorun/hook wiring - T3 does not create a competing autorun process
  and is not wired into any phase gate in this batch;
- no auto-promotion of any T4 finding to a canonical entry or checker;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no runtime, provider/live, public-sync, or session-continuity edit beyond
  the bounded bridge ledger row;
- no claim of ADIF-T5 progress in the T3/T4 dispatch batch;
- T3 must not overlap T4's write ownership; if any overlap is discovered
  during execution, Claude must stop parallel execution and serialize.

Risk ceiling: R1 - second and third ADIF tranches with executable code,
both read-only with no filesystem mutation beyond named new files, no
external surface, and full focused-test coverage required before either
checkpoint commit.

## Required Deliverables

- `governance/compat/run_adif_preflight_readout.py`
- `governance/compat/test_run_adif_preflight_readout.py`
- `governance/compat/run_adif_finding_intake_bridge.py`
- `governance/compat/test_run_adif_finding_intake_bridge.py`
- this GC-018 baseline
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T3_T4_PARALLEL_DISPATCH_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  (ADIF-T3/T4 rows only)
- `docs/reference/agent_defect_intelligence/README.md` (front-door pointer
  update only)

## Decision / Baseline / Proposed Tranche

Decision: authorize the joint ADIF-T3/T4 dispatch for parallel execution
under the canonical ADIF authorization's `PARALLEL_RELEASE_A`/
`PARALLEL_RELEASE_B` decision, released by the accepted ADIF-T2 checkpoint.
Baseline: dispatch base `adaecb04`. Proposed tranches: ADIF-T3 Early
Preflight Integration (read-only diagnostic readout) and ADIF-T4 Reviewer
Finding Intake And De-Dup Bridge (bounded intake function), executed in
isolated worktrees from an identical bridge HEAD, integrated without
squashing, then converged before ADIF-T5.

## Dependency Release Evidence

| Prerequisite artifact | Closure or dispatch commit | Disposition | Gate evidence |
|---|---|---|---|
| ADIF-T2 checkpoint commit | `b19a1918` | ACCEPT | committed |
| ADIF-T2 checkpoint review/acceptance | `07000fd6` | ACCEPT | `ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW` |
| ADIF-T2 handoff bridge and hardening | `4527c55a`; `dfaae2e7`; `adaecb04` | ACCEPT | continuity restored; bridge standard authored and hardened |
| Continuity sync restoring active-handoff HEAD alignment | `adaecb04` | ACCEPT | pre-implementation autorun 47/47 PASS at range `adaecb04..HEAD` before this packet |

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | direct Python import / function call of `run_adif_preflight_readout.py` (T3) and `run_adif_finding_intake_bridge.py` (T4) inside CVF-governed workspace | read-only function calls; no filesystem mutation beyond named new files; no commit/action authority; T4 never auto-promotes | this baseline, paired work order, and focused tests in both new test modules | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP adapter, not created in this tranche | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, or public claim exists or is authorized by ADIF-T3/T4 | ADIF-T1/T2 checkpoint reviews' deferred disposition; this baseline's Forbidden Scope | `DEFERRED_WITH_REASON` - no adapter exists; a future CLI/MCP surface requires its own source-verified GC-018/work order |

## Evidence / Verification

Pre-dispatch verification for this joint child packet:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base adaecb04 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base adaecb04 --head HEAD --enforce
python governance/compat/check_agent_packet_authority_and_encoding.py --base adaecb04 --head HEAD --enforce
```

Focused test verification after each branch's implementation:

```powershell
python -m pytest governance/compat/test_run_adif_preflight_readout.py -v
python -m pytest governance/compat/test_run_adif_finding_intake_bridge.py -v
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-selected continuous sequence and bridge standard absorbed into this joint T3/T4 dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T3 preflight readout; ADIF-T4 finding intake bridge |
| Disposition | ADAPT as bounded CVF-owned internal helpers; no external surface authorized |
| Claim boundary | roadmap tranche specs and bridge standard are design input only; this baseline and the canonical authorization are the CVF-governed dispatch authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_automation_assist.py` is 1320 lines, already over the 1200-line Python automation hard threshold per `check_python_automation_size.py`, without an approved exception; ADIF-T3 therefore creates a new sibling module instead of extending it |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed by ADIF-T3/T4 |
| Runtime behavior claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no provider, public-sync, or external-adapter behavior is claimed; the pre-existing AAF helper size violation is recorded as a separate F2G finding below, not repaired in this batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T3 read-only preflight readout and ADIF-T4 bounded finding-intake bridge, dispatched jointly |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: both helpers return data/classification only; neither performs or records a mutating action |
| invocationBoundary | local repository function calls, governed by direct Python import |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | read-only preflight readout (T3) and bounded, non-auto-promoting finding-intake classification (T4) only |
| forbiddenExpansion | CLI/MCP adapter, filesystem mutation beyond named files, autorun/hook wiring, auto-promotion, runtime/provider/live, public-sync, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without a preflight readout, agents cannot see relevant defect entries during pre-implementation without manually calling the resolver | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T3 implements the bounded readout helper | handled by this tranche |
| Without a bounded intake bridge, reviewer findings and worker friction have no structured path into the ADIF dictionary | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T4 implements the bounded, non-auto-promoting intake function | handled by this tranche |
| `governance/compat/run_agent_automation_assist.py` already exceeds the Python automation hard size threshold (1320/1200 lines) without an approved exception | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | route to a separate governed batch for a file-size exception or split; not in ADIF-T3/T4 scope | deferred - `SEPARATE_RUNTIME_TRANCHE` |
| Runtime/provider/cost applicability for ADIF-T3/T4 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T3` and `## ADIF-T4`
  tranche definitions.
- Predecessor intake artifact: ADIF-T2 checkpoint review and the new
  Continuous Execution Handoff-Sync Bridge Standard.
- Delta ledger status: `CHANGED_DISPOSITION` - T3 and T4 are now dispatched
  jointly with explicit disjoint-write-ownership declarations and a bridge
  protocol, rather than as independent sequential checkpoints.
- Routing matrix status: `DO_NOW` for the T3 readout and T4 intake bridge,
  their tests, and joint dispatch packet; `OUT_OF_SCOPE` for any CLI/MCP
  adapter or auto-promotion behavior.
- Semantic sampling status: sampled the ADIF-T0 contract, all eight
  ADIF-T1 entries, the ADIF-T2 resolver and contract, the ADIF-T2
  checkpoint review, the Continuous Execution Handoff-Sync Bridge
  Standard, F2G, and FPRC directly before authoring.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T3/T4 scope matches the roadmap tranche definitions exactly. |
| CHANGED_DISPOSITION | T3/T4 now dispatched as one joint parallel batch per the new bridge standard, rather than sequential single-tranche dispatches. |
| NEW_FINDING | `run_agent_automation_assist.py` already exceeds the Python automation hard size threshold; routed to a separate batch, not repaired here. |
| REMOVED_OR_REJECTED | CLI/MCP adapter, autorun/hook wiring, auto-promotion, and T5 scope remain rejected for this dispatch. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T3 read-only preflight readout, ADIF-T4 bounded finding-intake bridge, their focused tests, and this joint dispatch packet. |
| RESOLVED_BY_DESIGN | ADIF-T0's canonical-reuse field boundary and ADIF-T1's fixed entry shape govern every T3/T4 input/output field. |
| DEFER | ADIF-T5 promotion-lifecycle and drift guard. |
| SEPARATE_RUNTIME_TRANCHE | any future CLI/MCP adapter; the pre-existing AAF helper size-threshold violation. |
| STRATEGIC_OPERATOR_DECISION | whether and when a CLI/MCP adapter or autorun wiring is ever authorized remains open for a later, separately source-verified tranche. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity beyond the bounded bridge ledger row, auto-promotion. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T3T4-RS1 | ADIF roadmap T3 | T3 must not silently create a competing autorun process | DO_NOW | Does the T3 readout module get wired into any autorun phase command list in this batch? | PASS - `run_adif_preflight_readout.py` is a standalone callable module; it is not added to `run_agent_autorun_workflow_gate.py`'s command list |
| ADIF-T3T4-RS2 | ADIF roadmap T4 | T4 must not auto-promote every finding; required outcomes include reject as non-reusable/session-local with reason | DO_NOW | Does the T4 intake function ever write a new canonical entry file or change `enforcementLevel`/`lifecycleState` on disk? | PASS - intake function returns a classification only; no entry file is created, modified, or promoted |
| ADIF-T3T4-RS3 | canonical authorization Parallel Fork And Convergence Protocol | T3 and T4 child packets must declare disjoint write ownership; if paths overlap, parallel execution is forbidden | DO_NOW | Do the Write Ownership tables in the paired work order list any shared path between T3 and T4? | PASS - four distinct new files, two per branch, with zero path overlap |

## Corpus Completeness And Report Integrity

- Corpus task class: joint dispatch source verification for two bounded
  parallel governance-implementation tranches.
- Corpus root: repo-local source files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-23 ADIF-T3/T4 joint dispatch authoring.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no
  generated corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=13; ledger_terminal=13 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no historical finding corpus scan, no CLI/MCP
  adapter source, no public repository scan, no provider-local memory
  intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no generated aggregate created; both
  helpers read compact per-entry source files directly through the
  existing ADIF-T2 resolver.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: T3 readout fields map to resolver output fields; T4
  intake outcomes map to F2G disposition and FPRC defectRole vocabularies.
- Adversarial verification: checked for filesystem-mutation risk, write
  ownership overlap, and auto-promotion risk before authoring.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| ADIF governed artifact | committed implementation and final-review acceptance | PASS |
| GC-051 corpus registration | generated JSON aggregate and retained human companion | PASS |
| Runtime/provider receipt | N/A with reason: no runtime/provider/live claim | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T3/T4 is private provenance governance-implementation work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T3/T4 joint child dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, pytest, governance gates, git commit, git worktree |
| Target paths | this baseline; paired work order; T3 readout module and test; T4 intake bridge module and test; ADIF front door update; roadmap row updates |
| Allowed scope source | canonical continuous-execution authorization, master work order, ADIF-T2 checkpoint review, and Continuous Execution Handoff-Sync Bridge Standard |
| Before status evidence | dispatchBaseHead `adaecb04`; clean worktree confirmed; pre-implementation autorun 47/47 PASS |
| After status evidence | joint T3/T4 dispatch committed; isolated worktrees fork from the post-dispatch handoff-sync bridge HEAD |
| Diff evidence | joint dispatch-batch name-status and committed diff |
| Approval boundary | ADIF-T3/T4 joint dispatch scope only; no T5 implementation in this packet |
| Claim boundary | conditional parallel execution chain with evidence gates; no runtime/public/provider/external-adapter expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t3-t4-joint-dispatch-2026-06-23` |
| Expected manifest | this baseline; paired work order; T3 readout module and test; T4 intake bridge module and test; ADIF front door update; roadmap row updates |
| Actual changed set | recorded in the joint dispatch commit |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | T3 readout calls the existing ADIF-T2 resolver and formats a bounded human-readable result; it does not duplicate resolver logic. |
| AC2 | T3 does not create or wire into any competing autorun process in this batch. |
| AC3 | T4 intake function returns exactly one of the five required outcomes per finding, never auto-promoting. |
| AC4 | T4 preserves F2G disposition and FPRC defectRole vocabularies without redefining them. |
| AC5 | T3 and T4 declare fully disjoint write ownership; no shared path. |
| AC6 | Focused tests for both modules pass with full coverage of their required behaviors. |
| AC7 | Dual Agent Surface Matrix is present at dispatch time with both rows populated. |
| AC8 | No CLI entry point, MCP registration, or autorun/hook wiring is created by either tranche. |
| AC9 | Joint dispatch commit, then isolated worktree execution per the bridge protocol, with no Codex pause between T3, T4, and T5. |

## Claim Boundary

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | joint T3/T4 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | final ADIF completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | ADIF roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ADIF-T0-T5 entry generated from registry source | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | human companion retained; no quick-lookup delta required | PASS |
| External evidence digest | N/A | no external evidence intake | N/A with reason |
| Session continuity | active session surfaces | separate post-closure sync follows | N/A with reason |
| System loop interlock | N/A | no runtime loop changed | N/A with reason |

## Claim Boundary

This baseline authorizes only the joint ADIF-T3/T4 dispatch and their
isolated-worktree execution inside the canonical continuous-execution
chain's `PARALLEL_RELEASE_A`/`PARALLEL_RELEASE_B` step. It does not
authorize ADIF-T5 implementation, any CLI/MCP adapter, runtime/provider/
live behavior, public-sync, or final closure. Codex remains the designated
final reviewer/closer for the complete T0-T5 chain and reviews the full
graph after T5.
