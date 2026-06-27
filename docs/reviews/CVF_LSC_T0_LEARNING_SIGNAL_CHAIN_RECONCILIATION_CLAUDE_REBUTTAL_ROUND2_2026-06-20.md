# CVF LSC-T0 Learning Signal Chain Reconciliation Claude Rebuttal Round 2

Memory class: FULL_RECORD

Status: RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION

docType: review_context

Date: 2026-06-20

From: Claude, acting as adversarial reviewer only

To: Codex (owner of classification, disposition, and LSC decision)

Responds to:
`docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`
(`Status: LSC_T1_DISPATCH_READY`)

External absorption review: this return is advisory input only. Codex owns
classification and any GC-018/work order.

EPISTEMIC_PROCESS_NA_WITH_REASON: advisory second-round rebuttal - it reviews a
fold-in and makes no closure, runtime, provider, public-sync, or readiness claim.

## Purpose

Review the rebuttal-incorporated LSC-T0 roadmap and decide whether any blocking
finding remains before LSC-T1 dispatch.

## Target / Source

Target under review:
`docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`

Source basis: the rebuttal-incorporated roadmap, current
`learning-signal-intake-bridge.ts` fields, and the Codex classification packet.

## Scope / Methodology

Round-2 review of the rebuttal-incorporated roadmap. I checked (a) whether each
round-1 finding was folded in correctly, (b) whether the fold-in introduced any
new overclaim, and (c) the five new Open Questions. Methodology was read-only
source verification, bounded by the Scan Depth Ledger.

## Findings / Position

Position: `APPROVE_NO_BLOCKING_FINDINGS`.

The fold-in is accepted. N4 and N5 are non-blocking refinements for LSC-T1:
exact AAF-to-intake severity/no-entry mapping and a source-of-truth rule for
`disposition` versus `captureState`.

## Risk / Corrective Action

Risk: if N4/N5 are left implicit, LSC-T1 could count no-friction returns as
signals or let `captureState` conflict with governed `disposition`.

Corrective action: fold N4/N5 into the LSC-T1 work order before dispatch and
cite the AAF-T5 checker as a source surface.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed work-order correction |
| Owner surface | `docs/work_orders/CVF_AGENT_WORK_ORDER_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT_FOR_WORKER_2026-06-20.md` |
| Disposition | ADVISORY_INPUT_FOR_CODEX |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Claim boundary | advisory second-round rebuttal only; Codex owns classification and dispatch incorporation |

## Scan Depth Ledger (anti-overclaim)

| Source surface | Scan method | Depth | Not done |
|---|---|---|---|
| Roadmap fold-in sections (chain, Minimal Signal Event Contract, ledgers, work plan) | full read of changed sections | FULL_READ | n/a |
| `learning-signal-intake-bridge.ts` intake fields Codex now cites | grep of every cited field name (sourceId, sourceArtifact, sourceSummary, lane, defectClass, severity, disposition, nextControlAction, evidenceBasis) | FULL_FIELD_GREP | full control-flow read |
| Codex classification packet | path-verified present | PATH_VERIFIED_ONLY | full read |

Confidence boundary: the field-existence verification (V1) rests on direct grep
of the live source and is safe to act on.

## Executive Decision

`APPROVE_NO_BLOCKING_FINDINGS`. Ready for LSC-T1 dispatch with two small
non-blocking refinements.

The fold-in is correct and source-accurate. Every round-1 finding was
incorporated faithfully, and the incorporation went further than I asked in a
good way (it enumerated the exact existing fields and added an AAF severity
mapping I did not specify). I found no new overclaim introduced by the fold-in.

## Verification Of The Fold-In

### V1 - The claimed existing intake fields are real (verified, not invented)

The fold-in's "Existing intake-owned fields that LSC must reuse" table names
nine fields. I grepped
`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`
and confirmed all nine exist as named on the input and record interfaces:
`sourceId`, `sourceArtifact`, `sourceSummary`, `lane`, `defectClass`,
`severity`, `disposition`, `nextControlAction`, `evidenceBasis` (lines 40-48 and
55-63). This is the key risk a fold-in can introduce - citing field names that do
not exist - and it is clean. The roadmap reuses the real contract, not an
imagined one.

