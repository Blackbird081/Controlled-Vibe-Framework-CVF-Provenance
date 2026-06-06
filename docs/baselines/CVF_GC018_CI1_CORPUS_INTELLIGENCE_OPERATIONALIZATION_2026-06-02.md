# CVF GC-018 - CI1 Corpus Intelligence Operationalization

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_PLANNING_AND_T1_DISPATCH

docType: baseline

Date: 2026-06-02

## Purpose

Authorize CI1 as the next bounded corpus-intelligence tranche after Memory
plane closure. CI1 turns the new corpus standards into a repeatable operating
workflow before CVF resumes broad legacy rescans or starts the LPCI product
implementation.

## Scope / Target / Owner Boundary

Target owner surfaces:

- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
- `governance/toolkit/05_OPERATION/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_GUARD.md`
- `governance/toolkit/05_OPERATION/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_GUARD.md`

Boundary: CI1 authorizes planning and the first documentation/template tranche.
It does not authorize broad legacy scanning, runtime indexing, vector database
implementation, LPCI product implementation, public-sync, production readiness,
or semantic correctness claims.

## Decision

Proceed with CI1-T1 first: create a reusable Corpus Intelligence Readiness
Packet template and dispatch rules that combine GC-047, GC-048, CVF corpus
search/filter readiness, and GC-050.

Do not start broad legacy rescans until CI1-T1 is complete and reviewed.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Corpus completeness evidence | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | ACCEPT_AS_SOURCE_POLICY |
| Knowledge-map reconciliation | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | ACCEPT_AS_SOURCE_POLICY |
| Search/filter readiness | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACCEPT_AS_SOURCE_POLICY |
| Intelligence classification | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT_AS_SOURCE_POLICY |
| Local hook/autorun enforcement | `governance/compat/run_local_governance_hook_chain.py`, `governance/compat/run_agent_autorun_workflow_gate.py` | ACCEPT_AS_GATE_SURFACE |

## Source / Predecessor Evidence

- `docs/reviews/CVF_MKE1_MEMORY_ENFORCEMENT_COMPLETION_2026-06-02.md`
- `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md`
- `docs/roadmaps/CVF_MKE1_MEMORY_ENFORCEMENT_ROADMAP_2026-06-01.md`
- `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`
- `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md`
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

CI1-T1 is template/dispatch work only. It reads existing standards and guard
docs; it does not scan `.private_reference/legacy/` or any external corpus.

### Gate 2 - Prior Absorption Resolution

Memory plane is closed bounded. KGR1, MKE1, and MKG7 are
`CLOSED_PASS_BOUNDED`. CI1 builds on those closed boundaries and does not reopen
Memory implementation.

### Gate 3 - File-Level Value Extraction

CI1 extracts operating requirements from GC-047, GC-048, corpus search/filter
readiness, and GC-050 into a single readiness packet template.

### Gate 4 - Owner-Surface Normalization

Corpus search/filter readiness belongs to CVF-wide corpus intelligence, not
only to LPCI. LPCI is a downstream product consumer.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| CI1-T1 readiness packet template | ACCEPT_NOW | needed before broad corpus rescans |
| Legacy Graphify deep rescan | DEFER | wait until T1 template exists |
| LPCI implementation | DEFER | product work starts after corpus workflow is stable |
| Structural checker for search/filter readiness | DEFER | add only after T1/T2 show repeated structural defects |

### Gate 6 - Adversarial Role Review

Risk: CI1 becomes another document-only layer that does not change worker
behavior. Control: T1 output must include dispatch wording, required evidence,
acceptance criteria, and gate commands that future workers can execute.

### Gate 7 - Thin Proof And Closure Delta

T1 closes only when the packet template and work order pass markdown,
dispatch-quality, and corpus-intelligence structural gates.

Blind-spot verdict: CLEAR_FOR_T1_TEMPLATE_DISPATCH.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| GC-047 checker exists | `governance/compat/check_corpus_completeness_report_integrity.py` | `def main` | `main` | corpus completeness checker | ACCEPT |
| GC-048 checker exists | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | `def main` | `main` | corpus map checker | ACCEPT |
| GC-050 checker exists | `governance/compat/check_corpus_intelligence_classification.py` | `def main` | `main` | corpus classification checker | ACCEPT |
| Search/filter standard exists | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | standard file | `Corpus Search And Filter Readiness` | corpus intelligence standard | ACCEPT |

## Required Evidence

- `python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_corpus_intelligence_classification.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_core_guard_self_protection.py --enforce`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1 is private provenance planning and dispatch work. No public-sync
remote, public repository commit, public artifact path, hosted proof, or public
README claim is included.

## Claim Boundary

CI1 authorizes a bounded corpus-intelligence operating workflow. It does not
claim semantic correctness, completed legacy absorption, LPCI product delivery,
runtime retrieval quality, production readiness, or public readiness.
