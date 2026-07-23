# CVF GC-018 Baseline - EAIC KR T2 Provider-Neutral Invocation Policy Semantics

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

docType: baseline

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T2

dispatchBaseHead: `d1cb636bf`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: worker role selected by operator through manual copy/paste

## Purpose

Record the operator-ratified EAIC-KR T2 policy directions and release one
documentation-only worker to author provider-neutral invocation semantics.
This baseline releases no runtime, provider, CLI/MCP, process, public, or
implementation action.

## Scope / Target / Owner Boundary

Risk ceiling: R0 documentation and repository-local evidence only.

Allowed scope for this audit:

- read current CVF-governed roadmap, T1 ledger, completion review, active state,
  active handoff, templates, and checker sources;
- compare T1 terminal evidence with every T2 release condition;
- record the operator-ratified provider-neutral policy directions;
- refresh and release the paired documentation-only work order;
- run repository-local governance checks.

Forbidden scope:

- agent CLI/MCP invocation, separately dispatched agent session, provider/API
  call, account access, secret, paid query, or quota consumption;
- process launch, runtime test, browser/network retrieval, live proof, or
  provider-specific experiment;
- changing or extending the operator-ratified policy without returning to the
  operator;
- runtime, source, test, checker, hook, roadmap, registry, session, handoff,
  public-sync, deployment, or production mutation;
- worker staging, committing, pushing, publishing, deleting, or renaming.

## Audit Finding

EAIC-KR T2 is the next numbered tranche. The T1 ledger reports zero domains at
`READY_FOR_T2_DECISION`, three at `PARTIAL_REMAINS`, and one at
`OPAQUE_REQUIRES_OPERATOR_POLICY`. R1B preserved those evidence gaps, and the
operator then supplied the normative policy authority needed for all four
rows without claiming that the missing mechanisms exist.

| Reopen condition | Current accepted evidence | Audit disposition | Release owner |
| --- | --- | --- | --- |
| pre-launch admission decision boundary | lifecycle and process primitives exist; no CVF admission mechanism exists | SATISFIED_BY_OPERATOR_POLICY_WITH_IMPLEMENTATION_GAP | operator |
| task/receipt-to-session-and-process identity | host/session and OS identities exist; no cross-layer CVF runtime binding exists | SATISFIED_BY_OPERATOR_POLICY_WITH_RUNTIME_GAP | operator |
| provider-neutral cumulative envelope | some host usage is observable; no ratified runtime owner exists | SATISFIED_BY_OPERATOR_POLICY_WITH_RUNTIME_GAP | operator |
| fail-closed behavior for unavailable usage | machine-readable pre-launch usage is not guaranteed | SATISFIED_BY_OPERATOR_FAIL_CLOSED_POLICY | operator |

Dispatch readiness: `REVIEWER_ACCEPTED_DISPATCH_READY`.

## Operator-Ratified Policy Defaults

The operator ratified these documentation-level policy directions on
2026-07-23 after reviewing the accepted R1B decision evidence.

| Decision | Policy area | Provider-neutral policy | Operator disposition | Current state |
| --- | --- | --- | --- | --- |
| EAIC-T2-D1 | admission | deny an automatic external launch unless an approved assignment, cumulative envelope, identity plan, stop conditions, and receipt target are present before launch | REPLACE: accept as operator safety policy while preserving the admission-owner and implementation gap | OPERATOR_RATIFIED_POLICY_ONLY |
| EAIC-T2-D2 | identity | issue CVF task and invocation IDs before launch, then bind them to provider session/conversation identity and root process identity when each becomes observable; absence must remain explicit | ACCEPT | OPERATOR_RATIFIED_POLICY_ONLY |
| EAIC-T2-D3 | cumulative envelope | account at the parent assignment level across retry, resume, fallback, and separately dispatched external children; provider-native internal helpers remain autonomous, while any observable aggregate usage is charged to the parent | ACCEPT with the existing internal-autonomy boundary | OPERATOR_RATIFIED_POLICY_ONLY |
| EAIC-T2-D4 | unknown usage | fail closed for unattended or automatic launch when reliable admission-time usage cannot be obtained; any future manual exception requires a separate bounded operator authorization | ACCEPT | OPERATOR_RATIFIED_POLICY_ONLY |

Supplemental operator direction: the T2 receipt semantics must keep
operator-approved provider/model assignment separate from provider/model
observed at execution. Mismatch is explicit; unavailable observation remains
unknown. No provider or model is selected or hard-coded by this rule.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | authorized parent agent session and proposed T2 semantics | provider-native reasoning helpers stay autonomous inside the parent envelope unless they cross the governed perimeter | EAIC-KR roadmap, Agent Internal Autonomy And Invocation Perimeter | internal helpers inherit parent scope; no per-helper adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | proposed T2 reference contract | no launch, account, credential, mutation, runtime, or public authority | operator-ratified D1-D4 and accepted R1B evidence | provider-neutral adapter contract only; runtime adapter and admission owner remain deferred | `CONTRACT_ONLY` |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| accepted T1 closure | `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md` | T1 must be independently accepted | SATISFIED |
| admission policy | operator instruction on 2026-07-23 following accepted R1B review | exact D1 replacement text is recorded above | SATISFIED |
| identity policy | operator instruction on 2026-07-23 following accepted R1B review | exact D2 acceptance text is recorded above | SATISFIED |
| cumulative-envelope policy | operator instruction on 2026-07-23 following accepted R1B review | exact D3 acceptance and autonomy boundary are recorded above | SATISFIED |
| unknown-usage policy | operator instruction on 2026-07-23 following accepted R1B review | exact D4 fail-closed policy is recorded above | SATISFIED |
| invocation moratorium | EAIC-KR roadmap and active handoff | no CLI/MCP/provider/runtime action may be released by T2 documentation work | SATISFIED_AND_RETAINED |

