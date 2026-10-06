# NCR - Alibaba completion and downstream error handling

Memory class: FULL_RECORD

docType: baseline

Status: LOCAL_IMPLEMENTED_VERIFIED_BOUNDED

Date: 2026-10-06

executionBaseHead: `45b1a48d4f97e221adcd3e3bd21610b54d6f5f5a`

## Purpose

Continue the wider execution backlog after the bounded P06 repairs. Separate
successful HTTP delivery from an explicitly truncated Alibaba generation so
receiving workflows do not treat incomplete output as a successful artifact.
Current scope is the consolidated operator follow-up below, superseding the
initial adapter-only manifest. This record preserves the earlier observations.

## Source Verification Block

| Source | Disposition | Finding |
|---|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts, executeAlibaba/parseAlibabaStreamingResponse | ACCEPT | JSON response ignores finish_reason; streaming parser captures it but caller ignores it; both return success for length-limited output |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts, Alibaba cases | ACCEPT | Existing complete/HTTP/error/SSE compatibility tests; explicit truncation not covered |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts, ExecutionResponse | ACCEPT | Existing success/error/usage/diagnostic shape supports bounded failure without new response fields |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts | ACCEPT | Existing output_validation_failed class, revise_request action and retryable false fit an explicit generation limit |
| docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md, Audience-Specific Briefs Before Intake | ACCEPT | HTTP compatibility, generation completion and semantic fidelity remain distinct; partial output must not become silent completed handoff |
| https://help.aliyun.com/en/model-studio/partial-mode | NOT_CVF_SOURCE | Official protocol reference: length denotes max_tokens limit; stop denotes natural/stop-word termination; not CVF authority or semantic approval |

## Decision / Scope

Operator `next` authorizes continued Local reversible maintenance. Standing
operator authorization permits autonomous Alibaba API tests; other providers are
excluded. Local owns technical disposition. No research/delegation worker is
dispatched. Preserve twenty-one prior material paths except the NCR roadmap
selection paragraph. Exactly two product paths: providers.ts and its existing
providers.test.ts; add this baseline and update the existing roadmap paragraph.

For explicit finish_reason=length, return success false with a concise incomplete
output error and existing output_validation_failed diagnostic (retryable false).
Do not expose the partial body as completed output. Preserve reported token usage
and duration. Apply to Alibaba JSON and the existing QVQ SSE parser/caller only.
Natural stop and legacy missing-reason responses retain their existing behavior;
missing finish reason is not newly certified complete. This does not validate
semantics, tool-call completion, all malformed SSE or reasoning-only responses.
No automatic retry, token-budget increase, model default/ranking, schema, new
checker, quota policy, billing claim or adapter changes for other providers.

## Evidence / Verification Plan

Add deterministic JSON/SSE truncation regressions; consume existing positive
controls. Live evidence uses the actual executeAI Alibaba adapter and Node fetch,
through an ignored TypeScript loading harness, not a mock response or full Web
runtime. Three sequential synthetic calls: pre-edit max_tokens=8 long-answer
counterexample, post-edit same bounded case, then max_tokens=256 short OK control.
Requested model qwen3.8-flash, previously observed in the operator account; no
default selection. Existing intl compatible endpoint only, 60-second timeout,
no automatic retries/fallback. Expected new output ceiling 272 tokens, not an
input/reasoning/billing ceiling. Actual reported usage/call count will be recorded.
Diagnostic before any failed/ambiguous repeat; standing authorization allows
bounded follow-up only with named information gain and cost reason.

Load verified local Alibaba/DashScope aliases in-process; print/persist no key,
authorization headers or raw request/response bodies. Persist source hashes,
prompt hashes, HTTP status, finish reason, usage, result status and diagnostic
summaries. Unexpected HTTP/model/finish outcome stops the harness for diagnosis.
Real calls prove the bounded adapter observation only, not CVF governance,
mandatory gateway, release readiness, end-to-end UI behavior or semantic fidelity.
Run focused provider tests, typecheck/lint and applicable static gates.

