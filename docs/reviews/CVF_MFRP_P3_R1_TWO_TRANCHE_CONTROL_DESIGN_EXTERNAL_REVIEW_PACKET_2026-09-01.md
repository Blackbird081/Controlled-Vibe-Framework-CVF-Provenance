# CVF MFRP-P3-R1 Two-Tranche Control Design External Review Packet

Memory class: governed-review-context

Status: READY_FOR_EXTERNAL_REVIEW

docType: review_context

Date: 2026-09-01

Review mode: `DESIGN_ONLY`

Provider execution authority: `FORBIDDEN`

Successor tranche opened: `NO`

Planning base head: `b6c135b3077a44ae585118657fe0b2cf7e39229e`

## Purpose

Request one independent, source-bound critique of the corrected MFRP-P3-R1
control design before any R1A oracle authoring or R1B implementation. The
review must determine whether CVF has found the minimum safe split: R1 is a
non-executable umbrella/design checkpoint, R1A independently ratifies and
commits the oracle, and R1B later consumes that frozen oracle to invoke actual
P2 seams. The review should cut unnecessary ceremony while preserving the
oracle/runner independence boundary.

## Target / Source

| Target | Required SHA-256 | Review role |
|---|---|---|
| `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | `4438fcce757dcbe9bb6041a025b36adf2a3d3350199000bd18fc2ed9f6c11a07` | governing sequence and tranche boundary |
| `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | `22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011` | primary design under review |
| `docs/reviews/CVF_MFRP_P3_INDEPENDENT_REVIEW_RETURN_TO_DESIGN_2026-09-01.md` | `fe62e9996189afa8cd5bdf800acaa0ecaf8b4c6174a709ef647aee569390a91d` | defect and rejection evidence |
| `governance/compat/agent_autorun_machine_verification.py` | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` | actual P2 receipt-validation seam |
| `governance/compat/agent_automation_machine_verification_readout.py` | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` | actual P2 reviewer-readout seam |
| `docs/reviews/rejected_evidence/MFRP_P3_2026-09-01/ARCHIVE_MANIFEST.txt` | `24ff312195b39bdd950860d43f93cdce9164ce44587312f92e6ad9aa33ef0ba5` | content-addressed rejected evidence index; `NOT_ACTIVE_AUTHORITY` |

## Review Identity Gate

Before substantive review:

1. Confirm the current repository HEAD contains planning base head
   `b6c135b3077a44ae585118657fe0b2cf7e39229e` in its ancestry.
2. Recompute all six target hashes above and report `MATCH` or `MISMATCH` for
   every row.
3. Confirm the two original active Python/test/fixture paths and two original
   active review paths named by the archive manifest are absent.
4. Confirm the five preserved evidence files have `.rejected` suffixes and
   match the hashes recorded in the archive manifest.
5. If any identity check fails, return only `BLOCKED_TARGET_DRIFT` with the
   mismatch table; do not critique a guessed target.

## Scope / Methodology

Read the primary redesign in full and inspect the exact P2 symbols it proposes
to invoke. Use the rejected evidence only to reproduce or understand the
failure; never promote it to an oracle. Evaluate source binding, causal seam
invocation, freeze identity, coverage, mutation consumption, result semantics,
reviewer boundary and review cost. Read adjacent owners only when a concrete
question cannot be answered from the six pinned targets.

This is review, not re-performance. The external reviewer assesses whether the
specified evidence would be sufficient and independently generated; it must
not recreate the oracle, implement the runner, rerun all seven workflow phases,
or duplicate the future R1A/R1B work.

## CVF Source-Of-Truth Statement

CVF-governed files in the target table are the source authority for this
review. Public/simple lifecycle explanations, provider-local memory, chat
summaries, external examples and the preserved rejected artifacts are not CVF
authority. External output is advisory until locally verified and absorbed.

## Public / Private Boundary

| Surface | Disposition |
|---|---|
| Pinned private-provenance targets | May be read locally for this bounded critique; do not republish their full contents. |
| Public/simple lifecycle vocabulary | Context only; not an executable state machine or current authority. |
| Rejected evidence archive | Failure evidence only; never current code, test, fixture, ledger, worker return or oracle. |
| Secrets, credentials and provider data | Forbidden; no access, output or inference requested. |
| External publication/public-sync | Not authorized. |

## Workflow-Chain Interpretation Map

| Public/simple label | Review interpretation | CVF authority to check |
|---|---|---|
| `INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE` | explanatory vocabulary; evidence returns from every phase remain SOT-bound | roadmap, active session state, work order and review evidence |
| `R1` | umbrella redesign and design-review checkpoint only; no worker manifest | primary redesign `## Tranche Split And Authority Boundary` |
| `R1A` | executable documentary/machine-data tranche that ratifies and commits the oracle | primary redesign R1A and oracle contract sections |
| `R1B` | separate implementation/replay tranche consuming the frozen R1A oracle | primary redesign R1B, freeze and actual-seam sections |
| `REVIEW` | evaluate returned evidence and exceptions; do not redo role work | redesign reviewer boundary and result-semantics sections |

## Current Authority Surfaces

| Surface | Role | Why it matters |
|---|---|---|
| MFRP roadmap | sequencing authority | prevents R1, R1A, R1B or P4 from opening automatically |
| P3-R1 redesign assessment | design authority candidate | defines the proposed minimum two-tranche execution split |
| P3 rejection review | defect evidence | records why the original self-referential replay cannot be repaired in place |
| P2 receipt validator owner | implementation truth | determines whether proposed mutations can causally reach receipt validation |
| P2 readout owner | implementation truth | determines whether proposed observations can causally reach reviewer readout |
| active session state and handoff | current authority boundary | permits critique only; keeps implementation parked |

## Non-Authority Surfaces

| Surface | Allowed use | Must not be used for |
|---|---|---|
| Five `.rejected` artifacts | reproduce failure and test redesign assumptions | current helper, test, fixture, ledger, worker return, oracle or PASS evidence |
| External-review output | advisory critique | CVF acceptance, implementation authority or automatic roadmap change |
| Chat/provider memory | navigation hint only | source fact, hash identity, owner truth or closure evidence |
| Machine gate PASS | packet-shape evidence | semantic acceptance of the design |

## Review Questions

1. Is `R1` unambiguously non-executable, leaving exactly two execution
   tranches rather than three?
2. Is the R1A/R1B commit boundary the minimum sufficient mechanism to prevent
   the same producer from defining both expected truth and observed success?
3. Can R1A be dispatcher/reviewer-owned without causing the reviewer to redo
   phase-role work or creating AI-checks-AI circularity?
4. Are source path, locator, excerpt digest, mutation and normative predicate
   sufficiently independent and causal to serve as an oracle?
5. Can any allowed mutation be accepted syntactically yet fail to reach the
   actual P2 validation or readout seam?
6. Could an R1B runner special-case case IDs, precompute expected results,
   bypass a seam, or fabricate invocation/coverage evidence while still
   satisfying the proposed contract?
7. Are repository commit, blob/file SHA-256, JCS digest and coverage-set digest
   sufficient freeze identities, or are any redundant/missing?
8. Does the design fail closed when P2 seams or their dependencies change
   after R1A but before/during R1B, without requiring a new dependency graph?
9. Does the result model correctly separate execution completeness from safety
   disposition and prevent zero totals or incomplete coverage from becoming a
   PASS candidate?
10. Is the reviewer boundary limited to evaluating evidence, exceptions and
    disposition rather than replaying all cases or redoing R1A/R1B?
11. Which machine checks can replace AI review work safely, and which semantic
    judgments must remain reviewer-owned?
12. What fields, checks, documents or checkpoints can be removed or combined
    to reduce latency/quota without weakening oracle independence?
