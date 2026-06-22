# CVF GC-018 - ADIF-T2 Task/Role/Phase Defect Packet Resolver

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: gc018_baseline

dispatchBaseHead: 479e98e3

executionBaseHead: 479e98e3

closureBaseHead: c08f810e

Commit mode: `WORKER_MAY_COMMIT`

Batch ID: ADIF-T2

## Purpose

Authorize the third child tranche of the ADIF continuous-execution chain.
ADIF-T2 creates a deterministic, read-only resolver that accepts task
class, role, lifecycle phase, surface selectors, and an optional risk
ceiling, then returns a bounded, ordered defect packet drawn from the eight
ADIF-T1 seed entries with source citations and enforcement labels.

This baseline is authorized under, and subordinate to, the canonical
continuous-execution packet, the ADIF-T0 contract, and the ADIF-T1
checkpoint review. It does not waive that packet's stop conditions or
Codex final-review requirement. No external CLI/MCP adapter is authorized
by this baseline.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| Master work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CONTINUOUS_EXECUTION_T0_T5_FOR_CLAUDE_2026-06-22.md` | ACCEPT |
| ADIF-T1 checkpoint commit | `2fcd2395` | ACCEPT |
| ADIF-T1 checkpoint review | `docs/reviews/CVF_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_CHECKPOINT_REVIEW_2026-06-23.md` | ACCEPT - `ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW`, releases T2 |
| ADIF-T0 owner-reconciliation contract | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | ACCEPT |
| ADIF entry template | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | ACCEPT |
| Eight ADIF-T1 seed entries | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |
| Dual Agent Surface Accounting Standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | ACCEPT - mandates the matrix at dispatch time |
| Post-T1 continuity sync commits | `d59c5205`; `755785ce`; `479e98e3` | ACCEPT - HEAD continuity restored before T2 dispatch |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF-T2 output and required properties: caller-supplied or repository-governed inputs only, deterministic ranking and max result count, no filesystem mutation, no provider/model selection, no prompt execution or agent-memory reinjection, no comprehension claim | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T2 - Task/Role/Phase Defect Packet Resolver | Required properties list | ADIF roadmap | VALUE_SET | ACCEPT |
| ADIF-T1 checkpoint review requires T2 to include the Dual Agent Surface Matrix at dispatch time and defers external CLI/MCP integration to a separate source-verified authorization | `docs/reviews/CVF_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_CHECKPOINT_REVIEW_2026-06-23.md` | Risk / Corrective Action; Dual Agent Surface Matrix | required control for T2 | ADIF-T1 checkpoint review | VALUE_SET | ACCEPT |
| Mandatory Dual Agent Surface Matrix requires INTERNAL_AGENT and EXTERNAL_AGENT_CLI_MCP rows, each with exactly one disposition from IMPLEMENTED/CONTRACT_ONLY/DEFERRED_WITH_REASON/N/A_WITH_REASON | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Mandatory Dual Agent Surface Matrix | matrix table | Dual Agent Surface Accounting Standard | VALUE_SET | ACCEPT |
| Eight stable seed entries with fixed field shape exist | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Required Fields | `defectId`; `defectCategory`; `taskClasses`; `roles`; `lifecyclePhases`; `surfaceSelectors`; `enforcementLevel`; `severity`; `lifecycleState` | ADIF entry template | VALUE_SET | ACCEPT |
| Each seed entry's exact field values | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | fenced field block in each file | per-entry field values | ADIF-T1 seed entries | EXISTS | ACCEPT |
| Only `ACTIVE` entries are resolver-eligible; all other lifecycle states remain readable but excluded | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | Entry Lifecycle | lifecycle eligibility rule | ADIF-T0 contract | LITERAL_INVARIANT | ACCEPT |
| Guard Orientation owns the task-class and role vocabulary the resolver's `taskClasses`/`roles` inputs must align with | `docs/reference/guard_orientation/README.md` | Task Class Guard Map; Role Glossary | task-class and role columns | guard orientation front door | VALUE_SET | ACCEPT |
| `governance/compat/` is the existing location for read-only diagnostic/helper modules with frozen-dataclass output items | `governance/compat/run_agent_automation_assist.py` | `SignalReadoutItem`; `_build_signal_readout` | frozen dataclass + builder pattern | AAF helper | EXISTS | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create `governance/compat/run_adif_defect_resolver.py` as a deterministic,
  read-only Python module that loads the eight committed seed entries,
  accepts `taskClass`, `role`, `lifecyclePhase`, `surfaceSelectors`, and
  optional `riskCeiling` parameters, and returns a bounded, ordered list of
  matching entries with source citations and enforcement labels;
- create `governance/compat/test_run_adif_defect_resolver.py` with focused
  tests covering matching, ordering, max-result bounding, lifecycle
  exclusion, and no-match cases;
- create `docs/reference/agent_defect_intelligence/CVF_ADIF_T2_RESOLVER_CONTRACT.md`
  documenting the resolver's input/output contract and the Dual Agent
  Surface Matrix;
- update `docs/reference/agent_defect_intelligence/README.md` to point to
  the resolver contract;
- update `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  ADIF-T2 row only;
- create local checkpoint commit for this tranche only.

