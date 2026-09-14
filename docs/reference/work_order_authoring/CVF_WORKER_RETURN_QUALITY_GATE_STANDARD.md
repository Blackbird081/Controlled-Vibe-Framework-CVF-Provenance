# CVF Worker Return Quality Gate Standard

Memory class: governed-reference-standard
Status: ACTIVE_REFERENCE
Date: 2026-07-01

EPISTEMIC_PROCESS_NA_WITH_REASON: this reference standard defines a structural
quality gate and does not compare implementation evidence.

## Purpose

Define the minimum review-ready machine shape for changed no-commit worker
return packets. The gate catches unresolved scaffold placeholders, missing
trace/read-ahead fields, weak Delta evidence tokens, non-canonical external
input wording, and empty command evidence before reviewer acceptance.

## Applies To

Applies to changed Markdown files under `docs/reviews/` that self-declare as a
worker-return artifact or combine `Status: COMPLETE_PENDING_REVIEW` or
`Status: BLOCKED_WITH_REASON` with a work-order pointer.

Completion reviews, rebuttal/classification packets, baselines, work orders,
roadmaps, archived reviews, and reference standards are out of scope.

## Required Worker-Return Shape

Eligible worker-return packets must include:

- `Self-declared worker-return artifact: yes`
- `Responds to work order:`
- `dispatchWorkOrder:`
- `executionBaseHead:`
- Checker Source Read-Ahead Block section
- Agent Operation Trace Block section
- Delta Execution Claim Boundary Control Block section
- Public Export Disposition section
- External Knowledge Intake Routing section
- Rescan Intelligence Hardening section
- Corpus Completeness And Report Integrity section
- Finding-To-Governance Learning Disposition section
- Epistemic Process Block section
- git status section
- Changed Files section
- Command Evidence section
- No-Commit Statement section

The packet must not retain scaffold placeholders such as `FILL_ME` or
`WORKER_MUST_CAPTURE_AT_START`.

### Dispatch-Authorized Fast Doc Variant

`WORKER_RETURN_FAST_DOC_V1` retains every required heading above except the
three conditional headings for external intake, rescan intelligence, and
corpus completeness. It replaces them with:

- `## Conditional Controls Disposition`
- `conditionalControlsDisposition: EKI_NA; RIH_NA; CCRI_NA`

The variant is valid only when the `dispatchWorkOrder` file contains all
eligibility terms defined by the full-gate contract standard, including
`DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT`, no-commit mode, and explicit
forbidden dispositions for public-sync, live/runtime, checker mutation, and
worker self-selection. The worker cannot opt in from its return packet.

Purpose, scope, findings, risk, checker read-ahead, operation trace, Delta
boundary, public export, governance learning, epistemic process, claim
boundary, git status, changed files, command evidence, and no-commit evidence
remain required and blocking.

## Checker-Source Authoring Checklist

Before writing the first line of a no-commit worker return, read
`governance/compat/check_worker_return_quality_gate.py` and use the checker as
the literal source for packet shape. This standard intentionally mirrors the
checker constants below so workers do not learn these requirements by repeated
gate failure.

### Required Headings

The checker `REQUIRED_HEADINGS` tuple currently requires each heading below as
an exact physical-line heading:

- `## Purpose`
- `## Scope / Methodology`
- `## Findings / Position`
- `## Risk / Corrective Action`
- `## Checker Source Read-Ahead Block`
- `## Agent Operation Trace Block`
- `## Delta Execution Claim Boundary Control Block`
- `## Public Export Disposition`
- `## External Knowledge Intake Routing`
- `## Rescan Intelligence Hardening`
- `## Corpus Completeness And Report Integrity`
- `## Finding-To-Governance Learning Disposition`
- `## Epistemic Process Block`
- `## Claim Boundary`
- `## git status --short`
- `## Changed Files`
- `## Command Evidence`
- `## No-Commit Statement`

For `WORKER_RETURN_FAST_DOC_V1`, `FAST_DOC_REQUIRED_HEADINGS` removes only the
three conditional headings named above and adds `## Conditional Controls
Disposition`.

### Raw Placeholder Scan

The checker `PLACEHOLDER_MARKERS` scan is full-document raw text. The literal
tokens below must not appear anywhere in a worker return, including prose,
quoted examples, code spans, `literalTokensReviewed`, risk notes, or repair
history:

- `FILL_ME`
- `WORKER_MUST_CAPTURE_AT_START`

If a worker needs to discuss the class of defect, say "unresolved scaffold
placeholder token" instead of spelling the token inside the worker-return
packet.

