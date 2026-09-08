# CVF GC-018 Baseline - Encoding Rename Awareness T1

Memory class: governed-dispatch-baseline

docType: baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: ENCODING-RENAME-T1

Date: 2026-09-08

Dispatch base head: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

dispatchBaseHead: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: `d46a55d2b`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

sharedWorktreeCoordinationMode: `EXPLICIT_LANE_HANDOFF`

Decision owner: operator

Reviewer owner: internal orchestrator/reviewer

successorTrancheOpened: NO

EPISTEMIC_PROCESS_NA_WITH_REASON: dispatch baseline recording an operator
decision and its bounded scope; it authorizes work and makes no source-backed
evidence-comparison claim of its own.

## Purpose

Authorize one bounded local hardening tranche that makes the agent packet
authority and encoding gate rename-aware. The gate must stop reporting
pre-existing non-ASCII text as newly added when a governed file is renamed,
while keeping its existing detection of genuinely new non-ASCII text intact.

## Target / Source

Target: `governance/compat/check_agent_packet_authority_and_encoding.py` and
its focused tests, plus the encoding standard and ADIF-0011 as documentation
owners.

Source: the current checker at dispatch base `39be75a7c`, the canonical
encoding standard, and ADIF-0011 as the existing defect binding.

## Scope / Target / Owner Boundary

The batch enriches one existing checker owner and its existing focused test
file. It creates no new checker entrypoint, adds no hook or autorun wiring, and
does not touch the commit-choreography helper, which is governed by the separate
GC-020 post-commit SHA synchronization packet.

This baseline authorizes rename-provenance handling only. It does not authorize
normalizing historical Unicode, rewriting archived artifacts, or relaxing the
ASCII-default rule.

## Accepted Authority And Findings

| Authority | Accepted fact |
|---|---|
| `governance/compat/check_agent_packet_authority_and_encoding.py` | `_parse_name_status` keeps only the destination path for an `R` or `C` status, discarding the rename source recorded in the second field. |
| `governance/compat/check_agent_packet_authority_and_encoding.py` | `_added_lines` runs a pathspec-limited diff for the destination alone, so Git cannot pair source and destination blobs and reports the file as newly added. |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | Existing file convention is an allowed Unicode exception, and broad Unicode normalization across unrelated files is forbidden. |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md` | The encoding checker is the canonical binding for newly added non-ASCII text in governed markdown. |
| `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | The encoding standard was registered as a `BINDING_REFERENCE_ACTIVE_WINDOW` entry during dispatch authoring, so it is exempt from stale-dated archive pressure. |
| `governance/compat/check_active_archive_hygiene.py` | A changed dated doc outside the active window fails `changed_stale_dated_docs`, which would have blocked the material commit for this tranche before registration. |

## Decision / Baseline

ENCODING-RENAME-T1 selects one bounded control:

The encoding gate must derive newly added lines from rename-aware Git
provenance. For a renamed path it must preserve both source and destination,
compare the destination against the correct source blob or use an unrestricted
rename-aware diff that preserves pairing, and report only lines that are new
relative to that source. A pure rename must yield zero added lines. Parsing must
be lossless, using `git diff --name-status -z -M` or an equivalent, so quoting,
spaces and non-ASCII path names cannot corrupt the fields.

Git decides what is a rename. When similarity falls below the threshold and Git
reports a delete plus an add, no source relationship is established by that
evidence. The frozen behavior is to treat the destination as an ordinary added
file under existing enforcement, never to reconstruct provenance Git did not
establish.

Fail-closed behavior is retained only where provenance evidence is genuinely
unavailable. Treating every historical destination line as an addition is not
acceptable fail-closed behavior, because it produces false violations that push
agents toward the forbidden broad-normalization remedy.

The control is forward-only for changed paths. Historical artifacts are not
rewritten and the raw-preimage archive exceptions remain in force.

## Acceptance Matrix

