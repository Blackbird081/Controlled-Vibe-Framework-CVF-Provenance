# CVF GC-020 Baseline - Post-Commit SHA Synchronization T1

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: GC020-SYNC-T1

Date: 2026-09-08

Dispatch base head: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

dispatchBaseHead: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_TO_SET

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

Authorize one bounded tranche that makes the governed tranche commit helper
deterministic after the material commit: capture the real full material SHA,
synchronize continuity surfaces through their governed generators and checkers,
and fail with a copyable recovery instruction instead of an unhandled exception.

## Target / Source

Target: `scripts/cvf_commit_tranche.py`, a new focused test file for it, and the
tranche commit choreography standard as its canonical contract owner.

Source: the current helper at dispatch base `39be75a7c`, the GC-020 in-place
update rule in `governance/compat/check_active_session_state.py`, and the
Step 4A helper contract in the choreography standard.

## Scope / Target / Owner Boundary

The batch hardens one existing helper and its documented contract, and adds the
focused test file that does not yet exist. It does not modify the encoding gate,
which is governed by the separate encoding rename-awareness packet.

It adds no hook, autorun, command-catalog, session-state checker or
active-handoff checker expansion. Any such need is a separately blocked
successor requiring fresh operator authorization.

## Accepted Authority And Findings

| Authority | Accepted fact |
|---|---|
| `scripts/cvf_commit_tranche.py` | `_commit_staged` returns `_short_head()`, so the value written into the handoff marker is an abbreviated SHA rather than the full material SHA. |
| `scripts/cvf_commit_tranche.py` | `_active_handoff_path()` is called again after the material commit, so the active handoff is already re-resolved post-commit. This is correct behavior and must be preserved. |
| `scripts/cvf_commit_tranche.py` | Only the pre-closure autorun gate runs; the three mandated continuity postconditions are absent. |
| `scripts/cvf_commit_tranche.py` | `_run` defaults to `check=True`, so a failing post-material step raises an unhandled `CalledProcessError` instead of returning a recovery instruction. |
| `scripts/cvf_commit_tranche.py` | `_replace_handoff_head` prepends its marker above the document when the legacy marker line is absent, which places text above the H1. |
| `governance/compat/check_active_session_state.py` | The GC-020 in-place update rule already allows a dedicated session-sync-only commit to cite its material parent SHA, because a commit cannot contain its own future content-addressed SHA. |
| `AGENT_HANDOFF_V60_2026-09-08.md` | The current active handoff contains no legacy `Current HEAD recorded for this handoff:` marker line. |
| `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | The choreography standard was registered as a `BINDING_REFERENCE_ACTIVE_WINDOW` entry during dispatch authoring, so it is exempt from stale-dated archive pressure. |
| `governance/compat/check_active_archive_hygiene.py` | A changed dated doc outside the active window fails `changed_stale_dated_docs`, which would have blocked this tranche's material commit before registration. |
| `governance/compat/generate_active_session_state.py` | The session aggregate is generated from `CVF_SESSION/state/` sources, so continuity semantics cannot be synthesized by the helper. |
| `governance/compat/generate_active_session_state.py::generate_aggregate` | Writes `CVF_SESSION/ACTIVE_SESSION_STATE.json`, then calls `generate_bootstrap_read_model`, which writes `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`. Both are generated outputs of `--generate`, never caller-authored manifest sources. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Carries the caller-authored `activeHandoff` field (verified present at line 35 in this repository) that `load_source_state` consumes when building the aggregate; this is the pre-generation source of truth for the intended handoff, not either generated file. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Exists as a distinct source entry file, separate from the core file, verified present in this repository. |
| `governance/compat/run_agent_autorun_workflow_gate.py::_write_receipt` | Creates the receipt directory and writes a JSON file under `.cvf/runtime/autorun-receipts/` on a successful full-phase run; a real filesystem mutation that must never occur during dry-run. |
| This baseline's own generation-4 pending-path rule | A strict `pendingPaths == manifestPaths` equality, checked unconditionally before any topology branch exists, rejects a retry that finds either derived output already present from a prior partial attempt (since both are forbidden manifest entries and therefore always outside the manifest set), and independently makes `ALREADY_SYNCHRONIZED` unreachable, because a clean post-commit tree has zero pending change against any manifest path. |

## Corrected Prior Finding

An earlier dependency-discovery report claimed the helper never re-reads
`activeHandoff` after the first commit. That claim was false. Current source
calls `_active_handoff_path()` after the material commit, so handoff rotation is
already resolved correctly. The finding is reclassified `ALREADY_IMPLEMENTED`
and the behavior is a preservation requirement of this tranche, not a defect to
repair.

## Decision / Baseline

GC020-SYNC-T1 selects a deterministic, resumable two-phase transaction with an
explicit topology classifier gating two named branches.

A single-shot transaction is impossible. A closed tranche requires continuity
changes to a source state entry, `nextAllowedMove`, the bootstrap read model,
the session front door, the active handoff narrative and the generated
`CVF_SESSION/ACTIVE_SESSION_STATE.json`. Those are semantic values that the
helper cannot infer from a commit message or handoff summary, and both
`CVF_SESSION/ACTIVE_SESSION_STATE.json` and
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` are generated outputs
of `generate_active_session_state.py --generate`, never caller-authored.

