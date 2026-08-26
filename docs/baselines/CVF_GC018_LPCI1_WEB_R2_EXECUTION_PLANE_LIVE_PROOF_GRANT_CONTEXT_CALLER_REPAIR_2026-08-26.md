# CVF GC-018 Baseline - LPCI1 Web R2 Execution Plane Live-Proof Grant Context Caller Repair

Memory class: governed-dispatch-baseline

Status: ACCEPTED_FOR_DISPATCH

docType: baseline

Date: 2026-08-26

Batch ID: LPCI1-WEB-R2-EXECUTION-PLANE-GRANT-CONTEXT-CALLER-REPAIR

Dispatch base head: `6ebf7b4d1`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

## Purpose

Repair the one P1 successor left by LPCI1 Web R1: two Execution Plane call
sites still construct the live-proof harness without the orchestrator grant
context EAFR-R12 made mandatory. Preserve fail-closed authority, make the
non-live package and Web checks green, and prove the exact cvf-web production
build without executing a provider or reading a secret.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id LPCI1-WEB-R2 --title "Execution Plane Live-Proof Grant Context Caller Repair" --date 2026-08-26 --base f7f5cf1ef --commit-mode WORKER_MUST_NOT_COMMIT --dependency "LPCI1 Web R1 closed blocked at f7f5cf1ef" --stdout` |
| generatedProfile | public-sync-related private no-commit repair |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact authority propagation, denial accounting, runner pre-secret gate and build proof |
| checkerReadAheadConfirmation | work-order dispatch, task route, worker-return, trace, public export and Delta checkers already read for this packet family |
| docOnlyNewFields | Authority Consumption Accounting Invariants |
| claimBoundary | dispatch evidence only; no provider, live, hosted or public readiness claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R1 package composition | accepted blocked material `f7f5cf1ef`; original parse and monorepo-relative failures removed | only the independent TypeScript blocker may proceed | RELEASED_BOUNDED |
| exact blocker | cvf-web `npm run check` reports only two missing `LiveProofHarnessOptions` authority-context calls at lines 245 and 362 | source owner and test seam must exist | RELEASED |
| external effects | public export remains blocked | no provider, secret, push or deploy in R2 | RETAINED_PARK |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| live-proof harness requires grant identity and call-count context | TYPE_CONTRACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `LiveProofHarnessOptions` | `providerExecutionGrant`, `workerAgentId`, `delegationId`, `grantId`, `consumedCalls` | EAFR-R12 harness authority boundary | ACCEPT |
| harness evaluates authority before secret resolution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `runLiveProof` pre-secret branch | `evaluateProviderExecutionAuthority` | Control Plane evaluator | ACCEPT |
| direct lane omits all required context | NEGATIVE_SEARCH | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | `runDirectLane` harness call | `runLiveProof` | Execution Plane caller | ACCEPT |
| MAO worker lane omits all required context | NEGATIVE_SEARCH | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` | `runMaoWorkerCall` harness call | `runLiveProof` | Execution Plane caller | ACCEPT |
| runner loads key-bearing local environment before any grant preflight | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts` | start of `main` | `loadEnvLocal` | MAO live pilot runner | ACCEPT |
| existing canonical parsing and pre-environment evaluator pattern exists | OWNER_REUSE | `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts` | `parseProviderExecutionGrant` and `main` preflight | `CVF_PROVIDER_EXECUTION_GRANT_JSON` | Model Gateway runner | ACCEPT |
| focused fake-only test owner exists | TEST_SEAM | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.live.provider.value.pilot.test.ts` | direct, MAO and shared-ledger suites | `runDirectLane`; `runMaoLane` | Execution Plane tests | ACCEPT |

## Existing Vs Proposed Symbols

| Symbol | Existing state | R2 disposition |
| --- | --- | --- |
| `LiveProofHarnessOptions` | canonical required authority shape | reuse; do not weaken or make optional |
| `evaluateProviderExecutionAuthority` | canonical Control Plane evaluator | reuse before runner environment loading and before ledger/live attempt commitment |
| `MaoLiveCallLedger` | counts claimed live-call slots | reconcile with grant `consumedCalls`; denial must not count as a provider call |
| MAO runner | live-capable script without grant intake | require secret-safe grant parsing and fail before `.env.local` loading |

## Authority Consumption Accounting Invariants

1. `liveAuthorized: true` never substitutes for a provider execution grant.
2. Missing, malformed, expired or mismatched authority stops before local
   key-bearing environment loading, endpoint resolution, secret resolution and
   injected fetch invocation.
3. Direct, first MAO and revision attempts bind the same worker, delegation and
   grant identities.
4. `consumedCalls` advances deterministically across a shared ledger; a denied
   attempt consumes neither provider-call budget nor the MAO live-call ledger.
5. Tests use synthetic grants, fixed time, fake environment and injected fetch
   only. No live provider command is allowed.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R2 artifact collision | exact names absent before authoring | CREATE_NEW |
| other caller sites | `rg -n "runDirectLane\\(|runMaoLane\\(" EXTENSIONS scripts` | source, focused tests and one runner only |
| existing grant owner | Control Plane grant and evaluator plus Model Gateway runner pattern found | REUSE_OWNER |
| successor count | R1 names only this P1 blocker | ONE_CONSOLIDATED_R2 |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Code implementation`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Code implementation" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary no-commit implementation and independent review apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | required dispatch envelope, source verification, trace, no-commit, public disposition and worker-return packet fields |
| gateRunPurpose | confirmation after source mapping, not first discovery |
| claimBoundary | checker conformance does not prove runtime or build behavior |

## Risk And Stop Conditions

Stop if success requires weakening EAFR-R12, fabricating an orchestrator grant,
reading a secret, making a provider call, changing another live harness, or
editing public-sync. A new authority field must be caller-supplied and tested;
it may not be synthesized from trace IDs or hard-coded identities.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "LPCI1-WEB-R2",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "RUNTIME_INTEGRATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION", "docs/baselines", "docs/work_orders", "docs/reviews", "docs/roadmaps"],
  "claims": ["grant context reaches both MAO live-proof caller paths and exact non-live production build exits zero"],
  "requiredProof": ["focused fake-only tests", "package TypeScript", "cvf-web TypeScript", "exact production build", "independent review"],
  "operatorCheckpoints": ["scope expansion", "any provider/live/public effect"],
  "forbiddenEffects": ["provider call", "secret read", "public-sync mutation", "push", "deploy", "worker commit"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Value disposition: `CONTINUE_HIGH_VALUE`; one source-backed P1 blocks the
selected production build and is consolidated into the only R2 successor.

## Decision / Proposed Tranche

Decision: `PROCEED_TO_R2_NO_COMMIT_IMPLEMENTATION`. R2 is the only admitted
successor because it closes the exact build blocker while preserving the
existing grant evaluator and external-effect park.

## Evidence / Verification

Dispatch evidence consists of the independently reproduced TypeScript errors,
the EAFR-R12 harness type and pre-secret authority ordering, the tracked MAO
source/test/runner caller cluster, and the accepted blocked R1 material commit.
Implementation proof still requires the commands in the paired work order.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: R2 is private non-live repair authority only. Public sync, push,
Netlify deploy and hosted observation remain reviewer/operator checkpoints.

## Claim Boundary

This baseline authorizes one private no-commit caller reconciliation. It does
not authorize a live run, provider grant issuance, secret access, public write,
deployment or production-readiness claim.
