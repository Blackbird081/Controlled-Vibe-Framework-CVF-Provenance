# CVF Agent Work Order - LSC-T4 Promotion Threshold Policy

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-21

docType: work_order

dispatchBaseHead: cae048a3

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T4_PROMOTION_THRESHOLD_POLICY_FOR_WORKER_2026-06-21.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: LSC-T4 is a documentation/reference policy tranche only.
Its prerequisite is satisfied by LSC-T2 material closure commit `00214e9a` and
session-sync commit `cae048a3`. It follows the operator-selected roadmap order:
`LSC-T2 -> LSC-T4 -> LSC-T3 -> LSC-T6 -> LSC-T5/T7`. The mission is to define
promotion thresholds before the fast helper readout tranche, so future helpers
can show unresolved signals without turning every signal into a blocker.

Do-not-misread notes: do not build a checker, helper, ledger store, source
directory, generator, drift checker, CLI/MCP adapter, runtime bridge, provider
route, public-sync artifact, source implementation, or latency guard. Do not
edit `EXTENSIONS/**`, `governance/compat/**`, tests, scripts, session state,
active handoff, root startup routers, public-sync, or dependency manifests. Do
not reopen LSC-T3, LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1,
MLW7, or MLW8.

Required first actions: read this work order, read the LSC-T4 GC-018 baseline,
read the LSC-T0 roadmap, read the LSC reference front door, read the LSC-T1 and
LSC-T2 contracts, read the source files named in the Source Verification Block,
confirm actual `executionBaseHead`, and inspect current `git status --short`.

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
| baseHeadFor(phase) | `dispatchBaseHead=cae048a3`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending LSC-T4 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix LSC-T4 with LSC-T3, LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7/8, runtime/provider/live, MCP, public-sync, queue/daemon, direct-interception, or checker/helper implementation |
| Before status evidence | clean worktree at committed dispatch base `cae048a3`; `git status --short` was clean before LSC-T4 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY_COMPLETION_2026-06-21.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted LSC front door update; accepted LSC-T4 policy; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator roadmap order, LSC-T0 roadmap, LSC-T1 and LSC-T2 closure artifacts |
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
| Reason | LSC-T4 is derived from the current LSC roadmap and accepted LSC-T1/T2 reference contracts, not a raw `.private_reference/legacy` corpus scan or LHW wave. |
| Coverage evidence used instead | LSC-T0 roadmap, LSC reference front door, LSC-T1 contract, LSC-T2 contract, Learning Signal Intake Bridge, and external knowledge absorption chain map. |

## Required First Reads

