# CVF MAO Provider-Neutral Agent Host Lifecycle Adapter Foundation Uplift Roadmap — Independent Re-Review Of R2 Repair

Memory class: EXTERNAL_CRITIQUE_INPUT

Status: REVIEWER_ACCEPTED_PARKED

docType: external-critique (NOT_CVF_SOURCE)

Date: 2026-08-12

Text Encoding Exception: preserve UTF-8 punctuation returned by the independent
external reviewer as source-fidelity evidence. These symbols are documentation
only and introduce no parser, schema, runtime, or identifier requirement.

Reviewer: independent re-reviewer (Claude Opus 5), operator-commissioned external re-review

Verification base: canonical private Core `Controlled-Vibe-Framework-CVF` at HEAD `4fd1b6177`

Predecessor input: `docs/reviews/CVF_MAO_PROVIDER_NEUTRAL_AGENT_HOST_LIFECYCLE_ADAPTER_FOUNDATION_UPLIFT_ROADMAP_INDEPENDENT_CRITIQUE_2026-08-12.md` (round 1, `NOT_CVF_SOURCE`)

Artifacts re-reviewed:

- `docs/roadmaps/CVF_MAO_PROVIDER_NEUTRAL_AGENT_HOST_LIFECYCLE_ADAPTER_FOUNDATION_UPLIFT_ROADMAP_2026-08-09.md` (repaired)
- `docs/reviews/CVF_MAO_PROVIDER_NEUTRAL_AGENT_HOST_LIFECYCLE_ADAPTER_FOUNDATION_UPLIFT_ROADMAP_WORKER_RETURN_2026-08-09.md` (R2)
- `docs/reviews/CVF_MAO_PROVIDER_NEUTRAL_AGENT_HOST_LIFECYCLE_ADAPTER_FOUNDATION_UPLIFT_ROADMAP_INDEPENDENT_CRITIQUE_2026-08-12.md` (round-1 critique as placed)

All three untracked and unstaged in worktree `CVF-MAO-HOST-ROADMAP-PARKED`, branch
`codex/mao-agent-host-roadmap-parked`, worktree base `95340497f`.

