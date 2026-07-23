# CVF Agent Work Order - EAIC KR T2 Provider-Neutral Invocation Policy Semantics

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_WITH_REPAIRS

docType: work-order

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T2

dispatchBaseHead: `d1cb636bf`

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: delegated no-commit documentation worker for CVF-EAIC-KR-T2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md`

Paired baseline: `docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture with `git rev-parse --short HEAD` at worker start
and require the exact operator-supplied committed dispatch HEAD.

Current-time notes: refreshed 2026-07-23 from R1B material closure commit
`1843c5123` and explicit operator ratification of D1-D4. T2
documentation-only execution is released; T3 and all runtime/external-action
lanes remain held.

Do-not-misread notes: no CLI/MCP, provider/API/account, process, browser,
network, runtime, public-sync, push, or policy invention is authorized.

Required first actions: verify this `DISPATCH_READY` status and exact
executionBaseHead, read startup authority and required first reads, confirm a
clean worktree, then run the pre-implementation gate before writing.

Return contract: create exactly the two worker-owned outputs,
leave them unstaged and uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Author one provider-neutral documentation contract for the operator-ratified
admission, identity, cumulative-envelope, unknown-usage,
stop/retry/fallback, receipt, and provider/model assignment-reconciliation
semantics. Success preserves agent internal autonomy, labels every mechanism
gap, contains no implementation design, and leaves the external-invocation
moratorium in force.

## Authority Chain

- Operator instruction: 2026-07-23 explicit acceptance of the reviewer
  proposal and request to process D1-D4 and create this worker order.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V51_2026-07-22.md`.
- Roadmap: `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`.
- T1 accepted evidence: `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md`.
- T1 decision authority: `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md`.
- R1B decision evidence:
  `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_R1B_T2_DECISION_EVIDENCE_SUPPLEMENT.md`.
- R1B independent review:
  `docs/reviews/CVF_EAIC_KR_R1B_COMPLETION_REVIEW_2026-07-23.md`.
- GC-018: `docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md`.
- Handoff contract archive-qualified exception:
  `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

Authority boundary: D1-D4 are operator policy, not proof of a runtime owner,
host capability, enforcement, or implementation. If any source conflicts with
the receipt, stop and return to the orchestrator.

## Agent Roles

- Orchestrator/dispatcher: dispatcher role.
- Policy decision owner: operator.
- Future implementer: worker role chosen by operator via manual copy/paste.
- Reviewer/closer: independent reviewer/closer role.
- Fresh operator authority required for: any policy change, scope or risk expansion,
  and all external, runtime, or public action.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator-ratified EAIC-KR-T2 policy decision following R1B material closure commit `1843c5123` |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R0 documentation-only policy semantics |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | one no-commit documentation worker selected by operator through manual copy/paste |
| Reviewer role | independent reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | D1-D4 satisfied for documentation dispatch; external-action checkpoints remain closed |
| escalation condition | policy contradiction, scope expansion, forbidden paths, provider/live/public action, secrets/quota, destructive action, or claim-boundary change |

## Scope

Risk ceiling: R0 documentation and repository-local evidence only.

Allowed scope:

- read the authority chain and accepted T1 sources already represented in the
  repo-local ledger;
- translate the operator's four explicit decisions into one provider-neutral
  semantics specification;
- distinguish normative policy, observable evidence, unknown values, and later
  architecture decisions;
- create exactly the two worker outputs named below;
- run local read-only commands and listed governance gates.

Forbidden scope:

- inventing, choosing, or silently filling any unresolved operator policy;
- agent CLI/MCP invocation, provider/API/account use, secrets, quota, paid
  query, network retrieval, browser automation, or separately dispatched agent;
- process launch/control experiment, runtime code, architecture-owner
  selection, source/test/checker/hook mutation, or live proof;
- restricting provider-native internal reasoning helpers or requiring CVF
  permission for each internal exploration step;
- provider/model selection, cost-saving claim, public-sync, deployment,
  staging, commit, push, publish, deletion, or rename.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | authorized parent session and T2 policy contract | provider-native reasoning, exploration, and context helpers remain autonomous inside the parent envelope unless they cross a governed perimeter | EAIC-KR roadmap autonomy section and D3 receipt | internal helpers inherit parent scope; no per-helper adapter or permission row | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | T2 provider-neutral invocation policy specification | documentation defines admission and evidence requirements but authorizes no launch, credential, mutation, process, or public action | operator-ratified D1-D4 and R1B evidence | adapter contract only; admission owner, process binding, telemetry, and runtime enforcement remain deferred | `CONTRACT_ONLY` |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T1 accepted | T1 completion review status `REVIEWER_ACCEPTED_PARKED_KNOWLEDGE_GAP` | accepted T1 review must exist | SATISFIED |
