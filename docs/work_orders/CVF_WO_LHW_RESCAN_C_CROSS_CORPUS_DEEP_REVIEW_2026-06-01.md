# CVF Agent Work Order - LHW-RESCAN-C Cross-Corpus Deep Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-01

## Purpose

Execute `LHW-RESCAN-C`: generate reproducible file-level evidence for the
remaining partial Legacy roots, synthesize overlaps across the three corpora,
and perform source-traced deep review by semantic region. Return a bounded
closure packet that routes later concept-specific work without implementing
Legacy concepts.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 next move request | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_2026-06-01.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_ROADMAP_2026-06-01.md` | ACCEPT |
| Dispatch audit | `docs/audits/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_DISPATCH_AUDIT_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Preserve GC-047, GC-048, and read-only scope | No concept implementation |
| Implementer | Generate manifest, ledger, audit, and region synthesis | Allowed paths only |
| Reviewer | Recompute totals, sample high-risk sources, and challenge overclaims | Reject summary-only closure |
| Safety / boundary owner | Check tool, provider, database, Memory, and autonomous-mutation boundaries | No authority expansion |

## Scope / Target / Owner Boundary

Target roots:

- `.private_reference/legacy/CVF ADD/`
- `.private_reference/legacy/CVF 16.5/`
- `.private_reference/legacy/CVF_Restructure/`

Allowed scope:

