# CVF GC-018 Baseline - EAIC KR T3 Owner Architecture And Threat Model

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_WITH_REPAIRS_OPERATOR_SELECTION_ACCEPTED_T4_PARKED

docType: baseline

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T3

dispatchBaseHead: `a230678aa`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: worker role selected by operator through manual copy/paste

## Purpose

Release one documentation-only worker to compare source-verified owner
architectures and produce an EAIC admission-monitor-stop-reconcile threat
model. This baseline authorizes decision support, not runtime-owner
ratification, implementation, external-agent invocation, or moratorium lift.

## Scope / Target / Owner Boundary

Risk ceiling: R0 documentation and repository-local evidence only.

Allowed scope:

- read the EAIC-KR roadmap, accepted T2 contract and review, current runtime
  source, canonical contracts, and checker sources listed in the work order;
- compare at least three owner-architecture candidates;
- recommend one accountable architecture pattern while keeping final operator
  selection explicit;
- map D1-D6 and GAP-01 through GAP-09 to owner responsibilities, trust
  boundaries, threats, mitigations, residual gaps, and negative proof needs;
- create exactly the two worker outputs named in the paired work order;
- run repository-local governance checks.

Forbidden scope:

- CLI/MCP invocation, external-agent launch, provider/API/account use, secret,
  paid query, quota use, browser, network, or process-control action;
- runtime, source, test, checker, hook, registry, session, public-sync,
  deployment, or production mutation;
- provider/model selection or hard-coding;
- treating provider-native internal helpers as independently governed merely
  because the parent agent uses them;
- worker staging, committing, pushing, publishing, deleting, or renaming.

## Audit Finding

T2 has defined provider-neutral policy semantics, while nine architecture and
proof gaps remain. Direct source inspection confirms reusable primitives but
does not prove a complete EAIC owner:

| Candidate surface | Existing bounded capability | Missing EAIC proof |
| --- | --- | --- |
| governed command launcher | consumes preflight receipts, records execution intent and durable execution outcomes | universal external-agent interception, provider-session binding, cumulative assignment telemetry, and complete stop control |
| governed session contract | policy evaluation, limits, identity and audit receipt primitives | process launch ownership, process-tree binding, host telemetry, and termination |
| Model Gateway execution bridge | provider/model routing, quota decision, adapter execution and gateway receipts | parent assignment process lifecycle, CLI/MCP mediation, descendant stop, and cross-retry aggregation |
| new EAIC coordinator composition | can assign one accountable owner above existing primitives | interface, storage, adapter, monitoring, stop, and proof design do not yet exist |

The evidence supports bounded architecture comparison. It does not support
silently declaring any current component the universal runtime owner.

## T3 Decision Boundary

| Decision | Worker authority | Final authority |
| --- | --- | --- |
| compare candidate owners | AUTHORIZED | reviewer verifies evidence |
| recommend one accountable pattern | AUTHORIZED_AS_RECOMMENDATION | operator accepts, rejects, or parks |
| name reusable components and required adapters | AUTHORIZED_AS_DOCUMENTATION | later source-verified roadmap governs implementation |
| ratify runtime owner | FORBIDDEN | operator only |
| authorize T4 | FORBIDDEN | reviewer and operator after accepted T3 evidence |
| lift invocation moratorium | FORBIDDEN | fresh explicit operator decision |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | authorized parent agent session | provider-native helpers inherit parent scope unless they independently cross the governed perimeter | EAIC-KR roadmap, Agent Internal Autonomy And Invocation Perimeter | no per-helper admission or adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | candidate EAIC coordination boundary | no launch, provider/account use, process action, runtime mutation, or live proof is authorized | T2 semantics plus current source inventory | adapter architecture may be proposed; implementation remains deferred | `DEFERRED_WITH_REASON` |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| accepted T2 closure | `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_COMPLETION_REVIEW_2026-07-23.md`; material commit `9322829fb` | T2 semantics must be independently accepted | SATISFIED |
| T3 operator authorization | operator message `tiep` on 2026-07-23 after T2 closure | authorize packet authoring only | SATISFIED_FOR_DISPATCH_AUTHORING |
| current source candidates | source symbols listed in Source Verification Block | at least three bounded candidates must be source-verified | SATISFIED |
| invocation moratorium | roadmap and active handoff | no external or runtime action | SATISFIED_AND_RETAINED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "external-agent invocation architecture" --risk-ceiling HIGH --max-results 50 --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044.

