# CVF Agent Work Order - Governance Latency WS2 T0 Capability Owner Decision

## Dispatch Prompt Envelope

Role: documentation and source-verification worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GOVERNANCE_LATENCY_WS2_T0_2026-08-05.md`.

dispatchBaseHead: `eb055983f75b0170fdaf057a75de9987044db9d4`.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`.

closureBaseHead: `NOT_EXECUTED_YET`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Current-time notes: L0 is closed at `daf7dba04`; Gate A is
`PROCEED_WS2_ONLY`; operator released this bounded T0 continuation on
2026-08-05.

Do-not-misread notes: this is an owner/feasibility audit, not design
implementation or BUILD. The current sandbox status is not technical
zero-network proof.

Required first actions: complete startup acknowledgment; capture HEAD/status;
read the paired baseline, guard orientation, literal gotchas, source files and
checker sources named below; confirm no unexpected worktree changes.

Return contract: create exactly the audit and worker return, run the worker
fast gate, leave both uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

Memory class: FULL_RECORD

Status: DISPATCH_READY

Commit mode: WORKER_MUST_NOT_COMMIT

docType: work-order

Date: 2026-08-05

Batch ID: CVF-GOVERNANCE-LATENCY-WS2-T0

GC-018 required: Yes

GC-018 baseline:
`docs/baselines/CVF_GC018_GOVERNANCE_LATENCY_WS2_T0_2026-08-05.md`

Worker return path:
`docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_WORKER_RETURN_2026-08-05.md`

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-GOVERNANCE-LATENCY-WS2-T0 --title "Capability Enforcement Owner And Feasibility Decision" --date 2026-08-05 --base eb055983f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with bounded source audit, exact outputs, roles, evidence, and stop rules |
| checkerReadAheadConfirmation | named dispatch checker sources read before final authoring |
| docOnlyNewFields | ownerCandidate, capabilityProfile, deniedCapability, allowedCapability, platformDisposition, proofCase, enforcementReceipt, T0Decision |
| claimBoundary | dispatch provenance only; no runtime, provider, live, public, Web, CLI, or MCP behavior claim |

## Purpose

Determine the smallest source-native owner and viable enforcement seam for WS2
zero-network role profiles. Return a source-backed decision and future proof
contract without implementing, executing, or claiming the capability.

## Authority Chain

Operator continuation -> L0 completion `daf7dba04` and Gate A
`PROCEED_WS2_ONLY` -> paired WS2-T0 GC-018 -> this work order -> independent
review. The downstream roadmap remains non-authoritative evidence context.

## Agent Roles

- dispatcher owns packet fidelity and dispatch commit;
- documentation worker owns exactly the audit and worker return without commit;
- independent reviewer/closer verifies the decision and owns accepted closure;
- session-sync steward updates continuity only when the reviewed decision
  changes current mode or next move.

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, generated active session state, V54,
guard orientation, literal gotchas, paired baseline, this work order, all source
paths in Source Verification, and all checker paths in Checker Source
Read-Ahead before writing.

## Pre-Flight Checks

Capture HEAD and actual worktree status; verify the two worker paths do not
already exist; confirm downstream/public clones are outside write scope;
confirm no provider/network/package command is planned; run the ADIF resolver
for the worker task class if it differs from dispatch authoring.

## Write Ownership

Worker writes only the audit and worker return. Reviewer owns an optional
completion and all accepted commits. Session files, runtime source, tests,
checkers, roadmaps, downstream, and public-sync are excluded.

## Dependency Release Evidence

| Dependency | Artifact | Closure commit | Disposition |
|---|---|---|---|
| L0 independent Gate A | `docs/reviews/CVF_GOVERNANCE_LATENCY_L0_COMPLETION_2026-08-05.md` | `daf7dba04` | ACCEPT |
| Operator checkpoint | 2026-08-05 instruction to continue | current conversation authority reflected in paired baseline | ACCEPT |
| WS2 implementation authority | no such authority required for documentation-only T0 | N/A with reason: implementation remains forbidden | ACCEPT |

## Allowed Changed Paths

Worker-owned:

1. `docs/audits/CVF_GOVERNANCE_LATENCY_WS2_T0_OWNER_FEASIBILITY_AUDIT_2026-08-05.md`
2. `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_WORKER_RETURN_2026-08-05.md`

