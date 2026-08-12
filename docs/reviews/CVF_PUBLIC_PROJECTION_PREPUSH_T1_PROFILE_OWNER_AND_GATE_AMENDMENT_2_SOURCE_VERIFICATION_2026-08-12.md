# CVF Public Projection Pre-Push T1 Profile Owner And Gate Amendment 2 Source Verification

Memory class: FULL_RECORD

Status: ACCEPTED

docType: review

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2

## Purpose

Independently verify, against actual repository source, the closure-hook
size-guard failure that blocks commit/closure of the otherwise
functionally-accepted PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1 result, and
the exact refactor-target thresholds Amendment 2 must satisfy. This
document is dispatcher/Amendment-2-author work: it authors no
implementation, only the exact four-path authority repair (this file, the
Amendment 2 GC-018 baseline, the Amendment 2 work order, and the official
Python size-exception registry) that will govern a subsequent
maintainability-only refactor.

## Scope / Methodology

1. Read the existing worker return in full
   (`docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`,
   current SHA-256
   `2aa8da4d4d9682a02d0e5cfdcba6ced995f7101f6e8ec6857049dbb530232499`) to
   confirm its own recorded terminal disposition
   (`COMPLETE_PENDING_REVIEW`) and evidence.
2. Read the Amendment 1 authority set in full (work order, GC-018 baseline,
   source verification) to confirm this amendment's write-boundary,
   preimage-matrix, and pinned-command-manifest patterns before mirroring
   them for Amendment 2.
3. Read `governance/compat/check_python_automation_size.py` in full to
   verify the exact hard-threshold values and category-classification
   rules the dispatch's closure-hook failure cites.
4. Read `governance/compat/run_public_projection_pre_push_gate.py` and
   `governance/compat/test_run_public_projection_pre_push_gate.py` in full
   to confirm their current physical line counts and general structure
   (function boundaries, cohesive non-CLI helper candidates) as refactor
   input, without modifying either file.
5. Read `governance/compat/check_core_guard_self_protection.py` and
   `governance/compat/check_work_order_dispatch_quality.py` to confirm the
   required structural tokens this authority set and the eventual worker's
   refactor must satisfy.
6. Confirmed Core `HEAD`, the current five implementation paths' exact
   untracked status and SHA-256 preimages, staged content, and the public
   clone's clean state at dispatch, matching the dispatch prompt's own
   pinned values exactly (see Current Runtime Freshness Verification).
7. Read `governance/compat/policy_baseline.py` and
   `governance/compat/check_adif_defect_registry_disclosure.py` in full to
   verify the official new-exception seed and later downward-ratchet
   lifecycle, plus the exact repaired dispatcher disclosure query.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_python_automation_size.py`; `governance/compat/policy_baseline.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | existing-GC-018 `seedAuthorization` requirement; `approvedMaxLines`-only strict downward ratchet; `check_core_guard_self_protection.py`'s required `Authorized guard-maintenance scope` / `Protected paths` / `Operator authorization` / `Rollback boundary` tokens; `Large-Scope Change Authorization` marker and its 40-file default limit (not triggered); `check_python_automation_size.py`'s `DEFAULT_CLASS_THRESHOLDS` category names and hard-line values |
| gateRunPurpose | confirm the exact source facts this authority set cites (threshold values, classification rules, current line counts, preimage hashes) before authoring, so no claim in the baseline or work order is unverified prose |
| claimBoundary | source-fact verification and authority-document authoring only; no implementation, no package command execution, no commit |

## Authority And Base

- dispatchBaseHead: `225b6a01ab4400244a5cf56e47f58d16ecc0fba6`
  (Core `HEAD` at this authority repair).
- executionBaseHead: deliberately unset; the orchestrator supplies a
  distinct later value only after committing the exact four-path authority
  batch.