### Required Field Labels

The `## Checker Source Read-Ahead Block` must include:

- `applicableCheckersRead`
- `literalTokensReviewed`
- `gateRunPurpose`
- `claimBoundary`

The `## Agent Operation Trace Block` must include:

- `Actor`
- `Provider or surface`
- `Session or invocation`
- `Working directory`
- `Command or tool surface`
- `Target paths`
- `Allowed scope source`
- `Before status evidence`
- `After status evidence`
- `Diff evidence`
- `Approval boundary`
- `Claim boundary`
- `Agent type`
- `Invocation ID`
- `Expected manifest`
- `Actual changed set`
- `Manifest delta`
- `Deletion or rename disposition`

The `## Delta Execution Claim Boundary Control Block` must include:

- `claimScope`
- `claimDisposition`
- `receiptEvidence`
- `actionEvidence`
- `invocationBoundary`
- `interceptionBoundary`
- `claimLanguage`
- `forbiddenExpansion`

### Canonical Tokens

For `## External Knowledge Intake Routing`, the `Input type` row must use this
canonical value exactly when the packet is shaped for operator-provided
external comparison, critique, or recommendation:

`operator-provided external comparison, critique, or recommendation`

For Delta evidence, use one receipt token and one action token accepted by the
checker:

- `CLAIM_REJECTED_NO_RECEIPT`
- `CVF_RECEIPT_PRESENT`
- `CLAIM_REJECTED_NO_ACTION`
- `ACTION_EVIDENCE_PRESENT`

For public export disposition, use exactly one allowed disposition token:

- `DEFERRED_PRIVATE_ONLY`
- `EXPORTED`
- `BLOCKED_MISSING_PUBLIC_ARTIFACTS`

The no-commit statement must include:

`WORKER_MUST_NOT_COMMIT honored`

### Command Evidence Range Discipline

Command evidence must use real base/head anchors captured for the tranche. Do
not record a placeholder range where both base and head are `HEAD`; use the
captured `executionBaseHead` and current `HEAD`, for example:

`python governance/compat/run_worker_return_fast_gate.py --pytest-target <test path>`

`python governance/compat/check_worker_return_quality_gate.py --base <executionBaseHead> --head HEAD --enforce`

The purpose of the gate run is confirmation/evidence after reading checker
source, not first discovery of required literal tokens.

### Last-Mile Finalization Discipline

Do not return a packet while any scaffold placeholder remains -
`TODO_PASS_FAIL_BLOCKED`, `TODO_YES_NO`, `TODO_NONE_OR_SECTION`,
`TODO_NUMBER`, `TODO: fill before review`, `TODO_MATCH_OR_EXPLAIN`, or any
other bracketed TODO token. Before returning for review:

- Run the worker-return fast gate at least twice: once mid-draft to catch
  gate-shape defects early, and once as the final run whose actual result
  (not a placeholder) is recorded in `## Gate Evidence` and
  `## Command Evidence`.
- Replace every `Status:`, changed-set, and diff-evidence placeholder with
  the real value captured after edits are complete, not the value captured
  when the scaffold was first generated.
- Confirm the final `git status --short` and `git diff --name-status`
  output pasted into the packet reflects the actual final worktree state,
  not an earlier snapshot.

### Corpus Reconciliation Literal Shapes

When a changed `docs/reviews/` worker return also carries a
`## Corpus Completeness And Report Integrity` claim (not the compact
`NOT_APPLICABLE_WITH_REASON` disposition), `check_corpus_completeness_report_integrity.py`
enforces exact literal shapes that are easy to get wrong on the first pass:

- The `Reconciliation:` line must contain all four bare markers
  `manifest=`, `ledger_terminal=`, `exclusions=`, and `unresolved=` on the
  same line, for example `Reconciliation: manifest=16, ledger_terminal=16,
  exclusions=0, unresolved=0.`
- `Declared exclusions:` and `Unreadable or unsupported files:` must be a
  bare none-like value when there are none - `none`, `n/a`, or `0` (with or
  without a trailing period) - not a sentence such as `none; the reason is
  ...`. The checker's `_is_none_like` comparison only accepts the bare
  token, so any explanatory clause after `none`/`0` fails the check even
  though it reads naturally.
- `COMPLETE_VERIFIED` requires both `Declared exclusions:` and
  `Unreadable or unsupported files:` to be none-like; use
  `COMPLETE_WITH_DECLARED_EXCLUSIONS` instead when a real exclusion exists.

