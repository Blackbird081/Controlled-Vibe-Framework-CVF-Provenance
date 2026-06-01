# CVF LHW-RESCAN-C Cross-Corpus Deep-Review Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-01

## Purpose

Close the remaining partial Legacy scan gaps across `CVF ADD/`, `CVF 16.5/`,
and `CVF_Restructure/`, then synthesize cross-corpus value by semantic region
so later implementation candidates can be selected from source authority
rather than predecessor summaries.

## Authorization / Decision

Decision: dispatch one bounded source-analysis worker tranche.

Authority:

- operator instruction on 2026-06-01;
- `docs/baselines/CVF_GC018_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_2026-06-01.md`;
- `docs/audits/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_DISPATCH_AUDIT_2026-06-01.md`;
- GC-047 and GC-048 standards.

## Why This Tranche

`LHW-RESCAN-A` and `LHW-RESCAN-B` repaired `268` visible Legacy assets. The
remaining three partial roots contain `341` visible files. Existing ADD, 16.5,
and Restructure syntheses remain useful, but they predate current filesystem
evidence rules and cannot close file-level coverage.

## Scope

In scope:

- manifest and terminal ledger for `341` visible files;
- eight semantic review lanes;
- file-level source locators and extracted signals;
- cross-region links;
- owner-surface normalization;
- accept, defer, reject matrix;
- bounded GC-047 and GC-048 closure.

Out of scope:

- Legacy source edits;
- runtime implementation;
- provider or live-governance proof;
- public-sync;
- autonomous Memory or skill mutation;
- broad public catalog claims.

## Non-Goals

- no claim that routing metadata equals complete semantic understanding;
- no new architecture owner from Legacy source names;
- no runtime proof from direct provider scripts or static documents;
- no implementation packet until RESCAN-C closure routes a bounded candidate.

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| C1 | Enumerate current source truth | JSON manifest with `341` visible files | PASS |
| C2 | Parse or visibly disposition every file | Terminal processing ledger | PASS |
| C3 | Reconcile source families and semantic regions | GC-047 and GC-048 audit | PASS |
| C4 | Deep-review eight regions in priority order | Cross-corpus synthesis review | PASS |
| C5 | Run adversarial overlap and owner-map challenge | Synthesis findings and learning disposition | PASS |
| C6 | Close with bounded next-candidate routing | Completion review and continuity sync | PASS |

## Deep-Review Region Order

| Order | Region | Primary question |
| ---: | --- | --- |
| 1 | `memory_knowledge_graph` | Which Memory, graph, retrieval, provenance, drift, and reinjection-proposal concepts compose cleanly under current CVF owners? |
| 2 | `capability_tool_intake` | Which capability, skill, CLI, MCP, sandbox, approval, and retirement concepts deduplicate into existing intake owners? |
| 3 | `execution_runtime_provider` | Which diagnostics, health, quota, adapter, execution-envelope, and domain-boundary patterns remain useful? |
| 4 | `context_continuity` | Which profile, compaction, budget, checkpoint, resume, and artifact-promotion concepts remain open? |
| 5 | `agent_orchestration` | Which delegation, worker, mailbox, scheduler, and recovery concepts remain advisory-only or demand-gated? |
| 6 | `governance_policy_evidence` | Which policy, guard, receipt, audit, and contradiction controls repeat across corpora? |
| 7 | `product_noncoder` | Which operator-facing simplifications reduce friction without bypassing control? |
| 8 | `strategy_topology` | Which architecture decisions are current, superseded, or future-only? |

## Verification / Evidence

Required commands:

```powershell
python scripts/build_legacy_rescan_c_manifest.py
python governance/compat/check_corpus_completeness_report_integrity.py --base 68c0d289 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 68c0d289 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 68c0d289 --head HEAD
```

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Filesystem inventory | Current visible file set regenerated at closure |
| File-level processing | Every manifest row has an allowed terminal status |
| Source-family coverage | All `31` visible families reconciled |
| Semantic regions | Every authority asset mapped or visibly deferred |
| Deep-review synthesis | Eight region sections with source locators and owner-surface disposition |
| Cross-region links | Visible and rebuildable from source-traced ledger |
| GC-047 | Honest machine-checked verdict |
| GC-048 | Honest machine-checked verdict |
| Runtime/public boundary | No runtime or public claim |

## Failure Conditions

Return to Orchestrator if:

- corpus drift occurs after final manifest generation;
- any visible file lacks terminal treatment;
- any accepted concept lacks source locator or owner-surface disposition;
- Legacy edits or runtime implementation become necessary;
- public-sync, live-provider proof, secrets, quota, or destructive actions
  become necessary.

## Roadmap-To-Work-Order Trace

Execution packet:

`docs/work_orders/CVF_WO_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_2026-06-01.md`

Closure packet:

`docs/reviews/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`

## Completion Result

RESCAN-C closes bounded file-level corpus visibility and semantic-region
synthesis for `CVF ADD`, `CVF 16.5`, and `CVF_Restructure`.

Final evidence:

- manifest hash:
  `ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff`
- processing ledger hash:
  `49a0e6a241d603496d2cfb46de1f3c907c82b5d79d18fb47595cd7685f5668f3`
- visible source assets: `341`
- terminal rows: `341`
- unresolved files: `0`
- semantic regions: `8`
- source families: `31`
- recommended next candidate:
  Memory/Knowledge/Graph Owner-Surface Review under a fresh GC-018.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Legacy analysis only. No public-sync remote, public
repository commit, or public artifact path is included in this tranche; any
public-facing summary must be prepared separately from the public-sync clone.

## Claim Boundary

This roadmap dispatches bounded evidence generation and source synthesis. It
does not authorize runtime realization, public claims, hosted readiness,
production readiness, or autonomous mutation.
