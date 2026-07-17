# CVF Agent Work Order - SOT3-APP-T5 Operational Live Provider Proof

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: SOT3-APP-T5

dispatchBaseHead: `1bd039a07`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated implementation worker

Reviewer/closer: independent reviewer/designated closer

workerReturnPath: `docs/reviews/CVF_SOT3_APP_T5_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for SOT3-APP-T5.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T5_OPERATIONAL_LIVE_PROVIDER_PROOF_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture with `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-18. The operator authorized using
root CVF live keys for the sibling app test, but only by process environment.

Do-not-misread notes: one attempted live provider call maximum, zero retries,
no raw key persistence, no raw provider payload persistence, no browser/UI,
no public-sync, no production, and no worker commit.

Required first actions: read startup front doors, active handoff, paired
GC-018 baseline, this work order, cited sources and guards; capture
executionBaseHead and clean status; confirm key alias presence without printing
values.

Return contract: leave all changes uncommitted and unstaged, then return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement and execute one bounded operational live-provider proof for the
sibling SOT Application by placing provider execution behind the app's existing
`GovernedExecutionAdapter` boundary and using root CVF API keys only as process
environment for the one live command.

## Authority Chain

Operator T5 live/key authorization on 2026-07-18 -> SOT3-APP roadmap T5 lane ->
paired T5 GC-018 baseline -> this work order.

## Agent Roles

- Worker implements, tests, runs one live attempt, records evidence, and does
  not stage or commit.
- Independent reviewer recomputes tests, live receipt safety, changed set, and
  one-call/no-retry evidence.
- Designated closer owns material commit and completion review.
- Session-sync steward updates protected continuity only after accepted
  material commit.

## Required First Reads

`CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; active
handoff; `docs/reference/guard_orientation/README.md`;
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
paired baseline; this packet; and every source in the Source Verification
Block.

## Pre-Flight Checks

Capture `executionBaseHead`; require clean post-dispatch HEAD and no staged or
unstaged paths in the CVF root. Inspect sibling source status by filesystem
diff/listing only because the sibling root is not a Git repository. Confirm
root key alias presence without value output.

## Write Ownership

Exactly five fulfillment paths are authorized. Reviewer completion, roadmap,
session state, CVF generated registries, public artifacts, browser/UI, and
production files are forbidden to the worker.

## Evidence Requirements

Record executionBaseHead, clean before status, key alias presence with
PRESENT_REDACTED only, focused fake-fetch tests, typecheck/build command
results, exactly one live-attempt ledger, zero retries, sanitized provider/model
metadata, latency, usage when returned, raw-response hash, output identifiers,
diagnostic if failed, redaction scan, worker-return fast gate, changed-set
evidence, and no-commit statement.

## Target / Source

Target root: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`.

Use the existing T4 controlled quotation source-to-freeze concept as the
application scenario, but replace the local deterministic execution port with a
minimal live provider execution port only after the context decision is `ALLOW`.
The live prompt must be short, source-bounded, and instruct the model to draft a
commercial quotation summary from the governed record IDs supplied by the app
context.

## Scope / Target / Owner Boundary

The sibling app currently has no valid provider/live adapter. The worker may
create one minimal adapter behind `GovernedExecutionAdapter` and a one-call
runner to exercise `GovernedOutputService.create`. The adapter must not bypass
route decision checks, must not run for non-`ALLOW` contexts, and must not
expose raw provider access outside the single runner and tests.

## Operator Checkpoint

