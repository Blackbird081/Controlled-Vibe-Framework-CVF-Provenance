# CVF Agent Work Order - LSC-T2 Multi-Role Capture Contract And Eligibility Matrix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-21

docType: work_order

dispatchBaseHead: b2a90d52

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_FOR_WORKER_2026-06-21.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: LSC-T2 is a documentation/reference contract tranche only.
It follows LSC-T1 closure and operator lane selection. The mission is to define
role-specific capture eligibility for reviewer, reviewer/closer, dispatch
author, session-sync steward, operator, and external-agent returned-output
signals while preserving the existing AAF-T5 worker token and LSC-T1 de-dup
contract.

Do-not-misread notes: do not build a checker, helper, ledger store, source
directory, generator, drift checker, CLI/MCP adapter, runtime bridge, provider
route, public-sync artifact, source implementation, or read-receipt gate. Do
not edit `EXTENSIONS/**`, `governance/compat/**`, session state, active
handoff, root startup routers, or public-sync. Do not reopen AAF-T6, AAF-T7,
CGE-T3, ACE-R1, MLW7, or MLW8.

Required first actions: read this work order, read the LSC-T2 GC-018 baseline,
read the LSC-T0 roadmap, read the LSC-T1 front door and contract, read the
source files named in the Source Verification Block, confirm actual
`executionBaseHead`, and inspect current `git status --short`.

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
| rolePattern | two roles across phases: dispatcher creates packet; worker authors reference/front-door/return artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=b2a90d52`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending LSC-T2 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix LSC-T2 with AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP, public-sync, queue/daemon, direct-interception, or checker/helper implementation |
| Before status evidence | clean dispatch base `b2a90d52` before LSC-T2 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted LSC front door update; accepted LSC-T2 contract; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator lane selection, LSC-T0 roadmap, LSC-T1 closure artifacts |
| Intake role | worker authors bounded reference/front-door/return artifacts |
| Reviewer role | reviewer/closer validates source fidelity, gate results, claim boundary, and commit eligibility |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; no runtime/source/checker/helper implementation |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if runtime/source/test/MCP/provider/live/public-sync/session-sync/parked-lane expansion is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | LSC-T2 is derived from the current LSC roadmap, LSC-T1 reference contract, and current Learning Plane/AAF/external-review source files, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | LSC-T0 roadmap, LSC-T1 reference front door and contract, Learning Signal Intake Bridge, AAF-T5 checker, worker-experience standard, and external knowledge absorption chain map. |

## Purpose

Create the LSC-T2 multi-role capture contract and eligibility matrix so CVF can
learn from worker, reviewer/closer, dispatch author, session-sync steward,
operator, and external-agent friction without making every governed return a
long retrospective.

Success means future roles can read one contract and know:

- when a signal is eligible for capture;
- when a no-signal assertion is enough;
- where the role should record the signal;
- how the signal maps to LSC-T1 fields and existing intake fields;
- how external-agent returned output is routed before promotion;
- which future implementation lanes remain parked.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | documentation/reference author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-21 approval to issue work order after lane audit selected LSC-T2 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T2 GC-018 | `docs/baselines/CVF_GC018_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_2026-06-21.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| Learning Signal Intake Bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_AUTHORITY_FOR_EXISTING_INTAKE_FIELDS |
| Worker-experience checker | `governance/compat/check_worker_experience_retrospective.py` | SOURCE_AUTHORITY_FOR_EXISTING_WORKER_TOKEN |
| Worker-experience standard | `docs/reference/worker_experience_retrospective/README.md` | SOURCE_AUTHORITY_FOR_EXISTING_WORKER_TOKEN |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_RETURN_ROUTING |

## Scope / Target / Owner Boundary

Allowed scope:

- update `docs/reference/learning_signal_chain/README.md` to list LSC-T2;
- create `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`;
- create `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md`;
- update `docs/baselines/CVF_GC018_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_2026-06-21.md` status during reviewer/closer closure;
- create `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_COMPLETION_2026-06-21.md` during reviewer/closer closure;
- define role-neutral actor categories and capture eligibility;
- define no-signal assertion guidance and latency-preserving capture shape;
- define mapping from role signals to existing LSC-T1 extension fields and
  existing Learning Signal Intake fields;
