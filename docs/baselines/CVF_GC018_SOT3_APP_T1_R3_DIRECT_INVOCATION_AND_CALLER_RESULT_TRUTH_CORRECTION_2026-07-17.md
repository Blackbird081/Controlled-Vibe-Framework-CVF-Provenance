# CVF GC-018 Baseline - SOT3-APP-T1-R3 Direct Invocation And Caller Result Truth Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SOT3-APP-T1-R3

Dispatch base head: `a73a452ee`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Orchestrator/reviewer

Reviewer owner: independent reviewer/closer

Worker target: documentation worker

## Purpose

Authorize one final narrow documentation correction for the new critical
caller-edge contradictions independently established at T1-R2 review round
three. Preserve accepted 80-file and 14-file membership facts and correct only
direct invocation membership and caller-result semantics.

## Authority / Decision

Material review commit `49ab5350c` records
`CONTINUE_NEW_CRITICAL_EVIDENCE`. It proves six test invocations were collapsed
into constructor-only rows and the `EvidenceAdapter.recordFreeze` return-use
claim contradicted source. This is sufficient dependency-release evidence for
R3 only; T2 remains held.

## Baseline / Proposed Tranche

One bounded documentation worker corrects direct invocation and caller-result
evidence; independent review remains mandatory.

## Evidence / Verification

Evidence is review commit `49ab5350c`, the direct source anchors below, the
exact invocation search, Git proof, and mandatory dispatch/return gates.

## Scope

Allowed worker outputs are exactly:

1. `docs/reviews/CVF_SOT3_APP_T1_R3_DIRECT_INVOCATION_AND_CALLER_RESULT_TRUTH_CORRECTION_2026-07-17.md`
2. `docs/reviews/CVF_SOT3_APP_T1_R3_WORKER_RETURN_2026-07-17.md`

The worker may read the committed CVF packet chain and the copied read-only
root `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

## Non-Goals

- no source, test, runtime, package, registry, generated-state, UI, or queue edit;
- no provider, live call, network, public-sync, push, or production claim;
- no reopening of accepted 80-file or 14-file membership facts;
- no T2 or later-tranche execution;
- no worker commit or staging.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T1-R2 worker return | material review range `3a54fae91..49ab5350c` | SATISFIED |
| independent T1-R2 verdict | `docs/reviews/CVF_SOT3_APP_T1_R2_COMPLETION_REVIEW_2026-07-17.md`; material commit `49ab5350c`; `REVIEWED_NOT_ACCEPTED_R3_REQUIRED` | SATISFIED |
| round-three continuation authority | review telemetry `stopDisposition=CONTINUE_NEW_CRITICAL_EVIDENCE` | SATISFIED |
| clean packet-authoring base | session-sync commit `a73a452ee` | SATISFIED |
| T2 release | accepted T1 closure does not exist | HOLD |

## Source Verification Block

| Claimed item | Fact class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| six missing test invocations and false result-use claim | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T1_R2_COMPLETION_REVIEW_2026-07-17.md` | F1; F2 | `SOT3-APP-T1-R3` correction set | independent reviewer | ACCEPT |
| Flow test invokes route | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\integration\truth-flow-binding.test.ts` | line 12 | `adapter.route` | `TruthFlowAdapter.route` | ACCEPT |
| Kernel test invokes reference assertion | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\integration\truth-kernel-binding.test.ts` | line 10 | `adapter.assertReferences` | `TruthKernelAdapter.assertReferences` | ACCEPT |
| context test invokes build | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\integration\sot-to-context.test.ts` | line 14 | `service.build` | `ContextBuilderService.build` | ACCEPT |
| freeze test invokes freeze | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\integration\review-freeze.test.ts` | line 19 | `service.freeze` | `ReviewFreezeService.freeze` | ACCEPT |
| Refinery test invokes submit | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\integration\refinery-binding.test.ts` | line 6 | `submitSource` | `RefineryAdapter.submitSource` | ACCEPT |
| phase test invokes freeze gate | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\integration\phase-governance-binding.test.ts` | line 11 | `adapter.assertFreezeAllowed` | `PhaseGovernanceAdapter.assertFreezeAllowed` | ACCEPT |
| recordFreeze return discarded after record construction | RUNTIME_BEHAVIOR | N/A with reason: direct read-only external source at `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\application\src\services\review-freeze.service.ts` | lines 31-34 | `this.evidence.recordFreeze` | `ReviewFreezeService.freeze` | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `DIRECT_INVOCATION_SET` | exact direct method-call ledger separate from construction evidence | none |
| `CALLER_RESULT_DISPOSITION` | source-true caller handling of return/rejection | none |
| `CALLEE_INTERNAL_GUARD_NOTE` | optional separate callee behavior note | none |

