# CVF Agent Work Order - Active Session State Bootstrap Read Model And Aggregate Size Refactor

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-25

docType: work_order

Batch ID: STATE-BR-T1

dispatchBaseHead: 5e7d100d

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_FOR_CLAUDE_2026-06-25.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: ASSF-PIC-T0 is closed bounded at material commit
`24b49017`; session-sync HEAD before dispatch authoring is `5e7d100d`. The
selected pilot candidate is `cvf-dispatch-quality-reviewer`, but ASSF-PIC-T1 is
held until this active-session bootstrap refactor closes.

Do-not-misread notes: this is not ASSF-PIC-T1 package-instance work. Do not
create package instances, change certification state, edit ASSF generated index
or resolver behavior, change Web runtime, implement CLI/MCP adapter behavior,
run provider/live proof, public-sync, push, activate a package, or execute skill
instructions.

Required first actions: read this work order, read the paired GC-018 baseline,
read `CVF_SESSION_MEMORY.md`, read `CVF_SESSION/ACTIVE_SESSION_STATE.json`, read
`AGENT_HANDOFF_V22_2026-06-22.md`, read
`docs/reference/guard_orientation/README.md`, read
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
then record actual `executionBaseHead` and `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with uncommitted artifacts
only, actual `executionBaseHead`, actual `git status --short`, changed paths,
source inventory, focused tests, gate evidence, size evidence, and no commit.
If blocked, return `BLOCKED_WITH_REASON` and name the exact source, scope, or
gate that blocks completion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator instruction to handle Active Session State Bootstrap Read Model And Aggregate Size Refactor before T1 continues |
| Scope classification | bounded protected-path session-state generator/checker/front-door refactor; allowed changed paths are listed in Write Ownership |
| Intake role | worker implements compact active-session bootstrap read model and evidence |
| Reviewer role | Codex reviewer/closer validates implementation, tests, boundaries, and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker returns uncommitted artifacts |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require ASSF package instance, certification, generated-index mutation, resolver mutation, Web runtime, CLI/MCP adapter, provider/live proof, public-sync, push, package activation, destructive action, or a broader session-state redesign |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher creates packet; worker implements STATE-BR-T1 and returns no-commit evidence; reviewer/closer reviews, commits accepted material, and session-syncs if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=5e7d100d`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | execution changes only Write Ownership paths; closer owns status conversion, reviewer artifact, accepted material commit, and later session-sync |
| traceScope(phase, actor) | worker-return trace covers pending STATE-BR-T1 artifacts only; reviewer trace covers review/closure; session-sync trace covers continuity only |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material, closure, or session-sync commit |
| crossBatchIsolation | do not mix this refactor with ASSF-PIC-T1 package-instance work, certification, generated-index/resolver/Web/runtime/adapter/provider/public-sync work, or another dispatch batch |
| Before status evidence | dispatchBaseHead `5e7d100d`; clean worktree verified before dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after accepted material review if mode or next allowed move changes |
| Closer designation | Codex reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_COMPLETION_2026-06-25.md` |
| reviewerOwnedClosurePaths | this work order; paired GC-018 baseline; accepted generator/checker/test/front-door changes; worker-return artifact; reviewer completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | Codex reviewer/closer role |

## Purpose

Implement a compact active-session bootstrap read model so agents can obtain
current mode, active handoff, next allowed move, and the full aggregate pointer
without reading the entire `CVF_SESSION/ACTIVE_SESSION_STATE.json` file first.
The full aggregate remains the canonical generated registry.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-25 request to create the T1 work order after active-session aggregate size blocker | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_2026-06-25.md` | ACCEPT |
| ASSF-PIC-T0 completion | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` | ACCEPT |
| JSON generated aggregate discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | ACCEPT |
| Guard orientation index | `docs/reference/guard_orientation/README.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | Codex dispatch author role |
| Worker | Claude implementation and no-commit return role |
| Reviewer | Codex reviewer role after worker return |
| Closer | Codex closer role after acceptance |
| Session-sync steward | Codex session-sync role after material commit if next move changes |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/baselines/CVF_GC018_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_2026-06-25.md` | authorization, scope, protected paths, and claim boundary |
| `CVF_SESSION_MEMORY.md` | active front door and current next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated aggregate and active handoff pointer |
| `AGENT_HANDOFF_V22_2026-06-22.md` | active handoff and held ASSF-PIC-T1 checkpoint |
| `docs/reference/guard_orientation/README.md` | task-first guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | pre-write checklist for gate-parsed artifacts |
| `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated aggregate discipline |
| `governance/compat/generate_active_session_state.py` | active-session generator source |
| `governance/compat/check_active_session_state.py` | active-session compatibility gate |
| `governance/compat/test_generate_active_session_state.py` | focused test module |

