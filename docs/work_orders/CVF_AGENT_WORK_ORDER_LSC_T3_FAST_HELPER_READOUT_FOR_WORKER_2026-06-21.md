# CVF Agent Work Order - LSC-T3 Fast Helper Readout

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: work_order

dispatchBaseHead: aca3ec97

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T3_FAST_HELPER_READOUT_FOR_WORKER_2026-06-21.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: LSC-T3 is a read-only helper/readout tranche only. Its
prerequisites are satisfied by LSC-T2 material closure commit `00214e9a`,
LSC-T4 material closure commit `b568f248`, and session-sync commit `aca3ec97`.
It follows the operator-selected roadmap order:
`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7`. The mission is to make
current helper-detectable learning signals visible quickly without making every
readout item a blocker.

Do-not-misread notes: do not build a ledger store, source directory, generator,
drift checker, durable store, CLI/MCP adapter, runtime bridge, provider route,
public-sync artifact, queue/daemon, watcher, or latency enforcement gate. Do
not edit session state, active handoff, root startup routers, public-sync,
`.github/**`, dependency manifests, web UI, MCP packages, or runtime provider
routes. Do not reopen LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1,
MLW7, or MLW8.

Required first actions: read this work order, read the LSC-T3 GC-018 baseline,
read the LSC-T0 roadmap, read the LSC reference front door, read the LSC-T1,
LSC-T2, and LSC-T4 contracts, read the AAF helper and focused tests named in
the Source Verification Block, confirm actual `executionBaseHead`, and inspect
current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, focused gate evidence, and no commit. If
blocked, return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker implements helper/readout/reference/return artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=aca3ec97`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending LSC-T3 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix LSC-T3 with LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, or ledger/generator implementation |
| Before status evidence | clean worktree at committed dispatch base `aca3ec97`; `git status --short` was clean before LSC-T3 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted helper/test/reference/front-door updates; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator roadmap order, LSC-T0 roadmap, closed LSC-T1/T2/T4 reference contracts |
| Intake role | worker implements bounded helper/readout and focused tests |
| Reviewer role | reviewer/closer validates source fidelity, focused tests, claim boundary, and commit eligibility |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; read-only helper/readout only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime/source beyond allowed helper/test paths, MCP/provider/live/public-sync/session-sync/parked-lane expansion is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | LSC-T3 is derived from the current LSC roadmap and accepted LSC-T1/T2/T4 reference contracts, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | LSC-T0 roadmap, LSC reference front door, LSC-T1 contract, LSC-T2 contract, LSC-T4 policy, AAF helper, AAF helper focused tests, and worker-experience checker. |

## Required First Reads

The worker must read these sources before editing:

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and role-neutrality rule |
| `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T3_FAST_HELPER_READOUT_FOR_WORKER_2026-06-21.md` | current work order and packet shape |
| `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC roadmap, latency budget, and LSC-T3 row |
| `docs/reference/learning_signal_chain/README.md` | LSC reference front door to update |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | source-layout, de-dup, and field ownership |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | role capture and closure-blocking boundary |
| `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | outcome vocabulary and blocking-vs-readout policy |
| `governance/compat/run_agent_automation_assist.py` | helper implementation surface |
| `governance/compat/test_run_agent_automation_assist.py` | focused test surface |
| `governance/compat/check_worker_experience_retrospective.py` | worker-experience diagnostic source |

## Pre-Flight Checks

The worker must run or record these checks before returning:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base aca3ec97 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `governance/compat/run_agent_automation_assist.py` | worker | may update only to add LSC-T3 read-only signal readout |
| `governance/compat/test_run_agent_automation_assist.py` | worker | may update focused tests for LSC-T3 readout |
| `docs/reference/learning_signal_chain/README.md` | worker | may update only to add the LSC-T3 row |
| `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | worker | create |
| `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_WORKER_RETURN_2026-06-21.md` | worker | create |
| `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T3_FAST_HELPER_READOUT_FOR_WORKER_2026-06-21.md` | reviewer/closer | no worker edit |
| session state, active handoff, public-sync, runtime routes, provider code, MCP packages, dependency manifests | out of worker scope | forbidden |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify the existing read-only
automation-assist helper and focused tests for LSC-T3 fast helper readout only.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator approved the Learning Signal Chain roadmap
order on 2026-06-21 and instructed continuation without waiting. Active
continuity now identifies LSC-T3 as the next dispatch-ready move after LSC-T4
closure.

