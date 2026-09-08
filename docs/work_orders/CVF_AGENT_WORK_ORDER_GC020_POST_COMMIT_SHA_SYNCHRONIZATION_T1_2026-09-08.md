# CVF Agent Work Order - GC-020 Post-Commit SHA Synchronization T1

Memory class: governed-worker-dispatch

docType: work_order

## Dispatch Prompt Envelope

Role: internal governance implementation worker; the orchestrator/reviewer owns
acceptance and commits.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md`.

Paired baseline: `docs/baselines/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture the exact clean committed HEAD immediately before the
first edit and use it for every worker-range command.

Current-time notes: operator-authorized bounded packet on 2026-09-08 after
ROLE-SOT-MH-T1 closed at `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_MH_T1_DISPATCH_COORDINATION_AND_DEPENDENCY_DISCOVERY_MACHINE_HARDENING_2026-09-08.md` commit `94c4922c29390ac6f362a6a56a71b3e5054926ae`. Local hardening only; external invocation count remains
zero.

Do-not-misread notes: the helper already re-reads the active handoff after the
material commit. That behavior is correct and must be preserved, not
reimplemented. Never require any surface to predict its own future SHA. Do not
bypass hooks, do not automatically reset, amend or force-push, and do not touch
the encoding gate.

Return contract: return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` in `docs/reviews/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_WORKER_RETURN_2026-09-08.md` with full status, staging state and the exact owned-path manifest; do not stage or commit.

Required first actions: read the startup surfaces, guard orientation, literal
gotchas, the paired baseline and this packet; capture HEAD and full status;
require a clean worktree and empty staging; recompute every Source Pin Contract
hash; then run pre-implementation.

Status: DISPATCH_READY

Batch ID: GC020-SYNC-T1

Date: 2026-09-08

Dispatch base head: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

dispatchBaseHead: `39be75a7cff4fc9acdbf3dd129254ddb164947d0`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_TO_SET

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_WORKER_RETURN_2026-09-08.md`

successorTrancheOpened: NO

EPISTEMIC_PROCESS_NA_WITH_REASON: dispatch packet defining scope, ownership and
required proof; the worker return carries the evidence comparison.


## Purpose

Make the post-material phase of the governed tranche commit helper
deterministic: real full material SHA, governed continuity synchronization,
structurally valid marker placement, and copyable recovery instructions.

## 1. Mission

Make the post-material phase of the governed tranche commit helper
deterministic: real full material SHA, governed continuity synchronization,
structurally valid marker placement, and copyable recovery instructions instead
of unhandled exceptions.

## 2. Authority Chain

| Level | Artifact |
|---|---|
| Operator authorization | operator direction on 2026-09-08 to open encoding and GC-020 hardening as two separate bounded packets |
| Paired baseline | `docs/baselines/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md` |
| Canonical contract | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` Step 4A |
| Canonical GC-020 rule | `governance/compat/check_active_session_state.py` GC-020 In-Place Update Rule |
| Predecessor closure | ROLE-SOT-MH-T1 `CLOSED_PASS_BOUNDED` at `94c4922c29390ac6f362a6a56a71b3e5054926ae` |

## 3. Agent Roles

| Role | Responsibility | Limit |
|---|---|---|
| Operator | authorizes this exact packet and retains expansion checkpoints | no implementation role implied |
| Dispatcher | fixes sources, exact scope, cases, stop rules and rollback | does not edit worker-owned material after dispatch |
| Worker | implements and verifies exact owned paths | no stage, commit, scope expansion or external effect |
| Reviewer/closer | evaluates returned evidence, performs bounded allowed-scope repair if justified, and commits accepted material | does not recreate implementation or broaden claims |

## 4. Scope

In scope: the post-material behavior of the commit helper, its first focused
test file, and the Step 4A helper contract in the choreography standard.

Out of scope: the encoding gate and every rename-provenance concern, which are
governed by `docs/work_orders/CVF_AGENT_WORK_ORDER_ENCODING_RENAME_AWARENESS_T1_2026-09-08.md`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`commit choreography helper hardening`,
role=`reviewer/closer`, lifecyclePhase=`pre-closure`. No existing ADIF entry
binds this helper. Returned defects: NONE_RETURNED. No ADIF path is owned by this
tranche. If a recurrence pattern warrants an entry, return `BLOCKED_WITH_REASON`
instead of creating one.

## 5. Required First Reads

| Source | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | bootstrap facts |
| `AGENT_HANDOFF_V60_2026-09-08.md` | active handoff and its current marker state |
| `docs/reference/guard_orientation/README.md` | applicable role and task guards |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | known gate traps |
| `docs/baselines/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md` | paired baseline |
| `scripts/cvf_commit_tranche.py` | owned helper source |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | owned contract section |
| `governance/compat/check_active_session_state.py` | GC-020 parent-SHA rule |
| `governance/compat/check_next_move_freshness.py` | required postcondition |
| `governance/compat/generate_active_session_state.py` | generator and its check mode |

## 6. Pre-Flight Checks

Capture the full `executionBaseHead`; require an empty
`git status --short --untracked-files=all` and empty staging; prove that
dispatch `39be75a7cff4fc9acdbf3dd129254ddb164947d0` is an ancestor of HEAD;
recompute every Source Pin Contract hash; and run pre-implementation. Stop
before edits on drift or any unexpected path.

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously inside Write Ownership. Repair routine in-scope failures
after reading the failing checker source. Return `BLOCKED_WITH_REASON` for any
needed path expansion, source contradiction, maintainability violation, registry
mutation, hook or autorun change.

## 6F. Near-Threshold Owner Maintainability Plan

At dispatch base the owned helper is 215 lines against an 800-line hard
threshold for `python_cli_orchestrator`, and the new test file starts empty
against a 1200-line hard threshold for `python_test`. Neither enters the
near-hard band. Keep the synchronization logic inside the existing helper rather
than opening a module not listed in Write Ownership. If the helper would exceed
700 lines, stop and return `BLOCKED_WITH_REASON`.

This work order itself is governed `active_markdown` (advisory 900 lines, hard
1200 lines). Rework generation 2 froze the complete Phase 1/Phase 2 interface
inside this document. Rework generation 3 closed the dry-run/`--execute`
self-contradiction, the terminal-state enum, the manifest control-file
boundary, and the idempotency topology. Rework generation 4 corrected the
generated-versus-caller-authored ownership model, the pre/post-generation
handoff authority, the dry-run boundary, and pending-path equality, and
compacted the focused case matrix into grouped comma-separated lists. Rework
generation 5 introduced an explicit topology classifier with two named
branches (`PENDING_OR_RETRY`, `POSTCOMMIT_RECHECK`), replacing the
unreachable-idempotency and retry-deadlock defects the classifier repairs,
bringing this document to approximately 1100 lines - still comfortably clear
of the 1200-line hard threshold. If any future rework would push this
document within 25 lines of 1200, split the frozen protocol content into a
dedicated `docs/reference/` contract standard in that same batch, per the
Governed File Size Guard, rather than trimming prose to stay under the
limit.

## 6G. Work-Order Fulfillment Manifest

The Required Artifact Manifest is the complete fulfillment manifest. Exactly
those four paths may be pending at worker return; any fifth path is blocking.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/cvf_commit_tranche.py` | MODIFY post-material synchronization only |
| `scripts/test_cvf_commit_tranche.py` | CREATE focused tests over isolated temporary repositories |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | MODIFY the Step 4A helper contract |
| `docs/reviews/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_WORKER_RETURN_2026-09-08.md` | CREATE complete no-commit evidence return |

