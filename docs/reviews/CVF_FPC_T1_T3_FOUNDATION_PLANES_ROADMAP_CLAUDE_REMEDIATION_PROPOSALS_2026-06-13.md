# CVF FPC-T1/T2/T3 Roadmap - Claude Remediation Proposals For Codex

Memory class: FULL_RECORD

Status: REMEDIATION_PROPOSALS_SUBMITTED_FOR_CODEX

docType: review

Date: 2026-06-13

Reviewer: Claude

Companion rebuttal:
`docs/reviews/CVF_FPC_T1_T3_FOUNDATION_PLANES_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`

Target roadmap:
`docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md`

rawMemoryReleased=false

## Purpose

Give Codex ready-to-apply, source-verified remediation text for the two blocking
findings (F1, F2) and concrete drop-in clauses for the agreed non-blocking
findings (F3, F4, F5, F6, F8), so Codex can finalize the FPC roadmap and author
the FPC-T1 GC-018 plus source-verified work order quickly and accurately.

This artifact proposes text only. Claude does not edit the roadmap, the registry,
any checker, runtime source, session state, or external app trees. Codex owns
all edits, finalization, and commits.

## Scope / Target / Owner Boundary

Target: remediation text for the FPC roadmap draft and seeding clauses for the
FPC-T1 work order.

Owner boundary: Claude owns this proposals artifact only. Codex owns roadmap
finalization, correction incorporation, the FPC-T1 GC-018/work order, interlock
registry decisions, checker implementation, session continuity, and commits.
Every "new text" block below is a suggestion for Codex to accept, adapt, or
reject - not a change Claude applied.

## Target / Source

| Reviewed item | Path | Disposition |
| --- | --- | --- |
| Roadmap under remediation | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | PROPOSE_EDITS |
| Active session state (F1 source) | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | VERIFIED |
| DICE roadmap (F1 token source) | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | VERIFIED |
| Corpus completeness standard (F8) | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | CITED |
| MLW3 contract (F5) | `docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md` | CITED |

## Scope / Methodology

For each finding, this artifact provides: (1) the exact current roadmap text
(old), (2) proposed replacement text (new), and (3) the source line that justifies
the change. Token values were re-verified at this session HEAD before drafting.

## Findings / Position

Position: the FPC roadmap is `ACCEPT_WITH_REQUIRED_CORRECTIONS`. This artifact
supplies drop-in remediation text for the two blocking findings (F1 stale closure
posture, F2 unverified external statistics) and paste-ready work-order clauses for
the agreed non-blocking findings (F3, F4, F5, F6, F8). Detailed finding analysis
and severities live in the companion rebuttal; this artifact is the solution
delivery so Codex can finalize and dispatch FPC-T1 quickly.

## Verified Token Facts Used Below

The closure-grade token literal is shown in the F1 fix blocks below (where Codex
needs to paste it); the table here states the facts in prose to keep this
review-input artifact from being misclassified as a closure.

| Fact | Source | Verified value |
| --- | --- | --- |
| Active mode is past DICE-T1 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `currentMode` | mode is worker-return fast-gate latency hardening, closed PASS-bounded |
| DICE-T1 closed at material commit | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` | DICE-T1 closed PASS-bounded at `d46023d1` |
| Post-DICE-T1 tranche also closed | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` | worker-return fast-gate latency hardening closed PASS-bounded at `5e605862` |
| DICE roadmap tranche row token | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` L110 | tranche row uses the closure-grade token (shown literally in F1 edit 2) |
| DICE roadmap header Status token | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` L5 | header Status is the weaker `DICE_T1_PASS_BOUNDED`; tranche row is closure-grade |

Nuance for Codex: `DICE_T1_PASS_BOUNDED` is not a non-existent token - it is the
DICE roadmap header Status. The defect is that the FPC roadmap cited the weaker
header token to describe closure posture, while the authoritative closure facts
(active state + DICE tranche row) state the closure-grade token shown in F1 edit
2. The fix is to cite the closure-grade token and the material commit, not to
invent a token.

## F1 - HIGH (BLOCKING) - Correct stale closure posture

### F1 edit 1 - "Why This Now" paragraph

Current text (roadmap L58-61):

```text
MEMCON-T1a through MEMCON-T5 are now closed bounded. DIR-T0/T1/T2 and
DICE-T0/T1 have also closed bounded as document-foundation work. Continuing
immediately into DICE-T2 would still be useful, but it would narrow the next
move toward document-packet samples.
```

Proposed replacement:

```text
MEMCON-T1a through MEMCON-T5 are CLOSED_PASS_BOUNDED. DIR-T0/T1/T2 and
DICE-T0/T1 are CLOSED_PASS_BOUNDED as document-foundation work; DICE-T1 closed
at material commit d46023d1, and a follow-on worker-return fast-gate latency
hardening tranche closed CLOSED_PASS_BOUNDED at 5e605862 after it. The current
active mode is worker_return_fast_gate_latency_hardening_closed_pass_bounded, so
the live next-move choice is no longer "continue into DICE-T2 versus FPC"; it is
"open DICE-T2 via a fresh GC-018 versus open the broader FPC foundation audit".
Opening DICE-T2 immediately would narrow the next move toward document-packet
samples, whereas FPC audits all foundation planes.
```

