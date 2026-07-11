# CVF MAO-T8 Representative Pilot Selection Checkpoint

Memory class: FULL_RECORD

docType: review

Status: PILOT_SELECTED_FOR_DISPATCH

Date: 2026-07-11

## Purpose

Select the real bounded task and proof class required before MAO-T8 dispatch.

## Target / Source

The selected task uses the accepted MAO-T1 through T7 local contracts and the
MAO roadmap T8 acceptance boundary.

## Scope / Methodology

Execute one deterministic local task graph in which a worker produces an
operator evidence readout from seeded receipts, an independent reviewer detects
a deliberately stale readout, one classified revision regenerates the readout,
and one designated closer accepts only a consistent terminal receipt chain.

## Pilot Selection Decision

| Field | Selected value |
|---|---|
| pilotTaskId | `MAO-T8-LOCAL-STALE-READOUT-REPAIR` |
| task class | deterministic evidence-readout repair |
| proof class | `DETERMINISTIC_LOCAL_CONTRACT_PROOF` |
| provider disposition | `NO_PROVIDER_LOCAL_ONLY` |
| worker | delegated worker role |
| reviewer | independent reviewer identity distinct from worker |
| revision ceiling | exactly one classified revision allowed |
| closer | one designated closer identity distinct from worker/reviewer |
| concurrency ceiling | at most three execution roles |
| live-proof disposition | N/A with reason: no provider/runtime governance claim |

## Required Negative Scenarios

| Scenario | Required result |
|---|---|
| self-approval | rejected |
| duplicate execution/admission | rejected without duplicate side effect |
| timeout | terminal classified result, never inferred success |
| cancel | no new child starts after accepted cancellation |
| budget ceiling | graph or invocation rejected before over-budget execution |

## Findings / Position

The pilot is suitable because it exercises existing task-graph, lifecycle,
review, revision, closer, evidence, and readout contracts without inventing a
provider or production claim.

## Risk / Corrective Action

This is not a production orchestrator, durable queue, live provider proof, UI,
or throughput benchmark. Any missing integration surface must be reported as a
bounded T8 finding and may not be hidden behind test-only assumptions.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | review headings, epistemic fields, trace labels, public disposition |
| gateRunPurpose | pilot-selection confirmation before dispatch |
| claimBoundary | local deterministic pilot selection only |

## Epistemic Process Block

### Expected Result / Prediction

One stale readout can traverse worker, independent review, one revision, and
designated closer while each negative scenario fails closed.

### Evidence Comparison

Source inspection confirms the required individual contracts exist; T8 must
still prove their integrated use through fresh tests and receipts.

### Contradiction Or Gap Disposition

No integrated T8 proof exists yet, so dispatch creates only the bounded pilot
harness and evidence artifacts.

### Claim Update

The pilot task is selected; execution remains unproven until worker evidence is
independently reviewed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | MAO-T8 pilot selection 2026-07-11 |
| Working directory | repository root |
| Command or tool surface | source reads, resolver, patch, gates |
| Target paths | T8 selection checkpoint, baseline, and work order |
| Allowed scope source | operator instruction and MAO roadmap T8 dependency |
| Before status evidence | T7 closed; T8 held for fresh pilot selection |
| After status evidence | one local deterministic pilot selected |
| Diff evidence | `git diff --name-status` |
| Approval boundary | selection and dispatch authoring only |
| Claim boundary | no T8 execution or provider claim |
| Agent type | dispatcher |
| Invocation ID | `mao-t8-pilot-selection-2026-07-11` |
| Expected manifest | selection checkpoint plus refreshed T8 baseline/work order |
| Actual changed set | selection checkpoint plus refreshed T8 baseline/work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This checkpoint selects a local deterministic proof task only. It does not
prove MAO-T8 execution, provider behavior, production readiness, or public-safe
projection.
