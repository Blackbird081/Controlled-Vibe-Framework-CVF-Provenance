# CVF LHW-RESCAN-B Legacy Small-Roots Corpus Reconciliation Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-01

## Purpose

Build reproducible corpus evidence for the previously unscanned `CVF 17.05/`,
`CVF 25.05/`, and `CVF 28.05/` source trees: `38` visible files in total.

## Authority

- Operator authorization: 2026-06-01 accepted next move.
- GC-018:
  `docs/baselines/CVF_GC018_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`
- Failure audit:
  `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- GC-047:
  `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- GC-048:
  `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`

## Authorization / Decision

Decision: execute `LHW-RESCAN-B` now as the required remediation-first tranche.

The operator accepted this routed next move on 2026-06-01. No Legacy concept
promotion is authorized by that acceptance.

## Scope

In scope:

- the three target roots under `.private_reference/legacy/`;
- deterministic manifest and SHA-256 evidence;
- parser-backed file-level terminal statuses;
- broad semantic-region classification;
- root and top-level-family reconciliation;
- GC-047 and GC-048 closure packet.

Out of scope:

- Legacy source edits;
- runtime concept implementation;
- deep semantic absorption claim;
- autonomous Memory mutation;
- public-sync or live-provider proof.

## Non-Goals

- no runtime source changes;
- no public export;
- no provider or live-governance execution;
- no claim that broad routing metadata replaces deep source review.

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| B1 | Enumerate filesystem source truth | JSON manifest with 38 visible files | PASS |
| B2 | Parse or visibly disposition every file | Terminal processing ledger | PASS |
| B3 | Route broad semantic regions | Rebuildable semantic-region summary | PASS |
| B4 | Reconcile three roots and top-level families | LHW-RESCAN-B audit | PASS |
| B5 | Run adversarial recount and drift check | Audit evidence section | PASS |
| B6 | Close with bounded claim | Completion review and continuity sync | PASS |

## Verification / Evidence

Required closure evidence:

```powershell
python scripts/build_legacy_rescan_b_manifest.py
python governance/compat/check_corpus_completeness_report_integrity.py --base f5b3ef16 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base f5b3ef16 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base f5b3ef16 --head HEAD
```

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Filesystem inventory | Exactly the current visible file set, regenerated at closure |
| File-level ledger | Every manifest file has a terminal status |
| Format handling | Visible and reasoned, never silently omitted |
| Root coverage | All three roots and every top-level family reconciled |
| Semantic regions | Every authority asset routes to one broad region or explicit deferred state |
| GC-047 | Honest machine-checked corpus verdict |
| GC-048 | Honest machine-checked knowledge-map verdict |
| Runtime/public boundary | No runtime or public claim |

## Failure Conditions

Return to Orchestrator if:

- filesystem drift occurs after the final snapshot;
- any visible file lacks terminal status;
- any Legacy edit is required;
- concept promotion or runtime implementation is requested;
- public-sync, live-provider proof, secrets, or destructive actions become
  necessary.

## Roadmap-To-Work-Order Trace

Execution order:

`docs/work_orders/CVF_WO_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Legacy reconciliation only. The public-sync clone
remains untouched and no public catalog artifact is claimed.

## Closure Result

LHW-RESCAN-B closes `CLOSED_PASS_BOUNDED`: all `38` visible files across the
three target roots are represented by the filesystem-backed manifest and
terminal ledger; all `38` authority assets route into rebuildable broad
semantic regions; exclusions and unresolved files are both zero. Routed deep
interpretation remains explicitly outside this tranche.

## Claim Boundary

This roadmap authorizes evidence coverage for one bounded multi-root corpus. It
does not certify deep semantic understanding or authorize concept realization.