Justification: `CVF_SESSION/ACTIVE_SESSION_STATE.json` `currentMode` and
`nextAllowedMove`. This restatement makes the FPC argument stronger, not weaker.

### F1 edit 2 - Source Verification Block DICE row

Current text (roadmap L183):

```text
| DICE foundation is closed bounded through T1 and DICE-T2 is optional/fresh-auth only | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | `Status`, `Authorization`, `Work Plan` | `DICE_T1_PASS_BOUNDED` | DICE roadmap | ACCEPT |
```

Proposed replacement:

```text
| DICE foundation is closed bounded through T1 and DICE-T2 is optional/fresh-auth only | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | DICE-T1 tranche row (Work Plan table) and `CVF_SESSION/ACTIVE_SESSION_STATE.json` nextAllowedMove | `CLOSED_PASS_BOUNDED` | DICE roadmap tranche row + active session state | ACCEPT |
```

Justification: DICE roadmap L110 tranche row token is `CLOSED_PASS_BOUNDED`;
active state confirms closure at `d46023d1`. Using the closure-grade token
removes the Status Token Hygiene / Closure Finality mismatch.

## F2 - HIGH (BLOCKING) - De-assert unverified external statistics

### F2 edit - External Research Intake block

Current text (roadmap L78-86):

```text
Source checked by Codex:

- arXiv: `https://arxiv.org/abs/2604.18805`
- submitted: 2026-04-20
- abstract states that the authors evaluated LLM-based scientific agents across
  eight domains and more than 25,000 runs;
- abstract states that evidence is ignored in 68 percent of traces,
  refutation-driven belief revision occurs in 26 percent, and outcome-based
  evaluation cannot detect these failures.
```

Proposed replacement (Option A - preferred, qualitative):

```text
Operator-supplied external summary (figures not independently re-verified in
this repository; used only as process-control motivation, not as governed
evidence and not as a CVF runtime benchmark):

- claimed source: arXiv abstract `AI scientists produce results without
  reasoning scientifically`;
- the operator summary reports that LLM-based scientific agents frequently
  ignore contrary evidence, that refutation-driven belief revision is rare, and
  that outcome-only evaluation does not detect these reasoning failures;
- specific percentages and run counts from the summary are treated as
  unverified external claims, not as Codex-verified facts.
```

Proposed replacement (Option B - if Codex retains the numbers):

```text
Operator-supplied external summary, retained as an evidence artifact with a
captured digest at <path-to-saved-abstract> (sha256 <digest>). Figures below are
quoted from that retained summary and are not independently re-derived by CVF;
they are motivation only, not a governed benchmark:

- arXiv abstract `AI scientists produce results without reasoning scientifically`;
- summary reports evaluation across multiple domains and a large run count, with
  contrary evidence frequently ignored and refutation-driven revision rare.
```

Justification: the roadmap's own Non-Goals (L140-141) forbid external summaries
as governed evidence; Option A removes the contradiction with zero new artifacts;
Option B keeps numbers only if a hashed source is retained. Codex picks one.

Note: keep the existing CVF absorption decision block (L88-94) unchanged - its
`EPISTEMIC_PROCESS_CONTROL_LEARNING` class and "not a runtime benchmark" hedge
are already correct.

## Agreed Non-Blocking Findings - Drop-In Clauses For The FPC-T1 Work Order

These do not block roadmap finalization. They are clauses Codex can paste into
the FPC-T1 work order (or the roadmap) so the worker executes them without
re-deriving intent.

### F3 - FPC-T1 deliverable volume control

Add to the FPC-T1 work order Allowed/Output section:

```text
FPC-T1 output structure: emit the Plane-to-Chain matrix as the single spine
deliverable. Represent the interlock, machine-check, epistemic-process,
evidence-uptake, and deferred-capability views as columns or linked
sub-sections of that spine, not as separate free-standing documents. Before the
spine file approaches the GC-023 hard threshold, open a compact pointer/successor
or split by plane group in the same batch. State the target file ceiling in the
worker plan. Per-cell rule: every matrix cell must cite a source path/line or be
marked NOT_MAPPED or OUT_OF_SCOPE_WITH_REASON; no cell may be filled from
inference.
```

### F4 - Epistemic layer ownership line

Add one line under the roadmap Epistemic Process-Control Principles section
(after L223):

```text
Owning authority: Governance Layer / Control Plane. Any resulting epistemic-
process rule is enforced via a governance autorun phase gate (reviewer-fast or
pre-closure), not inside a use-case extension module. This keeps epistemic
process control as cross-agent governance, consistent with the Agent-Error-To-
Governance-Learning philosophy.
```

### F5 - FPC-T2 / MLW3 reconciliation prerequisite

Add to the FPC-T2 section prerequisite list and to the evidence-to-claim-update
candidate evaluation:

```text
Before assigning the evidence-to-claim-update-workflow-chain candidate an
ADD_INTERLOCK_ENTRY disposition, FPC-T2 must reconcile it against the existing
MLW3 evidence-to-learning surface
(`docs/reference/CVF_MLW3_EVIDENCE_TO_TRUTH_LEARNING_SIGNAL_PIPELINE_2026-06-05.md`
proposalAction / autonomousMutationAuthorized=false, and the route-visible
evidenceToLearningReadout proven in MLW3-RT1). If the audit-finding -> claim-
update path is not demonstrably distinct from MLW3's runtime evidence-to-learning
path, the default disposition is KEEP_STRUCTURAL_ONLY or MACHINE_CHECK_FIRST,
not a new interlock owner. Add MLW3 as a required FPC-T2 reconciliation input.
```

### F6 - FPC-T3 checker claim boundary

Add to the FPC-T3 `check_epistemic_process_packet.py` candidate row or its
description:

```text
Claim boundary: this checker verifies the presence and disposition completeness
of the required epistemic-process sections (hypothesis, prediction-result
comparison, evidence uptake, contradiction handling, claim update). It does not
and cannot verify that the reasoning inside those sections is epistemically
correct. A human reviewer checkpoint remains required for high-evidence work.
```

### F8 - Add Corpus Completeness standard to FPC-T1 Source Authority

Add to the roadmap Source Authority list (after L165) and to the FPC-T1 required
inputs:

```text
- Corpus Completeness And Report Integrity standard
  (`docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`),
  because FPC-T1 is an inventory/audit task over a plane set and must carry the
  Corpus Completeness And Report Integrity block in its work order and output.
