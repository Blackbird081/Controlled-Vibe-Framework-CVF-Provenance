# CVF As-Built System Architecture Catalog

Memory class: POINTER_RECORD

Status: DOC_ONLY_NEW

docType: reference

Date: 2026-07-11

Batch ID: MSEA-ASC-T0

executionBaseHead: `928bab031`

EPISTEMIC_PROCESS_NA_WITH_REASON: family front-door/index reference; no
empirical claim or evidence-comparison work is asserted by this document
itself.

## Purpose

Front door for the CVF as-built system architecture catalog family. This
family will eventually let a contributor or agent determine what CVF
contains, who owns each responsibility, how planes connect, which edges
execute, where evidence is retained, and which gaps are open, without
reconstructing the answer from historical reviews - per
`docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md`.

**This T0 tranche defines contracts only. No catalog record, generator,
checker, gap index, or diagram exists yet.**

## Scope / Applies To

Applies to any future ASC-T1 through ASC-T6 worker, reviewer, or operator
planning catalog implementation. Does not apply to runtime/product code.
Does not implement, modify, or supersede the R91 system-chain map family
(`docs/reference/system_chain/`), frozen doctrine, the module inventory, or
the governance control matrix.

## Family Contents (This Tranche)

| File | Purpose | Status |
|---|---|---|
| `README.md` | this file: family front door | DOC_ONLY_NEW |
| `CVF_AS_BUILT_SYSTEM_CATALOG_SCHEMA.json` | JSON Schema contract: entity types, fields, enums, conditional constraints | DOC_ONLY_NEW |
| `CVF_AS_BUILT_SYSTEM_CATALOG_RECONCILIATION_CONTRACT.md` | precedence, conflict, lineage, negative-search, migration table, admission routing | DOC_ONLY_NEW |
| `CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md` | generated-layout, freshness-ownership, and front-door topology decisions | DOC_ONLY_NEW |

## Relationship To The R91 System-Chain Map Family

This catalog family is **strictly additive** to
`docs/reference/system_chain/`. It does not modify, widen, or re-scope
`CVF_SYSTEM_CHAIN_MAP.json`, its `README.md` companion, the freshness
standard, or `governance/compat/check_system_chain_map_freshness.py`. See
`CVF_AS_BUILT_SYSTEM_CATALOG_TOPOLOGY_DECISIONS.md` Decision 2 and Decision 3
for the exact freshness-ownership and front-door boundary between the two
families.

If you need "is CVF's governance chain wired together for the 5 proven
lanes," read `docs/reference/system_chain/README.md` - that remains the
authority for those 5 lanes. If you need the fuller as-built plane/module/
edge/gap picture this catalog family will eventually provide, that surface
does not exist yet; this README will be updated to route to it once ASC-T1
through ASC-T4 are authorized and implemented.

## Future Routes (Not Yet Implemented)

| Future route | Owning tranche | Status |
|---|---|---|
| Populated catalog entities (`entries/` + generated aggregate) | ASC-T1, ASC-T2 | reserved path only, see Topology Decisions Decision 1 |
| Gap ledger front door and index (`docs/reference/system_chain/gaps/`) | ASC-T3 | reserved path only, roadmap-owned |
| Human as-built architecture front door | ASC-T4 | reserved path only, see Topology Decisions Decision 3 |
| Catalog/gap-index freshness checker | ASC-T5 | reserved path only, see Topology Decisions Decision 2 |
| Independent review and closure | ASC-T6 | not yet opened |

## Governing Documents

- Roadmap: `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md`
- External critique: `docs/reviews/CVF_MSEA_ASC_ARCHITECTURE_CATALOG_ROADMAP_CLAUDE_REBUTTAL_2026-07-11.md`
- Critique classification: `docs/reviews/CVF_MSEA_ASC_CLAUDE_REBUTTAL_CODEX_CLASSIFICATION_2026-07-11.md`
- This tranche's baseline: `docs/baselines/CVF_GC018_MSEA_ASC_T0_SOURCE_SCHEMA_AND_RECONCILIATION_CONTRACT_2026-07-11.md`
- This tranche's work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_ASC_T0_SOURCE_SCHEMA_AND_RECONCILIATION_CONTRACT_2026-07-11.md`

## Claim Boundary

This README is a family front door for a schema/contract-only T0 tranche. It
does not claim any catalog record exists, does not authorize ASC-T1 or later
implementation, and does not modify the R91 system-chain map family.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance T0 design tranche; no public-sync authorization
exists for this family.
