# CVF GC-018 - GGL-T2 Git Hook Lane And Worktree Finality Reliability

Memory class: FULL_RECORD

Status: DISPATCHED

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `5077cea5`

## Purpose

Authorize a bounded governance-control-plane tranche that resolves the finding
left after GGL-T1 and Delta-T7 closure: the installed pre-commit hook still
forces serial execution even though the hook runner defaults latency-sensitive
hooks to parallel, and autorun pre-closure worktree finality can misclassify Git
stderr warnings as dirty-worktree output.

This tranche may make the hook lane use the existing bounded parallel hook
runner and may make pre-closure finality distinguish Git status stdout from
Git diagnostic stderr. It must not remove, skip, weaken, or path-filter any
required checker.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch bounded hook-lane and finality reliability optimization |
| Proposed tranche | GGL-T2 Git Hook Lane And Worktree Finality Reliability |
| Base head | `5077cea5` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Upstream closure | Delta-T7 `CLOSED_PASS_BOUNDED` at commit `d82870b9`; final session sync `5077cea5` |
| Finding source | GGL-T1/Delta-T7 closure observation that hook execution remains serial and Git stderr can be misclassified as dirty status |

## Scope / Target / Owner Boundary

Allowed scope:

- change the root pre-commit hook to use the existing local hook runner's
  parallel default for `pre-commit`;
- preserve an explicit serial debugging path in the hook runner CLI;
- change autorun worktree-finality status capture so dirty status comes only
  from `git status --short` stdout;
- report Git diagnostic stderr separately without treating warnings as dirty
  paths when `git status` exits successfully;
- add focused tests for the hook invocation and stderr-safe finality behavior;
- add completion review and evidence JSON.

Forbidden scope:

- no checker removal, path-based checker suppression, weakened fail condition,
  hook bypass, runtime execution profile, direct interception, provider/live
  call, secrets/quota use, public-sync, queue/daemon, or CVF Web action;
- no production, public, release, or universal governed-coding control claim;
- no broad rewrite of the hook chain or autorun manifest.

Risk ceiling: governance-control R1.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Installed pre-commit hook forces serial execution. | LITERAL_INVARIANT | canonical-contract: `.githooks/pre-commit` | line 7 command body | `pre-commit hook invocation` | local git hook | ACCEPT |
| Local hook runner already defaults `pre-commit`, `pre-push`, and `reviewer-fast` to parallel unless `--serial` is passed. | RUNTIME_BEHAVIOR | `governance/compat/run_local_governance_hook_chain.py` | `PARALLEL_BY_DEFAULT_HOOKS`; `main` | `PARALLEL_BY_DEFAULT_HOOKS`; `use_parallel` | local governance hook chain | ACCEPT |
| Local hook runner preserves explicit serial debugging behavior. | RUNTIME_BEHAVIOR | `governance/compat/run_local_governance_hook_chain.py` | `main` argument parsing | `--serial` | local governance hook chain | ACCEPT |
| Autorun worktree-finality helper currently merges Git stderr into stdout. | RUNTIME_BEHAVIOR | `governance/compat/run_agent_autorun_workflow_gate.py` | `_git_status_short` | `stderr` | autorun workflow gate | ACCEPT |
| Autorun pre-closure treats any non-empty `_git_status_short()` result as unclean worktree output. | RUNTIME_BEHAVIOR | `governance/compat/run_agent_autorun_workflow_gate.py` | `_run_phase` pre-closure finality block | `_git_status_short`; `closure worktree finality` | autorun workflow gate | ACCEPT |
| Autorun focused test module exists for function-level coverage. | EXISTS | `governance/compat/test_run_agent_autorun_workflow_gate.py` | module | `test_valid_receipt_requires_exact_context` | autorun focused tests | ACCEPT |
| Local hook runner focused test module exists and already verifies parallel defaults. | EXISTS | `governance/compat/test_run_local_governance_hook_chain.py` | module | `test_latency_sensitive_hooks_default_to_parallel` | local hook chain focused tests | ACCEPT |

## New Doc-Only Fields

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| `Hook Lane Reliability Control Block` | governed Markdown table | declare hook/finality safety boundary |
| `hookDefault` | pre-commit uses runner default | avoid duplicated serial latency |
| `stderrPolicy` | diagnostics reported separately from status stdout | prevent false dirty-worktree claims |

## Hook Lane Reliability Control Block

| Field | Disposition |
| --- | --- |
| hookDefault | installed pre-commit should call `--hook pre-commit` and rely on the runner default |
| serialEscapeHatch | `run_local_governance_hook_chain.py --hook pre-commit --serial` remains available for debugging |
| checkerCoverage | unchanged hook chain and unchanged command list |
| stderrPolicy | successful Git status stderr is diagnostic-only; dirty status comes from stdout |
| failurePolicy | non-zero Git status remains fail-closed for finality |
| claimBoundary | bounded local hook/finality reliability only |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | finding -> CVF-owned GC-018/work order -> guarded implementation -> evidence |
| Matching local-view guard | `.githooks/pre-commit`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Owner surface | GGL-T2 GC-018 and work order |
| Disposition | `DO_NOW` for bounded control-plane reliability optimization |
| Claim boundary | no runtime/provider/public/readiness or universal speed/control claim |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | The installed pre-commit hook no longer forces `--serial`; it uses the runner's existing default for `pre-commit`. |
| AC2 | Explicit serial debugging remains available through the hook runner CLI. |
| AC3 | Pre-closure finality treats dirty worktree evidence as Git status stdout only. |
| AC4 | Successful Git status stderr diagnostics are printed or surfaced separately but do not cause dirty-worktree failure. |
| AC5 | Non-zero Git status remains fail-closed. |
| AC6 | Focused tests cover hook invocation shape, parallel default preservation, stderr-only clean status, dirty stdout, and non-zero status failure. |
| AC7 | Existing hook command coverage and autorun checker coverage remain unchanged. |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | bounded local hook-lane and worktree-finality reliability |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: this tranche does not create execution-control receipts |
| actionEvidence | ACTION_EVIDENCE_PRESENT through focused tests and hook/gate command output |
| invocationBoundary | cooperating local hook and autorun invocation only |
| interceptionBoundary | no direct IDE, shell, git, filesystem, or provider interception beyond existing hooks |
| claimLanguage | bounded local reliability optimization; no universal speed or governed-coding claim |
| forbiddenExpansion | runtime profiles, provider/live, public-sync, EDIT/COMMIT, queues, daemons, and direct interception remain parked |

## Evidence / Verification

Required evidence: focused tests, hook command diff, finality helper tests,
worker-return fast gate, implementation steward, pre-commit hook proof, and
committed-range pre-closure proof. Provider/live and public-sync evidence are
not applicable because both are forbidden.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance control-plane reliability optimization.
Public-sync is not authorized.

## Claim Boundary

GGL-T2 may prove only bounded local hook-lane latency reliability and
stderr-safe closure finality with unchanged checker coverage. It does not prove
runtime execution governance, provider behavior, public readiness, production
readiness, release readiness, universal speedup, or universal governed-coding
control.
