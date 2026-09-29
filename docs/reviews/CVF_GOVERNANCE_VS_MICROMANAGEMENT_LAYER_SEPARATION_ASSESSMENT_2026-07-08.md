# CVF Governance-vs-Micromanagement Layer Separation Assessment

Memory class: governed-assessment

Status: ASSESSMENT_INPUT_FOR_R72B_INVENTORY

Not a ratified classification: this document is decision input only. The
per-checker BLOCKING/ADVISORY verdict belongs to a later R72B checker
inventory that reads each checker's source; see the Decision section.

Author: Claude (assessment authored at operator request)

Date: 2026-07-08

Claim boundary up front: this is an advisory assessment. It authorizes no
checker deletion, no hook change, no runtime edit, no severity re-tiering, and
no scope reduction. It proposes a classification and a direction for operator
and Codex to decide. Every count below was read from the live repository at
authoring time and is reproducible with the command shown. Note on
reproducibility: the count table normalizes the shell pipe character to the
word "pipe" for Markdown display; the real, runnable commands (PowerShell on
this Windows workspace) are given verbatim in the "Runnable commands"
subsection immediately after the table.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | section name: Purpose; section name: Target / Source; section name: Scope / Methodology; section name: Findings / Position; section name: Risk / Corrective Action; section name: Decision / Recommendation / Disposition; section name: Public Export Disposition; section name: Claim Boundary; enum: DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation evidence after Codex review of the uncommitted assessment; not a claim that Claude read these checkers before first drafting. |
| claimBoundary | This block makes the assessment gate-visible as an R72B input artifact only. It does not promote the assessment to checker-change authority and does not authorize any implementation. |

## Purpose

Give the operator a source-backed classification of the CVF enforcement
surface into governance-grade controls and ceremony-grade controls, and a
recommended direction for keeping the former hard-blocking while demoting the
latter to advisory. (Note recorded as live evidence for Finding 2 below: this
very section exists only because the structural-completeness gate hard-blocked
the assessment for lacking a heading literally named "Purpose", even though a
`## Target / Source` section already stated the same intent. A ceremony gate
blocked a governance assessment on a heading synonym.)

## Target / Source

Target: the current CVF enforcement surface, specifically the direct checker
population under `governance/compat/check_*.py`, the reviewer-fast hook chain
in `governance/compat/run_local_governance_hook_chain.py`, and the
worker-return / dispatch-packet shape gates exercised during MSEA-R72A on
2026-07-08.

Source of evidence: direct execution of those gates during the R72A no-commit
tranche, plus repository inventory commands rerun at assessment authoring time.

## Epistemic Process Block

### Expected Result / Prediction

If CVF's governance layer has drifted into micromanagement, a low-risk,
doc-only tranche should still encounter hard-blocking failures whose harm, if
ignored, is mostly formatting or packet-shape loss rather than authority,
boundary, source-verification, or public/private safety loss.

### Evidence Comparison

The R72A evidence compared against that expectation supports the concern:
several blocks were format or literal-shape failures, while the truly
load-bearing failures were distinguishable as source-fidelity, public-boundary,
or continuity controls. The checker-count and hook-step counts provide
additional scale evidence, not by themselves a retirement decision.

### Contradiction Or Gap Disposition

The assessment does not prove that any individual checker is safe to retire.
That gap is intentionally assigned to R72B inventory and later R72F
criteria-backed retirement review. Any checker with boundary, source,
provenance, public/private, live-proof, or continuity harm remains outside a
blanket demotion claim.

### Claim Update

The assessment's claim remains advisory: CVF needs a governance-vs-ceremony
severity split and a checker lifecycle inventory before any checker deletion,
disablement, consolidation, or severity change. It does not authorize direct
implementation.

## Scope / Methodology

Scope: whether CVF's enforcement surface still separates governance-grade
controls (authority, scope, evidence integrity, cost, review, freeze) from
format-and-ceremony controls (heading spelling, token shape, section ordering,
ASCII discipline), or whether the two have merged into a single hard-blocking
surface that degrades agent effectiveness on low-risk work.

Methodology: this assessment does not theorize. It uses the R72A tranche as a
worked example because that tranche was doc-only, no-commit, and classified
three CI checks, which is near the lowest-risk work CVF governs. The friction
that low-risk tranche encountered is the strongest available signal about
whether the enforcement surface is proportionate. Counts are quantitative and
reproducible; the classification of individual findings as governance-grade or
ceremony-grade is a judgment call and is marked as such.

