# CVF Agent Work Order - NCR Processing Lifecycle

Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Date: 2026-10-12
Batch ID: CVF-NCR-PROCESSING-LIFECYCLE-20261012
Dispatch base head: 07fbf32cf04a6f4fd53697e6d3bb2216911e2afd
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
Worker return path: `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md`
Worker: shared-workspace implementation worker role
Reviewer/closer: Local reviewer/closer role

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT existing ProcessingScreen implementation/test worker.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture actual full HEAD and start clock before reads/edits.
Current-time notes: 2026-10-12 Asia/Saigon; released execution HEAD follows authoring base.
Do-not-misread notes: cancellation here suppresses client work/results, not confirmed backend/provider cancellation; tests use synthetic mocked transport only.
Required first actions: progressive startup, clean/staged-empty, pins/currentAuthority and bound pre-implementation before outputs; declared mandatory source scopes below.
Return contract: exactly four outputs, COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON; no stage/commit/push/subagents. Operator manually starts after committed bound release.

## Purpose

Make the existing task-processing UI safe to leave, cancel and render again: abandoned work must not deliver a result; one unchanged task must not be re-sent due to presentation/callback changes; manual and automatic result delivery must happen at most once. Deliver actual component code and offline regressions, preserving request payload and classified failure/approval behavior.

## Authority Chain

Operator2026-10-12 asks continuation and selects Sonnet 5.5 high for the next manually started worker. Standing audit-and-choose, useful coding outcome and quality/time collection instructions apply. Parent `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` R1 addresses cancel/error/recovery; R4 identifies duplicate/cancel/reconnect coverage. Paired baseline `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md` admits this finite reversible existing-consumer maintenance. Neither full R1/R4 admission nor provider/live/P11 is opened.

## Local Branch Audit And Selection

Selected: existing ProcessingScreen client lifecycle. Actual component probe at `07fbf32cf04a6f4fd53697e6d3bb2216911e2afd` confirms four failures with one passing uncancelled positive control: delayed callback after unmount=1; late response after Cancel=1; callback-only rerender POST count=2; two manual clicks plus auto timer completion count=3. `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` preserves source, config, raw results/digests and Local harness collection failures separately.

This serves Home and the existing wizard consumers without another dashboard or runtime. Dormant unused hook, global pin checker, retrospective model projections and S5 remain deferred; provider/media/real-data/public/deploy effects and full roadmap exits remain parked. No benchmark-only task. Stop after fixed component, meaningful regressions and complete pending return; no automatic successor.

## Agent Roles

Local dispatcher owns source-derived requirements and dispatch/admission. Operator starts the shared-workspace worker manually. INTERNAL_AGENT worker owns four paths. Local reviewer independently decides technical/procedure disposition and later collection admission; steward owns continuity. No worker or nested agent launches during authoring.

## Requested Configuration Metadata

Operator-requested provider label Claude, model Sonnet 5.5, effort high. This is assignment metadata, separate from role requirements and observed runtime identity. Worker records native model/effort/usage as null with reason if not exposed. Operator intends a model switch; the existing16 reviewed tasks are not recounted or relabeled, and no comparative winner is assumed.

## Scope / Target / Owner Boundary

Exactly four worker paths: existing ProcessingScreen.tsx; new sibling ProcessingScreen.lifecycle.test.tsx; new worker proof and return. Existing ProcessingScreen.test.tsx, Home, wizards, API routes, settings, setup/provider guard, dependencies/lockfiles, store/type/approval/receipt owners and all continuity are read-only. No new helper/hook/global gate, new runtime, actual user data or external call. Local alone stages/commits. Ignored diagnostics under .cvf/runtime/ncr-processing-lifecycle-worker-20261012 and existing mandatory helper receipts are admitted; record actual paths.

Budget: one invocation, maximum45 minutes including reads/tests/gates; component <=950 physical lines (current836, hard1000), new lifecycle test <=550, return<=450 lines/64000 bytes, proof<=128000 bytes. If a necessary split/extra path or authority change is discovered, report one consolidated blocker; ordinary implementation choices remain autonomous.

## Design Control Gate

Actual existing consumer contradiction established offline. Locked outcome is task lifetime isolation, request stability and at-most-once completion. Preserve public component props, request/governance envelope fields, classified failure/approval/recovery behavior and mock-only demo route. Client abort is best effort, never confirmed server cancellation. No new state owner or full roadmap release claim.

## Write Ownership