| admission decision | operator decision following R1B closure commit `1843c5123` | receipt contains REPLACE with exact policy and implementation-gap boundary | SATISFIED |
| identity decision | operator decision following R1B closure commit `1843c5123` | receipt contains ACCEPT with exact text | SATISFIED |
| cumulative-envelope decision | operator decision following R1B closure commit `1843c5123` | receipt contains ACCEPT and preserves internal autonomy | SATISFIED |
| unknown-usage decision | operator decision following R1B closure commit `1843c5123` | receipt contains ACCEPT and exact fail-closed boundary | SATISFIED |
| refreshed dispatch anchors and gates | clean refresh base `d1cb636bf`; packet status and receipt refreshed; pre-dispatch autorun PASS 75/75 | committed dispatch packet must preserve this evidence | SATISFIED |

Release invariant: all policy rows are terminal. This releases documentation
only and does not close any recorded mechanism or implementation gap.

## Operator Policy Decision Receipt

This table durably records the operator's explicit 2026-07-23 policy decision.

| Decision ID | Policy area | Proposed default source | Operator disposition | Ratified text or next action |
| --- | --- | --- | --- | --- |
| EAIC-T2-D1 | pre-launch admission | paired baseline and R1B decision supplement | REPLACE | deny an automatic external launch unless an approved assignment, cumulative envelope, identity plan, stop conditions, and receipt target exist before launch; treat this as operator safety policy with an explicit admission-owner and implementation gap |
| EAIC-T2-D2 | task/receipt/session/process identity | paired baseline and R1B decision supplement | ACCEPT | issue CVF task and invocation IDs before launch, then bind provider session, conversation, and root-process identity when observable; absence remains explicit |
| EAIC-T2-D3 | cumulative envelope | paired baseline and R1B decision supplement | ACCEPT | account retry, resume, fallback, and separately dispatched external children at parent-assignment level; provider-native internal helpers remain autonomous, and observable aggregate usage is charged to the parent |
| EAIC-T2-D4 | unavailable usage | paired baseline and R1B decision supplement | ACCEPT | fail closed for automatic or unattended launch when reliable admission-time usage is unavailable; manual exception requires separate bounded operator authorization |

Supplemental direction: receipts must distinguish operator-approved
provider/model assignment from provider/model observed at execution. Mismatch
is explicit; unavailable observation remains unknown. The worker must not
select or hard-code a provider or model.

## Worker Autonomy / No-Question Rule

After release, the worker proceeds without operator confirmation for
non-destructive actions inside Allowed scope, including checker-shaped
documentation repair and gate reruns. The worker must stop for any unresolved
policy, source contradiction, release-state mismatch, external action, scope
expansion, runtime/public request, or destructive action.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014,
ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024,
ADIF-0028, ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039, ADIF-0043,
ADIF-0044, ADIF-0045.

Dispatch impact: exact paths and authority are listed; provider-local memory is
not authority; no exhaustive corpus claim is made; checker sources were read
before drafting; the manifest is phase-local; dispatch authoring launches no
worker process; and output paths are repository-root-relative.

## Required First Reads

- `CVF_SESSION_MEMORY.md` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` - active
  mode and next-move authority.
- active handoff resolved by the state registry - parked checkpoint.
- `docs/reference/guard_orientation/README.md` - applicable guard surfaces.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
  - literal-format traps.
- paired baseline and this work order - exact release and scope boundary.
- EAIC-KR roadmap, T1 ledger, and T1 completion review - accepted evidence and
  four mandatory policy gaps.
- Archive-qualified canonical contract:
  `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`
  - phase, manifest, trace, and commit ownership.
- checker sources listed below - output shape before authoring.
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0047.md` -
  separate provider-backed host surface, outbound-call count, and measured
  usage in the worker return.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_artifacts.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Dependency Release Evidence; Operator Policy Decision Receipt; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm the released documentation-only packet shape; gate output is dispatch evidence, not first discovery |
