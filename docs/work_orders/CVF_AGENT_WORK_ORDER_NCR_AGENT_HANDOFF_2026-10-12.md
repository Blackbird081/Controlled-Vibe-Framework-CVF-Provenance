# CVF Agent Work Order - NCR Agent Handoff Lifecycle

Memory class: governed-worker-dispatch
docType: work_order
Status: READY
Date: 2026-10-12
Batch ID: CVF-NCR-AGENT-HANDOFF-20261012
Dispatch base head: f0199132050799c293f6b34db8c27b535694baed
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
Worker return path: `docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md`
Worker: shared-workspace implementation worker role
Reviewer/closer: Local reviewer/closer role

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT shared-workspace implementation worker.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture full HEAD and start UTC clock before mandatory reads.
Current-time notes: requested Sonnet5.5 high is operator configuration metadata only.
Required first actions: progressive startup, full paired baseline/order, scoped source/checker reads, source/authority pins, clean/staged-empty, committed bound pre-implementation.
Do-not-misread notes: four paths, only existing dashboard layout is writable production; no provider effects, no broader chat/history redesign.
Return contract: exact four artifacts, COMPLETE_PENDING_REVIEW only final fixed ledger/gates PASS; otherwise one consolidated BLOCKED_WITH_REASON. No stage/commit/push, installation, browser/server or nested agents.

## Purpose

Repair the receiving side of the accepted Working Brief handoff: incoming prompt opens the correct isolated Agent Chat session; minimize/restore preserves that same session and never replays an already delivered prompt; a new explicit handoff is received while a chat is already open. Existing source has two witnessed lifecycle failures. Offline client/session binding only, not AI governance correctness.

## Authority Chain

Operator asked next on2026-10-12 after bounded draft-export closure, under standing manual worker / Local orchestrator-reviewer roles. Existing NCR local consumer milestone admits this isolated receiving-side lifecycle repair. Paired baseline `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md` grants exactly four worker files. Existing parked effect lanes stay parked; Local owns final review/closure.

## Local Branch Audit And Selection

Inspection base f0199132050799c293f6b34db8c27b535694baed. Dashboard unmounts wrapper when minimized but retains initialPrompt; wrapper binds incoming prompt to mount-time session. Distinct Local witness uses actual DashboardLayout/AgentChatWithHistory/useChatHistory, Chat leaf delivery recorder and synthetic localStorage only: initial A control passes, restore records [A,A] instead of[A], and B while A open records[A] instead of[A,B]. Actual2/2 desired assertions FAIL. `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` preserves witness source/log/pins. This is no provider-call or AI-policy failure proof; worker must add its own consumer regressions.

## Agent Roles

Local orchestrator/dispatcher owns exact expected requirements, packet and release; operator copies the short prompt to the shared-workspace worker. Worker authors only the four outputs. Local independent reviewer evaluates actual UI assertions and procedural evidence; closer/steward owns all commits and continuity. No agent is launched by authoring this packet.

## Requested Configuration Metadata

Operator-selected manual Sonnet, requested5.5 high. Native model/effort/tokens/bill only observed metadata; null with reason if unavailable. A system prompt model string is self-reported and not independently verified native identity.20 previous reviewed tasks remain unchanged until Local reviews this new task.

## Scope / Target / Owner Boundary

Exactly four worker files: existing `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx` modify, new `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx`/`docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json`/`docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md` create. Wrapper, history store, AgentChat/hook, Home/export, old tests and governed owners are read-only. Existing layout378 lines, cap700; new test<=600; return<=450 lines/64000 bytes; proof<=128000 bytes. One manual60min invocation including reads/tests/gates. Ignored runtime ncr-agent-handoff-worker-20261012 may hold logs. No new helper, schema, session-ID policy, history-limit/retention rule, provider, server/browser, dependency install, new gate, subagent or other production path. Required out-of-scope repair => one consolidated blocked return.

## Design Control Gate