## Forbidden Path Manifest

- `governance/compat/check_agent_packet_authority_and_encoding.py` and every
  encoding surface;
- `AGENTS.md`, `CVF_SESSION/`, the active handoff, roadmaps, this packet and its
  paired baseline;
- the work-order template, dispatch scaffold and active-window registry;
- hook, autorun, command-catalog and exception-registry surfaces;
- `governance/compat/check_active_session_state.py`,
  `governance/compat/check_next_move_freshness.py` and
  `governance/compat/generate_active_session_state.py`, which are read-only
  dependencies here.

## Forbidden Scope

- no hook, autorun, command-catalog, session-state checker or active-handoff
  checker expansion;
- no `--no-verify` or any hook bypass;
- no automatic reset, amend, force-push or destructive recovery;
- no test that commits into this provenance repository;
- no future-SHA or self-referential current-commit requirement;
- no speed, cost or quota-reduction claim without measured evidence;
- no provider, live, network, credential, package install, public sync, push,
  deployment, runtime or production action;
- no staging or commit by the worker.

## Source Pin Contract

| Source | Expected SHA-256 |
|---|---|
| `scripts/cvf_commit_tranche.py` | `7fb9e1e45979e839639dd6c70de985706838b208b59377d3a09477d5a1562d9a` |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | `d02409b998552c117becf29c31c3c2c1f0711cb11b8a8bd16de3b748f5b4c782` |
| `governance/compat/check_active_session_state.py` | `7ef59d567124ce99b993d2f67e123cd458f0244797ffe8a87cbd152c6c514834` |
| `governance/compat/check_next_move_freshness.py` | `f21b072fb77faaa09324621eaf676c56705cdfe6b87b2115efa43f9d136e4add` |
| `governance/compat/generate_active_session_state.py` | `764115c0c9429cb4c39a355be02b7422325e114e6922debe26609ae6c890636a` |
| `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | `a5261b674cab6b112a8e45d0df9a2efa1d159a070656d985cbb4db5a70f9e866` |

## 7. Write Ownership

Modify exactly:

1. `scripts/cvf_commit_tranche.py`
2. `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`

Create exactly:

3. `scripts/test_cvf_commit_tranche.py`
4. `docs/reviews/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_WORKER_RETURN_2026-09-08.md`

All four paths remain unstaged and uncommitted at worker handoff. Add another
owner only if current source proves it strictly necessary; that proof requires
returning `BLOCKED_WITH_REASON` for operator authorization first.

## 7A. Protected-Path Authorization Carrier

The owned helper is a governed automation script under the Core Guard Self
Protection Guard. The authorization block below names it explicitly.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: harden the existing tranche commit helper
and add its first focused test file.

Protected paths:

- `scripts/cvf_commit_tranche.py`

Operator authorization: the operator authorized deterministic GC-020
post-commit SHA synchronization as one of two separate bounded packets after
ROLE-SOT-MH-T1 closure at `94c4922c29390ac6f362a6a56a71b3e5054926ae`.

Rollback boundary: revert only accepted GC020-SYNC-T1 material. Preserve
ROLE-SOT-MH-T1 at `94c4922c2`, ROLE-SOT-EVIDENCE-T0 at `6bcdeaca8`, the RABA
park at `0767a16e5` and P4-C1 at `b9bdba712`.

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

## Dated Owner Dependency Discovery

| Owned dated reference path | Classification | Registry evidence | Disposition |
|---|---|---|---|
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | `BINDING_REFERENCE_ACTIVE_WINDOW` | registry entry id `tranche_commit_choreography_standard_active_reference` in `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; registered during dispatch authoring, so the implementation worker neither owns nor mutates the registry | ACCEPT |

Registration was completed during dispatch authoring. The implementation worker
does not own the registry, must not mutate it, and inherits the binding
classification as a settled precondition.

## Shared Worktree Coordination

| Field | Value |
|---|---|
| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |
| activeLaneOwner | GC020-SYNC-T1 internal no-commit worker from execution anchor capture until returned status evidence |
| laneOwnedPaths | exactly the four Write Ownership paths |
| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |
| laneReleaseEvidence | worker return records final full status and empty staging; reviewer explicitly accepts control of the paths before any isolation or commit |

This is a packet-contract declaration. It does not intercept Git or filesystem
operations and does not prove that concurrent writes were technically prevented.

## Protocol / Contract / Requirements

### Preserved behavior

The helper already re-reads the active handoff after the material commit. That
call must be preserved so handoff rotation continues to resolve correctly. It
is not a defect and must not be reimplemented. The existing handoff-only
staged-path guard must be preserved.

### Generated Versus Caller-Authored Ownership (frozen)

