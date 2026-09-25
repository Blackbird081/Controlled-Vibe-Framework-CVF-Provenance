# CVF Dispatch Release Readiness Machine Standard

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference_standard

Date: 2026-09-25

providerExecutionAuthority: FORBIDDEN

## Purpose

Prevent an orchestrator from releasing a work order after authoring checks but
before the dispatch packet and its continuity projection are committed. A
worker must not be the first actor to discover that the packet is untracked,
the active handoff lacks its material-SHA marker, or `currentAuthority` still
points to a predecessor packet.

## Scope / Applies To

Applies to final release of a `docs/work_orders/*.md` packet through
`pre-dispatch`, and to revalidation through `pre-implementation` when an
`--active-work-order` binding is supplied. It does not block the preceding
authoring or material-commit step; authoring checks and pre-commit hooks remain
responsible for packet content before the material SHA exists.

## Dispatch Release Invariants

| Rule | Required evidence | Failure meaning |
|---|---|---|
| `DR-01` | explicit safe work-order binding equals bootstrap `currentAuthority.workOrderPath` | caller omitted or selected the wrong authority packet |
| `DR-02` | baseline and work order are tracked, clean, present, and match the recorded raw SHA-256 values | packet is uncommitted, dirty, absent, or stale |
| `DR-03` | both packet files share one material commit reachable from requested HEAD | dispatch has no coherent material anchor |
| `DR-04` | handoff, bootstrap, active aggregate, and front door share a clean committed continuity sync after the material commit | session continuity is missing, partial, or uncommitted |
| `DR-05` | active handoff GC-020 marker names the batch and material commit | worker cannot bind instructions to committed dispatch evidence |
| `DR-06` | bootstrap next move names the batch, exact work order, and an `EXECUTE` action class | current session authority has not released execution |

The gate is intentionally two-commit aware. It does not demand a material SHA
before the material commit can exist. It demands the completed packet commit
plus a later continuity commit before any worker handoff can be called ready.

## Machine Binding

Checker:
`governance/compat/check_dispatch_release_readiness.py`.

Final work-order dispatch command:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <authoringBaseHead> --head HEAD --active-work-order <exact-work-order-path>
```

When bootstrap `nextAllowedMove` is work-order based, omission of
`--active-work-order` fails before any gate bundle or receipt reuse. The same
binding at `pre-implementation` re-runs release readiness before worker edits.
The release checker is not wired into the ordinary pre-commit hook because the
first material commit necessarily precedes the knowable material SHA and the
continuity commit.

## Remediation

1. Commit the reviewed baseline and work order as one material dispatch commit.
2. Record that material SHA and batch in the active handoff marker.
3. Update split session-state sources so `currentAuthority` and
   `nextAllowedMove` select execution of the exact packet.
4. Regenerate session aggregates; commit the handoff, front door, source state,
   and generated projections as the continuity commit.
5. Run final `pre-dispatch` with the exact `--active-work-order` binding. Do not
   contact or launch the worker until it passes.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer and governance guard maintainer |
| Provider or surface | private CVF workspace |
| Session or invocation | AKOE-P1 dispatch-release defect hardening, 2026-09-25 |
| Working directory | repository root |
| Command or tool surface | governed source reads, `apply_patch`, focused pytest, autorun and Git |
| Target paths | this standard; dispatch-release checker and tests; autorun runner/catalog; ADIF-0058 |
| Allowed scope source | operator instruction to tighten the machine gate after premature AKOE-P1 worker handoff |
| Before status evidence | authoring pre-dispatch passed while packet files were untracked; worker first detected missing commits, marker and current-authority update |
| After status evidence | final work-order pre-dispatch requires explicit binding and proves both material and continuity commits before PASS |
| Diff evidence | bounded governance-control diff and regression fixtures |
| Approval boundary | local governance control plane only |
| Claim boundary | configured CLI/autorun release admission only; no universal interception of out-of-band messages |
| Agent type | orchestrator/reviewer |
| Invocation ID | `akoe-p1-dispatch-release-hardening-20260925` |
| Expected manifest | standard, checker, tests, autorun runner/catalog, autorun tests, ADIF-0058, affected routing prose |
| Actual changed set | verified before material commit |
| Manifest delta | pending final verification |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening; no public-sync action or
public catalog claim is authorized.

## Epistemic Process Block

### Expected Result / Prediction

Binding final work-order release to the two committed anchors should stop the
observed premature-handoff path before a CLI/MCP worker is invoked.

### Evidence Comparison

Regression fixtures reproduce dirty/untracked packet state, material commit
without continuity, missing material marker, stale current authority, and the
fully committed positive case.

### Contradiction Or Gap Disposition

The prior pre-dispatch bundle proved packet shape but did not distinguish
authoring readiness from worker-release readiness. The new phase-specific
binding closes that gap without making the material commit circular.

### Claim Update

The control claims fail-closed local gate behavior for configured autorun
calls. It does not claim that arbitrary out-of-band messaging is technically
intercepted.

## Claim Boundary

This standard and checker validate local Git and continuity evidence for one
explicit work-order release. They do not judge implementation quality, grant
scope expansion, contact a worker, commit worker changes, run providers, or
authorize public sync, deployment, or production action.