- Predecessor disposition: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1 is
  `FUNCTIONALLY_ACCEPTED` (independent reviewer reproduction: 58/58 focused
  tests PASS; real-candidate sandboxed run exit 0, `compliant: true`,
  `gateFailureCount: 0`; all seven external command categories PASS with
  exact evidence reconciliation; public clone unchanged at
  `021f8b852afc245a6383177dd69bf56caf488b02`) but
  `CLOSURE_REJECTED_SIZE_GUARD` (two of the five worker-owned files exceed
  their applicable hard physical-line thresholds under
  `governance/compat/check_python_automation_size.py`).

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `python_cli_orchestrator` hard threshold is 800 lines | `governance/compat/check_python_automation_size.py` | line 39 | `DEFAULT_CLASS_THRESHOLDS["python_cli_orchestrator"]["hardThresholdLines"]` | `DEFAULT_CLASS_THRESHOLDS` dict | ACCEPT |
| `python_test` hard threshold is 1200 lines | `governance/compat/check_python_automation_size.py` | line 37 | `DEFAULT_CLASS_THRESHOLDS["python_test"]["hardThresholdLines"]` | `DEFAULT_CLASS_THRESHOLDS` dict | ACCEPT |
| `python_library_helper` hard threshold is 900 lines, soft 600 | `governance/compat/check_python_automation_size.py` | line 38 | `DEFAULT_CLASS_THRESHOLDS["python_library_helper"]` | `DEFAULT_CLASS_THRESHOLDS` dict | ACCEPT |
| A `governance/compat/run_*.py` file classifies as `python_cli_orchestrator`; any other `governance/compat/*.py` (not `check_*.py`, not test-named) classifies as `python_library_helper` | `governance/compat/check_python_automation_size.py` | function `_classify_python`, lines 49-71 | `_classify_python` | classification function | ACCEPT |
| `governance/compat/run_public_projection_pre_push_gate.py` is currently 1380 physical lines | `governance/compat/run_public_projection_pre_push_gate.py` | full file | n/a | n/a | ACCEPT |
| `governance/compat/test_run_public_projection_pre_push_gate.py` is currently 1279 physical lines | `governance/compat/test_run_public_projection_pre_push_gate.py` | full file | n/a | n/a | ACCEPT |
| The profile's own `governed_python_automation_size` inherited-debt family checks a different, unrelated pinned file (`scripts/score_qbs_model_assisted_reviewers.py`), not this runner or test file - the dispatch's closure-hook failure is from the separate, general-purpose `check_python_automation_size.py` gate, not this profile's own inherited-debt mechanism | `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` | lines 65-71, `inheritedDebtFamilies.governed_python_automation_size` | `subjectPath` | policy `inheritedDebtFamilies` block | ACCEPT |
| `check_core_guard_self_protection.py` requires an `Authorized guard-maintenance scope` / `Protected paths` / `Operator authorization` / `Rollback boundary`-bearing `## Core Guard Self-Protection Authorization` section in any authorizing doc when a `governance/compat/*.py` path is created or modified | `governance/compat/check_core_guard_self_protection.py` | function `_has_core_auth`, referencing `_is_protected` (line 120) | `_has_core_auth`; `_is_protected` | self-protection required-token check | ACCEPT |
| `Large-Scope Change Authorization` is required only when changed files exceed 40 (default) or renames/deletes exceed the rename/delete limit; this four-path authoring delta does not trigger it | `governance/compat/check_core_guard_self_protection.py` | `DEFAULT_LARGE_SCOPE_LIMIT = 40`, line 30; large-scope evaluation at lines 405-413 | `DEFAULT_LARGE_SCOPE_LIMIT`; `_has_large_scope_auth` | large-scope gate | ACCEPT |
| A freshly seeded exception absent from the protected baseline is accepted only when `seedAuthorization` names an existing GC-018 file | `governance/compat/check_python_automation_size.py` | `_has_valid_seed_authorization`; new-exception branch in `build_report` | `_has_valid_seed_authorization` | size exception lifecycle | ACCEPT |
| A dirty tracked registry is compared with the committed `HEAD` version | `governance/compat/policy_baseline.py` | `load_json_policy_baseline` | `load_json_policy_baseline` | policy baseline loader | ACCEPT |
| After the seed is committed, the only automatically authorized mutation is a strict downward `approvedMaxLines` change with every other field identical | `governance/compat/check_python_automation_size.py` | `_is_authorized_ratchet_down` | `approvedMaxLines` | size exception lifecycle | ACCEPT |
| The five current implementation paths are untracked (not intent-to-added) at dispatch, staged content zero, Core `HEAD` `225b6a01ab4400244a5cf56e47f58d16ecc0fba6` | n/a (live Git working-tree state, not a file) | `git status --short`, `git diff --cached --stat`, `git rev-parse HEAD` run against Core at authoring time | n/a | n/a | ACCEPT |
| Public clone remains clean at `021f8b852afc245a6383177dd69bf56caf488b02` on `lpci1-ref-staging` | n/a (live Git working-tree state, not a file) | `git status --short`, `git rev-parse HEAD`, `git branch --show-current` run against the public-sync clone at authoring time | n/a | n/a | ACCEPT |