| Case | Required result |
|---|---|
| pure `R100` rename carrying historical Unicode | PASS with zero added lines |
| rename plus one newly introduced Unicode character | exactly one violation, naming only the new line |
| rename plus ASCII-only edit | PASS |
| ordinary new file containing Unicode without exception | FAIL |
| existing file with newly added Unicode | FAIL |
| move below the similarity threshold | destination treated as an ordinary added file; no reconstructed provenance claimed |
| path containing spaces | source and destination resolved correctly |
| path containing non-ASCII characters | source and destination resolved correctly |
| malformed name-status record | deterministic fail-closed diagnostic |
| missing source blob or decode failure | deterministic diagnostic, not silent pass |
| binary rename | classified explicitly, no text violation |
| valid Text Encoding Exception present | behavior unchanged |
| untracked or provenance-unknown file | existing fail-closed behavior retained |

## Evidence / Verification

The worker runs the focused encoding suite, the governed Python size guard, ADIF
entry integrity, and the worker-return fast gate, and records exact changed-set
evidence. Rename behavior must be proven with real Git provenance in isolated
temporary repositories, not asserted in prose. No provider or live proof applies
to this repository-local checker packet.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| rename source is discarded at parse time | current defect evidence | `governance/compat/check_agent_packet_authority_and_encoding.py` | `_parse_name_status` | `_parse_name_status` | encoding gate | ACCEPT |
| per-path diff loses rename pairing | current defect evidence | `governance/compat/check_agent_packet_authority_and_encoding.py` | `_added_lines` | `_added_lines` | encoding gate | ACCEPT |
| existing convention is an allowed exception | canonical policy | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | Exceptions | Existing file convention | encoding standard | ACCEPT |
| broad normalization is forbidden | canonical policy | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | Agent Requirements | broad Unicode normalization | encoding standard | ACCEPT |
| checker binding for this defect class | existing binding | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0011.md` | field block | `checkerBindings` | ADIF entry | ACCEPT |
| active-window membership source | machine source | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | `windows` | `activePath` | active-window registry | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`encoding gate hardening`, role=`worker`,
lifecyclePhase=`pre-commit`. Returned defects: ADIF-0011, the matching active
entry, which is an owned documentation path in this tranche. No new ADIF entry is opened by this
baseline; ADIF-0011 is updated only after executable proof passes.

## Task Governance Routing Manifest

| Task class | Canonical owner |
|---|---|
| Encoding / symbol discipline | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |
| Guard / checker maintenance | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md` |
| Worker execution | `docs/reference/guard_orientation/README.md` |
| ADIF entry authoring | `governance/compat/check_adif_entry_integrity.py` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ENCODING-RENAME-T1 --title "Encoding Rename Awareness T1" --date 2026-09-08 --base 39be75a7cff4fc9acdbf3dd129254ddb164947d0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance no-commit dispatch profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Reason for NOT_USED_WITH_REASON: the whole packet was authored directly from the canonical work-order template using the accepted ROLE-SOT-MH-T1 packet pair as structural reference. The helper command is recorded for provenance only and was not executed, so no scaffold file was generated or modified. |
| checkerReadAheadConfirmation | Applicable dispatch-quality, scaffold-provenance, structural, routing, size, self-protection and export checkers were read before authoring. |
| docOnlyNewFields | rename-provenance packet fields only; no runtime field |
| claimBoundary | Scaffold provenance proves authoring origin only, not implementation correctness. |

## Evidence Reuse And Encoding Plan

- verificationMode: RECOMPUTE_REQUIRED
- recomputeReason: all Source Pin Contract hashes and owner line counts were recomputed by direct source read at the dispatch base commit because the prior dependency-discovery report contained a false finding, so no earlier session value may be carried forward
- priorVerificationArtifact: N/A with reason: no prior verification artifact is reused as evidence
- priorVerificationAnchor: N/A with reason: no prior verification anchor is reused
- freshRecomputeRequired: true
- unicodePathHandling: literal repo-root paths only, read with UTF-8-safe readers; this packet introduces no Unicode path segment
- extractedTextAuthority: N/A with reason
- externalEvidenceDisposition: N/A with reason: no external evidence or source bundle is consumed
- encodingPlan: ASCII-only authoring for this packet
- claimBoundary: records reuse and encoding intent only; asserts no worker gate result

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_adif_entry_integrity.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `_parse_name_status`; `_added_lines`; `AddedLine`; `ENCODING_EXTENSIONS`; `ENCODING_PATH_PREFIXES`; `EXCEPTION_MARKERS`; `RAW_PREIMAGE_ARCHIVE_ENCODING_EXCEPTIONS`; ADIF `enforcementLevel`, `checkerBindings` and `promotionState`; size classes `python_checker` and `python_test` |
| gateRunPurpose | confirm this packet pair satisfies dispatch-quality, scaffold-provenance, size and structural gates before worker dispatch |
| claimBoundary | records consulted checker sources and literal tokens only; asserts no worker gate result |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: make the existing encoding gate
rename-aware and extend its existing focused tests.

