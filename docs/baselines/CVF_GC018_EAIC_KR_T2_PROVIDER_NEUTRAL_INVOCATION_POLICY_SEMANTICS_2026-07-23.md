# CVF GC-018 Baseline - EAIC KR T2 Provider-Neutral Invocation Policy Semantics

Memory class: governed-dispatch-baseline

Status: HOLD_PENDING_OPERATOR_DECISION

docType: baseline

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T2

dispatchBaseHead: `5a3094683`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: worker role selected by operator through manual copy/paste

## Purpose

Audit whether EAIC-KR T2 is releasable and define the exact policy decisions
needed before a documentation-only ratification worker may start. This baseline
does not release T2: the audit finds that all four T1 reopen conditions still
require an explicit operator policy decision or fresh accepted evidence.

## Scope / Target / Owner Boundary

Risk ceiling: R0 documentation and repository-local evidence only.

Allowed scope for this audit:

- read current CVF-governed roadmap, T1 ledger, completion review, active state,
  active handoff, templates, and checker sources;
- compare T1 terminal evidence with every T2 release condition;
- propose provider-neutral policy defaults for operator consideration;
- create the paired held work order;
- run repository-local governance checks.

Forbidden scope:

- agent CLI/MCP invocation, separately dispatched agent session, provider/API
  call, account access, secret, paid query, or quota consumption;
- process launch, runtime test, browser/network retrieval, live proof, or
  provider-specific experiment;
- ratifying an operator policy by inference or treating a proposed default as
  accepted;
- runtime, source, test, checker, hook, roadmap, registry, session, handoff,
  public-sync, deployment, or production mutation;
- staging, committing, pushing, publishing, deleting, or renaming.

## Audit Finding

EAIC-KR T2 is the next numbered tranche, but it is not dispatchable. The T1
ledger reports zero domains at `READY_FOR_T2_DECISION`, three at
`PARTIAL_REMAINS`, and one at `OPAQUE_REQUIRES_OPERATOR_POLICY`. The roadmap and
active handoff require all four reopen conditions, not any subset.

| Reopen condition | Current accepted evidence | Audit disposition | Release owner |
| --- | --- | --- | --- |
| pre-launch admission decision boundary | lifecycle and process primitives exist; no CVF admission decision is ratified | UNSATISFIED_POLICY_REQUIRED | operator |
| task/receipt-to-session-and-process identity | host/session and OS identities exist; no cross-layer CVF binding is ratified | UNSATISFIED_POLICY_REQUIRED | operator |
| provider-neutral cumulative envelope | some host usage is observable; retry/resume/fallback/internal-agent aggregation has no ratified owner | UNSATISFIED_POLICY_REQUIRED | operator |
| fail-closed behavior for unavailable usage | machine-readable pre-launch usage is not guaranteed | UNSATISFIED_POLICY_REQUIRED | operator |

Dispatch readiness: `HOLD_PENDING_OPERATOR_DECISION`.

## Proposed Operator Policy Defaults

These rows are recommendations, not authority. T2 remains held until the
operator explicitly accepts, replaces, or rejects every row.

| Policy area | Recommended provider-neutral default | Current state |
| --- | --- | --- |
| admission | deny an automatic external launch unless an approved assignment, cumulative envelope, identity plan, stop conditions, and receipt target are present before launch | PROPOSED_NOT_RATIFIED |
| identity | issue CVF task and invocation IDs before launch, then bind them to provider session/conversation identity and root process identity when each becomes observable; absence must remain explicit | PROPOSED_NOT_RATIFIED |
| cumulative envelope | account at the parent assignment level across retry, resume, fallback, and separately dispatched external children; provider-native internal helpers remain autonomous, while any observable aggregate usage is charged to the parent | PROPOSED_NOT_RATIFIED |
| unknown usage | fail closed for unattended or automatic launch when reliable admission-time usage cannot be obtained; any future manual exception requires a separate bounded operator authorization | PROPOSED_NOT_RATIFIED |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| accepted T1 closure | `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md` | T1 must be independently accepted | SATISFIED |
| admission policy | T1 completion review, Decision / Disposition item 1 | operator decision or fresh accepted evidence must supply the boundary | HOLD_UNSATISFIED |
| identity policy | T1 completion review, Decision / Disposition item 2 | operator decision or fresh accepted evidence must supply the model | HOLD_UNSATISFIED |
| cumulative-envelope policy | T1 completion review, Decision / Disposition item 3 | operator decision or fresh accepted evidence must supply the semantics | HOLD_UNSATISFIED |
| unknown-usage policy | T1 completion review, Decision / Disposition item 4 | operator decision or fresh accepted evidence must supply fail-closed behavior | HOLD_UNSATISFIED |
| invocation moratorium | EAIC-KR roadmap and active handoff | no CLI/MCP/provider/runtime action may be released by T2 documentation work | SATISFIED_AND_RETAINED |

