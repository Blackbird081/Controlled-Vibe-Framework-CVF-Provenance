# CVF Agent Work Order: Dispatch Packet Authoring Guard Hardening For Claude

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: CLOSED_PASS_BOUNDED

Worker / Implementer: Claude

Orchestrator: Codex

Reviewer / closer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `047f9ea4`

executionBaseHead: Claude must capture with `git rev-parse --short HEAD`
before the first edit.

closureBaseHead: Codex records after reviewer commit.

riskCeiling: R1_GOVERNANCE_CHECKER_ONLY_NO_LIVE_PROVIDER

completionReviewPath:
`docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md`

## Purpose

Promote the P4B-B dispatch packet authoring defects into reusable CVF
governance controls before anyone repairs the P4B-B packet. The current P4B-B
GC-018/work order is the regression sample and must remain read-only in this
work order.

## 1. Mission

Claude must:

1. prove the current P4B-B packet fails dispatch-quality for the known finding
   bundle before any fix;
2. add focused regression coverage for the finding bundle;
3. add or harden a packet-author fast gate so future packet authors have a
   single pre-return command;
4. document the rule in the relevant reference surface;
5. return uncommitted artifacts to Codex for review.

The new operator authorization to use existing API keys for later P4B-B live
test is acknowledged but out of scope here. This governance hardening work must
not read keys or call providers.

## 2. Authority Chain

| Authority | Path / basis | Disposition |
|---|---|---|
| Operator instruction | 2026-06-15 chat: raise CVF foundation, test with these findings before fixing, transfer to Claude | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_2026-06-15.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V19_2026-06-15.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | Defines governance hardening scope and keeps P4B-B repair out of scope |
| Worker | Claude | Implements checker/test/wrapper/reference changes only |
| Reviewer / closer | Codex | Runs reviewer-fast, focused tests, pre-closure, and commits if accepted |
| Operator | Human | Later authorizes P4B-B live provider execution under a separate corrected packet |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Repeated packet authoring defects in Claude-authored P4B-B work order |
| Scope classification | Governance/control-plane learning |
| Risk sensitivity | No provider, no credential, no runtime behavior, no public-sync |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Claude worker implements; Codex reviewer/committer closes |
| Escalation condition | Stop if repair requires editing P4B-B packet, live provider use, session state, or runtime source |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | Claude worker returns uncommitted artifacts; Codex reviewer closes |
| Evidence basis | Failing P4B-B packet gate output, focused tests, diff, reviewer-fast |
| Self-review boundary | Claude may run tests but must not commit or close |
| Gate sequence | baseline failure evidence -> focused regression test -> implementation -> worker-return fast gate |
| Escalation conditions | Stop for P4B-B packet edits, live provider/API use, credential reads, runtime source changes, session-state changes, package installs, or public-sync |

## 4. Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | active governance |
| `CVF_SESSION_MEMORY.md` | current mode and parked P4B-B boundary |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and session boundary |
| `docs/baselines/CVF_GC018_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_2026-06-15.md` | authorized scope |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_FOR_CODEX_2026-06-15.md` | read-only negative sample |
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_2026-06-15.md` | read-only negative sample |
| `governance/compat/check_work_order_dispatch_quality.py` | owner checker |
| `governance/compat/test_check_work_order_dispatch_quality.py` | regression test owner |
| `governance/compat/run_local_governance_hook_chain.py` | existing hook integration |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | template rule owner |

## 5. Allowed Scope

| Path | Action |
|---|---|
| `governance/compat/check_work_order_dispatch_quality.py` | modify only if needed to harden detection/message grouping |
| `governance/compat/test_check_work_order_dispatch_quality.py` | add regression test for P4B-B authoring defect bundle |
| `governance/compat/run_dispatch_packet_author_fast_gate.py` | create optional one-command packet-author gate |
| `governance/compat/test_run_dispatch_packet_author_fast_gate.py` | create optional wrapper tests |
| `docs/reference/CVF_DISPATCH_PACKET_AUTHORING_GUARD_STANDARD_2026-06-15.md` | create/update standard if wrapper or rule is added |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | minimal pointer update only if needed |
| `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` | create completion review |

## Write Ownership

The P4B-B GC-018/work-order files are read-only regression inputs:

- `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_2026-06-15.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_FOR_CODEX_2026-06-15.md`.

Do not edit, rename, move, stage, or repair those files in this work order.

