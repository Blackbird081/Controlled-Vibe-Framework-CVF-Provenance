# CVF Agent Work Order - EAIC KR T3 Owner Architecture And Threat Model

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_WITH_REPAIRS_OPERATOR_SELECTION_ACCEPTED_T4_PARKED

docType: work-order

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-T3

dispatchBaseHead: `a230678aa`

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: delegated no-commit documentation worker for CVF-EAIC-KR-T3.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_2026-07-23.md`

Paired baseline:
`docs/baselines/CVF_GC018_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_2026-07-23.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture with `git rev-parse --short HEAD` at worker start
and require the exact operator-supplied committed dispatch HEAD.

Current-time notes: T2 closed with reviewer repairs at material commit
`9322829fb`; continuity was synchronized at `a230678aa`. T3 documentation-only
architecture decision support is released. Runtime, T4, T5, external-agent
invocation, and moratorium lift remain held.

Do-not-misread notes: do not use CLI/MCP to invoke an agent; do not use any
provider/API/account, browser, network, external process, or live quota; do not
implement source or ratify a runtime owner.

Required first actions: verify this `DISPATCH_READY` status, exact
executionBaseHead, clean worktree, authority chain, and required first reads;
then run the pre-implementation gate before writing.

Return contract: create exactly the two worker-owned outputs, leave them
unstaged and uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Produce an evidence-backed T3 architecture decision-support packet and threat
model for one accountable admission-monitor-stop-reconcile owner pattern.
Compare current source-backed candidates, identify reusable components and
missing adapters, recommend one pattern without ratifying it, preserve
provider neutrality and internal-agent autonomy, and define the negative proof
that T4 would need.

## Authority Chain

