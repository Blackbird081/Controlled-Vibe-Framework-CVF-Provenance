# CVF LHW-RESCAN-A CVF_Important Corpus Reconciliation Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-01

## Purpose

Replace the superseded `13 subfolders / 97 files` CVF_Important scan claim
with a reproducible `24 subfolders / 230 files` corpus manifest, terminal
processing ledger, semantic-region routing view, and bounded closure audit.

## Authority

- Operator authorization: 2026-06-01 accepted next move.
- GC-018:
  `docs/baselines/CVF_GC018_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_RECONCILIATION_2026-06-01.md`
- Failure audit:
  `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- GC-047:
  `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- GC-048:
  `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`

## Authorization / Decision

Decision: execute `LHW-RESCAN-A` now as the required remediation-first tranche.

The operator accepted this routed next move on 2026-06-01. No Legacy concept
promotion is authorized by that acceptance.

## Scope

In scope:

- `.private_reference/legacy/CVF_Important/` read-only enumeration;
- deterministic manifest and SHA-256 evidence;
- parser-backed file-level terminal statuses;
- explicit generated or unsupported artifact handling;
- broad semantic-region classification;
- prior scan gap reconciliation;
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
| A1 | Enumerate filesystem source truth | JSON manifest with 230 visible files | PASS |
| A2 | Parse or visibly disposition every file | Terminal processing ledger | PASS |
| A3 | Route broad semantic regions | Rebuildable semantic-region summary | PASS |
| A4 | Reconcile all 24 subfolders | LHW-RESCAN-A audit | PASS |
| A5 | Run adversarial recount and drift check | Audit evidence section | PASS |
| A6 | Close with bounded claim | Completion review and continuity sync | PASS |

## Verification / Evidence

Required closure evidence:

```powershell
python scripts/build_cvf_important_rescan_manifest.py
python governance/compat/check_corpus_completeness_report_integrity.py --base e074082c --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base e074082c --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base e074082c --head HEAD
```

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Filesystem inventory | Exactly the current visible file set, regenerated at closure |
| File-level ledger | Every manifest file has a terminal status |
| Generated artifact handling | Visible and reasoned, never silently omitted |
| Folder coverage | All 24 top-level subfolders reconciled |
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

`docs/work_orders/CVF_WO_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_RECONCILIATION_2026-06-01.md`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Legacy reconciliation only. The public-sync clone
remains untouched and no public catalog artifact is claimed.

## Closure Result

LHW-RESCAN-A closes `CLOSED_PASS_BOUNDED`: `230` visible files are represented
in the filesystem-backed manifest, `230` terminal ledger rows reconcile, one
generated `.pyc` remains visible as a declared exclusion, and `229` authority
assets route into rebuildable broad semantic regions. Deep source
interpretation remains outside this tranche.

## Claim Boundary

This roadmap closes evidence coverage for one bounded corpus. It does not
certify deep semantic understanding or authorize concept realization.