Satisfied for this packet only: the operator authorized taking live API keys
from the CVF root and passing them to the sibling app live test. Any second
call, retry, provider/model expansion, public-sync, production use, copied key
file, or broader adapter owner returns to the operator.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | add and prove one bounded sibling live-provider execution path |
| scopeClassification | bounded runtime/provider/live proof |
| riskSensitivity | R2 |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | no-commit worker, independent reviewer/closer, session steward |
| escalationCondition | missing key, source contradiction, secret exposure, extra call need, or forbidden path need |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | source verification -> bounded live proof -> reviewer recomputation -> closure decision |
| Matching local-view guard | `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | paired baseline and this work order |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch; worker may produce proof evidence |
| Claim boundary | no web search, provider-local memory, or copied benchmark authority |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T4 accepted closure | material commit `1f815d7f5`; `docs/reviews/CVF_SOT3_APP_T4_COMPLETION_REVIEW_2026-07-17.md` | T4 must be accepted before T5 | ACCEPT |
| protected continuity | current dispatch base `1bd039a07` | active state must release T5 packet authoring | ACCEPT |
| operator live/key authorization | operator message on 2026-07-18 authorizes root keys for test process env | required before live packet | ACCEPT_BOUNDED_ONE_CALL |
| root key source | `AGENTS.md` operator-key continuity note and redacted local presence check | key may be used but not printed or persisted | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| packetKind | `runtime-provider-live` |
| scaffoldBase | `1bd039a07` |
| scaffoldDisposition | completed against current sources and checkers |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-APP-T5 --title "Operational Live Provider Proof" --date 2026-07-18 --base 1bd039a07 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-APP-T4 accepted closure 1f815d7f5" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact sibling path scope, key-transfer control, adapter manifest, live diagnostic, and worker-return shape |
| checkerReadAheadConfirmation | applicable checker sources and guard orientation were read before final packet text |
| docOnlyNewFields | `SOT3_APP_T5_LIVE_PROOF_PASS`; `SOT3_APP_T5_LIVE_PROOF_BLOCKED` |
| claimBoundary | scaffold provenance does not prove execution or live results |

## Worker Autonomy / No-Question Rule

Resolve implementation details inside the five-path scope. Stop only for a
missing key, source contradiction, secret-safety failure, forbidden-scope need,
or need for any second call or retry. Do not ask the operator for routine
test/typecheck or checker repairs inside allowed scope.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`SOT downstream application live provider proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "SOT downstream application live provider proof" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF controls beyond standard live, handoff, and worker-return gates |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Current Runtime Freshness Verification; Runtime Expansion Control Block; Live Key Transfer Control Block; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm the T5 live packet is source-faithful before worker execution |
| claimBoundary | validation is not live-result evidence |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T5 roadmap lane | EXISTS | `docs/roadmaps/CVF_SOT3_DOWNSTREAM_APPLICATION_ROADMAP_2026-07-15.md` | Work Plan row for SOT3-APP-T5 | `SOT3-APP-T5` | SOT3-APP roadmap | ACCEPT |
| T4 release for T5 | EXISTS | `docs/reviews/CVF_SOT3_APP_T4_COMPLETION_REVIEW_2026-07-17.md` | completion review status and T5 next route | `CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | T4 completion review | ACCEPT |
| mandatory live proof rule | EXISTS | `AGENTS.md` | Mandatory Live Governance Proof | `python scripts/run_cvf_release_gate_bundle.py --json` | CVF root agent instructions | ACCEPT |
| root key continuity rule | EXISTS | `AGENTS.md` | Operator-key continuity note | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` | CVF root agent instructions | ACCEPT |
| root key aliases present locally | RUNTIME_BEHAVIOR | `CANONICAL_CONTRACT: redacted local existence check; root cvf-web .env.local` | `ALIBABA_API_KEY`, `DASHSCOPE_API_KEY`, and `DEEPSEEK_API_KEY` present without value output | API key alias presence | local operator environment | ACCEPT |
| sibling provider default disabled | VALUE_SET | `CANONICAL_CONTRACT: external sibling direct-read evidence; .env.example` | `CVF_PROVIDER_CALLS_ENABLED=false` | `CVF_PROVIDER_CALLS_ENABLED` | SOT Application config | ACCEPT |
| direct provider bypass forbidden | EXISTS | `CANONICAL_CONTRACT: external sibling direct-read evidence; AGENTS.md` | Do not call providers directly | provider call boundary | SOT Application local instructions | ACCEPT |
| live provider use boundary | EXISTS | `CANONICAL_CONTRACT: external sibling direct-read evidence - LOCAL_FIRST_OPERATIONS_DOC` | live provider use is explicit, approved, budget-bounded, and separately evidenced | live provider use | SOT Application operations docs | ACCEPT |
| governed execution port | EXISTS | `CANONICAL_CONTRACT: external sibling direct-read evidence; packages/cvf-bindings/src/governed-execution.adapter.ts` | `GovernedExecutionPort.execute` | `GovernedExecutionPort` | SOT Application CVF bindings | ACCEPT |
| governed execution adapter | RUNTIME_BEHAVIOR | `CANONICAL_CONTRACT: external sibling direct-read evidence; packages/cvf-bindings/src/governed-execution.adapter.ts` | adapter fail-closes without port or context IDs and delegates to port | `GovernedExecutionAdapter.execute` | SOT Application CVF bindings | ACCEPT |
| output service execution call | RUNTIME_BEHAVIOR | `CANONICAL_CONTRACT: external sibling direct-read evidence; packages/application/src/services/governed-output.service.ts` | calls execution after `context.route_decision` check | `GovernedOutputService.create` | SOT Application application service | ACCEPT |
| Model Gateway live harness pattern | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `runLiveProof`; `createOpenAiCompatibleExecuteAdapter` | `runLiveProof` | Model Gateway live proof harness | ACCEPT |
| DashScope endpoint owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | endpoint constants and resolver | `resolveAlibabaDashScopeEndpoint` | Model Gateway Alibaba ledger | ACCEPT |
| usable default model | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | `qwen3.7-plus` entry with expiration 2026-08-31 | `qwen3.7-plus` | Model Gateway Alibaba ledger | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `SOT3_APP_T5_LIVE_PROOF_PASS` | reviewer token if bounded live proof is accepted | NONE_AT_DISPATCH |
| `SOT3_APP_T5_LIVE_PROOF_BLOCKED` | reviewer token if proof is blocked or rejected | NONE_AT_DISPATCH |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | YES_BOUNDED |
| freshnessVerificationMode | current source verification plus one new live attempt |
| requiredExecutionBase | clean post-dispatch HEAD captured by worker |
| staleEvidenceRule | prior local receipts and root live receipts cannot satisfy T5 |

