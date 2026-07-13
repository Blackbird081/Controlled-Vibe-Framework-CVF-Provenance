# CVF Agent Work Order - SOT3 Activation A3 Real Provider Approved Context Proof

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

docType: work_order

Batch ID: SOT3-ACT-A3

Date: 2026-07-13

dispatchBaseHead: `02d7b765c`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation and live-proof worker

Reviewer/closer: independent reviewer/closer

## Dispatch Prompt Envelope

Role: delegated SOT3 A3 live-proof worker.

Canonical packet: this work order.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: use the actual clean post-dispatch HEAD, current source,
and operator-local key bootstrap on 2026-07-13.

Do-not-misread notes: this is one bounded provider happy-path check, not A4
failure/recovery, A5 release integration, product runtime mutation, provider
comparison, prompt tuning, public export, or production deployment.

Required first actions: read startup front doors, guard orientation, literal
gotchas, paired baseline, parent roadmap, A2 completion, this work order, all
cited source/checkers, and the archived live diagnostic standard. Capture
clean HEAD/status and confirm key alias presence without printing its value.

Return contract: create exactly five worker outputs, spend one planned live
call with at most one diagnostic-gated retry, run the required checks, leave
HEAD unchanged, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Prove through a real Alibaba DashScope-compatible call that the selected CVF
Web `/api/execute` path sends SOT3 Flow-approved knowledge context downstream
in `ENFORCE`, then correlate that provider result with the persisted A2 record
in one new secret-safe receipt and hash manifest.

## Authority Chain

| Authority | Evidence |
|---|---|
| Operator instruction | A0-A5 operational proof authorized on 2026-07-13; operator instructed continuation because accepted A2 material commit `fdead7c99` exists |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; current mode `sot3_activation_a2_closed_bounded_a3_packet_next` |
| Parent roadmap | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; A3 Detailed Design and Next Allowed Move |
| GC-018 | `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` |
| Accepted predecessor | `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md`; material commit `fdead7c99` |
| Active handoff | `AGENT_HANDOFF_V42_2026-07-12.md` |

Authority boundary: current runtime source and canonical CVF artifacts control.
Chat and provider-local memory are not source authority. Any contradiction
returns to the reviewer before a live call.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatcher | dispatcher | source verification, packet, dispatch commit |
| Worker | delegated worker | exact five outputs, local checks, bounded live run, no commit |
| Reviewer/closer | independent reviewer/closer | semantic review, receipt recomputation, closure and commit |
| Operator | human | any third call, provider substitution, product/runtime expansion, A4-A5, public or production claim |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V42_2026-07-12.md`
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. the paired A3 baseline, parent roadmap, A2 completion, and this work order
7. all files named in Source Verification and Checker Source Read-Ahead
8. `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
9. `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`

## Pre-Flight Checks

- capture `git rev-parse --short HEAD` as executionBaseHead;
- require empty `git status --short` before edits;
- re-run the source symbol searches from Source Verification;
- run pre-implementation autorun with the captured execution base;
- call `bootstrap_repo_env` and report only the selected key alias name and
  presence, never its value;
- confirm both dated evidence paths are absent;
- confirm planned and observed provider-call counters start at zero.

## Write Ownership

Worker owns exactly the five paths in Work-Order Fulfillment Manifest. Existing
files, even adjacent live tests and A2 source, are read-only. Reviewer owns the
completion review, baseline/work-order closeout, roadmap update, governed
learning decision, material commit, and separate session sync.

## Scope / Target / Owner Boundary

Target: one tenant-scoped collection and one controlled execute request through
actual retrieval, SOT3 Refinery-Kernel-Flow evaluation, A2 persistence, and the
real Alibaba provider adapter.

The test may mock authentication, quota accounting, unrelated enforcement, and
output validation only to isolate A3 and prevent route auto-retry. It must not
mock `resolveKnowledgeContext`, the three SOT3 packages, the A2 store,
`executeAI`, global provider success, or the DashScope network response.

Risk ceiling: R2 live proof.

## Allowed Scope