---

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | review structural headings, external-input authority boundary, operation trace labels, Delta claim boundary, and `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm the canonical intake wrapper as evidence after checker read-ahead; gates are not used for first discovery |
| claimBoundary | this local governed wrapper does not modify the external reviewer's substantive findings, does not promote the re-review to CVF authority, and releases no implementation authority |

Wrapper provenance: the external reviewer authored the substantive re-review.
The local documentation reviewer added only governed intake wrapper metadata
after canonical placement; the `REVIEWER_ACCEPTED_PARKED` disposition and all
external findings remain unchanged.

---

## Purpose

Route the independently authored R2 re-review as external comparison input
while preserving its verdict and preventing promotion to CVF authority.

## Target / Source

Target: the repaired parked roadmap packet named in the external re-review.
Source: operator-provided Claude re-review text plus local CVF-governed wrapper
metadata. The external text is evidence input, not Source Verification authority.

## Scope / Methodology

The local wrapper supplies only the structural, trace, collision, export, and
claim-boundary metadata required for a file placed under `docs/reviews/`. It
does not independently endorse source claims beyond the governed review and
dispatch checks recorded outside this external artifact.

## Findings / Position

External substantive position remains `REVIEWER_ACCEPTED_PARKED`. Local intake
position is `ACCEPT_AS_INPUT_NOT_AUTHORITY`.

## Risk / Corrective Action

The primary risk is accidental authority promotion or loss of provenance.
Corrective action is mandatory local source reproduction before any finding is
used in a governed decision; machine-gate repairs inside allowed documentation
scope are performed directly by the responsible reviewer.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Search roots and coverage | bounded external review covered the named MAO source directory and three packet docs; local intake coverage additionally checks source, tests, docs, JSON state, and the named external-evidence files without claiming a complete external corpus | BOUNDED_NOT_CORPUS_COMPLETE |
| Exact search command or query | `rg -n --hidden --no-ignore "AgentHost|hostLifecycle|sendMessage|deliverMessage|clarification|inbound|waitFor|awaitTerminal|waitUntil" EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests docs CVF_SESSION --glob "*.ts" --glob "*.md" --glob "*.json"` | LOCAL_INTAKE_QUERY_TO_REPRODUCE_AT_DISPATCH_BASE |
| Same-token collision result | `BLOCKED_SOURCE_NOT_FOUND`, `NOT_CVF_SOURCE`, `REVIEW_REJECTED_REPAIR_REQUIRED`, `LPCI`, `Source Verification`, `CVF_EXECUTION_PLANE_FOUNDATION`, `CVF_SESSION`, `LANE_FOUNDATION`, and `LOW` have same-token occurrences elsewhere; these collisions are path, severity, governance, or provenance vocabulary with different meanings | COLLISIONS_RECORDED |
| Absent-versus-collision disposition | No same-token occurrence proves a MAO semantic owner; only locally reproduced source evidence is binding, and all external assertions remain non-authoritative | FAIL_CLOSED |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external comparison -> local source reproduction -> owner and value disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | parked roadmap, T0 baseline/work order, and governed reviewer decision |
| Disposition | `REJECT_DIRECT_IMPORT`; retain as external input only |
| Claim boundary | no external assertion becomes CVF authority without independent local verification |

## Epistemic Process Block

### Expected Result / Prediction

Canonical intake should preserve the external verdict while keeping every
source claim non-authoritative until reproduced locally.

### Evidence Comparison

The external reviewer reported all original findings repaired and three new
non-blocking refinements. Local packet checks accept the refinements only as
input constraints and re-run source and governance validation independently.

### Contradiction Or Gap Disposition

Any contradiction with current CVF source is resolved in favor of canonical
source or returned as blocked evidence; it is never resolved by promoting the
external review.

### Claim Update

The accepted local claim is that this file is useful external comparison input.
It is not authority and does not release T0 or any later tranche.

## Finding-To-Governance Learning Disposition

Runtime/provider/cost learning lane: `N/A_WITH_REASON` because the findings and
repairs affect documentation classification and dispatch discipline only.

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| N-01 distinguishes a genuine absence from an owned-primitives composition gap | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING | TEMPLATE_UPDATED | Keep the distinction mandatory in the T0 ownership ledger |
| N-02 requires wrapper provenance in changed-file reconciliation | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Preserve author-versus-wrapper attribution in governed intake metadata |
| N-03 restricts collision tables to pattern-matchable tokens | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Enforce exact query, roots, hits, collisions, and disposition in T0 |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | local documentation reviewer |
| Provider or surface | local governed workspace |
| Session or invocation | R2 external re-review canonical intake repair, 2026-08-12 |
| Working directory | canonical private Core repository root |
| Command or tool surface | local source reads, checker-source read-ahead, metadata patch, and documentation gates |
| Target paths | this external re-review intake file |
| Allowed scope source | operator authorization to review and prepare the T0 dispatch packet |
| Before status evidence | canonical external re-review lacked required governed-review wrapper blocks |
| After status evidence | wrapper blocks added; substantive external verdict and findings preserved |
| Diff evidence | local untracked file comparison, `git status --short`, and applicable checker output |
| Approval boundary | documentation intake repair only |
| Claim boundary | no T0 execution, DESIGN, BUILD, provider/live, commit, merge, or public action |
| Agent type | documentation reviewer |
| Invocation ID | `mao-ahla-r2-external-intake-wrapper-2026-08-12` |
| Expected manifest | this re-review wrapper metadata only |
| Actual changed set | this re-review wrapper metadata only |
| Manifest delta | MATCH |

---

## 0. Claim Boundary (read first)

This document is **external re-review input only**. It is `NOT_CVF_SOURCE`.

- Never cite it as canonical authority in Source Authority tables, Source
  Verification ACCEPT rows, corpus manifests, closure proof, or
  roadmap/work-order evidence.
- It modifies no artifact, commits nothing, stages nothing, merges nothing, and
  removes no worktree.
- **Acceptance does not release the roadmap.** Status remains
  `PARKED_PENDING_INDEPENDENT_CRITIQUE_AND_OPERATOR_RELEASE`.
- It opens no T0, DESIGN, SPEC, BUILD, provider, live, network, secrets,
  deployment, public-sync, or production authority.
- Operator selection plus a fresh documentation-only T0 GC-018 authority packet
  remain mandatory and are unaffected by this re-review.
- Every statement here is a **reviewer assertion** requiring independent
  re-verification before being treated as governed evidence.

---

## 1. Re-Review Disposition

`REVIEWER_ACCEPTED_PARKED`

All fifteen round-1 findings are repaired. The repair is **source-real, not
declarative**: I independently re-resolved every declaration anchor the R2 repair
added, and all of them land exactly on the claimed symbol at `4fd1b6177`. That
precision is itself evidence that R2 re-verified against CVF sources rather than
transcribing round-1 assertions.

Three new findings are recorded. All are `NON_BLOCKING` and none affects
evidence accuracy, ownership, authority, lifecycle semantics, proof validity, or
the go/no-go decision. They are refinements for T0 authoring.

**No blocking repair remains. The packet may stay PARKED awaiting
decision-owner selection and fresh T0 authority.**

---

## 2. Verification Performed

Read-only against canonical Core at `4fd1b6177`. Recorded so the author can
re-run rather than trust.

### 2.1 Declaration anchors — every new Source Verification row re-resolved

| File | Anchors claimed | Result |
|---|---|---|
| `task.graph.contract.ts` | L21, L32, L40, L49, L138 of 383 | all exact: `MaoRiskLevel`, `MaoBudgetAllocation`, `MaoAuthorityEnvelopeInput`, `MaoAuthorityEnvelope`, `buildAuthorityEnvelope` |
| `event.ledger.contract.ts` | L16, L28, L36-L37 of 283 | all exact: `MaoTaskState`, `MAO_TERMINAL_STATES`, recoverable-hold comment, `isTerminalState` |
| `read.model.contract.ts` | L18, L54, L101 of 122 | all exact: `MaoReadModelTaskState`, `buildReadModel`, `readModelsAreEqual` |
| `evidence.readout.contract.ts` | L31, L98, L279, L347 of 473 | all exact: `MaoReceiptKind`, `redactFields`, `buildEvidenceReadout`, `evaluateRetention` |
| `lifecycle.controller.contract.ts` | L80, L88, L118, L123, L144, L212, L240 of 330 | all exact: `recordHeartbeat`, `isHeartbeatStale`, `requestCancel`, `acceptCancel`, `classifyRetry`, `classifyOrphan`, `MaoLifecycleController` |
| `operational.worker.launcher.ts` | L35, L39, L76, L190, L207, L436, L452 of 498 | all exact, incl. `requestCancellation` L436 and `acceptCancellation` L452 |
| `durable.run.store.ts` | L111, L130, L172, L186 of 504 | all exact: `MaoFileRunStore`, `createRun`, `resumeRun`, `appendEvent` |
| `delegation.adapter.contract.ts` | L62, L89, L114, L149, L168, L262 of 269 | all exact |

Every file line-count denominator also matches. **Round-1 H-02 is genuinely
closed**, and the anchor form now survives base drift.

### 2.2 Literal tokens

| Token | Location | Result |
|---|---|---|
| `PARKED_OPERATOR_PRIORITY_LPCI1_WEB_REENTRY_BASELINE_ACCEPTED` | LPCI roadmap `Status:` | exact match |
| `REUSE_BASELINE_DELTA_ONLY` | re-entry baseline | present, 2 occurrences |
| `NO_VIABLE_BOUNDED_PATTERN` | NP-03 decision | present, 6 occurrences |
| `NOT_DESIGNABLE` | NP-03 decision | present, 3 occurrences |
| `MAO-LIVE-T1` / `runMaoLane` | pilot script header L2, L28, L185 | present |
| bootstrap `currentMode`, `activeHandoff`, `nextAllowedMove` | `ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | match roadmap L91 |

