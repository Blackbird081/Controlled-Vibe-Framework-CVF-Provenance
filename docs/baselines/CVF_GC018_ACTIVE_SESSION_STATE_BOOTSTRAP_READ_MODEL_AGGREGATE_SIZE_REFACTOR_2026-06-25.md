# CVF GC-018 Baseline: Active Session State Bootstrap Read Model And Aggregate Size Refactor

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: baseline

Batch ID: STATE-BR-T1

dispatchBaseHead: 5e7d100d

## Proposed Tranche

Tranche: STATE-BR-T1

Baseline decision: authorize a bounded active-session bootstrap refactor so
new and resumed agents can read a compact machine-readable startup view before
opening the full active-session aggregate. The full aggregate remains the
canonical generated state registry; this tranche adds a compact read model and
drift/size checks that keep it aligned.

This tranche is a prerequisite blocker for ASSF-PIC-T1. It does not release
ASSF-PIC-T1 package-instance evidence or skeleton hardening.

Verdicts:

- Dispatcher verdict: DISPATCH_APPROVED
- Worker verdict: COMPLETE_PENDING_REVIEW_ACCEPTED
- Reviewer verdict: CLOSED_PASS_BOUNDED

## Purpose

Claude reported that `CVF_SESSION/ACTIVE_SESSION_STATE.json` is too large for
practical bootstrap reading. The current file is generated and remains valid,
but at dispatch it is 2773 lines and 631698 bytes. This baseline authorizes a
small generated bootstrap read model that carries the startup facts agents need
first, while preserving the generated aggregate discipline for the full
registry.

Success means a worker returns source/test/doc changes that:

- add a compact generated bootstrap read model for startup facts;
- validate the read model against existing active-session sources or the
  generated aggregate;
- enforce a size ceiling for the bootstrap read model;
- update startup front doors to use the compact read model first without
  demoting the full aggregate as canonical registry;
- keep ASSF-PIC-T1 held until this refactor is reviewed and closed.

## Evidence / Verification

Dispatch evidence is limited to active session next-move authority, ASSF-PIC-T0
hold evidence, active-session generated aggregate source verification, ADIF
disclosure, protected-path authorization, and planned worker artifact paths.
Worker-created read model, source changes, tests, worker return, and reviewer
completion do not exist at dispatch time and must not be claimed as complete
until worker return and reviewer closure provide command-backed evidence.

## Scope / Applies To

Applies to:

- active-session generated state source layout;
- active-session aggregate generator and checker;
- focused tests for generator/checker behavior;
- startup/front-door text needed to route future agents through the compact
  bootstrap read model;
- worker return and reviewer completion for this refactor.

Does not apply to:

- ASSF package instance creation;
- ASSF certification or UAT decision;
- ASSF generated-index mutation;
- ASSF resolver mutation;
- CVF Web runtime mutation;
- CLI/MCP adapter implementation;
- provider call, live proof, public-sync, push, package activation, or package
  instruction execution.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| Current session next move authorizes this refactor | SATISFIED | `CVF_SESSION_MEMORY.md` lines 76-78; `AGENT_HANDOFF_V22_2026-06-22.md` lines 396-398 |
| ASSF-PIC-T0 closure selected one candidate and held PIC-T1 | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_COMPLETION_2026-06-25.md` lines 50-51, 120-121 |
| ASSF-PIC roadmap keeps PIC-T1 held until this refactor | SATISFIED | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` lines 166-167, 317-318 |
| Active-session aggregate already uses generated source layout | SATISFIED | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` line 60 |
| Current dispatch worktree isolation | SATISFIED | `git status --short` returned no paths before authoring |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | compact active-session bootstrap read model plus full aggregate pointer | internal agents may read compact startup facts first, then open the full aggregate only when needed; no package lifecycle, resolver, Web, adapter, commit, activation, or certification authority is granted | this baseline, work order, active-session generator/checker, active front-door docs | no internal loader, package resolver, Web bridge, or package root is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external startup/readout surface | external agents receive no adapter or MCP behavior through this tranche | no external adapter source is in scope | adapter implementation is deferred to a separate source-verified work order | `DEFERRED_WITH_REASON` |

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
| Governed artifact literal-format gotchas checklist exists | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Purpose | `CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | governed artifact checklist | EXISTS | ACCEPT |

## New Doc-Only And Source Terms

