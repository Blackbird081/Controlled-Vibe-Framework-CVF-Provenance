# CVF Work Order Closure Quality Gate Standard

Memory class: POINTER_RECORD

Status: ACTIVE_STANDARD

docType: reference

Date: 2026-05-28

Last updated: 2026-06-04

Authority: restored active canonical path plus CI/LPCI closure-friction learning

Historical full packet:

`docs/reference/archive/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

---

## Purpose

Prevent governed work from being called closed when the evidence chain exists
only in prose or chat memory.

Closure means the transition from authority to artifact to machine-readable
evidence to continuity state is reproducible from repository files and recorded
commands.

---

## Scope

This standard applies to every active CVF work order, roadmap task, completion
review, corpus scan, classification packet, public-sync batch, delegated worker
execution, and reviewer/committer closure.

Archive-qualified artifacts under `archive/` are historical evidence. They are
not active closure claims unless a later governed batch explicitly reopens
them.

---

## Rule

No artifact may be marked `CLOSED`, `CLOSED_PASS`,
`CLOSED_PASS_BOUNDED`, `DISPATCH_READY` for a dependency-released packet, or an
equivalent final state unless the applicable closure gates below are satisfied:

1. roadmap-to-work-order trace matrix;
2. closure diff and allowed-scope check;
3. command/path/receipt-backed claim integrity;
4. explicit fail-condition scan;
5. checklist finalization;
6. continuity sync;
7. committed-range autorun `pre-closure`;
8. public export disposition when applicable;
9. corpus completeness and knowledge reconciliation when applicable;
10. worker autonomy and no-question rule for delegated packets;
11. self-reported gate evidence consistency;
12. work-order fulfillment manifest for runtime/source work;
13. machine closure package for downstream loop inputs;
14. closure packaging preflight before full pre-closure claim.

Allowed-scope machine-gate failures are mandatory remediation, not operator
preference questions. Escalate only when remediation would exceed Allowed
scope, change risk or claim boundary, release a `HOLD_*` prerequisite, run
live/provider proof, use secrets/quota, public-sync, touch forbidden paths, or
perform destructive/irreversible actions.

---

## Required Closure Markers

This active standard intentionally exposes the exact marker names used by
dispatch-quality and autorun wiring. Work orders and closure packets may add
detail, but must not rename these concepts away from machine-readable form.

### Roadmap-To-Work-Order Trace Matrix

Map every roadmap requirement to a work-order instruction, output artifact,
verification command, and status.

### Negative And Fail-Condition Scan

Record the missing-field, stale-source, public/provenance, forbidden-runtime,
status-token, source-symbol, and checklist-residue conditions that would block
closure.

### Mandatory Gate-Failure Remediation Protocol

Repair allowed-scope guard failures and rerun the failed gate before handoff.
Do not ask the operator whether to fix owned machine-gate residue.

### Worker Autonomy / No-Question Rule

Ready delegated packets must authorize non-destructive reads, checks, routine
format fixes, required evidence-block completion, and gate reruns inside
Allowed scope.

### Pending Artifact Evidence Finality

Pending worker artifacts must state pending status honestly and must not claim
clean worktree, committed-range proof, or final pre-closure evidence before
reviewer/committer disposition.

### Commit Mode And Base-Anchor Lifecycle

Separate `dispatchBaseHead`, `executionBaseHead`, `closureBaseHead`, and
handoff-sync parent evidence. `--base HEAD --head HEAD` is not closure proof
for changed governed artifacts.

### Self-Reported Gate Evidence Consistency

Recorded gate results must match the current artifact and handoff state. After
rerun, update the evidence table before returning or committing the artifact.

### Near-Threshold Owner Maintainability Plan

When a touched governed owner file is near its hard threshold, include split,
rotation, archive, or shrink evidence in the same governed batch.

### Work-Order Fulfillment Manifest

Runtime/source work must declare required artifacts, forbidden paths, and
forbidden filesystem state before implementation.

### Closure Packaging Preflight

Before claiming full `pre-closure`, run the early closure-packaging preflight
or rely on the autorun wrapper that runs it first. The preflight catches
recurring packaging defects while the fix is still small:

- closed-equivalent artifacts retaining stale dispatch, hold, or pending
  pre-closure language;
- corpus completeness blocks using git-derived or bare `rg --files`
  enumeration instead of filesystem-backed enumeration such as
  `rg --files --hidden --no-ignore ...`;
- closure diff / changed-file sections citing paths that are not present in
  the changed range;
- protected guard/session files changed without a checker-recognized
  `Core Guard Self-Protection Authorization` artifact.

### Current Runtime Freshness Verification

Absence, missing, stale, hardcoded, or per-role-only runtime/source claims must
be backed by current source searches and owner-path evidence.

### ACCEPT_AS_OWNER_MAP coverage

Accepted concepts from a source audit must be represented as completed,
deferred, rejected, or out-of-scope with reason. Scope rejection is not source
rejection.

---

## Machine Closure Package

Any closure that feeds another CVF loop must record the downstream input
surfaces explicitly.

Required package:

| Closure item | Required artifact/path | Machine-readable evidence |
| --- | --- | --- |
| Work order status | `docs/work_orders/<work-order>.md` | final status, no stale ready/pending residue, closure anchor policy |
| Completion or reviewer artifact | `docs/reviews/<completion>.md` or `N/A with reason` | final disposition, changed files, claim boundary, gate evidence |
| Roadmap state | `docs/roadmaps/<roadmap>.md` or `N/A with reason` | tranche row final state and next dependency state |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` or `N/A with reason` | scan/readiness/gap fields when corpus state changes |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` or `N/A with reason` | operator/reviewer quick lookup when GC-051 state changes |
| External evidence digest | repo-local digest section or artifact | external path, schema/version, record count, hash, generated time, privacy boundary |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_*.json` or `N/A with reason` | upstream output, downstream input, learning/finding route, mutation boundary |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff | current mode, next allowed move, handoff HEAD or accepted parent marker |