The worker must read these sources before editing:

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and role-neutrality rule |
| `docs/baselines/CVF_GC018_LSC_T4_PROMOTION_THRESHOLD_POLICY_2026-06-21.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T4_PROMOTION_THRESHOLD_POLICY_FOR_WORKER_2026-06-21.md` | current work order and packet shape |
| `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | LSC roadmap, latency budget, and LSC-T4 row |
| `docs/reference/learning_signal_chain/README.md` | LSC reference front door to update |
| `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | source-layout, de-dup, and field ownership |
| `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | role capture and closure-blocking boundary |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | existing intake fields and false autonomous mutation invariant |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external-agent returned-output routing boundary |

## Pre-Flight Checks

The worker must run or record these checks before returning:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_automation_assist.py --base cae048a3 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/learning_signal_chain/README.md` | worker | may update only to add the LSC-T4 row |
| `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | worker | create |
| `docs/reviews/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY_WORKER_RETURN_2026-06-21.md` | worker | create |
| `docs/baselines/CVF_GC018_LSC_T4_PROMOTION_THRESHOLD_POLICY_2026-06-21.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T4_PROMOTION_THRESHOLD_POLICY_FOR_WORKER_2026-06-21.md` | reviewer/closer | no worker edit |
| session state, active handoff, public-sync, source, tests, checkers, scripts, runtime paths | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
runtime/source/test/checker/helper/generator/CLI-MCP/provider/live/public-sync
scope, parked-lane reopening, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Create the LSC-T4 promotion threshold policy so CVF can decide, without asking
the operator for every signal, whether a captured signal should remain readout
only, be watched for recurrence, become a governance proposal, or be promoted
as a rule/checker/work-order candidate.

Success means future roles can read one policy and know:

- which signals stay visible but non-blocking;
- when repeated signals cross the line into governance action;
- when severity or repeat evidence can block closure;
- when a proposed next control action should be a rule, checker, or work order;
- how promotion stays governed and does not authorize autonomous mutation.

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
| Operator instruction | 2026-06-21 roadmap order selecting LSC-T4 with LSC-T2 already closed at material commit `00214e9a` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| LSC-T4 GC-018 | `docs/baselines/CVF_GC018_LSC_T4_PROMOTION_THRESHOLD_POLICY_2026-06-21.md` | ACCEPT |
| LSC-T0 roadmap | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | ACCEPT |
| LSC reference front door | `docs/reference/learning_signal_chain/README.md` | ACCEPT |
| LSC-T1 contract | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | ACCEPT |
| LSC-T2 contract | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | ACCEPT |
| Learning Signal Intake Bridge | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | SOURCE_AUTHORITY_FOR_EXISTING_INTAKE_FIELDS |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_RETURN_ROUTING |

## Scope / Target / Owner Boundary

Allowed scope:

- update `docs/reference/learning_signal_chain/README.md` to list LSC-T4;
- create `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md`;
- create `docs/reviews/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY_WORKER_RETURN_2026-06-21.md`;
- update `docs/baselines/CVF_GC018_LSC_T4_PROMOTION_THRESHOLD_POLICY_2026-06-21.md` status during reviewer/closer closure;
- create `docs/reviews/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY_COMPLETION_2026-06-21.md` during reviewer/closer closure;
- define promotion threshold categories and a decision matrix;
- define blocking-vs-readout behavior using existing LSC-T1 and intake fields;
- define how role-captured signals from LSC-T2 are triaged without requiring a
  long retrospective for routine work;
- define future routing to LSC-T3 helper readout, LSC-T5 Learning Plane bridge,
  LSC-T6 external CLI/MCP signal contract, and LSC-T7 latency guard without
  implementing those tranches.

Reviewer/closer closure scope:

- update this work order status and closure evidence;
- update the LSC-T4 GC-018 baseline status;
- create the LSC-T4 completion review;
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
- no implementation of LSC-T3, LSC-T5, LSC-T6, LSC-T7, AAF-T6, AAF-T7, CGE-T3,
  ACE-R1, MLW7, or MLW8.

Risk ceiling: R1 documentation/reference policy.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and record a source inventory in the worker
   return.
3. Update the Learning Signal Chain reference front door with an LSC-T4 row.
4. Create the LSC-T4 policy with a promotion decision matrix, blocking-vs-readout
   thresholds, repeated-signal rules, role-signal handling, and future-tranche
   routing.
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

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed, so reviewer-fast can validate the packet without
reviewer repair:

| Packet item | Worker-return disposition |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| `executionBaseHead` | exact value from `git rev-parse --short HEAD` at worker start |
| `dispatchBaseHead` | `cae048a3` |
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

Within Allowed scope, the worker must repair machine-gate or packet-shape
defects and rerun the relevant gate without asking the operator or dispatcher.
This includes missing required sections, packet-shape rows, source-inventory
format, LSC reference-front-door row wording, claim-boundary wording, and
documentation-only terminology inside the Required Deliverables.

The worker must stop and return `BLOCKED_WITH_REASON` only when the repair would
exceed Allowed scope, change the claim boundary, require runtime/source/test/
checker/helper/generator/CLI-MCP/provider/live/public-sync/session-sync edits,
consume secrets or quota, alter parked-lane ordering, touch forbidden paths, or
perform destructive or irreversible actions.

## Acceptance Criteria

The worker return is acceptable only if:

- all Required Deliverables exist and no unauthorized paths are changed;
- the LSC-T4 policy defines at least five promotion outcomes:
  `READOUT_ONLY`, `WATCH_FOR_REPEAT`, `GOVERNANCE_PROPOSAL_CANDIDATE`,
  `RULE_CANDIDATE`, `CHECKER_CANDIDATE`, `WORK_ORDER_CANDIDATE`, and
  `CLOSURE_BLOCKER`;
- the policy defines when a lower-severity signal remains readout-only;
- the policy defines how `repeatRisk=OBSERVED_REPEATED` and shared
  `rootCauseGroupId` change promotion eligibility without creating duplicate
  counts;
- the policy preserves the LSC-T0/T2 closure blocker rule: routine unresolved
  signals do not block closure unless `severity=critical`,
  `repeatRisk=OBSERVED_REPEATED`, or a governing work order explicitly tightens
  the rule;
- the policy distinguishes rule, checker, and work-order candidates by the kind
  of control gap, not by provider/model/agent identity;
- the policy states that promotion never authorizes autonomous mutation and
  always requires governed review/GC-018/work-order authority before action;
- parked lanes remain parked;
- required gates pass or any failure is classified as `BLOCKED_WITH_REASON`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source | Work-order implementation | Disposition |
|---|---|---|---|
| LSC-T4 defines repeated-signal thresholds and blocking-vs-readout behavior | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` line 255 | Required LSC-T4 policy with promotion matrix and blocker rules | SATISFIED_BY_DISPATCH |
| Capture remains fast and promotion remains governed | LSC-T0 lines 33-39 and 197-204 | Purpose, Acceptance Criteria, and Claim Boundary forbid automatic promotion | SATISFIED_BY_DISPATCH |
| Lower-severity unresolved signals should appear in helper/readout output rather than block closure | LSC-T0 lines 212-213 | Acceptance Criteria require readout-only lower-severity handling | SATISFIED_BY_DISPATCH |
| T3 helper readout should follow, not precede, threshold policy | Operator-selected 2026-06-21 roadmap order | Current-time notes and Future-Tranche Routing keep LSC-T3 as the next candidate tranche once LSC-T4 is accepted | SATISFIED_BY_DISPATCH |
| Existing intake bridge remains the field owner for severity/disposition/action evidence | LPF intake bridge lines 39-65 and 163-170 | Source Verification and Acceptance Criteria bind T4 to existing fields | SATISFIED_BY_DISPATCH |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| LSC-T0 names the governing principle "Fast capture, slow promotion" | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 33-39 | Fast capture, slow promotion | LSC-T0 roadmap | ACCEPT |
| LSC-T0 states promotion remains governed, reviewed, and non-blocking for routine capture | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 36-57 | promotion boundaries | LSC-T0 roadmap | ACCEPT |
| LSC-T0 defines promotion as fresh GC-018, work order, or checker only when justified | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 197-204 | Promotion | LSC-T0 latency budget | ACCEPT |
| LSC-T0 states lower-severity unresolved signals should appear in helper/readout output and not block routine closure | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 212-213 | lower-severity unresolved signals | LSC-T0 blocking rule | ACCEPT |
| LSC-T0 defines LSC-T4 as Promotion Threshold Policy with repeated-signal thresholds and blocking-vs-readout behavior | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | line 255 | `LSC-T4`; Promotion Threshold Policy | LSC-T0 work plan | ACCEPT |
| LSC-T0 requires future work orders to keep capture fast and promotion governed | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` | lines 301-316 | Acceptance Criteria For Future Work Orders | LSC-T0 roadmap | ACCEPT |
| LSC-T1 owns allowed LSC extension fields for projection, root-cause grouping, capture state, and repeat risk | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 72-86 | `sourceProjection`; `rootCauseGroupId`; `captureState`; `repeatRisk` | LSC-T1 contract | ACCEPT |
| LSC-T1 says `rootCauseGroupId` is ledger-minted and projection de-dup must not inflate counts | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 143-173 | `rootCauseGroupId`; Projection De-Dup Rule | LSC-T1 contract | ACCEPT |
| LSC-T1 leaves generator and drift checker implementation to future work | `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md` | lines 185-199 | generator; drift checker | LSC-T1 contract | ACCEPT |
| LSC-T2 defines role-specific capture eligibility and preserves no-signal guidance | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 77-112 | Capture Eligibility Matrix; No-Signal Assertion Guidance | LSC-T2 contract | ACCEPT |
| LSC-T2 maps role signals to existing LSC-T1 fields without adding runtime fields | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 141-149 | Mapping To LSC-T1 Fields | LSC-T2 contract | ACCEPT |
| LSC-T2 preserves closure blocking only for critical severity or observed repeated repeat risk | `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md` | lines 194-202 | Latency Budget; Closure | LSC-T2 contract | ACCEPT |
| Existing intake bridge owns severity, disposition, nextControlAction, evidenceBasis, and autonomous mutation false invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | lines 39-65, 163-170 | `LearningSignalIntakeInput`; `LearningSignalIntakeRecord`; `autonomousMutationAuthorized` | LPF intake bridge | ACCEPT |
| External-agent returned output must be classified through the external knowledge absorption chain before governed action | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | lines 44-66, 73-75, 90-91 | External-agent returned output | external knowledge absorption chain map | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in LSC-T4 | Runtime status | Reason |
|---|---|---|---|
| `READOUT_ONLY` | LSC-T4 reference policy | DOC_ONLY_NEW | signal remains visible to helper/readout but does not trigger governance action |
| `WATCH_FOR_REPEAT` | LSC-T4 reference policy | DOC_ONLY_NEW | signal is weak alone but should be grouped by `rootCauseGroupId` if observed again |
| `GOVERNANCE_PROPOSAL_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | signal may become a written proposal or finding after review |
| `RULE_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | repeated or high-impact prose-rule gap may justify a rule update |
| `CHECKER_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | repeated or closure-costly machine-verifiable gap may justify checker work |
| `WORK_ORDER_CANDIDATE` | LSC-T4 reference policy | DOC_ONLY_NEW | bounded implementation or documentation work may be dispatched through GC-018 |
| `CLOSURE_BLOCKER` | LSC-T4 reference policy | DOC_ONLY_NEW | closure should pause only under critical or observed-repeated conditions already allowed by LSC-T0/T2 |