Use actual DashboardLayout, AgentChatWithHistory and persisted useChatHistory at decisive event/session boundaries. Preserve normal navigation, history and close behavior. Chat leaf may be a transparent synthetic recorder to isolate initialPrompt/message callbacks and minimize/close; disclose it. Include one real AgentChat/hook receiving case with in-process deterministic provider-adapter stub or no-key presentation; retain shared fetch/network denial. Transport mocks prove client wiring only; no AI governance decisions, full-mode certification, real provider/HTTP/backend cancellation or browser claim. No source change by dispatcher.

## Write Ownership

| Owned path | Action |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx` | modify existing dashboard event/prompt/modal lifecycle only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx` | create regression/proof/pending return |
| `docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json` | create regression/proof/pending return |
| `docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md` | create regression/proof/pending return |

## Implementation Contract

1. Fix shell-level handoff/session binding using existing components/callbacks. Choose a bounded implementation; keeping the same chat mounted while visually minimized and binding fresh identity to each explicit incoming handoff is one feasible approach. No global dedupe registry, timeout hack or modification to wrapper/history/hook is authorized.
2. A first explicit cvf:openAgent prompt must reach its own ready chat session exactly once. Initial A must be distinct from an unrelated saved history session; do not overwrite saved message fields. Compare complete prompt/messages, not only session/button counts.
3. Minimize then restore before and after the initial timer/delivery, and ordinary unrelated rerenders/StrictMode where supported, must preserve the same session and draft/messages without extra handoff delivery/session. A hidden chat is visually inaccessible; do not weaken modal/body-scroll behavior. Do not assert global provider abort from UI lifecycle.
4. A new explicit B handoff while A is open must create a ready fresh session for B with no A prompt/messages/ambient history contamination; completed A stays in history. Also cover ordinary empty chat already open before incoming B. Two deliberate events with identical prompt text are two user handoffs: do not silently dedupe intent by text; ordinary restore/rerender is not a new event.
5. Close clears shell incoming prompt and restores navigation/body overflow; reopening ordinary chat/history must not replay a handoff. Closing/replacing before deferred initial-send timer fires must not dispatch the stale queued prompt; consume existing hook cleanup controls, add only the composed seam cases. No guarantee aborting a request already started.
6. Add independently authored focused regressions, retain existing tests, and use the real AgentChat/hook in at least one bounded synthetic receiver integration. In-process adapter response is fixture text only; no actual AI/governance behavior claim. A required source fault beyond writable layout is a consolidated blocker, not authority to expand paths.

## Acceptance Criteria

REQ-RECEIVE: first/new/identical-text explicit handoffs reach isolated ready sessions and correct complete prompts/messages; ordinary open-chat control and real receiver seam.
REQ-LIFECYCLE: minimize/restore and rerenders preserve session/prompt binding and drafts without replay; close/replacement timer cleanup, saved A/ambient history retained, no contamination.
REQ-RETURN: four raw artifacts, honest read/model/clock/failure/source/stub scopes; focused/type/lint and final fast/ledger PASS, no staged/forbidden effects.

## Work-Order Fulfillment Manifest

Dispatcher-owned three requirements/proofs, exact four-file Git artifact union. Layout source mutation is mandatory for this witnessed repair; no worker-owned completion or collection edit.

## Required First Reads

