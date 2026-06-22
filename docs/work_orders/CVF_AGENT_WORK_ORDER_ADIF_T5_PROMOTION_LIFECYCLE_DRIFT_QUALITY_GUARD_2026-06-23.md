# CVF Agent Work Order - ADIF-T5 Promotion Lifecycle, Drift, And Quality Guard

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-06-23

docType: work_order

closureBaseHead: NOT_EXECUTED_YET

## Dispatch Prompt Envelope

Role: Claude continuous-execution orchestrator/worker, executing the sixth
and final child tranche of the ADIF chain. Codex is the designated final
reviewer/closer for the whole T0-T5 chain, reviewing once after this
tranche, per the operator's explicit continuous-execution instruction.

Canonical packet:
`docs/baselines/CVF_GC018_ADIF_T5_PROMOTION_LIFECYCLE_DRIFT_QUALITY_GUARD_2026-06-23.md`

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: `2b93b314` (the ADIF-T3/T4 convergence handoff-sync
bridge HEAD).

executionBaseHead: `2b93b314` (confirmed via `git rev-parse --short HEAD`
before any edit in this batch).

Current-time notes: this is the sixth and final tranche of the ADIF
continuous chain. The guard does not edit any hook chain or authorize
runtime behavior, per the roadmap's explicit T5 constraint.

Do-not-misread notes: the guard only reads the eight committed entries via
the existing `load_entries` helper; it never repairs a violation it finds,
and it is not wired into any autorun phase or hook chain in this tranche.

Required first actions: read the canonical authorization, the master work
order, the ADIF roadmap's T5 section, the ADIF-T0 contract, the entry
template's enum/lifecycle sections, and the ADIF-T2 resolver before
implementing the guard.

Return contract: this packet is returned `COMPLETE_PENDING_REVIEW`; per
the operator's instruction, Claude stops once after committing the T5
checkpoint and returns the complete T0-T5 graph to Codex for final review.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one standalone entry-integrity
machine guard plus its focused test under `governance/compat/` for
ADIF-T5 only, per the paired GC-018 baseline.

Protected paths (every changed guard/control path is listed):

- `governance/compat/check_adif_entry_integrity.py`
- `governance/compat/test_check_adif_entry_integrity.py`

Operator authorization: the operator pre-selected the T0-T5 continuous
sequence and instructed Claude to execute T3->T4->T5 continuously without
a Codex pause between these tranches.

Rollback boundary: if ADIF-T5 is rejected, remove only the two new guard
paths above, this work order, and its paired GC-018 baseline. Do not
revert the ADIF-T3/T4 convergence (`2b93b314`) or any earlier ADIF
checkpoint.

Scope boundary: this authorization does not extend to existing guard
behavior, active session files, root handoff files beyond the bounded
bridge ledger row, runtime/product source, public-sync, provider/live
proof, direct-interception tooling, any CLI/MCP adapter, or autorun/hook
chain wiring.

## Mission

Implement the ADIF-T5 standalone entry-integrity machine guard and its
focused tests, per the GC-018 baseline.

## Purpose

Translate the canonical continuous-execution authorization's sixth and
final sequence step into a source-verified, bounded ADIF-T5 execution that
detects entry-integrity drift without auto-repairing it or claiming
runtime authority.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority; pre-selected the T0-T5 continuous sequence; instructed T3->T4->T5 as one continuous run |
| Dispatcher | Claude authors this final child packet |
| Orchestrator/worker | Claude |
| Reviewer/closer | Codex, once after the complete T0-T5 graph returns |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Claude orchestrates and executes ADIF-T5 under `WORKER_MAY_COMMIT`; Codex reviews and closes the complete T0-T5 chain once after this tranche |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE |
| baseHeadFor(phase) | `dispatchBaseHead=2b93b314`; `executionBaseHead=2b93b314`; `closureBaseHead` captured by Codex after this tranche |
| changedSetScope(phase) | dispatch/execution = this work order, T5 baseline, integrity guard module, integrity guard test, ADIF front door update, roadmap row update; closure = Codex-owned final review of the complete T0-T5 graph |
| traceScope(phase, actor) | one trace covers this T5 child dispatch and execution; Codex's final trace covers the complete-graph review |
| commitOwner(phase) | Claude commits this T5 checkpoint under `WORKER_MAY_COMMIT`; Codex owns the final closure/session-sync commit |
| crossBatchIsolation | T5 is the final tranche; no further ADIF child packet follows without new operator authorization |
| nextMoveSurfaces | Claude does not edit session state, the review queue, or any handoff content beyond the bounded bridge ledger row; Codex owns final session sync after accepting this batch |
| Closer designation | Codex |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| ADIF-T5 GC-018 baseline | `docs/baselines/CVF_GC018_ADIF_T5_PROMOTION_LIFECYCLE_DRIFT_QUALITY_GUARD_2026-06-23.md` | ACCEPT |
| ADIF-T3/T4 convergence bridge | `2b93b314` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |

## Required First Reads

- `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md`
- `docs/baselines/CVF_GC018_ADIF_T5_PROMOTION_LIFECYCLE_DRIFT_QUALITY_GUARD_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
- `governance/compat/run_adif_defect_resolver.py`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2b93b314 --head HEAD
```

## Scope / Owner Boundary

Allowed scope: create `governance/compat/check_adif_entry_integrity.py`
and `governance/compat/test_check_adif_entry_integrity.py`, this work
order, and the paired GC-018 baseline; update the ADIF front door and the
roadmap's ADIF-T5 row only. See the paired GC-018 baseline's
`## Scope / Owner Boundary` for the full Allowed scope and Forbidden scope
lists, which this work order inherits in full.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/check_adif_entry_integrity.py` | Claude (this tranche) | create |
| `governance/compat/test_check_adif_entry_integrity.py` | Claude (this tranche) | create |
| `docs/reference/agent_defect_intelligence/README.md` | Claude (this tranche) | update front-door pointers only |
| `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Claude (this tranche) | update ADIF-T5 row only |
| this work order; ADIF-T5 GC-018 baseline | Claude (this tranche) | create, commit |

## Forbidden Scope

- no autorun/hook chain wiring;
- no automatic edit of any entry file;
- no runtime behavior authorization;
- no CLI entry point beyond the guard's own diagnostic CLI; no MCP
  registration or external adapter wiring;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no runtime, provider/live, public-sync, or session-continuity edit
  beyond the bounded bridge ledger row;
- no claim of ADIF closure.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one new standalone `governance/compat/check_adif_entry_integrity.py` checker plus matching test file, following existing flat-import `check_*.py` conventions |
| Storage decision | one integrity guard module, one test module; no generated aggregate; no relocation or refactor of any existing file |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | read-only diagnostic over committed entry files via the existing resolver's loader; no autorun/hook wiring, no CLI/MCP surface |

## Execution Plan

1. Confirm `executionBaseHead` and clean worktree.
2. Read all Required First Reads.
3. Implement `check_adif_entry_integrity.py` covering all six violation
   classes named in the GC-018 baseline's Acceptance Criteria.
4. Implement `test_check_adif_entry_integrity.py` with focused coverage of
   each violation class plus a clean-pass case.
5. Run focused tests; confirm all pass.
6. Confirm no autorun/hook-chain wiring via `grep`.
7. Update the ADIF front door and the roadmap's ADIF-T5 row.
8. Run real-range pre-implementation gate; repair and rerun until clean.
9. Commit the ADIF-T5 checkpoint.
10. Stop and return the complete T0-T5 graph to Codex for final review.

## Evidence Requirements

- actual `executionBaseHead` and `git status --short`;
- pre-implementation autorun result over the real range;
- `python -m pytest governance/compat/test_check_adif_entry_integrity.py -v`
  result with all tests passing;
- explicit statement that no CLI/MCP/autorun/hook file was created or
  modified;
- `git log --graph --oneline` excerpt showing the complete T0-T5 commit
  graph;
- exact claim boundary and public export disposition.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Fixed enum values for `severity`, `lifecycleState`, `enforcementLevel` | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Required Fields | `severity`; `lifecycleState`; `enforcementLevel` | ADIF entry template | VALUE_SET | ACCEPT |
| Existing entry loader to reuse rather than reimplement | `governance/compat/run_adif_defect_resolver.py` | `load_entries`; `ENTRIES_DIR` | `load_entries` | ADIF-T2 resolver | EXISTS | ACCEPT |

## Worker Autonomy / No-Question Rule

