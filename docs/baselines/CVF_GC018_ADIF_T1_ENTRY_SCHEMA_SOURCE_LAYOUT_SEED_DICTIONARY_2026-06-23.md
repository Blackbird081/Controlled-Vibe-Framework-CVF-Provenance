# CVF GC-018 - ADIF-T1 Entry Schema, Source Layout, And Seed Dictionary

Memory class: FULL_RECORD

Status: CHECKPOINT_ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW

Date: 2026-06-23

docType: gc018_baseline

dispatchBaseHead: 0fde5cf2

executionBaseHead: 0fde5cf2

closureBaseHead: NOT_EXECUTED_YET

Commit mode: `WORKER_MAY_COMMIT`

Batch ID: ADIF-T1

## Purpose

Authorize the second child tranche of the ADIF continuous-execution chain.
ADIF-T1 creates the entry schema, a compact per-entry source layout, and
8-15 source-verified seed entries drawn from the roadmap's Seed Defect
Candidates table, applying the ownership and taxonomy rules ADIF-T0 froze.

This baseline is authorized under, and subordinate to, the canonical
continuous-execution packet and the ADIF-T0 checkpoint review. It does not
waive that packet's stop conditions or Codex final-review requirement.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| Master work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CONTINUOUS_EXECUTION_T0_T5_FOR_CLAUDE_2026-06-22.md` | ACCEPT |
| ADIF-T0 checkpoint commit | `7c0480bc` | ACCEPT |
| ADIF-T0 checkpoint review | `docs/reviews/CVF_ADIF_T0_OWNER_RECONCILIATION_CHECKPOINT_REVIEW_2026-06-23.md` | ACCEPT - `ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW`, releases T1 |
| ADIF-T0 owner-reconciliation contract | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |
| Post-T0 continuity sync commits | `e454191f`; `6277cb28`; `5678ebcc`; `6abda284`; `0fde5cf2` | ACCEPT - HEAD continuity restored before T1 dispatch |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF-T0 checkpoint review requires T1 to mark new vocabulary as not-yet-implemented until built, cite the checkpoint and `7c0480bc`, and run pre-dispatch/pre-implementation from the post-sync HEAD | `docs/reviews/CVF_ADIF_T0_OWNER_RECONCILIATION_CHECKPOINT_REVIEW_2026-06-23.md` | Risk / Corrective Action | required control for T1 | ADIF-T0 checkpoint review | VALUE_SET | ACCEPT |
| ADIF-T1 may output a stable front door, entry template, compact per-entry source layout, and 8-15 source-verified seed entries; no bulk historical import | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T1 - Entry Schema, Source Layout, And Seed Dictionary | Outputs may include list | ADIF roadmap | VALUE_SET | ACCEPT |
| Eight roadmap seed candidates with category, pattern, and current-evidence columns | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Seed Defect Candidates | `ADIF-SEED-001` through `ADIF-SEED-008` | ADIF roadmap | VALUE_SET | ACCEPT |
| Seed IDs are roadmap placeholders; ADIF-T1 owns final stable IDs and must deduplicate against canonical entries | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Seed Defect Candidates | final stable ID ownership | ADIF roadmap | LITERAL_INVARIANT | ACCEPT |
| Canonical-reuse vs ADIF-owned field table; defectClass/defectRole/frictionLevel/frictionType/observedStep/preventiveControlCandidate/taskClasses are canonical reuse, not ADIF-defined enums | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | Canonical-Reuse Fields Versus ADIF-Owned Lookup Metadata | field ownership table | ADIF-T0 contract | VALUE_SET | ACCEPT |
| Four enforcementLevel values GUIDANCE_ONLY/PARTIAL_CHECK/MACHINE_CHECKED/RETIRED with the rule that MACHINE_CHECKED requires a verifiable checkerBindings citation | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | Guidance Versus Enforcement Distinction | enforcementLevel table | ADIF-T0 contract | VALUE_SET | ACCEPT |
| Five entry lifecycle states PROPOSED/ACTIVE/SUPERSEDED/RETIRED/REJECTED | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | Entry Lifecycle | lifecycle state table | ADIF-T0 contract | VALUE_SET | ACCEPT |
| defectCategory is orthogonal to defectClass; many-to-many relationship; never collapse one into the other | `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md` | `defectCategory` Is Orthogonal To `defectClass` | orthogonality rule | ADIF-T0 contract | LITERAL_INVARIANT | ACCEPT |
| ADIF-SEED-001 through 005 evidence exists in the MPI-T6 hardening completion review (exhaustive-claim, provider-local-authority, machine-closure, decided-roadmap-residue, closure-residue defects, focused tests) | `docs/reviews/CVF_MPI_T6_REVIEW_GATE_HARDENING_COMPLETION_2026-06-22.md` | Findings / Position; Closure Diff Gate; Gate Evidence | observed defect classes and focused-test evidence | MPI-T6 hardening completion review | EXISTS | ACCEPT |
| ADIF-SEED-006 evidence: work-order source-verification symbol-cell guard exists | `governance/compat/check_work_order_dispatch_quality.py` | `Verified path or symbol` field handling | symbol-cell value/type-annotation rejection | work-order dispatch quality checker | EXISTS | ACCEPT |
| ADIF-SEED-007 evidence: Boundary-Prose Trigger Discipline keyword-trap map | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | Boundary-Prose Trigger Discipline | known keyword trigger classes table | FPRC canonical standard | VALUE_SET | ACCEPT |
| ADIF-SEED-008 evidence: Provider Memory Learning Escape Guard | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | Provider Memory Learning Escape Guard | guard requirement and detection-signal list | FPRC canonical standard | VALUE_SET | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
  as the machine-readable per-entry template;
