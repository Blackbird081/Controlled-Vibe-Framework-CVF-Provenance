# CVF Agent Work Order - CADP-AI-T6 Live Compatibility Proof

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-15

Batch ID: CADP-AI-T6

## Dispatch Prompt Envelope

Role: live-proof worker. Independent reviewer/closer is later.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_2026-08-15.md
Commit mode: WORKER_MUST_NOT_COMMIT
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
Current-time notes: operator authorized a bounded provider API test on 2026-08-15 (at most 3 calls, US$1 total, DashScope-compatible primary). The live run is allowed only after the independent reviewer accepts this packet.
Do-not-misread notes: this packet does not authorize production mutation, deployment, public sync, T5 adapter implementation, MCP/CLI invocation, or any production, universal-provider, trusted-evidence, or cross-runtime readiness claim. The dispatch author ran no API call and disclosed no secret; local checks evaluated presence status only.
Required first actions: capture HEAD and status; read startup surfaces, guard orientation, literal gotchas, the paired baseline, this packet, and every checker source named in the Checker Source Read-Ahead Block; record a secret-safe diagnostic precheck before the first live run.
Return contract: create the worker return and secret-safe evidence JSONs at the exact governed paths; leave staging empty and HEAD unchanged; return COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED_WITH_REASON.

dispatchBaseHead: `1719e53cdb56de9d17180dd3a389585802b4b8ae`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute one bounded live compatibility proof for CADP-AI-T6 by running the
repository release gate bundle with real DashScope-compatible credentials
loaded by reference, synthetic non-sensitive input, a strict call and cost
ceiling, and secret-safe evidence capture. The worker produces evidence only;
it commits nothing.

completionReviewPath: `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_COMPLETION_2026-08-15.md`
roadmapPath: `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`
reviewerOwnedClosurePaths: completion review (optional); CADP roadmap T6 row
projection; separate session continuity. The worker owns none of these.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id CADP-AI-T6 --title "CADP AI T6 Bounded Live Compatibility Proof" --date 2026-08-15 --base 1719e53cdb56de9d17180dd3a389585802b4b8ae --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | dispatch, source verification, agent handoff contract, reviewer closure conversion, worker return shape, trace, delta block, public disposition, claim boundary |
| manualEditsAfterScaffold | bound T6 live-proof semantics, operator authorization scope, provider/model selection, call/cost ceiling, secret handling, evidence paths, diagnostic/retry protocol |
| checkerReadAheadConfirmation | checker sources listed in the paired baseline read-ahead block were read before authoring |
| docOnlyNewFields | `sot3CanonicalPath`; `e2eLiveSupplementarySurface`; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no live, runtime, provider, public-sync, or production behavior is implemented |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification | State |
|---|---|---|---|---|
| T6 credentials | Secret Handling; Provider And Model Selection Rule | `.env.local` key-alias presence status | secret-safe precheck | MAPPED |
| T6 cost ceiling | Cost And Call Ceiling | US$1 total | operator authorization | MAPPED |
| T6 call ceiling | Cost And Call Ceiling | at most 3 provider API calls | call ledger in worker return | MAPPED |
| T6 sandbox | Synthetic Input And Data Retention Boundary | synthetic non-sensitive input | worker return | MAPPED |
| T6 live diagnostic | Diagnostic And Retry Protocol | secret-safe diagnostic fields | evidence paths | MAPPED |
| T6 release work order | this packet | bounded live-proof execution | paired baseline | MAPPED |
| T6 exit: real provider evidence, no mocks | Required Live-Proof Execution; Acceptance Criteria | result JSON and manifest | worker return | MAPPED |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `docs/reference/guard_orientation/README.md`
4. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
5. `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`
6. `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
7. `scripts/run_cvf_release_gate_bundle.py`
8. `scripts/run_cvf_sot3_a5_release_proof.py`
9. `scripts/run_cvf_sot3_a4_failure_recovery_proof.py`
10. `scripts/_local_env.py`
11. `docs/baselines/CVF_GC018_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_2026-08-15.md`

## Authority Chain

| Authority item | Evidence | Disposition |
|---|---|---|
| operator instruction | operator authorization 2026-08-15 for bounded provider API test | ACCEPT |
| active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| roadmap T6 entry | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` Work Plan T6 | ACCEPT |
| GC-018 requirement | paired T6 baseline | ACCEPT |
| active handoff | `AGENT_HANDOFF_V59_2026-08-11.md` | ACCEPT |