No row marked `HOLD_UNSATISFIED` may be interpreted as released by the
operator's request to author this audit and work order.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014,
ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024,
ADIF-0028, ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039, ADIF-0043,
ADIF-0044, ADIF-0045.

Dispatch impact: the packet uses source-backed paths, checker read-ahead,
explicit authority boundaries, exact manifests, process-CWD evidence, and a
held status. No provider-local memory is accepted as authority, and no worker
or subprocess is launched by dispatch authoring.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm the held packet shape and identify only allowed-scope repairs after authoring |
| claimBoundary | checker compliance proves document structure, not policy acceptance or runtime effectiveness |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id EAIC-KR-T2 --title "EAIC KR T2 Provider Neutral Invocation Policy Semantics" --date 2026-07-23 --base 5a3094683 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "all four T1 reopen conditions require fresh accepted evidence or explicit operator policy" --stdout` |
| generatedProfile | held-dependency plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the T1 evidence audit, four-row hold decision, proposed defaults, exact paths, and stop rules |
| checkerReadAheadConfirmation | applicable checker sources and the canonical work-order and handoff contracts were inspected before writing |
| docOnlyNewFields | operatorPolicyDisposition; admissionDefault; identityBindingDefault; cumulativeEnvelopeDefault; unknownUsageDefault |
| claimBoundary | dispatch authoring provenance only; no runtime, provider, live, public, Web, or MCP behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T2 objective is provider-neutral policy-semantics ratification | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, T2 row | `T2` | EAIC-KR roadmap | ACCEPT |
| T2 cannot ratify unsupported fields | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules | `T2` | EAIC-KR roadmap | ACCEPT |
| no domain reached T2 decision readiness | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | Domain terminal-state summary | `READY_FOR_T2_DECISION` | T1 evidence ledger | ACCEPT |
| four reopen conditions are mandatory | VALUE_SET | `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md` | Decision / Disposition | `PARKED_KNOWLEDGE_GAP` | T1 completion review | ACCEPT |
| T2 is not released by the active handoff | VALUE_SET | `AGENT_HANDOFF_V51_2026-07-22.md` | Next Allowed Move; Parked Operator Checkpoint | `Next Allowed Move` | active handoff | ACCEPT |
| internal helpers remain autonomous until they cross a governed perimeter | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter | `INTERNAL_AGENT` | EAIC-KR roadmap | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned path existence | `Test-Path` returned false for this baseline, paired work order, proposed spec, worker return, and completion review before authoring | ACCEPT |
| batch-token collision | `rg -n --fixed-strings "EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS" docs CVF_SESSION AGENT_HANDOFF_V51_2026-07-22.md CVF_SESSION_MEMORY.md` returned no prior artifact | ACCEPT |
| field collision | all proposed policy fields are declared doc-only and are not represented as current runtime fields | ACCEPT |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: T1 evidence would sharpen policy choices but
would not itself authorize a provider-neutral T2 ratification.

Evidence Comparison Requirement: compare every T1 terminal domain with the
four active reopen conditions and preserve unresolved policy ownership.

Contradiction Handling Requirement: a host-specific capability cannot replace
a provider-neutral policy decision; contradictory evidence keeps the row held.

Claim Update Requirement: T2 remains held until an explicit four-row operator
decision receipt or fresh accepted evidence satisfies every dependency.

## Baseline Decision

`HOLD_PENDING_OPERATOR_DECISION`

The valuable next action is an operator decision on the four proposed defaults,
not worker execution. If any row is rejected or materially changed, this paired
work order must be refreshed and re-gated before dispatch.

## Verification / Evidence

- clean dispatch base: `5a3094683`;
- all five planned paths were absent before authoring;
- exact batch-token search returned no collision;
- no external invocation, network action, provider call, or process under study
  occurred during this audit.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | this audit reads current governed documentation and does not claim or alter runtime behavior |
| requiredFutureAction | any later runtime claim requires a separate roadmap, GC-018, source-verified work order, operator authorization, and live proof when applicable |

## Claim Boundary

This baseline records a repository-local T2 readiness audit, proposed policy
defaults, and a held dispatch packet. It does not accept those defaults,
authorize a worker, select a provider/model, invoke an agent, control a process,
measure quota, implement runtime, lift the moratorium, or establish public,
security, cost, production, or live-governance readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private held policy-decision packet with no public implementation or
release evidence.
