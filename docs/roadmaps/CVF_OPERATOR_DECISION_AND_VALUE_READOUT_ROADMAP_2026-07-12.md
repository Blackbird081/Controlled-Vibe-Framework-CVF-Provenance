# CVF Operator Decision And Value Readout Roadmap

Memory class: FULL_RECORD

Date: 2026-07-12

Status: CLOSED_VALUE_NOT_PROVEN

Roadmap ID: ODVR

## Purpose

Reduce the number of governed files an operator must inspect to answer five
questions: what mode CVF is in, what decision just closed, what value is
proven, what remains parked, and what may happen next.

## Authorization / Decision

The operator selected this roadmap before returning to absorption of a newly
chosen external repository. This roadmap authorizes ODVR-T0 packet authoring
only. Implementation requires a fresh GC-018, a source-verified work order,
and successful pre-dispatch gates.

## Current Evidence

- Active session state already owns `currentMode` and `nextAllowedMove`.
- The bootstrap read model already provides a compact startup projection.
- MAO-T7 already provides a task-graph evidence readout and freshness class.
- MLW-NRD1 already provides a route-visible advisory decision readout.
- The Web Workspace already has operator dashboard and lane-summary read
  models.
- MAO-LIVE-T1 proved that a final verdict can be value-negative even when the
  implementation and governance proof pass.

These surfaces solve narrower problems. None is authority for a cross-lane
operator answer that joins the latest decision, its value verdict, its claim
boundary, its reopen condition, and the canonical next move.

## Scope

A private, deterministic, read-only decision and value projection over
explicitly allowlisted CVF-governed sources. The initial implementation lane
is a local composer and CLI-readable JSON result. A Web or dashboard projection
is not part of the initial lane.

## Non-Goals

- No new source-of-truth store, mutable queue, or state registry.
- No autonomous lane selection, dispatch, mutation, commit, or push.
- No replacement of MAO-T7, MLW-NRD1, or Web Workspace read models.
- No provider call, live governance claim, public-sync, or production claim.
- No absorption or import of an external repository in ODVR.

## Design Control Gate

The projection must consume canonical owners without promoting completion
prose, provider memory, or UI state into authority. Every output field must
carry a source pointer and freshness result. Contradictory owners must produce
`CONTRADICTED`; the composer must not silently choose a preferred value.

The T0 overlap inventory must prove that each proposed field is absent from,
or materially broader than, the corresponding MAO-T7, MLW-NRD1, and Web
Workspace owner. A duplicate dashboard or duplicate truth store blocks T1.

## Work Plan

| Tranche | Objective | Required result | Release boundary |
|---|---|---|---|
| ODVR-T0 | Source and overlap inventory plus readout contract | field-level authority map, freshness rules, contradiction rules, JSON contract, representative fixtures | packet authoring only until fresh GC-018/work order passes |
| ODVR-T1 | Deterministic read-only composer | local library and CLI-readable JSON projection with focused positive, stale, missing-source, and contradiction tests | no Web/UI, mutation, provider, or external source intake |
| ODVR-T2 | Representative operator value proof | compare manual startup/decision reconstruction with the readout using one closed lane and one parked/reopen lane | UI remains value-gated; no broad rollout without proven reduction |

## Required Readout Contract

The bounded result must answer:

1. `currentMode` and active handoff.
2. Latest material decision and terminal value verdict.
3. Claim boundary and public export disposition.
4. Parked or blocked conditions, including a checkable reopen condition when
   one exists.
5. Canonical next allowed move.
6. Source anchors and aggregate freshness: `CURRENT`, `STALE`, or
   `CONTRADICTED`.

New field names are doc-only proposals until ODVR-T0 ratifies the contract.
They are not represented below as existing runtime fields.

## Acceptance Criteria