`docs/reference/CVF_LPCI1_WEB_CURRENT_ASSESSMENT_AND_PARKED_REENTRY_BASELINE_2026-08-12.md`
exists at `4fd1b6177`.

### 2.3 Reproduced searches

- Candidate-symbol negative search over `*.ts` / `*.md`: **zero hits**,
  reproduced independently.
- `rg --files --hidden --no-ignore EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao`:
  **17 files** — the manifest count is correct.
- `sendMessage|deliverMessage|clarification|inbound` in MAO: **zero hits** —
  `send` is genuinely absent.
- `waitFor|awaitTerminal|waitUntil` in MAO: **zero hits** — no finite-wait
  composition function exists, though all its primitives do (see N-01).

### 2.4 Packet and provenance state

`git status --short` in the worktree: exactly three untracked paths, nothing
staged. `git worktree list` confirms same-repository topology at `95340497f` —
not a second CVF, not a foundation, not a dependency.

### 2.5 Round-1 critique file integrity

Diff of my original round-1 output against the placed copy: **154 insertions,
3 deletions**.

- Insertions are a governed wrapper (Checker Read-Ahead, Purpose, Target/Source,
  Scope/Methodology, Findings/Position, Risk table, Negative Search And Collision
  Discipline, Epistemic Process, AOT, Public Export, Claim Boundary).
