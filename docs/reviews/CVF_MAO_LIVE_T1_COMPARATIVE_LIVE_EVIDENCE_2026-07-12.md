# CVF MAO-LIVE-T1 Comparative Live Evidence

Memory class: FULL_RECORD

docType: review

Status: EVIDENCE_RECORDED

Date: 2026-07-12

Batch ID: MAO-LIVE-T1

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_LIVE_T1_PROVIDER_ADAPTER_VALUE_PILOT_2026-07-12.md`

executionBaseHead: `e70d7a2ba`

## Purpose

Record command-backed direct-lane and MAO-lane live comparison metrics,
diagnostics, receipt completeness, and the terminal value verdict for the
selected task, using exactly one provider lane and at most four live calls
total, per
`docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md`.

## Target / Source

Target: one live comparative run of
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts`
through
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts`,
executed once against a real provider.

Source: the MAO-LIVE-T1 work order and GC-018 baseline; the existing Model
Gateway live proof harness
(`EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`); the MAO
delegation adapter, reviewer isolation, dissent/revision, and closer
interlock contracts (`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/`);
the written comparative receipt at
`docs/reviews/evidence/mao-live-t1-comparative-receipt-2026-07-12.json`.

## Scope / Methodology

Ran the local fake-fetch focused test suite and TypeScript typecheck first
(both PASS - see the paired worker return for exact counts). Confirmed a
live provider key alias was present in the local environment without
printing its value. Ran the live runner script once, which executed
exactly two live calls total (direct lane: 1 call; MAO lane: 1 worker call,
0 revision calls since the first attempt passed the shared rubric). Read
the runner's secret-safe JSON receipt directly and scanned it for
key-shaped patterns before including any of its content in this packet.

## Bounded Live Run Summary

| Field | Value |
|---|---|
| Provider lane | `alibaba` (DashScope, international endpoint) |
| Model | `qwen3.7-plus` |
| Task prompt | "List exactly three prime numbers between 10 and 20, separated by commas, and output nothing else." |
| Shared rubric | deterministic local scorer: non-empty (10 pts), within 120-char length ceiling (10 pts), proportional credit for matching 3 required whole-word tokens (`11`, `13`, `17`, any 3-of-4 valid; 80 pts max); `passed` requires all three conditions |
| Total live calls spent | 2 of 4 |
| Revision used | NO (first MAO worker attempt passed the rubric) |
| Started at | `2026-07-11T17:51:44.170Z` |
| Finished at | `2026-07-11T17:52:16.622Z` |

## Direct Lane

| Field | Value |
|---|---|
| Calls spent | 1 |
| Result | ok |
| Latency | 14705 ms |
| Usage | inputTokens=33, outputTokens=742 |
| Response length | 10 characters |
| Response preview | `11, 13, 17` |
| Rubric score | 100/100 (passed) |
| Matched tokens | `11`, `13`, `17` |
| Diagnostic | none |

## MAO Lane

| Field | Value |
|---|---|
| Calls spent | 1 (worker only; 0 revision) |
| Result | ok |
| Total latency | 17744 ms |
| Revision used | NO |
| Review count | 1 |
| Review decisions | `ACCEPT` |
| Integration (closer) decision | `ACCEPT` |
| Final response length | 10 characters |
| Final response preview | `11, 13, 17` |
| Final rubric score | 100/100 (passed) |
| Matched tokens | `11`, `13`, `17` |
| Diagnostic | none |

The MAO lane's independent reviewer recomputed the rubric score from the
worker's received response text directly (the same `scoreAgainstRubric`
function used for the direct lane), rather than trusting any worker
self-report, and the closer's integration decision (`ACCEPT`) required that
recomputed review's terminal decision to be `ACCEPT` before finalizing -
see `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts`
`runMaoReviewPhase`/`runMaoLane`.

## Latency And Cost Comparison

| Metric | Direct lane | MAO lane | Delta |
|---|---|---|---|
| Live calls | 1 | 1 | 0 |
| Latency | 14705 ms | 17744 ms | +3039 ms (+20.7%) |
| Rubric score | 100/100 | 100/100 | 0 (tie) |
| Output tokens | 742 | 742 (same underlying call) | 0 |

Both lanes used the identical task, model, and rubric, per the roadmap's
acceptance criterion. The MAO lane's added review/closer machinery cost
additional wall-clock latency (local computation only; it made no
additional live call) without producing a higher-scoring output on this
one run, since the direct lane's single response already satisfied every
rubric requirement.

## Receipt Completeness

| Receipt element | Present | Evidence |
|---|---|---|
| Worker invocation identity/timing | YES | `mao.direct`/`mao.mao` latency and call-count fields in the JSON receipt |
| Review decision | YES | `reviewDecisions: ["ACCEPT"]` |
| Revision count | YES | `revisionUsed: false`, `callsSpent: 1` |
| Closer integration decision | YES | `integrationDecision: "ACCEPT"` |
| Usage (input/output tokens) | YES | direct lane `usage.inputTokens=33`, `usage.outputTokens=742` |
| Final decision reconstructable without secrets | YES | every field in the JSON receipt is a count, boolean, score, or truncated (60-char) response preview; no key, header, or raw provider request/response body is present |

## Secret-Safety Scan

Command: manual grep of
`docs/reviews/evidence/mao-live-t1-comparative-receipt-2026-07-12.json` for
key-shaped patterns (`sk-[A-Za-z0-9]{16,}`, `Bearer [A-Za-z0-9._-]{16,}`).

Result: PASS - zero matches. The receipt contains only the provider/model
IDs, endpoint host (not full URL with any query string), the key alias
*name* used (`DASHSCOPE_API_KEY`, not its value), call counts, latencies,
usage token counts, rubric scores, and 60-character response-text previews
of a graded arithmetic answer (no secret-bearing content is possible in a
"list three prime numbers" response).

## Diagnostics

No live call failed on this run; no diagnostic was raised, and no retry was
required. The runner's diagnose-before-retry discipline
(`docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md`
Stop Rules) was not exercised because the first MAO worker attempt already
passed the rubric.

## Findings / Position

Both lanes produced an identical, fully correct answer on this one bounded
run (rubric score 100/100 on both sides). The MAO lane's independent
review/revision/closer machinery added real wall-clock latency (+20.7%)
without adding any material evidence value over the direct lane's already-
correct response, and it consumed the same one live call as the direct
lane since no revision was triggered. Per the roadmap's acceptance
criterion ("Added evidence or quality must be material enough to justify
measured latency and call-count cost; otherwise the result is
`VALUE_NOT_PROVEN`"), this run does not demonstrate value.

## Risk / Corrective Action

None required. The run completed within the four-call ceiling (2 of 4
spent), used one provider lane, one task/model/rubric shared by both
lanes, at most one revision (not triggered), and no key or raw
secret-bearing payload was printed or persisted. No rerun was performed to
seek a different verdict, per the roadmap's explicit prohibition on
rerunning "merely to obtain a preferred verdict."

## Decision / Recommendation / Disposition

**Verdict: `VALUE_NOT_PROVEN`**

Reason: the MAO lane's rubric score (100) does not exceed the direct
lane's rubric score (100) on this bounded run; the added latency and
governance-chain overhead is not justified by any measurable quality or
evidence gain for this deterministic, single-call-sufficient task.

Recommend the reviewer/closer record this as one bounded, honest negative
result rather than iterate the task to seek a `VALUE_PROVEN` verdict,
consistent with the roadmap's Stop Rules. A future task selected
specifically to exercise the MAO lane's revision/repair value (e.g., a
task where a single provider response is more frequently malformed or
incomplete) would be a more discriminating test, but selecting such a task
is a reviewer/closer or fresh-roadmap decision, not a rerun of this pilot.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live multi-agent provider adapter pilot`,
role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | review-docType heading groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition); full Agent Operation Trace Block label set; Epistemic Process Block four subsections; `ALLOWED_DISPOSITIONS` public-export enum |
| gateRunPurpose | confirmation ahead of worker-return fast gate |
| claimBoundary | one bounded live comparative run only; no production or provider-parity claim |