- create `docs/reference/agent_defect_intelligence/entries/` as the compact
  per-entry source directory;
- create 8 seed entry files under that directory, one per roadmap seed
  candidate, each citing its canonical evidence and declaring an
  `enforcementLevel`;
- update `docs/reference/agent_defect_intelligence/README.md` to point to the
  entry template and entries directory;
- update `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  ADIF-T1 row only;
- assign final stable `defectId` values distinct from the roadmap's
  placeholder `ADIF-SEED-NNN` IDs, recording the placeholder as a
  cross-reference inside each entry;
- create local checkpoint commit for this tranche only.

Forbidden scope:

- no resolver, helper, checker, generator, or hook wiring (reserved for
  ADIF-T2 and later);
- no generated aggregate or human-reviewable dictionary view (the roadmap
  permits this only if ADIF-T0 requires it; ADIF-T0 did not require it - see
  `## What ADIF-T0 Does Not Decide`, which leaves the aggregate question open
  to ADIF-T1 but does not mandate one; this tranche elects compact per-entry
  sources only, no aggregate);
- no bulk historical import beyond the eight named roadmap seed candidates;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no claim that any seed entry is `MACHINE_CHECKED` unless its
  `checkerBindings` citation is independently verified to exist;
- no runtime, provider/live, public-sync, or session-continuity edit;
- no claim of agent comprehension or defect-prevention effectiveness.

Risk ceiling: R0/R1 documentation/reference only.

## Required Deliverables

