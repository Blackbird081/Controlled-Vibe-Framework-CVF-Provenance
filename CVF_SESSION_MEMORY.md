# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-02

Current mode marker: `ci1_t4_closed_pass_bounded_t5_ready_for_gc018`
Enforcement posture: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It intentionally points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V15_2026-05-29.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `ci1_t4_closed_pass_bounded_t5_ready_for_gc018`.

Active handoff:

`AGENT_HANDOFF_V15_2026-05-29.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Owner Surface

Owner surface: CVF active session startup, continuity routing, and front-door
rule pointers for new or resumed agents.

## Protocol

Agents must treat this file as a compact pointer record, then resolve the
machine-readable registry, active review queue, active handoff, and required
startup guards before material governed work.

## Active Rule Additions

Blind-Spot Prevention Standard upgraded to v2 (2026-06-01). Two new
machine-verifiable rules added based on the LHW20 regression (24 subfolders /
230 files vs claimed 13 / 97):

- **Gate 1 — FILESYSTEM_LISTING_REQUIRED:** Agent MUST run
  `Get-ChildItem -Directory` (or equivalent) on the root folder and include
  raw shell output in Gate 1. Self-reported subfolder counts without shell
  output are not valid evidence; verdict is BLOCKED.
- **Gate 7 — COMPLETENESS_CROSS_CHECK:** Before claiming `CLEAR`, agent MUST
  produce a cross-check table: Gate 1 subfolder list MINUS Gate 3 subfolder
  list = UNREAD set. Each unread subfolder must have an explicit disposition.
  CLEAR without this table is a governance defect.

Active standard: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

Fast Lane authorization: `docs/baselines/CVF_GC021_BLINDSPOT_STANDARD_UPGRADE_2026-06-01.md`

All future LHW absorption scans must reference the 2026-06-01 version.

Corpus Completeness And Report Integrity is now the general control for any
folder/file-based inventory, report, extraction, comparison, audit, migration,
or knowledge-absorption task:

- Standard:
  `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- Guard:
  `governance/toolkit/05_OPERATION/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD.md`
- Checker:
  `governance/compat/check_corpus_completeness_report_integrity.py`

Before claiming completeness, agents must provide filesystem-backed manifest,
file-level processing ledger, reconciliation, explicit exclusions and
unreadable formats, aggregation check, drift check, traceability, adversarial
verification, and an allowed corpus verdict. `COMPLETE_VERIFIED` requires zero
unresolved files. The guard proves evidence discipline, not perfect semantic
understanding.

Corpus-To-Knowledge-Map Reconciliation is now the follow-on control for
corpus-derived knowledge maps, semantic-region ledgers, architecture
reconciliations, Memory syntheses, graphification plans, and
retrieval-readiness claims:

- Method:
  `docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md`
- Standard:
  `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
- Guard:
  `governance/toolkit/05_OPERATION/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_GUARD.md`
- Checker:
  `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`

GC-048 distinguishes source authority from rebuildable graph, semantic-region,
Palace, summary, cache, snapshot, and retrieval views. It requires
mapped/deferred/unmapped reconciliation, drift and rebuildability checks,
retrieval boundaries, and adversarial verification.

Work-order dispatch quality is machine-enforced by:

`governance/compat/check_work_order_dispatch_quality.py`

Worker autonomy dispatch prompting is now standardized:

`docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`

READY/DISPATCHED work orders must include a Worker Autonomy / No-Question Rule
so routine allowed-scope remediation is not escalated to the operator as a
preference question.

Governed file-size maintainability now requires proactive rotation/splitting
instead of last-minute text compression when active governed files approach
hard thresholds.

This applies to broad external knowledge absorption records, session front
doors, handoffs, reviews, work orders, and other blocked work classes that
would become hard to test or review if oversized.

Redefine size guard:

`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`

Agent autorun workflow control is mandatory for governed work phases. Agents
must pass the phase wrapper before dispatch, implementation, closure, or push:

`governance/compat/run_agent_autorun_workflow_gate.py`

Canonical autorun standard:

`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Autorun gates are now range-aware. Governed closure must use a captured
`baseHead` and a non-empty committed range; `--base HEAD --head HEAD` is not
valid closure evidence for changed artifacts. Source Verification false
invariants require literal source proof or runtime-path proof.

