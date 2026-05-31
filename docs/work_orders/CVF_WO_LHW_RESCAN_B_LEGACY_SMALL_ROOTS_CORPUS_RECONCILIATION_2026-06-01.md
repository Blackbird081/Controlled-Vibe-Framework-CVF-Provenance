# CVF Agent Work Order - LHW-RESCAN-B Legacy Small-Roots Corpus Reconciliation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-01

## Purpose

Execute the operator-authorized `LHW-RESCAN-B` evidence repair: enumerate all
visible files under `CVF 17.05/`, `CVF 25.05/`, and `CVF 28.05/` from
filesystem source truth, generate a stable manifest and terminal ledger, route
broad semantic regions, reconcile all source families, and file a bounded
closure packet.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 acceptance of routed next move | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_ROADMAP_2026-06-01.md` | ACCEPT |
| Legacy failure audit | `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Preserve remediation-first scope and authority chain | No concept promotion |
| Implementer | Generate manifest, ledger, routing audit, and evidence | Allowed paths only |
| Reviewer | Recompute totals, challenge omissions, and reject overclaims | No runtime expansion |

## Scope / Target / Owner Boundary

Target roots:

- `.private_reference/legacy/CVF 17.05/`
- `.private_reference/legacy/CVF 25.05/`
- `.private_reference/legacy/CVF 28.05/`

Allowed scope:

- `scripts/build_legacy_rescan_b_manifest.py`
- `docs/audits/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- `docs/audits/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`
- `docs/reviews/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`
- `docs/baselines/CVF_GC018_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`
- `docs/roadmaps/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_ROADMAP_2026-06-01.md`
- `docs/work_orders/CVF_WO_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden scope:

- `.private_reference/legacy/**` edits;
- runtime, provider, prompt, receipt, route, Memory reinjection, or autonomous
  mutation edits;
- public-sync;
- secrets, paid quota, destructive actions.

Risk ceiling: R1 source-analysis and governance-evidence repair.

## Required First Reads

- `docs/baselines/CVF_GC018_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`
- `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`

## Pre-Flight Checks

Captured batch base:

```text
baseHead=f5b3ef16
```

Required commands:

```powershell
git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base f5b3ef16 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base f5b3ef16 --head HEAD
```

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Legacy blind-spot standard exists | EXISTS | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | `Required Gate 1` | `FILESYSTEM_LISTING_REQUIRED` | Blind-spot prevention standard | ACCEPT |
| Corpus evidence standard exists | EXISTS | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `Corpus Manifest` | `Corpus Manifest` | GC-047 standard | ACCEPT |
| Terminal ledger vocabulary exists | VALUE_SET | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | `Processing Ledger` | `Processing Ledger` | GC-047 standard | ACCEPT |
| Knowledge-map standard exists | EXISTS | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | `Required Evidence Block` | `Knowledge System Reconciliation` | GC-048 standard | ACCEPT |
| Region invariant exists | LITERAL_INVARIANT | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | `Rule` | `authority assets` | GC-048 standard | ACCEPT |
| Legacy failure audit routed the three roots into LHW-RESCAN-B | VALUE_SET | `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md` | `Instructions for Codex` | `LHW-RESCAN-B` | Legacy failure audit | ACCEPT |

## New Doc-Only Fields

| Proposed field or artifact | Intended owner | Purpose | Source status |
| --- | --- | --- | --- |
| `cvf.lhwRescanB.legacySmallRootsManifest.v1` | generated JSON audit artifact | Deterministic manifest and terminal ledger | DOC_ONLY_NEW |
| `semanticRegion` | generated ledger row | Broad routing class, not deep semantic proof | DOC_ONLY_NEW |
| `LHW-RESCAN-B reconciliation audit` | docs audit surface | GC-047 and GC-048 bounded closure | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Filesystem inventory | Build deterministic multi-root generator | JSON `manifest` | regenerate and compare hash | PASS |
| File-level ledger | Parse or visibly disposition every file | JSON `processingLedger` | count terminal rows | PASS |
| Semantic routing | Assign broad region to every authority row | JSON `counts.semanticRegions` | region arithmetic | PASS |
| Family reconciliation | Cross-check all roots and families | audit family table | family count recompute | PASS |
| GC-047 closure | Add required block | audit corpus verdict | GC-047 checker | PASS |
| GC-048 closure | Add required block | audit knowledge-map verdict | GC-048 checker | PASS |
| Continuity | Route next move after closure | session state and handoff | active-session checker | PASS |

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Source inventory:
  - `CVF 17.05`: `31` files from shell recount.
  - `CVF 25.05`: `2` files from shell recount.
  - `CVF 28.05`: `5` files from shell recount.
  - Shell command run:
    `Get-ChildItem -LiteralPath "<root>" -Directory -Force`;
    `Get-ChildItem -LiteralPath "<root>" -File -Recurse -Force | Measure-Object`
  - Shell output (subfolder list):

```text
CVF 17.05:
CVF_EXTERNAL_CAPABILITY_INTAKE
REVIEW FOLDER
CVF 25.05:
(no subfolders; flat root)
CVF 28.05:
(no subfolders; flat root)
```

  - Total file count (from shell): `38`
