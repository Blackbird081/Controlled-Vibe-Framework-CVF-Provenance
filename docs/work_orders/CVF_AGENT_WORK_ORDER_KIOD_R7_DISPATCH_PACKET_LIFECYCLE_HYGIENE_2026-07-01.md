# CVF Agent Work Order - KIOD-R7 Dispatch Packet Lifecycle Hygiene

Memory class: FULL_RECORD

rawMemoryReleased=false

Status: CLOSED_PASS_BOUNDED

Date: 2026-07-01

docType: work_order

dispatchBaseHead: b743c085

executionBaseHead: RECORD_AT_WORKER_START_AFTER_DISPATCH_SYNC

closureBaseHead: ca790a48

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer remains separate.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md`

Paired baseline:
`docs/baselines/CVF_GC018_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: KIOD-R6 Memory Foundation Enrichment is
`CLOSED_PASS_BOUNDED` at material commit `8b89fc64`; active handoff is
`AGENT_HANDOFF_V30_2026-07-01.md`; current mode is
`kiod_r6_memory_foundation_enrichment_accepted_pending_operator_next_lane_selection`.

Do-not-misread notes: this is not KIOD-R6 rework, not a source-absorption
tranche, not runtime/provider work, not public-sync, not Web/UI/dashboard work,
and not package lifecycle promotion. The worker must not commit.

Required first actions: read this work order, the paired GC-018 baseline,
`CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, the active handoff named by the state
registry, `docs/reference/guard_orientation/README.md`, and
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
Then read all checker sources named in the Checker Source Read-Ahead Block
before writing any artifact.

Return contract: worker returns one uncommitted `COMPLETE_PENDING_REVIEW`
artifact under `docs/reviews/` and does not commit.

## Paired Baseline

`docs/baselines/CVF_GC018_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md`

## Scope

Allowed scope: implement a conservative dispatch-packet lifecycle hygiene
standard, checker, focused tests, and local hook/autorun catalog wiring.

Forbidden scope: runtime/provider behavior, live/API proof, source import,
public-sync, Web/UI/dashboard changes, MCP/CLI adapter implementation, package
activation or lifecycle promotion, generated package index mutation, session
state or active handoff edits by the worker, broad dispatch-quality refactor,
or any KIOD-R6 deferred-candidate closure.

## Purpose

Prevent repeated stale dispatch lifecycle mistakes before they reach the
operator or worker. The desired control is a narrow checker that catches
changed dispatch-ready artifacts when they contradict current active handoff,
active session state, or clearly closed lane evidence, and catches clear
provider-specific normative role assignment in dispatch packets.

## Authority Chain

| Authority | Source path | Verified line/section | Disposition |
| --- | --- | --- | --- |
| Active startup state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | lines 3-5 | ACCEPT |
| Active handoff KIOD-R6 closure | `AGENT_HANDOFF_V30_2026-07-01.md` | lines 52-75, 172-183 | ACCEPT |
| Guard orientation work-order/checker guidance | `docs/reference/guard_orientation/README.md` | lines 79-82, 89, 115 | ACCEPT |
| Dispatch quality checker source | `governance/compat/check_work_order_dispatch_quality.py` | lines 69-84, 202 | ACCEPT |
| Checker read-ahead checker source | `governance/compat/check_governed_artifact_checker_read_ahead.py` | lines 22-36, 153-214 | ACCEPT |
| Agent handoff contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 107-108, 243-249, 292-307 | ACCEPT |
| Tranche commit choreography | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | lines 58-68, 230-238, 277-281 | ACCEPT |
| Dual-agent accounting | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 30-41, 45-54, 115-123 | ACCEPT |
| Core guard self-protection | `docs/reference/guard_orientation/README.md` | lines 89, 102 | ACCEPT |

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Dispatcher | reviewer/dispatcher | author and validate this dispatch packet |
| Worker | operator-selected worker agent | implement allowed KIOD-R7 changes and return uncommitted evidence |
| Reviewer/closer | reviewer/closer after worker return | accept, reject, repair within scope, commit accepted material, and perform session sync |

## Required First Reads

Worker must read before editing:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by the state registry
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order and paired baseline
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`
- `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`
- all `governance/compat/check_*.py` files named in the Checker Source
  Read-Ahead Block