| Source (under Web package unless noted) | Mandatory semantic scope |
|---|---|
| `full paired baseline and work order` | all scope, authority, gates and fixed proof IDs |
| `src/app/(dashboard)/layout.tsx` | full; event handler, prompt state, mount/minimize/restore/close and URL synchronization |
| `src/components/AgentChatWithHistory.tsx` | full; initial prompt session binding and persisted message binding |
| `src/lib/chat-history.tsx` | load/save hook, initialization/create/update/setActiveSession; sidebar API and stale independent snapshot limits |
| `src/components/AgentChat.tsx` | full; callbacks and real hook wiring |
| `src/lib/hooks/useAgentChat.ts` | initial prompt timer/ref, send lifecycle, callbacks and unmount cleanup; transport boundary |
| `src/app/(dashboard)/layout.test.tsx and src/components/AgentChatWithHistory.test.tsx` | full; existing mocks and accepted initial binding controls |
| `src/lib/hooks/useAgentChat.test.ts and src/lib/chat-history.test.tsx` | fixtures and StrictMode/timer/single-send/persistence cases; do not import worker suite |
| `src/app/(dashboard)/home/page.tsx` | handleSendToAgent event detail only; reuse accepted export proof, no duplicate form/export suite |
| `src/test/setup.ts and vitest.config.ts` | full; provider/fetch denial and runner |
| `docs/reviews/CVF_NCR_DRAFT_EXPORT_COMPLETION_2026-10-12.md` | accepted emission boundary and limits |
| `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | full; initial source witness, synthetic leaf limits and raw source pins |

Read mandatory worker output-checker constants before return prose: quality gate, acceptance ledger, trace, review-cost, gate-closeability and applicable conditional owners. Record actual depth and omissions; no read quiz or retrospective certification. Full handoff history is not required; progressive current-authority reading remains canonical.

## Execution Plan

1. Start UTC clock and HEAD/status before reads; full paired order/baseline, bootstrap authority and raw/HEAD pins. Bound pre-implementation before creating output.
2. Read mandatory source scopes, run actual return scaffold, author own red regressions against current source and record first meaningful failure.
3. Repair only layout. Run new test plus existing layout/wrapper/hook selected suite, typecheck and lint two owned TypeScript files. Fill evidence/return on final bytes.
4. Final fixed ledger and fast gate; record final-test, final-gate and final terminal clocks after the last evidence mutation/confirmation. Stop finite scope or one consolidated blocker.
```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md
```
Installed Web package commands:
```powershell
node node_modules/vitest/vitest.mjs run 'src/app/(dashboard)/layout-agent-handoff.test.tsx' 'src/app/(dashboard)/layout.test.tsx' 'src/components/AgentChatWithHistory.test.tsx' 'src/lib/hooks/useAgentChat.test.ts'
node node_modules/typescript/bin/tsc --noEmit --incremental false
node node_modules/eslint/bin/eslint.js 'src/app/(dashboard)/layout.tsx' 'src/app/(dashboard)/layout-agent-handoff.test.tsx'
```
No duplicate whole package/form/export suite. Shared denial stays enabled; synthetic adapter cannot be live proof.

## Pre-Flight Checks

Clean/staged empty, four-path binding with three new paths absent, captured full HEAD/clock and read-depth; full paired packet, bootstrap authority hashes and twelve raw/HEAD source pins; bound pre-implementation and retained provider-denial setup. Existing saved history is synthetic only.

## Evidence Requirements

REQ-RECEIVE/REQ-LIFECYCLE/REQ-RETURN proof records first source-red and final controls, full prompt/session/message snapshots, existing history preservation, timer/rerender and actual receiving seam; source/stub/read scopes and all relevant omissions. Every command reports exit/log hash; preserve first/final results. Clock starts before reads and ends after last confirmation; distinguish preliminary and final terminal. Native identity unavailable => null with reason, self-reported identity separate; tokens/bill may stay unavailable. No all-files/complete-read claim unless actual scopes support it.

## Verification Commands

Use focused Web test/type/lint commands in Execution Plan. Root commands on final bytes:
```powershell
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md --max-return-lines 450 --max-return-bytes 64000
python governance/compat/check_work_order_acceptance_ledger.py --work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md --return docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md --enforce
git diff --check
git status --short
```
Scaffold command in Worker Return Packet Shape Contract must run before long prose. Preserve first failed and final gate results; only actual final PASS supports COMPLETE_PENDING_REVIEW.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap owner | Selected work | Worker output |
|---|---|---|
| docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md Current Delivery Checkpoint | receiving Agent Chat session lifecycle repair | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx`; `docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json`; `docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md` |

## Worker Autonomy / No-Question Rule

