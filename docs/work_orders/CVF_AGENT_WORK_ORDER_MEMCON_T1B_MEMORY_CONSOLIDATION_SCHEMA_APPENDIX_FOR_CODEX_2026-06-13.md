# CVF Agent Work Order - MEMCON-T1b Memory Consolidation Schema Appendix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex

Assigned executor: Codex

Commit mode: CODEX_MAY_COMMIT_AFTER_GATES

dispatchBaseHead: `b3bfa93e`

executionBaseHead: `b3bfa93e`

closureBaseHead: `b3bfa93e`

GC-018:
`docs/baselines/CVF_GC018_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Objective

Close MEMCON-T1b by authoring the doc-only Memory Consolidation schema appendix
and field tables that MEMCON-T2 can later validate with machine checks.

## Purpose

This work order gives MEMCON-T1b a bounded authority shell before schema
authoring and closure.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator authorization | chat authorization for MEMCON-T1b | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | Keeps scope bounded to T1b |
| Executor | Codex | Authors doc-only artifacts |
| Reviewer | Codex | Runs machine gates and source checks |
| Closer | Codex | Commits only after gates pass |

## Scope

Allowed paths:

- `docs/baselines/CVF_GC018_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_FOR_CODEX_2026-06-13.md`
- `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`
- `docs/reviews/CVF_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_COMPLETION_2026-06-13.md`
- `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`
- `docs/corpus-intelligence/registry/entries/memory-consolidation-schema-appendix.json`
- generated GC-051 aggregate files from the registry generator
- active session front-door/state/handoff files for closure sync only

Forbidden paths:

- `EXTENSIONS/`
- external Policy_Local workspace
- public-sync workspace
- provider key files
- runtime routes, package manifests, database files, OCR assets, vector stores

## Single-Agent Multi-Role Control Block

Codex may act as orchestrator, schema author, reviewer, and closer for this
bounded doc-only tranche because:

- the tranche has no runtime/source mutation;
- field claims are backed by current source and T1a artifacts;
- acceptance gates are machine-checked before commit;
- completion must include claim boundary and no-runtime evidence.

This does not authorize single-agent closure for broader runtime, provider,
Policy_Local, or public-sync work.

## Intake Role Routing Decision

Routing: `SINGLE_AGENT_MULTI_ROLE_ALLOWED_BOUNDED`.

Reason: T1b is a private provenance doc-only schema appendix with source
verification and no external workspace mutation.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`
- `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`
- `docs/reference/CVF_MEMORY_CONSOLIDATION_EXISTING_OWNER_RECONCILIATION_MAP_2026-06-12.md`
- `docs/reviews/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_CLAUDE_REBUTTAL_2026-06-12.md`

## Pre-Flight Checks

Required before file edits:

- `git status --short --branch`
- startup front-door/state/handoff read;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b3bfa93e --head HEAD`

## Write Ownership

Codex owns only the allowed paths listed in this work order. Generated GC-051
aggregate JSON may change only through the generator.

## Current Runtime Freshness Verification

Runtime/source facts cited by this work order were refreshed from the current
workspace before authoring. T1b does not modify runtime source.

Commands:

```powershell
rg -n "export type MemoryTier|export interface MemoryTierClassification|persistenceClass|describeMemoryTier" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts
rg -n "export type MemoryLifecycleState|evaluateLifecycleTransition|expired|disputed" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts
rg -n "export interface MemoryRetrievalCandidate|rawMemoryReleased|BLOCKED_STATES" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts
rg -n "MemorySignal|MemoryCandidate|ConsolidatedMemoryRecord" EXTENSIONS governance --glob '!**/node_modules/**'
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| MEMCON-T1b authorizes schema appendix and field tables | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T1b Detail`; proposed tranche table | `MEMCON-T1b` | MEMCON roadmap | ACCEPT |
| T1a defines vocabulary and says field tables are T1b scope | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | Scope, Non-Goals, Claim Boundary | `MemorySignal` | MEMCON T1a standard | ACCEPT |
| T1a defines candidate and record promotion gates | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | Vocabulary; Temporal Normalization Rule; Consolidation Decision Rule | `MemoryCandidate` | MEMCON T1a standard | ACCEPT |
| T1a defines retrieval raw-release boundary | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | Retrieval Eligibility Rule | `rawMemoryReleased` | MEMCON T1a standard | ACCEPT |
| Existing lifecycle owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | lines 4, 49, 57, 65 | `MemoryLifecycleState` | `evaluateLifecycleTransition` | ACCEPT |
| Existing tier owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | lines 1, 17-30, 48 | `MemoryTier` | `describeMemoryTier` | ACCEPT |
| Existing retrieval candidate owner exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17, 49, 52, 258 | `MemoryRetrievalCandidate` | `evaluateRetrievalRequest` | ACCEPT |
| Existing post-store memory workflow exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 29, 31, 49, 95 | `MemoryRuntimeWorkflowInput` | `runMemoryRuntimeWorkflowChain` | ACCEPT |
| Existing controlled-memory release invariant exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 25, 40, 50, 88 | `rawMemoryReleased` | `evaluateMemoryGatewayRequest` | ACCEPT |
| Existing W7 contradiction flag exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | lines 11, 28, 97 | `contradiction_flag` | `W7MemoryRecord` | ACCEPT |
| Existing knowledge maintenance taxonomy exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.maintenance.contract.ts` | lines 13-18, 153-191 | `KnowledgeMaintenanceSignalType` | `KnowledgeMaintenanceContract` | ACCEPT |

