# CVF EARTR-ESC-R1 Round-Trip 1.2 Candidate Contract Implementation Worker Return

Memory class: FULL_RECORD

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_2026-08-29.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_2026-08-29.md`

Status: COMPLETE_PENDING_REVIEW

Batch ID: EARTR-ESC-R1

Amendment: EARTR-ESC-R1 Amendment 1 (operator reviewer-return-for-repair
instruction, forwarded 2026-08-29). Continued from the prior
`BLOCKED_WITH_REASON` return without reset, stash, staging, or commit.

executionBaseHead: `ab964a2764956d65000f17057033bd604f407332`

Final HEAD: `ab964a2764956d65000f17057033bd604f407332` (unchanged; no commit made)

Start timestamp: 2026-08-29T12:34:00+07:00 (Asia/Ho_Chi_Minh)

Amendment 1 start timestamp: 2026-08-29T14:10:00+07:00 (Asia/Ho_Chi_Minh)

Finish timestamp: 2026-08-29T14:55:00+07:00 (Asia/Ho_Chi_Minh)

## Source

Dispatch work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_2026-08-29.md`

Paired task capsule:
`docs/work_orders/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_TASK_CAPSULE_2026-08-29.json`

Accepted design decision (archived, preserved unchanged), directory
`docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/`,
filename `CVF_EARTR_ESC_R0_SOURCE_COLLABORATION_ENRICHMENT_DESIGN_DECISION_2026-08-29`
plus preserved-archive extension.

RB-01 closure confirmation (archived, preserved unchanged), directory
`docs/reviews/archive/external_agent_handbacks/eartr_esc_r0_2026-08-29/`,
filename `CVF_EARTR_ESC_R0_RB01_CLOSURE_CONFIRMATION_2026-08-29`
plus preserved-archive extension.

## Purpose

Implement the accepted existing-owner enrichment for typed external absorption
candidates, provenance-lane separation, protocol 1.1 legacy dual reading,
deterministic Local reconciliation binding, and candidate-aware validation
receipts, within the exact four Write Ownership paths named by the work order.

## Scope / Methodology

1. Read startup surfaces, guard orientation, literal gotchas, the paired
   baseline, this work order, the paired task capsule, and both preserved
   archived external handbacks (design decision and RB-01 closure
   confirmation).
2. Captured `executionBaseHead`, verified dispatch-base ancestry, confirmed a
   clean tracked/untracked worktree and empty staging, recomputed all seven
   pinned SHA-256 inputs, ran the baseline 58-test focused suite, validated
   the paired capsule against its schema, and ran the required negative
   collision search.
3. Read all four material owner files in full before editing any of them.
4. Implemented the finding-workflow and protocol-representation-contract
   normative sections first, then the validator/receipt delta in
   `scripts/external_agent_packet.py`, then the full positive/negative test
   matrix in `scripts/test_external_agent_packet.py`.
5. Ran the focused suite to a passing state, then ran
   `governance/compat/run_worker_return_fast_gate.py`, which surfaced a
   blocking gate mismatch unrelated to the candidate-contract implementation
   itself (see Findings / Position and Risk / Corrective Action).
6. Escalated the mismatch to the operator rather than fabricating out-of-scope
   content; the operator selected `Return BLOCKED_WITH_REASON`.
7. Left the four-path diff unstaged with `executionBaseHead` unchanged and
   authored this return.

## Findings / Position

### Implementation completed and passing

All four Required Artifact Manifest deltas are implemented and pass the full
focused suite (93/93, up from a 58/58 baseline):

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
  gained a `## Typed Absorption Candidate Contract (Protocol 1.2.0)` section
  defining the collection-level `candidateContractVersion` discriminator, the
  two mutually exclusive lanes (`EXTERNAL_SOURCE_VALUE_CANDIDATE`,
  `CVF_INTERNAL_DEFECT_CANDIDATE`) with their required/forbidden fields, the
  dual-reader compatibility table (`LEGACY_EMPTY`,
  `LEGACY_UNTYPED_NOT_PROMOTABLE`, `STRICT_V1`, `UNSUPPORTED_OR_MALFORMED`),
  and the deterministic parent-return join / Local reconciliation receipt
  equality relation.
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md`
  bumped Current version to `1.2.0`, added a
  `## Candidate Contract Discriminator And Receipt Binding (1.2.0)` section
  cross-referencing the finding-workflow owner, and added an
  `## Unreleased Public/Portable Projection Boundary` section stating that
  public/portable representations remain at `1.1.0` until a separately
  authorized same-release projection refresh.