Protected paths:

- `governance/compat/check_agent_packet_authority_and_encoding.py`
- `governance/compat/test_check_agent_packet_authority_and_encoding.py`

Operator authorization: the operator authorized rename-aware encoding
enforcement as one of two separate bounded packets after ROLE-SOT-MH-T1 closure
at `94c4922c29390ac6f362a6a56a71b3e5054926ae`.

Rollback boundary: revert only accepted ENCODING-RENAME-T1 checker, test,
standard, ADIF-0011 and worker-return material. Preserve ROLE-SOT-MH-T1 at
`94c4922c2`, ROLE-SOT-EVIDENCE-T0 at `6bcdeaca8`, the RABA park at `0767a16e5`,
P4-C1 at `b9bdba712`, and all unrelated state.

Dispatch-authoring protected path, owned by the dispatch author rather than the
implementation worker:

- `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`

The dispatch author added exactly two additive `BINDING_REFERENCE_ACTIVE_WINDOW`
entries during authoring so the dated canonical standard this tranche must edit
is exempt from stale-dated archive pressure. No existing registry entry was
modified or removed. The implementation worker does not own this path and must
not mutate it.

Not authorized: hook, autorun, command-catalog, registry, session-state,
active-handoff, template, scaffold, commit-helper, provider/live, public-sync,
push, deploy or production changes.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Rename awareness could mask genuinely new Unicode | Negative cases require a rename plus new Unicode to report exactly the new line |
| Fail-closed removal could weaken the gate | Untracked, missing-blob, malformed-record and decode-failure paths keep deterministic fail-closed diagnostics |
| Agents could read this as license to normalize history | Standard update restates the broad-normalization prohibition alongside the rename rule |
| Binary renames could raise text violations | Binary classification is an explicit required case |
| Checker growth could approach the size guard | Owner is 567 of 1000 lines at dispatch base; the maintainability plan keeps the addition bounded |

## Current Runtime Freshness Verification

Verified at dispatch base `39be75a7c` on 2026-09-08: the encoding checker is 567
lines, its focused test file is 265 lines, the encoding standard is 96 lines and
ADIF-0011 is 124 lines. The active-window registry declares 17 `activePath`
entries after this dispatch authoring added two additive binding-reference
entries, and it now contains the encoding standard. ADIF-0011 is undated and
remains outside the dated-owner table. No runtime, provider or live surface was
contacted.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ENCODING_RENAME_AWARENESS_T1_COMPLETION_2026-09-08.md` | reviewer acceptance | PASS |
| Owned implementation | checker, tests, standard, ADIF-0011, worker return | material commit `d46a55d2b`; tests 40/40 | PASS |
| Roadmap state | N/A with reason: no roadmap row opened | N/A with reason | N/A with reason |
| Registry JSON | `governance/compat/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 aggregate drift check confirms source aggregate aligned; no tranche mutation required | PASS |
| Registry Markdown | `docs/reference/CVF_CORPUS_SCAN_REGISTRY.md` | GC-051 aggregate drift check confirms projection aligned; no tranche mutation required | PASS |
| External evidence digest | N/A with reason: no external evidence | N/A with reason | N/A with reason |
| System loop interlock | encoding standard and ADIF-0011 | policy and learning bindings | PASS |
| Session continuity | active continuity surfaces | separate continuity commit | N/A with reason: material-first choreography |

## Claim Boundary

This baseline authorizes one bounded encoding-gate hardening tranche. It claims
no implementation completion, no runtime or provider behavior, no public-sync or
deployment readiness, and no change to the commit-choreography helper, which is
governed separately.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private provenance dispatch material. No public-sync artifact or public claim is
authorized by this baseline.