- The 3 deletions only replace the volatile anchor `LPCI roadmap L3` with
  `current-Core LPCI roadmap` — the same drift-resistance fix H-02 required.
- All C/H/M/L finding bodies, Section 6, the `BLOCKED_SOURCE_NOT_FOUND`
  disposition on C-01, and the `REVIEW_REJECTED_REPAIR_REQUIRED` position
  survive verbatim.

**Nothing adverse was softened or removed.** See N-02 for the one disclosure gap.

---

## 3. Prior Finding Closure Matrix

| Finding | Disposition | Evidence | Remaining action |
|---|---|---|---|
| C-01 | `REPAIRED_ACCEPTED` | Roadmap L89 carries the exact LPCI token, the `8791b9b23` anchor, and the re-entry baseline path bound to `REUSE_BASELINE_DELTA_ONLY`. All three verified at Core. | none |
| C-02 | `REPAIRED_ACCEPTED` | L11-15 replace the blanket refresh claim with `Refresh verification base` plus an explicit **Refresh scope** enumerating what was re-read. L91 cites the bootstrap path, `AGENT_HANDOFF_V59_2026-08-11.md`, mode `public_projection_staging_branch_pushed_deploy_parked`, and states the next move is operator selection of *a new roadmap, not this one*. This is the stronger of the two options round 1 offered. | none |
| H-01 | `REPAIRED_ACCEPTED` | Source Verification L131 carries both `NO_VIABLE_BOUNDED_PATTERN` and `NOT_DESIGNABLE`. T5 (L399) requires a fresh operator scope-expansion decision satisfying an NP-03 Minimal Unblock Condition option and states "may be permanently unreachable". T4 (L398) is a "legitimate terminal state". L405: "T5/T6 are not promised future work." | none |
| H-02 | `REPAIRED_ACCEPTED` | Column converted to declaration-anchor-with-denominator form; verification base recorded in the section header; all anchors re-resolved (Section 2.1). | none |
| H-03 | `REPAIRED_ACCEPTED` | L57-64 retitled "Candidate gap, **not yet a source-backed finding**" and concede the name-based result "does not exclude an equivalent facade under different symbols". Six of seven candidates downgraded to `DOC_ONLY_NEW_HYPOTHESIS`. L465-472 record both exact commands then state they "are not corpus-complete proof". T0 (L394) must record an exact semantic negative search. Both commands reproduced. | none |
| H-04 | `REPAIRED_ACCEPTED` | `status` (L261) requires a total mapping from `MaoTaskState` and "not a second state lattice"; preserves `blocked`/`timed_out` as recoverable holds. New overlap rows `REJECT_SECOND_STATE_LATTICE` and `REJECT_SECOND_STATUS_OWNER`. New proof cases L306 (recoverable holds) and L307 (wait/status coherence). | T1-owned specifics, by design |
| M-01 | `REPAIRED_ACCEPTED` | `send` (L258) labelled "genuinely novel candidate"; T1/T2 must define per-identity ordering, acknowledgement, restart durability, and either an idempotency key or explicit at-most-once non-durable delivery. Threat row L275; proof case L303. Absence independently confirmed. | none |
| M-02 | `REPAIRED_ACCEPTED` | L260 separates effect idempotency ("at most one cancellation effect") from responses that "may change deterministically… as state advances". Proof case L304 now admits differing responses across calls. | none |
| M-03 | `REPAIRED_ACCEPTED` | Invariant 4 (L190) requires T1 to choose an explicit operation, a dispatch-returned manifest, or a source-justified attempt-based model. Threat row L286 directs reuse of `MaoAuthorityEnvelope.budget`. Principle 6 (L245) mandates reusing `MaoBudgetAllocation` and justifying only genuinely missing measures. | none |
| M-04 | `REPAIRED_ACCEPTED` | All three AOT blocks mark the path `TRANSIENT_PATH_NOT_A_DEPENDENCY`. | none |
| M-05 | `REPAIRED_ACCEPTED` | Acceptance Criteria split into "Author-verifiable now" (5, `[x]`) and "Reviewer-verifiable after this repair" (6, `[ ]`). Inversion removed. | dispositioned in Section 9 |
| M-06 | `REPAIRED_ACCEPTED` | T2 (L396) freezes overhead thresholds **and proof-harness design**, with stop boundary "thresholds cannot be tuned after the seam exists". T3 (L397) builds the seam "measured by the T2-frozen harness and thresholds". Circularity removed. | none |
| L-01 | `REPAIRED_ACCEPTED` | Worker return L11: `Revision: R2, 2026-08-12 independent-critique remediation`. | none |
| L-02 | `REPAIRED_ACCEPTED` | L480: re-run at `4fd1b6177` on 2026-08-12, zero candidates. Resolver script confirmed present. | none |
| L-03 | `REPAIRED_ACCEPTED` | New Source Verification row L133 cites the pilot script with `MAO-LIVE-T1` and `runMaoLane`; both verified in the script. | none |