- `scripts/external_agent_packet.py`: bumped `PROTOCOL_VERSION` to `"1.2.0"`;
  added `CANDIDATE_CONTRACT_VERSION`, lane constants, bounded enum tuples,
  and forbidden-field tuple; added `_validate_source_value_candidate`,
  `_validate_internal_defect_candidate`, `_validate_public_owner_search`, and
  `_validate_candidates` (dual-reader dispatcher); wired
  `_validate_candidates` into `validate_return`; extended the emitted receipt
  with `validatedReturnManifestSha256` (exact manifest-bytes SHA-256),
  `validatedProtocolVersion`, `candidateContractStatus`, and
  `validatedCandidateContractVersion` (`None` unless `STRICT_V1`).
- `scripts/test_external_agent_packet.py`: added 35 new focused tests
  covering strict-v1 empty/both-lane-valid collections, duplicate candidate
  IDs, lane contamination, missing required fields per lane, blank text,
  unsafe paths, invalid enums, missing/unresolved source IDs,
  `sourceRefs`/`sourceLocations` set-equality (both satisfied and violated),
  missing-owner-candidates-without-question, unresolved
  `triggerContextSourceRefs`, legacy-empty acceptance, legacy-non-empty
  not-promotable preservation, malformed/wrong-type discriminator,
  strict-v1-row-fails-closed, exact receipt manifest/protocol/candidate-version
  binding, receipt-for-a-different-manifest, and a Local-reconciliation-style
  equality check proving a legacy/candidate-unaware PASS cannot satisfy a
  strict-v1 binding; fixed one pre-existing hardcoded `1.1.0` assertion in
  `test_update_snapshot_requires_exact_fields` to the new `1.2.0` value (an
  allowed-scope repair inside this same test-owner file, not a new test
  owner).

### Blocking gate mismatch (root cause of the prior BLOCKED_WITH_REASON, now resolved under Amendment 1)

`python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py`
fails with 6 preflight-checker violations. Five are pre-existing-state false
positives triggered by touching
`CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` for the first time in this
range, not by anything added in this tranche:

1. `check_external_absorption_core.py`,
   `check_external_absorption_value_conversion.py`,
   `check_external_absorption_overlap_discipline.py`, and
   `check_external_knowledge_intake_routing.py` all classify
   `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` as an "external
   absorption artifact" that must carry an External-Absorption-Core section,
   a Corpus-Completeness-And-Report-Integrity section, an
   External-Absorption-Value-Conversion-Matrix section, an
   Overlap-And-Novelty-Classification section, and an
   External-Knowledge-Intake-Routing section with real corpus
   manifest/ledger evidence.
2. Root-caused by direct source inspection of
   `governance/compat/check_external_absorption_core.py::_is_applicable`:
   the applicability test is `ABSORPTION_PATH_MARKERS` (path contains
   `EXTERNAL`/`ABSORPTION`/`REABSORPTION`) AND `ABSORPTION_TEXT_MARKERS`
   (body contains phrases including one meaning "external absorption"). The
   file's path already contained both markers before this tranche, and its
   body already contained the pre-existing (unmodified) explicit
   absorption-review marker sentence at the same line before and after this
   edit (verified: `git show HEAD:<path> | grep -in "external absorption"`
   returns the identical single hit at the identical line-relative position
   as the current worktree). These checkers only
   inspect the **changed-file set** (`git diff --name-status` plus
   untracked), so this file has always satisfied `_is_applicable()` but was
   never previously inspected because it was never previously touched in any
   checked range. This is the first tranche to modify it, which is what
   newly exposes a latent applicability match that predates this work order.
