# CVF GC-018 - CI1-T2 Graphify Legacy Rescan Pilot

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `662b673b`

## Purpose

Authorize CI1-T2 as the first bounded legacy rescan pilot using the
CI1-T1 readiness packet template. The pilot corpus is the Graphify
knowledge-graph family at
`.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`
(5 files, confirmed by filesystem listing prior to this GC-018).

CI1-T2 applies the full CI1-T1 packet template to this corpus: corpus
boundary, filesystem discovery, GC-047 completeness block, GC-048
knowledge-map reconciliation block, corpus search/filter readiness block,
GC-050 classification block, negative search evidence, derived trace,
query receipt model, adversarial sampling, and disposition matrix.

## Source

Predecessor evidence:

- CI1 parent GC-018: `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md` — authorized CI1 planning and T1 dispatch
- CI1-T1 completion: `docs/reviews/CVF_CI1_T1_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_COMPLETION_2026-06-02.md` — packet template CLOSED_PASS_BOUNDED at `662b673b`
- CI1 roadmap: `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` — CI1-T2 designated as Graphify pilot
- Graphify filesystem evidence: `ls .private_reference/legacy/CVF_Important/Knowledge\ Base_Graphify/` — 5 files confirmed before this GC-018

## Decision

Authority:

- operator direction on 2026-06-02 to run CI1-T2 on the Graphify corpus;
- CI1 parent GC-018:
  `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md`;
- CI1-T1 template completed and committed at `662b673b`:
  `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`;
- CI1 roadmap tranche plan designating Graphify as preferred T2 pilot:
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  row CI1-T2.

Decision: proceed with CI1-T2. The Graphify corpus is small (5 files),
well-scoped, and already partially referenced in KGR1. It is the ideal
first pilot for the new readiness packet workflow.

## Scope / Target / Owner Boundary

Corpus target: `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`

Known files at dispatch (confirmed by `ls` before GC-018):

| File | Status |
| --- | --- |
| `CVF_GRAPHIFY_CLI_COMMAND_SPEC.md` | IN_SCOPE |
| `CVF_GRAPH_MEMORY_DATA_MODEL.md` | IN_SCOPE |
| `CVF_GRAPH_MEMORY_GUARD_SPEC.md` | IN_SCOPE |
| `CVF_GRAPH_MEMORY_LAYER_SPEC.md` | IN_SCOPE |
| `Thong_tin.md` | IN_SCOPE (language/info file — read and classify) |

Total in-scope files: 5

CVF owns:

- readiness packet evidence (GC-047, GC-048, search/filter, GC-050);
- corpus boundary documentation;
- disposition matrix;
- completion review.

Worker owns:

- reading all 5 files;
- filling every section of the CI1-T1 template;
- running required gates.

Out of scope:

- files outside `Knowledge Base_Graphify/`;
- runtime indexing, vector embedding, or LPCI product implementation;
- public-sync, push, or commit;
- production readiness or semantic correctness claims.

## Claim Boundary

CI1-T2 claims bounded corpus intelligence readiness evidence for the
Graphify corpus family only. It does not claim:

- runtime retrieval quality;
- LPCI implementation;
- production, hosted, or public readiness;
- any other legacy family.

## Risk Register

| Risk | Control |
| --- | --- |
| Worker reads partial corpus | GC-047 requires filesystem-backed manifest with all 5 files READ |
| Worker makes semantic correctness claim | GC-050 classification verdict must not claim semantic proof |
| Worker imports files outside scope | Forbidden Path Manifest in work order blocks other legacy folders |
| Worker commits or pushes | Work order explicitly blocks commit/push |
| GC-047/048 blocks trigger on completion review | Worker must include N/A blocks with correct format (learned from CI1-T1) |

## Knowledge Absorption Blind-Spot Control Block

Standard read: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

- Source inventory:
  - Root: `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`
  - Shell command run: `ls ".private_reference/legacy/CVF_Important/Knowledge Base_Graphify/"`
  - Shell output (file list):

    ```text
    CVF_GRAPHIFY_CLI_COMMAND_SPEC.md
    CVF_GRAPH_MEMORY_DATA_MODEL.md
    CVF_GRAPH_MEMORY_GUARD_SPEC.md
    CVF_GRAPH_MEMORY_LAYER_SPEC.md
    Thong_tin.md
    ```

  - Total file count (from shell): 5

