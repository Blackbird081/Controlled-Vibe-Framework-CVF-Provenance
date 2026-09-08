# CVF Text Encoding And Symbol Discipline Standard

Memory class: FULL_RECORD

Status: canonical text encoding and symbol discipline standard

Date: 2026-06-07

Owner: CVF Governance / Agent Execution Surface

## Purpose

This standard prevents agent-created artifacts from drifting into inconsistent
Unicode punctuation, invisible characters, or mixed symbol conventions that make
diffs, review, search, and machine checks harder for future agents.

## Scope

Applies to agent-created or agent-edited source files, tests, governed
markdown, work orders, completion packets, handoffs, registries, public-sync
summaries, and review artifacts.

## Owner / Source

Source authority: operator request on 2026-06-07 after G-GM-08/G-GM-06 closure
review identified a Unicode arrow in a test comment as a low-severity
consistency issue.

Owning interface: all CVF agent work orders and reviewer closure packets.

## Rule

Default to ASCII for agent-authored text unless a listed exception applies.

Allowed ASCII-preferred replacements:

| Avoid by default | Use instead |
|---|---|
| Curly quotes | Straight quotes |
| Em dash or en dash | Hyphen or colon |
| Unicode arrows | `->`, `<-`, `=>`, or prose |
| Ellipsis character | Three periods |
| Non-breaking spaces | Regular spaces |
| Decorative bullets or symbols | Plain markdown bullets or text |

## Exceptions

Unicode is allowed when:

| Exception | Requirement |
|---|---|
| Existing file convention | The file already consistently uses the same non-ASCII character set |
| User-facing copy requires it | The target language, product copy, or legal/source quote needs the characters |
| Protocol or data contract requires it | The literal value is part of an external schema, test fixture, provider response, or source citation |
| Filename/path already contains Unicode | Preserve the existing path; do not rename unless explicitly authorized |
| Evidence quote contains Unicode | Quote minimally and preserve only what is needed for evidence fidelity |

## Agent Requirements

- New work orders must state whether ASCII-only output is required or whether a
  bounded Unicode exception applies.
- Completion packets must mention any non-ASCII exception when agent-authored
  Unicode remains in changed files.
- Comments in source and tests should use ASCII unless they quote existing
  source or external evidence.
- Do not introduce invisible control characters, zero-width spaces,
  non-breaking spaces, or smart punctuation in governed artifacts.
- Do not perform broad Unicode normalization across unrelated files as cleanup;
  keep edits inside the assigned scope.

## Rename Provenance Rule

The machine checker binding this standard,
`governance/compat/check_agent_packet_authority_and_encoding.py`, derives
newly added non-ASCII lines from rename-aware Git provenance rather than
from a destination-only reading of a changed path.

- A renamed governed file carries its Git-reported source path alongside its
  destination; the checker compares the destination against the correct
  source blob, or uses an unrestricted rename-aware diff that preserves that
  pairing. A pathspec limited to the destination path alone is never the sole
  provenance source, because that restriction can prevent Git from pairing
  the two blobs at all, or can make Git recompute a lower content similarity
  than the original whole-tree rename detection and misreport the whole
  destination as newly added.
- A pure rename that carries historical non-ASCII text already present at the
  source produces zero newly-added non-ASCII violations under this rule. A
  rename that also introduces new non-ASCII text is reported for only the
  newly introduced lines.
- Provenance is lifecycle-specific. A committed-range rename compares the
  base source blob with the head destination blob; an index rename compares
  the current committed source blob with the staged destination blob. Later
  staged, worktree, or untracked changes to the same destination remain
  separate evidence layers and must not be hidden by the rename result.
- NUL-delimited name-status paths are data, not prose: the checker must not
  trim leading or trailing path whitespace. Malformed records and Git
  provenance failures produce deterministic non-compliance instead of an
  empty-change success.
- Git decides whether a content move qualifies as a rename. When similarity
  falls below Git's own detection threshold and Git reports a delete plus an
  add instead of a rename, the checker does not reconstruct a source
  relationship Git did not establish; the destination is treated as an
  ordinary added file under the existing exception rules above.
- This rule governs newly-added-line provenance only. It does not authorize
  broad Unicode normalization of historical or unrelated files, and the
  prohibition on broad normalization as cleanup stated above remains in
  force without exception for rename handling.

## Review Gate

Reviewers should treat unexpected non-ASCII in changed agent-authored text as a
style defect unless the artifact records an exception from this standard.

This is not a semantic correctness claim. Passing this standard means only that
text encoding and symbol usage are disciplined for review and machine handling.

## Claim Boundary

This standard does not require rewriting historical artifacts, external quotes,
localized user-facing copy, existing filenames, or provider/source evidence. It
also does not prove document quality, code quality, or runtime behavior.

## Related Artifacts

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- `governance/compat/check_markdown_structural_completeness.py`

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

This is a private provenance governance standard. Public export would require a
public-facing style/governance summary in the public-sync repository.
