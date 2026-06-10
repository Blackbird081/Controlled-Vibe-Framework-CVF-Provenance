# CVF Work Order: MLW0 Current Source Verification Map

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-05

dispatchBaseHead: `a1a93ed4`

executionBaseHead: `681a87ad`

closureBaseHead: `681a87ad`

Commit mode: CODEX_MULTI_ROLE_CLOSEOUT

## Purpose

Map legacy memory/learning concept vocabulary surfaced in CI1-T11 scan packets
to current CVF runtime source files, schemas, routes, and tests. This work order
produces the Source Verification Map that every subsequent MLW1–MLW8 tranche
must cite as its symbol authority before any runtime implementation begins.

## Authority Chain

| Role | Agent/Source | Evidence |
| --- | --- | --- |
| Operator | Operator instruction 2026-06-05 | selected option A: open MLW0 |
| GC-018 | `docs/baselines/CVF_GC018_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | AUTHORIZED_DISPATCH_PACKET |
| Roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | `MLW0: Current Source Verification Map` tranche entry |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Roadmap source row | Work order fulfillment | Disposition |
| --- | --- | --- | --- |
| MLW0 must produce current owner-surface map | `Tranche Plan` row MLW0: "current owner-surface map" | Phase 1 Current Owner Surface Table | ACCEPT |
| MLW0 must produce accepted/rejected legacy-to-current symbol table | `Tranche Plan` row MLW0: "accepted/rejected legacy-to-current symbol table" | Phase 2+3 Legacy Concept Verification Table | ACCEPT |
| MLW0 must produce exact runtime paths, doc paths, schema paths, and tests/checkers | `Tranche Plan` row MLW0: "exact runtime paths … and tests" | Phase 3 Evidence Trace Block per concept | ACCEPT |
| MLW0 must produce blocked fields with corrected names or explicit no-source-found disposition | `Tranche Plan` row MLW0: "blocked fields … no-source-found" | BLOCKED rows in Verification Table | ACCEPT |
| MLW0 must produce tranche dependency order for MLW1–MLW8 | `Tranche Plan` row MLW0: "tranche dependency order for MLW1–MLW8" | Phase 4 Tranche Dependency Update section | ACCEPT |
| Non-negotiable: no runtime file modified | `Non-Negotiable Boundaries` | Forbidden scope; no `.ts`/`.py` writes | ACCEPT |
| Non-negotiable: no public claim | `Non-Negotiable Boundaries` | Public Export Disposition: DEFERRED_PRIVATE_ONLY | ACCEPT |
| Exit criteria for MLW0 | `Dependency Order` item 1 | Closure Checklist | ACCEPT |

## Agent Roles

| Role | Assignment |
| --- | --- |
| Worker | Codex — source analysis, map document authoring, worker handoff packet |
| Reviewer/Closer | Codex — authors completion review, verifies map completeness, passes gates, commits |
| Orchestrator | Codex — updates closure continuity; operator authorizes next tranche |

## Worker Autonomy / No-Question Rule

The worker completes all allowed-scope remediation without escalating to the
operator. If a governance gate fails on files inside the allowed write paths,
the worker must repair and rerun the gate. Operator escalation is required only
for scope expansion, claim-boundary changes, HOLD release, risk-level changes,
public-sync, live/provider proof, secrets/quota, forbidden paths, or destructive
operations.

## Scope

Allowed scope:

- Reading current runtime source files to verify symbol existence.
- Reading current schema, route, and test files.
- Producing one Source Verification Map document classifying legacy concepts as
  ACCEPT, ACCEPT_RENAMED, REJECT, or BLOCKED.
- Authoring a completion review.
- Updating this MLW0 work order with closeout status and checklist results.
- Updating GC-051 corpus scan registry with the MLW0 source-verification
  cross-reference scan entry.
- Updating session state and front door with MLW0 closure.

Allowed write paths:

- `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md`
- `docs/reviews/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_COMPLETION_2026-06-05.md`
- `docs/work_orders/CVF_WO_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden scope:

- Modifying any runtime source file (`.ts`, `.py`, route files, test files).
- Creating new runtime modules, routes, schemas, or checkers.
- Claiming runtime behavior, live governance proof, public readiness,
  production readiness, or hosted readiness.
- Opening MLW1–MLW8 work orders without operator authorization.
- Public-sync or push.
- Autonomous memory, learning, policy, provider, or prompt mutation.

## Required First Reads

Before execution, worker must read:

1. `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` — tranche plan and non-negotiable boundaries
2. `docs/audits/CVF_CI1_T11A_LEARNING_PLANE_DEEP_SCAN_PACKET_2026-06-05.md` — Learning Plane concept inventory
3. `docs/audits/CVF_CI1_T11B_MEMORY_KNOWLEDGE_STORE_DEEP_SCAN_PACKET_2026-06-05.md` — memory/knowledge concept inventory
4. `docs/audits/CVF_CI1_T11C_RAG_CONTEXT_CONTROL_DEEP_SCAN_PACKET_2026-06-05.md` — RAG/context concept inventory
5. `docs/audits/CVF_CI1_T11D_EXECUTION_AUDIT_LEARNING_DEEP_SCAN_PACKET_2026-06-05.md` — execution/audit concept inventory

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| LPF memory runtime exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | MKG7 completion review | `memory-runtime-workflow-chain.ts` | LPF memory plane | ACCEPT |
| memory-lifecycle-policy exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | MKG7 completion review | `memory-lifecycle-policy.ts` | LPF lifecycle policy | ACCEPT |
| durable-memory-store exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | MKG7 completion review | `durable-memory-store.ts` | LPF durable store | ACCEPT |
| knowledge-graph-builder exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-builder.ts` | KGR1 completion review | `knowledge-graph-builder.ts` | KGR1 graph builder | ACCEPT |
| LearningSignalIntakeRecord exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | `docs/reference/archive/CVF_LEARNING_SIGNAL_INTAKE_BRIDGE_STANDARD_2026-05-29.md` | `LearningSignalIntakeRecord` | LPF intake bridge | ACCEPT |
| POST /api/memory/readout exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | MKG6 completion review (205L) | `readout/route.ts` | memory readout route | ACCEPT |
| POST /api/memory/write exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/write/route.ts` | MKG7 completion review | `write/route.ts` | memory write route | ACCEPT |
| W7MemoryRecord | T11A-D packets `docs/audits/CVF_CI1_T11B_MEMORY_KNOWLEDGE_STORE_DEEP_SCAN_PACKET_2026-06-05.md` | T11-F3 no-current-source finding | NOT_IN_CURRENT_SOURCE | legacy vocabulary only | BLOCKED_UNTIL_MAP |

## Write Ownership

Worker-owned paths (WORKER_MUST_NOT_COMMIT — hand off to reviewer):

| Owned path | Action | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | CREATE | source verification map document |

Reviewer-owned paths (authored by Reviewer/Closer after reviewing worker output):

| Owned path | Action | Notes |
| --- | --- | --- |
| `docs/reviews/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_COMPLETION_2026-06-05.md` | CREATE | completion review |

Runtime source, tests, checkers, routes, and schemas are forbidden writes for
this work order.

## Pre-Flight Checks

Before beginning execution, worker must confirm:

```powershell
# Confirm T11 scan packets exist
Test-Path "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\docs\audits\CVF_CI1_T11A_LEARNING_PLANE_DEEP_SCAN_PACKET_2026-06-05.md"
Test-Path "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\docs\audits\CVF_CI1_T11B_MEMORY_KNOWLEDGE_STORE_DEEP_SCAN_PACKET_2026-06-05.md"
Test-Path "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\docs\audits\CVF_CI1_T11C_RAG_CONTEXT_CONTROL_DEEP_SCAN_PACKET_2026-06-05.md"
Test-Path "d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF\docs\audits\CVF_CI1_T11D_EXECUTION_AUDIT_LEARNING_DEEP_SCAN_PACKET_2026-06-05.md"

# Confirm LPF source dir exists
rg --files --hidden --no-ignore EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/ | head -5
```

Both must pass. If T11 packets are missing, stop and surface as a blocker.

## Execution Plan

### Phase 1 — Enumerate current owner surface

Run `rg --files --hidden --no-ignore` on:

```text
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/
```

List all `.ts` files. Build Current Owner Surface Table.

### Phase 2 — Build legacy concept inventory from T11 packets

Read T11A–T11D packets and collect all legacy concept names:

- T11A: truth model, evaluation chain, reputation, adaptation, failure/simulation
  controls, LearningSignalIntakeRecord bridge references
- T11B: MemoryGateway, SharedKnowledgeSyncPolicy, MemoryAccessRecord,
  MemoryPacket, PrivacyFilter, DecayPolicy, KnowledgeCompilationLint,
  VaultReinjectionGate, MemoryLifecycle, MemoryProvenanceChain
- T11C: RAGRouter, ContextFusionPipeline, ContextProfile, CapabilityRegistry,
  ContextPackager, ContextBundleSchema, TokenBudget, CachePolicy,
  WorkflowContextWindow
- T11D: W7ArtifactRecord, W7TraceRecord, W7PlannerRecord, W7DecisionRecord,
  W7MemoryRecord, AgentLedger, SessionContinuityRecord, CheckpointRecord,
  RestoreRecord, AuditCouncilFeedback, TrustCalibrationRecord

### Phase 3 — Source-verify each concept

For each legacy concept, grep current source:

```powershell
rg -l "<concept>" EXTENSIONS/ docs/reference/ governance/compat/ --type ts --type py --type md
```

Classify result:

- **ACCEPT**: found with current symbol name at current path
- **ACCEPT_RENAMED**: found under different name (record both)
- **REJECT**: concept is actively contra-indicated by current CVF boundary
- **BLOCKED**: not found; legacy name only; no-source-found note required

### Phase 4 — Write Source Verification Map document

Target path: `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md`

Required sections:

1. Current Owner Surface Table (all LPF/MKG `.ts` files with region)
2. Legacy Concept Verification Table (all concepts, classification, evidence)
3. Tranche Dependency Update (for MLW1–MLW8: which concepts ACCEPT/BLOCKED/REJECT)
4. Finding-To-Governance Learning Disposition
5. Public Export Disposition: DEFERRED_PRIVATE_ONLY
6. Claim Boundary

Stop condition: if >30% of T11B/T11C/T11D concepts are BLOCKED, note this as a
gap finding (expected; does not block MLW0 closure; MLW1–MLW2 will author new
schemas).

### Phase 5 — Prepare worker handoff summary

Worker writes a concise handoff note in the source verification map document
(final section: `## Worker Handoff`) containing: row counts
(ACCEPT/ACCEPT_RENAMED/REJECT/BLOCKED), any stop-condition finding, gate
pre-check result, and boundary statement. The worker does NOT author the
completion review — that is the Reviewer/Closer's artifact.

## Evidence Requirements

Evidence Trace Block (required per significant claim in the map):

```text
Evidence Trace Block
- Claim: <exact legacy concept name>
- Command: rg -l "<concept>" EXTENSIONS/ --type ts
- Result: <file list or "no matches">
- Key path: <file:line if found, or "NOT_FOUND">
- Verdict: ACCEPT | ACCEPT_RENAMED | REJECT | BLOCKED
- Counter-evidence: none expected (source is ground truth)
```

## Acceptance Criteria

| Criterion | Required |
| --- | --- |
| Current Owner Surface Table present | YES |
| Legacy concept table present with 0 unclassified rows | YES |
| Every ACCEPT row has current path + verified symbol | YES |
| Every BLOCKED row has explicit no-source-found note | YES |
| Tranche Dependency Update present for MLW1–MLW8 | YES |
| Finding-To-Governance Learning Disposition present | YES |
| Public Export Disposition present | YES |
| Pre-closure autorun gate PASS | YES |
| No runtime file modified | YES |

## Review Gate

The reviewer must verify:

1. Legacy concept table is complete — no T11A–T11D concept rows missing.
2. ACCEPT rows have source-backed evidence (path + symbol or section).
3. BLOCKED rows have explicit no-source-found notation (not silence).
4. Pre-closure gate passed with no suppressed failures.
5. No runtime file was modified (`git diff --name-only` shows only new docs).
6. Completion review matches map content.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_WO_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | status `CLOSED_PASS_BOUNDED`; checklist resolved | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_COMPLETION_2026-06-05.md` | completion review created and aligned to source map | PASS |
| Roadmap state | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | MLW0 prerequisite fulfilled; MLW1/MLW2 remain fresh-authorization work | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `mlw0-current-source-verification-map` entry added | PASS |
| Registry Markdown | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | GC-051 registry standard remains the governing markdown registry surface | PASS |
| External evidence digest | N/A | N/A with reason - repo-local source verification only | N/A with reason |
| System loop interlock | N/A | N/A with reason - no runtime workflow/checker interlock added | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V15_2026-05-29.md` | MLW0 closure continuity updated | PASS |

## Closure Checklist

- [x] Source Verification Map document exists at target path
- [x] Completion review exists at target path
- [x] All legacy concept rows classified (0 unclassified)
- [x] Pre-closure autorun gate PASS
- [x] No runtime file modified
- [x] Session state updated with MLW0 closure
- [x] Front door updated with MLW0 closure and next allowed move

## Return-To-Orchestrator Conditions

Return to orchestrator when:

- All checklist items above are checked; OR
- A stop condition is encountered (missing T11 packet, unreadable source dir,
  >50% BLOCKED with unexpected pattern suggesting source restructure).

Return to operator when:

- Scope expansion is needed (MLW1+ work orders).
- A source symbol conflict is found that requires operator decision on naming.
- Pre-closure gate fails on a file outside allowed write paths.

## Operator Checkpoint

| Checkpoint | Required before | Decision |
| --- | --- | --- |
| Review MLW0 map completeness | opening MLW1 work order | operator reviews BLOCKED count and decides whether MLW1 must author new schemas first |
| Authorize MLW1–MLW2 | MLW1 runtime implementation | operator confirms durable memory backend choice (local file / SQLite / Postgres / Redis / adapter-only) |
| Authorize autonomous learning | any self-mutation design | default is reject; explicit operator authorization required |

operator.checkpoint.waiver: none — all three checkpoints are mandatory.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Legacy W7 field names unverified until source map | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | MLW0 closes this gap; MLW1+ must cite map |
| MLW1-MLW8 implementation blocked without map | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | MLW0 source map is mandatory prerequisite |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MLW0 reads current private runtime source and private legacy concepts.
No public-sync artifact is produced.

## Claim Boundary

This work order authorizes source-analysis documentation only. It does not
authorize runtime implementation, route changes, schema changes, test creation,
live governance proof, public-sync, hosted readiness, production readiness,
public readiness, or autonomous mutation.