Rollback boundary: if LSC-T3 is rejected, revert only the LSC-T3 edits to the
helper/test and remove the LSC-T3 reference, worker-return, reviewer, GC-018,
and work-order artifacts. Do not revert LSC-T4 closure commit `b568f248`,
LSC-T4 dispatch commit `275eb374`, or session-sync commit `aca3ec97`.

Scope boundary: this authorization does not extend to canonical checker
behavior outside the AAF helper, session files, root handoff files,
runtime/product source, public-sync, provider/live proof, MCP execution,
CLI/MCP adapter behavior, dependency manifests, queue/daemon, watcher, or
direct-interception tooling.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
runtime routes, MCP/provider/live/public-sync scope, parked-lane reopening,
dependency installation, secrets/quota, destructive action, or a change to the
claim boundary.

## Purpose

Add an LSC-T3 readout to the existing AAF helper so agents can quickly see
current helper-detectable learning signals and next suggested actions before
spending time on deeper gates or retrospective search.

Success means the helper can tell an internal or future external CLI/MCP agent:

- there are no helper-detectable signals in the current changed set; or
- the current changed set has advisory signals with source path, source surface,
  severity, repeat risk, LSC-T4 recommended outcome, next suggested action,
  blocker flag, and reason.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | helper/reference/test author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 roadmap order selecting LSC-T3 after LSC-T4 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T3 GC-018 | `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| LSC-T2 contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | ACCEPT |
| LSC-T4 policy | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | ACCEPT |
| AAF helper source | `governance/compat/run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_HELPER_INTERFACE |
| AAF helper focused tests | `governance/compat/test_run_agent_automation_assist.py` | SOURCE_AUTHORITY_FOR_FOCUSED_TEST_SHAPE |
| Worker-experience checker | `governance/compat/check_worker_experience_retrospective.py` | SOURCE_AUTHORITY_FOR_WORKER_RETRO_DIAGNOSTICS |

## Scope / Target / Owner Boundary

Allowed scope:

- update `governance/compat/run_agent_automation_assist.py` with read-only LSC
  signal readout logic;
- update `governance/compat/test_run_agent_automation_assist.py` with focused
  tests for JSON and human output;
- update `docs/reference/learning_signal_chain/README.md` to list LSC-T3;
- create `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md`;
- create `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_WORKER_RETURN_2026-06-21.md`;
- reviewer/closer may update `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md`
  status during closure;
- reviewer/closer may create
  `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_COMPLETION_2026-06-21.md`
  during closure;
- add helper-local dataclass/shape if needed for `signalReadout`;
- reuse existing diagnostics from `WorkOrderDiagnostic`, `CorpusDiagnostic`,
  worker-experience diagnostics, and steward-lane classification;
- keep `blocking=false` unless LSC-T4 blocker conditions are source-backed.

Reviewer/closer closure scope:

- update this work order status and closure evidence;
- update the LSC-T3 GC-018 baseline status;
- create the LSC-T3 completion review;
- repair allowed-scope helper/test/reference wording, manifests, or
  packet-shape defects required by machine gates before commit.

Forbidden scope:

- no edits to session state, active handoff, root startup routers, public-sync,
  `.github/**`, dependency manifests, web UI, MCP packages, runtime routes,
  provider routes, or source paths outside the named helper/test files;
- no ledger source directory, generated aggregate, generator, drift checker,
  durable store, CLI/MCP adapter, runtime bridge, provider/live proof,
  dependency install, queue/daemon/watcher, wrapper/proxy enforcement, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal
  governed-coding-control claim;
- no implementation of LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3,
  ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 read-only local helper diagnostic.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and record a source inventory in the worker
   return.
3. Add an LSC-T3 reference contract and front-door row.
4. Extend `run_agent_automation_assist.py` so `AssistReport` exposes a stable
   `signalReadout` list in JSON and human output.
5. Build readout items only from existing helper-detectable signals and LSC-T4
   outcome vocabulary.
6. Add focused tests for JSON shape, no-signal cheap path, at least one
   helper-detectable signal, and human output.
7. Create the worker-return artifact with required packet shape and
   worker-experience token.
8. Run required helper/gate commands and record results.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- focused unittest result;
- helper smoke result with `--json --enforce`;
- worker-return fast gate result with focused test target;
- explicit statement that no session/handoff/public-sync/provider/MCP/runtime
  paths were edited;
