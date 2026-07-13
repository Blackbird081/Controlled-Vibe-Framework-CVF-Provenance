# CVF GC-018 Baseline - SOT3 Activation A4 Failure And Recovery Boundary Proof

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

docType: baseline

Batch ID: SOT3-ACT-A4

Date: 2026-07-13

Dispatch base head: `48f5e70d3`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: Codex reviewer/closer

Worker target: delegated implementation and live-proof worker

## Purpose

Authorize one bounded A4 implementation and proof tranche that closes the
failure boundary between SOT3 and the execute provider call, proves the
roadmap negative matrix with real owner APIs, and demonstrates one bounded
recovery after local negative proof passes.

## Authorization / Decision

The operator authorized A0 through A5 toward
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, explicitly allowed Alibaba live calls
without a numeric quota, and retained diagnostic-before-rerun plus
diminishing-return controls. A3 closed at material commit `4d9263c7d` and the
activation roadmap names fresh A4 packet authoring as the next allowed move.

## Baseline / Proposed Tranche

Current A3 proves the happy path, but the product route still proceeds to the
provider without a knowledge block after an ENFORCE rejection. Truth Flow also
validates complete routing fields at creation but has no consumption-time
comparison against the intended recipient, role, task, phase, and dose. A4
adds those two bounded fail-closed seams, then records deterministic negative,
restart/replay, rollback, and one real-provider recovery evidence set.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A3 accepted live proof | `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md`; material commit `4d9263c7d`; `Status: CLOSED_PASS_BOUNDED` | accepted provider correlation exists before A4 recovery proof | ACCEPT |
| A4 roadmap release | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `Status: A3_CLOSED_PASS_BOUNDED_A4_PACKET_NEXT`; A4 Detailed Design | fresh source-verified A4 packet is required | ACCEPT |
| Operator live authority | operator instruction on 2026-07-13 | Alibaba calls are numerically unmetered; diagnostic and stop controls remain binding | ACCEPT |

## Risk Classification

Risk: R2 runtime and live proof.

Reason: A4 changes a bounded Truth Flow consumption contract and the execute
route's ENFORCE failure response, then makes one controlled provider recovery
call. It does not change source authority, provider selection, public surfaces,
or universal SOT3 behavior.

## Allowed Scope

- add a strict Truth Flow consumption binding and typed mismatch reason;
- make the existing product adapter use that strict consumption boundary;
- expose a route result that blocks provider execution only for SOT3 ENFORCE
  rejection or an explicitly requested but empty governed collection;
- add focused tests and a deterministic A4 evidence runner;
- reuse the A3 live test implementation without altering its historical
  receipt or claim;
- create fresh A4 negative and recovery evidence plus worker return;
- make Alibaba recovery calls only after the local negative gate passes.

## Forbidden Scope

- no prompt tuning, provider comparison, output-quality scoring, or broad
  retry campaign;
- no change to Refinery truth ownership, Kernel decision ownership, retrieval
  tenant scope, provider routing policy, public-sync, or release bundle;
- no production test hook or caller-supplied approval boolean;
- no raw key, raw prompt, raw provider body, or unredacted response in evidence;
- no A5 implementation or final roadmap claim;
- no commit by the worker.

## Call Control And Stop Rule

