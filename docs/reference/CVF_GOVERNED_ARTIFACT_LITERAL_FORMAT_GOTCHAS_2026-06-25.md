# CVF Governed Artifact Literal-Format Gotchas

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference_checklist

Date: 2026-06-25

EPISTEMIC_PROCESS_NA_WITH_REASON: reference checklist of observed literal
format traps; this file records prevention notes and does not compare
evidence or update an empirical claim.

## Purpose

A pre-write checklist of literal-format failure modes that several
`governance/compat/check_*.py` checkers enforce via exact substring,
regex, or self-recomputed-value matching. Each item below was an actual
gate failure encountered while authoring a GC-018, work order, or
worker-return/completion-review artifact, not a hypothetical risk. Read
this **before** drafting a new governed artifact to avoid discovering
these the slow way, one gate-run at a time.

This is a reference checklist, not a governance standard and not an ADIF
entry. It does not change any checker's behavior. If a pattern here
recurs across multiple tranches and is not yet an ADIF entry, promote it
per `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`.

## Scope / Applies To

Applies to any agent (Claude, Codex, Gemini, or a future agent) drafting a
GC-018, work order, worker-return, completion review, roadmap, or any
other artifact that a `governance/compat/check_*.py` gate will parse for
literal headings, tokens, line numbers, or path strings. Does not apply to
runtime/product code, and does not itself implement or modify any checker.

## Checklist

1. **Self-recomputed line numbers.** If a Source Verification table cites
   a `def`/section line number, the checker re-derives that number from
   current HEAD and fails on any mismatch, including off-by-one or
   off-by-two from counting a docstring or decorator line. Re-grep the
   exact line right before writing the row; do not estimate from memory
   or from a stale read.

2. **Word-wrapped multi-word literal terms.** A required term like
   `Scope / Methodology` must appear on **one physical line**. If prose
   wraps it across two lines (`Scope /\nMethodology`), literal substring
   matchers fail to find it. Write required multi-word terms as
   one-per-line bullets, not flowing prose, when a checker is known to
   look for them literally.

3. **Trailing punctuation after a verdict token.** Verdict-extraction
   regexes often anchor on the token at end-of-line/end-of-sentence.
   `...COMPLETE_WITH_DECLARED_LIMITS.` (with a period) can fail to match
   where `...COMPLETE_WITH_DECLARED_LIMITS` (no period) succeeds. Do not
   put a trailing period directly after a verdict/status enum token.

4. **Bare directory-path substrings in prose.** Some path-extraction
   regexes match a bare `docs/work_orders/`, `docs/reviews/`,
   `docs/baselines/`, etc. anywhere in text, even inside ordinary prose
   describing "the work-orders directory" with no specific file named,
   and then treat it as a cited file path to verify, failing when no such
   file exists. Avoid writing the bare directory path string in closed
   artifact prose; say "the reviews directory" instead of
   `` the `docs/reviews/` directory `` if no specific file is meant.

5. **Quoting a real heading inside backticks elsewhere in the same
   doc.** If you write `` `## Findings` `` in a risk/note section as a
   literal example, and the document also has a real `## Findings`
   section elsewhere, a checker using a bare `text.find(heading)` may
   match the **first** occurrence (the backtick-quoted mention) and
   truncate or miss the real section. Avoid quoting a heading string that
   also exists for real elsewhere in the same document.

6. **Proximity-based false-trigger phrases.** Some checkers flag a
   provider/registry/network claim if certain trigger words appear within
   roughly 100-150 characters of each other, regardless of grammatical
   relationship. Phrases like "no network/provider call" or "keeps no
   registry cap at N" can false-trigger a provider-registry guard.
   Rephrase to put unrelated trigger words farther apart, e.g. "no
   external network or provider invocation" / "does not keep the size
   exception frozen at N".

7. **Equivalence-claim phrases near a cited source path.** Words like
   *verbatim*, *identical*, *unchanged*, *same as*, *reused exactly*, *no
   new field*, or *maps to existing* near a cited file/section path will
   trigger `check_equivalence_claim_evidence.py` unless paired with an
   adjacent verification command (`rg`, `git diff --no-index`) or an
   explicit disposition token (`MATCH`, `ADAPTED_WITH_REASON`,
   `NEW_FIELD_INTRODUCED`, `NOT_LITERAL_WITH_REASON`). Add the evidence
   or token in the same sentence/row, not just nearby.