- `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through
  `CVF_ADIF-0008.md` (final stable IDs; exact filenames decided at execution)
- `docs/reference/agent_defect_intelligence/README.md` (front-door pointer
  update)
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  (ADIF-T1 row update only)
- this GC-018 baseline
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_2026-06-23.md`

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | direct governed reads of `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` and compact entries | read-only lookup guidance; no proof of reading, comprehension, or prevention | T1 template and eight committed entries | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future ADIF resolver/CLI/MCP adapter owner, not created by T1 | no ingress, authentication, approval, receipt, raw-data release, mutation, runtime, or public claim is authorized | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`; T1 forbidden scope | `DEFERRED_WITH_REASON` - ADIF-T2 may build only a local read-only resolver; any CLI/MCP adapter requires a separate source-verified packet |

## Decision / Baseline / Proposed Tranche

Decision: authorize ADIF-T1 for continuous execution under the canonical
ADIF authorization, released by the ADIF-T0 checkpoint review. Baseline:
dispatch/execution base `0fde5cf2`. Proposed tranche: ADIF-T1 Entry Schema,
Source Layout, And Seed Dictionary, executed and committed by Claude under
`WORKER_MAY_COMMIT`, then stopped for Codex GC-020 session-sync and
checkpoint review before any further tranche.

## Dependency Release Evidence

| Prerequisite artifact | Closure or dispatch commit | Disposition | Gate evidence |
|---|---|---|---|
| ADIF-T0 checkpoint commit | `7c0480bc` | ACCEPT | committed |
| ADIF-T0 checkpoint review | `6277cb28` | ACCEPT | `ACCEPTED_FOR_CONTINUATION_PENDING_FINAL_REVIEW`; reviewer-fast 34/34 PASS after continuity sync |
| Continuity sync restoring active-handoff HEAD alignment | `e454191f`; `5678ebcc`; `6abda284`; `0fde5cf2` | ACCEPT | `check_active_session_state.py` and pre-implementation autorun 47/47 PASS at range `0fde5cf2..HEAD` before this packet |

## Evidence / Verification

Pre-dispatch verification for this child packet:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0fde5cf2 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 0fde5cf2 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-selected continuous sequence absorbed into ADIF roadmap; ADIF-T1 ADAPTs the roadmap's proposed seed candidates into stable, source-verified entries |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T1 entry schema and seed dictionary |
| Disposition | ADAPT as bounded CVF-owned entry set; canonical F2G/FPRC/INDEX owners preserved |
| Claim boundary | roadmap seed candidates are design input only; this baseline and the canonical authorization are the CVF-governed dispatch authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: ADIF-T1 authorizes documentation/reference work only; no runtime route, provider gateway, or model registry behavior is changed |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed by ADIF-T1 |
| Runtime behavior claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no runtime, provider, helper/checker, or public-sync behavior is claimed by this dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T1 entry-schema and seed-dictionary authoring only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed documentation/reference classification only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | entry schema, source layout, and seed dictionary only |
| forbiddenExpansion | resolver/generator/checker/hook implementation, runtime/provider/live, public-sync, and universal control remain out of scope for ADIF-T1 |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without a fixed entry template, future ADIF entries could each invent their own field shape | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T1 fixes one entry template and a compact source layout before any resolver is built | handled by this tranche |
| Continuous-chain choreography between worker checkpoint commits and reviewer-owned session continuity (flagged in the ADIF-T0 checkpoint review) | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | this baseline stops after the T1 checkpoint commit and explicitly waits for Codex GC-020 sync before any further tranche | handled by this tranche's execution discipline |
| Runtime/provider/cost applicability for ADIF-T1 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T1` tranche definition and
  Seed Defect Candidates table.
- Predecessor intake artifact: ADIF-T0 checkpoint review and contract.
- Delta ledger status: `UNCHANGED_FROM_INTAKE` - ADIF-T1 executes exactly the
  roadmap-defined tranche with no scope change.
- Routing matrix status: `DO_NOW` for entry template, source layout, and
  eight seed entries; `DEFER` for resolver/preflight/intake/guard work
  (ADIF-T2 through T5).
- Semantic sampling status: sampled the ADIF-T0 contract, the roadmap's
  Seed Defect Candidates table, and the MPI-T6 hardening completion review
  directly before authoring.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T1 scope matches the roadmap tranche definition exactly. |
