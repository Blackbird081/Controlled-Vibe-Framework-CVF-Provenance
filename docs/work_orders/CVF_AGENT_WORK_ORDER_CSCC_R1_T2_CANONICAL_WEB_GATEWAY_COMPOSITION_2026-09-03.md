# CVF Agent Work Order - CSCC-R1-T2 Canonical Web Gateway Composition

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: CSCC-R1-T2

Dispatch base head: 066a07911

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker: delegated implementation worker

Reviewer/closer: orchestrator/reviewer

Worker return path: `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_WORKER_RETURN_2026-09-03.md`

## Dispatch Prompt Envelope

Role: worker/implementer for bounded CSCC-R1-T2; orchestrator/reviewer remains independent reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_2026-09-03.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture `git rev-parse --short HEAD` at worker start; expected dispatch anchor is `066a07911` plus the dispatch/continuity commits.

Current-time notes: P4-C1 automatic evidence collection is independent; all external/provider invocation counts and ceilings are zero.

Do-not-misread notes: implement only the frozen T1 port/identity contract and exact manifest. Do not run live tests, touch vision, delete the direct rollback path, activate both paths, open T3, or touch GC-010/P2/P4/canary/MAO/public/downstream surfaces.

Required first actions: read `AGENTS.md`, active bootstrap/front door/handoff, guard orientation, literal gotchas, `DESIGN.md`, paired baseline, T1 completion and both frozen T1 contracts, this packet, all named source owners and applicable checker sources; capture HEAD/status; run pre-implementation before writing.

Return contract: implement, test, create the exact worker return, run its full gate, leave HEAD unchanged and staged diff empty, then return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with exact evidence and terminal token.

## Purpose

Realize one canonical non-vision Web text path through the Gateway-owned port
without duplicate admission or provider calls, while preserving legacy Gateway
callers, current output safety/retry behavior, and a source-explicit direct
rollback implementation until independent acceptance.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CSCC-R1-T2 --title "Canonical Web Gateway Composition" --date 2026-09-03 --base 066a07911 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker plus no-commit and Web trigger stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with accepted T1 authority, exact source/test manifest and deterministic proof contract |
| checkerReadAheadConfirmation | all checker paths in the Checker Source Read-Ahead Block |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; no runtime proof |

## Authority Chain

1. frozen doctrine and operating model;
2. `AGENTS.md` and governed work-order standards;
3. CSCC-R1 roadmap;
4. accepted T1 completion and its two exact contracts;
5. paired GC-018 baseline and this work order;
6. current source and deterministic executable evidence.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| operator | authorizes bounded T2 and retains parked checkpoints |
| worker | implements exact manifest, tests, returns evidence, does not commit |
| reviewer/closer | independently reviews and owns accepted commits and continuity |

## Required First Reads

