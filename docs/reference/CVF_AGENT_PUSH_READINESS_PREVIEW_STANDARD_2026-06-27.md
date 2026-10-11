# CVF Agent Push Readiness Preview Standard

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference_standard

Date: 2026-06-27

EPISTEMIC_PROCESS_NA_WITH_REASON: operational sequencing standard; it defines
a local read-only preview step and does not assert empirical runtime,
provider, or public behavior.

## Purpose

Prevent repeated provenance or public push cascades by requiring an early
read-only preview before the full pre-push gate or `git push` attempt. The
preview is a diagnostic step, not a substitute for the canonical pre-push gate.

## Scope / Methodology

Applies when an agent plans to push a governed CVF branch, publish a
public-sync batch, or ask the operator to accept a push-ready state. The agent
must run the preview after material changes are staged enough to inspect, and
again after the final material commit if session-sync work was needed.

Required command:

```powershell
python governance/compat/run_agent_push_readiness_preview.py --base <baseHead> --head HEAD --enforce
```

Upstream backlog policy (operator revision, 2026-10-11): local ahead count is
an advisory disclosure, not an execution or push limit. More than 2 commits
produces WARN with exit 0; --enforce never fails solely because of this count.
Multiple admitted tranches may remain local until an operator-selected sync
checkpoint. No extra authorization, immediate push or stop-new-tranche rule is
required solely for an ahead count, regardless of stack length.

One material commit plus one dedicated continuity commit remains the preferred
shape for a single tranche, not a cap on the whole branch. Preserve separate
tranche ranges and evidence so a later multi-tranche push remains reviewable.
Run the preview at a planned sync checkpoint, before push, or when a concrete
range/continuity issue appears; do not impose a full preview after every pair.
The advisory threshold can be configured with --upstream-ahead-warning;
--upstream-ahead-limit remains a compatibility alias with advisory semantics.

Missing or unreadable upstream state and unreconciled remote commits still fail
push readiness. Hold the dependent push for reconciliation; this is not a ban
on independently authorized local work. Actual scope authorization, protected
paths, generated state, continuity, commit shape and mandatory pre-push checks
remain blocking. Ahead count is neither proof of a malformed stack nor push
authorization.
If the branch intentionally has no upstream tracking branch, use
`--skip-upstream` and record that reason in the closure packet. For final push
evidence, the preview range must be non-stale and must not be confused with the
full gate required by
`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`.

## Required Readout

The preview must report:

- repository remote and upstream tracking branch;
- upstream push-debt status and the local commit count ahead of upstream;
- `git status --short`;
- commit-shape split risk between material paths and protected
  session/handoff paths;
- generated active-session state drift;
- active session, session mode, next-move, core-guard, active-window,
  review-retention, repository-lifecycle, pre-public P3, knowledge-absorption,
  public-doc-drift, governed file-size, and Python automation-size checks;
- diff hygiene.

## Required Operator Discipline

When the preview fails, repair the first actionable local defect before running
the full pre-push gate again. Do not repeatedly call the full pre-push gate to
discover the next marker one at a time.

If the preview reports mixed material and protected session/handoff paths,
split the batch:

1. Commit material paths first.
2. Commit a dedicated session-sync or handoff-sync update second.
3. Run preview again over the relevant final range.
4. Then run the canonical pre-push gate.

When the preview reports an ahead-count advisory, disclose the local stack and
continue admitted local work. At an authorized push checkpoint, bind the intended
upstream..HEAD scope and inspect its actual authorizations and tranche split.
Escalate only a concrete blocker or a missing effect grant. Do not force a push,
request a numeric exception, or stop a new tranche merely because ahead > 2.

## Findings / Position

The preview exists because the full pre-push chain is intentionally broad and
can surface stale front-door markers, active-window registry issues,
review-retention registry scope issues, repository lifecycle markers,
pre-public P3 exposure markers, knowledge-absorption markers, or GC-020
handoff continuity after the agent already believes the batch is ready. Moving
these readouts earlier reduces noisy repair loops while preserving the
canonical gate as the authority.

## Risk / Corrective Action

Risk: an agent may treat the preview as push authorization.

Corrective action: the preview standard explicitly requires the canonical
pre-push autorun gate before push. A PASS from the preview means only that the
known cascade-prone read-only checks passed at that moment.

Risk: an agent may preview an empty or stale range.