- define external-agent returned-output eligibility through the external
  knowledge absorption chain map;
- define parking boundaries for AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, MLW8,
  runtime/provider/live/public-sync/CLI-MCP implementation.

Reviewer/closer closure scope:

- update this work order status and closure evidence;
- update the LSC-T2 GC-018 baseline status;
- create the LSC-T2 completion review;
- repair allowed-scope reference wording, manifests, or packet-shape defects
  required by machine gates before commit.

Forbidden scope:

- no edits to `EXTENSIONS/**`, `governance/compat/**`, tests, scripts, MCP,
  web UI, session state, active handoff, root startup routers, `.github/**`,
  dependency manifests, public-sync, or closed predecessor artifacts;
- no actual ledger source directory, generated aggregate, generator, checker,
  helper readout, runtime bridge, CLI/MCP adapter, provider/live proof,
  dependency install, queue/daemon, watcher, wrapper/proxy enforcement, direct
  IDE/shell/git/filesystem interception, arbitrary command execution, or
  EDIT/COMMIT execution;
- no public catalog update, public/production/release readiness, full-hook
  equivalence, cost optimization, speed claim, or universal
  governed-coding-control claim;
- no implementation of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 documentation/reference contract.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and record a source inventory in the worker
   return.
3. Update the Learning Signal Chain reference front door with an LSC-T2 row.
4. Create the LSC-T2 contract with role-specific eligibility, no-signal
   assertion guidance, role-signal mapping, false-positive prevention, and
   external-return routing.
5. Create the worker-return artifact with required packet shape and
   worker-experience token.
6. Run required helper/gate commands and record results.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- required gate commands and results;
- explicit statement that no source/runtime/test/session/handoff/public-sync
  paths were edited;
- explicit statement that no checker/helper/generator/CLI-MCP adapter was
  implemented;
- exact claim boundary and public export disposition.

## Acceptance Criteria

The worker return is acceptable only if:

- all Required Deliverables exist and no unauthorized paths are changed;
- the LSC-T2 contract defines role-specific capture eligibility for worker,
  reviewer or reviewer/closer, dispatch author or orchestrator, session-sync
  steward, operator, and external-agent returned-output signals;
- the contract defines no-signal assertion guidance so routine pass/acceptance
  work does not create unnecessary latency;
- the contract maps role signals to LSC-T1 fields without adding runtime fields;
- external-agent returned-output eligibility is bound to the external knowledge
  absorption chain map;
- parked lanes remain parked;
- required gates pass or any failure is classified as `BLOCKED_WITH_REASON`.

## Review Gate

The reviewer/closer must run reviewer-fast or a stricter applicable gate before
accepting the worker return. Acceptance requires checking source fidelity,
changed-set scope, public/provenance boundary, external-intake routing,
finding-to-governance disposition, Delta boundary N/A, and the worker-return
packet shape.

## Closure Checklist

Reviewer/closer closure evidence:

- Required deliverables exist: PASS.
- No forbidden paths changed: PASS.
- Source Verification claims remain current: PASS.
- Role-specific eligibility matrix is present: PASS.
- No-signal assertion guidance is present: PASS.
- External returned-output routing is bound to the chain map: PASS.
- Worker-return packet includes required sections and token: PASS.
- Reviewer-fast or stricter gate passes: PASS.
- Commit ownership remains reviewer/closer only: PASS.
- Session-sync is performed only if mode or next-move surfaces change: PASS.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all Required Deliverables are created
and required gate evidence is recorded. Return `BLOCKED_WITH_REASON` if the task
requires forbidden paths, runtime/source/test/checker/helper/generator
implementation, provider/live proof, public-sync, session-sync during worker
execution, dependency install, destructive actions, or parked-lane reopening.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_FOR_WORKER_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_COMPLETION_2026-06-21.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC-T2 dispatched and accepted by this closure; roadmap remains the governing LSC-T0 plan | PASS |
| Reference front door | `docs/reference/learning_signal_chain/README.md` | LSC-T2 row present | PASS |
| Reference contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Session continuity | active session front-door/state/handoff after material commit | session-sync follows material closure commit | N/A with reason |
| Registry JSON | N/A with reason: no generated JSON registry created or changed | no registry mutation | PASS |
| Registry Markdown | N/A with reason: no generated Markdown index created in LSC-T2 | no generated readout | PASS |
| External evidence digest | N/A with reason: no external benchmark/provider/live digest created | docs/reference closure only | N/A with reason |
| System loop interlock | N/A with reason: no runtime/source interlock changed | no runtime/source mutation | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: LSC-T2 creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: LSC-T2 performs no query acceptance | N/A_WITH_REASON |
| Worker-return acceptance | worker return present and accepted by reviewer/closer | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` documentation/reference contract closure only | PASS |

## Operator Checkpoint

Allowed-scope corrections are handled under the Worker Autonomy rule below.
Fresh operator authorization is required before any runtime/source/test
implementation, checker/helper/generator build, CLI/MCP adapter,
provider/live proof, public-sync, session-sync during worker execution, or
reopening of AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, or MLW8.

## Required First Reads

The worker must read these before editing:

- `docs/baselines/CVF_GC018_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_2026-06-21.md`
- `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`
- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`
- `governance/compat/check_worker_experience_retrospective.py`
- `docs/reference/worker_experience_retrospective/README.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`
- `docs/reference/guard_orientation/README.md`

## Pre-Flight Checks