**All fifteen: `REPAIRED_ACCEPTED`.**

---

## 4. New Findings

### CRITICAL

`NONE`

### HIGH

`NONE`

### MEDIUM

#### N-01 — `wait` and `send` are treated as comparable gaps although they are gaps of different kind

- **Severity:** `MEDIUM` · **Blocking:** `NON_BLOCKING`
- **Artifact:** Roadmap L153 (`AgentHostWaitRequest` = `DOC_ONLY_NEW_HYPOTHESIS`),
  L259; R2 worker return L148-152
- **Source evidence:** R2 argues `wait` "has owned primitives rather than a
  demonstrated provider-neutral finite-wait facade". Literally true — no
  `waitFor` / `awaitTerminal` / `waitUntil` symbol exists in MAO. But every input
  a finite wait needs **is** owned: `recordHeartbeat` (L80), `isHeartbeatStale`
  (L88), `checkTimeout`, `classifyOrphan` (L212), `isTerminalState`
  (event.ledger L37), `buildReadModel` (read.model L54). By contrast `send` has
  **no owned primitive whatsoever** — confirmed by zero hits on
  `sendMessage|deliverMessage|clarification|inbound`.
- **Problem:** both are presented as candidate gaps, inviting T0 to read "two
  gaps" as support for a facade. The honest reading is one genuine absence plus
  one small composition helper. Since T0's continue/cancel decision turns partly
  on how much is actually missing, this asymmetry can tilt a borderline verdict
  toward building.
- **Corrective action:** T0's ownership ledger should record `send` as
  `GENUINELY_ABSENT` and `wait` as
  `PARTIALLY_OWNED (all primitives owned; composition function absent)`, and
  state explicitly that a composition helper alone does not establish facade
  value.

#### N-02 — the governed wrapper added to the reviewer-authored critique is not disclosed in R2's changed-file ledger

- **Severity:** `MEDIUM` · **Blocking:** `NON_BLOCKING`
- **Artifact:** R2 worker return L364 (Changed Files); critique file L1-107 and
  L985-1019
- **Source evidence:** Section 2.5 — 154 insertions, 3 deletions. R2 L364
  describes the file only as "external critique input | independent-reviewer-
  authored, operator-placed". The wrapper's own Scope/Methodology (critique L46-48)
  *does* disclose that "a documentation repair worker added only this governed
  wrapper and operation trace without changing the substantive findings", so the
  disclosure exists — but not in the worker return's manifest, which is where a
  manifest audit would look.
- **Problem:** a reader reconciling R2's Changed Files table against the actual
  diff would find 154 unexplained inserted lines in an artifact attributed
  wholly to an external reviewer. Manifest tables are the surface CVF uses to
  detect unauthorized scope, so an undisclosed modification there is a
  reconciliation defect even when the modification is benign.
- **Corrective action:** amend R2's Changed Files row to read
  "independent-reviewer-authored substantive content; documentation worker added
  governed wrapper metadata only; substantive findings unchanged".
- **Explicitly not an integrity finding.** The wrapper marks itself as
  wrapper-only, reasserts `NOT_CVF_SOURCE` in four places, and preserves every
  adverse item — including the `BLOCKED_SOURCE_NOT_FOUND` row and the
  `REVIEW_REJECTED_REPAIR_REQUIRED` position that reflect badly on the packet.
  Nothing was laundered.

### LOW

#### N-03 — the collision table lists tokens the search pattern cannot match

- **Severity:** `LOW` · **Blocking:** `NON_BLOCKING`
- **Artifact:** Critique wrapper L86-93
- **Source evidence:** the table lists `BR1`, `CVF_MA`, `DOC_ONLY_NEW`, `LPCI`,
  `SOURCE_BACKED`, `TypeScript` as "same-token collisions". None is an
  `AgentHost*` identifier or `hostLifecycle`; the queried pattern could not have
  matched any of them.
