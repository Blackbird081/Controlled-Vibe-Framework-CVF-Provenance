# CVF GC-018 - ADIF-T5 Promotion Lifecycle, Drift, And Quality Guard

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_CONTINUOUS_EXECUTION

Date: 2026-06-23

docType: gc018_baseline

dispatchBaseHead: 2b93b314

executionBaseHead: NOT_EXECUTED_YET

closureBaseHead: NOT_EXECUTED_YET

Commit mode: `WORKER_MAY_COMMIT`

Batch ID: ADIF-T5

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one machine guard checker plus
its focused test under `governance/compat/` for ADIF-T5 only, per the
canonical continuous-execution authorization's final sequence step.

Protected paths (every changed guard/control path is listed):

- `governance/compat/check_adif_entry_integrity.py`
- `governance/compat/test_check_adif_entry_integrity.py`

Operator authorization: the operator pre-selected the T0-T5 continuous
sequence and instructed Claude to execute T3->T4->T5 continuously without
a Codex pause between these tranches.

Rollback boundary: if ADIF-T5 is rejected, remove only the two new guard
paths above, this baseline, and its paired work order. Do not revert the
ADIF-T3/T4 convergence (`2b93b314`) or any earlier ADIF checkpoint.

Scope boundary: this authorization does not extend to existing guard
behavior, active session files, root handoff files beyond the bounded
bridge ledger row, runtime/product source, public-sync, provider/live
proof, direct-interception tooling, any CLI/MCP adapter, or autorun/hook
chain wiring.

## Purpose

Authorize the sixth and final child tranche of the ADIF continuous-
execution chain. ADIF-T5 creates a standalone machine guard that checks
the integrity of every committed ADIF entry: dangling sources/checker
bindings, duplicate IDs, stale supersession references, invalid enum
values, and dishonest `enforcementLevel` claims (a `MACHINE_CHECKED` or
`PARTIAL_CHECK` claim whose `checkerBindings` path does not exist).

This baseline is authorized under, and subordinate to, the canonical
continuous-execution packet and the integrated T3/T4 convergence. It does
not waive that packet's Stop Conditions or Codex final-review requirement.
It does not automatically edit any hook chain or authorize runtime
behavior, per the roadmap's explicit T5 constraint.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| Master work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CONTINUOUS_EXECUTION_T0_T5_FOR_CLAUDE_2026-06-22.md` | ACCEPT |
| ADIF-T3/T4 joint dispatch | `af56db7c` | ACCEPT |
| ADIF-T3 branch checkpoint | `41b026a6` | ACCEPT |
| ADIF-T4 branch checkpoint | `fb4bac23` | ACCEPT |
| ADIF-T3/T4 convergence bridge | `2b93b314` | ACCEPT - integrated checkpoint evidence; releases T5 per `CONVERGENCE_RELEASE` |
| ADIF-T0 owner-reconciliation contract | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | ACCEPT |
| ADIF entry template and eight seed entries | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | ACCEPT |
| ADIF-T2 resolver | `governance/compat/run_adif_defect_resolver.py` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF-T5 prerequisite, output (machine guard for entry integrity, dangling sources/checker bindings, duplicate IDs, stale supersession, invalid enum values, dishonest enforcement-level claims), and constraint (no automatic hook-chain edit or runtime authorization) | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T5 - Promotion Lifecycle, Drift, And Quality Guard | T5 tranche definition | ADIF roadmap | VALUE_SET | ACCEPT |
| Fixed enum values: `severity` is `LOW \| MEDIUM \| HIGH`; `lifecycleState` is `PROPOSED \| ACTIVE \| SUPERSEDED \| RETIRED \| REJECTED`; `enforcementLevel` is `GUIDANCE_ONLY \| PARTIAL_CHECK \| MACHINE_CHECKED \| RETIRED` | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Required Fields | `severity`; `lifecycleState`; `enforcementLevel` | ADIF entry template | VALUE_SET | ACCEPT |
| `MACHINE_CHECKED`/`PARTIAL_CHECK` requires a `checkerBindings` path that exists in the repository at authoring or last re-verification time, else fall back to a weaker level | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Enforcement Level Verification Rule | enforcement verification rule | ADIF entry template | LITERAL_INVARIANT | ACCEPT |
| Entries are never deleted; retirement/supersession is a `lifecycleState`/`supersedes` state transition only | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Lifecycle And Retirement | lifecycle/supersession rule | ADIF entry template | LITERAL_INVARIANT | ACCEPT |
| Each entry's exact field values, including `defectId`, `supersedes`, `enforcementLevel`, `checkerBindings`, `lifecycleState`, `severity` | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | fenced field block in each file | per-entry field values | ADIF-T1 seed entries | EXISTS | ACCEPT |
| Entry parsing helper (`_parse_field_block`, `load_entries`) already exists and is reusable | `governance/compat/run_adif_defect_resolver.py` | `_parse_field_block`; `load_entries`; `ENTRIES_DIR` | `load_entries` | ADIF-T2 resolver | EXISTS | ACCEPT |
| Existing flat-import checker pattern: standalone `check_*.py` module with `--base`/`--head`/`--enforce` CLI and a `main()` returning a process exit code | `governance/compat/check_work_order_dispatch_quality.py` | argument parser and `main()` shape | `main` | dispatch-quality checker | EXISTS | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create `governance/compat/check_adif_entry_integrity.py` - a standalone,
  read-only machine guard that loads all committed ADIF entries (via the
  existing `run_adif_defect_resolver.load_entries` helper) and reports:
  dangling `checkerBindings` paths, dangling `supersedes` references,
  duplicate `defectId` values, stale supersession (an `ACTIVE` entry
  superseded by another `ACTIVE` entry, or a cycle), invalid enum values
  for `severity`/`lifecycleState`/`enforcementLevel`, and dishonest
  enforcement claims (`MACHINE_CHECKED`/`PARTIAL_CHECK` whose
  `checkerBindings` path does not exist);