- Every projected value traces to one explicit canonical owner.
- The output is regenerated and read-only; it cannot become execution truth.
- Missing required sources fail closed and identify the missing owner.
- Contradictory current-mode, verdict, claim-boundary, reopen, or next-move
  values return `CONTRADICTED` with both source anchors.
- The output distinguishes implementation success from value proof.
- ODVR-T2 records operator steps, files read, elapsed time, and answer
  correctness for manual and composed paths.
- T2 may recommend continued use only if the composed path reduces file reads
  and operator steps without losing or altering a canonical fact.
- No UI tranche may open unless T2 proves value and the operator approves a
  separate fresh packet.

## Verification / Evidence

ODVR-T0 must provide repository-search evidence, a field-level overlap matrix,
source excerpts for every accepted owner, and negative evidence for every
claimed composition gap. ODVR-T1 must provide focused deterministic tests,
type or syntax checks applicable to its implementation language, sample JSON
readouts, and committed-range governance gates. ODVR-T2 must provide the two
same-question operator traces, recomputed step and file-read counts, elapsed
times, answer comparison, and an independent terminal value verdict.

No tranche may use a zero-change range as evidence for changed artifacts.

## Current Runtime Freshness Verification

| Item | Search or inspection evidence | Current disposition |
|---|---|---|
| active session generated owner | `governance/compat/generate_active_session_state.py` directly declares `currentMode` and `nextAllowedMove` in `BOOTSTRAP_FIELDS` | current canonical owner |
| compact startup projection | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` currently contains mode, handoff, next move, and claim boundary | current generated projection |
| MAO evidence readout | repository inspection found `MaoEvidenceReadout`, `buildEvidenceReadout`, and `classifyReadoutFreshness` in the MAO-T7 source | current narrower owner |
| MLW decision readout | repository inspection found `MlwNextRuntimeDecisionReadout` and its builder in the MLW-NRD1 source | current narrower owner |
| Web Workspace read model | repository search found the server read-model source and its workspace consumers/tests | current narrower owner; UI reuse requires later proof |
| full ODVR composer | repository search for `ODVR` and `Decision And Value Readout` found no pre-existing owner before this roadmap | absent as implementation; T0 must refresh this search before dispatch |

This verification records current repository state for roadmap authorization.
It does not claim that a composer, CLI, UI, or runtime behavior exists.

## Stop Rules

- Stop if T0 finds an existing canonical surface that already owns the full
  required result.
- Stop if the composer needs to infer a verdict or reopen condition from free
  prose without an allowlisted owner.
- Stop if freshness cannot be computed deterministically.
- Do not add UI, provider calls, or new repository absorption to rescue a
  value-negative T2 result.

## Negative And Fail Conditions

- UI, handoff prose, or provider-local memory is treated as canonical truth.
- A contradiction is hidden by source precedence.
- The readout writes session state or changes `nextAllowedMove`.
- An implementation PASS is presented as proof of operator value.
- T2 compares different operator questions or incomplete fact sets.
- ODVR is used to authorize absorption of an unnamed external repository.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| generated active session state owns current mode and next move | EXISTS | `governance/compat/generate_active_session_state.py` | `BOOTSTRAP_FIELDS` | `currentMode`; `nextAllowedMove` | active session state generator | ACCEPT |
| compact bootstrap projection exists | EXISTS | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | top-level fields | `currentMode`; `activeHandoff`; `nextAllowedMove`; `claimBoundary` | active session bootstrap read model | ACCEPT |
| MAO evidence readout exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | deterministic read-model projection | `MaoEvidenceReadout`; `buildEvidenceReadout`; `classifyReadoutFreshness` | MAO-T7 evidence/readout contract | ACCEPT |
| route-visible advisory runtime decision readout exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw-next-runtime-decision-readout.ts` | exported readout and builder | `MlwNextRuntimeDecisionReadout`; `buildMlwNextRuntimeDecisionReadout` | MLW-NRD1 readout | ACCEPT |
| Web Workspace read-model owner exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | exported workspace read-model surface | `cvf-workspace-read-model` | Web Workspace server read model | ACCEPT |
| local workspace projection foundation is closed bounded | VALUE_SET | `CVF_SESSION/state/entries/localWorkspaceProjectionReadModelClosure20260627.json` | `value.status` | `localWorkspaceProjectionReadModelClosure20260627` | active session state entry | ACCEPT |
| MAO live value verdict and quantified reopen condition exist | VALUE_SET | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` | `Status`, `Next Allowed Move` | `REVIEWER_ACCEPTED_VALUE_NOT_PROVEN`; `Concrete reopen condition` | MAO-LIVE roadmap | ACCEPT |

## Roadmap-To-Work-Order Trace Requirements

Every ODVR work order must map each authorized tranche requirement, output,
acceptance criterion, negative condition, and stop rule to an exact work-order
instruction and evidence path. Unmapped roadmap requirements block dispatch.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | source-verification columns; roadmap trace matrix; ADIF disclosure; export token; AHB route token; AOT trace labels |
| gateRunPurpose | confirmation and evidence for already completed source/read-ahead review; not first discovery; ODVR-T0 packet-authoring release only |
| claimBoundary | no implementation, UI, provider, public-sync, or external source intake |

## Epistemic Process Block

### Expected Result / Prediction

A compact composed readout should reduce operator navigation while preserving
the exact distinction between closure, value, parked conditions, and the next
allowed move.

### Evidence Comparison

Existing readouts are scoped to startup, one MAO task graph, one MLW route, or
the Web Workspace. Their overlap must be measured in T0, not assumed away.

### Contradiction Or Gap Disposition

T0 must classify each proposed field as reuse, compose, omit, or blocked. T1
opens only for fields that require cross-owner composition.

### Claim Update

Operator-friction reduction is unproven until ODVR-T2 compares the same
questions and canonical facts across manual and composed paths.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: ODVR closed with value not proven, so no public artifact is justified.
Public-sync boundary: no ODVR artifact may be copied, committed, or pushed to
the sibling public repository by this closure.

## Next Allowed Move

Author a fresh ODVR-T0 GC-018 baseline and source-verified no-commit work order.
After ODVR is accepted, parked, or rejected, the operator may select a newly
justified external repository or folder for source-mirror-backed absorption.
No external target is selected by this roadmap.

## T2 Closure Decision

ODVR-T2 is `REVIEWER_ACCEPTED_VALUE_NOT_PROVEN`. The composed path preserved
3 of 7 exact canonical facts for the closed lane and 0 of 7 for the
parked/reopen lane. It reduced navigation only for the globally-latest lane,
lost public-export disposition entirely, and could not answer the parked lane.
No UI tranche opens. ODVR is closed without further implementation; a future
reopen requires a new operator decision and fresh packet tied to a concrete
lane-scoping and missing-field hypothesis.

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| ODVR-T2-A1 | `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | `$.scenarios[0].factsPreserved` | 7 for value proof | 3 | FAIL_VALUE_THRESHOLD |
| ODVR-T2-A2 | `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | `$.scenarios[1].factsPreserved` | 7 for value proof | 0 | FAIL_VALUE_THRESHOLD |
| ODVR-T2-A3 | `docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json` | `$.scenarios[*].traces[*].rawEvents` | all declared totals recompute | four of four traces recompute | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md` | `Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN` | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_VALUE_NOT_PROVEN` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no mutation; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no mutation required | PASS |
| External evidence digest | N/A with reason: internal local measurement | no external evidence | N/A with reason |
| System loop interlock | T2 receipt and reviewed report | negative value result retained | PASS |
| Session continuity | separate session-sync after material commit | not part of material closure | N/A with reason |

## Claim Boundary

Decision-first roadmap and ODVR-T0 packet-authoring authorization only. No
composer, CLI, UI, provider/live proof, public-sync, autonomous decision,
session mutation, or external repository absorption is implemented or claimed.