| Proposed term | Owner in STATE-BR-T1 | Status | Reason |
|---|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | active-session bootstrap refactor | NEW_GENERATED_READ_MODEL_PATH | compact startup read model to avoid opening the full aggregate first |
| `activeStateBootstrapReadModel` | active-session state core or aggregate field, if implemented | NEW_POINTER_FIELD | optional pointer from canonical registry to compact read model |
| `generate_bootstrap_read_model` | active-session generator helper, if implemented | NEW_HELPER_SYMBOL | deterministic read-model generation from existing state sources |
| `validate_bootstrap_read_model_matches_sources` | active-session generator/checker helper, if implemented | NEW_HELPER_SYMBOL | drift validation for compact read model |
| `CVF_ACTIVE_SESSION_BOOTSTRAP_READ_MODEL_MAX_BYTES` | test/checker constant, if implemented | NEW_SIZE_CEILING_SYMBOL | machine-readable size ceiling for bootstrap surface |

## Current Runtime Freshness Verification

| Runtime or source claim | Verification command or source | Dispatch result | Worker requirement |
|---|---|---|---|
| Full active-session aggregate is large at dispatch | `(Get-Content CVF_SESSION/ACTIVE_SESSION_STATE.json).Count`; `(Get-Item CVF_SESSION/ACTIVE_SESSION_STATE.json).Length` | 2773 lines; 631698 bytes | record before/after size evidence |
| Existing state source entry count is large | `(Get-ChildItem CVF_SESSION/state/entries/*.json | Measure-Object).Count` | 533 entries | preserve generated source layout |
| Bootstrap read model path is absent before dispatch | `Test-Path CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `False` | create through generator or documented deterministic source path |
| Worker return path is absent before dispatch | `Test-Path docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_WORKER_RETURN_2026-06-25.md` | `False` | create path |
| Completion review path is absent before dispatch | `Test-Path docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_COMPLETION_2026-06-25.md` | `False` | do not create; reviewer-owned |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This baseline cites bounded files and source rows only; no
  exhaustive directory coverage claim is made.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Exclusions are kept as scope boundaries, with concrete evidence
  rows separated from keyword-heavy prose.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: STATE-BR-T1 may add a compact
active-session bootstrap read model, update the active-session generator,
checker, focused tests, and startup/front-door text needed to route bootstrap
reads through the compact model while preserving the full generated aggregate
as canonical registry.

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

Operator authorization: the operator identified the full active-session
aggregate size as technical debt and directed Codex to handle the Active
Session State Bootstrap Read Model And Aggregate Size Refactor before T1
continues.

Rollback boundary: if rejected, revert only STATE-BR-T1 material changes and
the later session-sync commit for this tranche. Do not revert ASSF-PIC-T0
closure, the selected pilot candidate, prior active-session generated-source
layout, or any prior closed tranche.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator report that Claude bootstrap failed on active-session aggregate size, routed to local session-state refactor |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and the matching STATE-BR-T1 work order |
| Disposition | local active-session bootstrap refactor dispatch only; no external material is absorbed as source authority |
| Claim boundary | operator/Claude report motivates the refactor; implementation facts must still be source-verified against governed repository files |

## JSON Generated Aggregate Discipline Control

| Field | Disposition |
|---|---|
| Existing aggregate | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Existing source layout | `CVF_SESSION/state/` |
| Existing generator | `governance/compat/generate_active_session_state.py` |
| Existing drift checker | `governance/compat/check_active_session_state.py` |
| Required discipline | edit source fragments and generator/checker; do not hand-edit aggregate-only state |
| Closure disposition required | `EXISTING_GENERATED_SOURCE_LAYOUT_REUSED` plus command-backed drift checks |

## Required Worker Deliverables

| Path | Required at worker return | Purpose |
|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Yes | compact generated bootstrap read model |
| `governance/compat/generate_active_session_state.py` | Yes | generate/check compact read model and full aggregate together |
| `governance/compat/check_active_session_state.py` | Yes | enforce compact read model drift and size constraints |
| `governance/compat/test_generate_active_session_state.py` | Yes | focused tests for read model generation, drift, and size behavior |
| `AGENTS.md` | Yes | startup text points agents to compact bootstrap model first while keeping full aggregate canonical |
| `CVF_SESSION_MEMORY.md` | Yes | front-door bootstrap text is compact-read-model aware |
| `AGENT_HANDOFF_V22_2026-06-22.md` | Yes | active handoff bootstrap text is compact-read-model aware |
| `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_WORKER_RETURN_2026-06-25.md` | Yes | worker return with evidence, changed paths, gates, and boundary |

## Reviewer-Owned Closure Deliverables

| Path | Owner | Purpose |
|---|---|---|
| `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_COMPLETION_2026-06-25.md` | Codex reviewer/closer | completion review after worker return |
| this baseline | Codex reviewer/closer | status conversion after review |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_FOR_CLAUDE_2026-06-25.md` | Codex reviewer/closer | status conversion after review |
| active session front door, state sources, generated state, and active handoff | Codex session-sync steward | session continuity after material review commit |