A strict `pendingPaths == manifestPaths` equality, checked before any topology
branch exists, cannot represent two real cases: a retry after a partial
failure that left one or both derived outputs already pending, and the fully
clean tree that exists immediately after a successful continuity commit.
Both require a topology classifier that runs first, splitting Phase 2 into two
named branches before any pending-path rule applies.

1. Phase 1, only when `--execute` is present, validates the staged material
   manifest, runs the narrow material preflight, commits material once,
   captures and prints the full material SHA, re-resolves the active handoff,
   returns `MATERIAL_COMMITTED_CONTINUITY_PENDING`, and prints a resume argv
   template. Without `--execute` it returns `DRY_RUN_MATERIAL_VALIDATED`
   without invoking the autorun preflight, so no file is written at all.
2. Between phases the caller authors the manifest's required source paths and
   writes the ignored runtime control manifest at its frozen SHA-keyed path.
3. Phase 2 first classifies topology from the current repository state:
   `HEAD == materialSha` with `materialSha^ == base` enters
   `PENDING_OR_RETRY`; `HEAD^ == materialSha` with `materialSha^ == base`
   enters `POSTCOMMIT_RECHECK`; anything else fails closed with no commit.
4. `PENDING_OR_RETRY` covers both a fresh resume and a retry after any earlier
   failure. Its pending invariant is the bounded range
   `manifestPaths subset-of pendingPaths subset-of (manifestPaths union
   derivedOutputs)`: every manifest path must have a pending change, both
   derived outputs remain forbidden as manifest entries, but either or both
   may be tolerated as pending residue from a partial prior attempt, and
   nothing else is allowed. Only in execute mode does it apply an idempotent
   handoff-evidence update, regenerate both derived outputs deterministically,
   verify post-generation agreement, stage the exact union, run the two
   continuity checkers before and after the continuity commit, and assert
   topology.
5. `POSTCOMMIT_RECHECK` performs no generation, staging, marker rewrite, or
   commit in either dry-run or execute. It verifies the exact committed path
   set, generated-output freshness, handoff evidence, and reruns the
   continuity checkers; passing all of it returns `ALREADY_SYNCHRONIZED`,
   failing any of it returns `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`, and
   `--execute` never authorizes a second commit in this branch.
6. Every failure prints the full material SHA, HEAD, staged and unstaged
   paths, the active handoff (or `null` with a diagnostic when resolution
   itself failed), and either the failed subprocess argv or a stable
   diagnostic code with structured details, plus a branch-appropriate resume
   argv template. No failure automatically resets, unstages, restores, or
   deletes pending content; the bounded manifest/derived changes remain
   available for the next retry.

The material SHA is the truthfully knowable synchronization anchor. No
surface may be required to predict or contain its own future SHA, and the
existing GC-020 parent-SHA allowance for a dedicated session-sync-only commit
is preserved unchanged.

### Frozen interface summary

The work order freezes the complete implementation contract:

- one required `--mode` option (`material` or `resume`); `--execute` optional
  in both, strictly non-mutating when absent, including no autorun receipt
  write; four legacy/bypass options explicitly rejected in both modes;