Authority boundary: this work order authorizes only the bounded live proof
above. It does not authorize production mutation, deployment, public sync, T5
adapter implementation, MCP/CLI invocation, or any readiness generalization.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | authorizes the bounded provider API test and its ceilings |
| Dispatcher | authors baseline and work order; runs pre-dispatch gate; commits nothing in this turn |
| Worker | runs the bounded live proof and records secret-safe evidence without commit |
| Reviewer/closer | independently verifies evidence, projects roadmap T6 row, commits material closure, then session sync |
| External reviewer | N/A with reason: no external reviewer input is used |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | execute one bounded live compatibility proof and record secret-safe evidence |
| scope classification | LIVE_PROOF_NO_COMMIT |
| primary task class | bounded provider live compatibility proof |
| risk sensitivity | high: quota, cost, and secret exposure |
| selected role route | SINGLE_AGENT_SINGLE_ROLE |
| orchestration requirement | no-commit worker followed by independent reviewer/closer |
| role separation basis | worker evidence cannot close its own tranche |
| escalation condition | source contradiction, missing credential, or ceiling breach |

## Pre-Flight Checks

- confirm HEAD equals `1719e53cdb56de9d17180dd3a389585802b4b8ae` and staging is empty;
- confirm the two output evidence paths do not yet exist;
- run the secret-safe diagnostic precheck: `.env.local` presence, key-alias
  presence status, provider readiness saved-receipt state, and `--dry-run`
  enumeration of the bundle;
- do not start if any unrelated dirty path exists;
- record exact commands and results in the worker return.

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside Allowed scope: reading files, running the primary command, capturing
evidence, and repairing allowed-scope documentation shape. Escalation is
reserved for a source contradiction, a forbidden-scope need, or a condition
that would exceed the call or cost ceiling. Routine gate remediation inside
Allowed scope is not an operator-preference checkpoint.

## Allowed Scope

Worker may create exactly:

1. `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md`
2. `docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-result-2026-08-15.json`
3. `docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-manifest-2026-08-15.json`
4. `docs/reviews/evidence/cadp-ai-t6-live-compatibility-sot3-diagnostic-2026-08-15.json`
5. `docs/reviews/evidence/cadp-ai-t6-live-compatibility-e2e-diagnostic-2026-08-15.json`

Forbidden: every other path; any modification or deletion; staging or commit;
production source, tests, scripts, provider adapters, roadmap, catalog/GAP/
index, corpus registry, session state, active handoff, `.env.local`, or
generated aggregate mutation; credential rotation or quota mutation; MCP/CLI
invocation; deployment; public sync; production action.

## Write Ownership

Worker owns only the five allowed paths above. Reviewer owns the optional
completion review, roadmap T6 row projection, material commit, and separate
session/handoff sync.

## Provider And Model Selection Rule

- Primary route: DashScope-compatible provider (Alibaba lane), model lane
  `qwen-turbo`. Do not switch provider, model, or route outside this rule.
- Key aliases: `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`,
  `CVF_ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`. Secret-safe precheck
  result: `DASHSCOPE_API_KEY` PRESENT_REDACTED, `ALIBABA_API_KEY`
  PRESENT_REDACTED, the other two NOT_FOUND.
- Live route: `src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`.

## Cost And Call Ceiling

- Maximum 3 real provider API calls for the entire T6 live proof.
- Total cost ceiling US$1.
- SOT3 A5 canonical path is source-verified as exactly one real provider call.
- The authorized `--e2e` selection runs UI mock E2E plus SOT3 and does not run
  the three live E2E specs. The worker must observe exactly one real provider
  call; any additional call is a failure, not retry authority.
- Before execution, verify against a current official provider pricing source
  that the fixed one-call request with `max_tokens` 4096 has a worst-case cost
  below US$1. If not demonstrable, stop without calling.

## Synthetic Input And Data Retention Boundary

- Test input must be synthetic and non-sensitive; private provenance content is
  never used as a request payload.
- No deliberate storage upload is authorized beyond the ordinary bounded API
  request. Provider-side processing or retention is governed by provider terms
  and is not asserted. Evidence files are secret-safe by construction and carry
  no raw key, token, header, or raw provider body.
- The worker must not write any provider response body that may contain
  sensitive metadata to a repository path.

## Secret Handling