| claimBoundary | machine checks validate packet shape, not policy wisdom or runtime behavior |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id EAIC-KR-T2 --title "EAIC KR T2 Provider Neutral Invocation Policy Semantics" --date 2026-07-23 --base 5a3094683 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "all four T1 reopen conditions require fresh accepted evidence or explicit operator policy" --stdout` |
| generatedProfile | held-dependency plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact authority, operator-ratified decision receipt, provider-neutral scope, output contract, and stop conditions; refreshed from R1B closure commit `1843c5123` |
| checkerReadAheadConfirmation | canonical work-order, dependency-release, and handoff standards plus applicable checker sources were inspected |
| docOnlyNewFields | operatorPolicyDisposition; admissionDefault; identityBindingDefault; cumulativeEnvelopeDefault; unknownUsageDefault; approvedProvider; approvedModel; observedProvider; observedModel; assignmentReconciliationState |
| claimBoundary | dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T2 ratifies provider-neutral semantics | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, T2 row | `T2` | EAIC-KR roadmap | ACCEPT |
| T2 may record operator policy only while preserving evidence and mechanism gaps | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Knowledge Sufficiency Stop Rule; Roadmap Release Rules | `T2` | EAIC-KR roadmap | ACCEPT |
| four conditions must reopen T2 | VALUE_SET | `docs/reviews/CVF_EAIC_KR_T1_COMPLETION_REVIEW_2026-07-22.md` | Decision / Disposition | `PARKED_KNOWLEDGE_GAP` | T1 completion review | ACCEPT |
| T1 readiness count is zero | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | Domain terminal-state summary | `READY_FOR_T2_DECISION` | T1 ledger | ACCEPT |
| internal agent helpers are contract-only unless they cross the invocation perimeter | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter; Dual Agent Surface Matrix | `INTERNAL_AGENT` | EAIC-KR roadmap | ACCEPT |
| archive reviewer conversion | LITERAL_INVARIANT | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CF-07 commitOwner | `commitOwner` | Agent Handoff Contract | ACCEPT |
| R1B provides accepted bounded evidence for all four policy decisions | VALUE_SET | `docs/reviews/CVF_EAIC_KR_R1B_COMPLETION_REVIEW_2026-07-23.md` | Independent Decision Review; Decision / Disposition | `EAIC-T2-D1` through `EAIC-T2-D4` | R1B completion review | ACCEPT |
| paired baseline records exact operator dispositions | VALUE_SET | `docs/baselines/CVF_GC018_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_2026-07-23.md` | Operator-Ratified Policy Defaults | `EAIC-T2-D1` through `EAIC-T2-D4` | T2 GC-018 baseline | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
| --- | --- | --- |
| operatorPolicyDisposition | records ACCEPT, REPLACE, or REJECT for one decision row | DOC_ONLY_NEW |
| admissionDefault | normative pre-launch decision semantics | DOC_ONLY_NEW |
| identityBindingDefault | normative cross-layer identity semantics | DOC_ONLY_NEW |
| cumulativeEnvelopeDefault | normative aggregation boundary | DOC_ONLY_NEW |
| unknownUsageDefault | normative behavior when usage is unavailable | DOC_ONLY_NEW |
| approvedProvider | operator-approved provider identity when supplied | DOC_ONLY_NEW |
| approvedModel | operator-approved model identity when supplied | DOC_ONLY_NEW |
| observedProvider | provider identity observed at execution when exposed | DOC_ONLY_NEW |
| observedModel | model identity observed at execution when exposed | DOC_ONLY_NEW |
| assignmentReconciliationState | MATCH, MISMATCH, or UNKNOWN_NOT_EXPOSED comparison state | DOC_ONLY_NEW |

No row is represented as an existing runtime field or interface.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| worker output path existence | both worker-owned output paths remain absent before dispatch refresh | ACCEPT |
| exact batch-token search | exact-token search finds the committed packet family and recorded references only; neither worker output exists | ACCEPT |
| runtime-field collision | proposed fields are isolated in the New Doc-Only Fields table | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | accepted T1 ledger -> four explicit operator policy decisions -> provider-neutral T2 semantics -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_invocation_control/` family |
| Disposition | ADAPT accepted evidence and explicit operator policy; do not import provider-specific implementation |
| Claim boundary | no new external material is ingested by this tranche; any later external source requires a separate approved intake route |

## Pre-Flight Checks

The dispatcher uses the clean pre-authoring base below for pre-dispatch. The
worker must independently capture the committed executionBaseHead and run
pre-implementation before writing:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base d1cb636bf --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base d1cb636bf --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base d1cb636bf --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected results: exact base match, clean pre-worker worktree, all four decision
rows terminal, dispatch-ready status present, and every applicable gate
PASS. Any mismatch stops execution.

