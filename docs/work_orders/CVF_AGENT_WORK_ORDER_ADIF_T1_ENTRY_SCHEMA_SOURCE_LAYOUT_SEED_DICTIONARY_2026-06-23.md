# CVF Agent Work Order - ADIF-T1 Entry Schema, Source Layout, And Seed Dictionary

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-06-23

docType: work_order

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: 0fde5cf2

executionBaseHead: 0fde5cf2

closureBaseHead: NOT_EXECUTED_YET

## Dispatch Prompt Envelope

Role: Claude continuous-execution orchestrator/worker, executing the second
child tranche of the ADIF chain. Codex is the designated final reviewer/
closer for the whole T0-T5 chain, not per-tranche, and additionally
performs a GC-020 session-sync and checkpoint review after each tranche per
the ADIF-T0 checkpoint review's choreography finding.

Canonical packet:
`docs/baselines/CVF_GC018_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_2026-06-23.md`

Commit mode: `WORKER_MAY_COMMIT`

executionBaseHead: `0fde5cf2` (confirmed via `git rev-parse --short HEAD`
before any edit in this batch).

Current-time notes: this is the second of six tranches in the ADIF
continuous chain. ADIF-T1 is documentation/reference only - no resolver,
helper, checker, generator, or hook wiring.

Do-not-misread notes: the eight seed entries cite canonical evidence
directly verified to exist; no entry claims `MACHINE_CHECKED` without a
confirmed `governance/compat/*.py` path. Final stable `defectId` values
(`ADIF-0001` through `ADIF-0008`) are distinct from the roadmap's
placeholder `ADIF-SEED-NNN` IDs, with each entry recording the placeholder
as a cross-reference.

Required first actions: read the canonical authorization, the master work
order, the ADIF roadmap, the ADIF-T0 contract, and the ADIF-T0 checkpoint
review before authoring the schema and seed entries.

Return contract: this packet is returned `COMPLETE_PENDING_REVIEW`; per the
operator's instruction, Claude stops here after committing the T1
checkpoint and returns it to Codex for GC-020 session-sync and checkpoint
review before any further tranche.

## Mission

Create the ADIF entry template, a compact per-entry source layout under
`docs/reference/agent_defect_intelligence/entries/`, and eight
source-verified seed entries drawn from the roadmap's Seed Defect
Candidates table, applying the ownership and taxonomy rules ADIF-T0 froze.

## Purpose

Translate the canonical continuous-execution authorization's second sequence
step into a source-verified, bounded ADIF-T1 execution that fixes one entry
shape before any resolver (ADIF-T2) is built.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority; pre-selected the T0-T5 continuous sequence; instructed this turn to stop after the T1 checkpoint |
| Dispatcher | Codex authored the canonical packet; Claude authors this child packet |
| Orchestrator/worker | Claude |
| Reviewer/closer | Codex, after this checkpoint and again after the complete T0-T5 chain returns |
| Session-sync steward | Codex following accepted checkpoint review |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Claude orchestrates and executes ADIF-T1 under `WORKER_MAY_COMMIT`; Codex reviews and checkpoints this tranche, then later closes the complete T0-T5 chain |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=0fde5cf2`; `executionBaseHead=0fde5cf2`; `closureBaseHead` captured by Codex at checkpoint review |
| changedSetScope(phase) | dispatch/execution = this work order, ADIF-T1 baseline, ADIF entry template, eight seed entries, ADIF front door update, roadmap row update; closure = Codex-owned checkpoint review and continuity sync |
| traceScope(phase, actor) | one trace covers this ADIF-T1 child dispatch and execution; one Codex trace covers the checkpoint review and session sync |
| commitOwner(phase) | Claude commits this ADIF-T1 checkpoint under `WORKER_MAY_COMMIT`; Codex owns checkpoint-review and session-sync commits |
| crossBatchIsolation | ADIF-T1 is isolated from ADIF-T2 through T5, which require their own fresh child packets after a fresh release |
| nextMoveSurfaces | Claude does not edit session state/front door/handoff; Codex updates them after this checkpoint review |
| Closer designation | Codex |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| ADIF-T1 GC-018 baseline | `docs/baselines/CVF_GC018_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_2026-06-23.md` | ACCEPT |
| ADIF-T0 checkpoint review | `docs/reviews/CVF_ADIF_T0_OWNER_RECONCILIATION_CHECKPOINT_REVIEW_2026-06-23.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |

## Required First Reads