- `scripts/build_legacy_rescan_c_manifest.py`
- `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`
- `docs/reviews/CVF_LHW_RESCAN_C_CROSS_CORPUS_SEMANTIC_REGION_SYNTHESIS_2026-06-01.md`
- `docs/reviews/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`
- `docs/audits/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_DISPATCH_AUDIT_2026-06-01.md`
- `docs/baselines/CVF_GC018_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_2026-06-01.md`
- `docs/roadmaps/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_ROADMAP_2026-06-01.md`
- `docs/work_orders/CVF_WO_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_2026-06-01.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden scope:

- `.private_reference/legacy/**` edits;
- runtime, route, provider, prompt, receipt-envelope, database, tool execution,
  Memory reinjection, or autonomous mutation edits;
- public-sync;
- live-provider proof, secrets, paid quota, destructive actions.

Risk ceiling: R1 source-analysis and governance-evidence repair.

## Required First Reads

- `docs/baselines/CVF_GC018_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_2026-06-01.md`
- `docs/audits/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_DISPATCH_AUDIT_2026-06-01.md`
- `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- `docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md`
- `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

## Pre-Flight Checks

Captured batch base:

```text
baseHead=68c0d289
```

Required commands:

```powershell
git rev-parse --short HEAD
git status --short
Get-ChildItem -LiteralPath ".private_reference/legacy/CVF ADD" -Directory -Force
Get-ChildItem -LiteralPath ".private_reference/legacy/CVF 16.5" -Directory -Force
Get-ChildItem -LiteralPath ".private_reference/legacy/CVF_Restructure" -Directory -Force
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 68c0d289 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 68c0d289 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 68c0d289 --head HEAD --enforce
```

Expected result: packet passes dispatch checks before worker implementation
files are created.

Allowed-scope guard failures require remediation and rerun. Return to
Orchestrator only when the required action would exceed Allowed scope, change
the claim boundary, release a hold, increase risk, open public-sync, run
live-provider proof, consume secrets/quota, touch forbidden paths, or perform
destructive actions.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Blind-spot filesystem listing rule exists | EXISTS | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | `Required Gate 1` | `FILESYSTEM_LISTING_REQUIRED` | Blind-spot standard | ACCEPT |
| Blind-spot completeness cross-check rule exists | EXISTS | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | `Required Gate 7` | `COMPLETENESS_CROSS_CHECK` | Blind-spot standard | ACCEPT |
| GC-047 manifest requirement exists | EXISTS | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `Corpus Manifest` | `Corpus Manifest` | GC-047 standard | ACCEPT |
| GC-047 terminal ledger vocabulary exists | VALUE_SET | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `Processing Ledger` | `Processing Ledger` | GC-047 standard | ACCEPT |
| GC-048 reconciliation block exists | EXISTS | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | `Required Evidence Block` | `Knowledge System Reconciliation` | GC-048 standard | ACCEPT |
| Knowledge method requires semantic regions as review routing | RUNTIME_BEHAVIOR | `docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md` | `Semantic Region Model` | `Semantic Region Model` | Knowledge-system method | ACCEPT |
| Failure audit routes the three partial roots into LHW-RESCAN-C | VALUE_SET | `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md` | `Instructions for Codex` | `LHW-RESCAN-C` | Legacy failure audit | ACCEPT |
| Memory-method audit retains PARTIAL until LHW-RESCAN-C | VALUE_SET | `docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md` | `Corpus Completeness And Report Integrity` | `PARTIAL` | Memory-method rescan audit | ACCEPT |
| Legacy registry contains CVF 16.5 folder routing | EXISTS | `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | `CVF 16.5 Folder Registry` | `CVF 16.5 Folder Registry` | Legacy registry | ACCEPT |
| Legacy registry contains CVF ADD folder routing | EXISTS | `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | `CVF ADD Folder Registry` | `CVF ADD Folder Registry` | Legacy registry | ACCEPT |
| Legacy registry marks CVF_Restructure for scan | VALUE_SET | `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | `Other Legacy Roots` | `CVF_Restructure` | Legacy registry | ACCEPT |

## New Doc-Only Fields

| Proposed field or artifact | Intended owner | Purpose | Source status |
| --- | --- | --- | --- |
| `cvf.lhwRescanC.legacyPartialRootsManifest.v1` | generated JSON audit artifact | Deterministic manifest and terminal ledger | DOC_ONLY_NEW |
| `semanticRegion` | generated processing-ledger row | Broad review routing class | DOC_ONLY_NEW |
| `crossRegionLinks` | generated processing-ledger row or synthesis record | Preserve multi-region relationships | DOC_ONLY_NEW |
| `deepReviewLane` | synthesis review record | Group file-level evidence into bounded review regions | DOC_ONLY_NEW |

These fields are documentation and generated-evidence fields only. They do not
extend runtime schemas.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Current filesystem inventory | Build deterministic three-root generator | JSON `manifest` | Regenerate and compare hash | PASS |
| Terminal treatment | Parse or visibly disposition every file | JSON `processingLedger` | Count terminal rows | PASS |
| Source-family coverage | Reconcile all `31` visible families | audit family table | Family arithmetic | PASS |
| Eight region synthesis | Write source-traced review chapters | synthesis review | Reviewer source-locator sample | PASS |
| Cross-region links | Record multi-region relations | `crossRegionLinks` | Link arithmetic and sample | PASS |
| Owner normalization | Map accepted concepts to current CVF owners | synthesis matrix | Reviewer challenge | PASS |
| GC-047 closure | Add required evidence block | reconciliation audit | GC-047 checker | PASS |
| GC-048 closure | Add required evidence block | reconciliation audit | GC-048 checker | PASS |
| Continuity | Route bounded next move | session state and handoff | active-session checker | PASS |

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Source inventory:
  - `CVF ADD=167`
  - `CVF 16.5=100`
  - `CVF_Restructure=74`
  - total `341`
  - raw shell listing and family recount:
    `docs/audits/CVF_LHW_RESCAN_C_CROSS_CORPUS_DEEP_REVIEW_DISPATCH_AUDIT_2026-06-01.md`
- Prior absorption evidence resolved:
  failure audit, Memory-method audit, Legacy registry, and prior A/B closure.
- Detailed source files used:
  dispatch audit control block lists representative high-signal sources.
- Source families skipped:
  none silently skipped.
- File-level accepted value:
  manifest rows include source-traced extracted signals for all `341` files.
- Owner-surface normalization:
  accepted value maps into current CVF owner surfaces before later promotion.
- Accept/defer/reject matrix:
  synthesis and completion review disposition every source family and accepted
  concept.
- Adversarial roles completed:
  Implementer, Skeptic/Auditor, Product/Operator Advocate, and Safety/Boundary
  Owner completed in the synthesis/completion packet.
- Thin proof target:
  one JSON manifest, one reconciliation audit, one synthesis review, one
  completion review.
- Gate 7 completeness cross-check:
  dispatch audit contains `YES` inclusion for all `31` visible source
  families; closure recomputed the table from terminal rows.
- Blind-spot verdict: COMPLETE_FOR_BOUNDARY

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION
- Corpus root: `.private_reference/legacy/CVF ADD/`; `.private_reference/legacy/CVF 16.5/`; `.private_reference/legacy/CVF_Restructure/`
- Snapshot time: `2026-06-01T09:30:00+07:00`
- Enumeration command: `Get-ChildItem -LiteralPath "<root>" -File -Recurse -Force`; cross-check `rg --files --hidden --no-ignore -- "<root>"`
- Manifest artifact or inline manifest: `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- Manifest hash: `ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff`
- Processing ledger artifact or inline ledger: JSON field `processingLedger`
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=341; ledger_terminal=341; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: PASS - `167 + 100 + 74 = 341`
- Drift check: PASS
- Output traceability: manifest, reconciliation audit, synthesis review, and completion review
- Adversarial verification: filesystem recount, manifest totals, and terminal ledger agree
- Corpus verdict: COMPLETE_VERIFIED

## Knowledge System Reconciliation

- Knowledge task class: SEMANTIC_REGION_MAP
- Source manifest: `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- Source manifest hash: `ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff`
- Enumeration safety: filesystem-backed `Get-ChildItem` plus `rg --files --hidden --no-ignore`
- Intake registry or ledger: JSON field `processingLedger`
- Authority assets: `341` READ assets
- Derived views: semantic-region summary and cross-region link counts
- Semantic region ledger: JSON field `processingLedger[].semanticRegion`
- Region reconciliation: assets=341; mapped=341; deferred=0; unmapped=0
- Orphan or unmapped assets: none
- Cross-region links: JSON field `processingLedger[].crossRegionLinks`
- Drift check: PASS
- Rebuildability check: PASS
- Retrieval boundary: review routing only; implementation remains separately gated
- Adversarial verification: `341 = 341 + 0 + 0`
- Knowledge-map verdict: RECONCILED_VERIFIED

## Write Ownership

Write mode: create new worker outputs and modify only listed dispatch,
continuity, roadmap, baseline, work-order, audit, and completion paths.

Any path outside Allowed scope requires Orchestrator review and a revised work
order or separate governed batch.

## Execution Plan

1. Capture the worker base HEAD and run pre-implementation autorun.
2. Add `scripts/build_legacy_rescan_c_manifest.py` using filesystem recursion,
   SHA-256, text-like parsing, and visible exceptional-artifact treatment.
3. Generate the JSON manifest and ledger for all `341` current files.
4. Create the reconciliation audit with root, family, extension, terminal,
   semantic-region, drift, and rebuildability evidence.
5. Create the cross-corpus synthesis review with eight region sections,
   source locators, owner-surface mapping, cross-region links, and explicit
   accept, defer, reject dispositions.
6. Run adversarial review: recompute totals, sample high-risk files, and
   challenge parallel-owner, stale-map, selective-read, and overclaim risks.
7. Run GC-047, GC-048, dispatch-quality, file-size, active-session, and autorun
   closure gates with the real changed range.
8. File completion review and synchronize continuity.

## Evidence Requirements

- `git diff --name-status 68c0d289 HEAD`
- generator output and manifest SHA-256
- root totals, family totals, extension totals, terminal totals
- `341 = terminal rows + unresolved rows`
- authority arithmetic for mapped, deferred, and unmapped assets
- deep-review source-locator sample for each region
- `python governance/compat/check_corpus_completeness_report_integrity.py --base 68c0d289 --head HEAD --enforce`
- `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 68c0d289 --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base 68c0d289 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 68c0d289 --head HEAD`

## Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| Current source corpus enumerated | PASS |
| Every visible file retained | PASS |
| Every manifest row terminally treated | PASS |
| Every exceptional artifact visible | PASS with reason |
| All source families reconciled | PASS |
| Every authority asset region-mapped or visibly deferred | PASS |
| Eight deep-review sections source-traced | PASS |
| Cross-region links and owner mapping present | PASS |
| GC-047 and GC-048 direct checks | PASS |
| No Legacy, runtime, provider, or public-sync edit | PASS |

## Fail Conditions

Closure is blocked if:

- filesystem drift remains unresolved;
- any visible file lacks terminal treatment;
- any semantic-region count fails arithmetic reconciliation;
- any accepted concept lacks source locator or current owner-surface mapping;
- a Legacy source file changes;
- runtime, provider, route, receipt, database, tool-execution, Memory
  reinjection, autonomous-mutation, or public-sync changes enter the batch;
- direct provider scripts are mistaken for governed-route proof;
- predecessor review prose is used as a substitute for current manifest
  evidence.

## Review Gate

Implementation may proceed only after pre-dispatch and pre-implementation
autorun pass for the dispatch packet.

Closure proceeded only after:

- terminal manifest and ledger reconcile;
- synthesis review covers all eight regions;
- reviewer records no blocking objection;
- closure gates are run against the real changed range.

## Closure Checklist

| Item | Required closure resolution |
| --- | --- |
| GC-018 packet | PASS |
| Pre-dispatch autorun | PASS before worker execution |
| Pre-implementation autorun | PASS before material worker edits |
| Generated manifest and terminal ledger | PASS with current hash |
| GC-047 and GC-048 direct checks | PASS |
| Region synthesis | PASS with eight source-traced sections |
| Closure diff gate | PASS inside Allowed scope |
| Runtime/provider/public lane | N/A with reason: source-analysis tranche |
| Public export | N/A with reason: private provenance only |
| Continuity synchronization | PASS |

## Return-To-Orchestrator Conditions

Return to Orchestrator when the required action would exceed Allowed scope,
change the claim boundary, increase risk, require Legacy edits, open public-sync, run
live-provider proof, consume secrets/quota, touch forbidden paths, or perform
destructive actions.

## Operator Checkpoint

operator.checkpoint.waiver: Operator explicitly requested the RESCAN-C packet
and delegated implementation to another agent on 2026-06-01; the worker may
perform read-only source analysis and listed evidence writes without a second
checkpoint.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Legacy analysis only.

## Claim Boundary

This work order authorizes evidence generation and source-traced synthesis
only. It does not authorize runtime implementation, public claims, live
provider use, production readiness, or autonomous mutation.