- add `scripts/run_cvf_sot3_a3_live_proof.py`;
- add one route-adjacent Alibaba live test named in the fulfillment manifest;
- add one new receipt JSON and one manifest JSON under `docs/reviews/evidence`;
- add one full-profile worker return under `docs/reviews`;
- use local temporary stores and intercept `globalThis.fetch` only as a
  pass-through observer that forwards the real DashScope request;
- hash and compare context in memory, recording only booleans, lengths, IDs,
  hashes, timings, provider/model, call count, and safe diagnostics;
- perform one planned live call and one retry only when a recorded diagnostic
  says retryable and the rerun-changing action is explicit.

## Forbidden Scope

- no modification of existing runtime source, tests, package exports, SOT3
  owner packages, route helpers, provider adapter, store schema, receipt schema,
  release runner, governance checker/hook, Catalog/GAP, or session surfaces;
- no mock/fake provider output, cached response, or provider-call suppression;
- no full system prompt, raw provider body, raw output, source content, API key,
  bearer header, environment value, or signed header in evidence;
- no automatic output-validation provider retry during the proof;
- no A4 negative/recovery matrix, A5 canonical release bundle, public-sync,
  production, scale, distributed durability, provider ranking, or user claim.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A2 closure | A2 completion file at material commit `fdead7c99` is `CLOSED_PASS_BOUNDED`; focused 71/71 and full non-live 3207 PASS | durable record and restart lookup must exist | ACCEPT |
| Roadmap A3 release | parent roadmap status is `A2_CLOSED_PASS_BOUNDED_A3_PACKET_NEXT` and its A3 section requires a fresh packet | A3 packet only may be dispatched | ACCEPT |
| Key continuity | `scripts/_local_env.py` lists CVF Web `.env.local`; `AGENTS.md` requires checking it before claiming no live key | worker confirms alias presence without exposing value | ACCEPT |

## Worker Autonomy / No-Question Rule

Resolve allowed-scope test/runner details from verified source. Repair any
allowed-scope gate or test-shape defect directly. Stop only for missing
authority, source contradiction, credential/policy/secret failure, need to
change a forbidden path, or need to exceed the two-call hard ceiling.

