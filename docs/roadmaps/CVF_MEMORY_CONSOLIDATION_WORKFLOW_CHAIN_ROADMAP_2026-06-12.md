# CVF Memory Consolidation Workflow Chain Roadmap

Memory class: FULL_RECORD

Status: MEMCON_T5_DISPATCHED

docType: roadmap

Date: 2026-06-12

Owner: Codex

sourceAuthority:
`docs/reviews/CVF_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_COMPLETION_2026-06-13.md`
`docs/baselines/CVF_GC018_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_2026-06-13.md`

rawMemoryReleased=false

---

## Authorization / Decision

Decision: `MEMORY_CONSOLIDATION_FOUNDATION_BEFORE_POLICYLOCAL_USE_CASE`.

The operator supplied a memory-design learning signal on 2026-06-12: strong AI
memory is not "store more"; it is consolidation, pruning, conflict resolution,
temporal normalization, retrieval discipline, and operator-visible control.

This roadmap converts that signal into a proposed CVF foundation lane before
deeper Policy_Local use-case work. It is not a work order and does not
authorize implementation by itself.

## Purpose

Create a reusable Memory Plane workflow chain that turns raw conversation,
artifact, transcript, handoff, source-map, and worker-return signals into
clean, source-backed, operator-visible memory suitable for retrieval.

The intended product boundary is:

```text
RAW SIGNALS
  -> MEMORY INTAKE
  -> CANDIDATE EXTRACTION
  -> CONSOLIDATION
  -> CONFLICT AND STALENESS REVIEW
  -> TEMPORAL NORMALIZATION
  -> OPERATOR-VISIBLE MEMORY REVIEW
  -> RETRIEVAL PACKAGING
  -> PRUNE OR ARCHIVE
```

The chain should make agents remember less noise, preserve stronger evidence,
and retrieve only the right context for the current task.

## Scope / Target / Owner Boundary

Target owners:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION` for memory gateway, retrieval,
  and future consolidation contracts;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` for W7 memory and knowledge
  maintenance compatibility;
- `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and active
  handoffs as continuity pointer records, not long-term memory databases;
- `docs/reference` for canonical memory consolidation standards;
- `docs/reviews` or `docs/reference` for operator-visible memory review
  packets.

In scope:

- memory candidate lifecycle vocabulary;
- consolidation and pruning contract;
- temporal ambiguity detection and normalization;
- cross-agent memory consistency contract;
- source-authority and confidence metadata;
- conflict, staleness, and outdated-detection signals;
- operator-visible memory review packet;
- retrieval-packaging boundary that prevents raw memory release;
- machine-check candidates for missing memory metadata and ambiguous time
  references.

Out of scope:

- mutating external Policy_Local or `dich-tai-lieu` workspace files;
- implementing vector storage, SQLite, FTS5, embeddings, or a new database;
- provider/API-key calls;
- autonomous memory mutation;
- hidden memory trust;
- public-sync;
- production readiness, public readiness, or memory quality parity claims;
- replacing existing session handoff rules.

## Non-Goals

This roadmap does not:

- claim CVF already has a full Memory Plane workflow chain;
- make chat memory authoritative over repository artifacts;
- store complete transcripts by default;
- make a knowledge graph mandatory for isolated tasks;
- infer facts from vague relative dates;
- authorize any agent to write durable truth memory without review;
- require Policy_Local to be the schema owner for generic memory behavior.

## Authority Chain

| Authority | Path or source | Disposition |
| --- | --- | --- |
| Operator learning signal | 2026-06-12 chat article on memory consolidation | ACCEPT_AS_DESIGN_INPUT |
| Continuity doctrine | `docs/reference/CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md` | ACCEPT |
| Controlled memory gateway | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | ACCEPT |
| Memory retrieval policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | ACCEPT |
| Learning signal intake bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | ACCEPT_AS_EXISTING_FEEDBACK_SIGNAL_OWNER |
| Memory lifecycle policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | ACCEPT_AS_EXISTING_LIFECYCLE_PRIMITIVE |
| Memory tier classifier | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | ACCEPT_AS_EXISTING_RETENTION_PRIMITIVE |
| Memory runtime workflow chain | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | ACCEPT_AS_EXISTING_RETRIEVAL_TIME_CHAIN |
| W7 memory record contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | ACCEPT |
| Knowledge maintenance contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.maintenance.contract.ts` | ACCEPT |
| JSON aggregate discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | ACCEPT_AS_AUTHORING_CONTROL |
| Policy_Local successor roadmap | `docs/roadmaps/CVF_POLICYLOCAL_SUCCESSOR_PILOT_ROADMAP_2026-06-12.md` | ACCEPT_AS_DOWNSTREAM_USE_CASE |

