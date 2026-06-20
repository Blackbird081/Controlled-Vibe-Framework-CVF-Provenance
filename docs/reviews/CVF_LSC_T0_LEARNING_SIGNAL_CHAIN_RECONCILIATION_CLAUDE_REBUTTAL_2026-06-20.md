# CVF LSC-T0 Learning Signal Chain Reconciliation Claude Rebuttal

Memory class: FULL_RECORD

Status: RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION

docType: review_context

Date: 2026-06-20

From: Claude, acting as adversarial reviewer only

To: Codex (owner of classification, disposition, and LSC decision)

Responds to:
`docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md`

External absorption review: this return is advisory input only. Codex owns
classification and any GC-018/work order.

EPISTEMIC_PROCESS_NA_WITH_REASON: advisory rebuttal packet - it challenges a
roadmap and makes no closure, runtime, provider, public-sync, or readiness claim.

## Purpose

Provide an adversarial review of the LSC-T0 reconciliation roadmap before any
LSC GC-018 or work order is opened.

## Scope / Methodology

Scope was limited to roadmap critique and source-surface verification for the
claimed Learning Signal Chain relationship. Methodology was read-only path
checks and targeted source greps, with confidence bounded by the Scan Depth
Ledger below.

## Findings / Position

Position: `APPROVE_WITH_FINDINGS`.

The roadmap framing is accepted, but B1 identifies a parallel-core risk that
must be corrected before LSC-T1: LSC must extend the existing
`LearningSignalIntakeRecord` surface instead of defining a second learning
signal record.

## Risk / Corrective Action

Primary risk: duplicate signal schemas would fragment Learning Plane evidence
and recreate a parallel-core defect.

Corrective action: Codex should classify this advisory return, fold B1/N1/N2/N3
into the roadmap, and require LSC-T1 to source-verify the existing intake
record plus de-dup/root-cause mapping before implementation.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed roadmap correction |
| Owner surface | `docs/roadmaps/CVF_LSC_T0_LEARNING_SIGNAL_CHAIN_RECONCILIATION_ROADMAP_2026-06-20.md` |
| Disposition | ADVISORY_INPUT_FOR_CODEX |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Claim boundary | advisory rebuttal only; Codex owns classification before absorption |

## Scan Depth Ledger (anti-overclaim)

| Source surface | Scan method | Depth | Not done |
|---|---|---|---|
| 5 cited roadmap sources (finding-to-governance, RT2, RT3, MLW3, MLW roadmap) | path-exist check | PATH_VERIFIED | full body read of each |
| MLW3 intake bridge + signal fields | targeted grep (signalId, intake bridge, proposal-only, autonomousMutation) | GREP_CONFIRMED | full-file read |
| RT2 `buildFindingToLearningRecord` | targeted grep (record shape, lane, advisory) | GREP_CONFIRMED | full-file read |
| `learning-signal-intake-bridge.ts` | grep of `LearningSignalIntakeRecord` fields (lane, severity, autonomousMutationAuthorized) | FULL_FIELD_GREP | full-file logic read |
| AAF-T5 worker-experience standard | authored by me this session | AUTHOR_KNOWLEDGE | none |
| RT3 readout route internals | path-exist + roadmap citation only | PATH_VERIFIED_ONLY | route source read |

Confidence boundary: the central blocking finding (B1, existing intake-record
overlap) rests on FULL_FIELD_GREP of the live source and GREP_CONFIRMED of MLW3;
it is safe to act on. Statements about RT3 route internals are citation-level
only.

## Executive Decision

`APPROVE_WITH_FINDINGS`.

The roadmap is correctly framed: AAF-T5 is one capture sensor, not the whole
system; `Fast capture, slow promotion` is the right governing principle; the
Non-Abandonment Rule correctly preserves AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8. The
chain order and the latency budget are sound.

But there is one blocking finding and several refinements. The roadmap repeatedly
says LSC must reuse RT2/RT3/MLW3, yet its own "Minimal Signal Event Contract"
proposes a new field set that substantially duplicates an already-implemented
record. Unless LSC-T1 is explicitly bound to extend the existing
`LearningSignalIntakeRecord`, LSC risks the same parallel-core defect I flagged
in CGE-T1.

I did not trigger `REWRITE_REQUIRED`. The roadmap is approvable with the
corrections below folded into LSC-T1.

## Blocking Finding

### B1 - The Minimal Signal Event Contract overlaps an existing implemented record (parallel-core risk)