## Current Runtime Freshness Verification

Verified immediately before authoring this document:

- Core `HEAD`: `225b6a01ab4400244a5cf56e47f58d16ecc0fba6` - disposition
  MATCH against the dispatch's `CURRENT BASE`.
- Five current implementation paths: all five untracked (`??`), staged
  content zero (`git diff --cached --stat` empty) - disposition MATCH
  against the dispatch's stated "Current five implementation paths are
  untracked intentionally... Staged content is zero."
- Five preimage SHA-256 values: all five recomputed and MATCH the
  dispatch's `CURRENT PREIMAGE AUTHORITY` values exactly (see Preimage
  Authority Matrix in the accompanying GC-018 baseline for the full table).
- Line counts: `run_public_projection_pre_push_gate.py` 1380 lines,
  `test_run_public_projection_pre_push_gate.py` 1279 lines - disposition
  MATCH against the dispatch's stated closure-hook failure figures exactly.
- Public clone: clean, `HEAD` `021f8b852afc245a6383177dd69bf56caf488b02`,
  branch `lpci1-ref-staging` - disposition MATCH.

## Exact Amendment Decision

Authorize exactly one new implementation path:
`governance/compat/public_projection_pre_push_gate_lib.py`, classifying as
`python_library_helper` (soft 600 / hard 900) under
`check_python_automation_size.py`'s own classification rule (any
`governance/compat/*.py` that is not `check_*.py`-named, not `run_*.py`-named,
and not test-named).

Amendment 2 worker ownership becomes exactly seven paths (the prior six
plus `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`);
the existing worker return remains the only return path - no new
worker-return artifact is authorized.

Authorize exactly two freshly seeded registry exceptions: the runner as
`python_cli_orchestrator` capped at its exact 1380-line preimage, and the
test as `python_test` capped at its exact 1279-line preimage, both
`ACTIVE_EXCEPTION` and both seeded by the paired Amendment 2 baseline.
They exist only to admit the already-proven untracked preimages into the
governed commit flow. They authorize no growth and no semantic weakening.
After structural refactor the worker may ratchet only `approvedMaxLines`
downward to each file's exact final physical line count; every other field
is immutable, neither entry may be removed, and no helper exception is
authorized.

This is a maintainability-only structural refactor of already
independently proven behavior (see Authority And Base). It does not reopen
any semantic, functional, or evidentiary question Amendment 1 already
closed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects (bounded result of 10; resolver reported `Truncated: True`):
`ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`,
`ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`.

Disposition: the authority set applies these defects through exact source
and manifest verification, CVF-governed authority only, absorption N/A
boundaries, role-consistent dispatcher activity, checker read-ahead,
literal-marker discipline, bounded evidence claims, protected-path
authorization, and an execution ceiling sized above child-command timeouts.

## Findings / Position

**Functional correctness is independently proven and is not reopened by
this amendment.** The predecessor's real-candidate evidence (58/58 tests,
`compliant: true`, zero gate failures, exact evidence reconciliation on all
three `expectedEvidence`-bearing commands, public clone unchanged, no
sandbox/support residue) is accepted as-is. Amendment 2 authorizes no
change to any validation, evidence-reconciliation, or fail-closed logic;
it authorizes only where that logic physically lives across files.

**Maintainability/closure is genuinely blocked by hard size limits,
verified against actual source, not asserted.** `run_public_projection_pre_push_gate.py`
at 1380 lines exceeds the `python_cli_orchestrator` hard limit of 800 lines
by 580 lines - a violation, not a near-threshold warning. `test_run_public_projection_pre_push_gate.py`
at 1279 lines exceeds the `python_test` hard limit of 1200 lines by 79
lines. Both are real, source-verified hard-gate violations under
`check_python_automation_size.py`, independent of and separate from this
profile's own `governed_python_automation_size` inherited-debt family
(which pins an unrelated file, `scripts/score_qbs_model_assisted_reviewers.py`,
and is not implicated by this closure-hook failure).