- Operator instruction: `tiep` on 2026-07-23 following accepted T2 closure,
  interpreted as authorization to continue with the next bounded
  documentation tranche.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V51_2026-07-22.md`.
- Roadmap:
  `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`.
- T2 policy semantics:
  `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md`.
- T2 independent review:
  `docs/reviews/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS_COMPLETION_REVIEW_2026-07-23.md`.
- Paired GC-018:
  `docs/baselines/CVF_GC018_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_2026-07-23.md`.
- Handoff stable front door: `docs/reference/agent_handoff/README.md`.

Authority boundary: T2 policy is canonical for this comparison. Current
runtime source proves only the symbols and bounded behavior directly cited.
The worker may recommend an architecture but cannot ratify an owner or
authorize build work.

## Agent Roles

- Orchestrator/dispatcher: dispatcher role.
- Worker: worker selected by the operator through manual copy/paste.
- Reviewer/closer: independent reviewer/closer role.
- Architecture decision owner: operator.
- Fresh operator authority required for owner ratification, T4 release, all
  implementation, every external action, and moratorium lift.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | accepted T2 semantics plus current repo-local runtime and canonical contract sources |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R0 documentation-only architecture comparison |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | one no-commit documentation worker selected through manual copy/paste |
| Reviewer role | independent reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | architecture recommendation released; final selection and every external/runtime action held |
| escalation condition | source contradiction, need for network/provider/process evidence, owner ratification, scope expansion, destructive action, or claim-boundary change |

## Scope

Risk ceiling: R0 documentation and repository-local evidence only.

Allowed scope:

- read only the authority chain, required first reads, and repo-local source
  files named in the Source Verification Block;
- inspect additional repo-local files only when needed to verify a directly
  relevant candidate symbol, recording each additional source in the worker
  output inventory;
- compare at least three owner patterns against one common rubric;
- recommend one accountable architecture pattern as decision support;
- define responsibilities, trust boundaries, threats, mitigations, residual
  gaps, and a T4 negative-proof plan;
- create exactly the two worker outputs and run local repository checks.

Forbidden scope:

- agent invocation through CLI/MCP or any other automatic agent route;
- provider/API/account/subscription access, secrets, browser, network,
  external repository, paid action, or live quota consumption;
- launching, monitoring, cancelling, terminating, or experimenting on any
  external process;
- runtime/source/test/checker/hook/registry/session/public-sync mutation;
- provider/model selection or hard-coding;
- final architecture-owner ratification or T4/T5 release;
- gating provider-native internal reasoning helpers that remain inside an
  already authorized parent agent session;
- staging, commit, push, publish, delete, move, or rename.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | authorized parent agent session | internal reasoning, exploration, decomposition, and context management remain autonomous within parent scope | EAIC-KR roadmap autonomy perimeter | independent governance begins only when a helper crosses the external/process/provider/account/credential/durable-action boundary | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | candidate EAIC coordination owner and external adapters | no invocation, provider/account use, process action, implementation, or live proof | T2 contract and source candidate inventory | worker documents adapter needs only; later roadmap owns any implementation | `DEFERRED_WITH_REASON` |

## Dependency Release Evidence

| Dependency | Evidence | Required state | Disposition |
| --- | --- | --- | --- |
| T2 policy completion | T2 completion review and material commit `9322829fb` | independently accepted | SATISFIED |
| T3 packet authority | operator instruction on 2026-07-23 | documentation-only packet authoring | SATISFIED |
| source-backed candidates | paired baseline Source Verification Block | three or more bounded candidates | SATISFIED |
| clean dispatch base | `a230678aa` | clean before packet authoring | SATISFIED |
| invocation moratorium | roadmap and active handoff | retained | SATISFIED_AND_RETAINED |

No conditional prior-tranche dependency remains open for documentation
execution. Final owner selection remains an explicit operator checkpoint, not
a worker dependency.

## Architecture Candidate Minimum Set

The worker must compare these candidates and may add a source-backed variant:

| Candidate ID | Accountable pattern | Required comparison stance |
| --- | --- | --- |
| CANDIDATE-A | governed-command-launcher-centric owner | test whether a command-specific launcher can own the wider assignment/session/process/provider chain without unsupported expansion |
| CANDIDATE-B | governed-session-contract-centric owner | test whether the control-plane session contract can coordinate launch, monitoring, stop, and reconciliation through adapters |
| CANDIDATE-C | Model-Gateway-centric owner | test whether provider execution and quota ownership can extend to external CLI/MCP process lifecycle without collapsing distinct boundaries |
| CANDIDATE-D | new EAIC coordinator composing existing primitives | test whether one new accountable coordination interface above the launcher, session contract, receipt stores, and Model Gateway minimizes semantic overreach |

The comparison must use one common rubric: policy fit, process binding,
cumulative envelope, telemetry, stop completeness, receipt correlation,
provider neutrality, bypass resistance, internal-agent autonomy, implementation
surface, and negative-proof feasibility.

## Worker Autonomy / No-Question Rule

Use best judgment inside Allowed scope. Repair documentation-only gate
failures and rerun them without asking the operator. Stop and return
`BLOCKED_WITH_REASON` only when the missing fact requires forbidden external
action, a policy decision, final owner ratification, a new write path, or a
scope expansion.

Do not turn ordinary analysis uncertainty into repeated questions. Label an
unsupported architecture claim as a residual gap or recommend parking.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "external-agent invocation architecture" --risk-ceiling HIGH --max-results 50 --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044.

Dispatch impact: apply source verification, handoff controls, exact output
ownership, no-commit conversion, checker read-ahead, and the external-action
moratorium.

## Required First Reads

Read before analysis:

1. `CVF_SESSION_MEMORY.md`;
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
4. `AGENT_HANDOFF_V51_2026-07-22.md`;
5. `docs/reference/guard_orientation/README.md`;
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
7. this work order and paired GC-018;
8. the EAIC-KR roadmap;
9. the T2 policy semantics and completion review;
10. source files listed in the Source Verification Block;
11. applicable worker-return and Markdown checker sources before writing the
    return artifact.

Provider-specific memory may guide the provider that owns it but is
`NOT_CVF_SOURCE` and cannot be used as architecture evidence.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Required First Reads; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm dispatch structure before worker execution and return shape before handoff |
| claimBoundary | checker compliance proves artifact structure only, not threat coverage or runtime control |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAIC-KR-T3 --title "EAIC KR T3 Owner Architecture And Threat Model" --date 2026-07-23 --base a230678aa --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic documentation-only no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added source candidate inventory, common comparison rubric, threat catalog, output contract, operator checkpoint, and invocation moratorium |
| checkerReadAheadConfirmation | applicable checker sources and canonical work-order standards were inspected before writing |
| docOnlyNewFields | candidateId; accountableOwnerPattern; componentRole; trustBoundary; threatId; mitigationOwner; residualGap; operatorSelectionState |
| claimBoundary | packet provenance only; no runtime, provider, public, or external-agent behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 selects an owner architecture and threat model after T2 | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan, T3 row; Roadmap Release Rules | `T3` | EAIC-KR roadmap | ACCEPT |
| D1-D6 policy and nine gaps are the architecture inputs | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T2_PROVIDER_NEUTRAL_INVOCATION_POLICY_SEMANTICS.md` | D1 through D6; Preserved Gap Register | `GAP-01` through `GAP-09` | T2 policy semantics | ACCEPT |
| launcher owns receipt-gated bounded command execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 168-186, 274-359 | `launchGovernedCommand` | governed command launcher | ACCEPT |
| launcher does not claim external interception proof | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 200, 225, 359, 507 | `externalInterceptionProved` | governed command launcher response/evidence | ACCEPT |
| preflight persists a decision receipt and separates it from execution proof | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 181-296 | `preflightGovernanceAction` | governance action preflight | ACCEPT |
| receipt store can claim one receipt once | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 36-73 | `claimReceipt` | `JsonReceiptConsumptionStore` | ACCEPT |
| execution store owns begin/finalize/read record operations | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 13-59 | `GovernedExecutionStore` | `JsonGovernedExecutionStore` | ACCEPT |
| session contract exposes limits, governed action request, and audit receipt | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | lines 28-47, 141, 212-239 | `AgentGovernedSessionContract` | governed session contract | ACCEPT |
| session contract creates receipt and trace identifiers | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | lines 322-386 | `createReceipt` | governed session contract | ACCEPT |
| provider router exposes selected provider identity | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/provider.router.contract.ts` | lines 17, 38-39, 145-155 | `selectedProviderId` | provider router contract | ACCEPT |
| gateway bridge owns provider adapter execution, quota check, and receipt building | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 59-73, 97-220 | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |
| quota ledger records provider/model usage | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | lines 30-100 | `QuotaLedger` | quota ledger | ACCEPT |
| gateway receipt carries provider/model and quota evidence | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | lines 7-59, 67-112 | `GatewayReceipt` | `GatewayReceiptBuilder` | ACCEPT |
| internal helpers remain autonomous inside the parent perimeter | LITERAL_INVARIANT | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Agent Internal Autonomy And Invocation Perimeter | `INTERNAL_AGENT` | EAIC-KR roadmap | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
| --- | --- | --- |
| candidateId | stable label for one architecture option | DOC_ONLY_NEW |
| accountableOwnerPattern | recommended single coordination-accountability pattern | DOC_ONLY_NEW |
| componentRole | responsibility assigned to an existing or proposed component | DOC_ONLY_NEW |
| trustBoundary | named transition where authority or evidence changes | DOC_ONLY_NEW |
| threatId | stable threat-model row identifier | DOC_ONLY_NEW |
| mitigationOwner | component accountable for a proposed mitigation | DOC_ONLY_NEW |
| residualGap | source or proof need left open after the proposed design | DOC_ONLY_NEW |
| operatorSelectionState | `PENDING_OPERATOR_SELECTION`, `ACCEPTED`, `REJECTED`, or `PARKED` | DOC_ONLY_NEW |

These fields are architecture-document fields only. They are not represented
as current runtime interfaces.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| worker output paths | both required worker outputs are absent at dispatch authoring | ACCEPT |
| complete current EAIC owner | no candidate source is claimed by this packet to cover every T2 requirement | ACCEPT |
| proposed field collision | proposed architecture fields are isolated as doc-only | ACCEPT |
| provider/model hard-code | no provider or model is chosen | ACCEPT |
| internal helper overreach | parent-internal helpers remain outside separate admission unless they cross the governed perimeter | ACCEPT |

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

## Pre-Flight Checks

The worker must use the exact committed dispatch HEAD supplied in the manual
prompt:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected: exact base match, clean worktree, this packet is
`DISPATCH_READY`, and pre-implementation passes. Stop on mismatch or dirt.

Mandatory remediation: repair and rerun every documentation-only failure
inside Allowed scope. Return `BLOCKED_WITH_REASON` only when correction needs
forbidden authority or a new write path.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> one no-commit worker -> independent reviewer/closer; operator owns architecture selection |
| phase | DISPATCH_AUTHORING and documentation EXECUTION released; CLOSURE, operator selection, T4, and SESSION_SYNC held |
| baseHeadFor(phase) | dispatchBaseHead=`a230678aa`; executionBaseHead is the committed dispatch HEAD supplied by operator; closureBaseHead is reviewer-captured |
| changedSetScope(phase) | dispatch authoring: roadmap, paired baseline, and work order; worker execution: exactly two worker-owned outputs |
| traceScope(phase, actor) | dispatcher records packet evidence; worker records only local reads, analysis, gates, and two outputs; reviewer records closure separately |
| commitOwner(phase) | dispatcher commits dispatch packet; worker commit forbidden; reviewer owns accepted closure commit |
| crossBatchIsolation | worker starts from a clean worktree with no unrelated batch |
| nextMoveSurfaces | worker does not edit continuity; reviewer and session-sync steward update next-move surfaces only once closure is accepted and the operator decides |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_COMPLETION_REVIEW_2026-07-23.md` |
| reviewerOwnedClosurePaths | paired baseline; this work order; T3 decision packet; worker return; completion review; roadmap and continuity only through reviewer-owned closure/session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Required Artifact Manifest