Reviewer-owned only if needed:

3. `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md`

No other path is allowed.

## Required Source Audit

Inspect source-native owners for:

- policy decisions and risk mapping;
- command/runtime executor injection and default behavior;
- actual process creation or absence;
- filesystem/environment mutation boundaries;
- network/provider/remote-Git seams;
- sandbox ownership and whether it is label, delegation, or technical
  isolation;
- receipt and diagnostic owners;
- internal-agent and external CLI/MCP boundaries;
- Windows, Linux, and CI enforcement feasibility;
- existing tests and missing adversarial negative controls.

Search current source before proposing any field, enum, path, class, or owner.
Do not treat documentation aspiration as current runtime behavior.

## Execution Plan

1. Capture base/status and read checker sources.
2. Enumerate candidate provenance owners using local searches.
3. Inspect exact source and focused existing tests without running bypasses.
4. Build owner, enforcement-gap, platform, threat, cheap-option, proof, and
   receipt matrices.
5. Select exactly one T0 decision token.
6. Author the worker return, run worker fast gate, and stop uncommitted.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| owner/feasibility audit | produce source map, owner decision, platform and bypass matrices, cheap alternative, proof plan, cost budget, and one T0 decision |
| worker return | report exact commands, changed set, limitations, stop-rule state, and no-commit evidence |

## Audit Required Sections

The audit must contain:

1. Purpose.
2. Target / Source.
3. Scope / Methodology.
4. Current Owner Surface Map.
5. Present Versus Missing Enforcement Matrix.
6. Platform Feasibility Matrix.
7. Threat And Bypass Matrix.
8. Cheap-Alternative Comparison.
9. Candidate Profile Contract marked doc-only.
10. Adversarial Proof Plan that runs nothing in T0.
11. Receipt And Diagnostic Requirements.
12. Governance Cost And Stop Rule.
13. Findings / Position.
14. Risk / Corrective Action.
15. Source Verification Block.
16. Dual Agent Surface Matrix.
17. Epistemic Process Block.
18. Finding-To-Governance Learning Disposition.
19. Checker Source Read-Ahead Block.
20. Agent Operation Trace Block.
21. Delta Execution Claim Boundary Control Block.
22. Public Export Disposition.
23. Claim Boundary.

## Decision Contract

Return exactly one:

- `OWNER_FOUND_DESIGN_READY`: existing owner, interception boundary, platform
  feasibility, and adversarial proof seam are all source-backed;
- `OWNER_FOUND_NEEDS_FOUNDATION`: a source-native owner exists, but one bounded
  prerequisite foundation is missing and named;
- `VALUE_PARKED_NO_VIABLE_OWNER`: no existing owner can enforce the boundary at
  acceptable cost without a new control plane or wrapper;
- `BLOCKED_SOURCE_CONTRADICTION`: current sources conflict and a decision would
  require guessing.

No token authorizes implementation. A future design or build tranche requires
another explicit operator checkpoint and new governance packet.

## Acceptance Criteria

- audit and worker return are the only worker changes;
- every source fact cites a real path plus line/section or symbol;
- current runtime behavior and proposed doc-only contract are separated;
- default stub, injected executor, policy gate, and sandbox label are traced;
- no claim equates sandbox status with isolation;
- owner comparison prefers existing Execution Plane and policy owners before a
  new surface;
- platform matrix covers Windows, Linux, and CI independently;
- threat matrix covers `uv`, `pip`, `curl`, `wget`, remote Git, Python
  HTTP/socket, environment creation, inherited credentials/proxy, shell escape,
  alternate interpreter, and tracked-script allowance;
- proof plan specifies pre-effect blocking and residue assertions without
  executing any probe in T0;
- cheap alternatives and no-new-control-plane option are evaluated;
- external CLI/MCP support remains deferred unless source-backed;
- governance cost budget and third-repair stop are recorded;
- exactly one T0 decision token is returned;
- worker fast gate passes before return;
- worker makes no commit.

## Evidence Requirements

- source path plus line/section or symbol for each current fact;
- negative-search commands and exact bounded roots;
- Git evidence for the two-path changed set;
- explicit UNKNOWN or absent behavior where source does not prove enforcement;
- no execution receipt or provider receipt claimed;
- worker fast-gate output and actual pending status in the return.

## Review Gate

