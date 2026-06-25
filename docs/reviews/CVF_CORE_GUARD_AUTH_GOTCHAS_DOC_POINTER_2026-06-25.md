# Core Guard Self-Protection Authorization - Literal-Format Gotchas Doc Pointer

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: governed_authorization

Date: 2026-06-25

## Purpose

Authorize the small, doc-only edit that adds one cross-reference pointer
section to each of `AGENTS.md` and `CLAUDE.md`, pointing both at the new
reference checklist
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
No governance semantics, checker, or enforcement behavior changes.

## Target or Source Under Review

`AGENTS.md` and `CLAUDE.md`, the two protected front-door instruction
files read by every agent at session start.

## Scope or Methodology

Direct read of the diff for both files before commit: each file gains
exactly one new section ("Governed Artifact Literal-Format Gotchas")
appended after its existing last mandatory-rule section, with no edits to
any pre-existing line.

## Position on the Change

The added sections are pure pointers: a one-line cross-reference to
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
plus a short rationale paragraph. No mandatory rule, threshold, checker
binding, or role/route semantics is introduced, removed, or reworded.

## Risk / Corrective Action

Risk is bounded to documentation drift only; no executable or
machine-checked behavior changes. No corrective action required beyond
this authorization record.

## Decision / Recommendation / Disposition

`ACCEPT`. The change is authorized as a doc-only pointer addition under
operator instruction; see the authorization block below for protected
paths and rollback boundary.

## Core Guard Self-Protection Authorization

This commit touches the protected front-door files `AGENTS.md` and
`CLAUDE.md` solely to add a "Governed Artifact Literal-Format Gotchas"
pointer section near the end of each file's existing mandatory-rule list.
No other content in either file is modified.

### Authorized guard-maintenance scope

Add a doc-only pointer section to `AGENTS.md` and `CLAUDE.md` referencing
the new reference checklist file. No guard script, hook chain, checker
logic, or governance semantics are added, removed, or modified.

### Protected paths

- `AGENTS.md`
- `CLAUDE.md`

### Operator authorization

Operator requested this commit directly in-session after approving the
doc-only scope (no GC-018 required) for this reference checklist addition.

### Rollback boundary

Revert is a plain `git revert` of this commit; it removes only the two
added pointer sections and the new reference file. No other governed
artifact, checker, or runtime path is affected by rollback.

## Claim Boundary

This file is an authorization artifact only. It does not implement,
modify, or supersede any checker, and it does not itself describe the
content of the literal-format gotchas reference file beyond naming it.