- **Problem:** the table appears to discharge collision discipline for the
  candidate-symbol search while addressing tokens that search never queried.
  Harmless here because the wrapper's conclusion stays conservative, but it must
  not become the template T0 copies.
- **Corrective action:** at T0, restrict collision tables to tokens the search
  pattern can actually match.

---

## 5. Owner And Facade Verdict

**Facade-first framing: honest and adequately fail-closed.**

The reframe is structural, not cosmetic. Purpose (L44-48) opens with a bounded
*investigation* of whether a facade is needed and states T0 may terminate before
DESIGN. Scope (L52) says "Target hypothesis". Six of seven candidates are
`DOC_ONLY_NEW_HYPOTHESIS`.

One detail shows the classification was applied deliberately rather than
globally: `AgentHostMessageRequest` remains plain `DOC_ONLY_NEW` — correctly,
because `send` is the one operation with no existing owner.

**Duplication risk: closed.** The overlap matrix grew from 10 to 14 rows, adding
exactly the owners round 1 identified as unguarded:

| Concern | Disposition | Verified owner |
|---|---|---|
| authority, risk, checkpoints, budget | `REJECT_SECOND_AUTHORITY_OR_BUDGET_MODEL` | `MaoAuthorityEnvelope` L49, `MaoBudgetAllocation` L32, `buildAuthorityEnvelope` L138 |
| task state and terminal classification | `REJECT_SECOND_STATE_LATTICE` | `MaoTaskState` L16, `MAO_TERMINAL_STATES` L28, `isTerminalState` L37 |
| deterministic status projection | `REJECT_SECOND_STATUS_OWNER` | `buildReadModel` L54, `readModelsAreEqual` L101 |
| secret-safe evidence and retention | `REJECT_SECOND_EVIDENCE_OWNER` | `MaoReceiptKind` L31, `redactFields` L98, `evaluateRetention` L347 |

With the retained launcher, lifecycle, store, receipt, and handoff rejections,
plus T1's stop boundary (L395) forbidding "any second state, receipt, authority,
budget, lifecycle, or launcher owner", **the roadmap can no longer create a
second state, authority, budget, receipt, lifecycle, or launcher owner.** AHB,
workspace, EAIC, and Model Gateway remain referenced, never redefined.

**Direct-composition cancel path: present and load-bearing.** It appears in four
independent places — T0 objective (L394), Design Control Gate (L378), tranche
note (L405), Epistemic Claim Update (L508) — so no single edit reopens it.

**Minimum evidence for a positive T0.** All four round-1 conditions are now
roadmap obligations: the 17-file inventory with per-concept
`ALREADY_OWNED` / `PARTIALLY_OWNED` / `GENUINELY_ABSENT` classification; an exact
semantic negative search with scope, hit set, and reconciliation; a
direct-composition-versus-facade comparison; and **at least two consumers with
materially different lifecycle shapes** (L160, L376, L394). Add only N-01's
refinement.

---

## 6. Lifecycle Semantics Verdict

| Operation | Verdict | Residual |
|---|---|---|
| `dispatch` | **Accepted.** L257 projects `MaoAuthorityEnvelope` and existing launcher/invocation inputs instead of inventing an envelope. Identity allocation and capability discovery are explicit T1 decisions rather than silent omissions. Adds stale authority to fail-closed conditions. | T1 decisions, correctly scoped |
| `send` | **Accepted as the one genuine gap.** Absence independently confirmed. All four required semantics are T1/T2 obligations with a threat row and proof case. | T1/T2-owned |
| `wait` | **Accepted, subject to N-01.** Correctly recast as composition of heartbeat, timeout, orphan, ledger, and read-model owners. Adds `stale` to returns and requires coherence with `status`. | N-01: classify `PARTIALLY_OWNED`, not a peer of `send` |
| `interrupt` | **Accepted.** Effect-versus-response idempotency cleanly separated; proof case admits differing responses across state advancement. Reuses the verified cancellation owners (`requestCancel` L118, `acceptCancel` L123, launcher `requestCancellation` L436, `acceptCancellation` L452). | none |
| `status` | **Accepted.** Total mapping from `MaoTaskState`; monotonicity, freshness, and milestone vocabulary assigned to T1; second lattice prohibited; recoverable-hold preservation stated in the semantic, the overlap matrix, the threat matrix, and a dedicated proof case. | T1-owned specifics |