Alibaba calls have no numeric quota for this tranche. The A4 runner must still
permit no live call until local negative proof is green, issue at most one call
per explicit runner invocation, and require a secret-safe diagnostic plus a
result-changing action before every rerun after failure or ambiguity. Stop when
recovery is proven once; repeated equivalent success has no additional value.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A4 --title "SOT3 Activation A4 Failure And Recovery Boundary Proof" --date 2026-07-13 --base 48f5e70d3 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A3 closure 4d9263c7d PREDECESSOR_SATISFIED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with A3 release evidence, verified owner seams, exact matrix, exact manifest, diagnostic controls, and claim boundary |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, Delta, public, operation-trace, scaffold-provenance, and read-ahead checker sources read |
| docOnlyNewFields | A4 evidence fields are declared in the paired work order New Doc-Only Fields table |
| claimBoundary | dispatch authorization only; no A4 execution claim |

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
| Dispatch impact | A3 ADIF-0030 remains a mandatory source even though the resolver returned no lexical match |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirmation after source verification, not first discovery |
| claimBoundary | checker compliance cannot substitute for local negative evidence or the real recovery call |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Flow creation validates complete routing and dose | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | lines 51-86 | `create` | `DistributionEngine` | ACCEPT |
| Flow read action checks lifecycle, expiry, and current reference state | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | lines 112-141 | `deliverOrConsume` | `DistributionEngine` | ACCEPT |
| Flow has no consumption-time recipient binding | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_FLOW/src/distribution/distribution-engine.ts` | lines 128-141 | `DistributionEngine.deliverOrConsume` | Truth Flow distribution engine | REJECT |
| Kernel rejects evidence bound to another packet | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts` | test `evidence bound to another packet` | `evaluate` | `TruthKernel` admission/evaluation | ACCEPT |
| Kernel resolves expired, revoked, and superseded references | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | `computeCurrentReferenceState` | `computeCurrentReferenceState` | Truth Kernel reference resolver | ACCEPT |
| Store has atomic append, duplicate, integrity, and restart reads | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 272-367 | `Sot3ActivationEvidenceStore` | A2 evidence store | ACCEPT |
| Route resolves SOT3 before provider execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 686-741 | `POST` | execute route | ACCEPT |
| ENFORCE rejection currently omits context but still reaches provider | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts` | test beginning line 488 | `executeAIMock` | execute route knowledge test | REJECT |
| OFF is the fail-safe fallback for missing or invalid activation mode | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | lines 567-573 | `resolveSot3KnowledgeActivationMode` | SOT3 product adapter | ACCEPT |
| A3 runner provides one-use live permit and diagnostics | RUNTIME_BEHAVIOR | `scripts/run_cvf_sot3_a3_live_proof.py` | full runner | `main` | A3 live proof runner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned path existence | `Test-Path` returned false for the A4 baseline and work-order paths before authoring | ACCEPT |
| token collision | `rg -n "SOT3-ACT-A4|SOT3 Activation A4" docs CVF_SESSION` returned no prior artifact | ACCEPT |
| collision decision | create A4-specific artifacts; never overwrite A3 evidence | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_AT_WORKER_EXECUTION_ONLY |
| runtimeMutationAuthorized | BOUNDED_FLOW_CONSUMPTION_AND_ROUTE_REJECTION_ONLY |
| freshnessVerificationMode | FRESH_LOCAL_NEGATIVE_THEN_LIVE_RECOVERY |
| priorVerificationArtifact | A3 completion proves happy path only and is prerequisite evidence, not A4 proof |
| requiredFutureAction | implement exact manifest, pass local negative gate, then create fresh A4 recovery receipt |

## Acceptance Criteria

- every A4 negative row has a deterministic owner result and provider-call
  count of zero when it reaches the execute admission boundary;
- strict consumption rejects wrong recipient, role, task, phase, or dose;
- wrong packet evidence and non-active references fail closed through real
  Kernel and Flow APIs;
- duplicate/replay, restart/recovery, corruption/partial write, and atomicity
  use the real A2 store;
- OFF rollback preserves pre-SOT3 provider behavior;
- after local proof passes, one real Alibaba recovery call correlates to fresh
  durable SOT3 evidence without recording secrets or raw content;
- no worker commit and no A5/final claim.

## Evidence / Verification

The worker must provide package and route test output, a machine-readable
negative receipt with per-case provider call counts, a fresh live recovery
receipt, hash manifest, secret scan, exact diff, and no-commit worker return.
Prior A3 evidence releases the dependency only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: A4 changes private provenance runtime and uses operator-local live
credentials. Public export requires a later explicit packet.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired A4 work order | `Status: DISPATCH_READY` | N/A with reason: execution not started |
| Completion or reviewer artifact | reviewer-owned completion path in work order | future reviewer verdict | N/A with reason: closure not started |
| Roadmap state | activation roadmap | `Status: A3_CLOSED_PASS_BOUNDED_A4_PACKET_NEXT` | PASS |
| Registry JSON | corpus scan registry | no corpus ownership | BLOCKED with reason: A4 is not corpus intake and has no GC-051 ownership |
| Registry Markdown | corpus intelligence README | no catalog ownership | BLOCKED with reason: A4 is not corpus intake and has no registry-front-door ownership |
| External evidence digest | future A4 evidence manifest | future SHA-256 entries | N/A with reason: worker-owned future evidence |
| System loop interlock | system-loop standard | no automated loop edge changed | N/A with reason: no loop mutation |
| Session continuity | active session sources | reviewer-owned post-closure sync | N/A with reason: dispatch does not change next move |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| accepted A3 prerequisite | material commit `4d9263c7d` and completion artifact | PASS |
| fresh A4 negative receipt | worker-owned future artifact | N/A with reason: execution not started |
| fresh A4 recovery receipt | worker-owned future artifact | N/A with reason: execution not started |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime proof, live proof, and work-order source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` plus Source Verification Block |
| Owner surface | current governed CVF runtime source, A3 completion, and future A4 review |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch |
| Claim boundary | no external or provider-local material is source authority |

## Claim Boundary

This baseline authorizes only A4's bounded failure and recovery work. A PASS may
claim `SOT3_FAILURE_RECOVERY_PROVEN_BOUNDED`; it may not claim final
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, production universality, user value, or A5.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | SOT3-ACT-A4 dispatch authoring, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | startup reads, source scan, scaffold helper, ADIF resolver, checker reads, apply_patch, dispatch gates |
| Target paths | paired A4 baseline and work order |
| Allowed scope source | operator A0-A5 authority, accepted A3 closure, activation roadmap A4 release |
| Before status evidence | clean worktree at `48f5e70d3`; planned packet paths absent |
| After status evidence | source-verified A4 dispatch packet |
| Diff evidence | `git diff --name-status` before packet commit |
| Approval boundary | A4 packet authoring only |
| Claim boundary | no A4 execution claim at dispatch |
| Agent type | dispatcher |
| Invocation ID | `sot3-act-a4-dispatch-2026-07-13` |
| Expected manifest | paired A4 baseline and work order |
| Actual changed set | paired A4 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
