# CVF Agent Work Order - CADP-AI-T5 External Agent Adapter Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-14

Batch ID: CADP-AI-T5D

## Dispatch Prompt Envelope

```text
Role: decision-audit worker. Independent reviewer/closer is the later role.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: executionBaseHead captured from current committed HEAD at worker start.
Current-time notes: T4 is accepted bounded; T5 authorizes only a repo-local external-agent adapter decision audit.
Do-not-misread notes: do not implement an adapter, invoke MCP/CLI, launch an agent, access credentials, or invent missing authority.
Required first actions: capture HEAD/status; read startup surfaces, guard orientation, literal gotchas, paired baseline, this packet, checker sources, and every Source Verification path.
Return contract: create exactly the decision assessment and worker return; leave staging empty and HEAD unchanged; return COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED_WITH_REASON.
```

dispatchBaseHead: `17104935f442e63aba6a209faeaf31781c36d2e9`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Determine, from current CVF-governed sources, whether CADP T5 can later support
a bounded external-agent read/query metadata adapter, or must be rejected or
deferred. Produce decision evidence only; do not implement the recommendation.

completionReviewPath: `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md`

reviewerOwnedClosurePaths: completion review; CADP-AI roadmap; applicable
GC-051 registry source and generated aggregate; session continuity.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id CADP-AI-T5 --title "CADP AI T5 External Agent Adapter Decision" --date 2026-08-14 --base 17104935f442e63aba6a209faeaf31781c36d2e9 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "CADP-AI-T4 accepted bounded at 7dfee6e4d77d1fe1102f627869c20e176f630304" --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified decision-only scope, exact manifest, terminal enum, and reviewer conversion |
| checkerReadAheadConfirmation | all checker sources listed in the paired baseline read-ahead block were read before authoring |
| docOnlyNewFields | `terminalRecommendation`; `prerequisiteDisposition`; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no runtime, provider, live, public, MCP, or CLI behavior claim |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation | Acceptance evidence | Disposition |
|---|---|---|---|
| optional adapter decision | three-outcome terminal decision audit | exact `terminalRecommendation` | MAPPED |
| CLI/MCP read/query or rejection | bounded metadata candidate compared with explicit reject/defer routes | prerequisite and overlap matrices | MAPPED |
| auth, ingress, mutation, redaction | mandatory prerequisite rows with fail-closed gap states | source-backed row dispositions | MAPPED |
| dual-surface proof | internal/external consumer matrix | dual-agent accounting evidence | MAPPED |
| no auto-implementation | documentation-only two-path manifest | diff and no-action evidence | MAPPED |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION_MEMORY.md`
4. `AGENT_HANDOFF_V59_2026-08-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `docs/baselines/CVF_GC018_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md`
8. this work order and every Source Verification path below

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator release | 2026-08-14 `next`; T4 dependency evidence is cited in the next row | ACCEPT_DECISION_ONLY |
| roadmap order | CADP-AI Work Plan T5 follows accepted T3/T4 | ACCEPT |
| T4 prerequisite | completion review and material commit `7dfee6e4d77d1fe1102f627869c20e176f630304` | ACCEPT |
| implementation authority | no committed T5 implementation work order exists | DENY |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | authorizes T5 decision analysis only |
| Dispatcher | authors and commits baseline/work order/roadmap dispatch state |
| Worker | creates the two decision-evidence paths without commit |
| Reviewer/closer | independently challenges the recommendation and owns material closure |
| Session-sync steward | updates continuity separately following accepted reviewer disposition |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | decide whether a bounded CADP external-agent metadata adapter is currently supportable |
| scope classification | DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT |
| primary task class | source-backed architecture and readiness decision |
| risk sensitivity | high: a false-ready decision could imply external execution or mutation authority |
| selected role route | SINGLE_AGENT_SINGLE_ROLE |
| orchestration requirement | no-commit worker followed by independent reviewer/closer |
| role separation basis | the worker recommendation cannot independently authorize its own future implementation |
| escalation condition | source contradiction, missing governed input file, or any need for runtime/implementation action |