- the continuity manifest is an ignored JSON control file at a repo-relative
  (never absolute, even inside the correct directory) path exactly matching
  `.cvf/runtime/tranche-continuity/<full-material-sha>.json`, required to
  include five caller-authored members and forbidden from naming either
  derived output;
- the active handoff must exist as a root `AGENT_HANDOFF*.md` file, declare
  `Status: ACTIVE`, be the unique such file, and agree across the core
  source, the manifest, and post-generation resolution;
- topology classification runs before any pending-path check, splitting
  Phase 2 into `PENDING_OR_RETRY` (fresh resume or retry) and
  `POSTCOMMIT_RECHECK` (idempotency check only, never mutates);
- `PENDING_OR_RETRY`'s pending invariant is a bounded range tolerating zero,
  one, or both derived outputs as residue from a partial retry, never a
  strict equality that would deadlock a legitimate retry;
- `POSTCOMMIT_RECHECK` is the only path that reaches `ALREADY_SYNCHRONIZED`,
  making it actually reachable, unlike a design where idempotency is checked
  only after an unconditional pending-path equality that a clean tree can
  never satisfy;
- a closed eleven-value terminal-state enum with fixed exit codes, one frozen
  JSON Terminal Output Schema on every invocation including argument
  failures, `diagnosticCode` as a stable token with dynamic values isolated
  in `diagnosticDetails`, and `resumeArgvTemplate` available on every failure
  state that leaves the material commit intact - including
  `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`, whose safe recovery is a
  recheck, never a second commit;
- the handoff-evidence updater is idempotent: it replaces its own existing
  evidence block on retry rather than duplicating it;
- staged-path-set equality is normative in `PENDING_OR_RETRY`'s post-generation
  step; Git index ordering is never itself evidence of correctness.

This baseline and its paired work order describe one protocol; the work
order carries the full normative detail, and this summary must not drift
from it.

## Acceptance Matrix

| Case | Required result |
|---|---|
| full material SHA written | PASS, abbreviated form not substituted |
| missing/invalid `--mode` | `ARGUMENT_VALIDATION_FAILED`, exit code 2 |
| any of the four rejected legacy/bypass flags | `ARGUMENT_VALIDATION_FAILED` |
| `--execute` absent in either mode | zero mutation, including no autorun receipt write |
| material dry-run | `DRY_RUN_MATERIAL_VALIDATED`; autorun preflight not invoked |
| material validation failure (dry-run or execute) | `MATERIAL_VALIDATION_FAILED` |
| material commit operation failure | `MATERIAL_COMMIT_FAILED` |
| Phase 1 execute success | `MATERIAL_COMMITTED_CONTINUITY_PENDING` with `resumeArgvTemplate` |
| manifest names the generated aggregate or bootstrap model | `GENERATED_OUTPUT_MUST_NOT_BE_MANIFESTED` |
| manifest missing a mandatory member | `MANIFEST_MISSING_REQUIRED_MEMBER`, member class in `diagnosticDetails` |
| manifest control-file path is absolute, even inside the runtime directory | `MANIFEST_PATH_MUST_BE_REPO_RELATIVE` |
| manifest control-file path outside the frozen directory or SHA-mismatched | fail closed |
| active handoff not `Status: ACTIVE`, not unique, or disagreeing across sources | `STALE_HANDOFF_REJECTED` or a more specific diagnostic |
| topology unclassifiable (neither `HEAD == materialSha` nor `HEAD^ == materialSha`, given `materialSha^ == base`) | `CONTINUITY_VALIDATION_FAILED`, no commit |
| `HEAD == materialSha` | enters `PENDING_OR_RETRY` |
| `HEAD^ == materialSha` | enters `POSTCOMMIT_RECHECK` |
| a manifest path with no pending change, in `PENDING_OR_RETRY` | `MANIFESTED_PATH_HAS_NO_PENDING_CHANGE` |
| one or both derived outputs pending from a partial prior attempt | tolerated, not rejected as unrelated |
| a third/unrelated pending path outside manifest-union-derived | `UNRELATED_MATERIAL_STAGED` / `_PRESENT` |
| derived output named inside the manifest itself | still forbidden, regardless of pending-residue tolerance |
| retry after aggregate written, bootstrap generation failed | resumable; regeneration overwrites both outputs deterministically |
| retry after both outputs generated, a pre-commit checker failed | resumable from the same staged batch |
| retry after all paths staged, `git commit` failed | resumable; `CONTINUITY_COMMIT_FAILED` retry template targets `PENDING_OR_RETRY` |
| handoff evidence update on retry | idempotent; replaces its existing block, never duplicates |
| post-generation staged set | equals manifest paths union both derived outputs, verified by set equality, not staging order |
| generated output shows no staged diff | `GENERATED_OUTPUT_UNCHANGED`, fail before commit |
| `POSTCOMMIT_RECHECK` with clean tree, exact committed set, fresh derived outputs, matching handoff evidence, passing checkers | `ALREADY_SYNCHRONIZED`, no commit |
| `POSTCOMMIT_RECHECK` with any of those failing | `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`, carries `resumeArgvTemplate`, never a second commit even with `--execute` |
| commit topology | continuity parent is the material SHA; material parent is the closure base |
| any failure state | exactly one of `failedCommand` / `diagnosticCode` set, never both, never neither; no automatic reset/unstage/restore/delete of pending content |
| `activeHandoff` is `null` | only when handoff resolution itself failed, with a matching diagnostic |
| terminal output on any invocation, including argument errors | matches the frozen schema exactly |
| successful first run | `COMPLETE_ONE_MATERIAL_ONE_CONTINUITY`, exactly one material and one continuity commit |

