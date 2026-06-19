# CVF Agent Work Order - EKA-R1 External Knowledge Intake Routing Guard For Codex - 2026-06-19

Memory class: FULL_RECORD

Status: DISPATCH_READY_FOR_CODEX

Owner: Codex Orchestrator

Worker target: Codex

Commit mode: WORKER_MAY_COMMIT

rawMemoryReleased=false

dispatchBaseHead: `84e9d190`

executionBaseHead: `84e9d190`

closureBaseHead: `84e9d190`

## Dispatch Prompt Envelope

Agent: Codex

Task: implement EKA-R1, a bounded range-aware external knowledge intake
routing guard.

Read first:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V20_2026-06-19.md`
4. `docs/baselines/CVF_GC018_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_2026-06-19.md`
5. `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
6. `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
7. `governance/compat/check_external_agent_absorption_table.py`

Do:

- add `governance/compat/check_external_knowledge_intake_routing.py`;
- add focused tests;
- wire the checker into reviewer-fast, pre-commit, pre-push, and autorun;
- close with completion review and evidence JSON.

Do not:

- import or rescan external repos/folders;
- expand corpus registry content;
- run live providers or consume secrets/quota;
- public-sync;
- implement runtime, MCP, wrapper, IDE, shell, git, or filesystem
  interception;
- claim universal governed-coding control.

## Purpose

Make the external knowledge absorption chain map machine-visible at the intake
artifact boundary so future external/corpus/repo/legacy claims cannot quietly
skip routing evidence.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V20_2026-06-19.md`
- `docs/baselines/CVF_GC018_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_2026-06-19.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
- `governance/compat/check_external_agent_absorption_table.py`

## Authority Chain

| Layer | Artifact |
| --- | --- |
| Session front door | `CVF_SESSION_MEMORY.md` |
| Machine state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` |
| Upstream selection | `docs/reviews/CVF_POST_DELTA_T3_NEXT_FOUNDATION_TRANCHE_SELECTION_2026-06-19.md` |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Returned-output workflow | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` |
| Existing local-view guard | `governance/compat/check_external_agent_absorption_table.py` |
| GC-018 baseline | `docs/baselines/CVF_GC018_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_2026-06-19.md` |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | source-verify and authorize bounded local scope |
| Worker | Codex | implement checker, tests, hook wiring, and evidence |
| Reviewer | Codex | run focused tests and governance gates |
| Closer | Codex | commit material, then session-sync separately |

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Incoming operator request | Proceed with the recommended EKA-R1 tranche |
| Intake role | Codex single-agent implementation and review |
| Dispatch route | `SINGLE_AGENT_MULTI_ROLE` |
| Selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| Risk sensitivity | Medium governance-foundation change: checker/hook wiring only, with no runtime/provider/public-sync mutation |
| Escalation condition | Stop only if a fix requires scope expansion, live/provider proof, secrets/quota, public-sync, broad external import, broad legacy/corpus scan, runtime mutation, or universal interception/readiness claim |
| External worker needed | N/A with reason: bounded Python checker and hook wiring are local Codex scope |
| Commit owner | Codex |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Orchestrator | Codex |
| Worker | Codex |
| Reviewer | Codex |
| Closer | Codex |
| Separation control | Dispatch packet commit, material/closure commit, and session-sync commit remain separate where required by guard shape |
| Conflict control | No external worker material is accepted in this tranche |
| Role separation ledger | This block records Codex as orchestrator, worker, reviewer, and closer with separate gate evidence before closure |
| Self-review boundary | Codex may review only against this work order, current source, focused tests, and machine gates; no memory-only acceptance |
| Evidence basis independent of memory | Current source files, chain map, work order, completion review, evidence JSON, git diff, and command outputs |
| Gate sequence | dispatch author fast gate, pre-dispatch autorun, dispatch steward, pre-implementation, focused tests, worker fast gate, pre-closure, pre-push |
| Escalation conditions | Stop only if required repair exceeds allowed scope or touches parked live/provider/public-sync/runtime/interception lanes |

## Worker Autonomy / No-Question Rule

Codex must repair any allowed-scope gate failure without stopping for operator
preference. Stop and return only if the repair would expand beyond this work
order, run live or provider proof, use secrets/quota, open public-sync, import
external repos, perform broad legacy/corpus scan, mutate runtime behavior, or
make a universal interception/readiness claim.

## Pre-flight Checks

| Check | Result |
| --- | --- |
| Startup front doors read | PASS |
| Source verification completed | PASS |
| Clean worktree before dispatch authoring | PASS: `git status --short` was empty before authoring |
| Live provider authorization | N/A with reason: not authorized and not needed |
| Public-sync authorization | N/A with reason: not authorized |
| Broad external absorption authorization | N/A with reason: not authorized |

## Write Ownership

| Path class | Ownership |
| --- | --- |
| Checker source | Codex may add one bounded Python checker |
| Checker tests | Codex may add focused pytest coverage |
| Hook wiring | Codex may add the checker to existing local and autorun chains |
| Runtime/source outside governance compat | Read-only |
| Session state and handoff | Dedicated session-sync commit once material closure is accepted |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Applicable row | `NOT_APPLICABLE_WITH_REASON` |
| Reason | EKA-R1 implements a general intake routing guard from the chain map and does not open a legacy family absorption or rescan |
| Legacy source reading | Not authorized |
| Next action | Future legacy-adjacent work orders remain responsible for their own coverage-index row evidence |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Chain map requires external knowledge intake to identify input type before routing. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Mandatory Chain` | `Identify input type` | external knowledge chain map | ACCEPT |
| Chain map defines the input type router for legacy, external repo, external-agent, public vocabulary, corpus, and runtime/MCP claims. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Input Type Router` | `Input type` | external knowledge chain map | ACCEPT |
| Chain map records partial enforcement and requires the most specific existing local-view guard. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Enforcement Gap` | `most specific existing guard` | external knowledge chain map | ACCEPT |
| Chain map names changed external knowledge intake artifacts as a future checker target. | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Machine-Check Candidate` | `changed external knowledge intake artifacts cite this chain map` | external knowledge chain map | ACCEPT |
| Returned external-agent output already has a Required Absorption Table checker. | `governance/compat/check_external_agent_absorption_table.py` | module constants and `check_text` | `REQUIRED_SECTION`; `check_text` | external-agent absorption table guard | ACCEPT |
| Local hook chain wires local-view governance checks through reviewer-fast, pre-commit, and pre-push lists. | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS`; `HOOK_CHAINS` | `external-agent absorption table` | local governance hook chain | ACCEPT |
| Autorun phase gates compose range-aware checks through `_common_commands`. | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `external-agent absorption table` | autorun workflow gate | ACCEPT |
| Work-order source verification is mandatory for runtime/source field claims. | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `Source Verification Block` | `Disposition` | work-order template | ACCEPT |