Explicit limitation: this assessment reviewed the checker population by name
and by the specific gates R72A hit. It did not read the full source of all 186
checkers, and it deliberately does not contain a per-checker
BLOCKING/ADVISORY table, because producing one would require reading every
checker's source and is exactly the R72B inventory work this document is
meant to feed, not pre-empt. What this document does classify is narrower and
fully evidenced: the nine specific findings that blocked the R72A tranche
(Finding 2 table) and the risk/corrective directions (Risk section table).
The broad BLOCKING-vs-ADVISORY split is stated as a principle to test during
R72B inventory, not as a completed per-checker verdict.

## Findings / Position

### Finding 1: the enforcement surface is large and self-replicating

Reproducible counts at authoring time:

| Metric | Value | Command (pipe shown as the word "pipe" to keep the table intact) |
| --- | --- | --- |
| Direct checkers | 186 | `ls governance/compat/check_*.py` pipe `wc -l` |
| Reviewer-fast hook chain steps | 59 | first bracket in `run_local_governance_hook_chain.py --hook reviewer-fast` output |
| Checkers for one concept (`cross_family_approval_artifact`) | 42 | `ls governance/compat/check_cross_family*.py` pipe `wc -l` |
| ADIF defect entries | 26 | `ls docs/reference/agent_defect_intelligence/entries/*.md` pipe `wc -l` |

(The command column above had to write the shell pipe character as the word
"pipe" because a literal pipe inside a Markdown table cell is parsed as a
column separator and broke the table. This is one more small instance of the
same format-tax the assessment describes.)

Runnable commands (PowerShell, this Windows workspace; verified at authoring
time to return 186, 42, and 26 respectively):

```powershell
(Get-ChildItem governance/compat/check_*.py).Count
(Get-ChildItem governance/compat/check_cross_family*.py).Count
(Get-ChildItem docs/reference/agent_defect_intelligence/entries/*.md).Count
```

The reviewer-fast step count (59) is read from the first `[n/59]` bracket in
the output of
`python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`.

The `cross_family_approval_artifact` family is the clearest structural symptom.
It contains checker names that chain the same idea through successive
justification layers, for example a single checker whose name runs:
`approval artifact -> external revocation -> issuer -> proof -> authority ->
provenance -> attestation -> provenance -> freshness -> proof -> verification`.
This is ceremony recursion: each time someone asked "but who attests the
attestation?", a new checker was born. A healthy governance layer stops at
authority plus revocation. Forty-two files for one approval concept is the
enforcement surface auditing itself instead of auditing the work.

### Finding 2: R72A friction was almost entirely ceremony, not governance

R72A required nine repair rounds before the fast gate was clean. Classifying
each blocking finding by whether ignoring it would cause real harm beyond a red
gate:

| Round | Blocking finding | Real governance risk if ignored? |
| --- | --- | --- |
| 1 | missing `Required Artifact Manifest` table | No: duplicated an existing section |
| 2 | missing scope heading in a reference doc | No: pure form |
| 3-4 | non-ASCII em-dash characters | No: character choice |
| 5 | expected-vs-actual manifest path mismatch | Marginal |
| 6 | ten required worker-return headings | Mostly ceremony |
| 7 | step-observation field regex tripped by a bullet-marker prefix | No: checker bug, not author error |
| 8 | remote-URL substring co-occurring with the word "absorption" tripped three external-absorption guards | No: false positive |
| 9 | packet-shape contract had to literally enumerate every term | No: a machine can derive this |

Zero of the nine blocking findings concerned authority, scope, evidence
integrity, cost, or review. The single governance-grade finding surfaced during
R72A (a handoff HEAD-SHA staleness under the In-Place Update Rule) was one the
worker was correctly forbidden to fix. So the enforcement surface blocked the
worker on nine ceremony items and simultaneously blocked the worker from
touching the one real item. That inversion is the core symptom.

### Finding 3: at least two of the nine were self-inflicted checker defects

Rounds 7 and 8 were not author mistakes. Round 7: a required-field regex is
anchored so that a leading list-bullet prefix before the field label makes the
value read as empty. Round 8: three external-absorption guards classify any file
as an absorption artifact when its text contains a full HTTPS remote-URL prefix
co-occurring with the word "absorption", which co-occurs innocently whenever a
file cites the required external-knowledge chain-map (whose filename contains
that word) and also shows `git remote -v` evidence. Both are over-greedy
pattern matches. Per CVF's own error-to-governance-learning philosophy, a
checker that repeatedly fires on innocent input is itself a defect pattern to
fix, not a rule to keep interpreting around.