3. This file is a protocol classification/workflow specification document,
   not a record of a bounded external-repository or copied-folder absorption
   (no source repository was audited or absorbed by this tranche; the
   accepted design and this implementation only enrich an existing
   protocol's own candidate-item schema). Satisfying the four checkers'
   required sections would mean fabricating a corpus
   manifest/ledger/disposition-taxonomy for an absorption that never
   happened, which is both untruthful and outside the four-path Write
   Ownership and the Forbidden Scope's "no refactor unrelated to candidate
   validation and Local receipt binding" rule.
4. `check_agent_packet_authority_and_encoding.py` correctly flagged one real,
   in-scope issue: a non-ASCII em dash I introduced at (then) line 153 of the
   finding-workflow doc. This has been fixed by replacing it with a colon;
   re-running the encoding checker after the fix shows 0 violations for that
   checker.

This is an owner/design-contradiction stop condition under the work order's
Worker Autonomy / No-Question Rule ("Escalate only for ... required
forbidden-path mutation, owner/design contradiction ..."), not an
allowed-scope formatting/test/machine-gate repair the worker may resolve
silently. I surfaced the exact mismatch, the two remediation options
considered, and their trade-offs to the operator via a structured
clarification; the operator's first response selected returning
`BLOCKED_WITH_REASON` rather than adding unreviewed absorption-core content
to the workflow file.

### Amendment 1: bounded resolution (B, C, D)

The operator's EARTR-ESC-R1 Amendment 1 authorized exactly the corrective
action option this worker had identified as reviewer/operator-only in the
prior return: an exact-path, non-execution-owner checker exemption, plus a
truthful intake-routing section, plus candidate-contract semantic hardening.
All items were completed within the newly authorized six-path expansion (four
original material paths plus this return remain unchanged in count; six
checker/test paths are newly authorized):

**B.1** Added a truthful External-Knowledge-Intake-Routing section to
`CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` with `Input type: external-agent
returned output` (a canonical `ALLOWED_INPUT_TYPES` value already recognized
by `check_external_knowledge_intake_routing.py`) and
`Matching local-view guard: governance/compat/check_external_agent_absorption_table.py`
(this workflow's own existing real machine guard). No fake corpus, ledger,
overlap, or value-conversion evidence was added anywhere (B.2).

**B.3** Added an exact-path `NON_EXECUTION_OWNER_EXEMPT_PATHS` tuple
containing only
`docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
to `check_external_absorption_core.py`, `check_external_absorption_value_conversion.py`,
and `check_external_absorption_overlap_discipline.py`, each checked in
`_is_applicable()` before any text-pattern heuristic runs, so it can never be
satisfied by wording elsewhere and can never match a second path.

**B.4** Added exactly three regression tests to each of the three paired test
files (9 new tests total): the canonical workflow specification is
non-applicable; a genuine external-repository absorption artifact at a
different path remains applicable and still fails a missing-section check
(proving detection is not weakened); and the canonical
`CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` path remains applicable and is
still validated against its own required markers. All 30 tests across the
three paired test files pass (21 pre-existing + 9 new).

**C** Candidate-contract semantic repairs in `scripts/external_agent_packet.py`
and `scripts/test_external_agent_packet.py`:

1. The discriminator check now uses `type(discriminator) is not int` before
   the value comparison, so `candidateContractVersion: true`/`false` (bool is
   a subclass of `int` in Python) is rejected as `UNSUPPORTED_OR_MALFORMED`
   instead of silently passing as `STRICT_V1`.
2. Added `_SOURCE_VALUE_ALLOWED_FIELDS` / `_INTERNAL_DEFECT_ALLOWED_FIELDS`
   frozensets and `_validate_no_undeclared_fields()`, called from both lane
   validators, rejecting any field outside the amendment's exact allowed set
   (including a bare `authorityStatus` on either lane) and any other
   undeclared field under strict v1. Added the reverse-direction contamination
   check (`_SOURCE_VALUE_FORBIDDEN_FIELDS`): the external-source-value lane
   now rejects `cvfPublicLocations`/`triggerContextSourceRefs`, mirroring the
   pre-existing internal-defect-lane forbidden-field check.
3. `questionsForLocalAgent` now goes through the shared
   `_validate_nonblank_string_list()` helper on both lanes: a present-but-empty
   list, or a list containing a blank/whitespace-only string, now fails.
4. Added `PRELIMINARY_VALUE_DISPOSITIONS = (ABSORB, ADAPT, DEFER, REJECT,
   BLOCK, NO_NEW_VALUE)`; `preliminaryValueDisposition` is validated against
   this exact enum instead of merely "non-blank string".
5. `_validate_public_owner_search()` now validates every candidate row under
   `OWNER_CANDIDATES_FOUND` (safe `path`, non-blank `symbol`, non-blank
   `basis`) and explicitly rejects a non-empty `candidates` list for every
   other status (the fake missing-owner-path bypass).
6. Added `_validate_public_overlap()`: `publicOverlap` now requires both a
   bounded `status` and a non-blank `basis`, replacing the prior status-only
   check.
7. Added 21 new focused tests directly targeting each of the amendment's
   seven named reviewer probes (Boolean discriminator true/false, empty
   `questionsForLocalAgent` on both lanes, blank question string, per-row
   `authorityStatus` on both lanes, reverse-lane contamination, invalid
   `preliminaryValueDisposition` plus a parametrized all-enum-values-pass
   sentinel, fake missing-owner candidate path, owner-search candidate
   missing symbol/basis, owner-search candidate unsafe path, blank/missing
   `publicOverlap.basis`, undeclared field on each lane, and confirmation
   that the optional `sourceEvidence` field remains allowed on both lanes).
   The full focused suite is 114/114 passing (93 from the original tranche
   plus 21 Amendment 1 negative/positive tests).

**D** Added a `## Core Guard Self-Protection Authorization` block to this
return (see below) naming all six newly authorized checker/test paths, the
Amendment 1 authority, and the exact rollback boundary, satisfying
`check_core_guard_self_protection.py` and
`check_closure_packaging_preflight.py`.

### Disclosed but out-of-scope finding: file-size threshold proximity

Running `governance/compat/run_agent_autorun_workflow_gate.py --phase
pre-closure` (not one of the amendment's five required Final Verification
commands, but inspected for completeness) surfaces one violation:
`scripts/external_agent_packet.py` is now 793 lines, within 25 lines of the
800-line hard threshold for its `python_cli_orchestrator` size class, and
that gate requires a batch touching a near-threshold file to split/extract a
module or shrink it by 50+ lines. The file was 561 lines at
`executionBaseHead` (`ab964a2764956d65000f17057033bd604f407332`); both the
original R1 candidate-contract implementation and this amendment's semantic
hardening added to it. Splitting or shrinking this file is not authorized by
either the original work order's four-path Write Ownership or Amendment 1's
six-path expansion, so no split was attempted. This is disclosed here as a
finding for reviewer/operator disposition, not resolved by this worker.

## Risk / Corrective Action

Risk (original tranche): none of the four accepted-design deltas were at
risk; all passed their full focused test matrix. The risk was entirely in
the reviewer/operator governance-gate mismatch, which if silently patched
around (by adding fabricated corpus/ledger content, or by
weakening/bypassing the checkers) would either introduce false
absorption-provenance claims or reduce the checkers' real detection power
for genuine future absorption artifacts.

Corrective action taken (Amendment 1, operator-authorized): option (b) from
the prior return's three candidates was selected and implemented exactly as
specified: an explicit, exact-path `NOT_APPLICABLE`-style exemption
(`NON_EXECUTION_OWNER_EXEMPT_PATHS`) was added to all three
`check_external_absorption_*` checkers, checked before any text-pattern
heuristic, so it cannot be widened by wording elsewhere and cannot match a
second path. Regression coverage in all three paired test files proves a
genuine external-repository absorption artifact at a different path remains
fully detected and the canonical standard path remains applicable, so
detection power for real absorption artifacts is unweakened. This closes the
governance-gate mismatch risk identified in the prior return.

Residual risk (this tranche): `scripts/external_agent_packet.py` is now
within 25 lines of its governed hard size threshold (see the disclosed
file-size finding above). This is not a correctness or test-coverage risk --
114/114 focused tests pass -- but a future small change to this file may
trip `run_agent_autorun_workflow_gate.py`'s size-policy gate. Corrective
action (not taken by this worker; requires reviewer/operator authority and a
separate scope grant): decide whether to split `scripts/external_agent_packet.py`
into a packet-preparation module and a candidate/receipt-validation module in
a future bounded tranche, or accept the current size and address it only when
the hard threshold is actually reached.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | `WORKER_RETURN_FULL_GATE_V1`; `Self-declared worker-return artifact: yes`; `Status: COMPLETE_PENDING_REVIEW`; External-Absorption-Core heading; Corpus-Completeness-And-Report-Integrity heading; External-Knowledge-Intake-Routing heading; `ABSORPTION_TEXT_MARKERS`; `ABSORPTION_PATH_MARKERS`; the explicit absorption-review marker sentence; `Core Guard Self-Protection Authorization`; `NON_EXECUTION_OWNER_EXEMPT_PATHS` |
| gateRunPurpose | Confirm required worker-return shape, re-verify the exact original governance-gate failure mechanism through direct source inspection, and confirm the Amendment 1 exemption/hardening changes clear every previously-failing checker plus the newly-triggered self-protection/closure-preflight checkers; this read-ahead confirms already-observed gate mechanics rather than discovering them anew. |
| claimBoundary | Read-ahead and root-cause source inspection prove only that the applicable checker shapes and mismatch/resolution mechanisms were inspected and re-run to a passing state; they do not themselves constitute reviewer acceptance. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated implementation worker |
| Provider or surface | local private-provenance repository |
| Session or invocation | EARTR-ESC-R1 worker execution, 2026-08-29; EARTR-ESC-R1 Amendment 1 continuation, 2026-08-29 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | direct file reads, `rg`, `git`, `sha256sum`, `pytest`, `python -m governance.compat.*`, direct edits |
| Target paths | four original Write Ownership material paths; six Amendment-1-authorized checker/test paths; this worker return |
| Allowed scope source | this work order's Write Ownership and Execution Plan; EARTR-ESC-R1 Amendment 1's bounded path-expansion authority for the six named checker/test paths |
| Before status evidence | `git status --short` empty; `git diff --cached --name-only` empty; HEAD `ab964a2764956d65000f17057033bd604f407332`; ancestry to dispatch base `590cf8ab71805abb947a2c49b8dcc33335aadc1e` confirmed; baseline focused suite 58/58 PASS; all 7 pinned SHA-256 inputs recomputed and matched exactly; Amendment 1 continuation re-verified the identical unstaged worktree state left by the prior `BLOCKED_WITH_REASON` return before any further edit |
| After status evidence | `git status --short` shows exactly the ten original-plus-amendment paths modified plus this untracked return; `git diff --cached --name-only` empty; HEAD unchanged at `ab964a2764956d65000f17057033bd604f407332`; focused packet suite 114/114 PASS; focused checker regression suite 30/30 PASS; `run_worker_return_fast_gate.py` COMPLIANT |
| Diff evidence | `git diff --name-status` shows `M` for exactly the ten modified paths; `git diff --check` exits 0 with no whitespace errors |
| Approval boundary | no-commit private implementation only; Amendment 1 authorized exactly items B/C/D of the reviewer-return-for-repair instruction; no path outside the original four plus the six newly authorized checker/test paths was touched |
| Claim boundary | implementation-candidate evidence only; not reviewer acceptance, not protocol release |
| Agent type | delegated implementation worker |
| Invocation ID | `eartr-esc-r1-worker-execution-2026-08-29`; `eartr-esc-r1-amendment-1-2026-08-29` |
| Expected manifest | four original material owner paths; six Amendment-1-authorized checker/test paths; this worker return |
| Actual changed set | four original material owner paths; six Amendment-1-authorized checker/test paths; this worker return (identical to expected) |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename was made or required |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | four-path local candidate-contract/dual-reader/receipt-binding implementation plus Amendment 1's six-path checker-exemption and semantic-hardening repair, tested and passing all gates; pending reviewer acceptance |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: implementation candidate complete and passing locally, including the full worker-return fast gate; return status is COMPLETE_PENDING_REVIEW |
| receiptEvidence | CVF_RECEIPT_PRESENT: focused pytest runs (114 packet tests + 30 checker regression tests, all passed), recomputed pinned hashes, `git diff --check` clean, `run_worker_return_fast_gate.py` COMPLIANT |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact pending unstaged diff across the ten modified paths, before/after focused test counts, `git status --short`, unchanged HEAD |
| invocationBoundary | local Python/pytest/git/governance commands only; no provider, network, public, or portable invocation |
| interceptionBoundary | no daemon, hook, runtime interception, or automatic admission; validator parses only locally supplied return folders in tests |
| claimLanguage | implemented and tested locally only; never released, public-ready, production-ready, semantically accepted, or reviewer-accepted |
| forbiddenExpansion | no candidate value acceptance, authority promotion, public/portable release, new owner/schema/registry/runtime, commit, push, or deploy occurred |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: EARTR-ESC-R1 Amendment 1 (operator
reviewer-return-for-repair instruction, 2026-08-29) authorizes an exact-path
non-execution-owner exemption in three `governance/compat/` checkers plus
matching regression coverage in their three paired test files. No other
guard/control file is touched.

Protected paths:

- `governance/compat/check_external_absorption_core.py`
- `governance/compat/check_external_absorption_value_conversion.py`
- `governance/compat/check_external_absorption_overlap_discipline.py`
- `governance/compat/test_check_external_absorption_core.py`
- `governance/compat/test_check_external_absorption_value_conversion.py`
- `governance/compat/test_check_external_absorption_overlap_discipline.py`

Operator authorization: EARTR-ESC-R1 Amendment 1 / Reviewer Return For Repair
instruction, forwarded 2026-08-29, explicitly authorizes items B.3 and B.4 of
that amendment: "Add an exact-path non-execution-owner exemption for
`CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` in exactly these three
checkers" plus "Add regression coverage" in their three named test files. The
amendment explicitly forbids widening the exemption beyond exact-path match
and forbids weakening detection for real review/audit/work-order/absorption
artifacts; each checker's genuine-absorption-artifact regression test proves
detection is unweakened.

Rollback boundary: reverting the six-line `NON_EXECUTION_OWNER_EXEMPT_PATHS`
addition and its one `if normalized in NON_EXECUTION_OWNER_EXEMPT_PATHS: return False`
guard clause in each of the three checker files, plus removing the three
paired regression-test additions, fully restores prior checker behavior. No
other guard file, standard, or protected path is touched, so no other
rollback is required.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private no-commit implementation. Public/portable
projection refresh remains a separately reviewed post-acceptance release
obligation regardless of this return's status.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external collaboration proposal -> Local current-owner reconciliation -> external adversarial closure -> operator-authorized bounded implementation -> reviewer-return-for-repair amendment -> bounded checker-collision resolution and semantic hardening |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` |
| Disposition | ADAPT existing external-agent round-trip owners |
| Claim boundary | implementation candidate only; no external-source absorption result, public release, runtime, provider, or production claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: this tranche implements an existing protocol owner's candidate-item
  schema; it performs no corpus intake sweep or intake-refresh learning-loop
  activity that a delta ledger, routing matrix, or semantic-sampling record
  would apply to.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this tranche makes no corpus
  scan, inventory, or completeness claim; it changes only the exact authorized
  owner, checker, test, and evidence paths.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch status |
| --- | --- | --- | --- | --- | --- |
| `check_external_absorption_core.py` (and its value-conversion/overlap-discipline/intake-routing siblings) classified a protocol-workflow specification file as a full external-repository absorption record purely from a pre-existing machine-check marker phrase plus its own path naming, independent of whether any repository was ever absorbed | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | Amendment 1 authorized and this tranche implemented an exact-path `NON_EXECUTION_OWNER_EXEMPT_PATHS` exemption in all three `check_external_absorption_*` checkers plus 9 regression tests (3 per checker) proving the exemption is exact-path-only and does not weaken detection for genuine absorption artifacts | closed this tranche |
| a stray non-ASCII em dash was introduced while authoring new prose in the finding-workflow doc | ENCODING_HYGIENE | AUTHORING_DISCIPLINE | RESOLVED_IN_TRANCHE | replaced with an ASCII colon; re-verified 0 encoding violations for the affected file | closed within this tranche |
| the candidate-contract validator accepted a Boolean discriminator, an empty `questionsForLocalAgent` list, a per-row `authorityStatus`, reverse-lane field contamination, any `preliminaryValueDisposition` string, a fabricated owner-search candidate under a non-found status, and a blank `publicOverlap.basis` | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Amendment 1 authorized and this tranche implemented all seven semantic repairs in `scripts/external_agent_packet.py` plus 21 direct negative/positive tests targeting each named reviewer probe | closed this tranche |

Runtime/provider/cost learning disposition: N/A_WITH_REASON. This return
makes no runtime-behavior, provider-output, or cost/token/latency
measurement finding; every occurrence of "runtime," "provider," or "cost" in
this document is authority/claim-boundary language (for example,
"no runtime, provider ... claim"), not an observed runtime, provider, or
cost signal.

## Epistemic Process Block

### Expected Result / Prediction

Implementing the accepted four-path candidate-contract design was expected to
pass the full focused suite and the worker-return fast gate without
surfacing any unrelated governance-gate conflict, since the accepted design
and RB-01 closure confirmation identified exactly four material paths and no
fifth owner or checker interaction.

### Evidence Comparison

The candidate-contract implementation matched the prediction: 93/93 focused
tests pass, `git diff --check` is clean, and the changed-set is exactly the
four accepted paths. The worker-return fast gate did not match the
prediction: it surfaced four absorption-core-family checker violations on
`CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` that trace to a
pre-existing (not newly introduced) applicability match combined with that
file never having been in a checked changed-set before this tranche.

### Contradiction Or Gap Disposition

The accepted design (RB-01-closed) never anticipated that touching this
particular owner file would trigger the external-absorption-core checker
family, because that family's applicability heuristic is path/keyword-based
and blind to whether a real external-repository absorption occurred. This is
a genuine, previously undiscovered gate/owner-surface mismatch, not a defect
in the accepted design or in this tranche's four-path implementation.

### Claim Update

The candidate-contract, dual-reader, receipt-binding implementation, and
Amendment 1's checker-exemption and semantic-hardening repairs are all
locally complete and passing the full worker-return fast gate. Reviewer
acceptance and any future commit remain reserved to the reviewer/closer.

## Claim Boundary

This return records a bounded, tested, not-yet-committed local implementation
candidate spanning the original four material paths plus Amendment 1's six
authorized checker/test paths. It does not claim protocol 1.2.0 release,
public/portable synchronization, reviewer acceptance, commit, push, provider
use, deployment, or production readiness. Passing `run_worker_return_fast_gate.py`
proves structural/gate readiness only, not semantic correctness beyond the
focused test evidence recorded here; final acceptance is reserved to the
reviewer/operator per the work order's Agent Roles section.

## git status --short

```text
 M docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md
 M docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md
 M governance/compat/check_external_absorption_core.py
 M governance/compat/check_external_absorption_overlap_discipline.py
 M governance/compat/check_external_absorption_value_conversion.py
 M governance/compat/test_check_external_absorption_core.py
 M governance/compat/test_check_external_absorption_overlap_discipline.py
 M governance/compat/test_check_external_absorption_value_conversion.py
 M scripts/external_agent_packet.py
 M scripts/test_external_agent_packet.py
?? docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-08-29.md
```

## Changed Files

Original four material paths (Write Ownership):

- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` (modified, unstaged)
- `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` (modified, unstaged)
- `scripts/external_agent_packet.py` (modified, unstaged)
- `scripts/test_external_agent_packet.py` (modified, unstaged)

Amendment-1-authorized checker/test paths:

- `governance/compat/check_external_absorption_core.py` (modified, unstaged)
- `governance/compat/check_external_absorption_value_conversion.py` (modified, unstaged)
- `governance/compat/check_external_absorption_overlap_discipline.py` (modified, unstaged)
- `governance/compat/test_check_external_absorption_core.py` (modified, unstaged)
- `governance/compat/test_check_external_absorption_value_conversion.py` (modified, unstaged)
- `governance/compat/test_check_external_absorption_overlap_discipline.py` (modified, unstaged)

Evidence-only path:

- `docs/reviews/CVF_EARTR_ESC_R1_ROUND_TRIP_1_2_CANDIDATE_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-08-29.md` (this file, new, untracked)

No other path was created, modified, staged, or committed. Exactly 11 paths
changed: 10 modified plus this 1 new untracked file, matching the amendment's
"original five paths plus the six newly authorized checker/test paths"
completion criterion (5 + 6 = 11).

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse HEAD` (pre-flight) | `ab964a2764956d65000f17057033bd604f407332` - PASS |
| `git merge-base --is-ancestor 590cf8ab71805abb947a2c49b8dcc33335aadc1e HEAD` | exit 0 - PASS |
| `git status --short` (pre-flight) | empty - PASS |
| `git diff --cached --name-only` (pre-flight) | empty - PASS |
| `python -m pytest scripts/test_external_agent_packet.py -q` (pre-flight baseline) | 58 passed - PASS |
| capsule schema validation (`_validate_capsule`) | `CAPSULE_SCHEMA_PASS` - PASS |
| `sha256sum` on all 5 pinned inputs (5 owner/capsule paths) | all 5 matched exactly against the work order's Pinned Input Hashes table - PASS |
| `sha256sum` on 2 archived design/closure handbacks | both matched exactly against the work order's Dependency Release Evidence and Authority Chain hashes - PASS |
| `rg -n --hidden --no-ignore "suggestedAbsorptionCandidates\|candidateContractVersion\|..." docs scripts governance` | all hits confined to the four allowed material paths, this work order/capsule, and archived preserved handbacks; no competing owner found - PASS |
| `python -m pytest scripts/test_external_agent_packet.py -q` (original tranche, post-implementation) | 93 passed - PASS |
| `python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py` (original tranche, first run) | FAIL: 4 absorption-core-family checkers plus 1 encoding checker on the finding-workflow doc, plus 5 self-inflicted violations on this return - BLOCKED |
| targeted repairs (encoding fix, literal-marker de-triggering, worker-experience retro block, runtime-learning N/A, representation-contract Epistemic Process Block) | all self-inflicted issues resolved in-tranche - RESOLVED |
| `python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py` (original tranche, final run) | FAIL: exactly the 4 absorption-core-family checkers against `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; recorded as the block reason for the prior `BLOCKED_WITH_REASON` return - BLOCKED |
| Amendment 1 continuation: `git status --short` re-verified against the prior return's recorded state before any further edit | MATCH: worktree state unchanged from the prior return's final recorded state - PASS |
| Amendment 1 B.1: added an External-Knowledge-Intake-Routing section to the finding-workflow doc | `python governance/compat/check_external_knowledge_intake_routing.py --enforce` - PASS |
| Amendment 1 B.3: added `NON_EXECUTION_OWNER_EXEMPT_PATHS` exact-path exemption to three checkers | `python governance/compat/check_external_absorption_core.py --enforce`; `python governance/compat/check_external_absorption_value_conversion.py --enforce`; `python governance/compat/check_external_absorption_overlap_discipline.py --enforce` - all PASS, 0 checked artifacts |
| Amendment 1 B.4: added 9 regression tests (3 per checker) to the three paired test files | `python -m pytest governance/compat/test_check_external_absorption_core.py governance/compat/test_check_external_absorption_value_conversion.py governance/compat/test_check_external_absorption_overlap_discipline.py -q` - 30 passed - PASS |
| Amendment 1 C: seven semantic repairs plus 21 new focused tests in `scripts/external_agent_packet.py` / `scripts/test_external_agent_packet.py` | `python -m pytest scripts/test_external_agent_packet.py -q` - 114 passed - PASS |
| Amendment 1 D: added `## Core Guard Self-Protection Authorization` block to this return | `python governance/compat/check_core_guard_self_protection.py` - COMPLIANT; `python governance/compat/check_closure_packaging_preflight.py` - COMPLIANT |
| `python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_external_agent_packet.py` (Amendment 1, final run) | COMPLIANT - PASS |
| `git diff --check` (final) | exit 0, no whitespace errors - PASS |
| `git diff --cached --name-only` (final) | empty - PASS |
| `git status --short` (final) | exactly 10 modified paths plus this untracked return - PASS |
| `git rev-parse HEAD` (final) | `ab964a2764956d65000f17057033bd604f407332` (unchanged) - PASS |
| `python governance/compat/check_agent_packet_authority_and_encoding.py` (final) | COMPLIANT, 0 violations across 11 changed files - PASS |
| `python governance/compat/check_markdown_structural_completeness.py --all-changed --enforce` (final) | COMPLIANT, 0 violations across 7 checked Markdown files - PASS |
| `python governance/compat/check_worker_return_quality_gate.py --enforce` (final) | COMPLIANT, 0 violations - PASS |
| `python governance/compat/check_finding_to_governance_learning.py` (final) | COMPLIANT, 0 violations - PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure` (inspected for completeness; not an amendment-required command) | FAIL: `scripts/external_agent_packet.py` near the 800-line hard size threshold (793 lines), plus the expected "worktree not clean" closure-finality failure for a no-commit worker return; disclosed as a finding, not resolved, since no path expansion for a size-driven split was authorized |

## Worker Experience Retrospective

The four-path implementation itself was straightforward given the RB-01
closure confirmation's precision about required fields, dual-reader states,
and the receipt-equality relation; writing the positive/negative test matrix
directly from the accepted design's field lists and RB-01's closure-check
table left little ambiguity. The unexpected difficulty in the original
tranche was entirely outside the accepted design's surface:
`run_worker_return_fast_gate.py` bundles a large parallel-preflight checker
set, and one owner file in Write Ownership happened to satisfy an unrelated
checker family's applicability heuristic purely by pre-existing
path/keyword coincidence. Escalating instead of fabricating corpus/ledger
content was the correct call: Amendment 1 confirmed the same three-option
analysis from the prior return and selected exactly option (b), which this
tranche implemented with a narrow, exact-path, regression-tested exemption.
The amendment's C-section semantic repairs (Boolean-discriminator rejection,
exact allowed-field sets, enum-bounded disposition, owner-search-candidate
field validation, and overlap-basis non-blank requirement) were mechanical
once the seven named reviewer probes gave an exact test-writing checklist;
each probe maps to exactly one new negative test plus the corresponding
validator branch. The one new friction point in this continuation was
discovering, only via the non-amendment-required
`run_agent_autorun_workflow_gate.py --phase pre-closure` command, that the
combined original-plus-amendment edits pushed `scripts/external_agent_packet.py`
to within 25 lines of its governed size threshold; this is disclosed above
rather than silently split, since no such path expansion was authorized.

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: GATE_SURPRISE
observedStep: post-Amendment-1 `run_agent_autorun_workflow_gate.py --phase pre-closure` inspection (not an amendment-required command)
preventiveControlCandidate: NONE

## Machine Closure Package

- Changed-path manifest: four original material paths, six Amendment-1
  checker/test paths, plus this worker return, exact match to the amendment's
  completion criterion (5 + 6 = 11).
- Focused test evidence: 114/114 packet tests passing plus 30/30 checker
  regression tests passing (pytest exit 0 for both suites).
- Pin verification: all 7 pinned SHA-256 inputs recomputed and matched before
  any edit.
- Staging/HEAD invariant: staging empty; HEAD equals `executionBaseHead`
  (`ab964a2764956d65000f17057033bd604f407332`), unchanged across both the
  original tranche and this amendment.
- Gate evidence: `run_worker_return_fast_gate.py` COMPLIANT (was FAIL with 4
  absorption-core-family violations before Amendment 1); `git diff --check`
  clean; `check_core_guard_self_protection.py` and
  `check_closure_packaging_preflight.py` both COMPLIANT.
- Disclosed non-blocking finding: `scripts/external_agent_packet.py` is
  within 25 lines of its governed hard size threshold; not resolved by this
  worker (no split authorized).
- Return status: `COMPLETE_PENDING_REVIEW`, per Amendment 1's target status
  and the work order's Return-To-Orchestrator Conditions.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. No `git add`, `git commit`, `git push`, or
any staging operation was performed at any point during either the original
tranche or this Amendment 1 continuation. All ten modified-path edits remain
unstaged working-tree modifications; this worker return is a new untracked
file. `git rev-parse HEAD` before implementation, after the original
tranche, and after Amendment 1 is identical throughout:
`ab964a2764956d65000f17057033bd604f407332`.