13. What is the smallest corrected R1A deliverable manifest that could be
    source-verified and ratified in one tranche?
14. What must be proven before an R1B work order can be authored, and what must
    remain deferred to the post-R1B independent review?

## Mandatory Adversarial Probes

Analyze at least these concrete sequences against actual sources:

- oracle cases cover all named classes but one mutation is never consumed;
- locator/excerpt hash is valid but the predicate is unrelated to the invoked
  P2 field;
- runner calls a seam once but reports observations for every case;
- runner branches on case ID or reads expected predicate before producing the
  observed result;
- R1A oracle remains byte-identical while a P2 dependency changes;
- every case executes but one zero-tolerance class has zero cases or zero
  denominators;
- replay is mechanically complete with a real P2 miss;
- reviewer is asked to rerun or reconstruct the oracle rather than evaluate
  the evidence envelope;
- the two-tranche mechanism costs more than the review work it removes.

For each material failure mode, name the attacked assumption, exact source
path/symbol/section, failure sequence, whether existing/proposed controls catch
it, minimal correction and blocking level (`R1A`, `R1B`, `P4_ONLY`, or
`NON_BLOCKING`).

## Expected Result / Prediction

The minimum safe structure is expected to remain one umbrella review
checkpoint plus exactly two execution tranches. The critique may simplify
fields or proof steps, but should preserve a committed oracle boundary before
runner implementation unless source evidence demonstrates an equally strong,
cheaper control.

## Expected External-Agent Output

Create exactly one new file.

Output directory: `docs/reviews/`

Output filename:
`CVF_MFRP_P3_R1_TWO_TRANCHE_CONTROL_DESIGN_EXTERNAL_CRITIQUE_2026-09-01.md`

Required sections:

1. Review Identity Gate Results.
2. Executive Verdict.
3. Source Verification And Read Depth.
4. Answers To All Fourteen Review Questions.
5. Strongest Concrete Failure Modes.
6. R1/R1A/R1B Boundary Assessment.
7. Oracle Independence And Freeze Assessment.
8. Actual-Seam And Coverage Assessment.
9. Reviewer Boundary And Machine-First Cost Assessment.
10. Required Corrections And Ceremony Cuts.
11. Minimal R1A Deliverable Recommendation.
12. R1B Entry Gate Recommendation.
13. Final Disposition.
14. Claim Boundary, Checker Source Read-Ahead Block, Agent Operation Trace
    Block and Public Export Disposition.

Allowed final dispositions:

- `ACCEPT_TWO_TRANCHE_DIRECTION`;
- `REVISE_BEFORE_R1A`;
- `COLLAPSE_WITH_EQUIVALENT_CONTROL_PROOF`;
- `STOP_NO_SAFE_VALUE`;
- `BLOCKED_TARGET_DRIFT`.

`COLLAPSE_WITH_EQUIVALENT_CONTROL_PROOF` is valid only if the critique gives a
source-backed mechanism that preserves precommitted oracle independence and
prevents the runner producer from altering expected truth.

## Return And Mutation Boundary

- Create only the one critique file named above.
- Do not edit, rename or delete any existing file.
- Do not stage, commit, push, public-sync, install packages, access credentials
  or make provider/live/network calls.
- Local read-only commands and bounded deterministic probes are allowed.
- Report execution base HEAD, exact `git status --short`, target hashes and any
  pre-existing dirty paths.
- Do not author an R1A baseline, oracle, schema, fixture or work order; do not
  implement R1B; do not open P4.

## Evidence Comparison

The critique must compare the written design to actual P2 seam behavior and
the independently reproduced P3 failure. Agreement with the roadmap's prose
alone is not evidence. Machine PASS on packet shape cannot establish oracle
independence or adequate coverage.

## Contradiction Or Gap Disposition

Any target mismatch, missing source, unrepresentable safety class, uncertain
dependency closure, or unverifiable cost assumption remains explicit and
fail-closed. Do not fill missing evidence with a plausible design assumption.