| Owned path | Action |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | edit client lifecycle, cleanup and completion delivery only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx` | create independent actual-component offline lifecycle regressions |
| `docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json` | create actual source/proof/command/failure/clock/unknown evidence |
| `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md` | create complete pending return and fixed acceptance join |

## Implementation Contract

1. Cancel must invalidate pending/scheduled completion and call the supplied onCancel once per attempt; unmount must clear owned timeouts/intervals and invalidate late execute responses. Abort in-flight client fetch when feasible, but correctness must also hold for transport that ignores abort. No later output/receipt/error/progress/log from an abandoned attempt may become the current attempt's UI result.
2. For the same logical task, callback identity or language/presentation rerender must not issue an additional execute POST. Keep current request fields and settings selection. An actual replacement of request inputs/intent/template/overrides within the mounted component invalidates the old attempt; late A cannot overwrite current B. Test fresh equivalent input objects to distinguish request content from React object identity.
3. Unify manual View Results and delayed automatic completion into at-most-once delivery per active attempt, preserving exact output and receipt. Repeated clicks or leftover timers after result delivery cannot deliver again. Cancellation before the timer expires must suppress it, with or without risk badge.
4. Demo/mock interval and completion timer belong to the same attempt lifetime and are cleaned on cancellation/unmount. No real response failure may trigger mock fallback. React StrictMode effect setup/cleanup must not create duplicate execute calls for the same admitted mounted task.
5. Preserve governed overrides, provider/model selection, approval submission and classified BLOCK/CLARIFY/NEEDS_APPROVAL/diagnostic behavior. No durable cancelled status, backend cancellation endpoint, replay/retry feature or synthesized receipt. New fresh mount/request still executes normally; cancellation is local client isolation, not durable effect settlement.

## Acceptance Criteria

| ID | Required result |
|---|---|
| REQ-LIFETIME | cancel/unmount and actual request replacement invalidate old client work; late response/receipt cannot complete or overwrite another attempt; mock timers cleaned |
| REQ-ONCE | same logical request does not re-POST on callback/language/equivalent input rerender; completion manual+timer at most once; StrictMode no duplicate |
| REQ-CONTROLS | uncancelled success with/without badge preserves output/receipt; replacement B wins over late A; existing payload/failure/approval controls remain green |
| REQ-RETURN | exact four owned outputs; declared mandatory semantic reads fulfilled; actual scaffold/clocks/failures/red-green proof; focused/type/lint and final fast gate/ledger PASS; staged empty/no commit |

## Work-Order Fulfillment Manifest

Fixed requirement/proof set in acceptance ledger below. Product requirements bind component/new lifecycle test/proof; return requirement binds proof/return. No worker completion/guide/helper output.

## Required First Reads

The orchestrator supplies these scopes and source-derived conditions before dispatch under `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`, Orchestrator Source And Acceptance Clarification. Worker need not recreate this map or seek pre-edit approval; it executes and reports evidence against the fixed acceptance set. Hash-only verification is not semantic reading. Do not silently downgrade a mandatory scope; unfulfilled mandatory scope means BLOCKED_WITH_REASON. Optional context creates no reading blocker.

Progressive startup plus governing baseline/order are mandatory. Existing applicable output-checker constants remain required before prose; do not replay full continuity history.

| Source and scope | Classification / reason | Derived condition and acceptance evidence |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` complete current component | mandatory: owns all startup, async, timer, cancel, manual result and approval paths; small single consumer | REQ-LIFETIME/ONCE: asynchronous work must belong to its active attempt, completion once; real component with fake timers, deferred transport and actual buttons |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx` mocks/baseProps and named describe groups: forwarding, guided response/failures, risk badge, evidence visibility, NEEDS_APPROVAL, W96 completion | mandatory: preserve established payload/error/approval/completion contracts; no need to reread unrelated copy assertions | REQ-CONTROLS: existing suite green, exact output/receipt and no mock fallback; keep this test file read-only |
| Home source: exact path in Source Pin Contract row3; handleProcessingComplete, handleBack and ProcessingScreen render props | mandatory: actual parent consumes onComplete, removes component on Cancel; closure/callback identity may change | REQ-LIFETIME/ONCE: component must not invoke abandoned callback; same task callback change cannot dispatch; no Home edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` full configuration; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` setup/provider/external-store guard branches | mandatory: select installed offline tests and maintain external-call denial | REQ-RETURN/CONTROLS: mocked fetch only, default non-live mode, no provider/network or setup weakening |
| `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` sourceFinding/reproduction/limits | mandatory: actual Local red fixes expected behavior and distinguishes oracle failures | REQ-LIFETIME/ONCE: four observed failures + passing control are task evidence; independently construct worker tests, do not import Local oracle |
| NCR roadmap R1/R4 | optional context: parent maintenance rationale, no full phase exit needed | packet-derived boundary: cancel/recovery/duplicate coverage is bounded offline; provider/full pilot exits stay parked |
| `docs/reference/CVF_ORACLE_O6_INTEGRITY_DESIGN_2026-10-11.md` Precondition Chain P0-P7 | optional context: existing manual oracle design, operational conditions supplied below | test proof must use valid controls, independent fixtures, declared changes, non-target invariants, actual consumer and attributed first/final results |

Fixture conditions already derived by orchestrator: unmodified uncancelled response completes with exact output/receipt (P0); A/B request/output objects independently constructed (P1); cancellation/unmount/prop replacement/callback change/click+timer explicitly named (P2); prove changed lifecycle event actually happened (P3); other attempt output/receipt/input unchanged (P4); render real ProcessingScreen and act through actual UI/props (P5); expected result follows the contract and source branch, not implementation-private refs (P6); retain first harness/product failures and final results with their real actor (P7). Reviewer checks decision-changing mappings, not a reading quiz.

## Execution Plan

1. Capture start clock/full HEAD before reads; clean/staged-empty; source/authority pins and bound pre-implementation before outputs. No additional read-approval phase.
2. Read declared mandatory scopes. Invoke actual return scaffold before long prose. Use this supplied source/acceptance mapping; retain actual read depth and any omissions truthfully.
3. Independently construct actual-component tests with deferred mocked transport/fake timers/real cancel+result buttons. Preserve at least one meaningful original-source failing lifecycle assertion and a passing positive control before fixing. Worker tests must not import Local harness/source-string oracle.
4. Implement owned compatible lifecycle repair. Cover cancel-before-response, after-response-before-timer, unmount, callback/equivalent props/StrictMode, A->B late A, manual+timer and mock cleanup as one finite outcome. Implementation structure remains autonomous.
5. Run new lifecycle + existing ProcessingScreen + Home tests, TypeScript and owned lint via installed binaries. No install/build/browser/live mode or broad duplicate suite. Stop when required checks establish the fixed result.
6. Return actual proof/first-final failures/clocks/unknown metadata; full fast gate and ledger enforce on final bytes, diff hygiene, staged empty. Save terminal clock/hash receipt after verification without editing final outputs. COMPLETE_PENDING_REVIEW or one consolidated blocker; no stage/commit.

## Pre-Flight Checks

Local commits exact packet/authority material, then six-path actual material-SHA/batch continuity. Bound pre-dispatch and dry pre-implementation must PASS on clean final released HEAD. Worker recaptures full execution HEAD; no stale authoring-base range.

## Evidence Requirements

Actual source/test/final raw hashes; argv/exit/log hashes and claimed proof bytes; declared event preconditions plus expected/observed callback/POST counts and output/receipt identity. Independent A/B fixtures, real consumer, positive control and planned-red vs harness-fail attribution. Actual start before first read, final gate end and terminal end separately; retain unknown intervals. Requested Sonnet5.5/high separate from unexposed native identity/effort/token/bill (null with reason). Count defect groups, severity, self-repairs and review burden; cost evaluation deferred. No preparation quiz or duplicate plan.

## Verification Commands

From repository root:
```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <actual-executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md --check-shape --max-lines 450 --max-bytes 64000
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md --max-return-lines 450 --max-return-bytes 64000
python governance/compat/check_work_order_acceptance_ledger.py --work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md --return docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md --enforce
git diff --check
git status --short
```
From existing Web package, installed binaries only:
```powershell
node node_modules/vitest/vitest.mjs run src/components/ProcessingScreen.lifecycle.test.tsx src/components/ProcessingScreen.test.tsx 'src/app/(dashboard)/home/page.test.tsx'
node node_modules/typescript/bin/tsc --noEmit --incremental false
node node_modules/eslint/bin/eslint.js src/components/ProcessingScreen.tsx src/components/ProcessingScreen.lifecycle.test.tsx
```
Synthetic offline UI/transport only; no live/provider governance proof. Existing test setup/provider denial stays enabled.

## Worker Autonomy / No-Question Rule

Resolve ordinary owned implementation/test/return choices autonomously. Hold source/authority contradiction, missing assigned surface, necessary extra path/split, outside effect or budget exhaustion; return one consolidated BLOCKED_WITH_REASON. No checker weakening, fallback model substitution or automatic redispatch.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED
dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-PROCESSING-LIFECYCLE-20261012
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

One operator-started shared-workspace assignment; zero nested agents, zero external-agent/provider invocations. No automatic redispatch. Routine review remains M5/M10/safety/M20 under active MFRP; consume valid returned evidence, with named contradiction/information gain/cost reason before any rerun. Final release and actual worker result are separate from this initial assignment envelope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order" --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated. This query does not prove absence of all applicable defects; refresh the final task class at release if classification changes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| fetch and no-badge timer lack abandonment guard | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | executeReal response and 300ms completion branches | ProcessingScreen | ProcessingScreenProps | ACCEPT |
| startup reruns on executeReal dependency changes | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | useCallback executeReal dependencies; startup useEffect | ProcessingScreen | existing lifecycle effects | ACCEPT |
| manual and auto completion separate | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | completedOutput effect; view-results-btn onClick | ProcessingScreen | existing result delivery | ACCEPT |
| mock interval cleanup unused; Cancel forwards only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | runMockExecution; startup mock branch; Cancel button | ProcessingScreen | existing demo/cancel consumer | ACCEPT |
| actual failures with valid uncancelled control | `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` | sourceFinding and reproduction | reproduction | Local offline actual-component probe | ACCEPT |
| Home consumes completion and removes processing on back | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | handleProcessingComplete; handleBack; ProcessingScreen render | HomePage | existing parent UI | ACCEPT |
| current behavior contract regression suite | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx` | named describe groups in Required First Reads | ProcessingScreen | current offline component tests | ACCEPT |
| installed offline selection and provider denial | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | default non-live include/exclude/setupFiles | defineConfig | current Vitest configuration | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | CLOSED_PASS_BOUNDED; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | targeted current checker constants/required sections and ready-state predicates read; not an all-lines reading claim |