Direct source verification of `governance/compat/generate_active_session_state.py`:
`generate_aggregate()` writes `CVF_SESSION/ACTIVE_SESSION_STATE.json`, then
calls `generate_bootstrap_read_model()`, which writes
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`. Both files are
generated outputs of `--generate`; neither is a caller-authored manifest
source, and the manifest must forbid both.

The caller-authored source of truth for the intended active handoff is
`CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` (`activeHandoff` field,
verified present at `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json:35` in
this repository), consumed by `load_source_state()` when building the
aggregate. `CVF_SESSION/state/entries/nextAllowedMove.json` is a distinct
source entry file (verified present), separate from the core file.

`governance/compat/run_agent_autorun_workflow_gate.py::_write_receipt` writes a
JSON receipt under `.cvf/runtime/autorun-receipts/` (`path.parent.mkdir` plus a
file write) whenever a full autorun phase run succeeds. That write is a real
filesystem mutation and must never occur during dry-run.

### Frozen CLI Interface

One required option, `--mode`, accepting exactly `material` or `resume`,
mutually exclusive by construction. Omitting `--mode`, or any other value, is
`ARGUMENT_VALIDATION_FAILED`, exit `2`. `--execute` is OPTIONAL in both modes;
absent selects dry-run, present selects mutating execution; never required.

`--mode material`: `--base`, `--message` required; `--execute` optional.
Forbidden: `--resume-material-sha`, `--continuity-manifest`,
`--continuity-message`.

`--mode resume`: `--resume-material-sha` (exactly 40 hex chars), `--base`,
`--continuity-manifest` required; `--continuity-message` required only with
`--execute`; `--execute` optional. Forbidden: `--message`.

Rejected in both modes, `ARGUMENT_VALIDATION_FAILED`: `--handoff-message`,
`--handoff-summary`, `--allow-unstaged`, `--skip-preclosure`. No flag may
bypass any preflight, check, or hook.

### Dry-Run Boundary (frozen, corrected)

Material dry-run performs only internal, read-only validation of arguments and
the staged manifest. It never invokes
`run_agent_autorun_workflow_gate.py` (which would write an ignored autorun
receipt - a real mutation) and never writes any file. It returns
`DRY_RUN_MATERIAL_VALIDATED` as a plan-validation result, not gate proof. The
narrow material preflight (the autorun runner) is invoked only in execute
mode, immediately before the material commit.

Resume dry-run validates arguments, the manifest, repository topology, the
current core-resolved handoff, and pending-path equality against the
manifest. It invokes no generator, no autorun gate, no receipt-writing
command, and stages nothing. It returns `DRY_RUN_CONTINUITY_PLAN_VALIDATED`
and never claims generated-output or post-generation checks passed, since
generation never ran.

Both dry-run modes preserve, exactly: the byte hashes of every repository file
(excluding nothing - no ignored receipt is written, so this is a true
byte-for-byte claim), HEAD, the index, and the complete `git status` output.

### Continuity Manifest File (frozen, corrected mandatory members)

A JSON control file at the frozen path
`.cvf/runtime/tranche-continuity/<full-material-sha>.json` (ignored, never
staged or committed). `--continuity-manifest <path>` must resolve to exactly
that location; a mismatched SHA filename or a path outside that directory
fails closed (`MANIFEST_SHA_MISMATCH`, `MANIFEST_PATH_OUTSIDE_RUNTIME_DIRECTORY`).

Shape: `{"schemaVersion": "cvf.gc020ContinuityManifest.v1", "paths": [...]}`,
an ordered array of repo-root-relative POSIX-style strings.

Path-level rules, each a named validation failure naming the exact path:
`NON_SESSION_SYNC_PATH_REJECTED`, `PATH_TRAVERSAL_REJECTED`,
`DUPLICATE_MANIFEST_PATH`, `MANIFEST_PATH_NOT_FOUND`.

Forbidden entries, each `GENERATED_OUTPUT_MUST_NOT_BE_MANIFESTED` naming the
exact path: `CVF_SESSION/ACTIVE_SESSION_STATE.json` and
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` - both are generated,
never caller-authored.

Mandatory members, `paths` must include exactly once (a missing one is
`MANIFEST_MISSING_REQUIRED_MEMBER`, with the member class carried in
`diagnosticDetails`, never interpolated into the code string itself):

