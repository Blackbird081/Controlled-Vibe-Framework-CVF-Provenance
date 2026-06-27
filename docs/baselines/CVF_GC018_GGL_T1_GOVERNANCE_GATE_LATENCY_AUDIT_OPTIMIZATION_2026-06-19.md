# CVF GC-018 - GGL-T1 Governance Gate Latency Audit And Optimization

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `e5dc8d7d`

## Purpose

Authorize a bounded governance-control-plane optimization after Delta-T6 exposed
systematic gate amplification. The current flow can run the same autorun phase
once directly and again through commit steward, while autorun executes its
common command bundle serially. GGL-T1 may add fail-closed receipt reuse for an
identical gate context, parallel execution for independent common checks, and
duration evidence. It must not remove, skip, weaken, or path-filter any required
checker.

The next tranche selected by a recorded GGL-T1 `CLOSED_PASS_BOUNDED` result is
the receipt-to-execution evidence auditor.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch bounded latency audit and orchestration optimization |
| Proposed tranche | GGL-T1 Governance Gate Latency Audit And Optimization |
| Base head | `e5dc8d7d` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Runtime receipt location | `.cvf/runtime/autorun-receipts/`; ignored, local, non-canonical |
| Later tranche | Receipt-to-execution evidence auditor, released only by a recorded GGL-T1 `CLOSED_PASS_BOUNDED` artifact |

## Scope / Target / Owner Boundary

Allowed scope:

- measure and record current gate topology and duplication;
- run independent autorun common checks concurrently with bounded workers;
- emit per-check duration and total-duration evidence;
- write a local ignored PASS receipt after a complete successful autorun;
- let commit steward reuse only an exact valid receipt for the same phase,
  resolved base/head, command manifest, and worktree fingerprint;
- fail closed and run the full autorun phase when receipt validation fails;
- add focused tests and update the canonical commit steward standard;
- add completion review and evidence JSON.

Forbidden scope:

- no checker removal, path-based checker suppression, weakened fail condition,
  pre-commit/pre-push bypass, provider/live call, secrets/quota use, public-sync,
  runtime execution profile, direct interception, queue/daemon, or CVF Web action;
- no committed receipt or claim that timing from one machine predicts all hosts;
- no edit to `AGENTS.md` in this tranche because it is above its advisory size
  threshold and the optimization can be implemented without expanding it.

Risk ceiling: governance-control R1.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Autorun owns 43 common commands and currently executes the command list serially. | RUNTIME_BEHAVIOR | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands`; command loop near line 448 | `_common_commands`; `_run_phase` | autorun workflow gate | ACCEPT |
| Commit steward phase modes invoke autorun as their first phase command. | RUNTIME_BEHAVIOR | `governance/compat/run_agent_commit_steward_preflight.py` | `_mode_commands`, lines 186-207 | `_mode_commands` | commit steward preflight | ACCEPT |
| Local reviewer-fast, pre-commit, and pre-push hooks already use bounded parallel execution. | RUNTIME_BEHAVIOR | `governance/compat/run_local_governance_hook_chain.py` | `PARALLEL_BY_DEFAULT_HOOKS`; `_run_parallel_chain` | `PARALLEL_BY_DEFAULT_HOOKS`; `_run_parallel_chain` | local governance hook chain | ACCEPT |
| Commit steward latency discipline says to run only the gate set matching the phase. | LITERAL_INVARIANT | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | `## Latency Discipline` | `Latency Discipline` | commit steward standard | ACCEPT |
| `.cvf/runtime/` is ignored and suitable for local non-canonical receipts. | LITERAL_INVARIANT | `.gitignore` | line 49 | `.cvf/runtime/` | repository ignore policy | ACCEPT |
| Existing autorun tests use direct function-level pytest coverage. | EXISTS | `governance/compat/test_run_agent_autorun_workflow_gate.py` | current test module | `test_range_shape_preflight_*` | autorun focused tests | ACCEPT |
| Existing steward tests verify phase command construction. | EXISTS | `governance/compat/test_run_agent_commit_steward_preflight.py` | `test_session_sync_commands_include_closure_packaging_preflight` | `_mode_commands` | commit steward focused tests | ACCEPT |

## New Doc-Only Fields

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| `Gate Latency Control Block` | governed Markdown table | declare optimization safety boundary |
| `receiptScope` | local ignored PASS receipt only | prevent canonical-evidence confusion |
| `reuseKey` | phase + resolved refs + command manifest + worktree fingerprint | exact reuse boundary |
| `fallbackPolicy` | full autorun on any mismatch | fail-closed behavior |
| `parallelPolicy` | bounded workers, independent common checks only | concurrency boundary |

## Gate Latency Control Block

| Field | Disposition |
| --- | --- |
| baseline | 31 reviewer-fast, 54 pre-commit, 76 pre-push, and 43 autorun common command slots at base `e5dc8d7d` |
| receiptScope | local ignored optimization receipt; not closure or governance authority |
| reuseKey | exact phase, resolved base/head, command manifest, and worktree fingerprint |
| fallbackPolicy | missing, malformed, stale, mismatched, or failed receipt triggers full autorun |
| parallelPolicy | bounded concurrency for complete independent common command set; failures remain blocking |
| checkerCoverage | unchanged; no checker removal or path filtering authorized |
| claimBoundary | lower orchestration duplication and wall time only; no universal performance claim |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | promote repeated agent/workflow latency finding into CVF-owned rule, implementation, tests, and evidence |
| Matching local-view guard | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Owner surface | GGL-T1 GC-018 and work order |
| Disposition | `DO_NOW` for bounded control-plane optimization |
| Claim boundary | no runtime/provider/public/readiness or universal speed claim |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Autorun executes the complete common command manifest with bounded parallel workers by default and supports serial debugging. |
| AC2 | Autorun reports per-command and total duration. |
| AC3 | Successful autorun writes a local ignored receipt with exact validation inputs. |
| AC4 | Commit steward requests receipt reuse for matching phase execution. |
| AC5 | Any receipt mismatch runs the full autorun command set instead of passing from cache. |
| AC6 | Focused tests cover exact reuse, stale worktree, command-manifest mismatch, malformed receipt, parallel failure, and serial mode. |
| AC7 | Existing range-shape, clean-worktree, hook, and blocking semantics remain intact. |
| AC8 | Completion evidence sets receipt-to-execution evidence auditor as the next allowed move. |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | bounded local gate-orchestration optimization |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT only as a local ignored optimization receipt validated by focused tests |
| actionEvidence | ACTION_EVIDENCE_PRESENT in focused serial, parallel, and mismatch test output |
| invocationBoundary | cooperating local autorun and commit steward invocation only |
| interceptionBoundary | no direct IDE, shell, git, filesystem, or provider interception |
| claimLanguage | bounded local latency optimization; no universal speed or governed-coding claim |
| forbiddenExpansion | runtime profiles, provider/live, public-sync, EDIT/COMMIT, queues, daemons, and direct interception remain parked |

## Evidence / Verification

Required evidence: focused tests, complete command-manifest comparison,
serial/parallel blocking behavior, exact receipt reuse and mismatch fallback,
per-command timing, committed diff/status, worker-return gate, and committed-
range closure gates. Provider/live and public-sync evidence are not applicable
because both are forbidden.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance orchestration optimization. Public-sync
is not authorized.

## Claim Boundary

GGL-T1 may prove only bounded local orchestration optimization with unchanged
checker coverage and fail-closed receipt reuse. It does not prove identical
speedups on every host, runtime execution governance, provider behavior,
public readiness, production readiness, or universal governed-coding control.
