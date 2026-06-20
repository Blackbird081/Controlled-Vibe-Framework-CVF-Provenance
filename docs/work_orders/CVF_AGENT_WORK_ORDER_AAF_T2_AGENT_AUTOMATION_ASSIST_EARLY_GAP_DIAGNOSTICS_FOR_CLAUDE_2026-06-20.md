# CVF Agent Work Order - AAF-T2 Agent Automation Assist Early Gap Diagnostics

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: work_order

dispatchBaseHead: 31b7ef35

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Implementer/worker (Claude). Codex is reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_FOR_CLAUDE_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T2 is a bounded follow-up to AAF-T1. AAF-T1 improved
CVF lane selection and worker-return guidance, but a late full-hook failure
still appeared when a worker-return packet had an incomplete Corpus Completeness
And Report Integrity block. AAF-T2 moves that known defect class into the
read-only helper's early diagnostics and adds drift coverage for helper mirrors.

Do-not-misread notes: do not open runtime execution, MCP wiring, provider/live
proof, public-sync, wrapper/proxy enforcement, direct IDE/shell/git/filesystem
interception, arbitrary command execution, queue/daemon, watcher, background
service, AAF-T3, or universal control. The helper remains read-only and
advisory, with `--enforce` failing only on local helper-detectable defects.

Required first actions: read this work order, read the AAF-T2 GC-018 baseline,
read the source files named in the Source Verification Block, confirm actual
`executionBaseHead`, and inspect current `git status --short` before editing.

Return contract: return `COMPLETE_PENDING_REVIEW` with exactly the three
uncommitted artifacts named in Required Deliverables, actual `executionBaseHead`,
actual `git status --short`, focused test result, worker-return fast gate result,
and no commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact source
or gate that blocked the work.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two agents, one role each: Claude implements helper/test/worker-return; Codex reviews/closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=31b7ef35`; `executionBaseHead` confirmed by Claude; `closureBaseHead` set by Codex before closure commit |
| changedSetScope(phase) | worker changes only the three required artifacts; Codex owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one Claude worker-return trace covers pending helper/test/worker-return; one Codex trace covers review/closure if accepted |
| commitOwner(phase) | Claude commits nothing (`WORKER_MUST_NOT_COMMIT`); Codex owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T2 with CGE-T3 absorption, runtime, public-sync, provider/live, MCP, AAF-T3, or direct-interception work |
| Before status evidence | clean worktree at dispatch base `31b7ef35`, except recurring Windows global git-ignore permission warning |
| nextMoveSurfaces | Codex updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | Codex is the designated reviewer and closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md`
- session front-door/state/handoff paths only if Codex changes current mode or
  next allowed move after accepting the worker return.

Claude must not create the completion review and must not mark the work closed.

## Purpose

Improve the existing AAF helper so it catches, before late full hooks, the known
Corpus Completeness And Report Integrity shape defect class observed during
AAF-T1 review, while adding drift tests for helper mirrors of canonical machine
gate vocabulary.

## Agent Roles

| Role | Owner |
|---|---|
| Dispatcher | Codex |
| Worker | Claude |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex after review, only if next-move surfaces change |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 AAF-T2 approval | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T2 GC-018 | `docs/baselines/CVF_GC018_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_2026-06-20.md` | ACCEPT |
| AAF-T1 closure | `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md` | ACCEPT |
| AAF-T1 helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| AAF-T1 focused tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |
| Corpus completeness checker | `governance/compat/check_corpus_completeness_report_integrity.py` | ACCEPT |
| Dispatch-quality checker | `governance/compat/check_work_order_dispatch_quality.py` | ACCEPT |
| Worker-return fast gate | `governance/compat/run_worker_return_fast_gate.py` | ACCEPT |
| Commit steward protocol | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- modify `governance/compat/run_agent_automation_assist.py`;
- modify `governance/compat/test_run_agent_automation_assist.py`;
- create the AAF-T2 worker-return artifact named in Required Deliverables;
- add read-only helper diagnostics for changed active Markdown artifacts that
  would fail the Corpus Completeness And Report Integrity output gate;
- add drift tests comparing helper worker-return packet-shape constants to
  canonical constants in `check_work_order_dispatch_quality.py`;
- preserve AAF-T1 behavior and CLI.

Forbidden scope:

- no edits outside the three Required Deliverables;
- no edits under `EXTENSIONS/**`, product runtime, web UI, MCP packages,
  `.github/**`, public-sync, dependency manifests, session state, or root
  handoff files;
- no provider/live proof, benchmark, public push, secret read, dependency
  install, CodeGraph install/init, watcher/daemon, queue, or background service;
- no automatic mutation by the helper: no writing, staging, committing, pushing,
  deleting, moving, shelling into arbitrary user commands, or direct
  IDE/shell/git/filesystem interception;
- no readiness, production, public release, universal speed, universal
  governed-coding control, or full-hook equivalence claim.

Risk ceiling: R1 governance tooling, read-only assistance.

## Required First Reads

Claude must read these before editing:

- `docs/baselines/CVF_GC018_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_2026-06-20.md`
- `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `governance/compat/check_corpus_completeness_report_integrity.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`

## Pre-Flight Checks

Before implementation, Claude must run or record:

```powershell
git rev-parse --short HEAD
git status --short
```

If the worktree contains unrelated dirty paths, Claude must preserve them and
avoid editing outside the three Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_agent_automation_assist.py` | Claude | modify within AAF-T2 scope |
| `governance/compat/test_run_agent_automation_assist.py` | Claude | modify within AAF-T2 scope |
| `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_WORKER_RETURN_2026-06-20.md` | Claude | create only |
| Any other path | Not Claude | forbidden unless Codex issues a revised work order |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify the existing read-only
automation-assist helper and focused tests for AAF-T2 early diagnostics only.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator explicitly approved continuing to AAF-T2 on
2026-06-20.

Rollback boundary: if AAF-T2 is rejected, revert only the AAF-T2 edits to the
helper/test and remove the AAF-T2 worker-return/reviewer artifacts. Do not revert
AAF-T1 closure commit `3b26e23a` or session-sync commit `31b7ef35`.

Scope boundary: this authorization does not extend to canonical corpus checker
behavior, dispatch-quality checker behavior, session files, root handoff files,
runtime/product source, public-sync, provider/live proof, MCP execution, or
direct-interception tooling.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated AAF-T2 automation continuation request |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R1; read-only local governance helper hardening |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | Claude implements helper/test/worker-return only |
| Reviewer role | Codex reviews, commits, closes, and session-syncs if accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | satisfied for dispatch; fresh checkpoint required for scope expansion |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency install, destructive actions, or claim-boundary change |

## Worker Autonomy / No-Question Rule

Claude must repair and rerun gate failures inside Allowed scope. Claude must
stop and return `BLOCKED_WITH_REASON` only for scope expansion, forbidden paths,
live/provider proof, public-sync, secret/quota consumption, dependency install,
destructive actions, or claim-boundary changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing `governance/compat/` helper and focused test |
| Storage decision | update existing helper/test; add one worker-return review artifact |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | helper remains read-only advisory automation; no hidden state store |

## Required Deliverables

Claude must leave exactly these uncommitted artifact changes:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_WORKER_RETURN_2026-06-20.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AAF helper mirrors worker-return packet-shape required terms | `governance/compat/run_agent_automation_assist.py` | lines 52-63 | `WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS` | AAF helper packet-shape diagnostics | ACCEPT |
| AAF helper diagnoses no-commit work-order packet shape | `governance/compat/run_agent_automation_assist.py` | lines 145-174 | `diagnose_no_commit_work_order` | AAF helper diagnostics | ACCEPT |
| AAF helper recommends steward mode from path plan | `governance/compat/run_agent_automation_assist.py` | lines 177-193 | `recommend_mode` | AAF helper mode router | ACCEPT |
| AAF helper maps modes to exact next commands | `governance/compat/run_agent_automation_assist.py` | lines 214-244 | `_next_command` | AAF helper command suggestion | ACCEPT |
| AAF helper report currently serializes defects and command fields | `governance/compat/run_agent_automation_assist.py` | lines 247-284 | `AssistReport.to_dict` | AAF helper JSON report | ACCEPT |
| AAF helper build path collects diagnostics and defects | `governance/compat/run_agent_automation_assist.py` | lines 286-356 | `build_report` | AAF helper report builder | ACCEPT |
| Corpus checker declares allowed verdict vocabulary | `governance/compat/check_corpus_completeness_report_integrity.py` | lines 38-44 | `ALLOWED_VERDICTS` | corpus completeness output gate | ACCEPT |
| Corpus checker declares required terminal statuses | `governance/compat/check_corpus_completeness_report_integrity.py` | lines 45-50 | `ALLOWED_TERMINAL_STATUSES` | corpus completeness output gate | ACCEPT |
| Corpus checker declares required section fields | `governance/compat/check_corpus_completeness_report_integrity.py` | lines 51-68 | `REQUIRED_SECTION_FIELDS` | corpus completeness output gate | ACCEPT |
| Corpus checker extracts unresolved count and verdict | `governance/compat/check_corpus_completeness_report_integrity.py` | lines 220-230 | `_extract_unresolved_count`; `_extract_verdict` | corpus completeness output gate | ACCEPT |
| Corpus checker validates safe enumeration | `governance/compat/check_corpus_completeness_report_integrity.py` | lines 242-248 | `_is_safe_enumeration` | corpus completeness output gate | ACCEPT |
| Corpus checker validates applicable active Markdown output | `governance/compat/check_corpus_completeness_report_integrity.py` | lines 206-218, 277-329 | `_is_applicable_output`; `_validate_output` | corpus completeness output gate | ACCEPT |
| Dispatch-quality checker canonical worker-return packet-shape constants exist | `governance/compat/check_work_order_dispatch_quality.py` | lines 51, 159-177 | `WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER`; `WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS`; `WORKER_RETURN_PACKET_SHAPE_CONDITIONAL_TERMS` | dispatch-quality gate | ACCEPT |
| Dispatch-quality checker validates worker-return packet-shape contract | `governance/compat/check_work_order_dispatch_quality.py` | lines 777-805 | `_validate_worker_return_packet_shape_contract` | dispatch-quality gate | ACCEPT |
| Worker-return fast gate currently runs focused pytest, corpus registry drift, reviewer-fast, and diff hygiene | `governance/compat/run_worker_return_fast_gate.py` | lines 30-52, 81-99 | `build_commands`; `--pytest-target` | worker-return fast gate | ACCEPT |
| Commit steward path plan and mode commands remain canonical for lane classification | `governance/compat/run_agent_commit_steward_preflight.py` | lines 21-28, 41-54, 139, 195 | `SESSION_PREFIXES`; `HANDOFF_PREFIXES`; `PathPlan`; `build_path_plan`; `_mode_commands` | commit steward | ACCEPT |

## Required Helper Contract

Implement AAF-T2 with these constraints:

- preserve all AAF-T1 CLI flags and existing JSON keys;
- add a structured list for early gap diagnostics, named clearly in JSON;
- include corpus completeness diagnostics in human output;
- use existing checker logic or constants where practical instead of inventing
  new vocabulary;
- do not make the helper run full hook chains or subprocess gate bundles;
- make `--enforce` fail when local early diagnostics identify a corpus-shape
  defect that would fail the corpus completeness checker;
- keep helper output advisory and local: it can say "defect/risk detected", not
  "full closure pass".

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and preserve unrelated dirty paths.
3. Add helper internals for early corpus-completeness diagnostics without
   changing the public AAF-T1 CLI.
4. Add JSON and human-output coverage for the new diagnostics.
5. Add focused tests for corpus diagnostics and canonical mirror drift.
6. Run the Test / Gate Requirements and repair allowed-scope failures.
7. Return `COMPLETE_PENDING_REVIEW` with no commit.

## Worker Return Packet Shape Contract

Claude's worker return must include these always-required sections:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- executionBaseHead
- git status --short

Claude's worker return must include or explicitly mark `N/A with reason` for
these conditional gate sections:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Return vocabulary:

- success: `COMPLETE_PENDING_REVIEW`
- blocked: `BLOCKED_WITH_REASON`
- no commit: `WORKER_MUST_NOT_COMMIT`

## Acceptance Criteria

| ID | Criterion | Evidence required |
|---|---|---|
| AC1 | Existing AAF-T1 mode recommendation behavior remains intact | focused tests pass |
| AC2 | Helper detects changed active Markdown with missing or malformed Corpus Completeness block when applicable | focused tests plus helper JSON fixture |
| AC3 | Helper emits the new early diagnostics in human and JSON output | focused tests |
| AC4 | `--enforce` returns non-zero for local corpus-shape defects | focused tests |
| AC5 | Clean N/A-with-reason corpus block does not produce a defect | focused tests |
| AC6 | Helper worker-return packet-shape constants match canonical dispatch-quality constants | drift test |
| AC7 | No forbidden mutation or runtime/provider/public scope is introduced | worker-return claim boundary and reviewer inspection |

## Test / Gate Requirements

Claude must run:

```powershell
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base 31b7ef35 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
```

If the helper smoke command fails only because it correctly detects AAF-T2's own
in-progress worker-return packet defect, Claude must fix the packet within
Allowed scope and rerun. Do not ask the operator for allowed-scope repairs.

## Evidence Requirements

Claude's worker return must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- focused unittest command and result;
- helper smoke command and result;
- worker-return fast gate command and result;
- exact changed paths;
- any reviewer-relevant defect repaired inside Allowed scope;
- explicit N/A-with-reason rows for runtime/provider/live/public/cost scope.

## Review Gate

Codex reviewer must run, at minimum:

```powershell
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base <closureBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

Codex may repair only AAF-T2 allowed-scope defects before committing. Any scope
expansion returns to the operator.

## Closure Checklist

- [ ] Worker changed only the three Required Deliverables.
- [ ] Helper remains read-only and advisory.
- [ ] Existing AAF-T1 tests still pass.
- [ ] New corpus diagnostic tests pass.
- [ ] New drift test passes.
- [ ] Worker-return packet includes required shape sections.
- [ ] Public Export Disposition is resolved.
- [ ] Delta/runtime/provider/live/public-sync claims are N/A with reason.
- [ ] Codex reviewer owns completion review and session-sync.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all Required Deliverables are present,
focused tests pass, helper smoke passes, worker-return fast gate passes, and no
forbidden scope was touched.

Return `BLOCKED_WITH_REASON` only when blocked by missing source authority,
forbidden path requirements, dependency install need, provider/live proof,
public-sync, destructive action, secret/quota access, or claim-boundary change.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope repairs. A fresh operator
checkpoint is required before opening AAF-T3, CLI/MCP integration,
watcher/daemon behavior, runtime/provider/live proof, public-sync, direct
interception, full-hook equivalence claims, or universal control claims.

## Commit Prompt Readiness

This section exists only because the dispatch packet includes commit-prompt
language in the worker-return contract and review gate. It does not authorize
Claude to commit.

- Diff scope: PASS - dispatch authoring changes are limited to the AAF-T2
  GC-018 baseline and this work order.
- Tests: PASS - dispatch authoring gates are required before Codex commits this
  packet; Claude must run focused implementation tests before returning.
- Gates: PASS - dispatch-quality and pre-dispatch gates are required before
  Codex dispatch commit.
- Untracked unrelated: NONE - dispatch author observed no unrelated dirty paths
  except the recurring Windows global git-ignore permission warning.
- Forbidden touched paths: NONE - no forbidden implementation/runtime/public
  paths are touched by dispatch authoring.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | `governance/compat/run_agent_automation_assist.py` |
| Disposition | ADAPT as CVF-owned governance helper hardening |
| Claim boundary | existing CVF helpers and standards remain source authority; no third-party code or claim is absorbed |

## Rescan Intelligence Hardening

- Original source artifact: operator AAF-T2 selection and AAF-T1 closure
  finding.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because AAF-T2 promotes a late
  full-hook surprise into early helper diagnostics.
- Routing matrix status:
  - `DO_NOW`: helper early corpus diagnostics and drift tests.
  - `RESOLVED_BY_DESIGN`: read-only helper remains advisory.
  - `SEPARATE_RUNTIME_TRANCHE`: CLI/MCP integration, watcher/daemon, provider/live.
  - `OUT_OF_SCOPE`: public-sync, direct interception, universal control.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to AAF-T1 late-gap
  finding and helper diagnostics.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF helper remains read-only, local, and advisory. |
| CHANGED_DISPOSITION | AAF-T1 late full-hook surprise becomes AAF-T2 early helper diagnostics. |
| NEW_FINDING | Helper mirror drift needs focused test coverage against canonical gate constants. |
| REMOVED_OR_REJECTED | Runtime/MCP/watcher/provider/public-sync/direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Implement helper early corpus diagnostics and drift tests. |
| RESOLVED_BY_DESIGN | Keep helper read-only and enforce only local defects. |
| SEPARATE_RUNTIME_TRANCHE | CLI/MCP integration, watcher/daemon, provider/live, direct interception. |
| STRATEGIC_OPERATOR_DECISION | Future AAF-T3 or reviewer-fast integration after AAF-T2 evidence. |
| DEFER | Full-hook equivalence or automatic remediation. |
| OUT_OF_SCOPE | Public-sync, production readiness, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T2-RS1 | Required Helper Contract | helper remains read-only | OUT_OF_SCOPE mutation | Could diagnostics write files or run arbitrary commands? | PASS_READ_ONLY_SCOPE |
| AAF-T2-RS2 | Required Helper Contract | corpus shape is detected early | DO_NOW | Could a missing Corpus block still wait for pre-commit? | PASS_EARLY_DIAGNOSTIC_TARGET |
| AAF-T2-RS3 | Acceptance Criteria | mirror drift test protects packet-shape constants | RESOLVED_BY_DESIGN | Could helper vocabulary silently diverge? | PASS_DRIFT_TEST_REQUIRED |

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a work order authoring packet,
  not a corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated.
- Snapshot time: 2026-06-20 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source
  lookups over named AAF-T2 authority files.
- Manifest artifact or inline manifest: Source Verification Block and Required
  First Reads.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was
  produced.
- Processing ledger artifact or inline ledger: inline in Source Verification
  Block and Test / Gate Requirements.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0.
- Unresolved files: 0
- Declared exclusions: full corpus inventory, folder-tree scan, extraction
  report, runtime/provider proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: work order source verification rows cite source files and
  line anchors.
- Adversarial verification: claim rejects any full-corpus, complete-inventory,
  full-hook equivalence, runtime, or public readiness assertion.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

- Defect class: `GATE_LATENCY_LATE_FAILURE`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `MACHINE_CHECK_CANDIDATE_IMPLEMENTED_AS_HELPER_DIAGNOSTIC`
- Next action: Claude implements AAF-T2 helper/test hardening; Codex reviews
  whether a future AAF-T3 should wire diagnostics into reviewer-fast or keep
  them helper-only.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - no runtime or
  provider behavior is involved.

| Finding or lesson | Disposition | Reason |
|---|---|---|
| A worker-return packet can pass reviewer-fast but fail later corpus completeness checks | GOVERNANCE_LEARNING_PROMOTED | Move the known late failure into helper early diagnostics. |
| Helper mirror constants can drift from canonical gates | GOVERNANCE_LEARNING_PROMOTED | Add focused drift tests before future worker returns. |

## Epistemic Process Block

| Field | Disposition |
|---|---|
| Source basis | current repository files named in Source Verification Block |
| Inference boundary | AAF-T2 value is inferred from AAF-T1 observed late gate failure, not from public or production usage |
| Uncertainty | helper diagnostics may still be narrower than full hooks |
| Falsification path | focused tests, helper smoke, worker-return fast gate, Codex review |
| Claim status | bounded dispatch-ready work order |

## Machine Closure Package

N/A with reason: this is a dispatch work order, not a closure artifact. Codex
owns reviewer closure conversion after Claude returns `COMPLETE_PENDING_REVIEW`.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T2 read-only governance automation helper diagnostics work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user invokes the helper manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | early gap diagnostics helper, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, readiness, and universal control remain parked |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local workspace |
| Session or invocation | AAF-T2 dispatch authoring, 2026-06-20 |
| Working directory | repository root |
| Command or tool surface | file reads, `rg -n`, `apply_patch`, governance gates |
| Target paths | AAF-T2 GC-018 baseline and this work order |
| Allowed scope source | operator AAF-T2 approval and AAF-T1 closure finding |
| Before status evidence | HEAD `31b7ef35`; clean worktree except recurring Windows global git-ignore warning |
| After status evidence | AAF-T2 dispatch packet ready for pre-dispatch gates |
| Diff evidence | exact dispatch diff and dispatch-quality gate |
| Approval boundary | dispatch authoring only; no implementation by Codex in this packet |
| Claim boundary | no runtime mutation, provider/live, public-sync, direct interception, or universal enforcement claim |
| Agent type | single-agent dispatch author |
| Invocation ID | `aaf-t2-dispatch-codex-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_FOR_CLAUDE_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_FOR_CLAUDE_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T2 is private provenance governance tooling. Public export requires
separate public-sync authorization and a bounded public-facing summary if the
operator requests it later.

## Claim Boundary

This work order authorizes only a read-only AAF helper hardening tranche for
early local diagnostics and drift-test coverage. It does not authorize runtime
execution, provider/live proof, MCP execution, public-sync, direct interception,
automatic mutation, full-hook equivalence claims, production readiness, public
release readiness, universal speed, or universal governed-coding-control claims.