Before implementation, the worker must run or record:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b2a90d52 --head HEAD
```

If the worktree contains unrelated dirty paths, the worker must preserve them
and avoid editing outside Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | worker | modify-listed |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | worker | create |
| `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md` | worker | create |
| Any other path | Not worker-owned | forbidden unless a revised work order authorizes it |

## Worker Autonomy / No-Question Rule

The worker must repair and rerun machine-check or packet-shape failures inside
Allowed scope. The worker must stop and return `BLOCKED_WITH_REASON` only if a
needed action would exceed Allowed scope, alter the claim boundary, require
runtime/source/test edits, provider/live proof, public-sync, secrets/quota,
dependency install, destructive actions, AAF-T6/T7/CGE-T3/ACE-R1/MLW7/MLW8
scope, or any forbidden path.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | stable reference front door plus stable LSC-T2 contract under `docs/reference/learning_signal_chain/` |
| Storage decision | extend the LSC reference family created by LSC-T1; do not create a ledger source directory |
| Existing aggregate impact | none in LSC-T2 |
| Generated state impact | none in LSC-T2; future generated Markdown index and drift checker remain separate tranches |
| Durable governance boundary | LSC-T2 defines role-capture eligibility only; it does not create an active ledger store |
| Index/readout boundary | no helper/readout implementation in LSC-T2 |

## Required Deliverables

The worker must leave exactly these uncommitted artifact changes:

- `docs/reference/learning_signal_chain/README.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`
- `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md`

## Required Contract Content

The LSC-T2 contract must include these sections:

- Purpose and scope.
- Source authority and non-authority inputs.
- Role vocabulary with role-neutral names and no provider/model/agent names.
- Capture Eligibility Matrix with separate rows for:
  - worker;
  - reviewer or reviewer/closer;
  - dispatch author or orchestrator;
  - session-sync steward;
  - operator;
  - external reviewer or external agent returned output;
  - runtime/provider/public-surface placeholders marked out of implementation
    scope.
- No-Signal Assertion Guidance that states when routine pass/acceptance work
  should not emit a signal.
- False Positive Prevention Rules.
- Mapping to LSC-T1 fields: `sourceProjection`, `rootCauseGroupId`,
  `captureState`, `repeatRisk`.
- Mapping to existing intake fields: `sourceId`, `sourceArtifact`,
  `sourceSummary`, `lane`, `defectClass`, `severity`, `disposition`,
  `nextControlAction`, `evidenceBasis`, and `autonomousMutationAuthorized`.
- External Agent Returned-Output Routing through the external knowledge
  absorption chain map.
- Latency Budget: short capture, slow promotion, and no closure blocker for
  lower-severity unresolved signals unless a future checker authorizes it.
- Parking ledger for AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, and MLW8.
- Public Export Disposition.
- Delta Execution Claim Boundary Control Block.
- Claim Boundary.

## New Doc-Only Fields

| Proposed field or term | Owner in LSC-T2 | Runtime status | Reason |
|---|---|---|---|
| `captureEligibility` | LSC-T2 reference contract | DOC_ONLY_NEW | names role-specific conditions for when a signal should be captured |
| `noSignalAssertion` | LSC-T2 reference contract | DOC_ONLY_NEW | prevents routine work from becoming retrospective latency |
| `roleSignalSurface` | LSC-T2 reference contract | DOC_ONLY_NEW | describes the role-owned artifact surface where a signal may be declared |
| `externalReturnEligibility` | LSC-T2 reference contract | DOC_ONLY_NEW | binds external-agent returned outputs to chain-map classification before CVF promotion |

These fields are documentation/reference vocabulary only. They must not be used
as Source Verification ACCEPT rows or claimed as current runtime fields.

## Current Runtime Freshness Verification

| Runtime surface | Verification | Disposition |
|---|---|---|
| Runtime/source implementation | N/A with reason: LSC-T2 authorized documentation/reference contract work only | NOT_APPLICABLE_WITH_REASON |
| Provider/live behavior | N/A with reason: no provider/live proof authorized or claimed | NOT_APPLICABLE_WITH_REASON |
| CLI/MCP adapter behavior | N/A with reason: external-agent returned-output routing is a contract boundary only | NOT_APPLICABLE_WITH_REASON |
| Ledger store/source directory/generator/drift checker/helper readout | N/A with reason: future LSC implementation tranche only | NOT_APPLICABLE_WITH_REASON |
| Public-sync behavior | N/A with reason: private provenance closure only | NOT_APPLICABLE_WITH_REASON |
| Checker/helper enforcement | N/A with reason: LSC-T2 adds no machine check or helper implementation | NOT_APPLICABLE_WITH_REASON |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement |
|---|---|
| LSC-T2 extends capture beyond workers | Required Contract Content and Capture Eligibility Matrix |
| Separate eligibility per role to avoid false positives | Required Contract Content and No-Signal Assertion Guidance |
| Preserve capture-fast, promotion-slow | Latency Budget and Forbidden scope |
| Support external CLI/MCP agents without chat memory | External returned-output routing and minimal payload boundary |
| Extend existing intake/LSC-T1 fields, no parallel core | Source Verification Block and Required Contract Content |
| Preserve parked lanes | Forbidden scope and Parking ledger requirement |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 includes reviewer/orchestrator/operator friction and external-agent critique in the Learning Signal Chain purpose | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 14, 53-56 | reviewer/orchestrator/operator friction; external-agent CLI/MCP readiness | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines unified signal classes for reviewer, orchestrator, operator, and external-agent signals | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 131-138 | `REVIEWER_FRICTION`; `ORCHESTRATOR_FRICTION`; `OPERATOR_CORRECTION`; `EXTERNAL_AGENT_CRITIQUE` | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines `actorRole` as role-neutral | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 173 | `actorRole` | LSC-T0 roadmap minimal signal event contract | ACCEPT |
| LSC-T0 identifies LSC-T2 as Multi-Role Capture Contract with separate eligibility per role | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 253 | `LSC-T2`; Multi-Role Capture Contract | LSC-T0 work plan | ACCEPT |
| LSC-T0 requires capture-fast and promotion-slow latency behavior | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 197-213 | Latency Budget; blocking rule | LSC-T0 roadmap | ACCEPT |
| LSC-T1 owns allowed LSC extension fields for source projection, root cause grouping, capture state, and repeat risk | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 72-86 | `sourceProjection`; `rootCauseGroupId`; `captureState`; `repeatRisk` | LSC-T1 contract | ACCEPT |
| LSC-T1 defines `disposition` as governed source of truth and `captureState` as derived/advisory | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 117-139 | `disposition`; `captureState` | LSC-T1 contract | ACCEPT |
| LSC-T1 defines CLI/MCP minimal payload boundary but no adapter implementation | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 202-210 | CLI/MCP minimal payload | LSC-T1 contract | ACCEPT |
| LSC-T1 keeps AAF-T6/T7, CGE-T3, ACE-R1, and MLW7/8 parked | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 212-221 | Parking Ledger | LSC-T1 contract | ACCEPT |
| Existing intake bridge owns lane, defect class, severity, disposition, input, record, and autonomous mutation false invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 11-65, 123-170 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| AAF-T5 checker owns existing worker-experience token names and friction levels only for eligible worker-return artifacts | `governance/compat/check_worker_experience_retrospective.py` | lines 5-10, 34-56, 165-192 | `WORKER_EXPERIENCE_RETRO`; `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`; `FRICTION_LEVELS` | worker-experience checker | ACCEPT |
| Worker-experience standard owns existing worker token syntax and exact no-friction assertion | `docs/reference/worker_experience_retrospective/README.md` | lines 23-25, 54-68 | token block; exact NA assertion | worker-experience standard | ACCEPT |
| External-agent returned output must be classified through the external knowledge absorption chain before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 25, 55-66, 73-75, 90 | External-agent returned output | external knowledge absorption chain map | ACCEPT |

## Work-Order Fulfillment Manifest

| Required artifact | Required content | Worker disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | LSC-T2 row added to current contracts and no implementation claim | modify-listed |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | multi-role capture eligibility, no-signal guidance, mapping, boundaries | create |
| `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md` | worker return with evidence and token | create |

## Required Artifact Manifest

| Required artifact | Required content | Owner | Disposition |
|---|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | LSC-T2 row added to current contracts and no implementation claim | worker | ACCEPT |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | multi-role capture eligibility, no-signal guidance, mapping, boundaries | worker | ACCEPT |
| `docs/reviews/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_WORKER_RETURN_2026-06-21.md` | worker return with evidence and token | worker | ACCEPT |

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed:

| Packet item | Worker-return disposition |
|---|---|
| Purpose section | MUST_INCLUDE |
| Scope / Methodology section | MUST_INCLUDE |
| Findings / Position section | MUST_INCLUDE |
| Risk / Corrective Action section | MUST_INCLUDE |
| Work-Order Fulfillment Manifest section | MUST_INCLUDE |
| Source Inventory or equivalent source ledger | MUST_INCLUDE |
| Agent Operation Trace Block section | MUST_INCLUDE |
| Delta Execution Claim Boundary Control Block section | MUST_INCLUDE |
| External Knowledge Intake Routing section | MUST_INCLUDE |
| Rescan Intelligence Hardening section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Corpus Completeness And Report Integrity section | MUST_INCLUDE_OR_NA_WITH_REASON |
| Finding-To-Governance Learning Disposition section | MUST_INCLUDE |
| Epistemic Process Block section | MUST_INCLUDE_OR_EPISTEMIC_PROCESS_NA_WITH_REASON |
| Machine Closure Package section | MUST_INCLUDE_OR_NA_WITH_REASON; worker must not mark closure |
| Public Export Disposition section | MUST_INCLUDE |
| Claim Boundary section | MUST_INCLUDE |
| `executionBaseHead` | exact value from `git rev-parse --short HEAD` |
| `git status --short` | exact output after worker changes |
| Worker-experience token | structured `WORKER_EXPERIENCE_RETRO` or exact asserting `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` |

Conditional sections must not be omitted silently. If not applicable, the worker
must include the section with `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON`, and state why it is not applicable to this
docs-only tranche.

## Test And Gate Requirements

The worker must run or record:

```powershell
python governance/compat/run_agent_automation_assist.py --base b2a90d52 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T2 moves multi-role
  capture from deferred roadmap item to dispatch-ready contract work.
