# CVF GC-018 Baseline - SOT3 CVF Authority Surface Inventory And Staleness Audit

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-18

Batch ID: SOT3-CVF-PROJ-T0

dispatchBaseHead: `0eee70743`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one documentation-only worker to inventory the exact CVF authority
and navigation surfaces that must be refreshed after accepted SOT3 package,
activation, and downstream-application closure.

## Proposed Tranche / Decision

Decision: release T0 read-only audit with exactly two worker-owned review
outputs. The worker must not edit any architecture, catalog, README, runtime,
test, registry, generated aggregate, session, or handoff surface.

## Scope / Target / Owner Boundary

Allowed writes:

- `docs/reviews/CVF_SOT3_CVF_PROJ_T0_AUTHORITY_SURFACE_INVENTORY_AND_STALENESS_LEDGER_2026-07-18.md`
- `docs/reviews/CVF_SOT3_CVF_PROJ_T0_WORKER_RETURN_2026-07-18.md`

All other paths are read-only or forbidden.

## Authority Surface Seed Manifest

The ledger must contain one terminal row for each exact seed:

1. `README.md`
2. `ARCHITECTURE.md`
3. `CVF_ECOSYSTEM_ARCHITECTURE.md`
4. `docs/CVF_ARCHITECTURE_DECISIONS.md`
5. `docs/reference/CVF_MASTER_ARCHITECTURE_WHITEPAPER.md`
6. `docs/reference/CVF_ARCHITECTURE_MAP.md`
7. `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`
8. `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
9. `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
10. `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md`
11. `docs/reference/sot_three_layer/README.md`
12. `docs/reference/sot_three_layer/CVF_SOT3_ACTIVATION_ARCHITECTURE_DECISION.md`
13. `docs/reference/system_architecture_catalog/README.md`
14. `docs/reference/system_architecture_catalog/entries/interface.sot_three_layer_contract_chain.v1.json`
15. `docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json`

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Refinery runtime owner exists | EXISTS | `EXTENSIONS/CVF_REFINERY/src/pipeline/engine.ts` | lines 23, 48, 86 | `RefineryEngine`; `REQUIRED_STAGE_CHAIN` | Refinery pipeline | ACCEPT |
| Truth Kernel runtime owner exists | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | lines 49-55, 83 | `TruthKernel`; `evaluate` | Truth Kernel | ACCEPT |
| Truth Flow runtime owner exists | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | class declaration and lifecycle methods | `DistributionEngine` | Truth Flow distribution | ACCEPT |
| three-layer composition exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/orchestrator.ts` | line 52 and composition body | `runThreeLayerScenario` | SOT3 vertical slice | ACCEPT |
| as-built contract entry denies current runtime | LITERAL_INVARIANT | `docs/reference/system_architecture_catalog/entries/interface.sot_three_layer_contract_chain.v1.json` | `claimBoundary`; `boundaryCaveat` | `cvf.asc.interface.sot_three_layer_contract_chain.v1` | as-built system catalog entry | ACCEPT |
| SOT3 application live proof is accepted boundedly | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` | status and reviewer decision | `SOT3_APP_T5_LIVE_PROOF_PASS` | T5 completion review | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
|---|---|
| `surfaceClass` | classify each seed as front door, architecture, operational, product, SOT3 owner, or generated catalog |
| `sot3Freshness` | terminal value `CURRENT`, `STALE`, `MISSING`, or `NO_CHANGE_WITH_REASON` |
| `targetTranche` | route accepted update work to T1, T2, T3, T4, or `NONE_WITH_REASON` |
| `editDisposition` | terminal value `UPDATE`, `ADD_POINTER`, `REGENERATE_FROM_SOURCE`, `DEFER_WITH_REASON`, or `NO_CHANGE_WITH_REASON` |

## Verification / Evidence

- all 15 seed paths must exist and be read in full;
- every row must cite current section/line or JSON field evidence;
- all SOT3-related statements must be compared against current runtime source
  and accepted closure evidence;
- ledger totals must reconcile to 15 terminal seed rows;
- stale-claim count, missing-navigation count, update count, and no-change count
  must reconcile to the same denominator;
- `git status --short` must show only the two allowed untracked review paths;
- worker-return fast gate and pre-implementation autorun must pass.

## Acceptance Criteria

- AC-01: 15/15 seed rows are terminal and evidence-backed.
- AC-02: zero seed path is unread, silently omitted, or grouped into a range.
- AC-03: the stale no-runtime catalog claim is explicitly routed to T1.
- AC-04: master architecture, workflow/navigation, and product/readme work are
  separated into T2, T3, and T4 instead of one uncontrolled edit batch.
- AC-05: no worker edit occurs outside the two review outputs.
- AC-06: no public, production, provider/live, runtime, test, generated-state,
  registry, session, or push action occurs.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T0 ledger and worker return | read-only architecture audit; no mutation authority | exact seed manifest and source reads | internal review artifacts only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter output | no CLI/MCP invocation or support claim | no authorized adapter scope | separate future packet required | `DEFERRED_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-design`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture-design --role dispatcher --lifecycle-phase pre-dispatch --surface-selector sot-three-layer --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Purpose; Proposed Tranche / Decision; Scope / Target / Owner Boundary; Authority Surface Seed Manifest; Source Verification Block; New Doc-Only Fields; Verification / Evidence; Acceptance Criteria; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and dispatch evidence after checker-source read-ahead, not first discovery |
| claimBoundary | structural read-ahead only; source truth and ledger semantics remain independently reviewable |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-CVF-PROJ-T0 --title "SOT3 CVF Authority Surface Inventory And Staleness Audit" --date 2026-07-18 --base 0eee70743 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact authority, source, scope, output, evidence, and boundary requirements |
| checkerReadAheadConfirmation | applicable checkers are listed in the read-ahead block |
| docOnlyNewFields | `surfaceClass`; `sot3Freshness`; `targetTranche`; `editDisposition` |
| claimBoundary | dispatch-authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T0 is a private provenance audit and does not authorize public-sync.

## Claim Boundary

This baseline authorizes the exact T0 audit and two review outputs only. It
does not authorize architecture/catalog/README edits, generated aggregate
mutation, runtime/provider/live actions, public-sync, push, or later tranches.
