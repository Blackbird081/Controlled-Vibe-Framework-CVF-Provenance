# CVF Tranche Commit Choreography Standard

Memory class: POINTER_RECORD

Status: ACTIVE_STANDARD

docType: reference

Date: 2026-06-03

Authority: operator finding after CI2-T1 closure friction

---

## Purpose

Define the required commit choreography for governed CVF tranches so archive
hygiene, artifact implementation, closure transition, session state, and active
handoff sync do not collide in one oversized or ambiguous commit range.

This standard converts the CI2-T1 closure friction into a reusable workflow
rule before CI2-T2 checker work begins.

Dependency-release evidence is governed by:

`docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md`

---

## Scope

This standard applies to any governed tranche, work order, roadmap task,
reviewer closure, archive hygiene batch, guard-maintenance batch, or session
sync batch that:

- touches active work orders, roadmaps, reviews, baselines, session state, or
  handoff files;
- runs autorun workflow gates;
- changes more than 40 files;
- changes `governance/compat/*`;
- closes a tranche and opens the next ordered tranche;
- uses `WORKER_MUST_NOT_COMMIT`.

It is especially binding for CI2-T2 and later Corpus Intelligence enforcement
work, because those tranches edit guard/checker code and will otherwise be
vulnerable to range bleed from archive or session commits.

---

## Root Cause Lessons

| Root cause | Required control |
| --- | --- |
| Archive script creates large unstaged diff | Run archive hygiene as a separate pre-session batch, or explicitly split archive deletion/copy/reference commits before tranche work. |
| Large-scope authorization must be in the same commit | Stage the authorization review in the same commit as the large-scope change it authorizes. A prior commit is not enough. |
| Windows decoding can break checker subprocess output | Governance scripts that read git output must use UTF-8 with replacement for non-ASCII bytes. |
| Archived review files can trigger active corpus checks | Corpus/path checkers must exclude archive paths unless the archive batch explicitly reopens them. |
| Stale dispatch base expands closure range | Use the worker-captured `executionBaseHead` for worker validation and reviewer-captured `closureBaseHead` for closure, not an old dispatch base after unrelated commits. |
| Session mode must exist in JSON and front door | Any mode/next-move change must update both `CVF_SESSION/ACTIVE_SESSION_STATE.json` and `CVF_SESSION_MEMORY.md` in the same authorized session commit. |
| Handoff HEAD cannot be known before commit | Expect a dedicated handoff-sync-only commit after material/session commits. |
| Next work order released from HOLD with stale prerequisite placeholders | Before marking the next work order READY/DISPATCH_READY, replace `REQUIRED` or `after closure` dependency rows with artifact path plus closure commit evidence, and refresh base anchors. |

---

## Required Commit Sequence

### Step 0 - Archive Hygiene Preflight

Before starting tranche implementation, check whether archive hygiene or stale
active-doc cleanup is already pending.

If archive hygiene is needed:

1. run the archive batch before tranche work;
2. create or update the large-scope authorization review in the same commit as
   the large archive diff;
3. keep archive commits separate from tranche artifact commits;
4. rerun active archive hygiene and dispatch-quality gates before continuing.

Do not mix archive hygiene with a tranche implementation commit unless the
work order explicitly owns archive cleanup.

### Step 1 - Worker Artifact Batch

The worker records `executionBaseHead` immediately before material edits:

```powershell
git rev-parse --short HEAD
```

For `WORKER_MUST_NOT_COMMIT`, the worker must leave artifacts pending and must
not claim closure. The worker may claim only component test/gate results that
are valid against the pending working tree.

For `WORKER_MAY_COMMIT`, the worker may commit only owned artifact changes
after tests and gates pass.

### Step 2 - Reviewer Closure Batch

The reviewer or committer captures `closureBaseHead` immediately before the
closure commit. This base must be the actual start of the closure range, not an
old dispatch base that includes unrelated archive or prior tranche commits.

Closure transition may include:

- closing the current work order;
- updating the roadmap row;
- opening the next ordered work order;
- creating the completion review;
- recording committed-range gate evidence.

If protected session or governance files are changed, the authorization review
for those protected changes must be staged in the same commit.

### Step 2A - Dependency Release Refresh

Canonical dependency-release standard:

`docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md`