Dispatch impact: the packet applies source verification, explicit
session-start and dispatch provenance, exact write ownership, no-commit
conversion, checker read-ahead, and the invocation moratorium.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm documentation-only dispatch shape and allowed-scope repairs |
| claimBoundary | checker compliance proves document structure, not architecture correctness or runtime effectiveness |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAIC-KR-T3 --title "EAIC KR T3 Owner Architecture And Threat Model" --date 2026-07-23 --base a230678aa --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic documentation-only no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added T2 release evidence, source-backed candidate surfaces, decision boundary, exact manifests, threat-model requirements, and moratorium controls |
| checkerReadAheadConfirmation | applicable checker sources and canonical work-order contracts were inspected before writing |
| docOnlyNewFields | candidateId; accountableOwnerPattern; componentRole; trustBoundary; threatId; mitigationOwner; residualGap; operatorSelectionState |
| claimBoundary | dispatch-authoring provenance only; no runtime, provider, public, or external-agent behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 objective is owner architecture and threat-model selection | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, T3 row | `T3` | EAIC-KR roadmap | ACCEPT |
| T2 defines policy but does not select an architecture owner | LITERAL_INVARIANT | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md` | Purpose; D1 Admission-owner and implementation gap | `OWNER_SURFACE_NOT_FOUND` | T2 policy semantics | ACCEPT |
| command launcher accepts a preflight receipt and emits execution evidence | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 168-186, 274-359 | `launchGovernedCommand` | governed command launcher | ACCEPT |
| preflight evaluates and persists an admission receipt but does not prove execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 181-296 | `preflightGovernanceAction` | governance action preflight | ACCEPT |
| receipt consumption supports one-time claim semantics | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 36-73 | `claimReceipt` | `JsonReceiptConsumptionStore` | ACCEPT |
| governed execution store begins and finalizes durable execution records | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 13-59 | `GovernedExecutionStore` | `JsonGovernedExecutionStore` | ACCEPT |
| governed session contract owns policy, limits, identity, and audit receipt primitives | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | lines 28-47, 141, 212-239, 322-386 | `AgentGovernedSessionContract` | governed session contract | ACCEPT |
| Model Gateway bridge checks quota, invokes a selected adapter, and builds a receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 59-73, 97-220 | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |
| Model Gateway quota is keyed by provider and model usage | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | lines 30-100 | `QuotaLedger` | quota ledger | ACCEPT |
| gateway receipt carries provider and selected-model evidence | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | lines 7-59, 67-112 | `GatewayReceipt` | `GatewayReceiptBuilder` | ACCEPT |
| internal helpers remain autonomous until they cross a governed perimeter | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter | `INTERNAL_AGENT` | EAIC-KR roadmap | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| worker output path existence | both worker-owned output paths are absent before dispatch | ACCEPT |
| current universal EAIC owner | no source-backed component in this packet is claimed to cover all D1-D6 and GAP-01 through GAP-09 | ACCEPT |
| new field collision | all proposed architecture fields are doc-only | ACCEPT |
| provider/model collision | no provider or model is selected or hard-coded | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: T3 uses current repo-local governed sources and absorbs no new external material |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_invocation_control/` |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | external knowledge acquisition requires a separate operator-approved intake packet |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: existing components would cover bounded portions
of the control chain but no single current source would prove complete EAIC
ownership.

Evidence Comparison Requirement: compare launcher-centric,
session-contract-centric, gateway-centric, and composed-coordinator options
against the same D1-D6, GAP-01 through GAP-09, and threat criteria.

Contradiction Handling Requirement: a candidate with a useful primitive cannot
be promoted to complete owner when required process, telemetry, stop, or
receipt evidence is absent.

Claim Update Requirement: recommend, park, or return NOT_READY based on source
coverage. Never manufacture a runtime capability to keep T3 moving.

## Baseline Decision

`REVIEWER_ACCEPTED_WITH_REPAIRS_OPERATOR_SELECTION_ACCEPTED_T4_PARKED`

The documentation worker return is independently accepted after bounded
source, proof-verdict, and command-signature repairs. The operator accepted
CANDIDATE-D as the architecture direction on 2026-07-23. This decision does
not authorize T4 or implementation; all external/runtime action remains held.

## Verification / Evidence

- clean packet-authoring base: `a230678aa`;
- T2 material closure commit: `9322829fb`;
- worker output paths absent before authoring;
- no external invocation, provider call, network action, or process under
  study occurred during this audit;
- pre-dispatch results are recorded after authoring and before commit.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | REPOSITORY_SOURCE_INSPECTION_ONLY |
| reason | current runtime source is read only to bound architecture candidates |
| requiredFutureAction | any runtime claim needs a later roadmap, GC-018, source-verified work order, operator authorization, implementation, and applicable live proof |

## Claim Boundary

This baseline authorizes one documentation-only comparison and threat model.
It does not ratify an owner, invoke an agent, control a process, measure live
quota, implement runtime, select a provider/model, authorize T4, lift the
moratorium, or establish public, security, cost, production, or live readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private architecture decision-support packet with no public
implementation or release evidence.