Do not ask the operator whether to fix an allowed-scope failure. Do not rerun a
failed call until its diagnostic and result-changing action are recorded.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | execute one bounded SOT3 real-provider proof from accepted A2 state |
| scopeClassification | runtime-provider-live evidence with proof-only instrumentation |
| riskSensitivity | R2 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | delegated worker; independent reviewer/closer |
| escalationCondition | source contradiction, secret risk, third-call need, provider substitution, runtime owner mutation, or broader claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live provider proof work-order authoring dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "live provider proof work-order authoring dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | exact query above |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific constraint returned |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | gate PASS proves packet shape only, not a live SOT3 result |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execute route entry | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 95 | `POST` | CVF Web execute route | ACCEPT |
| provider call follows knowledge resolution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 686-741 | `resolveKnowledgeContext`; `executeAI` | execute route | ACCEPT |
| SOT3 result and approved prompt owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | lines 270-358 | `resolveKnowledgeContext` | `KnowledgeContextResult` | ACCEPT |
| durable SOT3 lookup | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 278-359 | `Sot3ActivationEvidenceStore`; `findByRecordId` | A2 evidence store | ACCEPT |
| governance receipt construction | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 74, 147-169 | `buildExecuteFinalResponse` | Web governance evidence receipt | ACCEPT |
| knowledge fixture store | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | lines 59-79 | `seed` | knowledge store | ACCEPT |
| audit reader | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | line 163 | `readAuditEvents` | unified audit event store | ACCEPT |
| key alias resolver | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | lines 1-18 | `resolveAlibabaApiKey` | Alibaba environment boundary | ACCEPT |
| operator local env loader | RUNTIME_BEHAVIOR | `scripts/_local_env.py` | lines 7-61 | `bootstrap_repo_env` | repository env bootstrap | ACCEPT |
| provider diagnostic builder | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | `ExecutionDiagnostic` and `buildProviderExecutionDiagnostic` | `ExecutionDiagnostic` | execution diagnostic contract | ACCEPT |
| existing live route pattern | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.dlp.live.test.ts` | lines 51-100 | `describe.skipIf`; `POST` | execute route live test | ACCEPT |
| live evidence manifest builder | EXISTS | `scripts/build_cvf_live_evidence_manifest.py` | lines 57-88 | `build_manifest` | live evidence manifest builder | ACCEPT |

## New Doc-Only Fields

The following fields are new evidence-only fields. They are not represented as
pre-existing runtime fields and must not be added to product response schemas:

| Evidence object | New fields | Boundary |
|---|---|---|
| A3 receipt root | `schemaVersion`, `batchId`, `executionBaseHead`, `startedAtUtc`, `finishedAtUtc`, `overall`, `claim` | live evidence only |
| call budget | `plannedCallBudget`, `diagnosticGatedRetryBudget`, `observedCallCount`, `attempts` | call-level accounting only |
| provider proof | `provider`, `model`, `keyAliasUsed`, `httpStatus`, `success`, `latencyMs`, `outputLength` | no raw key/output/payload |
| correlation | `governanceReceiptId`, `envelopeId`, `sot3RecordId`, `sot3IntegrityHash`, `sot3RequestId`, `traceCount`, `packetIds`, `kernelDecisionIds`, `truthReceiptIds`, `truthReferenceIds`, `flowPackageIds` | joins existing IDs without changing owner schemas |
| context observation | `approvedContextHash`, `providerSystemPromptHash`, `approvedContextIncluded`, `providerRequestObserved`, `rawPromptPersisted` | hashes/booleans only |
| secret safety | `rawKeyPersisted`, `rawProviderBodyPersisted`, `rawOutputPersisted`, `fullPromptPersisted` | all must be false |
| diagnostic | `stage`, `class`, `retryable`, `userAction`, `safeMessage`, optional provider/model/status/latency/receipt/trace | copied from canonical diagnostic vocabulary when failure occurs |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact worker paths | all five worker-output paths returned false from `Test-Path` before packet authoring | ACCEPT |
| token search | exact `rg` search for `SOT3-ACT-A3` and `sot3-act-a3-approved-context` returned no pre-existing output | ACCEPT |
| collision decision | create new dated evidence; never overwrite historical receipt or manifest | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | accepted CVF-native SOT3 runtime -> bounded provider proof -> reviewer claim decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SOT3 A3 private live evidence |
| Disposition | verify current runtime behavior without importing external authority |
| Claim boundary | no external knowledge absorption or corpus-completeness claim |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/run_cvf_sot3_a3_live_proof.py` | create a bounded runner using `bootstrap_repo_env`, exact live-test invocation, one-call default, diagnostic-gated retry control, receipt validation, and manifest generation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts` | create controlled real-provider route proof with pass-through fetch observation, actual SOT3/A2 execution, retry-neutralized output validation, and receipt writing only to the explicit runner path |
| `docs/reviews/evidence/sot3-act-a3-approved-context-live-receipt-2026-07-13.json` | generate fresh secret-safe call-level and correlation evidence; never hand-author a PASS without the live test |
| `docs/reviews/evidence/sot3-act-a3-approved-context-live-manifest-2026-07-13.json` | generate with the canonical manifest builder from the receipt |
| `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_WORKER_RETURN_2026-07-13.md` | return exact command, receipt, call-budget, diagnostic, secret-scan, diff, and no-commit evidence |

## Required Artifact Manifest

| Artifact | Required state | Status |
|---|---|---|
| `scripts/run_cvf_sot3_a3_live_proof.py` | runner-only permit and portable launcher | PASS_AFTER_REPAIR |
| `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json` | zero-call local launch diagnostic | PASS |
| `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json` | correlated real-provider PASS receipt | PASS |
| `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json` | receipt hash and rerun manifest | PASS |
| `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` | closed bounded baseline | PASS |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` | closed bounded work order | PASS |
| `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | A3 closed and A4 packet next | PASS |
| `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` | reviewer closure | PASS |

## Required Proof Behavior

The live test must:

1. resolve a real Alibaba key through existing aliases and skip only when the
   runner failed to provide one;
2. create isolated control-plane and A2 store paths under a temporary folder;
3. seed exactly one in-scope collection containing one safe controlled chunk
   with valid SOT3 provenance;
4. set `CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE=ENFORCE`;
5. mock only unrelated auth/quota/enforcement and force output validation to a
   terminal accepted shape so the route cannot auto-retry the provider;
6. wrap `globalThis.fetch` as a pass-through observer, forward with the original
   fetch, count only DashScope calls, inspect the outbound system message in
   memory, and persist no raw message or authorization value;
7. call the real `POST` route once with provider `alibaba` and model
   `qwen-turbo`;
8. assert success, provider/model, one governance receipt, knowledge injection,
   and exactly one provider call;
9. read the A2 record and audit events from fresh readers, prove one full
   acknowledged trace and collect all owner identifiers;
10. verify the observed provider system prompt contains the approved context,
    then write only hashes, booleans, lengths, identifiers, timing, and safe
    diagnostics to the explicit receipt path;
11. restore environment, fetch, stores, and temporary files even on failure.

If the live call fails, the receipt must still be written with `overall=BLOCKED`,
the complete secret-safe diagnostic, observed call count, and no PASS claim.

## Call Budget And Rerun Protocol

| Control | Required behavior |
|---|---|
| planned call | one route invocation and exactly one DashScope request |
| default retry | forbidden |
| diagnostic retry | at most one additional call, only after receipt diagnostic is complete and retryable |
| rerun-changing action | worker return must name the exact change; unchanged broad rerun is forbidden |
| original attempt ceiling | two total DashScope calls; breach retained in the blocked receipt |
| operator recovery override | Alibaba calls numerically unmetered on 2026-07-13; runner-only permit, diagnostic-before-rerun, and diminishing-return controls remain binding |
| denominator | receipt reports call-level attempts and observed provider requests; event counts are separate |

## Execution Plan

1. Capture `executionBaseHead` and clean status; run pre-implementation gate.
2. Generate the worker-return scaffold before other output prose.
3. Implement runner and live test inside the exact manifest.
4. Run non-live focused A2 regression and TypeScript check without a live key.
5. Confirm alias presence secret-safely, then run the A3 runner once.
6. On PASS, generate/validate the manifest and scan all five outputs for secrets.
7. On failure, write diagnostic evidence and stop unless one meaningful retry
   is permitted by the diagnostic.
8. Run worker-return fast gate and return without commit.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 02d7b765c --head HEAD
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/app/api/execute/route-knowledge-context.test.ts src/lib/sot3-knowledge-adapter.test.ts src/lib/sot3-activation-evidence-store.test.ts
npm run check
cd ../../..
python scripts/run_cvf_sot3_a3_live_proof.py --receipt docs/reviews/evidence/sot3-act-a3-approved-context-live-receipt-2026-07-13.json --manifest docs/reviews/evidence/sot3-act-a3-approved-context-live-manifest-2026-07-13.json
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

Do not run the canonical release bundle in A3; that belongs to A5. Do not run
the live command a second time unless the first receipt contains the required
diagnostic and the worker documents the meaningful retry change.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_AT_EXECUTION |
| runtimeMutationAuthorized | PROOF_INSTRUMENTATION_ONLY |
| freshnessVerificationMode | FRESH_LIVE_RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md` proves local durability only |
| requiredFutureAction | generate a new A3 real-provider receipt and manifest from current HEAD |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md`

priorVerificationAnchor: material commit `fdead7c99`

freshRecomputeRequired: yes; A2 local evidence cannot be reused as A3 live proof

unicodePathHandling: use literal repository paths and UTF-8-safe readers; author
new prose and source in ASCII

extractedTextAuthority: N/A with reason: no external extraction or OCR input

## Acceptance Criteria

- [x] exactly five worker outputs and no existing runtime file mutation;
- [x] real Alibaba `qwen-turbo` call succeeds through `/api/execute`;
- [x] original call-ceiling breach is retained, and the separately authorized
  recovery records one successful provider call after diagnostic repair;
- [x] `ENFORCE` provider system message contains Flow-approved context;
- [x] durable record is re-read and correlated with governance receipt ID and
  envelope ID in the A3 receipt;
- [x] full trace identifiers and acknowledged lifecycle are present;
- [x] receipt `overall=PASS` only when all proof assertions pass;
- [x] canonical evidence manifest hash matches the receipt;
- [x] no raw key, bearer header, raw provider body/output, full prompt, or
  source content is committed;
- [x] required local checks, typecheck, fast gate, diff hygiene, and no-commit
  evidence pass.

## Evidence Requirements

- command line and exit status for the focused non-live suite, typecheck, live
  runner, manifest validation, worker-return fast gate, diff, and status;
- call-level count and per-attempt outcome/latency, distinct from audit-event
  counts;
- provider/model and key alias name only;
- governance receipt ID, envelope ID, SOT3 record ID, integrity hash, request
  ID, and all per-trace owner identifiers;
- approved-context and observed-system-prompt hashes plus inclusion boolean;
- complete diagnostic before any retry;
- secret scan over all changed artifacts without printing the key searched.

## Review Gate

The independent reviewer/closer must inspect the pass-through observer,
ensure it forwards a real network call, recompute the receipt/manifest hash,
verify call count and correlation against source evidence, inspect any failure
diagnostic before accepting a retry, rerun non-live checks proportionately, and
refuse any A3 claim based only on mock or checker PASS.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | delegated worker; independent reviewer and designated closer |
| phase | A3 proof implementation, live execution, worker return, reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=02d7b765c; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly five fulfillment-manifest outputs; reviewer-owned closure paths excluded from worker set |
| traceScope(phase, actor) | worker records exact live calls and five-path diff; reviewer recomputes receipt and closure evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; independent reviewer/closer owns material commit |
| crossBatchIsolation | clean dispatch worktree at `02d7b765c`; A2 material/session commits already closed; A4-A5 excluded |
| nextMoveSurfaces | reviewer/session steward updates using the accepted A3 material commit |

Before status evidence: `git status --short` was empty at dispatch base
`02d7b765c`; A2 material `fdead7c99` and session sync `02d7b765c` are committed.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| reviewerOwnedClosurePaths | completion review; paired baseline/work-order status; parent roadmap A3 status; any required governed learning; separate session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Mandatory evidence |
|---|---|---|
| one controlled scoped collection | isolated fixture and tenant session | retrieval and one durable trace |
| READY, eligible receipt/reference, acknowledged Flow | actual SOT3 adapter plus A2 record read | terminal outcome and full owner IDs |
| approved ENFORCE context reaches provider | pass-through DashScope request observer | inclusion boolean and paired hashes |
| one real provider response | existing Alibaba adapter, no executeAI mock | route success and provider/model/call count |
| correlate provider and durable evidence | new evidence-only receipt join | governance receipt/envelope plus SOT3 record/integrity IDs |
| one call plus diagnosed retry | runner hard budget | attempt ledger and diagnostic |
| no output-quality tuning | forced terminal validator for proof isolation | no retry/tuning branch |
| A3 bounded claim only | completion reviewer decision | no A4/A5/final claim |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for the review path and
conditional live content. Use the generated full-profile skeleton and fill all
placeholders. Required section names include Purpose, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, External Knowledge Intake Routing, Rescan
Intelligence Hardening, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Claim
Boundary, git status --short, Changed Files, Command Evidence, and No-Commit
Statement.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_WORKER_RETURN_2026-07-13.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command:
`python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_WORKER_RETURN_2026-07-13.md --title "CVF SOT3 ACT A3 Real Provider Approved Context Proof Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