- `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md`
- `docs/baselines/CVF_GC018_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_2026-06-23.md`
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md`
- `docs/reviews/CVF_ADIF_T0_OWNER_RECONCILIATION_CHECKPOINT_REVIEW_2026-06-23.md`
- `docs/reviews/CVF_MPI_T6_REVIEW_GATE_HARDENING_COMPLETION_2026-06-22.md`
- `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0fde5cf2 --head HEAD
```

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Claude (this tranche) | create |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | Claude (this tranche) | create |
| `docs/reference/agent_defect_intelligence/README.md` | Claude (this tranche) | update front-door pointers only |
| `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Claude (this tranche) | update ADIF-T1 row only |
| this work order; ADIF-T1 GC-018 baseline | Claude (this tranche) | create, commit |

## Forbidden Scope

- no resolver, helper, checker, generator, or hook wiring;
- no generated aggregate or human-reviewable dictionary view;
- no bulk historical import beyond the eight named roadmap seed candidates;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no claim that any seed entry is `MACHINE_CHECKED` unless its
  `checkerBindings` citation is independently verified to exist;
- no runtime, provider/live, public-sync, or session-continuity edit;
- no claim of agent comprehension or defect-prevention effectiveness;
- no claim of ADIF-T2 through T5 progress;
- no continuation into ADIF-T2 in this batch; stop after the T1 checkpoint
  commit per this turn's instruction.

## Execution Plan

1. Confirm `executionBaseHead` and clean worktree.
2. Read all Required First Reads.
3. Verify each cited checker path exists before assigning `MACHINE_CHECKED`.
4. Create the ADIF entry template.
5. Create the eight seed entry files.
6. Update the ADIF front door and the roadmap's ADIF-T1 row.
7. Run focused gates; commit the ADIF-T1 checkpoint; stop for Codex review.

## Evidence Requirements

- actual `executionBaseHead` and `git status --short`;
- pre-implementation autorun result over the real range;
- explicit statement that no resolver/helper/checker/generator/hook file was
  created;
- explicit confirmation that every `MACHINE_CHECKED` entry's
  `checkerBindings` path was verified to exist;
- exact claim boundary and public export disposition.

## Source Verification Block

The fourteen `ACCEPT` rows in the ADIF-T1 GC-018 baseline are incorporated
here by exact path and section.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ADIF-T1 tranche boundary and allowed outputs | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T1 - Entry Schema, Source Layout, And Seed Dictionary | Outputs may include list | ADIF roadmap | VALUE_SET | ACCEPT |
| ADIF-T0 checkpoint review releases T1 with required controls | `docs/reviews/CVF_ADIF_T0_OWNER_RECONCILIATION_CHECKPOINT_REVIEW_2026-06-23.md` | Risk / Corrective Action | required control for T1 | ADIF-T0 checkpoint review | VALUE_SET | ACCEPT |
| Eight seed candidates with canonical evidence sources | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Seed Defect Candidates | `ADIF-SEED-001` through `ADIF-SEED-008` | ADIF roadmap | VALUE_SET | ACCEPT |
| ADIF-0001/0003/0004/0005 checker bindings exist | `governance/compat/check_closure_packaging_preflight.py` | `_validate_exhaustive_directory_claims`; `_validate_decided_roadmap_residue` | named functions | closure packaging preflight checker | EXISTS | ACCEPT |
| ADIF-0003 checker binding exists | `governance/compat/check_machine_closure_package.py` | module-level checker | Machine Closure Package validation | machine closure package checker | EXISTS | ACCEPT |
| ADIF-0006 checker bindings exist | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` | `Verified path or symbol` cell handling | symbol-cell value/type rejection | work-order dispatch quality and packet authority checkers | EXISTS | ACCEPT |
| ADIF-0007 checker bindings exist | `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_finding_to_governance_learning.py` | module-level checkers | keyword-trigger-adjacent validation | corpus scan registry and F2G learning checkers | EXISTS | ACCEPT |
| ADIF-0008 checker binding exists | `governance/compat/check_finding_to_governance_learning.py` | Provider-memory learning boundary enforcement | provider-memory-only escape detection | F2G learning checker | EXISTS | ACCEPT |

## Worker Autonomy / No-Question Rule

Claude repairs and reruns all allowed-scope gate failures on its own
initiative. Claude stops only for the canonical packet's Stop Conditions, or
at the end of this tranche per this turn's explicit instruction to halt
before T2.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | new `docs/reference/agent_defect_intelligence/entries/` compact source directory plus one entry template file |
| Storage decision | one entry per file, no generated aggregate, no hand-edited large JSON |
| Existing aggregate impact | none |
| Generated state impact | none during this tranche |
| Durable governance boundary | documentation/reference only; no runtime memory store |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | roadmap seed candidates ADAPTed into stable, source-verified entries |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T1 entry schema and seed dictionary |
| Disposition | ADAPT as bounded CVF-owned entry set |
| Claim boundary | roadmap seed candidates are design input only |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T1` tranche definition and
  Seed Defect Candidates table.
