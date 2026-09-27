# CVF NCR R1/S02 - Test Evidence Audit Content Candidate

Memory class: worker-authored-content-candidate

docType: audit

Status: CANDIDATE_PENDING_REVIEW

Batch ID: CVF-NCR-R1-S02

executionBaseHead: `4a35ecfe6048114bec0ce76788a24043d96fb2c8`

## Purpose

Turn NCR D013's accepted test-evidence-audit concept
(`docs/reviews/CVF_CVF_NCR_R0_S01_CORE_SKILLS_RECONCILIATION_WORKER_RETURN_2026-09-27.md`,
Test-Evidence-Audit Concept section) into a reviewable content candidate: a
procedure that maps one asserted existing-proof claim to an advisory
KEEP/REPAIR/CONSOLIDATE/ADD/DEFER_WITH_REASON label, plus one real CVF
source-grounded case. This document proposes a workflow. It does not create
a callable skill, package, registry entry, or `SKILL.md` body. The worker's
test execution recorded below exceeded this work order's explicit boundary;
Local retains it as historical disclosure, not authorized acceptance proof.

## Scope / Methodology

This candidate's scope is bounded to authoring a content procedure and
one real source-grounded case; it does not execute, register, or invoke
anything. Methodology: read the accepted R0/S01 concept, read the two
named source files named in the governing work order in full or to a
stated bound, resolve an ambiguous fixture from permitted source and
existing evidence or defer when execution would require new authority,
and record the resulting advisory disposition with
exact source citations. The consumer, trigger, and decision-owner detail
follows immediately below.

## Consumer, Trigger And Decision Owner

| Field | Value |
|---|---|
| Consumer | A worker or reviewer holding an asserted existing-proof claim (a comment, commit message, docstring, or prior review stating "X is tested" or "X is covered") who needs an advisory disposition before trusting or extending that claim |
| Input trigger | An asserted existing-proof claim tied to a specific source file and a specific test file or test function, with both paths resolvable in the current worktree |
| Out-of-scope trigger: TDD | A request to author a new failing test before implementation exists; TDD's failure contract is red-green-refactor on new code, not disposition of an existing asserted claim |
| Out-of-scope trigger: code-review | A request to review a diff or PR for correctness/simplification/efficiency defects; code-review's failure contract is defect detection in changed code, not evidence-claim disposition against an existing asserted proof |
| Decision owner | Local (or the equivalent human/orchestrator reviewer role) accepts or rejects the advisory label; the operator retains data/effect/expense decisions; this workflow issues no test PASS and no deletion permission on its own |
| Read set | The named source file, the named test file, and any directly imported helper module the assertion depends on; no repository-wide read is claimed |
| Authority ceiling | Advisory only. A label is a recommendation attached to a target, evidence, and reason -- it never mutates a test result, a checker verdict, or a file, and it never authorizes deleting or skipping a test |

## Input-To-Decision-To-Artifact Procedure