Rules:

- External/local workspace paths are evidence inputs, not canonical Source
  Verification source files. Record their digest in the repository before a
  later packet cites them as evidence.
- Corpus scan, classification, readiness, or gap state changes must update
  both GC-051 registry surfaces when applicable. JSON is the machine input;
  Markdown is the reviewer/operator lookup.
- Closed-equivalent artifacts must not retain stale `DISPATCH_READY`,
  `READY_WITH_CONDITIONS`, `NOT_EXECUTED_YET`, `PRE_CLOSURE_NOT_RUN`, unchecked
  required checklist items, or placeholder dependency rows except in explicit
  pending-review worker handoffs.
- Finding-bearing artifacts must use checker-accepted
  Finding-To-Governance defect classes. `EVIDENCE_GAP` is not a defect class;
  `N/A_WITH_REASON` is a disposition, not a defect class.

---

## Commit Choreography

Governed closure follows:

`docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`

Required principles:

- stage the intended file set before running hook-chain or commit validation;
- use `executionBaseHead` for pending worker validation and `closureBaseHead`
  for reviewer/committer closure;
- never use `--base HEAD --head HEAD` as evidence for changed governed
  artifacts;
- split archive hygiene, artifact implementation, closure transition, session
  sync, and handoff-only sync unless a work order explicitly owns the combined
  scope;
- after material or session commits, create a dedicated handoff-only sync
  commit when active handoff HEAD proof requires it.

---

## Enforcement

This standard is enforced by work-order authors, workers, reviewers,
committers, local governance hooks, and autorun gates. Relevant machine checks
include:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_closure_packaging_preflight.py`
- `governance/compat/check_machine_closure_package.py`
- `governance/compat/check_markdown_structural_completeness.py`
- `governance/compat/check_active_session_state.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/check_corpus_scan_registry.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

Manual compliance is mandatory even when a particular machine check has not
yet learned the defect.

---

## Claim Boundary

This standard defines closure evidence discipline. It does not prove semantic
correctness, product readiness, public export, legal advice quality, runtime
integration, or live governance behavior unless those claims are backed by
their own required standards and proof commands.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is an internal provenance workflow and closure-evidence standard.