## Reviewer Closure Package

| Closure item | Evidence | Disposition |
|---|---|---|
| Worker return reviewed | `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_WORKER_RETURN_2026-06-25.md` | ACCEPTED |
| Protected bootstrap surface commit | `4c0d29e0` | ACCEPTED_WITH_REASON: split required by commit steward to keep protected session/handoff paths out of AOT material review commit |
| Completion review | `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_COMPLETION_2026-06-25.md` | PRESENT |
| Final disposition | focused tests, generator drift check, active-session compatibility, worker-return fast gate, pre-implementation autorun gate | CLOSED_PASS_BOUNDED |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_FOR_CLAUDE_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ACTIVE_SESSION_STATE_BOOTSTRAP_READ_MODEL_AGGREGATE_SIZE_REFACTOR_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ASSF-PIC-T1 dependency on STATE-BR-T1 closure is satisfied for later GC-018/work-order authoring only | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | protected bootstrap surface committed at `4c0d29e0` | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V22_2026-06-22.md`; `AGENTS.md` | compact startup read-order pointers present | PASS |
| External evidence digest | N/A with reason | no external-source authority accepted; operator report used only as trigger | N/A with reason |
| System loop interlock | active-session generator/checker/test changes | no runtime loop, Web adapter, provider, or package execution released | PASS |
| Session continuity | separate session-sync after material closure | REQUIRED_AFTER_MATERIAL_COMMIT | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Worker return accepted | reviewer accepts `COMPLETE_PENDING_REVIEW` return | accepted in completion review | PASS |
| Bootstrap read model exists | file committed and size-bounded | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; 1377 bytes at worker return | PASS |
| Full aggregate remains canonical | `activeStateRegistry` remains `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generator/checker preserve full aggregate pointer | PASS |
| Forbidden scope remains closed | no ASSF package/runtime/adapter/live/public/push release | closure claim boundary keeps all forbidden scope closed | PASS |

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| Compact bootstrap read model exists and is generated or checked from active-session sources | PASS |
| Compact bootstrap read model includes current mode, active handoff, next allowed move, active state registry pointer, and enough startup context to avoid opening the full aggregate first | PASS |
| Full aggregate remains canonical and still validates against `CVF_SESSION/state/` | PASS |
| Active-session checker fails on bootstrap read model drift or oversize condition | PASS |
| Focused tests cover generation/check behavior and drift or size failure | PASS |
| Startup/front-door text routes agents to compact bootstrap read model first without removing the full aggregate registry requirement | PASS |
| ASSF-PIC-T1 remains held until reviewer closure | PASS |
| Worker does not commit | PASS |

## Fail Conditions

Return `BLOCKED_WITH_REASON` if any condition is true:

- the worker must remove the full active-session aggregate or demote it from
  canonical registry;
- the compact read model cannot be kept deterministic from governed sources;
- the checker cannot detect drift or size regression inside allowed scope;
- the worker needs package instance creation, certification, generated-index
  mutation, resolver mutation, Web runtime change, CLI/MCP adapter behavior,
  provider/live proof, public-sync, push, or package activation;
- source verification uses provider-local memory as authority;
- a required gate failure cannot be repaired inside owned paths.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | STATE-BR-T1 active-session bootstrap read model and aggregate size refactor dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch baseline only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, or adapter receipt exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and artifact manifest |
| invocationBoundary | governed local documentation and generator/checker dispatch only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes a bounded no-commit bootstrap read-model refactor for Claude worker execution |
| forbiddenExpansion | no ASSF package instance, certification decision, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, or package instruction execution |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch changes private provenance session-continuity and
governance-helper surfaces. No public-sync repository work or public catalog
claim is authorized.

## Claim Boundary

This baseline authorizes only STATE-BR-T1 active-session bootstrap read-model
and aggregate-size refactor work. It does not create or certify an ASSF package,
mutate the ASSF generated index, modify the ASSF resolver, change CVF Web
runtime source, implement a CLI/MCP adapter, activate or execute any skill, run
provider/live proof, export public artifacts, push to any remote, or update
session continuity by worker action.
