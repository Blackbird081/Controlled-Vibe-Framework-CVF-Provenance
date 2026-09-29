# CVF GC-018 Baseline - CADP-AI-T6 Live Compatibility Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-15

Batch ID: CADP-AI-T6

Dispatch base head: `1719e53cdb56de9d17180dd3a389585802b4b8ae`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

Worker target: live-proof worker role (not a specific provider name)

## Purpose

Authorize a bounded live compatibility proof tranche for CADP-AI-T6. The
future worker runs the repository release gate bundle with real
DashScope-compatible provider credentials loaded by reference from
`.env.local`, using synthetic non-sensitive input, inside a strict call and
cost ceiling, and records secret-safe evidence. This dispatch packet authorizes
only the future live run and its evidence capture; it makes no live claim and
runs no provider call itself.

## Authorization

The operator authorized on 2026-08-15 a bounded provider API test for T6 after
this dispatch packet is accepted by the independent reviewer. The authorization
scope is exactly:

- bounded provider API test via the repository release gate bundle;
- secrets loaded by reference from `.env.local` (variable names only, values
  never printed, copied, logged, or committed);
- synthetic, non-sensitive test input; private provenance is never used as a
  request payload;
- at most 3 provider API calls;
- total cost ceiling US$1;
- DashScope-compatible provider is the primary route;
- secret-safe diagnostic and evidence capture.

The authorization does not include: printing, copying, logging, or committing
API keys; credential rotation or quota mutation; MCP/CLI external-agent
invocation; production mutation; deployment; public sync or export; persistent
provider data upload; T5 adapter implementation; hook, autorun, or CI changes;
or any production-readiness, universal-provider-compatibility,
trusted-evidence-readiness, or cross-runtime-determinism claim.

## Dependency Release Evidence

| Dependency | Evidence | Required state | Result |
|---|---|---|---|
| T6 credentials | operator authorization, 2026-08-15; secret-safe precheck confirms `DASHSCOPE_API_KEY` and `ALIBABA_API_KEY` present in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` | present by reference, not printed | SATISFIED |
| T6 cost ceiling | operator authorization, 2026-08-15 | US$1 total | SATISFIED |
| T6 call ceiling | operator authorization, 2026-08-15 | at most 3 provider API calls | SATISFIED |
| T6 sandbox | this packet Synthetic Input And Data Retention Boundary | synthetic non-sensitive input; no repository persistence of raw provider bodies; provider-side retention is not asserted | SATISFIED |
| T6 live diagnostic | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` plus release bundle diagnostic arguments | secret-safe stage/class/retryable/userAction/httpStatus | SATISFIED |
| T6 release work order | paired work order `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_2026-08-15.md` | bounded live proof execution packet | SATISFIED |
| T6 roadmap row | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` Work Plan T6 | entry conditions now supplied by operator authorization | PASS_PENDING_REVIEWER_PROJECTION |

## Scope

- authorize exactly one future bounded live compatibility proof run by the
  worker, executed only after the independent reviewer accepts this dispatch;
- source-verify the release gate bundle and every script/provider adapter it
  invokes against current HEAD;
- record the chosen provider/model selection rule, call and cost ceiling,
  synthetic input boundary, secret handling, diagnostic/retry protocol, and
  evidence output paths;
- require the worker to run the primary command and capture evidence JSON,
  manifest, and secret-safe diagnostics at exact governed paths;
- require the worker to stop on any fail, partial, timeout, or ambiguous result
  and record a secret-safe diagnostic before any retry.

## Non-Goals

No live run, API call, quota consumption, or secret disclosure occurs during
this dispatch-authoring turn; local checks evaluate presence status only. No production source, tests, scripts, provider
adapter, roadmap, catalog/GAP/index, corpus registry, session state, active
handoff, `.env.local`, or generated aggregate is modified by this dispatch. No
deployment, public sync, or production action. No claim of production
readiness, universal provider compatibility, trusted-evidence readiness, or
cross-runtime determinism.

## Provider And Model Selection Rule

- Primary route: DashScope-compatible provider (Alibaba lane), model lane
  `qwen-turbo` per `scripts/evaluate_cvf_provider_lane_certification.py`
  `PROVIDERS`.
- Key aliases accepted by the release bundle and A4 runner:
  `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`,
  `CVF_BENCHMARK_ALIBABA_KEY`. Secret-safe precheck result: `DASHSCOPE_API_KEY`
  PRESENT_REDACTED, `ALIBABA_API_KEY` PRESENT_REDACTED, the other two
  NOT_FOUND.
- The live route is the A4 runner's
  `src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`; the SOT3
  A5 canonical proof makes exactly one bounded Alibaba recovery call.
- The worker must not switch provider, model, or route outside this rule.

## Cost And Call Ceiling

- Maximum 3 real provider API calls for the entire T6 live proof.
- Total cost ceiling US$1.
- The SOT3 A5 canonical path is source-verified as exactly one real provider
  call (`recoveryProviderCallCount == 1` admission requirement; the ENFORCE-to-OFF
  rollback row uses a provider spy and is not a real API call; 18 negative
  cases make zero provider calls).
- The authorized primary command selects `--e2e`, which runs the UI mock E2E
  surface plus the mandatory SOT3 path. It does not select the three-spec live
  E2E surface. Source inspection shows the SOT3 path admits exactly one real
  provider call, keeping the run inside the 3-call ceiling.
- Before execution, the worker must verify that the fixed one-call request with
  the repository's 4096-token maximum has a worst-case provider charge below
  US$1 using a current official provider pricing source. If that bound cannot
  be established, the worker returns `BLOCKED_WITH_REASON` without calling.

## Synthetic Input And Data Retention Boundary

- Test input must be synthetic and non-sensitive. Private provenance content is
  never used as a request payload.
- No deliberate storage upload is authorized beyond the ordinary bounded API
  request. Provider-side processing or retention is governed by provider terms
  and is not asserted by this packet. Repository evidence files are secret-safe
  by construction and carry no raw key, bearer token, signed header, or raw
  provider body.
- The worker must not write any provider response body that may contain
  sensitive metadata to a repository path.

## Secret Handling

- Secrets are loaded by reference from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`
  via `scripts/_local_env.py` `bootstrap_repo_env` (DEFAULT_ENV_FILES order).
