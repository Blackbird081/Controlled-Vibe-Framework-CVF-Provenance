# CVF Agent Work Order FPC-SCG-T8 Foundation System-Chain Acceptance Ledger Provenance Carrier Reconciliation For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: agent_work_order

Date: 2026-06-27

Owner: Codex

rawMemoryReleased: false

## Purpose

Execute FPC-SCG-T8 by reconciling the T7 acceptance ledger's material carrier
rows with the current provenance rebuild carrier and by hardening the local
ledger checker against stale carrier evidence.

## Target / Reviewed Source

Baseline:
`docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md`.

Target outputs:

- `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json`
- `governance/compat/check_fpc_system_chain_acceptance_ledger.py`
- `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py`
- `docs/reviews/CVF_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_COMPLETION_2026-06-27.md`
- updated FPC guidance

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | current chat instruction: agreement to T8 recommendation | ACCEPT |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V24_2026-06-27.md` | ACCEPT |
| This GC-018 baseline | `docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md` | ACCEPT |

## Agent Roles

| Role | Owner | Commit boundary |
|---|---|---|
| Dispatcher | Codex | may author T8 baseline/work order |
| Worker | Codex | may implement because this is single-agent `WORKER_MAY_COMMIT` scope |
| Reviewer/closer | Codex | must run gates and commit material only |
| Session-sync steward | Codex | must update session surfaces in a separate commit after material closure |

## Required First Reads

| Path | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V24_2026-06-27.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | SOURCE_VERIFIED |

## Scope / Methodology

Update the T7 ledger and its checker so the accepted closure chain reflects
current provenance carrier evidence after the rebuild. Preserve downstream
parking and avoid any runtime/provider/public/MPI-T6 implementation.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Reconcile T7 ledger carrier rows | `materialCommit` rows match active handoff/front-door carrier evidence |
| 2 | Harden checker | `EXPECTED_MATERIAL_COMMITS` validates required current carrier rows |
| 3 | Add focused test | stale carrier fixture fails validation |
| 4 | Update FPC guidance | T8 closure and next decision boundary recorded |
| 5 | Run focused and governance gates | command output before commit |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Worktree status | `git status --short --branch` | clean before material patch |
| Base head | `git rev-parse --short HEAD` | `1f229fc6` |
| ADIF query | `python - <<resolver import call>>` with taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch` | `ADIF-0001`, `ADIF-0002`, `ADIF-0006`, `ADIF-0007` |

## Write Ownership

Allowed material paths are exactly the T8 baseline/work order/completion, the
T7 ledger JSON, the T7 checker, the T7 focused test file, and FPC guidance.
Active session state, active handoff, and front-door files are reserved for a
later session-sync commit.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| current material carrier for FPC-SCG-T2 through FPC-UAP-T2 is `be253923` | `AGENT_HANDOFF_V24_2026-06-27.md` | `Provenance Push Debt Rebuild Sync - 2026-06-27` | `Current provenance material carrier` | active handoff | VALUE_SET | ACCEPT |
| pre-rebuild material SHAs must not be current remote ancestry evidence | `AGENT_HANDOFF_V24_2026-06-27.md` | `Provenance Push Debt Rebuild Sync - 2026-06-27` | `backup-history references only` | active handoff | LITERAL_INVARIANT | ACCEPT |
| front door records FPC-SCG-T2 through FPC-SCG-T7 as closed at `be253923` | `CVF_SESSION_MEMORY.md` | `Latest Closed Work` and `Parked Checkpoint` | `FPC-SCG-T2`; `FPC-SCG-T7`; `be253923` | active session front door | VALUE_SET | ACCEPT |
| T7 ledger has required closure rows with `materialCommit` | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `acceptedClosureChain` | `materialCommit` | T7 ledger schema | EXISTS | ACCEPT |
| T7 checker validates required closure fields | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | `REQUIRED_CLOSURE_FIELDS` | `materialCommit` | T7 checker | VALUE_SET | ACCEPT |
| T8 checker hardening is local governance validation only | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | new edit in this tranche | `EXPECTED_MATERIAL_COMMITS` | T7 checker | DOC_ONLY_NEW | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Agent Handoff Contract Control Block

Contract source:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Commit mode: WORKER_MAY_COMMIT
dispatchBaseHead: 1f229fc6
executionBaseHead: 1f229fc6
closureBaseHead: 1f229fc6

| Field | Disposition |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | single-agent dispatcher/implementer/reviewer/closer |
| phase | DISPATCH_AUTHORING; EXECUTION; REVIEW; CLOSURE |
| baseHeadFor(phase) | `dispatchBaseHead=1f229fc6`; `executionBaseHead=1f229fc6`; `closureBaseHead=1f229fc6` |
| changedSetScope(phase) | material T8 ledger/checker/test/docs only; session-sync follows separately |
| traceScope(phase, actor) | Agent Operation Trace Block required in work order and completion review for Codex |
| commitOwner(phase) | Codex owns material commit; Codex owns later session-sync commit |
| crossBatchIsolation | material and session-sync ranges must be split |
| nextMoveSurfaces | active handoff/front-door/state updated only after material commit |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Storage class | dated reference evidence ledger plus dated guidance update |
| Index/front door | N/A with reason: no stable folder front door or index relocation is authorized by this tranche |
| Date policy | dated paths retained for GC-018, work order, completion review, JSON ledger, and guidance evidence |
| Archive disposition | N/A with reason: no historical file movement authorized |
| Deferred layout work | N/A with reason: T8 reconciles bounded evidence only; no storage refactor is opened |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T7 ledger and checker | internal agents may verify bounded foundation acceptance against current provenance carrier evidence before downstream selection | ledger JSON, checker, tests, completion review | N/A with reason: internal provenance governance only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP interface authorized | no external read/write/runtime authority is added | forbidden scope and public export disposition | deferred adapter owner; fresh source-verified authorization required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