- Routing matrix status: `DO_NOW` for LSC-T2 documentation/reference contract;
  `SEPARATE_RUNTIME_TRANCHE` for checker/helper/generator/drift/CLI-MCP/
  runtime work; `STRATEGIC_OPERATOR_DECISION` for AAF-T6/T7, CGE-T3, ACE-R1,
  MLW7/8; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/
  readiness claims.
- Semantic sampling status: sampled LSC-T0 LSC-T2 row, LSC-T1 extension fields,
  AAF-T5 token source, and external returned-output routing.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T2 multi-role capture moved from roadmap row into dispatch requirements. |
| NEW_FINDING | Multi-role capture requires no-signal assertions to avoid creating new latency. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected for LSC-T2. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T2 documentation/reference multi-role capture contract. |
| SEPARATE_RUNTIME_TRANCHE | checker, helper readout, generator, drift checker, CLI/MCP adapter, runtime bridge. |
| STRATEGIC_OPERATOR_DECISION | AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, MLW8 ordering after LSC-T2. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | extend LSC-T1 field/de-dup contract instead of creating a parallel signal core. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T2-S1 | LSC-T0 work plan | LSC-T2 extends capture beyond workers | mapped into Required Deliverables | prevents worker-only learning blind spot | PASS |
| LSC-T2-S2 | LSC-T1 extension fields | LSC owns `sourceProjection`, `rootCauseGroupId`, `captureState`, `repeatRisk` | reused by T2 contract | avoids new runtime schema | PASS |
| LSC-T2-S3 | External chain map | external-agent returned output needs classification | routed through External Knowledge Intake | prevents external output becoming authority by shortcut | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T2 is a bounded
  documentation/reference contract, not a corpus enumeration or legacy scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block and Required First Reads; no corpus enumeration command is
  authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and Work-Order Fulfillment Manifest above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=corpus enumeration and legacy scan surfaces out of scope; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: corpus scan, legacy source-family enumeration,
  public-sync copy, runtime/provider/live proof, and parked lanes.
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
| Chain map route | returned output to finding classification to governed work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T2 multi-role capture contract and eligibility matrix |
| Disposition | ADAPT as CVF-owned Learning Signal Chain role-capture contract |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T2 multi-role capture contract work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference contract authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | multi-role capture eligibility, no-signal assertion, and external-return routing contract only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker-only capture leaves reviewer/orchestrator/operator friction chat-only | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | worker contract must define role-specific capture eligibility | handled by this work order |
| Multi-role capture can create latency if every role must write long retrospectives | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | worker contract must define no-signal assertions and fast capture shape | handled by this work order |
| External-agent returned output needs classification before becoming CVF authority | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | worker contract must bind external returns to the chain map | handled by this work order |
| Runtime/provider/cost applicability for this work order | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this work order | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order for Learning Signal Chain contract work.
No public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Commit Prompt Readiness