8. **ADIF disclosure query must match exactly what you wrote.** The
   `check_adif_defect_registry_disclosure.py` re-runs the **exact** query
   string written in the `## ADIF Defect Registry Disclosure` section and
   fails if any defectId the resolver actually returns is missing from
   the listed set. Adding an unverified filter (e.g. `riskCeiling=MEDIUM`)
   can silently shrink the result set below what you disclosed, or
   conversely a bare query without it can return more IDs than you
   listed. Run the resolver call yourself before writing the disclosure
   block; list every ID it actually returns for that exact query.

9. **`N/A with reason` vs `BLOCKED with reason`.** Several closure-row
   checkers only accept `PASS` or `BLOCKED <with reason>` as a row
   disposition for binary gate rows (e.g. "Registry Markdown" companion
   updates); `N/A with reason` is not an accepted token even when it
   reads naturally. Use the checker's accepted enum, not the most
   natural-sounding phrase.

10. **Canonical-token fields want an exact token, not free prose.** Fields
    like "Input type" in an external-intake section expect one of a fixed
    set of canonical phrases (e.g. `operator-provided external comparison,
    critique, or recommendation`), not a paraphrase. Check the field's
    governing standard for its literal accepted value set before writing
    free text into it.

11. **Section-specific field labels and required subsections.** Sections
    like "Corpus Completeness and Report Integrity" and "Knowledge System
    Reconciliation" require exact field labels and a fixed subsection set
    per their governing standards
    (`docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`,
    `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`).
    Copying a similar section from an older artifact without re-checking
    against the current standard risks missing a renamed field or a newly
    required subsection.

12. **Mixed committed-range shape across material and session-sync
    commits.** The pre-closure "committed range shape preflight" rejects a
    single range that mixes material change commits with session-sync/
    handoff-sync commits. When verifying closure, run the gate separately
    on each sub-range (e.g. `dispatch..closure-material` and
    `closure-material..session-sync`), not on one combined
    `dispatch..HEAD` span.

13. **Windows-specific subprocess text decoding.** Any new Python
    automation that calls `subprocess.run(..., text=True)` without an
    explicit `encoding="utf-8"` decodes git/tool output using the
    platform default codec (`cp1252` on Windows), which raises
    `UnicodeDecodeError` or silently returns `None` for `stdout` on
    non-ASCII output. Always pass `encoding="utf-8", errors="replace"`
    explicitly, and guard every `.stdout`/`.stderr` access for `None`.

14. **ADIF entries need the full trace label set.** ADIF entry files carry
    their own Agent Operation Trace Block section. The ADIF integrity guard
    now checks the exact labels, including `Diff evidence`; copying a
    nearby entry or older template that omits one label will fail. Copy the
    block from `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md`
    and run `python governance/compat/check_adif_entry_integrity.py --enforce`
    before committing ADIF entries.

15. **Learning-record commits are material, not session-sync.** A commit
    that adds or edits `docs/reference/agent_defect_intelligence/entries/`
    is a material learning-record commit even when it happens during a
    review session. Do not mix it with `AGENT_HANDOFF_*.md`,
    `CVF_SESSION_MEMORY.md`, or `CVF_SESSION/` updates; commit the learning
    record first, then use a dedicated session-sync or handoff-sync commit.

16. **Closed-equivalent tokens can reclassify a dispatch artifact.** A
    `DISPATCH_READY` GC-018 or work order can be treated like a closure
    artifact if its top section uses closure-status tokens such as
    `CLOSED_PASS_BOUNDED` for prerequisite rows or dependency prose. For
    dispatch packets, record prerequisite release as `SATISFIED` or
    `PASS` with the artifact path and commit evidence; reserve
    `CLOSED_PASS_BOUNDED` for the referenced artifact's own closure packet
    or for the actual closure conversion.

17. **Future deliverables are not present proof manifests.** Headings like
    `## Required Artifact Manifest` and `## Required Proof Manifest` can
    trigger artifact-existence checks immediately. In a dispatch packet,
    use `## Planned Artifact Manifest`, `## Planned Worker Fulfillment
    Manifest`, or another clearly planned/future heading for worker
    deliverables that do not exist yet. Use the exact required-manifest
    headings only when the listed paths are present for the current phase
    or the checker explicitly requires that heading for the artifact type.

18. **Closure-only sections change the artifact's parsing lane.** Adding
    closure-oriented sections such as `## Machine Closure Package` to a
    dispatch-only GC-018 baseline can make closure gates look for closure
    invariants before the tranche has executed. Keep dispatch baselines to
    dispatch-readiness evidence, dependency release, source verification,
    acceptance criteria, fail conditions, and claim boundary. Add machine
    closure packaging during the reviewer/closer conversion phase unless
    the governing template for that specific dispatch artifact requires it.

