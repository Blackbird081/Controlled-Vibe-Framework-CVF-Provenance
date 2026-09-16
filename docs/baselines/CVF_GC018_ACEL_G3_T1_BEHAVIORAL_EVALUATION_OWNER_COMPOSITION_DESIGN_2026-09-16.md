# CVF GC-018 Baseline - ACEL G3 T1 Behavioral Evaluation Owner Composition Design

Memory class: governed-dispatch-baseline

docType: baseline

Status: AUTHORIZED_READY

Batch ID: ACEL-G3-T1-BEHAVIORAL-EVALUATION-OWNER-COMPOSITION-DESIGN

Dispatch base head: `63bd1614a591a1362b1c118236b1e43a6cf38fe7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer/orchestrator

Worker target: INTERNAL_AGENT design and source-verification worker

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded design pass that decides how generic behavioral
capability evaluation should compose with current ASSF certification/UAT,
release-gate, and provider-canary owners. The worker must refresh time-sensitive
T0 facts, prevent duplicate ownership, and produce an implementation-ready
owner contract or a truthful blocker without changing source or executing any
capability, provider, agent, runtime, or live path.

## Operator Authorization

The operator directed the Local reviewer/orchestrator to choose the next work,
issue its work order, and provide it for relay to Claude. This baseline treats
the relayed shared-workspace worker as `INTERNAL_AGENT`; Local retains final
technical disposition and commit ownership.

## Target / Source

The bounded source set is the accepted ACEL T0 gap record, current ASSF package
and lifecycle contracts, current generated skill index, manual UAT evidence,
the release bundle, and provider-lane readiness matrix. These sources must be
read from the current dispatch ancestry; provider-local memory and chat are not
authority.

## Scope / Methodology

Map, without implementation, one canonical owner composition for:
positive/negative invocation, outcome grading, process/tool grading,
tool-order verification, repeated trials, WITH/WITHOUT comparison,
mock/replay, and regression. Separate generic evaluation ownership from
domain-specific release and provider certification. Reconcile the T0 statement
that generated entries were `NOT_STARTED` with the current index, which now
contains both `NOT_STARTED` and `CERTIFIED/PASSED` records.

## Proposed Tranche

One INTERNAL_AGENT authors exactly three uncommitted design/evidence outputs.
Local reviews the return. No code, test, package, registry, generated index,
checker, hook, runtime, provider, public, or continuity file is worker-owned.

## Required Evidence

- exact eight-source path/hash/status ledger;
- current-state freshness comparison against the accepted T0 claims;
- owner/consumer/dependency graph and overlap decision;
- generic behavioral-evaluation contract with required evidence fields;
- fail-closed admission, grading-independence, repeat, replay, and regression rules;
- exact later implementation manifest or named blocker/reopen evidence;
- zero provider, network, credential, live, agent, or runtime execution.

## Non-Goals

- no behavioral harness implementation or test authoring;
- no skill certification-state or generated-index mutation;
- no release-bundle, provider-canary, checker, hook, CI, or runtime wiring;
- no provider/live calls, credentials, quota, CLI/MCP, public sync, or deploy;
- no claim that current certification proves generic behavioral quality;
- no automatic successor execution.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | proposed composition under existing ASSF lifecycle owner | read-only design with three uncommitted docs | exact current private-CVF sources and hashes | later implementation requires a separate exact-path work order | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no G3 CLI/MCP evaluator is authorized | no external ingress, auth, receipt, mutation, raw-data, or public claim | no current generic external adapter evidence | separate adapter owner and work order required if later selected | `DEFERRED_WITH_REASON` - internal owner composition must be settled first |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| G3 is accepted as ADAPT, not implementation-ready | CLAIM_BOUNDARY | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | Findings / Position | G3 generic behavioral capability evaluation | Local T0 completion | ACCEPT |
| generic positive/negative and process/tool evaluation was not proved at T0 | GAP_FACT | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md` | G3 required sub-findings | G3-C1 | ACEL T0 audit | ACCEPT |
| ASSF lifecycle contract owns certification/UAT ordering | VALUE_SET | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState`; `uatState` | ASSF lifecycle contract | ACCEPT |
| package schema already carries certification and UAT fields | SCHEMA_FACT | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `certificationState`; `uatState` | ASSF package contract | ACCEPT |
| current index is mixed, not uniformly NOT_STARTED | FRESHNESS_FACT | `docs/reference/agent_system_skills/generated/skill-index.json` | skill entries | `certificationState`; `uatState` | generated skill index | ACCEPT |
| release bundle is release-readiness specific and includes live boundaries | CLAIM_BOUNDARY | `scripts/run_cvf_release_gate_bundle.py` | module contract; command modes | `check_provider_readiness`; `check_e2e` | release gate bundle | ACCEPT |
| provider certification uses three consecutive 6/6 canary passes | VALUE_SET | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | Certification States | `CERTIFIED` | provider-lane readiness owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact five dispatch/output paths | absent before authoring | NO_COLLISION |
| generic behavioral owner search | no current generic positive/negative, process/tool, WITH/WITHOUT evaluator found in bounded owners | DESIGN_GAP_RETAINED |
| lifecycle checker path claimed by old prose | `governance/compat/check_assf_certification_lifecycle_guard.py` is absent | SOURCE_FACT_MUST_BE_CORRECTED |
| adjacent owners | ASSF lifecycle, release bundle, UAT evidence, and provider canary exist | REUSE_AND_COMPOSE; DO_NOT_DUPLICATE |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | ready status, dispatch envelope, source-verification columns, convergence fields, no-commit return shape, gate graph, trace labels and forbidden provider authority |
| gateRunPurpose | confirm dispatch evidence and packet shape before worker relay, not discover requirements after execution |
| claimBoundary | structural conformance does not prove an evaluation owner is implemented or behaviorally valid |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0007, ADIF-0016,
ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049 and
ADIF-0006.

Dispatch impact: use an exact bounded corpus, current source hashes, checker
read-ahead, truthful base anchors, no protected worker paths, no provider
authority, exact three-output ownership, and one complete return packet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design authority; no public artifact is authorized.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: owner-composition design only; no package lifecycle transition.

Target lifecycle state: N/A with reason: no package or skill state changes.

Prior phase evidence: accepted ACEL T0 gap audit and current ASSF owner sources.

Next forbidden skip: implementation, activation, certification, or runtime promotion without a separate work order.

Runtime/provider proof: N/A with reason: runtime and provider execution are forbidden.

Claim boundary: references to package/skill owners are source inputs, not productionization authority.

## Claim Boundary

This baseline authorizes documentation-only current-owner reconciliation and
design. It does not authorize implementation, certification changes, generic
behavioral-quality claims, provider/live execution, runtime wiring, public
sync, or deployment.