Mandatory remediation: repair and rerun every allowed-scope documentation gate
failure. Return `BLOCKED_WITH_REASON` only when repair would exceed Allowed
scope or require a policy change, external action, public action,
secrets/quota, forbidden path, or destructive action.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> one no-commit worker -> independent reviewer/closer |
| phase | DISPATCH_AUTHORING and EXECUTION released; CLOSURE and SESSION_SYNC remain reviewer-owned |
| baseHeadFor(phase) | dispatchBaseHead=`d1cb636bf`; executionBaseHead is captured from the committed dispatch HEAD at worker start; closureBaseHead is reviewer-captured |
| changedSetScope(phase) | dispatch authoring: roadmap, paired baseline, and this work order; execution: exactly two worker-owned output paths |
| traceScope(phase, actor) | dispatcher records local packet audit; worker records only its two outputs and commands; reviewer records closure paths separately |
| commitOwner(phase) | dispatcher commits the dispatch packet; worker commit is forbidden; reviewer owns accepted closure commit |
| crossBatchIsolation | worker may start only from a clean worktree with no other uncommitted batch |
| nextMoveSurfaces | worker does not mutate continuity; reviewer decides closure and a separately authorized session-sync steward updates next-move surfaces |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_COMPLETION_REVIEW_2026-07-23.md` |
| reviewerOwnedClosurePaths | paired baseline; this work order; T2 specification; worker return; completion review; roadmap and continuity only through separate explicit authorization |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Required Artifact Manifest

| Path | Required at worker handoff | Purpose |
| --- | --- | --- |
| `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md` | Yes | provider-neutral normative policy-semantics proposal bound to the operator receipt |
| `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_WORKER_RETURN_2026-07-23.md` | Yes | no-commit execution evidence and stop disposition |

Every other path is read-only or forbidden for worker writes.

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
| --- | --- | --- | --- |
| T2 policy specification | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md` | worker | REQUIRED |
| Worker return | `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_WORKER_RETURN_2026-07-23.md` | worker | REQUIRED |
| Material closure commit | accepted specification, worker return, and reviewer closure artifacts | reviewer/closer | PENDING_REVIEW |
| Session sync | only if accepted closure changes current mode or next allowed move | session-sync steward | PENDING_REVIEW |

## Write Ownership

Worker-owned create-only paths:

- `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md`;
- `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_WORKER_RETURN_2026-07-23.md`.

Write mode: create-only, unstaged, uncommitted. Repository root is the required
process working directory for every relative output path.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| durable owner family | `docs/reference/external_agent_invocation_control/` |
| new durable artifact | one stable undated T2 provider-neutral semantics specification |
| owner front door | existing family README is read-only in worker scope; reviewer decides any later index update |
| storage class | governed normative documentation, not runtime state, queue, cache, receipt store, or provider memory |
| generated aggregate disposition | N/A with reason: the proposed Markdown specification has no generated aggregate owner |
| claim boundary | provider-neutral documentation only; no runtime or public authority |

## Worker Output Checker Read-Ahead Mandate

Before creating the worker return, run the prescribed scaffold and fast gate
while it is short. Required real review headings include Purpose, Target /
Source, Scope / Methodology, Findings / Position, Decision / Disposition, Risk /
Corrective Action, Source Inventory, Checker Source Read-Ahead Block, External
Knowledge Intake Routing, Epistemic Process Block, Agent Operation Trace Block,
Delta Execution Claim Boundary Control Block, Public Export Disposition, Claim
Boundary, git status --short, Changed Files, and No-Commit Statement.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_WORKER_RETURN_2026-07-23.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Execution Plan