## New Doc-Only Fields

| Proposed field/symbol | Required use | Runtime boundary |
| --- | --- | --- |
| `MemorySignal` | T1b field table | No runtime type/interface claim |
| `MemoryCandidate` | T1b field table | No runtime type/interface claim; distinct from `MemoryRetrievalCandidate` |
| `ConsolidatedMemoryRecord` | T1b field table | No runtime type/interface claim |
| `MemoryRetrievalPackInput` | T1b field table | No runtime retrieval behavior claim |
| `OperatorMemoryReviewPacket` | T1b field table | No UI/runtime workflow claim |

## Negative Search And Collision Discipline

Search roots:

- `EXTENSIONS/`
- `governance/`
- governed MEMCON docs for doc collisions

Runtime/source-owner results:

- `MemorySignal`: no runtime type/interface/function owner found.
- `MemoryCandidate`: no runtime type/interface owner found; helper functions
  named `graphNodeToMemoryCandidate` and `kgrNodeToMemoryCandidate` exist, and
  existing interface `MemoryRetrievalCandidate` must remain the retrieval-stage
  owner.
- `ConsolidatedMemoryRecord`: no runtime type/interface/function owner found.

Disposition: define doc-only field tables only. Future runtime work must open a
fresh source-verified implementation tranche before claiming these symbols as
runtime owners.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Work-order instruction | Closure artifact |
| --- | --- | --- |
| Schema appendix under `docs/reference/` | Create schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` |
| Field tables for five surfaces | Add five field-table sections | schema appendix |
| Negative search evidence for proposed names | Record collision block | GC-018, work order, schema appendix |
| No runtime/storage/retrieval/Policy_Local mutation | Restrict allowed scope | completion review and diff evidence |
| T2 remains later checker tranche | Update roadmap after T1b | parent roadmap |

## Execution Plan

1. Author GC-018, work order, schema appendix, completion review, and registry
   source entry.
2. Generate GC-051 aggregate registry from source entries.
3. Update the MEMCON roadmap status and tranche table.
4. Run reviewer-fast.
5. Run pre-commit.
6. Commit material closure.
7. Update active session state/front door/handoff in a separate sync commit if
   required by active-session continuity.

## Evidence Requirements

- Source verification table with current source paths and symbols.
- New doc-only fields table.
- Negative search and collision block.
- Roadmap-to-work-order trace matrix.
- Machine Closure Package.
- Gate command results.

## Review Gate

Codex must run reviewer-fast before pre-commit and must repair any in-scope
finding before committing.

## Closure Checklist

- [x] GC-018 exists.
- [x] Work order exists.
- [x] Schema appendix exists.
- [x] Completion review exists.
- [x] Roadmap row updated.
- [x] GC-051 source entry exists.
- [x] Runtime collision evidence recorded.
- [x] Claim boundary recorded.
- [x] Public Export Disposition recorded.

## Return-To-Orchestrator Conditions

Return to operator instead of closing if:

- runtime implementation becomes necessary;
- Policy_Local mutation becomes necessary;
- provider/API-key execution becomes necessary;
- public-sync becomes necessary;
- source verification contradicts the T1b boundary.

## Operator Checkpoint

No operator checkpoint is required inside T1b unless the scope expands. The next
checkpoint is whether to authorize MEMCON-T2 or hold MEMCON for a downstream
Policy_Local foundation decision.

## Acceptance Criteria

- Schema appendix exists and is `Status: CLOSED_PASS_BOUNDED`.
- All five field tables exist.
- Existing owners are reused and not redefined.
- Runtime collision evidence is present.
- GC-051 generator/checker passes.
- Reviewer-fast passes.
- Pre-commit governance chain passes.
- Completion review includes Machine Closure Package, Finding-To-Governance
  Learning Disposition, Public Export Disposition, and Claim Boundary.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `Status: MEMCON_T1B_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 generator and checker PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | GC-051 checker PASS; no Markdown aggregate mutation required by generator | PASS |
| Runtime/source mutation | `git diff --name-status` | no `EXTENSIONS/` paths changed | PASS |
| External evidence digest | N/A with reason | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop mutation authorized | N/A with reason |
| Session continuity | active state and handoff | separate session-sync commit follows material closure if active-session gate requires it | N/A with reason |

## Finding-To-Governance Learning Disposition

| Finding / risk | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| T1a intentionally left typed field tables to T1b | SPEC_COMPLETION_GAP | governance/control-plane learning | RULE_APPLIED | Close T1b schema before T2 checker |
| Proposed symbols collide with doc-only vocabulary and retrieval helper names | SOURCE_COLLISION_RISK | governance/control-plane learning | RULE_APPLIED | Record collision disposition; do not claim runtime owner |
| Future T2 could overread T1b as runtime implementation | CLAIM_BOUNDARY_RISK | governance/control-plane learning | RULE_APPLIED | Add explicit schema-only boundary in all artifacts |

## Claim Boundary

This work order closes doc-only schema authoring. It does not claim runtime
implementation, durable memory storage, retrieval behavior change,
Policy_Local readiness, EC activation, T12 unlock, provider/API-key proof,
public-sync export, production/public readiness, memory reinjection,
high-risk promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Memory Plane schema appendix; public-sync is not authorized in
this tranche.