## Roadmap-to-Work-Order Trace Matrix

| Existing owner | Receiving output | Limit |
|---|---|---|
| NCR R1 cancel/error/recovery consumer contract | processing UI safely abandoned and results delivered once | bounded offline maintenance, no full R1/R3 exit |
| NCR R4 duplicate/cancel fault coverage | deferred transport/rerender/timer/cleanup regressions | no durable effect, two-provider replaceability or R4 pilot closure |
| model-selection manual AGENT_SEAT S3/S4 method | operator switches requested configuration on actual useful task | observation only after Local review, no S5/model ranking |
| O6 manual P0-P7 | supplied fixture preconditions applied to actual lifecycle assertions | no helper/global gate or new worker planning phase |

## Review Gate

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Local conducts one complete source/behavior/authority/test/identity/unknown/preparation matrix before first repair. Consume valid focused evidence; one distinct source-derived abandoned-attempt/duplicate-delivery challenge verifies semantics without importing worker tests. Routine MFRP remains M5/M10/safety/M20; reruns require named contradiction/information gain/cost reason, no broad repetition.

## Closure Checklist

Local reconciles exact four submitted paths and fixed requirements, actual test/proof/result identity, final bytes and mandatory read/clock disclosures before first repair. Consume valid worker evidence; only a distinct bounded lifecycle challenge with named information gain. Technical acceptance and procedure disposition separate. Add a reviewed observation only after Local decision, preserving all16 historical rows including four Luna configurations; Opus same-session advisory excluded. Preserve raw worker bytes/first failures and actual time. Local owns completion/collection, material then dedicated continuity; no push.

