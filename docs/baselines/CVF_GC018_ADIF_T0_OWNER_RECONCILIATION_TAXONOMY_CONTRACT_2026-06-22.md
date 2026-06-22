# CVF GC-018 - ADIF-T0 Owner Reconciliation And Taxonomy Contract

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_CONTINUOUS_EXECUTION

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: 7745339c

executionBaseHead: 7745339c

closureBaseHead: NOT_EXECUTED_YET

Commit mode: `WORKER_MAY_COMMIT`

Batch ID: ADIF-T0

## Purpose

Authorize the first child tranche of the ADIF continuous-execution chain.
ADIF-T0 produces one reference contract that freezes ownership relationships
between ADIF and its existing canonical owners (F2G, FPRC, Worker Experience
Retrospective, Guard Orientation, INDEX classification), defines the
`defectCategory` axis as orthogonal to canonical `defectClass`, defines the
entry lifecycle and severity semantics, and resolves the INDEX classification
question for the future ADIF cross-reference surface.

This baseline is authorized under, and subordinate to, the canonical
continuous-execution packet. It does not waive that packet's stop conditions,
parallel-fork protocol, or Codex final-review requirement.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Canonical continuous-execution authorization | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | ACCEPT |
| Master work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_CONTINUOUS_EXECUTION_T0_T5_FOR_CLAUDE_2026-06-22.md` | ACCEPT |
| ADIF roadmap | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ACCEPT |
| Dispatch commit containing the three artifacts above | `783b2b8a` | ACCEPT |
| Session sync commit after dispatch | `7745339c` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| F2G owns defect class, learning lane, disposition, next action | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Protocol; Minimum learning lanes; Minimum defect classes | `Finding-To-Governance Learning Disposition` | F2G canonical standard | VALUE_SET | ACCEPT |
| F2G minimum defect classes are WORKER_EXECUTION_ERROR, ORCHESTRATOR_PACKET_GAP, RULE_GAP, MACHINE_GATE_GAP, PHASE_GATE_PLACEMENT_GAP, OPERATOR_SCOPE_CLARITY_GAP, RUNTIME_SIGNAL_GAP | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | Minimum defect classes | `Minimum defect classes` | F2G canonical standard | VALUE_SET | ACCEPT |
| FPRC owns root-cause role vocabulary ROOT_CAUSE, PROPAGATED_SYMPTOM, EVIDENCE_REPLICATION, STALE_SYNC, REVIEWER_REPAIR_SIDE_EFFECT | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | Root Cause To Propagated Findings; Defect Role Field | `defectRole` | FPRC canonical standard | VALUE_SET | ACCEPT |
| FPRC owns the Boundary-Prose Trigger Discipline keyword-trap map | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | Boundary-Prose Trigger Discipline | known keyword trigger classes table | FPRC canonical standard | VALUE_SET | ACCEPT |
| Worker Experience Retrospective owns frictionLevel, frictionType, observedStep, preventiveControlCandidate | `docs/reference/worker_experience_retrospective/README.md` | Required Token; Enum Meaning | `WORKER_EXPERIENCE_RETRO` | worker experience retrospective standard | VALUE_SET | ACCEPT |
| Guard Orientation is the task-first, role-neutral map to guard surfaces | `docs/reference/guard_orientation/README.md` | Purpose; Task Class Guard Map | `Task Class Guard Map` | guard orientation front door | EXISTS | ACCEPT |
| INDEX classification distinguishes GOVERNED_DOC from INDEX_ARTIFACT from RAW_LEGACY; a GOVERNED_DOC must never be INDEX-labeled | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | Core Distinction: GOVERNED_DOC vs INDEX_ARTIFACT vs RAW_LEGACY; Rules for each class | `GOVERNED_DOC`; `INDEX_ARTIFACT` | INDEX classification standard | LITERAL_INVARIANT | ACCEPT |
| INDEX_ARTIFACT requires seven metadata fields: INDEX type, Source authority, Status, Date, Human-reviewable, Claim boundary, Public Export Disposition | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | Required Metadata Per INDEX Artifact | required metadata table | INDEX classification standard | VALUE_SET | ACCEPT |
| IDX-2 PLANE_OWNER_MAP is the closest existing INDEX type to a future cross-owner lookup map | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | IDX-2: PLANE_OWNER_MAP | `IDX-2 PLANE_OWNER_MAP` | INDEX classification standard | VALUE_SET | ACCEPT |
| ADIF roadmap defines proposed defectCategory axis as new doc-only planning vocabulary, not current source enums | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Proposed Defect Category Axis | `defectCategory` | ADIF roadmap | DOC_ONLY_NEW | ACCEPT |
| ADIF roadmap defines proposed entry contract fields including defectCategory, defectClass, defectRole, enforcementLevel | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | Proposed Entry Contract | proposed field table | ADIF roadmap | VALUE_SET | ACCEPT |
| ADIF-T0 must decide canonical-reuse vs ADIF-owned fields, INDEX classification, task-class alignment, guidance-vs-enforcement, and retirement/supersession without deleting audit history | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T0 - Owner Reconciliation And Taxonomy Contract | Must decide list | ADIF roadmap | VALUE_SET | ACCEPT |
| ADIF-T0 boundary is documentation/reference only; no schema file, directory population, helper, checker, generator, hook, or historical migration | `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md` | ADIF-T0 - Owner Reconciliation And Taxonomy Contract | Boundary statement | ADIF roadmap | LITERAL_INVARIANT | ACCEPT |
| Continuous authorization requires a fresh child GC-018/work order, predecessor anchor, real-range pre-dispatch/pre-implementation gates, and commit before implementation | `docs/baselines/CVF_GC018_ADIF_CONTINUOUS_EXECUTION_AUTHORIZATION_2026-06-22.md` | Continuous Execution Decision | `AUTO_RELEASE_WITH_EVIDENCE` | ADIF continuous-execution authorization | DOC_ONLY_NEW | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- create `docs/reference/agent_defect_intelligence/README.md` as the stable
  ADIF front door;
- create `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md`
  as the owner-reconciliation and taxonomy contract;
- update `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  tranche/checkpoint row for ADIF-T0 only;
- decide and record: canonical-reuse field list, ADIF-owned lookup metadata
  list, INDEX classification decision for the future ADIF cross-reference
  surface, task-class alignment approach with Guard Orientation, guidance vs.
  enforcement distinction, and retirement/supersession policy;
