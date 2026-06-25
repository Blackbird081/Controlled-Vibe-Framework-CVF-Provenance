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
    their own `## Agent Operation Trace Block`. The ADIF integrity guard
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
