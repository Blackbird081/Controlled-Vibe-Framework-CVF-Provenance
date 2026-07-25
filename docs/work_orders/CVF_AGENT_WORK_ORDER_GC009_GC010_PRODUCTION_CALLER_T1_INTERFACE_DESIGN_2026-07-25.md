# CVF Agent Work Order GC-009/GC-010 Production Caller T1-Interface Design

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: GC009-GC010-PCALLER-T1I

Date: 2026-07-25

dispatchBaseHead: `c6ca6428c`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: NOT_EXECUTED_YET

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: no-commit documentation worker for GC009-GC010-PCALLER-T1I.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture current HEAD before any worker edit.

Current-time notes: T0A closed materially at `0e97a0ace`, with continuity
recorded at `c6ca6428c`, with
`CLOSED_PASS_BOUNDED_NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE`. The
operator then authorized this fresh source-verified interface-design packet,
explicitly scoped to only the interface/adapter design gap T0A found, not to
any runtime composition.

Do-not-misread notes: design the interface method signature and receipt
adapter shape on paper only. Do not edit `mandatory-gateway.ts`, create the
proposed singleton, edit the execute route, add package exports, add tests,
release T1 runtime composition, or claim a production caller exists.

Required first actions: capture HEAD and `git status --short`; read the
active session front doors, guard orientation, literal-format gotchas, paired
GC-018, this work order, the T0A audit and completion review, and every
source/checker named below; run pre-implementation before writing either
output.

Return contract: create exactly the two canonical outputs, run the worker
return fast gate, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce one source-verified specification for the exact context-preserving
`MandatoryGateway` interface method and the receipt/audit projection adapter
that T0A identified as the blocking requirement before any GC-009 production
composition can be released. The output must remove ambiguity about the
method signature, request/result field mapping, duplicate-evaluation
prevention, bypass configuration, and receipt/audit projection boundary,
without implementing any of them.

## Authority Chain

- Operator authorization: explicit confirmation following accepted T0A
  material commit `0e97a0ace` and continuity commit `c6ca6428c`, naming the
  interface-change gap as the reason to
  authorize this fresh packet.
- Paired baseline:
  `docs/baselines/CVF_GC018_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md`.
- Companion roadmap:
  `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`.
- Active state at dispatch authoring: commit `c6ca6428c`.
- T0A completion:
  `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md`.

Authority boundary: this work order does not authorize work outside this
cited authority chain. If any authority artifact conflicts with this work
order, stop and reconcile before implementation.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | N/A with reason: authored directly from the T0A work order template (`docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_2026-07-25.md`), which already provides a source-verified, checker-compliant structural template for this same lane |
| generatedProfile | generic-worker-dispatch plus no-commit worker and held-dependency trigger profiles, inherited from the T0A packet shape |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced T0A-specific design questions, manifests, and proof rules with T1-Interface-specific ones; narrowed scope to interface/adapter specification only |
| checkerReadAheadConfirmation | dispatch-quality, manifest-table, prompt-envelope, handoff-boundary, read-ahead, structural, worker-return, trace, and Delta checkers read before final authoring |
| docOnlyNewFields | proposed method signature and adapter shape are documentation-only until a later implementation work order independently source-verifies and authorizes them |
| claimBoundary | scaffold provenance only; no runtime behavior or production owner is claimed |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T0A independent closure | completion review at material commit `0e97a0ace` records `CLOSED_PASS_BOUNDED_NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE`; continuity commit `c6ca6428c` routes the checkpoint | T1-Interface may open only after operator authorizes a fresh interface-design packet | PASS |
| Operator checkpoint | explicit operator confirmation citing the T0A interface-change finding | release T1-Interface documentation only; preserve T1-runtime/T2/T3/T4 HOLD | PASS |
| Fresh dispatch anchor | HEAD `c6ca6428c`; clean worktree before packet authoring | worker must use committed dispatch tip and capture its own execution base | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | source-verify the exact context-preserving gateway interface method and receipt/audit adapter shape T0A found missing |
| scopeClassification | documentation-only interface/adapter design |
| riskSensitivity | R0 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | dispatcher releases; worker must not commit; reviewer/closer independently accepts |
| escalationCondition | source contradiction or need for any forbidden mutation/action |

## Agent Roles