Chain map citation:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: this tranche absorbs no new external knowledge item; the section is present because external-agent boundary terms appear in the artifact |
| Matching local-view guard | N/A with reason: no external knowledge intake item is promoted or absorbed |
| Owner surface | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_FOR_CODEX_2026-06-27.md` |
| Disposition | N/A_WITH_REASON: no external input is used as source authority |
| Claim boundary | CVF-governed source files remain the only source authority for this tranche |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | T7 ledger carrier rows are reconciled | PASS |
| AC2 | checker detects stale pre-rebuild carrier SHAs | PASS |
| AC3 | focused tests cover stale carrier detection | PASS |
| AC4 | downstream lanes remain parked | PASS |
| AC5 | material commit excludes session-state mutation | PASS |

## Evidence Requirements

| Evidence | Required command or artifact | Required disposition |
|---|---|---|
| Ledger validation | `python governance/compat/check_fpc_system_chain_acceptance_ledger.py --enforce` | PASS |
| Focused regression tests | `python -m pytest governance/compat/test_check_fpc_system_chain_acceptance_ledger.py -q` | PASS |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1f229fc6 --head HEAD --serial` | PASS |
| Commit steward | `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 1f229fc6 --head HEAD --enforce` | PASS |

## Review Gate

Reviewer/closer must verify the actual changed set against the Agent Operation
Trace Block and run commit steward preflight before material commit.

## Closure Checklist

| Item | Status |
|---|---|
| T7 ledger reconciled | PASS |
| T7 checker hardened | PASS |
| Focused stale carrier test present | PASS |
| Downstream gates remain parked | PASS |
| Session-sync left for separate commit | PASS |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if the checker fails, if T7 ledger carrier rows
cannot be reconciled from source-backed current state, or if any gate requires
runtime/provider/public/MPI-T6 implementation.

## Operator Checkpoint

No additional checkpoint is required to close T8 because the approved T8 scope
is bounded to acceptance-ledger provenance-carrier reconciliation. Any
downstream runtime/use-case/provider/public/MPI-T6 lane requires a fresh
source-verified GC-018 and recorded reopen condition before it can open.

## Risk / Corrective Action

| Risk | Corrective action | Final status |
|---|---|---|
| T7 ledger points to backup-history SHAs as current evidence | reconcile material carrier rows to current provenance carrier | CONTAINED |
| stale carrier reappears later | checker rejects unexpected materialCommit values | CONTAINED |
| downstream lane opens implicitly | preserve T7 parked gates and claim boundary | CONTAINED |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Ledger checker | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | `EXPECTED_MATERIAL_COMMITS` | PASS |
| Focused test | `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py` | pytest pass required before commit | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T8 recorded as completed bounded reconciliation | PASS |
| Registry JSON | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | carrier rows reconciled | PASS |
| Registry Markdown | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T8 reconciliation recorded in guidance | PASS |
| External evidence digest | N/A with reason: no external knowledge input or external evidence digest is consumed by T8 | no external source promoted | N/A with reason |
| System loop interlock | `python governance/compat/check_system_loop_interlock.py --base 1f229fc6 --head HEAD --enforce` | PASS required before commit | PASS |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 FPC-SCG-T8 work order execution |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, source reads, apply_patch, Python, pytest, governance gates |
| Target paths | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json`; `governance/compat/check_fpc_system_chain_acceptance_ledger.py`; `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py`; `docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_COMPLETION_2026-06-27.md`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Allowed scope source | approved T8 roadmap direction after UAP-T2 closure |
| Before status evidence | `git rev-parse --short HEAD` = `1f229fc6`; `git status --short --branch` clean |
| After status evidence | T8 ledger/checker/test/docs authored; gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded acceptance ledger provenance-carrier reconciliation only |
| Claim boundary | local governance evidence reconciliation only; no runtime/provider/live/public/use-case/MPI-T6 implementation or readiness claim |
| Agent type | single-agent dispatcher/implementer/reviewer |
| Invocation ID | `fpc-scg-t8-foundation-system-chain-acceptance-ledger-provenance-carrier-reconciliation-2026-06-27` |
| Expected manifest | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json`; `governance/compat/check_fpc_system_chain_acceptance_ledger.py`; `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py`; `docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_COMPLETION_2026-06-27.md`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Actual changed set | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json`; `governance/compat/check_fpc_system_chain_acceptance_ledger.py`; `governance/compat/test_check_fpc_system_chain_acceptance_ledger.py`; `docs/baselines/CVF_GC018_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T8_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_PROVENANCE_CARRIER_RECONCILIATION_COMPLETION_2026-06-27.md`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance evidence reconciliation. Public-sync is
not authorized.

## Claim Boundary

This work order closes only T8 acceptance-ledger carrier reconciliation. It
does not open runtime/provider/public/use-case/MPI-T6 implementation or certify
downstream readiness.