## Negative Search And Collision Discipline

Before creating files, search for the proposed adapter, runner, evidence, and
worker-return basenames. If an exact owner exists, stop and report collision.
Do not duplicate provider or credential ownership.

## Evidence Reuse And Encoding Plan

Reuse the existing sibling adapter abstraction and root Model Gateway protocol
pattern. Do not reuse prior live results. Write ASCII. Persist only sanitized
content, provider/model metadata, usage counts when returned, latency, raw
response hash, diagnostic, command evidence, and no-commit evidence.

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | minimal sibling live execution adapter plus one runner |
| providerOwner | sibling adapter behind `GovernedExecutionAdapter`; protocol based on Model Gateway harness |
| callBudget | one attempted provider call maximum |
| retryBudget | zero |
| governedComparison | forbidden |
| persistentRuntimeState | N/A with reason: evidence JSON only |

## Live Key Transfer Control Block

| Field | Value |
|---|---|
| sourceKeyLocation | root CVF `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` |
| transferMode | process environment only for the live command |
| allowedAliases | `DASHSCOPE_API_KEY`; `ALIBABA_API_KEY`; `CVF_ALIBABA_API_KEY`; `CVF_BENCHMARK_ALIBABA_KEY`; `DEEPSEEK_API_KEY` |
| allowedPresenceEvidence | key alias names and PRESENT_REDACTED only |
| forbiddenEvidence | raw key values, authorization headers, copied `.env.local`, raw request payload, raw response payload |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| siblingRoot | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application` |
| adapterPlacement | `packages/cvf-bindings/src/live-provider-governed-execution.adapter.ts` |
| barrelPlacement | `packages/cvf-bindings/src/index.ts` |
| testPlacement | `tests/e2e/live-governed-output.e2e.test.ts` |
| runnerPlacement | `scripts/run-live-governed-output.ts` |
| evidencePlacement | CVF root `docs/reviews/evidence/sot3-app-t5-live-provider-proof-2026-07-18.json` |
| duplicateOwnerCheck | required before create |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Closure evidence |
|---|---|---|
| optional operational/live proof | one authorized provider-call attempt | evidence JSON and worker return |
| separately authorized real provider evidence | operator key authorization and root env transfer control | reviewer accepts or rejects receipt |
| exact bounded claim only | one-call/no-retry/no-production boundaries | completion review |
| identifier/evidence/replay boundaries | source IDs, context ID, output ID, content hash, receipt ID | sanitized evidence JSON |
| no universal SOT3 inference | claim boundary excludes production/public/universal proof | closure claim boundary |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\live-provider-governed-execution.adapter.ts` | create minimal DashScope-compatible governed execution port with injected fetch for tests and secret-safe diagnostics |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\packages\cvf-bindings\src\index.ts` | export the new adapter without breaking existing exports |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\tests\e2e\live-governed-output.e2e.test.ts` | create fake-fetch tests for ALLOW path, blocked context no-call path, missing-key diagnostic, provider-error diagnostic, and secret redaction |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application\scripts\run-live-governed-output.ts` | create one-call runner that loads root key aliases into process env without printing values and invokes the app service chain |
| `docs/reviews/evidence/sot3-app-t5-live-provider-proof-2026-07-18.json` | write sanitized live receipt or diagnostic evidence |
| `docs/reviews/CVF_SOT3_APP_T5_WORKER_RETURN_2026-07-18.md` | write full no-commit worker return with exact command/status evidence |

## Required Artifact Manifest

| Artifact group | Owner | Required final status |
|---|---|---|
| five fulfillment paths plus worker return | worker | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON |
| completion review | reviewer/closer | REVIEWER_TO_DECIDE |
| roadmap and continuity | reviewer/session steward | REVIEWER_TO_DECIDE |

## Execution Plan

1. Capture executionBaseHead and clean status.
2. Confirm key alias presence from root `.env.local` without printing values.
3. Add the minimal adapter and fake-fetch tests.
4. Run focused tests and typecheck/build commands needed for confidence.
5. Run exactly one live attempt through the one-call runner.
6. Persist sanitized evidence JSON and worker return.
7. Run required gates and leave all changes uncommitted and unstaged.

## Required Behavior

The adapter must accept injected fetch for tests, resolve keys only at runtime,
support the DashScope-compatible chat-completions shape, return the
`GovernedExecutionPort` result shape, classify missing key, endpoint, provider,
transport, malformed-output, and timeout failures, and never expose raw
credentials. The runner must fail closed if `CVF_PROVIDER_CALLS_ENABLED` is not
set to `true` for the live process.

## Focused Test Matrix

| Case | Expected result |
|---|---|
| ALLOW context with fake provider output | execution returns governed result and one fetch call |
| BLOCK or non-continuable context | no provider fetch is called |
| missing key | secret-safe diagnostic and no raw key output |
| provider error status | diagnostic includes status and safe class, not raw body |
| malformed output | fail-closed diagnostic |
| redaction scan | serialized evidence contains no key aliases as values and no authorization header |

## Mandatory Live Run Diagnostic Block

On failed, partial, timed-out, or empty call, record a secret-safe diagnostic
with stage, class, retryability, user action, provider/model when known, HTTP
status/latency when available, receipt/trace when available, and safe message.
Do not retry. Separate call-level result from event denominator.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_APP_T5_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; External Knowledge Intake Routing; Corpus Completeness And Report Integrity; Rescan Intelligence Hardening; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package; Public Export Disposition; Claim Boundary; git status --short; Changed Files; Command Evidence; No-Commit Statement.

Required fields: executionBaseHead; git status --short.

Return includes exact status/diff, fulfillment manifest, call ledger, tests,
gates, secret scan, diagnostic/result, no-commit proof, and one terminal token.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker, independent reviewer/designated closer, session-sync steward |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=1bd039a07; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly five fulfillment paths plus worker return |
| traceScope(phase, actor) | worker call receipt/diagnostic; reviewer recomputation; closer commit; steward continuity |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | T4 closure `1f815d7f5`; dispatch base `1bd039a07`; later lanes parked |
| Before status evidence | clean worktree at `1bd039a07`; `git status --short` produced no output before authoring |
| nextMoveSurfaces | reviewer/session steward only from accepted material commit |

Before status evidence: clean worktree at `1bd039a07`; `git status --short`
produced no output before authoring; no pending paths before worker execution.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` |
| reviewerOwnedClosurePaths | completion review, baseline/work-order disposition updates, roadmap disposition, and any disclosed narrow repair |
| closureOwner | independent reviewer/designated closer |
| workerCommitPermission | FORBIDDEN |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker |
| Provider or surface | local filesystem, sibling app, one DashScope-compatible provider attempt |
| Session or invocation | SOT3-APP-T5 Operational Live Provider Proof, 2026-07-18 |
| Working directory | CVF root plus sibling SOT Application root |
| Command or tool surface | PowerShell, pnpm/tsx/vitest, Python governance gates |
| Target paths | five fulfillment paths plus worker return |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | clean worktree at `1bd039a07`; `git status --short` produced no output before authoring |
| After status evidence | worker must paste `git status --short` |
| Diff evidence | `git diff --name-status` plus external sibling path listing |
| Approval boundary | operator one-call key authorization only |
| Claim boundary | bounded live proof attempt only |
| Agent type | external delegated worker |
| Invocation ID | `sot3-app-t5-2026-07-18` |
| Expected manifest | five fulfillment paths plus worker return |
| Actual changed set | worker to fill |
| Manifest delta | worker to fill |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one sibling application live-provider proof attempt |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE required from worker and reviewer |
| receiptEvidence | CVF_RECEIPT_PRESENT required through sanitized evidence JSON plus worker return |
| actionEvidence | ACTION_EVIDENCE_PRESENT required through focused tests, one-call runner output, and no-commit status |
| invocationBoundary | manual local command invocation only |
| interceptionBoundary | no universal wrapper, proxy enforcement, or arbitrary agent-command interception claim |
| claimLanguage | bounded SOT Application live proof, not production certification |
| forbiddenExpansion | runtime/provider/live beyond one call, public-sync, UI/browser, production, queue/daemon, or CVF Core mutation |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | sibling copied-folder application |
| Upstream or source-mirror disposition | retained local operator-authored sibling root |
| Enumeration or manifest plan | T5 does not re-enumerate the full corpus; it consumes accepted T0B/T4 evidence plus current targeted source reads |
| Per-file terminal-ledger plan | N/A with reason: no full-corpus semantic ledger mutation |
| Owner or overlap route | SOT Application local adapter behind current binding abstraction |
| Value-disposition route | runtime proof only |
| Claim boundary | targeted live proof; no new full-corpus absorption claim |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | operator-named sibling copied-folder application |
| Control disposition | APPLICABLE_BOUNDED |
| Corpus completeness section | PRESENT_WITH_NA_REASON |
| Completeness trigger model | no full-corpus claim; targeted files are listed in fulfillment manifest |
| Blind-spot prevention action | exact allowed path manifest, collision search, and reviewer recomputation |
| Residual gap | full product readiness and UI/public behavior remain unproven |
| Blind-spot verdict | T5_TARGETED_SCOPE_ONLY |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - T5 is a targeted live proof over
  six named fulfillment artifacts, not a full-corpus intake or rescan. Accepted
  T0B corpus evidence remains unchanged.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the sibling app can produce one governed output
