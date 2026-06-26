# CVF Agent Work Order: ASSF Package Certification Decision T0-T3

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-CERT-DECISION

dispatchBaseHead: aad3b819

executionBaseHead: aad3b819

closureBaseHead: aad3b819

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. This packet authorizes a bounded
certification evidence decision for `cvf-dispatch-quality-reviewer`.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_2026-06-26.md`

Do-not-misread notes: this work order does not authorize lifecycle source
mutation, package registry mutation, generated-index mutation, resolver source
mutation, package instance creation, Web runtime change, CLI/MCP adapter
behavior, provider/live proof, public-sync, push, activation, readiness claim,
package instruction execution, package integration, or session-sync in the
material commit.

## Purpose

Execute T0-T3 certification-decision review for
`cvf-dispatch-quality-reviewer`.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | agree to next roadmap and process T0-T3 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Real UAT evidence | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md` | ACCEPT |
| Paired baseline | `docs/baselines/CVF_GC018_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | scope authorization |
| Dispatcher | Codex |
| Worker | Codex single-agent multi-role |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex in a separate commit after material closure |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | SOURCE_VERIFIED | package source |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | SOURCE_VERIFIED | lifecycle decision rules |
| `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md` | SOURCE_VERIFIED | real UAT evidence |
| `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_COMPLETION_2026-06-26.md` | SOURCE_VERIFIED | UAT evidence closure |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0
```

## Scope / Methodology

Codex reviews the package source, lifecycle guard, real UAT evidence, drift
check, and resolver readout. T2 records whether certification evidence is
approved, held, or rejected. T3 records the next-control lane.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | T0 protocol | certification decision protocol review |
| 2 | T1 evidence review | source and command evidence comparison |
| 3 | T2 decision | certification evidence disposition |
| 4 | T3 next-control | lifecycle source-state update lane decision |
| 5 | Closure | completion review and material gates |

## Findings / Position

The package has sufficient evidence to approve certification evidence for a
future source-state update. The package is not source-certified until a later
lane mutates registry source and generated index under explicit authority.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/roadmaps/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP_2026-06-26.md` | Codex | create and close roadmap |
| `docs/baselines/CVF_GC018_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_2026-06-26.md` | Codex | create and close baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_FOR_CODEX_2026-06-26.md` | Codex | create and close work order |
| `docs/reviews/CVF_ASSF_CERT_T0_CERTIFICATION_DECISION_PROTOCOL_2026-06-26.md` | Codex | create T0 review |
| `docs/reviews/CVF_ASSF_CERT_T1_EVIDENCE_REVIEW_2026-06-26.md` | Codex | create T1 review |
| `docs/reviews/CVF_ASSF_CERT_T2_CERTIFICATION_DECISION_2026-06-26.md` | Codex | create T2 review |
| `docs/reviews/CVF_ASSF_CERT_T3_POST_DECISION_NEXT_CONTROL_2026-06-26.md` | Codex | create T3 review |
| `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | Codex | create completion review |

## Forbidden Changed Paths And Actions

No package registry source, generated index, resolver source, Web runtime,
adapter source, provider/live proof, public-sync, push, package activation,
package instance, lifecycle source mutation, or session-sync path is inside
this material work order.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| package acceptance evidence requires dispatch-quality PASS and fast gate 5/5 PASS | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `acceptanceEvidence` | ASSF registry entry | VALUE_SET | ACCEPT |
| package UAT state is source-visible | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| package certification state is source-visible | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| lifecycle guard requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState` | ASSF lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| real UAT evidence records dispatch-quality PASS | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_2026-06-26.md` | UAT Execution Evidence | `UAT-02` | ASSF real UAT evidence review | LITERAL_INVARIANT | ACCEPT |
| real UAT completion recommends certification-decision roadmap | `docs/reviews/CVF_ASSF_REAL_MANUAL_UAT_EXECUTION_EVIDENCE_COMPLETION_2026-06-26.md` | Next roadmap recommendation | `OPEN_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP` | ASSF real UAT completion review | VALUE_SET | ACCEPT |
| generated index drift checker exists | `governance/compat/check_assf_skill_index_drift.py` | module | `main` | ASSF drift checker | EXISTS | ACCEPT |
| ASSF resolver exists | `governance/compat/run_assf_skill_resolver.py` | module | `resolve_skill_packet` | ASSF resolver | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| ASSF generated index drift | ran current drift check before authoring | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| ASSF resolver readout | ran current resolver query before authoring | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | PASS |

## Worker Return Packet Shape Contract

This single-agent multi-role work order does not require a separate worker
return artifact, but because the commit mode is `WORKER_MUST_NOT_COMMIT`, the
packet shape contract is recorded for gate compatibility and future external
worker reuse.

Required worker-return sections if delegated later:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- command evidence
- no commit statement

If any section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes, reviews, and closes this certification-decision tranche |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=aad3b819`; `executionBaseHead=aad3b819`; `closureBaseHead=aad3b819` |
| changedSetScope(phase) | material closure paths only; session-sync follows separately |
| traceScope(phase, actor) | Codex trace covers material artifacts only |
| commitOwner(phase) | Codex owns material commit and later session-sync commit |
| crossBatchIsolation | material closure is separate from session-sync |
| nextMoveSurfaces | updated only after material commit succeeds |
| Closer designation | Codex is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | roadmap, baseline, this work order, T0-T3 reviews, completion review |
| workerReturnStatus | N/A with reason: Codex is executing single-agent multi-role closure |
| closer | Codex |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | authorized certification-decision roadmap |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Evidence Requirements

