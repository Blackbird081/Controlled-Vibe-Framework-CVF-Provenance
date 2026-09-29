# CVF GC-018 Baseline - CADP-AI-T6-R2 Qwen3.7 Flash Free Quota Cost Gate Retry

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-15

Batch ID: CADP-AI-T6-R2

Dispatch base head: `8ce45e190b16f9dc262ef672016fa758d9d04daa`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

## Purpose

Authorize a second bounded retry of the CADP-AI-T6 live compatibility proof
using the same exact model `qwen3.7-flash`, replacing R1's official-pricing
cost gate (which blocked because the public Alibaba Model Studio pricing page
does not currently list `qwen3.7-flash`) with an operator-directed
free-quota-based cost gate: current governed console/documentation evidence
that Free Quota Only mode is enabled for the account plus remaining quota
above the request ceiling, sourced from official Alibaba free-quota
documentation and the governed free-quota model ledger.

## Authorization And Dependency Release Evidence

| Dependency | Evidence | Required state | Result |
|---|---|---|---|
| R1 blocker | `docs/reviews/CVF_CADP_AI_T6_R1_QWEN37_FLASH_LIVE_COMPATIBILITY_RETRY_WORKER_RETURN_2026-08-15.md` | reviewer-accepted `REVIEWER_ACCEPTED_BLOCKED_R1_REOPEN_R2_SAME_MODEL`, zero calls | ACCEPT |
| npm/npx recovery | R1 worker return Command Evidence: node/npm/npx all resolved in execution shell | reconfirmed by R2 worker before any call | PENDING_WORKER_PREFLIGHT |
| model selection | same exact model as R1; already hardcoded in the canonical route with no stale reference | `qwen3.7-flash` unchanged | ACCEPT |
| free-quota ledger snapshot | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `qwen3.7-flash` row: `freeQuotaRemaining` 1,000,000 / `freeQuotaTotal` 1,000,000; `statusAtCapture` Enabled; `expirationDate` 2026-10-22; `captureDate` 2026-08-15 | ACCEPT_AS_OF_CAPTURE_DATE; worker must independently reverify currency before relying on it |
| operator console toggle evidence | operator-provided Model Studio Free Quota screenshot captured 2026-08-15 and incorporated into this governed baseline | `qwen3.7-flash` row shows Stop-on-Exhaust enabled | ACCEPT_AS_OF_CAPTURE_DATE; not a same-session console pull |
| official free-quota mode documentation | `https://www.alibabacloud.com/help/en/model-studio/new-free-quota` (fetched 2026-08-15) | describes a "Free Quota Only" toggle that halts service with error `AllocationQuota.FreeTierOnly` and zero charge once quota is exhausted | ACCEPT |
| operator ceiling | existing bounded-live authorization | at most 3 cumulative calls and US$1 total; R1 consumed zero calls | ACCEPT |
| live proof | `AGENTS.md` Mandatory Live Governance Proof | real provider call required for acceptance | PENDING_WORKER |

The operator allows API keys to be used by reference for this test. Values may
never be printed, copied, logged, persisted, or committed.

## Scope And Non-Goals

Scope is exactly one release-gate-bundle execution using synthetic,
non-sensitive input and secret-safe evidence, gated by fresh free-quota
console/documentation evidence instead of R1's official-pricing evidence. The
canonical SOT3 path must make exactly one real Alibaba/DashScope call. No
source, test, configuration, roadmap, registry, session, handoff, environment
file, deployment, public repository, or production system may be mutated.
This dispatch turn makes no API call and no live compatibility claim.

## Provider And Model Selection Rule

- Provider route: Alibaba/DashScope-compatible only.
- Exact model: `qwen3.7-flash`; snapshot reference: `qwen3.7-flash-2026-07-15`
  (unchanged from R1).