## Evidence / Verification

The worker proves behavior with focused tests over isolated temporary
repositories only. No test may commit into this provenance repository. The
worker also runs the governed Python size guard and the worker-return fast gate,
and records exact changed-set evidence. No provider or live proof applies.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| abbreviated SHA is returned after commit | current defect evidence | `scripts/cvf_commit_tranche.py` | `_commit_staged` | `_short_head` | tranche commit helper | ACCEPT |
| handoff is re-resolved post-commit | already-implemented behavior | `scripts/cvf_commit_tranche.py` | post-material section of `main` | `_active_handoff_path` | tranche commit helper | ACCEPT |
| continuity postconditions are absent | current gap evidence | `scripts/cvf_commit_tranche.py` | `_run_preclosure` | `_run_preclosure` | tranche commit helper | ACCEPT |
| failures raise instead of instructing | current defect evidence | `scripts/cvf_commit_tranche.py` | `_run` | `check` | tranche commit helper | ACCEPT |
| marker is prepended above the document | current defect evidence | `scripts/cvf_commit_tranche.py` | `_replace_handoff_head` | `HEAD_LINE_RE` | tranche commit helper | ACCEPT |
| parent SHA is allowed for session-sync-only commits | canonical rule | `governance/compat/check_active_session_state.py` | GC-020 In-Place Update Rule | `parent_sha_in_handoff` | active session state guard | ACCEPT |
| helper contract owner | canonical standard | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | Step 4A - Optional Commit Helper | Helper contract | choreography standard | ACCEPT |
| generator exposes a check mode | machine interface | `governance/compat/generate_active_session_state.py` | argument parser | `--check` | session state generator | ACCEPT |
| active-window membership source | machine source | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | `windows` | `activePath` | active-window registry | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`commit choreography helper hardening`,
role=`reviewer/closer`, lifecyclePhase=`pre-closure`. Returned defects:
NONE_RETURNED. No existing ADIF entry binds this helper. No new ADIF entry is opened by this baseline; if the worker
finds a recurrence pattern worth recording, it must return
`BLOCKED_WITH_REASON` rather than creating an entry outside Write Ownership.

## Task Governance Routing Manifest

