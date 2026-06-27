# CVF GC-018 Baseline: MEMCON-T1a Memory Consolidation Standard And Owner Reconciliation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-12

Owner: Codex

baseHead: `16d9fdf5`

Parent roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

Roadmap rebuttal:
`docs/reviews/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_CLAUDE_REBUTTAL_2026-06-12.md`

Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T1A_MEMORY_CONSOLIDATION_STANDARD_OWNER_RECONCILIATION_FOR_CLAUDE_2026-06-12.md`

## Purpose

Authorize MEMCON-T1a as the first bounded Memory Consolidation foundation
tranche.

MEMCON-T1a must create the canonical memory consolidation workflow-chain
standard and an existing-owner reconciliation map. It is documentation/spec
work only. It must not implement runtime behavior, create schema appendix
field tables, add machine checkers, mutate memory records, touch Policy_Local,
or claim retrieval, production, public, or memory-quality readiness.

## Scope / Target / Owner Boundary

In scope:

- define the Memory Consolidation standard under `docs/reference/`;
- define vocabulary for memory signal lifecycle, memory candidate lifecycle,
  consolidation decisions, source authority, confidence, conflict, staleness,
  temporal normalization, retrieval eligibility, and operator-visible review;
- include the temporal-blocking rule in the standard;
- create an existing-owner reconciliation map covering current CVF memory,
  learning, retrieval, lifecycle, tier, W7, and knowledge-maintenance surfaces;
- record planned follow-up boundaries for MEMCON-T1b through MEMCON-T5.

Out of scope:

- runtime/source implementation;
- TypeScript or Python code edits;
- schema appendix or field-table closure;
- machine checker implementation;
- generated aggregate JSON changes;
- external Policy_Local mutation;
- EC activation, retrieval behavior change, OCR/provider/API proof, corpus
  ingestion, public-sync, T12 unlock, readiness claim, memory reinjection,
  high-risk promotion, or autonomous mutation.

## Authority Chain

| Authority | Path or source | Status |
| --- | --- | --- |
| Operator instruction | 2026-06-12 authorization for MEMCON-T1a | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | next move permits MEMCON-T1a authorization |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff names MEMCON-T1a as next allowed move |
| Parent roadmap | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `REVISED_READY_FOR_MEMCON_T1A_AUTHORIZATION` |
| Claude rebuttal | `docs/reviews/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_CLAUDE_REBUTTAL_2026-06-12.md` | incorporated into roadmap |

## Decision / Baseline

Decision: `DISPATCH_MEMCON_T1A_WORKER_MUST_NOT_COMMIT`.

Claude may author the MEMCON-T1a standard and existing-owner reconciliation map
inside the allowed documentation scope. Codex remains reviewer and committer.

Baseline: CVF already has partial memory owner surfaces, but not a composed
pre-store consolidation standard. MEMCON-T1a must build on those owners instead
of re-authoring them as missing.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Treat memory as consolidation, not accumulation.
2. Keep repository artifacts and source maps above chat memory.
3. Define pre-store consolidation as feeding the existing retrieval-time memory
   runtime workflow chain.
4. Require temporal ambiguity to block durable consolidation unless normalized.
5. Make operator-visible memory review part of the standard.
6. Preserve Policy_Local as a downstream use case, not as the generic memory
   owner.

Rejected design:

- storing full transcripts as default durable memory;
- treating current owner surfaces as absent;
- creating schema appendix and checker in T1a;
- changing runtime retrieval behavior;
- authorizing autonomous memory mutation;
- touching Policy_Local.

## Current Runtime Freshness Verification

| Runtime surface | Freshness check | Disposition |
| --- | --- | --- |
| Controlled memory gateway | `rg -n "CONTROLLED_MEMORY_GATEWAY_PHASE2_VERSION|rawMemoryReleased|global_memory_scope_not_authorized|memory_reinjection_not_authorized" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` returned lines 1, 50, 88, 102, and 121 | PASS |
| Learning signal intake bridge | `rg -n "LearningSignalIntakeRecord|LearningSignalIntakeInput|autonomousMutationAuthorized" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` returned lines 39, 51, 65, 123, and 170 | PASS |
| Memory lifecycle policy | `rg -n "MemoryLifecycleState|evaluateLifecycleTransition|unreinforced_memory_expired" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` returned lines 4, 49, and 65 | PASS |
| Memory tier classifier | `rg -n "MemoryTier|persistenceClass|describeMemoryTier" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` returned lines 1, 20, and 48 | PASS |
| Memory retrieval policy | `rg -n "MemoryRetrievalCandidate|BLOCKED_STATES|rawMemoryReleased" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` returned lines 17, 49, 52, 121, 161, 176, 217, and 258 | PASS |
| Memory runtime workflow chain | `rg -n "runMemoryRuntimeWorkflowChain|MemoryRuntimeWorkflowStatus|rawMemoryReleased" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` returned lines 29, 60, 95, 137, 161, 199, and 215 | PASS |
| W7 memory record | `rg -n "W7MemoryRecord|contradiction_flag" EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` returned lines 11, 28, 79, and 97 | PASS |
| Knowledge maintenance/refactor | `rg -n "KnowledgeMaintenanceSignalType|lint|contradiction|drift|orphan|staleness" EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.maintenance.contract.ts EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.refactor.contract.ts` returned owner lines for all five signal types | PASS |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Controlled memory gateway exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 1-13 | `CONTROLLED_MEMORY_GATEWAY_PHASE2_VERSION`, `MemoryGatewayOperation` | memory gateway contract | ACCEPT |
| Gateway raw-memory non-release invariant exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 50 and 88 | `rawMemoryReleased` | memory gateway result | ACCEPT |
| Gateway denies global memory scope | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 102 | `global_memory_scope_not_authorized` | `evaluateMemoryGatewayRequest` | ACCEPT |
| Gateway blocks unauthorized reinjection | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 121 | `memory_reinjection_not_authorized` | `evaluateMemoryGatewayRequest` | ACCEPT |
| Learning signal intake bridge exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 9, 39, 51, 123, 170 | `LearningSignalIntakeRecord` | learning signal intake bridge | ACCEPT |
| Memory lifecycle primitive exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | lines 4, 49, 65 | `MemoryLifecycleState`, `evaluateLifecycleTransition` | memory lifecycle policy | ACCEPT |
| Memory tier and retention primitive exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | lines 1, 17-30, 48-49 | `MemoryTier`, `persistenceClass`, `describeMemoryTier` | memory tier classifier | ACCEPT |
| Memory retrieval policy exists and blocks expired/disputed states | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17-24, 49, 52, 147-148, 232-233 | `MemoryRetrievalCandidate`, `BLOCKED_STATES`, `rawMemoryReleased` | memory retrieval policy | ACCEPT |
| Retrieval-time workflow chain exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 27, 29, 95, 206-215 | `runMemoryRuntimeWorkflowChain`, `MemoryRuntimeWorkflowStatus`, `rawMemoryReleased` | memory runtime workflow chain | ACCEPT |
| W7 memory record carries contradiction flag | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | lines 11-31, 97 | `W7MemoryRecord`, `contradiction_flag` | W7 memory record contract | ACCEPT |
| Knowledge maintenance carries lint/contradiction/drift/orphan/staleness signals | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.maintenance.contract.ts` | lines 13-18, 153-191 | `KnowledgeMaintenanceSignalType` | knowledge maintenance contract | ACCEPT |
| Knowledge refactor reacts to drift, staleness, orphan, lint, and contradiction | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.refactor.contract.ts` | lines 38-58 | `selectAction`, `buildRationale` | knowledge refactor contract | ACCEPT |
| MEMCON-T1a standard path is new doc-only output | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | MEMCON-T1a Detail | `CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | roadmap planned artifact | ACCEPT |
| MEMCON-T1a owner map is new doc-only output | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | MEMCON-T1a Detail | existing-owner reconciliation map | roadmap planned artifact | ACCEPT |