Resolve ordinary owned implementation/test/return choices autonomously. Hold source/authority contradiction, missing assigned surface, necessary extra path/split, outside effect or budget exhaustion; return one consolidated BLOCKED_WITH_REASON. No checker weakening, fallback model substitution or automatic redispatch.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED
dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-AGENT-HANDOFF-20261012
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

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | previous bounded dispatch; WORKER_MUST_NOT_COMMIT; INTERNAL_AGENT; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; SECTION_GROUPS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of selected packet structure; not a dispatch or implementation proof |
| claimBoundary | targeted current checker constants/required sections and ready-state predicates read; not an all-lines reading claim |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: incoming event mount/minimize route | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | actual DashboardLayout event and modal render | ACCEPT |
| EXISTS: prompt session binds on mount | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | AgentChatWithHistory/useChatHistory | ACCEPT |
| EXISTS: deferred once-send cleanup controls | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | sourceFacts / sourcePins | sourceFacts | useAgentChat timer/ref and tests | ACCEPT |
| EXISTS: two scoped UI lifecycle failures | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` | admissionWitness | admissionWitness | actual shell/wrapper/history with disclosed Chat recorder | ACCEPT |

## Review Gate

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Local checks returned actual DOM/blob/event/storage assertions, exact artifact/proof join and read/clock telemetry. One distinct Local revision/isolation challenge provides independent information gain beyond worker test counts; no broad duplicate suite. Routine M5/M10/safety/M20 with retained original failures. Technical result and worker procedure are separate dispositions.

## Closure Checklist

Local alone owns later completion, independent proof, model observation and dedicated continuity. Consume accepted evidence and preserve all failures. Worker test PASS is not Local acceptance or a whole NCR milestone exit. No automatic successor or push.

## Return-To-Orchestrator Conditions

COMPLETE_PENDING_REVIEW only all mandatory rows/final gates PASS and closeabilityDisposition CLOSEABLE/outsideAuthorityBlockers NONE. Preserve own witnessed initial source failures and repairs. A required repair outside layout is BLOCKED_WITH_REASON, not permission to expand paths. Record clocks after final evidence confirmation; native metadata null with reason if unavailable.

## Operator Checkpoint

Operator has selected Sonnet and manual copy transfer. No repeat model/branch question. Any effect outside scope or extra path requires Local orchestration; worker returns one consolidated blocker rather than seeking blanket permission. Provider/public/deploy checkpoints stay parked.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named consumer/test evidence only; no repository/corpus scan.

## Epistemic Process Block

Expected Result / Prediction: each explicit incoming handoff owns one fresh ready chat; shell minimize/restore preserves it, while new handoff changes session.
Evidence Comparison: existing mount controls consumed; distinct two-case shell/history witness initial A passes then desired2/2 fail (replay A, lost B); source/log in dispatch JSON. No production mutation by dispatcher.
Contradiction Or Gap Disposition: concrete receiving-session lifecycle defect, distinct from accepted prompt emission; repair layout only or consolidated blocker.
Claim Update: bounded offline client repair selected; worker implementation and independent Local review pending.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-AGENT-HANDOFF-20261012 --title "NCR Agent Handoff Lifecycle" --date 2026-10-12 --base f0199132050799c293f6b34db8c27b535694baed --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_DRAFT_EXPORT_COMPLETION_2026-10-12.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-agent-handoff-lifecycle --scec-successor-scope NO_SUCCESSOR --stdout |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: prior verified ready role-contract shape, four paths and witnessed receiving lifecycle contract; no copied closure |
| checkerReadAheadConfirmation | current dispatch/closeability/scaffold/read-ahead constants; retained verified role/trace/ledger/probe bindings, scoped read only |
| docOnlyNewFields | source witness and consumer repair contract; no new schema |
| claimBoundary | packet preparation and scoped source witness only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT orchestrator/dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-agent-handoff-dispatch-20261012 |
| Working directory | repository root and installed Web package |
| Command or tool surface | targeted source/owner reads, actual scaffold/ADIF, bounded two-case inspection witness, source pins, dispatch/gates/commits |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator next following manual worker role assignment; existing outcome-bound lifecycle |
| Before status evidence | HEAD f0199132050799c293f6b34db8c27b535694baed; clean/staged empty; temporary Local witness removed |
| After status evidence | exact11 dispatch material then dedicated exact6 continuity; worker not started |
| Diff evidence | git diff --check and exact manifests |
| Approval boundary | manual shared-workspace worker; offline client source only |
| Claim boundary | two synthetic leaf-boundary failures witnessed; no provider or AI governance claim |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-agent-handoff-dispatch-20261012 |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`; `docs/roadmaps/README.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`; `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`; `.gitattributes`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH required before commit |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch and offline proof only; no publication grant.

