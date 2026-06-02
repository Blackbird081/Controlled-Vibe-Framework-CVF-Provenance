# Finding Packet: legacy-cvf-important-graphify

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-02

## Purpose

Finding disposition packet for the CI1-T2 Graphify corpus scan. Records
F1–F4 findings and their dispositions for cross-agent discovery.

## Scope / Target / Owner Boundary

Target: future agents assigned graph-related tasks. Owner: CI1-T2 scan wave.

## Source / Predecessor Evidence

GC-018: `docs/baselines/CVF_GC018_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_2026-06-02.md`
Full packet: `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`

## Decision / Baseline

Findings F1–F4 are dispositioned. See individual sections below.

## Evidence / Verification

All 5 Graphify files read; GC-047 COMPLETE_VERIFIED; GC-048 RECONCILED_VERIFIED;
GC-050 CLASSIFIED_STRUCTURAL_PASS. Registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.

## Claim Boundary

Claims: finding disposition for CI1-T2 Graphify corpus.
Does not claim: full absorption; production readiness; semantic correctness.

Corpus: `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`

Scan wave: CI1-T2 | Date: 2026-06-02

Full evidence: `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`

---

## Learning Classification Summary

| Finding | Scan disposition | defectClass | learningLane | Action evidence |
| --- | --- | --- | --- | --- |
| F1 — KGR1 partial | ACCEPT_NO_ACTION | RULE_GAP | GOVERNANCE_CONTROL_PLANE | None — correct bounded scope |
| F2 — Guard spec absent | DEFER_WITH_ROADMAP | RULE_GAP | GOVERNANCE_CONTROL_PLANE | `f2gRef` → completion review; `roadmapRef` → graph guard tranche (pending) |
| F3 — CLI commands absent | DEFER_PHASED | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | `f2gRef` → completion review; `workOrderRef` → cvf graph query WO (pending) |
| F4 — Performance claim | ACCEPT_WITH_BOUNDARY | UNVERIFIED_CLAIM | DOCUMENTATION_ONLY_LEARNING | Boundary note in completion review; no roadmap |

F2G classification source: `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md#finding-to-governance-learning-disposition`