- create local checkpoint commit for this tranche only.

Forbidden scope:

- no schema file, entry directory, generated aggregate, helper, checker,
  generator, or hook wiring (reserved for ADIF-T1 and later);
- no historical finding migration;
- no change to F2G, FPRC, Worker Experience, Guard Orientation, or INDEX
  canonical enums;
- no runtime, provider/live, public-sync, or session-continuity edit;
- no claim of agent comprehension or defect-prevention effectiveness.

Risk ceiling: R0/R1 documentation/reference only.

## Required Deliverables

- `docs/reference/agent_defect_intelligence/README.md`
- `docs/reference/agent_defect_intelligence/CVF_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT.md`
- `docs/roadmaps/CVF_AGENT_DEFECT_INTELLIGENCE_FOUNDATION_ROADMAP_2026-06-22.md`
  (ADIF-T0 row update only)
- this GC-018 baseline
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ADIF_T0_OWNER_RECONCILIATION_TAXONOMY_CONTRACT_2026-06-22.md`

## Decision / Baseline / Proposed Tranche

Decision: authorize ADIF-T0 for continuous execution under the canonical
ADIF authorization. Baseline: dispatch commit `783b2b8a`, session-sync commit
`7745339c`. Proposed tranche: ADIF-T0 Owner Reconciliation And Taxonomy
Contract, executed and committed by Claude under `WORKER_MAY_COMMIT`.

## Dependency Release Evidence

| Prerequisite artifact | Closure or dispatch commit | Disposition | Gate evidence |
|---|---|---|---|
| Canonical continuous-execution authorization and master work order | `783b2b8a` | ACCEPT | committed; pre-implementation autorun 47/47 PASS at range `7745339c..HEAD` before this packet |
| ADIF roadmap | `d86f49e9` (original); dispatch-state update in `783b2b8a` | ACCEPT | committed |

## Evidence / Verification

Pre-dispatch verification for this child packet:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7745339c --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 7745339c --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator proposal absorbed into ADIF roadmap; ADIF-T0 ADAPTs the proposed taxonomy into a CVF-owned reference contract |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ADIF-T0 owner-reconciliation contract |
| Disposition | ADAPT as bounded CVF-owned taxonomy contract; canonical F2G/FPRC/INDEX owners preserved |
| Claim boundary | operator proposal and roadmap design input only; this baseline and the canonical authorization are the CVF-governed dispatch authority |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: ADIF-T0 authorizes documentation/reference work only; no runtime route, provider gateway, or model registry behavior is changed |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed, consumed, or claimed by ADIF-T0 |
| Runtime behavior claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no runtime, provider, helper/checker, or public-sync behavior is claimed by this dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ADIF-T0 owner-reconciliation and taxonomy-contract authoring only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed documentation/reference classification only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | owner-reconciliation taxonomy contract only |
| forbiddenExpansion | schema/entry/generator/checker/hook implementation, runtime/provider/live, public-sync, and universal control remain out of scope for ADIF-T0 |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Defect knowledge is distributed across F2G/FPRC/Worker Experience/Guard Orientation with no bounded cross-owner lookup contract | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | ADIF-T0 produces the owner-reconciliation contract that later tranches build on | handled by this tranche |
| Runtime/provider/cost applicability for ADIF-T0 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: ADIF roadmap `## ADIF-T0` tranche definition.
- Predecessor intake artifact: canonical continuous-execution authorization
  and master work order.
- Delta ledger status: `UNCHANGED_FROM_INTAKE` - ADIF-T0 executes exactly the
  roadmap-defined tranche with no scope change.
- Routing matrix status: `DO_NOW` for the owner-reconciliation contract;
  `DEFER` for schema/resolver/preflight/intake/guard work (ADIF-T1 through
  T5).