through a real provider only after a minimal adapter is added behind the
existing execution boundary.

Evidence Comparison Requirement: compare local fake-fetch tests, live receipt
or diagnostic, call count, redaction scan, output identifiers, and route
decision evidence.

Contradiction Handling Requirement: missing key, unsupported model, provider
failure, malformed output, or adapter source conflict is a valid
`BLOCKED_WITH_REASON`; do not retry.

Claim Update Requirement: reviewer records `SOT3_APP_T5_LIVE_PROOF_PASS` or
`SOT3_APP_T5_LIVE_PROOF_BLOCKED`.

## Verification Commands

```powershell
cd "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application"
pnpm vitest run tests/e2e/live-governed-output.e2e.test.ts
pnpm -r typecheck
pnpm -r build
$env:CVF_PROVIDER_CALLS_ENABLED="true"
pnpm tsx scripts/run-live-governed-output.ts
cd "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF"
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short
git diff --cached --name-only
git rev-parse --short HEAD
```

Worker may add a secret-safe pre-command that reads root `.env.local` and sets
process env variables without outputting values. Do not paste raw key values
into command evidence.

## Acceptance Criteria

- [x] dependency evidence current at dispatch;
- [x] operator live/key checkpoint recorded;
- [x] exact allowed worker manifest declared;
- [x] one provider-call attempt maximum and zero retries required;
- [x] root key transfer limited to process environment;
- [x] worker commit forbidden;
- [x] reviewer closure conversion declared.

