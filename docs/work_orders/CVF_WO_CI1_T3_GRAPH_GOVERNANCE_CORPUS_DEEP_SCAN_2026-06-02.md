# CVF Work Order - CI1-T3 Graph Governance Corpus Deep Scan

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

## Purpose

Apply the CI1 readiness packet workflow to the 7-file graph governance corpus:

`.private_reference/legacy/CVF ADD/code-review-graph/`

This tranche tests the full corpus intelligence loop after CI1-T2: read a
second real graph-adjacent corpus, classify it structurally, reconcile it to
owner surfaces, and route findings into GC-051 and GC-052 so the scan loop feeds
the learning loop.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 direction to create CI1-T3 work order | ACCEPT |
| CI1-T3 GC-018 | `docs/baselines/CVF_GC018_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_2026-06-02.md` | ACCEPT |
| CI1 parent GC-018 | `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md` | ACCEPT |
| CI1-T1 template | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| CI1-T2 finding packet | `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md` | ACCEPT |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |
| GC-052 interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Dispatch CI1-T3 after GC-018 exists | no implementation |
| Worker | Read all 7 target files, fill packet, update registry/findings, create completion review | no runtime/checker/guard edits; no commit/push |
| Reviewer | Verify gates, registry routing, and claim boundary | reject prose-only findings |

## Scope

Allowed scope:

- read all 7 files under `.private_reference/legacy/CVF ADD/code-review-graph/`;
- produce `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`;
- produce `docs/reviews/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_COMPLETION_2026-06-02.md`;
- create `docs/corpus-intelligence/findings/legacy-cvf-add-code-review-graph.md` if any finding is recorded;
- update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`;
- update the CI1 roadmap CI1-T3 row/status only;
- repair allowed-scope markdown, corpus, registry, interlock, and dispatch-gate defects.

Forbidden scope:

- reading files outside `.private_reference/legacy/CVF ADD/code-review-graph/`;
- scanning full `.private_reference/legacy/CVF ADD/`;
- modifying runtime TypeScript, Python checker code, hook chain, guard docs, or AGENTS/front-door files;
- implementing graph guards, graph CLI commands, vector indexes, retrieval routes, or chatbot/product behavior;
- public-sync, push, or commit;
- claiming semantic correctness, production readiness, hosted readiness, public readiness, or runtime graph enforcement.

Risk ceiling: R1 read-only legacy scan plus documentation/registry updates.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_2026-06-02.md`
2. `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
3. `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
4. `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
5. `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
6. `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
7. `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
8. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`
9. CI1-T2 findings:
   `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md`
10. All 7 target corpus files:
    - `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md`
    - `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_GOVERNANCE_EXTENSION_SPEC.md`
    - `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_IMPLEMENTATION_PLAN.md`
    - `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md`
    - `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_KNOWLEDGE_SPEC.md`
    - `.private_reference/legacy/CVF ADD/code-review-graph/README.md`
    - `.private_reference/legacy/CVF ADD/code-review-graph/Thong_tin.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 13c91de8 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 13c91de8 --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T3 GC-018 exists | `docs/baselines/CVF_GC018_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_2026-06-02.md` | full document | `CVF_GC018_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_2026-06-02.md` | CI1-T3 baseline | ACCEPT |
| CI1 readiness template exists | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | full document | `CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | CI1 packet template | ACCEPT |
| GC-051 registry exists | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `corpora` | `corpora` | corpus scan registry | ACCEPT |
| GC-052 scan-learning interlock exists | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `scan-loop-to-learning-loop` | `scan-loop-to-learning-loop` | system loop interlock registry | ACCEPT |
| Target corpus has 7 files | N/A - filesystem enumeration | `rg --files --hidden --no-ignore` output in GC-018 | `.private_reference/legacy/CVF ADD/code-review-graph/` | filesystem source corpus | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `13c91de8` | git repository state | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| CI1-T3 graph governance deep scan | Scope + Execution Plan | readiness packet | GC-047/048/050 gates | READY |
| Use second real corpus before index model | Purpose | CI1-T3 packet | reviewer check | READY |
| Route scan findings to GC-051 | System Loop Interlock Requirement | registry + findings packet | GC-051 checker | READY |
| Route learning candidates through GC-052/F2G | System Loop Interlock Requirement | F2G disposition rows | GC-052 + F2G gates | READY |
| Avoid runtime/guard implementation | Forbidden scope | no runtime/checker/guard diffs | git status/diff | READY |

## Worker Autonomy / No-Question Rule

Proceed autonomously with reading the 7 target files, filling the readiness
packet, updating allowed registry/finding artifacts, running gates, and fixing
allowed-scope defects.

Allowed-scope markdown, registry, classification, reconciliation, and
dispatch-quality failures are mandatory repairs. Escalation is permitted only
when remediation would expand scope, touch forbidden paths, consume
secrets/quota, run live provider proof, perform public-sync, commit/push, or
change the claim boundary.

## Pending Artifact Evidence Finality

Do not commit. Record `git status --short` in the completion review.
Do not cite committed-only or empty ranges as proof for pending files.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | No (produced during execution) | filled CI1 readiness packet |
| `docs/reviews/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_COMPLETION_2026-06-02.md` | No (produced during execution) | completion review |
| `docs/corpus-intelligence/findings/legacy-cvf-add-code-review-graph.md` | Required if findings exist | finding disposition packet |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Required update | machine-readable scan registry |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Required update | human-readable registry |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Optional update | CI1-T3 status only |

## Write Ownership

Owned:

- `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
- `docs/reviews/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_DEEP_SCAN_COMPLETION_2026-06-02.md`
- `docs/corpus-intelligence/findings/legacy-cvf-add-code-review-graph.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` CI1-T3 row/status only