## 6. Forbidden Scope And Stop Conditions

Stop before:

- editing the P4B-B packet;
- reading `.env.local`, API keys, or provider credentials;
- running a live provider/API call;
- modifying Model Gateway runtime source;
- changing active session state or handoff;
- weakening existing dispatch-quality checks;
- making public, production, provider-quality, or provider-preference claims.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Work-order template requires Worker Autonomy / No-Question Rule for ready/dispatched work orders | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 98 and 523 | `Worker Autonomy / No-Question Rule` | work-order template | ACCEPT |
| Work-order template names dispatchBaseHead as required dispatch evidence | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | line 1028 | `dispatchBaseHead` | work-order template | ACCEPT |
| Dispatch checker identifies ready/dispatched/closed status as dispatching | `governance/compat/check_work_order_dispatch_quality.py` | lines 130-141 and 296 | `DISPATCH_STATUS_TOKENS`; `_is_ready_or_dispatch_status` | dispatch-quality checker | ACCEPT |
| Dispatch checker requires Worker Autonomy / No-Question Rule | `governance/compat/check_work_order_dispatch_quality.py` | lines 618 and 2175 | `_has_worker_autonomy_clause` | dispatch-quality checker | ACCEPT |
| Dispatch checker rejects non-commit dispatchBaseHead | `governance/compat/check_work_order_dispatch_quality.py` | lines 649-656 | `dispatchBaseHead` | dispatch-quality checker | ACCEPT |
| Dispatch checker rejects noncanonical Source Verification columns | `governance/compat/check_work_order_dispatch_quality.py` | line 922 | `Source Verification table uses noncanonical columns` | dispatch-quality checker | ACCEPT |
| Dispatch checker rejects noncanonical Source Verification disposition values | `governance/compat/check_work_order_dispatch_quality.py` | line 61 | `ALLOWED_SOURCE_VERIFICATION_DISPOSITIONS` | dispatch-quality checker | ACCEPT |
| Reviewer-fast already includes dispatch-quality | `governance/compat/run_local_governance_hook_chain.py` | line 24 | `REVIEWER_FAST_CHECKS` | local hook chain | ACCEPT |
| Autorun pre-dispatch already includes dispatch-quality | `governance/compat/run_agent_autorun_workflow_gate.py` | line 50 | `_common_commands` | autorun workflow gate | ACCEPT |

## Worker Autonomy / No-Question Rule

Claude must repair any failing gate inside the Allowed Scope without asking the
operator. Ask only if the repair would require editing the P4B-B packet, running
live provider/API calls, reading credentials, touching runtime source, changing
session state, adding package dependencies, or broadening the claim boundary.

## Reviewer Closure Conversion

Because `Commit mode: WORKER_MUST_NOT_COMMIT`, Claude must return uncommitted
artifacts only. Codex owns:

- reviewing the real diff;
- authoring or accepting the completion review;
- running reviewer-return and pre-closure gates;
- committing material artifacts if accepted;
- deciding whether a separate session-sync is required.

## Regression-First Protocol

Before implementation, run:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 047f9ea4 --head HEAD --enforce
```

Record the failure output in the completion review. It must include these
finding classes from the current P4B-B packet:

- missing Worker Autonomy / No-Question Rule;
- non-commit `dispatchBaseHead`;
- noncanonical Source Verification table columns;
- noncanonical Source Verification disposition values.

Then add a focused regression test that constructs a P4B-B-like defective packet
and asserts all four issue classes are detected together. The test must live in
`governance/compat/test_check_work_order_dispatch_quality.py` unless Claude
creates a more focused fixture file within the Allowed Scope.

## Implementation Requirements

If the existing checker already catches the finding bundle, do not weaken it.
Instead, add:

- a bundle regression test so future edits cannot lose coverage;
- a packet-author fast gate wrapper or documented one-command authoring command
  that runs dispatch-quality, markdown structural completeness, authority and
  encoding, and agent operation trace checks before a worker returns a dispatch
  packet;
- clear output telling the author to keep the packet in draft/hold when any
  dispatch-quality issue remains.

If a wrapper is created, it must default to the captured packet-author base
commit and `--head HEAD --enforce` for uncommitted packet-author returns and
accept explicit `--base` / `--head` overrides.

## Pre-Flight Checks

Before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 047f9ea4 --head HEAD --enforce
```