| Field | Disposition |
|---|---|
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` |
| Worker return token | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Reviewer commit owner | reviewer/closer role after accepted worker return |
| Material commit scope | LSC-T2 required deliverables only |
| Session-sync | reviewer/closer only if mode or next-move surfaces change |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | LSC-T2 dispatch authoring, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | `apply_patch` file edits plus governance checks |
| Target paths | `docs/baselines/CVF_GC018_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_FOR_WORKER_2026-06-21.md` |
| Allowed scope source | operator instruction for LSC-T2 after lane-selection audit; LSC-T0 roadmap; LSC-T1 closure artifacts |
| Before status evidence | clean worktree at committed base `b2a90d52` |
| After status evidence | LSC-T2 GC-018 and work order created |
| Diff evidence | `git status --short` and dispatch gates on range `b2a90d52..HEAD` |
| Approval boundary | operator authorized LSC-T2 dispatch; no worker implementation or commit by worker |
| Claim boundary | dispatch authoring only; no runtime/source/test/session/public-sync implementation |
| Agent type | dispatcher role |
| Invocation ID | `lsc-t2-dispatch-authoring-2026-06-21` |
| Expected manifest | LSC-T2 GC-018 and LSC-T2 work order |
| Actual changed set | `docs/baselines/CVF_GC018_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX_FOR_WORKER_2026-06-21.md` |
| Manifest delta | MATCH |

## Claim Boundary

This work order authorizes only LSC-T2 documentation/reference contract
artifacts. It does not implement a ledger store, generator, drift checker,
helper readout, runtime Learning Plane mutation, provider/live proof, CLI/MCP
adapter behavior, public-sync, direct IDE/shell/git/filesystem interception,
wrapper/proxy enforcement, queue/daemon, watcher, readiness, cost optimization,
full-hook equivalence, or universal governed-coding control.