- Prior absorption evidence resolved:
  - KGR1 GC-018: `docs/baselines/CVF_GC018_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_WAVE1_2026-06-01.md` — KGR1 absorbed graph-retrieval concepts from this family; `knowledge-graph-builder.ts` + `knowledge-graph-store.ts` delivered
  - KGR1 local review: `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` — bounded local tests + T5 live provider proof PASS
  - LHW-RESCAN-A: `docs/reviews/CVF_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md` — `CVF_Important/` scanned as 24-folder, 230-file corpus; Graphify family listed as `Knowledge Base_Graphify`

- Detailed source files used (at dispatch — worker reads all):
  - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPHIFY_CLI_COMMAND_SPEC.md` — not yet read at GC-018 authoring; to be read by worker
  - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_DATA_MODEL.md` — not yet read at GC-018 authoring; to be read by worker
  - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_GUARD_SPEC.md` — not yet read at GC-018 authoring; to be read by worker
  - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_LAYER_SPEC.md` — not yet read at GC-018 authoring; to be read by worker
  - `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/Thong_tin.md` — not yet read at GC-018 authoring; to be read by worker

- Source families skipped:
  - All other `CVF_Important/` subfolders — out of CI1-T2 scope; separate tranches required

- File-level accepted value (at GC-018 level — detail deferred to worker packet):
  - Graphify family covers: graph memory data model, CLI command spec, memory guard spec, layer architecture, and info file
  - KGR1 already absorbed core graph-retrieval patterns into `knowledge-graph-builder.ts` and `knowledge-graph-store.ts`
  - CI1-T2 focuses on corpus intelligence readiness classification, not re-implementing KGR1 output

- Owner-surface normalization:
  - Graph memory concepts → KGR1 LPF owner surfaces (`knowledge-graph-builder.ts`, `knowledge-graph-store.ts`) — already delivered
  - Readiness classification output → `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` — new documentation artifact, no runtime mutation

- Accept/defer/reject matrix:
  - CVF_GRAPHIFY_CLI_COMMAND_SPEC.md → DEFER to worker for full classification; KGR1 CLI patterns partially absorbed
  - CVF_GRAPH_MEMORY_DATA_MODEL.md → DEFER to worker; core data model absorbed into KGR1 LPF types
  - CVF_GRAPH_MEMORY_GUARD_SPEC.md → DEFER to worker; guard patterns not yet absorbed
  - CVF_GRAPH_MEMORY_LAYER_SPEC.md → DEFER to worker; layer architecture partially absorbed into KGR1
  - Thong_tin.md → DEFER to worker; likely metadata or language-context file

- Adversarial roles completed:
  - Implementer: Graphify corpus is small (5 files) and already partially absorbed via KGR1; CI1-T2 adds structured readiness classification without duplicating KGR1 work
  - Skeptic/Auditor: Risk that worker duplicates KGR1 implementation — mitigated by work order Forbidden Scope (no runtime TypeScript changes) and bounded documentation-only output
  - Product/Operator Advocate: Readiness packet gives CVF structured evidence for future retrieval readiness claims; Graphify is the right first pilot because KGR1 provides a comparison baseline
  - Safety/Boundary Owner: No raw Memory release, no prompt injection, no autonomous mutation; worker output is documentation only; N/A for safety-critical boundary

- Thin proof target:
  - Worker produces filled CI1-T1 packet (`docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`) with GC-047 `COMPLETE_VERIFIED` (all 5 files READ), GC-048 reconciliation, GC-050 ledger, and ≥5 adversarial sampling rows — no runtime execution required

