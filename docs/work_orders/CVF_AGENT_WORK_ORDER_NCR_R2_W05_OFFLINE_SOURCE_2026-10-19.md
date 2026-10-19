# NCR R2/W05 Integrated Offline Source

Memory class: governed-work-order
docType: work_order
Status: DISPATCH_READY
Date: 2026-10-19
Batch ID: CVF-NCR-R2-W05-OFFLINE-SOURCE-20261019
Inspection base: de63f6707a913af902b21b4958ff5ea31736bfe3
Commit mode: WORKER_MUST_NOT_COMMIT
rawMemoryReleased=false
providerExecutionAuthority: FORBIDDEN
Decision owner: LOCAL
Intended governed path: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT implementation worker; LOCAL owns review/commit.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; baseline `docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`.
Commit mode: WORKER_MUST_NOT_COMMIT; capture actual clean executionBaseHead.
Current-time notes: integrated offline source11+return2; one180min assignment; focused verification proposal included.
Do-not-misread notes: injected synthetic sends only; no real-network/provider/browser/app runtime.
Required first actions: mapped reads, sourcepins, explicit packet execution instruction, bound pre-implementation; then implement and verify.
Return contract: connected chain, source/test evidence, exact13, Local independent probe pending; no stage/commit.

## Purpose And Authority

Implement the accepted Local HQ1-HQ7 design as one integrated offline artifacts receipt-operation source package. Authority is standing roadmap continuation plus Local locked decisions; operator manually assigns the complete source/verification packet. No real effect granted. AuditS1/current0/counters0,0,0,1/documentary/NO_SUCCESSOR remains closed, not reset. GoalLocalS3/current0/counters0,0,0,0/originalworkerS2fork and ClarityS1/current3/counters0,0,0,1 retained. Parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 unchanged. FullR1 prelive/R2partial; R3R4open; R5R6deferred.

## Agent Roles

MULTI_AGENT_MULTI_ROLE: Local dispatcher/reviewer/closer and one operator-transferred INTERNAL_AGENT implementation worker. No worker/subagent invocation by Root; no detached research, CLI/MCP or provider task. Normative role is provider neutral.

## Locked Implementation Contract

Finite deliverable: implement one connected artifacts-domain OFFLINE fixture chain under HQ1-HQ7 in the accepted Local audit review. This packet proposes the source and focused verification assignment for operator manual transfer. Root packet preparation adds/runs no product test. Operator instruction to execute this complete packet must include its focused offline verification scope; structural release alone is not an effect grant. No standalone helper-only completion.