- Predecessor intake artifact: ADIF-T0 checkpoint review and contract.
- Delta ledger status: `UNCHANGED_FROM_INTAKE`.
- Routing matrix status: `DO_NOW` for entry template and eight seed entries;
  `DEFER` for ADIF-T2 resolver.
- Semantic sampling status: sampled the ADIF-T0 contract, the ADIF-T0
  checkpoint review, the roadmap's Seed Defect Candidates table, and the
  MPI-T6 hardening completion review.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T1 scope matches the roadmap tranche definition exactly. |
| CHANGED_DISPOSITION | None for this tranche. |
| NEW_FINDING | None beyond the ADIF-T0 checkpoint review's choreography finding, already handled by stopping after this checkpoint. |
| REMOVED_OR_REJECTED | Resolver/helper/checker/generator/hook/aggregate scope remains rejected for ADIF-T1. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T1 entry template, source layout, eight seed entries. |
| RESOLVED_BY_DESIGN | ADIF-T0's canonical-reuse vs ADIF-owned boundary governs every seed entry field list. |
| DEFER | ADIF-T2 resolver, ADIF-T3/T4 fork, ADIF-T5 guard. |
| SEPARATE_RUNTIME_TRANCHE | any future generated aggregate/dictionary view. |
| STRATEGIC_OPERATOR_DECISION | whether to continue to T2 in a future turn; this turn halts at T1. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity, historical migration beyond the eight named seeds. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T1-WO-RS1 | ADIF-T0 contract Guidance Versus Enforcement Distinction | `MACHINE_CHECKED` requires a verifiable `checkerBindings` citation | DO_NOW | Were all cited checker paths confirmed to exist on disk before assignment? | PASS - confirmed via direct file existence checks before each entry was written |
| ADIF-T1-WO-RS2 | Roadmap Seed Defect Candidates | seed IDs are placeholders; ADIF-T1 owns final stable IDs | DO_NOW | Do the final entries retain a cross-reference to the original roadmap seed ID? | PASS - each entry's `roadmapSeedId` field cites the originating `ADIF-SEED-NNN` |

## Corpus Completeness And Report Integrity

- Corpus task class: work-order dispatch source verification for a bounded
  governance-reference tranche.
- Corpus root: repo-local source files named in Required First Reads and
  Source Verification Block.
- Snapshot time: 2026-06-23 ADIF-T1 execution.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Required First Reads and Source
  Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch.
- Processing ledger artifact or inline ledger: Source Verification Block
  rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=9; ledger_terminal=9 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no `.private_reference/legacy` scan, no runtime/web/
  MCP scan, no public-sync corpus scan, no provider-local memory intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: each seed entry maps to a named source row.
- Adversarial verification: checked for fake `MACHINE_CHECKED` claims and
  `defectCategory`/`defectClass` collisions before assignment.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Without a fixed entry template, future ADIF entries could each invent their own field shape | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T1 fixes one entry template before any resolver is built | handled by this tranche |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed | handled |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: ADIF-T1 is a documentation/reference
entry-schema and seed-dictionary tranche; it defines field templates and
catalogs existing evidence, not an evidence-comparison or
hypothesis-testing artifact.

## Machine Closure Package

