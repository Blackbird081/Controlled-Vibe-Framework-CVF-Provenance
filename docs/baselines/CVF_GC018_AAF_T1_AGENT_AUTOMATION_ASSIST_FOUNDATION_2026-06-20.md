# CVF GC-018 - AAF-T1 Agent Automation Assist Foundation

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: baseline

dispatchBaseHead: 21521829

Batch ID: AAF-T1

## Purpose

Authorize AAF-T1 as a bounded governance-tooling foundation tranche that turns
the CGE-T2 latency finding into operator-facing automation assistance. The goal
is to reduce external-agent and noncoder reviewer latency by adding a deterministic
read-only helper that classifies the current governed batch, recommends the
correct steward lane, lists missing packet-shape blocks, and prints exact next
commands without weakening CVF guard coverage.

## Operator Authorization

The operator stated on 2026-06-20 that future external agents connected through
CLI/MCP, with a noncoder user, will lose much CVF value if mechanical review
latency repeats. The operator authorized raising CVF automation through helper
functions so the machine supports control and speed, and approved issuing this
work order to Claude as a test of the newly enforced worker-return packet-shape
contract.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 automation-foundation instruction | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| Worker-return packet-shape guard hardening | `docs/reviews/CVF_WORKER_RETURN_PACKET_SHAPE_CONTRACT_GUARD_HARDENING_COMPLETION_2026-06-20.md` | ACCEPT |
| Commit steward protocol | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | ACCEPT |
| Session-sync pack helper | `governance/compat/build_session_sync_pack.py` | ACCEPT |
| Commit steward helper | `governance/compat/run_agent_commit_steward_preflight.py` | ACCEPT |
| Worker-return fast gate | `governance/compat/run_worker_return_fast_gate.py` | ACCEPT |
| Dispatch packet author fast gate | `governance/compat/run_dispatch_packet_author_fast_gate.py` | ACCEPT |

## Scope / Owner Boundary

Allowed scope:

- add a read-only governance helper under `governance/compat/`;
- add focused tests under `governance/compat/`;
- author a worker-return packet under `docs/reviews/`;
- reuse existing helper logic by import or subprocess rather than duplicating
  canonical gate semantics;
- support dispatch, reviewer-return, closure, session-sync, and handoff-sync
  guidance as advisory automation assistance.

Forbidden scope:

- no edits under `EXTENSIONS/**`, product runtime, provider adapters, web UI,
  MCP packages, public-sync, `.github/**`, or dependency manifests;
- no live/provider/API proof, benchmark, public push, or secret access;
- no automatic file edits, staging, committing, pushing, or destructive
  filesystem actions by the new helper;
- no wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, queue/daemon, watcher, or background service;
- no claim that AAF-T1 delivers universal governed-coding control, production
  readiness, public release readiness, or latency elimination.

Risk ceiling: R1 governance tooling, read-only assistance.

## Required Deliverables

Claude must return uncommitted `COMPLETE_PENDING_REVIEW` with exactly these
owned artifacts:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_WORKER_RETURN_2026-06-20.md`

No other files are authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: AAF-T1 is ready for Claude dispatch as a bounded helper
implementation tranche.

Proposed tranche: `AAF-T1 Agent Automation Assist Foundation`.

Tranche owner split: Claude implements the read-only helper, focused tests, and
worker-return artifact without committing. Codex reviews, repairs only within
allowed scope if needed, commits accepted material, and session-syncs if the
current mode or next allowed move changes.

Baseline evidence:

- Current HEAD is `21521829`.
- Worktree was clean before dispatch authoring except the recurring Windows
  global git-ignore permission warning.
- `run_agent_commit_steward_preflight.py`, `build_session_sync_pack.py`,
  `run_worker_return_fast_gate.py`, and `run_dispatch_packet_author_fast_gate.py`
  already provide machine-readable behavior that the new helper can orchestrate.
- `check_work_order_dispatch_quality.py` now enforces Worker Return Packet Shape
  Contract requirements for `WORKER_MUST_NOT_COMMIT` work orders.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 automation-foundation selection | ACCEPT |
| Prior latency hardening | `docs/reviews/CVF_WORKER_RETURN_PACKET_SHAPE_CONTRACT_GUARD_HARDENING_COMPLETION_2026-06-20.md` | ACCEPT |
| Current helper inventory | `governance/compat/build_session_sync_pack.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/run_dispatch_packet_author_fast_gate.py` | ACCEPT |
| External knowledge intake standard | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `21521829`.
- `git status --short` was clean except the recurring Windows global git-ignore
  permission warning.
- Source verification used direct file reads and line anchors from the current
  workspace.

Required pre-dispatch verification before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 21521829 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 21521829 --head HEAD --enforce
```

## Required Helper Behavior

The new helper must:

- be read-only by default and by design;
- accept `--base`, `--head`, `--mode auto|dispatch|implementation|reviewer-return|closure|session-sync|handoff-sync`, `--json`, and `--enforce`;
- classify changed paths into material paths, session paths, active handoff
  paths, and docs/review/work-order dispatch paths using existing steward logic
  where practical;
- recommend the steward lane and exact next command;
- detect whether changed work orders using `WORKER_MUST_NOT_COMMIT` include a
  Worker Return Packet Shape Contract;
- report missing required worker-return return sections and conditional-gate
  sections by reusing or mirroring the machine-enforced contract vocabulary;
- call or reference existing fast gates in command recommendations without
  executing destructive or live/provider actions;
- emit concise human output for noncoder operators and structured JSON for
  future external agent CLI/MCP integration.

## Claim Boundary

AAF-T1 may claim only a deterministic helper foundation for faster local
governance navigation and earlier defect detection. It must not claim automated
governance decisions, runtime control, provider control, public sync readiness,
agent behavior enforcement outside the local governed helper, production
readiness, or universal latency reduction.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | input router to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` and `governance/compat/run_agent_commit_steward_preflight.py` |
| Owner surface | `governance/compat/run_agent_automation_assist.py` after implementation |
| Disposition | ADAPT as CVF-owned governance helper |
| Claim boundary | no third-party source is promoted to CVF authority by this baseline |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T1 read-only governance automation helper only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user invokes the helper manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | automation-assist helper, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, readiness, and universal control remain parked |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T1 is private provenance governance tooling. Public export requires
separate public-sync authorization and a bounded public-facing summary if the
operator requests it later.