## External Knowledge Intake Routing

External knowledge intake routing: REQUIRED

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Operator-provided external comparison, critique, or recommendation |
| Chain map route | `Mandatory Chain` plus `Machine-Check Candidate` |
| Matching local-view guard | `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| Owner surface | New EKA-R1 guard under `governance/compat/` |
| Disposition | `ADAPT` into bounded routing guard |
| Claim boundary | This block does not prove broad external absorption, runtime enforcement, public readiness, or universal interception |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex orchestrator/worker/reviewer/closer in one bounded material batch |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE |
| baseHeadFor(phase) | dispatch=`84e9d190`; execution=`84e9d190`; closure=`84e9d190` |
| changedSetScope(phase) | checker, tests, hook wiring, GC-018, work order, completion review, evidence JSON |
| traceScope(phase, actor) | Codex owns dispatch, execution, and closure trace for this material batch |
| commitOwner(phase) | Codex |
| crossBatchIsolation | No session-sync in material commit; no public-sync; no runtime/provider/live work |
| nextMoveSurfaces | Dedicated session-sync records the closed EKA-R1 state and updates active mode and next allowed move |
| closerDesignation | Codex is the closer |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Central Core artifact | Chain map remains stable under `docs/reference/external_agent_review/` |
| Local View artifact | EKA-R1 checker under `governance/compat/` composes existing local-view guards |
| Dated execution artifacts | GC-018, work order, completion review, evidence JSON |
| Stable path rule | No new dated foundation front door; no date-sprawl reference path |
| Archive policy | No archive movement |
| Machine enforcement | New checker wired into existing hook and autorun chains |

## Agent Workspace Design Control Block

| Field | Disposition |
| --- | --- |
| Workspace purpose | N/A with reason: this tranche implements a governance checker, not an agent workspace |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | N/A with reason: no workspace surface changed |
| Storage class | no workspace state, queue, inbox, dashboard, or read model is created |
| Handoff fields | inherited from Agent Handoff Contract Control Block |
| State ownership | N/A with reason: no workspace state aggregate changes |
| Guard owner | Existing workspace guards are N/A for this scope |
| Build boundary | UI, Local Workspace Runtime, MCP workspace bridge, runtime source changes outside `governance/compat/`, provider proof, public-sync, registry edits, and runtime state mutation remain out of scope |

## Execution Plan

1. Implement `check_external_knowledge_intake_routing.py` using the existing
   range-aware checker style.
2. Add focused tests covering valid block, missing chain-map citation, missing
   routing block, missing local-view guard, N/A-with-reason acceptance, and
   unrelated/archived artifact ignores.
3. Wire the checker into reviewer-fast, pre-commit, pre-push, and autorun
   common gates.
4. Add completion review and evidence JSON.
5. Run focused tests, worker fast gate, and closure/push gates on real ranges.

## Acceptance Criteria

| ID | Criterion | Status |
| --- | --- | --- |
| AC1 | Checker detects changed external knowledge intake artifacts by explicit marker and bounded path markers. | OPEN |
| AC2 | Checker requires citation of `CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`. | OPEN |
| AC3 | Checker requires `## External Knowledge Intake Routing` with input type, chain route, owner surface, disposition, and claim boundary. | OPEN |
| AC4 | Checker requires matching local-view guard or bounded `N/A with reason`. | OPEN |
| AC5 | Checker is wired into reviewer-fast, pre-commit, pre-push, and autorun. | OPEN |
| AC6 | Focused tests and governance gates pass. | OPEN |

