# CVF Work Order - MKG4 Gate Evidence Consistency Probe

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Dispatch a worker to test the Self-Reported Gate Evidence Consistency rule by
auditing MKG3's pending review and producing one pending MKG4 review with
current working-tree-aware gate evidence.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request to continue guard testing | ACCEPT |
| MKG4 GC-018 | `docs/baselines/CVF_GC018_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_2026-06-01.md` | ACCEPT |
| MKG4 roadmap | `docs/roadmaps/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_ROADMAP_2026-06-01.md` | ACCEPT |
| MKG3 review | `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md` | ACCEPT |
| Closure-quality standard | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | provide this packet and review worker output | no silent runtime expansion |
| Worker | audit evidence consistency and file pending review | no commit, push, runtime edit, or live proof |
| Reviewer | verify self-reported gate evidence and pending finality | reject stale gate results |

## Scope

Allowed scope:

- read MKG3 review, MKG4 GC-018, MKG4 roadmap, and the closure-quality
  standard;
- create one pending review artifact:
  `docs/reviews/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_REVIEW_2026-06-01.md`;
- run working-tree-aware pending-artifact gates;
- fix documentation-format or evidence-block defects inside this work order's
  Allowed scope.

Forbidden scope:

- `.private_reference/legacy/**` edits;
- runtime/source code edits;
- live/provider proof;
- graph retrieval execution;
- Memory reinjection;
- skill mutation;
- public-sync, push, publish, or local commit by the worker;
- destructive action.

Risk ceiling: R1 planning and documentation.

## Required First Reads

- `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md`
- `docs/baselines/CVF_GC018_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_2026-06-01.md`
- `docs/roadmaps/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_ROADMAP_2026-06-01.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`

## Pre-Flight Checks

Required before worker audit:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MKG3 pending review exists as the audit target | EXISTS | `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md` | Status line | `Status` | MKG3 review | ACCEPT |
| MKG4 GC-018 authorizes documentation-only guard test | EXISTS | `docs/baselines/CVF_GC018_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_2026-06-01.md` | Purpose | `MKG4` | MKG4 GC-018 | ACCEPT |
| Self-Reported Gate Evidence Consistency standard exists | EXISTS | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | Section 4D | `Self-Reported Gate Evidence Consistency` | closure-quality standard | ACCEPT |
| Pending Artifact Evidence Finality standard exists | EXISTS | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | Section 4C | `Pending Artifact Evidence Finality` | closure-quality standard | ACCEPT |
| Worker Autonomy standard exists | EXISTS | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Section 6C | `Worker Autonomy / No-Question Rule` | work-order template | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Read MKG3 and guard authority | Required First Reads | authority summary | source citations | DISPATCHED |
| Check self-reported gate evidence | Execution Plan | MKG4 audit finding | review text inspection | DISPATCHED |
| Run working-tree-aware gates | Pre-Flight Checks / Evidence Requirements | gate evidence block | listed commands | DISPATCHED |
| Preserve pending finality | Pending Artifact Evidence Finality | pending review status | `git status --short` evidence | DISPATCHED |

## Worker Autonomy / No-Question Rule

The worker must not ask the operator before performing non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with reading named files, running git status/diff/rev-parse,
running listed governance gates, fixing documentation format defects inside
Allowed scope, adding missing required evidence blocks, and rerunning failed
guards after allowed-scope remediation.

Ask only if the next action would exceed Allowed scope, edit Legacy source,
edit runtime/source code, run live/provider proof, use secrets/quota,
public-sync, push/publish, commit, change claim boundary or risk, release a
`HOLD_*` prerequisite, touch forbidden paths, or perform destructive/
irreversible action.

## Pending Artifact Evidence Finality

The worker must not commit. Leave the MKG4 review pending for operator review.

Because the review artifact will be pending, it must not claim
`git status --short` is clean. Record the actual pending status line for the
MKG4 review artifact.

Do not cite `--base HEAD~1 --head HEAD` as proof for the pending MKG4 review.
Use working-tree-aware pending-artifact checks and label them as such. If a gate
fails inside Allowed scope, repair and rerun instead of asking whether to fix it.

## Self-Reported Gate Evidence Consistency

If the MKG4 review records a governance gate as `FAIL`, the review must be
`BLOCKED` or `HOLD_*` and name the return action. A non-blocked MKG4 review must
not hand off stale failed gate evidence to the reviewer or operator.