## Claim Boundary

Incoming client/session lifecycle repair only. Accepted export/emission evidence consumed; no whole NCR/full/app-builder/wizard/browser/backend/live/AI-governance/public/deploy/model-winner claim. Provider effects remain forbidden. Stop after selected outcome.

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-RECEIVE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx","docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json"],"requiredProofIds":["PROOF-REQ-RECEIVE"]},{"requirementId":"REQ-LIFECYCLE","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx","docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json"],"requiredProofIds":["PROOF-REQ-LIFECYCLE"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json","docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md"],"requiredProofIds":["PROOF-REQ-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-REQ-RECEIVE","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json#REQ-RECEIVE"},{"proofId":"PROOF-REQ-LIFECYCLE","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json#REQ-LIFECYCLE"},{"proofId":"PROOF-REQ-RETURN","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json#REQ-RETURN"}]}
```

Exact three proof IDs; expected/Git-observed union exactly four worker paths.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"ncr-agent-handoff-composition","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"NCR-AGENT-HANDOFF-COMPOSITION-DISPATCH","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON - shared-workspace synthetic UI composition proof; no external architecture invocation.
High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - no transactional filesystem/durable writer/binding mutation.

## Intake Role Routing Decision

Intake summary: incoming Agent Chat shell/session receiving lifecycle; two scoped source witness failures.
Scope classification: bounded existing client layout repair and new regressions/evidence.
Risk sensitivity: synthetic local client session data.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Decision owner: Local orchestrator/reviewer.
Escalation condition: required out-of-manifest path or authority; one consolidated blocker. No new external research.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json` |
| Chain map route | Local receiving dashboard handoff/session lifecycle repair -> existing component -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing UI lifecycle/source-fidelity/closure owners |
| Disposition | internal existing product composition proof; no external research |
| Claim boundary | Local private source verification and final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Enrolled Learning Application Plan

```learning-application-plan-json
{"schemaVersion":"cvf.learningApplicationPlan@1.0.0","bindings":[{"findingId":"NCR-LEARNING-APPLICATION-OBSERVABILITY","control":{"path":"governance/compat/learning_application_binding.py","sha256":"84068b6f197c19404a23daa643266d7f9ed334f313cd2d8bbe2f2e6d37d7b7b8"},"action":"Use actual scaffold before prose, supplied source/acceptance mapping, honest read depth/clocks and exact four-path join; independently constructed fixtures and actual incoming event/session/rerender/timer assertions.","verificationPlan":"Local checks actual preparation/actions and delivered regression results; citation alone is not application proof."}]}
```

## Dated Owner Dependency Discovery