## Pre-Flight Checks

Worker must run before writing implementation:

- `git rev-parse --short HEAD`
- `git status --short`
- `python governance/compat/check_work_order_dispatch_quality.py --base b743c085 --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b743c085 --head HEAD`

If these fail for defects inside this packet, repair this packet only if the
repair is inside allowed scope. If failure is outside KIOD-R7 allowed scope,
stop and return `BLOCKED` with command output.

## Write Ownership

Worker may write only:

- `docs/reference/external_agent_review/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_STANDARD.md`
- `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`
- `governance/compat/test_dispatch_packet_lifecycle_hygiene.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md`

Worker must not edit `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
`CVF_SESSION/state/**`, `AGENT_HANDOFF_V30_2026-07-01.md`, archived handoffs,
public-sync files, Web/UI files, runtime source, external source mirrors, or
package registries.

Reviewer/closer owns acceptance, allowed repairs, material commit, optional
completion review if required, and session sync after worker return.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current mode is KIOD-R6 accepted pending next lane selection | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | line 3 | `currentMode` | active session bootstrap read model | VALUE_SET | ACCEPT |
| Active handoff is V30 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | line 4 | `activeHandoff` | active session bootstrap read model | VALUE_SET | ACCEPT |
| KIOD-R6 closed at material commit `8b89fc64` | `AGENT_HANDOFF_V30_2026-07-01.md` | lines 52-75 | `KIOD-R6 Memory Foundation Enrichment Closure` | active handoff | VALUE_SET | ACCEPT |
| Active next move is operator selection following KIOD-R6 closure | `AGENT_HANDOFF_V30_2026-07-01.md` | lines 172-183 | `Next Allowed Move` | active handoff | VALUE_SET | ACCEPT |
| Work-order authoring requires checker read-ahead and source verification | `docs/reference/guard_orientation/README.md` | line 79 | `Work-order authoring / dispatch` | guard orientation index | LITERAL_INVARIANT | ACCEPT |
| Worker execution under `WORKER_MUST_NOT_COMMIT` must leave artifacts uncommitted | `docs/reference/guard_orientation/README.md` | line 80 | `WORKER_MUST_NOT_COMMIT` | guard orientation index | LITERAL_INVARIANT | ACCEPT |
| Guard/checker maintenance needs Core Guard Self-Protection Authorization | `docs/reference/guard_orientation/README.md` | lines 89, 102 | `Core Guard Self-Protection Authorization` | guard orientation index | LITERAL_INVARIANT | ACCEPT |
| Dispatch-quality checker defines required source-verification columns | `governance/compat/check_work_order_dispatch_quality.py` | line 202 | `REQUIRED_SOURCE_COLUMNS` | dispatch quality checker | EXISTS | ACCEPT |
| Checker read-ahead block fields are machine-checked | `governance/compat/check_governed_artifact_checker_read_ahead.py` | lines 22-36 | `REQUIRED_HEADING`; `REQUIRED_FIELDS`; `CHECKER_PATH_RE` | checker read-ahead guard | EXISTS | ACCEPT |
| C4 handoff route needs Reviewer Closure Conversion | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | lines 243-249 | `Reviewer Closure Conversion` | agent handoff contract | LITERAL_INVARIANT | ACCEPT |
| Stale dispatch bases and stale `DISPATCH_READY` residue are known closure defects | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | lines 58-68, 230-238 | `DISPATCH_READY` | tranche commit choreography standard | LITERAL_INVARIANT | ACCEPT |
| Dual-agent surface matrix must account for internal and external consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | lines 30-41, 45-54 | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent accounting standard | LITERAL_INVARIANT | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query:
`python governance/compat/run_adif_defect_resolver.py --task-class governance_checker_maintenance --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: NONE_RETURNED

Resolver query: taskClass=`governance_checker_maintenance`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `## ADIF Defect Registry Disclosure`; `Resolver query: taskClass=`; `Returned defects: NONE_RETURNED`; `REQUIRED_SOURCE_COLUMNS`; `WORKER_MUST_NOT_COMMIT`; `Core Guard Self-Protection Authorization`; `Dual Agent Surface Matrix` |
| gateRunPurpose | confirmation/evidence only after checker constants and literal tokens were read before writing this work order |
| claimBoundary | This block proves only read-ahead discipline for this work order; it does not prove the future KIOD-R7 checker works until worker implementation and tests pass. |

## Agent Handoff Contract Control Block

| Field | Value |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher authors packet; worker returns uncommitted implementation evidence; reviewer/closer accepts, repairs if allowed, and commits |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=b743c085; executionBaseHead=RECORD_AT_WORKER_START_AFTER_DISPATCH_SYNC; closureBaseHead=REVIEWER_RECORDS_AFTER_WORKER_RETURN |
| changedSetScope(phase) | dispatch packet now; worker implementation and worker return after dispatch; reviewer closure and session sync after return |
| traceScope(phase, actor) | dispatcher records read-ahead/source verification; worker records implementation trace; reviewer records closure trace |
| commitOwner(phase) | dispatcher/reviewer for dispatch packet; nobody during WORKER_MUST_NOT_COMMIT execution; reviewer/closer for accepted worker material and session sync |
| crossBatchIsolation | no KIOD-R6 rework, source import, runtime, Web, public-sync, generated aggregate, package activation, provider/live proof, or production claim |
| Before status evidence | dispatchBaseHead `b743c085`; `git status --short` was empty before dispatch authoring |
| After status evidence | only this work order and paired GC-018 are changed for dispatch authoring |
| nextMoveSurfaces | after dispatch sync, worker executes only KIOD-R7 and returns uncommitted worker-return evidence |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_COMPLETION_2026-07-01.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md`;
`docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_COMPLETION_2026-07-01.md`

Reviewer may close directly in the worker return if the evidence is complete
and no separate completion review is needed. If a separate completion review is
created, it is reviewer-owned, not worker-owned.

## Commit Mode And Base-Anchor Lifecycle

| Phase | Base anchor | Commit owner | Required behavior |
| --- | --- | --- | --- |
| DISPATCH_AUTHORING | `b743c085` | dispatcher/reviewer | author and validate this packet |
| EXECUTION | worker records current HEAD after dispatch sync | nobody | worker leaves all changes uncommitted |
| CLOSURE | reviewer records fresh HEAD before accepting worker return | reviewer/closer | commit accepted material, then session-sync separately if needed |
| SESSION_SYNC | reviewer records post-material commit | reviewer/closer | update front door/state/handoff only after material commit exists |

## Worker Autonomy / No-Question Rule

Worker must make conservative implementation decisions inside allowed scope and
must not ask the operator to choose checker internals. Stop and return
`BLOCKED` only if a required source file is missing, a gate fails outside
allowed scope, or the checker would require runtime/provider/session-state
mutation.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator selected dispatch lifecycle hygiene as next roadmap value |
| Scope classification | bounded guard-maintenance dispatch; changed paths are limited by Write Ownership |
| Risk sensitivity | high governance precision value; no runtime, provider, live, secret, legal, public-sync, readiness, Web, package, or production behavior |
| Selected role route | worker implementation return to reviewer/closer closure conversion |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| Routing decision | `GUARD_MAINTENANCE_DISPATCH`; not external knowledge intake and not source absorption |
| Role separation basis | worker implements allowed checker tranche and returns uncommitted evidence; reviewer/closer accepts, repairs within scope, commits, and session-syncs if needed |
| Escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require runtime/provider/session-state mutation, public-sync, Web/UI, external adapter, package promotion, live proof, or broader dispatch-quality refactor |

## External Knowledge Intake Routing

External knowledge intake routing: N/A with reason.

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | N/A with reason: KIOD-R7 is guard-maintenance dispatch, not external knowledge absorption |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md` and paired GC-018 |
| Disposition | N/A with reason |
| Claim boundary | no source import, external absorption claim, raw memory release, or external adapter support |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: dispatch packet and future worker implementation must use current repo state and fresh gate output, not prior evidence reuse

unicodePathHandling: use literal paths and UTF-8-safe readers

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| Prior verification reuse | N/A with reason: dispatch authoring uses fresh source reads and fresh gate runs in this working tree |
| External evidence | N/A with reason: no external source bundle, extracted text, T11B evidence, or Unicode-path evidence is consumed |
| Encoding boundary | ASCII-only authored packet; no non-ASCII evidence quote or path handling claim is introduced |
| verificationMode | RECOMPUTE_REQUIRED |
| unicodePathHandling | N/A with reason: no Unicode-path evidence is consumed or dispatched |
| extractedTextAuthority | N/A with reason: no extracted text is consumed or treated as source authority |
| Worker requirement | worker must record fresh command output for implementation evidence instead of reusing this dispatch evidence |

## Current Runtime Freshness Verification

| Runtime or source claim | Verification command or source | Dispatch result | Worker requirement |
| --- | --- | --- | --- |
| Runtime/provider behavior | scope and forbidden-scope sections in this work order | no runtime/provider behavior is authorized or claimed | do not implement runtime/provider behavior |
| Existing active handoff | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `AGENT_HANDOFF_V30_2026-07-01.md` | active handoff is V30 at dispatch authoring | stop if active handoff changes before worker start |
| Worker return path | `Test-Path docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md` | absent at dispatch authoring | create uncommitted worker return |

## Foundation Storage Layout Block

| Field | Required content |
| --- | --- |
| Foundation files touched | planned new stable standard under `docs/reference/external_agent_review/` plus governance checker/test/catalog paths |
| Storage class | local-view guard-maintenance standard and internal governance checker |
| Index/front door | existing `docs/reference/external_agent_review/README.md` remains the family front door unless worker proves a narrower README update is required |
| Date policy | new standard uses stable descriptive path without date; work order/review remain dated execution artifacts |
| Archive disposition | N/A with reason: no existing foundation file is being superseded or archived in dispatch authoring |
| Deferred layout work | N/A with reason: worker must report if implementation discovers a missing README/front-door update need |

## Delta Execution Claim Boundary Control Block

Delta execution claim boundary: REQUIRED

| Field | Value |
| --- | --- |
| claimScope | KIOD-R7 dispatch authoring and future checker implementation scope only |
| claimDisposition | N/A with reason: no delta execution/runtime claim is made by this dispatch packet |
| receiptEvidence | N/A with reason: no runtime receipt or execution-control receipt exists or is claimed |
| actionEvidence | N/A with reason: no action execution or runtime interception is claimed |
| invocationBoundary | worker may run repo-local checker/tests only; no provider, live API, public-sync, or runtime invocation |
| interceptionBoundary | no wrapper, proxy, direct interception, universal governed-coding control, or mandatory invocation behavior is claimed |
| claimLanguage | bounded governance checker work order only |
| forbiddenExpansion | do not infer runtime governance behavior, provider routing, public readiness, Web/dashboard support, package activation, or action authority |

## Negative Search And Collision Discipline

Before creating the new standard or checker, worker must run and record:

- `rg -n --fixed-strings "dispatch packet lifecycle" docs governance CVF_SESSION`
- `rg -n --fixed-strings "stale DISPATCH_READY" docs governance CVF_SESSION`
- `rg -n --fixed-strings "provider-specific normative role" docs governance CVF_SESSION`
- `rg -n --fixed-strings "WORKER_MUST_NOT_COMMIT" docs/reference governance/compat`
- `rg -n --fixed-strings "Core Guard Self-Protection Authorization" docs/reference governance/compat`

If a same-owner surface already exists, enrich it instead of creating duplicate
doctrine. If only adjacent surfaces exist, create the KIOD-R7 standard and
explain the boundary.

## Core Guard Self-Protection Authorization

Authorization reason: KIOD-R7 is explicitly a guard-maintenance tranche for
dispatch packet lifecycle hygiene.

Authorized guard-maintenance scope: create one dispatch lifecycle hygiene
checker, one focused test module, one standard, and local hook/autorun wiring.

Operator authorization: operator asked to write the next work order after
selecting the dispatch lifecycle hygiene roadmap value.

Protected paths authorized for worker mutation:

- `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`
- `governance/compat/test_dispatch_packet_lifecycle_hygiene.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Protected paths mentioned but not authorized for worker mutation:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V30_2026-07-01.md`

Rollback boundary: revert only KIOD-R7 files and KIOD-R7 catalog entries. Do
not revert KIOD-R6 material commit `8b89fc64`, V30 session sync, or unrelated
governance entries.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | KIOD-R7 checker, standard, tests, and local governance catalogs | may inspect changed governed dispatch artifacts and session/handoff text; no runtime or provider behavior | this work order, paired baseline, future worker return, focused tests | internal governance checker only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | external worker consuming work order text | may execute the packet as a worker and return uncommitted evidence; no external adapter or MCP behavior is implemented | this work order and paired baseline | adapter implementation is out of scope and requires separate GC-018 | DEFERRED_WITH_REASON |

## Execution Plan

Worker must:

1. Complete required first reads and record `executionBaseHead`.
2. Inspect applicable checker sources before writing implementation.
3. Run negative-search commands and decide whether to create or enrich the
   KIOD-R7 standard.
4. Create or update the dispatch-packet lifecycle hygiene standard.
5. Implement `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`.
6. Add focused tests for stale active handoff reference, closed-lane stale
   dispatch packet, provider-specific normative role assignment, and unchanged
   historical artifacts ignored by range.
7. Wire the checker into autorun, reviewer-fast, pre-commit, and pre-push
   catalogs.
8. Run required verification commands.
9. Write one worker return under `docs/reviews/`.
10. Stop without committing.

## Checker Requirements

The checker must be conservative and changed-range aware:

- It must inspect changed `docs/baselines/*.md`, `docs/work_orders/*.md`, and
  dispatch-equivalent governed artifacts only.
- It must support `--base`, `--head`, and `--enforce`.
- It must reject changed dispatch-ready artifacts that cite a root-level active
  handoff different from `activeHandoff` in
  `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` or
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, unless the path is archive-qualified.
- It must reject changed dispatch-ready artifacts whose lane key is clearly
  recorded as closed in active session/front-door/handoff text.
- It must reject clear provider-specific normative role assignment in dispatch
  artifacts, such as provider names in `Agent Roles`, `Role`, `Worker`, or
  `rolePattern` assignment cells.
- It must not reject provider names that appear only in historical evidence,
  source path names, quoted prior defects, or existing unchanged artifacts.
- It must emit actionable messages with artifact path, failed rule, and repair
  hint.

## Worker Return Packet Shape Contract

Worker return path:
`docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_WORKER_RETURN_2026-07-01.md`

Required status line: `Status: COMPLETE_PENDING_REVIEW`

The worker return must include:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Source Verification Block
- Negative Search And Collision Discipline
- Checker Source Read-Ahead Block
- Core Guard Self-Protection Authorization
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Verification Evidence
- executionBaseHead
- git status from `git status --short`
- Claim Boundary
- Return-To-Reviewer Conditions

Conditional sections may be `N/A with reason` only when genuinely inapplicable.
The worker return must explicitly name these conditional gates:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

## Evidence Requirements

Worker must run and record:

- `python -m unittest governance.compat.test_dispatch_packet_lifecycle_hygiene`
- `python governance/compat/check_dispatch_packet_lifecycle_hygiene.py --base <executionBaseHead> --head HEAD --enforce`
- `python governance/compat/run_worker_return_fast_gate.py`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`
- `git diff --name-status`
- `git status --short`

If any command fails, worker must either repair inside allowed scope and rerun
or return `BLOCKED` with the exact failing command and reason.

## Acceptance Criteria

- New or enriched standard names lifecycle hygiene rules and claim boundary.
- Checker detects stale active handoff references in changed dispatch packets.
- Checker detects closed-lane stale dispatch-ready packets when closure evidence
  is clear in active session/handoff/front-door sources.
- Checker detects provider-specific normative role assignment in changed
  dispatch packets while avoiding historical/evidence false positives.
- Tests cover pass and fail fixtures.
- Catalog wiring adds the checker to autorun, reviewer-fast, pre-commit, and
  pre-push surfaces.
- Worker return is complete, uncommitted, and marks all public/runtime/provider
  claims out of scope.

## Review Gate

Reviewer must run at least:

- `python -m unittest governance.compat.test_dispatch_packet_lifecycle_hygiene`
- `python governance/compat/check_dispatch_packet_lifecycle_hygiene.py --base <closureBaseHead> --head HEAD --enforce`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <closureBaseHead> --head HEAD`

Reviewer must reject or repair if the worker broadened scope, committed, edited
session state/handoff, made runtime/provider claims, or left hook wiring
untested.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | KIOD-R7 dispatch packet lifecycle hygiene work order authoring, 2026-07-01 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, rg, ADIF resolver, apply_patch, governance gates |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator instruction to write the next work order after selecting dispatch lifecycle hygiene roadmap value |
| Before status evidence | dispatchBaseHead `b743c085`; `git status --short` (empty) before dispatch authoring |
| After status evidence | two new dispatch artifacts pending validation and commit |
| Diff evidence | `git diff --name-status`: two added dispatch artifacts |
| Approval boundary | dispatch packet only; worker implementation follows after material dispatch and session-sync |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public/Web/package claim |
| Agent type | dispatcher |
| Invocation ID | `kiod-r7-dispatch-packet-lifecycle-hygiene-dispatch-2026-07-01` |
| Expected manifest | `docs/baselines/CVF_GC018_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md` |
| Actual changed set | `docs/baselines/CVF_GC018_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Closure Checklist

- [x] Worker return exists and says `Status: COMPLETE_PENDING_REVIEW`.
- [x] Worker did not commit.
- [x] Changed files are within allowed scope.
- [x] Protected paths are covered by Core Guard Self-Protection Authorization.
- [x] Focused tests pass.
- [x] Reviewer-fast or commit-steward gate passes before material commit.
- [x] Material commit is separate from any session-sync commit.
- [x] Session front door/state/handoff are updated only after accepted material
  commit if current mode or next allowed move changes.

## Return-To-Orchestrator Conditions

Return without implementation if:

- active session state no longer names `AGENT_HANDOFF_V30_2026-07-01.md` and
  the packet has not been refreshed;
- KIOD-R7 would require runtime/provider/session-state mutation;
- gate failures are outside allowed scope;
- the checker would need to parse broad historical closure semantics beyond
  conservative changed-range rules.

## Operator Checkpoint

No operator checkpoint is required for worker implementation inside this packet.
Operator checkpoint is required before any runtime/provider/live proof,
public-sync, Web/UI dashboard, external adapter, package promotion, or KIOD-R6
deferred-candidate work.

Public Export Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening only; no public-sync batch is
authorized by KIOD-R7.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_2026-07-01.md` | `Status: CLOSED_PASS_BOUNDED` after reviewer acceptance | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_KIOD_R7_DISPATCH_PACKET_LIFECYCLE_HYGIENE_COMPLETION_2026-07-01.md` | reviewer closure artifact required after worker return | PASS |
| Roadmap state | N/A with reason | no dedicated R7 roadmap file is changed by this dispatch packet; operator selected the lane in chat following KIOD-R6 closure | N/A with reason |
| Registry JSON | N/A with reason | no corpus or scan registry JSON is changed by dispatch authoring | BLOCKED with reason: not applicable to this non-corpus dispatch packet |
| Registry Markdown | N/A with reason | no corpus or scan registry Markdown is changed by dispatch authoring | BLOCKED with reason: not applicable to this non-corpus dispatch packet |
| External evidence digest | N/A with reason | no external source evidence consumed by dispatch authoring | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry changed by dispatch authoring | N/A with reason |
| Session continuity | active session surfaces | session-sync is required only after dispatch material commit if next move changes | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
| --- | --- | --- | --- | --- | --- |
| KIOD-R7-DISPATCH-RECEIPT | N/A with reason: no runtime receipt is produced by dispatch authoring | N/A with reason | no runtime receipt claim | no runtime receipt claim | PASS |
| KIOD-R7-ACTION-EVIDENCE | N/A with reason: no action-execution receipt is produced by dispatch authoring | N/A with reason | no action execution claim | no action execution claim | PASS |

## Claim Boundary

This work order authorized KIOD-R7 implementation and is now closed bounded
after reviewer acceptance. It does not authorize worker commits or
runtime/provider/live/public/Web/package behavior.