| Path | Required at worker handoff | Purpose |
| --- | --- | --- |
| `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md` | Yes | candidate comparison, recommendation, responsibility map, threat model, residual gaps, and T4 negative-proof needs |
| `docs/reviews/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_WORKER_RETURN_2026-07-23.md` | Yes | no-commit execution evidence and pending-review return |

Every other path is read-only or forbidden for worker writes.

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
| --- | --- | --- | --- |
| T3 architecture decision packet | stable reference path in Required Artifact Manifest | worker | REQUIRED |
| Worker return | dated review path in Required Artifact Manifest | worker | REQUIRED |
| Independent completion review | Reviewer Closure Conversion path | reviewer/closer | PENDING_REVIEW |
| Material closure commit | accepted outputs and reviewer artifacts | reviewer/closer | PENDING_REVIEW |
| Operator selection | explicit decision over reviewer-accepted recommendation | operator | ACCEPTED_CANDIDATE_D |
| Session sync | required only when accepted closure changes next allowed move | session-sync steward | PENDING_REVIEW |

## Write Ownership

Worker-owned create-only paths:

- `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md`;
- `docs/reviews/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_WORKER_RETURN_2026-07-23.md`.

Write mode: create-only, unstaged, uncommitted. Repository root is the required
working directory for all relative paths.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| durable owner family | `docs/reference/external_agent_invocation_control/` |
| new durable artifact | one stable undated T3 architecture decision-support packet |
| owner front door | existing family README remains read-only in worker scope |
| storage class | governed architecture documentation, not runtime state, queue, receipt store, or provider memory |
| generated aggregate disposition | N/A with reason: the Markdown decision packet has no generated aggregate |
| claim boundary | documentation-only recommendation; no implementation or public authority |