### Evidence Readiness Binding (EVIDENCE-READINESS-T1)

The checker extends its existing `diagnose`/`run` path with one reusable,
importable validator, `governance/compat/worker_evidence_readiness.py`. It is
reached by the *same* checker invocation already used by the standalone CLI,
`run_worker_return_fast_gate.py`, `local_governance_hook_catalog_reviewer_fast.py`,
and `local_governance_hook_catalog_pre_commit.py` -- there is no second
checker invocation and no new top-level gate process.

**Rework note (2026-09-14, generation 1).** A Local reviewer probe found the
initial pass's `evaluate_worker_return()` never actually resolved a row's
claimed source identity, never reached its own structural-safety helpers,
and could not parse a reuse binding at all through the real entrypoint.

**Rework note (2026-09-14, generation 2).** A second independent probe found
four further gaps in generation 1: (a) a row's declared `lineCount` was
never checked against the source's real line count -- only `blobSha256` was
verified, which proves the bytes match but says nothing about a fabricated
line count; (b) `sourcePin` containing the substring `N/A` exempted ALL
source verification for a binding even when it had rows with real
`blobSha256`/`READ` claims, a blanket bypass; (c) `REUSED` rows were
entirely excluded from source-identity resolution, so a REUSED row's own
current-source claim was never checked; (d) the reuse chain-of-custody only
compared worker-declared strings against each other within the same return,
never against anything independently readable. This section documents the
corrected, verified generation-2 behavior; see
`docs/reviews/CVF_EVIDENCE_READINESS_T1_WORKER_RETURN_2026-09-14.md` for the
full rejected-then-fixed history across both generations.

Applicability is derived only from the return's cited **dispatch work
order**, never from anything the worker return itself asserts. A worker
cannot opt a covered task out by omission or by tampering with its own
return. The exact trusted token, read verbatim from the dispatch work order
text:

`evidenceReadinessContract: REQUIRED_V1`

When (and only when) the dispatch work order carries that token, the worker
return must include:

`## Evidence Readiness Binding`

with these scalar fields (mirrors
`worker_evidence_readiness.REQUIRED_BINDING_FIELDS`):

- `evidenceBindingSchema` -- must equal `cvf.workerEvidenceReadiness.v1`
- `auditPath` -- repo-relative path to the bound audit/evidence artifact
- `auditSha256` -- sha256 of the audit artifact's current bytes
- `discoveryManifestPath` -- repo-relative path to a declared, independent
  discovery manifest (one normalized candidate path per line; never a
  recomputed scan)
- `sourceRoot` -- source root the row table is relative to (a Git mirror
  directory, or the source-project root for a non-Git snapshot)
- `sourcePin` -- immutable Git ref/commit or exact snapshot identity

`auditPath`, `discoveryManifestPath`, and `sourceRoot` are filesystem paths
and are validated with the same normalize/containment/symlink-escape check
as every row and manifest path (`worker_evidence_readiness.resolve_contained_path`)
-- a traversal segment, an absolute path, or a path that resolves through a
symlink outside the repository root is rejected on the binding field itself,
not only on manifest rows.

followed by a pipe table with exactly these five columns, in this order
(mirrors `worker_evidence_readiness.ROW_COLUMNS`):

`| path | blobSha256 | lineCount | readSpans | status |`

`status` must be one of `READ`, `REUSED`, or `EXCLUDED` (mirrors
`worker_evidence_readiness.ROW_STATUSES`). `readSpans` uses `start-end`
segments joined by `;`, for example `1-40;41-89`, or `none`/blank for an
`EXCLUDED` row. A `READ` row's span union must cover `1-lineCount` with no
gap -- a partial read can never satisfy a full-read claim.

**Source identity resolution.** Every non-`EXCLUDED` row (`READ` or `REUSED`
-- generation 2 closed the gap where `REUSED` rows skipped this entirely)
has its `blobSha256` AND `lineCount` resolved against the declared
`sourceRoot`/`sourcePin` through one bounded resolver, chosen automatically
from `sourcePin`'s shape: a hex Git sha/ref (or `HEAD`, or a `refs/...` ref)
uses `worker_evidence_readiness.GitBatchResolver` (one batched `git ls-tree`
call per distinct `(sourceRoot, sourcePin)` pair for blob identity, plus one
batched `git cat-file --batch` call to read blob content and count lines --
never a per-file subprocess); anything else uses
`worker_evidence_readiness.SnapshotResolver` for a non-Git local project (a
bounded, cached read of the exact file at `<sourceRoot>/<sourcePin>/<path>`,
hashed for digest and counted for lines from that same single read, never
read twice). A row whose source cannot be resolved at all (nonexistent
path, fabricated pin) is a hard issue, never silently skipped; a row whose
declared `blobSha256` does not match the resolved digest is rejected as a
mismatch; a row whose declared `lineCount` does not match the resolved
source's real line count is separately rejected -- a correct `blobSha256`
only proves the bytes match, it says nothing about a fabricated line count.
This is the check that certifies bound source identity, not merely internal
table consistency.