## Epistemic Process Block

### Expected Result / Prediction

Per the roadmap's own Epistemic Process Block: "The MAO lane may improve
evidence quality but will cost more calls and latency." The prediction was
that the MAO lane would either cost more without improving quality (a
`VALUE_NOT_PROVEN` result) or would improve quality enough to justify the
added cost (`VALUE_PROVEN`), with the actual outcome depending on whether
the direct lane's single response already satisfied the rubric.

### Evidence Comparison

Confirmed the "costs more, does not improve quality" branch of the
prediction: the direct lane's single call already scored 100/100, so the
MAO lane's reviewer had nothing to repair (no revision was triggered) and
could only match, not exceed, the direct lane's score, while still
incurring additional latency from its review/closer computation.

### Contradiction Or Gap Disposition

No contradiction. This is the expected negative branch of the roadmap's own
stated prediction, now backed by one real bounded live run rather than
inference.

### Claim Update

MAO-LIVE-T1 proves that, for this one deterministic single-call-sufficient
task, the governed MAO chain does not add measurable value over a direct
call. It does not prove the MAO chain never adds value - a task class
where single-call outputs are less reliable was not tested. No provider
parity, production readiness, durable queue, or UI claim is made.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated live-pilot worker |
| Provider or surface | Alibaba DashScope (international endpoint), via existing Model Gateway live harness |
| Session or invocation | MAO-LIVE-T1 comparative live run 2026-07-12 |
| Working directory | repository root and `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` |
| Command or tool surface | `npx tsx scripts/run-mao-live-provider-value-pilot.ts` |
| Target paths | this comparative evidence packet; `docs/reviews/evidence/mao-live-t1-comparative-receipt-2026-07-12.json` |
| Allowed scope source | MAO-LIVE-T1 work order Work-Order Fulfillment Manifest |
| Before status evidence | clean execution HEAD `e70d7a2ba`; live key alias present (unprinted); call ledger at 0/4 |
| After status evidence | 2/4 live calls spent; both lanes `ok=true`; verdict `VALUE_NOT_PROVEN` |
| Diff evidence | `git diff --name-status` / `git status --short` |
| Approval boundary | one bounded live comparative run only |
| Claim boundary | one live value comparison; no production, provider-parity, or broader claim |
| Agent type | delegated live-pilot worker |
| Invocation ID | `mao-live-t1-comparative-run-2026-07-12` |
| Expected manifest | this evidence packet |
| Actual changed set | this evidence packet |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This packet records one bounded, secret-safe live comparative run only. It
does not claim provider parity, production orchestration readiness,
durable queue behavior, UI, or public-sync readiness. The `VALUE_NOT_PROVEN`
verdict applies to this one task/model/rubric combination and does not
generalize to all possible MAO-governed live tasks.