This work order does not claim ADIF-T1 closed in the canonical sense;
closure of the whole T0-T5 chain belongs to Codex after T5, and a checkpoint
review of this tranche specifically belongs to Codex per the ADIF-T0
choreography finding.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ADIF_T1_ENTRY_SCHEMA_SOURCE_LAYOUT_SEED_DICTIONARY_2026-06-23.md` | `Status: AUTHORIZED_FOR_CONTINUOUS_EXECUTION` | PASS |
| ADIF entry template | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Seed entries | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0001.md` through `CVF_ADIF-0008.md` | `Status: ACTIVE` each | PASS |
| Completion or reviewer artifact | N/A with reason: Codex performs a checkpoint review of this tranche, then reviews and closes the complete T0-T5 chain after T5 | N/A with reason | N/A with reason |
| Session continuity | active session front-door/state/handoff | N/A with reason: session-sync is forbidden in this batch and remains Codex-owned | N/A with reason |
| System loop interlock | N/A | no runtime/source interlock changed | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T1 is private provenance governance-reference work. No
public-sync repository work or public catalog claim is authorized.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: ADIF-T1 authorizes documentation/reference work only |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed |
| Freshness disposition | PASS - no runtime, provider, helper/checker, or public-sync behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T1 entry-schema and seed-dictionary execution only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local repository work, tests, gates, commit |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | entry schema, source layout, and seed dictionary only |
| forbiddenExpansion | resolver/generator/checker/hook implementation, runtime/provider/live, public-sync, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T1 execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, governance gates, git commit |
| Target paths | this work order; ADIF-T1 baseline; ADIF entry template; eight seed entries; ADIF front door update; roadmap row update |
| Allowed scope source | ADIF-T1 GC-018 baseline, canonical continuous-execution authorization, and ADIF-T0 checkpoint review |
| Before status evidence | executionBaseHead `0fde5cf2`; clean worktree confirmed |
| After status evidence | ADIF-T1 checkpoint committed; execution stops for Codex review |
| Diff evidence | child-batch name-status and committed diff |
| Approval boundary | ADIF-T1 child scope only |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t1-execution-2026-06-23` |
| Expected manifest | this work order; ADIF-T1 baseline; ADIF entry template; eight seed entries; ADIF front door update; roadmap row update |
| Actual changed set | recorded in the ADIF-T1 checkpoint commit |
| Manifest delta | MATCH |

WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond the usual checks;
no surprise blocker, no helper gap, no worktree contamination this return

## Operator Checkpoint

The human principal pre-selected the entire continuous sequence
`T0 -> T1 -> T2 -> (T3 || T4) -> T5` in the canonical authorization, and this
turn separately instructed a stop after the T1 checkpoint for review. A
fresh pause beyond that applies only to scope/risk/claim expansion,
runtime/provider/live/public work, secrets/quota, destructive action,
canonical-owner semantic change, or a different execution order than the
one named above.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Entry template includes every field from the ADIF-T0 contract's canonical-reuse and ADIF-owned tables | template review |
| AC2 | Each of the eight seed entries cites canonical evidence and declares exactly one `enforcementLevel` | entry review |
| AC3 | No seed entry claims `MACHINE_CHECKED` without an independently verified `checkerBindings` path | entry review against `ls` confirmation |
| AC4 | No seed entry conflates `defectCategory` with `defectClass` | entry review |
| AC5 | Pre-implementation autorun gate passes over the real range | gate receipt |
| AC6 | Execution stops after the T1 checkpoint commit; no T2 work begins in this batch | `git status --short`; diff |

## Review Gate

Codex performs a checkpoint review of this ADIF-T1 tranche specifically (per
the ADIF-T0 checkpoint review's choreography finding), restores
active-handoff HEAD continuity, and only then may release ADIF-T2 with a
fresh dependency-release evidence row. Codex separately reviews the complete
T0-T5 committed graph after T5 for final closure.

## Closure Checklist

- [x] ADIF-T0 checkpoint accepted T1 for continuation.
- [x] ADIF-T1 child GC-018 and work order exist and are source-verified.
- [x] ADIF-T1 deliverables are created inside Allowed scope only.
- [x] Pre-implementation autorun gate passes over the real range.
- [x] No resolver/helper/checker/generator/hook file was created.
- [x] Execution stopped after the T1 checkpoint commit.
- [ ] Codex checkpoint review and continuity sync for ADIF-T1 (pending; not
      owned by this child packet).

## Return-To-Orchestrator Conditions

Return success only as `COMPLETE_PENDING_REVIEW` for this child tranche.
Return `BLOCKED_WITH_REASON` for any Stop Condition in the canonical
authorization packet. Do not continue into ADIF-T2 in this batch.

## Claim Boundary

This work order authorizes and records execution of only the ADIF-T1
entry-schema, source-layout, and seed-dictionary tranche. It does not
authorize ADIF-T2 through T5 implementation, resolver/checker/helper code,
runtime/provider/live behavior, public-sync, or final closure. Codex remains
the designated final reviewer/closer for the complete T0-T5 chain and must
checkpoint-review this tranche before any further release.