**`sourcePin: N/A` is not a blanket opt-out (generation 2).** A `sourcePin`
value containing `N/A` (or empty, `NONE`, `NOT_APPLICABLE`) is a legitimate
skip of source verification ONLY when the binding has no rows requiring it
in the first place -- every row is `EXCLUDED` with no populated
`blobSha256`, or the row table is empty. A binding whose rows have a
`READ`/`REUSED` status or a populated `blobSha256` cannot declare
`sourcePin: N/A` and expect that evidence to go unverified: an N/A pin is
not an immutable Git blob or exact snapshot pin (requirement 2), so this
shape is itself rejected as a hard issue (`/binding/sourcePin`) rather than
silently skipping verification.

**Reuse bindings.** A `REUSED` row must carry a corresponding row in a
dedicated `### Reuse Bindings` sub-table immediately inside the `## Evidence
Readiness Binding` section, with exactly these four columns (generation 2
added `priorArtifactPath`; see below):

`| path | priorArtifactSha256 | priorArtifactPath | priorBlobSha256 |`

keyed by the same normalized `path` as the main row table. This is a
dedicated pipe table, not a `reuse.<path>.<field>: value` scalar field line
-- a row path containing `.` or `/` (e.g. `src/a.ts`) cannot round-trip
through the generic scalar field-line grammar (`worker_evidence_readiness._FIELD_LINE_RE`
only matches a bare identifier key), so encoding the path into the field
name never worked and is not a supported binding shape. `priorArtifactSha256`
must point at an immutable prior artifact digest, never the current
`auditSha256` (rejected as a self-hash cycle); `priorBlobSha256` must equal
the row's current `blobSha256` (a changed source blob since the reuse was
recorded invalidates that reuse). The row's own current source
(`blobSha256`/`path`/`sourceRoot`/`sourcePin`) is ALSO resolved against the
real resolver exactly like a `READ` row (see Source identity resolution
above) -- a `REUSED` row with a fabricated/mismatched `blobSha256` is caught
the same way a `READ` row is, independent of the reuse-chain check below.

**`priorArtifactPath` -- chain-of-custody against real bytes (generation
2).** `priorArtifactSha256` alone is a bare hex string the worker typed;
comparing it only against other worker-declared strings in the same
document (`priorBlobSha256`, `auditSha256`) never confirms the referenced
prior artifact genuinely exists or genuinely has the claimed content -- a
fully self-consistent, fabricated reuse chain would previously pass clean.
`priorArtifactPath` is a repo-relative path to the real prior artifact
`priorArtifactSha256` claims to hash; when present, the checker resolves it
(same normalize/containment/symlink-escape check as every other path) and
hashes the real bytes, rejecting a `priorArtifactSha256` that does not
match. A reuse binding with no `priorArtifactPath` at all, or one that does
not resolve to a real, readable file, is itself an issue -- an unverifiable
bare digest is never a silent pass.

The prior artifact must contain the versioned Markdown Evidence Readiness
Binding and exactly one original `READ` row for the reused path. Its source
root, pin, blob and line count must match the current binding, with full
read-span coverage. Reference the original READ receipt directly; an
intermediate REUSED receipt or a file without a matching row is insufficient.
Prior bytes and parsed rows are reused within each validation call.
Git batch framing is parsed as bytes, preserving UTF-8 and CRLF boundaries.
An index integrity failure is a standalone blocking diagnostic from `run()`,
including when only an audit artifact changed and no return was selected.

Multiple source roots use repeated `## Evidence Readiness Binding` sections.
Each section owns its sourceRoot/sourcePin, audit projection, manifest and rows;
identical relative paths in different sections retain their source identity.
The checker aggregates section diagnostics and shares resolvers during `run()`.
Git pins must be full immutable object IDs; HEAD, refs and abbreviations are
rejected. Git tree lookups use only literal declared paths, with argument-size
bounded chunks, and reject symlink/tree entries.