1. the current active root handoff, resolved per Active Handoff Handling below;
2. `CVF_SESSION_MEMORY.md`;
3. `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
4. `CVF_SESSION/state/entries/nextAllowedMove.json`;
5. at least one additional closure/dispatch state entry under
   `CVF_SESSION/state/entries/`, distinct from `nextAllowedMove.json`.

### Active Handoff Handling (frozen, corrected pre/post-generation authority)

Before generation runs, `CVF_SESSION/ACTIVE_SESSION_STATE.json` and its
bootstrap model are intentionally stale relative to the caller's not-yet-
generated edits, so Phase 2 must never resolve the intended handoff from
either generated file pre-generation. Phase 2 instead reads the candidate
`activeHandoff` directly from
`CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`, validates it names exactly
one existing root `AGENT_HANDOFF*.md` file, and requires the manifest's
handoff entry to equal that exact path (`STALE_HANDOFF_REJECTED` otherwise).

Phase 1 is unaffected by this and preserves its existing post-material
re-read, because no continuity source edits have occurred yet at that point.

After generation (execute mode only), the helper verifies that the core
source's `activeHandoff`, the freshly generated aggregate, the freshly
generated bootstrap model, and the manifest's handoff entry all agree
(`GENERATED_HANDOFF_DISAGREEMENT` otherwise); any disagreement fails before
the continuity commit.

### Topology Classification (frozen, runs before pending-path validation)

Resolving `ALREADY_SYNCHRONIZED` through the ordinary pending-path invariant is
unreachable, because after a successful continuity commit every manifest path
has zero pending change, which the pending invariant would reject before any
idempotency check runs. Topology must therefore be classified first, and the
pending-path invariant applies only inside one of its branches.

Immediately after parsing arguments, loading the control manifest, and
resolving the active handoff (from `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`,
never from either generated file), classify:

1. `HEAD == materialSha` and `materialSha^ == base`: enter
   `PENDING_OR_RETRY`.
2. `HEAD^ == materialSha` and `materialSha^ == base`: enter
   `POSTCOMMIT_RECHECK`.
3. Anything else: return `CONTINUITY_VALIDATION_FAILED`, create no commit.

### Branch: PENDING_OR_RETRY

This branch covers both a fresh Phase 1 handoff and a retry after any earlier
failure that left partial continuity progress. Both cases are the same
branch, because the recovery invariant (below) already tolerates the
generated residue a partial prior attempt may have left behind.

**Pending invariant (frozen, corrected from strict equality to a bounded
range):**

```
manifestPaths subset-of pendingPaths subset-of (manifestPaths union derivedOutputs)
```

where `derivedOutputs = {CVF_SESSION/ACTIVE_SESSION_STATE.json,
CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json}` and `pendingPaths` is
every currently staged plus unstaged/untracked path, excluding the ignored
runtime control manifest. Concretely:

- every manifest path must have a pending change - a manifest path with none
  is `MANIFESTED_PATH_HAS_NO_PENDING_CHANGE`;
- pending paths may additionally include zero, one, or both derived outputs,
  left over from an earlier partial attempt;
- no other pending path is allowed - anything outside
  `manifestPaths union derivedOutputs` is `UNRELATED_MATERIAL_STAGED` /
  `UNRELATED_MATERIAL_PRESENT`, naming the exact offending path;
- derived outputs remain forbidden as manifest *entries* even though they are
  now tolerated as pending residue; the manifest content rule from Continuity
  Manifest File is unaffected;
- this invariant, and the topology classification before it, apply
  identically in dry-run and execute.

If `--execute` is absent: return `DRY_RUN_CONTINUITY_PLAN_VALIDATED` once the
invariant passes. No generation, staging, marker rewrite, or commit.

In execute mode:

1. Apply the handoff SHA/parent evidence block. This update is idempotent: it
   locates and replaces its own existing evidence block rather than
   appending a duplicate, on both a first attempt and a retry.
2. Run `generate_active_session_state.py --generate`, deterministically
   regenerating both derived outputs from source regardless of any stale
   residual content already present.
3. Verify post-generation agreement between the core source, both generated
   outputs, and the manifest (Active Handoff Handling); fail
   `CONTINUITY_VALIDATION_FAILED` on disagreement.
4. Stage the manifest paths and both derived outputs; verify the final staged
   set equals `manifestPaths union derivedOutputs` exactly and that both
   derived outputs show an actual staged diff (`GENERATED_OUTPUT_UNCHANGED`
   if not). Staged-path-set equality is the normative check; command
   invocation order may be deterministic, but Git index ordering is never
   itself evidence of correctness.
5. Run the three continuity checkers (pre-continuity); failure is
   `CONTINUITY_VALIDATION_FAILED`, no commit.
6. Create the continuity commit. A failure here is `CONTINUITY_COMMIT_FAILED`.

On any failure inside this branch, before or after mutation, do not
automatically reset, unstage, restore, delete, or rewrite unrelated content.
Return the exact recovery state (staged/unstaged/untracked paths, HEAD,
material SHA, diagnostic or failed command) and leave the bounded
manifest/derived changes exactly as they are for a subsequent retry, which
re-enters this same branch and this same pending invariant.

### Branch: POSTCOMMIT_RECHECK

Entered whenever `HEAD` is already the continuity commit for the supplied
material SHA. This branch performs no generation, no staging, no marker
rewrite, and no commit - in dry-run or execute alike; `--execute` never
authorizes mutation here.

1. Require a clean worktree and empty staging.
2. Verify `HEAD` changed exactly the manifest paths plus both derived
   outputs, no other path.
3. Verify both derived outputs match their generated sources (no drift).
4. Verify the active handoff is the resolved one and its evidence block
   contains the exact supplied material SHA.
5. Rerun the three continuity checkers against the current committed state.
6. If all of 1-5 pass: return `ALREADY_SYNCHRONIZED`.
7. If any fail: return `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`. This is the
   only way that state is produced; it never falls through to
   `PENDING_OR_RETRY` and never creates a second commit.

### Phase 1 - MATERIAL

1. Validate arguments; reject forbidden/legacy options.
2. Validate the staged material manifest and unrelated-change absence.
3. If `--execute` is absent: return `DRY_RUN_MATERIAL_VALIDATED`, no mutation.
4. Run the narrow material preflight (only now, in execute mode).
5. Commit material once. A failure before any commit exists is
   `MATERIAL_VALIDATION_FAILED` (dry-run or execute); a failure in the commit
   operation itself is `MATERIAL_COMMIT_FAILED`.
6. Capture the full material SHA; re-resolve the active handoff (preserved
   behavior - Phase 1 is unaffected by Topology Classification, since no
   continuity commit can exist yet at this point).
7. Return `MATERIAL_COMMITTED_CONTINUITY_PENDING` with a `resumeArgvTemplate`.

Never requires or predicts the future continuity SHA.

### Between phases

The caller authors the manifest paths using the known material SHA, including
rotating `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json::activeHandoff` if
needed, then writes the ignored control manifest at its frozen location. The
helper invents no semantic content and never hand-edits either derived
output.

### Phase 2 - CONTINUITY RESUME (entry sequence)

1. Parse `--resume-material-sha` (40 hex chars) and load/validate the control
   manifest (location, schema, path rules, mandatory members).
2. Resolve the active handoff per Active Handoff Handling; reject a stale
   one.
3. Classify topology (above). Anything outside the two named cases is
   `CONTINUITY_VALIDATION_FAILED`, no commit.
4. Dispatch to `PENDING_OR_RETRY` or `POSTCOMMIT_RECHECK` per the
   classification.

A continuity failure at any step never amends, resets, or recreates the
material commit.

### Recovery Output By Branch (frozen)

`resumeArgvTemplate` always reflects the branch the failure occurred in, not
a generic template:

| Terminal state | Branch | Resume action the template targets |
|---|---|---|
| `MATERIAL_COMMITTED_CONTINUITY_PENDING` | (from Phase 1) | resume Phase 2 normally; enters `PENDING_OR_RETRY` |
| `CONTINUITY_VALIDATION_FAILED` while `HEAD == materialSha` | `PENDING_OR_RETRY` | retry the same `PENDING_OR_RETRY` invocation |
| `CONTINUITY_COMMIT_FAILED` | `PENDING_OR_RETRY` | retry `PENDING_OR_RETRY` with the existing staged batch intact |
| `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED` while `HEAD^ == materialSha` | `POSTCOMMIT_RECHECK` | invoke `POSTCOMMIT_RECHECK`; this never creates another commit even if the printed template carries `--execute` |

The same resume argv template may carry `--execute` in every row; topology
classification takes precedence over the flag, so `--execute` inside
`POSTCOMMIT_RECHECK` never authorizes mutation. Every failure output
truthfully reports current `stagedPaths`, `unstagedPaths`, `untrackedPaths`,
`currentHead`, `materialSha`, and the diagnostic or failed-command state at
the moment of failure - never a stale or predicted value.

### Deterministic Terminal States (frozen, closed enum)

| Terminal state | Meaning | Exit |
|---|---|---|
| `ARGUMENT_VALIDATION_FAILED` | `--mode` missing/invalid, forbidden/legacy option, malformed value | `2` |
| `DRY_RUN_MATERIAL_VALIDATED` | material dry-run validation passed | `0` |
| `MATERIAL_VALIDATION_FAILED` | material validation failed before any commit, in dry-run or execute | `1` |
| `MATERIAL_COMMIT_FAILED` | the material commit operation itself failed | `1` |
| `MATERIAL_COMMITTED_CONTINUITY_PENDING` | material committed; continuity authoring is owed by the caller | `0` |
| `DRY_RUN_CONTINUITY_PLAN_VALIDATED` | `PENDING_OR_RETRY` dry-run validation passed | `0` |
| `CONTINUITY_VALIDATION_FAILED` | topology unclassifiable, or `PENDING_OR_RETRY` rejected the manifest/handoff/pending-range, or a pre-commit check failed | `3` |
| `CONTINUITY_COMMIT_FAILED` | the continuity commit operation itself failed | `4` |
| `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED` | `POSTCOMMIT_RECHECK` found a disagreement after the commit already exists | `5` |
| `COMPLETE_ONE_MATERIAL_ONE_CONTINUITY` | one material and one continuity commit exist; all postconditions passed | `0` |
| `ALREADY_SYNCHRONIZED` | `POSTCOMMIT_RECHECK` passed all six checks | `0` |

A commit that succeeded followed by a failed post-commit check is always
`CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`, never `CONTINUITY_COMMIT_FAILED`.
Every invocation, including argument failures, ends with exactly one Terminal
Output JSON object.

### Terminal Output Schema (frozen)

```json
{
  "schemaVersion": "cvf.gc020TerminalOutput.v1",
  "terminalState": "MATERIAL_COMMITTED_CONTINUITY_PENDING",
  "materialSha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "currentHead": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "activeHandoff": "AGENT_HANDOFF_V60_2026-09-08.md",
  "stagedPaths": [],
  "unstagedPaths": [],
  "untrackedPaths": [],
  "failedCommand": null,
  "diagnosticCode": null,
  "diagnosticDetails": null,
  "resumeArgvTemplate": ["python", "scripts/cvf_commit_tranche.py", "--mode", "resume", "--resume-material-sha", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "--base", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "--continuity-manifest", ".cvf/runtime/tranche-continuity/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json", "--continuity-message", "<continuityCommitMessage>", "--execute"],
  "resumeCommand": null
}
```

Field rules:

- `terminalState`: one of the eleven frozen values.
- `activeHandoff` is the resolved active handoff path once handoff resolution
  succeeded. It is `null` only when handoff resolution itself is what failed;
  in that case the failure's `diagnosticCode` names the resolution failure.
- `failedCommand`: `null` unless a subprocess (checker, generator, `git
  commit`) failed, then its exact argv array.
- `diagnosticCode`: `null` on non-failure states and on raw subprocess
  failures. On a semantic validation failure, a stable enum-like token only
  (for example `MANIFEST_MISSING_REQUIRED_MEMBER`,
  `STALE_HANDOFF_REJECTED`, `UNRELATED_MATERIAL_STAGED`,
  `GENERATED_HANDOFF_DISAGREEMENT`) - never a string with an interpolated
  dynamic value.
- `diagnosticDetails`: `null` unless `diagnosticCode` is set; then a JSON
  object carrying the dynamic values for that failure. Exactly one of
  `failedCommand` / `diagnosticCode` is non-null on any failure state; all
  three failure fields are `null` on any non-failure state.
- `resumeArgvTemplate`: `null` except on `MATERIAL_COMMITTED_CONTINUITY_PENDING`,
  `CONTINUITY_VALIDATION_FAILED`, `CONTINUITY_COMMIT_FAILED`, and
  `CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`, per Recovery Output By Branch
  above. Identity arguments are concrete once known; `--continuity-message`
  stays the literal placeholder `"<continuityCommitMessage>"` when unknown.
  Never predicts a future continuity SHA.
- `resumeCommand`: `null` in machine output. A human-readable rendering MAY be
  emitted separately, labelled for exactly one named shell; no string is ever
  claimed portable across POSIX and PowerShell.

### Manifest Control-File Path (frozen, corrected)

`--continuity-manifest <path>` must be a repo-relative POSIX-style path
exactly matching `.cvf/runtime/tranche-continuity/<materialSha>.json`. An
absolute path is rejected (`MANIFEST_PATH_MUST_BE_REPO_RELATIVE`) even when it
resolves into that same directory; a path outside the directory is
`MANIFEST_PATH_OUTSIDE_RUNTIME_DIRECTORY`; a traversal segment is
`PATH_TRAVERSAL_REJECTED`; a filename SHA mismatch is
`MANIFEST_SHA_MISMATCH`.

### Active Handoff Validation (frozen, corrected)

The resolved active handoff must satisfy all of: it exists as a root
`AGENT_HANDOFF*.md` file; it declares `Status: ACTIVE`; it is the unique such
root handoff (no ambiguity between multiple candidates); and it exactly
matches both the `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json::activeHandoff`
value and the manifest's handoff entry. Any mismatch among these three
sources, or failure of any individual condition, is `STALE_HANDOFF_REJECTED`
or a more specific named diagnostic, never a silent pass.

### Topology Rules (frozen)
Material parent equals `--base` exactly. Continuity parent equals the full
material SHA exactly. A successful first run creates exactly one of each
commit. A failed resume never amends, resets, force-pushes, or recreates the
material commit; it is permanent once
`MATERIAL_COMMITTED_CONTINUITY_PENDING` is printed.

### SHA truthfulness and failure reporting

Use the full material SHA wherever required; never substitute the abbreviated
form; never require any surface to predict its own future SHA. The GC-020
session-sync-only parent-SHA allowance is preserved unchanged. Every failure
prints the Terminal Output Schema with the correct `terminalState`, exactly
one of `failedCommand`/`diagnosticCode` (plus `diagnosticDetails` when
applicable), and a `resumeArgvTemplate` when applicable. Never leaks an
unhandled `CalledProcessError`; never uses `--no-verify` or any bypass flag;
never automatically resets, amends, force-pushes, or deletes files.

## Focused Case Matrix

Focused test names, grouped by category, each using an isolated temporary
repository. No test may commit into this provenance repository.

**Mode/argument (13):** `test_missing_mode_returns_argument_validation_failed`, `test_invalid_mode_value_returns_argument_validation_failed`, `test_material_mode_rejects_resume_only_arguments`, `test_resume_mode_rejects_material_only_arguments`, `test_both_modes_reject_handoff_message_flag`, `test_both_modes_reject_handoff_summary_flag`, `test_both_modes_reject_allow_unstaged_flag`, `test_both_modes_reject_skip_preclosure_flag`, `test_resume_material_sha_must_be_exactly_40_hex_characters`, `test_execute_is_optional_in_material_mode`, `test_execute_is_optional_in_resume_mode`, `test_continuity_message_optional_in_resume_dry_run`, `test_continuity_message_required_in_resume_execute`.

**Dry-run non-mutation, corrected (8):** `test_material_dry_run_returns_dry_run_material_validated`, `test_material_dry_run_does_not_invoke_autorun_gate`, `test_material_dry_run_writes_no_autorun_receipt`, `test_material_dry_run_preserves_all_file_byte_hashes_head_index_and_status`, `test_resume_dry_run_returns_dry_run_continuity_plan_validated`, `test_resume_dry_run_does_not_invoke_generator_or_autorun_gate`, `test_resume_dry_run_does_not_stage_any_path`, `test_resume_dry_run_preserves_all_file_byte_hashes_head_index_and_status`.

**Phase 1 (8):** `test_phase1_writes_full_material_sha_not_short_sha`, `test_phase1_returns_material_committed_continuity_pending`, `test_phase1_resume_argv_template_carries_full_sha_and_base`, `test_phase1_does_not_require_or_predict_future_continuity_sha`, `test_material_validation_failure_in_dry_run_or_execute_returns_material_validation_failed`, `test_material_commit_operation_failure_returns_material_commit_failed`, `test_active_handoff_is_reresolved_after_material_commit`, `test_handoff_rotation_targets_the_current_active_handoff`.

**Manifest location/schema (3):** `test_continuity_manifest_must_be_under_frozen_runtime_directory`, `test_continuity_manifest_control_file_is_never_staged_or_committed`, `test_continuity_manifest_is_a_json_file_not_inline_cli_value`.

**Manifest content, corrected ownership (13):** `test_continuity_manifest_rejects_non_session_sync_path`, `test_continuity_manifest_rejects_path_traversal`, `test_continuity_manifest_rejects_duplicate_path`, `test_continuity_manifest_rejects_missing_on_disk_path`, `test_continuity_manifest_rejects_generated_aggregate_entry`, `test_continuity_manifest_rejects_generated_bootstrap_entry`, `test_continuity_manifest_requires_active_root_handoff_member`, `test_continuity_manifest_requires_session_memory_member`, `test_continuity_manifest_requires_core_source_member`, `test_continuity_manifest_requires_next_allowed_move_member`, `test_continuity_manifest_requires_additional_state_entry_member`, `test_continuity_manifest_missing_member_sets_diagnostic_details_member_class`, `test_continuity_manifest_preserves_declared_path_order_when_staging`.

**Manifest control-file path, corrected (4):** `test_continuity_manifest_must_be_repo_relative_not_absolute`, `test_continuity_manifest_absolute_path_rejected_even_inside_runtime_directory`, `test_continuity_manifest_filename_must_match_material_sha_exactly`, `test_continuity_manifest_outside_runtime_directory_fails_closed`.

**Active handoff authority, corrected (7):** `test_phase2_resolves_handoff_from_core_source_not_stale_aggregate`, `test_rotation_via_core_source_is_accepted_before_generation`, `test_resume_rejects_stale_handoff_not_currently_active`, `test_active_handoff_must_declare_status_active`, `test_active_handoff_must_be_unique_root_handoff`, `test_post_generation_verifies_core_aggregate_bootstrap_and_manifest_agree`, `test_generated_handoff_disagreement_fails_before_continuity_commit`.

**Topology classification, new (4):** `test_topology_classification_runs_before_pending_path_validation`, `test_head_equals_material_sha_enters_pending_or_retry`, `test_head_parent_equals_material_sha_enters_postcommit_recheck`, `test_unclassifiable_topology_returns_continuity_validation_failed`.

**PENDING_OR_RETRY pending invariant, corrected from strict equality to a bounded range (7):** `test_every_manifest_path_must_have_pending_change`, `test_extra_pending_path_outside_manifest_and_derived_outputs_fails_closed`, `test_one_derived_output_pending_from_partial_retry_is_tolerated`, `test_both_derived_outputs_pending_from_partial_retry_is_tolerated`, `test_derived_outputs_remain_forbidden_as_manifest_entries_even_when_tolerated_as_residue`, `test_pending_invariant_applies_identically_in_dry_run_and_execute`, `test_third_unrelated_residual_path_is_rejected`.

**Retry and idempotent handoff update, new (7):** `test_retry_after_aggregate_written_bootstrap_generation_failed`, `test_retry_after_both_outputs_generated_precommit_checker_failed`, `test_retry_after_all_paths_staged_git_commit_failed`, `test_retry_with_mixed_staged_and_unstaged_manifest_and_derived_paths`, `test_regeneration_overwrites_manually_stale_derived_residual_content`, `test_retry_reaches_exactly_one_continuity_commit`, `test_handoff_evidence_update_is_idempotent_replaces_not_duplicates_on_retry`.

**Generator/postcondition ordering (5):** `test_resume_runs_generator_generate_before_staging_outputs`, `test_resume_stages_manifest_and_both_derived_outputs_set_equality_not_order`, `test_resume_runs_three_checks_before_continuity_commit`, `test_resume_reruns_three_checks_after_continuity_commit`, `test_postcommit_check_failure_returns_continuity_postcommit_validation_failed_not_commit_failed`.

**Topology (4):** `test_post_continuity_asserts_head_parent_is_material_sha`, `test_post_continuity_asserts_material_parent_is_closure_base`, `test_session_only_commit_may_cite_material_parent_sha`, `test_final_worktree_and_staging_are_clean`.

**Failure/diagnostics/no-cleanup, corrected (12):** `test_continuity_validation_failure_sets_diagnostic_code_and_details_not_failed_command`, `test_continuity_commit_failure_sets_failed_command_argv`, `test_exactly_one_of_failed_command_or_diagnostic_code_is_set_on_failure`, `test_all_three_failure_fields_null_on_success`, `test_active_handoff_null_only_when_resolution_itself_failed`, `test_continuity_failure_does_not_amend_or_reset_material_commit`, `test_failure_does_not_automatically_reset_unstage_restore_or_delete_pending_content`, `test_bounded_manifest_and_derived_changes_remain_available_for_retry_after_failure`, `test_argument_validation_failed_exit_code_is_two`, `test_continuity_validation_failed_exit_code_is_three`, `test_continuity_commit_failed_exit_code_is_four`, `test_continuity_postcommit_validation_failed_exit_code_is_five`.

**POSTCOMMIT_RECHECK branch, new (7):** `test_postcommit_recheck_requires_clean_worktree_and_staging`, `test_postcommit_recheck_verifies_head_changed_exactly_manifest_plus_derived_outputs`, `test_postcommit_recheck_verifies_derived_outputs_match_source`, `test_postcommit_recheck_verifies_handoff_evidence_contains_material_sha`, `test_postcommit_recheck_reruns_continuity_checkers`, `test_postcommit_recheck_all_pass_returns_already_synchronized`, `test_postcommit_recheck_execute_flag_never_creates_a_second_commit`.

**Idempotency reachability, corrected (5):** `test_clean_post_commit_tree_reaches_already_synchronized`, `test_clean_tree_with_unrelated_head_is_not_already_synchronized`, `test_wrong_committed_path_set_is_not_already_synchronized`, `test_already_synchronized_creates_no_commit`, `test_postcommit_failure_then_later_pass_returns_already_synchronized_without_new_commit`.

**Recovery output by branch, new (4):** `test_material_committed_pending_resume_argv_enters_pending_or_retry`, `test_continuity_validation_failed_resume_argv_retries_pending_or_retry`, `test_continuity_commit_failed_resume_argv_retries_with_existing_staged_batch`, `test_postcommit_validation_failed_resume_argv_invokes_postcommit_recheck_only`.

**Resume argv and shell labelling (4):** `test_resume_argv_template_is_json_array_one_argument_per_element`, `test_resume_argv_template_handles_spaces_and_non_ascii_without_shell_parsing`, `test_resume_argv_template_never_contains_a_future_continuity_sha`, `test_human_readable_resume_rendering_is_labelled_with_exactly_one_shell`.

**Hook/bypass (2):** `test_no_no_verify_flag_is_ever_used`, `test_no_preflight_or_hook_is_bypassed_by_any_flag`.

## 8. Execution Plan

1. Capture execution identity, verify pins, run pre-implementation.
2. Implement Phase 1 material, the terminal-state vocabulary, and the explicit
   Phase 2 continuity resume mode in the existing helper.
3. Add the focused cases above over isolated temporary repositories, asserting
   command ordering and post-commit execution.
4. Update the Step 4A helper contract after the focused proof passes.
5. Write the worker return last, rerun gates, leave staging empty.

### Worker Trace Requirement

The worker return must carry a complete Agent Operation Trace Block including
`Deletion or rename disposition` and `git diff --name-status` diff evidence.

## 9. Evidence Requirements

Return exact start and final HEAD, full status, staging state, recomputed
hashes, focused counts, Python size result, the worker-return fast result, the
exact four-path manifest, and explicit no-commit and no-external-effect
evidence. Confirm that no test committed into this provenance repository.

## 10. Acceptance Criteria

All focused cases pass; the Python size guard passes with no touched near-hard
growth; the changed set is exactly four paths; staging is empty; the preserved
post-material handoff re-read is documented as preserved rather than added; the
transaction is resumable after material success; dry-run performs zero
mutation in either mode, including no autorun receipt write; the manifest
correctly excludes both generated outputs
(`CVF_SESSION/ACTIVE_SESSION_STATE.json` and
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`) and requires the five
frozen caller-authored members; the active handoff is resolved from
`CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` before generation and
cross-checked against both generated outputs after generation; topology is classified into exactly `PENDING_OR_RETRY` or
`POSTCOMMIT_RECHECK` before any pending-path validation runs, so
`ALREADY_SYNCHRONIZED` is actually reachable through a clean post-commit tree;
inside `PENDING_OR_RETRY` the pending invariant is the bounded range
`manifestPaths subset-of pendingPaths subset-of (manifestPaths union
derivedOutputs)`, never a strict equality that would deadlock a legitimate
retry against generated residue, and derived outputs remain forbidden as
manifest entries even while tolerated as pending residue; the handoff
evidence updater is idempotent on retry, replacing rather than duplicating
its block; every emitted terminal state matches the frozen eleven-value enum,
its exit code, and the frozen Terminal Output Schema exactly, with
`diagnosticCode` as a stable token and dynamic values only in
`diagnosticDetails`; a post-commit check failure is reported as
`CONTINUITY_POSTCOMMIT_VALIDATION_FAILED`, never `CONTINUITY_COMMIT_FAILED`,
is produced only by the `POSTCOMMIT_RECHECK` branch, and also carries a
`resumeArgvTemplate` whose branch-specific retry action matches Recovery
Output By Branch; no failure automatically resets, unstages, restores, or
deletes pending content; post-continuity checks rerun against the final
committed state; no future-SHA requirement exists; the manifest control-file
path is rejected when absolute even inside the runtime directory; the active
handoff validation requires `Status: ACTIVE`, uniqueness, and agreement across
core source, manifest, and resolution; the CLI mode argument, the continuity
manifest's frozen control-file location and content rules, and the
resumeArgvTemplate contract match this packet exactly with no
worker-invented alternative; and the reviewer can evaluate the return without
recreating implementation.

