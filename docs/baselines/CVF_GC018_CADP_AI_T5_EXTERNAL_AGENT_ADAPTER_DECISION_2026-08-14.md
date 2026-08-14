# CVF GC-018 Baseline - CADP-AI-T5 External Agent Adapter Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-14

Batch ID: CADP-AI-T5D

Dispatch base head: `17104935f442e63aba6a209faeaf31781c36d2e9`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

Worker target: decision-audit worker role

## Purpose

Authorize a documentation-only decision audit for the optional CADP external-
agent adapter lane. The worker must decide whether current CVF authority can
support a bounded read/query metadata interface, or whether T5 must be rejected
or deferred with an evidence-backed reason.

## Authorization

The operator's 2026-08-14 `next` direction releases T5 decision analysis only
after bounded T4 closure. It does not authorize adapter implementation, MCP or
CLI invocation, external-agent launch, mutation, provider/live execution,
credentials, public sync, deployment, or production.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T4 accepted bounded | `docs/reviews/CVF_CADP_AI_T4_AUTHORITY_BOUNDARY_MACHINE_ENFORCEMENT_COMPLETION_2026-08-14.md`; material commit `7dfee6e4d77d1fe1102f627869c20e176f630304` | independent acceptance plus explicit operator direction | ACCEPT |
| T5 roadmap decision lane | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`, Work Plan T5 | accepted T3/T4 plus operator authorization | ACCEPT_FOR_DECISION_ONLY |

## Scope

- inventory the current CADP T1/T3A/T3B/T4 interfaces relevant to a read-only
  external consumer;
- reconcile the generic advisory MCP guide, existing MCP bridge boundary,
  ASSF external-agent readout boundary, and current external-agent invocation
  moratorium;
- evaluate authentication, ingress validation, mutation denial, redaction,
  dual-agent accounting, receipt, and package/discoverability prerequisites;
- return exactly one terminal recommendation:
  `IMPLEMENTATION_READY_BOUNDED_READ_ONLY`, `REJECT_WITH_REASON`, or
  `DEFER_WITH_MISSING_AUTHORITY`;
- create a decision assessment and worker-return packet only.

## Non-Goals

No production source, tests, schema, checker, hook, autorun, CI, MCP tool, CLI
command, runtime adapter, provider call, external-agent process, credential,
network, public-sync, deployment, roadmap closure, session sync, staging, or
commit mutation.

## Decision Test

`IMPLEMENTATION_READY_BOUNDED_READ_ONLY` is allowed only if current governed
sources identify an owner and fail-closed contract for authentication, input
validation, field allowlisting/redaction, zero mutation/activation/execution
authority, deterministic error/receipt semantics, and both internal-agent and
external-agent surfaces. Any missing prerequisite requires rejection or
deferral; absence may not be filled with worker-designed semantics.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T5 is optional and requires an explicit adapter decision | ROADMAP_BOUNDARY | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` | Work Plan T5 | `CLI/MCP read/query interface or explicit rejection` | CADP-AI roadmap | ACCEPT |
| CADP T4 is accepted standalone and unwired | CLOSURE_EVIDENCE | `docs/reviews/CVF_CADP_AI_T4_AUTHORITY_BOUNDARY_MACHINE_ENFORCEMENT_COMPLETION_2026-08-14.md` | final disposition and claim boundary | `Final Disposition` | independent T4 review | ACCEPT |
| generic MCP integration is advisory and grants no runtime execution authority | LITERAL_INVARIANT | `docs/guides/CVF_GENERIC_MCP_ADAPTER_INTEGRATION_GUIDE_2026-05-31.md` | Protocol and Claim Boundary | `runtimeExecutionAuthorized` | generic MCP integration guide | ACCEPT |
| existing MCP-to-Model-Gateway work is a boundary, not implementation authority | ROADMAP_BOUNDARY | `docs/baselines/CVF_GC018_RTAD_T5_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY_2026-06-18.md` | Forbidden Scope and Claim Boundary | `CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY` | RTAD-T5 boundary | ACCEPT |
| external-agent readout requires separate adapter evidence | LITERAL_INVARIANT | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md` | Source Verification and Dual Agent Surface Matrix | `EXTERNAL_AGENT_CLI_MCP` | ASSF external-agent boundary | ACCEPT |
| external-agent invocation implementation remains under moratorium | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, Release Rules, Next Allowed Move | `NOT_OPENED_NO_IMPLEMENTATION_AUTHORITY` | external-agent invocation-control roadmap | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Dependency Release Evidence`; `Source Verification Block`; `Dual Agent Surface Matrix`; `External Knowledge Intake Routing`; `Delta Execution Claim Boundary Control Block`; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirm exact dispatch and decision-return structure before authoring |
| claimBoundary | structural checker read-ahead does not prove T5 readiness or adapter safety |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id CADP-AI-T5 --title "CADP AI T5 External Agent Adapter Decision" --date 2026-08-14 --base 17104935f442e63aba6a209faeaf31781c36d2e9 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T4 accepted bounded at 7dfee6e4d77d1fe1102f627869c20e176f630304" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with decision-only scope, terminal enum, current source authority, exact two-path worker manifest, and no-runtime boundary |
| checkerReadAheadConfirmation | checker sources in the preceding block were read before governed authoring |
| docOnlyNewFields | `terminalRecommendation`; `prerequisiteDisposition`; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no MCP, CLI, runtime, provider, or adapter behavior is implemented |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Exact path existence | all four proposed T5 artifact paths returned `False` before authoring | ABSENT_BEFORE_AUTHORING |
| Exact title token | focused `rg --fixed-strings` across active governed roots returned no match | NO_EXACT_COLLISION |
| Collision decision | prior MCP, ASSF, RTAD, and invocation-control artifacts are mandatory inputs with different owners; none is CADP T5 authority | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; canonical source and no-runtime boundaries remain mandatory |