- Dispatcher: owns packet source verification, repair, pre-dispatch gate, and
  dispatch commit.
- Worker: owns exactly the audit decision and worker-return paths.
- Reviewer/closer: independently reviews, may repair those two outputs, owns
  completion conversion and material commit.
- Session-sync steward: updates state only following the material dispatch or
  material closeout commit.

## Scope

Allowed scope:

- read current source and governed artifacts named by this packet;
- run bounded read-only searches and governance gates;
- create
  `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md`;
- create
  `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md`;
- repair structural defects inside those two paths and rerun gates.

Forbidden scope:

- no edit under `EXTENSIONS/`, `governance/compat/`, `CVF_SESSION/`, any
  package manifest, source file, test, checker, hook, public-sync clone, or
  handoff;
- no package installation, build, test execution, provider/API/network/browser
  call, CVF CLI/MCP invocation, process control, push, deploy, or credential
  access;
- no creation of the proposed interface method, adapter, singleton, or any
  other source/test path;
- no release of T1 runtime composition, T2, T3, or T4;
- no `git add` or `git commit`.

Risk ceiling: R0.

## Write Ownership

Worker-owned create-only paths:

- `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md`;
- `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md`.

Forbidden paths: everything else in the repository, explicitly including
`EXTENSIONS/**`, `governance/compat/**`, `CVF_SESSION/**`,
`CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, and any other `docs/**` path not
listed above.

Write mode: create-only. No file outside this ownership may be created,
modified, staged, or deleted.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; active
   handoff named by the registry.
2. `docs/reference/guard_orientation/README.md`.
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
4. This work order and its paired GC-018 baseline.
5. `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md`.
6. `docs/audits/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_2026-07-25.md` -
   the accepted owner/interface findings this packet builds on.
7. `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` -
   independent reviewer acceptance and the exact risk/corrective-action rows.
8. `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json`.
9. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` - the
   exact interface to extend.
10. `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` - the canonical
    `GuardRequestContext` field set the new method must preserve losslessly.
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
    (lines around 561, 578) - the existing direct evaluation call the future
    interface must replace without duplication.
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts` -
    `buildWebGuardContext`, the Web context builder whose output the new
    gateway method must accept verbatim.
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` -
    `buildEvidenceReceipt`, the existing governance evidence-receipt builder the future
    adapter must project into.
14. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` -
    `appendAuditEvent`, the existing durable audit seam the future adapter
    must project into.
15. `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` -
    confirms the execute route's current GC-023 boundary.
16. Checker paths in `## Checker Source Read-Ahead Block`.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role worker --lifecycle-phase pre-implementation --json --max-results 50
$executionBaseHead = git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
```

Stop before authoring if the dispatch tip is not a descendant of `c6ca6428c`,
the canonical outputs already exist, a required source path is missing, or a
gate failure cannot be repaired within the two worker-owned paths. Always run
`pre-implementation` with `--base` set to the worker's own freshly captured
`executionBaseHead`, not a stale dispatch-time head, since a later routing
commit will otherwise appear as a false-positive violation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0A accepted not-ready with interface-change requirement | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_OWNER_DESIGN_T0A_COMPLETION_2026-07-25.md` | Findings / Position | `NOT_READY_OWNER_CONTRACT_REQUIRES_INTERFACE_CHANGE` | T0A completion review | ACCEPT |
| `MandatoryGateway.check` signature and internal behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 80-180 | `check` | guard-contract gateway helper | ACCEPT |
| Canonical `GuardRequestContext` field set | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 93-110 | `GuardRequestContext` | guard-contract type | ACCEPT |
| Web context builder | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-runtime-adapter.ts` | lines 86-129 | `WebGuardInput`; `buildWebGuardContext` | Web guard adapter | ACCEPT |
| Existing direct route evaluation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 561, 578 | `getSharedGuardEngine`; `guardEngine.evaluate` | execute POST route | ACCEPT |
| Web receipt builder | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 55-78, 241-280 | `BuildGovernanceEvidenceReceiptInput`; `buildEvidenceReceipt` | Web evidence receipt | ACCEPT |
| Web audit event | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 140-152 | `appendAuditEvent` | control-plane event store | ACCEPT |
| Execute route active GC-023 boundary | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | `activeOwners`, lines 42-47 | `activeOwners`; `status` | governed file-size registry | ACCEPT |
| Prior route exception is a resolved non-usable tombstone | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | exception entries, lines 159-172 | `status`; `removalProcedure` | governed file-size registry | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Disposition |
|---|---|---|
| `contextPreservingMethodName` | exact future method name/signature added to or extending `MandatoryGateway` that accepts a pre-built `GuardRequestContext` verbatim and preserves `requestId` | DOC_ONLY_NEW |
| `receiptAdapterShape` | exact future secret-safe field projection from `GatewayResult` into the existing Web receipt/audit seam | DOC_ONLY_NEW |
| `bypassConfigurationRequirement` | exact future configuration value disabling gateway bypass actions for the execute route | DOC_ONLY_NEW |
| `duplicateEvaluationProofMechanism` | exact future deterministic test/assertion approach proving exactly one `engine.evaluate` call per request | DOC_ONLY_NEW |

## Required Design Questions

1. What exact new or extended `MandatoryGateway` method signature accepts an
   already-built `GuardRequestContext` verbatim, preserving `requestId` and
   every canonical field, with no re-defaulting or mutation?
2. Does this new method replace `check()`, extend it with an overload, or
   add a sibling method? What is the source-backed reason for that choice?
3. What exact mechanism (source-verifiable, not just descriptive) guarantees
   the future route path calls `engine.evaluate` exactly once, whether via
   the gateway or directly, never both?
4. What exact bypass-configuration value or flag must the future execute-route
   integration set so no `bypassActions` substring can silently allow an
   execute request through?
5. What exact field-by-field projection maps `GatewayResult` (`decision`,
   `allowed`, `bypassed`, `controlMode`) and its nested evidence fields
   (`evidence.requestId`, `evidence.blockedBy`,
   `evidence.escalatedBy`) into the existing `buildEvidenceReceipt` /
   `appendAuditEvent` seams, and which fields (if any) cannot be represented
   without loss?
6. What exact future tests would deterministically prove: (a) context/request-ID
   preservation, (b) exactly one evaluation per request, (c) no bypass reaches
   execution, and (d) BLOCK/ESCALATE fail closed before any provider call?
7. Which of the interface-change files (`mandatory-gateway.ts` and its test,
   `types.ts` if extended) are in scope for this interface change itself, as
   distinct from the separate T1-runtime files (proposed singleton, route
   adapter, route.ts) that a later composition packet would touch?
8. Does current source support one terminal disposition below?

## Terminal Disposition Enum

Record exactly one:

- `INTERFACE_SPEC_READY_FOR_FRESH_T1_RUNTIME_PACKET`
- `PARTIAL_INTERFACE_SPEC_REQUIRES_FURTHER_DESIGN`
- `NOT_READY_INTERFACE_SPEC_BLOCKED`
- `NO_CURRENT_VALUE_WITH_REOPEN_CONDITION`

The first token authorizes only a future T1-runtime packet-authoring
checkpoint. It does not itself release T1 runtime composition, T2, T3, or T4.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Output | Verification | Status |
|---|---|---|---|---|
| Resolve T0A's interface-change blocker before any T1 runtime release | Required Design Questions | audit interface/adapter specification | reviewer semantic check | PASS pending worker |
| Preserve T1-runtime/T2-T4 HOLD | Terminal Disposition Enum; Claim Boundary | explicit no-release decision | roadmap review | PASS pending worker |
| Prevent duplicate evaluation by design, not convention | questions 3, 6 | mechanism and test proposal | source citations | PASS pending worker |
| Bound receipt/audit adapter to existing durable seams | question 5 | field-by-field projection table | source citations | PASS pending worker |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | roadmap Scope | documentation-only two-output tranche | PASS |
| Non-goals | roadmap Non-Goals | forbidden scope blocks implementation/live/public work | PASS |
| Lane split | roadmap T0A/T1 | T0A closed; this packet is a T1-Interface sub-tranche; T1 runtime remains held | PASS |
| Dependency/source verification | roadmap T0A result | dependency and source tables cite current evidence | PASS |
| Claim boundary | roadmap Claim Boundary | no owner-exists or T1-runtime-release claim | PASS |
| Acceptance criteria | this work order | observable questions, enum, manifests, gates | PASS |
| Verification/evidence | this work order | exact commands and output paths | PASS |
| Dispatch-readiness decision | operator checkpoint plus paired GC-018 | documentation worker may dispatch once reviewer accepts | PASS pending review |

## Worker Autonomy / No-Question Rule

Repair allowed-scope formatting or checker defects directly. Do not ask the
operator to choose the terminal token. Return `BLOCKED_WITH_REASON` only for a
source contradiction, missing authority, or forbidden-scope dependency.

## Work-Order Fulfillment Manifest

The exact handoff contract is defined by the four sibling manifest sections
below.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | Yes | eight-question source-backed interface/adapter specification |
| `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md` | Yes | full-profile no-commit return |

## Forbidden Path Manifest

| Path or class | Required disposition |
|---|---|
| `EXTENSIONS/**` | no change |
| `governance/compat/**` | no change |
| package manifests, source, and tests | no change |
| `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md` | no change |
| public-sync, provider, CLI/MCP, deployment surfaces | no action |

## Forbidden Filesystem State At Dispatch

| Canonical output | Required state | Observed state | Disposition |
|---|---|---|---|
| `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | ABSENT | ABSENT (confirmed via `git status --short --untracked-files=all` at packet-authoring time) | PASS |
| `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md` | ABSENT | ABSENT (confirmed via `git status --short --untracked-files=all` at packet-authoring time) | PASS |

## Required Proof Manifest

| Proof | Path | Atomic literal | Required |
|---|---|---|---|
| Terminal disposition present | `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | N/A with reason: semantic validation must confirm exactly one enum token | No |
| Exact method/adapter specification recorded | `docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_2026-07-25.md` | `contextPreservingMethodName` | Yes |
| No-commit state recorded | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md` | `git status --short` | Yes |

Required Proof Manifest Atomic Literal Discipline: every Required=Yes row
uses one contiguous literal that can be checked in the named artifact.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | dispatcher, worker, reviewer/closer | two documentation outputs only | audit and worker return | native governed workflow | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | not applicable; this tranche concerns only the internal guard-contract gateway interface | no adapter or execution authority | N/A with reason: no CLI/MCP candidate compared | no adapter authorized | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external repository, corpus, packet, or provider output is consumed |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T1-Interface audit and worker return |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed source may support the design decision |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher author/reviewer, no-commit worker, independent reviewer/closer, session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`c6ca6428c`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | dispatch: baseline, work order, roadmap; execution: two worker outputs; closure: completion plus allowed reviewer repairs and roadmap/work-order status; session-sync: continuity only |
| traceScope(phase, actor) | each actor records its own phase trace |
| commitOwner(phase) | worker must not commit; reviewer/closer owns material closure; steward owns continuity |
| crossBatchIsolation | no unrelated worktree path permitted |
| nextMoveSurfaces | steward updates only following the material dispatch or material closeout commit |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md`

reviewerOwnedClosurePaths: this work order; paired baseline; companion roadmap
T1 row; both worker outputs; completion review.

closureOwner: independent reviewer/closer.

workerCommitPermission: FORBIDDEN.

Allowed pending worker-return status tokens: `COMPLETE_PENDING_REVIEW`,
`BLOCKED_WITH_REASON`.

Forbidden closed-equivalent residue tokens in the worker return: `CLOSED`,
`CLOSED_PASS_BOUNDED`, `DISPATCH_READY`.

## Execution Plan

1. Capture base/status and complete all reads and pre-implementation.
2. Recompute current gateway signature, context, route evaluation, receipt,
   and audit facts at the worker's own execution base.
3. Specify the exact context-preserving method signature, field-by-field
   request mapping, and result mapping.
4. Specify the exact duplicate-evaluation prevention mechanism and bypass
   configuration requirement.
5. Specify the exact receipt/audit adapter field projection, naming any
   field that cannot be represented without loss.
6. Answer all eight design questions and choose exactly one terminal token.
7. Create the worker return from the checker-safe scaffold, run the fast
   gate, record final status, and stop without commit.

Each step stops on a source contradiction or forbidden-scope need.

## Evidence Requirements

- exact source citations for every existing fact;
- proposed method/adapter names only in clearly labeled doc-only design
  tables;
- exact field-by-field request/result mapping;
- explicit duplicate-evaluation prevention mechanism;
- `executionBaseHead`, initial/final `git status --short`, and full Agent
  Operation Trace Block;
- worker-return fast gate PASS.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: source should support specifying one lossless
context-preserving method and one bounded receipt/audit adapter shape.

Evidence Comparison Requirement: compare that prediction against the
gateway's current `check` signature, canonical context fields, and existing
Web receipt/audit builder signatures.

Contradiction Handling Requirement: contradictory evidence requires a
Contradiction Or Gap Disposition and a not-ready or narrowed terminal result.

Claim Update Requirement: record whether the interface/adapter specification
is confirmed, narrowed, rejected, or parked.

## Acceptance Criteria

- [ ] All eight design questions have source-backed answers.
- [ ] Exactly one terminal token is recorded.
- [ ] Existing facts and proposed doc-only items are not conflated.
- [ ] The context-preserving method signature, duplicate-evaluation
  mechanism, bypass configuration, and receipt/audit adapter are explicit or
  the packet returns not-ready.
- [ ] Exactly two worker paths changed and the worker did not commit.

Fail conditions:

- [ ] Confirmed absent: proposed method/adapter claimed as existing source.
- [ ] Confirmed absent: duplicate guard evaluation left ambiguous in a
  ready/partial result.
- [ ] Confirmed absent: T1-runtime release or runtime/package/test mutation
  claimed.
- [ ] Confirmed absent: provider, network, browser, CVF CLI/MCP, public, or
  deployment action.

Closure is blocked if any fail condition is present.

## Review Gate

Worker execution requires the committed dispatch packet plus pre-dispatch and
pre-implementation PASS. Closure requires independent reviewer acceptance,
reviewer-return commit steward PASS, a material commit, committed-range
pre-closure PASS, and separate session-sync when next-move state changes.

## Operator Checkpoint

The operator authorized this T1-Interface documentation packet, citing T0A's
interface-change finding. No additional checkpoint is required for the
no-commit worker to execute it. Fresh operator authority remains mandatory
for T1 runtime composition, any runtime/package/test change, provider or live
proof, CLI/MCP invocation, public-sync, deployment, or scope expansion.

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_WORKER_RETURN_2026-07-25.md`

```text
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: python governance/compat/run_worker_return_fast_gate.py
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
requiredSections: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition
requiredEvidenceTerms: executionBaseHead; git status --short
conditionalSections: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package
conditionalDispositionRule: include each conditional section with evidence when applicable, otherwise record N/A with reason
```

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
$executionBaseHead = git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

No live proof is required or authorized because this tranche does not claim
or change live provider governance behavior.

## Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required evidence commands run and recorded
- [ ] `pre-closure` autorun gate passed on the committed closure range
  (reviewer/closer-owned; not applicable to the worker's pending return)
- [ ] Commit mode recorded as `WORKER_MUST_NOT_COMMIT`
- [ ] `dispatchBaseHead`, `executionBaseHead`, and closure-stage base
  evidence recorded
- [ ] Pending handoff used `COMPLETE_PENDING_REVIEW` or
  `BLOCKED_WITH_REASON`, recorded actual `git status --short`, and left
  committed-range `pre-closure` to reviewer/closer
- [ ] Worker-return fast gate result recorded
- [ ] Agent Operation Trace Block present and complete
- [ ] Changed-file set is inside this work order's Allowed scope
- [ ] Roadmap-to-work-order trace matrix final statuses are PASS or N/A with
  reason
- [ ] No open checkbox residue remains once the reviewer/closer finalizes
  closure
- [ ] GC-020 handoff updated with current HEAD after reviewer/closer commit

## Return-To-Orchestrator Conditions

Return to orchestrator (reviewer/dispatcher, then packet-author if
needed) without continuing if:

- pre-flight fails outside allowed scope;
- `pre-implementation` fails and cannot be repaired inside this work order's
  two owned paths;
- source-fidelity pass finds a missing path, invented symbol, or unverified
  claim that cannot be resolved by bounded read-only search;
- scope conflict is discovered (a runtime/test/checker edit appears
  necessary to answer a design question);
- required citation cannot be found;
- implementation would exceed the R0 risk ceiling;
- public/provenance boundary is unclear.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`

Returned defects (20): ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044,
ADIF-0045, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031,
ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50`

Dispatch impact: exact paths and symbols are used, doc-only proposals are
separate, no external/provider memory is authority, manifests and base heads
are explicit.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_tables.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; manifest sibling headings (`##`-level, not `###`); `Required Proof Manifest Atomic Literal Discipline`; `Source Verification Block`; `New Doc-Only Fields`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `WORKER_MUST_NOT_COMMIT`; exact ADIF query; ASCII-only prose |
| gateRunPurpose | confirm complete dispatch shape after source verification, informed by the literal-format gate-trap patterns already diagnosed in the prior T0 worker-return cycle (heading depth, non-ASCII characters, retro field names) |
| claimBoundary | checker compliance evidence only; no execution or closure claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | packet-author (Claude, Sonnet 5) |
| Provider or surface | Claude Code CLI, operator manual copy/paste invocation |
| Session or invocation | GC009-GC010-PCALLER-T1I work-order authoring, 2026-07-25 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Grep, Bash (`git rev-parse`, `git status`, `python governance/compat/run_adif_defect_resolver.py`) |
| Target paths | this work order; its paired GC-018 baseline; the companion roadmap update |
| Allowed scope source | operator task-specific execution declaration authorizing exactly these three packet-author outputs |
| Before status evidence | HEAD `c6ca6428c`; `git status --short` clean at authoring start |
| After status evidence | one modified roadmap plus two untracked packet files; HEAD unchanged at `c6ca6428c` |
| Diff evidence | `git status --short` (one `M` path and two `??` paths) |
| Approval boundary | packet authoring only; no worker execution performed by this session |
| Claim boundary | repo-local trace only; no OS/user attribution |
| Agent type | packet-author |
| Invocation ID | `gc009-gc010-production-caller-t1-interface-design-work-order-authoring-2026-07-25` |
| Expected manifest | this work order; paired GC-018 baseline; companion roadmap update |
| Actual changed set | same three paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded interface/receipt-adapter design work order for GC-009 |
| claimDisposition | N/A with reason: no Delta execution behavior is implemented by this work order |
| receiptEvidence | N/A with reason: no runtime receipt is created by this work order |
| actionEvidence | N/A with reason: documentation/architecture-decision artifact only |
| invocationBoundary | governed local document editing; no broader claim |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | this work order authorizes a bounded, source-verified interface/adapter specification and one terminal disposition; it does not claim any interface change is implemented |
| forbiddenExpansion | no runtime/source/test/checker mutation, no package installation, no provider/live proof, no public-sync, no CLI/MCP invocation, no T1-runtime implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order authoring only; no public-sync batch is
authorized by this artifact.

## Claim Boundary

This work order authorizes exactly one bounded interface/receipt-adapter
design tranche: source-verified specification of the context-preserving
`MandatoryGateway` method and receipt/audit adapter that T0A found missing,
plus one terminal disposition. It does not authorize T1-runtime
implementation, package export changes, CLI/MCP invocation, provider/live
proof, public-sync, or any runtime mutation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_INTERFACE_DESIGN_COMPLETION_2026-07-25.md` | does not exist yet; worker execution and independent closure remain pending | N/A with reason: substantive execution and independent closure remain pending |
| Roadmap state | `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | T1-Interface dispatch pending review; T1-runtime/T2-T4 `HOLD_*` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no new corpus packet; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no new corpus entry required for a bounded interface-design tranche with no corpus scan | PASS |
| External evidence digest | N/A with reason | no external evidence | N/A with reason |
| System loop interlock | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_GAP_INDEX.json` | gap entry remains `IMPLEMENTED_NOT_INVOCATION_PROVEN` pending independent acceptance | N/A with reason: gap closure requires independent reviewer acceptance, not this dispatch |
| Session continuity | active front doors | not updated by this work order | N/A with reason: session-sync is a separate reviewer/closer-owned step |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Terminal disposition | one fixed enum token | not yet recorded; worker execution pending | N/A with reason: pending worker execution |
| Worker commit | none | not yet executed | N/A with reason: pending worker execution |
| T1-runtime release | HOLD until T1I independent closure | T1-runtime/T2-T4 remain `HOLD_*` | PASS |
| Registry JSON/Markdown acceptance | no new corpus packet required | no corpus scan performed by this dispatch | PASS |