- Gate 7 completeness cross-check:

  | Subfolder / file | In source inventory? | Disposition if absent | Reason |
  | --- | --- | --- | --- |
  | `CVF_GRAPHIFY_CLI_COMMAND_SPEC.md` | YES — listed in shell output | READ by worker | In-scope |
  | `CVF_GRAPH_MEMORY_DATA_MODEL.md` | YES — listed in shell output | READ by worker | In-scope |
  | `CVF_GRAPH_MEMORY_GUARD_SPEC.md` | YES — listed in shell output | READ by worker | In-scope |
  | `CVF_GRAPH_MEMORY_LAYER_SPEC.md` | YES — listed in shell output | READ by worker | In-scope |
  | `Thong_tin.md` | YES — listed in shell output | READ by worker | In-scope — classify even if metadata |
  | Other `CVF_Important/` subfolders | NO — out of scope | SKIPPED | Separate tranches |

- Blind-spot verdict: CLEAR

  Rationale: all 5 files are identified from filesystem, prior absorption via KGR1 is documented, no runtime implementation is authorized, and the worker must read all files before claiming classification. No undispositioned rows in Gate 7 cross-check.

## Evidence

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base 662b673b --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 662b673b --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 662b673b --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 662b673b --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 662b673b --head HEAD --enforce
python governance/compat/check_core_guard_self_protection.py --enforce
python governance/compat/check_forbidden_filesystem_state.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 662b673b --head HEAD
```

## Corpus Completeness And Report Integrity

This GC-018 is a dispatch authorization document. It does not scan the
corpus — the worker executes CI1-T2 and produces the filled packet. This
block is required because the GC-018 references the Graphify corpus path.

- Corpus task class: GC018_DISPATCH_AUTHORIZATION
- Corpus root: `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` (scoped to worker; not scanned at GC-018 authoring)
- Snapshot time: 2026-06-02 — filesystem confirmed by `ls` before GC-018 creation
- Enumeration command: `ls ".private_reference/legacy/CVF_Important/Knowledge Base_Graphify/"` (at GC-018 authoring; worker must run `rg --files --hidden --no-ignore` for GC-047 evidence)
- Manifest artifact or inline manifest: N/A — no manifest produced at GC-018 level; worker produces manifest in readiness packet
- Manifest hash: N/A — deferred to worker packet
- Processing ledger artifact or inline ledger: N/A — deferred to worker packet
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=0 ledger_terminal=0 exclusions=0 unresolved=0 (GC-018 level only; all counts zero — worker produces real values)
- Unresolved files: 0 (at GC-018 level; worker resolves all 5 to READ)
- Declared exclusions: none at GC-018 level
- Unreadable or unsupported files: none known at GC-018 level
- Aggregation check: N/A — deferred to worker packet
- Drift check: N/A — deferred to worker packet
- Output traceability: `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` (worker produces)
- Adversarial verification: N/A at GC-018 level — worker produces adversarial sampling in packet
- Corpus verdict: PARTIAL

Reason for PARTIAL: GC-018 is a dispatch authorization, not a corpus scan. PARTIAL records that the block is present as required by the guard but actual corpus processing is deferred to the worker. No corpus completeness claim is made at GC-018 level.

## Knowledge System Reconciliation

This GC-018 does not produce a knowledge map. This block is required because
the document references knowledge graph and corpus intelligence content.

- Knowledge task class: GC018_DISPATCH_AUTHORIZATION
- Source manifest: N/A — deferred to worker packet
- Source manifest hash: N/A — deferred to worker packet
- Enumeration safety: N/A at GC-018 level — worker must use `rg --files --hidden --no-ignore`
- Intake registry or ledger: N/A — deferred to worker packet
- Authority assets: 0 at GC-018 level (5 known files not yet read)
- Derived views: 0 — no knowledge map produced at GC-018 level
- Semantic region ledger: N/A — deferred to worker packet
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0 (GC-018 level only)
- Orphan or unmapped assets: 0 at GC-018 level
- Cross-region links: N/A
- Drift check: N/A — no prior map at GC-018 level
- Rebuildability check: N/A — no derived views produced at GC-018 level
- Retrieval boundary: N/A — no retrieval claims made at GC-018 level
- Adversarial verification: N/A at GC-018 level
- Knowledge-map verdict: PARTIAL

Reason for PARTIAL: GC-018 is dispatch authorization only. PARTIAL records that this block is present as required by the guard but no actual knowledge map was produced. Worker produces the real reconciliation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T2 reads private legacy corpus at
`.private_reference/legacy/`. No public-sync remote, public repository
commit, public artifact path, hosted proof, or public README claim.