- `docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md`
- `docs/reference/CVF_CANONICAL_EXECUTION_IDENTITY_AND_RECEIPT_JOIN_CONTRACT_2026-09-03.md`
- `docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md`
- every source/test path in Allowed And Forbidden Paths
- worker-return, structural, trace, delta, SCEC and public-disposition checker sources

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CSCC-R1-T2
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "cscc-r1-t0-canonical-composition-owner",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 3,
  "predecessor": {
    "path": "docs/work_orders/CVF_AGENT_WORK_ORDER_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_2026-09-03.md",
    "sha256": "ffda2f622ad34e81111c82d509ae187c5e302fe9cafa3fd3ac61704658ed674b"
  },
  "blockerDelta": {"prior": ["exact_contract_names", "receipt_join_schema", "future_test_manifest"], "resolved": ["exact_contract_names", "receipt_join_schema", "future_test_manifest"], "retained": [], "new": ["executable_composition", "deterministic_parity", "rollback_evidence"], "reopened": [], "current": ["executable_composition", "deterministic_parity", "rollback_evidence"]},
  "resolutionEvidence": {
    "exact_contract_names": {"evidenceClass": "ACCEPTED_REVIEW", "evidencePath": "docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md", "sha256": "09c0abdecc848b461a9759ea3253e49c7f13164e7edae9466bd03647d9153980", "locator": "## Findings / Position"},
    "receipt_join_schema": {"evidenceClass": "ACCEPTED_REVIEW", "evidencePath": "docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md", "sha256": "09c0abdecc848b461a9759ea3253e49c7f13164e7edae9466bd03647d9153980", "locator": "## Findings / Position"},
    "future_test_manifest": {"evidenceClass": "ACCEPTED_REVIEW", "evidencePath": "docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md", "sha256": "09c0abdecc848b461a9759ea3253e49c7f13164e7edae9466bd03647d9153980", "locator": "## Verification"}
  },
  "counters": {"partialReadyClosures": 1, "reviewerScopeExpansions": 1, "sameClaimCorrections": 2, "nonDecreasingBlockerTransitions": 1},
  "claims": [{"claimId": "CSCC-R1-T2-DISPATCH", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md"}],
  "requiredDisposition": "ROOT_CONTRACT_REQUIRED",
  "successorScope": "INTEGRATED_ROOT_CONTRACT"
}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CSCC-R1-T2","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"RUNTIME_INTEGRATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","EXTENSIONS/CVF_MODEL_GATEWAY/","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/","docs/reviews/"],"claims":["frozen canonical composition can be realized deterministically"],"requiredProof":["typechecks","ten risk-class tests","legacy parity","single active path","zero live calls","independent review"],"operatorCheckpoints":["T3","provider/live","public sync","deployment"],"forbiddenEffects":["live call","worker commit","direct path deletion","automatic successor","canary mutation"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T1 root contract | accepted completion at material commit `f93b00e42` and continuity commit `066a07911` | exact accepted terminal releases bounded T2 implementation dispatch | ACCEPT |

## Worker Autonomy / No-Question Rule

Repair allowed-manifest source/test/checker defects directly. Return only for
a frozen-contract contradiction, required forbidden path, dirty overlap, live
credential need, or architecture expansion that prevents bounded completion.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | current private CVF source and accepted T1 contracts |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | bounded cross-package runtime integration with deterministic local proof |
| risk sensitivity | R3; exactly-once accounting and schema compatibility, with external effects forbidden |
| selected role route | dispatcher authors; no-commit worker implements; independent reviewer/closer accepts |
| Intake role | worker performs bounded source verification; no external corpus intake |
| Authority promotion | forbidden; worker output remains pending evidence |
| External agent disposition | internal agent surface only; external CLI/MCP invocation count remains zero |
| escalation condition | source contradiction, additional-path need, live credential need, dirty overlap, or third repair round |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: current-source runtime composition is not an
external corpus intake, legacy absorption refresh, or coverage-index update.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | bounded manifest, exact authority, provider prohibition, durable receipt symmetry and no-commit evidence |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch fields; source headers; full worker-return profile; SCEC schema; trace and delta labels; public disposition |
| gateRunPurpose | confirm dispatch shape after source and frozen-contract reconciliation |
| claimBoundary | machine conformance only; executable behavior requires worker evidence and independent review |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| implementation contract | accepted reference | `docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md` | stable types, callback ordering, compatibility and ten tests | `CanonicalExecutionPort` | Model Gateway | ACCEPT |
| identity contract | accepted reference | `docs/reference/CVF_CANONICAL_EXECUTION_IDENTITY_AND_RECEIPT_JOIN_CONTRACT_2026-09-03.md` | four-owner matrix and transition window | `canonicalExecutionId` | evidence owners | ACCEPT |
| direct Web provider path | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | initial and retry branches | `executeAI`; `admitAndInvokeProvider` | Web | ACCEPT |
| atomic ledger operations | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` | admission and call-start functions | `admitProviderAttempt`; `recordProviderCallStart` | Web | ACCEPT |
| bridge hook location | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | execute options and one adapter call | `ProviderExecutionBridgeExecuteOptions`; `ProviderExecutionBridge.execute` | Model Gateway | ACCEPT |
| identity schemas | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | current interfaces/builders | `GatewayReceipt`; `MaterialContextManifest`; `Sot3ActivationEvidenceRecord`; `GovernanceEvidenceReceipt` | respective packages | ACCEPT |
| package import direction | package source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | dependency and exports | `cvf-model-gateway` | Web consumes Gateway | ACCEPT |

## Current Runtime Freshness Verification

Rerun before edits:

```powershell
rg -n "executeAI|admitAndInvokeProvider|recordProviderCallStart" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts
rg -n "ProviderExecutionBridgeExecuteOptions|adapter.execute|GatewayExecuteRequest" EXTENSIONS/CVF_MODEL_GATEWAY/src
rg -n "CanonicalExecutionPort|canonicalExecutionId|beforeProviderInvoke" EXTENSIONS --glob '!**/node_modules/**'
```

Stop on a competing implementation or changed ordering that contradicts T1.

## Implementation Contract

The worker must implement T1 verbatim:

- Gateway owns `CanonicalExecutionPort` and `CanonicalExecutionAdapter`;
- `GatewayExecuteRequest.canonicalExecutionId` and `beforeProviderInvoke` are
  additive/optional for legacy callers;
- Gateway completes every pre-adapter stop before the callback;
- Web callback awaits only `admitProviderAttempt`, then synchronously records
  call start and returns its fresh index with no fallible gap;
- retries reuse identity but allocate a fresh attempt index;
- envelope identity fans out to SOT3 before the port and to all receipt owners;
- non-vision text chooses exactly one direct or port-backed path per route
  build; direct code remains an explicit rollback implementation but is not
  simultaneously invoked;
- no raw prompts, payloads or credential values are copied into join schemas.

## Ten Deterministic Risk Classes

Implement exact assertions for: all eight pre-adapter stops; callback denial;
callback allow and immediate single invocation; callback rejection; retry
fresh index; legacy bridge omission; mandatory Web callback; mutually
exclusive direct/port wiring; zero MAO-to-Web imports; and equal secret-safe
identity across Gateway receipt, manifest and SOT3 evidence.

## Work-Order Fulfillment Manifest

| Requirement | Artifact class | Proof | Forbidden substitution |
| --- | --- | --- | --- |
| Gateway-owned port | Gateway source/tests | exported interface, adapter and sequence assertions | Web-owned duplicate port |
| atomic attempt boundary | bridge plus Web adapter/tests | denial/allow/throw/retry counters and call order | prose-only claim |
| exclusive Web cutover | route and route tests | one active path per build; direct code retained | dual invocation or deletion |
| identity propagation | four schema owners and tests | equal ID, legacy shapes, hash coverage, no payload copying | aggregate payload receipt |
| pending handoff | worker return | full gate, exact diff, zero calls and no commit | self-closure |

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/canonical-execution-port.ts` | CREATE port types and concrete adapter |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | EDIT additive request identity |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | EDIT optional atomic callback and all terminal receipt propagation |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | EDIT additive identity input/schema/builder |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts` | EDIT additive identity and digest/validation propagation |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | EDIT public package exports |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/canonical-execution-port.test.ts` | CREATE frozen risk-class tests 1-7 and Gateway identity coverage |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts` | EDIT legacy parity and callback terminal behavior |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/gateway-receipt.test.ts` | EDIT additive/legacy receipt coverage |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts` | EDIT digest and legacy-shape coverage |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.ts` | CREATE Web composition factory/adapter and attempt boundary |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.test.ts` | CREATE wiring, retry and secret-safe lineage tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | EDIT non-vision text initial/retry selection; preserve vision and direct rollback code |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.provider-attempt-admission.test.ts` | EDIT route-level exactly-once and exclusivity assertions |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | EDIT pass existing envelope identity into SOT3 lane |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.test.ts` | EDIT SOT3 identity propagation coverage |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | EDIT optional canonical identity input/record propagation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.test.ts` | EDIT canonical and legacy coverage |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | EDIT optional field, exact dual-shape validation and hash behavior |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.test.ts` | EDIT dual-shape, stable ID and integrity tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | EDIT additive Web receipt field |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | EDIT receipt builder equality propagation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts` | EDIT identity equality and legacy-reader coverage |
| `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_WORKER_RETURN_2026-09-03.md` | CREATE full pending worker return |

No substitution or additional path is allowed. If a compile error proves one
additional existing test is inseparable, return blocked with the exact path
and reason; do not widen the manifest silently.

## Allowed And Forbidden Paths

Writes are exactly the 24 manifest paths above. All other paths are read-only.
No live-test file may run or change. No governance, session, roadmap, baseline,
work-order, lockfile, generated aggregate, MAO, GC-010, public or canary path
may change.

## Write Ownership

| Path class | Worker permission | Owner |
| --- | --- | --- |
| exact Gateway source/tests | CREATE_OR_EDIT | Model Gateway pending review |
| exact Web source/tests | CREATE_OR_EDIT | Web pending review |
| exact worker return | CREATE | worker pending review |
| all other paths | READ_ONLY | current canonical owner |

## Execution Plan

1. Capture base/status, verify no overlap, run pre-implementation.
2. Implement additive Gateway schemas, bridge hook, port and exports; typecheck
   and pass focused Gateway tests.
3. Implement the Web composition factory and atomic callback, then route
   non-vision initial/retry calls through exactly one selected port path.
4. Propagate canonical identity through pre-port SOT3 and Web receipts; retain
   legacy optional shapes and direct rollback code.
5. Run focused deterministic tests, both typechecks and bounded non-live route
   regressions; never run a live-pattern test.
6. Complete the worker return, full gate and exact manifest/status checks;
   return without staging, committing or opening T3.

## Pre-Flight Checks

- Confirm execution base descends from dispatch base and there are no overlapping changes.
- Confirm new target files are absent and staged diff is empty.
- Rerun current-symbol searches and the pre-implementation gate.
- Stop if adapter or credential coverage needs a new provider, secret path, lockfile, or forbidden owner.

## Dual Agent Surface Matrix

| Surface | Dispatch disposition | Evidence boundary |
| --- | --- | --- |
| INTERNAL_AGENT | AUTHORIZED | one delegated no-commit implementation worker |
| EXTERNAL_AGENT_CLI_MCP | NOT_USED | cumulative invocation count and ceiling zero |
| Adapter boundary | LOCAL_DETERMINISTIC_ONLY | Gateway/Web adapters may be tested with doubles; no provider invocation |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | delegated implementation worker; independent orchestrator/reviewer closure |
| phase | T2 canonical Web-Gateway composition |
| baseHeadFor(phase) | dispatchBaseHead=066a07911; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact 24-path worker manifest |
| traceScope(phase, actor) | reads, edits, commands, tests, counts, status and diff |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | preserve unrelated work and stop on overlap |
| nextMoveSurfaces | worker return only; reviewer owns acceptance, commits and T3 decision |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_COMPLETION_2026-09-03.md` |
| reviewerOwnedClosurePaths | work order, baseline, roadmap and completion only when acceptance requires them |
| closureOwner | orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_WORKER_RETURN_2026-09-03.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Source Inventory;
Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Public Export Disposition; Epistemic Process
Block; Machine Closure Package; Claim Boundary; Changed Files; Command
Evidence; No-Commit Statement.

Required scalars: `rootCauseClusterId: INITIAL_SCOPE_CSCC_R1_T2`;
`reworkGeneration: 0`; `consolidatedDefectClassSweep:
COMPLETE_ALL_KNOWN_DEPENDENCIES`; `productionBindingEvidence:
LOCAL_DETERMINISTIC_IMPLEMENTATION_ONLY`; `adversarialRegressionDisposition:
PASS_TARGETED_DEFECT_CLASS`; `successorTrancheOpened: NO`;
`internalAgentInvocationCount: 1`; `externalAgentInvocationCount: 0`;
`providerCallCount: 0`; `terminalReadinessVerdict: READY_FOR_REVIEW`.

Terminal token: `READY_FOR_T2_INDEPENDENT_REVIEW`,
`PARTIAL_IMPLEMENTATION_CONTRACT_OR_MANIFEST_CONFLICT`, or
`BLOCKED_SOURCE_CONTRADICTION`. No token opens T3.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_AND_RECOMPUTE

priorVerificationArtifact: `docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md`

priorVerificationAnchor: material commit `f93b00e42`; SHA-256 `09c0abdecc848b461a9759ea3253e49c7f13164e7edae9466bd03647d9153980`

freshRecomputeRequired: current symbols, typechecks, focused tests, import graph, diff and status

unicodePathHandling: use literal paths and UTF-8-safe readers from repository root

extractedTextAuthority: current CVF-governed source and command output only

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | one Gateway source beside its bridge and one Web composition source beside current execution helpers |
| Storage decision | extend existing package owners; create no new foundation root or evidence store |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | existing Gateway, SOT3 and Web owners remain authoritative; T3 remains separate |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | current private source verification and independent CVF review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired baseline, this work order, frozen T1 contracts and current source owners |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for any readiness assertion |
| Claim boundary | delegated worker output is pending evidence and cannot replace governed source authority |

## Evidence Requirements

| Claim | Evidence | Required result |
| --- | --- | --- |
| compile compatibility | both package typechecks | PASS |
| frozen risk coverage | focused non-live tests | all ten classes PASS |
| no duplicate path | static search and route spies | exactly one adapter invocation per admitted attempt |
| exact containment | diff and full status | exact 24 paths |
| no external effect | trace and invocation counters | external/provider counts zero |
| no worker commit | HEAD and staged diff | unchanged execution base and empty staged diff |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
npm test -- --run tests/canonical-execution-port.test.ts tests/provider-execution-bridge.test.ts tests/gateway-receipt.test.ts tests/material-context-manifest.test.ts
npm run check
npm run test:run -- src/lib/canonical-web-gateway-execution.test.ts src/lib/sot3-knowledge-adapter.test.ts src/lib/sot3-activation-evidence-store.test.ts src/lib/web-governance-envelope.test.ts src/app/api/execute/route-knowledge-context.test.ts src/app/api/execute/route.provider-attempt-admission.test.ts
npm run check
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

Run the first Gateway commands from `EXTENSIONS/CVF_MODEL_GATEWAY`; run the
second command group from the Web package. Do not run any filename containing
`.live.test.` or the release-gate bundle.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher authoring governed T2 packet |
| Provider or surface | local private provenance workspace |
| Session or invocation | CSCC-R1-T2 dispatch authoring, 2026-09-03 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, scaffold preview, resolver, `apply_patch`, dispatch gates |
| Target paths | paired T2 baseline and work order |
| Allowed scope source | operator continuation plus accepted T1 completion |
| Before status evidence | clean worktree at `066a07911`; three dispatch/return targets absent |
| After status evidence | paired dispatch artifacts only before commit |
| Diff evidence | `git diff --name-status` and full status |
| Approval boundary | dispatch authoring and bounded worker handoff only |
| Claim boundary | no worker execution or runtime proof yet |
| Agent type | dispatcher |
| Invocation ID | `cscc-r1-t2-dispatch-author-2026-09-03` |
| Expected manifest | exact baseline and work-order paths |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | bounded deterministic T2 implementation dispatch |
| claimDisposition | CLAIM_REJECTED: packet authoring itself implements no runtime control |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must produce test evidence; no live receipt authorized |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch authoring performs no runtime action |
| invocationBoundary | future worker may invoke local typechecks and deterministic test doubles only |
| interceptionBoundary | no IDE, shell, filesystem, provider or external interception claim |
| claimLanguage | pending local implementation subject to independent review |
| forbiddenExpansion | no live/public/production/T3/MAO/GC-010/P2/P4/canary/downstream effect |

## Acceptance Criteria

- Exact 24-path worker manifest and no other change.
- All ten T1 risk classes have deterministic executable assertions.
- Legacy Gateway calls omit the optional fields and retain prior behavior.
- Every pre-adapter stop and callback denial/rejection invokes no adapter.
- Allowed admission and call-start occur exactly once immediately before one
  adapter call; retry has a fresh index and shared identity.
- Non-vision Web text uses one selected port path; vision is unchanged; direct
  implementation remains rollback code and is never dual-invoked.
- Four identity owners preserve legacy readers and reject payload copying.
- Both package typechecks, focused suites, full worker-return gate, zero calls,
  unchanged HEAD and empty staged diff pass.

## Closure Checklist

- Worker return carries commands/results, first/final status and manifest reconciliation.
- Reviewer reproduces focused tests and inspects every terminal branch.
- Material and continuity commits remain separate and reviewer-owned.
- Direct rollback code is retained through independent T2 acceptance.
- Successor, live, public and parked lanes remain unopened.

## Review Gate

Reviewer must independently inspect the full changed source, reproduce focused
tests, audit all terminal branches and verify the exact manifest before any
commit. Worker completion is not acceptance.

## Operator Checkpoint

No new checkpoint is needed for deterministic local T2 execution. T3, live
provider proof, public/deploy, MAO, GC-010, P2/P4/canary/P5/P6 remain parked.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance criterion and the
full worker-return gate pass. Otherwise return `BLOCKED_WITH_REASON` with the
exact contradiction, additional-path need, failed command and current status;
do not commit or widen scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private bounded implementation dispatch; public sync is forbidden.

## Claim Boundary

This order authorizes exact-manifest deterministic T2 implementation and a
pending no-commit return. It does not prove acceptance, authorize provider/live
execution, delete rollback code, open T3, or change any parked lane.
