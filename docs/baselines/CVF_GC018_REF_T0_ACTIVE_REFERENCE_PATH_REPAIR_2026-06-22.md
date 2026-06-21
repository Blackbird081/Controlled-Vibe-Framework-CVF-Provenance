# CVF GC-018 - REF-T0 Active Reference Path Repair

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: baseline

dispatchBaseHead: 938cfb2d

Batch ID: REF-T0

## Purpose

Authorize a bounded reference-lifecycle repair before AAF-T6A. Some active
CVF authority surfaces name reference standards at active
`docs/reference/...` paths while the files currently exist only under
`docs/reference/archive/`. If a file is still binding enough to be cited by
AGENTS or generated active session state, REF-T0 restores an active copy rather
than treating the missing active path as a harmless dispatch note.

This is the first small cleanup after L2A-T0 closure and before AAF-T6A early
diagnostic wire-in.

## Operator Authorization

The operator approved repairing important active reference path drift before
AAF-T6A, stating that if an important file is referenced as active but is under
archive, the classification is wrong and the file should be restored to active
state rather than merely avoided in source verification.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 active reference path repair before AAF-T6A | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Root agent instructions | `AGENTS.md` | ACCEPT |
| Archive source files | `docs/reference/archive/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`; `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |

Provider-specific memory is not CVF authority. The dispatch is based on
repo-local active surfaces and archive source files.

## Scope / Owner Boundary

Allowed worker scope:

- create active copy `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` from its archive source;
- create active copy `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` from its archive source;
- update `docs/reference/learning_to_acceleration/README.md` to point at the
  restored active learning-philosophy path instead of the archive path;
- create `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_WORKER_RETURN_2026-06-22.md`;
- preserve the archive copies; do not delete, move, or rewrite historical
  archive records.

Reviewer/closer closure scope:

- update this GC-018 status and paired work order status;
- create `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md`;
- repair allowed-scope reference wording, manifests, or packet-shape defects
  required by machine gates before commit.

Forbidden worker scope:

- no edits to `AGENTS.md`, `CVF_SESSION/**`, active handoff, archive index,
  governance/compat, runtime/provider routes, web, MCP, dependency manifests,
  generated aggregates, public-sync, queue, daemon, watcher, wrapper/proxy,
  direct IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no semantic rewrite of the restored standards beyond preserving their current
  archive content as active reference copies;
- no AAF-T6A, AAF-T7A, MPI-T3/MPI-T4, checker/helper/scaffold/patch behavior,
  provider/live proof, public-sync, readiness, speed/cost, or universal
  governed-coding-control claim.

Risk ceiling: R0/R1 reference lifecycle repair only.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed or created:

- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/learning_to_acceleration/README.md`
- `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_WORKER_RETURN_2026-06-22.md`

No commit is authorized for the worker.

## Decision / Baseline / Proposed Tranche

Baseline decision: REF-T0 is ready for worker dispatch as a narrow active
reference path repair.

Proposed tranche: `REF-T0 Active Reference Path Repair`.

Tranche owner split: dispatcher creates this GC-018 baseline and paired work
order; worker restores active reference copies and updates the L2A pointer
without committing; reviewer/closer reviews and commits accepted material if
gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AGENTS names the autorun workflow standard at active reference path | `AGENTS.md` | Mandatory Agent Autorun Workflow Control section | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | root agent instructions | ACCEPT |
| AGENTS names the agent-error learning philosophy at active reference path | `AGENTS.md` | Mandatory Agent Autorun Workflow Control section | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | root agent instructions | ACCEPT |
| Active state names the agent-error learning philosophy at active path | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `agentErrorToGovernanceLearningPhilosophy` | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | active session state registry | ACCEPT |
| Autorun archive source exists | `docs/reference/archive/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | file existence and title | `CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | archive reference source | ACCEPT |
| Learning philosophy archive source exists | `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | file existence and title | `CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | archive reference source | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in REF-T0 | Runtime status | Reason |
|---|---|---|---|
| `Active Reference Path Repair` | REF-T0 baseline/work order | DOC_ONLY_NEW | names a bounded reference lifecycle cleanup where active authority paths are restored from archived sources |

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `938cfb2d`.
- `git status --short` was clean before REF-T0 dispatch authoring.
- `Test-Path` verified both active paths are missing and both archive sources
  exist.
- `rg -n` verified AGENTS and active session state cite the active paths.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 938cfb2d --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 938cfb2d --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 938cfb2d --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 938cfb2d --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator critique about active/archive misclassification to governed reference repair |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; reviewer-fast gate |
| Owner surface | REF-T0 active reference path repair |
| Disposition | ADAPT as CVF-owned reference lifecycle repair |
| Claim boundary | operator/external critique remains input only until promoted through this governed dispatch |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: REF-T0 repairs documentation/reference file placement only |
| Runtime behavior claimed | N/A_WITH_REASON |
| Helper/checker implementation claimed | N/A_WITH_REASON |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no runtime, provider, helper/checker, public-sync, generated aggregate, or provider registry behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | REF-T0 dispatch and active reference path repair only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed documentation/reference lifecycle repair only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | active reference path repair only |
| forbiddenExpansion | checker/helper/scaffold implementation, patch application, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Active authority paths can drift into archive-only storage | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | REF-T0 restores active copies for binding references | handled by this dispatch |
| Future INDEX/lifecycle enforcement may need a checker for active path drift | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | consider a later checker after REF-T0 if the pattern recurs | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: operator critique about active files incorrectly
  living in archive.
- Predecessor intake artifact: L2A-T0 closure and current active startup
  surfaces.
- Delta ledger status: `CHANGED_DISPOSITION` because a dispatch note becomes a
  repair work order before AAF-T6A.
- Routing matrix status: `DO_NOW` for REF-T0; `DEFER` for AAF-T6A until REF-T0
  closure; `SEPARATE_RUNTIME_TRANCHE` for any checker/helper implementation.
- Semantic sampling status: sampled AGENTS, ACTIVE_SESSION_STATE, archive
  source files, and L2A README pointer.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | The two standards remain binding reference concepts. |
| CHANGED_DISPOSITION | Archive-only placement is treated as active reference drift to repair. |
| NEW_FINDING | Active-path references need filesystem-backed existence before future dispatches cite them. |
| REMOVED_OR_REJECTED | Deleting archive copies, rewriting semantics, and checker/helper implementation remain rejected. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Restore active copies for the two binding standards and update L2A pointer. |
| RESOLVED_BY_DESIGN | Preserve archive copies as historical records; create active copies for active authority paths. |
| DEFER | AAF-T6A early diagnostic wire-in remains deferred until `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md` records a reviewer disposition. |
| STRATEGIC_OPERATOR_DECISION | Operator decides once `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md` exists whether to proceed to AAF-T6A immediately or inspect additional active/archive drift first. |
| SEPARATE_RUNTIME_TRANCHE | checker/helper/scaffold/patch/apply/runtime/provider/public-sync behavior. |
| OUT_OF_SCOPE | public-sync, provider/live proof, direct interception, universal control, MPI continuation during REF-T0. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| REF-T0-RS1 | AGENTS autorun section | active standard paths are canonical | DO_NOW | Should worker only cite archive path? | PASS - active copy should be restored |
| REF-T0-RS2 | archive source files | archived standards still exist | DO_NOW | Should archive files be moved/deleted? | PASS - preserve archive and create active copy |
| REF-T0-RS3 | L2A README related surface | pointer currently uses archive path | DO_NOW | Should closed L2A be left stale? | PASS - narrow pointer update is allowed |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for bounded active reference path repair.
- Corpus root: repo-local files named in Authority Chain and Source Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted `rg -n` and `Test-Path` checks.
- Manifest artifact or inline manifest: Authority Chain and Source Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan, semantic rewrite, generated registry mutation, runtime/provider/web/MCP/public-sync corpus scan; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no full `.private_reference/legacy` scan, no runtime/provider/web/MCP/public-sync corpus scan, no archive deletion.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: REF-T0 baseline maps operator finding to worker deliverables.
- Adversarial verification: active missing/archive exists condition was checked before dispatch.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: REF-T0 is private provenance reference-lifecycle repair work. No
public-sync repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local Codex session |
| Session or invocation | REF-T0 dispatch authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, `rg`, `Test-Path`, apply_patch, governance gates |
| Target paths | this GC-018 baseline and paired REF-T0 work order |
| Allowed scope source | operator instruction to repair active reference path drift before AAF-T6A |
| Before status evidence | HEAD `938cfb2d`; clean worktree before dispatch authoring |
| After status evidence | REF-T0 dispatch artifacts pending pre-dispatch gates and commit |
| Diff evidence | dispatch diff and gate receipts |
| Approval boundary | dispatch only; worker implementation remains no-commit |
| Claim boundary | reference lifecycle repair dispatch only; no helper/checker/runtime implementation |
| Agent type | dispatcher |
| Invocation ID | `ref-t0-active-reference-path-repair-dispatch-2026-06-22` |
| Expected manifest | this baseline; paired REF-T0 work order |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH_PENDING_COMMIT |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker creates active copies of both binding archive-only standards. |
| AC2 | Worker preserves archive copies without deletion or semantic rewrite. |
| AC3 | L2A README points to restored active learning-philosophy path. |
| AC4 | No AGENTS/session/handoff/governance/compat/runtime/public/provider/generated path is edited by worker. |
| AC5 | Worker return records actual base, status, source inventory, gates, and claim boundary. |

## Claim Boundary

REF-T0 authorizes only bounded active reference path repair. It does not
authorize semantic standard rewrites, archive deletion, checker/helper/scaffold
implementation, patch preview/apply behavior, autorun/hook wiring, runtime
behavior, provider/live behavior, CLI/MCP adapter behavior, public-sync,
session-sync by worker, direct interception, readiness claims, speed/cost
claims, or universal governed-coding control.