- create `governance/compat/test_check_adif_entry_integrity.py` with
  focused tests covering each violation class plus a clean-pass case;
- create local checkpoint commit for this tranche only.

Forbidden scope:

- no autorun/hook chain wiring - the guard is callable standalone via its
  own CLI, mirroring the existing `check_*.py` pattern, but is not added
  to any `run_agent_autorun_workflow_gate.py` command list or the
  pre-commit hook chain in this tranche;
- no automatic edit of any entry file - the guard reports violations only,
  it never repairs them;
- no runtime behavior authorization;
- no CLI entry point beyond the guard's own diagnostic CLI; no MCP
  registration or external adapter wiring;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no runtime, provider/live, public-sync, or session-continuity edit
  beyond the bounded bridge ledger row;
- no claim of ADIF closure - closure of the complete T0-T5 chain remains
  Codex's after this tranche returns.

Risk ceiling: R1 - read-only diagnostic guard with no filesystem mutation,
no external surface, no autorun wiring, and full focused-test coverage
before its checkpoint commit.

## Required Deliverables

- `governance/compat/check_adif_entry_integrity.py`
- `governance/compat/test_check_adif_entry_integrity.py`
- this GC-018 baseline
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T5_PROMOTION_LIFECYCLE_DRIFT_QUALITY_GUARD_2026-06-23.md`
- `docs/reference/agent_defect_intelligence/README.md` (front-door pointer
  update only)
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  (ADIF-T5 row only)

## Decision / Baseline / Proposed Tranche

Decision: authorize ADIF-T5 for continuous execution under the canonical
ADIF authorization, released by the integrated ADIF-T3/T4 convergence.
Baseline: dispatch base `2b93b314`. Proposed tranche: ADIF-T5 Promotion
Lifecycle, Drift, And Quality Guard, executed and committed by Claude
under `WORKER_MAY_COMMIT`, then one final stop for Codex review of the
complete T0-T5 graph.

## Dependency Release Evidence

| Prerequisite artifact | Closure or dispatch commit | Disposition | Gate evidence |
|---|---|---|---|
| ADIF-T3 branch checkpoint | `41b026a6` | ACCEPT | committed; 7/7 focused tests pass |
| ADIF-T4 branch checkpoint | `fb4bac23` | ACCEPT | committed; 10/10 focused tests pass |
| ADIF-T3/T4 convergence bridge | `2b93b314` | ACCEPT | combined 30/30 focused tests pass; pre-implementation autorun 47/47 PASS over the converged range |

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | direct Python import / function call, or standalone CLI invocation, of `governance/compat/check_adif_entry_integrity.py` | read-only diagnostic; no filesystem mutation; no commit/action authority; not wired into any autorun phase or hook chain in this tranche | this baseline, paired work order, and focused tests in the new test module | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP adapter, not created in this tranche | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, or public claim exists or is authorized by ADIF-T5 | ADIF-T1/T2 checkpoint reviews' deferred disposition; this baseline's Forbidden Scope | `DEFERRED_WITH_REASON` - no adapter exists; a future CLI/MCP surface requires its own source-verified GC-018/work order |

## Evidence / Verification

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2b93b314 --head HEAD
python -m pytest governance/compat/test_check_adif_entry_integrity.py -v
python governance/compat/check_adif_entry_integrity.py --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-selected continuous sequence and roadmap T5 spec ADAPTed into a bounded, standalone internal guard |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T5 entry integrity guard |
| Disposition | ADAPT as bounded CVF-owned internal guard; no external surface authorized |
| Claim boundary | roadmap tranche spec is design input only; this baseline and the canonical authorization are the CVF-governed dispatch authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: ADIF-T5 authorizes a read-only local Python guard only; no runtime route, provider gateway, or model registry behavior is changed |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed by ADIF-T5 |
| Runtime behavior claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no provider, public-sync, or external-adapter behavior is claimed; no autorun/hook chain wiring is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T5 standalone entry-integrity guard implementation only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: guard reports violations only; it does not perform or record a repair action |
| invocationBoundary | local repository function call or standalone CLI invocation |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | read-only entry-integrity diagnostic guard only |
| forbiddenExpansion | autorun/hook chain wiring, automatic entry repair, CLI/MCP adapter, runtime/provider/live, public-sync, and universal control remain out of scope for ADIF-T5 |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without an integrity guard, dangling checker bindings, duplicate IDs, or dishonest enforcement claims could accumulate silently as the ADIF dictionary grows | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T5 implements the bounded standalone guard | handled by this tranche |
| Whether to wire the guard into autorun/hook chains | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | the roadmap explicitly forbids automatic hook-chain edits in this tranche; routed as a separate, later, operator-authorized decision | deferred - `STRATEGIC_OPERATOR_DECISION` |
| Runtime/provider/cost applicability for ADIF-T5 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T5` tranche definition.
- Predecessor intake artifact: integrated ADIF-T3/T4 convergence and the
  ADIF-T0/T1 entry-shape contracts.