If the next ordered work order was drafted earlier in `HOLD_*` status, do not
release it by changing only the status line. In the same release batch:

1. replace placeholder dependency evidence such as `after closure`,
   `after Tn closure`, or `Disposition: REQUIRED` with the actual closed
   artifact path and closure commit;
2. set `dispatchBaseHead` to the closure commit or current dispatch anchor;
3. set `executionBaseHead` to `WORKER_MUST_CAPTURE_AT_START` unless the worker
   already captured it after dispatch;
4. keep `closureBaseHead` as `NOT_EXECUTED_YET`;
5. rerun dispatch-quality and pre-dispatch autorun gates before handing the
   packet to a worker.

This is the CI2-T4 to CI2-T5 lesson: a downstream work order must receive the
machine-readable output of the closed tranche, not a prose memory that the
worker is expected to reinterpret.

### Step 3 - Session State Sync Batch

When mode, next allowed move, closed status, or active front-door text changes,
update these together:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- `CVF_SESSION_MEMORY.md`;
- active handoff if the handoff text also needs next-move context;
- a same-commit authorization review if protected paths require it.

This commit may still be followed by a handoff-only sync commit because its
final SHA is not knowable before commit.

### Step 4 - Dedicated Handoff Sync Commit

After any material or session sync commit, run:

```powershell
python governance/compat/check_active_session_state.py --enforce
```

If the active handoff lacks the current HEAD or accepted parent marker, create
a dedicated handoff-sync-only commit. That commit must modify only the active
handoff file unless a new handoff version is being opened under its own
handoff-transition rules.

---

## Base Anchor Rules

| Anchor | Owner | Use |
| --- | --- | --- |
| `dispatchBaseHead` | Orchestrator | dispatch provenance only |
| `executionBaseHead` | Worker | worker edits, pending checks, component tests |
| `closureBaseHead` | Reviewer / committer | committed closure range |
| `handoffSyncParentHead` | Reviewer / committer | parent marker for handoff-sync-only commit |

Rules:

- Do not reuse `dispatchBaseHead` for closure after intervening commits.
- Do not use `--base HEAD --head HEAD` as closure evidence.
- Do not cite `HEAD~1` for a pending artifact.
- Do not claim clean worktree while untracked or modified artifacts remain.
- Do not claim `pre-closure` PASS for `WORKER_MUST_NOT_COMMIT` pending output.
- Do not mark a dependency-gated work order `DISPATCH_READY` while its
  Authority Chain or Source Verification rows still say `REQUIRED` or
  `<prior tranche> after closure`.

---

## Large-Scope Authorization Rule

Any commit that changes more than 40 files, performs archive cleanup, renames or
deletes governed artifacts, or changes protected governance/session files must
include the appropriate authorization review in that same commit.

The authorization review must name:

- scope and target;
- allowed paths or path families;
- reason the large scope is necessary;
- protected paths touched;
- claim boundary;
- finding-to-governance disposition when the batch responds to a repeated
  agent/process defect.

---

## CI2-T2 Binding

CI2-T2 must follow this standard exactly:

1. capture a fresh `executionBaseHead` at worker start;
2. avoid archive cleanup;
3. keep checker implementation, tests, and hook/autorun wiring inside CI2-T2
   allowed scope;
4. leave output pending if worker mode remains `WORKER_MUST_NOT_COMMIT`;
5. reviewer captures a fresh `closureBaseHead` before committing;
6. session sync and handoff sync are separate from the implementation batch.

If CI2-T2 encounters archive hygiene, stale session state, or unrelated
governance drift, it must stop and return that drift to orchestrator instead of
folding it into the checker implementation.

---

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| CI2-T1 closure consumed excessive time due to mixed archive, closure, session, and handoff commits | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | Apply this standard to CI2-T2 and future work orders before implementation |
| Stale dispatch base expanded closure ranges into unrelated commits | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | Work orders must distinguish dispatch, execution, closure, and handoff-sync bases |

---

## Claim Boundary

This standard is an operational commit-sequencing rule. It does not implement a
new machine checker, change runtime behavior, authorize public-sync, authorize
LPCI runtime work, or guarantee semantic correctness of any worker output.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this standard governs private provenance repository workflow,
session-state continuity, archive hygiene, and internal guard operation.