## Claim Update

The return remains advisory regardless of disposition. CVF must classify and
re-verify every finding before amending the design or opening R1A.

## Absorption Instruction

Route the returned file through
`docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`.
Split findings atomically, verify them against CVF-governed sources and record
the Required Absorption Table before any roadmap, baseline or work-order
change. No external finding changes SOT by itself.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | committed CVF redesign -> bounded external critique -> atomic finding absorption -> CVF reconciliation -> operator decision on R1A |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; returned output later uses `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | this packet plus the pinned MFRP roadmap and P3-R1 redesign assessment |
| Disposition | `PACKET_READY` after local review and commit; returned output remains advisory |
| Claim boundary | no authority transfer, implementation, oracle ratification, runtime/provider/public or readiness claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local external-review packet and CVF absorption workflow | read-only critique; no mutation or implementation authority | pinned target paths/hashes and current session boundary | internal repository review only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | operator transfers this committed packet to an external reviewer | transport/invocation is operator-owned; returned file is advisory and uncommitted | exact one-file return contract and identity gate | no CLI/MCP runtime adapter is implemented or claimed | `DEFERRED_WITH_REASON` |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | review-context purpose/target/scope/findings/risk/claim groups; external-routing seven-row table; checker read-ahead four-row table; trace labels; public disposition |
| gateRunPurpose | confirm, as evidence after source/checker read-ahead, that this critique packet is structurally complete and correctly routed without treating machine shape as semantic acceptance |
| claimBoundary | checker PASS cannot prove reviewer independence, ratify R1A, implement R1B or open P4 |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher / external-review packet author |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3-R1 two-tranche design review packet, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | governed source reads, hashes, `rg`, `apply_patch`, focused governance gates and git |
| Target paths | this packet; MFRP roadmap; P3-R1 redesign assessment |
| Allowed scope source | operator authorization of R1 umbrella plus separate R1A/R1B structure and instruction to proceed |
| Before status evidence | clean HEAD `b6c135b3077a44ae585118657fe0b2cf7e39229e` |
| After status evidence | one external-review packet; no authority-source modification, implementation or external invocation |
| Diff evidence | exact one-path changed set reconciled before commit |
| Approval boundary | record the R1 umbrella interpretation and dispatch one design-only critique |
| Claim boundary | no oracle authoring/ratification, runner implementation, P2 edit, P4 or external effect |
| Agent type | dispatcher / packet author |
| Invocation ID | `mfrp-p3-r1-two-tranche-external-review-packet-2026-09-01` |
| Expected manifest | `docs/reviews/CVF_MFRP_P3_R1_TWO_TRANCHE_CONTROL_DESIGN_EXTERNAL_REVIEW_PACKET_2026-09-01.md` |
| Actual changed set | `docs/reviews/CVF_MFRP_P3_R1_TWO_TRANCHE_CONTROL_DESIGN_EXTERNAL_REVIEW_PACKET_2026-09-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Risk / Corrective Action

Primary risks are reintroducing a self-referential oracle, turning reviewer
work into a full replay, or adding a third ceremony tranche with no independent
control value. The corrective boundary is explicit: R1 is review-only, R1A
commits truth expectations, R1B can only observe actual seams, and the reviewer
judges evidence/disposition without reconstructing either tranche.

## Findings / Position

Packet-author position: dispatch one critique now. Do not author R1A until the
return is absorbed and reconciled. The favored design is exactly two execution
tranches, but the reviewer is invited to challenge redundancy and cost with
source-backed evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance design-review context; public-sync is not
authorized.

## Claim Boundary

This packet authorizes one bounded advisory critique file only. It does not
authorize an external provider call by the repository, make the returned
critique authoritative, ratify an oracle, implement a runner, mutate P2,
activate machine-first review, open P4, change downstream workspaces, or claim
latency, quota, safety, runtime, public, deployment or production improvement.