| CHANGED_DISPOSITION | None for this tranche. |
| NEW_FINDING | None beyond the ADIF-T0 checkpoint review's choreography finding, already handled by this tranche's stop-after-commit discipline. |
| REMOVED_OR_REJECTED | Resolver/helper/checker/generator/hook/aggregate scope remains rejected for ADIF-T1. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T1 entry template, source layout, and eight seed entries. |
| RESOLVED_BY_DESIGN | ADIF-T0's canonical-reuse vs ADIF-owned field boundary governs every seed entry's field list; no new ownership decision is needed here. |
| DEFER | ADIF-T2 resolver. |
| SEPARATE_RUNTIME_TRANCHE | ADIF-T3 preflight integration, ADIF-T4 intake bridge, ADIF-T5 integrity guard. |
| STRATEGIC_OPERATOR_DECISION | whether a generated aggregate/dictionary view is ever built remains open for a later tranche to decide, not this one. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity, historical migration beyond the eight named seeds. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T1-RS1 | ADIF-T0 contract Guidance Versus Enforcement Distinction | `MACHINE_CHECKED` requires a verifiable `checkerBindings` citation | DO_NOW | Does any seed entry claim `MACHINE_CHECKED` without confirming the cited checker file exists? | PASS - all `MACHINE_CHECKED` candidates verified against an existing `governance/compat/*.py` path before assignment |
| ADIF-T1-RS2 | ADIF-T0 contract `defectCategory` Is Orthogonal To `defectClass` | the two axes must never collapse into one | DO_NOW | Does any seed entry use `defectCategory` as a synonym for `defectClass`? | PASS - each entry records both fields separately, citing F2G for `defectClass` |
| ADIF-T1-RS3 | Roadmap Seed Defect Candidates | seed IDs are placeholders; ADIF-T1 owns final stable IDs | DO_NOW | Does this tranche keep the roadmap's `ADIF-SEED-NNN` IDs as the final IDs? | PASS - final `defectId` values are assigned separately, with the roadmap placeholder recorded as a cross-reference |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded
  governance-reference tranche.
- Corpus root: repo-local source files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-23 ADIF-T1 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=14; ledger_terminal=14 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no historical finding corpus scan beyond the eight
  named roadmap seeds, no schema/resolver/runtime source mutation, no public
  repository scan, no provider-local memory intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: each seed entry maps to a named canonical evidence
  source row above.
- Adversarial verification: checked for fake `MACHINE_CHECKED` claims and
  `defectCategory`/`defectClass` collisions before assignment.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T1 is private provenance governance-reference work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T1 child dispatch and execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, governance gates, git commit |
| Target paths | this baseline; paired work order; ADIF entry template; eight seed entry files; ADIF front door; roadmap row update |
| Allowed scope source | canonical continuous-execution authorization, master work order, and ADIF-T0 checkpoint review |
| Before status evidence | executionBaseHead `0fde5cf2`; clean worktree confirmed; pre-implementation autorun 47/47 PASS |
| After status evidence | ADIF-T1 child packet and deliverables committed as one checkpoint; execution stops for Codex review |
| Diff evidence | child-batch name-status and committed diff |
| Approval boundary | ADIF-T1 child scope only; no T2-T5 implementation in this batch |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t1-execution-2026-06-23` |
| Expected manifest | this baseline; paired work order; ADIF entry template; eight seed entry files; ADIF front door update; roadmap row update |
| Actual changed set | recorded in the ADIF-T1 checkpoint commit |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Entry template includes every field from the ADIF-T0 contract's canonical-reuse and ADIF-owned tables. |
| AC2 | Each of the eight seed entries cites canonical evidence and declares exactly one `enforcementLevel`. |
| AC3 | No seed entry claims `MACHINE_CHECKED` without an independently verified `checkerBindings` path. |
| AC4 | No seed entry conflates `defectCategory` with `defectClass`. |
| AC5 | Final stable `defectId` values are distinct from roadmap placeholder IDs, with a cross-reference retained. |
| AC6 | No resolver/helper/checker/generator/hook file is created. |
| AC7 | Execution stops after the T1 checkpoint commit; no T2 work begins in this batch. |

## Claim Boundary

This baseline authorizes only the ADIF-T1 entry-schema, source-layout, and
seed-dictionary tranche inside the canonical continuous-execution chain. It
does not authorize ADIF-T2 through T5 implementation, resolver/checker/helper
code, runtime/provider/live behavior, public-sync, or final closure. Codex
remains the designated final reviewer/closer for the complete T0-T5 chain
and must session-sync and checkpoint-review this tranche before any further
release.
