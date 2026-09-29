# CVF GC-018 Baseline - CADP-AI-T6-R1 Qwen3.7 Flash Live Compatibility Retry

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-15

Batch ID: CADP-AI-T6-R1

Dispatch base head: `3536a3b67ba4752d16c16834b006515568b97915`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

## Purpose

Authorize a fresh bounded retry of the CADP-AI-T6 live compatibility proof.
The predecessor attempt is preserved as `BLOCKED_WITH_REASON` because its
worker shell could not resolve npm/npx and made zero provider calls. This R1
packet targets the current Alibaba free-quota model `qwen3.7-flash`, requires
an explicit Node/npm/npx preflight, and authorizes no provider call until every
preflight and price-bound condition passes.

## Authorization And Dependency Release Evidence

| Dependency | Evidence | Required state | Result |
|---|---|---|---|
| predecessor attempt | `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md` | historical blocker preserved; zero calls | ACCEPT |
| npm/npx recovery | dispatcher shell resolves node, npm and npx; worker must independently reverify | all executable in worker shell | PENDING_WORKER_PREFLIGHT |
| model refresh | governed JSON/Markdown/TypeScript Alibaba ledgers and canonical SOT3 route at dispatch HEAD | `qwen3.7-flash`, enabled, quota current | ACCEPT |
| quota snapshot | `qwen3.7-flash` and `qwen3.7-flash-2026-07-15`; 1,000,000/1,000,000; expiry 2026-10-22; captured 2026-08-15 | current operator-supplied governed ledger | ACCEPT |
| operator ceiling | operator authorization | at most 3 calls and US$1 total | ACCEPT |
| live proof | `AGENTS.md` Mandatory Live Governance Proof | real provider call required for acceptance | PENDING_WORKER |

The operator allows API keys to be used by reference for this test. Values may
never be printed, copied, logged, persisted, or committed.

## Scope And Non-Goals

Scope is exactly one release-gate-bundle execution using synthetic,
non-sensitive input and secret-safe evidence. The canonical SOT3 path must
make exactly one real Alibaba/DashScope call. No source, test, configuration,
roadmap, registry, session, handoff, environment file, deployment, public
repository, or production system may be mutated. This dispatch turn makes no
API call and no live compatibility claim.

## Provider And Model Selection Rule

- Provider route: Alibaba/DashScope-compatible only.
- Exact model: `qwen3.7-flash`; snapshot reference:
  `qwen3.7-flash-2026-07-15`.
- Canonical route:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`.
- Accepted key aliases: `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`,
  `CVF_ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`.
- The worker must not fall back to `qwen-turbo` or select another provider or
  model.

## Environment Preflight Gate

Before any provider call, the worker must capture secret-safe results for
`where.exe node`, `where.exe npm`, `where.exe npx`, `node --version`,
`npm --version`, and `npx --version`. npm and npx must resolve in the same
PowerShell process used for the live command, through the active NVM4W nodejs
path. The worker must also run the bundle `--dry-run` and the focused local
route negative gate. Any missing executable, path mismatch, unrelated dirty
path, or failed local gate requires `BLOCKED_WITH_REASON` with zero calls.

## Cost And Call Ceiling

- Maximum cumulative real provider calls: 3; expected and accepted count: 1.
- Total charge ceiling: US$1.
- Before execution the worker must reverify current official Alibaba Model
  Studio pricing for `qwen3.7-flash` and calculate a conservative worst-case
  bound for the repository request (`max_tokens` 4096). If the official source
  or a below-US$1 bound cannot be established, stop with zero calls.
- No probe call and no blind retry. A second call requires a recorded,
  result-changing remediation and must remain inside both ceilings.

## Synthetic Input, Data Retention, And Secret Handling

Only repository-defined synthetic non-sensitive input is permitted. Private
provenance content must not enter the request. Secrets load from
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` through
`scripts/_local_env.py`; only alias names and `PRESENT_REDACTED`, `EMPTY`, or
`NOT_FOUND` status may appear in evidence. Raw provider bodies, bearer tokens,
signed headers, and key values must never be written to the repository.
Provider-side retention is not asserted by this packet.

## Diagnostic And Retry Protocol

Follow `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.
Before the first call, record executable resolution, secret-alias presence,
dry-run selection, pricing source/date, computed cost bound, and call counter.
On failure, partial result, timeout, or ambiguity, stop and record stage,
class, retryable, userAction, safeMessage, and HTTP status when available. No
blind retry is authorized.

## Evidence Output Paths

- `docs/reviews/CVF_CADP_AI_T6_R1_QWEN37_FLASH_LIVE_COMPATIBILITY_RETRY_WORKER_RETURN_2026-08-15.md`
- `docs/reviews/evidence/cadp-ai-t6-r1-release-gate-result-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r1-release-gate-manifest-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r1-sot3-diagnostic-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r1-e2e-diagnostic-2026-08-15.json`

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| release command and outputs | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | argparse | `--e2e`; JSON and diagnostic flags | release bundle | ACCEPT |
| env loading | LITERAL_INVARIANT | `scripts/_local_env.py` | `bootstrap_repo_env` | `DEFAULT_ENV_FILES` | local env bootstrap | ACCEPT |
| exact one-call admission | VALUE_SET | `scripts/run_cvf_sot3_a5_release_proof.py` | admission constants | `REQUIRED_RECOVERY_PROVIDER_CALL_COUNT` | SOT3 A5 | ACCEPT |
| canonical live test | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | live path and aliases | `LIVE_TEST_RELATIVE_PATH`; `ALIBABA_KEY_ALIASES` | SOT3 A4 | ACCEPT |
| selected model | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts` | Alibaba live request | `qwen3.7-flash` | SOT3 route | ACCEPT |
| governed quota facts | VALUE_SET | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | T6 target and model row | `qwen3.7-flash` | Alibaba ledger | ACCEPT |
| historical blocker | VALUE_SET | `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md` | disposition and diagnostic | npm/npx unavailable; zero calls | predecessor return | ACCEPT |
| live proof requirement | LITERAL_INVARIANT | `AGENTS.md` | Mandatory Live Governance Proof | real API call | root carrier | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition`; `Reviewer Closure Conversion`; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirmation and evidence after source read-ahead, not first discovery |
| claimBoundary | checker success does not prove a provider call or compatibility |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id CADP-AI-T6-R1 --title "CADP AI T6 R1 Qwen3.7 Flash Live Compatibility Retry" --date 2026-08-15 --base 6291ac3dd --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | runtime-provider-live, no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | source verification, handoff, reviewer conversion, trace, delta and public disposition |
| manualEditsAfterScaffold | bound predecessor blocker, executable preflight, refreshed model/quota, ceilings and exact evidence paths; re-anchored final dispatch after route and handoff commits |
| checkerReadAheadConfirmation | applicable checker sources read before authoring |
| docOnlyNewFields | no runtime schema field introduced |
| claimBoundary | packet authoring only; no provider action |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact R1 paths | both absent before authoring | ABSENT_BEFORE_AUTHORING |
| bounded token search | no `CADP-AI-T6-R1` owner existed | NO_COLLISION |
| predecessor | original T6 packet and blocked return remain immutable evidence | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cadp`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cadp --risk-ceiling HIGH --max-results 10 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added constraint; preflight and no-live-claim boundary remain mandatory |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| liveProofAuthorized | YES, only after packet acceptance and preflight PASS |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | source verification at dispatch HEAD; worker must execute fresh proof |
| reason | prior attempt made zero calls and cannot serve as live evidence |
| requiredFutureAction | worker runs exact packet and returns uncommitted evidence |

## Acceptance Matrix And Stop Conditions

| Criterion | Required state |
|---|---|
| executable preflight | node/npm/npx resolve and report versions in worker shell |
| provider/model | Alibaba/DashScope and exact `qwen3.7-flash` |
| live evidence | one real non-mock SOT3 call |
| ceilings | exactly 1 call accepted; cumulative at most 3; total below US$1 |
| evidence | exact five paths and secret-safe content |
| repository state | staging empty and HEAD unchanged |

Any failed preflight, missing key alias, official-price uncertainty, local gate
failure, ceiling risk, timeout, ambiguous result, or forbidden-scope need stops
execution and yields `BLOCKED_WITH_REASON`.

## Decision / Baseline

Proceed with one bounded R1 proof only after every executable, local-test,
credential-presence, and official-price preflight passes. The worker must use
exactly `qwen3.7-flash`, create only the five governed evidence paths, and
leave the repository uncommitted for independent review.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | release bundle and SOT3 A5/A4 | bounded live evidence only | future R1 return | none | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no invocation or mutation authority | T5 remains separate | fresh packet required | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

| Field | Requirement |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | no-commit worker then independent reviewer/closer |
| phase | worker execution pending |
| baseHeadFor(phase) | dispatchBaseHead=`3536a3b67ba4752d16c16834b006515568b97915`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| executionBaseHead | worker records exact clean dispatch HEAD |
| dirtyPathPolicy | zero unrelated dirty paths |
| changedSetScope(phase) | exact five-path R1 manifest |
| traceScope(phase, actor) | reads, commands, diagnostics, calls, cost, diff and status |
| operationReceiptWriteOrder | worker return written last |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | no predecessor or unrelated path mutation |
| nextMoveSurfaces | reviewer acceptance/closure then separate session sync |
| commitBoundary | staging empty; worker must not commit |

## Reviewer Closure Conversion

The independent reviewer must verify the real-call receipt, exact model,
pricing computation, ceilings, secret safety, five-path manifest, and clean
no-commit boundary. Only the reviewer may convert evidence into closure and
roadmap/session projection.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local repository tools |
| Session or invocation | CADP-AI-T6-R1 dispatch, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | PowerShell, repository guards, apply-patch |
| Target paths | paired R1 baseline and work order |
| Allowed scope source | operator instruction and CADP T6 authority |
| Before status evidence | clean HEAD `3536a3b67ba4752d16c16834b006515568b97915` |
| After status evidence | paired dispatch files only before validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; zero API calls |
| Claim boundary | authoring and local guard results only |
| Agent type | single dispatcher role |
| Invocation ID | `cadp-ai-t6-r1-dispatch-2026-08-15` |
| Expected manifest | paired R1 baseline and work order |
| Actual changed set | paired R1 baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | CADP-AI-T6-R1 dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or compatibility is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no live receipt in dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no provider action occurred |
| invocationBoundary | local source verification and document authoring |
| interceptionBoundary | no wrapper, proxy, hook, or process interception |
| claimLanguage | bounded future retry authorization |
| forbiddenExpansion | no production, universal-provider, deployment, public-export, or T5 claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private credentials and private provenance workflow; no public-sync
authorization or evidence exists.

## Claim Boundary

This baseline authorizes only the bounded future R1 live proof. It neither
asserts compatibility nor authorizes production mutation, deployment, public
sync, external CLI/MCP use, or worker commit.
