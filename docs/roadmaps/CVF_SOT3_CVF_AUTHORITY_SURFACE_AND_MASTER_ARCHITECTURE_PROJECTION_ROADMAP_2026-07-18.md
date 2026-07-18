# CVF SOT3 Authority Surface And Master Architecture Projection Roadmap

Memory class: FULL_RECORD

Status: SOT3_CVF_PROJ_T1_CLOSED_PASS_BOUNDED_T2_PACKET_AUTHORING_NEXT

Date: 2026-07-18

Roadmap ID: SOT3-CVF-PROJ

## Authorization / Decision

The operator authorized cleanup of the current workspace and creation of a
fresh worker packet to project the accepted SOT3 capability into CVF-wide
architecture, workflow, navigation, and product information surfaces.

This roadmap does not reopen the closed SOT3 absorption, activation, or
downstream-application roadmaps. It owns documentation and as-built projection
of their accepted bounded results.

## Purpose

Make the accepted SOT3 information lifecycle discoverable and internally
consistent across CVF authority surfaces. The intended cross-surface model is:

`source intake -> Refinery -> Truth Kernel -> Truth Flow -> governed context -> governed execution -> review/freeze -> impact/recall`

The model must preserve these boundaries:

- Refinery prepares source-bound material deterministically and does not create
  truth or call a provider.
- Truth Kernel is the sole SOT3 decision, receipt, and truth-reference owner.
- Truth Flow distributes Kernel-authorized references and manages the
  post-Kernel lifecycle without recreating Refinery or Kernel authority.
- provider output remains downstream content, not a new truth authority.
- bounded application and live proof do not imply production, scale,
  certification, public export, or universal SOT3 coverage.

## Scope / Target / Owner Boundary

In scope:

- CVF master architecture and architecture navigation;
- SOT3 reference front door and activation decision freshness;
- as-built system architecture catalog entries and generated aggregate;
- end-to-end workflow and operator/agent reference navigation;
- root README and technical product catalog claim alignment;
- closure audit across the updated projection surfaces.

Out of scope:

- runtime, package, test, provider, browser/UI, queue, daemon, or production
  changes;
- another live provider call;
- public-sync, push, publication, or certification;
- reopening SOT3 package implementation or application behavior;
- treating the sibling SOT Application repository as CVF canonical authority.

## Non-Goals

- no rewrite of the accepted SOT3 contracts or package behavior;
- no consolidation of every CVF architecture document into one monolith;
- no replacement of the as-built catalog generator with hand-edited output;
- no claim that every CVF use case now runs through SOT3;
- no external-agent adapter, public release, or production-readiness expansion.

## Starting Evidence

| Evidence | Current fact | Projection implication |
|---|---|---|
| `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | accepted bounded closure | three-layer doctrine and packages are accepted boundedly |
| `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | accepted bounded live-governance closure | one CVF product seam has bounded live governance evidence |
| `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | accepted bounded application live-proof closure | one sibling application path has bounded local and live proof |
| `EXTENSIONS/CVF_REFINERY/src/pipeline/engine.ts` | `RefineryEngine`; `REQUIRED_STAGE_CHAIN` | Refinery is implemented, not contract-only |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `TruthKernel.evaluate` | Kernel runtime owner exists |
| `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | `DistributionEngine` | post-Kernel distribution runtime owner exists |
| `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/orchestrator.ts` | `runThreeLayerScenario` | executable three-layer composition exists |
| `docs/reference/system_architecture_catalog/entries/interface.sot_three_layer_contract_chain.v1.json` | still says no SOT3 runtime exists | stale as-built claim requires repair |

## Design Control Gate

| Control | Decision |
|---|---|
| Canonical owner model | SOT3-specific references own detailed contracts; CVF-wide surfaces summarize and link rather than duplicate them |
| Architecture shape | represent SOT3 as a trusted-information lifecycle crossing existing CVF planes, not as a competing top-level framework |
| Workflow shape | distinguish source/truth lifecycle from agent autorun and work-order lifecycle |
| As-built discipline | only source-verified implementation and accepted review evidence may be promoted to as-built |
| Public boundary | private provenance projection only; public export remains separately authorized |
| Runtime boundary | documentation/catalog changes only in this roadmap |

## Tranche Plan

