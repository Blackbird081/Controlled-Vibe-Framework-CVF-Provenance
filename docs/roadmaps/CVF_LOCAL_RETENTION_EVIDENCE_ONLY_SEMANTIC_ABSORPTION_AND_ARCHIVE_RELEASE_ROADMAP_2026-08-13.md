# CVF Local Retention Evidence-Only Semantic Absorption And Archive Release Roadmap

Memory class: governed-roadmap

Status: T0_DISPATCH_READY

docType: roadmap

Date: 2026-08-13

Roadmap ID: LRA-SA

## Purpose

Close the remaining knowledge-retention gap for the 56 ZIP entries currently
classified `ARCHIVE_EVIDENCE_ONLY`. The roadmap extracts and maps semantic
value into CVF-owned documentation without copying archived source or claiming
runtime behavior, then separately decides whether the pinned ZIP can be
released.

## Authorization / Decision

The operator explicitly selected continued absorption on 2026-08-13. T0 is
authorized only through the paired fresh GC-018 and no-commit work order. T1
and deletion remain unauthorized.

## Scope

In scope:

- exactly 56 manifest rows carrying `ARCHIVE_EVIDENCE_ONLY`;
- complete read and per-file semantic coverage;
- comparison with the existing full-package inventory and absorption map;
- a CVF-owned per-file semantic absorption ledger;
- minimal updates to the existing absorption map when a real uncovered delta
  is proven;
- terminal reclassification and a later archive-release recommendation.

## Non-Goals

Out of scope:

- raw source, schema, script, test, CLI, MCP, runtime, or package import;
- execution of anything inside the ZIP;
- DESIGN, BUILD, provider/live, public-sync, deploy, or production work;
- ZIP deletion before an accepted T0 and a separately released T1.

## Current Evidence

- Accepted LRA closure: material commit
  `c1e7af8f18da92e33e2af0b582f8d04fd20a528b`.
- Corpus: 129 terminal rows, including 56 `ARCHIVE_EVIDENCE_ONLY`.
- Of those 56, 54 are path-and-hash identical to the previously inventoried
  Workspace Layer package; two are changed package metadata (`PACKAGE_MANIFEST.json`
  and `README.md`).
- Existing owners:
  `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md`
  and
  `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`.
- The inventory proves identity; the absorption map captures group-level useful
  patterns. Neither alone proves per-file semantic completeness for all 56.

## Design Control Gate

| Control | Binding decision |
|---|---|
| Corpus boundary | exact 56 evidence-only rows from the accepted manifest |
| Knowledge boundary | semantic claims require per-file read evidence and a current owner path |
| Import boundary | no archived bytes enter a source/runtime/package owner |
| Adaptation boundary | only CVF-owned prose/ledger updates are allowed |
| Deletion boundary | T0 cannot delete or move the ZIP |
| Failure posture | any uncovered value remains `BLOCKED_VALUE_GAP`; do not force closure |

## Work Plan

| Tranche | Mission | Required output | Entry condition | Status |
|---|---|---|---|---|
| T0 | audit and semantically absorb the 56 evidence-only entries | 56-row ledger, owner/value matrix, minimal owner-map adaptation, manifest/registry reconciliation | operator release; fresh GC-018/work order | DISPATCH_READY |
| T1 | decide archive release | accepted T0 proves zero evidence-only and zero unresolved semantic gaps; retain/delete recommendation | independent T0 acceptance; explicit operator release | PARKED |

T0 succeeds only if every file is read and classified as
`ADAPTED_TO_EXISTING_OWNER`, `SUPERSEDED_BY_CURRENT_CVF_OWNER`, or
`NO_NEW_VALUE`. `BLOCKED_VALUE_GAP` is an honest non-success outcome and keeps
T1 parked.

## Acceptance Criteria

- ZIP digest and 56 entry hashes reproduce exactly;
- semantic ledger contains one row per file, not group-only sampling;
- 54 identical files are not treated as semantically covered by hash alone;
- the two changed metadata files are read and their delta is explicitly judged;
- every useful concept names a CVF-owned target surface;
- manifest, registry source/aggregates, findings, audit, and worker return agree;
- no source import, execution, runtime authority, or deletion occurs;
- independent reviewer acceptance is required before T1.

## Verification / Evidence

Verification requires archive SHA-256, all 56 entry hashes, complete per-file
ledger reconciliation, owner-path evidence, registry generation/checks,
worker-return fast gate, and `git diff --check`.

## Source Verification

| Claim | Source | Verified section | Disposition |
|---|---|---|---|
| 56 evidence-only rows remain | `docs/corpus-intelligence/manifests/local-retention-artifacts-20260812.json` | `counts.dispositionTotals`; `entries[]` | ACCEPT |
| 54 are path/hash identical to prior scan | same manifest and `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | per-row comparison; full manifest | ACCEPT |
| two changed metadata rows add no proven capability by themselves | accepted T2 audit and manifest rows 1-2 | rationale fields | ACCEPT_WITH_RECOMPUTE |
| group-level useful patterns already have a CVF owner | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | Useful Patterns; CVF Mapping; Two-Layer Absorption | ACCEPT_WITH_PER_FILE_RECONCILIATION |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | dispatch status; Source Verification; corpus and knowledge reconciliation fields; absorption ledger enums; Public Export Disposition |
| gateRunPurpose | confirm roadmap and dispatch evidence after source inspection, not discover semantic value |
| claimBoundary | checker shape does not prove per-file semantic absorption |

## Next Allowed Move

Execute only LRA-SA-T0 under its fresh baseline and no-commit work order. T1,
ZIP deletion, source import, DESIGN, BUILD, runtime, provider/live, public-sync,
deploy, and production remain parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local-retention knowledge reconciliation only.

## Claim Boundary

This roadmap authorizes documentation-only semantic reconciliation. It does not
make archive content CVF source, implement archived designs, or authorize ZIP
deletion.
