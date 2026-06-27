# CVF FPC-T1/T2/T3 Foundation Planes Roadmap - Claude Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_SUBMITTED_FOR_CODEX_FINALIZATION

docType: rebuttal

Date: 2026-06-13

Reviewer: Claude

Target roadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

Roadmap status under review: `FPC_T1_T3_ROADMAP_DRAFT_FOR_CLAUDE_REBUTTAL`

rawMemoryReleased=false

## Purpose

Provide Claude's required pre-finalization rebuttal of the FPC-T1/T2/T3
foundation-planes roadmap draft. This artifact records source-grounded findings,
severities, and suggested corrections so Codex can finalize, correct, or reject
the roadmap before authoring any FPC-T1 GC-018 baseline or work order. This is a
review-input artifact only; it does not finalize the roadmap or dispatch work.

## Scope / Target / Owner Boundary

Target: the roadmap draft
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`.

Owner boundary: Claude owns only this rebuttal artifact and its findings. Codex
owns roadmap finalization, correction incorporation, the FPC-T1 GC-018/work
order, interlock registry edits, checker implementation, and all commits. Claude
did not edit the roadmap, the registry, any checker, any runtime source, session
state, or external app trees.

## Target / Source

| Reviewed item | Path | Disposition |
| --- | --- | --- |
| Roadmap under review | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | REVIEWED |
| Interlock standard | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | VERIFIED |
| Interlock registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | VERIFIED |
| Closure quality gate standard | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | VERIFIED |
| MLW3 contract | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | VERIFIED |
| MLW3-RT1 completion | `docs/reviews/CVF_MLW3_RT1_EVIDENCE_TO_LEARNING_RUNTIME_PROOF_COMPLETION_2026-06-05.md` | VERIFIED |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | VERIFIED (drift found, F1) |

## Scope / Methodology

Read-only, source-grounded review. Claude re-read the named standards,
registries, and active state at this session HEAD and compared the roadmap's
claims against them, then mapped findings to severity, blocking/non-blocking
disposition, and suggested corrections. No runtime mutation, no registry edit,
no external app inspection, no provider/OCR/live proof was performed.

## Method And Evidence Basis

This rebuttal is grounded in current repository source, not memory or chat. The
following were re-read or verified at this session HEAD before findings:

| Verified item | Source | Result |
| --- | --- | --- |
| All 11 roadmap source-authority files exist | listed Source Authority paths | EXISTS 11/11 |
| Interlock standard Registry + `automationLevel` enum | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` L45, L79 | `MACHINE_CHECKED`/`STRUCTURAL_GUARDED`/`HUMAN_ROUTED`/`PARKED` confirmed |
| Registry has populated connections with the FPC-T2 field shape | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` L6+ | `upstreamLoop`/`downstreamLoop`/`automationLevel` confirmed populated |
| Closure quality gate `## Purpose`/`## Rule` | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` L22, L45 | confirmed |
| MLW3 `proposalAction`, `autonomousMutationAuthorized=false` | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` L59-60 | confirmed |
| MLW3-RT1 `evidenceToLearningReadout` bound to runtime | `docs/reviews/CVF_MLW3_RT1_EVIDENCE_TO_LEARNING_RUNTIME_PROOF_COMPLETION_2026-06-05.md` L142 | confirmed at `route-final-response.ts` L297/L351 |
| No pre-existing epistemic-process checker | `governance/compat/` listing | none found - FPC-T3 candidate is net-new |
| Actual DICE-T1 / next-move state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` L62, L218 | **drift found - see F1** |

The roadmap's Source Verification Block is substantially accurate. Eight of nine
rows verified directly. The two that need attention are addressed below.

## Verdict Summary

Recommended overall disposition: **ACCEPT_WITH_REQUIRED_CORRECTIONS**.

The roadmap is well-bounded, keeps foundation ahead of use cases, and is
authorized by the active `nextAllowedMove` ("another CVF foundation lane"). It
should NOT be finalized into an FPC-T1 GC-018 until findings F1, F2, and F5
(severity HIGH/MEDIUM) are corrected. F3, F4, F6, F7, F8 are MEDIUM/LOW and can
be folded into the FPC-T1 work order rather than blocking the roadmap.

