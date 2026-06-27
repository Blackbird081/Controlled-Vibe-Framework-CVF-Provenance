# CVF GC-018 - Delta-T4B Mutating Profile Boundary Guard

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `bbb84de0`

## Purpose

Authorize a bounded governance-control tranche after Delta-T4A closure.
Delta-T4B promotes the Delta-T4A learning into an early machine guard: future
mutating-profile, EDIT, COMMIT, or approval-backed mutation artifacts must
declare fixed target policy, approval evidence source, caller path-input
boundary, command authority, receipt chain, and claim boundary before they can
be dispatched or closed.

This tranche does not authorize new runtime mutation, new execution profiles,
provider/live calls, public-sync, direct IDE/shell/git/filesystem
interception, queues, daemons, or universal governed-coding claims.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch a bounded machine guard for future Delta mutating-profile artifacts |
| Proposed tranche | Delta-T4B Mutating Profile Boundary Guard |
| Base head | `bbb84de0` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Upstream evidence | Delta-T4A completion review and active session continuity |
| Later tranche | EDIT/COMMIT profiles, arbitrary mutating commands, hosted approval service, direct interception, and mandatory governed-coding control remain separate authorization |

## Scope / Target / Owner Boundary

Allowed scope:

- add one range-aware governance checker for changed governed Markdown artifacts;
- trigger only when a changed artifact explicitly concerns mutating profiles,
  approval-backed mutation, EDIT profile, COMMIT profile, or governed mutation
  boundary;
- require a `Delta Mutating Profile Boundary Control Block` with non-empty rows;
- add focused tests for valid block, missing block, missing field, no-caller-path
  evidence, and unrelated-doc non-applicability;
- wire the checker into reviewer-fast, pre-commit, pre-push, and autorun common
  gates;
- add completion review and evidence JSON.

Forbidden scope:

- no MCP/runtime source mutation except governance checker code;
- no new Delta execution profile, no CLI behavior change, no approval policy
  runtime change, and no marker-write behavior change;
- no provider/live proof, public-sync, queue, daemon, CVF Web action execution,
  external repo import, broad legacy scan, or readiness claim;
- no claim that this guard intercepts direct IDE, shell, git, filesystem, or
  agent tool actions.

Risk ceiling: governance-control R1. The guard is repo-local, range-aware, and
forward-only.

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | `MACHINE_GUARD_ONLY`: no new runtime profile |
| fixedTargetPolicy | future applicable artifacts must state fixed target or `N/A with reason` |
| approvalEvidenceSource | future applicable artifacts must state approval evidence source or `N/A with reason` |
| callerPathInput | future applicable artifacts must state `NO_CALLER_PATH_INPUT`, `CALLER_PATH_INPUT_FORBIDDEN`, or `N/A with reason` |
| commandAuthority | future applicable artifacts must state static profile/command authority or `N/A with reason` |
| receiptChain | future applicable artifacts must state T1/T2/T3/T4-style receipt chain or `N/A with reason` |
| claimBoundary | future applicable artifacts must reject universal governed-coding and direct interception claims unless separately authorized |
| forbiddenExpansion | this tranche forbids new runtime profiles, EDIT/COMMIT execution, arbitrary commands, provider/live, public-sync, queue, daemon, and direct interception |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T4A recorded a future machine-check candidate for mutating profiles to declare fixed target, approval evidence source, and no caller path input. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | line 118 | `Machine-check action` | Delta-T4A Finding-To-Governance Learning Disposition | ACCEPT |
| Delta-T4A kept arbitrary, EDIT, COMMIT, and external interception scope parked. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | line 120 | `Next action` | Delta-T4A Finding-To-Governance Learning Disposition | ACCEPT |
| Local hook chain contains reviewer-fast, pre-commit, and pre-push checker registration lanes. | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 24, 143, 151, and 368 | `REVIEWER_FAST_CHECKS`; `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| Autorun common commands are the correct owner for a range-aware governance checker. | EXISTS | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 52 and 399 | `_common_commands` | autorun workflow gate | ACCEPT |
| Existing EKA-R1 checker provides the range-aware changed-governed-Markdown pattern. | EXISTS | `governance/compat/check_external_knowledge_intake_routing.py` | module `CVF external knowledge intake routing guard` | `_get_changed_paths`; `check_text`; `main` | EKA-R1 checker | ACCEPT |

## New Doc-Only Fields

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| `Delta Mutating Profile Boundary Control Block` | governed Markdown section with required row labels | future mutating-profile artifact declaration |
| `profileScope` | non-empty row | state whether artifact opens runtime profile or guard-only scope |
| `fixedTargetPolicy` | non-empty row | prevent silent caller-selected mutation target |
| `approvalEvidenceSource` | non-empty row | bind approval claim to durable evidence source or N/A reason |
| `callerPathInput` | `NO_CALLER_PATH_INPUT`, `CALLER_PATH_INPUT_FORBIDDEN`, or `N/A with reason` | make path-input boundary explicit |
| `commandAuthority` | non-empty row | identify static profile/command owner |
| `receiptChain` | non-empty row | identify durable admission/evidence chain |
| `claimBoundary` | non-empty row | keep direct interception and universal enforcement claims bounded |
| `forbiddenExpansion` | non-empty row | state parked expansion classes |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | Runtime/MCP claim must cite current proof, work-order source verification, and local-view guard before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; this proposed Delta-T4B guard |
| Owner surface | Delta-T4B GC-018 and work order |
| Disposition | `DO_NOW` for guard-only machine enforcement; `BLOCKED_UNTIL_CVF_PROOF` for runtime mutation expansion |
| Claim boundary | no runtime/provider/live/public-sync/direct interception/universal governed-coding control claim |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | A new checker fails applicable changed governed Markdown artifacts that omit the Delta mutating-profile control block. |
| AC2 | The checker requires all control-block rows to be non-empty. |
| AC3 | The checker rejects caller path-input rows unless they say `NO_CALLER_PATH_INPUT`, `CALLER_PATH_INPUT_FORBIDDEN`, or `N/A with reason`. |
| AC4 | The checker ignores unrelated governed Markdown artifacts. |
| AC5 | Focused tests cover positive, negative, and non-applicable cases. |
| AC6 | The checker is wired into reviewer-fast, pre-commit, pre-push, and autorun common gates. |
| AC7 | Completion evidence records no runtime/provider/live/public/direct-interception claim. |

## Evidence / Verification

Required evidence:

- focused unittest or pytest for the new checker;
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target <new-test>`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <implementationBaseHead> --head HEAD`;
- commit-steward preflight for implementation and closure;
- exact changed-set evidence and completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance guard. Public-sync is not authorized.

## Claim Boundary

Delta-T4B may prove only that changed governed artifacts about future mutating
profiles must carry a bounded control block. It does not prove runtime
interception, mandatory wrapper use, provider behavior, hosted readiness, public
readiness, production readiness, or universal governed-coding control.