## MCP/CLI Adapter Boundary

| Field | Value |
|---|---|
| Adapter scope | decision evidence for a possible future read/query metadata adapter only |
| No-runtime-overclaim | this packet does not claim an adapter executes, intercepts, wraps, launches, or mutates any runtime command |

## Acceptance Criteria

- exact two-path worker manifest and no other changes;
- every prerequisite has source evidence and one terminal disposition;
- decision distinguishes read/query metadata from launch, execution, mutation,
  activation, provider, credential, and secret-resolution authority;
- unknown or missing ownership fails closed into rejection or deferral;
- dual-agent, external-knowledge, delta-claim, and public-export blocks are
  complete;
- worker return passes the full worker-return fast gate with staging empty and
  HEAD unchanged.

## Decision / Baseline

Proceed with one documentation-only independent T5 decision audit. No adapter
implementation is released by this baseline or by a positive recommendation.

## Evidence / Verification

Dispatch evidence consists of exact current-source citations, the T4 material
closure anchor, real ADIF and collision searches, scaffold provenance, focused
dispatch gates, exact pending manifest, and diff hygiene. These prove dispatch
shape only; the worker and independent reviewer still own the T5 decision.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: operator selected a repo-local governed decision lane and supplied no external artifact |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | CVF-governed repository sources remain the only authority for this decision |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | CADP T5 documentation-only adapter decision dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, interception, or adapter behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or external-agent action occurs |
| invocationBoundary | local read-only inspection and governed document authoring only |
| interceptionBoundary | no wrapper, proxy, runtime gate, MCP/CLI tool, or process interception |
| claimLanguage | dispatch-ready decision audit only |
| forbiddenExpansion | no implementation, provider/live, credential, external launch, public, deployment, T6, or T7 action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision packet; no public artifact or sync action
is authorized.

## Claim Boundary

This baseline authorizes evidence collection and a bounded recommendation only.
It does not authorize or prove authentication, MCP/CLI behavior, external-agent
invocation, runtime interception, mutation, redaction effectiveness, provider
compatibility, live behavior, deployment, public readiness, or production use.
