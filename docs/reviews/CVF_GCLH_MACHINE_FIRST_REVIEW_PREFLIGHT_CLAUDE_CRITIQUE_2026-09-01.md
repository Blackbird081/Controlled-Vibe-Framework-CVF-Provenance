# CVF GCLH Machine-First Review Preflight Claude Critique

Memory class: governed-review

Status: ADVISORY_EXTERNAL_CRITIQUE_PENDING_CVF_ABSORPTION

docType: review_context

Date: 2026-09-01

Batch ID: GCLH-MFRP-P0

## Review Identity

| Field | Expected | Observed | Result |
|---|---|---|---|
| Target roadmap | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | same path present | MATCH |
| Filesystem-byte SHA-256 | `b89119ae5791154a463032a5c7c3acbe3e511e9939edae20cc47af083da98c20` | `b89119ae5791154a463032a5c7c3acbe3e511e9939edae20cc47af083da98c20` | MATCH |
| Status | `DRAFT_FOR_CLAUDE_CRITIQUE_IMPLEMENTATION_HOLD` | line 5 identical | MATCH |
| Planning base | `90c2952b642e962c274e07f1f1f5b7cda03d4451` | ancestor of HEAD `d5a1ed352` | MATCH |
| Worktree at review start | clean expected | `git status --porcelain` empty | CLEAN |

Identity gate PASS. No `BLOCKED_TARGET_DRIFT`. The hash was recomputed from
filesystem bytes, not read from the roadmap's own declaration.

## Executive Verdict

Disposition: `REVISE_BEFORE_P1`.

The direction is sound and the roadmap is unusually honest about its own
risks. But source inspection shows the roadmap **understates how much of its
proposal already exists**, and therefore mis-sizes both the work and the
threat model. Three facts dominate this critique:

1. A machine verification receipt with content-addressed caching **already
   ships** as `cvf.autorun.pass-receipt.v1` in
   `governance/compat/run_agent_autorun_workflow_gate.py`. The roadmap
   proposes it as new.
2. That existing receipt has a **real, currently-live verifier-trust hole**:
   `_command_manifest_hash` hashes argv strings only, so editing a checker's
   body does not change the manifest hash. The roadmap's anti-self-attestation
   rule 3 is therefore not a future safeguard - it is an unfixed present
   defect, and closing it is the single most valuable thing in this roadmap.
3. Canonical receipt hashing is **already solved** at
   `cvf.sotThreeLayer.receiptHash.v1` (RFC 8785 JCS, published test vector).
   The roadmap defers canonicalization as an open question and so risks
   minting a second, divergent profile.

Read together: the roadmap's genuine value is roughly one hardening tranche
plus a readout, not an eight-tranche P0-P7 program. The eight-tranche shape is
the largest cost defect and the main route by which this becomes a second
governance system.

## Source Verification

| Surface | Depth | What was actually confirmed |
|---|---|---|
| target roadmap | FULL (470 lines) | all claims below quoted from read text |
| critique packet | FULL (320 lines) | assignment, twelve questions, mandatory probes |
| `review_cost_control/...CONTROL_STANDARD.md` | FULL (446 lines) | owns `elapsedReviewMinutes`, `providerCallCount`, `tokenOrQuotaUsage`, five-token `stopDisposition`, round-three rule, single-pass SOP, ENFORCE/REVIEWER_JUDGMENT matrix |
| `semantic_convergence_control/...CONTROL_STANDARD.md` | FULL (412 lines) | schema `cvf.semanticConvergenceControl.v1`; thirteen invariants; predecessor path+sha256 recomputed not trusted; invariant 13 evidence binding |
| `sot_three_layer/README.md` | FULL (193 lines) | `cvf.sotThreeLayer.receiptHash.v1`, RFC 8785 JCS, test vector; bounded-not-global activation |
| `truth_foundation/README.md` | FULL (118 lines) | provenance labeling and claim-movement ownership |
| `run_agent_autorun_workflow_gate.py` | TARGETED (receipt/cache/exec paths, ~lines 30-360) | `RECEIPT_SCHEMA`, `_command_manifest_hash`, `_worktree_fingerprint`, `_load_valid_receipt`, `_write_receipt` |
| `run_agent_commit_steward_preflight.py` | TARGETED (`build_path_plan` 189-226) | changed-path plan feeds the fingerprint |
| `GCLH_T1_INTEGRATED_CORE_CONTROL_DESIGN` | TARGETED (Amendment 2, claim boundary) | five-step minimal review sequence; no global SOT3 claim |
| `external_agent_review/` family | INDEX ONLY | absorption workflow and packet template exist |
| `check_governed_file_size.py` + registry | TARGETED | `active_markdown` soft 900 / hard 1200 lines |
| `run_agent_automation_assist.py` (1318 lines) | NOT INSPECTED | see limitation below |
| 196 `check_*.py` sources | NOT INSPECTED individually | see limitation below |