## Pre-Flight Checks

- record `git rev-parse HEAD` as execution base;
- require clean staging and no pre-existing changes on either target path;
- confirm both target paths are absent;
- read all required authority and checker sources;
- run worker-context ADIF resolution before writing;
- stop if a third changed path is required.

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact two-path manifest. Return
`BLOCKED_WITH_REASON` only for a source contradiction or missing governed file
that prevents any terminal decision. Missing implementation prerequisites are
an expected `DEFER_WITH_MISSING_AUTHORITY` result, not a reason to invent them.

## Allowed Scope

Worker may create exactly:

1. `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md`
2. `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_WORKER_RETURN_2026-08-14.md`

Read-only inspection elsewhere is allowed. Any third changed path is a scope
violation.

Forbidden: production/test/schema/checker/registry/roadmap/session edits;
MCP/CLI/browser/provider/network invocation; external-agent launch; secrets or
credentials; staging; commit; public sync; deploy; production action.

## Write Ownership

Worker owns only the two allowed paths. Reviewer owns repairs, completion
review, roadmap/registry disposition, material commit, and session continuity.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T5 permits adapter decision or explicit rejection only after T3/T4 acceptance | ROADMAP_BOUNDARY | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` | Work Plan T5 | `optional external-agent adapter decision` | CADP-AI roadmap | ACCEPT |
| T4 guard is standalone and unwired | CLOSURE_EVIDENCE | `docs/reviews/CVF_CADP_AI_T4_AUTHORITY_BOUNDARY_MACHINE_ENFORCEMENT_COMPLETION_2026-08-14.md` | Final Disposition | `ACCEPTED_CLOSED_PASS_BOUNDED` | T4 independent review | ACCEPT |
| generic MCP integration is advisory only | LITERAL_INVARIANT | `docs/guides/CVF_GENERIC_MCP_ADAPTER_INTEGRATION_GUIDE_2026-05-31.md` | Protocol and Claim Boundary | `runtimeExecutionAuthorized` | MCP integration guide | ACCEPT |
| Model Gateway MCP bridge remains boundary-only | ROADMAP_BOUNDARY | `docs/baselines/CVF_GC018_RTAD_T5_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY_2026-06-18.md` | Forbidden Scope | `CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY` | RTAD T5 | ACCEPT |
| external-agent metadata readout has a prior decision boundary but no adapter implementation | VALUE_SET | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md` | T0-T4 Result and Dual Agent Surface Matrix | `DEFERRED_WITH_REASON` | ASSF external-agent boundary | ACCEPT |
| invocation implementation remains unauthorized | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan and Next Allowed Move | `NOT_OPENED_NO_IMPLEMENTATION_AUTHORITY` | invocation-control roadmap | ACCEPT |

## Current Runtime Freshness Verification

