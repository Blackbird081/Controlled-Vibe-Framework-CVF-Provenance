# CVF Agent Work Order - SOT3 Activation A4 Failure And Recovery Boundary Proof

Memory class: governed-worker-dispatch
Status: CLOSED_PASS_BOUNDED
docType: work_order
Batch ID: SOT3-ACT-A4
Date: 2026-07-13
dispatchBaseHead: `48f5e70d3`
executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`
closureBaseHead: `REVIEWER_TO_SET`
Commit mode: `WORKER_MUST_NOT_COMMIT`
Worker: delegated implementation and live-proof worker
Reviewer/closer: Codex reviewer/closer
Worker return path: `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_WORKER_RETURN_2026-07-13.md`

boundedRepairBaseHead: `bf50f7b6b`

boundedRepairDisposition: `MANIFEST_PATH_ADDED_AFTER_VALID_BLOCKER`

## Dispatch Prompt Envelope

Role: delegated SOT3 A4 implementation and proof worker.

Canonical packet: this work order.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: use the actual clean post-dispatch HEAD, current source,
and operator-local key bootstrap on 2026-07-13.

Do-not-misread notes: this is bounded failure/recovery work, not A5 release
integration, final activation closure, universal SOT3 runtime, prompt tuning,
provider comparison, public export, or production deployment.

Required first actions: read startup front doors, guard orientation, literal
gotchas, this packet, paired baseline, A3 completion, A4 roadmap section,
ADIF-0030, and every checker named below. Capture a clean executionBaseHead
before edits and run pre-implementation with a real range.

Return contract: implement the exact manifest, run the local negative gate
before any live call, create the worker return, run all required gates, leave
changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Close A4's real product failure boundary: strict Flow consumption binding,
ENFORCE rejection before provider execution, complete owner-backed negative
matrix, durable recovery/replay proof, OFF rollback, and one post-negative-gate
Alibaba recovery call.

## Authority Chain

Operator A0-A5 authorization -> activation roadmap A4 release -> paired
GC-018 baseline -> this work order -> delegated worker return -> independent
reviewer/closer decision. Runtime source and canonical contracts override chat
or provider-local memory.

## Agent Roles

The delegated worker owns implementation, tests, fresh evidence, diagnostics,
and the no-commit return. The reviewer/closer owns acceptance, bounded repair,
material commit, roadmap transition, and session synchronization. The operator
retains final decision authority.

## Required First Reads

- `CVF_SESSION_MEMORY.md`, active state registry, and active handoff;
- `docs/reference/guard_orientation/README.md` and literal gotchas;
- paired A4 baseline, activation roadmap A4 section, and A3 completion;
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0030.md`;
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0031.md`;
- current Flow, adapter, store, execute route, and checker sources below.

## Pre-Flight Checks

- clean worktree and captured executionBaseHead;
- exact manifest confirmed and historical A3 evidence unchanged;
- pre-implementation autorun PASS on a real range;
- local key bootstrap checked without printing values;
- negative runner defaults to local-only and has no live permit.

## Write Ownership

The worker may write only the Work-Order Fulfillment Manifest. Historical A3
evidence, roadmaps, baselines, work orders, session state, handoffs, public-sync,
and all other runtime paths are read-only to the worker.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A3 live proof | `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md`; material commit `4d9263c7d`; `Status: CLOSED_PASS_BOUNDED` | predecessor accepted before A4 | ACCEPT |
| A4 authorization | paired GC-018 baseline and activation roadmap A4 Detailed Design | both must remain source-consistent | ACCEPT |
| Live-call authority | operator instruction, 2026-07-13 | Alibaba numerically unmetered; diagnostic and stop controls binding | ACCEPT |

## Worker Autonomy / No-Question Rule

Repair allowed-scope test and checker failures directly by reading their source.
Return to the reviewer only for a current-source contradiction, a need outside
the exact manifest, a secret-safety failure, or a live failure whose diagnostic
does not justify a result-changing rerun.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A4 --title "SOT3 Activation A4 Failure And Recovery Boundary Proof" --date 2026-07-13 --base 48f5e70d3 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A3 closure 4d9263c7d PREDECESSOR_SATISFIED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified source facts, exact implementation design, evidence matrix, manifest, diagnostics, and handoff controls |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, Delta, public, operation-trace, scaffold-provenance, and read-ahead checker sources read |
| docOnlyNewFields | listed in New Doc-Only Fields |
| claimBoundary | dispatch authorization only; execution remains future worker evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`SOT3 failure recovery proof work-order authoring dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "SOT3 failure recovery proof work-order authoring dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "live provider negative recovery proof" --max-results 30 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | exact query above |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | worker must read `CVF_ADIF-0030` for live entrypoint control and `CVF_ADIF-0031` for repaired manifest fidelity |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | Status; exact manifest; Source Verification; handoff route; closure conversion; evidence reuse; runtime freshness; Public Export Disposition |
| gateRunPurpose | confirmation/evidence after source verification |
| claimBoundary | machine shape does not prove runtime or live behavior |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Flow package carries recipient, role, task, phase, dose, expiry, and state | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/types/distribution-package.ts` | `DistributionPackage` interface | `DistributionPackage` | Truth Flow schema | ACCEPT |
| Flow package creation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | lines 51-86 | `create` | `DistributionEngine` | ACCEPT |
| Flow read action | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | lines 112-141 | `deliverOrConsume` | `DistributionEngine` | ACCEPT |
| Consumption-time binding is absent | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | lines 128-141 | `DistributionEngine.deliverOrConsume` | Truth Flow distribution engine | REJECT |
| Truth Flow public package exports | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` | public export surface | `DistributionEngine` | Truth Flow package entrypoint | ACCEPT |
| Reference current-state authority | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | `computeCurrentReferenceState` | `computeCurrentReferenceState` | Truth Kernel | ACCEPT |
| Wrong-packet evidence fails admission | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts` | test `evidence bound to another packet` | `evaluate` | `TruthKernel` | ACCEPT |
| Product adapter currently creates and consumes Flow package | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | `evaluateSingleSot3KnowledgeChunk` | `evaluateSot3KnowledgeActivation` | SOT3 product adapter | ACCEPT |
| Durable evidence append and replay | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 278-367 | `Sot3ActivationEvidenceStore` | A2 evidence store | ACCEPT |
| Route SOT3 seam precedes provider call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 686-741 | `POST` | execute route | ACCEPT |
| Existing ENFORCE reject still calls provider once | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts` | test beginning line 488 | `executeAIMock` | execute route test | REJECT |
| Activation result is returned to route | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | lines 55-63 and 270-358 | `sot3` | `KnowledgeContextResult` | ACCEPT |
| Invalid mode rolls back to OFF | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | lines 567-573 | `resolveSot3KnowledgeActivationMode` | SOT3 product adapter | ACCEPT |
| A3 one-use live runner exists | EXISTS | `scripts/run_cvf_sot3_a3_live_proof.py` | full runner | `main` | A3 live proof runner | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
|---|---|---|
| `negativeCaseCount` | receipt count of executed A4 negative rows | DOC_ONLY_NEW |
| `zeroProviderCallCaseCount` | receipt count of rows whose provider spy stayed at zero | DOC_ONLY_NEW |
| `localNegativeGatePassed` | proves live recovery was released only after local proof | DOC_ONLY_NEW |
| `recoveryProviderCallCount` | call-level recovery denominator | DOC_ONLY_NEW |
| `rollbackProviderCallCount` | OFF rollback observation | DOC_ONLY_NEW |
| `claim` | bounded A4 claim token | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| A4 packet paths | absent before authoring | ACCEPT |
| A4 artifact token | `rg -n "SOT3-ACT-A4|SOT3 Activation A4" docs CVF_SESSION` returned no prior artifact | ACCEPT |
| historical evidence | A3 paths exist and are read-only inputs | ACCEPT |
| collision decision | create only A4-specific evidence and return paths | ACCEPT |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator-directed SOT3 A4 runtime and proof dispatch |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | dispatcher -> no-commit implementation/live-proof worker -> reviewer/closer |
| scope classification | bounded Truth Flow consumption, execute admission, local negative proof, and live recovery |
| risk sensitivity | R2 runtime and real-provider proof |
| escalation condition | stop for forbidden paths, authority movement, secret risk, unresolved negative gate, unjustified live rerun, A5, public-sync, or claim expansion |
| Dispatcher role | Codex dispatcher |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | Codex reviewer/closer after accepted worker return |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: A4 implements an already-absorbed SOT3 runtime
roadmap and does not scan, classify, or absorb a legacy corpus. No coverage
index row is owned by this tranche.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime proof, live proof, and work-order source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` plus paired A4 GC-018 and Source Verification Block |
| Owner surface | current governed CVF runtime source, A3 completion, and A4 reviewer completion |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch; reviewer may accept only fresh A4 evidence |
| Claim boundary | provider-local memory and external material are not source authority |

## Execution Plan

1. Capture a clean executionBaseHead and pass pre-implementation.
2. Add `DistributionConsumptionBinding` and a strict `consumeFor` operation
   that compares recipient, role, task, phase, and dose against the immutable
   package, then applies existing actionable, expiry, and current-reference
   checks. A mismatch returns typed `PACKAGE_CONSUMER_BINDING_MISMATCH`.
3. Update the SOT3 product adapter to deliver, strictly consume for its fixed
   product binding, and acknowledge. Do not add production fault injection.
4. In the execute route, inspect the returned `sot3` result. In ENFORCE, when
   SOT3 returns `REJECTED`, return a secret-safe 409 before `executeAI`. Also
   reject an explicitly requested governed collection that resolves to
   `NO_CONTEXT`; an unrequested empty retrieval must preserve ordinary route
   behavior. Update the pre-existing missing-provenance ENFORCE regression in
   `route.knowledge.test.ts` to expect the same 409 and zero provider calls;
   do not exempt `MISSING_PROVENANCE` and do not delete that regression.
5. Add a focused A4 test file. Use real Refinery, Kernel, Flow, adapter, and A2
   store APIs. Mock only the downstream provider to count calls.
6. Generate the deterministic negative receipt. The runner must refuse live
   execution unless every required row is present and green.
7. After that gate passes, invoke the existing real Alibaba path once using a
   fresh A4 evidence path. Record diagnostics before any result-changing rerun.
8. Prove OFF rollback separately: legacy context/provider behavior is restored
   and exactly one provider spy call occurs.
9. Run focused regressions, package tests, typecheck, build if source requires,
   secret scan, full worker-return gate, commit-steward preflight, and return
   without commit.

## Required Negative And Recovery Matrix

| Case | Required owner path | Required result | Provider-call assertion |
|---|---|---|---|
| empty source input | Refinery plus product adapter | not approved | zero |
| structurally invalid source | Refinery plus product adapter | `REFINERY_NOT_READY` | zero |
| wrong-packet evidence | real Kernel | non-acceptance | zero |
| expired reference | Kernel resolver plus Flow | rejected | zero |
| revoked reference | Kernel resolver plus Flow | rejected | zero |
| superseded or inactive reference | Kernel resolver plus Flow | rejected | zero |
| wrong recipient | strict Flow consume | binding mismatch | zero |
| wrong role | strict Flow consume | binding mismatch | zero |
| wrong phase | strict Flow consume | binding mismatch | zero |
| wrong task | strict Flow consume | binding mismatch | zero |
| wrong dose | strict Flow consume | binding mismatch | zero |
| expired package | strict Flow consume | package expired | zero |
| duplicate request same record | A2 store | duplicate no-op | zero additional call |
| duplicate request conflict | A2 store | typed conflict | zero |
| replay after acknowledgement | strict Flow consume | not actionable | zero |
| restart and valid recovery | fresh A2 store reader | integrity-valid record restored | live released only after PASS |
| corrupt main file | A2 store | typed corrupt-store diagnostic | zero |
| partial/temp write | A2 store fault port | prior main record survives | zero |
| ENFORCE to OFF rollback | execute route | legacy behavior restored | exactly one provider spy call |
| bounded live recovery | real execute route and Alibaba | approved context and correlated durable evidence | exactly one per invocation |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | add strict consumption binding without weakening existing checks |
| `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` | export the new consumption-binding type required by the product adapter |
| `EXTENSIONS/CVF_TRUTH_FLOW/tests/negative-matrix.test.ts` | cover binding, inactive lifecycle, expiry, and replay |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | use strict Flow consumption |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.test.ts` | add adapter rejection coverage |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | stop ENFORCE rejection before provider call |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts` | update the existing ENFORCE missing-provenance assertion to 409 and zero provider calls; preserve the regression |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation-failure-recovery.test.ts` | new route-level zero-call and rollback proof |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.test.ts` | fill any missing A4 restart, corrupt, partial, or replay row |
| `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | local-negative-first runner and one-use live permit |
| `docs/reviews/evidence/sot3-act-a4-failure-recovery-negative-receipt-2026-07-13.json` | deterministic negative and rollback receipt |
| `docs/reviews/evidence/sot3-act-a4-failure-recovery-live-diagnostic-2026-07-13.json` | secret-safe launch/failure diagnostic |
| `docs/reviews/evidence/sot3-act-a4-failure-recovery-live-receipt-2026-07-13.json` | fresh correlated recovery receipt |
| `docs/reviews/evidence/sot3-act-a4-failure-recovery-manifest-2026-07-13.json` | hash manifest over A4 evidence |
| `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_WORKER_RETURN_2026-07-13.md` | checker-safe no-commit worker return |