## Required Contract Content

The LSC-T4 policy must include these sections:

- Purpose
- Scope
- Promotion Principles
- Promotion Outcome Vocabulary
- Threshold Decision Matrix
- Blocking-Vs-Readout Policy
- Repeated-Signal And De-Dup Policy
- Rule / Checker / Work-Order Candidate Split
- Role-Signal Promotion Rules
- External-Agent Signal Promotion Rules
- Future-Tranche Routing
- Latency Budget
- Parking Ledger
- Public Export Disposition
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Claim Boundary

Required policy assertions:

- `READOUT_ONLY` is the default for first-observed low/medium signals without a
  concrete repeated root cause.
- `WATCH_FOR_REPEAT` requires a plausible repeatable root cause but lacks enough
  evidence for immediate governance action.
- `GOVERNANCE_PROPOSAL_CANDIDATE` requires concrete evidence and a named owner
  surface.
- `RULE_CANDIDATE` is for prose governance gaps where a written rule would
  prevent recurrence.
- `CHECKER_CANDIDATE` is for deterministic, machine-verifiable gaps that have
  repeated, caused closure latency, or escaped earlier phase gates.
- `WORK_ORDER_CANDIDATE` is for bounded implementation or documentation work
  that needs GC-018 and source verification.
- `CLOSURE_BLOCKER` is reserved for `severity=critical`,
  `repeatRisk=OBSERVED_REPEATED`, or a governing work order that explicitly
  tightens the closure rule.