Declared limitations. I did not read the 1318-line automation-assist helper
body, so my "extend AAF rather than add an entrypoint" recommendation is
argued from the owner map and the roadmap's own cost budget, not from
inspecting that helper's extension seams. I did not inspect all 196 checkers,
so Question 5's feasibility answer rests on the autorun gate's actual command
construction rather than a per-checker survey. Neither gap changes the
disposition, because the three dominant findings all rest on surfaces read in
full or at the exact symbol level.

## Answers To The Twelve Review Questions

**Q1 - Is a new Phase Return interface owner justified?**

Not as a new reference family, on current evidence. SCEC already owns stable
problem identity, predecessor path+digest binding, blocker set algebra and
per-blocker evidence binding. Review Cost already owns cost/telemetry and the
stop vocabulary. The genuinely unowned sliver is narrow: the *receipt* contract
binding a verifier set to a return. Recommendation: extend SCEC's schema family
with a sibling `cvf.machineVerificationReceipt.v1`, and place envelope
requirements in the work-order template. A new family should open only if P1
demonstrates a concrete required field that neither SCEC nor the template can
host - and the roadmap should state that as a falsifiable test, not a
preference.

**Q2 - Which machine checks cross into semantic truth?**

Three in the proposed always-on core.

- "source/authority resolution and **freshness**." Resolution is mechanical;
  freshness is not. Whether a resolvable authority is *stale for this claim* is
  semantic. Split into `resolves` (machine) and `is-current-for-this-claim`
  (reviewer).
- "**hard-obligation coverage**." A machine can prove an obligation ID has a
  linked evidence record. It cannot prove the evidence discharges the
  obligation. The authority matrix says this correctly, but the Always-On list
  drops the qualifier. Rename to `hardObligationLinkPresence`.
- "**exception completeness**." A machine can only prove completeness relative
  to exceptions it can express. Calling that "complete" is the automation-bias
  seed. Rename to `declaredExceptionIntegrity`.

SCEC already models this discipline correctly and states the limit explicitly:
unique locator occurrence "does not establish relevance, correctness, or
semantic truth." Every MFRP check should carry an equivalent sentence.

**Q3 - Does the receipt bind enough, and only enough?**

Enough, no. Only enough, no. Both directions are wrong.

Under-binding: `verifierSetDigest` and `verifierVersions[]` are undefined. If
`verifierSetDigest` follows the existing `_command_manifest_hash` precedent -
hashing argv - it does not bind checker **bytes**, and the receipt is forgeable
by editing a checker in place. It must bind the SHA-256 of each verifier source
file. Also missing: the interpreter version, and any config or fixture path a
verifier reads. Both change results without changing argv.

Over-binding: `repositoryTreeOrCommit` at whole-tree granularity guarantees a
near-total cache miss rate, since any unrelated file invalidates every receipt.
That silently converts the cache into dead weight while adding hashing cost.
Bind the changed-path set plus verifier bytes instead - which is what
`_worktree_fingerprint` already does via `steward.build_path_plan`.

**Q4 - Can a worker still influence the verifier accepting its own return?**

**Yes - today, in shipped code.** This is the strongest finding; see FM-1. The
roadmap's rule 3 is necessary but under-specified in one decisive way: it says
"if a batch changes a verifier used by its own receipt." Machine enforcement
needs the contrapositive - the receipt must *prove* which verifier bytes ran,
or "the batch did not change a verifier" remains an unverifiable worker
assertion. Rule 3 must be restated as a receipt-content requirement, not a
batch-scope rule. Configuration and fixtures need the same treatment: the
size-exception registry is worker-editable JSON that directly changes checker
verdicts.