| Step | Action | Output/evidence | Stop condition |
| --- | --- | --- | --- |
| 1 | verify refreshed status, decision receipt, base, and clean worktree | command transcript | any pending row, held status, mismatch, or dirt |
| 2 | run pre-implementation autorun | gate result | any unrepairable failure |
| 3 | scaffold the worker return and read output-specific checker sources | checker-safe skeleton | required shape unresolved |
| 4 | translate each accepted operator decision into normative semantics and explicit unknowns | T2 specification | inference beyond decision or accepted evidence |
| 5 | reconcile admission, identity, approved-versus-observed provider/model, budget, retry/resume/fallback, stop, receipts, and internal-agent boundary | cross-field consistency matrix | contradiction or architecture choice required |
| 6 | run final local gates and record actual pending status | worker return | failure outside Allowed scope |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| ratify provider-neutral budget semantics | policy receipt and execution plan | cumulative envelope section | reviewer compares to EAIC-T2-D3 | PASS for dispatch mapping |
| ratify telemetry and unknown-usage behavior | policy receipt and execution plan | availability and unknown-state section | reviewer compares to EAIC-T2-D4 | PASS for dispatch mapping |
| ratify stop and retry/fallback semantics | scope and execution plan | stop/retry/fallback matrix | semantic review | PASS for dispatch mapping |
| ratify receipt semantics | identity decision and output contract | identity/receipt and assignment reconciliation | reviewer compares to EAIC-T2-D2 plus supplemental direction | PASS for dispatch mapping |
| preserve fail-closed design control | operator receipt and fail conditions | unknown-usage rule | exact operator receipt | PASS for dispatch mapping |
| do not select runtime owner | forbidden scope and claim boundary | explicit architecture deferral | diff review | PASS for packet design |
| do not release implementation | forbidden scope and claim boundary | no implementation authority | diff review | PASS for packet design |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| knowledge before architecture | Design Control Gate | consumes T1 evidence and operator decisions only | PASS |
| architecture before implementation | Design Control Gate | no runtime owner or build path may be selected | PASS |
| provider neutrality | Design Control Gate | all policy language applies across provider/access modes | PASS |
| fail-closed unknown usage | Design Control Gate | D4 exact operator decision is recorded | PASS |
| external-service authority | Design Control Gate | all external action remains denied | PASS |
| dependency/source verification | Roadmap Release Rules | four-row receipt and source-verification rows are present | PASS |
| dispatch readiness | Next Allowed Move | documentation-only manual dispatch is released | PASS |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: explicit operator policy can close the normative
decision gaps without pretending that host-specific evidence is universal.

Evidence Comparison Requirement: every normative statement must trace to an
operator decision row or accepted T1 evidence; all other points remain unknown
or deferred.

Contradiction Handling Requirement: contradictory policy/evidence returns
`BLOCKED_WITH_REASON`; the worker must not silently choose a side.

Claim Update Requirement: the worker states whether the four decisions form a
coherent provider-neutral contract or require another operator decision.

## Evidence Requirements

The future specification must include:

- operator decision trace matrix for EAIC-T2-D1 through EAIC-T2-D4;
- normative admission inputs and deny conditions;
- task, invocation, provider-session, conversation, and root-process identity
  layers, including explicit unavailable states;
- cumulative-envelope inclusion/exclusion rules for retry, resume, fallback,
  separately dispatched children, and provider-native internal helpers;
- usage availability and fail-closed state machine;
- stop-reason and retry/fallback interaction matrix;
- receipt schema at the documentation level, with no invented runtime field
  claim;
- separate approved provider/model from observed provider/model, with
  `MATCH`, `MISMATCH`, and `UNKNOWN_NOT_EXPOSED` reconciliation states;
- architecture-owner decisions explicitly deferred to T3;
- contradiction/gap ledger and bounded T3 readiness recommendation.

The worker return must include exact command evidence, executionBaseHead,
actual pending `git status --short --untracked-files=all`, provider/model/surface
declaration when known, `internalSubagentInvocationCount` when observable, and
separate counts for the provider-backed host surface versus worker-initiated
outbound/recursive CLI/MCP or direct API actions. Host usage must remain
`UNKNOWN_NOT_EXPOSED` unless a receipt exists.