- Secrets load by reference from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`
  via `scripts/_local_env.py` `bootstrap_repo_env`.
- Report only variable names and presence status (`PRESENT_REDACTED`, `EMPTY`,
  `NOT_FOUND`). The authorized runtime may load a value by reference but must
  never display or persist it outside process memory; do not validate a key
  through a separate probe call.
- Never print, copy, log, or commit any key value, bearer token, signed header,
  or request body containing a secret.

## Diagnostic And Retry Protocol

- Before the first live run, record a secret-safe diagnostic precheck.
- On any fail, partial, timeout, or ambiguous result, stop and record a
  secret-safe diagnostic classifying stage, failure class, retryability, and
  HTTP status using the stable vocabulary of the live-run diagnostic standard.
- No blind retry. A retry is allowed only when this work order permits it, the
  result-changing action is explicit, and cumulative call count and cost remain
  inside the ceiling.
- A mock result is never used as governance-behavior acceptance evidence.

## Evidence Output Paths

- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-result-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-manifest-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-sot3-diagnostic-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-e2e-diagnostic-2026-08-15.json`

## Required Live-Proof Execution

Primary command:

```powershell
python scripts/run_cvf_release_gate_bundle.py --e2e --json --output docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-result-2026-08-15.json --manifest-output docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-manifest-2026-08-15.json --sot3-diagnostic-output docs/reviews/evidence/cadp-ai-t6-live-compatibility-sot3-diagnostic-2026-08-15.json --e2e-diagnostic-output docs/reviews/evidence/cadp-ai-t6-live-compatibility-e2e-diagnostic-2026-08-15.json
```

The SOT3 canonical path is the mandatory governance-behavior acceptance
evidence and makes exactly one real Alibaba/DashScope recovery call. `--e2e`
selects the UI-only mock E2E surface and does not select the three-spec live E2E
surface, whose call cardinality is outside this packet's ceiling. Before the
run, the worker must establish from a current official provider pricing source
that the fixed one-call request with the repository's 4096-token maximum has a
worst-case charge below US$1. Otherwise return `BLOCKED_WITH_REASON` without a
provider call.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| primary command and evidence flags | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | main argparse flags | `--json`; `--output`; `--manifest-output`; `--sot3-diagnostic-output`; `--e2e-diagnostic-output` | release gate bundle | ACCEPT |
| env bootstrap and DashScope alias mapping | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | `bootstrap_live_provider_env` | `bootstrap_repo_env`; `DASHSCOPE_API_KEY` | release gate bundle | ACCEPT |
| `.env.local` load order and no-overwrite | LITERAL_INVARIANT | `scripts/_local_env.py` | `bootstrap_repo_env`; `DEFAULT_ENV_FILES` | `bootstrap_repo_env` | env bootstrap | ACCEPT |
| A5 invokes A4 runner only | LITERAL_INVARIANT | `scripts/run_cvf_sot3_a5_release_proof.py` | `run_a4_live`; module docstring | `run_a4_live`; `A4_RUNNER` | A5 adapter | ACCEPT |
| one recovery call admission | VALUE_SET | `scripts/run_cvf_sot3_a5_release_proof.py` | admission constants | `REQUIRED_RECOVERY_PROVIDER_CALL_COUNT` | A5 adapter | ACCEPT |
| Alibaba live route | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | `LIVE_TEST_RELATIVE_PATH` | `route.sot3-activation.alibaba.live.test.ts` | A4 runner | ACCEPT |
| key aliases | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | `ALIBABA_KEY_ALIASES` | `ALIBABA_KEY_ALIASES` | A4 runner | ACCEPT |
| provider/model lanes | VALUE_SET | `scripts/evaluate_cvf_provider_lane_certification.py` | `PROVIDERS` | `qwen-turbo`; `deepseek-chat`; `gpt-4o-mini` | provider certification evaluator | ACCEPT |
| Alibaba request maximum output tokens | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai-providers.ts` | Alibaba-compatible chat request body | `max_tokens` | Alibaba provider adapter | ACCEPT |
| canonical provider capability registry names alibaba/qwen-turbo | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` entry (providerId alibaba, modelId qwen-turbo) | `PROVIDER_CAPABILITY_REGISTRY` | model gateway provider capability registry | ACCEPT |
| provider registry enforces routable provider/model admission | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry` class | `assertAllowed`; `listRoutable` | model gateway provider registry | ACCEPT |
| no blind retry | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | `check_e2e` comment | no-blind-retry requirement | release gate bundle | ACCEPT |
| mock cannot bypass SOT3 | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | `check_sot3` docstring | `--mock` has no effect on SOT3 | release gate bundle | ACCEPT |
| manifest accepted secret env | VALUE_SET | `scripts/build_cvf_live_evidence_manifest.py` | `build_manifest` rerun block | `acceptedSecretEnv`; `requiresLiveProviderKey` | live evidence manifest | ACCEPT |
| diagnostic fields and stable vocab | VALUE_SET | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | Required Diagnostic Fields and Stable Classes | `stage`; `class`; `retryable`; `userAction`; `safeMessage` | live-run diagnostic owner | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Source Verification Block`; `Checker Source Read-Ahead Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition`; `Reviewer Closure Conversion`; `Worker Autonomy / No-Question Rule`; `WORKER_MUST_NOT_COMMIT`; `Work-Order Fulfillment Manifest`; `Worker Return Packet Shape Contract` |
| gateRunPurpose | confirmation and evidence after reading checker source ahead of writing |
| claimBoundary | structural read-ahead does not prove live provider behavior or production readiness |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO: this work order makes no live claim; the worker's future return makes it |
| liveProofAuthorized | YES: bounded, after independent reviewer acceptance |
| runtimeMutationAuthorized | NO: no production/runtime/source mutation |
| freshnessVerificationMode | SOURCE_VERIFIED_LIVE_PATH: release bundle, A5, A4, env bootstrap, provider readiness, and manifest verified against current HEAD without execution |
| reason | the live run is authorized but not yet executed; provider-call behavior was source-verified |
| requiredFutureAction | worker runs the primary command after acceptance and records secret-safe evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; no-live-claim-at-dispatch and no-commit boundaries remain mandatory |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Path existence for the two T6 dispatch artifact paths | both proposed baseline and work order paths were absent before authoring | ABSENT_BEFORE_AUTHORING |
| Bounded collision search | searched governed artifact roots plus session state for `CADP-AI-T6` and `live compatibility`; no existing T6 baseline or work order found | EXISTING_OWNER_SURFACES_REUSED |
| Collision decision | roadmap T6 row and SOT3 A5/A4 evidence remain their existing owners | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | release gate bundle and A5/A4 runners under `scripts/` | bounded live proof only; no runtime/source mutation, no public/session authority | source-verified scripts and future worker evidence | none introduced | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP surface | no invocation, launch, credential, mutation, or public authority | T5 decision remains deferred | future fresh packet required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact or recommendation is ingested |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T6 baseline and this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources may support this dispatch |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Requirement |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit live-proof worker, then independent reviewer/closer |
| phase | worker execution pending |
| baseHeadFor(phase) | dispatchBaseHead=`1719e53cdb56de9d17180dd3a389585802b4b8ae`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| executionBaseHead | worker records exact dispatcher HEAD before edits |
| dirtyPathPolicy | zero unrelated dirty paths |
| changedSetScope(phase) | exact five-path worker manifest (one worker return plus four evidence JSONs) |
| traceScope(phase, actor) | worker records reads, searches, commands, diagnostics, diff, status, and gates |
| operationReceiptWriteOrder | worker writes return last after evidence stabilizes |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; independent reviewer owns commits |
| crossBatchIsolation | no unrelated changed path may be touched or absorbed |
| nextMoveSurfaces | reviewer-owned completion/roadmap projection/material commit, then separate session sync |
| commitBoundary | worker MUST NOT stage or commit |