## Pre-Flight Checks

The worker must run or record these checks before editing. For commands that
use `<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
(Get-Content CVF_SESSION/ACTIVE_SESSION_STATE.json).Count
(Get-Item CVF_SESSION/ACTIVE_SESSION_STATE.json).Length
python governance/compat/generate_active_session_state.py --check
python governance/compat/check_active_session_state.py --enforce
python -m unittest governance.compat.test_generate_active_session_state
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-test, size-check, and generated-state drift failures and
rerun the required checks without asking the operator. Ask the operator only if
remediation would exceed Allowed scope, change the claim boundary, release
ASSF-PIC-T1, require live/provider proof, require public-sync, require push,
touch forbidden paths, consume secrets/quota, require a destructive action, or
contradict this work order.

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections so reviewer-fast can
diagnose issues before closure:

- `Status`
- `Purpose`
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
- full aggregate and bootstrap read-model size evidence
- focused test and gate evidence
- `WORKER_EXPERIENCE_RETRO` block or
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`

If any listed section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active-session aggregate path is `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `governance/compat/generate_active_session_state.py` | line 15 | `STATE_PATH` | active-session generator | EXISTS | ACCEPT |
| Active-session source layout uses `CVF_SESSION/state/` | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | line 60 | `CVF_SESSION/state/` | JSON generated aggregate discipline | LITERAL_INVARIANT | ACCEPT |
| Active-session generator has bootstrap-from-current function | `governance/compat/generate_active_session_state.py` | line 91 | `bootstrap_from_current` | active-session generator | EXISTS | ACCEPT |
| Active-session generator has aggregate generation function | `governance/compat/generate_active_session_state.py` | line 126 | `generate_aggregate` | active-session generator | EXISTS | ACCEPT |
| Active-session generator has source drift validator | `governance/compat/generate_active_session_state.py` | line 135 | `validate_aggregate_matches_sources` | active-session generator | EXISTS | ACCEPT |
| Active-session checker invokes source drift validation | `governance/compat/check_active_session_state.py` | line 348 | `validate_aggregate_matches_sources` | active-session checker | RUNTIME_BEHAVIOR | ACCEPT |
| Active-session checker expects active registry pointer to full aggregate path | `governance/compat/check_active_session_state.py` | line 352 | `activeStateRegistry` | active-session checker | LITERAL_INVARIANT | ACCEPT |
| ASSF-PIC roadmap holds PIC-T1 for this refactor | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | lines 166-167 | `ASSF-PIC-T1` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |

## New Doc-Only And Source Terms

| Proposed term | Owner in STATE-BR-T1 | Status | Reason |
|---|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | active-session bootstrap refactor | NEW_GENERATED_READ_MODEL_PATH | compact startup read model |
| `activeStateBootstrapReadModel` | active-session state core or aggregate field, if implemented | NEW_POINTER_FIELD | optional pointer from full registry to compact read model |
| `generate_bootstrap_read_model` | active-session generator helper, if implemented | NEW_HELPER_SYMBOL | deterministic read-model generation from existing state sources |
| `validate_bootstrap_read_model_matches_sources` | active-session generator/checker helper, if implemented | NEW_HELPER_SYMBOL | drift validation for compact read model |
| `CVF_ACTIVE_SESSION_BOOTSTRAP_READ_MODEL_MAX_BYTES` | test/checker constant, if implemented | NEW_SIZE_CEILING_SYMBOL | machine-readable size ceiling for bootstrap surface |

## Current Runtime Freshness Verification

| Runtime or source claim | Verification command or source | Dispatch result | Worker requirement |
|---|---|---|---|
| Full active-session aggregate is large at dispatch | `(Get-Content CVF_SESSION/ACTIVE_SESSION_STATE.json).Count`; `(Get-Item CVF_SESSION/ACTIVE_SESSION_STATE.json).Length` | 2773 lines; 631698 bytes | record before/after size evidence |
| Existing state source entry count is large | `(Get-ChildItem CVF_SESSION/state/entries/*.json | Measure-Object).Count` | 533 entries | preserve generated source layout |
| Bootstrap read model path is absent before dispatch | `Test-Path CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `False` | create through generator or documented deterministic source path |
| Worker return path is absent before dispatch | `Test-Path docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_WORKER_RETURN_2026-06-25.md` | `False` | create |
| Completion review path is absent before dispatch | `Test-Path docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_COMPLETION_2026-06-25.md` | `False` | do not create; reviewer-owned |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This work order cites bounded files and source rows only; the
  worker must record exact changed paths and command outputs.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Exclusions are recorded as scope boundaries, not proof of runtime
  behavior.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator report that Claude bootstrap failed on active-session aggregate size, routed to local session-state refactor |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this STATE-BR-T1 work order and paired GC-018 baseline |
| Disposition | local active-session bootstrap refactor dispatch only; no external material is absorbed as source authority |
| Claim boundary | operator/Claude report motivates the refactor; implementation facts must still be source-verified against governed repository files |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or checkpoint requirement | Work-order coverage | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| ASSF-PIC-T0 selected one pilot candidate and held PIC-T1 | Scope and forbidden actions | no package instance or certification files | reviewer diff and worker return | PASS |
| Active session requires bootstrap read-model refactor before PIC-T1 release | Mission and Execution Plan | compact read model, generator/checker/tests | active-session check and focused tests | PASS |
| Full aggregate remains canonical generated registry | Source Verification and JSON discipline | `activeStateRegistry`; generator/checker behavior | `generate_active_session_state.py --check`; `check_active_session_state.py --enforce` | PASS |
| Later ASSF-PIC-T1 remains dependency-held | Claim Boundary and Fail Conditions | no ASSF package-instance output | git diff and reviewer closure | PASS |

## Execution Plan

1. Read all required sources, record `executionBaseHead`, and record the current
   full aggregate line and byte size.
2. Design the compact bootstrap read model so it includes at minimum:
   `currentMode`, `activeHandoff`, `nextAllowedMove`, `activeStateRegistry`,
   `activeSessionFrontDoor`, `lastUpdated`, and a claim boundary that points to
   the full aggregate for complete state.
3. Update `governance/compat/generate_active_session_state.py` so generation
   and check mode keep the full aggregate and compact bootstrap read model in
   sync.
4. Update `governance/compat/check_active_session_state.py` so enforce mode
   fails if the compact read model drifts, is missing, or exceeds the worker's
   documented size ceiling.
5. Update focused tests in
   `governance/compat/test_generate_active_session_state.py` for read-model
   generation, drift detection, and size-bound behavior.
6. Update startup/front-door text in `AGENTS.md`, `CVF_SESSION_MEMORY.md`, and
   `AGENT_HANDOFF_V22_2026-06-22.md` so future agents read the compact bootstrap
   model first, then use the full aggregate as canonical registry when needed.
7. Run required checks and create the worker-return artifact without staging,
   committing, pushing, or changing ASSF package surfaces.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | worker | create compact generated bootstrap read model |
| `CVF_SESSION/state/**` | worker | update only if needed to add a pointer or source-backed bootstrap metadata |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | worker | regenerate only through `governance/compat/generate_active_session_state.py` |
| `governance/compat/generate_active_session_state.py` | worker | add read-model generation and check support |
| `governance/compat/check_active_session_state.py` | worker | add read-model drift and size validation |
| `governance/compat/test_generate_active_session_state.py` | worker | add focused tests |
| `AGENTS.md` | worker | update bootstrap read order only |
| `CVF_SESSION_MEMORY.md` | worker | update bootstrap read order only; do not add long history |
| `AGENT_HANDOFF_V22_2026-06-22.md` | worker | update bootstrap read order only; do not add unrelated chronology |
| `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_WORKER_RETURN_2026-06-25.md` | worker | create |
| `docs/reference/agent_system_skills/**` | out of worker scope | forbidden |
| `EXTENSIONS/**`, Web runtime, CLI/MCP adapter source, public-sync clone, provider/live proof files | out of worker scope | forbidden |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: the worker may update active-session
generator/checker/test files and protected startup/session files only to add and
enforce a compact active-session bootstrap read model while preserving the full
generated aggregate as canonical registry.

Protected paths:

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/**`
- `governance/compat/generate_active_session_state.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_generate_active_session_state.py`

Operator authorization: the operator identified the active-session aggregate
size as technical debt and directed this refactor before T1 continues.

Rollback boundary: revert only STATE-BR-T1 material changes if rejected. Do not
revert ASSF-PIC-T0 closure, selected candidate evidence, or prior active-session
generated-source layout.

## JSON Generated Aggregate Discipline Control

| Field | Disposition |
|---|---|
| Existing aggregate | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Existing source layout | `CVF_SESSION/state/` |
| Existing generator | `governance/compat/generate_active_session_state.py` |
| Existing drift checker | `governance/compat/check_active_session_state.py` |
| Required discipline | edit source fragments and generator/checker; do not hand-edit aggregate-only state |
| Closure disposition required | `EXISTING_GENERATED_SOURCE_LAYOUT_REUSED` plus command-backed drift checks |

## Planned Worker Fulfillment Manifest

| Path | Required at worker return | Purpose |
|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Yes | compact generated bootstrap read model |
| `governance/compat/generate_active_session_state.py` | Yes | read-model generation/check support |
| `governance/compat/check_active_session_state.py` | Yes | read-model drift and size enforcement |
| `governance/compat/test_generate_active_session_state.py` | Yes | focused tests |
| `AGENTS.md` | Yes | startup read-order update |
| `CVF_SESSION_MEMORY.md` | Yes | front-door read-order update |
| `AGENT_HANDOFF_V22_2026-06-22.md` | Yes | handoff read-order update |
| `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_WORKER_RETURN_2026-06-25.md` | Yes | worker return evidence |

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- changed-path list;
- current and final byte size of full aggregate and compact bootstrap read
  model;
- source inventory for generator/checker/front-door paths;
- `python governance/compat/generate_active_session_state.py --check`;
- `python governance/compat/check_active_session_state.py --enforce`;
- `python -m unittest governance.compat.test_generate_active_session_state`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`;
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_generate_active_session_state.py`;
- explicit statement that no ASSF package instance, certification, generated
  index, resolver, Web runtime, CLI/MCP adapter, provider/live proof,
  public-sync, push, activation, or package instruction execution occurred.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
ASSF package-instance release, certification, generated-index mutation,
resolver mutation, Web runtime, CLI/MCP adapter behavior, provider/live proof,
public-sync, push, package activation, secrets/quota, destructive action, or a
change to the claim boundary.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Write
Ownership, run reviewer-fast or committed-range gates as appropriate, verify
the compact read model is source-backed and size-bounded, verify startup text
does not demote the full aggregate, and only then convert accepted material into
a completion review.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Compact bootstrap read model exists and is deterministic from governed state sources or the generated aggregate | generator/checker diff and focused tests |
| AC2 | Full aggregate remains canonical and generated from `CVF_SESSION/state/` | generator check and active-session check |
| AC3 | Active-session checker detects missing, drifted, or oversized bootstrap read model | source diff and focused tests |
| AC4 | Startup/front-door docs tell agents to read compact bootstrap model first while keeping full aggregate canonical | diff review |
| AC5 | No ASSF package, generated-index, resolver, Web runtime, adapter, live, public-sync, push, or activation scope changed | git status and diff |
| AC6 | Worker returns no-commit evidence in required packet shape | worker-return artifact and gate evidence |

## Closure Checklist

- [ ] Worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Changed paths stay inside Write Ownership.
- [ ] Compact bootstrap read model is generated or checked from governed state sources.
- [ ] Full aggregate remains canonical and validates against sources.
- [ ] Focused tests and active-session checks pass or block with reason.
- [ ] Startup/front-door text updates are bounded to read order and do not add long history.
- [ ] ASSF-PIC-T1 remains held until reviewer closure.
- [ ] Worker did not commit, push, public-sync, run provider/live proof, or change ASSF package surfaces.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Write Ownership.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, the compact read model cannot be made
deterministic, or the repair would require forbidden ASSF/runtime/provider/
public scope.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | STATE-BR-T1 active-session bootstrap read model and aggregate size refactor work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch work order only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned manifest |
| invocationBoundary | governed local documentation and generator/checker work only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes a bounded no-commit bootstrap read-model refactor for Claude worker execution |
| forbiddenExpansion | no ASSF package instance, certification decision, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, or package instruction execution |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: STATE-BR-T1 is private provenance session-continuity and governance
helper work. No public-sync repository work or public catalog claim is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | STATE-BR-T1 dispatch authoring, 2026-06-25 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, rg, Test-Path, apply_patch |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator instruction to create T1 work order after active-session aggregate size blocker |
| Before status evidence | dispatchBaseHead `5e7d100d`; clean worktree verified before dispatch authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker implementation follows after material dispatch and session-sync |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `state-br-t1-active-session-bootstrap-read-model-dispatch-2026-06-25` |
| Expected manifest | `docs/baselines/CVF_GC018_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_2026-06-25.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_FOR_CLAUDE_2026-06-25.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_2026-06-25.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_FOR_CLAUDE_2026-06-25.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes only STATE-BR-T1 active-session bootstrap read-model
and aggregate-size refactor work. It does not authorize ASSF-PIC-T1 package
instance evidence or skeleton hardening, package certification, UAT advancement,
ASSF generated-index mutation, ASSF resolver mutation, Web runtime source,
CLI/MCP adapter behavior, provider/live proof, public-sync, push, package
activation, or package instruction execution.