NOT_BINDING_REFERENCE_WITH_REASON: existing dashboard layout, AgentChatWithHistory/chat-history and AgentChat hook source control. No new schema/status or normative owner; source witness and finite requirements resolved before implementation.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md --max-return-lines 450 --max-return-bytes 64000`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Conditional terms: External Knowledge Intake Routing (internal source route); Rescan Intelligence Hardening (N/A with reason: no rescan); Corpus Completeness And Report Integrity (named inputs/no whole scan); Finding-To-Governance Learning Disposition (attributed deviations); Epistemic Process Block (prediction/evidence/limits); Machine Closure Package (N/A with reason: worker must not close; Local closure owns package). Use explicit N/A with reason for non-applicable sections.

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; actual full executionBaseHead; git status --short; Changed Files; No-Commit Statement; Self-declared worker-return artifact: yes; one dispatchWorkOrder link.

Worker output read-ahead: governance/compat/check_worker_return_quality_gate.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_review_cost_control.py; governance/compat/check_gate_to_role_closeability.py and applicable docType/conditional checkers. Use current source constants before authoring; scaffold placeholders are not evidence. Worker records independentProbeDisposition: PENDING_REVIEWER_EXECUTION; it does not certify its own independent result. Return-Time Closeability Recheck is required. Omit non-applicable knowledge-map reconciliation headings; use Knowledge System Applicability with a reason. Required corpus token is the exact bullet Corpus verdict: NOT_APPLICABLE_WITH_REASON followed by the named-sources/no-scan reason. Preserve both failed and final evidence; initial and accepted identities never overwrite one another.
Final fast gate runs on final bytes. If a provisional PASS assertion is needed by checker shape, preserve the first failure and validate the assertion with an actual later PASS before returning. No manufactured red or gate evidence.

scaffoldPreparationCommand: `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md --check-shape --max-lines 450 --max-bytes 64000`
Run before long prose, not by manual skeleton recreation. Generated full-profile preview fits450/64000; final actual return must also fit. Capture command/profile receipt; pending fields are not acceptance.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: INCOMING_HANDOFF_SESSION_LIFECYCLE_ISOLATION
independentProbeDispositionAtDispatch: PLANNED_FOR_LOCAL_REVIEW
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: Local separately authors event/session/timer challenge; no worker test imports.
positiveControl: actual shell receives current prompt in ready wrapper/history session.
negativeMutationClasses: restore replay, lost replacement, stale queued prompt, saved session contamination.
expectedInformationGain: actual binding/once-only behavior beyond counts.
rerunCostReason: one distinct finite Local probe after valid worker evidence; no broad repeated suite.
reviewerDecisionOwner: LOCAL

## Required Artifact Manifest

| Path | Required worker action |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx` | modify layout only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx` | create; fixed acceptance ledger |
| `docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json` | create; fixed acceptance ledger |
| `docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md` | create; fixed acceptance ledger |

Completion is Local-owned.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> shared-workspace worker -> Local independent reviewer/closer -> session-sync steward |
| phase | packet authoring; bounded visible handoff lifecycle composition proof; review; closure |
| baseHeadFor(phase) | dispatchBaseHead=f0199132050799c293f6b34db8c27b535694baed; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
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
| Workspace purpose | Existing shared private workspace is the execution surface for the bounded visible handoff lifecycle proof worker |
| Contract source | archive-handled historical AHB contract `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; current `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | Existing review/evidence plus return/evidence; no workspace storage is created |
| Handoff fields | AHB block above and explicit lane handoff own route, base, paths, return and commit |
| State binding | Local session-sync steward updates active continuity after material disposition |
| Guard owner | Existing handoff, workspace-design, trace and autorun checkers |
| Build boundary | runtime source: bounded existing client layout only; provider proof: no; public-sync: no; registry edits: no; workspace UI/queue/runtime: no |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation path class | existing UI pages and sibling test; review/evidence |
| Storage decision | preserve existing persisted chat history through existing hook; no new writer/schema/migration |
| Existing aggregate impact | no worker aggregate edits |
| Generated state impact | steward-only authority/continuity |
| Durable governance boundary | existing approvals/receipts unchanged |
| Duplicate-owner control | no new store/service |

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
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | visible handoff lifecycle composition regressions and evidence | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity,pre_implementation_autorun |
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
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-AGENT-HANDOFF-20261012","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md","docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md","docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json","docs/roadmaps/README.md","docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md","docs/roadmaps/CVF_ROADMAP_INVENTORY.md","docs/roadmaps/CVF_ROADMAP_INVENTORY.csv",".gitattributes","CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json","CVF_SESSION/ACTIVE_SESSION_STATE.json","CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout-agent-handoff.test.tsx","docs/reviews/evidence/ncr-agent-handoff-worker-20261012.json","docs/reviews/CVF_NCR_AGENT_HANDOFF_WORKER_RETURN_2026-10-12.md","AGENT_HANDOFF_V63_2026-09-18.md","CVF_SESSION_MEMORY.md","CVF_SESSION/state/entries/nextAllowedMove.json"],"claims":["BOUNDED_OFFLINE_CLIENT_SESSION_LIFECYCLE_REPAIR","NO_AI_GOVERNANCE_OR_WHOLE_NCR_EXIT"],"requiredProof":["PROOF-REQ-RECEIVE","PROOF-REQ-LIFECYCLE","PROOF-REQ-RETURN"],"operatorCheckpoints":[],"forbiddenEffects":["PROVIDER_CALL","NETWORK_WRITE","PUBLIC_WRITE","DEPLOYMENT","REAL_DATA_MUTATION","HOOK_WIRING"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":null,"completenessClaimChanged":false}}
```

