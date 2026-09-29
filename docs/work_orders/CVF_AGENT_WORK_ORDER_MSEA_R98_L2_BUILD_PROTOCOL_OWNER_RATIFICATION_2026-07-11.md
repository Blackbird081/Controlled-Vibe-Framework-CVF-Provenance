# CVF Agent Work Order MSEA-R98 L2 Build Protocol Owner Ratification

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R98

Dispatch base head: `138762889`

Commit mode: `WORKER_MAY_COMMIT`

## Dispatch Prompt Envelope

Role: sequential dispatcher, decision implementer, self-reviewer/closer and
session-sync steward. Canonical packet: this file. Commit mode:
`WORKER_MAY_COMMIT`. executionBaseHead: dispatch-session commit.

Current-time notes: 2026-07-11; use current `AGENTS.md` and doctrine text.

Do-not-misread notes: ratify mapping only; do not edit doctrine or AGENTS.

Required first actions: read startup files, paired baseline, R96 completion,
frozen L2 section, `AGENTS.md`, route map and single-agent standard.

Return contract: make a bounded decision, self-review without claiming
independence, run real-range closure gates, and split material/session commits.

## Purpose

Decide whether `AGENTS.md` is the active differently named L2 Build Protocol
owner and record the accepted mapping with explicit exclusions.

## Authority Chain

User authorization -> R96 accepted candidate -> R98 baseline/work order ->
source comparison -> self-review boundary -> commit steward -> session sync.

## Agent Roles

- Implementer: route/map decision only.
- Self-reviewer/closer: challenge coverage and overclaim; independence rejected.
- Session-sync steward: separate protected commit.

## Scope / Target / Owner Boundary

Material paths:

- `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md`
- `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
- `docs/reference/system_chain/README.md`
- `docs/reviews/CVF_MSEA_R98_L2_BUILD_PROTOCOL_OWNER_RATIFICATION_COMPLETION_2026-07-11.md`

No `AGENTS.md`, doctrine, legacy, runtime, checker, public, provider, or MAO
path may change.

## Write Ownership

Exactly four material paths plus standard separate session-sync paths.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| R96 candidate accepted | `docs/reviews/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_COMPLETION_2026-07-11.md` | `d733abd70` | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R98 --title "L2 Build Protocol Owner Ratification" --date 2026-07-11 --base 138762889 --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic worker dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact four-path decision scope and self-review controls |
| checkerReadAheadConfirmation | dispatch, single-agent, handoff, trace, freshness, closure and public guards |
| docOnlyNewFields | ratification boundary |
| claimBoundary | scaffold provenance only |

## Required First Reads

1. `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`
2. `AGENTS.md`
3. `docs/reviews/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_COMPLETION_2026-07-11.md`
4. `docs/reference/system_chain/CVF_DOCTRINE_TO_CONTRACT_ROUTE_MAP.md`
5. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`
6. `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md`

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
is not used as corpus authority. MSEA-R98 consumes only the already accepted
MSEA-R96 L2 candidate decision and current governed sources; it performs no
legacy corpus scan or absorption.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md`; `AGENTS.md` |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external input is ingested, adapted, or promoted |
| Claim boundary | MSEA-R98 decides only the bounded current L2 owner mapping |

## Pre-Flight Checks

- Confirm clean worktree and current HEAD.
- Run pre-implementation from dispatch session commit.
- Compare all three L2 responsibilities and explicit exclusions.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| doctrine L2 contract | VALUE_SET | canonical contract: `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | L2 responsibilities | L2 - Build Protocol | frozen doctrine | ACCEPT |
| active operational rules | EXISTS | `AGENTS.md` | mandatory rule sections | AGENTS.md | root instruction owner | ACCEPT |
| R96 calibrated candidate | VALUE_SET | `docs/reviews/CVF_MSEA_R96_DOCTRINE_ROUTE_GAP_RECONCILIATION_COMPLETION_2026-07-11.md` | L2 finding | ADAPTATION_CANDIDATE | R96 review | ACCEPT |

## Current Runtime Freshness Verification

N/A with reason: authority/read-model decision only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | none |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | source table; route token; self-review boundary; CURRENT freshness; closure fields |
| gateRunPurpose | confirmation after source reads |
| claimBoundary | decision and route mapping only |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Ratify or reject the L2 active owner mapping. |
| scopeClassification | DOCUMENTATION_AND_EVIDENCE_ONLY |
| riskSensitivity | R1 |
| selectedRouteMode | SINGLE_AGENT_MULTI_ROLE |
| roleSeparationBasis | sequential implementation, adversarial self-review and closure |
| escalationCondition | any doctrine/AGENTS mutation or runtime/public/provider expansion |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> implementer -> self-reviewer/closer -> session-sync steward |
| phase | DISPATCH, IMPLEMENTATION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=138762889; executionBaseHead=dispatch session commit; closureBaseHead=dispatch session commit |
| changedSetScope(phase) | two packet paths; four material paths; seven session paths |
| traceScope(phase, actor) | source comparison, diff, fingerprint and gates |
| commitOwner(phase) | same agent through commit steward; material/session split |
| crossBatchIsolation | Before status evidence: clean worktree at `138762889`; unrelated changes prohibited |
| nextMoveSurfaces | only after material commit evidence |