Registry machine record: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` → `legacy-cvf-important-graphify` → `findings[]`

---

## F1 — KGR1 Partial Absorption Confirmed

**Disposition:** ACCEPT_NO_ACTION | **defectClass:** RULE_GAP | **learningLane:** GOVERNANCE_CONTROL_PLANE

**What was found:** The Graphify data model (12 node types, 10 edge types,
4 CVF record types) was partially absorbed by KGR1 into `knowledge-graph-builder.ts`
and `knowledge-graph-store.ts`. The KGR1 implementation covers bounded graph
retrieval — it does not implement the full Graphify spec, which is correct scope.

**Evidence:** KGR1 GC-018 at `docs/baselines/CVF_GC018_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_WAVE1_2026-06-01.md`

**Next action:** None. KGR1 delivery is correct bounded scope. Over-implementing
the full Graphify spec would violate bounded tranche principle.

**Cross-reference for future agents:** When working on graph retrieval, knowledge
graph data model, or KGR1 extension — this finding confirms KGR1 is the correct
owner surface. Do not restart absorption from Graphify spec; extend KGR1.

---

## F2 — Guard Spec G-GM-01 through G-GM-08 Absent from CVF Runtime

**Disposition:** DEFER_WITH_ROADMAP | **defectClass:** RULE_GAP | **learningLane:** GOVERNANCE_CONTROL_PLANE

**What was found:** `CVF_GRAPH_MEMORY_GUARD_SPEC.md` defines 8 guard policies:

| Guard ID | Name | What it requires |
| --- | --- | --- |
| G-GM-01 | Graph Priority Guard | Use graph before grep/glob |
| G-GM-02 | No Bypass Guard | Prohibit bypassing graph |
| G-GM-03 | Provenance Guard | Mandatory source tracing |
| G-GM-04 | Integrity Guard | Graph data integrity |
| G-GM-05 | Access Control Guard | Access control |
| G-GM-06 | Confidentiality Guard | Data confidentiality |
| G-GM-07 | Drift Detection Guard | Detect graph drift |
| G-GM-08 | Compliance Guard | CVF compliance |

**Negative search:** `rg "G-GM-0" --include="*.ts"` across EXTENSIONS/ → 0 results.

**Why deferred:** Guard enforcement needs its own GC-018 + work order. The
PreToolUse hook pattern (G-GM-01/02) requires changes to agent settings behavior,
not CVF TypeScript. G-GM-03 through G-GM-08 map to existing CVF guard surfaces
but have not been wired to graph-specific inputs.

**Next action when operator authorizes:** Open separate governed tranche for
graph guard enforcement. G-GM-01 (graph priority before grep) is highest value
and maps to existing CPG-1 INT1 policy pattern.

**Cross-reference for future agents:** If assigned "implement graph guard" or
"enforce graph priority" — cite this finding. Do not rediscover as new gap.
Prior context: CPG-1/2/3 established the connection point guard pattern that
graph guards would extend.

---

## F3 — CLI `cvf graph` Commands Absent from Runtime

**Disposition:** DEFER_PHASED | **defectClass:** MACHINE_GATE_GAP | **learningLane:** GOVERNANCE_CONTROL_PLANE

**What was found:** `CVF_GRAPHIFY_CLI_COMMAND_SPEC.md` defines 8 CLI commands
(`cvf graph build`, `update`, `query`, `visualize`, `export`, `validate`,
`status`, `purge`). None exist in `command.registry.ts`.

**Negative search:** `rg "cvf graph" --include="*.ts"` in EXTENSIONS/ → 0 results.

**Priority order when implementing:**

1. `cvf graph query` — routes into KGR1 `evaluateRetrievalRequest()`; highest
   value; bounded implementation following WCE W1 `cvf workflow` pattern
2. `cvf graph status` — reads `KgrStore` state; low-risk
3. `cvf graph build` — requires full graph builder pipeline; more complex

**Next action when authorized:** Separate work order for `cvf graph query` CLI
command. Follows WCE W1 pattern: new module + register in `command.registry.ts`.
KGR1 runtime is already the backend.

**Cross-reference for future agents:** If assigned "add cvf graph CLI" — cite
this finding. Backend (KGR1) is ready. Frontend (CLI command) is missing.

---

## F4 — 71.5x Token Reduction Claim Unverified

**Disposition:** ACCEPT_WITH_BOUNDARY | **defectClass:** UNVERIFIED_CLAIM | **learningLane:** DOCUMENTATION_ONLY_LEARNING

**What was found:** `Thong_tin.md` (operator analysis file) cites 71.5x token
reduction per query compared to raw file scanning. This is the Graphify author's
published benchmark, not a CVF measurement.

**Boundary:** CVF does not repeat this claim in any documentation or catalog
without a CVF-run live proof. The claim may be true in some scenarios; it is
not independently verifiable from the spec files alone.

**Next action:** None currently. If a live proof of graph-vs-grep token efficiency
is desired, open a separate benchmarking tranche with explicit live proof setup.

---

## Relationship to CI1 Roadmap

| Finding | CI1 tranche that addresses it |
| --- | --- |
| F1 — KGR1 partial | CI1-T2 ✓ CLOSED — no further action |
| F2 — Guard spec absent | Post-CI1 — Graph Guard Enforcement Roadmap (separate) |
| F3 — CLI commands absent | Post-CI1 — Graph CLI Tranche (separate, after scan wave) |
| F4 — Token claim | Post-CI1 — Benchmarking tranche only if operator requests |

CI1-T3 next candidate: `CVF ADD/code-review-graph/` — 5 files directly related
to F2 (graph guard governance patterns).