## Verification Commands

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_WORKER_RETURN_2026-07-23.md --title "CVF EAIC KR T2 Provider-Neutral Invocation Policy Semantics Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
```

## Acceptance Criteria

- [ ] packet was explicitly released by a refreshed non-HOLD status;
- [ ] all four operator decision rows are terminal and exact;
- [ ] exactly two worker-owned outputs exist and no other path changed;
- [ ] every normative statement traces to operator policy or accepted evidence;
- [ ] provider-neutral semantics remain separate from host observations;
- [ ] internal helper autonomy and external invocation perimeter are preserved;
- [ ] architecture, runtime, provider, public, and live-proof work remain deferred;
- [ ] worker-return fast gate and listed checks pass after final edit;
- [ ] worker leaves all changes unstaged and uncommitted.

Fail conditions:

- any decision row remains pending, ambiguous, or inferred;
- status remains HOLD or base anchors are stale;
- one provider/host fact is promoted to a universal guarantee;
- unknown usage is converted into an allow path without explicit operator text;
- internal agent reasoning steps are individually permissioned by CVF;
- implementation owner, runtime field, cost saving, moratorium lift, or public
  readiness is claimed;
- changed set exceeds the two worker paths;
- a required gate cannot pass inside Allowed scope.

## Review Gate

This packet is eligible for manual operator copy/paste only after the committed
dispatch HEAD is supplied to the worker. Worker handoff is
`COMPLETE_PENDING_REVIEW`, never closure. The independent reviewer recomputes
all four decision mappings, the provider/model reconciliation semantics, and
every retained mechanism gap.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository; no external agent invocation |
| Session or invocation | EAIC-KR-T2 policy receipt and dispatch refresh, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | local PowerShell, rg, Git reads, scaffold helper stdout, ADIF resolver, apply_patch, and governance checks |
| Target paths | EAIC-KR roadmap, paired T2 baseline, and this work order |
| Allowed scope source | operator acceptance of D1-D4 and request to process the decisions and create the worker order |
| Before status evidence | clean worktree at HEAD `d1cb636bf`; both worker output paths absent |
| After status evidence | three tracked dispatch artifacts modified; author-fast 5/5 and pre-dispatch autorun 75/75 PASS; no worker or external action |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | operator-ratified documentation policy and manual no-commit worker dispatch only |
| Claim boundary | repo-local dispatch trace; policy authority only, with no provider, process, or runtime proof |
| Agent type | dispatcher/reviewer |
| Invocation ID | `eaic-kr-t2-policy-dispatch-refresh-2026-07-23` |
| Expected manifest | EAIC-KR roadmap; paired T2 baseline; this T2 work order |
| Actual changed set | EAIC-KR roadmap; paired T2 baseline; this T2 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | repository-local T2 operator-policy receipt and documentation dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: operator policy receipt is documentation authority only; no runtime receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local reads, audit, packet authoring, and gates only |
| invocationBoundary | no agent CLI/MCP/provider/API/browser/network/process invocation |
| interceptionBoundary | no IDE, shell, Git, filesystem, provider, process, or internal-reasoning interception claim |
| claimLanguage | operator-ratified provider-neutral documentation policy and one no-commit worker assignment |
| forbiddenExpansion | no policy inference, implementation, architecture owner, provider selection, CLI/MCP invocation, public-sync, live proof, or moratorium lift |

## Worker Pending-Return Gate

| Check | Required worker result |
| --- | --- |
| release state | `DISPATCH_READY` and complete decision receipt |
| output manifest | exactly two untracked worker paths |
| staging state | nothing staged |
| base state | executionBaseHead matches operator-supplied current HEAD |
| worker-return gate | PASS after final edit |
| return status | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON |

## External Action Checkpoint

The D1-D4 policy checkpoint is satisfied. Every external-action checkpoint
remains closed: no CLI/MCP invocation, provider/API/account use,
network/browser action, process test, runtime implementation, public-sync,
push, deployment, or live proof is authorized.

## Closure Checklist

- [x] operator resolved EAIC-T2-D1 through EAIC-T2-D4;
- [x] dispatcher refreshed decision rows, status, and base heads;
- [x] worker outputs match the two-path manifest;
- [x] reviewer checked semantic accuracy and provider-neutral boundaries;
- [x] all acceptance and fail conditions are terminal;
- [x] pending work was not described as clean closure;
- [x] committed-range pre-closure and continuity sync are reviewer-owned;
- [x] public export remains deferred unless separately authorized.

Reviewer closure resolved every row after actual execution and independent
semantic review.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any unresolved operator row, held status, base
mismatch, dirty worktree, source contradiction, required external action,
architecture choice, change outside ownership, or unrepairable gate failure.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | T2 is a documentation-policy tranche and no runtime capability is asserted or changed |
| requiredFutureAction | runtime or live claims require a separate post-T4 implementation roadmap and fresh explicit operator authorization |

## Claim Boundary

This work order authorizes one no-commit worker to document
operator-ratified provider-neutral semantics through manual copy/paste. It
does not invoke or constrain an agent through CLI/MCP, select a provider/model,
implement a supervisor, measure quota, control a process, lift the invocation
moratorium, or establish runtime, public, security, cost, production, or
live-governance readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only decision packet with no public
implementation or release authority.