**Amendment 2's purpose is structural extraction only, not semantic
reopening.** The refactor contract (see the accompanying GC-018 baseline's
Required Semantic Delta and Forbidden Scope sections) requires every
behavioral invariant Amendment 1 proved to be preserved byte-for-byte in
observable behavior: exact policy pins, exact 41-path manifest, check-
registry reconciliation, copy-isolated dependency topology (no live
links/hard links into Core/public-sync), the physical in-sandbox copy of
`next`, exact test/type/lint/build argv, exact evidence counts, public-root
before/after invariants, cleanup on success and failure, deterministic
JSON/human output, and current CLI arguments/exit semantics. Only the
physical file location of cohesive non-CLI logic changes.

## Risk / Corrective Action

None identified at the authoring stage. The refactor contract explicitly
forbids every known short-cut to satisfying a size guard without a genuine
structural extraction (deleting validation, weakening fail-closed
behavior, removing evidence reconciliation, semicolon-compression, hiding
executable Python in non-Python files, raising thresholds, removing or
mutating either seeded exception beyond its exact downward cap ratchet, or
editing the size guard) - see the
GC-018 baseline's Forbidden Scope section for the complete, literal list
carried forward from this dispatch.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher / Amendment 2 authority author |
| Provider or surface | local private Core only; no public clone or sandbox access |
| Session or invocation | `public-projection-prepush-t1-amendment-2-author-20260812` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | local file reads, Git read-only inspection (`git status --short`, `git rev-parse HEAD`, `git diff --cached --stat`, `sha256sum`), and read-only ADIF resolver query |
| Target paths | exact four-path authority repair: this file, the accompanying GC-018 baseline, the accompanying work order, and the size-exception registry |
| Allowed scope source | this dispatch's exact four-path authority-repair instruction |
| Before status evidence | Core `HEAD` `225b6a01ab4400244a5cf56e47f58d16ecc0fba6`; five implementation paths and three authority documents untracked; registry at its pinned pre-repair hash; staged zero; public clone clean at `021f8b852` |
| After status evidence | exact four-path authority repair authored; all five implementation preimages untouched; public clone still clean at `021f8b852afc245a6383177dd69bf56caf488b02` (disposition MATCH) |
| Diff evidence | `git status --short` shows the eight expected untracked paths plus the tracked registry repair; staged-content diff remains zero before return |
| Approval boundary | authority-authoring only; implementation worker executes the refactor in a separate, subsequent dispatch |
| Claim boundary | no implementation, no package command execution, no sandbox materialization, no commit, no push, deploy, provider/store, secret, network install, or public-clone mutation at any point |
| Agent type | dispatcher / Amendment 2 authority author |
| Invocation ID | `public-projection-prepush-t1-amendment-2-author-20260812` |
| Expected manifest | exactly four authority-repair paths |
| Actual changed set | exactly four authority-repair paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no path deleted or renamed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | authoring the exact four-path Amendment 2 authority repair; no implementation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT - no runner receipt is produced by authority-authoring work; the cited real-candidate receipt is the predecessor Amendment 1 worker's own, not reproduced here |
| actionEvidence | ACTION_EVIDENCE_PRESENT: direct source reads of the size checker, the two oversized files' line counts, the self-protection checker's required tokens, and the current Core/public-clone Git state, all performed and recorded above |
| invocationBoundary | exact four local authority paths only; no implementation preimage touched; no sandbox, no public clone write |
| interceptionBoundary | no IDE, provider, browser, network, or remote mutation claim |
| claimLanguage | authority-authoring complete; this document itself makes no functional or closure claim about the refactor, which has not yet been performed |
| forbiddenExpansion | no implementation, no package command, no sandbox execution, no commit, no push, deploy, secrets, provider/store, production, session-sync, or public mutation - none occurred |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this source verification and its sibling authority artifacts are
private provenance governance-control-plane work. No public artifact is
created.

## Claim Boundary

This document verifies, against actual repository source, the exact
thresholds, classification rules, current line counts, and required
structural tokens that govern PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2. It
authorizes the official two-entry GC-018-seeded exception repair but no
implementation, no commit, no package command execution, no
sandbox materialization, and no public-clone mutation. Functional
correctness of the existing five-path implementation is treated as already
independently proven (Amendment 1) and is not reopened here; only the
question of where that already-proven logic should physically live across
files, to satisfy the closure-hook size guard, is addressed by the
accompanying GC-018 baseline and work order.
