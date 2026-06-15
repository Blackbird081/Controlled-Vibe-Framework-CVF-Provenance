# CVF Agent Work Order: Agent Dispatch Prompt Envelope Standardization For Claude

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: DISPATCH_READY

Worker / Implementer: Claude

Orchestrator: Codex

Reviewer / closer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 4895bca3

executionBaseHead: 4895bca3

closureBaseHead: Codex records after reviewer commit

completionReviewPath:
`docs/reviews/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_COMPLETION_2026-06-15.md`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

riskCeiling: R1_GOVERNANCE_AUTHORING_TIME_ONLY

## Purpose

Implement the T1 foundation for standardized dispatch prompt envelopes. The
goal is to help agents understand current-time handoff facts quickly while
keeping the canonical work order as the source of truth.

## Authority Chain

| Authority | Path / basis | Disposition |
|---|---|---|
| Operator instruction | 2026-06-15 chat: standardize dispatch prompts for multi-agent and role-switching work | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_2026-06-15.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V19_2026-06-15.md` | ACCEPT |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | authored roadmap, GC-018, and dispatch packet |
| Worker / implementer | Claude | implements standard, checker, tests, fast-gate wiring, completion review |
| Reviewer / closer | Codex | reviews diff, runs gates, commits if accepted |
| Operator | Human | authorizes scope expansion only |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Standardize short dispatch prompt envelopes for multi-agent and role-switching handoffs |
| Scope classification | Governance/control-plane authoring-time foundation |
| Risk sensitivity | Low runtime risk; protected governance checker paths require core guard authorization |
| Selected role route | SINGLE_AGENT_MULTI_ROLE_ALLOWED_WITH_REVIEWER_SPLIT |
| Role separation basis | Claude implements; Codex reviews and commits |
| Escalation condition | Stop for runtime/provider/live/public scope or broader authority claims |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | Claude records standard authoring, checker implementation, test execution, and completion review as separate steps |
| Evidence basis | source diff, focused tests, dispatch author fast gate, reviewer-fast if run |
| Self-review boundary | Claude may self-check but cannot commit or close |
| Gate sequence | focused tests, dispatch author fast gate, diff check, worker-return fast gate when applicable |
| Escalation conditions | runtime/provider/live/public scope, package install, or protected path beyond Allowed Scope |

## Mission

Create a bounded authoring-time standard and machine gate for dispatch prompt
envelopes:

1. Author the canonical standard.
2. Add a concise pointer/template section to the existing work-order template.
3. Add a checker that validates dispatch-ready work orders include the envelope
   or explicit `N/A with reason`.
4. Add focused checker tests.
5. Wire the checker into `run_dispatch_packet_author_fast_gate.py`.
6. Author a completion review and return uncommitted.

## Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | active governance rules |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff/state registry |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff |
| Roadmap | scope and acceptance |
| GC-018 | authorization and not-authorized list |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | template owner |
| `governance/compat/run_dispatch_packet_author_fast_gate.py` | fast-gate owner |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Work-order template already defines Single-Agent Multi-Role Control Block | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 414 | `Single-Agent Multi-Role Control Block` | work-order template | ACCEPT |
| Work-order template already requires Worker Autonomy / No-Question Rule | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 523 | `Worker Autonomy / No-Question Rule` | work-order template | ACCEPT |
| Work-order template already names Reviewer Closure Conversion | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 599 | `Reviewer Closure Conversion Block` | work-order template | ACCEPT |
| Dispatch author fast gate exists and runs authoring checks | `governance/compat/run_dispatch_packet_author_fast_gate.py` | lines 1-29 | `GATE_COMMANDS` | dispatch author fast gate | ACCEPT |
| Agent Operation Trace marker is machine-recognized | `governance/compat/check_agent_operation_trace.py` | line 24 | `TRACE_MARKER` | agent operation trace checker | ACCEPT |
| Commit steward standard separates operation trace and commit scope | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | line 32 | `Agent Operation Trace Block` | commit steward standard | ACCEPT |

## Allowed Scope

| Path | Action |
|---|---|
| `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | create |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | minimal pointer/template update |
| `governance/compat/check_dispatch_prompt_envelope.py` | create |
| `governance/compat/test_check_dispatch_prompt_envelope.py` | create |
| `governance/compat/run_dispatch_packet_author_fast_gate.py` | add checker to fast gate |
| `docs/reviews/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_COMPLETION_2026-06-15.md` | create |

## Write Ownership

Claude owns only the Allowed Scope paths above. All runtime/provider source,
session front doors, handoffs, public-sync, package manifests, and unrelated
governance checkers are read-only.

## Forbidden Scope

- Runtime/source behavior outside authoring guard files;
- provider calls, live API calls, key reads, network tests, or credential use;
- public-sync;
- co-work product/platform development;
- provider-specific memory as source authority;
- work outside the Allowed Scope table;
- claims that dispatch prompts can override work orders, GC-018, standards, or
  source verification.

## Dispatch Prompt Envelope

This is the runtime cover note Codex is using for this work order:

```text
Role: Claude is worker/implementer. Codex is reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_FOR_CLAUDE_2026-06-15.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: executionBaseHead 4895bca3.
Current-time notes: implement authoring-time prompt-envelope standardization only; no runtime/provider/live/public work.
Required first actions: read AGENTS.md, CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V19_2026-06-15.md, roadmap, GC-018, and this work order.
Return contract: COMPLETE_PENDING_REVIEW with exact changed paths, tests/gates run, and HEAD unchanged; or BLOCKED_WITH_REASON.
```

## Pre-Flight Checks

Before implementation:

```
git rev-parse --short HEAD
git status --short
python governance/compat/check_active_session_state.py --enforce
```

Before worker return:

```
python governance/compat/run_dispatch_packet_author_fast_gate.py --base 4895bca3 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Claude may add one bounded authoring-time
checker, tests, and fast-gate wiring for dispatch prompt envelope validation.
No runtime/provider behavior is authorized.

Protected paths:

- `governance/compat/check_dispatch_prompt_envelope.py`
- `governance/compat/test_check_dispatch_prompt_envelope.py`
- `governance/compat/run_dispatch_packet_author_fast_gate.py`

Operator authorization: operator requested CVF foundation hardening for
standardized dispatch prompts on 2026-06-15.

Rollback boundary: if guard gates fail, revert only this dispatch prompt
envelope standardization batch. Do not revert P4B-B T2 material commit
`d15f973e` or session-sync commit `4895bca3`.

## Worker Autonomy / No-Question Rule

Claude must fix any failing gate inside Allowed Scope and rerun it before
returning. Ask the operator only if completion requires runtime/provider
behavior, live credentials, public-sync, package installation, changes outside
Allowed Scope, or a broader claim boundary.

## Reviewer Closure Conversion

Claude returns uncommitted artifacts only. Codex owns diff inspection,
pre-closure on the committed range, commit, and any session-sync update.

## Evidence Requirements

Completion review must include:

- exact changed paths;
- source verification result;
- focused checker tests;
- dispatch author fast gate result;
- reviewer-fast result if run;
- diff hygiene;
- claim boundary;
- Agent Operation Trace Block;
- Finding-To-Governance Learning Disposition.

## Execution Plan

| Step | Action | Output |
|---|---|---|
| 1 | Required reads and source verification | source-backed implementation plan |
| 2 | Author standard | reference doc |
| 3 | Patch work-order template with pointer/envelope section | template diff |
| 4 | Implement checker and tests | checker + tests |
| 5 | Wire checker into fast gate | fast-gate diff |
| 6 | Run tests/gates and author completion review | worker return |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Canonical dispatch prompt envelope standard exists | reference doc |
| AC2 | Work-order template points to required envelope fields | template diff |
| AC3 | Checker passes valid envelope and valid `N/A with reason` cases | focused tests |
| AC4 | Checker fails dispatch-ready work order missing envelope evidence | focused tests |
| AC5 | Fast gate runs the checker | fast-gate output |
| AC6 | No runtime/provider/live/public behavior changed | diff and claim boundary |

## Closure Checklist

- [ ] executionBaseHead captured
- [ ] standard authored
- [ ] template pointer/update authored
- [ ] checker created
- [ ] focused tests created and passing
- [ ] dispatch author fast gate includes checker and passes
- [ ] no runtime/provider/live/public scope touched
- [ ] completion review authored
- [ ] worker returns without commit

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Disposition |
|---|---|---|
| Standardize runtime cover note | Mission; Acceptance Criteria | RELEASED |
| Keep work order canonical | Forbidden Scope; standard requirement | ENFORCED |
| Machine-check early | Allowed Scope; AC3-AC5 | RELEASED |
| Avoid runtime/provider scope | Forbidden Scope | ENFORCED |

## Review Gate

Codex verifies that the checker is bounded, tests cover pass/fail cases, the
fast gate invokes the checker, and no runtime/provider/public surfaces changed.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` if all acceptance criteria pass. Return
`BLOCKED_WITH_REASON` if the checker cannot be wired without broader hook or
runtime changes.

## Operator Checkpoint

No operator pause is required inside Allowed Scope. Operator approval is
required for runtime/provider/live/public scope, package installation, or any
change outside Allowed Scope.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 Claude dispatch packet authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | apply_patch, source inspection, governance gates |
| Target paths | roadmap, GC-018, this work order |
| Allowed scope source | operator requested CVF foundation standardization for dispatch prompts |
| Before status evidence | P4B-B T2 closed; session-sync commit `4895bca3` |
| After status evidence | Claude work order dispatch-ready |
| Diff evidence | dispatch authoring range from `4895bca3` |
| Approval boundary | authoring-time prompt envelope standardization only |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `work-order-dispatch-prompt-envelope-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARDIZATION_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet. No public-sync batch is authorized.

## Claim Boundary

This work order authorizes authoring-time dispatch prompt envelope
standardization only. It does not authorize runtime behavior, provider calls,
live proofs, public-sync, co-work product development, production readiness, or
public readiness.