Latest-closure continuity is now machine-enforced. When a connector wave is
closed, the active front door, state registry, and handoff must all reference
the latest closed LHW wave; stale lower-wave `nextAllowedMove` text blocks the
active-session gate.

Closure finality is now machine-enforced. Closed-equivalent governed artifacts
must not retain `| OPEN |` rows, unchecked `- [ ]` checklist items, stale
roadmap dispatch/hold residue, or Fast Lane active/pass status conflicts.

Status-token and Source Verification symbol hygiene are now machine-enforced:
`HOLD_*`, `DRAFT`, or `PROPOSED` statuses must not contain `CLOSED`, and
`Verified path or symbol` cells must contain only symbols only, not value
assignments such as `rawMemoryReleased: false`.

Allowed-scope and whole-wave range closure hygiene are now machine-enforced:
single-work-order closure ranges must not include files outside Allowed scope,
closed LHW wave roadmaps must be checked with a full T1/T2/T3 changed range,
and connector spec line-count claims must match the current file.

Agent-error learning philosophy is now canonical:

`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

Repeated agent mistakes are governance training samples, not merely worker
blame. Promote repeated defects from finding to written rule, from rule to
machine check, and from late machine check to the earliest applicable autorun
phase gate.

Allowed-scope gate remediation is now mandatory. If an autorun or machine guard
fails on files/artifacts inside the dispatched work order's Allowed scope, the
assigned agent must repair and rerun the gate instead of asking the non-coder
operator whether to perform routine cleanup. Operator escalation is reserved for
scope expansion, claim-boundary changes, `HOLD_*` release, risk changes,
public-sync, live/provider proof, secrets/quota, forbidden paths, or destructive
operations.

IDE-extension multi-provider execution logging is now machine-enforced:

`docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`

`governance/compat/check_multi_provider_execution_log.py`

Mixed-provider sessions using VS Code extension tabs, Antigravity, direct
provider scripts, CLI, MCP, or browser agents must record provider/model,
execution surface, role, evidence basis, commit range, direct-provider-proof
boundary, quality findings, cost attribution, and an Execution Attribution
Block that separates roadmap/order author, worker/executor, and reviewer/closer
when closing governed work or claiming provider effectiveness. Autorun and
local hook chains now fail missing or overclaimed multi-provider execution logs.

Finding-to-governance learning disposition is now machine-enforced:

`docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md`

`governance/compat/check_finding_to_governance_learning.py`

Changed logs, reviews, assessments, or audits that record findings or known
issues must classify each material finding into governance/control-plane,
runtime-behavior, provider-output, cost/economics, or documentation-only
learning lanes, with next control action.

Learning Signal Intake Bridge is now the typed Learning Plane intake route for
those learning lanes:

`docs/reference/CVF_LEARNING_SIGNAL_INTAKE_BRIDGE_STANDARD_2026-05-29.md`

`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`

Runtime/provider/cost candidates, phase-gate placement gaps, design-review
candidates, and machine-check candidates must normalize into
`LearningSignalIntakeRecord` / `LearningFeedbackInput` before a follow-up
roadmap claims Learning Plane routing. Autonomous mutation remains false unless
a separate governed roadmap authorizes it.

Public export disposition is now machine-enforced:

`docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md`

`governance/compat/check_public_export_disposition.py`

Changed closed roadmaps, final wave completion packets, and public catalog
claims must state whether the work is `EXPORTED`, `DEFERRED_PRIVATE_ONLY`, or
`BLOCKED_MISSING_PUBLIC_ARTIFACTS`. Private provenance closure does not imply
public-sync catalog export.

LHW scope rejection is not source rejection. For doc-only LHW connector waves,
families such as `abtop` or `gridex` that require live route execution must be
labeled `rejected from this LHW wave (doc-only scope) - requires live route;
eligible for separate live-proof roadmap post-LHW`, not globally rejected.
Finish absorption of remaining `PARTIALLY_ABSORBED` LH1 connector value before
opening separate live-proof roadmaps.

## Next Allowed Move

LHW24 is the latest closed LHW wave. LHW22-LHW24 agent-intelligence absorption
is CLOSED_PASS_BOUNDED at the documentation-only advisory boundary:

`docs/roadmaps/CVF_LHW22_LHW23_LHW24_AGENT_INTELLIGENCE_ROADMAP_2026-05-31.md`

Next allowed move: CPG-1, CPG-2, CPG-3, and CCG-1 are CLOSED_PASS_BOUNDED.
GC-048 Knowledge System foundation is `CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_GC048_CVF_KNOWLEDGE_SYSTEM_FOUNDATION_COMPLETION_2026-06-01.md`

Memory-method Legacy rescan audit remains `PARTIAL`:

`docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md`

`LHW-RESCAN-A` is `CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`

The current `CVF_Important/` source truth is `24` top-level folders and `230`
visible files: `229` parser-backed authority assets, one visible generated
`.pyc` exclusion, and zero unresolved ledger rows. Broad semantic-region
routing is rebuildable; deep interpretation remains explicitly open.

`LHW-RESCAN-B` is `CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`

The current bounded small-root truth is `38` visible files: `CVF 17.05=31`,
`CVF 25.05=2`, and `CVF 28.05=5`. All `38` text-like authority assets have
terminal `READ` status and broad semantic-region routing; exclusions and
unresolved rows are both zero. Deep interpretation remains explicitly open.

`LHW-RESCAN-C` is `CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`

The current partial-root truth is `341` visible files: `CVF ADD=167`,
`CVF 16.5=100`, and `CVF_Restructure=74`. All `341` authority assets have
terminal `READ` status, zero exclusions, zero unresolved rows, and broad
semantic-region routing across eight regions. Manifest hash:
`ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff`.

`MKG1` Memory/Knowledge/Graph Owner-Surface Review is `CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`

Result: `47/47` RESCAN-C `memory_knowledge_graph` assets reconciled; `26`
doc-only owner-surface mappings accepted; `21` runtime/bridge/skill/
implementation candidates deferred; zero unmapped assets. Manifest JSON:

`docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`

Manifest hash:
`ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff`.

`MKG2` Deferred Runtime Candidate Triage is `REVIEW_READY`:

- GC-018:
  `docs/baselines/CVF_GC018_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_2026-06-01.md`
- roadmap:
  `docs/roadmaps/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_ROADMAP_2026-06-01.md`
- dispatched work order:
  `docs/work_orders/CVF_WO_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_2026-06-01.md`

MKG2 worker review filed for audit:
`docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md`.
MKG3 Current Owner Negative Search Evidence is `REVIEW_READY_UNCOMMITTED`:

- GC-018:
  `docs/baselines/CVF_GC018_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_2026-06-01.md`
- roadmap:
  `docs/roadmaps/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_ROADMAP_2026-06-01.md`
- work order:
  `docs/work_orders/CVF_WO_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_2026-06-01.md`

Review:
  `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md`

MKG6 Memory Runtime Readout Route is `IMPLEMENTATION_REVIEW_READY`:

- GC-018:
  `docs/baselines/CVF_GC018_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md`
- roadmap:
  `docs/roadmaps/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_ROADMAP_2026-06-01.md`
- work order:
  `docs/work_orders/CVF_WO_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md`

Completion:
  `docs/reviews/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_COMPLETION_2026-06-01.md`

Result: bounded authenticated `POST /api/memory/readout` route, sanitized
summary-only Memory projection, LPF `./memory-runtime` export, focused route
and projection tests, and guard-backed Work-Order Fulfillment Manifest. Local
verification passed LPF focused tests 3/3, cvf-web focused tests 9/9, both
TypeScript checks, dispatch-quality, markdown structural, public-export,
finding-learning, execute-route sequence, governed file-size, and
pre-implementation autorun. Boundary remains private, uncommitted, no
live/provider proof, no prompt injection, no reinjection, no persistence/graph
mutation, no public-sync, no push.

Memory system tranche completion is `TRANCHE_REVIEW_READY`:

`docs/reviews/CVF_MKG_MEMORY_SYSTEM_TRANCHE_COMPLETION_2026-06-01.md`

WSR1 Workspace Public-Core Reconciliation is
`PUBLICATION_READY_PENDING_OPERATOR_COMMIT`:

- GC-018:
  `docs/baselines/CVF_GC018_WSR1_WORKSPACE_PUBLIC_CORE_RECONCILIATION_2026-06-01.md`
- roadmap:
  `docs/roadmaps/CVF_WSR1_WORKSPACE_PUBLIC_CORE_RECONCILIATION_ROADMAP_2026-06-01.md`
- completion:
  `docs/reviews/CVF_WSR1_WORKSPACE_PUBLIC_CORE_RECONCILIATION_COMPLETION_2026-06-01.md`

Local `CVF-Workspace` hidden core was migrated from unrelated `dc841d33`
history to fresh public `eb87479`; backup is preserved; `qt-saigon-works`
doctor is `PASS WITH NOTE (16 passed, 1 warning)`. The remaining warning is the
reviewed public workspace-kit overlay. Public-sync static CI gate is PASS after
README workspace onboarding, concise guard registry links, and public-surface
cleanup. Next allowed WSR1 move is operator review of the bounded public-sync
delta before commit or push.

CPG-2 is CLOSED_PASS_BOUNDED with
release-quality proof:

`docs/roadmaps/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_ROADMAP_2026-05-31.md`

`docs/work_orders/CVF_WO_CPG2_CP2_HARD_GATE_ENFORCEMENT_2026-05-31.md`

`docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md`

CPG-3 is CLOSED_PASS_BOUNDED with bounded receipt trace proof:

`docs/baselines/CVF_GC018_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`

`docs/roadmaps/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_ROADMAP_2026-05-31.md`

`docs/work_orders/CVF_WO_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_2026-05-31.md`

Boundary: do not edit `/api/execute/route.ts`; do not add public-sync,
provider-routing, raw prompt/output, secret, or framework-private memory
capture.

Completion:

`docs/reviews/CVF_CPG3_GOVERNANCE_TRACE_RECEIPT_ENRICHMENT_COMPLETION_2026-05-31.md`

Public-safe subset sync remains available only from the public-sync clone after
remote verification.

Memory plane is `CLOSED_PASS_BOUNDED` as a governed enforcement substrate:
MKG7, MKE1, and KGR1 are complete within their recorded boundaries.

CI1-T3 Graph Governance Corpus Deep Scan is `CLOSED_PASS_BOUNDED`
(`7c068eeb` + handoff-sync `b0d0249c`):

`docs/reviews/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_COMPLETION_2026-06-02.md`

GC-053 Work Order Commit Mode And Anchor Lifecycle Hardening is
`CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_GC053_WORK_ORDER_COMMIT_MODE_ANCHOR_LIFECYCLE_HARDENING_2026-06-02.md`

LHW24 remains the latest closed numbered LHW wave. CI1-T4 Cross-Corpus Index
Model is `CLOSED_PASS_BOUNDED`:

`docs/reviews/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md`

Next allowed move: open a fresh CI1-T5 GC-018 for the adversarial
classification sampling protocol over the T4 model. CI1-T6 checker decision
and CI1-T7 LPCI intake bridge remain locked until their direct prerequisites
close. LPCI chatbot runtime implementation remains blocked.

Parked checkpoints:

- VI5-T4/T5 hosted Netlify freshness and operator external-agent retest
- Delta production hardening for MCP/client memory direction

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