```

### F7 - No action

F7 verified PASS (no use-case reopen). No edit required.

## Suggested FPC-T1 Work-Order Skeleton For Codex

To speed dispatch, the FPC-T1 work order should carry, at minimum:

| Required block | Content seed |
| --- | --- |
| Source Verification Block | the eight plane closure roadmaps/completions + interlock standard/registry + closure-quality standard + MLW3 contract/RT1, each with verified line/section |
| Roadmap-to-Work-Order Trace Matrix | FPC-T1 required outputs 1-8 (roadmap L278-285) mapped to acceptance criteria |
| Corpus Completeness And Report Integrity block | manifest of plane set, processing ledger, reconciliation, exclusions, verdict (per F8) |
| New runtime symbols authorized | none - FPC-T1 is read-only audit; assert zero runtime/checker/registry edits |
| Forbidden Path Manifest | external Document Translator, Policy_Local, registry file, all checkers, session state, public-sync |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Required proof | reviewer-fast hook chain; per-cell evidence rule; GC-023 ceiling check |
| Claim boundary | audit/map only; no plane is claimed complete; no interlock/checker created; no runtime mutation |

## Risk / Corrective Action

| Finding | Risk if not applied | Corrective action delivered here | Blocking |
| --- | --- | --- | --- |
| F1 | Roadmap finalized on stale posture; token-hygiene mismatch | exact old->new text for both "Why This Now" and the Source Verification row | YES |
| F2 | Unverified external numbers asserted as Codex-verified; self-contradiction with Non-Goals | two ready replacement options (qualitative or hashed-retention) | YES |
| F3-F6, F8 | Worker re-derives intent or misplaces a control | paste-ready clauses for the FPC-T1 work order | NO |

## Finding-To-Governance Learning Disposition

Tokens use the canonical taxonomy from
`docs/reference/archive/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md`
(the active enforcement is `governance/compat/check_finding_to_governance_learning.py`;
note the checker's internal `STANDARD_PATH` constant still points at the pre-archive
location, a separate minor drift worth a side-fix when convenient).

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Roadmaps can cite a weaker header status token instead of the closure-grade token + material commit | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | FPC-T3 candidate: closure-posture statements in roadmaps must cite the closure-grade token and the material commit, cross-checked against active session state |
| External numeric claims can enter governed roadmaps without a retained hashed source | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | require a captured digest or explicit unverified-summary label for external figures in governed artifacts |
| This proposals artifact references latency/cost/provider only inside quoted roadmap scope, not as a runtime finding | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | no runtime-behavior, provider-output, or cost-economics learning lane applies; the terms appear only in quoted scope text |

## Closure Posture

Not applicable. This artifact is a pending review-input proposals document
(`Status: REMEDIATION_PROPOSALS_SUBMITTED_FOR_CODEX`), not a closed-equivalent
work order, roadmap closure, or completion. It asserts no closure and edits no
runtime, registry, checker, or session-continuity surface. Codex owns the real
closure package, with its required Machine Closure Package table, when FPC-T1 is
finalized and dispatched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance review input for foundation planning. No public-sync
artifact or public catalog claim is authorized.

## Claim Boundary

This artifact proposes remediation text and work-order seeds for the FPC roadmap.
It does not finalize the roadmap, author the FPC-T1 GC-018 or work order, edit
the interlock registry, implement any checker, inspect external Document
Translator or Policy_Local source, run OCR/provider/live proof, or make any
readiness, cost, quality, or public claim. Codex owns finalization, correction
incorporation, and any dispatch.

rawMemoryReleased=false