## Initial Verification Results

Preflight passed before edits/calls (preflight.log, 8.72s). Deterministic red:
both new JSON/SSE length cases failed against old source; 43 existing controls
passed (red.log, 8.90s). Green: 45/45 passed (green.log, 8.90s). Typecheck and
targeted lint exit 0; product-pair git diff --check passed. Source diff changes
the diagnostic import, one private failure builder and the two Alibaba branches.

Three actual calls through executeAI, requested/returned qwen3.8-flash, HTTP 200:

| Case | Finish reason | Adapter status | Reported total tokens | Latency ms |
|---|---|---|---|---|
| Before edit, long prompt/max_tokens=8 | length | success true, partial output 50 characters: defect reproduced | 205 | 4168 |
| After edit, same prompt/limit | length | success false; partial output withheld; usage and non-retryable diagnostic retained | 146 | 1657 |
| After edit, short OK/max_tokens=256 | stop | success true, output OK | 95 | 1300 |

New reported usage: 446 tokens, three calls, no retries/fallback. Actual completion
counts exceeded the requested tiny limit in the two length cases and included
reasoning accounting; a requested max_tokens value is not established here as a
hard billed-token ceiling. Pricing, quota decrement and billed cost are UNKNOWN.
Receipts preserve source/prompt hashes and safe summaries in
.cvf/runtime/ncr-alibaba-completion-20261006/ (before-1.json, after-1.json,
after-2.json). Before/after prompt hashes match; provider-source hashes differ.
The pre-edit receipt confirms the counterexample, not successful workflow output.
Post-edit repeat has named information gain: verify the exact classification
repair against a real length response; only one extra bounded negative call.

QVQ SSE classification is covered by deterministic fixtures only; a real QVQ
call was not required or executed. Missing-reason compatibility is retained,
not newly certified complete. This does not close full route/gateway/UI semantics,
retry cost accounting, semantic fidelity or general provider completion behavior.
The routed diagnostic standard path remains absent; existing archived text was
consulted as lookup context, without migrating its authority or changing routing.
Final applicable static confirmation is retained in final-static.log.

## Consolidated Operator Follow-Up - 2026-10-06

Operator `xu ly 1 lan cho tron ven` supersedes the earlier two-product-path
boundary for this completion/error batch. Local decision owner; implementation
and verification phase. Five product paths: existing provider pair, existing
execute/route-final-response.ts and route.test.ts, ProcessingScreen.test.tsx
(all below EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src). Preserve prior work.
No automatic roadmap successor or unrelated provider policy expansion.

Source verification: route-final-response.ts overwrote failed reported usage,
could emit successful workflow projection for empty success, and the exhausted
422 builder omitted diagnostic/usage. ProcessingScreen.tsx already conditions
completion on success/output and renders classified failures. These are CVF
source ACCEPT findings. Official Alibaba streaming reference
https://www.alibabacloud.com/help/en/model-studio/stream is NOT_CVF_SOURCE;
it separates reasoning_content from answer content and shows terminal stop.
Rejecting an unterminated/invalid stream is Local artifact-completion policy,
not a new upstream guarantee. Missing JSON finish reason retains compatibility.

Bounded repair: reject Alibaba empty/non-string answers and explicit non-stop
JSON completions; do not promote reasoning-only, malformed JSON chunks or SSE
without terminal stop into completed answers. Preserve reported usage including
SSE input/output breakdown. Final route strips failed partial output, normalizes
empty success, retains reported usage on failure and emits no completion/write
side effects for that response. Exhausted 422 retains last-attempt usage and
adds existing non-retryable diagnostic linked to its existing receipt. Existing
validation retry policy stays unchanged; no retry-cost aggregation or billing
accuracy claim. Failure telemetry cost estimation remains absent rather than
estimating input/output from withheld partial output or missing counts.