### Finding 4: hard-block is applied uniformly regardless of harm class

The reviewer-fast chain runs 59 steps and exits non-zero (exit 2 in several
sub-checks) on any failure. An em-dash and a forbidden-commit attempt receive
the same disposition: hard block. This is the actual mechanism by which CVF has
started to borrow governance authority to enforce a linter's conventions. The
problem is not the count of gates; it is that format-grade and governance-grade
controls share one severity and one blocking behavior.

### Counter-position (what must NOT be cut)

The critique should not become an argument to delete controls indiscriminately.
Several controls that look like ceremony are proxies for evidence integrity and
must stay BLOCKING:

- Source Verification tables requiring a real line or section: this blocks an
  agent from citing a symbol that does not exist. That is evidence integrity.
- `N/A with reason` requirements: these block reflexive empty tick-boxes and
  force an explicit, falsifiable "considered and does not apply". That is a
  real boundary, not ceremony.
- No-commit and commit-authority gates: these enforce who may change history.
  Governance-grade, keep hard.

The correct cut line is not "small versus large". It is: if this finding is
ignored, does anything harmful happen beyond the gate turning red? Em-dash: no.
Fabricated symbol: yes. That is the scalpel.

## Risk / Corrective Action

| Risk if left unaddressed | Corrective direction (for operator/Codex decision) |
| --- | --- |
| Agents spend most of a low-risk tranche on format repair, degrading throughput and inviting exactly the tick-box reflex CVF wants to prevent | Introduce a severity split: BLOCKING for authority/scope/evidence/cost/review/freeze; ADVISORY for format/heading/token-shape. Advisory prints and records but does not exit non-zero |
| Self-inflicted checker false positives (rounds 7, 8) keep recurring for every future worker return | Fix the two identified checker defects as ordinary ADIF-tracked corrections; scope is small and low-controversy |
| Enforcement surface keeps self-replicating (the 42-file family) | Freeze new checker creation for already-covered concepts; require that a new checker prove it catches a harm not already caught, not merely a new justification layer |
| Low-risk doc-only no-commit tranches run the full 59-step chain | Route R0/R1 `DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT` work through the existing Fast Lane (GC-021) instead of the full reviewer-fast chain |

## Decision / Recommendation / Disposition

Recommendation: CVF should re-tier, not deflate. The governance layer should
intervene hard at exactly the six surfaces the operator named (authority,
scope, evidence, cost, review, freeze) and should demote format, heading,
token-shape, and section-ordering controls to advisory. This preserves guard
coverage as an audit signal while removing the hard-block authority from
linter-grade conventions.

This is a large, internally political design change: it reduces the governance
layer's blocking reach. It is out of scope for any single tranche and requires
its own GC-018 authorization before any hook-chain or checker behavior is
altered. This document is the assessment input for that decision only.

Proposed sequence if the operator agrees:

1. Treat this document as assessment/decision input only, not as a ratified
   classification. Because it deliberately did not read all 186 checkers
   (see the Explicit limitation above), it cannot itself be the authority
   that ratifies a per-checker split.
2. Run an R72B-style checker inventory that reads each checker's source and
   assigns a per-checker BLOCKING or ADVISORY verdict with a one-line harm
   rationale. Ratify the BLOCKING-vs-ADVISORY principle on the back of that
   inventory, not on the back of this document.
3. Fix the two checker false positives (rounds 7 and 8) as a small bounded
   correction; these are independently justified as ADIF defects and do not
   need to wait for the inventory.
4. Author a GC-018 for the severity split in the hook chain.
5. Only then implement advisory demotion, one checker family at a time, with
   each demotion recording why the control is not harm-bearing.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance assessment. It does not change public-sync, push
public branches, or publish public artifacts.

## Claim Boundary

This assessment records a classification proposal and a recommended direction
only. It authorizes no checker deletion, no hook-chain edit, no severity
change, no runtime or test edit, no commit, no push, and no public-sync
mutation. The BLOCKING/ADVISORY split is a recommendation for operator and
Codex decision, not an implemented state. All counts are reproducible with the
commands shown and were current at 2026-07-08 authoring time.
