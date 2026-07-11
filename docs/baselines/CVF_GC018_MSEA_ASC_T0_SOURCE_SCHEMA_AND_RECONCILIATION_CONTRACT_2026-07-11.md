# CVF GC-018 MSEA-ASC-T0 Source Schema And Reconciliation Contract

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-ASC-T0

Dispatch base head: `4c1abb6ff`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize a documentation/schema-only worker tranche that defines the source
schema, vocabulary, reconciliation contract, generated-layout decision,
migration plan, freshness topology decision, and human-front-door topology for
the future CVF as-built architecture catalog.

## Scope / Target / Owner Boundary

The worker may create exactly the T0 reference/schema outputs and worker return
named by the paired work order. It may read all cited current sources. It may
not inventory the full repository, populate the catalog, create gap entries or
index aggregates, implement a generator/checker, change R91 semantics, update
human architecture diagrams, mutate runtime, or commit.

## Decision / Baseline / Proposed Tranche

The MSEA-ASC roadmap and critique classification are accepted planning inputs.
T0 must make schema-time decisions before T1-T5 implementation, especially:

- entity/field/enum vocabulary and stable-ID grammar;
- proof-class, evidence-recency, and operator-visibility separation;
- reconciliation precedence among current governed views;
- compact-source/generated-aggregate topology;
- R91 five-lane versus catalog freshness ownership boundary;
- dedicated as-built front-door versus R91 README boundary.

## Evidence / Verification

Current R91 freshness code binds one five-lane map through `MAP_PATH`,
`EXPECTED_LANE_COUNT`, and `CANONICAL_LANE_IDS`. T0 must not claim unchanged
reuse for an N-entity catalog. The generated-aggregate standard requires a
compact source layout, deterministic generator, and drift check when a future
aggregate is implemented; T0 records the contract but does not implement it.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-ASC-T0 --title "Source Schema And Reconciliation Contract" --date 2026-07-11 --base 4c1abb6ff --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact T0 schema/design-only outputs and no-implementation boundary |
| checkerReadAheadConfirmation | dispatch, handoff, trace, roadmap, source verification, external routing, public, closure guards |
| docOnlyNewFields | catalog entity/field/enum vocabulary and topology decisions named in T0 outputs |
| claimBoundary | scaffold provenance only |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| MSEA-ASC roadmap | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | `6485fc7ad` | SATISFIED |
| external critique classified | `docs/reviews/CVF_MSEA_ASC_CLAUDE_REBUTTAL_CODEX_CLASSIFICATION_2026-07-11.md` | `6485fc7ad` | SATISFIED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0 requirements | VALUE_SET | `docs/roadmaps/CVF_AS_BUILT_ARCHITECTURE_AND_SYSTEM_CATALOG_ROADMAP_2026-07-11.md` | ASC-T0 | ASC-T0 - Source Schema And Reconciliation Contract | roadmap | ACCEPT |
| five-lane map binding | VALUE_SET | `governance/compat/check_system_chain_map_freshness.py` | module constants | MAP_PATH; EXPECTED_LANE_COUNT; CANONICAL_LANE_IDS | R91 freshness checker | ACCEPT |
| generated aggregate requirements | VALUE_SET | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Protocol / Contract / Requirements | compact source layout; deterministic generator; drift check | generated aggregate discipline | ACCEPT |
| current L1 owner disposition | VALUE_SET | `docs/reviews/CVF_MSEA_R99_L1_SYSTEM_DEFINITION_OWNER_DESIGN_COMPLETION_2026-07-11.md` | Findings / Position | ACTIVE_OWNER_CREATED_WITH_BOUNDARY | R99 review | ACCEPT |
| current L2 owner disposition | VALUE_SET | `docs/reviews/CVF_MSEA_R98_L2_BUILD_PROTOCOL_OWNER_RATIFICATION_COMPLETION_2026-07-11.md` | Findings / Position | NAMED_DIFFERENTLY_ACTIVE_OWNER_WITH_BOUNDARY | R98 review | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: schema and documentation contract only; no runtime claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | none |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; source table; roadmap trace; worker return; public disposition |
| gateRunPurpose | confirmation and evidence after source-backed packet authoring; not first discovery |
| claimBoundary | T0 dispatch authorization only |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Define the architecture-catalog schema and reconciliation decisions without implementing the catalog. |
| scopeClassification | DOCUMENTATION_AND_SCHEMA_ONLY |
| riskSensitivity | R1 |
| selectedRouteMode | DELEGATED_WORKER_REVIEWER_CLOSER |
| roleSeparationBasis | worker returns uncommitted outputs; Codex independently reviews and closes |
| escalationCondition | any checker/runtime/public/provider/diagram/catalog-population requirement |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | dispatcher/reviewer/closer | governed packet, source, gates | CVF sources control acceptance | source citations, diff, gates | ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | delegated worker | local filesystem and shell | advisory implementation return; no commit/authority | worker return and exact manifest | ALLOWED_BOUNDED_NO_COMMIT |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance schema planning.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| owner family | `docs/reference/system_architecture_catalog/` |
| schema artifact | JSON Schema contract, not populated aggregate |
| compact-source decision | documented in T0; implementation deferred to T3 |
| generator/checker | paths reserved by decision; files not implemented in T0 |
| generated aggregate impact | none in T0 |

## Claim Boundary

T0 defines contracts and topology decisions only. It does not prove catalog
coverage, implement freshness, populate gaps, or authorize later tranches.
