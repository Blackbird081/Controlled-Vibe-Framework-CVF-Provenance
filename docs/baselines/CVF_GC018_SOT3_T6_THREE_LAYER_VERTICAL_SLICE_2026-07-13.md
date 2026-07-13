# CVF GC-018 Baseline - SOT3-T6 Three-Layer Vertical Slice

Memory class: FULL_RECORD

Status: PROPOSED_PRE_DISPATCH

Date: 2026-07-13

Baseline ID: GC-018-SOT3-T6

## Purpose

Authorize a bounded deterministic integration slice across the accepted
Refinery, Truth Kernel, and Truth Flow packages without duplicating layer logic.

## Target / Source

Target: a new `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/` integration package and
one worker-return packet. Sources are the accepted T2 contracts and the public
exports of the three accepted packages.

## Scope / Methodology

Build three deterministic scenarios (`INTERNAL`, `PROJECT`, `MARKET_SOURCE`)
that invoke the real package APIs in sequence. Preserve observable source,
scope, conflict, evidence, decision, receipt, reference, route, dose, and
lifecycle evidence. The integration layer may orchestrate and serialize
evidence only; it must not normalize, decide truth, or distribute independently.

## Findings / Position

T3-T5 provide separate accepted owners. T6 is valuable only if it proves their
contract chain using real instances and fail-closed negative cases. A parallel
business framework, adapter, provider path, or fourth authority layer is out of
scope.

## Risk / Corrective Action

Primary risks are fixture-only proof, reimplemented layer logic, stale Kernel
authority, and evidence loss between package boundaries. Require real public
APIs, dependency scans, deterministic outputs, and a single reviewer dependency
matrix before repair.

## Decision / Baseline / Proposed Tranche

PROPOSED: one no-commit T6 integration tranche after pre-dispatch passes.

## Evidence / Verification

Require tests, strict typecheck, deterministic-output comparison, forbidden
dependency scan, changed-path evidence, and no-commit status.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| deterministic Refinery entry | `EXTENSIONS/CVF_REFINERY/src/index.ts` | public exports | `RefineryEngine` | `RefineryEngine.run` | EXISTS | ACCEPT |
| Refinery input contract | `EXTENSIONS/CVF_REFINERY/src/pipeline/engine.ts` | `RefineryRunInput` | `RefineryRunInput` | `RefineryEngine.run` | EXISTS | ACCEPT |
| Kernel evaluation entry | `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts` | public exports | `TruthKernel` | `TruthKernel.evaluate` | EXISTS | ACCEPT |
| Kernel evaluation input | `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | `EvaluateInput` | `EvaluateInput` | `TruthKernel.evaluate` | EXISTS | ACCEPT |
| Flow distribution entry | `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` | public exports | `DistributionEngine` | `DistributionEngine.create` | EXISTS | ACCEPT |
| Flow feedback entry | `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` | public exports | `FeedbackEngine` | `FeedbackEngine` | EXISTS | ACCEPT |
| three scenario classes and preserved evidence chain | `docs/roadmaps/CVF_SOT_THREE_LAYER_ABSORPTION_ROADMAP_2026-07-12.md` | Tranche Plan, SOT3-T6 | `SOT3-T6` | roadmap release condition | DOC_ONLY_NEW | ACCEPT |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| T3 Refinery | `EXTENSIONS/CVF_REFINERY/` | accepted predecessor in roadmap | SATISFIED |
| T4 Kernel plus T4R1 | `EXTENSIONS/CVF_TRUTH_KERNEL/` | `cda8fec64` | SATISFIED |
| T5 Flow | `docs/reviews/CVF_SOT3_T5_COMPLETION_REVIEW_2026-07-13.md` | `8a653370a` | SATISFIED |

## Acceptance Criteria

- Three scenario classes traverse real Refinery, Kernel, and Flow instances.
- Evidence chain preserves source, scope, conflict, receipt, reference, route,
  dose, and final lifecycle state.
- Negative cases prove failed Refinery output cannot enter Kernel, non-released
  Kernel outcome cannot create Flow distribution, and stale/non-active
  references fail closed at action time.
- Repeated identical inputs and injected clocks/IDs produce byte-equivalent
  canonical evidence.
- No AI, agent, prompt, provider, network, database, UI, activation, adapter,
  or public-sync dependency is introduced.
- No implementation is copied from the retained legacy roots.

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker and reviewer | local files and commands | no-commit, integration package only | tests, scans, worker return | local process |
| EXTERNAL_AGENT_CLI_MCP | future worker | same governed packet | no provider or MCP authority | locally revalidated evidence | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Source Verification Block; Dependency Release Evidence; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm pre-read packet shape and source-fidelity evidence before dispatch |
| claimBoundary | checker success does not prove integration behavior |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Chain map route | accepted owner packages -> deterministic integration proof |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T6 packet |
| Disposition | NOT_APPLICABLE_WITH_REASON: no new external intake |
| Claim boundary | T6 does not re-absorb retained sources |

## Finding-To-Governance Learning Disposition

NOT_APPLICABLE_WITH_REASON: no new repeated defect is asserted at dispatch.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: this baseline authorizes future executable
proof and makes no new measured runtime claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private-provenance implementation baseline.

## Claim Boundary

This baseline authorizes only local deterministic T6 implementation after a
passing pre-dispatch gate. It does not authorize T7, package activation,
adapters, provider/live work, public-sync, release, or production claims.