| Tranche | Mission | Primary outputs | Release condition |
|---|---|---|---|
| SOT3-CVF-PROJ-T0 | inventory authority surfaces and stale SOT3 claims | exact surface ledger and no-commit worker return | every named surface has a terminal update/defer/no-change disposition |
| SOT3-CVF-PROJ-T1 | reconcile as-built architecture catalog | source entries, regenerated aggregate, catalog front-door update | no contract-only/no-runtime statement contradicts accepted source |
| SOT3-CVF-PROJ-T2 | refresh master architecture and SOT3 front door | master architecture, architecture map/diagram, SOT3 reference front door | roles, cross-plane placement, boundaries, and proof ladder agree |
| SOT3-CVF-PROJ-T3 | project end-to-end workflow and navigation | operational reference index, architecture navigation, workflow map | operators and agents can locate the correct owner and lifecycle step |
| SOT3-CVF-PROJ-T4 | align product/readme claims and close | README, technical product catalog, final cross-surface audit | all updated claims remain bounded and roadmap closes without stale residue |

T1 is released by the accepted T0 review, the closed CVF Web inheritance
roadmap, and the operator resume instruction dated 2026-07-18. T2 through T4
remain parked until the immediately preceding tranche has committed reviewer
acceptance and a fresh dispatch base.

## Work Plan

1. Dispatch T0 as a read-only audit with exactly two worker-owned review files.
2. Independently review every stale-claim and target-tranche disposition.
3. Author each later tranche from the accepted ledger, with fresh source
   verification and exact write ownership.
4. Update generated catalog aggregates only through their source layout and
   generator.
5. Close with a cross-surface claim and navigation consistency audit.

## Acceptance Criteria

- AC-01: T0 enumerates every required seed surface with zero missing rows.
- AC-02: each row records current authority role, SOT3 freshness, evidence,
  exact target tranche, and a terminal disposition.
- AC-03: false contract-only/no-runtime claims are identified precisely.
- AC-04: detailed SOT3 authority remains in the SOT3 reference family; summary
  surfaces do not create a competing source of truth.
- AC-05: the final architecture shows Refinery, Kernel, Flow, governed context,
  provider, review/freeze, and recall boundaries without authority collapse.
- AC-06: workflow documentation distinguishes information flow, governance
  flow, agent/work-order flow, and product execution flow.
- AC-07: public, production, scale, certification, and universal-support claims
  remain explicitly unclaimed.
- AC-08: generated aggregates pass drift checks and all governed gates pass.

## Verification / Evidence

Each tranche must provide command-backed path, source-symbol, diff, file-size,
and applicable generator/gate evidence. Documentation closure may reuse the
accepted live-proof reviews as evidence; it must not consume another provider
call.

## Dependency And Sequence Control

T0 is released by the operator instruction dated 2026-07-18 and the accepted
SOT3 closures listed in Starting Evidence. Later tranches require the prior
tranche's committed reviewer acceptance and a fresh dispatch base.

## Reverse Architecture Projection Matrix

| Accepted capability | Current projection owner | Current disposition | Planned target | Claim class |
|---|---|---|---|---|
| canonical three-layer contracts | SOT3 reference front door plus two catalog interface entries | UPDATE_EXISTING | T1/T2 | contract and implemented-owner summary |
| Refinery runtime | package source only | ADD_CATALOG_ENTRY | T1 | as-built module |
| Truth Kernel runtime | package source only | ADD_CATALOG_ENTRY | T1 | as-built module |
| Truth Flow runtime | package source only | ADD_CATALOG_ENTRY | T1 | as-built module |
| vertical slice | package source and completion evidence | ADD_CATALOG_ENTRY | T1 | bounded executable composition |
| CVF activation seam | activation decision and accepted reviews | UPDATE_EXISTING | T1/T2/T3 | bounded product integration |
| downstream application proof | closed roadmap and completion review | UPDATE_EXISTING | T2/T4 | bounded sibling proof, not CVF runtime ownership |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | CVF architecture, SOT3 reference, operational index, and catalogs | read-only architecture/navigation authority; no execution permission | accepted source and review evidence listed above | internal documentation references only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP surface is added by this roadmap | no external invocation, mutation, authentication, or public claim | no authorized external adapter tranche | separate source-verified adapter packet required | `DEFERRED_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-design`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture-design --role dispatcher --lifecycle-phase pre-dispatch --surface-selector sot-three-layer --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Status; Authorization / Decision; Purpose; Scope / Target / Owner Boundary; Design Control Gate; Tranche Plan; Work Plan; Acceptance Criteria; Verification / Evidence; Dependency And Sequence Control; Reverse Architecture Projection Matrix; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and dispatch evidence after checker-source read-ahead, not first discovery |
| claimBoundary | read-ahead records structural expectations only; semantic truth still requires source and reviewer verification |