## 11. Review Gate

Reviewer applies `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`.
Bounded reruns require a named contradiction, expected information gain and a
cost reason.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_COMPLETION_2026-09-08.md` (create only if machine closure or a material reviewer finding requires it) |
| reviewerOwnedClosurePaths | the exact four worker paths plus bounded in-scope repairs; session surfaces only in a separate continuity commit |
| closureOwner | internal orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator request on 2026-09-08 to resume deterministic GC-020 post-commit SHA synchronization as its own bounded packet |
| scope classification | bounded blast radius: exactly four allowed-scope changed paths, one existing helper owner plus its first focused test file |
| risk sensitivity | moderate; the helper performs commits, so hook bypass, destructive recovery and provider/live/public/deploy actions are all forbidden and no production readiness is claimed |
| selected role route | route mode `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | dispatcher authors, internal no-commit worker implements, reviewer/closer accepts and commits |
| escalation condition | worker must stop and return `BLOCKED_WITH_REASON` on any fifth path, hook or autorun expansion need, session-state checker change, or operator checkpoint |
| externalAgentDisposition | NOT_ROUTED_EXTERNAL; external invocation remains unauthorized for this packet |
| adapterBoundary | no adapter, CLI or MCP surface is opened by this tranche |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this tranche hardens one existing reviewer-local
commit helper and its documented contract. It absorbs no legacy corpus, opens no
foundation or workflow-chain plane, and adds no coverage-index row.