No other file may be changed. If a required correction needs another path,
return `BLOCKED_WITH_REASON` with source evidence.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence owner |
|---|---|---|
| invalid and empty source | matrix rows 1-2 | adapter test and negative receipt |
| wrong packet evidence | matrix row 3 | Kernel real API test |
| inactive reference states | matrix rows 4-6 | Kernel/Flow tests |
| wrong routing/dose/expiry | strict consume and matrix rows 7-12 | Flow tests |
| duplicate and replay | matrix rows 13-15 | store and Flow tests |
| restart and corruption | matrix rows 16-18 | A2 store tests |
| rollback | matrix row 19 | route test |
| zero provider calls | route provider spy and receipt totals | A4 runner |
| bounded recovery | local gate then real Alibaba call | live receipt and manifest |

## Evidence Reuse Declaration

priorEvidenceReused: true

reusedEvidence: A3 completion and runner are prerequisite/implementation-pattern inputs only.

freshEvidenceRequired: all A4 negative, rollback, diagnostic, recovery, and manifest artifacts.

reuseBoundary: A3 evidence cannot satisfy any A4 matrix row or A4 claim.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one implementation/live-proof worker, then independent reviewer/closer |
| phase | implementation and worker return |
| baseHeadFor(phase) | dispatchBaseHead=`48f5e70d3`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Work-Order Fulfillment Manifest only |
| traceScope(phase, actor) | worker records commands, calls, evidence, diff, and HEAD; reviewer owns closure conversion |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | A3 evidence is read-only; A5 and unrelated changes forbidden |
| nextMoveSurfaces | reviewer updates roadmap, session state, handoff, and memory only following the accepted material closure commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_COMPLETION_2026-07-13.md` |
| reviewerOwnedClosurePaths | completion review; paired baseline/work-order status; activation roadmap; active session state sources; active handoff; session memory |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_WORKER_RETURN_2026-07-13.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include Purpose, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Checker Source Read-Ahead Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, External Knowledge Intake
Routing, Rescan Intelligence Hardening, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Machine
Closure Package, Claim Boundary, git status, Changed Files, retrospective,
command evidence, and no-commit statement.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 48f5e70d3 --head HEAD
pnpm --dir EXTENSIONS/CVF_TRUTH_FLOW test
pnpm --dir EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web exec vitest run src/lib/sot3-knowledge-adapter.test.ts src/lib/sot3-activation-evidence-store.test.ts src/app/api/execute/route.knowledge.test.ts src/app/api/execute/route.sot3-activation-failure-recovery.test.ts
python scripts/run_cvf_sot3_a4_failure_recovery_proof.py --local-only --json
python scripts/run_cvf_sot3_a4_failure_recovery_proof.py --live --json
pnpm --dir EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web typecheck
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --steward worker-return --base 48f5e70d3 --head HEAD
git diff --name-status
git status --short
```