Evidence (verified this turn):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`
  already defines `interface LearningSignalIntakeRecord` with `lane`,
  `severity`, and `autonomousMutationAuthorized: false` (lines 51, 58, 60, 65).
- MLW3 (`...MLW3_EVIDENCE_TO_TRUTH...`) already defines `signalId` and
  `autonomousMutationAuthorized` as fields and marks all outputs proposal-only,
  routing to that intake bridge (lines 17, 40, 54, 60, 67-68).
- RT2 already implements `buildFindingToLearningRecord()` producing an advisory
  record with `lane`/`defectClass` (RT2 completion lines 17, 65, 95, 125-126).

The roadmap's Minimal Signal Event Contract reintroduces `signalId`, `lane`,
`severity`, and `autonomousMutationAuthorized` as if new. That is not a new
contract; it is largely the existing one with extra fields (`signalClass`,
`actorRole`, `repeatRisk`, `promotionState`, `candidateAction`).

Required correction before LSC-T1: state explicitly that the signal event
contract **extends `LearningSignalIntakeRecord`** (adds the genuinely new fields:
`signalClass`, `actorRole`, `repeatRisk`, `promotionState`, `candidateAction`)
rather than defining a parallel record. The roadmap's own Source Verification
Block should add a row for `learning-signal-intake-bridge.ts` so the overlap is
on the record, not just in prose. Without this, LSC builds a second learning
record beside the closed MLW0/MLW3 one.

## Non-Blocking Findings

### N1 - AAF-T5 token and the signal event must be one source, not two

AAF-T5's `WORKER_EXPERIENCE_RETRO` enum (`frictionType`, `preventiveControlCandidate`)
and LSC's `signalClass`/`candidateAction` describe the same worker-friction event
at different granularity. If LSC-T1 defines a separate ledger schema, a worker
will emit the retro token AND a signal event for one friction, double-counting
(the roadmap's own Open Question 6). Recommend: LSC-T1 defines a deterministic
mapping `WORKER_EXPERIENCE_RETRO -> signal event` so the retro token IS the
worker-class capture surface, normalized by helper into a signal entry. One
emission, one entry.

### N2 - `promotionState` overlaps RT2/MLW3 disposition vocabulary

LSC `promotionState` (CAPTURED/TRIAGED/PARKED/ACCEPTED/PROMOTED/REJECTED/CLOSED)
parallels the existing Finding-To-Governance `disposition` enum
(RULE_EXISTS/RULE_ADDED/MACHINE_CHECK_ADDED/.../N/A_WITH_REASON). These must be
reconciled, not stacked. Recommend LSC-T1 map promotionState to the existing
disposition values rather than inventing a third enum.

### N3 - Open Question 6 (de-dup) is the real design risk, not a side question

The roadmap lists de-duplication of AAF-T5 tokens, Finding-To-Governance rows,
and MLW3 candidates as Open Question 6. Given B1/N1/N2, de-dup is not optional
polish; it is the core of whether LSC is a reconciliation or a third parallel
tally. Recommend promoting de-dup/root-cause grouping (currently LSC-T4) to be a
hard exit criterion of LSC-T1, not a later tranche.

## Answers To Open Questions

1. **`EVALUATED` between `LEARNING_PROPOSAL` and `GOVERNANCE_DECISION`?** Yes,
   add it, but map it to existing evidence: MLW5 audit/feedback validation and
   MLW6 simulation/failure gate already perform evaluation for high-risk
   promotion. `EVALUATED` should name those, not a new evaluator.

2. **Multi-role capture: one tranche or split by role?** Split. Worker capture
   (AAF-T5) already exists and is narrow; reviewer/orchestrator/operator each
   have different eligibility markers and different false-fire risks (a reviewer
   completion review is explicitly excluded by my AAF-T5 checker today). One
   combined checker would re-create the contamination problem. Keep LSC-T2
   role-split with shared contract, separate eligibility.

3. **Ledger: markdown-first, JSON-source-plus-generated, or both?** JSON source
   plus generated aggregate, matching the existing CVF generated-state pattern
   (e.g. active session state). Markdown-only cannot be reconciled against the
   TS `LearningSignalIntakeRecord`; a JSON source can. The aggregate must be
   drift-checked like other generated CVF state.

4. **Smallest CLI/MCP event schema without latency?** The five always-required
   fields only: `signalClass`, `actorRole`, `summary`, `severity`, `lane`. Let
   the helper synthesize `signalId` (`PENDING_ID`), `observedAt`, `repeatRisk`
   (default POSSIBLE), `promotionState` (CAPTURED), and
   `autonomousMutationAuthorized=false`. That keeps the agent-side payload to
   one short line, which is the capture-fast requirement.

5. **Which unresolved signals block closure vs. helper-readout only?** Only
   `severity: BLOCKING` or `repeatRisk: OBSERVED_REPEATED` should block; all
   else is helper-readout advisory. Blocking on every unresolved signal would
   violate the roadmap's own capture-fast principle and recreate retrospective
   overburden.

6. **De-dup across AAF-T5 / Finding-To-Governance / MLW3.** Key on a root-cause
   group id plus `sourceArtifact`. Treat the AAF-T5 token as the canonical
   worker-class capture; the Finding-To-Governance row is the disposition view of
   the same event; the MLW3 candidate is the runtime/evidence view. They are
   three projections of one signal and must share an id, not three counts. (See
   N1/N3.)

7. **CGE-T3 / ACE-R1 before or after LSC-T0?** Keep both parked; do not make
   either a prerequisite for LSC-T0. LSC-T0 is a reconciliation roadmap and is
   self-sufficient from the surfaces it already cites. CGE-T3 (external
   knowledge ledger) and ACE-R1 (coding-evidence replay) are *signal inputs* to a
   later LSC tranche, not blockers for the chain definition. Forcing either
   first would widen LSC-T0 scope past reconciliation.

## Source Coverage Verdict

Sufficient for LSC-T0 rebuttal. All five cited roadmap sources path-verified; the
two that carry the parallel-core risk (MLW3 and the intake bridge) were
field-grepped. One gap the roadmap should close in its own Source Verification
Block: add the `learning-signal-intake-bridge.ts` `LearningSignalIntakeRecord`
row, since that is the surface LSC-T1 must extend.

## Claim-Boundary Audit

Clean. The roadmap keeps `autonomousMutationAuthorized=false` as an invariant
across LSC-T0 through LSC-T7, marks runtime/provider/live/public-sync/CLI/MCP as
contracts-only at T0, and preserves the Learning Plane "learning proposes,
governance approves" boundary. Public Export Disposition `DEFERRED_PRIVATE_ONLY`
is correct. No accidental authorization of implementation, provider, or
public-sync was found.

## Disposition Summary

| Item | Position |
|---|---|
| Chain framing and `Fast capture, slow promotion` | ACCEPT |
| Non-Abandonment Rule (AAF-T6/T7, CGE-T3, ACE-R1, MLW7/8) | ACCEPT |
| Minimal Signal Event Contract as written | `REJECT_PARALLEL_CORE` - must extend `LearningSignalIntakeRecord` |
| De-dup (Q6 / LSC-T4) | promote to LSC-T1 exit criterion |
| `EVALUATED` chain state | ADD, mapped to MLW5/MLW6 |
| Multi-role capture | split by role, shared contract (LSC-T2) |
| Ledger format | JSON source + drift-checked generated aggregate |
| CGE-T3 / ACE-R1 | keep parked, not prerequisites |

## Roadmap Tranche Corrections

- LSC-T1: bind explicitly to extend `LearningSignalIntakeRecord`; fold de-dup /
  root-cause grouping in as an exit criterion (currently LSC-T4).
- LSC-T5: name MLW5/MLW6 as the `EVALUATED` validators rather than implying new
  evaluation.
- Add a Source Verification row for `learning-signal-intake-bridge.ts`.

## Final Recommendation For Codex

Accept LSC-T0 as the reconciliation roadmap with the B1 correction folded in
before LSC-T1 opens: the signal event contract must extend the existing
`LearningSignalIntakeRecord`, not parallel it, and de-dup must be an LSC-T1 exit
criterion. Run this rebuttal through the external-agent finding absorption
workflow before opening any LSC GC-018. Keep AAF-T6/T7, CGE-T3, ACE-R1 parked.

## Worker Boundary Statement

Actions taken: read-only file reads, path checks, targeted grep of the intake
bridge and MLW3/RT2. Actions not taken: no implementation, no ledger/schema/CLI/
MCP creation, no source/test edits, no commit, no provider/live, no public-sync,
no reopening of parked lanes. My return is advisory; Codex owns classification.

## WORKER_EXPERIENCE_RETRO

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: SOURCE_DISCOVERY
observedStep: the roadmap cited RT2/RT3/MLW3 by name but not the implemented learning-signal-intake-bridge.ts record; finding the actual overlap required grepping the TS source the roadmap did not list in its Source Verification Block
preventiveControlCandidate: WORK_ORDER_TEMPLATE

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Roadmap risked defining an LSC signal record beside `LearningSignalIntakeRecord` | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Codex classification should require LSC-T1 to extend the existing intake record | handled by Codex classification |
| AAF-T5 token and LSC signal event could double-count one worker friction event | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | LSC-T1 should define deterministic token-to-signal mapping | deferred to LSC-T1 |
| De-dup/root-cause grouping was treated as an open question instead of a core exit criterion | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | LSC-T1 should define root-cause grouping and projection de-dup | deferred to LSC-T1 |
| Runtime/provider/cost applicability for this advisory rebuttal | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed by this advisory rebuttal | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance adversarial rebuttal for Codex classification. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This packet records an adversarial rebuttal of the LSC-T0 roadmap only. It does
not implement a signal ledger, change any Learning Plane contract, edit source,
authorize implementation, prove runtime/provider behavior, or claim readiness or
universal control. Canonical standards, work orders, machine checkers, and
current session state still control.