New audit projections declare `schemaVersion: cvf.evidenceAudit.v1` in JSON
and a `workerReturnPath` locator. Unknown schema versions, non-object JSON,
invalid count types and duplicate scalar binding fields are rejected. Existing
unversioned JSON objects retain the original v1 projection-only checks; their
arbitrary payload is not certified as a recognized audit schema.
When the index is missing, changed versioned audits recover through a reciprocal
return binding or produce a blocking missing-coverage diagnostic. The locator
only selects a receipt; the receipt's dispatch and audit digest are still
validated. Legacy unversioned/uncontracted audits are not retrospectively
certified by this migration rule. Index entry types and duplicate keys are
checked. The evidence module is loaded on demand, with no new gate process.

The checker rejects: any declared discovery-manifest path with no matching
row (missing candidate), any row path outside the declared manifest (unknown
path), duplicate rows for the same path, a stale `auditSha256` that does not
match the bound audit artifact's current bytes, a missing `auditSha256`
altogether, non-JSON or duplicate-key audit content (the bound audit's bytes
are parsed with `worker_evidence_readiness.parse_strict_json`, not merely
hashed as opaque bytes -- a structurally declared count field inside the
audit JSON, when present, is cross-checked against the binding's row-derived
counts), a row's `blobSha256` or `lineCount` that does not match the
resolved source (generation 2 adds `lineCount`), a `sourcePin: N/A`-shaped
value on a binding with rows claiming real evidence (generation 2), a
`REUSED` row's reuse chain lacking a `priorArtifactPath` or whose
`priorArtifactSha256` does not match the real bytes at that path
(generation 2), and the current readiness placeholder tokens `TO_FILL`,
`FILL_ME`, any `TODO_` prefix, `WORKER_MUST_CAPTURE_AT_START`, and
`PENDING_BEFORE_READY` appearing inside a binding field or row -- while
historical fail/fix narrative written as ordinary prose elsewhere in the
return stays valid and untouched by this scan.

Binding is strictly one-directional: the finalized audit JSON's digest is
recorded into the Markdown return, never the reverse, avoiding a self-hash
cycle.

**Audit-only drift.** If a later change touches only the bound audit
artifact and not the worker-return Markdown, the checker still reaches the
same validator for the unchanged return. It finds the reverse binding
through the small bounded index at
`governance/compat/evidence_readiness_audit_index.json` (a declared
`auditPath -> [workerReturnPath, ...]` map), never through a full-repository
search. This index is populated **automatically**: every time `diagnose()`
successfully evaluates an applicable binding, it registers that return's
`auditPath -> workerReturnPath` mapping as a side effect
(`check_worker_return_quality_gate._register_evidence_readiness_binding`) --
no human ever hand-edits this file. A path with no entry in the index --
which today means every pre-existing historical packet and the parked R4
evidence, since neither was ever evaluated as an applicable binding -- is
simply not swept into evidence-readiness re-diagnosis; this is the explicit
migration rule for unchanged historical packets (worker order requirement
10). A newly authored applicable binding gains audit-only-drift coverage
automatically the first time it is diagnosed, with no separate registration
step.

**Index integrity (generation 2).** A MISSING index file (the ordinary,
expected first-use state) is never flagged -- it degrades to "no bindings
registered" exactly as before, with zero diagnostic noise. A PRESENT-BUT-
MALFORMED index file (not valid JSON, an empty file, or a JSON value that is
not an object) is now a real, surfaced integrity problem, not silently
equivalent to an empty index: `run()` reads the index once per invocation
and, if malformed, attaches a visible `evidence readiness: audit-readiness
index ... could not be read (...)` issue to every eligible return diagnosed
in that run, so a human sees the coverage gap instead of it vanishing.
Likewise, a failed index WRITE (disk full, permission denied, a concurrent-
write race) is no longer swallowed as a "non-fatal convenience side effect"
-- `_register_evidence_readiness_binding` surfaces the write failure as a
visible issue (`evidence readiness: audit-readiness index could not be
written (...)`) on the return being diagnosed.

**Shared resolver reuse across one `run()` invocation (generation 2, real
F5 wiring).** `run()` constructs exactly one resolver registry (keyed by
`(sourceRoot, sourcePin)`) for the whole invocation and threads it through
every `diagnose()` call in both the changed-path loop and the audit-only-
drift re-diagnosis loop. Two or more worker returns sharing the same
`(sourceRoot, sourcePin)` within one `run()` invocation therefore reuse a
single resolver instance -- and hence a single batched `git ls-tree`/
`git cat-file --batch` resolution pass -- instead of each `diagnose()` call
constructing its own resolver with an empty cache. A standalone `diagnose()`
call made without a `resolver_registry` (the previous, still-supported
shape used by direct callers and most existing tests) is unaffected: it
constructs a fresh resolver per call exactly as before.