- explicit statement that no ledger/generator/drift checker/CLI-MCP adapter was
  implemented;
- exact claim boundary and public export disposition.

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed, so reviewer-fast can validate the packet without
reviewer repair:

| Packet item | Worker-return disposition |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| `executionBaseHead` | exact value from `git rev-parse --short HEAD` at worker start |
| `dispatchBaseHead` | `aca3ec97` |
| `git status --short` | exact output after worker changes |
| Purpose section | MUST_INCLUDE |
| Scope / Methodology section | MUST_INCLUDE |
| Findings / Position section | MUST_INCLUDE |
| Risk / Corrective Action section | MUST_INCLUDE |
| Claim Boundary section | MUST_INCLUDE |
| Agent Operation Trace Block section | MUST_INCLUDE |
| Delta Execution Claim Boundary Control Block section | MUST_INCLUDE |
| Public Export Disposition section | MUST_INCLUDE |
| External Knowledge Intake Routing section | MUST_INCLUDE |
| Rescan Intelligence Hardening section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Corpus Completeness And Report Integrity section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Finding-To-Governance Learning Disposition section | MUST_INCLUDE |
| Epistemic Process Block section | MUST_INCLUDE_OR_EPISTEMIC_PROCESS_NA_WITH_REASON |
| Machine Closure Package section | MUST_INCLUDE_OR_NA_WITH_REASON; worker must not mark closure |
| Worker-experience token | structured `WORKER_EXPERIENCE_RETRO` or exact asserting `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` |

Conditional sections that do not apply must still be present with `N/A with
reason` or `NOT_APPLICABLE_WITH_REASON` rows. The worker must not record a
clean `git status --short` when the worker-return file or other deliverables
are untracked or modified.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, focused-test, helper
smoke, or packet-shape defects and rerun the relevant gate without asking the
operator or dispatcher. This includes missing required sections, packet-shape
rows, helper JSON/human output shape, LSC reference-front-door row wording,
claim-boundary wording, and documentation-only terminology inside the Required
Deliverables.

The worker must stop and return `BLOCKED_WITH_REASON` only when the repair would
exceed Allowed scope, change the claim boundary, require session/handoff/
public-sync/runtime/provider/live/MCP/CLI-adapter/dependency edits, consume
secrets or quota, alter parked-lane ordering, touch forbidden paths, or perform
destructive or irreversible actions.

## Acceptance Criteria

The worker return is acceptable only if:

- all Required Deliverables exist and no unauthorized paths are changed;
- the helper remains read-only and does not run full gates internally;
- `python -m unittest governance.compat.test_run_agent_automation_assist` passes;
- `python governance/compat/run_agent_automation_assist.py --base aca3ec97 --head HEAD --json --enforce` passes or returns only expected current changed-set defects caused by the worker-return artifact and documents the reason;
- `--json` output includes `signalReadout` as a list;
- human output includes a concise Learning Signal Readout section;
- no-signal path is concise and does not create defects;
- at least one focused test proves a helper-detectable issue becomes an advisory readout item;
- readout items use only LSC-T4 outcome vocabulary;
- `blocking=true` appears only when LSC-T4 blocker conditions are explicitly source-backed;
- LSC-T3 reference contract and README row state no ledger store, generator,
  drift checker, CLI/MCP adapter, runtime mutation, provider/live proof, or
  public-sync behavior is implemented.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source evidence | Work-order mapping | Disposition |
|---|---|---|---|
| LSC-T3 surfaces unresolved relevant signals and next action | LSC-T0 line 254 | Required Helper Contract and Acceptance Criteria | SATISFIED_BY_DISPATCH |
| Exit criteria include read-only helper diagnostic and focused tests | LSC-T0 line 254 | Write Ownership and Pre-Flight Checks include helper/test paths and unittest | SATISFIED_BY_DISPATCH |
| Capture remains fast and promotion remains governed | LSC-T0 lines 301-316 and LSC-T4 policy | helper is advisory; no full gates or autonomous mutation | SATISFIED_BY_DISPATCH |
| LSC-T4 outcomes guide helper readout | LSC-T4 lines 61-130 and 205-219 | Required Helper Contract uses LSC-T4 vocabulary and blocker rules | SATISFIED_BY_DISPATCH |
| Existing helper interface owns JSON and human output | AAF helper lines 459-510 and 624-669 | worker modifies `AssistReport.to_dict` and `_print_human` only inside helper scope | SATISFIED_BY_DISPATCH |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 defines LSC-T3 as Fast Helper Readout | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 254 | `LSC-T3`; Fast Helper Readout | LSC-T0 roadmap | ACCEPT |
| LSC-T0 requires future work orders to keep capture fast and promotion governed | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-316 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | ACCEPT |
| LSC-T2 defines multi-role signal eligibility and no-signal boundaries | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 85-90, 106-126 | Capture Eligibility Matrix; no-signal guidance | LSC-T2 contract | ACCEPT |
| LSC-T2 maps role signals to existing intake fields without adding runtime fields | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 141-149, 161-164 | `sourceSummary`; `lane`; `severity` | LSC-T2 contract | ACCEPT |
| LSC-T2 preserves closure blocking only for critical or observed repeated signals | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | line 202 | closure blocking rule | LSC-T2 contract | ACCEPT |
| LSC-T4 defines outcome vocabulary consumed by LSC-T3 | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 61-79 | LSC-T4 outcome vocabulary | LSC-T4 policy | ACCEPT |
| LSC-T4 defines threshold matrix and blocking-vs-readout behavior | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 83-130 | Threshold Decision Matrix; Blocking-Vs-Readout Policy | LSC-T4 policy | ACCEPT |
| LSC-T4 states LSC-T3 helper should consume outcome vocabulary | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | lines 205-219 | LSC-T3 Future-Tranche Routing; Latency Budget | LSC-T4 policy | ACCEPT |
| AAF helper is read-only and changed-set based | `governance/compat/run_agent_automation_assist.py` | lines 1-18 | module docstring | AAF helper | ACCEPT |
| AAF helper report owns JSON fields and defects list | `governance/compat/run_agent_automation_assist.py` | lines 459-510 | `AssistReport`; `to_dict` | AAF helper | ACCEPT |
| AAF helper builds report from changed paths and diagnostics | `governance/compat/run_agent_automation_assist.py` | lines 514-620 | `build_report` | AAF helper | ACCEPT |
| AAF helper owns human output rendering | `governance/compat/run_agent_automation_assist.py` | lines 624-669 | `_print_human` | AAF helper | ACCEPT |
| AAF helper CLI owns `--json` and `--enforce` behavior | `governance/compat/run_agent_automation_assist.py` | lines 672-710 | `main` | AAF helper CLI | ACCEPT |
| Existing focused tests cover BuildReport and CLI output shape | `governance/compat/test_run_agent_automation_assist.py` | lines 258-365 | `BuildReportTests`; `CliOutputTests` | AAF helper focused tests | ACCEPT |
| Existing focused tests cover corpus diagnostics JSON | `governance/compat/test_run_agent_automation_assist.py` | lines 365-499 | `CorpusDiagnosticTests`; `BuildReportCorpusTests` | AAF helper focused tests | ACCEPT |
| Existing focused tests cover worker-experience helper diagnostics | `governance/compat/test_run_agent_automation_assist.py` | lines 597-623 | `WorkerExperienceHelperDiagnosticTests` | AAF helper focused tests | ACCEPT |
| Worker-experience checker exposes `diagnose` and eligible retro semantics | `governance/compat/check_worker_experience_retrospective.py` | lines 34-61, 153-201 | `RETRO_TOKEN`; `RETRO_NA_TOKEN`; `diagnose` | worker-experience checker | ACCEPT |

## New Doc-Only / Helper-Local Terms

| Proposed term | Owner in LSC-T3 | Runtime status | Reason |
|---|---|---|---|
| `signalReadout` | AAF helper JSON report and LSC-T3 reference contract | DOC_ONLY_NEW / helper-local | advisory list of helper-detectable current signals |
| `SignalReadoutItem` | AAF helper internal dataclass if used | DOC_ONLY_NEW / helper-local | stable internal shape for one advisory readout row |
| `nextSuggestedAction` | AAF helper readout item | DOC_ONLY_NEW / helper-local | human-readable next action, not an executable command |
| `blocking` | AAF helper readout item | DOC_ONLY_NEW / helper-local | advisory boolean derived from LSC-T4 blocker rules; no gate authority |

## Required Contract Content

The LSC-T3 reference contract must include these sections:

- Purpose
- Scope
- Readout Principles
- Readout Item Shape
- Signal Source Mapping
- LSC-T4 Outcome Mapping
- Blocking Boundary
- JSON And Human Output Contract
- Latency Budget
- Parking Ledger
- Public Export Disposition
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Claim Boundary

Required policy assertions:

- LSC-T3 readout is advisory and read-only.
- LSC-T3 surfaces current helper-detectable signals only.
- `signalReadout` is not a ledger, store, generator, drift checker, CLI/MCP
  adapter schema, or runtime Learning Plane mutation.
- `repeatRisk=OBSERVED_REPEATED` must not be claimed without ledger/de-dup
  proof.
- `blocking=true` is reserved for LSC-T4 blocker conditions only.
- Routine readout items must not block closure.
- `autonomousMutationAuthorized=false` remains invariant.

## Review Gate

The reviewer/closer must run reviewer-fast or a stricter applicable gate before
accepting the worker return. Acceptance requires checking source fidelity,
focused tests, helper read-only behavior, JSON/human output shape,
public/provenance boundary, external-intake routing, finding-to-governance
disposition, Delta boundary N/A, and the worker-return packet shape.

## Closure Checklist

Reviewer/closer closure evidence must resolve these items:

- Required deliverables exist.
- No forbidden paths changed.
- Source Verification claims remain current.
- Helper remains read-only and local.
- Focused unittest passes.
- Helper smoke with `--json --enforce` is recorded.
- `signalReadout` JSON list is present.
- Human output Learning Signal Readout section is present.
- No-signal cheap path is covered by test.
- At least one helper-detectable signal is covered by test.
- LSC-T4 outcome vocabulary is used without invented outcomes.
- Blocking boundary preserves LSC-T4 policy.
- Worker-return packet includes required sections and token.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T3_FAST_HELPER_READOUT_FOR_WORKER_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer/closer patch | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer/closer patch | PASS |
| Worker return | `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_WORKER_RETURN_2026-06-21.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LSC_T3_FAST_HELPER_READOUT_COMPLETION_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC-T3 accepted by this closure; roadmap remains the governing LSC-T0 plan | PASS |
| Reference front door | `docs/reference/learning_signal_chain/README.md` | LSC-T3 row present; stale no-helper-readout boundary repaired | PASS |
| Reference contract | `docs/reference/learning_signal_chain/CVF_LSC_T3_FAST_HELPER_READOUT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Helper implementation | `governance/compat/run_agent_automation_assist.py` | `signalReadout` JSON list and human readout section implemented | PASS |
| Focused tests | `governance/compat/test_run_agent_automation_assist.py` | focused unittest and pytest target pass 45/45 | PASS |
| Session continuity | active session front-door/state/handoff after material commit | session-sync follows material closure commit | N/A with reason |
| Registry JSON | N/A with reason: no generated JSON registry created or changed | no registry mutation | PASS |
| Registry Markdown | N/A with reason: no generated Markdown index created in LSC-T3 | no generated Markdown registry | PASS |
| External evidence digest | N/A with reason: no external benchmark/provider/live digest created | helper/reference closure only | N/A with reason |
| System loop interlock | N/A with reason: no runtime/source interlock changed | no runtime/source mutation | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: LSC-T3 creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: LSC-T3 performs no query acceptance | N/A_WITH_REASON |
| Worker-return acceptance | worker return present and accepted by reviewer/closer | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` read-only helper/readout closure only | PASS |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all Required Deliverables are created
and required gate evidence is recorded. Return `BLOCKED_WITH_REASON` if the task
requires forbidden paths, runtime route changes, provider/live proof, public-sync,
MCP/CLI adapter behavior, dependency install, destructive actions, or parked-lane
reopening.

## Current Runtime Freshness Verification

| Claim | Freshness evidence | Disposition |
|---|---|---|
| Helper source path exists | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Focused test path exists | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |
| Worker-experience checker path exists | `governance/compat/check_worker_experience_retrospective.py` | ACCEPT |
| Runtime route implementation is not authorized | Allowed and Forbidden scope in this work order | N/A_WITH_REASON |
| CLI/MCP adapter behavior is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Provider/live proof is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Public-sync is not authorized | Public route and Public Export Disposition | N/A_WITH_REASON |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor capture artifact: `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`.
- Predecessor promotion artifact: `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T3 moves helper readout
  from roadmap row into dispatch-ready helper work.