Forbidden:

- runtime TypeScript or Python source;
- governance checker, hook, or guard files;
- `AGENTS.md`, `CVF_SESSION_MEMORY.md`, active handoff, or state registry;
- `.private_reference/legacy/` writes;
- public-sync clone;
- any file outside the owned list above for writing.

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `.private_reference/legacy/CVF ADD/` outside `code-review-graph/` | other source families require separate tranches |
| `.private_reference/legacy/CVF 16.5/` | future candidate, not CI1-T3 |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` | already scanned in CI1-T2 |
| runtime `*.ts` / `*.tsx` | no implementation authorized |
| `governance/compat/` and `governance/toolkit/` | no guard maintenance authorized |
| public-sync clone | out of scope |

## Forbidden Filesystem State At Dispatch

| Forbidden path | State at dispatch (baseHead `13c91de8`) | Outcome |
| --- | --- | --- |
| `.private_reference/legacy/CVF ADD/` outside `code-review-graph/` | no write authorization; worker may not read these folders | COMPLIANT |
| `.private_reference/legacy/CVF 16.5/` | not selected for CI1-T3 | COMPLIANT |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` | CI1-T2 already completed; no CI1-T3 reads | COMPLIANT |
| runtime `*.ts` / `*.tsx` | no runtime implementation authorized | COMPLIANT |
| `governance/compat/` and `governance/toolkit/` | no guard maintenance authorized | COMPLIANT |
| public-sync clone | no public-sync work authorized | COMPLIANT |

## System Loop Interlock Requirement

CI1-T3 must not return findings as prose only.

If the scan records any finding, the worker must:

- add a `legacy-cvf-add-code-review-graph` corpus entry to
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- include `defectClass`, `learningLane`, and a concrete `nextAction`;
- cite `f2gRef`, `roadmapRef`, or `workOrderRef` for any deferred or blocked
  finding;
- create or update the finding packet at
  `docs/corpus-intelligence/findings/legacy-cvf-add-code-review-graph.md`;
- include `Finding-To-Governance Learning Disposition` in the completion
  review when findings exist.

This satisfies the GC-052 `scan-loop-to-learning-loop` routing rule. It does not
authorize autonomous rule mutation, guard implementation, runtime behavior
change, or provider prompt changes.

## Execution Plan

1. Capture `baseHead` with `git rev-parse --short HEAD`.
2. Confirm clean working tree or record pre-existing unrelated changes.
3. Enumerate the target corpus with:

   ```powershell
   rg --files --hidden --no-ignore ".private_reference/legacy/CVF ADD/code-review-graph"
   ```

   Expected count: 7.

4. Read all 7 files fully.
5. Produce the filled readiness packet with all CI1-T1 sections:
   - corpus boundary;
   - GC-047 source corpus evidence;
   - GC-048 knowledge-map reconciliation;
   - search/filter readiness;
   - negative search evidence;
   - derived trace;
   - query receipt model;
   - adversarial sampling;
   - GC-050 classification ledger;
   - disposition matrix;
   - public export disposition;
   - finding-to-governance learning disposition when applicable;
   - claim/final/verification boundary.
6. Produce the completion review.
7. Update GC-051 registry and finding packet when findings exist.
8. Run all required gates and repair allowed-scope failures.
9. Return pending files for reviewer/operator disposition.

## Required Gate Commands

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_corpus_scan_registry.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_system_loop_interlock.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_core_guard_self_protection.py --enforce
python governance/compat/check_forbidden_filesystem_state.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 13c91de8 --head HEAD
```

Record results in the completion review. If pre-closure fails only because the
worker leaves uncommitted pending artifacts as instructed, record that boundary
without claiming clean closure.

## Evidence Requirements

- `git status --short` recorded in completion review;
- raw corpus enumeration output recorded in packet;
- manifest hash recorded from sorted file list;
- processing ledger with 7 terminal rows;
- GC-050 classification ledger with 7 rows;
- adversarial sampling table with at least 5 rows;
- negative search evidence before any "not found" claim;
- GC-051 registry entry when findings exist;
- F2G/GC-052 routing evidence when findings exist.

## Acceptance Criteria

- [ ] All 7 target files read and recorded with terminal processing status
- [ ] GC-047 block uses `manifest=7; ledger_terminal=7; exclusions=0; unresolved=0`
- [ ] GC-048 block uses `assets=7; mapped=N; deferred=N; unmapped=0`
- [ ] GC-050 classification ledger has 7 rows with valid enum values
- [ ] Search/filter readiness includes facet schema and graph-governance domain fields
- [ ] Adversarial sampling includes accepted, deferred, rejected, and zero-result cases
- [ ] Findings, if any, appear in GC-051 registry and finding packet
- [ ] Deferred or blocked findings include F2G-compatible routing evidence
- [ ] Worker did not commit, push, write legacy files, or touch forbidden paths
- [ ] No runtime graph guard, CLI, retrieval, product, public, or production claim

## Review Gate

CI1-T3 may be returned for review only after the packet, completion review, and
required registry/finding updates exist, all allowed-scope gate failures are
repaired, and the completion review records pending working-tree status.

## Closure Checklist

- [ ] Readiness packet produced with all CI1-T1 sections filled
- [ ] Completion review produced
- [ ] All 7 files recorded with terminal processing status
- [ ] GC-051 registry updated for `legacy-cvf-add-code-review-graph`
- [ ] Finding packet created when findings exist
- [ ] F2G/GC-052 routing evidence recorded for deferred or blocked findings
- [ ] Required gates run and results recorded
- [ ] Working tree status recorded in completion review
- [ ] Worker did not commit or push

## Return-To-Orchestrator Conditions

Return only if execution requires scope expansion, forbidden path edits,
runtime implementation, guard/checker maintenance, public-sync, secrets/quota,
live/provider proof, commit/push, or a claim-boundary change.

## Operator Checkpoint

Operator selected CI1-T3 after reviewing the CI1-T2 Graphify result and Claude's
recommendation. The filesystem-confirmed source count is 7 files. CI1-T3 scans
the selected graph governance folder before CVF opens the cross-corpus index
model.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T3 reads private legacy corpus under `.private_reference/legacy/`.
No public-sync remote, public repository commit, public artifact path, hosted
proof, or public README claim is included.

## Corpus Intelligence Classification

- Classification task class: GOVERNANCE_QA
- Source corpus evidence: `.private_reference/legacy/CVF ADD/code-review-graph/` - 7 files, filesystem-confirmed at dispatch
- Knowledge map evidence: worker-produced packet
- Classification ledger: dispatch-level deferred rows below
- Legal/policy corpus: NO
- Domain fields: N/A - graph governance legacy corpus, not legal/policy
- Response Boundary: DIRECT_CITED_ANSWER | SUMMARY_WITH_SOURCE | PROCEDURAL_GUIDANCE | ESCALATE_OR_ABSTAIN
- Adversarial sampling plan: worker-produced packet
- Classification verdict: CLASSIFIED_STRUCTURAL_PASS

### Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer | answerClass | domainFields |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_GOVERNANCE_EXTENSION_SPEC.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_IMPLEMENTATION_PLAN.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF ADD/code-review-graph/CVF_GRAPH_KNOWLEDGE_SPEC.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF ADD/code-review-graph/README.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |
| `.private_reference/legacy/CVF ADD/code-review-graph/Thong_tin.md` | DEFERRED | GRAPH_GOVERNANCE | PRIVATE_PROVENANCE | DEFER | read during CI1-T3 execution | SUMMARY_WITH_SOURCE | N/A |

## Claim Boundary

CI1-T3 claims only dispatch of a bounded 7-file graph governance corpus scan.
The worker output may claim corpus completeness and structural classification
only after all required evidence exists and gates pass. CI1-T3 does not claim
semantic correctness, graph guard enforcement, graph CLI implementation, runtime
retrieval quality, LPCI product implementation, production readiness, hosted
readiness, or public readiness.