**Semantics boundary.** A clean evidence-readiness result certifies evidence
consistency and bound source identity only. It never proves a human or agent
actually read a file, never proves a discovery pass was exhaustive outside
the declared candidate set, and never certifies the correctness of any
implementation claim -- those remain reviewer obligations.

**Scaffold applicability (self-determining, not opt-in).** Applicability for
generated scaffolds is derived automatically from the packet's own
already-declared shape (`worker_evidence_readiness.resolve_evidence_readiness_applicable`),
never from a flag a worker must remember to pass. `build_dispatch_packet_scaffold.py`
and `build_worker_return_skeleton_scaffold.py` both accept
`evidence_readiness_applicable` as a tri-state (`None` by default): when
unset, applicability auto-detects from the packet kind and from
indicator words in the title/dependency text (`audit`, `evidence
readiness`, `source verification`, `corpus scan`, `discovery manifest`,
`evidence binding`, `runtime value audit`, matched on word boundaries).
Passing `--evidence-readiness-applicable` forces it on; passing
`--no-evidence-readiness-applicable` is a deliberate, explicit override to
force it off for a genuine false positive -- but the *default* (neither flag
passed) now actively inspects the packet instead of silently defaulting to
uncovered. When applicable (by auto-detection or explicit flag), the
generated work order automatically carries the `evidenceReadinessContract:
REQUIRED_V1` token and a matching `## Evidence Readiness Binding` skeleton,
and the generated worker-return skeleton automatically carries the same
binding skeleton -- a future worker cannot omit the block by forgetting to
add it. An unfilled generated skeleton still fails evidence-readiness
validation (its `TO_FILL` tokens trip the current-placeholder check), so the
block cannot be shipped as inert boilerplate.

### Work-Order Dispatch Contract

No-commit work orders should cite the compact worker-return full-gate profile
instead of repeating each individual worker-return checker section:

`contractProfile: WORKER_RETURN_FULL_GATE_V1`

The dispatch-quality checker requires this profile, the
`run_worker_return_fast_gate.py` command, `individualCheckerSubstitution:
FORBIDDEN`, and `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`.

Dispatch-authorized docs-only work orders may instead use the Fast Doc Contract
from `CVF_WORKER_RETURN_FULL_GATE_CONTRACT_STANDARD.md`. The dispatch-quality
checker validates all fail-closed eligibility terms before dispatch, and the
worker-return checker validates the cited work order again at return time.

## Claim Boundary

This standard defines a structural quality gate only. It does not prove worker
implementation correctness, source absorption completeness, runtime/provider
behavior, public-sync readiness, MCP/CLI adapter behavior, model-router work,
action authority, automatic invocation, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-control reference standard; no public-sync artifact
is created by this tranche.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | worker-return quality gate standard |
| claimDisposition | CLAIM_REJECTED: this standard defines structural packet checks only |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local checker/helper invocation only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control |
| claimLanguage | structural worker-return quality guidance only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | WOAS-R4 worker-return quality gate and WOAS-R6 standard-checklist parity hardening, 2026-07-01 |
| Working directory | repository root |
| Command or tool surface | apply_patch, focused tests, governance gates |
| Target paths | this standard; worker-return quality checker parity tests; WOAS-R6 completion review |
| Allowed scope source | operator instruction to process the WOAS-R5 worker-return lessons by adding a worker authoring checklist and reducing repeated gate-discovery loops |
| Before status evidence | WOAS-R5 review identified repeated worker-return failures caused by hidden checker constants and literal-token traps already covered by ADIF entries |
| After status evidence | focused parity tests and pre-implementation autorun pass before material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | structural worker-return authoring checklist and checker-standard parity only |
| Claim boundary | no runtime/provider/public/source-import/MCP/model-router claim |
| Agent type | reviewer/closer |
| Invocation ID | `woas-r6-worker-return-standard-checklist-parity-2026-07-01` |
| Expected manifest | reference standard; parity test; completion review |
| Actual changed set | `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md`; `governance/compat/test_check_worker_return_quality_gate.py`; `docs/reviews/CVF_WOAS_R6_WORKER_RETURN_STANDARD_CHECKLIST_PARITY_COMPLETION_2026-07-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |
