# CVF Agent Work Order - LPCI1 Web R2 Execution Plane Live-Proof Grant Context Caller Repair

Memory class: governed-work-order

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-26

Batch ID: LPCI1-WEB-R2-EXECUTION-PLANE-GRANT-CONTEXT-CALLER-REPAIR

dispatchBaseHead: `6ebf7b4d1`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: no-commit authority-sensitive caller repair worker. The current
orchestrator is independent reviewer/closer.

Canonical packet: this work order and
`docs/baselines/CVF_GC018_LPCI1_WEB_R2_EXECUTION_PLANE_LIVE_PROOF_GRANT_CONTEXT_CALLER_REPAIR_2026-08-26.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R1 material `f7f5cf1ef` fixed package composition and
closed blocked only on two Execution Plane authority-context caller errors.

Do-not-misread notes: compile repair must preserve and extend EAFR-R12
fail-closed authority. Do not fabricate a grant, run the live script, read
`.env.local`, invoke a provider, mutate public-sync, push or deploy.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, EAFR-R12 harness/evaluator, all selected source/test
files, then capture HEAD and clean-state evidence.

Return contract: implement only the exact Write Ownership subset, run non-live
proof, create the named return, leave HEAD unchanged and staging empty, and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Make the MAO live-value caller accept and propagate the canonical provider
execution grant context, fail closed before any secret-bearing environment or
provider attempt, account grant consumption across direct/MAO/revision calls,
and restore exact cvf-web production build exit zero without a live call.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id LPCI1-WEB-R2 --title "Execution Plane Live-Proof Grant Context Caller Repair" --date 2026-08-26 --base f7f5cf1ef --commit-mode WORKER_MUST_NOT_COMMIT --dependency "LPCI1 Web R1 closed blocked at f7f5cf1ef" --stdout` |
| generatedProfile | public-sync-related private no-commit repair |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact authority propagation, denial accounting, runner pre-secret gate and build proof |
| checkerReadAheadConfirmation | work-order dispatch, task route, worker-return, trace, public export and Delta checkers read for this packet family |
| docOnlyNewFields | Authority Consumption Accounting Invariants |
| claimBoundary | dispatch authoring provenance only; no runtime/provider/live/public claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R1 accepted blocked | material `f7f5cf1ef` and reviewer addendum in its return | RELEASED |
| exact two-call-site error | reviewer reran cvf-web `npm run check`; only lines 245 and 362 fail on missing context | ACCEPT |
| canonical authority owner | Control Plane evaluator and EAFR-R12 harness contract source-verified | REUSE_REQUIRED |

## Authority And Scope

Operator authorized serious roadmap repair and independent review. This R2 is
the sole source-backed successor. Worker authority is private, local, fake-only
and no-commit; reviewer retains every public or external effect.

## Authority Chain

Operator serious-repair authority -> accepted blocked R1 material
`f7f5cf1ef` -> paired R2 GC-018 baseline -> this no-commit work order -> one
worker -> independent reviewer/closer.

## Agent Roles

Worker: bounded authority-context caller implementer. Reviewer/closer: current
orchestrator. Session-sync and every material/public commit remain reviewer
owned.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake source | R1 independently reproduced build blocker |
| Route | MULTI_AGENT_SINGLE_ROLE |
| canonical route mode | MULTI_AGENT_SINGLE_ROLE |
| risk sensitivity | P1 build blocker; P3 authority-sensitive caller repair |
| scope classification | bounded private fake-only authority-context caller repair |
| selected role route | dispatcher -> no-commit worker -> independent reviewer |
| Worker role | propagate existing grant context and prove fake-only denial/consumption behavior |
| Reviewer role | inspect authority semantics, rerun exact build and own commit/export decision |
| Commit mode | WORKER_MUST_NOT_COMMIT |
| Checkpoint disposition | local manifest released; external effects remain parked |
| escalation condition | any owner expansion, weakened grant gate, secret/live/public effect or new authority type |

## Pre-Flight Checks

Capture execution HEAD, prove dispatch ancestry, private/public worktrees clean
and staging empty, confirm every selected path, and rerun or cite the exact two
TypeScript diagnostics before editing.

## Required First Reads