| Evidence | Required disposition |
|---|---|
| Package source entry | read and cited |
| Real UAT evidence | PASS |
| ASSF generated index drift | PASS |
| Resolver readout | one metadata-only candidate |
| Certification decision | evidence approved, source-state update deferred |
| Forbidden actions | no runtime/source/session mutation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-CERT-DECISION work order and reviews | internal agents may use this decision to prepare a future lifecycle-state update work order only | T0-T3 reviews and completion review | no checker, loader, runtime, or generated-index mutation implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents cannot consume, certify, activate, mutate, or execute packages through this work order | package external disposition remains deferred | adapter remains deferred | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | T0 protocol review exists | PASS |
| AC2 | T1 evidence review exists | PASS |
| AC3 | T2 certification evidence decision exists | PASS |
| AC4 | T3 next-control review exists | PASS |
| AC5 | No forbidden mutation occurs | PASS |

## Review Gate

Codex reviewer/closer must verify command outputs, exact changed paths, and gate
evidence before material commit.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex single-agent multi-role |
| Agent type | dispatcher/worker/reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | ASSF package certification decision work order, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, ASSF drift check, ASSF resolver, apply_patch, governance gates, git |
| Target paths | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Allowed scope source | active session next allowed move plus user approval to process T0-T3 |
| Before status evidence | baseHead `aad3b819`; worktree clean before authoring |
| After status evidence | material artifacts pending commit |
| Diff evidence | `git diff --name-status`; `git diff --check`; autorun gates |
| Approval boundary | certification evidence decision only |
| Claim boundary | no lifecycle source mutation, generated-index mutation, resolver mutation, runtime, provider/live, public-sync, package activation, package instance, or adapter behavior |
| Invocation ID | `assf-package-certification-decision-work-order-2026-06-26` |
| Expected manifest | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Actual changed set | roadmap, baseline, work order, T0 review, T1 review, T2 review, T3 review, completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

| Check | Required resolution |
|---|---|
| T0 protocol review exists | PASS |
| T1 evidence review exists | PASS |
| T2 decision review exists | PASS |
| T3 next-control review exists | PASS |
| Forbidden mutation absent | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if T0-T3 reviews, completion review, and gates
pass. Return `BLOCKED_WITH_REASON` if source evidence or command evidence cannot
be established inside scope.

## Operator Checkpoint

| Boundary | Disposition |
|---|---|
| Current certification evidence decision | no additional human checkpoint required |
| Lifecycle source mutation | fresh governed authorization required |
| Runtime, adapter, provider/live, public-sync, push, or scope expansion | fresh governed authorization required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance certification-decision evidence; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF package certification-decision work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- certification evidence decision only |
| receiptEvidence | CVF_RECEIPT_PRESENT - UAT evidence PASS, drift PASS, resolver PASS |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- T0-T3 reviews and completion review |
| invocationBoundary | governed local documentation and read-only command evidence |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, package instruction execution, package instance, lifecycle source mutation, or generated-index mutation |
| claimLanguage | approves certification evidence and defers source-state update |
| forbiddenExpansion | no package instance creation, lifecycle source mutation, registry-source mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, readiness claim, package instruction execution, package integration, worker commit, or session-sync in material commit |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ARAM-01 | UAT evidence review | dispatch-quality violations | 0 | 0 | PASS |
| ARAM-02 | UAT evidence review | fast gate checks passed | 5/5 | 5/5 | PASS |
| ARAM-03 | drift command output | ASSF generated index drift | PASS | PASS | PASS |
| ARAM-04 | resolver output | totalCandidates | 1 | 1 | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_T0_T3_COMPLETION_2026-06-26.md` | final disposition and gate evidence | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_CERTIFICATION_DECISION_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized in this work order | no corpus registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized in this work order | no corpus registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this work order and completion review | no runtime loop or provider call | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded | N/A with reason |

## Claim Boundary

This work order closes certification evidence decision recording only. It does
not mutate lifecycle source state or certify the registry entry itself.