## Current Runtime Freshness Verification

Verified at planning time from current workspace source.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- |
| Controlled memory gateway contract exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 1-13 | `CONTROLLED_MEMORY_GATEWAY_PHASE2_VERSION`, `MemoryGatewayOperation` | ACCEPT |
| Gateway denies global memory scope | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 102 | `global_memory_scope_not_authorized` | ACCEPT |
| Gateway blocks unauthorized reinjection | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 121 | `memory_reinjection_not_authorized` | ACCEPT |
| Gateway never releases raw memory | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 50 and 88 | `rawMemoryReleased` | ACCEPT |
| Retrieval policy lifecycle states exist | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17-24 | `MemoryRetrievalCandidate.lifecycleState` | ACCEPT |
| Retrieval excludes expired and disputed memory | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 52, 147-148, 232-233 | `BLOCKED_STATES` | ACCEPT |
| Retrieval never releases raw memory | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 49, 121, 161, 176, 217, 258 | `rawMemoryReleased` | ACCEPT |
| Learning signal intake exists for feedback signals | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 9, 11, 39, 51, 123 | `LearningSignalIntakeRecord` | ACCEPT |
| Memory lifecycle transition primitive exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | lines 4, 49, 65 | `MemoryLifecycleState`, `evaluateLifecycleTransition`, `unreinforced_memory_expired` | ACCEPT |
| Memory tier and retention primitive exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | lines 1, 17-30, 36, 48-49 | `MemoryTier`, `persistenceClass`, `describeMemoryTier` | ACCEPT |
| Retrieval-time memory workflow chain exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 27, 29, 95, 206-215 | `runMemoryRuntimeWorkflowChain`, `MemoryRuntimeWorkflowStatus`, `rawMemoryReleased` | ACCEPT |
| W7 memory record exists and carries contradiction flag | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | lines 11-31, 97 | `W7MemoryRecord`, `contradiction_flag` | ACCEPT |
| Knowledge maintenance supports lint, contradiction, drift, orphan, staleness | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.maintenance.contract.ts` | lines 13-18, 153-191 | `KnowledgeMaintenanceSignalType` | ACCEPT |
| Continuity doctrine rejects hidden memory authority | `docs/reference/CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md` | lines 35-40 | `Repository truth outranks chat memory`, `Hidden memory must not become authority` | ACCEPT |

## Gap Statement

CVF currently has useful memory-related pieces, but not a complete Memory Plane
workflow-chain system.

Existing pieces:

- session continuity pointer records;
- active state and handoff routing;
- controlled memory gateway decisions;
- retrieval policy with lifecycle filtering;
- learning-signal intake for governance feedback signals;
- memory lifecycle and tier/retention primitives;
- retrieval-time memory runtime workflow chain;
- W7 memory record placement;
- knowledge maintenance checks for lint, contradiction, drift, orphan, and
  staleness;
- learning-plane and finding-to-governance feedback rules.

Remaining gap:

- no memory-specific candidate intake lifecycle for transcript, worker-return,
  handoff, source-map, and operator-supplied memory signals. The existing
  `learning-signal-intake-bridge.ts` covers feedback/defect routing, not
  memory consolidation;
- no composing consolidation contract that merges duplicates, resolves
  conflicts, supersedes stale records, and prunes low-value notes by building
  on the existing lifecycle, tier, retrieval, and maintenance primitives;
- no temporal ambiguity rule for relative time phrases such as `today`,
  `yesterday`, and `last week` in durable memory;
- no cross-agent consistency ledger that interlinks Codex, Claude, Gemini, or
  other worker memory;
- no operator-visible memory review packet that shows active, stale,
  conflicted, pruned, and retrieval-eligible memories;
- no machine gate that blocks memory artifacts missing source authority,
  confidence, conflict, staleness, or retrieval boundary metadata.

MEMCON therefore covers the pre-store consolidation half of the Memory Plane:
raw signals become source-backed consolidated memory. It should feed, not
replace, the existing post-store retrieval-time chain represented by
`runMemoryRuntimeWorkflowChain()`.

## Design Control Gate

Design verdict: `PASS_BOUNDED_DRAFT`.

Selected design:

1. Treat memory as consolidation, not accumulation.
2. Keep repository artifacts and source maps above chat memory.
3. Split raw signals, candidates, consolidated memory, and retrieval packs.
4. Require source authority and confidence metadata before retrieval use.
5. Normalize ambiguous time into concrete dates or block the memory as
   `TIME_AMBIGUOUS`.
6. Make operator-visible memory review a first-class artifact.
7. Define the temporal-blocking rule before consolidation semantics can close.
8. Add machine checks only after the standard and schema are precise enough.
9. Keep Policy_Local as a downstream use case, not as the generic memory owner.

Rejected design:

- store full transcripts as default durable memory;
- let each agent write separate unlinked memory notes;
- make vector search the first tranche;
- treat knowledge graph as mandatory for every task;
- let memory retrieval release raw sensitive memory;
- auto-prune without an operator-visible report;
- use relative dates as durable memory facts.

## Proposed Workflow Chain

### Stage 0 - Source Authority Inventory

Inputs:

- active session front door;
- active state registry;
- handoff;
- governed artifacts;
- worker returns;
- external transcripts only when explicitly authorized.

Output:

- bounded inventory of memory-eligible signals with source paths and capture
  dates.

Gate:

- memory cannot be created from hidden or uncited memory alone.

### Stage 1 - Memory Signal Intake

Create a `MemorySignal` record for each relevant signal.

Required fields:

- `signalId`;
- `sourceType`;
- `sourcePathOrTranscriptRef`;
- `capturedAtDate`;
- `operatorSupplied`;
- `agentSource`;
- `claimText`;
- `riskClass`;
- `sensitiveDataFlag`;
- `candidateAction`.

Allowed `candidateAction` values:

- `PROMOTE_TO_CANDIDATE`;
- `MERGE_WITH_EXISTING`;
- `DEFER_LOW_SIGNAL`;
- `REJECT_NOISE`;
- `BLOCKED_SOURCE_MISSING`.

### Stage 2 - Candidate Extraction

Convert accepted signals into `MemoryCandidate` records.

Required fields:

- `candidateId`;
- `canonicalClaim`;
- `sourceAuthority`;
- `confidenceLevel`;
- `scope`;
- `domainTags`;
- `timeReferences`;
- `temporalNormalizationStatus`;
- `conflictSetIds`;
- `stalenessRisk`;
- `retrievalEligibility`;
- `operatorReviewRequired`.

Allowed `temporalNormalizationStatus` values:

- `ABSOLUTE_DATE_PRESENT`;
- `NORMALIZED_TO_ABSOLUTE_DATE`;
- `NO_TIME_REFERENCE`;
- `TIME_AMBIGUOUS_BLOCKED`.

### Stage 3 - Consolidation

Merge candidates into `ConsolidatedMemoryRecord` only when:

- source authority is present;
- conflict status is resolved or explicitly marked;
- temporal status is not `TIME_AMBIGUOUS_BLOCKED`;
- low-value duplicate candidates are pruned or merged;
- retrieval boundary is declared.

Allowed consolidation decisions:

- `CONSOLIDATED`;
- `MERGED`;
- `SUPERSEDED`;
- `PRUNED_LOW_VALUE`;
- `BLOCKED_CONFLICT`;
- `BLOCKED_STALE`;
- `BLOCKED_TIME_AMBIGUOUS`;
- `DEFERRED_NEEDS_OPERATOR`.

### Stage 4 - Conflict, Staleness, And Outdated Review

Use existing knowledge maintenance semantics where possible:

- `lint`;
- `contradiction`;
- `drift`;
- `orphan`;
- `staleness`.

Additional memory-specific review fields:

- `conflictsWith`;
- `supersedes`;
- `supersededBy`;
- `lastValidatedDate`;
- `nextReviewDate`;
- `staleReason`;
- `operatorDecision`.

### Stage 5 - Operator-Visible Review Packet

Produce a review packet that a non-coder operator can inspect.

Required sections:

- `Active Consolidated Memories`;
- `New Candidate Memories`;
- `Conflicts Requiring Decision`;
- `Stale Or Outdated Memories`;
- `Pruned Or Rejected Noise`;
- `Temporal Ambiguity Blocks`;
- `Retrieval-Eligible Pack Preview`;
- `Operator Actions Required`;
- `Claim Boundary`.

### Stage 6 - Retrieval Packaging

Build a retrieval pack from consolidated memory only.

Rules:

- prefer compact summary over raw transcript;
- include source path and confidence;
- exclude sensitive raw memory;
- exclude `expired`, `disputed`, conflicted, stale-blocked, and
  time-ambiguous memory;
- include only context relevant to the current task;
- never present memory as truth when source authority is weaker than the claim.

### Stage 7 - Prune Or Archive

Memory must have a retirement path.

Allowed outcomes:

- keep active;
- keep as archive-only evidence;
- supersede with newer consolidated record;
- prune as duplicate/noise;
- block pending operator review;
- delete only when a separate explicit deletion authority exists.

## Proposed Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| MEMCON-T1a | Memory consolidation standard, vocabulary, and existing-owner reconciliation map | Operator approval after Claude rebuttal | CLOSED_PASS_BOUNDED |
| MEMCON-T1b | Memory consolidation schema appendix and field tables | MEMCON-T1a closure | CLOSED_PASS_BOUNDED |
| MEMCON-T2 | Temporal ambiguity and source-authority checker | MEMCON-T1b closure | CLOSED_PASS_BOUNDED |
| MEMCON-T3 | Consolidated memory ledger and Markdown-first operator-visible review packet | MEMCON-T2 closure | CLOSED_PASS_BOUNDED |
| MEMCON-T4 | Retrieval-pack integration boundary and conformance tests | MEMCON-T3 closure | CLOSED_PASS_BOUNDED |
| MEMCON-T5 | Cross-agent memory consistency contract | MEMCON-T4 closure | DISPATCHED |
| PL-S1 | Policy_Local evidence-resolution pilot using Memory Plane outputs | MEMCON foundation decision plus fresh authorization | HOLD_PENDING_MEMCON_DECISION |

## Work Plan

1. Send this draft roadmap to Claude for rebuttal before dispatch.
2. Incorporate accepted rebuttal findings into the roadmap without widening
   implementation authority.
3. Open MEMCON-T1a only through fresh GC-018 and a source-verified work order.
4. Author the canonical memory consolidation standard and existing-owner
   reconciliation map before schema authoring.
5. Open MEMCON-T1b for schema only after T1a closes.
6. Add machine checks only after the T1a/T1b vocabulary is precise enough.
7. Keep Policy_Local held until a later PL-S work order consumes closed
   MEMCON foundation outputs.

## MEMCON-T1a Detail

Dispatch artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_MEMCON_T1A_MEMORY_CONSOLIDATION_STANDARD_OWNER_RECONCILIATION_2026-06-12.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T1A_MEMORY_CONSOLIDATION_STANDARD_OWNER_RECONCILIATION_FOR_CLAUDE_2026-06-12.md`.