The dispatch-quality command is expected to fail because the P4B-B negative
sample is present. Claude must record the four finding classes and then proceed
only within this work order's Allowed Scope.

## Required Tests And Gates

Minimum focused tests:

```powershell
python -m unittest governance.compat.test_check_work_order_dispatch_quality
```

If a wrapper is added:

```powershell
python -m unittest governance.compat.test_run_dispatch_packet_author_fast_gate
python governance/compat/run_dispatch_packet_author_fast_gate.py --base 047f9ea4 --head HEAD --enforce
```

Worker-return gates:

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

Do not claim closure if any command fails.

## Execution Plan

| Step | Action | Output |
|---|---|---|
| 1 | Read required first reads and capture executionBaseHead | startup evidence |
| 2 | Run dispatch-quality against current P4B-B negative sample | expected failure evidence |
| 3 | Add bundle regression test for the four findings | focused test coverage |
| 4 | Add packet-author fast gate or documented equivalent | one-command authoring control |
| 5 | Run focused tests and worker-return fast gate | command evidence |
| 6 | Author completion review and return uncommitted artifacts | worker return |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Current P4B-B packet failure reproduced before implementation | completion review command output |
| AC2 | Regression test covers all four finding classes together | focused test |
| AC3 | Packet-author fast command or reference rule exists | wrapper or standard path |
| AC4 | P4B-B GC-018/work-order files unchanged | git diff/status evidence |
| AC5 | No live provider, credential, runtime, session, public-sync, or package work occurred | completion review claim boundary |
| AC6 | Worker-return fast gate and diff hygiene pass | command evidence |

## Review Gate

Codex reviewer must inspect that the P4B-B negative sample was not modified,
verify the regression test names the four finding classes, rerun focused tests,
run `run_worker_return_fast_gate.py`, and only then decide whether to commit.

## Operator Checkpoint

No operator pause is required inside the Allowed Scope. Operator input is
required only if Claude needs to edit the P4B-B packet, run live/provider tests,
read credentials, modify runtime source, change session state, install packages,
or broaden the claim boundary.

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order section | Disposition |
|---|---|---|
| Raise CVF foundation instead of blaming worker | Purpose; Finding-To-Governance Learning Disposition | RELEASED |
| Test against current findings before fixing | Regression-First Protocol | RELEASED |
| Do not fix P4B-B packet in this batch | Write Ownership; Forbidden Scope | ENFORCED |
| Add reusable guard/test coverage | Implementation Requirements | RELEASED |
| Transfer to Claude for implementation | Agent Roles; Commit mode | RELEASED |

## Evidence Requirements

Completion review must include:

- executionBaseHead;
- pre-implementation failing output from current P4B-B packet;
- focused regression test result;
- wrapper test result if wrapper is added;
- worker-return fast gate result;
- `git diff --check` result;
- exact changed set;
- explicit statement that no P4B-B packet repair, live provider call, API key
  read, Model Gateway runtime change, public-sync, production-readiness, or
  provider-preference claim occurred.

## Return-To-Orchestrator Conditions

Return to Codex without implementation if:

- the P4B-B negative sample is no longer present;
- the required failure evidence cannot be reproduced;
- the fix requires editing P4B-B packet files;
- the fix requires runtime/provider/credential/session changes;
- the new wrapper would duplicate an existing equivalent command without a
  clear routing improvement.

## Required Artifact Manifest

Expected material paths may include only:

| Artifact | Action |
|---|---|
| `governance/compat/check_work_order_dispatch_quality.py` | modify if needed |
| `governance/compat/test_check_work_order_dispatch_quality.py` | modify |
| `governance/compat/run_dispatch_packet_author_fast_gate.py` | create optional |
| `governance/compat/test_run_dispatch_packet_author_fast_gate.py` | create optional |
| `docs/reference/CVF_DISPATCH_PACKET_AUTHORING_GUARD_STANDARD_2026-06-15.md` | create optional |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | minimal pointer update optional |
| `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` | create |

The P4B-B GC-018/work-order files must not appear in the material changed set.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded dispatch-packet authoring guard
hardening. This batch may add or harden tests and wrapper tooling for dispatch
packet authoring checks only.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `governance/compat/run_dispatch_packet_author_fast_gate.py`
- `governance/compat/test_run_dispatch_packet_author_fast_gate.py`

Operator authorization: 2026-06-15 operator instruction to raise the CVF
foundation first, test against the current findings before fixing the P4B-B
packet, and transfer implementation to Claude.