## Return-To-Orchestrator Conditions

COMPLETE_PENDING_REVIEW only when all fixed criteria/final gates PASS, acceptance ledger COMPLIANT, closeabilityDisposition CLOSEABLE, outsideAuthorityBlockers NONE and staged empty. Otherwise BLOCKED_WITH_REASON with exact requirement/source/owner/next action. Planned red is evidence; unexplained required final FAIL is blocking.

## Operator Checkpoint

Operator delegated selection and manual worker preference; no repeat branch/model question needed. Changed effect/risk/scope or unavailable necessary surface is the checkpoint. Native execution remains operator-started after Local release; public/provider/deploy effects remain parked.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named contracts/source/case only; no repository/corpus scan.

## Epistemic Process Block

Expected Result / Prediction: abandoned attempts never deliver; one same-task POST and one active completion.
Evidence Comparison: actual source component at07fbf32cf04a6f4fd53697e6d3bb2216911e2afd has four failed lifecycle assertions and one uncancelled control PASS in `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`.
Contradiction Or Gap Disposition: zero-test Local harness collection failures retained separately. Client-side lifecycle failures established; backend cancellation/real effect settlement unknown and outside this scope.
Claim Update: finite implementation task selected; no worker outcome, independent acceptance or model comparison yet.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-PROCESSING-LIFECYCLE-20261012 --title "NCR Processing Lifecycle" --date 2026-10-12 --base 07fbf32cf04a6f4fd53697e6d3bb2216911e2afd --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_HOME_HISTORY_BINDING_COMPLETION_2026-10-11.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-processing-lifecycle --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: bounded ProcessingScreen consumer, exact four outputs, orchestrator-derived scopes/assertions and honest read/clock proof |
| checkerReadAheadConfirmation | applicable constants, section/trace tokens and role predicates read before declarations |
| docOnlyNewFields | dispatch evidence only; no new runtime schema/store |
| claimBoundary | packet preparation, no implementation or worker outcome |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/selector and collection steward |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-processing-lifecycle-dispatch-20261012 |
| Working directory | repository root |
| Command or tool surface | progressive startup; scoped code/roadmap/owner reads; actual component five-case red; resolver/scaffold; exact packet and pending owner/collection integration |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`; `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` |
| Allowed scope source | operator continuation, explicit Sonnet5.5 high switch, standing audit/select and proportional quality/time tracking |
| Before status evidence | 07fbf32cf04a6f4fd53697e6d3bb2216911e2afd; exact four previously pending documentation files; staged empty;16 reviewed rows |
| After status evidence | exact seven material documentation paths pending; no product edit; dedicated six-path continuity later |
| Diff evidence | git diff --check; exact staged manifest before commit |
| Approval boundary | private packet/continuity; release requires clean worktree and staged empty after both commits, verified before operator manually starts worker; no push/provider effect |
| Claim boundary | synthetic UI source contradiction and task admission only |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-processing-lifecycle-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`; `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`; `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private provenance packet; no public catalog or publication claim.

## Claim Boundary

Finite ProcessingScreen client-lifecycle repair packet and synthetic offline red. Product source unchanged at dispatch. No confirmed backend cancellation, durable approval, full roadmap/release/live/provider/production/model-rank or cost claim. Requested model is operator metadata; reviewed collection remains16 until actual review.

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-LIFETIME","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx","docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json"],"requiredProofIds":["PROOF-REQ-LIFETIME"]},{"requirementId":"REQ-ONCE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx","docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json"],"requiredProofIds":["PROOF-REQ-ONCE"]},{"requirementId":"REQ-CONTROLS","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx","docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json"],"requiredProofIds":["PROOF-REQ-CONTROLS"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json","docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md"],"requiredProofIds":["PROOF-REQ-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-REQ-LIFETIME","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json#REQ-LIFETIME"},{"proofId":"PROOF-REQ-ONCE","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json#REQ-ONCE"},{"proofId":"PROOF-REQ-CONTROLS","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json#REQ-CONTROLS"},{"proofId":"PROOF-REQ-RETURN","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json#REQ-RETURN"}]}
```