1. paired R2 baseline
2. R1 worker return and reviewer addendum
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
4. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts`
6. every selected Execution Plane source/test/package path

## Write Ownership

Worker may change only the minimum subset of:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package-lock.json`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.live.provider.value.pilot.test.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts`
- one NEW focused static/runner test under `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/` only if the existing test cannot prove pre-environment ordering
- one GC-051 per-entry source plus generated aggregate only if a new test path is created
- `docs/reviews/CVF_LPCI1_WEB_R2_EXECUTION_PLANE_LIVE_PROOF_GRANT_CONTEXT_CALLER_REPAIR_WORKER_RETURN_2026-08-26.md`

Do not touch the R1 package-composition source, the Control Plane evaluator,
the Model Gateway harness, cvf-web source, public-sync or session state.

## Required Artifact Manifest

| Artifact | Required state |
| --- | --- |
| Execution Plane live-pilot source | required if implementation proceeds |
| existing focused test | required and expanded |
| live-pilot runner | required; must deny before local env loading |
| package manifest/lock | only if canonical Control Plane package dependency is needed |
| worker return | required at exact named path |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| authority-context caller API | require and propagate canonical grant fields |
| runner pre-secret gate | parse/evaluate before local environment loading |
| consumption accounting | prove exact direct/MAO/revision ordinals and denial non-consumption |
| fake-only tests | positive plus missing/mismatched/expired/exhausted negatives |
| worker return | exact changed set, command receipts and no-commit evidence |

## Authority Consumption Accounting Invariants

1. Reuse `ProviderExecutionGrant` and `evaluateProviderExecutionAuthority`;
   no parallel grant type or evaluator.
2. `runDirectLane` and `runMaoLane` require caller-supplied authority context.
3. The runner parses `CVF_PROVIDER_EXECUTION_GRANT_JSON` secret-safely and
   evaluates the exact provider/identity/grant binding before `loadEnvLocal`,
   key-alias inspection or endpoint resolution.
4. Each actual harness attempt receives the same identities and the correct
   pre-call `consumedCalls` ordinal.
5. Denied authority produces zero fetches, zero secret resolution and zero
   increment of the live-call ledger/provider-call count.
6. The harness still re-evaluates authority; caller preflight is defense in
   depth, not a bypass.
7. All tests use synthetic grant metadata, fixed `nowIso`, fake environment and
   injected fetch. No provider or network call is allowed.

## Execution Plan

1. Define the smallest shared authority-context input using canonical types.
2. Add a caller-side canonical evaluator gate before live-call ledger claim.
3. Propagate context through direct, MAO first attempt and optional revision.
4. Reconcile `consumedCalls` with shared ledger call ordering.
5. Repair the runner so grant parsing/evaluation precedes key-bearing env load.
6. Add positive and adversarial fake-only tests for missing, malformed,
   mismatched, expired and exhausted grants plus direct/MAO/revision ordering.
7. Run package checks/tests, cvf-web check, exact production build and gates.

## Verification Commands

```powershell
npm --prefix EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION run check
npm --prefix EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION test -- --run tests/mao.live.provider.value.pilot.test.ts
npm --prefix EXTENSIONS/CVF_MODEL_GATEWAY run check
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web run check
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web test -- --run src/lib/lpci/provider-binding.test.ts src/app/api/lpci/query/route.test.ts src/lib/package-test-script-boundary.test.ts
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web run build
python -X utf8 governance/compat/run_worker_return_fast_gate.py
git status --short
```

The live runner command itself is forbidden. Tests must prove zero real network
and zero secret read by injected fakes and source ordering.

## Acceptance Criteria

- both TypeScript errors are absent without weakening harness types;
- missing/mismatched/expired/exhausted grant paths fail before environment,
  endpoint, secret, ledger and fetch effects;
- valid synthetic context reaches direct, MAO and revision attempts with exact
  monotonically increasing consumption ordinals;
- Execution Plane focused tests and TypeScript pass;
- Model Gateway and focused cvf-web regression proof pass;
- exact cvf-web production build exits zero;
- no live/provider/secret/public effect and no path outside ownership;
- public-sync remains clean, HEAD unchanged and staging empty.

## Evidence Requirements

Record before/after TypeScript diagnostics, exact authority context shape,
denial ordering, call-consumption sequence, fake fetch counts, every command
and count, production build exit code, generated-artifact cleanup, both Git
statuses and zero external-effect confirmation.

## Fail Conditions

Return `BLOCKED_WITH_REASON` if completion requires weakening EAFR-R12,
hard-coding or self-issuing grant identity, reading `.env.local`, running the
live script, changing another owner, or making any external/public effect.

## Review Gate

Reviewer independently inspects every authority field and denial branch,
replays focused fake-only proof, runs both TypeScript checks and the exact
production build, verifies public-sync remains untouched, then decides closure.

## Closure Checklist

Exact diff; canonical evaluator reuse; no self-issued grant; denial before
environment/secret/ledger/fetch; correct consumption ordinals; focused tests;
TypeScript; exact build; gates; public clone clean; zero live call.

## Return-To-Orchestrator Conditions

Return only after all criteria pass, or immediately with the first concrete
forbidden-scope/source contradiction. HEAD and staging must remain unchanged.

## Operator Checkpoint

No checkpoint is required inside the exact private fake-only manifest. Any
provider call, secret use, public sync, push, deploy or scope expansion returns
to the reviewer/operator and is not implied by this dispatch.

## Worker Autonomy / No-Question Rule

Within scope, repair source and fake-only tests directly. Stop only for an
actual fail condition; do not widen into another roadmap or optional cleanup.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_R2_EXECUTION_PLANE_LIVE_PROOF_GRANT_CONTEXT_CALLER_REPAIR_COMPLETION_2026-08-26.md` (optional if the accepted worker return carries sufficient closure evidence) |
| reviewerOwnedClosurePaths | worker return, roadmap, required registry closure packaging and continuity |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_R2_EXECUTION_PLANE_LIVE_PROOF_GRANT_CONTEXT_CALLER_REPAIR_WORKER_RETURN_2026-08-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python -X utf8 governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Source Verification Block