## Reviewer Closure Conversion

| Field | Requirement |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_COMPLETION_2026-08-15.md` (optional; prefer repairing evidence in the worker return) |
| reviewerOwnedClosurePaths | optional completion review; CADP roadmap T6 row projection; session continuity separately |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| publicRule | no EXPORTED disposition without public-sync remote, commit, and artifact path evidence |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
|---|---|
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| evidence JSONs under the evidence paths | derive the release bundle, A5, A4, and manifest schemas before running |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| worker return | record execution base, final HEAD, call count, cost, diagnostic, evidence paths, gate outcomes, no-commit confirmation |
| release gate result JSON | `--output` result of the primary command |
| release gate manifest JSON | `--manifest-output` manifest with evidence hashes and secret-safe rerun command |
| SOT3 diagnostic JSON | `--sot3-diagnostic-output` secret-safe diagnostic |
| E2E diagnostic JSON | `--e2e-diagnostic-output` secret-safe E2E diagnostic |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Acceptance Criteria

- the primary command ran with real DashScope-compatible credentials loaded by
  reference;
- the SOT3 canonical path is the governance-behavior acceptance evidence and
  is not a mock;
- cumulative real provider calls stayed at exactly 1 and the pre-execution
  official-price worst-case bound stayed below US$1;
- evidence JSON, manifest, and diagnostics landed at the exact governed paths;
- no raw key, token, header, or raw provider body was printed or persisted;
- the worker return passes the fast gate before return;
- exactly the five allowed worker paths are changed; staging empty; HEAD
  unchanged; worker did not commit.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1719e53cdb56de9d17180dd3a389585802b4b8ae --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-only
git diff --cached --name-only
git rev-parse HEAD
```

