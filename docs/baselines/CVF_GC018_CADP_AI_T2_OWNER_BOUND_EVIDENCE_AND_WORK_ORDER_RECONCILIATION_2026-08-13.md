# CVF GC-018 Baseline - CADP-AI-T2 Owner-Bound Evidence And Work-Order Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-13

Batch ID: CADP-AI-T2

Risk ceiling: R2

dispatchBaseHead: `1dd6ed07eb517e140acfe2e2ec0c41ea196ab2b4`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `DISPATCH_READY`, `WORKER_MUST_NOT_COMMIT`, Source Verification Block, Dependency Release Evidence, Expected manifest, Actual changed set, Manifest delta, Public Export Disposition |
| gateRunPurpose | confirmation evidence after source and owner inspection, not first discovery |
| claimBoundary | structural dispatch conformance does not prove implementation correctness, owner authenticity or runtime safety |

## Purpose

Authorize one hermetic T2 implementation that removes the caller-self-attested
evidence trust path and reconciles a governed work-order grant with an explicit
execution observation. The result must fail closed when a source-verified owner
cannot be established.

## Authorization

The operator explicitly instructed the reviewer to commit accepted T1 and open
T2 on 2026-08-13. T1 material is committed at
`a17051bcd810e6cc80a069712ce670365c2e7790`; this packet authorizes T2 only.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| CADP-AI-T1 bounded acceptance | `docs/reviews/CVF_CADP_R1_CVF_13_08_CAPABILITY_ADMISSION_DISTRIBUTION_PROFILE_ABSORPTION_COMPLETION_2026-08-13.md`; commit `a17051bcd810e6cc80a069712ce670365c2e7790` | independent acceptance plus material commit | SATISFIED |
| F11 residual is preserved | `docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`; `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION` | T2 must not start from a false fixed claim | SATISFIED |
| operator release | explicit commit-and-open-T2 instruction dated 2026-08-13 | explicit release after accepted T1 | SATISFIED |
| fresh owner verification | current Guard Contract sources named below | implementation may proceed only through verified owners or fail closed | SATISFIED_FOR_DISPATCH |

## Scope / Applies To

T2 applies only to the Guard Contract's hermetic contract layer, focused tests,
barrel/package-boundary checks and its no-commit worker return. It may replace
the unsafe public `CompatibilityEvidenceIndex` trust path and add one separate
owner-binding/reconciliation module beside the existing CADP contract.

## Evidence / Verification

Dispatch evidence consists of source rows, dependency release anchors, exact
scope, negative collision checks and pre-dispatch governance gates. Worker
evidence must add compiler, focused/full tests, public-boundary checks, exact
diff and no-commit state; reviewer evidence must add independently authored
adversarial probes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| current caller-supplied trust input exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | lines 125 and 551-583 | `CompatibilityEvidenceIndex`; `readTrustedArtifact`; `validateCompatibilityEvidence` | CADP contract | ACCEPT |
| workflow binding owns step grant and trace vocabulary | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts` | lines 25-74 and 105-187 | `WorkflowBinding`; `WorkflowStepExecutionTrace`; `validateWorkflowBinding` | Guard Contract workflow binding | ACCEPT |
| receipt binding owns selected-flow obligation/emission correlation | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | lines 23-118 | `StepReceiptObligation`; `StepReceiptEmission`; `bindStepReceipts` | Guard Contract receipt binding | ACCEPT |
| receipt envelope owns deterministic record envelope types | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts` | lines 32-83 | `Receipt`; `ReceiptEnvelopeReceiptRecord` | Guard Contract receipt envelope | ACCEPT |
| public CADP barrel currently exports the unsafe index type and validator | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` | CADP export block | `CompatibilityEvidenceIndex`; `validateCompatibilityEvidence` | contracts barrel | ACCEPT |
| package root is the only public contract subpath | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | `exports` map | `.` -> `./src/index.ts` | package export map | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| baseline, work order and worker-return paths | `Test-Path` returned `False` for all three paths before authoring | CLEAR |
| owner-binding module name | verified contracts directory had no `capability-owner-binding.contract.ts` | CLEAR_FOR_NEW_MODULE |
| unsafe trust path | source contains the public caller-supplied index and validator named above | REPLACEMENT_REQUIRED |
| exact search roots and coverage | `EXTENSIONS/CVF_GUARD_CONTRACT/src` plus `docs`, with source, tests, docs, JSON and retained external evidence considered | COVERED |
| exact search command or structured query | `rg -n "CompatibilityEvidenceIndex|capability-owner-binding" EXTENSIONS/CVF_GUARD_CONTRACT/src docs` plus the three `Test-Path` checks recorded above | EXECUTED |
| same-token collision/occurrence result | `CompatibilityEvidenceIndex` has authoritative current source/test/barrel occurrences; those collisions are the defect target, not evidence of an absent symbol | RECORDED_NON_ABSENT_COLLISION |
| absent-versus-collision disposition | only the new owner-binding module and three packet paths were absent; existing index occurrences are binding inputs to replacement | ACCEPT |
| collision decision | create a new T2 packet/module and replace the unsafe existing occurrence through review; do not overwrite another tranche | ACCEPT |

## Baseline Decision

Authorize a no-commit worker to implement a module-private, runtime-verifiable
owner capability and exact grant-versus-observation reconciliation. A generic
factory, caller-supplied resolver, arbitrary map, boolean authority assertion,
or structurally valid plain object must never mint trusted evidence.

If no real owner adapter exists for a requested evidence class, the correct
result is rejection or `BLOCKED_SOURCE_NOT_FOUND`; high evidence ranks may
remain unreachable rather than being self-certified.

## Required Behavior

1. Remove or deprecate the public arbitrary `CompatibilityEvidenceIndex` trust
   path so the exact T1 F11 probe cannot certify itself.
2. Add a separate owner-binding contract using module-private runtime identity;
   copied, spread, serialized, cast or plain-object projections must fail.
3. Expose only named, source-verified owner adapters; do not expose a generic
   mint/factory/resolver that accepts arbitrary caller records.
4. Reconcile capability, assignment, work-order, action, transport, resource,
   credential reference, time window, invocation count and retry limit exactly.
5. Require explicit observation plus trace/receipt linkage where the grant says
   execution occurred; observation records may prove use but never mint power.
6. Accept explicit `evaluatedAt`; do not read ambient time, filesystem, network,
   process, environment, provider, database or credential material.
7. Return deterministic, secret-safe validation output for identical supported
   inputs on the tested runtime; do not claim cross-runtime determinism.

## Exact Worker Scope

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.test.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`
4. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts`
5. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts`
6. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-workflow-binding.test.ts`
7. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts`
8. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-receipt-binding.test.ts`
9. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`
10. `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts`
11. `docs/reviews/CVF_CADP_AI_T2_OWNER_BOUND_EVIDENCE_AND_WORK_ORDER_RECONCILIATION_WORKER_RETURN_2026-08-13.md`