First composed run: 110/110 across provider, actual route and existing UI suites
passed (25.68s), before the final 422 diagnostic addition. These deterministic
tests establish transport/response/rendering behavior only; not AI governance.
Static autorun passed 85/85 in 8.53s after initial edits; this is not claimed as
a before-edit preflight. Final focused verification follows the 422 change.
Existing real-call receipts remain historical observations bound to earlier
source; final adapter gets two bounded synthetic Alibaba calls only after the
updated static gate passes. Information gain: unchanged length rejection and
natural-stop compatibility on the expanded adapter; no model comparison.
New receipts are isolated in .cvf/runtime/ncr-completion-batch-20261006/.

Follow-up trace: expected/actual manifest is five product paths above plus this
baseline and the existing roadmap selection paragraph. Prior delta retained;
no commit, push, public, deployment, state/handoff change or new checker.

Final follow-up results: 110/110 focused tests PASS in 24.03s (tests.log),
TypeScript exit 0 and targeted ESLint exit 0 (two pre-existing unused-parameter
warnings in the exhausted builder). Static preflight-final.log PASS 85/85,
9.09s, before provider calls. Initial follow-up static gate caught a duplicate
read-ahead heading; removed the duplicate and retained its failed log. Initial
typecheck caught optional failed usage incorrectly entering typed success cost
telemetry; separated resolved success usage from preserved raw failure usage.

Two final-source real Alibaba calls, HTTP 200, qwen3.8-flash: length/max_tokens=8
returned success false, no exposed output, usage 165; stop/max_tokens=256 returned
success true/OK, usage 94. Total 259 reported tokens, exactly two calls and no
retry/fallback/other provider. after-1.json and after-2.json retain source/prompt
hashes, finish reasons, duration, usage and diagnostics. These are new adapter
observations only. SSE and route/UI branches have deterministic coverage;
no browser, full live Web route, gateway, billing or release claim is made.
No more model sampling is needed to disposition this repair batch.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | Source/Decision/Evidence/Claim Boundary; read-ahead fields; complete trace labels; Resolver query; Returned defects; Public Export Disposition |
| gateRunPurpose | Confirm authored bounded scope/evidence; not first discovery of literals |
| claimBoundary | Static packet admission, not release/governance proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED. Zero candidates and no truncation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local implementer/reviewer |
| Provider or surface | Local workspace; Alibaba real API for bounded adapter evidence |
| Session or invocation | NCR Alibaba explicit truncation, 2026-10-06 |
| Working directory | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | Source reads, apply_patch, Vitest, Node live harness, typecheck/lint, static autorun |
| Target paths | Five product paths in the consolidated follow-up; baseline; existing NCR roadmap |
| Allowed scope source | Operator next and consolidated completion request; standing Alibaba test authorization |
| Before status evidence | Twenty-one prior modified/untracked material paths; provider pair initially clean |
| After status evidence | Consolidated batch: 110/110 focused, typecheck/lint, static gate and two final-source real adapter calls pass |
| Diff evidence | git diff for provider pair and roadmap; baseline untracked |
| Approval boundary | Local reversible maintenance and bounded Alibaba calls; no other effects |
| Claim boundary | Explicit length-limited Alibaba generation status only |
| Agent type | Local implementer/reviewer |
| Invocation ID | NCR-ALIBABA-LENGTH-20261006 |
| Expected manifest | Provider pair, route-final-response.ts, route.test.ts, ProcessingScreen.test.tsx, baseline and roadmap paragraph |
| Actual changed set | Expected manifest; prior delta retained |
| Manifest delta | MATCH consolidated follow-up; three product paths added to initial manifest by fresh operator request |

## Claim Boundary

Adapter completion classification is distinct from semantic correctness,
governance enforcement and billed cost. Alibaba completion validity plus
downstream failure usage/diagnostics are addressed within the declared batch.
Existing pending readiness/rights/data/production checkpoints remain parked.
No commit, push, public release or deployment is requested.
Material remains uncommitted. Return to the wider backlog; no automatic model
survey, completion-policy expansion or release successor follows this sample.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - local repair and bounded Alibaba evidence.
