# CVF GC-018 Baseline - SOT3 Activation A3 Real Provider Approved Context Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: SOT3-ACT-A3

Date: 2026-07-13

Dispatch base head: `02d7b765c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: Codex reviewer/closer

Worker target: delegated implementation and live-proof worker

## Purpose

Authorize one bounded A3 proof that a real Alibaba DashScope-compatible
provider call receives only SOT3 Flow-approved knowledge context in ENFORCE
mode and that the provider result is correlated with the durable A2 record.

## Authorization / Decision

The operator authorized the A0-A5 activation sequence and instructed continued
execution. A2 closed at material commit `fdead7c99`; the parent roadmap now
names fresh A3 packet authoring as the only next move. This baseline authorizes
the exact A3 worker manifest below after dispatch gates pass.

## Baseline / Proposed Tranche

Baseline: A2 proves durable local evidence and replay, but no current artifact
proves that a real provider received the Flow-approved context. Proposed
tranche A3 adds proof-only instrumentation, one bounded live call, and one
correlated receipt plus manifest without changing product owners.

## Scope / Target / Owner Boundary

Target: one controlled CVF Web `/api/execute` invocation using one tenant-scoped
knowledge collection, SOT3 `ENFORCE`, the existing Alibaba provider adapter,
and one secret-safe correlated live receipt.

Owner boundary: retrieval retains tenant scope; Refinery, Kernel, and Flow keep
their existing authority; CVF Web invokes the provider downstream. The worker
may add proof instrumentation and evidence only. No product route, package,
provider adapter, governance policy, or durable-store schema mutation is
authorized.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A2 durable evidence closure | `docs/reviews/CVF_SOT3_ACT_A2_DURABLE_ACTIVATION_EVIDENCE_COMPLETION_2026-07-13.md`; material commit `fdead7c99`; `Status: CLOSED_PASS_BOUNDED`; claim `DURABLE_EVIDENCE_REPLAY_PROVEN_LOCAL` | accepted durable restart and integrity evidence exists before provider quota is spent | ACCEPT |
| A3 roadmap release | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; `Status: A2_CLOSED_PASS_BOUNDED_A3_PACKET_NEXT`; A3 Detailed Design | fresh source-verified packet is required | ACCEPT |
| Operator live-proof authority | operator instruction to execute A0 then A1-A5 toward `LIVE_GOVERNANCE_PROVEN_BOUNDED`, renewed by `tiep tuc` on 2026-07-13 | A3 remains within one planned call plus one diagnostic-gated retry | ACCEPT |

## Risk Classification

Risk: R2 live proof.

Reason: a real provider call consumes operator quota and observes a controlled
prompt, while no product runtime owner or public surface is changed.

## Allowed Scope

- create one SOT3-specific Alibaba live test adjacent to the execute route;
- create one Python runner that bootstraps local keys without printing values,
  invokes the exact live test, and validates the generated receipt;
- produce one new secret-safe receipt and one live-evidence hash manifest;
- produce one checker-safe no-commit worker return;
- use one planned provider call and at most one diagnostic-gated retry;
- run focused live/non-live checks, typecheck, build only if source behavior
  changes, worker-return fast gate, and secret scans.

## Forbidden Scope

- no edit to `route.ts`, route helpers, SOT3 packages, provider adapters,
  durable store, governance receipt schema, release bundle, or public-sync;
- no mock provider result, saved-response substitution, prompt tuning, output
  quality scoring, provider comparison, or broad rerun campaign;
- no raw key, raw provider request body, full system prompt, or raw provider
  response in committed evidence;
- no A4 negative/recovery cases or A5 release-gate integration;
- no production, distributed durability, public, universal, or user-value claim.

## Call Budget And Stop Rule

The runner and receipt must show `plannedCallBudget=1`,
`diagnosticGatedRetryBudget=1`, and the observed call count. The live test must
neutralize route output-validation retry so one invocation cannot silently
spend multiple calls. Any failed or partial call requires the standard
secret-safe diagnostic before a retry. No third call is authorized.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A3 --title "SOT3 Activation A3 Real Provider Approved Context Proof" --date 2026-07-13 --base 02d7b765c --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A2 closure fdead7c99 CLOSED_PASS_BOUNDED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with A2 release evidence, verified symbols, exact manifest, live budget, diagnostics, and boundaries |
| checkerReadAheadConfirmation | dispatch, handoff, worker-return, Delta claim, public export, operation trace, and checker-read-ahead sources read |
| docOnlyNewFields | fields in the A3 evidence receipt are declared in the paired work order New Doc-Only Fields table |
| claimBoundary | authoring provenance only; no live result exists at dispatch |

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
| Dispatch impact | no additional ADIF-specific control beyond the mandatory packet controls |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirmation and evidence after source verification; not first discovery |
| claimBoundary | checker compliance cannot substitute for the real provider call or expand A3 scope |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| A2 durable store schema and lookup | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-activation-evidence-store.ts` | lines 42, 278, 356 | `SOT3_ACTIVATION_EVIDENCE_SCHEMA_VERSION`; `Sot3ActivationEvidenceStore`; `findByRecordId` | A2 evidence store | ACCEPT |
| SOT3 activation precedes prompt construction | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | lines 270-358 | `resolveKnowledgeContext` | `KnowledgeContextResult` | ACCEPT |
| execute route calls provider after knowledge resolution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 686-741 | `POST` | execute route | ACCEPT |
| final response emits governance receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 74, 147-169 | `buildExecuteFinalResponse` | Web governance evidence receipt | ACCEPT |
| Alibaba key alias resolver | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | lines 1-18 | `resolveAlibabaApiKey` | Alibaba environment boundary | ACCEPT |
| repository local env bootstrap | RUNTIME_BEHAVIOR | `scripts/_local_env.py` | lines 7-61 | `bootstrap_repo_env` | secret-safe local environment loader | ACCEPT |
| live test route pattern | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.dlp.live.test.ts` | lines 51-100 | `describe.skipIf`; `POST` | existing execute-route live test pattern | ACCEPT |
| diagnostic schema | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | `ExecutionDiagnostic` interface | `ExecutionDiagnostic` | execution diagnostic contract | ACCEPT |
| live manifest builder | EXISTS | `scripts/build_cvf_live_evidence_manifest.py` | lines 57-88 | `build_manifest` | live evidence manifest builder | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned path existence | `Test-Path` returned false for all six baseline/work-order and worker-output paths before authoring | ACCEPT |
| token collision | `rg -n "SOT3-ACT-A3|sot3-act-a3-approved-context" docs CVF_SESSION EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute` returned no pre-existing artifact | ACCEPT |
| collision decision | create new A3-specific paths; do not overwrite historical live evidence | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_AT_WORKER_EXECUTION_ONLY |
| runtimeMutationAuthorized | PROOF_INSTRUMENTATION_ONLY |
| freshnessVerificationMode | FRESH_LIVE_RECOMPUTE_REQUIRED |
| priorVerificationArtifact | A2 completion establishes local durability only and is not reused as live proof |
| requiredFutureAction | run the new A3 test through a real DashScope-compatible provider and generate a new receipt plus manifest |

## Acceptance Criteria

- one scoped collection produces a READY Refinery packet, eligible Kernel
  decision/receipt/reference, and acknowledged Flow package;
- `ENFORCE` injects approved context and one real Alibaba response succeeds;
- provider request observation proves approved-context inclusion without
  persisting raw prompt or key;
- receipt correlates the route governance receipt ID and envelope ID with one
  durable SOT3 record ID and its full trace identifier chain;
- receipt reports exactly one call, or at most two only when the first has a
  complete diagnostic and the rerun-changing action is recorded;
- receipt and manifest contain no raw secret, raw provider body, full prompt,
  or unredacted response;
- worker changes only the exact fulfillment manifest and does not commit.

## Verification / Evidence

Required verification is one fresh live receipt generated by the bounded A3
runner, its canonical hash manifest, exact provider-call accounting, durable
record correlation, safe diagnostics for any failure, focused local regression,
TypeScript check, secret scan, worker-return fast gate, diff, and clean no-commit
handoff evidence.

## Stop Conditions

- no compatible live key is available after checking the governed local env;
- a source symbol or predecessor claim no longer matches current source;
- proof requires product route, provider adapter, SOT3 package/store, release
  runner, governance schema, or public-sync mutation;
- the first call fails without a complete diagnostic;
- a third call, prompt-tuning branch, or provider substitution is proposed;
- secret-safe correlation cannot be produced without storing raw content.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: A3 uses operator-local live credentials and private provenance evidence.
No public-sync action or public capability claim is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` | `Status: DISPATCH_READY` | N/A with reason: A3 is dispatched, not closed |
| Completion or reviewer artifact | N/A with reason: reviewer-owned completion does not exist at dispatch | worker must first return live evidence | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | `Status: A2_CLOSED_PASS_BOUNDED_A3_PACKET_NEXT`; A3 is the open next tranche | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: A3 does not scan or classify a corpus and has no GC-051 registry ownership | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/README.md` | BLOCKED with reason: A3 does not scan or classify a corpus and has no registry front-door ownership | BLOCKED with reason |
| External evidence digest | N/A with reason: fresh live receipt is a worker output | pending worker execution | N/A with reason |
| System loop interlock | N/A with reason: no automated loop edge is changed | no interlock mutation | N/A with reason |
| Session continuity | separate post-dispatch session sync | pending packet material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| A2 prerequisite is accepted before live quota | material commit `fdead7c99` and bounded A2 completion exist | PASS |
| A3 receipt is fresh rather than reused | no A3 receipt or manifest exists at dispatch; worker must generate both | PASS |
| dispatch makes no live result claim | current claim remains `DURABLE_EVIDENCE_REPLAY_PROVEN_LOCAL` | PASS |

## Claim Boundary

This baseline authorizes one private, bounded real-provider happy-path proof for
the selected CVF Web knowledge-context seam. Even a PASS may claim only
`REAL_PROVIDER_APPROVED_CONTEXT_PROVEN_BOUNDED` for A3. It cannot claim the
roadmap-final `LIVE_GOVERNANCE_PROVEN_BOUNDED`, which still requires A4 and A5.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | SOT3-ACT-A3 dispatch authoring, 2026-07-13 |
| Working directory | repository root |
| Command or tool surface | startup reads, source search, scaffold helper, checker reads, apply_patch, gates |
| Target paths | paired A3 baseline and work order |
| Allowed scope source | operator A0-A5 authorization, A2 closure, and parent roadmap A3 next move |
| Before status evidence | clean worktree at `02d7b765c`; all planned paths absent |
| After status evidence | source-verified A3 dispatch packet only |
| Diff evidence | `git diff --name-status` before packet commit |
| Approval boundary | A3 packet authoring and dispatch only |
| Claim boundary | no provider call or A3 result at dispatch |
| Agent type | dispatcher |
| Invocation ID | `sot3-act-a3-dispatch-2026-07-13` |
| Expected manifest | `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` |
| Actual changed set | `docs/baselines/CVF_GC018_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A3_REAL_PROVIDER_APPROVED_CONTEXT_PROOF_2026-07-13.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