- The worker reports only variable names and presence status
  (`PRESENT_REDACTED`, `EMPTY`, `NOT_FOUND`); the authorized runtime may load a
  value by reference but must never display or persist it outside process memory.
- The worker must not print, copy, log, or commit any key value, bearer token,
  signed header, or request body containing a secret.
- The dispatch authoring turn reports only local presence status and performs
  no network validation or secret disclosure.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| primary live-proof command and JSON/output/manifest/diagnostic flags | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | main argparse flags and usage docstring | `--json`; `--output`; `--manifest-output`; `--sot3-diagnostic-output`; `--e2e-diagnostic-output` | release gate bundle | ACCEPT |
| bundle loads provider env from `.env.local` then maps DashScope aliases | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | `bootstrap_live_provider_env` | `bootstrap_repo_env`; `DASHSCOPE_API_KEY` | release gate bundle | ACCEPT |
| `.env.local` load order and no-overwrite behavior | LITERAL_INVARIANT | `scripts/_local_env.py` | `bootstrap_repo_env`; `DEFAULT_ENV_FILES` | `bootstrap_repo_env` | env bootstrap | ACCEPT |
| SOT3 A5 adapter invokes the accepted A4 runner only, never the provider route directly | LITERAL_INVARIANT | `scripts/run_cvf_sot3_a5_release_proof.py` | module docstring and `run_a4_live` | `run_a4_live`; `A4_RUNNER` | A5 adapter | ACCEPT |
| SOT3 A5 admits only one recovery provider call | VALUE_SET | `scripts/run_cvf_sot3_a5_release_proof.py` | admission constants | `REQUIRED_RECOVERY_PROVIDER_CALL_COUNT` | A5 adapter | ACCEPT |
| A4 live route is Alibaba/DashScope and makes exactly one bounded recovery call | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | `LIVE_TEST_RELATIVE_PATH`; `cmd_live`; module docstring | `route.sot3-activation.alibaba.live.test.ts` | A4 runner | ACCEPT |
| A4 key aliases for Alibaba/DashScope | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | `ALIBABA_KEY_ALIASES` | `ALIBABA_KEY_ALIASES` | A4 runner | ACCEPT |
| provider/model lanes | VALUE_SET | `scripts/evaluate_cvf_provider_lane_certification.py` | `PROVIDERS` | `qwen-turbo`; `deepseek-chat`; `gpt-4o-mini` | provider certification evaluator | ACCEPT |
| Alibaba request maximum output tokens | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai-providers.ts` | Alibaba-compatible chat request body | `max_tokens` | Alibaba provider adapter | ACCEPT |
| canonical provider capability registry names alibaba/qwen-turbo | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` entry (providerId alibaba, modelId qwen-turbo) | `PROVIDER_CAPABILITY_REGISTRY` | model gateway provider capability registry | ACCEPT |
| provider registry enforces routable provider/model admission | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry` class | `assertAllowed`; `listRoutable` | model gateway provider registry | ACCEPT |
| provider readiness evaluator reads saved receipts and makes no live call | LITERAL_INVARIANT | `scripts/check_cvf_provider_release_readiness.py` | module docstring | `run_evaluator` | provider readiness gate | ACCEPT |
| no automatic blind retry on E2E failure | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | `check_e2e` comment block | no-blind-retry requirement | release gate bundle | ACCEPT |
| mock mode cannot bypass SOT3 | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | `check_sot3` docstring | `--mock` has no effect on SOT3 | release gate bundle | ACCEPT |
| manifest declares accepted secret env names and live-key requirement | VALUE_SET | `scripts/build_cvf_live_evidence_manifest.py` | `build_manifest` rerun block | `acceptedSecretEnv`; `requiresLiveProviderKey` | live evidence manifest | ACCEPT |
| secret-safe diagnostic fields and stable vocab | VALUE_SET | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | Required Diagnostic Fields and Stable Classes | `stage`; `class`; `retryable`; `userAction`; `safeMessage` | live-run diagnostic owner | ACCEPT |
| mock result is not governance-behavior acceptance evidence | LITERAL_INVARIANT | `AGENTS.md` | Mandatory Live Governance Proof | real provider API call required | root instruction carrier | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Source Verification Block`; `Checker Source Read-Ahead Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition`; `Reviewer Closure Conversion`; `Worker Autonomy / No-Question Rule`; `WORKER_MUST_NOT_COMMIT`; `Dependency Release Evidence`; `Scaffold Provenance Block` |
| gateRunPurpose | confirmation and evidence after reading checker source ahead of writing |
| claimBoundary | structural read-ahead does not prove live provider behavior, provider compatibility, or production readiness |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id CADP-AI-T6 --title "CADP AI T6 Bounded Live Compatibility Proof" --date 2026-08-15 --base 1719e53cdb56de9d17180dd3a389585802b4b8ae --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | dispatch, source verification, negative search, agent handoff contract, reviewer closure conversion, worker return shape, trace, delta block, public disposition, claim boundary |
| manualEditsAfterScaffold | bound T6 live-proof semantics, operator authorization scope, provider/model selection, call/cost ceiling, secret handling, evidence paths, diagnostic/retry protocol, dependency release rows, and no-live-claim-at-dispatch boundary |
| checkerReadAheadConfirmation | checker sources in the preceding block were read before governed authoring |
| docOnlyNewFields | `sot3CanonicalPath`; `e2eLiveSupplementarySurface`; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no live, runtime, provider, public-sync, or production behavior is implemented |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Path existence for the two T6 dispatch artifact paths | both proposed baseline and work order paths were absent before authoring | ABSENT_BEFORE_AUTHORING |
| Bounded collision search for existing T6 live-compatibility owners | searched governed artifact roots plus session state for `CADP-AI-T6` and `live compatibility`; no existing T6 baseline or work order found | EXISTING_OWNER_SURFACES_REUSED |
| Collision decision | roadmap T6 row, SOT3 A5/A4 evidence, and live-run diagnostic standard remain their existing owners; T6 dispatch adds new baseline and work order only | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; canonical source and no-live-claim-at-dispatch boundaries remain mandatory |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO: this dispatch makes no live claim; the worker's future return makes it |
| liveProofAuthorized | YES: bounded, per operator authorization 2026-08-15, effective only after independent reviewer acceptance |
| runtimeMutationAuthorized | NO: no production/runtime/source mutation is authorized |
| freshnessVerificationMode | SOURCE_VERIFIED_LIVE_PATH: release bundle, A5 adapter, A4 runner, env bootstrap, provider readiness, and evidence manifest were verified against current HEAD without executing them |
| reason | the dispatch authorizes a future bounded live run; provider-call behavior was source-verified, not executed |
| requiredFutureAction | after acceptance, worker runs the primary command, records secret-safe diagnostic and evidence, and returns pending independent review |