Goal: define the canonical standard, vocabulary, and existing-owner
reconciliation map before implementation.

Expected artifacts:

- `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`;
- existing-owner reconciliation map covering learning signal intake, memory
  lifecycle policy, tier classifier, retrieval policy, runtime workflow chain,
  W7 memory record, and knowledge maintenance;
- GC-018 baseline;
- source-verified work order for implementation only after roadmap rebuttal.

T1a must define:

- memory signal lifecycle;
- memory candidate lifecycle;
- consolidation decision vocabulary;
- source authority taxonomy;
- confidence and confirmation fields;
- conflict and staleness fields;
- temporal normalization rule;
- retrieval eligibility rule;
- operator-visible packet requirements.

T1a must include the temporal-blocking rule. Consolidation semantics may not
close unless `TIME_AMBIGUOUS_BLOCKED` or an equivalent blocking status is
defined in the standard.

T1a must not:

- implement runtime storage;
- mutate existing memory records;
- change retrieval behavior;
- call providers;
- touch Policy_Local.

## MEMCON-T1b Detail

Goal: author the schema appendix and field tables after the standard and
owner-reconciliation map close.

Closure artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_FOR_CODEX_2026-06-13.md`;
- schema appendix:
  `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`;
- completion:
  `docs/reviews/CVF_MEMCON_T1B_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_COMPLETION_2026-06-13.md`.

Expected artifacts:

- schema appendix under `docs/reference/`;
- field table for `MemorySignal`, `MemoryCandidate`,
  `ConsolidatedMemoryRecord`, retrieval pack input, and operator review
  packet;
- negative search evidence for proposed new symbol names such as
  `MemorySignal`, `MemoryCandidate`, and `ConsolidatedMemoryRecord`, with
  collision dispositions if any current CVF surface already uses those tokens.

T1b must not:

- redefine lifecycle/tier states already owned by current contracts;
- implement runtime storage;
- mutate existing memory records;
- change retrieval behavior;
- call providers;
- touch Policy_Local.

## MEMCON-T2 Detail

Goal: add early machine checks for memory artifacts after the temporal rule and
schema fields exist.

Dispatch artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_2026-06-13.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T2_TEMPORAL_SOURCE_AUTHORITY_CHECKER_FOR_CLAUDE_2026-06-13.md`.