An independent reviewer must verify semantics before any commit: existing-owner
coverage, current/proposed separation, platform feasibility, bypass completeness,
cheap-alternative analysis, one decision token, and no hidden BUILD authority.

## Closure Checklist

- [ ] Audit and worker return exist at exact paths.
- [ ] No other worker path changed.
- [ ] All source claims are directly verified.
- [ ] Current sandbox semantics are not overstated.
- [ ] Windows/Linux/CI and all bypass families are covered.
- [ ] Exactly one T0 decision is present.
- [ ] Worker fast gate passes.
- [ ] Independent reviewer disposition is recorded.
- [ ] Public export remains private/deferred.
- [ ] Continuity is synchronized only if closure changes next move.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all worker acceptance items pass and the
two outputs remain uncommitted. Return `BLOCKED_WITH_REASON` immediately on a
stop condition, with the exact source or authority blocker.

## Operator Checkpoint

The operator's continue instruction releases WS2-T0 documentation execution after this
packet passes and is committed. It does not release any subsequent design or
build. After independent T0 review, stop for a new operator decision before
opening another tranche.

## Stop Conditions

Stop on third repair, source contradiction, unexpected mutation, need for any
network/process/package-manager execution, forbidden path, implementation need,
or inability to source-verify a claimed current field/symbol. Do not widen the
packet to make the decision appear ready.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Gate A releases only WS2 consideration | VALUE_SET | `docs/reviews/CVF_GOVERNANCE_LATENCY_L0_COMPLETION_2026-08-05.md` | Gate A Recommendation, lines 64-72 | `PROCEED_WS2_ONLY` | L0 completion review | ACCEPT |
| Worker may inspect an injectable task executor | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` | lines 36-38 | `executeTask` | `CommandRuntimeContractDependencies` | ACCEPT |
| Default task execution is a deterministic stub | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` | lines 43-67 | `defaultExecuteTask` | `CommandRuntimeContract` | ACCEPT |
| Allow and sandbox decisions reach the task executor with a boolean sandbox argument | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` | lines 87-97 | `execute` | `CommandRuntimeContract` | ACCEPT |
| Policy maps R3 to sandbox and R2 to review | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/policy.gate.contract.ts` | lines 39-49 | `deriveGateDecision` | `PolicyGateContract` | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `ownerCandidate` | audit owner comparison | NONE |
| `capabilityProfile` | candidate role profile name | NONE |
| `deniedCapability` | candidate denial family | NONE |
| `allowedCapability` | candidate allowance family | NONE |
| `platformDisposition` | Windows/Linux/CI result | NONE |
| `proofCase` | future adversarial proof case | NONE |
| `enforcementReceipt` | future receipt requirements | NONE |
| `T0Decision` | bounded audit decision | NONE |

## Worker Autonomy / No-Question Rule