## Evidence Requirements

Return exact start and final HEAD, full status, staging state, recomputed
hashes, focused counts, the governed Python size result, the worker-return fast
result, the exact owned-path manifest, and explicit no-commit and
no-external-effect evidence.

## Closure Checklist

- [ ] all focused cases pass
- [ ] prior suites for the owned surfaces pass
- [ ] governed Python size guard passes with no touched near-hard growth
- [ ] changed set matches the Required Artifact Manifest exactly
- [ ] staging is empty and no commit was made by the worker
- [ ] worker return carries complete packet-shape evidence
- [ ] reviewer accepts before any commit

## Operator Checkpoint

The operator authorized this exact bounded packet on 2026-09-08. Any scope
expansion, hook or autorun wiring, registry mutation, provider/live/public or
deployment step requires a fresh operator checkpoint before it may proceed.

## External Knowledge Intake Routing

| Row | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external input was received or consumed while authoring this packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | N/A with reason: no external material entered this tranche |
| Disposition | N/A with reason: nothing to absorb, adapt, defer or reject |
| Claim boundary | all inputs were repository-local governed surfaces read at the dispatch base |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationImpact | NOT_APPLICABLE_WITH_REASON: this tranche hardens one existing reviewer-local helper and adds its first test file; it creates, splits, relocates or refactors no durable governance foundation file |
| storageLocation | no durable governance foundation file is created, split, relocated or refactored |
| indexUpdateDisposition | NOT_APPLICABLE_WITH_REASON: no foundation index row is added or moved |
| claimBoundary | records storage-layout impact only; asserts no runtime or retrieval behavior |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order | this packet | dispatch-quality gate result | PENDING_WORKER_RETURN |
| Paired baseline | the paired GC-018 baseline | dispatch-quality gate result | PENDING_WORKER_RETURN |
| Owned implementation | Required Artifact Manifest rows | focused suite counts | PENDING_WORKER_RETURN |
| Worker return | the packet worker-return path | worker-return fast gate result | PENDING_WORKER_RETURN |
| Roadmap row | N/A with reason: no roadmap row is opened | N/A with reason | NOT_APPLICABLE |
| Registry JSON/MD | N/A with reason: no registry is mutated | N/A with reason | NOT_APPLICABLE |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | NOT_APPLICABLE |
| Loop interlock | N/A with reason: no interlock edge added | N/A with reason | NOT_APPLICABLE |

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

