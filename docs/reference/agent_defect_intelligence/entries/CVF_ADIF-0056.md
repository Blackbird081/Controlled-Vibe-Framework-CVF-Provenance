# ADIF-0056 - Dispatch Base Reused As Worker Execution Base

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0056
title: Dispatch base reused as worker execution base
defectCategory: GATE_TRIGGER_FRICTION
defectClass: ORCHESTRATOR_PACKET_GAP
defectRole: ROOT_CAUSE
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review
roles: dispatcher; worker; reviewer; closer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: docs/work_orders/*.md that declare executionBaseHead capture and a pre-implementation autorun command
detectionSignals: pre-implementation command hard-codes dispatchBaseHead or an older commit instead of worker-captured executionBaseHead; range includes committed packet or continuity paths outside worker ownership; worker stops before edits
enforcementLevel: MACHINE_CHECKED
checkerBindings: governance/compat/check_work_order_dispatch_quality_core.py
promotionState: MACHINE_CHECK_ADDED
supersedes: NONE
lastVerifiedCommit: 28ecdde32
roadmapSeedId: NONE
```

## Purpose

Prevent an orchestrator or dispatcher from reusing the packet-authoring
`dispatchBaseHead` as the worker's pre-implementation range base after the
packet and continuity commits have landed. Role accountability belongs to the
dispatcher who authored the executable packet; worker fail-closed behavior is
the correct response and is not an implementation failure.

`defectRole: ROOT_CAUSE` describes this finding's position in the causal chain.
The `roles` field identifies the dispatcher as the prevention owner and the
worker/reviewer/closer as consumers of the corrected boundary.

## Scope / Applies To

Applies when a work order requires the worker to capture
`executionBaseHead` immediately before edits, especially under
`WORKER_MUST_NOT_COMMIT` with separate material and continuity commits. It
does not require the two anchors to have the same value.

## Bad Example

The dispatcher authors a packet at commit A, commits the packet and continuity
at commits B and C, but leaves this worker command in the packet:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base A --head HEAD
```

At C, the range includes B and C. Range-aware path checks then report packet
and session-sync paths outside worker ownership even though the worker has not
edited anything.

## Good Example

The packet keeps the two anchors distinct and makes the worker command consume
the captured execution anchor:

```powershell
git rev-parse HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

The worker substitutes the full HEAD captured at start, verifies clean status
and empty staging, and stops without edits if the command exposes a
contradiction. The dispatcher, not the worker, corrects a bad packet anchor.

## Canonical Sources

- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`, Core Philosophy, Escalation Ladder, and Closure Rule.
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`, Protocol and Generalizable finding promotion.
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`, Base-Anchor Lifecycle and commit choreography rules.
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`, Worker pre-implementation stop boundary.
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_2026-09-08.md`, R1 Anchor Correction Disposition and corrected pre-flight command.

## Remediation

1. Preserve `dispatchBaseHead` as packet-authoring provenance only.
2. Require the worker to capture `executionBaseHead` from the committed HEAD
   immediately before worker edits.
3. Bind every worker pre-implementation command to that captured execution
   anchor, never a packet-authoring SHA.
4. Classify a resulting pre-edit stop as `ORCHESTRATOR_PACKET_GAP`; retain the
   worker's no-edit evidence and account for the consumed invocation without
   inflating worker repair-failure counts.
5. ROLE-SOT-MH-T1 added that pre-dispatch check. When a packet declares
   `executionBaseHead: WORKER_MUST_CAPTURE_AT_START`,
   `_validate_execution_anchor_substitution` in
   `governance/compat/check_work_order_dispatch_quality_core.py` scans only the
   real `## Verification Commands` section and rejects a pre-implementation
   autorun command whose `--base` is the packet's dispatch SHA,
   `dispatchBaseHead`, or `<dispatchBaseHead>`; `<executionBaseHead>` and
   `$executionBaseHead` are accepted. The work-order template and dispatch
   scaffold were deliberately not modified, because both are
   maintainability-sensitive owners and the prevention did not require growing
   them. Enforcement is forward-only for changed packets; historical packets
   are not rewritten.

## Epistemic Process Block

### Expected Result / Prediction

Running pre-implementation from the worker-captured clean HEAD should produce
an empty pre-edit range and should not attribute the already-committed packet
or continuity paths to the worker.

### Evidence Comparison

ROLE-SOT-EVIDENCE-T0 first ran the packet's hard-coded older base from clean
execution HEAD `60c969e02` and failed on paths outside the exact worker scope.
The worker correctly returned `BLOCKED_WITH_REASON` without edits. After the
dispatcher changed only the base formula to `<executionBaseHead>`, the same
pre-implementation phase passed 83/83 at clean HEAD `df4fe6ad4`.

### Contradiction Or Gap Disposition

The failure was not evidence that the worker violated scope. It contradicted
the packet's dispatch-ready claim because the dispatcher encoded the wrong
lifecycle anchor in an executable command.

### Claim Update

Anchor names are not interchangeable metadata. Their role-specific lifecycle
meaning must reach the command that consumes them, and the earliest prevention
owner is the dispatcher at pre-dispatch.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker preflight consumed the packet-authoring base and swept committed material/continuity paths outside worker ownership | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Update the work-order template/scaffold and reject hard-coded pre-implementation base SHAs when `executionBaseHead` is worker-captured | Finding and guidance recorded now; template/checker implementation deferred to the post-RABA-T1-T3 CVF role-foundation hardening |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - the evidence is a
repository-local orchestration and phase-range defect; no provider, live,
runtime, model, quota, or cost behavior was exercised.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/dispatcher acting as governance-learning recorder |
| Provider or surface | local private provenance workspace |
| Session or invocation | ROLE-SOT-EVIDENCE-T0 anchor-gap learning, 2026-09-08 |
| Working directory | repository root |
| Command or tool surface | returned blocker evidence, governed source reads, Git inspection, ADIF intake/resolver, SHA-256 capture, exact-path stash isolation, `apply_patch`, and local governance checks |
| Target paths | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0056.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Allowed scope source | operator instruction on 2026-09-08 to record this as a CVF Finding-To-Governance learning |
| Before status evidence | corrected work order committed at `28ecdde32`; continuity at `df4fe6ad4`; no ADIF entry captured the dispatch-versus-execution anchor substitution defect |
| After status evidence | ADIF-0056 is resolver-discoverable and the entries front door names it as guidance-only machine-check candidate |
| Diff evidence | exact two-path ADIF entry and entries-front-door diff, isolated from the three completed unstaged worker paths |
| Approval boundary | defect recording and future-control routing only; no template, scaffold, checker, hook, worker artifact, runtime, provider, or public mutation |
| Claim boundary | guidance-only defect record; no current machine prevention or universal agent compliance claim |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `role-sot-evidence-t0-adif-0056-2026-09-08` |
| Expected manifest | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0056.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Actual changed set | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0056.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance agent-defect learning. No public-sync action or
public catalog claim is authorized.

## Claim Boundary

This entry records one reusable role-owned orchestration defect and routes a
future template/checker improvement. It does not implement that checker,
change the current worker result, reopen RABA-T1 through RABA-T3, or authorize
runtime, provider/live, public-sync, deployment, push, or production action.
