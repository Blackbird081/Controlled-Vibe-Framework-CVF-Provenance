# CVF GC-018 — LHW13 Workflow Connector Wave 13

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize LHW13 Workflow Connector Wave 13: three documentation-only connector
specs closing governance-protocol and boundary-definition gaps from CVF 25.05
Gop_y.md audit. LHW13 addresses agent reading protocol normalization, memory
continuity level advisory, and graph context resolver boundary — all doc-only
gaps requiring no runtime code change.

---

## Scope

Three documentation-only connector specs:

- T1 — Agent Reading Protocol Governance Connector
- T2 — Memory Continuity Level Advisory Connector
- T3 — Graph Context Resolver Boundary Connector

No `.ts` / `.tsx` / `.js` / `.py` file change. No `EXTENSIONS/` source file
change. No receipt envelope schema change. No public-sync repo change.

---

## Source / Predecessor Evidence

- LHW12 GC-018:
  `docs/baselines/CVF_GC018_LHW12_WORKFLOW_CONNECTOR_WAVE12_2026-05-29.md`
  — Status: ACTIVE; LHW12 open (T1 WORK_ORDER_READY)
- LHW11 roadmap:
  `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- CVF 25.05 Gop_y.md review:
  `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 1 (Agent Reading Protocol), GAP 4 (Memory L0-L3 boundary),
    GAP 9 (Graph context resolver)
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Source surfaces at HEAD `7de75901`:

| Surface | File | Key symbol |
| --- | --- | --- |
| Session front door | `CVF_SESSION_MEMORY.md` | read-order anchor |
| CLAUDE.md startup acknowledgment | `CLAUDE.md` | Mandatory Startup Acknowledgment section |
| `MemoryGatewayDecision.canReinject` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 49 — boolean field; not source proof of false |
| `MemoryGatewayDecision.rawMemoryReleased` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | line 50 — literal `rawMemoryReleased: false` |
| LHW8-T1 `memorySnapshotAdvisoryType` | `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md` | S3 field |
| LHW11-T3 `memoryContextSeedDecayAdvisoryType` | `docs/reference/CVF_LHW11_T3_MEMORY_CONTEXT_SEED_DECAY_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S3 field |
| AIF-B graph modules | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` | `GraphKnowledgeService` interface |
| LH1 `tolaria` trigger | `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 129 |

---

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Absorbed source families:

- CVF 25.05 Gop_y.md Gap 1 — agent reading protocol.
- CVF 25.05 Gop_y.md Gap 4 — memory L0-L3 boundary.
- CVF 25.05 Gop_y.md Gap 9 — graph context resolver boundary.
- LH1 `tolaria` partially absorbed trigger — memory snapshot / graph context
  readout value only.

Blind-spot controls:

- Source facts must prefer current runtime/source or canonical connector specs
  over handoff memory.
- Memory work must not claim reinjection, L2/L3 activation, or raw memory
  release.
- Graph work must not claim route wiring or graph retrieval execution.
- New advisory fields are doc-only planning fields, not runtime/source facts.

Blind-spot verdict: CLEAR for documentation-only connector specs; BLOCK if any
tranche requires runtime graph execution, memory reinjection, or agent behavior
enforcement.

## Decision / Baseline

LHW13 is authorized. Each tranche is documentation-only, binds surfaces already
in HEAD, adds no runtime authority, and extends no receipt envelope schema.

T2 is gated as `HOLD_UNTIL_T1_PASS`. T3 is gated as
`HOLD_UNTIL_T1_AND_T2_PASS`.

LHW13 may be dispatched in parallel with LHW12 — they share no source
dependencies. However, each tranche within LHW13 must still gate on prior
tranche CLOSED_PASS per standard wave rule.

---

## Required Evidence

Same per-tranche requirements as all LHW waves: spec (5 sections S1–S5);
Fast Lane audit; work order with Source Verification Table; completion review
with all required sections; both governance gates PASS; spec < 250 lines;
no code file in diff; session continuity updated.

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 7de75901 --head <lhw13-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 7de75901 --head <lhw13-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 7de75901 --head <lhw13-commit> --enforce
```

---

## Claim Boundary

LHW13 does not claim runtime agent protocol enforcement, memory reinjection,
graph-based context retrieval execution, MCP transport, tool execution, CLI
invocation, new role taxonomy, RBAC changes, receipt envelope extensions,
external skill ingestion, provider behavior changes, hosted readiness,
production readiness, or public release readiness.