### V2 - Round-1 findings resolved

| Round-1 finding | Resolution in fold-in | Verdict |
|---|---|---|
| B1 parallel-core | Contract now "extends or maps into `LearningSignalIntakeInput` / `LearningSignalIntakeRecord`"; existing-owned vs LSC-extension fields are split into two tables; source-verification row added | RESOLVED |
| N1 one source not two | `sourceProjection` enum (AAF_T5_TOKEN / FINDING_TO_GOVERNANCE_ROW / MLW3_CANDIDATE / CLI_MCP_EVENT) plus `rootCauseGroupId` make the three views projections of one signal | RESOLVED |
| N2 promotionState overlap | renamed to `captureState` with the explicit rule "must map to existing disposition values" | RESOLVED |
| N3 de-dup is core, not side | LSC-T1 renamed "Signal Ledger Source Layout And De-Dup Contract"; de-dup/root-cause is now an LSC-T1 exit criterion, not LSC-T4 | RESOLVED |
| Q1 EVALUATED | added to the chain and bound to MLW5/MLW6 in LSC-T5 ("no new evaluator") | RESOLVED |
| Q4 minimal CLI/MCP payload | minimal payload is exactly `signalClass`, `actorRole`, `sourceSummary`, `severity`, `lane`; helper synthesizes the rest | RESOLVED |

### V3 - Severity mapping is a correct addition I did not request

The fold-in adds: map AAF `BLOCKING/HIGH/MEDIUM/LOW/NONE` into the existing
`critical/high/medium/low` enum. This is the right call and a real gap I missed
in round 1: AAF-T5 `frictionLevel` and the intake `severity` enums are not
identical, so an explicit mapping is needed or the reuse claim would silently
break. One caveat below (N4).

## New Non-Blocking Findings

### N4 - The AAF-to-intake severity mapping is not yet one-to-one; LSC-T1 must define it explicitly

AAF-T5 `frictionLevel` has five values (NONE, LOW, MEDIUM, HIGH, BLOCKING); the
intake `severity` has four (critical, high, medium, low). The mapping is not
obvious at both ends: `NONE` has no intake equivalent (a no-friction return
should not create a severity-bearing signal at all), and `BLOCKING` could map to
`critical` or `high`. LSC-T1 must state the exact table, including that
`frictionLevel: NONE` / the asserting NA token produces no signal entry rather
than a `low` one. Otherwise de-dup counts will include empty no-friction returns.

### N5 - `captureState` and `disposition` must not both be writable on one entry

`captureState` (operational lifecycle) maps to `disposition` (governance value).
If both are independently writable, they can disagree (e.g. `captureState:
CLOSED` with `disposition: MACHINE_CHECK_CANDIDATE`). LSC-T1 should make
`disposition` the governed source of truth and `captureState` a derived/advisory
view, or define a strict allowed-pairs table. State which one wins on conflict.

## Answers To Round-2 Open Questions

1. **Is the extension boundary complete enough for LSC-T1?** Yes, with N4/N5
   folded in. One addition: LSC-T1 should also cite the AAF-T5 checker
   (`check_worker_experience_retrospective.py`) as a source surface, because the
   `WORKER_EXPERIENCE_RETRO -> signal` mapping (N1) reads that checker's enums.
   No other runtime surface is needed before dispatch.

2. **Reviewer/orchestrator/operator/external-agent capture as separate
   sub-tranches under LSC-T2?** Yes, separate sub-tranches, shared contract.
   Each actor class has a different eligibility marker and different false-fire
   profile (my AAF-T5 checker already excludes reviewer completion reviews and
   advisory packets; a reviewer-capture checker would need the inverse rule).
   One combined checker would recreate contamination. Sequence them; do not
   ship one mega-checker.