Use exactly these fixed IDs in one current acceptance-evidence-json; expected/Git-observed union is exact four worker paths.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"ncr-processing-lifecycle","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"NCR-HOME-HISTORY-DISPATCH","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON - shared-workspace existing ProcessingScreen/component-test profile, no external architecture invocation.
High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - only client attempt lifecycle and synthetic regressions; transactional filesystem operations are outside scope.

## Intake Role Routing Decision

Intake summary: actual processing task lifecycle isolation and at-most-once dispatch/completion.
Scope classification: one existing component edit, one new sibling regression file and two proof/return files.
Risk sensitivity: offline client-only UI, no durable settlement.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Escalation condition: necessary split/new path, authority or source contradiction.
Reviewer/orchestrator narrows task and supplies acceptance; worker retains implementation autonomy.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` |
| Chain map route | Local ProcessingScreen lifecycle contradiction -> existing component -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing UI lifecycle/source-fidelity/closure owners |
| Disposition | internal existing product repair; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Enrolled Learning Application Plan

```learning-application-plan-json
{"schemaVersion":"cvf.learningApplicationPlan@1.0.0","bindings":[{"findingId":"NCR-LEARNING-APPLICATION-OBSERVABILITY","control":{"path":"governance/compat/learning_application_binding.py","sha256":"84068b6f197c19404a23daa643266d7f9ed334f313cd2d8bbe2f2e6d37d7b7b8"},"action":"Use actual scaffold before prose, supplied orchestrator source/acceptance mapping, honest actual read depth/clocks and four-path acceptance join; apply fixture independence and real component lifecycle assertions.","verificationPlan":"Local checks actual preparation/actions and delivered regression results; citation alone is not application proof."}]}
```

## Dated Owner Dependency Discovery

NOT_BINDING_REFERENCE_WITH_REASON: existing ProcessingScreen/component consumer and source-fidelity owner control. No new normative surface/schema. The authoring requirement is integrated into the existing owner/template in this material batch.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md --max-return-lines 450 --max-return-bytes 64000`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Conditional terms: External Knowledge Intake Routing (internal source route); Rescan Intelligence Hardening (N/A with reason: no rescan); Corpus Completeness And Report Integrity (named inputs/no whole scan); Finding-To-Governance Learning Disposition (attributed deviations); Epistemic Process Block (prediction/evidence/limits); Machine Closure Package (N/A with reason: worker must not close; Local closure owns package). Use explicit N/A with reason for non-applicable sections.

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; actual full executionBaseHead; git status --short; Changed Files; No-Commit Statement; Self-declared worker-return artifact: yes; one dispatchWorkOrder link.