C01. Logical key is SHA256 of fixed-order [schema,userId,orgId,teamId,sourceRecordId,recomputedRequestSha256,effectKind]. Exclude jobId/versionId/config/endpoint/htmlSha from the key, bind them in the immutable envelope. Bind all schema/config/policy/transform revisions, actor/source/job/input/payload/output identities available at preparation, declared endpoint/store IDs/config digest, auth reference/scope without values, R1/REVIEW, call limit1, synthetic disclosure, no-expiry retention and disable/revoke posture. Exact key and envelope serialization must be explicit, strict and tested. Input is copied/validated, never a mutable caller alias.
C02. At most256 logical operations per owner, max16384 UTF-8 bytes per record, at most3 immutable lifecycle records (intent/start/outcome) per operation. Do not reuse readSidecar's absent/corrupt/expired->null behavior for operation admission: distinguish missing, corrupt, unconfirmed and unsupported state. No operation TTL, eviction, retry, cleanup or key reuse; draft24h TTL remains separate. Tombstone/redaction protocol is deferred, not implemented now.
C03. Select a one-shot, monotonic exclusive-create protocol, using an operations-only child directory within the existing artifacts owner namespace. Validate root/owner/operation-directory realpaths and deny symlinks; only the operations child directory has the bounded recognized-name scan, leaving existing draft/job files outside that scan. Do not acquire a mutex or releaseable cross-process lock, append/rollback mutable data, or mutate ownership/DACL. Reserve one of256 fixed numbered capacity markers with wx, sync and exact byte readback BEFORE an intent can be created. Reservation bytes bind owner/key/config identity; an empty, torn, unreadable or abandoned slot consumes capacity and cannot be recycled. Then exclusively create the key-index/intent, then STARTED, then outcome. Racing duplicate reservations may conservatively waste slots; never exceed256 or release a consumed slot. Existing-record lookup precedes reservation and consumes no new slot. Other shapes are allowed only if they preserve these exact monotonic bounds without introducing a new risk family. All created metadata records, including reservation/index markers, are <=16384bytes. Use bounded scan256; unknown files/state deny, not silently ignore. No process crash recovery deletes claims.
C04. One caller's verified exclusive STARTED record can mint an opaque in-memory single-use grant bound to owner/key/envelope/attempt and one injected invoker. Consume it before invoke, reject fabricated/copied/spent grants. Durable start existence alone never mints a replacement grant. A write/readback/error at any boundary denies before invoke or yields OUTCOME_UNKNOWN after invoke. PREPARED/STARTED/unknown/corrupt/expired evidence gives no retry. Store outcomes include RECEIPT_VERIFIED, DENIED, FAILED_BEFORE_SEND, OUTCOME_UNKNOWN; all terminal records remain consumed. Copy/read back serialized exact evidence and enforce namespace/symlink checks; file sync does not establish directory/power-loss/distributed durability. Assume cooperative processes on trusted fixture root; malicious same-user filesystem races are not proven.
C05. RECEIPT_VERIFIED exact same target/config returns existing operation outcome with zero sends. Never combine a prior receipt with freshly generated HTML. Persist immutable output identity (generatedAt/sourceHash/htmlSha/artifactId) in the envelope, not full HTML above the metadata cap. A repeated HTTP Build that renders a different target/digest gets reference-only ALREADY_PROCESSED (409, no success.data HTML/receipt), including newly minted jobId/versionId/config. Exact-target cache reuse can be exercised directly through the branch with the original immutable target; do not weaken equality for a more convenient UI result.
C06. New server selector is CVF_NCR_RECEIPT_OPERATION_PROFILE, recognized before legacy resolution. UNDECLARED and no job selectors may retain legacy outside controlled proof. Explicit DISABLED/invalid/unsupported/production-denied, or malformed/partial/duplicate/comma-conflicting selectors => deny with zero sends, no legacy fallback. Valid LOCAL_SYNTHETIC remains the existing controlled LOCAL_ONLY/no-receipt branch, not permission for injected receipt effect. Job selectors under that branch may bind local job identity without granting receipt. With selectors but no valid local/receipt-controlled profile, deny. Persistent server disable/revoke posture cannot be cleared by missing marker/config. Do not create a runtime enable path from environment alone.
C07. Active controlled receipt profile exists ONLY as an explicitly constructed injected fixture composition, not a remotely supplied field or environment activation. identityTrust=DECLARED_UNATTESTED, synthetic source prefix, production=false, fixed declared endpoint/backend-store IDs/config digest and a separate permitted effect INJECTED_SYNTHETIC_RECEIPT (not JOB_EFFECTS). The runtime resolver denies held/unsupported activation and never supplies global fetch. Tests may inject a synthetic invoker through the typed profile factory and mock this resolver for actual POST composition. Fixture invoker must be explicit; no default fetch/credential reads/engine import. Do not inspect active env/secrets; use a complete synthetic env argument in tests. Real endpoint attestation/auth/per-hop/store proof remain held.
C08. Headers X-CVF-Job-Id and X-CVF-Source-Record-Id are bounded untrusted selectors. Keep seven-field JSON body unchanged, no permit field. Hook sends both only when prepareJob returns a valid job reference; retain Stop/stale/owner-change fences and no-header legacy behavior. Controlled route authenticates same-origin normal signed session with user/org/team, no break-glass/service-token substitution; source prefix validation, owner-scoped getJob plus recomputed requestIdentity/requestSha256 BEFORE preparation/admission/Build invoke. Existing local-only selected profile remains no-receipt. Do not getVersion before first Build: version is absent until Save; immutable absent version is not a placeholder to mutate later. Any later version-bound request requires owner-scoped getVersion after Save and mismatch rejection; no new Save/version endpoint in this packet.
C09. Operation branch integrates into actual export POST after bounded body/schema/secret-like validation and before any receipt request. Share render/response seams inside allowed files; no Next-disallowed auxiliary exports from route.ts. Controlled proof uses phase REVIEW/riskR1, one supplied attemptId, exact artifact/payload digest and only one injected send. Retain legacy fetchGovernanceReceipt behavior separately (R0 and existing response parsing); controlled code never falls through to it. Abort/timeout mark local unknown; they do not prove remote cancellation or cost. Bound pending invocation and outcome read/write; delayed late responses cannot publish an outcome inconsistent with a consumed/unknown state. Preserve DRAFT_UNACCEPTED/human review boundaries even for fixture ALLOW.
C10. Reconcile B is optional pure diagnostic presence lookup only, injected fixture response, no ledger endpoint call. Present=>REMOTE_PRESENCE_OBSERVED; absent/wrong actor/config/store/attempt=>unknown; neither releases UNKNOWN nor grants replay. Local exact immutable readback is separate. No new HTTP operation reader, engine read-by-id, proxy, engine policy, auth owner, approval record, SDK or provider gateway. No import/transplant of frozen pending-agent admission/SQLite/composition, provider-attempt quota or engine ledger as receipt permission.
C11. Required output is source implementation plus named offline fixtures and truthful final evidence. The focused verification proposal below binds actual code and failures, not AI governance behavior. Synthetic/mock results establish protocol/structure and invocation counters only, never live governance, remote approval, attestation, billing, human acceptance or full R2 readiness. Full release-quality governance proof remains separately held; do not run it here.

## Required Artifact Manifest

Worker return path: `docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md`

