# CVF Agent Work Order - SOT3-T8 Refinery-To-Kernel Packet Binding Contract

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-13

Work Order ID: SOT3-T8

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `d04715b1c`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: bounded implementation worker

Canonical packet: paired T8 GC-018 and this work order

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: worker captures clean HEAD at start

Current-time notes: T7 is accepted; packet-binding GAP is open; T8 is the only active lane.

Do-not-misread notes: this is not Kernel/Flow redesign, activation, provider work, or public export.

Required first actions: read startup surfaces, capture clean status, reopen every source-verification row.

Return contract: uncommitted `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Close the owner-level Refinery-to-Kernel packet-binding contract GAP through a
Refinery-owned canonical hash profile and source-backed integration migration.

## Target / Source

The paired GC-018 is source authority. Direct runtime sources named in its
Source Verification Block control over summaries or provider-local memory.

## Scope / Methodology

Implement the smallest owner-level contract, tests, documentation, T6 consumer
migration, worker return, and GAP update required to prove interoperability.

## Authority Chain

Current user direction -> T7 closure -> open system-chain GAP -> paired T8 GC-018 ->
this work order -> no-commit worker -> reviewer/closer.

## Agent Roles

Dispatcher owns source fidelity; worker implements without commit; reviewer owns
semantic review, repairs, GAP closure decision, and material commit.

## Worker Autonomy / No-Question Rule

Repair in-scope source, test, document, and machine-gate defects. Stop only for
a verified source contradiction, forbidden path, or scope expansion.
Return blocked only for a verified source contradiction, dirty start tree,
forbidden-scope requirement, or missing local dependency that cannot be safely
resolved inside the package.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| intakeClass | current private-provenance source/test contract change |
| workerRole | bounded implementation worker |
| reviewerRole | independent reviewer/closer |
| externalReviewer | N/A with reason: no new external source or advisory intake |
| routingDecision | direct governed worker execution from source-verified packet |
| selectedRoleRoute | dispatcher -> worker -> reviewer/closer |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| riskSensitivity | high: shared cross-package binding identity |
| escalationCondition | verified source contradiction or required forbidden-scope mutation |

## Write Ownership

Worker owns only Allowed Scope while uncommitted. Session continuity remains
reviewer/session-steward owned.

## Required First Reads

Startup front doors, guard orientation, literal gotchas, paired GC-018, T7
completion, open GAP entry, SOT contract-chain README, current Refinery and
Kernel public types/exports/admission, and the T6 local helper plus tests.

## Allowed Scope

- `EXTENSIONS/CVF_REFINERY/src/**`
- `EXTENSIONS/CVF_REFINERY/tests/**`
- `EXTENSIONS/CVF_REFINERY/package.json`
- `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/**`
- `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/tests/**`
- `docs/reference/sot_three_layer/**`
- the one packet-binding GAP entry and generated GAP index/front door
- `docs/reviews/CVF_SOT3_T8_WORKER_RETURN_2026-07-13.md`

## Forbidden Scope

Truth Kernel and Truth Flow source mutation; other extensions; retained legacy;
governance checkers/hooks; session state; adapters; Web/UI; provider/live;
network/database; activation; public-sync; unrelated Catalog/GAP entries.

## Source Verification Block

The worker must reopen every ACCEPT row in the paired baseline. A mismatch
returns `BLOCKED_WITH_REASON` with direct source evidence before editing.

## Dependency Release Evidence

T7 closeout is accepted by roadmap closure commit `f017dc775`; session routing
is commit `d04715b1c`; the operator explicitly approved proceeding to T8.

## Implementation Contract

- Define profile ID `cvf.sotThreeLayer.refineryPacketHash.v1`.
- Refinery owns and exports `packetContentHash(packet)` or an equally explicit
  source-verified name; do not leave the canonical implementation in T6.
- Hash a documented stable projection of `RefineryPacket`, not arbitrary
  enumerable properties. Use SHA-256 over UTF-8 deterministic canonical JSON
  and return `sha256:<lowercase-hex>`.
- Specify array ordering and reject unsupported/non-serializable values rather
  than silently dropping them.
- Publish at least one fixed input/preimage/digest vector.
- Migrate the T6 orchestrator to the Refinery export. Delete its local helper,
  or retain only a compatibility wrapper that delegates to Refinery and has no
  independent algorithm.
- Do not change Kernel admission semantics. Its equality mismatch must still
  fail closed.
- Update the SOT contract reference and GAP record only after tests prove the
  owner path. Regenerate the GAP aggregate.

## Negative Test Matrix

| Case | Required result |
|---|---|
| Same packet and profile repeated | identical digest |
| Included scalar or nested field changes | digest changes |
| Object insertion order changes without semantic change | digest unchanged |
| Unsupported value appears | explicit rejection |
| T6 supplies a digest for a different packet | Kernel admission rejects |
| Caller attempts another profile | unsupported profile fails closed or is unavailable |

## Execution Plan

1. Capture clean HEAD/status and reopen all source-verification rows.
2. Record the exact stable field projection before implementation.
3. Implement the profile in Refinery and export it.
4. Add fixed vectors, mutation, ordering, and rejection tests.
5. Migrate T6 to the owner API and rerun its full tests/typecheck.
6. Update canonical contract/GAP evidence and regenerate the GAP index.
7. Run worker-return fast gate and pre-implementation controls.
8. Return uncommitted `COMPLETE_PENDING_REVIEW`.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Acceptance Evidence

Return exact commands/results for focused and full package tests, typechecks,
fixed vector digest, negative cases, GAP generator/checker, diff/status, and
no-commit evidence.

## Evidence Requirements

Evidence must distinguish contract ownership, implementation behavior, and GAP
disposition. A passing T6 integration test alone does not prove shared owner.

## Acceptance Criteria

All baseline criteria and negative rows pass; the changed set stays within
Allowed Scope; no Kernel/Flow mutation or forbidden external action occurs.

## Review Gate

The reviewer independently reviews stable-field selection, canonicalization, vectors,
consumer migration, negative cases, GAP status, and changed scope before commit.

## Closure Checklist

- [ ] Refinery owns and exports the versioned profile.
- [ ] Fixed vector and all negative cases pass.
- [ ] T6 uses the owner API and retains full test/typecheck pass.
- [ ] Kernel mismatch remains fail-closed without Kernel source mutation.
- [ ] Contract reference and GAP aggregate reconcile.
- [ ] Worker made no commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with exact source
evidence. Do not broaden scope and do not commit.

## Operator Checkpoint

Stop for Kernel/Flow mutation, a second hash profile, public/provider work,
destructive action, or a field-stability decision not supported by source.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap/GAP requirement | Work order section | Output | Verification | Status |
|---|---|---|---|---|
| canonical algorithm | Implementation Contract | Refinery profile | vectors/tests | REQUIRED |
| owning package | Allowed Scope | Refinery export | import/consumer test | REQUIRED |
| field-stability rules | Implementation Contract | contract documentation | mutation/order tests | REQUIRED |
| future callers interoperate | T6 migration | owner API consumption | full slice tests | REQUIRED |
| GAP close decision | Review Gate | updated entry/index | generator/reviewer | REQUIRED |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phaseDisposition | packet dispatch, bounded implementation, reviewer closure, separate session sync |
| baseHeadFor(phase) | dispatch=`d04715b1c`; implementation=worker start HEAD; closure=reviewer capture |
| changedSetScope(phase) | exact Allowed Scope only |
| traceScope(phase, actor) | worker return records actual manifest and commands; reviewer records closure evidence |
| commitOwner(phase) | reviewer/closer for material; session steward for continuity |
| crossBatchIsolation | no activation, provider/live, public, or unrelated GAP mutation |
| nextMoveSurfaces | reviewer updates when accepted completion evidence exists |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T8_REFINERY_KERNEL_PACKET_BINDING_CONTRACT_COMPLETION_2026-07-13.md`

reviewerOwnedClosurePaths: completion review, accepted GAP disposition, material
commit, and separate session continuity.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --file docs/reviews/CVF_SOT3_T8_WORKER_RETURN_2026-07-13.md --base <executionBaseHead> --head HEAD`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must contain: Purpose; Target / Source; Scope / Methodology;
Findings / Position; Risk / Corrective Action; Dependency Release Evidence;
Source Verification Recheck; git status --short; Changed Files; Commands And
Results; Negative Test Matrix Results; Agent Operation Trace Block; No-Commit
Statement; Claim Boundary; and final status `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py --file docs/reviews/CVF_SOT3_T8_WORKER_RETURN_2026-07-13.md --base <executionBaseHead> --head HEAD
python governance/compat/generate_as_built_system_catalog.py --gaps-only
python governance/compat/check_as_built_system_catalog_drift.py
git diff --check
git status --short --untracked-files=all
```

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| applicability | NOT_APPLICABLE_WITH_REASON |
| reason | T8 changes already-absorbed CVF-native owner packages and does not rescan or absorb a legacy corpus |
| coverageIndexMutation | none |

## Negative Search And Collision Discipline

| Field | Evidence |
|---|---|
| search target | packet hash producer/export across Refinery, Kernel, and T6 slice |
| command | `rg -n "packetContentHash|content_hash|packetHash" EXTENSIONS/CVF_REFINERY/src EXTENSIONS/CVF_TRUTH_KERNEL/src EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src` |
| collision result | one caller-local helper exists; no Refinery owner export exists |
| disposition | create one Refinery owner and migrate the caller; do not create a second independent algorithm |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | accepted SOT3 corpus -> T7 terminal ledger -> open architecture GAP -> T8 owner contract |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Refinery package plus canonical SOT contract reference |
| Disposition | implement the already-approved owner repair without reopening corpus absorption |
| Claim boundary | no new external authority or direct legacy import |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Disposition |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Source Verification Block; Dependency Release Evidence; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirmation after checker/source read-ahead |
| claimBoundary | dispatch PASS does not prove implementation |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T8 --title "Refinery Kernel Packet Binding Contract" --date 2026-07-13 --base d04715b1c --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit source/test contract worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | authored directly from source-verified T8 boundary |
| checkerReadAheadConfirmation | dispatch, handoff, trace, and public guards |
| docOnlyNewFields | profile identifier and T8 evidence vocabulary |
| claimBoundary | dispatch only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This work order authorizes one bounded no-commit T8 execution. It does not
authorize activation, provider/live work, public-sync, release, or production
readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local governed workspace |
| Session or invocation | SOT3-T8 packet authoring, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | direct source reads, search, patch, governance gates |
| Target paths | paired T8 baseline and work order |
| Allowed scope source | current user direction plus accepted T7 completion evidence |
| Before status evidence | clean worktree at `d04715b1c` |
| After status evidence | exactly two uncommitted packet artifacts before dispatch commit |
| Diff evidence | `git diff --name-status` and commit hook |
| Approval boundary | T8 packet authoring and dispatch only |
| Claim boundary | no worker implementation in packet-authoring batch |
| Agent type | dispatcher |
| Invocation ID | sot3-t8-packet-authoring-2026-07-13 |
| Expected manifest | paired T8 baseline and work order |
| Actual changed set | paired T8 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