| Task class | Canonical owner |
|---|---|
| Autorun / commit steward | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` |
| Reviewer / closure choreography | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` |
| Session-sync | active handoff; `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Worker execution | `docs/reference/guard_orientation/README.md` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id GC020-SYNC-T1 --title "GC-020 Post-Commit SHA Synchronization T1" --date 2026-09-08 --base 39be75a7cff4fc9acdbf3dd129254ddb164947d0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance no-commit dispatch profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Reason for NOT_USED_WITH_REASON: the whole packet was authored directly from the canonical work-order template using the accepted ROLE-SOT-MH-T1 packet pair as structural reference. The helper command is recorded for provenance only and was not executed, so no scaffold file was generated or modified. |
| checkerReadAheadConfirmation | Applicable dispatch-quality, scaffold-provenance, structural, routing, size, self-protection and export checkers were read before authoring. |
| docOnlyNewFields | post-commit synchronization packet fields only; no runtime field |
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
| applicableCheckersRead | `governance/compat/check_active_session_state.py`; `governance/compat/check_next_move_freshness.py`; `governance/compat/generate_active_session_state.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `HEAD_LINE_RE`; `_short_head`; `_active_handoff_path`; `_replace_handoff_head`; `_run_preclosure`; GC-020 tokens `head_sha_in_handoff`, `parent_sha_in_handoff` and `handoff_sync_commit_only`; generator flags `--generate` and `--check`; size class `python_cli_orchestrator` |
| gateRunPurpose | confirm this packet pair satisfies dispatch-quality, scaffold-provenance, size and structural gates before worker dispatch |
| claimBoundary | records consulted checker sources and literal tokens only; asserts no worker gate result |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: harden the existing tranche commit helper
and add its first focused test file.

Protected paths:

- `scripts/cvf_commit_tranche.py`

Operator authorization: the operator authorized deterministic GC-020
post-commit SHA synchronization as one of two separate bounded packets after
ROLE-SOT-MH-T1 closure at `94c4922c29390ac6f362a6a56a71b3e5054926ae`.

Rollback boundary: revert only accepted GC020-SYNC-T1 helper, test, standard and
worker-return material. Preserve ROLE-SOT-MH-T1 at `94c4922c2`,
ROLE-SOT-EVIDENCE-T0 at `6bcdeaca8`, the RABA park at `0767a16e5`, P4-C1 at
`b9bdba712`, and all unrelated state.

Dispatch-authoring protected path, owned by the dispatch author rather than the
implementation worker:

- `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`

The dispatch author added exactly two additive `BINDING_REFERENCE_ACTIVE_WINDOW`
entries during authoring so the dated canonical standard this tranche must edit
is exempt from stale-dated archive pressure. No existing registry entry was
modified or removed. The implementation worker does not own this path and must
not mutate it.

Not authorized: hook, autorun, command-catalog, registry, session-state checker,
active-handoff checker, encoding gate, template, scaffold, provider/live,
public-sync, push, deploy or production changes.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Hardening could reintroduce a future-SHA requirement | The material SHA is the only synchronization anchor; a required case forbids self-reference |
| Removing `check=True` could hide failures | Failures must surface as deterministic recovery instructions with a state summary, never as silent success |
| Recovery automation could become destructive | Reset, amend, force-push and automatic destructive recovery are forbidden; the helper instructs, it does not repair |
| Marker insertion could corrupt document structure | A required case asserts H1-first structure when the legacy marker is absent |
| Tests could mutate this provenance repository | Focused tests must use isolated temporary repositories only |
| Helper growth could approach the size guard | Owner is 215 of 800 lines for `python_cli_orchestrator` at dispatch base |

## Current Runtime Freshness Verification

Verified at dispatch base `39be75a7c` on 2026-09-08: the helper is 215 lines,
the choreography standard is 371 lines, `scripts/test_cvf_commit_tranche.py` does
not exist, `generate_active_session_state.py` exposes `--check`, and the current
active handoff contains zero occurrences of the legacy marker line. The
active-window registry declares 15 `activePath` entries and does not contain the
choreography standard. No runtime, provider or live surface was contacted.

## Machine Closure Package

Applicable at closure: this baseline, the paired work order, the changed helper,
the new focused test file, the choreography standard, and the packet worker
return. Roadmap, registry JSON, external evidence digest and loop interlock are
`N/A with reason`: this bounded helper tranche opens no roadmap row, mutates no
registry, consumes no external evidence and adds no interlock edge.

## Claim Boundary

This baseline authorizes one bounded commit-helper hardening tranche. It claims
no implementation completion, no measured speed, cost or quota reduction, no
hook or autorun change, no encoding-gate change, and no public-sync, deployment
or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private provenance dispatch material. No public-sync artifact or public claim is
authorized by this baseline.