Use the paired baseline rows and refresh every changed symbol. Explicitly show
the call-consumption sequence and prove denial occurs before side effects.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch envelope, artifact manifest, trace, no-commit, Delta and public-export fields |
| gateRunPurpose | confirm packet/return shape after source verification |
| claimBoundary | gate shape is not authority/runtime/build proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Code implementation`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Code implementation" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary private no-commit repair controls apply |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact artifact names | absent before authoring | CREATE_NEW |
| live-lane callers | source, test and runner exact search | BOUNDED_CLUSTER |
| canonical evaluator | Control Plane owner and Model Gateway runner pattern found | REUSE_EXISTING_OWNER |
| successor proliferation | R1 identifies exactly one P1 build blocker | R2_ONLY |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker then independent reviewer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`6ebf7b4d1`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact Write Ownership subset |
| traceScope(phase, actor) | source, fake tests, checks, build and cleanup |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | clean worktree and empty staging at execution start; no R1 rewrite, public-sync, live or unrelated roadmap work |
| Before status evidence | private worktree clean, public-sync worktree clean and private staging empty at dispatch start |
| nextMoveSurfaces | named worker return then independent review |

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
  "claims": ["canonical grant context is enforced by the MAO caller and exact non-live Web build exits zero"],
  "requiredProof": ["fake-only authority tests", "TypeScript", "exact production build", "worker-return gate", "independent review"],
  "operatorCheckpoints": ["scope expansion", "any external or public effect"],
  "forbiddenEffects": ["provider call", "secret read", "public-sync mutation", "push", "deploy", "worker commit"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Value disposition: `CONTINUE_HIGH_VALUE`; this is the one P1 successor required
to make the selected hosted build plane shippable, not an optional tranche.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | LPCI1 Web R2 dispatcher |
| Provider or surface | private repository source and fake-only test surfaces |
| Session or invocation | R1 independent review and R2 dispatch, 2026-08-26 |
| Working directory | private provenance repository root |
| Command or tool surface | source reads, Git, npm non-live checks, ADIF and scaffold |
| Target paths | paired R2 baseline/work order and current LPCI roadmap |
| Allowed scope source | operator serious-repair authority plus R1 source-backed blocked disposition |
| Before status evidence | private HEAD `6ebf7b4d1`; private worktree clean; public-sync worktree clean; staging empty |
| After status evidence | dispatcher records final exact set before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | no implementation, live call, secret, push or deploy |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `lpci1-web-r2-dispatch-2026-08-26` |
| Expected manifest | paired R2 baseline, work order and roadmap status |
| Actual changed set | reviewer records before dispatch commit |
| Manifest delta | NONE expected |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R2 dispatch plus later private fake-only caller repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: R1 blocked build and reviewer TypeScript reproduction |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch docs only in this phase |
| invocationBoundary | later local source/test/build commands only |
| interceptionBoundary | no live/provider interception claim from dispatch |
| claimLanguage | repair authority and proof contract, not hosted readiness |
| forbiddenExpansion | provider/live/secret/public/push/deploy or unrelated owner change |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current CVF source and build evidence only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Control Plane grant evaluator, Model Gateway harness and Execution Plane caller |
| Disposition | BLOCKED_UNTIL_CVF_PROOF for hosted readiness |
| Claim boundary | no external source or runtime claim is promoted |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: bounded named source/test cluster, not a corpus rescan.

## Foundation Storage Layout Block

N/A with reason: R2 reuses existing Control Plane, Model Gateway and Execution
Plane owners; it creates no durable foundation file, storage layout or index.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no complete-corpus claim.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| EAFR-R12 changed a required live-harness authority shape without compiling the tracked Execution Plane caller | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | require affected-caller TypeScript/build proof when a public harness interface gains required authority fields |

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: R2 is private repair only; export requires accepted material, a clean
public-sync projection, push gates and Netlify observation.

## Claim Boundary

This work order authorizes only a private no-commit, fake-only authority-context
caller repair. No provider grant issuance, secret access, live run, public
mutation, push, deploy or production claim is authorized.