Repair allowed-scope shape failures directly after reading the failing checker.
Return to the orchestrator only for a stop condition. Do not ask the operator to
choose among equivalent read-only source inspection methods.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | `NONE_RETURNED` |
| Dispatch impact | canonical source-verification and handoff controls remain binding |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | candidate Execution Plane policy/runtime seam | read-only owner audit; no executor or policy mutation | verified runtime sources | internal source analysis only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no accepted enforcement adapter | no external ingress, authentication, mutation, receipt, or runtime support claim | source verification has not established an adapter | separate future source-verified packet required | `DEFERRED_WITH_REASON` |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | provenance runtime/source plus previously accepted L0 completion |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| scopeClassification | `DOCUMENTATION_AND_SOURCE_VERIFICATION_ONLY_NO_COMMIT` |
| risk sensitivity | capability-boundary decision with no execution |
| Worker role | source audit and no-commit return |
| Reviewer role | independent semantic review and closure ownership |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | operator released T0 only; later design/build remains stopped |
| escalation condition | stop conditions in this work order |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> documentation worker -> independent reviewer/closer -> session-sync steward |
| phase | dispatch then no-commit worker return then reviewer closure conversion |
| baseHeadFor(phase) | dispatchBaseHead=`eb055983f75b0170fdaf057a75de9987044db9d4`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`NOT_EXECUTED_YET` |
| changedSetScope(phase) | worker owns exactly audit and worker return; reviewer may own optional completion |
| traceScope(phase, actor) | each role records its own commands, status, diff, authority, and claim boundary |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; reviewer/closer owns accepted material commit |
| crossBatchIsolation | no downstream, public-sync, session, runtime, test, checker, package, Web, CLI, or MCP paths |
| nextMoveSurfaces | session-sync steward updates active state/front door/V54 only when accepted review changes mode or next move |
| closerOwner | independent reviewer/closer designated before worker execution |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` if semantic corrections or a separate decision record are needed |
| reviewerOwnedClosurePaths | optional completion plus accepted audit and worker return commit ownership |
| closureOwner | independent reviewer/closer who did not author the audit decision |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before authoring the audit or return, read all applicable audit/review,
epistemic, finding-learning, public-disposition, AOT, delta-boundary,
corpus/rescan, and worker-return checker sources. Gate runs confirm a prepared
shape; they are not the first discovery method.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | L0 completion -> source-native owner audit -> independent T0 review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | WS2-T0 audit and review |
| Disposition | use provenance L0 conclusion; do not re-absorb or import downstream runner |
| Claim boundary | source audit only; downstream remains non-authoritative and read-only |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| durable owner | existing `docs/audits/` for T0 decision evidence and `docs/reviews/` for worker return |
| new foundation directory | N/A with reason: no new storage or control-plane foundation is authorized |
| index or discovery surface | N/A with reason: two bounded execution artifacts do not create a new canonical reference family |
| aggregate discipline | N/A with reason: no JSON aggregate is created or modified |
| relocation/split | N/A with reason: no existing foundation file is moved or split |
| claim boundary | storage accounting only; no runtime owner is created by documentation placement |

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <committed-dispatch-head> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

No provider, network, package manager, remote Git, live-proof, or denied-tool
command belongs in the T0 verification set.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Dispatch Prompt Envelope, Dependency Release Evidence, Source Verification Block, New Doc-Only Fields, Agent Handoff Contract Control Block, Reviewer Closure Conversion, Worker Return Packet Shape Contract |
| gateRunPurpose | confirm dispatch conformance after source-first authoring; machine gates provide evidence rather than first discovery |
| claimBoundary | T0 work-order readiness only; no implementation, execution, provider, or external-agent support claim |

## Epistemic Process Block

Expected Result / Prediction: current source will identify a plausible
Execution Plane owner but will expose missing technical isolation below the
existing sandbox status.

Evidence Comparison Requirement: compare source and tests for policy, executor,
process/network/environment, receipt, and adapter paths; retain absent or
contradictory behavior explicitly.

Contradiction Handling Requirement: use `BLOCKED_SOURCE_CONTRADICTION` rather
than inventing a field, wrapper, platform guarantee, or owner.

Claim Update Requirement: select design-ready only when owner, interception,
platform, and proof seams are source-backed; otherwise narrow or park.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | WS2-T0 work-order dispatch, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | local source reads, ADIF resolver, apply-patch, pre-dispatch gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | operator continuation after L0 Gate A |
| Before status evidence | HEAD `eb055983f`; clean worktree |
| After status evidence | exact paired dispatch packet pending commit |
| Diff evidence | `git status --short`; exact two-path name-status |
| Approval boundary | documentation-only T0 owner/feasibility audit |
| Claim boundary | no design implementation, build, runtime proof, provider, downstream, public, or production claim |
| Agent type | dispatcher |
| Invocation ID | `governance-latency-ws2-t0-work-order-2026-08-05` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only owner and feasibility analysis |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists or is required for T0 |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local source and Git evidence only |
| invocationBoundary | read-only provenance inspection plus two governed documentation outputs |
| interceptionBoundary | no direct process, network, filesystem, environment, shell, IDE, CLI, MCP, or provider interception |
| claimLanguage | candidate owner and future proof contract only |
| forbiddenExpansion | runtime, tests executing bypasses, provider/live, downstream, public, deployment, readiness, and universal enforcement |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: WS2-T0 is private provenance source analysis. No public artifact or
public-sync action is authorized.

## Claim Boundary

This work order authorizes exactly two documentation outputs that decide the
source-native owner and feasibility for WS2. It does not authorize DESIGN
implementation, SPEC implementation, BUILD, process/network/package execution,
provider calls, downstream edits, public-sync, push, deployment, or a claim
that zero-network capability enforcement currently exists.