All policy dependencies are terminal. This releases only the two-path
documentation worker manifest in the paired work order.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014,
ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024,
ADIF-0028, ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039, ADIF-0043,
ADIF-0044, ADIF-0045.

Dispatch impact: the packet uses source-backed paths, checker read-ahead,
explicit authority boundaries, exact manifests, process-CWD evidence, and a
dispatch-ready documentation-only status. No provider-local memory is accepted as authority, and no worker
or subprocess is launched by dispatch authoring.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm the released documentation-only packet shape and identify only allowed-scope repairs after authoring |
| claimBoundary | checker compliance proves document structure, not runtime effectiveness |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id EAIC-KR-T2 --title "EAIC KR T2 Provider Neutral Invocation Policy Semantics" --date 2026-07-23 --base 5a3094683 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "all four T1 reopen conditions require fresh accepted evidence or explicit operator policy" --stdout` |
| generatedProfile | held-dependency plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the T1 evidence audit, operator-ratified decision receipt, exact paths, and stop rules; refreshed the packet after R1B closure |
| checkerReadAheadConfirmation | applicable checker sources and the canonical work-order and handoff contracts were inspected before writing |
| docOnlyNewFields | operatorPolicyDisposition; admissionDefault; identityBindingDefault; cumulativeEnvelopeDefault; unknownUsageDefault; approvedProvider; approvedModel; observedProvider; observedModel; assignmentReconciliationState |
| claimBoundary | dispatch authoring provenance only; no runtime, provider, live, public, Web, or MCP behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T2 objective is provider-neutral policy-semantics ratification | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, T2 row | `T2` | EAIC-KR roadmap | ACCEPT |
| operator policy must preserve unsupported evidence and implementation gaps | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules | `T2` | EAIC-KR roadmap | ACCEPT |
| no domain reached T2 decision readiness | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | Domain terminal-state summary | `READY_FOR_T2_DECISION` | T1 evidence ledger | ACCEPT |
| four reopen conditions are mandatory | VALUE_SET | `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md` | Decision / Disposition | `PARKED_KNOWLEDGE_GAP` | T1 completion review | ACCEPT |
| R1B supplies accepted non-ratifying decision evidence | VALUE_SET | `docs/reviews/CVF_EAIC_KR_R1B_COMPLETION_REVIEW_2026-07-23.md` | Independent Decision Review; Decision / Disposition | `EAIC-T2-D1` through `EAIC-T2-D4` | R1B completion review | ACCEPT |
| internal helpers remain autonomous until they cross a governed perimeter | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter | `INTERNAL_AGENT` | EAIC-KR roadmap | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| worker output path existence | both worker-owned output paths remain absent before dispatch refresh | ACCEPT |
| batch-token collision | exact-token search finds only the committed T2 packet family and its recorded references; neither worker output exists | ACCEPT |
| field collision | all proposed policy fields are declared doc-only and are not represented as current runtime fields | ACCEPT |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: T1 evidence would sharpen policy choices but
would not itself authorize a provider-neutral T2 ratification.

Evidence Comparison Requirement: compare every T1 terminal domain with the
four active reopen conditions and preserve unresolved policy ownership.

Contradiction Handling Requirement: a host-specific capability cannot replace
a provider-neutral policy decision; contradictory evidence keeps the row held.

Claim Update Requirement: operator policy satisfies the four normative
dependencies for documentation only; every runtime and mechanism gap remains
explicit.

## Baseline Decision

`REVIEWER_ACCEPTED_DISPATCH_READY`

The next action is manual copy/paste dispatch of the paired work order to one
no-commit documentation worker. Any policy change returns to the operator and
requires packet refresh before execution.

## Verification / Evidence

- clean dispatch-refresh base: `d1cb636bf`;
- both worker output paths were absent before dispatch refresh;
- exact batch-token search found no worker-output collision;
- pre-dispatch autorun PASS 75/75 on range `d1cb636bf..HEAD`;
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

This baseline records operator-ratified policy semantics and authorizes one
documentation-only worker through manual copy/paste. It does not select a
provider/model, invoke an agent through CLI/MCP, control a process, measure
quota, implement runtime, lift the invocation moratorium, or establish public,
security, cost, production, or live-governance readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only policy packet with no public implementation
or release evidence.