## New Doc-Only Fields

These names may be defined in MEMCON-T1a as standard vocabulary only. They are
not runtime/source facts until a later authorized implementation creates them.

| Proposed item | Required meaning | Boundary |
| --- | --- | --- |
| `MemorySignal` | raw source-backed signal eligible for memory consolidation review | doc-only in T1a |
| `MemoryCandidate` | normalized candidate extracted from a memory signal | doc-only in T1a |
| `ConsolidatedMemoryRecord` | reviewed memory record after merge/conflict/staleness/temporal gates | doc-only in T1a |
| `TIME_AMBIGUOUS_BLOCKED` | temporal status that blocks durable consolidation until normalized | doc-only in T1a |
| `OPERATOR_VISIBLE_MEMORY_REVIEW_PACKET` | Markdown-first operator inspection packet requirement | doc-only in T1a |

## Acceptance Criteria

1. MEMCON-T1a standard exists and defines the required lifecycle vocabulary and
   temporal-blocking rule.
2. Existing-owner reconciliation map exists and classifies each current memory
   owner surface as reused, extended later, out-of-scope, or blocked.
3. The standard explicitly states that MEMCON is pre-store consolidation and
   feeds the existing post-store retrieval-time workflow chain.
4. No runtime/source files, generated JSON aggregate files, external
   Policy_Local paths, provider/OCR surfaces, retrieval behavior, or EC/T12
   surfaces are changed.
5. Worker return records actual changed files, source verification, gate
   evidence, findings or N/A, and `WORKER_MUST_NOT_COMMIT`.

## Evidence / Verification

Worker pending-return evidence must include:

- startup acknowledgment and `executionBaseHead`;
- `git status --short` with actual pending file list;
- `Test-Path` for every required output artifact;
- `rg` evidence for the temporal-blocking rule, owner-map classification, raw
  memory non-release boundary, autonomous mutation prohibition, and
  Policy_Local non-mutation boundary;
- reviewer-fast result, or command-backed pending-finality reason;
- Finding-To-Governance Learning Disposition if any finding is recorded.

Codex reviewer closure must commit the approved range and run pre-closure with
a non-empty committed range before any closed-equivalent claim.

## Claim Boundary

MEMCON-T1a authorizes documentation/specification only for the memory
consolidation standard and existing-owner reconciliation map. It does not prove
runtime memory consolidation, storage behavior, retrieval correctness,
cross-agent consistency, operator UI behavior, provider behavior, Policy_Local
readiness, public readiness, production readiness, memory quality parity,
memory reinjection, high-risk promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Memory Plane foundation dispatch; public-sync is not
authorized.