Any twelfth worker path is forbidden. The worker may use fewer paths and must
record every unused optional path.

## Forbidden Scope

No runtime folder, provider/live call, raw credential or private key, filesystem,
network, process, environment lookup, persistence, execution-plane or model-
gateway consumer wiring, checker/hook change, CLI/MCP adapter, source-folder
mutation, public/session-state mutation, package installation, commit, push,
deployment or production claim.

## Acceptance Criteria

- the original caller-created trusted-index attack is rejected or impossible;
- forged, cast, copied, spread and serialized projections fail at runtime;
- wrong owner, artifact, capability, work order or assignment fails;
- action, transport, resource, credential reference, expiry, invocation and
  retry mismatches fail;
- missing required observation, trace or receipt linkage fails;
- accessors, proxies and exotic inputs fail closed without invoking caller hooks;
- success exists only through a named verified owner adapter;
- outputs contain no secret value and no new authority;
- TypeScript, focused tests, package-boundary tests and full hermetic package pass;
- independent reviewer reruns an adversarial probe before any acceptance.

## Stop Conditions

Return `BLOCKED` if exact scope is insufficient, source owners contradict, a
trusted path requires invented authority, safe compatibility requires a
twelfth path, or any forbidden side effect is necessary.

## Dual Agent Surface Matrix

| Consumer class | Owner surface | Boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Guard Contract public barrel | hermetic owner binding and reconciliation only | TypeScript tests and independent probe | no runtime execution | AUTHORIZED_FOR_IMPLEMENTATION |
| EXTERNAL_AGENT_CLI_MCP | none | no ingress, auth, mutation or export | forbidden scope | separate T5 packet | DEFERRED_WITH_REASON |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T2 dispatch for hermetic owner-binding and grant-observation reconciliation |
| claimDisposition | CLAIM_REJECTED until worker evidence and independent review exist |
| receiptEvidence | N/A with reason: contract fixtures only; no runtime receipt claim |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch authorization and source verification only |
| invocationBoundary | repository-local build and tests |
| interceptionBoundary | no runtime interception, proxy, wrapper or provider enforcement |
| claimLanguage | dispatch-ready, not implemented or accepted |
| forbiddenExpansion | runtime/provider/live/public/deploy/production and T3+ |

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: T2 consumes accepted CVF-owned T1 artifacts and
makes no new external corpus enumeration or completeness claim.

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: no new repository or copied-folder intake occurs;
the accepted CADP-R1 evidence remains immutable provenance.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - T2 consumes accepted CVF-owned
  T1 artifacts and makes no new corpus completeness claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Chain map route | accepted CADP-R1 -> accepted bounded T1 -> T2 owner binding |
| Input type | External repo or copied folder |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Guard Contract contracts directory |
| Disposition | implement deferred T2 candidate without reopening intake |
| Claim boundary | no new external scan, runtime, live or adapter claim |

## Foundation Storage Layout Block

N/A with reason: T2 adds at most one bounded contract module beside existing
owners and does not create or relocate a durable governance foundation.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current Guard Contract contract, barrel, package export and focused-test surfaces named in source verification |
| Runtime behavior claimed | N/A_WITH_REASON: T2 packet authorizes hermetic contract work only |
| Helper/checker implementation claimed | N/A_WITH_REASON: no checker or runtime helper change is authorized |
| Provider/live proof claimed | N/A_WITH_REASON: no provider or live call is authorized |
| Provider registry surfaces | out of scope and untouched; no absence or hardcoding claim is made |
| Public-sync claimed | N/A_WITH_REASON: private dispatch only |
| Freshness disposition | PASS - current owner paths were inspected for dispatch; implementation and review remain pending |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defectIds: NONE_RETURNED

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --max-results 100 --json`

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T2 --title "Owner-Bound Evidence and Work-Order Reconciliation" --date 2026-08-13 --base a17051bcd810e6cc80a069712ce670365c2e7790 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | owner verification, exact-11 scope, F11 attack boundary, reconciliation fields and fail-closed rules |
| checkerReadAheadConfirmation | dispatch, read-ahead, return, size, authority/encoding, public and intake checkers read |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2 is a private hermetic implementation dispatch with no public-sync
artifact or authorization.

## Claim Boundary

This baseline authorizes T2 implementation only. F11 remains open and still
blocks `CERTIFIED_BOUNDED`, trusted-evidence, deployment-readiness and
production-readiness claims until T2 is independently accepted. It does not
prove owner authenticity, cross-runtime determinism or runtime enforcement.