- Prior absorption evidence resolved:
  failure audit and active handoff read; prior per-gap notes do not constitute
  a GC-047 filesystem manifest.
- Detailed source files used:
  generated file-level terminal ledger will retain every path and extracted
  signal.
- Source families skipped:
  none.
- File-level accepted value:
  broad routing evidence only.
- Owner-surface normalization:
  later deep review must map accepted concepts to existing CVF owner surfaces.
- Accept/defer/reject matrix:
  all five visible families are `DEFER_DEMAND_GATED` until broad routing closes
  and later deep-review GC-018 packets authorize interpretation.
- Adversarial roles completed:
  - Implementer: multi-root deterministic generator is the smallest proof.
  - Skeptic/Auditor: compare totals back to `31 + 2 + 5`.
  - Product/Operator Advocate: keep operator feedback and code artifacts
    visible.
  - Safety/Boundary Owner: no runtime implementation or autonomous mutation.
- Thin proof target:
  one JSON artifact, one reconciliation audit, one closure review.
- Gate 7 completeness cross-check:

| Root / top-level family | In Gate 3? | Disposition if absent | Reason |
| --- | --- | --- | --- |
| `CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE` | YES | N/A | Enters terminal ledger |
| `CVF 17.05/REVIEW FOLDER` | YES | N/A | Enters terminal ledger |
| `CVF 17.05/(root files)` | YES | N/A | Enters terminal ledger |
| `CVF 25.05/(root files)` | YES | N/A | Flat root enters terminal ledger |
| `CVF 28.05/(root files)` | YES | N/A | Flat root enters terminal ledger |

- Blind-spot verdict: PARTIAL

## Execution Plan

1. Add a deterministic generator using filesystem recursion and SHA-256.
2. Generate one JSON manifest and terminal ledger for the three roots.
3. Parse text-like assets and visibly disposition exceptional artifacts.
4. Create a bounded audit with root, family, extension, semantic-region,
   drift, and rebuildability evidence.
5. Run GC-047, GC-048, dispatch, file-size, and autorun gates.
6. File completion review, close roadmap and work order, commit, and
   synchronize continuity.

## Write Ownership

Only the allowed script, generated audit artifacts, closure packet, roadmap,
work order, baseline, and continuity paths may change. The Legacy corpus is
read-only.

## Evidence Requirements

- `git diff --name-status f5b3ef16 HEAD`
- generator command and JSON manifest hash
- root count, family count, extension count, terminal count, exclusion count
- `python governance/compat/check_corpus_completeness_report_integrity.py --base f5b3ef16 --head HEAD --enforce`
- `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base f5b3ef16 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base f5b3ef16 --head HEAD`

## Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| Current corpus enumerated from filesystem | PASS |
| Every visible file retained in manifest | PASS |
| Every manifest row has terminal status | PASS |
| Every authority asset has broad region | PASS |
| Every exceptional artifact remains visible | PASS with declared treatment |
| All three roots and visible families reconciled | PASS |
| GC-047 and GC-048 evidence blocks pass machine checks | PASS |
| No Legacy, runtime, or public-sync edit | PASS |

## Fail Conditions

Stop and return to Orchestrator if:

- the filesystem changes after final generation;
- any manifest file lacks terminal status;
- any authority asset lacks region mapping;
- Legacy edits or runtime implementation become necessary;
- public-sync, provider proof, secrets, or destructive actions become
  necessary.

Allowed-scope gate failures must be repaired and rerun without asking the
operator to choose routine cleanup.

## Review Gate

Reject closure if the manifest omits any visible file, terminal rows do not
reconcile, semantic routing hides deferred assets, exceptional artifacts
disappear from evidence, corpus drift remains unresolved, or any Legacy,
runtime, provider, public-sync, or autonomous-mutation change enters the batch.

## Closure Checklist

| Item | Required closure resolution |
| --- | --- |
| GC-018 packet committed | PASS: authorization packet commit `193f218a` |
| Pre-dispatch gate | PASS against captured base `f5b3ef16` |
| Pre-implementation gate | PASS after allowed-scope continuity remediation commit `b1adb607` |
| Generated manifest and ledger | PASS: implementation commit `563c61b7`; `38/38` terminal rows |
| GC-047 and GC-048 machine checks | PASS on committed range `f5b3ef16..92fe9173` |
| Completion review | PASS: `docs/reviews/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md` |
| Public export | N/A with reason: private provenance scan only |
| Runtime/provider/live-proof lane | N/A with reason: source-analysis tranche |
| Continuity synchronization | PASS: final front-door, state-registry, and handoff sync included in closure batch |

## Operator Checkpoint

SATISFIED. Operator accepted the routed `LHW-RESCAN-B` next move on 2026-06-01.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Legacy reconciliation only. The public-sync clone
remains untouched and no public catalog artifact is claimed.

## Claim Boundary

This work order authorizes evidence generation and bounded source analysis
only. It does not authorize concept implementation or complete semantic
understanding claims.