Forbidden scope:

- no CLI entry point, MCP tool registration, or external adapter wiring;
- no filesystem mutation by the resolver itself (it may only read the
  committed entry files under `docs/reference/agent_defect_intelligence/entries/`);
- no provider/model selection or prompt execution;
- no agent-memory reinjection;
- no claim that returning a packet proves it was read or understood;
- no autorun/hook wiring (reserved for ADIF-T3);
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no runtime, provider/live, public-sync, or session-continuity edit;
- no claim of ADIF-T3 through T5 progress.

Risk ceiling: R1 - first ADIF tranche with executable code, but read-only,
no filesystem mutation, no external surface, and fully covered by focused
tests.

## Required Deliverables

- `governance/compat/run_adif_defect_resolver.py`
- `governance/compat/test_run_adif_defect_resolver.py`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_T2_RESOLVER_CONTRACT.md`
- `docs/reference/agent_defect_intelligence/README.md` (front-door pointer
  update)
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  (ADIF-T2 row update only)
- this GC-018 baseline
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T2_TASK_ROLE_PHASE_DEFECT_PACKET_RESOLVER_2026-06-23.md`

## Decision / Baseline / Proposed Tranche

Decision: authorize ADIF-T2 for continuous execution under the canonical
ADIF authorization, released by the ADIF-T1 checkpoint review. Baseline:
dispatch/execution base `479e98e3`. Proposed tranche: ADIF-T2 Task/Role/
Phase Defect Packet Resolver, executed and committed by Claude under
`WORKER_MAY_COMMIT`, then stopped for Codex GC-020 session-sync and
checkpoint review before any further tranche.

## Dependency Release Evidence

| Prerequisite artifact | Closure or dispatch commit | Disposition | Gate evidence |
|---|---|---|---|
| ADIF-T1 checkpoint commit | `2fcd2395` | ACCEPT | committed |
| ADIF-T1 checkpoint review | `755785ce` | ACCEPT | `ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW`; reviewer-fast 34/34 PASS after continuity sync `d59c5205` |
| Continuity sync restoring active-handoff HEAD alignment | `d59c5205`; `755785ce`; `479e98e3` | ACCEPT | pre-implementation autorun 47/47 PASS at range `479e98e3..HEAD` before this packet |

## Mandatory Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | direct Python import / function call of `governance/compat/run_adif_defect_resolver.py` inside CVF-governed workspace | read-only function call; no filesystem mutation; no commit/action authority; returns a bounded list, does not execute or apply remediation | this baseline, paired work order, and focused tests in `test_run_adif_defect_resolver.py` | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future separately authorized CLI/MCP adapter, not created in this tranche | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, or public claim exists or is authorized by ADIF-T2 | ADIF-T1 checkpoint review's deferred disposition; this baseline's Forbidden Scope | `DEFERRED_WITH_REASON` - no adapter exists; a future CLI/MCP surface requires its own source-verified GC-018/work order per the Dual Agent Surface Accounting Standard |