Checker candidates:

- required source authority fields;
- forbidden durable relative-date phrases unless normalized;
- missing conflict or staleness fields;
- missing retrieval boundary;
- raw transcript release marker;
- missing operator-visible review section for consolidation packets.

Temporal ambiguity examples to block in durable memory unless normalized:

- `today`;
- `yesterday`;
- `tomorrow`;
- `last week`;
- `recently`;
- `earlier`;
- `this month`;
- `three months ago`;
- Vietnamese equivalents when the artifact is explicitly Vietnamese-facing.

The checker must allow quoted source evidence only when the artifact records
that the phrase is a quote and not the durable normalized memory value.

## MEMCON-T3 Detail

Goal: create a ledger and Markdown-first operator-visible packet.

Dispatch artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_2026-06-13.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_FOR_CLAUDE_2026-06-13.md`.

Closure artifacts:

- contract:
  `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md`;
- sample packet:
  `docs/reviews/CVF_MEMCON_T3_OPERATOR_MEMORY_REVIEW_PACKET_SAMPLE_2026-06-13.md`;
- worker return:
  `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_WORKER_RETURN_2026-06-13.md`;
- completion:
  `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md`.

Expected outputs:

- Markdown review packet for operator inspection;
- JSON or generated aggregate ledger only if entries become large or
  append-heavy;
- sample fixtures proving active, stale, conflicted, pruned, and
  time-ambiguous memories are rendered distinctly.

JSON authoring must follow the generated aggregate discipline if the ledger is
append-heavy or agent-edited.

## MEMCON-T4 Detail

Dispatch artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_2026-06-13.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_FOR_CLAUDE_2026-06-13.md`.