## Closure Checklist

- [x] execution base and clean status captured before edits;
- [x] five worker outputs only and no forbidden runtime mutation;
- [x] original breach, zero-call launch diagnostic, and recovery call count recorded;
- [x] receipt generated by live execution, not handwritten PASS;
- [x] receipt-manifest hash verified;
- [x] secret safety scan passed;
- [x] focused regression, typecheck, and worker-return fast gate passed;
- [x] worker HEAD remained unchanged until reviewer-owned evidence commit;
- [x] worker returned one terminal disposition.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` when the key remains unavailable after governed
local bootstrap, the provider/policy rejects the call non-retryably, a safe
diagnostic cannot be captured, source changed incompatibly, proof needs a
forbidden path, receipt correlation is ambiguous, a secret may have been
written, or a third call would be needed.

## Operator Checkpoint

Fresh operator approval is required for a third live call, another provider or
model lane, prompt/output tuning, product route or package mutation, A4/A5,
release bundle integration, public-sync, production/scale, or user-value claim.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing CVF Web route live-test family plus root proof runner and review evidence |
| Storage decision | one adjacent test, one runner, one dated receipt, one dated manifest, one worker return |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | A2 local store remains owner; A3 evidence joins IDs without schema mutation |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one bounded real-provider SOT3 approved-context proof |
| claimDisposition | CLAIM_REJECTED: no A3 live result exists at dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker must generate a fresh receipt from the real call |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: packet authoring made no provider call |
| invocationBoundary | one controlled local `/api/execute` invocation through Alibaba `qwen-turbo` |
| interceptionBoundary | pass-through test observation only; no IDE, MCP, CLI, proxy, or mandatory-wrapper enforcement claim |
| claimLanguage | A3 may reach `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` only after reviewer acceptance |
| forbiddenExpansion | no A4/A5, final roadmap claim, release, public, production, scale, universal, or user-value assertion |

## Current Runtime Freshness Claim Boundary

The source verification reflects HEAD `02d7b765c`. Worker must re-run named
symbol searches before editing. A successful live test proves only the selected
scenario and evidence window; it does not ratify unchanged source universally.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private live proof using operator-local credentials. No public-sync or
public capability statement is authorized.

## Claim Boundary

This work order authorizes one A3 proof and five worker outputs. A reviewer may
accept `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` only when the receipt,
manifest, real-call count, context observation, and durable correlation all
pass. The roadmap-final `LIVE_GOVERNANCE_PROVEN_BOUNDED` remains forbidden
until A4 failure/recovery and A5 canonical release proof close.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | `Status: A3_CLOSED_PASS_BOUNDED_A4_PACKET_NEXT` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: A3 does not scan or classify a corpus and has no GC-051 registry ownership | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/README.md` | BLOCKED with reason: A3 does not modify corpus routing and has no registry front-door ownership | BLOCKED with reason |
| External evidence digest | recovery receipt SHA-256 `cec9eb0925e7afaec48b3af92fb55abb0484b92480b2ee5d1987e87a1b40df56` | recomputed PASS; unsigned, no external anchor | PASS |
| System loop interlock | N/A with reason: no automated loop edge added | N/A | N/A with reason |
| Session continuity | separate post-closure session sync | pending closure material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| recovery receipt overall is `PASS` | `$.overall=PASS` | PASS |
| bounded A3 claim is exact | `$.claim=REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` | PASS |
| approved context reached provider | `$.contextObservation.approvedContextIncluded=true` | PASS |
| provider and SOT3 correlation is complete | HTTP 200, one trace, governance IDs, and all layer IDs present | PASS |
| secret persistence flags are false | all four `$.secretSafety` values are false | PASS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A3 --title "SOT3 Activation A3 Real Provider Approved Context Proof" --date 2026-07-13 --base 02d7b765c --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A2 closure fdead7c99 CLOSED_PASS_BOUNDED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact authority, source facts, five outputs, proof behavior, budgets, receipt schema, commands, and boundaries |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, Delta, public, operation-trace, and read-ahead checker sources read |
| docOnlyNewFields | declared in New Doc-Only Fields table |
| claimBoundary | authoring provenance only; no live evidence at dispatch |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher; reviewer/closer amendment |
| Provider or surface | private provenance workspace |
| Session or invocation | SOT3-ACT-A3 dispatch authoring, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | A3 recovery and closure material manifest |
| Allowed scope source | operator A0-A5 authorization, A2 accepted closure, parent roadmap A3 release |
| Before status evidence | clean worktree at `02d7b765c`; planned paths absent |
| After status evidence | source-verified packet plus accepted recovery receipt and bounded closure |
| Diff evidence | `git diff --name-status` before packet commit |
| Approval boundary | A3 packet, bounded repair, recovery, learning, and closure only |
| Claim boundary | `REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` only |
| Agent type | dispatcher |
| Invocation ID | `sot3-act-a3-dispatch-2026-07-13` |
| Expected manifest | `scripts/run_cvf_sot3_a3_live_proof.py`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json`; `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| Actual changed set | `scripts/run_cvf_sot3_a3_live_proof.py`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-launch-diagnostic-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-receipt-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a3-approved-context-live-recovery-manifest-2026-07-13.json`; `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `docs/reviews/CVF_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_COMPLETION_2026-07-13.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