Rollback boundary: revert only this bounded hardening batch if the guard or
wrapper creates false positives. Do not revert unrelated Model Gateway,
session, public-sync, or P4B-B draft-sample commits.

## Work-Order Fulfillment Manifest

The Required Artifact Manifest above is the fulfillment manifest for this work
order. Claude must report exact changed paths in the completion review.

## Closure Checklist

- [x] executionBaseHead captured before first edit.
- [x] Current P4B-B negative sample failure reproduced before implementation.
- [x] Regression test covers all four finding classes.
- [x] Packet-author fast command/wrapper or documented rule added.
- [x] No P4B-B packet files changed in this hardening material range.
- [x] No live provider/API key/runtime/session/public-sync work performed.
- [x] Focused tests PASS.
- [x] Worker-return fast gate PASS after reviewer repair.
- [x] `git diff --check` PASS.
- [x] Completion review authored with finding-to-governance learning.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | Codex reviewer converted to closed bounded after worker return | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` | completion review authored and closed bounded | PASS |
| Roadmap state | N/A | N/A with reason: this work order derives from GC-018 and operator authorization, not a roadmap tranche | N/A with reason |
| Registry JSON | N/A | BLOCKED with reason: corpus/search signal appears only in negative-search discipline prose; no GC-051 JSON registry update is in scope | BLOCKED with reason |
| Registry Markdown | N/A | BLOCKED with reason: corpus/search signal appears only in negative-search discipline prose; no Markdown registry update is in scope | BLOCKED with reason |
| External evidence digest | N/A | N/A with reason: no external evidence artifact or external path is claimed | N/A with reason |
| System loop interlock | N/A | N/A with reason: no system-loop interlock registry or rule changed | N/A with reason |
| Session continuity | N/A | N/A with reason: no active session nextAllowedMove or handoff state changed in this material range | N/A with reason |
| Regression evidence | completion review | P4B-B packet fails before implementation | PASS |
| Guard/test coverage | governance/compat tests | focused test PASS | PASS |
| Worker-return gate | completion review | `run_worker_return_fast_gate.py` output after reviewer repair | PASS |
| Public export | this file | DEFERRED_PRIVATE_ONLY | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Claude returned a dispatch packet with missing No-Question Rule, prose dispatchBaseHead, noncanonical Source Verification columns, and boundary prose in disposition | PACKET_AUTHORING_GUARD_GAP | governance/control-plane learning | MACHINE_CHECK_CANDIDATE | Add regression coverage and packet-author fast gate/routing |

## Negative Search And Collision Discipline

Claude must not use broad repo search to reclassify unrelated packets. The only
authorized negative sample is the current P4B-B GC-018/work-order pair. If a
finding string appears in unrelated documentation, classify it as a same-token
documentation collision and keep the control focused on dispatch packet
authoring.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 Claude work order dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `apply_patch`; governance review |
| Target paths | GC-018 and this work order |
| Allowed scope source | operator instruction 2026-06-15 |
| Before status evidence | current P4B-B packet fails dispatch-quality |
| After status evidence | Claude guard-hardening work order authored |
| Diff evidence | uncommitted dispatch packet |
| Approval boundary | governance checker/template hardening only |
| Claim boundary | no P4B-B repair, no live call, no runtime behavior claim |
| Agent type | Codex orchestrator |
| Invocation ID | dispatch-packet-authoring-guard-hardening-for-claude-2026-06-15 |
| Expected manifest | `docs/baselines/CVF_GC018_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_FOR_CLAUDE_2026-06-15.md`; `governance/compat/test_check_work_order_dispatch_quality.py`; `governance/compat/run_dispatch_packet_author_fast_gate.py`; `governance/compat/test_run_dispatch_packet_author_fast_gate.py`; `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_FOR_CLAUDE_2026-06-15.md`; `governance/compat/test_check_work_order_dispatch_quality.py`; `governance/compat/run_dispatch_packet_author_fast_gate.py`; `governance/compat/test_run_dispatch_packet_author_fast_gate.py`; `docs/reviews/CVF_DISPATCH_PACKET_AUTHORING_GUARD_HARDENING_COMPLETION_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

This work order authorizes only governance packet-authoring guard hardening. It
does not authorize P4B-B packet repair, live provider execution, credential
reads, Model Gateway runtime changes, session-state mutation, public-sync,
production readiness, public readiness, or provider preference claims.