## Required Artifact Manifest

| Path | Required disposition |
| --- | --- |
| `governance/compat/check_external_knowledge_intake_routing.py` | add |
| `governance/compat/test_check_external_knowledge_intake_routing.py` | add |
| `governance/compat/run_local_governance_hook_chain.py` | update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update |
| `governance/compat/test_run_local_governance_hook_chain.py` | update |
| `docs/reviews/CVF_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_COMPLETION_2026-06-19.md` | add |
| `docs/reviews/evidence/eka-r1-external-knowledge-intake-routing-guard-2026-06-19.json` | add |

## Work-Order Fulfillment Manifest

| Manifest item | Required evidence |
| --- | --- |
| Checker implementation | `governance/compat/check_external_knowledge_intake_routing.py` exists and passes focused tests |
| Test coverage | `governance/compat/test_check_external_knowledge_intake_routing.py` covers pass, fail, and ignore cases |
| Hook wiring | local hook and autorun chains include `external knowledge intake routing` |
| Completion artifact | completion review records closed evidence and claim boundary |
| Evidence artifact | evidence JSON records command results |

## Evidence Requirements

| Evidence | Required result |
| --- | --- |
| Focused checker tests | PASS |
| Checker smoke over material range | PASS |
| Worker-return fast gate | PASS |
| Pre-closure autorun gate | PASS |
| Pre-push autorun gate | PASS |
| `git diff --check` | PASS |

## Review Gate

Codex reviewer may close only if the checker composes existing guard evidence,
does not duplicate absorption-table semantics, does not overclaim universal
interception, and all focused/governance gates pass.

## Operator Checkpoint

N/A with reason: this bounded checker tranche has no in-scope operator
checkpoint. Any out-of-scope condition is governed by the
Return-To-Orchestrator Conditions section.

## Closure Checklist

- [ ] Dispatch Prompt Envelope present.
- [ ] Source Verification Block present.
- [ ] External Knowledge Intake Routing block present.
- [ ] Agent Handoff Contract Control Block present.
- [ ] Agent Operation Trace Block present in completion review.
- [ ] Public Export Disposition present.
- [ ] Evidence JSON present.
- [ ] Focused and governance checks pass.

## Return-To-Orchestrator Conditions

Return to operator/orchestrator if the implementation requires broad external
repo import, broad legacy scan, corpus registry content expansion, provider
calls, secrets/quota, public-sync, runtime/MCP behavior mutation, wrapper
interception, or a universal governed-coding claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_FOR_CODEX_2026-06-19.md` | Status moves to `CLOSED_PASS_BOUNDED` only at closure | OPEN |
| Completion review | `docs/reviews/CVF_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_COMPLETION_2026-06-19.md` | Completion review exists before closure | OPEN |
| GC-018 | `docs/baselines/CVF_GC018_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_2026-06-19.md` | Status moves to `CLOSED_PASS_BOUNDED` only at closure | OPEN |
| Focused tests | `governance/compat/test_check_external_knowledge_intake_routing.py` | PASS required | OPEN |
| Hook wiring | `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/run_agent_autorun_workflow_gate.py` | checker appears in required gate chains | OPEN |
| Public-sync | N/A with reason: not authorized | no public path changed | N/A with reason |
| Live proof | N/A with reason: not authorized and not needed | no live command run | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI / local filesystem |
| Session or invocation | `eka_r1_external_knowledge_intake_routing_guard_2026-06-19` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, Python governance gates |
| Target paths | EKA-R1 checker, tests, hook wiring, GC-018, work order, completion review, evidence JSON |
| Allowed scope source | Operator authorization and this work order |
| Before status evidence | Base head `84e9d190`; clean worktree before dispatch authoring |
| After status evidence | Pending implementation |
| Diff evidence | `git status --short`; `git diff --check`; autorun gates |
| Approval boundary | Bounded external knowledge intake routing guard only |
| Claim boundary | No runtime/provider/live/public-sync/broad external absorption/universal interception |
| Agent type | Codex |
| Invocation ID | `eka-r1-routing-guard-codex-2026-06-19` |
| Expected manifest | GC-018, work order, checker, tests, hook wiring, completion review, evidence JSON |
| Actual changed set | Pending implementation |
| Manifest delta | Pending implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance guard. Public-sync is not authorized.

## Claim Boundary

This work order authorizes only a range-aware routing guard over changed
governed external-intake artifacts. It does not authorize broad external
absorption, legacy rescan, runtime behavior, provider/live proof, public-sync,
wrapper/proxy control, or universal bypass prevention.