- Promotion recommendation is not promotion execution.
- `autonomousMutationAuthorized=false` remains invariant.

## Review Gate

The reviewer/closer must run reviewer-fast or a stricter applicable gate before
accepting the worker return. Acceptance requires checking source fidelity,
changed-set scope, public/provenance boundary, external-intake routing,
finding-to-governance disposition, Delta boundary N/A, and the worker-return
packet shape.

## Closure Checklist

Reviewer/closer closure evidence must resolve these items:

- Required deliverables exist.
- No forbidden paths changed.
- Source Verification claims remain current.
- Promotion outcome vocabulary is present.
- Threshold decision matrix is present.
- Blocking-vs-readout policy preserves LSC-T0/T2 latency rule.
- Repeated-signal and de-dup policy reuse LSC-T1 fields.
- Rule/checker/work-order candidate split is present.
- Worker-return packet includes required sections and token.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all Required Deliverables are created
and required gate evidence is recorded. Return `BLOCKED_WITH_REASON` if the task
requires forbidden paths, runtime/source/test/checker/helper/generator
implementation, provider/live proof, public-sync, session-sync during worker
execution, dependency install, destructive actions, or parked-lane reopening.

## Current Runtime Freshness Verification

| Claim | Freshness evidence | Disposition |
|---|---|---|
| Runtime/source implementation is not authorized | Allowed and Forbidden scope in this work order | N/A_WITH_REASON |
| Checker/helper/generator implementation is not authorized | Forbidden scope and Required Deliverables | N/A_WITH_REASON |
| CLI/MCP adapter behavior is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Provider/live proof is not authorized | Forbidden scope and Claim Boundary | N/A_WITH_REASON |
| Public-sync is not authorized | Public route and Public Export Disposition | N/A_WITH_REASON |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`.
- Predecessor intake artifact: `docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md`.
- Predecessor capture artifact: `docs/reference/learning_signal_chain/CVF_LSC_T2_MULTI_ROLE_CAPTURE_CONTRACT_AND_ELIGIBILITY_MATRIX.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because LSC-T4 moves promotion
  thresholds from the roadmap row into dispatch-ready policy work.
- Routing matrix status: `DO_NOW` for LSC-T4 documentation/reference policy;
  `SEPARATE_RUNTIME_TRANCHE` for checker/helper/generator/drift/CLI-MCP/
  runtime work; `STRATEGIC_OPERATOR_DECISION` for LSC-T3/T5/T6/T7 after
  LSC-T4; `OUT_OF_SCOPE` for provider/live/public-sync/direct-interception/
  readiness claims.
- Semantic sampling status: sampled LSC-T0 LSC-T4 row, LSC-T0 latency budget,
  LSC-T1 de-dup fields, LSC-T2 latency budget, and LPF intake fields.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | LSC remains capture-fast, promotion-slow, and proposal-only. |
| CHANGED_DISPOSITION | LSC-T4 promotion thresholds moved from roadmap row into dispatch requirements. |
| NEW_FINDING | Promotion policy must distinguish readout-only signals from rule/checker/work-order candidates before a fast helper is useful. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected for LSC-T4. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | LSC-T4 documentation/reference promotion threshold policy. |
| SEPARATE_RUNTIME_TRANCHE | checker, helper readout, generator, drift checker, CLI/MCP adapter, runtime bridge. |
| STRATEGIC_OPERATOR_DECISION | LSC-T3, LSC-T5, LSC-T6, LSC-T7 remain future operator-selected tranches; current dispatch does not authorize them. |
| OUT_OF_SCOPE | provider/live, public-sync, direct interception, readiness, universal control. |
| RESOLVED_BY_DESIGN | extend LSC-T1/T2 field and capture contracts instead of creating a parallel signal core. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| LSC-T4-S1 | LSC-T0 latency budget | capture is fast; promotion is slower and governed | mapped into Required Deliverables | prevents automatic promotion of routine notes | PASS |
| LSC-T4-S2 | LSC-T0 work plan | LSC-T4 defines repeated thresholds and blocking-vs-readout behavior | mapped into Required Deliverables | prevents helper readout before promotion semantics exist | PASS |
| LSC-T4-S3 | LSC-T1 de-dup fields | repeat risk and root-cause grouping belong to LSC field layer | reused by T4 policy | avoids duplicate count inflation | PASS |
| LSC-T4-S4 | LSC-T2 closure rule | closure blocking remains critical or observed repeated only | reused by T4 blocker policy | avoids new low-severity blockers | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - LSC-T4 is a bounded
  documentation/reference policy, not a corpus enumeration or legacy scan.
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
| Chain map route | returned output to finding classification to governed baseline/work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | LSC-T4 promotion threshold policy |
| Disposition | ADAPT as CVF-owned Learning Signal Chain promotion-threshold policy |
| Claim boundary | external-agent returns remain input only until classified and promoted through governed CVF artifacts |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T4 promotion threshold policy dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation/reference policy authoring only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | promotion threshold, readout-vs-promotion, and closure-blocking policy only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for Learning Signal Chain policy work. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | LSC-T4 dispatch authoring, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | local file edits and governance gates |
| Target paths | `docs/baselines/CVF_GC018_LSC_T4_PROMOTION_THRESHOLD_POLICY_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T4_PROMOTION_THRESHOLD_POLICY_FOR_WORKER_2026-06-21.md` |
| Allowed scope source | operator-selected LSC roadmap order and active session next allowed move |
| Before status evidence | clean worktree at committed base `cae048a3`; `git status --short` clean before dispatch authoring |
| After status evidence | two uncommitted dispatch artifacts created for pre-dispatch review |
| Diff evidence | new GC-018 baseline and new worker dispatch packet |
| Approval boundary | dispatcher role may create dispatch artifacts only; worker remains `WORKER_MUST_NOT_COMMIT` |
| Claim boundary | documentation/reference policy dispatch only; no runtime/source/checker/helper implementation |
| Agent type | dispatcher role |
| Invocation ID | `lsc-t4-dispatch-2026-06-21` |
| Expected manifest | LSC-T4 GC-018 and LSC-T4 worker dispatch packet |
| Actual changed set | `docs/baselines/CVF_GC018_LSC_T4_PROMOTION_THRESHOLD_POLICY_2026-06-21.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T4_PROMOTION_THRESHOLD_POLICY_FOR_WORKER_2026-06-21.md` |
| Manifest delta | MATCH |

## Claim Boundary

This work order authorizes only LSC-T4 documentation/reference policy work for
promotion thresholds and blocking-vs-readout behavior. It does not implement a
ledger store, generator, drift checker, helper readout, runtime Learning Plane
mutation, provider/live proof, CLI/MCP adapter behavior, public-sync, direct
interception, wrapper/proxy enforcement, queue/daemon, watcher, readiness, cost
optimization, full-hook equivalence, or universal governed-coding control.