| Runtime claim | Verification source | Observed value | Disposition |
|---|---|---|---|
| CADP T4 remains standalone and unwired | T4 completion review plus current roadmap | no hook/autorun/CI wiring authorized | ACCEPT |
| generic MCP adapter remains advisory | generic MCP integration guide Claim Boundary | runtime execution authorization remains false | ACCEPT |
| external-agent invocation implementation remains parked | invocation-control roadmap Work Plan and Next Allowed Move | T5 implementation not opened | ACCEPT |
| this packet adds no runtime path | exact Required Artifact Manifest | two Markdown evidence paths only | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Source Verification Block`; `Current Runtime Freshness Verification`; `Agent Operation Trace Block`; `Worker Return Packet Shape Contract` |
| gateRunPurpose | confirm the exact dispatch and worker-return structure before commit |
| claimBoundary | structural read-ahead does not establish adapter readiness or implementation authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint; current authority and no-runtime boundaries remain mandatory |

## Required Decision Analysis

Build a prerequisite matrix with at least these rows:

- owner and package boundary;
- caller authentication and identity binding;
- ingress schema and size validation;
- exact metadata field allowlist;
- secret/private-provenance redaction;
- mutation, activation, certification, execution, provider-call, credential-
  resolution, and external-launch denial;
- deterministic error and receipt shape;
- replay/freshness behavior;
- internal-agent and external-agent surface accounting;
- package-root/transport discoverability;
- focused negative-proof plan;
- registry, hook, public, and session effects.

For every row record source, observed state, gap, and one of `SATISFIED`,
`MISSING_AUTHORITY`, `CONFLICT`, or `NOT_APPLICABLE_WITH_REASON`.

Then return exactly one `terminalRecommendation`:

- `IMPLEMENTATION_READY_BOUNDED_READ_ONLY`: all mandatory rows are satisfied;
- `REJECT_WITH_REASON`: current authority conflicts with the candidate or the
  candidate has no bounded value distinct from existing owners;
- `DEFER_WITH_MISSING_AUTHORITY`: value may exist, but one or more mandatory
  owners/contracts/proofs are absent.

A positive result must propose a future implementation manifest and tests but
must not create them. A rejection or deferral must list exact reopen conditions.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | CADP Guard Contract, Execution Plane projection, Model Gateway constraint projection | may consume governed metadata only within existing contract authority | T1/T3A/T3B/T4 sources | no new internal adapter in T5 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | candidate read/query surface, not implemented | no mutation, execution, provider, credential, launch, or public authority | T5 decision assessment | decision only; future packet required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact or recommendation is ingested |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T5 baseline and this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources may support the decision |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one decision-audit worker, followed by independent reviewer/closer |
| phase | worker execution pending |
| baseHeadFor(phase) | dispatchBaseHead=`17104935f442e63aba6a209faeaf31781c36d2e9`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact two-path worker manifest |
| traceScope(phase, actor) | worker records commands, evidence reads, diff, status, and terminal recommendation |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; independent reviewer owns commits |
| crossBatchIsolation | no unrelated changed path may be touched or absorbed |
| nextMoveSurfaces | reviewer-owned completion, roadmap, registry decision, and separate session sync |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_COMPLETION_2026-08-14.md` |
| reviewerOwnedClosurePaths | completion review; CADP-AI roadmap; applicable GC-051 entry/aggregate; session continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md` | create source-backed prerequisite matrix, overlap/value analysis, terminal recommendation, and reopen/future-manifest conditions |
| `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_WORKER_RETURN_2026-08-14.md` | create full-gate pending-review evidence packet |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_WORKER_RETURN_2026-08-14.md`

contractProfile: `WORKER_RETURN_FULL_GATE_V1`

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: `FORBIDDEN`

workerReturnSkeleton: `CHECKER_SAFE_SKELETON_REQUIRED`

Literal contract terms:

contractProfile: WORKER_RETURN_FULL_GATE_V1

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Required Artifact Manifest

| Path | Owner | Required state at worker return |
|---|---|---|
| `docs/assessments/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md` | Worker | new decision assessment with one terminal recommendation |
| `docs/reviews/CVF_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_WORKER_RETURN_2026-08-14.md` | Worker | new full-gate pending independent review packet |

## Acceptance Criteria

- exact two worker paths and no other diff;
- every required prerequisite row has source evidence and terminal state;
- overlap with generic MCP, RTAD, ASSF, and invocation-control owners is
  reconciled without duplicating authority;
- terminal recommendation uses exactly one allowed enum and follows the matrix;
- positive recommendation contains only a future manifest/test plan;
- rejection/deferral contains exact reopen conditions;
- no runtime, adapter, external-agent, provider, credential, network, or public
  behavior occurs or is claimed;