## Worker Output Checker Read-Ahead Mandate

Before creating the worker return, inspect the worker-return fast-gate and
Markdown structural checker sources and use a checker-safe skeleton. The
return must contain real content under Purpose, Target / Source, Scope /
Methodology, Findings / Position, Decision / Disposition, Risk / Corrective
Action, Source Inventory, Checker Source Read-Ahead Block, External Knowledge
Intake Routing, Epistemic Process Block, Agent Operation Trace Block, Delta
Execution Claim Boundary Control Block, Public Export Disposition, Claim
Boundary, `git status --short`, Changed Files, and No-Commit Statement.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_WORKER_RETURN_2026-07-23.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate:
`python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Required Decision Packet Content

The decision packet must include:

1. a one-paragraph bounded recommendation;
2. a candidate matrix covering CANDIDATE-A through CANDIDATE-D;
3. one accountable-owner responsibility map for admission, identity, launch,
   monitor, cumulative usage, stop, reconciliation, persistence, and review;
4. a D1-D6 and GAP-01 through GAP-09 coverage matrix;
5. a trust-boundary and data-flow sequence from approved assignment to final
   reconciled receipt;
6. a threat model covering at minimum spoofed assignment, receipt replay,
   double consumption, launch bypass, process escape/descendant survival,
   provider-session mismatch, approved-versus-observed provider/model
   mismatch, quota opacity, retry/fallback budget evasion, cancellation
   failure, forged completion, durable-store failure, and over-governance of
   provider-native internal helpers;
7. proposed mitigations, mitigation owners, evidence needs, and residual gaps;
8. a T4 negative-proof plan with deterministic pass/fail evidence;
9. an operator decision row set to `PENDING_OPERATOR_SELECTION`;
10. an explicit statement that the recommendation does not authorize build,
    invocation, provider use, or moratorium lift.

If no candidate safely satisfies the comparison rubric, recommend
`PARKED_KNOWLEDGE_GAP` or `NOT_READY` instead of forcing a selection.

## Execution Plan

| Step | Action | Output/evidence | Stop condition |
| --- | --- | --- | --- |
| 1 | verify dispatch status, exact base, clean tree, and startup authority | command evidence | mismatch, dirt, or held status |
| 2 | run pre-implementation autorun before writes | gate result | failure outside Allowed scope |
| 3 | read T2 semantics, completion review, and source candidate files | source inventory | critical source missing |
| 4 | compare four candidate patterns with one rubric | candidate matrix | inconsistent criteria |
| 5 | recommend or park; map responsibilities and D1-D6/GAP-01-09 | architecture packet | unsupported runtime claim |
| 6 | build threat model and T4 negative-proof plan | threat and proof tables | proof requires forbidden live action in T3 |
| 7 | create checker-safe worker return and run local gates | final two-path manifest | unrepairable scope violation |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| select one owner architecture | Candidate Minimum Set; Required Decision Packet Content | bounded recommendation plus operator selection row | reviewer checks common rubric and authority boundary | PASS for dispatch mapping |
| produce threat model | Required Decision Packet Content | threat catalog, mitigations, residual gaps | reviewer maps minimum threats | PASS for dispatch mapping |
| architecture after T2 semantics | Dependency Release Evidence | D1-D6/GAP matrix | compare to accepted T2 contract | PASS for dispatch mapping |
| preserve provider neutrality | Scope; candidate rubric | no hard-coded provider/model | exact-token and semantic review | PASS for packet design |
| preserve internal autonomy | Dual Agent Surface Matrix | internal-helper threat and boundary | roadmap perimeter comparison | PASS for packet design |
| no implementation | Forbidden scope; Claim Boundary | documentation-only disposition | changed-file review | PASS for packet design |
| define T4 evidence needs | Required Decision Packet Content | negative-proof plan | reviewer checks deterministic pass/fail shape | PASS for dispatch mapping |

## Design Control Carry-Forward

| Design control | Source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| knowledge before architecture | EAIC-KR Design Control Gate | T3 consumes accepted T1/T2 evidence | PASS |
| architecture before implementation | same | runtime and T4/T5 remain held | PASS |
| one accountable control owner | T3 objective | recommendation must name one coordination-accountability pattern | PASS |
| reuse without semantic overreach | source inventory | candidate must separate proven primitives from proposed adapters | PASS |
| fail-closed unknown usage | T2 D4 | architecture must preserve denial for automatic unknown-usage launch | PASS |
| provider neutrality | roadmap and T2 | no provider/model default | PASS |
| internal-agent autonomy | roadmap perimeter | no per-helper governance inside parent session | PASS |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a composed EAIC coordinator may provide the
cleanest accountability boundary while existing launcher, session, stores, and
gateway components remain bounded collaborators rather than being stretched
into universal owners.

Evidence Comparison Requirement: evaluate every candidate with the same
rubric and cite current source for every claimed existing capability.

Contradiction Handling Requirement: downgrade a candidate when source
boundaries contradict the proposed ownership. Preserve the contradiction as a
residual gap.

Claim Update Requirement: the worker may recommend a different candidate or
park T3 if evidence warrants it. The conclusion must name what changed the
prediction.

## Evidence Requirements

- exact executionBaseHead and clean pre-worker status;
- pre-implementation gate result before writes;
- source inventory with path, section or symbol, and bounded claim;
- candidate comparison using identical criteria;
- D1-D6 and GAP-01 through GAP-09 coverage;
- threat-to-mitigation-to-owner-to-proof mapping;
- exact `git diff --name-status` and `git status --short` at handoff;
- only the two Allowed output paths changed;
- worker-return fast gate and governed file-size check pass;
- explicit no-commit/no-stage statement;
- no external action, provider call, process action, or quota use.

## Verification Commands

Run from repository root:

```powershell
git diff --name-status
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
```

Do not run any command that invokes another agent, an MCP server, provider
API, browser, network, or external process under study.

## Acceptance Criteria

- [ ] Exactly two worker-owned outputs exist.
- [ ] CANDIDATE-A through CANDIDATE-D use one common comparison rubric.
- [ ] The recommendation is bounded and final selection remains
  `PENDING_OPERATOR_SELECTION`.
- [ ] Existing capabilities and proposed interfaces are clearly separated.
- [ ] One accountability pattern covers admission-monitor-stop-reconcile
  responsibilities without claiming implementation.
- [ ] D1-D6 and GAP-01 through GAP-09 are all mapped.
- [ ] All minimum threats have mitigation, owner, proof need, and residual gap.
- [ ] T4 negative proof has deterministic evidence and failure conditions.
- [ ] Provider/model neutrality and internal-agent autonomy are preserved.
- [ ] No runtime, live, external, public, or implementation claim is made.
- [ ] Worker fast gate and file-size check pass.
- [ ] Outputs are unstaged and uncommitted.

## Review Gate

The reviewer must independently re-read cited source, check the candidate
rubric for symmetry, challenge the recommended owner for semantic overreach,
verify the threat and gap coverage, and decide whether the packet is adequate
for operator selection. Reviewer acceptance does not itself authorize T4 or
ratify the recommended owner.

## Operator Checkpoint

Checkpoint state: `ACCEPTED_CANDIDATE_D`.

The reviewer accepted the decision packet as adequate evidence, and the
operator accepted CANDIDATE-D as the architecture direction on 2026-07-23.
That selection is not execution authorization. T4 and every implementation or
external-action lane remain held pending separate explicit authorization.

## Agent Operation Trace Block

| Field | Required worker evidence |
| --- | --- |
| Actor | no-commit documentation worker |
| Provider or surface | manually dispatched worker environment; identity recorded when exposed |
| Session or invocation | worker session or invocation identifier when exposed; otherwise `UNKNOWN_NOT_EXPOSED` |
| Working directory | repository root |
| Command or tool surface | repository-local read/edit/check only |
| Target paths | exactly the two Required Artifact Manifest paths |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | clean worktree at exact operator-supplied executionBaseHead |
| After status evidence | exactly two allowed untracked outputs and no staged changes |
| Diff evidence | `git diff --name-status` and `git status --short --untracked-files=all` |
| Approval boundary | documentation analysis only; no owner ratification or external action |
| Claim boundary | architecture recommendation and threat model only |
| Agent type | external worker manually dispatched by operator |
| Expected manifest | exactly two worker-owned outputs |
| Actual changed set | worker records the exact two-path changed set |
| Manifest delta | NONE when compliant; otherwise return `BLOCKED_WITH_REASON` |

Unknown provider/model/session data must remain unknown; do not guess it.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | one documentation-only architecture decision packet and one worker return |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: T3 creates documentation evidence, not a runtime CVF receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT through worker-return command evidence and exact changed manifest |
| invocationBoundary | no agent CLI/MCP, provider, browser, network, or process invocation |
| interceptionBoundary | no claim that any external invocation path is intercepted |
| claimLanguage | recommendation, proposed architecture, threat, mitigation, residual gap, and negative-proof need |
| forbiddenExpansion | runtime control, live proof, owner ratification, provider/model selection, cost claim, public claim, or moratorium lift |

## Worker Pending-Return Gate

Before returning, verify:

- work order status and execution base still match;
- only two allowed untracked outputs exist;
- no staged changes exist;
- all required decision-packet sections are substantive;
- worker fast gate and file-size guard pass;
- the return says `COMPLETE_PENDING_REVIEW`, not closed or approved;
- any repeated non-obvious defect is proposed for reviewer ADIF handling.

## External Action Checkpoint

Status: DENIED.

No CLI/MCP invocation, provider/API/account access, network, browser, process
launch/monitor/stop, quota use, public-sync, push, or deployment is authorized.

## Closure Checklist

- [ ] Reviewer re-computes worker gates.
- [ ] Reviewer verifies only allowed files changed.
- [ ] Reviewer challenges source claims and candidate symmetry.
- [ ] Reviewer maps every D1-D6, GAP, and minimum threat row.
- [ ] Reviewer records architecture recommendation disposition.
- [ ] Operator selection remains pending unless separately supplied.
- [ ] T4 remains held unless separately authorized once T3 evidence is accepted.
- [ ] Reviewer owns material commit and any continuity sync.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for base mismatch, dirty starting tree, missing
canonical source, need for external evidence, need for final operator choice,
required new write path, forbidden mutation, or unrepairable gate failure.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | CURRENT_REPOSITORY_SOURCE_INSPECTION_ONLY |
| reason | source is read only to bound current primitives and architecture gaps |
| requiredFutureAction | a later build roadmap must re-verify selected symbols and add implementation plus applicable live negative proof |

## Claim Boundary

This work order authorizes architecture decision support only. It does not
ratify an owner, implement or test runtime, invoke an agent through CLI/MCP,
use a provider/account, measure live quota, control a process, select a
provider/model, release T4/T5, lift the moratorium, or establish public,
security, cost, production, or live-governance readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only architecture packet with no public
implementation or release evidence.