## Single-Agent Multi-Role Control Block

| Field | Value |
|---|---|
| role separation ledger | packet -> decision edit -> adversarial self-review -> gates -> material commit -> session sync |
| evidence basis | frozen responsibilities, current AGENTS sections, R96 calibration, diff and freshness |
| self-review boundary | independent review is not claimed; bounded R1 documentation decision |
| escalation conditions | stop for doctrine/AGENTS mutation, secrets, destructive action, public/provider/runtime or claim expansion |
| gate sequence | pre-dispatch; pre-implementation; reviewer-fast; commit steward; real-range pre-closure; session sync |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | sequential roles | local governed docs | bounded authority mapping | citations, diff, gates | ALLOWED_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | N/A with reason | no external authority | N/A with reason | DEFERRED |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R98_L2_BUILD_PROTOCOL_OWNER_RATIFICATION_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: four material paths; separate session paths.

closureOwner: same agent under explicit self-review boundary.

workerCommitPermission: ALLOWED_THROUGH_COMMIT_STEWARD

## Roadmap-to-Work-Order Trace Matrix

| R96 state | R98 decision | Evidence |
|---|---|---|
| ADAPTATION_CANDIDATE | ratify bounded active owner or retain candidate | responsibility/exclusion comparison |

## Work-Order Fulfillment Manifest

| Artifact | Required action |
|---|---|
| route map | record final L2 disposition and boundary |
| system-chain JSON/README | reconcile lane wording and fingerprint |
| completion review | document decision and self-review boundary |

## Execution Plan

1. Commit/sync dispatch and run pre-implementation.
2. Compare L2 responsibilities to current `AGENTS.md` controls.
3. Record ratification only if all responsibilities have active coverage.
4. State exclusions: broader AGENTS scope, no doctrine restatement, no frozen status transfer.
5. Refresh R91 fingerprint/human map.
6. Self-review, commit material, real-range pre-closure, session sync.

## Verification Commands

```powershell
python governance/compat/check_system_chain_map_freshness.py --enforce
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <dispatchSessionCommit> --head HEAD
git diff --check
```

## Acceptance Criteria

- Final L2 disposition is source-backed and not inferred from filename.
- `AGENTS.md` and frozen doctrine remain unchanged.
- Boundary rejects transfer of frozen status or one-to-one textual equivalence.
- R91 freshness CURRENT.
- Four material paths only; session commit separate.

## Evidence Requirements

Map each doctrine responsibility to current controls; record unmatched items,
exclusions, exact diff, fingerprint, gates and review-boundary statement.

## Worker Autonomy / No-Question Rule

Repair allowed-scope gate failures. Stop for any required doctrine/AGENTS edit
or inability to state a truthful bounded mapping.

## Negative And Fail-Condition Scan

Fail for doctrine edit, AGENTS edit, frozen-status transfer, false equivalence,
runtime/public/provider expansion, or independent-review claim.

## Review Gate

Adversarial self-review must attempt to reject the mapping and record why the
bounded mapping remains valid. Independent review is not claimed.

## Closure Checklist

- [ ] Three L2 responsibilities mapped.
- [ ] Exclusions explicit.
- [ ] No doctrine/AGENTS edit.
- [ ] Freshness CURRENT.
- [ ] Independent review not claimed.

## Return-To-Orchestrator Conditions

Stop for source contradiction, unmatched core responsibility, or scope growth.

## Operator Checkpoint

No checkpoint is pending for the route decision. Any future doctrine wording
change remains separately authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex sequential multi-role agent |
| Provider or surface | local private provenance repository |
| Session or invocation | MSEA-R98 dispatch, 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | reads, rg, apply_patch, gates, git |
| Target paths | paired packet paths |
| Allowed scope source | user instruction to continue after R97 |
| Before status evidence | clean worktree at `138762889`; packet paths absent |
| After status evidence | two packet paths pending |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only |
| Claim boundary | L2 route decision; no doctrine/AGENTS mutation |
| Agent type | dispatcher |
| Invocation ID | msea-r98-dispatch-2026-07-11 |
| Expected manifest | paired GC-018 and work order |
| Actual changed set | paired GC-018 and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | L2 active-owner ratification decision |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt applies |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source comparison, diff and gates |
| invocationBoundary | documentation/read-model only |
| interceptionBoundary | no provider, MCP, Web, proxy, or runtime interception |
| claimLanguage | bounded owner mapping, not doctrine rewrite |
| forbiddenExpansion | no doctrine, AGENTS, runtime, public, provider or MAO mutation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private doctrine-route decision.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| active owner | existing root `AGENTS.md` |
| route record | existing system-chain reference surfaces |
| new protocol file/folder | none |
| storage decision | no duplicate protocol owner |
| generated aggregate impact | none |

## Claim Boundary

R98 decides and records the L2 mapping only. It does not edit doctrine or
`AGENTS.md`, copy historical protocol text, or authorize runtime/public work.