- Delta ledger status: `UNCHANGED_FROM_INTAKE` - T5 scope matches the
  roadmap definition exactly; no reviewer-driven scope change preceded
  this dispatch.
- Routing matrix status: `DO_NOW` for the standalone integrity guard and
  its tests; `OUT_OF_SCOPE` for autorun/hook-chain wiring.
- Semantic sampling status: sampled the ADIF-T0 contract, the entry
  template's enum and lifecycle sections, all eight ADIF-T1 entries, and
  the ADIF-T2 resolver's existing parsing helpers directly before
  authoring.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T5 scope matches the roadmap tranche definition exactly. |
| CHANGED_DISPOSITION | None for this tranche; the Dual Agent Surface Matrix pattern from T2-T4 is reused, not changed. |
| NEW_FINDING | None beyond the already-recorded hook-chain-wiring deferral. |
| REMOVED_OR_REJECTED | autorun/hook-chain wiring, automatic entry repair, and any CLI/MCP adapter remain rejected for ADIF-T5. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T5 standalone entry-integrity guard and its focused tests. |
| RESOLVED_BY_DESIGN | ADIF-T0's enum/lifecycle contract and ADIF-T1's fixed entry shape define exactly what the guard checks. |
| DEFER | none remaining inside the ADIF roadmap; T0-T5 is the full named sequence. |
| SEPARATE_RUNTIME_TRANCHE | any future CLI/MCP adapter for the guard or the resolver. |
| STRATEGIC_OPERATOR_DECISION | whether and when to wire the guard into autorun/hook chains. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity beyond the bounded bridge row, automatic entry repair. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T5-RS1 | ADIF roadmap T5 | T5 does not automatically edit hook chains or authorize runtime behavior | DO_NOW | Is the new guard added to `run_agent_autorun_workflow_gate.py` or `run_local_governance_hook_chain.py` in this tranche? | PASS - the guard is a standalone module; it is not added to either command list |
| ADIF-T5-RS2 | ADIF entry template Enforcement Level Verification Rule | `MACHINE_CHECKED`/`PARTIAL_CHECK` requires a verifiable `checkerBindings` path | DO_NOW | Does a focused test prove the guard flags a fabricated `checkerBindings` path as a violation? | PASS - test suite includes a dishonest-enforcement-claim fixture asserting a violation |
| ADIF-T5-RS3 | ADIF entry template Lifecycle And Retirement | entries are never deleted; supersession is a state transition only | DO_NOW | Does the guard ever delete or rewrite an entry file when it finds a violation? | PASS - the guard is read-only; it returns a violations report and never writes |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded
  governance-implementation tranche.