**Q5 - Is verifier-set digesting feasible with current catalogs?**

Yes, and more cheaply than the roadmap assumes. Commands come from a static
import (`agent_autorun_command_catalog`) with a small phase-conditional
prepend, not from arbitrary dynamic dispatch. Resolving argv to script paths
and hashing those files is a bounded change to one existing function; cost is
tens of file hashes per gate run. The roadmap's implied difficulty here is
overstated, and that matters: this is the highest-value, lowest-cost item, yet
it sits at P2 behind a schema program.

**Q6 - Does the cache have a safe, affordable invalidation boundary?**

Affordable yes; safe not yet - and no dependency graph is needed, which also
answers the roadmap's own Q7. The existing three-part key (`baseSha`/`headSha`,
`commandManifestHash`, `worktreeFingerprint`) is the right shape and already
proves affordability. Its live gap is exactly the Q3/Q4 gap: verifier bytes and
environment are absent from the key. Adding those two is a small, closed fix.
What should be dropped is the open-ended "relevant environment fingerprint,"
which is unbounded as written. Replace it with an enumerated, fail-closed list
(interpreter version, verifier bytes, config/fixture digests) and treat
anything unenumerated as a cache miss.

**Q7 - Could exception-focused readout hide a material claim?**

Yes, in two distinct ways worth separating.

- *Filter failure* (FM-3): a material item is never classified as an exception,
  so it never reaches the reviewer.
- *Automation bias* (FM-2): the item is shown, but a prominent PASS suppresses
  scrutiny of it.

The roadmap treats these as one risk and mitigates only the first. The bias
risk is worsened by a specific line: the readout is to include an "explicit
statement that no rerun is needed." That sentence converts a mechanical result
into review advice and should be removed. The readout should state coverage and
limitations and let the reviewer conclude. It must also always print what was
**not** checked - unchecked scope is the material fact a PASS-only summary
erases.

**Q8 - Are always-on versus phase-specific packs correctly split?**

Mostly, with two corrections. "Protected-path and external-effect escalation"
overlaps commit-steward path classification and should be declared as reuse,
not restated as a new always-on check. Conversely, **secret-safe output must
never be phase-conditional or cacheable** - it is the one check that must run
on every emission path including cache hits, since a cached receipt could
replay sanitized output while fresh output leaks. The phase packs are otherwise
reasonable; the WORK ORDER pack duplicates checker read-ahead that already
exists as a checker.

**Q9 - Is replay/canary evidence sufficient?**

The replay families are well chosen - notably "worker-modified verifier used
for self-acceptance," which the current gate would fail. But P4 is
under-specified in the one dimension that decides credibility: no minimum count
and no requirement that fixtures come from **real historical returns with known
outcomes**. Synthetic fixtures authored alongside the verifier test the
author's imagination, not the corpus. Minimum credible basis: every
zero-tolerance class needs at least one fixture derived from an actual past CVF
return, and the false-negative ledger must be frozen *before* canary - the
roadmap says this for seeded defects but not for the corpus sample.

**Q10 - Which metrics are cheap, which invite gaming?**

Cheap and already owned: `providerCallCount`, `materialCommitCount`,
`continuityCommitCount`, `reviewRoundCount` - all existing Review Cost fields.
MFRP should **consume** these, never re-declare them; re-declaration is the
exact ceremony the roadmap warns against while creating.

Gaming-prone: "reviewer elapsed minutes" (already exempted as often
unavailable, so a trend line built on it is unsound), "machine exception
precision" (improvable by suppressing true positives - precision without recall
rewards hiding findings), and "focused probes per review" (the roadmap itself
concedes count is not quality, so it should not be a metric).

Keep: seeded-defect recall and escaped material defects. Those two carry nearly
all the safety signal. Cut the rest to what Review Cost already collects.

**Q11 - Are rollback and reactivation credible?**

Structurally yes - config/routing based, receipts preserved, reactivation
repeats replay, operator override insufficient. That last clause is the
strongest sentence in the roadmap. One credibility gap: every listed rollback
trigger is *detectable only by the route being replaced*. If machine-first
routing lets a defect through, the legacy route is no longer running to notice.
Rollback triggers therefore need an independent detection source - a sampled
dual-run during canary, or a defined post-hoc audit cadence. Without one, "any
escape triggers rollback" is not operationally credible.

**Q12 - What should be removed, simplified, added or reordered?**

Remove: the new reference family (Q1); the "no rerun is needed" readout line
(Q7); the three low-value metrics (Q10); whole-tree `repositoryTreeOrCommit`
(Q3). Simplify: adopt `cvf.sotThreeLayer.receiptHash.v1` instead of authoring a
canonicalization profile. Add: verifier-byte binding, interpreter/config
binding, an independent rollback detection source, an explicit
`notCheckedScope` readout field. Reorder: see the revised sequence below.

## Strongest Failure Modes

### FM-1 - Verifier body edit is invisible to the existing receipt hash

- **Attacked assumption:** that pinning a "verifier set" via a command manifest
  binds the verifier.
- **Source:** `governance/compat/run_agent_autorun_workflow_gate.py`,
  `_command_manifest_hash` (hashes only `{"name", "command": [argv]}`);
  `_receipt_context`; `_load_valid_receipt`; `RECEIPT_SCHEMA =
  "cvf.autorun.pass-receipt.v1"`.
- **Sequence:** A worker edits a checker body in `governance/compat/` to weaken
  an assertion, leaving argv unchanged. `_command_manifest_hash` is
  byte-identical. The gate runs, the weakened checker passes, and a PASS receipt
  is written. The receipt names the command that ran but proves nothing about
  the code that ran.
- **Would existing guards catch it?** Partially, and not by design.
  `_worktree_fingerprint` hashes the contents of changed paths, so if the
  checker edit is *inside the reviewed range* the fingerprint differs and the
  cached receipt misses - the checker still runs weakened, but the receipt is at
  least fresh. The dangerous case is the **cross-batch** one: the checker was
  modified in an earlier batch, so it is not in the current changed set, and no
  receipt field records which checker bytes executed. Nothing in the receipt
  distinguishes a run against hardened code from a run against weakened code.
  Path protection is asserted in the roadmap as a future control, not
  demonstrated in current source.
- **Minimal correction:** resolve each command's script path and include those
  files' SHA-256 values in the manifest hash; record them as
  `verifierVersions[]` in the receipt.
- **Blocks:** this is a **present defect in shipped code**, not merely a P1
  design question. It should be fixed as its own bounded protected-path tranche
  and should not wait for the full MFRP program.

### FM-2 - Machine PASS induces reviewer automation bias (false confidence)

- **Attacked assumption:** that reviewers reliably read PASS as "shape checked"
  rather than "return is fine."
- **Source:** roadmap `## Reviewer Minimal Sufficient Verification`, which pairs
  a "machine PASS/FAIL/BLOCK summary" with an "explicit statement that no rerun
  is needed"; Review Cost `REVIEWER_JUDGMENT` rows, which assign the reviewer
  precisely the judgments a PASS cannot make.
- **Sequence:** The envelope is well-formed, every hard obligation has a linked
  evidence record, the manifest reconciles - the receipt reads PASS. The
  evidence is real but does not substantively discharge the obligation, which
  the machine by contract never evaluates. The readout leads with PASS and adds
  that no rerun is needed. Over repeated reviews the reviewer's prior shifts and
  the semantic step degrades into confirming the machine.
- **Would existing guards catch it?** No. The roadmap says the reviewer "may not
  use helper PASS as semantic truth," but that is an instruction to a human, not
  a control - and it is contradicted by the same section's rerun advice. Review
  Cost enforces that a `stopDisposition` token is *present*, explicitly not that
  it is the semantically correct one. No machine surface detects this drift, and
  its signature - faster reviews, fewer findings - is exactly what the MFRP
  metrics count as **success**. That inversion is the core danger.