| ID | Path | Action | Dependency / purpose | Max lines |
| --- | --- | --- | --- | --- |
| M01 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.ts` | CREATE | fixed-order key/envelope/state validators | 400 |
| M02 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts` | MODIFY | existing artifacts namespace; immutable operation reservation/start/outcome | 650 |
| M03 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.test.ts` | CREATE | key/envelope/size/secret-like negative cases | 450 |
| M04 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.operation.test.ts` | CREATE | real files/processes/capacity/restart/fault cases | 650 |
| M05 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | MODIFY | separate injected controlled invoker; preserve legacy helper | 400 |
| M06 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.operation.test.ts` | CREATE | one-invoke/timeout/abort/payload/receipt join | 500 |
| M07 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/receipt-operation-profile.ts` | CREATE | tri-state declared server posture plus fixture-only composition | 350 |
| M08 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation-branch.ts` | CREATE | authenticated selector/job/hash -> operation admission -> injected proof | 500 |
| M09 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | MODIFY | early selection/no fallback and integrated response boundary | 650 |
| M10 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation.test.ts` | CREATE | actual POST composed branch and hook selector transport regression | 650 |
| M13 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/useHtmlBuildAttempts.ts` | MODIFY | two bounded job selectors; unchanged seven-field body/stop fence | 220 |
| W01 | `docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md` | CREATE | worker return | 450 |
| W02 | `docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json` | CREATE | evidence ledger | 900 |

Exact13 writes:11 source/test/hook paths plus return/EP. M11/M12 existing route.test.ts/job-profile.test.ts are READ_ONLY retained oracles; no deletion/rename. Frozen source owners, package/lockfiles, build config and current6 read-only. All new files must be created; modify rows must materially implement their named seam. Return/evidence may state a precise blocked outcome instead of inventing code or proof.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Local locked design | docs/reviews/CVF_NCR_R2_W05_OPERATION_CONTRACT_AUDIT_LOCAL_COMPLETION_REVIEW_2026-10-19.md | HQ1-HQ7 | HQ1 | Local reviewer | ACCEPT |
| existing artifacts namespace | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts | directory/writeSidecar/createJob/getJob | HtmlDraftSnapshotStore | artifacts store | ACCEPT |
| request identity | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-draft-recovery-contract.ts | requestIdentity/sha256 | requestIdentity | artifacts draft contract | ACCEPT |
| local effects only | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-job-contract.ts | JOB_EFFECTS/makeJob | JOB_EFFECTS | HTML job owner | ACCEPT |
| receipt seam | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts | fetchGovernanceReceipt | fetchGovernanceReceipt | export proof | ACCEPT |
| actual producer and export | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/useHtmlBuildAttempts.ts | generate after prepareJob before fetch | useHtmlBuildAttempts | build attempts hook | ACCEPT |
| actual POST integration | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts | POST selectedJobProfile/body/parser/receiptCheck | POST | export route | ACCEPT |
| local server resolver | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-synthetic-profile.ts | resolveHtmlJobSyntheticProfile | resolveHtmlJobSyntheticProfile | job profile | ACCEPT |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap concern | Requirement | Observable proof | Status |
| --- | --- | --- | --- |
| R2/W05 HQ1 key/envelope | REQ-IDENTITY | fixed serialization/replay negative tests | PLANNED |
| R2/W05 HQ6 monotonic capacity | REQ-STORE | files/readback/8OS contenders/near-full | PLANNED |
| R2/W05 HQ2/HQ3/HQ7 helper | REQ-PROOF | injected payload/one-send/unknown/no reconciliation release | PLANNED |
| R2/W05 HQ4/HQ5 actual consumer | REQ-INTEGRATION | POST+hook/body/auth/no-fallback cases | PLANNED |
| finite source-only disposition | REQ-RETURN | exact13/finality/pending distinct Local probe | PLANNED |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-R2-W05-OFFLINE-SOURCE-20261019
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

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"ncr-r2-w05-locked-protocol-offline-implementation","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"LOCKED-OFFLINE-SOURCE-PLAN","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md#Integrated Offline Implementation Contract"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

New implementation claim after completed design audit and committed HQ decisions, not another correction to the audit or an executable-readiness claim. The prior audit and all STOP/runtime chains remain frozen with exact counters. This INITIAL identifies first implementation evidence for the newly locked protocol; it does not erase unresolved remote/effect blockers or permit replay. Return derives SUCCESSOR1 from THIS exact workorder/hash; runtime claims require actual matching proof. No automatic successor. Local independent probe remains pending, so no full runtime READY claim.

## Work-Order Acceptance Evidence Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-IDENTITY","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.test.ts","docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md","docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json"],"requiredProofIds":["PROOF-REQ-IDENTITY"]},{"requirementId":"REQ-STORE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.operation.test.ts","docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md","docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json"],"requiredProofIds":["PROOF-REQ-STORE"]},{"requirementId":"REQ-PROOF","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.operation.test.ts","docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md","docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json"],"requiredProofIds":["PROOF-REQ-PROOF"]},{"requirementId":"REQ-INTEGRATION","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/receipt-operation-profile.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation-branch.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation.test.ts","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/useHtmlBuildAttempts.ts","docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md","docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json"],"requiredProofIds":["PROOF-REQ-INTEGRATION"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md","docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json"],"requiredProofIds":["PROOF-REQ-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-REQ-IDENTITY","kind":"OFFLINE_SOURCE_FIXTURE","locator":"docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json#REQ-IDENTITY"},{"proofId":"PROOF-REQ-STORE","kind":"OFFLINE_SOURCE_FIXTURE","locator":"docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json#REQ-STORE"},{"proofId":"PROOF-REQ-PROOF","kind":"OFFLINE_SOURCE_FIXTURE","locator":"docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json#REQ-PROOF"},{"proofId":"PROOF-REQ-INTEGRATION","kind":"OFFLINE_SOURCE_FIXTURE","locator":"docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json#REQ-INTEGRATION"},{"proofId":"PROOF-REQ-RETURN","kind":"OFFLINE_SOURCE_FIXTURE","locator":"docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json#REQ-RETURN"}]}
```

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
returnTimeRecheck: REQUIRED_BEFORE_REPAIR
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | integrated source pair and exact dependency/authority admission | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet and exact current6 | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker and exact current6 | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | exact13 worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | IMPLEMENTATION | worker | IMPLEMENTATION | named offline fixture suite, tsc and targeted ESLint within exact13 | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity, pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | exact return/evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact13 final evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| independent_probe | PRE_MATERIAL_COMMIT | reviewer | REVIEW | owned ignored independent oracle and exact13 read-only | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact13 plus Local review and independent probe | EXACT_PATHS | closer | MATERIAL_COMMIT | independent_probe |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | bounded material exact15 | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | actual source/fixture evidence and distinct Local probe | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | current6 after Local offline source disposition | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | committed material and continuity ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: OFFLINE_OPERATION_ADMISSION_AND_CONCURRENCY
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: Local authors a separate ignored Node oracle after consuming worker evidence; no rerun/relabel of the worker suite. Actual production store/branch invoked with fresh fixture root and independent assertions.
positiveControl: one admitted operation invokes injected callback once and writes exact joined outcome.
negativeMutationClasses: forged grant; partial capacity/start record; competing process; changed target/config; disabled profile; ledger presence attempting to release unknown.
expectedInformationGain: independently challenge the one-send boundary and immutable target joining not established by worker self-report.
rerunCostReason: mandatory bounded independent probe, maximum one8min process; no broad duplicate suite.
reviewerDecisionOwner: LOCAL

## Budget / Tools / Temporary Resources

Proposed execution envelope for operator transfer: one INTERNAL_AGENT180min; exact13 writes, no stage/commit/subagents. Read/search/hash/Git status/diff/show, existing local Node/Python/TypeScript/Vitest/ESLint tools only. No install/package/config change. Complete mandatory mapped reads before first edit. Record actual preparation, coding and verification time; token/paid cost unknown.

Focused verification proposal: <=4 focused Vitest invocations, <=2 tsc, <=2 targeted ESLint, <=3 full requiredGate. These counts include failed/timeout starts once target tool executes. Source/test fixes are allowed between runs, preserve every failed log. Final source revision must have passing required focused checks; a fix after last run invalidates its evidence. No arbitrary post-browser freeze: browser/app/provider/network/live runs are0. Per suite300s, tsc180s, ESLint180s, fullgate180s safety limits, not success evidence. Stop dependent proof when envelope exhausted; no budget refill.

Ignored worker scratch `.cvf/runtime/ncr-r2-w05-offline-source-20261019/worker`: <=256files/64MiB excluding gate-owned caches; <=8 bounded child processes simultaneously, <=32 total process starts for production-store contention/restart proof; hard join/timeout and PID-owned cleanup. Every child runs actual store source via existing TypeScript transpiler and source hash pin; no handwritten duplicate store or added dependency. Generated child harness can be authored only in owned ignored scratch, hash and preserve it. Test roots are newly created inside this scratch, sourceRecordId ncr-synthetic-*; no active store/env/secret read. Monotonic record fixtures retained, no recursive deletion/move, global kill/reset/stash. gate-owned caches/receipts are trusted separate resources and permitted.

## Forbidden Scope

All paths outside exact13 are read-only, including frozen pair, roadmap/session/checkers/hooks/catalog/registry/package/lockfiles, existing test oracles, pending-agent/provider/gateway/Python engine/auth/core job contracts. No network/socket/listener/HTTP client/provider/browser/Next server/start/build/live proof/public/push/deploy/active-data/store/env/secret access. No mutable append/rollback, DACL/ownership change, held/releaseable lock, retry/GC/key recycling or tombstone implementation. No fake approval record or new engine authority. No worker commits/subagents.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python -B governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md --max-return-lines 450 --max-return-bytes 64000`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Canonical scaffold before return prose, source inventory bare tokens and actual ranges/order separate. Return <=450lines/64000bytes, EP <=900lines/96000bytes. Include actual executionBaseHead, exact13 diff, all tool attempts, acceptance-evidence-json with unique locators, SCEC SUCCESSOR1 against actual WO and Local independent probe pending. Honest late/partial reads remain violations. COMPLETE_PENDING_REVIEW requires finished implementation/required focused checks/final fullgate; worker cannot self-certify the independent Local probe. BLOCKED_WITH_REASON names one consolidated digest and completed useful evidence.

Finish source/test/EP/return before final requiredGate. Hash exact return and EP bytes immediately before and after that gate; equality required, NO_POST_GATE_MUTATION. Receipt outside frozen return at owned ignored worker/final-gate-receipt.json with command/exit/raw log/pins/both hashes. Any material edit renews focused evidence as applicable, final fullgate and detached receipt within envelope. No self-embedded file hash or invented green result.

## Reviewer Closure Conversion

Local consumes returned evidence, uses EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION, performs named bounded independent probe and semantic review. M5/M10/safety/M20 measurement posture retained. Worker exact13 + Local completion/roadmap => material exact15, then dedicated current6 and actual nonempty split closure. Root repairs only admitted paths; new source/risk family requires consolidated amendment, not technical micro-question. Preserve worker failures and procedure history.

| Field | Value |
|---|---|
| completionReviewPath | docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-19.md |
| reviewerOwnedClosurePaths | docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-19.md; docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md; separate current6 |
| closureOwner | LOCAL Root |
| workerCommitPermission | FORBIDDEN |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | NOT_APPLICABLE_WITH_REASON: current private source composition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | this source admission pair |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Local verifies private CVF; no external source promotion |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source/dependency reads only, no all-files claim.

## Knowledge System Reconciliation

- Knowledge task class: NON_KNOWLEDGE_SOURCE_IMPLEMENTATION
- Source manifest: exact13 implementation/evidence manifest and named read-only owners; no corpus enumeration
- Source manifest hash: NOT_APPLICABLE; no corpus manifest or map produced
- Enumeration safety: filesystem-backed explicit named-file reads
- Intake registry or ledger: no knowledge intake selected
- Authority assets: immutable accepted source, Local review, design and current continuity
- Derived views: no knowledge view produced
- Semantic region ledger: no mapping regions
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: NONE within zero-asset scope
- Cross-region links: NONE
- Drift check: read-only oracle pins and final changed source identities
- Rebuildability check: Git/source manifest and named commands
- Retrieval boundary: no retrieval-readiness assertion
- Adversarial verification: no map verification selected
- Knowledge-map verdict: PARTIAL

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: bounded implementation dependencies, not a corpus scan; existing path-scope registry coverage verified without an inventory assertion.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | integrated offline source implementation plan |
| claimDisposition | CLAIM_REJECTED: proposed interfaces and source facts provide no runtime readiness |
| receiptEvidence | N/A with reason: no product receipt or provider proof produced |
| actionEvidence | N/A with reason: dispatch preparation only; worker not invoked |
| invocationBoundary | one manually transferred INTERNAL_AGENT owns exact13; focused offline verification proposed |
| interceptionBoundary | no runtime/browser/host interception claimed |
| claimLanguage | source-backed audit with exact limits; no implementation/enforcement claim |
| forbiddenExpansion | out-of-manifest/policy/remote/provider/active-data/production/public/deploy effects |

## Learning Application Plan

```learning-application-plan-json
{
  "schemaVersion": "cvf.learningApplicationPlan@1.0.0",
  "bindings": [
    {
      "findingId": "NCR-LEARNING-APPLICATION-OBSERVABILITY",
      "control": {
        "path": "governance/compat/learning_application_binding.py",
        "sha256": "84068b6f197c19404a23daa643266d7f9ed334f313cd2d8bbe2f2e6d37d7b7b8"
      },
      "action": "Before writes complete proportional mapped reads, then implement the connected C01-C11 source chain inside exact13. Preserve chronology/counters and all failed runs; no real effects.",
      "verificationPlan": "Return actual first-read depth/order,5requirement evidence joins, final source identities, focused checks and final fullgate receipt; no plan-only APPLIED/effectiveness claim."
    }
  ]
}
```

Plan only; no effectiveness or APPLIED claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source packet; public catalog/export remains deferred until separately admitted.

## Foundation Storage Layout Block

Exact13 tracked worker paths declared above. Operation data exists only in newly owned ignored synthetic fixtures, not active stores. No generated aggregate/config/package/public catalog mutation.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_finding_to_governance_learning.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_delta_execution_claim_boundary.py |
| literalTokensReviewed | exact13; full-gate contract; source columns;5requirements; INITIAL0/documentationproof/INTEGRATED_ROOT_CONTRACT; workerS1actualpredecessor; manifest/topology/atomic proof locators; independent probe; confirmation purpose |
| gateRunPurpose | confirmation/evidence of source/authority/scope and bounded packet shape; no product proof |
| claimBoundary | file identity and declared shape only; future design validation/runtime behavior unevaluated |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`.
Returned27; IDs: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006. Raw `.cvf/runtime/ncr-r2-w05-offline-source-20261019/adif.json` SHA256 `669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687`. Apply actual predecessor binding, complete contract dependency review, mapped preparation chronology, source-evidence qualification and bounded review cost.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| generatorScript | governance/compat/build_dispatch_packet_scaffold.py |
| scaffoldHelperCommand | python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R2-W05-OFFLINE-SOURCE-20261019 --title NCR R2 W05 integrated offline source --date 2026-10-19 --base de63f6707a913af902b21b4958ff5ea31736bfe3 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id NOT_APPLICABLE_INITIAL_DISPATCH --scec-problem-key ncr-r2-w05-locked-protocol-offline-implementation --no-evidence-readiness-applicable |
| generatedProfile | generic-worker-dispatch; INITIAL INTERNAL_AGENT |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | integrated exact13 HQ contract, monotonic reservation/no rollback, dependency/size/registry/verification scope and manual transfer |
| checkerReadAheadConfirmation | source/closeability/ledger/SCEC/ReviewCost/high-risk/probe/output checker sources inspected |
| docOnlyNewFields | packet proposal fields; no implementation created by Root |
| claimBoundary | scaffold PASS is not implementation/effect authority |

## Negative Search And Collision Discipline

Negative Search And Collision Discipline: initial HEAD clean/empty stage. Exact future packet/output names checked before creation; no pre-existing matching artifact. Accepted audit already compared pending-agent/quota/gateway/engine owners; this packet resolves artifacts integration, no repository-wide absence claim or duplicate generic engine.

## Current Runtime Freshness Verification

No active runtime inspected or claimed. Source freshness at de63f6707a913af902b21b4958ff5ea31736bfe3; exact pins `.cvf/runtime/ncr-r2-w05-offline-source-20261019/source-freshness.json` SHA256 9d22386f92fd67773fd56b7cf31b52ad99e07e8fca2414d532f2f11e52fa5e67. Read-only dependencies remain pinned; modified source identities renewed by worker proof. Pair/current6 are committed before bound release. No secret/env/active-ledger inspection.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT Local dispatcher; decision owner=LOCAL |
| Provider or surface | private shared checkout |
| Session or invocation | ncr-r2-w05-offline-source-dispatch-20261019 |
| Working directory | repository root |
| Command or tool surface | source/dependency read, integrated source packet/scaffold/governance gates |
| Target paths | `docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Allowed scope source | standing roadmap source-packet planning under locked HQ decisions/manual transfer |
| Before status evidence | de63f6707a913af902b21b4958ff5ea31736bfe3; clean worktree; empty stage |
| After status evidence | Root material3 pair/roadmap then current6; workerexact13 later |
| Diff evidence | git diff --name-status; git diff --check; no source changes |
| Approval boundary | manualworker transfer; Root product changes0; worker proposed offline scope |
| Claim boundary | integrated source/verification proposal only |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-r2-w05-offline-source-dispatch-20261019 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH Rootmaterial3; workerexact13 distinct |
| Deletion or rename disposition | none |

## Epistemic Process Block

Expected Result / Prediction: integrated offline implementation can bind one-start/one-injected-invoke to an immutable logical operation. Evidence Comparison: accepted audit and actual seams support this source plan; execution remains unobserved. Contradiction Or Gap Disposition: real identity/auth/engine policy/retention/remote reconcile held, no live promotion. Claim Update: concrete source/verification proposal only; worker implementation and Local independent acceptance remain pending.

## Claim Boundary

Root only authors/releases a source workorder; no product source/test created/run, no worker invoked. Worker scope after operator assignment is offline protocol fixture proof, not live governance/readiness. AuditS1/current0/counters0,0,0,1/documentary/NO_SUCCESSOR remains closed, not reset. GoalLocalS3/current0/counters0,0,0,0/originalworkerS2fork and ClarityS1/current3/counters0,0,0,1 retained. Parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 unchanged. FullR1 prelive/R2partial; R3R4open; R5R6deferred.

## Authority Chain

| Authority | Binding | Disposition |
| --- | --- | --- |
| Operator continuation | roadmap continuation, Local technical decisions and operator manual source/verification assignment | ACCEPT |
| Local design | docs/reviews/CVF_NCR_R2_W05_OPERATION_CONTRACT_AUDIT_LOCAL_COMPLETION_REVIEW_2026-10-19.md HQ1-HQ7; material4f9cfa355ba4179b78073e42178ed0fe90d6801b/currentde63f6707 | ACCEPT |
| Current roadmap | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md; integrated offline source packet only, dependent effects parked | ACCEPT |
| GC-018 | docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md; exact13 and fixture-only boundary | ACCEPT |

## Intake Role Routing Decision

Intake Role Routing Decision: MULTI_AGENT_MULTI_ROLE
Scope classification: INTERNAL_OFFLINE_SOURCE_AND_FIXTURE
Intake summary: accepted audit design/HQ decisions become first implementation evidence; no same-claim audit correction.
Risk sensitivity: synthetic operation deduplication and before-invoke boundary; no remote/governance authority.
Selected role route: one INTERNAL_AGENT implementation worker, Local independent reviewer/closer; operator manual transfer.
Escalation condition: exact scope/risk/authority contradiction, consolidated Local amendment; no automatic source/live successor.

## Required First Reads And Source-to-Requirement Mapping

| Mandatory source / scope | Derived condition / acceptance | Timing |
| --- | --- | --- |
| bootstrap, compact frontdoor and active handoff current authority/next move | current manual-transfer envelope; no parent effect/counter replay | before edit |
| guard_orientation README action quick read and worker row; gotchas checklist; SOP Worker Preparation/temporary resources; lifecycle continuation/outcome sections | required preparation/resource boundaries, truthful first-read sequence | before edit |
| workorder template Worker Return/Source Verification/No-Question; this FULL packet and baseline; docs/reviews/CVF_NCR_R2_W05_OPERATION_CONTRACT_AUDIT_LOCAL_COMPLETION_REVIEW_2026-10-19.md HQ1-HQ7 and Findings/Decision | locked scope and ordinary technical choices settled; exact13/C01-C11 | before edit |
| relay method Relay Termination; funnel Two-Step Operating Agreement | INTERNAL_AGENT implementation, Local decision owner; no external role promotion | before edit |
| M02/M05/M09/M13 FULL_READ; html-job-contract and html-draft-recovery-contract FULL_READ | immutable namespace/request hash/current response/stop fences => REQ-IDENTITY/STORE/PROOF/INTEGRATION | before edit |
| server html-job-synthetic-profile/html-draft-synthetic-profile FULL_READ; html-job-api auth GET/POST and normalPrincipal/requireAdminApiSession selected functions | exact session/owner/profile and first-Build timing; no receipt permission from JOB_EFFECTS | before edit |
| M11/M12 existing route and job-profile tests FULL_READ; existing store tests selected constructor/job cases; ArtifactExportPanel.test.tsx attempt/Stop cases; setup.ts FULL_READ | retained branch/oracle compatibility, avoid storage/prototype pollution | before edit |
| package.json/vitest.config.ts/tsconfig.json/eslint.config.mjs FULL_READ; DESIGN.md claim/workflow sections | tool availability, alias/transpiler and hook UI boundaries; no UI redesign | before edit |
| applicable output checker constants/regex for return quality, acceptance ledger, source symbols, SCEC, closeability, independent probe, trace/learning/retro/encoding | canonical literal shape and exact finality evidence, no gate-discovery loop | before return prose |

Exact source paths are pinned in source-freshness.json; relative paths above are resolved under EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web. Optional context: frozen pending-agent/SQLite/composition, quota/gateway and engine ledger owners already compared in audit; do not reread whole files or modify them absent a decision-changing contradiction. No all-files-read claim. Source facts come from named code, design choices from HQ and C01-C11, unknown endpoint/auth/cost remain held.

## Write Ownership

Only exact13 in Required Artifact Manifest. New source/test paths are ordinary implementation, not protected governance. Local completion/roadmap/current6 are reviewer/closer-only. Gate-owned caches/receipts and admitted ignored scratch permitted. Immutable READ_ONLY oracle hashes must match start/end; all changed source/test hashes named in final EP. Abort dependent writes if another actor changes tracked paths.

## Pre-Flight Checks

Capture clock/HEAD/status/empty stage; verify committed released packet and expected source pins. Operator manual transfer includes source plus proposed offline verification scope; no Root worker start. Mapped reads before edit. Bound pre-implementation full autorun once. Check local dependencies exist without installation or network. No source/env/config effect during Root packet preparation.

## Execution Plan

Read/pin -> contract and monotonic store -> injected helper -> tri-state fixture profile and branch -> actual POST/hook integration -> consolidated focused suite/type/lint feedback and owned fixes -> final source/evidence reconciliation -> canonical return scaffold/fullgate/hash receipt -> stop for Local independent review. All phases belong to one assignment, no intermediate human approval for ordinary in-scope fixes.

## Evidence Requirements

EP schema cvf.ncrReceiptOperationOfflineSource.v1: actual base/pair identities, source13 exact hashes/actions/read depths, requirement/proof rows, named fixture case precondition/action/expected/observed/sendcount/readback identity, tool attempts command/time/exit/raw log/source revision, peer PIDs/events/256slot cap proof, unknown/replay dispositions, size/import/dependency/registry evidence, finality receipt and PENDING_REVIEWER_EXECUTION. No claim that planned cases ran. Reconcile all cases with PASS/FAIL/NOT_EXECUTED and actual evidence.

## Acceptance Criteria

REQ-IDENTITY: C01 strict fixed-order key excludesjobId and envelope binds all target/config identities. REQ-STORE: C02-C05 real file and OS-process evidence, max256 monotonic slots, one start/invoke winner, unknown cannot replay, no stale receipt mixed with new HTML. REQ-PROOF: C07/C09-C10 injected-only callback/R1/REVIEW/exact joined receipt, failures retain unknown, presence cannot release. REQ-INTEGRATION: C06/C08-C09 actual POST and hook, body/auth/selector boundaries, first Build without version, local/no-selector legacy retained. REQ-RETURN: exact13 final pins/read history/checks, <=limits and final detached fullgate receipt; distinct reviewer probe pending. Full R2/live readiness remains outside acceptance.

## Review Gate

Worker required final fullgate and named offline checks; no product rerun during dispatch planning. Local reviews evidence plus separate bounded oracle; no broad/per-row replay. Normal91 hooks at material/continuity commits; final bound pre-dispatch before manual transfer; later actual nonempty split closure after Local acceptance.

## Closure Checklist

Worker exact13/empty stage/connected integration/all named cases honestly reconciled/current tsc+targeted lint/final focused suite/fullgate/unchanged returnEP aftergate; Local independent probe+review exact15/current6/actual split closure. No automatic source-to-live promotion or invocation refill.

## Return-To-Orchestrator Conditions

Return once finite exact13 and proposed admitted checks complete; otherwise BLOCKED_WITH_REASON with one consolidated defect/authority digest and useful completed evidence. Independent probe pending is normal reviewer ownership, not worker self-approval. No automatic follow-up dispatch or extra local effect.

## Worker Autonomy / No-Question Rule

Resolve ordinary implementation and test defects inside exact13 without asking operator each step; preserve failures, fix and rerun inside envelope. Do not weaken assertions to obtain green. Contract contradiction, new dependency/protected path/risk family or real effect is routed to Local in one return, dependent action held. Do not ask noncoder to select storage/auth mechanisms already fixed.

## Work-Order Fulfillment Manifest

| Requirement | Expected artifacts | Proof IDs |
| --- | --- | --- |
| REQ-IDENTITY | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.test.ts; docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md; docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json | PROOF-REQ-IDENTITY |
| REQ-STORE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.operation.test.ts; docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md; docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json | PROOF-REQ-STORE |
| REQ-PROOF | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.operation.test.ts; docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md; docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json | PROOF-REQ-PROOF |
| REQ-INTEGRATION | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/receipt-operation-profile.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation-branch.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation.test.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/useHtmlBuildAttempts.ts; docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md; docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json | PROOF-REQ-INTEGRATION |
| REQ-RETURN | docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md; docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json | PROOF-REQ-RETURN |

Required Proof Manifest Atomic Literal Discipline: one unique requirement/proof locator per row, full exact paths. Gate ledger controls expected artifact sets.

## Verification Commands

Pre-edit: `python -B governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md`.
Return scaffold: `python -B governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md --title "NCR R2 W05 Offline Source Worker Return"`.

Proposed worker checks, from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`, installed binaries only (no npx download):

`node node_modules/vitest/vitest.mjs run src/lib/artifacts-receipt-operation-contract.test.ts src/lib/server/html-draft-snapshot-store.operation.test.ts src/app/api/artifacts/export/proof.operation.test.ts src/app/api/artifacts/export/operation.test.ts src/app/api/artifacts/export/route.test.ts src/app/api/artifacts/export/job-profile.test.ts src/lib/server/html-draft-snapshot-store.test.ts src/components/ArtifactExportPanel.test.tsx`

`node node_modules/typescript/bin/tsc --noEmit --incremental false`

`node node_modules/eslint/bin/eslint.js src/lib/artifacts-receipt-operation-contract.ts src/lib/server/html-draft-snapshot-store.ts src/lib/artifacts-receipt-operation-contract.test.ts src/lib/server/html-draft-snapshot-store.operation.test.ts src/app/api/artifacts/export/proof.ts src/app/api/artifacts/export/proof.operation.test.ts src/lib/server/receipt-operation-profile.ts src/app/api/artifacts/export/operation-branch.ts src/app/api/artifacts/export/route.ts src/app/api/artifacts/export/operation.test.ts src/components/useHtmlBuildAttempts.ts --max-warnings=0`

Lint targets exact11 rather than unrelated read-only UI files with known warnings. No suppressions, new warnings or waived nonzero exit. A selected baseline failure cannot be silently called green. Final full gate: `python -B governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md --max-return-lines 450 --max-return-bytes 64000`.

Required case groups: PA profile/auth/partial/conflicting selectors/forged permit/production deny=>0; PB intent/reservation/start/write/readback/corrupt/oversize/full=>0, including boundary reservation256/257 with simultaneous processes; PC one success1, denial0, eight real OS contenders<=1, restart/spent/fabricated grant0, outcome-write failure unknown and newjob/config/version reference-only0; PD present/absent/wrong actor/store/config/attempt diagnostic does not release UNKNOWN or invoke; PE >24h no reuse, disable retains facts, source/secret rejection and partial consumed slot; PF old helper+existing route/job/store/panel compatibility; PG import graph permits only Node builtins/current artifacts and explicit injection; PH firstBuild owner getJob/hash with no savedversion, seven-field body/two headers, identical-target reuse0 vs new-render409/noHTML. The audited32case plan is input, not evidence; map all its relevant cases and Local additions to actual tests, disclose not applicable Safe-copy migration (not implemented). No browser, live governance, remote ledger or real invoker proof.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: internal source implementation under accepted Local HQ1-HQ7 and exact chain below; no external architecture admission. Actual architecture/consumer bindings are still mandatory.

## Local Transaction Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - this packet uses one-shot immutable exclusive-create reservations/start records without a held guard, rollback protocol or security change. Losing/partial claims are permanently consumed, not released. Real-process atomic-create contention is verified under REQ-STORE. The authorization excludes all four target risk families in the standard; changing mechanism requires revised applicability/contract before implementation. Read-only token inspection found no restoration privilege; this plan does not depend on it.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Root dispatcher/reviewer/closer; one separate INTERNAL_AGENT offline implementation worker |
| phase | DISPATCH -> IMPLEMENTATION -> WORKER_RETURN -> REVIEW -> FREEZE |
| baseHeadFor(phase) | dispatchBaseHead=de63f6707a913af902b21b4958ff5ea31736bfe3; executionBaseHead=actual clean released HEAD captured at start; closureBaseHead=actual dispatch continuity commit |
| changedSetScope(phase) | Root exact3 dispatch; separate current6; worker exact13; Root exact15 material; separate current6 actual-SHA continuity |
| traceScope(phase, actor) | worker exact13 and owned ignored scratch only; Root pair/review/roadmap/continuity; manual operator handoff |
| commitOwner(phase) | worker WORKER_MUST_NOT_COMMIT; Local Root commits |
| crossBatchIsolation | all prior actors/counters remain spent/frozen; distinct first implementation evidence after accepted design/HQ; all prior counters frozen; no live successor |
| nextMoveSurfaces | bootstrap, compact front door, active handoff; aggregate targeted only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: selected INTERNAL_AGENT only after operator transfer and pre-implementation PASS
laneOwnedPaths: exact2 Required Artifact Manifest plus owned ignored worker root
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return, exact2 reconciliation and stage empty

## Worker Output Checker Read-Ahead Mandate

Worker Output Checker Read-Ahead Mandate: before drafting, inspect applicable checker constants/branches for review/EP outputs, not just this dispatch checklist. Use canonical scaffold. Source Inventory cells bare READ/FULL_READ/PARTIAL_READ/SOURCE_VERIFIED tokens; actual ranges/order/limits outside cells. Gate Run Purpose is confirmation/evidence; no source/hash/comprehension conflation. Preserve any skipped/late mandatory read.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-R2-W05-OFFLINE-SOURCE-20261019","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md","docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md","docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-19.md","docs/reviews/CVF_NCR_R2_W05_OFFLINE_SOURCE_WORKER_RETURN_2026-10-19.md","docs/reviews/evidence/ncr-r2-w05-offline-source-worker-20261019.json","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION_MEMORY.md","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/state/entries/nextAllowedMove.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json"],"claims":["Root packet authoring/release only; worker proposed integrated offline implementation and fixture verification"],"requiredProof":["exact13 dependencies/registry/size/architecture","HQ1-HQ7/C01-C11 source mapping","proposed offline cases/budgets/independent review","clean bound source packet release"],"operatorCheckpoints":["actual destination/data/writer/provider/cost/acceptance effects","production/public/deploy"],"forbiddenEffects":["Root product source/test creation or execution","Root worker invocation","real network/provider/active-data/production/public/deploy","worker paths outside exact13 or commit"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","completenessClaimChanged":false}}
```

## Baseline Binding

Baseline `docs/baselines/CVF_GC018_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md` SHA256 is bound at release after all material edits; worker reads the actual committed pair and hashes, not inspection base as executionBaseHead. Baseline and workorder are immutable for worker.

## Operator Checkpoint

Manual transfer boundary retained: operator assigns this canonical packet including its proposed focused offline verification scope. Root does not start a worker or add/run product tests. No confirmation needed for technical choices already locked; any later real endpoint/provider/data/public/deploy effect needs its own authority.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: internal artifacts source implementation from accepted private design, no external corpus absorption; no legacy index update.

## Architecture And Dependency Disposition

M01 contract -> M02 existing artifacts store -> M05 injected proof -> M07 server fixture composition -> M08 branch -> M09 actual POST -> M13 job-selector hook. Tests M03/M04/M06/M10 bind these same production owners. Normal session helper/normalPrincipal/getJob/requestIdentity are reused read-only; getVersion is conditional post-Save only. TypeScript dev dependency can transpile real store for child fixture, no dependency install. No new package/config/generated build/catalog file needed. Existing package/vitest source pins show tool/include/alias coverage; registry-coverage.json records all seven new source/test paths covered by current GC-051 scopePaths. M17 registry mutation NOT_REQUIRED; M18 public catalog DEFERRED_PRIVATE_ONLY, no accepted as-built claim yet; Local review updates roadmap after acceptance. M14 HTTP reader and M15/M16 remote read-by-id remain deferred. Frozen pending-agent/quota/gateway/engine/auth owners read-only. No foreseeable split with listed maxima<700soft source threshold; any over-budget split needs consolidated Local amendment before new path creation, not hidden helper. No new user-visible control/layout; DESIGN.md applies to existing hook flow.