- Canonical route:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`.
- Accepted key aliases: `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`,
  `CVF_ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`.
- The worker must not fall back to `qwen-turbo`, substitute any other model,
  or select another provider.

## Free-Quota Cost Gate (Replaces R1's Official-Pricing Gate)

Before any provider call, the worker must establish all of the following from
current evidence, not from the R1 return or the 2026-08-15 ledger capture
alone:

1. **Current governed console evidence.** Re-verify the free-quota status for
   `qwen3.7-flash` is still current: cross-check
   `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json`
   against the current date (2026-08-15 execution date must be on or before
   `expirationDate` 2026-10-22 for the `qwen3.7-flash` row). If the worker has
   no way to pull a fresher-than-ledger console reading in this environment,
   the worker must record the ledger `captureDate` and treat the ledger as the
   most current available governed evidence, explicitly noting it is not a
   same-session live console pull.
2. **Free Quota Only / Stop-on-Exhaust must be enabled.** Cite official
   Alibaba documentation
   (`https://www.alibabacloud.com/help/en/model-studio/new-free-quota`) for
   the exact behavior: with the toggle enabled, exceeding the free quota halts
   the call with `AllocationQuota.FreeTierOnly` and applies zero charge. The
   worker must confirm the state from the committed operator console evidence
   above when execution remains on capture date 2026-08-15, or from a fresher
   console observation. The committed screenshot is confirmation, not an
   assumption; disclose when no same-session console pull is available.
3. **Remaining quota must exceed the request ceiling.** The fixed one-call
   request is bounded at `max_tokens` 4096 output; the ledger's
   `freeQuotaRemaining` (1,000,000 as of 2026-08-15 capture) must be
   verified greater than a conservative worst-case total-token estimate for
   one bounded request before the call.
4. **Official Alibaba free-quota documentation citation is mandatory**,
   parallel to R1's mandatory pricing-page citation: record the exact URL,
   access date, and the quoted behavior (toggle name, halt error code,
   zero-charge-on-halt guarantee).
5. **Preflight receipt goes to a dedicated R2 evidence path**, not reused
   from R1: `docs/reviews/evidence/cadp-ai-t6-r2-free-quota-preflight-2026-08-15.json`.
   This receipt must record the four points above plus the R2
   executionBaseHead, before the primary command runs.
6. If any of points 1 through 4 cannot be established with current evidence,
   the worker stops with `BLOCKED_WITH_REASON` and zero calls, exactly as the
   R1 gate required for pricing.

This replaces R1's "official pricing source plus arithmetic worst-case bound
below US$1" gate. It does not relax the ceiling below; it substitutes a
different, operator-directed evidence class (quota-exhaustion hard-stop
plus zero-charge-on-halt) for the same underlying goal (bounded financial
exposure).

## Environment Preflight Gate

Unchanged from R1: before any provider call, the worker must capture
secret-safe results for `where.exe node`, `where.exe npm`, `where.exe npx`,
`node --version`, `npm --version`, and `npx --version` in the same PowerShell
process used for the live command, through the active NVM4W nodejs path. The
worker must also run the bundle `--dry-run` and the focused local route
negative gate (`python scripts/run_cvf_sot3_a4_failure_recovery_proof.py
--local-only --json --receipt docs/reviews/evidence/cadp-ai-t6-r2-local-negative-receipt-2026-08-15.json`). Any missing executable, path mismatch, unrelated dirty
path, or failed local gate requires `BLOCKED_WITH_REASON` with zero calls.

## Cost And Call Ceiling

- Maximum cumulative real provider calls across R1 and R2 combined: 3;
  expected and accepted count for R2: 1. R1 made 0 calls, so R2's ceiling is
  unconsumed.
- Total charge ceiling: US$1, unchanged. The free-quota gate's expected
  outcome is US$0 (zero-charge Free Quota Only halt behavior applies only on
  exhaustion; a single bounded in-quota call is expected to cost nothing
  against the free allocation), but the worker must not assume zero cost
  without the Free-Quota Cost Gate evidence above.
- No probe call and no blind retry. A second call requires a recorded,
  result-changing remediation and must remain inside both ceilings.

## Synthetic Input, Data Retention, And Secret Handling