Worker output read-ahead: governance/compat/check_worker_return_quality_gate.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_review_cost_control.py; governance/compat/check_gate_to_role_closeability.py and applicable docType/conditional checkers. Use current source constants before authoring; scaffold placeholders are not evidence. Worker records independentProbeDisposition: PENDING_REVIEWER_EXECUTION; it does not certify its own independent result. Return-Time Closeability Recheck is required. Omit non-applicable knowledge-map reconciliation headings; use Knowledge System Applicability with a reason. Required corpus token is the exact bullet Corpus verdict: NOT_APPLICABLE_WITH_REASON followed by the named-sources/no-scan reason. Preserve both failed and final evidence; initial and accepted identities never overwrite one another.
Final fast gate runs on final bytes. If a provisional PASS assertion is needed by checker shape, preserve the first failure and validate the assertion with an actual later PASS before returning. No manufactured red or gate evidence.

scaffoldPreparationCommand: `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md --check-shape --max-lines 450 --max-bytes 64000`
Run before long prose, not by manual skeleton recreation. Generated full-profile preview fits450/64000; final actual return must also fit. Capture command/profile receipt; pending fields are not acceptance.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: ABANDONED_ASYNC_RESULT_AND_DUPLICATE_CLIENT_ATTEMPT
independentProbeDispositionAtDispatch: PLANNED_FOR_LOCAL_REVIEW
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: worker independently constructs tests; distinct Local actual-component lifetime/identity challenge, no import of worker tests.
positiveControl: valid uncancelled response delivers exact output and receipt once.
negativeMutationClasses: transport ignores abort; cancelled/unmounted late completion; same-task callback rerender duplicate POST; manual and timer race; replacement A response leaks into B.
expectedInformationGain: actual component callback/attempt behavior beyond test counts, without claiming backend cancellation.
rerunCostReason: consume focused worker evidence; one bounded distinct lifecycle challenge, not broad duplicate suite.
reviewerDecisionOwner: LOCAL

## Required Artifact Manifest

| Path | Required worker action |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | exact owned edit/create, fixed acceptance ledger |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx` | exact owned edit/create, fixed acceptance ledger |
| `docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json` | exact owned edit/create, fixed acceptance ledger |
| `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md` | exact owned edit/create, fixed acceptance ledger |

No additional worker output. Completion reserved for Local.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> shared-workspace worker -> Local independent reviewer/closer -> session-sync steward |
| phase | packet authoring; bounded ProcessingScreen lifecycle repair; review; closure |
| baseHeadFor(phase) | dispatchBaseHead=07fbf32cf04a6f4fd53697e6d3bb2216911e2afd; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact four worker-owned paths; baseline/order and continuity separately owned |
| traceScope(phase, actor) | each actor records own actual reads/actions/results |
| commitOwner(phase) | Local closer; WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no other dirty tracked files at worker release |
| nextMoveSurfaces | active handoff and session state are steward-only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: distinct INTERNAL_AGENT implementation worker after committed dispatch
laneOwnedPaths: exact four Required Artifact Manifest paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return, four-path changed-set reconciliation and empty staged set

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Existing shared private workspace is the execution surface for the bounded ProcessingScreen repair worker |
| Contract source | archive-handled historical AHB contract `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; current `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | Existing review/evidence plus return/evidence; no workspace storage is created |
| Handoff fields | AHB block above and explicit lane handoff own route, base, paths, return and commit |
| State ownership | Local session-sync steward updates active continuity after material disposition |
| Guard owner | Existing handoff, workspace-design, trace and autorun checkers |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no; workspace UI/queue/runtime: no |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation path class | existing UI component and sibling tests; review/evidence |
| Storage decision | client attempt lifetime only, no new durable writer/storage |
| Existing aggregate impact | no worker aggregate edits |
| Generated state impact | steward-only authority/continuity |
| Durable governance boundary | existing approvals/receipts unchanged |
| Duplicate-owner control | no new schema/store/service |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
returnTimeRecheck: REQUIRED_BEFORE_REPAIR
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker; complete six-path continuity: `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | four allowed worker paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | ProcessingScreen lifecycle regressions and evidence | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity,pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | evidence and return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | WORKER_RETURN | worker | WORKER_RETURN | four allowed worker paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | REVIEW | reviewer | REVIEW | four worker paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | PRE_MATERIAL_COMMIT | reviewed worker paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | POST_MATERIAL | reviewer | REVIEW | Local completion review | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | current continuity surfaces | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL_CLOSURE | reviewed material/continuity ranges | EXACT_PATHS | Local-closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

This graph assigns repair and commit owners; it does not report those future gates as passed. Actual seat admission and pre-dispatch release remain separate.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-PROCESSING-LIFECYCLE-20261012","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md","docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md","docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json","docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md","docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md","docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json","docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx","docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json","docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION_MEMORY.md","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/state/entries/nextAllowedMove.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json","docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md","docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json"],"claims":["BOUNDED_PROCESSING_CLIENT_LIFECYCLE_REPAIR","NO_BACKEND_CANCEL_OR_LIVE_GOVERNANCE_CLAIM"],"requiredProof":["PROOF-REQ-LIFETIME","PROOF-REQ-ONCE","PROOF-REQ-CONTROLS","PROOF-REQ-RETURN"],"operatorCheckpoints":[],"forbiddenEffects":["PROVIDER_CALL","NETWORK_WRITE","PUBLIC_WRITE","DEPLOYMENT","REAL_DATA_MUTATION","HOOK_WIRING"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":null,"completenessClaimChanged":false}}
```

## Knowledge System Applicability

NOT_APPLICABLE_WITH_REASON: finite ProcessingScreen lifecycle repair and named source/fixture evidence; no semantic knowledge-map/retrieval production.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: internal source defect, no external/legacy absorption reopened.

## Evidence Reuse And Encoding Plan

ASCII authored packet/proof/return. Preserve existing product EOL/localized copy; any new localized copy follows explicit local Text Encoding Exception. Consume source/Local red evidence; no historical accepted suites replay for comparison. Source pins and Git blob IDs are separate. Provider memory is NOT_CVF_SOURCE.

## Negative Search And Collision Discipline

Exact new packet/baseline/case/return/proof/completion names checked absent by Path.exists before authoring; two existing product paths intentionally edit-owned. Collision with another lane or dirty unrelated path blocks release; no overwrite permission. No repository-wide absence claim.

## Source Pin Contract

| Source path | Working-file SHA-256 | HEAD-blob SHA-256 | Required semantic read |
|---|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | `82517a0870b432c327b2f9f04f75fb8dbfe40407bc6178c2f3fecdea5de3c96a` | `82517a0870b432c327b2f9f04f75fb8dbfe40407bc6178c2f3fecdea5de3c96a` | full component |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.test.tsx` | `62bb5e13d29f3e1df5a1ff3018e38c71a52f50b75070fa55171522afe1c5bcd1` | `62bb5e13d29f3e1df5a1ff3018e38c71a52f50b75070fa55171522afe1c5bcd1` | declared mocks and named contract groups |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | `9400ddde799b7c2ec386cdd1bd618df98be12b25020dba427607ecfb433d13fd` | `9400ddde799b7c2ec386cdd1bd618df98be12b25020dba427607ecfb433d13fd` | declared completion/back/render props only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | `9a4a65976b5b7a5d038f9cb412a90d417f804108cf1dd33bae4421989a863420` | `9a4a65976b5b7a5d038f9cb412a90d417f804108cf1dd33bae4421989a863420` | full configuration |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | `bc573b2a6133b07404c42f797bce43fe73464711e0281f29da8234bf2fed6b27` | `bc573b2a6133b07404c42f797bce43fe73464711e0281f29da8234bf2fed6b27` | guard/setup branches |
| `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json` | `445bb04cfd63a7dee67375a817a43e9322086b3a31555513b12a9223d499d70f` | `6e3af94f372fe1bd34a57dd397c6d89b07d542f5e56015c4c75f016697fc08c0` | sourceFinding/reproduction/limits |

Raw-file pins bind actual Windows bytes; HEAD-blob pins bind committed bytes, separate from Git object IDs. The new dispatch proof is introduced with this packet, not present at authoring base. All six rows must match released HEAD before edits; worker cannot repin. Hash checking does not substitute semantic reads. Baseline/order raw hashes must also match bootstrap currentAuthority. Global autorun PASS alone does not cover source pins.

```python
from pathlib import Path
import hashlib,re,subprocess
text=Path("docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md").read_text(encoding="utf-8")
block=text.split("## Source Pin Contract\n",1)[1].split("\n## ",1)[0]
rows=re.findall(r"\| `([^`]+)` \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|",block)
assert len(rows)==6, "Expected exactly6 source-pin rows"
digest=lambda b:hashlib.sha256(b).hexdigest()
for path,raw_pin,blob_pin in rows:
    raw=Path(path).read_bytes()
    blob=subprocess.check_output(["git","show","HEAD:"+path])
    assert digest(raw)==raw_pin, "Working-file pin mismatch: "+path
    assert digest(blob)==blob_pin, "HEAD-blob pin mismatch: "+path
    assert raw.replace(b"\r\n",b"\n")==blob.replace(b"\r\n",b"\n"), "Content drift: "+path
print("SOURCE_PIN_PASS: 6 working files + 6 HEAD blobs")
```

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md`
reviewerOwnedClosurePaths: `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md`; `docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json`; four exact worker paths; order/baseline disposition; matching authority projections when needed.
closureOwner: Local reviewer/closer
workerCommitPermission: FORBIDDEN

One reviewed material then separate actual-SHA six-path continuity, followed by clean split-range closure. Completion exclusively Local-owned.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: dedicated exact six-path dispatch/closure continuity and currentAuthority only; no guard/checker/hook mutation.
Protected paths:

- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: 2026-10-12 continuation and Sonnet5.5 high manual worker switch, standing audit/select/useful work-order/collection direction. Local owns necessary private commits and continuity; no push.
Rollback boundary: exact new packet and matching continuity only; preserve Home closure and historical observations.
Dispatcher material exact manifest: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_PROCESSING_LIFECYCLE_2026-10-12.md`; `docs/reviews/evidence/ncr-processing-lifecycle-dispatch-20261012.json`; `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json`; `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md`.
Dedicated continuity exact manifest: `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
Worker exact manifest: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.lifecycle.test.tsx`; `docs/reviews/evidence/ncr-processing-lifecycle-worker-20261012.json`; `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_WORKER_RETURN_2026-10-12.md`.
Local reserves `docs/reviews/CVF_NCR_PROCESSING_LIFECYCLE_COMPLETION_2026-10-12.md` and `docs/reviews/evidence/ncr-processing-lifecycle-local-20261012.json`; collection admission only after review. Never hand-edit generated aggregates.

## Near-Threshold Owner Maintainability Plan

ProcessingScreen current836 physical lines, ceiling950, hard1000. Lifecycle regression new<=550; existing826-line test remains read-only. Reuse component lifecycle mechanisms; do not compress semicolon statements or extract unauthorized helper solely to evade limits. If necessary scope cannot fit, one consolidated blocker. Return450/64000, proof128000. Handoff<=32768 bytes: steward replaces compact current paragraphs, does not append history or grow migration debt. No threshold exception change.

## Commit Prompt Readiness

Local first commits exact seven material docs after required preflight, then exact six actual-SHA continuity. Bound pre-dispatch and dry pre-implementation on clean released HEAD must PASS before operator-started worker. Worker cannot commit; reviewed product material and matching closure continuity follow only after acceptance. No push. Authoring base=07fbf32cf04a6f4fd53697e6d3bb2216911e2afd; worker recaptures executionBaseHead.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | source-selected ProcessingScreen lifecycle repair packet; offline synthetic contradiction |
| claimDisposition | CLAIM_REJECTED for live governance or host interception |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker result pending |
| actionEvidence | ACTION_EVIDENCE_PRESENT: actual Local five-case ProcessingScreen red and packet source audit |
| invocationBoundary | operator-started worker only after committed release |
| interceptionBoundary | no host/Gateway interception |
| claimLanguage | bounded client lifecycle outcome; implementation/review proof pending |
| forbiddenExpansion | provider/live/durable approval/store/type/schema/S5/Expense/public/deploy |