No finding rises to "block the FPC direction entirely." One finding (F1) is a
report-integrity defect that must be fixed in the roadmap text before
finalization because it misstates current closure posture.

## Findings

### F1 - HIGH - Roadmap "Why This Now" and DICE source row understate actual closure posture

Evidence:

- Roadmap L60-61: "Continuing immediately into DICE-T2 would still be useful,
  but it would narrow the next move" - framing DICE-T2 as the live alternative.
- Roadmap Source Verification Block L183 cites DICE status as
  `DICE_T1_PASS_BOUNDED`.
- Actual `CVF_SESSION/ACTIVE_SESSION_STATE.json` L62:
  `currentMode = worker_return_fast_gate_latency_hardening_closed_pass_bounded`.
- Actual L218 `nextAllowedMove`: DICE-T1 is `CLOSED_PASS_BOUNDED` at material
  commit `d46023d1`, AND a further tranche ("worker-return fast gate latency
  hardening") is `CLOSED_PASS_BOUNDED` at `5e605862` AFTER DICE-T1.
- The DICE roadmap itself
  (`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`
  L110) shows DICE-T1 row `CLOSED_PASS_BOUNDED`, not merely `PASS_BOUNDED`.

Why this matters: a foundation-priority roadmap whose own "Why This Now"
section is one-to-two tranches behind the registry is exactly the priority-drift
/ stale-continuity defect class the roadmap is trying to govern against. It also
risks an FPC-T1 worker inheriting the stale "DICE-T2 is the next move" frame.

Suggested correction:

- Update "Why This Now" to state that DICE-T1 is CLOSED_PASS_BOUNDED and that a
  post-DICE-T1 worker-return fast-gate latency hardening tranche has also closed,
  so the live choice is now between DICE-T2 (fresh GC-018) and a broader
  foundation lane (FPC). The FPC argument is actually STRONGER stated this way.
- Change the Source Verification row token from `DICE_T1_PASS_BOUNDED` to the
  literal `CLOSED_PASS_BOUNDED` token that appears in the DICE roadmap tranche
  row, to avoid a status-token mismatch under the Closure Finality / Status
  Token Hygiene gates.

### F2 - HIGH - External arXiv claim is presented as Codex-verified fact but is not independently verifiable in-repo

Evidence:

- Roadmap L78-86 states "Source checked by Codex" and lists arXiv
  `2604.18805`, a submission date, and exact statistics (68 percent, 26 percent,
  25,000+ runs, eight domains).
- The roadmap correctly hedges in the absorption decision (L88-94: do not treat
  as proof of CVF runtime failure, not a benchmark). That hedge is good.
- However, the per-number claims are stated as established fact under "Source
  checked by Codex," and no in-repo evidence artifact (saved abstract, hash, or
  external evidence digest) backs them. Per CVF rules, external evidence used in
  governed artifacts should carry a captured digest, and external summaries are
  explicitly named as NOT governed evidence (roadmap's own Non-Goals L140-141).

Why this matters: this is a "report integrity" exposure - a precise external
statistic asserted without a retained, hashed source. It is internally
self-contradictory with the roadmap's own Non-Goal that forbids external
summaries as governed evidence. It does not need the paper to be wrong to be a
defect; it needs the citation discipline to match CVF's own standard.

Suggested correction:

- Demote the numeric claims to "operator-supplied external summary; figures not
  independently re-verified in-repo; used only as motivation."
- Either retain a captured abstract with a sha256 digest as an evidence artifact,
  or restate the motivation qualitatively ("a recent external study reports that
  LLM scientific agents frequently ignore contrary evidence") without asserting
  specific percentages as Codex-verified.
- Keep the absorption class `EPISTEMIC_PROCESS_CONTROL_LEARNING` - that part is
  sound.

### F3 - MEDIUM - FPC-T1 is broad but acceptably bounded; risk is matrix volume, not scope creep

Answering Rebuttal Gate question 1 ("too broad for one audit tranche").

Evidence:

- Roadmap Scope L107-118 lists ~9 planes + adapter layer.
- FPC-T1 required outputs L278-285 list 8 matrices/lists, each across all planes,
  PLUS an epistemic coverage matrix with its own 5-class taxonomy (L237-243).

Assessment: this is NOT scope creep in the forbidden sense - it is read-only,
source-backed, no runtime mutation (L302-309 forbid edits well). But 8 outputs x
9 planes x 2 taxonomies is a large single deliverable that invites either
shallow per-cell fills or a GC-023-threatening single file.

Suggested correction (non-blocking):

- Permit FPC-T1 to emit the plane-to-chain matrix as the spine, and allow the
  remaining matrices (interlock, machine-check, epistemic, deferred) as columns
  or linked sub-sections rather than 8 free-standing documents.
- Pre-authorize a split/rotation plan so the FPC-T1 worker does not hit GC-023
  mid-tranche and improvise. State a target file ceiling in the work order.
- Require a per-plane "evidence cited or marked NOT_MAPPED" rule so no cell is
  filled from inference. The roadmap exit criteria (L311-319) already imply this;
  make it an explicit per-cell rule in the work order.

### F4 - MEDIUM - Epistemic controls belong in FPC, but the placement table mislabels CVF layers

Answering Rebuttal Gate question 2 (right roadmap) and operator question 2
(right CVF layer).

Evidence:

- Epistemic Process-Control Principles table L214-223 places controls at "FPC-T1
  audit criterion", "FPC-T2 interlock candidate", "FPC-T3 checker candidate".
- These are TRANCHE placements, not CVF LAYER placements. The operator's
  question 2 asks whether they sit in the right CVF layer (L0 doctrine .. L5
  adapter; or Control/Governance/Learning plane).

Assessment: keeping epistemic process control INSIDE FPC (a governance-control
roadmap) is correct - it is process control, not a use-case feature, matching
operator direction 4. But the roadmap never states WHICH governed layer owns the
resulting rule. Epistemic-process discipline is a Governance Layer / Control
Plane concern (it governs how every agent reasons before closure), and the
checker would live in `governance/compat/` at an autorun phase - consistent with
the Agent-Error-To-Governance-Learning philosophy in CLAUDE.md.

Suggested correction:

- Add one line to the Epistemic Process-Control Principles section stating the
  owning layer: "Owning authority: Governance Layer / Control Plane; enforcement
  via governance autorun phase gate, not a use-case module." This directly
  answers operator question 2 and prevents a future worker from placing an
  epistemic check inside an extension module (wrong layer).

### F5 - MEDIUM - FPC-T2 "evidence-to-claim-update" interlock partially overlaps existing MLW3 surface; risk of double-owning a loop

Answering Rebuttal Gate question 3 (speculative FPC-T2 candidate).

Evidence:

- FPC-T2 proposes a net-new interlock `evidence-to-claim-update-workflow-chain`
  (L337-351).
- MLW3 already owns an evidence-to-learning pipeline with `proposalAction` and
  `autonomousMutationAuthorized=false` (verified L59-60), and MLW3-RT1 already
  binds a route-visible `evidenceToLearningReadout` (verified L142).
- The FPC-T2 candidate's `downstreamLoop = claim update / learning intake loop`
  and `inputArtifact = ... learning disposition` overlap MLW3's territory.

Assessment: the candidate is NOT purely speculative (the roadmap lists it as
"candidate to evaluate, not pre-accept", L326, L353-360, which is correct
discipline). But there is a real risk FPC-T2 registers a NEW interlock for a loop
MLW3 already partially owns, producing two owners for one chain - the exact
SYSTEM_LOOP_VISIBILITY_GAP inverse problem.

Suggested correction:

- FPC-T2 must, for the epistemic interlock candidate specifically, first
  reconcile against MLW3's existing evidence-to-learning surface and decide
  `KEEP_STRUCTURAL_ONLY` or `MACHINE_CHECK_FIRST` rather than
  `ADD_INTERLOCK_ENTRY`, UNLESS it can show the audit-finding -> claim-update
  path is genuinely distinct from MLW3's runtime evidence-to-learning path.
- Add MLW3 as a required reconciliation input to the FPC-T2 prerequisite list.

### F6 - LOW - FPC-T3 checker candidate is machine-checkable only for STRUCTURE, not reasoning quality; the roadmap should say so explicitly

Answering Rebuttal Gate question 4 (machine-checkable without semantic
overclaiming).

Evidence:

- `check_epistemic_process_packet.py` (L374) is described as requiring
  "hypothesis, prediction-result comparison, evidence uptake, contradiction
  handling, and claim update sections."
- These are all SECTION-PRESENCE / structural checks - feasible and deterministic.
- A machine cannot verify that the reasoning inside those sections is
  epistemically sound (that contradictory evidence was genuinely weighed). The
  external paper's own finding is that OUTCOME evaluation misses reasoning
  failure - a structural section check is closer to outcome-shape than to
  reasoning audit.

Assessment: feasible and early enough (reviewer-fast / pre-closure are correct
phases). No semantic overclaiming AS LONG AS the roadmap states the checker
proves section presence and disposition completeness, not reasoning correctness.

Suggested correction:

- Add an explicit claim-boundary line to the FPC-T3 candidate: "this checker
  verifies presence and disposition of required epistemic-process sections; it
  does not and cannot verify that the reasoning is epistemically correct - a
  human reviewer checkpoint remains required for high-evidence work." This
  matches the roadmap's own "Separate verifier checkpoint" principle (L221).

### F7 - LOW - Roadmap does not accidentally reopen use-case lanes

Answering Rebuttal Gate question 5.

Evidence: Non-Goals L136-144 and Out of scope L120-132 explicitly park
Policy_Local, Document Translator, OCR/provider, retrieval, public-sync, DICE-T2,
Model Gateway, Sandbox Runtime. FPC-T1 forbidden list L302-309 forbids inspecting
external Document Translator / Policy_Local source.

Assessment: PASS. No accidental reopening. The only residual risk is the stale
"DICE-T2 next move" frame in F1, which is a continuity defect, not a use-case
reopen.

### F8 - LOW - Source authority and forbidden boundaries are tight; one addition recommended

Answering Rebuttal Gate question 6.

Evidence: Source Authority L153-168 limits to operator instruction, front
door/active state/handoff, named standards/registries/roadmaps, and the arXiv
abstract; explicitly excludes private agent memory (L167-168, L146-149). This is
tight and correct.

Suggested addition:

- Add the Corpus Completeness And Report Integrity standard as a required
  authority for FPC-T1, since FPC-T1 is an inventory/audit task over a plane set
  - exactly the task class that standard governs (per CLAUDE.md Mandatory Corpus
  Completeness And Report Integrity). The roadmap already lists the block as a
  future work-order requirement (L436) but does not name the standard in Source
  Authority. Naming it closes the loop.

## Direct Answers To Operator's Six Focus Questions

1. Does FPC-T1/T2/T3 prioritize foundation over use-case drift? **YES.** Scope,
   Non-Goals, and forbidden lists keep all app lanes downstream; the tranche plan
   is audit-first, runtime-second. The only drift risk is the roadmap's own stale
   DICE framing (F1), which is the inverse of a use-case reopen.

2. Are epistemic process-control principles in the right CVF layer? **DIRECTION
   YES, PLACEMENT UNDERSPECIFIED.** They correctly live in a governance-control
   roadmap, but the roadmap labels tranche placement, not layer ownership. Fix
   per F4: name Governance Layer / Control Plane + autorun enforcement.

3. Is FPC-T2 interlock expansion too broad/narrow/correct? **CORRECTLY BOUNDED AS
   A DECISION TRANCHE,** because it evaluates candidates rather than pre-accepting
   them. One candidate (evidence-to-claim-update) needs MLW3 reconciliation to
   avoid double-owning a loop (F5).

4. Are FPC-T3 machine checks feasible and early enough? **YES, AS STRUCTURAL
   CHECKS at reviewer-fast/pre-closure.** They must explicitly disclaim reasoning-
   correctness verification (F6). No existing checker duplicates this (verified).

5. Missing source authority / forbidden scope / claim-boundary issues? **TWO.**
   The unverified arXiv statistics (F2) and the missing Corpus Completeness
   standard in Source Authority (F8). Forbidden scope is otherwise tight.

6. Should anything be blocked before final approval? **THE ROADMAP TEXT EDITS IN
   F1 AND F2 SHOULD BLOCK FINALIZATION** (report-integrity defects in the roadmap
   itself). F3-F8 can be carried as FPC-T1 work-order requirements rather than
   roadmap blockers.

## Blocking vs Non-Blocking Summary

| Finding | Severity | Blocks roadmap finalization? | Disposition |
| --- | --- | --- | --- |
| F1 stale DICE/closure posture | HIGH | YES - fix roadmap text | correct "Why This Now" + Source Verification token |
| F2 unverified arXiv statistics | HIGH | YES - fix roadmap text | demote to operator-supplied summary or retain hashed evidence |
| F3 FPC-T1 matrix volume | MEDIUM | NO | fold into FPC-T1 work order + GC-023 split plan |
| F4 epistemic layer placement | MEDIUM | NO | add one layer-ownership line |
| F5 FPC-T2/MLW3 overlap | MEDIUM | NO | add MLW3 reconciliation to FPC-T2 prereq |
| F6 checker claim boundary | LOW | NO | add structural-only claim boundary |
| F7 no use-case reopen | LOW | NO (PASS) | none |
| F8 corpus standard authority | LOW | NO | add standard to FPC-T1 Source Authority |

## Risk / Corrective Action

| Finding | Risk if unaddressed | Required corrective action | Blocking |
| --- | --- | --- | --- |
| F1 | Roadmap finalized on stale closure posture; FPC-T1 worker inherits superseded "DICE-T2 next" frame; status-token mismatch under Closure Finality / Status Token Hygiene gates | Correct "Why This Now" to current closure posture; change Source Verification DICE token to `CLOSED_PASS_BOUNDED` | YES |
| F2 | External statistic asserted as Codex-verified without a retained hashed source; self-contradicts the roadmap's own Non-Goal forbidding external summaries as governed evidence | Demote numbers to operator-supplied unverified summary, or retain a captured abstract with sha256 digest | YES |
| F3 | FPC-T1 deliverable volume risks shallow cells or a GC-023-threatening single file | Add matrix-spine + linked-columns structure and a pre-authorized split/rotation + per-cell evidence rule to the FPC-T1 work order | NO |
| F4 | Epistemic checker could be placed in the wrong layer (a use-case module) by a future worker | Add one line naming Governance Layer / Control Plane ownership with autorun-phase enforcement | NO |
| F5 | FPC-T2 may register a second owner for a loop MLW3 already partially owns | Require MLW3 reconciliation as an FPC-T2 prerequisite for the evidence-to-claim-update candidate | NO |
| F6 | FPC-T3 checker could be read as verifying reasoning correctness (semantic overclaim) | Add a structural-only claim boundary to the checker candidate; keep human reviewer checkpoint for high-evidence work | NO |
| F8 | Audit-class tranche dispatched without naming the Corpus Completeness standard | Add the Corpus Completeness And Report Integrity standard to FPC-T1 Source Authority | NO |

## Finding-To-Governance Learning Disposition

Defect classes, lanes, and dispositions below use the canonical taxonomy from
`docs/reference/archive/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md`
(active enforcement: `governance/compat/check_finding_to_governance_learning.py`).

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Roadmap drafted with one-to-two-tranche-stale closure framing (F1) | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | candidate FPC-T3 check: a roadmap "Why This Now" must cite the current `currentMode`/`nextAllowedMove` token, not a superseded one |
| External statistic asserted as verified without retained hashed source (F2) | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | external numeric claims in governed artifacts require a captured digest or an explicit "unverified summary" label |
| Findings reference latency/cost/provider terms only as quoted roadmap scope, not as a runtime/provider/cost defect in this review | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | this rebuttal raises no runtime/provider/cost behavior finding; latency/cost/provider appear only inside quoted roadmap scope text, so no runtime-behavior, provider-output, or cost-economics learning lane applies |

## Machine Closure Package

Not applicable. This artifact is a pending review-input rebuttal
(`Status: REBUTTAL_SUBMITTED_FOR_CODEX_FINALIZATION`), not a closed-equivalent
work order, roadmap closure, or completion. No closure package is asserted.
Codex owns any subsequent closure-equivalent artifact and its Machine Closure
Package when the roadmap is finalized.

## Claim Boundary

This rebuttal reviews the FPC-T1/T2/T3 roadmap draft against current in-repo
source. It does not finalize the roadmap, does not author the FPC-T1 GC-018 or
work order, does not edit the interlock registry, does not implement any checker,
does not inspect external Document Translator or Policy_Local source, does not
run OCR/provider/live proof, and makes no readiness, cost, quality, or public
claim. Codex owns finalization, correction incorporation, and any dispatch.

rawMemoryReleased=false