**Cross-cutting.** Capability discovery now has a named T1 decision with three
enumerated options. Timeout/orphan/retry ownership is bound to
`lifecycle.controller.contract.ts` with verified anchors. Wait/status coherence
has both a threat row (L278) and a proof case (L307). The one remaining
question — how the normalized readout surfaces `SAFE_RETRY` versus `ESCALATE` —
now sits inside T1's mapping obligation rather than being unassigned.

**Agent sovereignty preserved verbatim.** L197-232 are unchanged from the
original. The schema-field-versus-opaque-payload distinction and the negative
proof case (L313) survive intact, as recommended in round 1.

---

## 7. Tranche And Authority Verdict

**No authority leakage. No dispatch-ready wording.**

| Tranche | Verdict |
|---|---|
| T0 | May terminate the roadmap; entry requires accepted repair re-review, operator selection, and fresh documentation-only authority; objective carries all four audit obligations. **Correct.** |
| T1 | Entry is "accepted **positive** T0 plus fresh DESIGN authority"; objective is conditional ("only if T0 proves a genuine gap"). **Correct.** |
| T2 | Freezes send ordering/idempotency, effect-versus-response idempotency, milestone vocabulary, overhead thresholds, **and harness design**; forbids post-hoc tuning. **Correct.** |
| T3 | Builds only the seam, measured by the T2-frozen harness. **Correct.** |
| T4 | "legitimate terminal state for this roadmap". **Correct.** |
| T5 | Conditional; requires fresh operator scope-expansion satisfying an NP-03 Minimal Unblock Condition option; both EAIC tokens cited; "may be permanently unreachable"; proof matrix uses `T5_CONDITIONAL_MAY_BE_UNREACHABLE`. **Correct.** |
| T6 | "only if T5 becomes reachable and closes"; labelled `T6_CONDITIONAL_MAY_BE_UNREACHABLE`. **Correct.** |
| T7 | Closes on "the actual terminal tranche, including T0 cancellation or T4 terminal closure". **Correct.** |

