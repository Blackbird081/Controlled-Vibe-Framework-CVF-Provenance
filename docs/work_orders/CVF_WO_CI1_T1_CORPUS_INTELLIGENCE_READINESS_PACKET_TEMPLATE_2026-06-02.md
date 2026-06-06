# CVF Work Order - CI1-T1 Corpus Intelligence Readiness Packet Template

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

## Purpose

Create a reusable Corpus Intelligence Readiness Packet template that future
agents must fill before broad legacy rescans, arbitrary project corpus scans,
retrieval-readiness claims, chatbot-readiness claims, or knowledge-absorption
classification work.

This T1 work order is documentation/template work only. It must not scan legacy
or implement runtime indexing.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 direction to continue corpus intelligence | ACCEPT |
| CI1 GC-018 | `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| GC-047 standard | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | ACCEPT |
| GC-048 standard | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | ACCEPT |
| Search/filter readiness standard | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACCEPT |
| GC-050 standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Dispatch CI1-T1 and verify template completeness | no corpus scan |
| Worker | Create the readiness packet template and completion review | no runtime/index/vector work |
| Reviewer | Verify template is usable, bounded, and gate-compliant | reject vague prose-only template |

## Scope

Allowed scope:

- create `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`;
- create `docs/reviews/CVF_CI1_T1_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_COMPLETION_2026-06-02.md`;
- update `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` status rows for T1 only if completed;
- run listed governance gates and repair allowed-scope doc defects.

Forbidden scope:

- scanning `.private_reference/legacy/`;
- modifying runtime TypeScript, Python checker code, hook chain, or guard files;
- implementing a vector database, indexer, chatbot UI, retrieval route, or LPCI product behavior;
- public-sync, push, or commit;
- claiming semantic correctness, corpus absorption, production readiness, hosted readiness, or public readiness.

Risk ceiling: R1 documentation/template workflow.

## Required First Reads

- `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md`
- `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| GC-047 evidence block exists | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `## Required Evidence Block` | `Corpus Completeness And Report Integrity` | corpus completeness standard | ACCEPT |
| GC-048 reconciliation block exists | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | `## Required Evidence Block` | `Knowledge System Reconciliation` | corpus map standard | ACCEPT |
| Search/filter readiness block exists | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | `## Search / Filter Readiness Block` | `Corpus Search And Filter Readiness` | search/filter standard | ACCEPT |
| GC-050 classification block exists | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | `## Required Evidence Block` | `Corpus Intelligence Classification` | classification standard | ACCEPT |
| GC-047 checker exists | `governance/compat/check_corpus_completeness_report_integrity.py` | `def main` | `main` | corpus completeness checker | ACCEPT |
| GC-048 checker exists | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | `def main` | `main` | corpus map checker | ACCEPT |
| GC-050 checker exists | `governance/compat/check_corpus_intelligence_classification.py` | `def main` | `main` | classification checker | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| CI1-T1 readiness packet template | Scope | readiness packet template | markdown + dispatch gates | READY |
| Include GC-047/048/search-filter/GC-050 chain | Acceptance Criteria | template sections | reviewer check | READY |
| Prevent broad scan before template | Forbidden scope | no legacy scan | git diff/status | READY |
| Make future worker execution clear | Execution Plan | packet template + completion review | reviewer check | READY |

## Worker Autonomy / No-Question Rule

The worker must fix allowed-scope markdown, dispatch-quality, and structural
gate failures without asking the operator. Ask only if the fix would exceed
Allowed scope, scan a corpus, modify runtime/checker/guard files, run live
provider proof, consume secrets/quota, public-sync, push, commit, or change the
claim boundary.

## Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short` in the completion review.
Do not cite empty committed ranges as proof for pending files.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | No (produced during execution) | reusable packet template |
| `docs/reviews/CVF_CI1_T1_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_COMPLETION_2026-06-02.md` | No (produced during execution) | completion review |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Optional update | T1 status only |

## Write Ownership

Owned:

- `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
- `docs/reviews/CVF_CI1_T1_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_COMPLETION_2026-06-02.md`
- `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` status rows for CI1-T1 only

Forbidden:

- runtime TypeScript or Python source;
- governance checker, hook, or guard files;
- `.private_reference/legacy/`;
- public-sync clone;
- archive cleanup outside this work order.

Write mode: additive documentation/template only.

## Execution Plan

1. Capture `baseHead`.
2. Read required first-read docs.
3. Create readiness packet template with these sections:
   - purpose and corpus boundary;
   - source corpus evidence;
   - filesystem discovery index;
   - GC-047 block;
   - GC-048 block;
   - corpus search/filter readiness block;
   - GC-050 classification block;
   - negative search evidence;
   - derived trace;
   - query receipt model;
   - adversarial sampling plan;
   - disposition matrix;
   - claim/final/verification boundary.
4. Create completion review with changed files, gate output, and explicit
   public export disposition.
5. Run required gates.
6. Return pending files for reviewer/operator decision.

## Evidence Requirements

- `git status --short`
- `python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_corpus_intelligence_classification.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_core_guard_self_protection.py --enforce`

## Acceptance Criteria

- The template is fillable by a future worker without inventing section names.
- The template contains all four evidence layers: GC-047, GC-048, search/filter
  readiness, and GC-050.
- Negative search evidence is mandatory before "not found" claims.
- Query receipt model separates filters, candidate set, excluded set, rank
  reasons, citations, and answer boundary.
- Adversarial sampling includes accepted, deferred, rejected, and zero-result
  cases.
- The template states semantic correctness remains review work.
- No runtime/source/checker/guard file is modified.

## Review Gate

CI1-T1 may be returned for review only after the template exists, completion
review exists, required gates pass, and no forbidden paths are touched.

## Closure Checklist

Worker must not close or commit. Return pending implementation and review packet
for orchestrator/reviewer.

## Return-To-Orchestrator Conditions

Return if T1 requires scanning a corpus, changing guard/checker code, modifying
runtime source, creating an indexer, touching public-sync, or making product
readiness claims.

## Operator Checkpoint

Operator said to continue Corpus Intelligence after Memory plane closure. T1 is
the first safe step because it prepares the operating packet before the next
legacy or product corpus task.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corpus-intelligence workflow preparation only. No public-sync
remote, public repository commit, public artifact path, hosted proof, or public
README claim is included.

## Claim Boundary

CI1-T1 claims only a reusable readiness packet template and dispatch workflow.
It does not claim legacy scan completion, semantic correctness, runtime
retrieval quality, LPCI product implementation, production readiness, hosted
readiness, or public readiness.