## Evidence / Verification

Pre-dispatch verification for this child packet:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 479e98e3 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 479e98e3 --head HEAD --enforce
```

Focused test verification after implementation:

```powershell
python -m pytest governance/compat/test_run_adif_defect_resolver.py -v
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-selected continuous sequence absorbed into ADIF roadmap; ADIF-T2 ADAPTs the roadmap's resolver spec into a deterministic, read-only, internal-only implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T2 resolver |
| Disposition | ADAPT as bounded CVF-owned internal resolver; no external surface authorized |
| Claim boundary | roadmap spec and T1 checkpoint review are design input only; this baseline and the canonical authorization are the CVF-governed dispatch authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: ADIF-T2 authorizes a read-only local Python helper only; no runtime route, provider gateway, or model registry behavior is changed |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed by ADIF-T2 |
| Runtime behavior claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no provider, public-sync, or external-adapter behavior is claimed by this dispatch; the resolver itself is a local read-only function |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T2 deterministic read-only resolver implementation only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: resolver returns data only; it does not perform or record an action |
| invocationBoundary | local repository function call, governed by direct Python import |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | read-only task/role/phase defect packet resolver only |
| forbiddenExpansion | CLI/MCP adapter, filesystem mutation, autorun/hook wiring, runtime/provider/live, public-sync, and universal control remain out of scope for ADIF-T2 |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without a deterministic resolver, agents must manually cross-reference all eight entries against task/role/phase | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T2 implements the bounded resolver | handled by this tranche |
| New agent-facing foundations must declare the Dual Agent Surface Matrix at dispatch time (ADIF-T1 finding) | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | this baseline includes the matrix at dispatch time, not as a post-hoc reviewer repair | handled by this tranche |
| Runtime/provider/cost applicability for ADIF-T2 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T2` tranche definition.
- Predecessor intake artifact: ADIF-T1 checkpoint review and its Dual Agent
  Surface Matrix finding.
- Delta ledger status: `CHANGED_DISPOSITION` - T2 now includes the Dual
  Agent Surface Matrix at dispatch time rather than as a post-hoc repair.
- Routing matrix status: `DO_NOW` for the read-only resolver, its tests, and
  contract document; `OUT_OF_SCOPE` for any CLI/MCP adapter.
- Semantic sampling status: sampled the ADIF-T0 contract, all eight ADIF-T1
  entries, the ADIF-T1 checkpoint review, and the Dual Agent Surface
  Accounting Standard directly before authoring.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T2 scope matches the roadmap tranche definition exactly. |
| CHANGED_DISPOSITION | Dual Agent Surface Matrix now included at dispatch time per the ADIF-T1 reviewer finding. |
| NEW_FINDING | None beyond the dual-agent matrix finding, already handled. |
| REMOVED_OR_REJECTED | CLI/MCP adapter, autorun/hook wiring, and T3-T5 scope remain rejected for ADIF-T2. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T2 read-only resolver, focused tests, and resolver contract document. |
| RESOLVED_BY_DESIGN | ADIF-T0's canonical-reuse field boundary and ADIF-T1's fixed entry shape govern every resolver input/output field. |
| DEFER | ADIF-T3 early preflight integration, ADIF-T4 intake bridge, ADIF-T5 integrity guard. |
| SEPARATE_RUNTIME_TRANCHE | any future CLI/MCP adapter for the resolver. |
| STRATEGIC_OPERATOR_DECISION | whether and when a CLI/MCP adapter is ever authorized remains open for a later, separately source-verified tranche. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity, autorun/hook wiring. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T2-RS1 | ADIF roadmap Required properties | no filesystem mutation; no provider/model selection; no prompt execution or agent-memory reinjection | DO_NOW | Does the resolver implementation write any file, call any provider, or execute a prompt? | PASS - implementation is verified read-only with no provider/prompt surface before commit |
| ADIF-T2-RS2 | ADIF-T0 contract Entry Lifecycle | only `ACTIVE` entries are eligible without making other states unreadable | DO_NOW | Does the resolver include proposed/rejected/retired/superseded entries or delete their files? | PASS_AFTER_REVIEWER_REPAIR - eligibility now requires `ACTIVE`; files remain unchanged |
| ADIF-T2-RS3 | Dual Agent Surface Accounting Standard Core Rule | silence is not a valid disposition; each consumer row needs exactly one disposition | DO_NOW | Does this baseline declare a disposition for both `INTERNAL_AGENT` and `EXTERNAL_AGENT_CLI_MCP`? | PASS - matrix above declares `IMPLEMENTED` and `DEFERRED_WITH_REASON` respectively |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded
  governance-implementation tranche.
- Corpus root: repo-local source files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-23 ADIF-T2 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=9; ledger_terminal=9 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no historical finding corpus scan, no CLI/MCP adapter
  source, no public repository scan, no provider-local memory intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no generated aggregate created; the
  resolver reads compact per-entry source files directly.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: resolver input fields map to canonical entry-template
  fields; resolver output fields map to canonical-reuse and ADIF-owned
  field tables.
- Adversarial verification: checked for filesystem-mutation risk,
  provider/prompt surface risk, and lifecycle-exclusion correctness before
  implementation.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| ADIF governed artifact | committed implementation and final-review acceptance | PASS |
| GC-051 corpus registration | generated JSON aggregate and retained human companion | PASS |
| Runtime/provider receipt | N/A with reason: no runtime/provider/live claim | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T2 is private provenance governance-implementation work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T2 child dispatch and execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, pytest, governance gates, git commit |
| Target paths | this baseline; paired work order; resolver module; resolver tests; resolver contract document; ADIF front door update; roadmap row update |
| Allowed scope source | canonical continuous-execution authorization, master work order, and ADIF-T1 checkpoint review |
| Before status evidence | executionBaseHead `479e98e3`; clean worktree confirmed; pre-implementation autorun 47/47 PASS |
| After status evidence | ADIF-T2 child packet and deliverables committed as one checkpoint; execution stops for Codex review |
| Diff evidence | child-batch name-status and committed diff |
| Approval boundary | ADIF-T2 child scope only; no T3-T5 implementation in this batch |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider/external-adapter expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t2-execution-2026-06-23` |
| Expected manifest | this baseline; paired work order; resolver module; resolver tests; resolver contract document; ADIF front door update; roadmap row update |
| Actual changed set | recorded in the ADIF-T2 checkpoint commit |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Resolver accepts task class, role, lifecycle phase, surface selectors, and an optional risk ceiling. |
| AC2 | Resolver returns a bounded, deterministically ordered list with source citations and enforcement labels. |
| AC3 | Resolver never mutates the filesystem, never calls a provider/model, never executes a prompt. |
| AC4 | Resolver returns only `ACTIVE` entries without deleting or hiding other lifecycle-state source files. |
| AC5 | Resolver's docstring/contract explicitly disclaims that returning a packet proves comprehension. |
| AC6 | Focused tests cover matching, ordering, bounding, lifecycle exclusion, and no-match cases, and all pass. |
| AC7 | Dual Agent Surface Matrix is present at dispatch time with both rows populated. |
| AC8 | No CLI entry point, MCP registration, or autorun/hook wiring is created. |
| AC9 | Execution stops after the T2 checkpoint commit; no T3 work begins in this batch. |

## Claim Boundary

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T2 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | final ADIF completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | ADIF roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ADIF-T0-T5 entry generated from registry source | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | human companion retained; no quick-lookup delta required | PASS |
| External evidence digest | N/A | no external evidence intake | N/A with reason |
| Session continuity | active session surfaces | separate post-closure sync follows | N/A with reason |
| System loop interlock | N/A | no runtime loop changed | N/A with reason |

## Claim Boundary

This baseline authorizes only the ADIF-T2 read-only resolver tranche inside
the canonical continuous-execution chain. It does not authorize ADIF-T3
through T5 implementation, any CLI/MCP adapter, runtime/provider/live
behavior, public-sync, or final closure. Codex remains the designated final
reviewer/closer for the complete T0-T5 chain and must session-sync and
checkpoint-review this tranche before any further release.