## Dispatch Boundary

The worker must start from the clean committed execution base supplied after
packet commit, capture it as `executionBaseHead`, and stop with exactly two
untracked outputs. The worker must not alter this baseline, the work order,
roadmap, review history, registry, generated aggregates, or protected session
surfaces.

## Current Runtime Freshness Verification

NOT_APPLICABLE_WITH_REASON: this baseline authorizes documentation-only review
outputs against a fixed copied source snapshot and makes no current integration
or runtime-availability claim.

## Acceptance Criteria

- every direct invocation returned by the declared call search has its own row;
- construction-only evidence is never substituted for invocation evidence;
- each invocation row distinguishes caller handling from callee internal guard;
- `recordFreeze` is correctly classified as caller discards adapter return;
- accepted 80/14 set facts are retained by citation, not recomputed or rewritten;
- all caller rows reconcile with zero open invocation gaps;
- exactly two worker paths, no stage, unchanged HEAD, all fast gates pass.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`downstream caller edge correction dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "downstream caller edge correction dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T1-R3 --title "Direct Invocation And Caller Result Truth Correction" --date 2026-07-17 --base a73a452ee --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1-R2 review 49ab5350c records new critical caller-edge contradictions" --stdout --include-worker-return-skeleton` |
| scaffoldOutputUsed | trigger map and required no-commit blocks used for paired packet authoring |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Machine Closure Package |
| gateRunPurpose | confirm complete packet shape after direct source verification |
| claimBoundary | checker conformance does not execute R3 or release T2 |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-APP-T1-R3 --title "Direct Invocation And Caller Result Truth Correction" --date 2026-07-17 --base a73a452ee --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T1-R2 review 49ab5350c records new critical caller-edge contradictions" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact R3 authority, source anchors, two-output boundary, round-three stop control |
| checkerReadAheadConfirmation | dispatch and closure checkers reviewed |
| docOnlyNewFields | direct invocation and caller-result tokens |
| claimBoundary | scaffold use does not prove caller closure or runtime behavior |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: DISPATCH_READY` | PASS |
| Work order status | paired R3 work order | `Status: DISPATCH_READY` | PASS |
| Roadmap state | SOT3-APP roadmap | `Status: SOT3_APP_T1_R3_DISPATCHED_WORKER_NEXT` | PASS |
| Registry JSON | existing GC-051 aggregate | no registry mutation authorized | N/A with reason |
| Registry Markdown | existing registry documentation | no new governed source path | N/A with reason |
| Completion or reviewer artifact | future R3 completion review | reviewer-owned after worker return | N/A with reason |
| System loop interlock | R2 rejection -> R3 worker -> independent review | T2 parked | PASS |
| Session continuity | protected sync after material dispatch commit | separate commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance correction packet; public export is not authorized.

## Claim Boundary

This baseline authorizes two documentation outputs only. It does not accept R2,
close T1, release T2, authorize source/runtime/provider/live/public work, or
make production, integration, certification, shipment, scale, or user-value
claims.