## Review Gate

Reviewer independently verifies changed set, redaction safety, call count,
diagnostic/result classification, tests, typecheck/build, worker-return fast
gate, and no-commit evidence. A worker-authored PASS token is not accepted
without reviewer recomputation.

## Closure Diff Gate

Compare roadmap, baseline, work order, five fulfillment artifacts, evidence
JSON, worker return, command output, and claims. Missing fields, ambiguous
thresholds, stale sources, extra calls/paths, raw secrets, raw provider payloads,
or overclaims fail closure.

## Closure Checklist

- [x] dependency release evidence refreshed;
- [x] dispatch base captured;
- [x] exact worker scope declared;
- [x] live diagnostic requirement included;
- [x] public export disposition private-only;
- [x] reviewer-owned closure required;
- [x] protected session continuity excluded from worker scope.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before any live call if key presence cannot be
confirmed, the sibling source contradicts the adapter boundary, a required
path already has a conflicting owner, or secret safety cannot be guaranteed.
Return `BLOCKED_WITH_REASON` after at most one live attempt if provider,
network, endpoint, model, timeout, or malformed-output failure occurs. Do not
retry.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: DISPATCH_READY` | READY |
| Worker return | `docs/reviews/CVF_SOT3_APP_T5_WORKER_RETURN_2026-07-18.md` | worker to create | PENDING_WORKER |
| Evidence JSON | `docs/reviews/evidence/sot3-app-t5-live-provider-proof-2026-07-18.json` | worker to create | PENDING_WORKER |
| Completion review | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` | reviewer-owned | PENDING_REVIEW |
| Registry JSON | N/A with reason: no generated registry mutation authorized for worker | no registry mutation | N/A with reason |
| Session continuity | N/A with reason: session steward owns protected sync after material commit | no worker state mutation | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling application live proof; public-sync is not authorized.

## Claim Boundary

This work order authorizes one no-commit worker to add and execute a bounded
sibling SOT Application live-provider proof using root CVF keys as process
environment only. It does not certify production, public, browser/UI, queue,
daemon, or universal SOT3 behavior and does not release any later tranche.