- **Minimal correction:** remove the rerun-advice line; require the readout to
  lead with `notCheckedScope` and limitations before any PASS; rename the
  summary from PASS to a non-verdict token such as
  `DETERMINISTIC_CHECKS_COMPLETE`; and track finding rate per review as a safety
  signal, not an efficiency one.
- **Blocks:** activation (P5/P6). Does not block P1-P2.

### FM-3 - Exception filter suppresses the one material item

- **Attacked assumption:** that "material" is a machine-decidable partition.
- **Source:** roadmap `## Reviewer Minimal Sufficient Verification` ("only
  unresolved exceptions and material claims"); contrast SCEC invariant 4, which
  fails closed on *silent blocker disappearance* - a filter designed on the
  opposite principle.
- **Sequence:** A return carries a limitation the verifier has no rule to
  express - for example an authority path that resolves correctly but whose
  owner meaning has changed. It produces no exception, so it is filtered out of
  the readout. The reviewer, working from the readout by design under Amendment
  2's minimal-verification sequence, never sees it. The filter has converted an
  unmodeled risk into an invisible one.
- **Would existing guards catch it?** No. SCEC's set algebra prevents silent
  disappearance of *declared* blockers, but an item never declared as an
  exception falls outside that algebra entirely. This is the "authority path
  resolves but semantic owner meaning is wrong" probe, and the roadmap's design
  cannot catch it, because the item is semantically material and mechanically
  clean.
- **Minimal correction:** adopt SCEC's fail-closed posture in the readout -
  anything the verifier cannot classify is surfaced as `UNCLASSIFIED`, never
  dropped. Filtering may reorder and de-emphasize; it may never remove.
- **Blocks:** P3 (readout design), since it is a contract property rather than a
  tuning parameter.

### FM-4 - Cost of the machine layer exceeds the review cost removed

- **Attacked assumption:** that eight tranches of governance authoring pay back
  in reviewer minutes.
- **Source:** roadmap tranche table (P0-P7); Review Cost 10-minute fast-path
  target and `DEFAULT_ONE_MATERIAL_ONE_CONTINUITY` choreography.
- **Sequence:** Each tranche is itself a governed CVF batch requiring baseline,
  work order, review, telemetry, SCEC block and closure - the very ceremony MFRP
  exists to reduce. Eight tranches of that overhead are spent to save minutes on
  reviews already targeted at ten minutes, while the concrete safety win (FM-1)
  sits at P2.
- **Would existing guards catch it?** Only after the fact. The roadmap's own "if
  telemetry cost exceeds saved review cost, simplify or stop" is the right
  instinct but has no baseline: no current reviewer-minute measurement is cited,
  so the payback test is unfalsifiable as written.
- **Minimal correction:** measure the baseline in P1 from Review Cost telemetry
  already being collected; split FM-1 out as an immediate standalone hardening
  tranche; collapse P2-P3.
- **Blocks:** P1 scope, not the direction.

### Mandatory probes not elevated to full findings

*Stale receipt after checker hardening* - real but bounded: hardening a checker
inside the reviewed range changes `_worktree_fingerprint` and misses the cache;
the cross-batch case is FM-1 and is fixed by the same correction. *Manifest
under-declaration* - already owned by `build_path_plan`, which reconciles range
paths with `_status_paths()`; MFRP should declare reuse rather than restate it.
*Cache hit across a hidden environment change* - real and currently unbound (no
interpreter version in the receipt context), corrected by the Q6 enumerated key.
*High-risk/live/public/destructive path* - out of scope here; no provider
surface is authorized in P0-P4.

## Owner Placement Recommendation

Do not open a new reference family in P1. Place the contract as:

| Element | Recommended owner | Rationale |
|---|---|---|
| envelope required fields | `CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | already owns dispatch/return shape |
| predecessor/evidence binding | SCEC `cvf.semanticConvergenceControl.v1` | invariants 2 and 13 already do this |
| receipt schema | new sibling `cvf.machineVerificationReceipt.v1` in SCEC's family | narrow, versioned, adds no doctrine |
| receipt hash profile | reuse `cvf.sotThreeLayer.receiptHash.v1` | RFC 8785 JCS with published test vector |
| cost/telemetry | existing `review_cost_control/` fields | consume, never re-declare |
| execution and caching | `run_agent_autorun_workflow_gate.py` | receipt/cache already implemented there |
| readout | extend `run_agent_automation_assist.py` | the roadmap's own budget forbids a competing entrypoint |

The falsifiable test for a new family: P1 must exhibit a required field that
cannot live in any surface above. Absent that, no family.

## Receipt, Verifier And Cache Corrections

1. `verifierSetDigest` must hash **verifier file bytes**, not argv (FM-1).
2. Add `interpreterVersion` and digests of every config/fixture a verifier
   reads - including `CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json`, which is
   worker-editable and changes verdicts.
3. Replace whole-tree `repositoryTreeOrCommit` with the changed-path plan
   fingerprint already computed by `_worktree_fingerprint`.
4. Adopt `cvf.sotThreeLayer.receiptHash.v1`; do not author a second profile.
5. Enumerate the cache key exhaustively and fail closed on anything
   unenumerated. No dependency graph is required.
6. Restate anti-self-attestation rule 3 as a receipt-content property: the
   receipt proves which verifier bytes ran. A batch-scope rule is a worker
   assertion.
7. Exclude secret-safe output from all caching.
8. Version the receipt schema from day one; an unrecognized schema version fails
   closed rather than being ignored.

## Replay, Canary And Rollback Corrections

- Fix a minimum fixture count per zero-tolerance class in P1, and require at
  least one fixture per class drawn from a **real historical CVF return**.
- Freeze the false-negative ledger before canary, not during it.
- Add an independent detection source for rollback triggers - sampled dual-run
  or a defined post-hoc audit - since the replaced route cannot report escapes.
- Add one replay family the roadmap omits: **verifier changed in a prior batch**
  (the FM-1 cross-batch case). The listed family covers the same-batch case only.
- Keep the rule that operator override alone cannot reactivate. It is correct
  and should survive absorption unchanged.

## Cost And Ceremony Cuts

- Cut the new reference family (Q1).
- Cut re-declared telemetry; consume Review Cost fields (Q10).
- Cut `focused probes per review`, `reviewer elapsed minutes` as a trend metric,
  and `machine exception precision` as an optimization target.
- Cut the per-checker metadata program unless replay proves group-level mapping
  insufficient - the roadmap already says this; hold it to that.
- Collapse P2 and P3 into one tranche; a schema and its only consumer should not
  be separately ratified.
- Measure the reviewer-minute baseline in P1, or the payback test stays
  unfalsifiable (FM-4).

## Revised Tranche Sequence

| Tranche | Mission | Change from roadmap |
|---|---|---|
| MFRP-H0 | **verifier-byte binding hardening** of the existing autorun receipt | **NEW, do first** - closes a live defect (FM-1); independently valuable even if MFRP stops |
| MFRP-P1 | owner ratification, reviewer-minute baseline, threat model | adds baseline measurement; no new family |
| MFRP-P2 | receipt schema plus verifier library and hostile tests | absorbs old P3 |
| MFRP-P3 | readout composition, fail-closed `UNCLASSIFIED` surfacing | adds the FM-3 correction |
| MFRP-P4 | historical replay with real-return fixtures | adds a corpus-derived minimum |
| MFRP-P5 | shadow canary with sampled dual-run | adds independent detection |
| MFRP-P6 | selective gate activation | unchanged |
| MFRP-P7 | seven-phase and downstream adoption | unchanged; still after Core closure |

H0 first is the substantive reordering. If CVF adopts only one item from this
critique, it should be H0 - it closes a real hole today at a fraction of the
program's cost.

## Final Disposition

`REVISE_BEFORE_P1`

The machine-first direction is justified, and the roadmap's governing principles
and rollback rules are sound. It must not proceed to P1 unchanged, because it
would open a new owner over ground SCEC and Review Cost already hold, defer a
canonicalization question SOT3 already answered, and schedule behind six
tranches the one fix that closes a live verifier-trust hole. The
false-confidence risk (FM-2) is real and partly self-inflicted by the readout's
rerun advice, and the exception filter (FM-3) needs SCEC's fail-closed posture
before P3.

Second governance system: the risk is genuine but avoidable, and it concentrates
almost entirely in the new-reference-family decision. Decline the family and
consume the existing owners, and this becomes an extension of CVF rather than a
parallel to it.

## Claim Boundary

This critique is advisory external input pending CVF absorption and
reconciliation. It defines no governance semantics, accepts no architecture,
opens no tranche, and overrides no standard, checker or review. Its source
claims must be re-verified by CVF before use as evidence. Findings about
`run_agent_autorun_workflow_gate.py` describe source read at HEAD `d5a1ed352`
and are static-read claims; no gate, checker, test or provider call was
executed, so no runtime, live-proof, deployment, public-sync or production
readiness claim is made. Two surfaces were not inspected and are declared in
Source Verification.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_file_size.py`; `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` thresholds; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | `active_markdown` soft 900 / hard 1200 line boundary; `RECEIPT_SCHEMA`; `_command_manifest_hash`; `_worktree_fingerprint`; `build_path_plan` |
| gateRunPurpose | source verification for critique claims; no gate was executed as acceptance evidence |
| claimBoundary | no machine PASS is claimed for this file; structural conformance remains CVF's to verify during absorption |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | external reviewer (Claude, Opus 5) |
| Provider or surface | Claude Code CLI, local private provenance repository |
| Session or invocation | GCLH-MFRP-P0 critique, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | read-only `sha256sum`, `git rev-parse`, `git status`, `git merge-base`, `git log`, `sed`, `grep`, `wc`, `ls`, `python -c` JSON read; one file write |
| Target paths | this critique file only |
| Allowed scope source | `CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_CLAUDE_CRITIQUE_PACKET_2026-09-01.md` |
| Before status evidence | `git status --porcelain` empty at HEAD `d5a1ed352` |
| After status evidence | one untracked file: this critique |
| Diff evidence | no tracked file modified; nothing staged; nothing committed |
| Approval boundary | one advisory critique file; no implementation |
| Claim boundary | no implementation, downstream, provider/live, public, deploy or production authority |
| Agent type | external review agent |
| Invocation ID | `gclh-mfrp-p0-claude-critique-2026-09-01` |
| Expected manifest | `docs/reviews/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_CLAUDE_CRITIQUE_2026-09-01.md` |
| Actual changed set | same single path |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Core architecture critique context; public-sync is not
authorized.

## Purpose

CVF structural preservation alias added after return: the external review's
purpose is defined by Review Identity and Executive Verdict above. This alias
adds no external finding or authority.

## Scope / Methodology

CVF structural preservation alias added after return: the external review's
scope, read depth, method and limitations are recorded in Source Verification.
The original handback byte hash is retained by the separate CVF reconciliation.

## Findings / Position

CVF structural preservation alias added after return: the external findings
and position are the Executive Verdict, Twelve Review Questions, Strongest
Failure Modes and Final Disposition above. They are not rewritten here.

## Risk / Corrective Action

CVF structural preservation alias added after return: the proposed corrective
actions remain those in Receipt, Verifier And Cache Corrections; Replay,
Canary And Rollback Corrections; and Cost And Ceremony Cuts. This envelope
changes no recommendation or disposition.

## Epistemic Process Block

### Expected Result / Prediction

CVF structural preservation alias added after return: the external review
predicted that source inspection could confirm or refute the roadmap's assumed
owner and implementation gaps.

### Evidence Comparison

The external review compared the roadmap against the source depths declared in
Source Verification and reported the confirmed overlaps and receipt gap in its
Executive Verdict and Twelve Review Questions.

### Contradiction Or Gap Disposition

The external review declared two bounded unread surfaces and kept its final
disposition at `REVISE_BEFORE_P1`; CVF independently handles their effect in the
separate reconciliation.

### Claim Update

This structural alias changes no external claim. The external critique remains
advisory pending the CVF disposition recorded separately.

## External Knowledge Intake Routing

CVF structural preservation alias added after return:

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | bounded Claude critique -> CVF source verification -> required absorption table -> CVF reconciliation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | separate CVF reconciliation; this file remains advisory input |
| Disposition | advisory pending the CVF-owned disposition |
| Claim boundary | this alias adds routing metadata only; no finding becomes authority |