- Corpus root: repo-local source files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-23 ADIF-T5 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=10; ledger_terminal=10 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no historical finding corpus scan, no CLI/MCP
  adapter source, no public repository scan, no provider-local memory
  intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: the guard reads compact per-entry
  source files directly; no generated aggregate is created or consumed.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: each violation class maps directly to a named
  ADIF-T0/T1 contract rule.
- Adversarial verification: checked for filesystem-mutation risk and
  autorun-wiring risk before implementation.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T5 is private provenance governance-implementation work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T5 child dispatch and execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, pytest, governance gates, git commit |
| Target paths | this baseline; paired work order; integrity guard module; integrity guard test; ADIF front door update; roadmap row update |
| Allowed scope source | canonical continuous-execution authorization, master work order, and integrated ADIF-T3/T4 convergence |
| Before status evidence | dispatchBaseHead `2b93b314`; clean worktree confirmed; pre-implementation autorun 47/47 PASS |
| After status evidence | ADIF-T5 child packet and deliverables committed as the final checkpoint; one final stop for Codex review of the complete T0-T5 graph |
| Diff evidence | child-batch name-status and committed diff |
| Approval boundary | ADIF-T5 child scope only |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider/external-adapter expansion; no ADIF closure claim |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t5-execution-2026-06-23` |
| Expected manifest | this baseline; paired work order; integrity guard module; integrity guard test; ADIF front door update; roadmap row update |
| Actual changed set | recorded in the ADIF-T5 checkpoint commit |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Guard detects dangling `checkerBindings` paths. |
| AC2 | Guard detects dangling `supersedes` references. |
| AC3 | Guard detects duplicate `defectId` values. |
| AC4 | Guard detects stale supersession (e.g., an `ACTIVE` entry pointed to by `supersedes` from another `ACTIVE` entry, or a supersession cycle). |
| AC5 | Guard detects invalid `severity`/`lifecycleState`/`enforcementLevel` enum values. |
| AC6 | Guard detects dishonest enforcement claims (`MACHINE_CHECKED`/`PARTIAL_CHECK` with a non-existent `checkerBindings` path). |
| AC7 | Guard never mutates any entry file; it reports violations only. |
| AC8 | Guard is not wired into any autorun phase or hook chain in this tranche. |
| AC9 | Focused tests cover every violation class plus a clean-pass case, and all pass. |
| AC10 | Execution stops once after the T5 checkpoint commit; the complete T0-T5 graph is returned to Codex for final review. |

## Claim Boundary

This baseline authorizes only the ADIF-T5 standalone entry-integrity guard
tranche, the final step of the canonical continuous-execution chain. It
does not authorize any CLI/MCP adapter, runtime/provider/live behavior,
public-sync, autorun/hook-chain wiring, or final closure. Codex remains
the designated final reviewer/closer for the complete T0-T5 chain and
reviews the full graph once after this tranche returns.