19. **Trace-checked reference files need their own trace block.** Some
    active reference/checklist files under `docs/reference/` are scanned by
    `check_agent_operation_trace.py` when changed. If the file lacks a full
    Agent Operation Trace Block section, pre-implementation can fail even when
    the edit is a small checklist note. Add or update the complete trace
    label set in the same changed file before rerunning the gate.

20. **Source Inventory action cells are bare tokens.** Worker-return
    `## Source Inventory` and Required First Read tables are parsed by exact
    action-cell vocabulary. Use only `READ`, `FULL_READ`, `PARTIAL_READ`, or
    `SOURCE_VERIFIED` in the action cell; do not write `READ - targeted grep`,
    `READ (lines only)`, or other prose there. Put qualifiers in adjacent prose
    or a separate note row.

21. **`## External Knowledge Intake Routing` is a `Field`/`Value` row-label
    table, not a 5-column table.** `check_external_knowledge_intake_routing.py`
    requires exactly the seven row labels `Chain map`, `Input type`,
    `Chain map route`, `Matching local-view guard`, `Owner surface`,
    `Disposition`, `Claim boundary` as the first cell of each row. A table with
    columns like `External item | Route | Local guard | Disposition | Claim
    boundary` looks plausible but fails the guard outright because none of its
    column headers match a required row label. `Input type` must also be one
    of the guard's canonical enum values (for example `operator-provided
    external comparison, critique, or recommendation`), not a free-form `N/A
    with reason` string - see gotcha B20 in agent memory for the same
    enum-not-free-N/A rule.

22. **Describing the rescan guard's own keyword matching can itself trigger
    the rescan guard.** `check_rescan_intelligence_hardening.py` matches the
    bare word `rescan` anywhere in non-excluded prose. Writing about the guard's
    behavior - for example calling out that "rescan" and "hardening" or
    "rescan" and "body" appear near each other in a sentence, while compactly
    marking the section `NOT_APPLICABLE_WITH_REASON` - can re-trigger the same
    applicability pattern the sentence is describing. If a worker return must
    discuss this class of false trigger, prefer the guard's own already-safe
    vocabulary (`rescan guard`, `rescan standard`, `non-rescan`, `real rescan
    output`) instead of inventing new word pairings, and verify with
    `python governance/compat/check_rescan_intelligence_hardening.py --base <executionBaseHead> --head HEAD --enforce`
    before relying on the worker-return fast gate alone to catch it.

23. **The Delta block guard's own required section must be an actual
    `Field`/`Disposition` markdown table, not `key: value` prose lines.**
    `check_delta_execution_claim_boundary.py` parses only `|`-delimited
    table rows (`_field_rows`) for the eight required fields (`claimScope`,
    `claimDisposition`, `receiptEvidence`, `actionEvidence`,
    `invocationBoundary`, `interceptionBoundary`, `claimLanguage`,
    `forbiddenExpansion`). Writing `executionBaseHead: ...` or
    `receiptEvidence: CVF_RECEIPT_PRESENT - ...` as plain prose lines, even
    with the right-looking field names, produces zero parsed rows and fails
    all eight required-field checks at once. Use a real two-column table with
    one row per required field. Caution: this same guard's applicability
    check fires on a short boundary-related word sequence naming its own
    domain anywhere in a document, so describing this gotcha itself can make
    an otherwise-unrelated reference file subject to the guard - prefer
    "Delta block guard" or "Delta block control section" when discussing this
    trap in a document that does not already carry that section, and verify
    with a direct guard command rather than only the bundled fast gate.

24. **A new `docs/reviews/*.md` artifact needs at least one heading from
    every `review`-type structural group before the first fast-gate run, not
    only the three named in gotcha 19/B19.** `check_markdown_structural_
    completeness.py` requires one heading matching each of five groups:
    target/source, scope/methodology, findings/position, risk/corrective
    action, and decision/recommendation/disposition. A draft that supplies
    only the scaffold's default sections plus the three named in the
    work-order template's no-commit guidance can still be missing a
    target/source or decision/disposition heading, which only surfaces as a
    violation once `run_worker_return_fast_gate.py` actually runs.

25. **Long markdown content with backticks and an em dash in a single
    `write_to_file`-style call can fail to parse as a tool argument before
    any CVF guard ever runs.** This is an agent-tooling caution, not a CVF
    checker. Draft long review/work-order bodies without an em-dash
    character (use ` - ` per gotcha B1) and prefer writing or editing the
    file in smaller sections when a single call mixes long prose, multiple
    fenced code blocks, and many backticked inline tokens, so a tool-call
    argument-parse failure does not consume a repair round that looks like a
    governance gate failure but is actually unrelated to any checker.

26. **Closing a roadmap top `Status:` line makes the roadmap itself need
    closure package sections immediately.** If a roadmap top status is changed
    to `CLOSED`, `CLOSED_PASS_BOUNDED`, or another closed-equivalent token,
    add a roadmap-local `## Machine Closure Package` in the same edit before
    the first gate run. A completion review or work-order closure package does
    not satisfy the roadmap-local requirement once the roadmap itself carries
    the closed top status. If the roadmap closure uses receipt/query
    acceptance language or receipt-based PASS claims, also add
    `## Acceptance Receipt Assertion Matrix` immediately with the template
    columns `Query ID`, `Receipt artifact`, `JSON path`, `Required value`,
    `Observed value`, and `Status`. This prevents `check_machine_closure_package.py`
    from discovering the missing sections only after the closer has already
    edited the top status.

27. **A closed or closeable work order still needs `## Execution Plan`.**
    `check_markdown_structural_completeness.py` treats work orders as a
    structural artifact class and requires an execution-plan section even when
    the work order is authored and closed by the same agent in a small evidence
    tranche. Do not rely on `Scope / Methodology`, `Evidence Requirements`, or
    `Acceptance Criteria` as substitutes. Add `## Execution Plan` before the
    first dispatch-quality or structural-completeness gate run, with a compact
    step/action/evidence table if the work is already executed.

28. **Source Verification `Verified path or symbol` cells need a real symbol,
    not the filename being cited.** A row that cites
    `governance/compat/check_work_order_dispatch_quality.py` in the Source file
    column and then repeats `check_work_order_dispatch_quality.py` as the
    verified symbol looks readable to humans, but the dispatch-quality checker
    searches for that symbol inside the file and fails because filenames are
    not source symbols. Use an actual function, constant, section marker, or
    field present in the cited source, such as `main` or `GATE_COMMANDS`.

29. **Mentioning a real `EXTENSIONS/...` path in review or audit prose can
    trigger GC-051 corpus registry expectations.** If a changed review or audit
    cites an extension path as closure evidence, `check_corpus_scan_registry.py`
    can require a matching source entry under the corpus scan registry source
    layout. Do not silently avoid a required path when it is real evidence;
    either keep nonessential extension examples out of governed prose, or add a
    narrow registry source entry and regenerate the aggregate in the same
    material batch. Treat this as a corpus-source accountability issue, not as
    a reason to hide material evidence from the review.

30. **Optional completion reviews become full closure artifacts once created.**
    If a work order says `completionReviewPath` is optional, do not create a
    `Status: CLOSED_PASS_BOUNDED` completion review merely to make the
    closeout feel formal. The new file can trigger Machine Closure Package
    exact-column requirements, Delta claim-boundary requirements, work-order
    closed-status residue checks, and Agent Operation Trace manifest checks.
    Prefer repairing small evidence defects inside the worker return, run
    `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBase> --head HEAD --enforce`,
    commit material paths, then do a separate session-sync. Create the
    completion review only when the work order requires it or when the worker
    return cannot safely carry the reviewer decision.

## When This Checklist Is Not Enough

This file only captures gotchas already observed. It is not a substitute
for running the relevant `governance/compat/run_agent_autorun_workflow_gate.py
--phase <phase>` gate before claiming an artifact is closeable, and it is
not a substitute for the Mandatory Work Order Source Verification or ADIF
Defect Registry Disclosure rules in `CLAUDE.md`. If a new literal-format
trap is discovered while authoring a future artifact, add it here in the
same batch, and if it recurs across more than one tranche, promote it to
an ADIF entry per
`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`.

## Claim Boundary

This file records observed literal-format gate-failure patterns only. It
does not implement, modify, or supersede any `governance/compat/check_*.py`
checker, does not define new governance semantics, and is not itself a
verification or closure artifact for any tranche.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | optional completion review gotcha update, 2026-06-29 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, rg, apply_patch, governance gates |
| Target paths | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0018.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Allowed scope source | operator instruction to make reviewer/closure speed rules durable before future agent work |
| Before status evidence | AGSK-T4 closeout briefly created an optional completion review that triggered avoidable closure-shape gates |
| After status evidence | checklist records optional completion review overbuild as item 30 |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | governed artifact authoring friction checklist and ADIF/guard routing only |
| Claim boundary | checklist guidance only; no runtime/provider/live behavior, public-sync, package instance, certification, generated-index mutation, resolver mutation, or adapter behavior |
| Agent type | reviewer/closer |
| Invocation ID | `optional-completion-review-gotcha-update-2026-06-29` |
| Expected manifest | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0018.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Actual changed set | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0018.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this hardening batch |