## Epistemic Process Block

### Expected Result / Prediction

CVF-wide architecture and navigation surfaces should lag the rapid SOT3
implementation sequence and contain both omissions and stale bounded claims.

### Evidence Comparison

Direct reads confirm the master whitepaper predates SOT3, the operational and
product indexes omit SOT3, and the as-built catalog still denies runtime that
now exists in source and accepted completion evidence.

### Contradiction Or Gap Disposition

Treat this as a projection/freshness gap. Do not reopen accepted implementation
or infer new runtime behavior.

### Claim Update

The accepted claim is that a fresh projection roadmap is required. Exact edit
scope remains subject to the T0 terminal ledger and independent review.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | prior worker output -> governed CVF completion review -> accepted roadmap closure -> T0 direct source verification -> independent reviewer recomputation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | this roadmap owns projection planning; current CVF runtime source and accepted governed reviews remain factual authority |
| Disposition | N/A with reason: the sibling application is summarized through governed CVF reviews, not promoted as a new external authority |
| Claim boundary | no source mirror, external repository absorption, provider-local memory authority, or public import |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-CVF-PROJ roadmap authoring, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, governance gates |
| Target paths | this roadmap; paired T0 baseline and work order |
| Allowed scope source | operator instruction to clean the workspace and create a worker work order for CVF-wide SOT3 information updates |
| Before status evidence | HEAD `0eee70743`; `git status --short` empty; workspace overlay catalog verified tracked and unchanged |
| After status evidence | roadmap and T0 dispatch packet pending validation and material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | documentation and architecture projection planning only |
| Claim boundary | no runtime, provider/live, public-sync, push, production, browser/UI, queue, or daemon action |
| Agent type | dispatcher |
| Invocation ID | `sot3-cvf-proj-roadmap-2026-07-18` |
| Expected manifest | this roadmap; paired T0 baseline and work order |
| Actual changed set | pending exact three-path material dispatch set |
| Manifest delta | pending pre-commit verification |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CVF-wide SOT3 documentation and as-built projection roadmap |
| claimDisposition | N/A with reason: roadmap authoring does not execute or enforce runtime behavior |
| receiptEvidence | N/A with reason: accepted prior closure artifacts are reused; this roadmap creates no runtime receipt |
| actionEvidence | N/A with reason: roadmap authoring performs no runtime action |
| invocationBoundary | dispatcher and future bounded workers |
| interceptionBoundary | no shell, IDE, provider, filesystem, or agent-action interception claim |
| claimLanguage | planned projection, source-verified update, and bounded evidence reuse |
| forbiddenExpansion | runtime implementation, live call, public-sync, push, production, certification, and universal SOT3 claims |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap updates private provenance authority surfaces. Public-safe
export requires a separate public-sync authorization and evidence set.

## Claim Boundary

T0 and T1 are independently accepted. T1 updates the bounded private
as-built catalog and reference navigation only; it does not change runtime,
provider behavior, production state, or public surfaces. T2 packet authoring
is released. T3 and T4 remain parked behind sequential reviewer acceptance.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | T1 GC-018 baseline | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| Work order status | T1 work order | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_CVF_PROJ_T1_COMPLETION_REVIEW_2026-07-18.md` | `Status: REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | PASS |
| Worker return | T1 worker return | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIR` | PASS |
| Roadmap state | this roadmap | `Status: SOT3_CVF_PROJ_T1_CLOSED_PASS_BOUNDED_T2_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | existing GC-051 registry aggregate | changed-corpus coverage and aggregate drift PASS | PASS |
| Registry Markdown | existing registry front door | existing family coverage remains sufficient | PASS |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate successor-dispatch sync | N/A with reason |

## Current Runtime Freshness Verification

Direct source reads confirm the bounded SOT3 runtime owners named by T1. CVF
also has an existing provider registry at
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`, including
`PROVIDER_CAPABILITY_REGISTRY`; this roadmap neither denies nor modifies that
surface. Provider routing remains outside the documentation/catalog projection
scope, and no absence claim is made about it.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| runtime receipt evidence | N/A with reason: T1 catalog reconciliation creates no runtime receipt | N/A_WITH_REASON |
| provider query evidence | N/A with reason: no provider call was authorized | N/A_WITH_REASON |
| T1 worker-return acceptance | independently recomputed with one bounded provenance repair | PASS |
| T1 closure claim | private-provenance catalog truth only | PASS |