Boundary controls re-verified: `NO_DESIGN_RELEASED`; Machine Closure Package
`N/A with reason`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`;
`runtimeMode` `READ_MODEL_ONLY`; Next Allowed Move names re-review as the only
next action and releases nothing; `WORKER_MUST_NOT_COMMIT honored` with all three
files untracked and nothing staged.

Worth recording as good practice: R2 L375-379 discloses that the **full gate
FAILs** with 10 system-chain freshness violations and states the failure "does
not touch any of the three packet paths and is **not waived**". That is honest
reporting of an adverse result rather than a selective PASS claim.

---

## 8. External Critique Routing Verdict

**The round-1 critique remains `NOT_CVF_SOURCE`. Routing is correct.**

- `docType: external-critique (NOT_CVF_SOURCE)` retained; Claim Boundary
  reasserts it at both head and tail.
- The wrapper's own risk table states "no Source Verification ACCEPT row may cite
  this file".
- **No Source Verification ACCEPT row cites the critique.** I checked all 18
  rows; every one cites a CVF-governed path.
- Dependency row L92 classifies the critique
  `SATISFIED_AS_INPUT_NOT_AUTHORITY`.
- R2's External Knowledge Intake Routing sets `REJECT_DIRECT_IMPORT` and records
  that accepted findings were "independently reproduced in CVF-governed sources
  before repair". The declaration-anchor precision verified in Section 2.1 is
  consistent with genuine re-verification rather than transcription.
- No provider-specific memory, private API, tool behavior, or session
  observation appears in any Source Verification row.
- The worktree path is marked `TRANSIENT_PATH_NOT_A_DEPENDENCY` in all three AOT
  blocks; `git worktree list` confirms same-repository topology.

The governed wrapper does **not** promote the critique to authority — it
disclaims that explicitly in four places. N-02 concerns manifest disclosure of
the wrapper, not the routing itself.

**This re-review carries the same class.** It is `NOT_CVF_SOURCE` and must be
routed as external input, not cited as authority.

---

## 9. Reviewer-Verifiable Acceptance Criteria — Disposition

Dispositioning the six boxes the repair left `[ ]` for the re-reviewer (M-05):

- [x] dependency tokens, continuity evidence, and Source Verification anchors are
  exact at the integration base — **verified; all declaration anchors re-resolved**
- [x] the 17-file owner matrix and facade-first framing prevent a second state,
  receipt, authority, budget, lifecycle, launcher, store, or handoff owner —
  **verified**
- [x] T0's negative-search, consumer, composition, and cancellation criteria are
  sufficient to test whether the facade has value — **verified, subject to N-01**
- [x] `send`, `wait`, `interrupt`, `status`, capability discovery, and overhead
  obligations are complete enough for later T1/T2 authoring — **verified**
- [x] T2 freezes thresholds and harness design before T3 implementation —
  **verified**
- [x] the repaired packet is acceptable while remaining PARKED — **verified**

---

## 10. Value And Go/No-Go Verdict (unchanged in substance from round 1)

Expected value remains **moderate**, and the repaired roadmap now says so itself
rather than implying more. Four of five operations are owned; `send` is the one
genuine absence; `wait` needs at most a composition helper; external ingress is
gated behind an EAIC verdict of `NO_VIABLE_BOUNDED_PATTERN`. The honest ceiling
is: *normalize what exists, add `send`, stop at T4.*

**Minimum evidence to proceed past T0** — now roadmap obligations: recorded
semantic negative search; two consumers with materially different lifecycle
shapes; written direct-composition-versus-facade comparison; per-concept
ownership classification across all 17 files.

**Evidence that should cancel the uplift:** T0 finds the operations expressible
by composition with acceptable ergonomics; only one consumer is ever identified;
EAIC scope expansion is declined; or the overhead budget cannot be stated in
measurable terms at T1.

**Disposition: remain PARKED.** The packet is accepted as a parked planning
artifact. Acceptance is not selection, and selection is the operator's.

---

## 11. Final Repair Matrix

`NONE — packet may remain PARKED awaiting decision-owner selection and fresh T0 authority.`

The three items below are T0-authoring refinements, not conditions on accepting
this packet.

| Finding ID | Artifact | Required repair | Acceptance evidence | Blocking |
|---|---|---|---|---|
| N-01 | Roadmap L153, L259; T0 objective L394 | Classify `send` `GENUINELY_ABSENT` and `wait` `PARTIALLY_OWNED (primitives owned, composition absent)`; state a composition helper alone does not establish facade value | T0 ownership ledger distinguishes the two gap kinds | `NON_BLOCKING` |
| N-02 | R2 worker return L364 | Disclose the governed-wrapper addition in the Changed Files row | Row states worker added wrapper metadata only, substantive findings unchanged | `NON_BLOCKING` |
| N-03 | Critique wrapper L86-93 | At T0, restrict collision tables to tokens the search pattern can match | T0 collision table lists only pattern-matchable tokens | `NON_BLOCKING` |

---

## 12. What The Repair Got Right

Recorded so future edits do not regress strengths:

1. **The repair is source-real.** Every added declaration anchor resolves
   exactly. This is the single strongest signal that findings were reproduced
   rather than transcribed.
2. **The reframe is structural.** Purpose, Scope, candidate table, T0 objective,
   Design Control Gate, and Epistemic block all moved together to facade-first.
   No stale "missing port" claim survives in one corner.
3. **Overlap matrix now covers the owners round 1 found unguarded** — authority,
   budget, state lattice, status projection, evidence readout.
4. **Adverse results are disclosed**, including the 10-violation system-chain
   gate failure marked explicitly "not waived".
5. **Agent sovereignty preserved verbatim** rather than being rewritten during
   an unrelated repair.
6. **The critique's adverse findings were preserved** when wrapping it,
   including the disposition most damaging to the packet.
7. **Cancel authority is redundantly encoded** in four places.

---

## 13. Reviewer Process Disclosure

- Verification base `4fd1b6177`; artifacts read at worktree base `95340497f`.
- Read-only throughout; no file modified, staged, or committed by this
  re-review. This document is a new file and changes no existing artifact.
- Methods: declaration-line extraction, file line counts, literal-token
  searches, reproduced negative search and MAO manifest, path existence checks,
  `git status --short`, `git worktree list`, and a diff of the round-1 critique
  against its placed copy.
- I ran **no** test, build, runtime, provider, network, or governance-checker
  command. Where R2 reports checker outcomes — including its disclosed
  61-of-62 reviewer-fast result and the 10-violation system-chain failure — I
  neither confirm nor dispute them.
- Section 2.1 is direct verification. N-01's characterization of `wait`
  primitives rests on symbol extraction, not full reads of the four contract
  files; it remains a **reviewer hypothesis for T0 confirmation**.

## Claim Boundary

This canonical intake copy remains external re-review input and
`NOT_CVF_SOURCE`. The local wrapper and wording normalization exist only to
satisfy governed review structure and machine parsing; they do not change the
external verdict, release the roadmap, or authorize T0, DESIGN, BUILD,
provider/live, commit, merge, public-sync, deployment, or production work.