## Semantic Convergence And Escalation Control

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "gc020-post-commit-synchronization-t1",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "GC020-SYNC-T1-DISPATCH-PACKET", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/baselines/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_2026-09-08.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

This packet is dispatch documentation only. It authorizes work and carries no
executable proof of its own; the worker return supplies that proof.

## Review-Dispatch Convergence Control

Review-Dispatch Convergence Control: REQUIRED

- dispatchKind: INITIAL
- dispatchSurface: INTERNAL_AGENT
- parentAssignmentId: GC020-SYNC-T1
- reviewRoundCount: 0
- priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
- dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
- reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
- newIndependentCriticalEvidence: NONE
- regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
- cumulativeExternalInvocationCount: 0
- externalInvocationCeiling: 0
- usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
- quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
- nextDispatchDisposition: INITIAL_DISPATCH
- rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
- reworkGeneration: 0
- consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
- successorTrancheOpened: NO
- implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
- preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
- preExecutionReviewTrigger: NONE
- nextRoutineReviewBoundary: WORKER_RETURN
- reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION
- latencyDisposition: BOUNDED_LOCAL_AUTHORING
- avoidableDelayClass: NONE_OBSERVED

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: <!--archive-name-exception-->`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> internal no-commit worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`39be75a7cff4fc9acdbf3dd129254ddb164947d0`; executionBaseHead=captured by the worker at its actual start; closureBaseHead=set by the reviewer |
| changedSetScope(phase) | dispatch pair now; the exact owned paths during execution; material then continuity at closure |
| traceScope(phase, actor) | each actor records only its phase-local changes and inherited concurrent HEAD movement separately |
| commitOwner(phase) | reviewer/closer for accepted material; session-sync steward for continuity; worker commit forbidden |
| crossBatchIsolation | explicit lane handoff with dispatcher mutation forbidden on worker-owned paths while the lane is active |
| sharedWorktreeCoordinationMode | `EXPLICIT_LANE_HANDOFF` |
| activeLaneOwner | GC020-SYNC-T1 internal no-commit worker from execution anchor capture until returned status evidence |
| laneOwnedPaths | exactly the Required Artifact Manifest paths |
| dispatcherMutationBoundary | `NO_MUTATION_WHILE_LANE_ACTIVE` |
| laneReleaseEvidence | worker return records final full status and empty staging; reviewer explicitly accepts control before any isolation or commit |
| nextMoveSurfaces | reviewer disposition, material commit, then separate active continuity projection |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author (packet authoring only) |
| Provider or surface | local workspace; no provider or network surface used |
| Session or invocation | GC020-SYNC-T1 dispatch authoring, 2026-09-08 |
| Working directory | repository root |
| Command or tool surface | local file authoring; `git`; local `governance/compat` checkers |
| Target paths | this work order, its paired baseline and the dispatch-author return |
| Allowed scope source | operator authorization on 2026-09-08 for two separate bounded packets |
| Before status evidence | clean worktree; `git status --short` empty; empty staging at `39be75a7cff4fc9acdbf3dd129254ddb164947d0` |
| After status evidence | five pending documentation paths; staging empty; HEAD unchanged |
| Diff evidence | `git diff --name-status` and `git status --short --untracked-files=all` recorded in the dispatch-author return |
| Approval boundary | packet authoring only; no implementation, staging or commit |
| Claim boundary | authorizes bounded work; claims no implementation or runtime behavior |
| Agent type | dispatch author |
| Invocation ID | cvf-gc020-sync-t1-dispatch-authoring-2026-09-08 |
| Expected manifest | five documentation paths |
| Actual changed set | five documentation paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | no deletion, rename or path move occurred |

## Current Runtime Freshness Verification

Verified at dispatch base `39be75a7cff4fc9acdbf3dd129254ddb164947d0` on
2026-09-08 by direct source read. Every owner line count, absent-path claim and
registry classification in this packet was recomputed at that base rather than
carried from an earlier session. No runtime, provider or live surface was
contacted.

## Verification Commands

```powershell
$executionBaseHead = git rev-parse HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python -m pytest scripts/test_cvf_commit_tranche.py -q
python governance/compat/check_python_automation_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GC020_POST_COMMIT_SHA_SYNCHRONIZATION_T1_WORKER_RETURN_2026-09-08.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; Public Export Disposition; executionBaseHead; git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for every non-applicable conditional block.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"GC020-SYNC-T1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["scripts","docs/reference","docs/reviews","docs/baselines","docs/work_orders","governance/compat"],"claims":["deterministic post-material SHA synchronization for the tranche commit helper"],"requiredProof":["full-material-SHA case","postcondition execution cases","fail-closed staged-path case","deterministic recovery case","focused tests","independent review"],"operatorCheckpoints":["scope expansion","hook or autorun change","runtime or external effect"],"forbiddenEffects":["template or scaffold growth","hook or autorun wiring","runtime or provider execution","public sync","worker commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named control cluster","completenessClaimChanged":false}}
```

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

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_active_session_state.py`; `governance/compat/check_next_move_freshness.py`; `governance/compat/generate_active_session_state.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `HEAD_LINE_RE`; `_short_head`; `_active_handoff_path`; `_replace_handoff_head`; `_run_preclosure`; GC-020 tokens `head_sha_in_handoff`, `parent_sha_in_handoff` and `handoff_sync_commit_only`; generator flags `--generate` and `--check`; size class `python_cli_orchestrator` |
| gateRunPurpose | confirm this packet pair satisfies dispatch-quality, scaffold-provenance, size and structural gates before worker dispatch |
| claimBoundary | records consulted checker sources and literal tokens only; asserts no worker gate result |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic post-material synchronization for one commit helper, plus its first focused tests and contract documentation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-dispatch autorun receipt recorded by the dispatch author |
| actionEvidence | ACTION_EVIDENCE_PRESENT - packet pair authored and validated at dispatch base |
| invocationBoundary | zero external, provider, live or network invocations |
| interceptionBoundary | no Git or filesystem interception is implemented or claimed; the helper instructs rather than repairs |
| claimLanguage | bounded helper claims only; no speed, cost, quota, readiness or production language |
| forbiddenExpansion | no hook, autorun, registry, template, scaffold, session-checker or encoding-gate mutation; no fifth path |

## Review-Cost Telemetry

- rootCauseClusterId: GC020-POST-COMMIT-SYNCHRONIZATION
- reworkGeneration: 0
- consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
- productionBindingEvidence: none; repository-local reviewer helper only
- adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
- successorTrancheOpened: NO
- implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
- internalAgentInvocationCount: 0
- externalAgentInvocationCount: 0
- providerCallCount: 0
- tokenOrQuotaUsage: 0
- terminalReadinessVerdict: READY_FOR_REVIEW
- reviewerWorkBoundary: reviewer owns acceptance, bounded in-scope repair and all commits

## 13. Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any required fifth path, source contradiction,
maintainability violation, registry mutation need, hook or autorun change, or
any case where deterministic synchronization cannot be achieved without
expanding scope.

## Rollback Boundary

Revert only accepted GC020-SYNC-T1 material: the helper, its new test file, the
choreography standard and the packet worker return. Preserve every other lane
and commit.

## Claim Boundary

This packet authorizes one bounded commit-helper hardening tranche. It claims no
implementation completion, no measured speed, cost or quota reduction, no hook
or autorun change, no encoding-gate change, and no public-sync, deployment or
production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private provenance dispatch material. No public-sync artifact or public claim is
authorized by this work order.
