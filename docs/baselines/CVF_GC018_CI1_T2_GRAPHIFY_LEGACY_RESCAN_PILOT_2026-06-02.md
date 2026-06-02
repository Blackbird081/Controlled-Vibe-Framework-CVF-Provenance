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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T2 reads private legacy corpus at
`.private_reference/legacy/`. No public-sync remote, public repository
commit, public artifact path, hosted proof, or public README claim.