Closure artifacts:

- helper:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts`;
- focused tests:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-consolidation-retrieval-pack-boundary.test.ts`;
- worker return:
  `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_WORKER_RETURN_2026-06-13.md`;
- completion:
  `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md`.

Goal: retrieval-pack boundary.

It should connect consolidated memory to the existing
`memory-retrieval-policy.ts` and `memory-runtime-workflow-chain.ts` surfaces
without claiming semantic correctness or raw memory release.

Required conformance:

- expired memory excluded;
- disputed memory excluded;
- sensitive memory redacted or summary-only;
- time-ambiguous memory excluded;
- stale-blocked memory excluded;
- source path and confidence included in selected context.

## MEMCON-T5 Detail

Dispatch artifacts:

- GC-018:
  `docs/baselines/CVF_GC018_MEMCON_T5_CROSS_AGENT_MEMORY_CONSISTENCY_CONTRACT_2026-06-13.md`;
- work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T5_CROSS_AGENT_MEMORY_CONSISTENCY_CONTRACT_FOR_CLAUDE_2026-06-13.md`.

Goal: cross-agent consistency.

The contract must distinguish:

- `agentSource`;
- `agentRole`;
- `sourceArtifact`;
- `claimBoundary`;
- `conflictsWithAgentMemory`;
- `resolutionOwner`;
- `operatorConfirmed`.

It must prevent Codex, Claude, Gemini, or another worker from writing separate
authoritative memories without a shared ledger and source-backed reconciliation.

## Policy_Local Relationship

Policy_Local is a downstream use case, not the owner of the memory system.

After MEMCON foundation, PL-S1 can use the memory chain to:

- retain clean context about scan findings;
- remember operator decisions with dates and source authority;
- avoid reprocessing stale or duplicate evidence;
- expose missing metadata and unresolved memory conflicts to the operator;
- prepare retrieval only from consolidated, eligible memory.

Policy_Local must not proceed merely because this roadmap exists. It still
requires a fresh PL-S1 GC-018 baseline and source-verified work order.

## Claude Rebuttal Questions

Claude should review this roadmap for:

1. missing existing CVF memory owners or contracts;
2. overclaim about current Memory Plane capability;
3. unsafe schema fields or ambiguous lifecycle states;
4. whether MEMCON-T1a/T1b split is sufficient to keep standard and schema
   closure bounded;
5. whether temporal normalization should be its own tranche before
   consolidation;
6. whether operator-visible review packet should be Markdown-only first;
7. whether retrieval-pack integration before cross-agent consistency is the
   correct lower-risk order;
8. whether any tranche accidentally authorizes autonomous memory mutation.

## Claude Rebuttal Incorporation

Claude rebuttal artifact:

`docs/reviews/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_CLAUDE_REBUTTAL_2026-06-12.md`

Disposition: `ACCEPTED_WITH_ROADMAP_CORRECTIONS`.

| Rebuttal finding | Roadmap disposition |
| --- | --- |
| RF-1 signal-intake overclaim | ACCEPTED - Gap Statement now distinguishes existing learning-signal intake from missing memory-specific consolidation intake |
| RF-2 consolidation-contract overclaim | ACCEPTED - Gap Statement now says composing consolidation contract over existing lifecycle/tier/maintenance primitives |
| RF-3 runtime-chain not mapped | ACCEPTED - surface table and Gap Statement now distinguish pre-store consolidation from existing post-store retrieval chain |
| RF-4 T1 too broad | ACCEPTED - tranche split into MEMCON-T1a standard/reconciliation and MEMCON-T1b schema |
| RF-5 temporal rule sequencing | ACCEPTED - temporal block rule must be defined in T1a; machine checker remains T2 |
| RF-6 Markdown-first packet | ACCEPTED - MEMCON-T3 is Markdown-first; JSON only if append-heavy |
| RF-7 T4/T5 ordering | ACCEPTED - T4 now retrieval-pack boundary; T5 now cross-agent consistency |
| RF-8 autonomous mutation | CONFIRMED - no roadmap change required |

The rebuttal also produced a governance-learning candidate: future roadmap Gap
Statements that use "missing", "no X exists", or equivalent absence claims
should carry source search evidence or explicitly classify the current owner as
`PARTIAL_OWNER`. This roadmap records the candidate but does not add a checker;
that requires a separate control-plane hardening tranche.

## Acceptance Criteria For Roadmap Approval

1. The roadmap keeps foundation memory behavior separate from Policy_Local.
2. It maps current owner surfaces without claiming a full existing workflow
   chain.
3. It defines a bounded chain from signal intake to consolidation, retrieval,
   and pruning.
4. It includes temporal normalization as a required control.
5. It includes operator-visible memory review.
6. It blocks raw memory release and hidden-memory authority.
7. It requires fresh GC-018 and a source-verified work order before build.
8. It leaves implementation, storage, provider calls, and Policy_Local changes
   unauthorized.

## Verification / Evidence

Planning evidence is bounded to source-visible CVF artifacts and the
operator-provided design signal.

Commands used during roadmap authoring:

```text
python governance\compat\check_active_session_state.py --enforce
rg -n "CONTROLLED_MEMORY_GATEWAY_PHASE2_VERSION|MemoryGatewayOperation|MemoryGatewayRequest|rawMemoryReleased|evaluateMemoryGatewayRequest|global_memory_scope_not_authorized|memory_reinjection_not_authorized" EXTENSIONS\CVF_LEARNING_PLANE_FOUNDATION\src\controlled-memory-gateway.ts
rg -n "MEMORY_RETRIEVAL_POLICY_VERSION|MemoryRetrievalCandidate|lifecycleState|BLOCKED_STATES|rawMemoryReleased|evaluateRetrievalRequest" EXTENSIONS\CVF_LEARNING_PLANE_FOUNDATION\src\memory-retrieval-policy.ts
rg -n "W7MemoryRecord|contradiction_flag|KnowledgeMaintenance|staleness|drift|orphan|lint" EXTENSIONS\CVF_CONTROL_PLANE_FOUNDATION\src\w7.memory.record.contract.ts EXTENSIONS\CVF_CONTROL_PLANE_FOUNDATION\src\knowledge.maintenance.contract.ts
rg -n "Repository truth outranks chat memory|Hidden memory must not become authority|checkpoint|artifact memory|reinjection" docs\reference\CVF_AGENT_CONTINUITY_AND_DELEGATION_DOCTRINE_2026-05-07.md
rg -n "LearningSignalLane|LearningSignalIntakeInput|LearningSignalIntakeRecord|cvf.learningSignalIntakeBridge" EXTENSIONS\CVF_LEARNING_PLANE_FOUNDATION\src\learning-signal-intake-bridge.ts
rg -n "MemoryLifecycleState|evaluateLifecycleTransition|unreinforced_memory_expired|expired" EXTENSIONS\CVF_LEARNING_PLANE_FOUNDATION\src\memory-lifecycle-policy.ts
rg -n "MemoryTier|persistenceClass|ephemeral|bounded|durable|append_only" EXTENSIONS\CVF_LEARNING_PLANE_FOUNDATION\src\memory-tier-classifier.contract.ts
rg -n "memoryRuntimeWorkflowChain|runMemoryRuntimeWorkflowChain|MemoryRuntimeWorkflowStatus|rawMemoryReleased|packaged|denied|deferred" EXTENSIONS\CVF_LEARNING_PLANE_FOUNDATION\src\memory-runtime-workflow-chain.ts
```

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: operator provided a memory consolidation learning signal.
- DESIGN: this roadmap proposes the workflow chain and boundaries.
- SPEC: MEMCON-T1a must create the canonical standard and owner
  reconciliation map; MEMCON-T1b must create the schema.
- WORK ORDER: each tranche requires fresh GC-018 and source verification.
- BUILD: no build is authorized by this roadmap alone.
- REVIEW: Claude rebuttal is requested before dispatch.
- FREEZE: only closed foundation artifacts may feed Policy_Local PL-S1.

## Latest Closed Tranche Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_FOR_CLAUDE_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return artifact | `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_WORKER_RETURN_2026-06-13.md` | `WORKER_MUST_NOT_COMMIT observed` | PASS |
| Roadmap state | this file | `Status: MEMCON_T3_CLOSED_PASS_BOUNDED` | PASS |
| Contract artifact | `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | file exists | PASS |
| Sample packet artifact | `docs/reviews/CVF_MEMCON_T3_OPERATOR_MEMORY_REVIEW_PACKET_SAMPLE_2026-06-13.md` | file exists | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry update authorized for MEMCON-T3 closure | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry update authorized for MEMCON-T3 closure | BLOCKED with reason |
| External evidence digest | N/A with reason | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop mutation authorized | N/A with reason |
| Session continuity | active state and handoff | Codex-owned session-sync commit follows material closure | N/A with reason - separate sync commit follows |

## Claim Boundary

This roadmap proposes a Memory Plane consolidation workflow chain. It does not
claim that CVF already has full long-term teammate memory, cross-agent memory
consistency, operator UI, production memory storage, vector retrieval, memory
quality parity, autonomous memory mutation, Policy_Local readiness, public
readiness, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation planning. No public-sync is authorized.