If the actual post-dispatch HEAD differs, substitute captured
executionBaseHead for `48f5e70d3` in worker-range commands.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_AT_WORKER_EXECUTION_ONLY |
| runtimeMutationAuthorized | exact Flow, adapter, and route paths in the manifest |
| freshnessVerificationMode | fresh local negative proof followed by fresh live recovery |
| priorVerificationArtifact | A3 is prerequisite evidence only |
| requiredFutureAction | worker implements and returns uncommitted A4 evidence |

## Acceptance Criteria

- all matrix rows are present and pass through their named real owners;
- ENFORCE rejections and explicit requested-collection no-context stop before
  provider execution with a secret-safe 409;
- OFF rollback preserves legacy provider execution;
- no production fault injection or caller approval shortcut exists;
- live recovery is impossible before the local negative gate passes;
- each live invocation is one call, with diagnostics before any rerun;
- evidence is secret-safe, content-safe, fresh, hashed, and correlated;
- exact manifest only, HEAD unchanged, no worker commit.

## Evidence Requirements

Provide per-row owner outcome and provider-call count, local-gate release
evidence, fresh diagnostic and live receipt, evidence hashes, focused test and
typecheck output, secret scan, exact diff, captured HEAD, and no-commit status.
Event counts must not be presented as provider-call counts.