Corrective action: the closure packet must name the base/head range used for
final push readiness and must keep material and session-sync ranges separate
when commit-shape says to split them.

Risk: a multi-tranche transport range may contain a real missing authorization,
stale continuity marker or malformed per-tranche commit shape.

Corrective action: show the full ahead/behind count as context and verify actual
scope/continuity at the selected sync checkpoint. Count alone stays advisory;
repair or hold only the named failed condition. No automatic push follows WARN.

## Decision / Disposition

Disposition: ACTIVE_REFERENCE.

The helper `governance/compat/run_agent_push_readiness_preview.py` is the
local implementation of this standard. Future agents should run it before
provenance push, public-sync push, or push-readiness claims.

## Claim Boundary

This standard adds an early local diagnostic step only. It does not push,
fetch, mutate files, replace the pre-push gate, relax any guard, authorize
public-sync, claim live provider behavior, open runtime work, change MPI-T6
status, or certify CVF readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is provenance governance workflow documentation only; no
public-facing artifact is authorized in this batch.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | push-readiness preview standard only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no receipt is created or consumed by the standard |
| actionEvidence | N/A with reason: helper performs read-only local checks |
| invocationBoundary | local agent shell invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or network interception claim |
| claimLanguage | read-only preview before canonical pre-push gate |
| forbiddenExpansion | push authorization, public-sync authorization, runtime/provider/live proof, readiness certification, queue/daemon/watcher, or universal governed-coding-control claim |

## Historical Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | push-readiness preview standardization, 2026-06-27 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | apply_patch, focused pytest, preview helper, governance gates |
| Target paths | `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/guard_orientation/README.md`; `docs/reviews/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARDIZATION_COMPLETION_2026-06-27.md`; `governance/compat/CVF_REVIEW_RETENTION_REGISTRY.json` |
| Allowed scope source | operator instruction to standardize the prevention path for provenance pre-push cascades before returning to FPC-SCG next move |
| Before status evidence | baseHead `3e4b7266`; worktree clean before patch |
| After status evidence | read-only helper and standard added; upstream push-debt limit documented; focused tests updated |
| Diff evidence | `git diff --name-status` against baseHead `3e4b7266` |
| Approval boundary | push-readiness preview standardization only |
| Claim boundary | read-only preview; no public-sync, runtime/provider/live behavior, registry edit beyond documentation, push authorization, MPI-T6 work, or FPC implementation |
| Agent type | reviewer/closer |
| Invocation ID | `agent-push-readiness-preview-standardization-2026-06-27` |
| Expected manifest | `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/guard_orientation/README.md`; `docs/reviews/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARDIZATION_COMPLETION_2026-06-27.md`; `governance/compat/CVF_REVIEW_RETENTION_REGISTRY.json` |
| Actual changed set | `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/guard_orientation/README.md`; `docs/reviews/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARDIZATION_COMPLETION_2026-06-27.md`; `governance/compat/CVF_REVIEW_RETENTION_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py` |
| Manifest delta | MATCH |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local Codex maintainer |
| Provider or surface | private shared workspace |
| Session or invocation | operator count-policy revision, 2026-10-11 |
| Working directory | repository root |
| Command or tool surface | source read, apply_patch, focused pytest and maintenance gates |
| Target paths | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/baselines/CVF_GC018_PUSH_BACKLOG_ADVISORY_2026-10-11.md` |
| Allowed scope source | direct operator request and that GC-018 authorization |
| Before status evidence | clean HEAD 3700b4ee949af6a216b2f74b652fc027f7a72ba3, ahead 2 / behind 0 |
| After status evidence | ahead-only WARN is nonblocking; 17 focused tests passed |
| Diff evidence | exact named-owner policy/helper/test and active-window binding changes; historical trace retained above |
| Approval boundary | authorized local maintenance, no push grant |
| Claim boundary | static policy checks; no worker/provider/live/public proof |
| Agent type | INTERNAL_AGENT maintainer |
| Invocation ID | cvf-push-backlog-advisory-20261011 |
| Expected manifest | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/baselines/CVF_GC018_PUSH_BACKLOG_ADVISORY_2026-10-11.md` |
| Actual changed set | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/baselines/CVF_GC018_PUSH_BACKLOG_ADVISORY_2026-10-11.md` |
| Manifest delta | MATCH |