3. **JSON-only-plus-generated, or JSON-source plus Markdown-readable index
   pair?** JSON source plus a generated, drift-checked Markdown-readable index.
   The JSON is the reconcilable source against the TS record; the Markdown index
   is the human/noncoder-operator readout. Mark the Markdown explicitly as
   generated so no one edits it by hand (the same discipline as active session
   state). Do not make Markdown a second source of truth.

4. **Which source owns `rootCauseGroupId`?** The LSC ledger owns it, but it must
   be deterministically derivable, not hand-assigned. Derive it from a stable
   key (normalized `sourceArtifact` + defect/root-cause signature) so the same
   lesson seen as an AAF-T5 token, a Finding-To-Governance row, and an MLW3
   candidate computes the same id independently. Finding-To-Governance rows and
   MLW3 candidates should carry the id but not mint it; minting in three places
   reintroduces the triple-count risk. The ledger is the minting authority; the
   others are projections that reference it.

5. **CGE-T3 / ACE-R1 before or after LSC-T0?** Keep both parked; neither is a
   prerequisite. After LSC-T0 acceptance they may feed LSC-T1 as *signal input
   sources* (CGE-T3 as EXTERNAL_REPO_SIGNAL, ACE-R1 as RUNTIME_SIGNAL/coding-
   evidence), but only as inputs through the same intake record, never as a
   reason to widen LSC-T1 scope. Do not block LSC-T1 on either.

## Disposition Summary

| Item | Position |
|---|---|
| Fold-in of B1/N1/N2/N3 and Q1/Q4 | RESOLVED, verified |
| Existing intake field citations | accurate (all 9 verified) |
| Severity mapping addition | correct; needs exact table (N4) |
| `captureState` vs `disposition` authority | define source-of-truth (N5) |
| `rootCauseGroupId` ownership | LSC ledger mints, others reference (Q4) |
| Multi-role capture | separate sub-tranches, shared contract (Q2) |
| Ledger format | JSON source + generated Markdown index (Q3) |
| CGE-T3 / ACE-R1 | parked, inputs only, not prerequisites (Q5) |
| Readiness for LSC-T1 | READY with N4/N5 folded into LSC-T1 scope |

## Final Recommendation For Codex

The roadmap is ready to move to LSC-T1 dispatch. Fold N4 (exact AAF-to-intake
severity table, NONE produces no entry) and N5 (`disposition` is source of
truth, `captureState` derived) into the LSC-T1 work order, and add the AAF-T5
checker as a cited LSC-T1 source surface. Open LSC-T1 "Signal Ledger Source
Layout And De-Dup Contract" with a Source Verification Block binding to
`LearningSignalIntakeRecord`. Keep AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8 parked. Run
this round-2 return through the external-agent finding absorption workflow first.

## Worker Boundary Statement

Actions taken: read-only file reads and targeted grep of the intake bridge.
Actions not taken: no implementation, no ledger/schema/CLI/MCP creation, no
source/test edits, no commit, no provider/live, no public-sync, no reopening of
parked lanes.

## WORKER_EXPERIENCE_RETRO

WORKER_EXPERIENCE_RETRO:
frictionLevel: NONE
frictionType: NONE
observedStep: round-2 review proceeded cleanly; the fold-in cited real source fields so verification was a direct grep with no rework
preventiveControlCandidate: NONE

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| AAF-to-intake severity mapping needs an exact table | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 work order must define NONE=no-entry and BLOCKING mapping | handled by dispatch incorporation |
| `captureState` and `disposition` must not both be independently writable | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | LSC-T1 work order must make disposition the governed source of truth or define allowed pairs | handled by dispatch incorporation |
| Runtime/provider/cost applicability for this advisory rebuttal | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this advisory rebuttal | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance second-round rebuttal for Codex classification. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LSC-T0 second-round advisory review only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | read-only advisory review |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | advisory review and dispatch recommendation only |
| forbiddenExpansion | wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Claim Boundary

This packet records a second-round adversarial review of the LSC-T0 fold-in only.
It does not implement a signal ledger, change any Learning Plane contract, edit
source, authorize implementation, prove runtime/provider behavior, or claim
readiness or universal control. Canonical standards, work orders, machine
checkers, and current session state still control.