## Review Gate

The independent reviewer must reproduce the local matrix, inspect strict
binding and route ordering, recompute evidence hashes, verify the live receipt
against diagnostic/call accounting, run pre-closure, and reject any matrix
omission, provider call on a reject row, secret leak, or scope expansion.

## Closure Checklist

- [x] Exact manifest only after R2; no historical A3 mutation.
- [x] All negative and rollback rows resolved with command evidence.
- [x] Local negative gate preceded the live permit.
- [x] Live receipt is fresh, one-call-per-invocation, and secret-safe.
- [x] Worker-return full gate and reviewer closure gates pass.
- [x] Worker HEAD remained unchanged and worker made no commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every checklist item is evidenced.
Return `BLOCKED_WITH_REASON` for a source contradiction, forbidden-path need,
unresolved local negative, unsafe evidence, or diagnostically unjustified
live rerun. Do not return a partial PASS.

## Operator Checkpoint

No operator checkpoint is parked before worker execution. Stop and return only
if new authority is required beyond A4 or if a live failure cannot be safely
resolved under the diagnostic and result-changing-action rules.

## Stop Conditions

- current source contradicts a verified claim;
- implementation requires a path outside the exact manifest;
- strict binding would move Kernel or Flow authority into CVF Web;
- local negative gate is not fully green;
- live output is failed/partial/unclear without a complete diagnostic;
- a proposed rerun has no result-changing action;
- raw content or a secret would need to be persisted;
- work expands into A5, public-sync, prompt tuning, or provider comparison.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace; Alibaba only during worker recovery proof |
| Session or invocation | SOT3-ACT-A4 dispatch, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | governed reads, source verification, scaffold, ADIF resolver, apply_patch, dispatch gates |
| Target paths | paired packet now; exact worker manifest during execution |
| Allowed scope source | operator authority, A3 accepted closure, A4 roadmap release |
| Before status evidence | clean `48f5e70d3`; A4 packet paths absent |
| After status evidence | source-verified A4 packet ready for worker |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | A4 only |
| Claim boundary | no execution claim at dispatch |
| Agent type | dispatcher |
| Invocation ID | `sot3-act-a4-dispatch-2026-07-13` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | dispatch authorization and future A4 bounded proof |
| claimDisposition | CLAIM_REJECTED: no A4 runtime or live behavior is claimed at dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: future fresh A4 receipts required |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: future local matrix and real recovery required |
| invocationBoundary | one explicit runner invocation per live call |
| interceptionBoundary | route-level SOT3 ENFORCE admission only; no universal provider wrapper |
| claimLanguage | future PASS may claim only `SOT3_FAILURE_RECOVERY_PROVEN_BOUNDED` |
| forbiddenExpansion | no A5, final claim, production universality, public, prompt, or provider-comparison claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime/evidence tranche using operator-local credentials; no
public-sync authority exists.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired A4 baseline | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | A4 completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | activation roadmap | `Status: A4_CLOSED_PASS_BOUNDED_A5_PACKET_NEXT` | PASS |
| Registry JSON | corpus registry | BLOCKED with reason: A4 has no corpus ownership | BLOCKED with reason |
| Registry Markdown | corpus front door | BLOCKED with reason: A4 has no catalog ownership | BLOCKED with reason |
| External evidence digest | A4 evidence manifest | live receipt sha256 `8489595af1eb0050dd4b89107c362f7447f3933ce8ea553d6f9b3877b63cedd1` | PASS |
| System loop interlock | N/A with reason: no automated loop edge added | N/A | N/A with reason |
| Session continuity | separate post-material session sync | pending until material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| local negative gate PASS | 19/19 rows GREEN | PASS |
| zero-call negative denominator | 18 rows | PASS |
| rollback provider-spy denominator | 1 call | PASS |
| retained recovery call denominator | 1 Alibaba call | PASS |
| bounded claim token | `SOT3_FAILURE_RECOVERY_PROVEN_BOUNDED` | PASS |