- Semantic sampling status: sampled F2G, FPRC, Worker Experience, Guard
  Orientation, and INDEX classification standards directly before authoring.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | ADIF-T0 scope matches the roadmap tranche definition exactly. |
| CHANGED_DISPOSITION | None for this tranche. |
| NEW_FINDING | None beyond the roadmap's own design-review requirement. |
| REMOVED_OR_REJECTED | Schema/directory/helper/checker/generator/hook/migration scope remains rejected for ADIF-T0. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | ADIF-T0 owner-reconciliation contract. |
| DEFER | ADIF-T1 schema/source layout/seed dictionary. |
| DEFER | ADIF-T2 resolver, ADIF-T3 preflight integration, ADIF-T4 intake bridge, ADIF-T5 integrity guard. |
| RESOLVED_BY_DESIGN | F2G/FPRC/Worker Experience/Guard Orientation/INDEX remain the existing canonical owners; ADIF-T0 adds an orthogonal lookup axis rather than replacing any of them. |
| SEPARATE_RUNTIME_TRANCHE | any future schema generator, resolver helper, checker, or hook wiring belongs to ADIF-T1 through T5, not this contract. |
| STRATEGIC_OPERATOR_DECISION | whether ADIF-T1/T2 ultimately builds the IDX-2 aggregate view named in the INDEX Classification Decision section remains an operator/Codex call at that later tranche. |
| OUT_OF_SCOPE | runtime/provider/live, public-sync, session-continuity, historical migration. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ADIF-T0-RS1 | INDEX Classification Standard Core Distinction | a GOVERNED_DOC must never be labeled as an INDEX type | DO_NOW | Does the ADIF-T0 contract itself claim an INDEX type label? | PASS - contract is classified GOVERNED_DOC, not INDEX_ARTIFACT |
| ADIF-T0-RS2 | F2G Minimum defect classes | F2G owns the canonical defect-class enum | DO_NOW | Does ADIF-T0 define a competing defectClass enum? | PASS - defectCategory is declared orthogonal; defectClass remains F2G-owned |
| ADIF-T0-RS3 | FPRC Boundary-Prose Trigger Discipline | certain trigger words in N/A prose force unintended evidence classes | DO_NOW | Does this baseline's prose contain unguarded trigger words? | PASS - no bare trigger tokens used in N/A reasons |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded
  governance-reference tranche.
- Corpus root: repo-local source files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-22 ADIF-T0 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=12; ledger_terminal=12 READ; exclusions=4; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no historical finding corpus scan, no schema/runtime
  source mutation, no public repository scan, no provider-local memory
  intake.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated.
- Drift check: N/A with reason: no generated artifact edited.
- Output traceability: each ownership decision maps to a named canonical
  source row above.
- Adversarial verification: checked for duplicate taxonomy ownership claims
  and INDEX-as-authority risk; both pass to the ADIF-T0 contract itself.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ADIF-T0 is private provenance governance-reference work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude continuous-execution orchestrator/worker |
| Provider or surface | local workspace |
| Session or invocation | ADIF-T0 child dispatch and execution, 2026-06-22 |
| Working directory | repository root |
| Command or tool surface | governed source reads, file write tool, governance gates, git commit |
| Target paths | this baseline; paired work order; ADIF reference front door and taxonomy contract; roadmap row update |
| Allowed scope source | canonical continuous-execution authorization and master work order |
| Before status evidence | executionBaseHead `7745339c`; clean worktree confirmed; pre-implementation autorun 47/47 PASS |
| After status evidence | ADIF-T0 child packet and deliverables committed as one checkpoint |
| Diff evidence | child-batch name-status and committed diff |
| Approval boundary | ADIF-T0 child scope only; no T1-T5 implementation in this batch |
| Claim boundary | conditional execution chain with evidence gates; no runtime/public/provider expansion |
| Agent type | continuous-execution orchestrator/worker |
| Invocation ID | `adif-t0-execution-2026-06-22` |
| Expected manifest | this baseline; paired work order; ADIF reference front door; ADIF-T0 taxonomy contract; roadmap row update |
| Actual changed set | recorded in the ADIF-T0 checkpoint commit |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | ADIF-T0 contract distinguishes canonical-reuse fields from ADIF-owned lookup metadata. |
| AC2 | `defectCategory` is declared explicitly orthogonal to canonical `defectClass`. |
| AC3 | INDEX classification decision is recorded for the future ADIF cross-reference surface without claiming an INDEX type for this contract itself. |
| AC4 | Guidance-only vs. machine-checked distinction is defined. |
| AC5 | Retirement/supersession policy preserves audit history. |
| AC6 | No schema/helper/checker/generator/hook file is created. |

## Claim Boundary

This baseline authorizes only the ADIF-T0 owner-reconciliation and
taxonomy-contract tranche inside the canonical continuous-execution chain. It
does not authorize ADIF-T1 through T5 implementation, schema/checker/helper
code, runtime/provider/live behavior, public-sync, or final closure. Codex
remains the designated final reviewer/closer for the complete T0-T5 chain.
