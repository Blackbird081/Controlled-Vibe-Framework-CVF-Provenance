# CVF Agent Handoff Boundary Machine Check Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD_AND_MACHINE_ENFORCED

docType: reference

## Purpose

Define the machine-enforced local view of the ratified Agent Handoff Contract so
future agents cannot author governed handoff work orders by improvising
per-batch semantics.

## Scope / Target / Owner Boundary

Target: governed work orders and closure artifacts that carry agent handoff
semantics.

Owner boundary: this standard governs handoff-boundary contract evidence and
the matching checker. It does not replace the AOT trace checker, commit steward,
dispatch prompt envelope standard, session-state generator, provider behavior,
runtime code, public-sync, or the future agent-interaction workspace.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core for CF-01 through CF-09 |
| AHB roadmap | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | Authorizes AHB-T3 as machine-check candidate after T2 |
| AOT checker | `governance/compat/check_agent_operation_trace.py` | Existing trace/manifest local view |
| Commit steward | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | Phase and commit-owner predecessor surface |
| Dispatch envelope | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | Worker prompt and execution-base predecessor surface |

## Required Work Order Block

Any changed governed work order that uses agent handoff semantics must include:

`## Agent Handoff Contract Control Block`

Required fields:

| Field | Meaning |
|---|---|
| Contract source | Must cite `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | Exactly one of `SINGLE_AGENT_SINGLE_ROLE`, `SINGLE_AGENT_MULTI_ROLE`, `MULTI_AGENT_SINGLE_ROLE`, `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Named actor-to-role pattern under the route |
| phase | Covered phases: DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC as applicable |
| baseHeadFor(phase) | Dispatch, execution, and closure base-head anchors |
| changedSetScope(phase) | Phase-local changed-set scope |
| traceScope(phase, actor) | Actor trace ownership per phase |
| commitOwner(phase) | Commit owner per phase |
| crossBatchIsolation | One-batch-per-clean-worktree disposition |
| nextMoveSurfaces | Session-sync surfaces if the batch changes the next move |

The work order must state `dispatchBaseHead`, `executionBaseHead`, and
`closureBaseHead` when applicable.

## Commit Mode Rules

`WORKER_MUST_NOT_COMMIT` work orders must include:

`## Reviewer Closure Conversion`

The section must include `completionReviewPath` and
`reviewerOwnedClosurePaths`.

`WORKER_MAY_COMMIT` work orders must still include the contract control block
when they carry handoff semantics, because single-agent/multi-role batches also
move across dispatch, execution, closure, and session-sync roles.

## C3 Rule

Three-or-more-agent or N-plus-agent chains must designate the closer before
dispatch. The closer is the actor who authors the completion review and commits
accepted material at CLOSURE phase.

## Cross-Batch Isolation Rule

Dispatch-ready handoff work orders must record clean worktree evidence in the
Agent Operation Trace Block's `Before status evidence` row. This is the
machine-checkable local view of CF-08 `crossBatchIsolation`.

## Machine Enforcement

Mandatory command:

```powershell
python governance/compat/check_agent_handoff_boundary.py --base <baseHead> --head HEAD --enforce
```

The guard runs in autorun and local hook chains. It checks changed handoff work
orders and AHB-T3 completion artifacts for missing contract control fields,
missing base-head anchors, missing reviewer closure conversion, missing C3
closer designation, missing clean-worktree evidence for dispatch-ready packets,
and missing AHB-T3 checker evidence.

## Central Core And Local View

The ratified contract is the Central Core. This standard and checker are stable
machine-enforced local views. Individual GC-018 baselines, work orders,
worker returns, completion reviews, trace blocks, and session-sync updates are
dated local evidence.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-T3 unified handoff-boundary checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reference/agent_handoff/README.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py` |
| Allowed scope source | operator authorization for AHB-T3 on 2026-06-17 |
| Before status evidence | HEAD `230565e4`; worktree clean |
| After status evidence | AHB-T3 material closure pending commit |
| Diff evidence | `git diff --name-status 230565e4..HEAD` |
| Approval boundary | bounded governance-control checker and stable standard |
| Claim boundary | no runtime/provider/live/public/workspace implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-t3-unified-handoff-boundary-checker-2026-06-17` |
| Expected manifest | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reference/agent_handoff/README.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py` |
| Actual changed set | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reference/agent_handoff/README.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance standard. No public-sync batch is
authorized.

## Claim Boundary

This standard machine-enforces handoff-boundary contract evidence for changed
governed artifacts. It does not prove runtime governance behavior, provider
behavior, public readiness, production readiness, or workspace isolation.
