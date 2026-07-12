# CVF System Chain Gap Ledger

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-07-11

Batch ID: MSEA-ASC-RW

executionBaseHead: `0a2f3c2e6`

EPISTEMIC_PROCESS_NA_WITH_REASON: gap-ledger front door and index summary; no
new empirical claim beyond the reviewer-accepted MSEA-R90/R96 findings this
ledger migrates from.

## Purpose

Provide a stable, retrievable front door for CVF's known architecture gaps:
missing, partial, intentionally separated, parked, or unresolved connections
between planes and owners. This front door lets a contributor or agent find
every active gap by ID, plane, owner, status, proof class, or reopen trigger
without reopening every historical audit.

## Scope / Applies To

Applies to any operator, developer, or agent asking "what is not yet
connected or resolved in CVF's architecture, and what would change that."
Does not apply to runtime/product code and does not itself implement,
modify, or supersede the R91 system-chain map, its freshness checker, or any
frozen doctrine. Historical reviews (R90-R99 audits and completions) remain
the evidentiary record; this ledger is the active, retrievable index, not a
replacement for that evidence.

## Canonical Source

- Compact gap entries: `docs/reference/system_chain/gaps/entries/`
- Generated machine index: `docs/reference/system_chain/gaps/CVF_SYSTEM_CHAIN_GAP_INDEX.json`
- Generator: `governance/compat/generate_as_built_system_catalog.py --target gaps`
- Freshness/drift checker: `governance/compat/check_as_built_system_catalog_drift.py`
- Schema contract: `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_SCHEMA.json` (`GAP` definition)
- Reconciliation contract: `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_RECONCILIATION_CONTRACT.md`

The compact entries under `entries/` are the editable authority. The JSON
index is generated and must not be hand-edited; run the generator after
adding, editing, or closing a gap entry.

## Current Gaps (Generated Summary)

This table is a human summary of the 6 gap entries generated at authoring
time. Always trust `CVF_SYSTEM_CHAIN_GAP_INDEX.json` and the `entries/`
directory over this prose if they disagree; re-run the generator and refresh
this table when entries change.

### Counts By Status

| Status | Count |
|---|---|
| `VALUE_PARKED_WITH_REOPEN_CONDITIONS` | 2 |
| `EVIDENCED_NOT_OPERATOR_VISIBLE` | 1 |
| `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE` | 3 |

### Open / Parked / Intentionally Separated Gaps

| gapId | Plane | Owner (source -> target) | Status | Proof class | Entry / Evidence | Next action |
|---|---|---|---|---|---|---|
| `cvf.asc.gap.l4_product_implementation_unresolved.v1` | doctrine_to_contract | `NONE_WITH_REASON` -> `EXTENSIONS/CVF_v3.0_CORE_GIT_FOR_AI/` | `VALUE_PARKED_WITH_REOPEN_CONDITIONS` | `DECLARED_EDGE` | `entries/l4_product_implementation_unresolved.json`; `docs/audits/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_2026-07-11.md` | Reopen only when the L4 module exits Pre-Public Status and an operator-authorized promotion review accepts it |
| `cvf.asc.gap.l6_ecosystem_layer_partial.v1` | doctrine_to_contract | `docs/` -> `EXTENSIONS/examples/`; `governance/toolkit/06_EXAMPLES/` | `PARTIAL_CHAIN_WITH_BOUNDARY` | `DECLARED_EDGE` | `entries/l6_ecosystem_layer_partial.json` | Reopen only after a governed L6 consolidation decision is authorized |
| `cvf.asc.gap.web_checker_inventory_not_unified.v1` | evidence_to_operator_surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` -> `NONE_WITH_REASON` | `EVIDENCED_NOT_OPERATOR_VISIBLE` | `EXECUTED_AND_EVIDENCED_EDGE` | `entries/web_checker_inventory_not_unified.json` | Reopen only when a fresh Deliverable B or maintenance packet implements a unified Web checker readout |
| `cvf.asc.gap.sot3_independent_refinery_owner_unresolved.v1` | doctrine_to_contract -> contract_to_runtime | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` -> `NONE_WITH_REASON` | `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE` | `DECLARED_EDGE` | `entries/sot3_independent_refinery_owner_unresolved.json`; `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` | Reopen only when an operator-authorized Refinery implementation tranche is dispatched |
| `cvf.asc.gap.sot3_truth_kernel_runtime_unresolved.v1` | doctrine_to_contract -> contract_to_runtime | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` -> `NONE_WITH_REASON` | `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE` | `DECLARED_EDGE` | `entries/sot3_truth_kernel_runtime_unresolved.json`; `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` | Reopen only when an operator-authorized Truth Kernel runtime implementation tranche is dispatched; existing TKG-T1 doctrine owner is unaffected |
| `cvf.asc.gap.sot3_post_kernel_truth_flow_owner_unresolved.v1` | contract_to_runtime -> runtime_to_enforcement | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` -> `NONE_WITH_REASON` | `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE` | `DECLARED_EDGE` | `entries/sot3_post_kernel_truth_flow_owner_unresolved.json`; `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` | Reopen only when an operator-authorized post-Kernel Truth Flow implementation tranche is dispatched |

### Recently Closed Gaps

None. This is the ledger's first populated wave (ASC-RW); no gap has been
closed since creation.

## Search Examples

- By `gapId`: `grep -r "cvf.asc.gap.l4_product_implementation_unresolved" docs/reference/system_chain/gaps/entries/`
- By plane: search `sourcePlaneId` or `targetPlaneId` for `cvf.asc.plane.doctrine_to_contract.v1` across `entries/*.json`
- By owner: search `sourceOwner`/`targetOwner` string fields for a repo-relative path
- By status: search `currentStatus` for a canonical token (see Vocabulary below)
- By reopen trigger: read the `reopenCondition.conditionText` field of each entry

## Vocabulary And Rules For Adding/Updating An Entry

1. Every entry is one compact JSON file under `entries/`, named
   `<slug>.json`, whose `stableId` matches
   `cvf.asc.gap.<slug>.v<version>` per the schema's `stableId` grammar.
2. `currentStatus` must be one of the ten canonical `gapTerminalStatus`
   enum values in the schema. No free-text status is permitted.
3. `VALUE_PARKED_WITH_REOPEN_CONDITIONS` requires a non-empty
   `reopenCondition.conditionText` (schema-enforced).
4. `ACTIVE_OWNER_CREATED_WITH_BOUNDARY` and
   `NAMED_DIFFERENTLY_ACTIVE_OWNER_WITH_BOUNDARY` require a non-empty
   `boundaryCaveat` (schema-enforced).
5. `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE` requires at least one of
   `rejectedCandidates` or `negativeSearchEvidence` (schema-enforced).
6. After adding, editing, or closing any entry, run
   `python governance/compat/generate_as_built_system_catalog.py --target gaps`
   to regenerate `CVF_SYSTEM_CHAIN_GAP_INDEX.json`, then run
   `python governance/compat/check_as_built_system_catalog_drift.py --enforce`
   to confirm the aggregate matches a fresh rebuild.
7. A gap entry is never hand-edited only at the generated-index level; the
   compact `entries/` source is always the edited artifact.

## Historical Reviews Are Evidence, Not The Active Index

R90-R99 audits, reviews, and completions remain the authoritative evidence
for how each gap's status was determined. This ledger is the current,
retrievable index built from that evidence; it does not restate or
re-litigate the underlying findings, and a historical review document is
never treated as more current than this ledger's own `lastReviewed` field
once a gap entry has been migrated here.

## Relationship To The R91 System-Chain Map

This gap ledger is strictly additive to `docs/reference/system_chain/`. It
does not modify `CVF_SYSTEM_CHAIN_MAP.json`, its `README.md` companion, the
freshness standard, or `governance/compat/check_system_chain_map_freshness.py`.
Freshness for this ledger's own generated index is owned exclusively by the
scoped sibling checker `governance/compat/check_as_built_system_catalog_drift.py`,
per `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md`
Decision 2.

## Claim Boundary

This README is the gap ledger's human front door for the 3 gap entries
populated in the MSEA-ASC-RW wave. It does not claim exhaustive coverage of
every possible CVF architecture gap, does not modify any R91-owned artifact,
and does not authorize runtime, public, provider, Web, or L4 promotion work.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture-catalog wave; no public-sync
authorization exists for this family.