## Diagnostic And Retry Protocol

- Before the first live run, the worker records a secret-safe diagnostic
  precheck: `.env.local` presence, key-alias presence status, provider
  readiness saved-receipt state, and a `--dry-run` enumeration of the bundle.
- On any fail, partial, timeout, or ambiguous result, the worker stops and
  records a secret-safe diagnostic classifying stage, failure class,
  retryability, and HTTP status using the stable vocabulary of the live-run
  diagnostic standard.
- No blind retry. A retry is allowed only if the work order permits it, the
  result-changing action is explicit, and the cumulative call count and cost
  remain inside the ceiling.
- A mock result is never used as governance-behavior acceptance evidence.

## Evidence Output Paths

Future worker-owned evidence JSON paths (secret-safe by construction):

- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-result-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-release-gate-manifest-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-sot3-diagnostic-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-live-compatibility-e2e-diagnostic-2026-08-15.json`

## Acceptance Matrix

| Criterion | Required state | Result |
|---|---|---|
| provider call is real | SOT3 A5 canonical path makes one real DashScope/Alibaba recovery call | source-verified |
| call ceiling | exactly one SOT3 real provider call; still below the operator ceiling of 3 | governed |
| cost ceiling | official-price worst-case bound for the fixed one-call request is below US$1 before execution | required |
| synthetic input | non-sensitive synthetic payload only | governed |
| secret safety | no key value, token, header, or raw body printed or persisted | governed |
| diagnostic before first live run | secret-safe precheck recorded | required |
| evidence output | result JSON, manifest, and diagnostics at exact governed paths | required |
| mock exclusion | mock result is not acceptance evidence | required |

## Failure And Stop Conditions

The worker must stop and record a secret-safe diagnostic when any of the
following occurs: no Alibaba/DashScope key alias present; local negative gate
not green; live test process failure or missing observation; SOT3 admission
failure; cumulative provider calls would exceed 3; cost would exceed US$1; or
any timeout or ambiguous result. The worker returns `BLOCKED_WITH_REASON` when
the live proof cannot complete inside the ceiling.

## Decision / Baseline

Proceed with one bounded CADP-AI-T6 live compatibility proof after independent
reviewer acceptance. The worker runs the primary command with real
DashScope-compatible credentials loaded by reference, synthetic input, a
3-call and US$1 ceiling, and secret-safe evidence capture. No live run, secret
value read, production action, or public export occurs until independent
review.

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
| Chain map route | N/A with reason: no external artifact or recommendation is ingested; operator supplied only an authorization instruction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources may support this dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | CADP-AI-T6 bounded live compatibility proof dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created by this dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or provider action occurs during dispatch authoring |
| invocationBoundary | local read-only source verification and governed document authoring only |
| interceptionBoundary | no wrapper, proxy, runtime gate, or process interception |
| claimLanguage | bounded live-proof authorization only, pending independent review |
| forbiddenExpansion | no production readiness, universal provider compatibility, trusted-evidence readiness, cross-runtime determinism, public export, or T5 adapter implementation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: live proof uses private credentials and private provenance workflow; no
public-sync authorization exists.

## Claim Boundary

This baseline authorizes only a bounded future live compatibility proof. It
makes no live claim itself, does not prove provider compatibility or
production readiness, and does not authorize public sync, deployment, T5
adapter implementation, MCP/CLI invocation, or any runtime/source mutation.
The T6 roadmap row remains `PARKED_NOT_AUTHORIZED` until the independent
reviewer projects it after acceptance.