## Knowledge System Applicability

NOT_APPLICABLE_WITH_REASON: named dashboard/chat source and fixture evidence only; no corpus rescan or semantic knowledge-map/retrieval production.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: internal source defect, no external/legacy absorption reopened.

## Evidence Reuse And Encoding Plan

ASCII governance prose, UTF-8 existing UI/source labels. Text Encoding Exception: localized UI labels may be asserted in new tests; retain existing UTF-8/EOL. Raw and Git blob hashes are separate; provider memory is NOT_CVF_SOURCE. Consume accepted export and once-send controls; new owned source must remain bounded.

## Negative Search And Collision Discipline

Existing layout tracked; three new output paths absent before dispatch/worker start. No overwrite of other lane, old tests or source wrappers. Named path absence only, not whole corpus absence.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_NCR_AGENT_HANDOFF_COMPLETION_2026-10-12.md`
reviewerOwnedClosurePaths: `docs/reviews/CVF_NCR_AGENT_HANDOFF_COMPLETION_2026-10-12.md`; `docs/reviews/evidence/ncr-agent-handoff-local-20261012.json`; four worker paths; order/baseline disposition and raw authority projections.
closureOwner: Local reviewer/closer
workerCommitPermission: FORBIDDEN

One reviewed material then separate actual-SHA six-path continuity, clean split-range closure; completion exclusively Local-owned.

## Commit Prompt Readiness

Local commits exact11 dispatch material then exact6 actual-material SHA continuity; clean committed bound pre-dispatch and dry pre-implementation PASS before manual start. Inspection base f0199132050799c293f6b34db8c27b535694baed; worker captures actual released executionBaseHead. Worker must not commit, no push.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: named UI composition proof, no rescan/intake.

## Source Pin Contract

| Source path | Raw SHA256 | HEAD blob SHA256 |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.tsx` | `18e35af0031172385bc9e16811ba242011c0a3d8cefc9c3888403e61979f16a8` | `18e35af0031172385bc9e16811ba242011c0a3d8cefc9c3888403e61979f16a8` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/layout.test.tsx` | `bc3b183f79782da0e42725cb576b3287747b43e7edddd7848e3f3e83cd50f133` | `bc3b183f79782da0e42725cb576b3287747b43e7edddd7848e3f3e83cd50f133` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.tsx` | `20d74655258b5c9033f7a42d6821c07cc5c23d857abf3faf057e16bb78f949bf` | `20d74655258b5c9033f7a42d6821c07cc5c23d857abf3faf057e16bb78f949bf` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.test.tsx` | `278becb72892428deb1aa1341c077f9989e814102de7d6a1b87009b6312154cd` | `278becb72892428deb1aa1341c077f9989e814102de7d6a1b87009b6312154cd` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChat.tsx` | `f5e31153e8b0482d1036904aae64cd7d81d36ab654076afcbe355568c9bd238a` | `f5e31153e8b0482d1036904aae64cd7d81d36ab654076afcbe355568c9bd238a` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.tsx` | `dc4a450b97cd74dea6f67c23b253e06726622382c055c4cc48c1be8849803d0b` | `dc4a450b97cd74dea6f67c23b253e06726622382c055c4cc48c1be8849803d0b` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.test.tsx` | `17b4e014a05d22a5547a2b8341029a4b6ad4a2de5ce3e611833ca38c4e094289` | `17b4e014a05d22a5547a2b8341029a4b6ad4a2de5ce3e611833ca38c4e094289` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.ts` | `5f60cb289473b21e0d3c017992478cfa9bb062b7c891c7ba1479d854ad0b5192` | `5f60cb289473b21e0d3c017992478cfa9bb062b7c891c7ba1479d854ad0b5192` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.test.ts` | `09ecf7a2c9d63ed6ecd7b188a6a56d3cb4e37d0f4b55231916b6ce67cae30494` | `09ecf7a2c9d63ed6ecd7b188a6a56d3cb4e37d0f4b55231916b6ce67cae30494` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/home/page.tsx` | `b6b1d7ff64bcc5586b830b2a23c8e1b94957ef276a4abd9cea9eaa0825965322` | `b6b1d7ff64bcc5586b830b2a23c8e1b94957ef276a4abd9cea9eaa0825965322` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | `bc573b2a6133b07404c42f797bce43fe73464711e0281f29da8234bf2fed6b27` | `bc573b2a6133b07404c42f797bce43fe73464711e0281f29da8234bf2fed6b27` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | `9a4a65976b5b7a5d038f9cb412a90d417f804108cf1dd33bae4421989a863420` | `9a4a65976b5b7a5d038f9cb412a90d417f804108cf1dd33bae4421989a863420` |

Worker verifies base raw and HEAD pins plus authority; no repin. Only layout may change afterward, record final hash; all other pins stay intact.

## Near-Threshold Owner Maintainability Plan

NOT_APPLICABLE_WITH_REASON: layout currently378 lines, capped700; new regression capped600, below1200 hard threshold. Exact writable paths need no foreseeable split. An extra helper requires consolidated blocked return, not implicit topology expansion.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | selected visible handoff lifecycle UI composition packet |
| claimDisposition | CLAIM_REJECTED for live governance/interception |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker proof pending |
| actionEvidence | ACTION_EVIDENCE_PRESENT: named current source inspection and exact scaffold/ADIF |
| invocationBoundary | operator manually starts worker after clean committed bound release |
| interceptionBoundary | no host/Gateway interception |
| claimLanguage | synthetic UI/source revision and export only |
| forbiddenExpansion | out-of-manifest source/provider/live/public/deploy/real data |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local dispatch raw authority projection then exact6 continuity. Worker cannot edit protected paths.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: next under standing manual worker/Local orchestrator-reviewer roles,2026-10-12.
Rollback boundary: exact11 dispatch and exact6 continuity, prior accepted worker/evidence and20 observations retained; no guard/hook changes.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST
Atomicity reason: selected roadmap/index/inventory, new packet/witness and raw authority projections bind one dispatch; dedicated continuity binds actual material SHA.
Rollback boundary: exact11 dispatch below.
Exact changed manifest:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_AGENT_HANDOFF_2026-10-12.md`
- `docs/baselines/CVF_GC018_NCR_AGENT_HANDOFF_2026-10-12.md`
- `docs/reviews/evidence/ncr-agent-handoff-dispatch-20261012.json`
- `docs/roadmaps/README.md`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.md`
- `docs/roadmaps/CVF_ROADMAP_INVENTORY.csv`
- `.gitattributes`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Expected Artifact Existence: packet/witness authored before commit; other material paths tracked. Existing worker layout tracked; three future worker outputs absent.

## Finding-To-Governance Learning Disposition

Defect class: ORCHESTRATOR_PACKET_GAP
Learning lane: GOVERNANCE_CONTROL_PLANE
Disposition: RULE_EXISTS - first Local authoring preflight exposed envelope/fence/baseline-shape omissions and UI session-binding risk-word ambiguity; one consolidated packet correction, failure preserved in dispatch JSON.
Next action: apply existing checker literals and finite source contract before transfer; no new checker, worker quiz or scope.