- Routing matrix status: `DO_NOW` for read-only helper diagnostic and focused
  tests; `SEPARATE_RUNTIME_TRANCHE` for ledger/generator/drift/CLI-MCP/runtime
  work; `STRATEGIC_OPERATOR_DECISION` for LSC-T6 and LSC-T5/T7 after LSC-T3;
  `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/readiness
  claims.
- Semantic sampling status: sampled LSC-T0 LSC-T3 row, LSC-T0 future-work
  acceptance criteria, LSC-T2 role signal rules, LSC-T4 outcome/blocking rules,
  AAF helper report functions, AAF helper tests, and worker-experience checker.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T3 helper readout moved from roadmap row into dispatch requirements. |
| NEW_FINDING | Helper needs explicit `signalReadout` output so agents see unresolved local diagnostics without running deep gates. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception/CLI-MCP adapter scope remains rejected for LSC-T3. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T3 read-only helper readout and focused tests. |
| SEPARATE_RUNTIME_TRANCHE | ledger store, source directory, generator, drift checker, CLI/MCP adapter, runtime bridge, latency guard. |
| STRATEGIC_OPERATOR_DECISION | LSC-T6, then LSC-T5/T7 per active roadmap order. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | surface current helper-detectable signals instead of creating a global signal store. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T3-S1 | LSC-T0 work plan | LSC-T3 exits with read-only helper diagnostic and focused tests | mapped into Required Deliverables | prevents docs-only closure for helper tranche | PASS |
| LSC-T3-S2 | LSC-T4 outcome vocabulary | readout must use T4 outcomes | mapped into Required Helper Contract | prevents invented outcome names | PASS |
| LSC-T3-S3 | AAF helper source | helper is read-only and changed-set based | allowed scope limited to helper/test | prevents runtime or gate execution expansion | PASS |
| LSC-T3-S4 | LSC-T4 blocking policy | routine readout does not block closure | Required Helper Contract sets `blocking=false` unless blocker conditions are met | prevents latency regression | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T3 is a bounded helper
  readout implementation and reference update, not a corpus enumeration or
  legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block and Required First Reads; no corpus enumeration command is
  authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and Roadmap-To-Work-Order Trace Matrix above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and legacy scan surfaces out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration,
  public-sync copy, runtime/provider/live proof, CLI/MCP adapter, and parked lanes.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is
  created.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate or generated
  corpus registry is changed.
- Output traceability: Required Deliverables and Source Verification Block
  define all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T3 fast helper readout |
| Disposition | ADAPT as CVF-owned helper/readout tranche |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts; LSC-T3 does not implement external-agent CLI/MCP IO |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T3 fast helper readout dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | read-only local helper diagnostics only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | helper readout, unresolved local signal visibility, and next suggested action only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain helper work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | LSC-T3 dispatch authoring, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | local file edits and governance gates |
| Target paths | `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T3_FAST_HELPER_READOUT_FOR_WORKER_2026-06-21.md` |
| Allowed scope source | operator-selected LSC roadmap order and active session next allowed move |
| Before status evidence | clean worktree at committed base `aca3ec97`; `git status --short` clean before dispatch authoring |
| After status evidence | two uncommitted dispatch artifacts created for pre-dispatch review |
| Diff evidence | new GC-018 baseline and new worker dispatch packet |
| Approval boundary | dispatcher role may create dispatch artifacts only; worker remains `WORKER_MUST_NOT_COMMIT` |
| Claim boundary | read-only helper/readout dispatch only; no runtime/provider/MCP/public-sync implementation |
| Agent type | dispatcher role |
| Invocation ID | `lsc-t3-fast-helper-readout-dispatch-2026-06-21` |
| Expected manifest | LSC-T3 GC-018 and LSC-T3 worker dispatch packet |
| Actual changed set | `docs/baselines/CVF_GC018_LSC_T3_FAST_HELPER_READOUT_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T3_FAST_HELPER_READOUT_FOR_WORKER_2026-06-21.md` |
| Manifest delta | MATCH |

## Claim Boundary

This work order authorizes only LSC-T3 read-only local helper readout work and
focused tests for current helper-detectable signals. It does not implement or
authorize a ledger store, generator, drift checker, durable store, runtime
Learning Plane mutation, provider/live proof, CLI/MCP adapter behavior,
public-sync, direct interception, wrapper/proxy enforcement, queue/daemon,
watcher, readiness, cost optimization, full-hook equivalence, read-receipt
enforcement, or universal governed-coding control.