## Claim Boundary

This work order authorizes exactly A4. Even a complete worker return remains
pending independent review and may support only
`SOT3_FAILURE_RECOVERY_PROVEN_BOUNDED`. The final
`LIVE_GOVERNANCE_PROVEN_BOUNDED` claim remains reserved for accepted A5.

## Bounded Repair R1 - Writable Manifest Reconciliation

The first worker return correctly identified that the behavior-changing
Source Verification `REJECT` row for `route.knowledge.test.ts` conflicted with
the original writable manifest. R1 adds that one existing test path and
requires its missing-provenance ENFORCE assertion to move from one provider
call to secret-safe 409 plus zero calls. All other authority, runtime, live,
claim, and no-commit boundaries remain unchanged.

## Bounded Repair R2 - Source-Required Export And Evidence Reconciliation

Independent review found that the product adapter imports the new
`DistributionConsumptionBinding` type through the Truth Flow package public
entrypoint, so `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts` is a source-required
part of the same bounded implementation. R2 adds that path to the exact
manifest. R2 also requires the runner's wrong-packet row to execute the real
Truth Kernel negative-matrix test and requires rollback provider-spy count to
be reported as one, leaving 18 of 19 local rows with zero provider calls.
No additional live call is authorized or required; the accepted live
observation remains immutable and only derived local aggregates and hashes
may be reconciled.