Unchanged from R1. Only repository-defined synthetic non-sensitive input is
permitted. Secrets load from
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` through
`scripts/_local_env.py`; only alias names and `PRESENT_REDACTED`, `EMPTY`, or
`NOT_FOUND` status may appear in evidence. Raw provider bodies, bearer tokens,
signed headers, and key values must never be written to the repository.

## Diagnostic And Retry Protocol

Follow `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`.
Before the first call, record executable resolution, secret-alias presence,
dry-run selection, the four Free-Quota Cost Gate points, and call counter. On
failure, partial result, timeout, or ambiguity, stop and record stage, class,
retryable, userAction, safeMessage, and HTTP status when available. No blind
retry is authorized.

## Evidence Output Paths

- `docs/reviews/CVF_CADP_AI_T6_R2_QWEN37_FLASH_FREE_QUOTA_COST_GATE_RETRY_WORKER_RETURN_2026-08-15.md`
- `docs/reviews/evidence/cadp-ai-t6-r2-free-quota-preflight-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r2-release-gate-result-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r2-release-gate-manifest-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r2-sot3-diagnostic-2026-08-15.json`
- `docs/reviews/evidence/cadp-ai-t6-r2-e2e-diagnostic-2026-08-15.json`

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| release command and outputs | LITERAL_INVARIANT | `scripts/run_cvf_release_gate_bundle.py` | argparse | `--e2e`; JSON and diagnostic flags | release bundle | ACCEPT |
| env loading | LITERAL_INVARIANT | `scripts/_local_env.py` | `bootstrap_repo_env` | `DEFAULT_ENV_FILES` | local env bootstrap | ACCEPT |
| exact one-call admission | VALUE_SET | `scripts/run_cvf_sot3_a5_release_proof.py` | admission constants | `REQUIRED_RECOVERY_PROVIDER_CALL_COUNT` | SOT3 A5 | ACCEPT |
| canonical live test | VALUE_SET | `scripts/run_cvf_sot3_a4_failure_recovery_proof.py` | live path and aliases | `LIVE_TEST_RELATIVE_PATH`; `ALIBABA_KEY_ALIASES` | SOT3 A4 | ACCEPT |
| selected model | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts` | Alibaba live request | `qwen3.7-flash` | SOT3 route | ACCEPT |
| governed quota facts | VALUE_SET | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `qwen3.7-flash` model row | `freeQuotaRemaining`; `freeQuotaTotal`; `expirationDate`; `statusAtCapture` | Alibaba free-quota ledger | ACCEPT |
| R1 blocker and reviewer acceptance | VALUE_SET | `docs/reviews/CVF_CADP_AI_T6_R1_QWEN37_FLASH_LIVE_COMPATIBILITY_RETRY_WORKER_RETURN_2026-08-15.md` | top `Status:` line and Reviewer Acceptance Note section | `REVIEWER_ACCEPTED_BLOCKED_R1_REOPEN_R2_SAME_MODEL` | R1 worker return | ACCEPT |
| live proof requirement | LITERAL_INVARIANT | `AGENTS.md` | Mandatory Live Governance Proof | real API call | root carrier | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition`; `Reviewer Closure Conversion`; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirmation and evidence after source read-ahead, not first discovery |
| claimBoundary | checker success does not prove a provider call, compatibility, or that the free-quota toggle is actually enabled at execution time |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id CADP-AI-T6-R2 --title "CADP AI T6 R2 Qwen3.7 Flash Free Quota Cost Gate Retry" --date 2026-08-15 --base c607779d31771dbdd9e789baf69ba297e01de2f5 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | runtime-provider-live, no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | source verification, handoff, reviewer conversion, trace, delta and public disposition |
| manualEditsAfterScaffold | bound R1 reviewer-accepted blocker, free-quota cost gate replacing pricing gate, official free-quota documentation citation, dedicated R2 evidence paths |
| checkerReadAheadConfirmation | applicable checker sources read before authoring |
| docOnlyNewFields | Free-Quota Cost Gate section introduces no new machine-checked schema field; it is prose-governed worker guidance |
| claimBoundary | packet authoring only; no provider action |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact R2 paths | both absent before authoring (`Test-Path`/file-existence check) | ABSENT_BEFORE_AUTHORING |
| bounded token search | `rg`-equivalent search found no prior `CADP-AI-T6-R2` owner | NO_COLLISION |
| R1 | R1 worker return and reviewer acceptance note remain immutable evidence, reused as source not duplicated | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |
| "Free Quota Only" / "Stop-on-Exhaust" terminology | searched repository for prior governed use; none found | NO_COLLISION_NEW_EVIDENCE_CLASS |

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
| liveProofAuthorized | YES, only after packet acceptance and preflight PASS including the Free-Quota Cost Gate |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | source verification at dispatch HEAD; worker must execute fresh proof including a fresh free-quota gate check |
| reason | R1 made zero calls and cannot serve as live evidence; the free-quota ledger capture date must be reverified as still current by the worker |
| requiredFutureAction | worker runs exact packet and returns uncommitted evidence including the dedicated preflight receipt |

## Acceptance Matrix And Stop Conditions

| Criterion | Required state |
|---|---|
| executable preflight | node/npm/npx resolve and report versions in worker shell |
| provider/model | Alibaba/DashScope and exact `qwen3.7-flash`, unchanged from R1 |
| free-quota cost gate | current console/ledger evidence, Free Quota Only toggle status recorded, remaining quota above ceiling, official documentation cited |
| live evidence | one real non-mock SOT3 call |
| ceilings | exactly 1 call accepted for R2; cumulative at most 3 across R1+R2; total below US$1 |
| evidence | exact seven R2 paths and secret-safe content |
| repository state | staging empty and HEAD unchanged |

Any failed preflight, missing key alias, free-quota-gate uncertainty, local
gate failure, ceiling risk, timeout, ambiguous result, or forbidden-scope need
stops execution and yields `BLOCKED_WITH_REASON`.

## Decision / Baseline

Proceed with one bounded R2 proof only after every executable, local-test,
credential-presence, and free-quota-gate preflight passes. The worker must use
exactly `qwen3.7-flash`, create only the seven governed R2 evidence paths, and
leave the repository uncommitted for independent review.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | release bundle and SOT3 A5/A4 | bounded live evidence only | future R2 return | none | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no invocation or mutation authority | T5 remains separate | fresh packet required | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

| Field | Requirement |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | no-commit worker then independent reviewer/closer |
| phase | worker execution pending |
| baseHeadFor(phase) | dispatchBaseHead=`8ce45e190b16f9dc262ef672016fa758d9d04daa`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| executionBaseHead | worker records exact clean dispatch HEAD |
| dirtyPathPolicy | zero unrelated dirty paths; the historical SOT3 receipt must remain unchanged |
| changedSetScope(phase) | exact seven-path R2 manifest |
| traceScope(phase, actor) | reads, commands, free-quota-gate checks, diagnostics, calls, cost, diff and status |
| operationReceiptWriteOrder | preflight receipt first, then evidence JSONs, worker return written last |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | no R1 or unrelated path mutation |
| nextMoveSurfaces | reviewer acceptance/closure then separate session sync |
| commitBoundary | staging empty; worker must not commit |

## Reviewer Closure Conversion

The independent reviewer must verify the real-call receipt, exact model,
free-quota-gate evidence and official documentation citation, ceilings,
secret safety, seven-path manifest, and clean no-commit boundary. Only the
reviewer may convert evidence into closure and roadmap/session projection.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local repository tools plus two official Alibaba documentation fetches (pricing page confirmation of the R1 gap, free-quota-mode documentation) |
| Session or invocation | CADP-AI-T6-R2 dispatch, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | file reads, web documentation fetch, governed scaffold helper, repository guards |
| Target paths | this baseline; paired R2 work order |
| Allowed scope source | operator instruction proposing `REVIEWER_ACCEPTED_BLOCKED_R1_REOPEN_R2_SAME_MODEL` with a free-quota-based cost gate, 2026-08-15 |
| Before status evidence | clean HEAD `8ce45e190b16f9dc262ef672016fa758d9d04daa` with R1 accepted-blocked committed and handoff anchored; both R2 paths absent |
| After status evidence | this baseline and the paired R2 work order only, before validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only; zero API calls |
| Claim boundary | authoring and local guard results plus two official documentation fetches only |
| Agent type | single dispatcher role |
| Invocation ID | `cadp-ai-t6-r2-dispatch-2026-08-15` |
| Expected manifest | this baseline; paired R2 work order |
| Actual changed set | this baseline; paired R2 work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | CADP-AI-T6-R2 dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or compatibility is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no live receipt in dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no provider action occurred |
| invocationBoundary | local source verification, two documentation fetches, and document authoring |
| interceptionBoundary | no wrapper, proxy, hook, or process interception |
| claimLanguage | bounded future retry authorization |
| forbiddenExpansion | no production, universal-provider, deployment, public-export, or T5 claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private credentials and private provenance workflow; no public-sync
authorization or evidence exists.

## Claim Boundary

This baseline authorizes only the bounded future R2 live proof under the
free-quota cost gate. It neither asserts compatibility nor authorizes
production mutation, deployment, public sync, external CLI/MCP use, or
worker commit. It does not itself verify that the account-level Free Quota
Only toggle is enabled at execution time; the worker must establish that
before any call.
