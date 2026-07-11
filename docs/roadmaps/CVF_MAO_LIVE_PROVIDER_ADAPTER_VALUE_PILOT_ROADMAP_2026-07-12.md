# CVF MAO Live Provider Adapter Value Pilot Roadmap

Memory class: FULL_RECORD

Date: 2026-07-12

Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN

Roadmap ID: MAO-LIVE

## Purpose

Determine whether one live provider-backed MAO worker-reviewer-revision-closer
chain creates enough evidence value to justify its added latency and cost over
one direct provider call.

## Authorization / Decision

The operator selected one bounded live pilot after the canonical CVF live
governance bundle passed at evidence commit `a0b40ecfb`. This roadmap authorizes
packet authoring only until a fresh GC-018 and source-verified work order pass
pre-dispatch gates.

## Current Evidence

- MAO T0-T9 deterministic local foundation is closed at `29c55ca36`.
- Canonical CVF live governance proof is PASS at `a0b40ecfb`.
- Model Gateway already owns an OpenAI-compatible live execution harness.
- No live MAO-to-Model-Gateway bridge or comparative value receipt exists.

## Scope

One private provenance-only bridge, one same-task comparison, one provider
lane, and at most four live calls.

## Non-Goals

No durable queue, scheduler, UI, public-sync, provider parity, prompt tuning,
production deployment, or broad MAO redesign.

## Design Control Gate

The bridge must reuse Model Gateway credential and execution boundaries, keep
MAO reviewer/closer separation, and persist only secret-safe receipts. Any need
to bypass those owners blocks implementation.

## Work Plan

1. Author and gate the fresh GC-018/work order.
2. Implement the thin bridge and deterministic negatives.
3. Run the same-task direct and governed live lanes once within budget.
4. Independently review receipts and issue the value verdict.
5. Close or reject further investment, then sync session state separately.

## Verification / Evidence

Required evidence includes focused tests, typecheck, live diagnostics, exact
call count, latency/usage comparison, receipt completeness, secrets scan,
worker-return fast gate, and committed-range closure gates.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| live execute adapter factory exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported factory | `createOpenAiCompatibleExecuteAdapter` | Model Gateway live proof harness | ACCEPT |
| live harness options exist | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported interface | `LiveProofHarnessOptions` | Model Gateway live proof harness | ACCEPT |
| MAO invocation contract exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | invocation request/result | `MaoInvocationRequest` | MAO delegation adapter | ACCEPT |
| local representative chain exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/representative.pilot.contract.ts` | full pilot function | `runPilotChain` | MAO representative pilot | ACCEPT |
| canonical live bundle exists | EXISTS | `scripts/run_cvf_release_gate_bundle.py` | main entrypoint | `main` | release gate bundle | ACCEPT |

## MAO-LIVE-T1 - Thin Bridge And Comparative Live Pilot

Dependency: fresh GC-018 and source-verified work order.

Deliverables:

- one thin adapter mapping MAO invocation/diagnostic/usage receipts to the
  existing Model Gateway live execution boundary;
- one direct-call baseline and one governed MAO chain using the same bounded
  task, model lane, scoring rubric, and secret-safe input;
- one worker, one identity-distinct reviewer, at most one revision, and one
  designated closer;
- maximum four live provider calls for the entire accepted run;
- deterministic local negatives for self-approval, timeout, budget, duplicate,
  malformed output, and retry ambiguity;
- command-backed latency, usage, receipt-completeness, and quality comparison;
- one explicit decision: `VALUE_PROVEN`, `VALUE_NOT_PROVEN`, or
  `BLOCKED_LIVE_PROVIDER`.

## Acceptance Criteria

- Both lanes use the same task and grading rubric.
- Raw keys, prompts containing secrets, and provider payloads are never stored.
- Every live failure receives a diagnostic before any retry.
- MAO receipts reconstruct worker, review, revision, closer, usage, and final
  decision without treating worker output as reviewer authority.
- Added evidence or quality must be material enough to justify measured latency
  and call-count cost; otherwise the result is `VALUE_NOT_PROVEN`.
- A PASS does not authorize durable queue, UI, public-sync, or production use.

## Stop Rules

- Stop after four live calls total.
- Stop immediately on credential, policy, secret-safety, or ambiguous-side-effect failure.
- Do not tune prompts broadly or rerun merely to obtain a preferred verdict.
- One bounded repair is the maximum.

## Negative And Fail Conditions

- Direct and MAO lanes use different tasks/models/rubrics.
- Reviewer consumes worker conclusions as authority.
- A retry occurs before the prior failure is diagnosed.
- Evidence omits latency, usage, call count, or receipt completeness.
- Any key or raw secret-bearing payload is printed or persisted.
- Local/mock evidence is presented as live MAO provider proof.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | source verification columns, epistemic fields, export token, trace labels |
| gateRunPurpose | roadmap authoring confirmation |
| claimBoundary | packet authoring route only; no new live MAO result |

## Epistemic Process Block

### Expected Result / Prediction

The MAO lane may improve evidence quality but will cost more calls and latency.

### Evidence Comparison

No same-task direct-versus-MAO live comparison exists yet.

### Contradiction Or Gap Disposition

Run one bounded comparative pilot rather than infer value from local tests.

### Claim Update

Live MAO value is unproven pending MAO-LIVE-T1.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Next Allowed Move

Roadmap closed. Do not continue MAO live investment unless a materially harder
task and measurable reopen hypothesis receive fresh operator authorization.

## Claim Boundary

Decision-first live pilot planning only; no live MAO adapter or value claim yet.