- fast gate passes, staging is empty, and HEAD equals execution base.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_markdown_structural_completeness.py --enforce
python governance/compat/check_external_agent_absorption_table.py --enforce
python governance/compat/check_external_knowledge_intake_routing.py --enforce
python governance/compat/check_delta_execution_claim_boundary.py --enforce
git diff --check
git diff --stat
git status --short
git diff --cached --name-only
git rev-parse HEAD
```

## Execution Plan

1. capture clean execution base and verify the two-path manifest;
2. read all current authority and checker sources;
3. build prerequisite and owner-overlap matrices;
4. derive exactly one terminal recommendation without inventing semantics;
5. author the assessment and worker return;
6. run all gates, repair only the two allowed paths, and return uncommitted.

## Evidence Requirements

Evidence must identify every source actually read, counts for each prerequisite
disposition, owner overlap, the logical derivation of the terminal outcome,
future manifest or reopen conditions, command exits, exact diff, staging state,
and execution-base/HEAD equality.

## Review Gate

Worker success is pending review only. The reviewer must independently test the
matrix against current sources, challenge false-ready and false-reject paths,
verify no existing owner was duplicated, and decide closure or repair.

## Closure Checklist

- [ ] both required worker artifacts exist;
- [ ] exactly one terminal recommendation is present;
- [ ] mandatory prerequisites reconcile to the recommendation;
- [ ] no runtime or implementation claim is made;
- [ ] full worker-return fast gate passes;
- [ ] staging is empty and HEAD unchanged;
- [ ] independent reviewer disposition remains pending.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_INDEPENDENT_REVIEW` when all worker-owned criteria and
gates pass. Return `BLOCKED_WITH_REASON` only when the assessment itself cannot
be completed due to source contradiction or missing required governed input.

## Operator Checkpoint

No T5 implementation, T6 live proof, or T7 closure/public lane opens from the
worker recommendation. Following independent review, await a new explicit operator
decision and fresh governed packet for any further action.

## Worker Return Required Evidence

Record execution base, exact changed paths, prerequisite counts by disposition,
terminal recommendation, overlap result, reopen or future-manifest conditions,
all command exits, empty staging, unchanged HEAD, and residual uncertainty.

## MCP/CLI Adapter Boundary

| Field | Value |
|---|---|
| Adapter scope | decision evidence for a possible future read/query metadata interface only |
| No-runtime-overclaim | no adapter executes, intercepts, wraps, launches, mutates, authenticates, or calls a provider in this tranche |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | CADP-AI-T5D dispatch authoring, 2026-08-14 |
| Working directory | repository root |
| Command or tool surface | PowerShell, repository Python guards, and apply-patch editing |
| Target paths | paired T5 baseline, paired T5 work order, CADP-AI roadmap dispatch row |
| Allowed scope source | operator `next`, T4 completion review, and CADP-AI roadmap T5 entry |
| Before status evidence | clean worktree at HEAD `17104935f442e63aba6a209faeaf31781c36d2e9` |
| After status evidence | exact three-path unstaged dispatch authoring set before validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | decision-only T5 dispatch; no implementation or runtime release |
| Claim boundary | packet authoring and dispatch gates only |
| Agent type | single dispatcher role |
| Invocation ID | `cadp-ai-t5d-dispatch-2026-08-14` |
| Expected manifest | T5 baseline; T5 work order; CADP-AI roadmap |
| Actual changed set | T5 baseline; T5 work order; CADP-AI roadmap |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repo-local CADP T5 adapter decision audit |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local read-only inspection and governed Markdown authoring only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | decision recommendation only, pending independent review |
| forbiddenExpansion | no source implementation, MCP/CLI invocation, agent launch, provider/live, credentials, public sync, deploy, production, T6, or T7 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision audit with no public artifact change.

## Claim Boundary

This work order authorizes exactly two documentation artifacts and a bounded
recommendation. It does not authorize an adapter or prove runtime, auth,
redaction, transport, provider, external-agent, public, or production behavior.