After any rerun, update the Governance Gates Run section before returning the
artifact. Do not say the reviewer/operator should rerun to decide routine
allowed-scope evidence cleanup.

## Worker Dispatch Prompt

Send this exact bounded prompt with the work order when assigning MKG4:

```text
You are assigned MKG4 Gate Evidence Consistency Probe.

Primary work order:
docs/work_orders/CVF_WO_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_2026-06-01.md

Deliverable:
- create docs/reviews/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_REVIEW_2026-06-01.md;
- audit MKG3's pending review for stale self-reported gate evidence;
- run current working-tree-aware pending-artifact gates;
- record actual git status and current gate results;
- leave the review pending and uncommitted for operator review.

Worker Autonomy Rule:
Do not ask the operator before performing non-destructive actions inside the
work order's Allowed scope. If a machine gate fails inside Allowed scope, repair
it and rerun.

Pending Artifact Evidence Finality:
Do not claim git status is clean while the review is pending. Do not use
HEAD~1..HEAD as proof for the pending review. Record actual pending status and
working-tree-aware gate results.

Self-Reported Gate Evidence Consistency:
Do not return a non-blocked artifact that records a required gate as FAIL or
asks the reviewer/operator to rerun/decide routine gate evidence. Repair and
rerun inside Allowed scope, or mark BLOCKED/HOLD with return action if the fix
exceeds scope.

Stop and ask only if the next action would exceed Allowed scope, edit Legacy
source, edit runtime/source code, run live/provider/API proof, use
secrets/quota, public-sync, push/publish, commit, change claim boundary or
risk, release a HOLD prerequisite, touch forbidden paths, or perform destructive
or irreversible action.
```

## Write Ownership

Owned future path:

- `docs/reviews/CVF_MKG4_GATE_EVIDENCE_CONSISTENCY_PROBE_REVIEW_2026-06-01.md`

Forbidden paths are listed in Scope.

Write mode:

- create-only review artifact;
- no commit by worker.

## Execution Plan

1. Read MKG3 review, MKG4 GC-018, MKG4 roadmap, and standards.
2. Capture `baseHead` with `git rev-parse --short HEAD`.
3. Run `git status --short` and record the actual pending state.
4. Inspect MKG3 for stale self-reported gate evidence and summarize finding.
5. Run dispatch-quality and autorun pre-dispatch gates with `--base <baseHead> --head HEAD`.
6. Create the MKG4 review with Source Verification, Gate Evidence Consistency,
   Pending Artifact Evidence Finality, Public Export Disposition, and Claim
   Boundary.
7. If a required gate fails inside Allowed scope, repair and rerun.
8. Leave the review pending for operator review without committing.

## Evidence Requirements

- MKG3 review citation;
- current closure-quality standard citation;
- actual pending `git status --short` line;
- current gate command/result lines;
- explicit PASS or BLOCKED disposition for self-reported gate evidence;
- no-runtime/no-live/no-public/no-commit boundary.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Current gate evidence | no stale self-reported PASS/FAIL mismatch |
| Pending finality | no false clean/staged/range evidence |
| Runtime boundary | no implementation, live proof, or public-sync |
| Worker autonomy | no routine allowed-scope questions |

## Review Gate

Reviewer must reject any MKG4 packet that:

- records a required gate as `FAIL` while status is not `BLOCKED` or `HOLD_*`;
- claims clean git status while the review is pending;
- cites `HEAD~1..HEAD` as proof for an uncommitted review;
- asks the operator whether to fix allowed-scope guard failures.

## Closure Checklist

- N/A with reason: MKG4 worker must not close this tranche or commit the review;
  the worker returns a pending review artifact for operator/reviewer audit.

## Return-To-Orchestrator Conditions

Return if implementation becomes necessary, live proof is required, a guard
failure cannot be repaired inside Allowed scope, or the worker needs to exceed
Allowed scope.

## Operator Checkpoint

Operator explicitly requested continued guard hardening and a new work order to
test the worker behavior after MKG3.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private dispatched work order only. No public-sync remote, public
repository commit, or public artifact path is included.

## Claim Boundary

MKG4 is dispatched as bounded guard-behavior testing only. It does not authorize
implementation, live proof, runtime behavior, public-sync, graph retrieval,
Memory reinjection, skill mutation, hosted readiness, production readiness,
public readiness, or local commit by the worker.
