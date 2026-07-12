# CVF GC-018 SOT3-RAP-T0 Reverse Architecture Projection

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Batch ID: SOT3-RAP-T0

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-RAP-T0 --title "Reverse Architecture Projection" --date 2026-07-12 --base 73326a907 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit documentation projection worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Added verified Catalog/GAP owners, projection scope, manifest, evidence, acceptance, and boundaries. |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF disclosure, handoff, scaffold provenance, and Catalog drift checkers |
| docOnlyNewFields | SOT3 projection claim class |
| claimBoundary | Dispatch baseline only; no projection execution proof. |

## Purpose

Authorize one no-commit worker to project accepted SOT3-T2 contract,
owner-candidate, runtime-candidate, and rejected-shape facts into the existing
as-built Catalog and system-chain GAP source families.

## Target / Source

Target owners are the compact source layouts and their generated aggregates.
Accepted SOT3 evidence is fixed at `9c7b05b40`; governance learning is fixed at
`b054829a7`.

## Scope / Methodology

The worker reads current schema/examples, authors only schema-valid compact
entries and front-door updates, runs the existing generator, and returns one
review packet without committing.

## Baseline Decision / Proposed Tranche

Decision: authorize SOT3-RAP-T0 as one bounded documentation/reference
projection tranche. SOT3-RCS-T1 remains held.

## Evidence / Verification

Evidence requires exact accepted commits, schema-valid compact entries,
generator receipts, drift-checker PASS, front-door stable IDs, and reviewer
audit of claim boundaries.

## Allowed Scope

- compact Catalog JSON entries;
- compact GAP JSON entries;
- Catalog and GAP README summaries;
- generated Catalog aggregate and GAP index;
- one SOT3-RAP-T0 worker return.

## Forbidden Scope

- runtime, schema-contract modification, product tests, packages, provider/live;
- changes to generator/checker source or hook catalogs;
- SOT3 Refinery/Kernel/Flow implementation;
- public-sync;
- session/handoff mutation by the worker;
- direct import of retained SOT prototype code.

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Catalog compact entries are editable authority | RUNTIME_BEHAVIOR | `docs/reference/system_architecture_catalog/README.md` | Family Contents | `entries/` | as-built Catalog family | ACCEPT |
| GAP compact entries are editable authority | RUNTIME_BEHAVIOR | `docs/reference/system_chain/gaps/README.md` | Canonical Source | `entries/` | GAP ledger family | ACCEPT |
| Catalog aggregate generator | EXISTS | `governance/compat/generate_as_built_system_catalog.py` | generator constants and builders | `build_catalog_aggregate` | generator | ACCEPT |
| GAP index generator | EXISTS | `governance/compat/generate_as_built_system_catalog.py` | generator constants and builders | `build_gap_index` | generator | ACCEPT |
| Catalog/GAP drift checker | EXISTS | `governance/compat/check_as_built_system_catalog_drift.py` | scoped path constants and main | `main` | drift checker | ACCEPT |
| GAP README must contain every generated gapId | RUNTIME_BEHAVIOR | `governance/compat/check_as_built_system_catalog_drift.py` | README drift validation | `GAP_README_PATH` | drift checker | ACCEPT |
| Accepted T2 contract basis | VALUE_SET | `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` | Disposition | `REVIEWER_ACCEPTED_BOUNDED` | T2 completion review | ACCEPT |
| Review-cost/reverse-projection learning | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Remediation | `reviewRoundCount` | ADIF entry | ACCEPT |
| Reverse-projection closure matrix | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0027.md` | Remediation | `Projection disposition` | ADIF entry | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Reason |
|---|---|---|
| `SOT3 projection claim class` | T0 worker return | distinguish contract/candidate/rejected-shape projection without modifying Catalog schema |

## ADIF Defect Registry Disclosure

Query:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "architecture catalog" --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0014, ADIF-0015,
ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Mandatory direct reads despite zero query matches: `ADIF-0026`, `ADIF-0027`.

## Negative Search And Collision Discipline

| Field | Evidence |
|---|---|
| Search command | `rg -n -i "sot|refinery|truth.kernel|truth.flow|TruthReceipt|cvf.asc.(module|interface|gap).sot" docs/reference/system_architecture_catalog/entries docs/reference/system_chain/gaps/entries docs/reference EXTENSIONS governance .private_reference/legacy` |
| Search roots | Catalog/GAP compact JSON sources; current docs; runtime/extensions; governance source/tests; retained external evidence |
| Coverage | source, tests, docs, JSON, and external/legacy evidence |
| Absent versus collision disposition | every hit is `MATCH_EXISTING_OWNER`, `COLLISION_NON_AUTHORITATIVE`, or `ABSENT_WITH_COMMAND_EVIDENCE`; no bare absence claim |
| Required action | reuse a matching owner; otherwise cite the negative-search receipt before adding a candidate/gap entry |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| SOT3-T2 accepted | `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` | `9c7b05b40` | PASS |
| shared learning committed | ADIF-0026 and ADIF-0027 | `b054829a7` | PASS |
| session next move released | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `add1b1fb3` | PASS |

## Planned Artifact Manifest

| Artifact class | Planned path family | Required result |
|---|---|---|
| Catalog compact entries | `docs/reference/system_architecture_catalog/entries/` | schema-valid bounded SOT3 projection |
| GAP compact entries | `docs/reference/system_chain/gaps/entries/` | three candidate/gap projections with reopen/close conditions |
| Catalog front door | `docs/reference/system_architecture_catalog/README.md` | new stable IDs and bounded claim classes visible |
| GAP front door | `docs/reference/system_chain/gaps/README.md` | new gap IDs/counts/statuses visible |
| generated Catalog aggregate | `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json` | generator-produced only |
| generated GAP index | `docs/reference/system_chain/gaps/CVF_SYSTEM_CHAIN_GAP_INDEX.json` | generator-produced only |
| worker return | `docs/reviews/CVF_SOT3_RAP_T0_WORKER_RETURN_2026-07-12.md` | `COMPLETE_PENDING_REVIEW` |

## Acceptance Criteria

- exact accepted evidence and stable IDs are cited;
- no runtime-existence claim;
- schema, generator, drift checker, worker-return fast gate, and diff hygiene pass;
- reverse projection covers all six T0 Projection Set rows from the roadmap;
- changed set stays within the planned families;
- worker does not commit.

## Fail Conditions

- aggregate-only edit;
- guessed schema field or enum;
- missing GAP README stable ID;
- owner/runtime candidate promoted to active runtime;
- checker/generator modification;
- T1 work mixed into T0.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_as_built_system_catalog_drift.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | DISPATCH_READY; ACCEPT; WORKER_MUST_NOT_COMMIT; Public Export Disposition |
| gateRunPurpose | confirm author-derived bounded T0 dispatch and provide pre-worker evidence |
| claimBoundary | gate conformance does not prove semantic projection correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Catalog/GAP projection.

## Claim Boundary

This baseline authorizes only the matching no-commit T0 work order.