Claude repairs and reruns all allowed-scope gate failures on its own
initiative. Claude stops only for the canonical packet's Stop Conditions,
or at the end of this tranche to return the complete T0-T5 graph.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | roadmap T5 spec ADAPTed into a bounded standalone internal guard |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T5 entry integrity guard |
| Disposition | ADAPT as bounded CVF-owned internal guard |
| Claim boundary | roadmap spec is design input only |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T5` tranche definition.
- Predecessor intake artifact: integrated ADIF-T3/T4 convergence.
- Delta ledger status: `UNCHANGED_FROM_INTAKE` - T5 scope matches the
  roadmap definition exactly.
- Routing matrix status: `DO_NOW` for the integrity guard and its tests;
  `OUT_OF_SCOPE` for autorun/hook-chain wiring.
- Semantic sampling status: sampled the ADIF-T0 contract, the entry
  template's enum/lifecycle sections, and the ADIF-T2 resolver's loader.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T5 scope matches the roadmap tranche definition exactly. |
| CHANGED_DISPOSITION | None for this tranche. |
| NEW_FINDING | None beyond the already-recorded hook-chain-wiring deferral. |
| REMOVED_OR_REJECTED | autorun/hook-chain wiring, automatic entry repair, and any CLI/MCP adapter remain rejected for ADIF-T5. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T5 standalone entry-integrity guard and its focused tests. |
| RESOLVED_BY_DESIGN | ADIF-T0's enum/lifecycle contract defines exactly what the guard checks. |
| DEFER | none remaining inside the ADIF roadmap; T0-T5 is the full named sequence. |
| SEPARATE_RUNTIME_TRANCHE | any future CLI/MCP adapter for the guard or resolver. |
| STRATEGIC_OPERATOR_DECISION | whether and when to wire the guard into autorun/hook chains. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity beyond the bounded bridge row, automatic entry repair. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T5-WO-RS1 | ADIF roadmap T5 | T5 does not automatically edit hook chains or authorize runtime behavior | DO_NOW | Is the guard added to any autorun/hook command list in this tranche? | PASS - confirmed via `grep` before commit |
| ADIF-T5-WO-RS2 | ADIF entry template Enforcement Level Verification Rule | dishonest enforcement claims must be detected | DO_NOW | Does a focused test prove detection of a fabricated `checkerBindings` path? | PASS - dedicated fixture and assertion in the test suite |

## Corpus Completeness And Report Integrity

- Corpus task class: work-order dispatch source verification for a
  bounded governance-implementation tranche.
- Corpus root: repo-local source files named in Required First Reads.
- Snapshot time: 2026-06-23 ADIF-T5 execution.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Required First Reads and Source
  Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=6; ledger_terminal=6 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no `.private_reference/legacy` scan, no runtime/web/
  MCP scan, no public-sync corpus scan, no provider-local memory intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: each violation class maps to a named ADIF-T0/T1
  contract rule.
- Adversarial verification: checked for filesystem-mutation risk and
  autorun-wiring risk before commit.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without an integrity guard, entry-integrity drift could accumulate silently | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T5 implements the bounded standalone guard | handled |
| Whether to wire the guard into autorun/hook chains | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | the roadmap forbids automatic hook-chain edits here; routed to a later, separately authorized decision | deferred - `STRATEGIC_OPERATOR_DECISION` |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed | handled |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: ADIF-T5 implements a deterministic
read-only integrity guard verified by focused tests, not an
evidence-comparison or hypothesis-testing narrative.

## Machine Closure Package

This work order does not claim ADIF closed in the canonical sense; closure
of the complete T0-T5 chain belongs to Codex after this batch returns.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ADIF_T5_PROMOTION_LIFECYCLE_DRIFT_QUALITY_GUARD_2026-06-23.md` | `Status: AUTHORIZED_FOR_CONTINUOUS_EXECUTION` | PASS |
| Integrity guard module | `governance/compat/check_adif_entry_integrity.py` | focused tests pass | PASS |
| Completion or reviewer artifact | N/A with reason: Codex reviews and closes the complete T0-T5 chain once after this tranche | N/A with reason | N/A with reason |
| Session continuity | active session front-door/state/handoff | N/A with reason: session-sync is forbidden in this batch and remains Codex-owned | N/A with reason |
| System loop interlock | focused tests | all pass | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T5 is private provenance governance-implementation work. No
public-sync repository work or public catalog claim is authorized.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: ADIF-T5 authorizes a local read-only helper only |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed |
| Freshness disposition | PASS - no runtime, provider, public-sync, or external-adapter behavior is claimed |

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | direct Python import / function call, or standalone CLI invocation, of `governance/compat/check_adif_entry_integrity.py` | read-only diagnostic; no commit/action authority; not wired into any autorun phase or hook chain | `governance/compat/test_check_adif_entry_integrity.py` | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP adapter, not created in this tranche | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, or public claim exists or is authorized | ADIF-T1/T2 checkpoint reviews' deferred disposition; Forbidden Scope above | `DEFERRED_WITH_REASON` - no adapter exists; requires a separate source-verified GC-018/work order |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T5 standalone entry-integrity guard execution only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: guard reports violations only |
| invocationBoundary | local repository function call or standalone CLI invocation |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | read-only entry-integrity diagnostic guard only |
| forbiddenExpansion | autorun/hook chain wiring, automatic entry repair, CLI/MCP adapter, runtime/provider/live, public-sync, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T5 execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, pytest, governance gates, git commit |
| Target paths | this work order; T5 baseline; integrity guard module; integrity guard test; ADIF front door update; roadmap row update |
| Allowed scope source | ADIF-T5 GC-018 baseline, canonical continuous-execution authorization, and integrated ADIF-T3/T4 convergence |
| Before status evidence | executionBaseHead `2b93b314`; clean worktree confirmed |
| After status evidence | ADIF-T5 checkpoint committed; complete T0-T5 graph returned to Codex |
| Diff evidence | child-batch name-status and committed diff |
| Approval boundary | ADIF-T5 child scope only |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider/external-adapter expansion; no ADIF closure claim |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t5-execution-2026-06-23` |
| Expected manifest | this work order; T5 baseline; integrity guard module; integrity guard test; ADIF front door update; roadmap row update |
| Actual changed set | recorded in the ADIF-T5 checkpoint commit |
| Manifest delta | MATCH |

WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond the usual checks
this return.

## Operator Checkpoint

The human principal pre-selected the entire continuous sequence and this
turn separately instructed Claude to run T3->T4->T5 continuously without a
Codex pause. A fresh pause applies only to scope/risk/claim expansion,
runtime/provider/live/public work, secrets/quota, destructive action,
canonical-owner semantic change, or a different execution order than the
one named above.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Guard detects dangling `checkerBindings` paths | focused test |
| AC2 | Guard detects dangling `supersedes` references | focused test |
| AC3 | Guard detects duplicate `defectId` values | focused test |
| AC4 | Guard detects stale supersession | focused test |
| AC5 | Guard detects invalid enum values | focused test |
| AC6 | Guard detects dishonest enforcement claims | focused test |
| AC7 | Guard never mutates any entry file | focused test |
| AC8 | Guard is not wired into autorun/hook chains | `grep` |
| AC9 | Focused tests pass | `pytest` run |
| AC10 | Execution stops once after T5; complete graph returned to Codex | this return |

## Review Gate

Codex performs final review and closure of the complete T0-T5 graph after
this tranche, per the canonical authorization's Return Contract.

## Closure Checklist

- [x] ADIF-T3/T4 convergence released T5.
- [x] ADIF-T5 child GC-018 and work order exist and are source-verified.
- [x] ADIF-T5 deliverables are created inside Allowed scope only.
- [x] Pre-implementation autorun gate passes over the real range.
- [x] Focused tests pass.
- [x] No CLI/MCP/autorun/hook file was created or modified.
- [x] Execution stopped after the T5 checkpoint commit.
- [ ] Codex final review and closure of the complete T0-T5 graph (pending;
      owned by Codex, not this child packet).

## Return-To-Orchestrator Conditions

Return success only as `COMPLETE_PENDING_REVIEW` for this final child
tranche, accompanied by the complete T0-T5 graph summary. Return
`BLOCKED_WITH_REASON` for any Stop Condition in the canonical
authorization. Do not claim final closure - that is Codex's after this
batch returns.

## Claim Boundary

This work order authorizes and records execution of only the ADIF-T5
standalone entry-integrity guard tranche, the final step of the canonical
continuous-execution chain. It does not authorize any CLI/MCP adapter,
runtime/provider/live behavior, public-sync, autorun/hook-chain wiring, or
final closure. Codex remains the designated final reviewer/closer for the
complete T0-T5 chain.