No credential rotation, quota mutation, MCP/CLI invocation, deployment, public
sync, or production action is permitted.

## Execution Plan

1. capture execution base and clean state;
2. read all required authorities and checker sources;
3. run the secret-safe diagnostic precheck;
4. run the primary command with evidence outputs;
5. record the one-call observation and official-price worst-case cost bound;
6. capture secret-safe diagnostics on any failure;
7. write the worker return;
8. run fast gates and repair only the five owned paths;
9. confirm staging empty and HEAD unchanged.

## Evidence Requirements

- exact source path and locator for every accepted claim;
- commands and outputs for the primary command and gates;
- cumulative real provider call count and official-price worst-case cost bound;
- secret-safe diagnostic records with stage, class, retryability, and HTTP
  status;
- evidence output paths and manifest hashes;
- actual git status, changed set, staging state, and HEAD;
- no self-reported clean claim that omits the five untracked worker paths.

## Review Gate

The independent reviewer must challenge provider/model selection, call and cost
ceiling compliance, secret safety, diagnostic completeness, evidence paths,
mock exclusion, and the exact five-path manifest. Gate success alone is not
semantic acceptance.

## Closure Checklist

- [ ] exact five worker paths only
- [ ] SOT3 canonical path is real, not mock
- [ ] call count exactly 1 and official-price worst-case cost bound below US$1
- [ ] evidence JSON, manifest, and diagnostics at exact governed paths
- [ ] secret-safe diagnostics recorded for any failure
- [ ] worker-return fast gate passes
- [ ] staging empty and HEAD unchanged
- [ ] worker did not commit

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_INDEPENDENT_REVIEW` only after the evidence and
required gates pass. Return `BLOCKED_WITH_REASON` when a source contradiction,
missing credential, or ceiling breach prevents completion.

## Operator Checkpoint

No T5 adapter implementation, MCP/CLI invocation, deployment, public sync,
production mutation, or readiness generalization opens from this packet. Any
later action requires the independent reviewer conversion and a fresh governed
packet where applicable.

## Worker Return Required Evidence

The worker return must state executionBaseHead, final HEAD, exact five-path
status, staging state, provider/model used, cumulative call count, cost bound,
secret-safe diagnostic records, evidence paths, gate outcomes, and no-commit
confirmation.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Planned durable reference folder | N/A with reason: no durable governance foundation reference folder is created, split, relocated, or refactored by this tranche |
| Planned front door/index | N/A with reason: no foundation front door or index is created or changed |
| Date policy | N/A with reason: no dated foundation file is introduced |
| Owner surface | existing evidence paths under the reviews evidence family and the worker return |
| Claim boundary | live-proof evidence only; no foundation storage or index mutation |

## MCP/CLI Adapter Boundary

| Field | Binding |
|---|---|
| Adapter scope | none; T5 implementation remains deferred |
| External-agent surface | no CLI/MCP invocation or launch |
| Public surface | no public artifact, remote, commit, push, or deploy |
| No-runtime-overclaim | no runtime, provider, credential, mutation, interception, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | CADP-AI-T6 dispatch authoring, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | PowerShell, repository Python guards, and apply-patch editing |
| Target paths | paired T6 baseline and paired T6 work order |
| Allowed scope source | operator authorization 2026-08-15, CADP roadmap T6 entry |
| Before status evidence | clean worktree at HEAD `1719e53cdb56de9d17180dd3a389585802b4b8ae` |
| After status evidence | exact two-path unstaged dispatch authoring set before validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded T6 live-proof dispatch only; no live run, secret disclosure, or production action |
| Claim boundary | packet authoring and dispatch gates only |
| Agent type | single dispatcher role |
| Invocation ID | `cadp-ai-t6-dispatch-2026-08-15` |
| Expected manifest | T6 baseline; T6 work order |
| Actual changed set | T6 baseline; T6 work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repo-local CADP-AI-T6 bounded live compatibility proof |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created by this dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or provider action occurs during dispatch authoring |
| invocationBoundary | local read-only source verification and governed document authoring only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | bounded live-proof authorization only, pending independent review |
| forbiddenExpansion | no production readiness, universal provider compatibility, trusted-evidence readiness, cross-runtime determinism, public export, or T5 adapter implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: live proof uses private credentials and private provenance workflow; no
public-sync authorization exists.

## Claim Boundary

This work order authorizes exactly one bounded live compatibility proof with
its secret-safe evidence capture. It makes no live claim itself, does not prove
provider compatibility or production readiness, and does not authorize public
sync, deployment, T5 adapter implementation, MCP/CLI invocation, or any
runtime/source mutation. The worker commits nothing.