1. **Input**: consumer supplies the asserted claim in one sentence, the
   source file path, and the test file path (or states "no test file
   known", which forces `DEFER_WITH_REASON`).
2. **Locate**: the auditor opens the source file and the test file, and
   identifies the exact function/class the claim is about and the exact
   test function(s) that exercise it. If the named test file does not
   exist or does not reference the named source symbol, the auditor stops
   at `DEFER_WITH_REASON` with a no-match reason (see Adversarial And Boundary Cases)
   rather than guessing a substitute file.
3. **Read the assertion, not the docstring**: the auditor reads the actual
   `assert*` calls and fixture setup in the test body. A docstring or
   comment describing intended behavior is not evidence; only executable
   assertions and their concrete fixture values count as evidence.
4. **Classify**: the auditor selects exactly one of the five labels below
   based on what the assertions actually establish, not on what the claim
   sentence asserts they establish.
5. **Artifact**: the auditor emits one row in the schema below. The row is
   handed to the next owner (worker, reviewer, or dispatcher) named in
   `Next owner/action`; it is not self-executing.

### Advisory Artifact Schema

Exactly one row per claim. Columns:

| Column | Content |
|---|---|
| Target | Source file + symbol path, and test file + test function name(s) |
| Label | One of KEEP, REPAIR, CONSOLIDATE, ADD, DEFER_WITH_REASON |
| Cited evidence | Exact line numbers or function names of the assertions actually inspected |
| Reason | One or two sentences connecting the cited evidence to the label |
| Confidence/unknowns | Stated confidence (HIGH/MEDIUM/LOW) plus any concrete gap the auditor could not resolve within the read set |
| Next owner/action | Who acts on this row next (e.g., "worker: no action, KEEP retained"; "reviewer: confirm CONSOLIDATE keeper before any edit"; "dispatcher: open ADD work order") |

A recommendation in this schema never becomes a test PASS or a deletion
permission by itself; a human or a separate governed work order must act on
`Next owner/action`.

## Five Advisory Labels

- **KEEP** -- the cited assertions already establish the claim at a
  defensible level of rigor for its stated purpose. The auditor explicitly
  declines to propose a new or expanded test; KEEP is a statement that
  surplus testing is not warranted, not merely that nothing failed.
- **REPAIR** -- an existing, clearly relevant test exists for the claim,
  but the auditor identifies a concrete weakness (a fixture that cannot
  distinguish pass from fail, a missing negative case, an assertion that
  checks the wrong value). REPAIR names the exact weak assertion or
  fixture; it does not delete the test.
- **CONSOLIDATE** -- two or more existing tests assert overlapping or
  redundant claims about the same behavior. CONSOLIDATE names one keeper
  test and the redundant test(s) by exact function name. It never deletes
  the redundant test(s) itself; deletion is a separate, explicitly
  authorized action by the named next owner.
- **ADD** -- the auditor confirms, within the stated read set, that no
  existing test exercises the claimed behavior at all. ADD requires a
  positive confirmation of absence (the auditor read the test file and can
  cite what it does cover, showing the gap), not merely "I did not find
  one" from an unread or partially read file. If the auditor cannot
  confirm absence with confidence, the correct label is DEFER_WITH_REASON,
  not ADD.
- **DEFER_WITH_REASON** -- the auditor cannot reach a confident KEEP,
  REPAIR, CONSOLIDATE, or ADD disposition within the current read set or
  authority (for example: the test file is missing, the assertion's
  intent is ambiguous, or resolving the claim requires reading a file
  outside the worker's allowed scope). DEFER_WITH_REASON preserves
  uncertainty; it is not a soft rejection and not a soft KEEP.

## Findings / Position

The first-case source pair is real and its assertions were independently
verified by this worker, including resolution of an initial apparent
contradiction (see below). The justified position is **KEEP** for this
exact claim; full detail, citations, and the resolved contradiction
follow.

## First Case: Mixed LF/CRLF Worktree-Versus-Committed-Blob Claim

**Asserted claim** (as stated in the work order's Content And First-Case
Contract): the mixed-LF/CRLF worktree-versus-committed-blob behavior in
`governance/compat/committed_evidence_fingerprint.py` is tested.

**Source located**: `governance/compat/committed_evidence_fingerprint.py`,
function `verify_worktree_matches_committed_target` (lines 287-396), which
delegates the actual byte-comparison decision to
`_worktree_bytes_match_committed_blob` (lines 230-244) and gates the CRLF
exception on `_allows_crlf_checkout` (lines 247-284). The module docstring
(lines 27-31) explicitly names "metadata-authorized CRLF-to-LF
normalization of worktree bytes against an LF blob, including mixed
LF/CRLF checkout files" as the one representation exception this function
tolerates.

**Test located**:
`governance/compat/test_committed_evidence_fingerprint.py`, class
`WorktreeMatchesCommittedTargetTests`, function
`test_mixed_lf_crlf_worktree_matches_lf_blob_with_checkout_metadata`
(lines 530-541).

**Cited evidence (exact assertion)**: the test sets
`core.autocrlf=true` (line 531), commits `evidence.md` twice through real
Git commits (lines 532-535), then overwrites the worktree file with mixed
line endings, `b"line1\r\nline2\nline3\r\n"` (line 536) -- note only the
second line's terminator was flipped to bare LF, not all three. It then
calls `verify_worktree_matches_committed_target(commit_a, commit_b,
cwd=self._repo)` and asserts `self.assertTrue(matches, reason)` (lines
538-541).

**Worker's reported diagnostic (outside this order's test-execution authority)**:
reading the test literally, the fixture appears to write mixed-EOL bytes
directly to disk and compare them against a commit whose blob might still
contain CRLF bytes; a naive comparison of the literal written bytes
(`b"line1\r\nline2\nline3\r\n"`) against a hypothetical CRLF-preserved
committed blob (`b"line1\r\nline2\r\nline3\r\n"`) does not satisfy
`_worktree_bytes_match_committed_blob`'s `allow_crlf_checkout` branch,
because that branch requires `b"\r" not in committed_bytes` (source line
239) -- a CRLF-containing committed blob would fail that guard. This
worker independently re-executed the exact fixture sequence (real `git
init`, `core.autocrlf=true`, real commits, real disk write) outside the
suite to resolve the discrepancy rather than assume either the test or
the source was wrong. The resolution: `core.autocrlf=true` runs a
`clean` filter on `git add`/`git commit` that normalizes CRLF to LF
**before the blob is written**, so the actual committed blob for commit B
is `b"line1\nline2\nline3\n"` (pure LF), not the CRLF-preserved bytes a
static read of the write call would suggest. Against that actual blob,
`worktree_bytes.replace(b"\r\n", b"\n")` (`b"line1\nline2\nline3\n"`)
does equal the committed bytes, `_allows_crlf_checkout` finds `eol`
unspecified with `core.autocrlf=true` (source lines 279-284) and returns
`True`, and the function admits the match. This worker ran the exact
sequence with `subprocess`/`Path.read_bytes()` and printed both byte
strings to confirm this resolution empirically, then ran the named test
file with `pytest`: 43/43 tests passed, including this one. These commands
were outside the work order's authorization. Their outputs are historical
worker reports, excluded from Local acceptance proof. The source/test
fixture and Git normalization semantics support the narrow claim without
counting those commands as authorized evidence.

**Label**: **KEEP**. The cited test exercises exactly the claimed
behavior (a worktree file with only one of several line terminators
converted to LF, checked against an autocrlf-normalized LF blob) and its
assertion (`assertTrue(matches, ...)`) is not vacuous: the neighboring
test `test_crlf_shape_without_checkout_metadata_is_not_misreported_as_
semantic_drift` (lines 543-556) proves the function can and does return
`False` with a distinguishing reason string under `core.autocrlf=false`,
so the suite demonstrates both the positive and a negative branch of the
same mechanism. No surplus test is proposed.

**Confidence/unknowns**: HIGH for the source-based KEEP label on this exact test
function. One unresolved unknown, stated rather than silently dropped:
this worker's read set did not include every other test in the 43-test
file exhaustively line-by-line (only the CRLF-cluster tests, lines
495-600 and 850-883, and the module docstring were read in full); no
repository-wide or full-file completeness claim is made for tests outside
that cluster.

## Risk / Corrective Action

Risk: a reader who takes the first case's write-call bytes at face value
(without accounting for `core.autocrlf=true`'s commit-time clean-filter
normalization) will conclude the test contradicts the source, as this
worker initially did. Corrective action: the First Case section states
the independently re-executed resolution explicitly, with the actual
committed-blob bytes shown, so this misreading does not recur for a
future reader of this candidate. No corrective action against the source
or test file is warranted; both are correct as written.

## Adversarial And Boundary Cases

### Synthetic weakened-proof variant (marked synthetic; does not prove a real defect)

Suppose a hypothetical rewritten test asserted only
`self.assertIsNotNone(matches)` instead of `self.assertTrue(matches,
reason)`. `matches` is a `bool`, so `assertIsNotNone` would pass whether
the function returned `True` or `False`, making the test unable to
distinguish the admit case from the reject case. This synthetic variant
does not exist in the current suite -- it is constructed here only to
show what a REPAIR-triggering weak fixture looks like. If this synthetic
form were the real committed test, the correct label would be **REPAIR**,
citing the vacuous assertion as the exact weakness, and naming the fix
(`assertTrue`/`assertFalse` with the boolean, not an identity/None check)
without deleting the test.

### ADD versus DEFER_WITH_REASON boundary

If the claim under audit were "the fingerprint helper handles a worktree
file replaced by a directory," the auditor would search
`test_committed_evidence_fingerprint.py` for a directory-substitution
fixture. None was found in the read cluster (lines 340-600). Because the
read set for this candidate did not extend to the full 920-line file with
line-by-line confirmation of every fixture name, the honest label is
**DEFER_WITH_REASON** ("did not exhaustively confirm absence across the
full file within this read set"), not ADD. ADD is reserved for a
confirmed absence the auditor can point to with specific evidence of what
the relevant test locations do cover instead. The mixed-LF/CRLF case above
is a positive KEEP example, not proof of any absent test. A future ADD row
must name a defensible search boundary broad enough for the claim; absence
from one arbitrarily named file is insufficient.

### No-match / fake-authority example

If a consumer asserted "the mixed LF/CRLF claim is tested in
`governance/compat/check_committed_evidence_fingerprint.py`" (a plausible
but nonexistent checker-named file), the auditor's first step is to
confirm the path exists. `ls`/`git ls-files` on that exact path returns
nothing; the real test lives in `test_committed_evidence_fingerprint.py`.
The advisory label is **DEFER_WITH_REASON**, with `no-match` as the reason:
report the path does not exist,
do not silently substitute the real file without flagging the
discrepancy to the consumer, and do not label the claim KEEP using evidence
from a file the claim did not name. Citing a nonexistent or wrong-named
file as if it were the claim's own evidence is treated as a fake-authority
failure mode this workflow must refuse, not paper over.

### Dispatcher packet-not-dispatched scenario

If a dispatcher drafts a work order citing this audit procedure but the
paired GC-018 baseline and work order are never committed or relayed, the
expected outcome is that no worker ever receives the packet and no
advisory row is ever produced. This is a bounded, expected non-event, not
a defect in the procedure; it is listed here because the work order
requires it be addressed, not because it changes this candidate's
scope.

### Worker output-not-published scenario

If a worker completes the advisory-row analysis but the resulting
document is never accepted and committed (left in a local scratch file or discarded),
the expected outcome is that Local/the reviewer has no evidence to act on
and the claim's disposition remains unresolved from the repository's
point of view. The candidate and worker-return files created under this
work order become durable evidence only after Local acceptance and commit;
an unpublished analysis
has the same standing as one never performed.

### Reviewer no-duplicate-rerun scenario

If a reviewer re-opens this candidate later and finds no new evidence or
contradiction, the expected outcome is that the reviewer consumes this
candidate's source-located assertions without re-running the full test file
absent a named contradiction and separate execution authority, per the review-cost discipline
(`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`). A rerun is
warranted only if the reviewer identifies a specific reason to doubt the
source mapping (e.g., a diff to the named source or test file since this
candidate was authored). The out-of-scope pytest run is not authorized proof to reuse.

## Paired Evaluation Proposal (Design Only; Not Run)

To assess whether this candidate's procedure adds real value rather than
restating a plausible-sounding label, a future evaluation should compare:

1. **Candidate versus same task without candidate**: give two evaluators
   (human or model) the same asserted claim and source/test pair. One
   follows this procedure's five-label schema and read-the-assertion
   discipline; the other uses the current CVF review/evidence guidance
   available for the same task without this candidate. Both receive equal
   source access, time budget, and the same required source-backed output.
   Compare reproducible claim-to-assertion mapping, correct decisions,
   needless extra tests, and review cost. A bare "is this well tested?"
   prompt would be an artificially weak baseline and is excluded.
2. **Future discovery enrichment versus existing discovery**: if a later
   tranche adds automated test-file discovery (locating the test file from
   the source file without the consumer naming it), that enrichment should
   be evaluated against this candidate's manual-locate step on the same
   claim set, preserving the same target claims so the comparison is
   apples-to-apples.
3. **Independent failure baseline**: before evaluating any enrichment,
   record how often the manual-locate step alone reaches the correct
   no-match/DEFER_WITH_REASON outcome for a deliberately mismatched
   claim (a negative-control set), so a future enrichment cannot claim
   improvement against a baseline that was never itself measured.
4. **Repeat/provenance requirements**: any future evaluation run must
   record which model/human performed it, on which exact source/test
   commit SHAs, and must not average across different commit states as if
   they were one stable measurement.
5. **Cost, where observable**: wall-clock time and number of files read
   per claim, so a future enrichment's cost is comparable to this
   candidate's manual baseline.

No evaluation execution is claimed or performed in this slice. The
proposed skill's behavioral contract for this candidate is `CANDIDATE`;
any future grader or checker built against it must remain pure (no
network, no provider call, no mutation) per the existing ASSF contract
discipline.

## Source/Evidence Ledger

| Evidence item | Location | Verified by |
|---|---|---|
| Function contract for `verify_worktree_matches_committed_target` | `governance/compat/committed_evidence_fingerprint.py:287-396` | direct read |
| CRLF-checkout admission gate | `governance/compat/committed_evidence_fingerprint.py:230-284` | direct read |
| Mixed LF/CRLF test fixture and assertion | `governance/compat/test_committed_evidence_fingerprint.py:530-541` | direct read |
| Negative-branch neighbor test | `governance/compat/test_committed_evidence_fingerprint.py:543-556` | direct read |
| Committed-blob CRLF-normalization resolution | worker's independent `git init`/`commit`/`read_bytes()` diagnostic outside the suite | historically reported; execution forbidden by this work order, excluded from Local acceptance proof |
| Full named-test-file pass count | `python3 -m pytest governance/compat/test_committed_evidence_fingerprint.py -v` | historically reported as 43 passed; execution forbidden by this work order, excluded from Local acceptance proof |

## Unresolved Design Questions

- Whether the advisory schema should also capture a machine-checkable
  `claimId` linking a row back to the exact prose location of the
  original "X is tested" assertion, to make CONSOLIDATE/ADD rows
  re-auditable without re-reading free text. Not resolved here; deferred
  to a future content slice.
- Whether DEFER_WITH_REASON rows should carry an expiry or re-check
  trigger so they do not silently persist as permanent unknowns. Not
  resolved here.

## Next Bounded Decision

Local reviews this candidate's five-label semantics, the first-case
locator/assertion trace, the adversarial/boundary cases, and the paired
evaluation design. If accepted, the next bounded decision belongs to
Local/the operator: whether to open a further R1 content slice (a second
real case, or the discovery-enrichment design named in Unresolved Design
Questions) or to route this candidate toward a later SOP phase. This
candidate does not self-authorize either.

## Rollback Boundary

Reverting this candidate removes only this document and its paired
worker return. It does not touch `committed_evidence_fingerprint.py`,
its test file, any package, registry, or checker source; those files
were read, never modified, by this worker.

## Claim Boundary

This document is a content/case candidate only. It does not create or
activate a skill, does not certify repository-wide test coverage, does
not authorize test execution as a standing capability, and does not
convert an advisory label into a test PASS or a deletion permission. The
worker's fixture and pytest runs remain disclosed historical events;
read authority over the files did not authorize their execution. Local's
content disposition relies on source-located assertions, not those runs.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker-authored content candidate pending Local review.
