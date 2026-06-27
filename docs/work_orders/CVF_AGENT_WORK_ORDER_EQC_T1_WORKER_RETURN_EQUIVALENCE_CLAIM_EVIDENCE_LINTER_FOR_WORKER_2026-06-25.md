# CVF Agent Work Order EQC-T1 Worker Return Equivalence Claim Evidence Linter For Worker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-25

docType: work_order

Batch ID: EQC-T1

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: EQC-T1 no-commit worker; equivalence-claim-evidence checker builder.

Canonical packet: this work order plus `docs/baselines/CVF_GC018_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_2026-06-25.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead `a63de6d3` (capture actual with `git rev-parse --short HEAD` at worker start).

Current-time notes: current dispatch date is 2026-06-25; worker must record actual local start time in the return packet.

Do-not-misread notes: this is a checker-authoring tranche only, not a
retroactive rewrite of any existing closed worker-return. Do not "fix" any
pre-existing ASSF or other closed worker-return found by the dry run; report
it as a finding only. The checker must not call any network/provider/LLM
API; it is a static-pattern text scan only. Build exactly one new
`governance/compat/check_*.py` file and add exactly one new entry to
`REVIEWER_FAST_CHECKS`; do not create a second autorun entrypoint or wire it
into any other phase list.

Required first actions: read front door/state/handoff/guard orientation
documents, this work order, the GC-018 baseline, the
`check_rescan_intelligence_hardening.py` precedent, and the ASSF-T4
completion review's Finding-To-Governance Learning Disposition section;
capture `git status --short`; run the pre-implementation gate.

Return contract: return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` without
committing.

You are the EQC-T1 worker. Build only the equivalence-claim-evidence checker,
its single hook-chain registration, paired tests, and the worker-return
packet described here. You must not commit. Return
`COMPLETE_PENDING_REVIEW` only with the required artifacts present and
reviewer-fast evidence captured, or return `BLOCKED_WITH_REASON` if a gate
fails outside allowed scope.

## Core Guard Self-Protection Authorization

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | EQC-T1 creates one NEW governed automation file under `governance/compat/` (`check_equivalence_claim_evidence.py`) and its paired test file; it modifies exactly one existing file, `governance/compat/run_local_governance_hook_chain.py`, to append one new tuple entry to `REVIEWER_FAST_CHECKS`; it does not modify, delete, or weaken any existing check, hook, or autorun gate entry |
| Protected paths | `governance/compat/run_local_governance_hook_chain.py` (one additive entry only); `governance/compat/run_agent_autorun_workflow_gate.py` remains unmodified |
| Operator authorization | operator selected EQC-T1 as a bounded micro-governance tranche and agreed the no-bottleneck constraint before dispatch |
| Rollback boundary | worker creates only the new checker file, its test file, and the one additive hook-chain entry; revert is deletion of the new files and removal of the one added tuple line |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: the worker
  must not claim an exhaustive directory enumeration; the dry run reports
  only the files the checker's own scan logic flags, named explicitly in the
  worker return.
- ADIF-0002 - Provider-local interaction accepted as authority: the checker
  itself enforces the opposite of this defect; the worker must not accept
  any unverified provider-local claim while authoring it.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class:
  the worker must avoid bare gate-trigger tokens in exclusion prose where
  they would falsely signal a different evidence class than
  checker-authoring.

## Scope / Target / Owner Boundary

Target: one bounded no-commit worker-return building the EQC-T1
equivalence-claim-evidence checker, its single hook-chain entry, paired
tests, and a read-only dry run.

Owner boundary:

- this work order names the dispatcher (Claude), the worker (assigned at
  dispatch), and the reviewer/closer (operator-designated at dispatch time);
- the worker owns only the paths in Write Ownership below;
- work outside those boundaries requires a new work order or an operator
  correction.

## Purpose

Provide a no-commit worker packet for EQC-T1 so the equivalence-claim-evidence
checker the ASSF-T4 reviewer proposed is built, tested, and dry-run against
the existing governed corpus before Codex (or the operator-designated
reviewer) reviews and wires it as enforcing.

## Objective

Build `governance/compat/check_equivalence_claim_evidence.py`: a static-text
checker that scans changed `docs/reviews/*.md` files and any changed file
under `docs/work_orders/*.md` containing a worker-return block, for
equivalence-claim phrases used near a named source-file reference without an
adjacent evidence-command-or-disposition-token pair. Add exactly one entry
for it to `REVIEWER_FAST_CHECKS` in
`governance/compat/run_local_governance_hook_chain.py`. Write paired tests.
Run a read-only dry run against the full existing `docs/reviews/` and
docs/work_orders/ (directory) history and report results in the worker return.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | informational; EQC-T1 does not require a session-state mode change to dispatch |
| GC-018 baseline | `docs/baselines/CVF_GC018_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_2026-06-25.md` | continuation baseline for this work order |
| ASSF-T4 completion review | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | source of the concrete linter proposal this tranche implements |
| Rescan-intelligence checker precedent | `governance/compat/check_rescan_intelligence_hardening.py` | structural pattern to mirror: changed-range diff resolution, `--base`/`--head` args, violations list, `main()` exit code |
| Hook chain registry | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` list (line 24) this tranche appends one entry to |
| ADIF resolver | `governance/compat/run_adif_defect_resolver.py` | `resolve_defect_packet` read-only query pattern |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Claude (this turn) | Create source-verified dispatch packet; dispatcher does not execute |
| Worker | assigned worker agent | Build the checker, hook-chain entry, tests, and worker-return packet; do not commit |
| Reviewer/closer | operator-designated at dispatch time | Validate the checker against the no-bottleneck constraint, run the dry run independently, close EQC-T1, and commit if accepted |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `docs/reference/guard_orientation/README.md`
- this work order
- `docs/baselines/CVF_GC018_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_2026-06-25.md`
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a63de6d3 --head HEAD
```

Expected results:

- clean or worker-owned-only working tree before edits
- pre-implementation gate passes against the dispatch base

If a pre-flight check fails, stop and record the failed command and result.

## Write Ownership

The worker owns only the artifacts named in Allowed Scope. The reviewer owns
the closure review, the one additive hook-chain registration's final
acceptance, and any material commit.

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | reviewer creates a completion review under the reviews directory after accepting this return |
| workerReturnPath | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md` |
| reviewerOwnedClosurePaths | EQC-T1 completion review, the one additive `REVIEWER_FAST_CHECKS` commit, and session-sync commit if the active mode changes |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | reviewer may commit only after independently rerunning the checker's tests and dry run and confirming the no-bottleneck constraint is satisfied |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Claude dispatcher creates work order; worker builds the checker and returns review artifacts; operator-designated reviewer decides closure and commit |
| phase | DISPATCH_AUTHORING -> WORKER_EXECUTION -> REVIEWER_CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`a63de6d3`; executionBaseHead=worker must capture with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may create only the paths named in Allowed Scope and Write Ownership |
| traceScope(phase, actor) | worker records commands, test results, dry-run findings, and gate receipts in the return packet |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; reviewer owns any material and session-sync commit |
| crossBatchIsolation | no ASSF-T5 work; no unrelated cleanup; no second checker entrypoint |
| nextMoveSurfaces | worker must not edit active session state, session front door, active handoff, or generated active-session aggregate |
| closer designation | operator-designated reviewer/closer |

## 6C. Worker Autonomy / No-Question Rule

The worker must repair any machine-gate failure inside Allowed Scope and
rerun the relevant gate without pausing for approval. The worker must stop
and return `BLOCKED_WITH_REASON` only when repair would exceed Allowed
Scope, alter commit mode, touch forbidden paths, require live/provider/
public-sync/secrets, add a second checker entrypoint, add a network/
provider/LLM-judge call, or require retroactively editing an existing
closed worker-return or completion review (report it as a dry-run finding
instead).

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake class | operator-provided external comparison, critique, or recommendation (the ASSF-T4 reviewer finding) |
| Route mode | `MULTI_AGENT_SINGLE_ROLE` |
| Selected route | Claude dispatcher -> worker checker-builder -> operator-designated reviewer/closer |
| Primary worker role | equivalence-claim-evidence checker, hook-chain entry, and tests builder |
| Reviewer role | independently validate the no-bottleneck constraint and the dry-run results, then close |
| External intake route | N/A with reason: this finding originates from this repository's own governed completion review, not an external or legacy source |
| Scope classification | bounded no-commit worker-return building one new governance checker |
| Risk sensitivity | moderate: the checker becomes a standing reviewer-fast gate for every future governed worker-return and completion review, so a false-positive-prone pattern list would create friction across all future tranches |
| Escalation condition | stop with `BLOCKED_WITH_REASON` if remediation exceeds allowed scope, touches forbidden paths, needs new human authorization, requires a second checker entrypoint, or requires retroactively editing an existing closed artifact |
| Dispatch status | ACCEPT |
| Reason | EQC-T1 is selected, source-verified, and bounded to a no-commit single-checker worker-return |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Reason | EQC-T1 does not scan or absorb any legacy corpus; it authors a checker from an internal completion-review finding |
| Required worker evidence | N/A with reason: no legacy absorption ledger row applies to this tranche |
| Future guard candidate | N/A with reason |

## Required Artifact Manifest

| Required output | Path | Required at handoff | Exists |
|---|---|---|---|
| Equivalence-claim-evidence checker | `governance/compat/check_equivalence_claim_evidence.py` | yes | worker must create |
| Checker test file | `governance/compat/test_check_equivalence_claim_evidence.py` | yes | worker must create |
| Hook-chain registration (one additive `REVIEWER_FAST_CHECKS` tuple) | `governance/compat/run_local_governance_hook_chain.py` | yes | worker must add |
| EQC-T1 worker return | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md` | yes | worker must create |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Equivalence-claim-evidence checker | `governance/compat/check_equivalence_claim_evidence.py` | worker | WORKER_RETURNED |
| Checker test file | `governance/compat/test_check_equivalence_claim_evidence.py` | worker | WORKER_RETURNED |
| Hook-chain registration | `governance/compat/run_local_governance_hook_chain.py` | worker | WORKER_RETURNED |
| EQC-T1 worker return | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md` | worker | WORKER_RETURNED |
| EQC-T1 completion review | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_COMPLETION_2026-06-25.md` | reviewer | CLOSED_PASS_BOUNDED |
| Material commit | git commit after reviewer acceptance | reviewer | CLOSURE_READY |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| any existing `docs/reviews/*.md` or `docs/work_orders/*.md` (other than this dispatch pair) | this tranche must not retroactively edit any existing closed worker-return or completion review; dry-run findings are reported, not repaired in-place |
| `governance/compat/run_agent_autorun_workflow_gate.py` | the no-bottleneck constraint forbids adding a second autorun phase entrypoint for this checker |
| any new test, source, or config file requiring network or provider credentials | the checker must remain a static-pattern text scan with no network/provider/LLM-judge call |
| `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, any `AGENT_HANDOFF*.md` | EQC-T1 does not require a session-state mode change |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `governance/compat/check_equivalence_claim_evidence.py` | ABSENT | ABSENT (verified by dispatcher before this dispatch) | N/A |
| `governance/compat/test_check_equivalence_claim_evidence.py` | ABSENT | ABSENT (verified by dispatcher before this dispatch) | N/A |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Violation raised on bare equivalence claim | `governance/compat/test_check_equivalence_claim_evidence.py` | `test_flags_claim_without_evidence` | Yes |
| No violation when evidence command is adjacent | `governance/compat/test_check_equivalence_claim_evidence.py` | `test_allows_claim_with_evidence_command` | Yes |
| No violation when disposition token is adjacent | `governance/compat/test_check_equivalence_claim_evidence.py` | `test_allows_claim_with_disposition_token` | Yes |
| No false-fire on isolated phrase with no nearby path | `governance/compat/test_check_equivalence_claim_evidence.py` | `test_no_path_reference_does_not_fire` | Yes |
| Dry-run false-positive report present in worker return | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md` | `Dry-Run Findings` | Yes |

## 7. Write Ownership

Owned files or modules:

- `governance/compat/check_equivalence_claim_evidence.py`
- `governance/compat/test_check_equivalence_claim_evidence.py`
- `governance/compat/run_local_governance_hook_chain.py` (additive entry only)
- `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md`

Forbidden paths:

- any other file in the repository

Write mode: create-only for new files; modify-listed (additive single-tuple
append only) for `run_local_governance_hook_chain.py`.

## 8. Execution Plan

1. Capture startup state:
   - `git rev-parse --short HEAD`
   - `git status --short`
2. Read the required first reads, including the rescan-intelligence checker
   precedent and the ASSF-T4 completion review's finding.
3. Run the pre-implementation gate using the dispatch base unless the
   reviewer has provided a newer dispatch commit:
   - `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a63de6d3 --head HEAD`
4. Author `governance/compat/check_equivalence_claim_evidence.py`:
   - mirror `_get_changed_name_status`/`_resolve_range`/`_add`/`main` from
     `check_rescan_intelligence_hardening.py` for changed-range resolution,
     `--base`/`--head` args, and violation collection;
   - scan changed `docs/reviews/*.md` files and changed `docs/work_orders/*.md`
     files for a worker-return block;
   - define a closed phrase list: `verbatim`, `identical`, `no new field`,
     `maps to existing`, `unchanged`, `same as`, `reused exactly`;
   - for each phrase occurrence within the same paragraph as a path-like
     token (a backtick-quoted file path or contract name), check a bounded
     character window (e.g. 300 chars) around the match for either an
     evidence-command pattern (`rg `, `git diff --no-index`, a markdown table
     row) or a disposition token (`MATCH`, `ADAPTED_WITH_REASON`,
     `NEW_FIELD_INTRODUCED`, `NOT_LITERAL_WITH_REASON`);
   - if neither is found, record a violation naming the phrase, the cited
     path, and the file/line;
   - exit non-zero with a printed report when violations exist, mirroring
     `check_rescan_intelligence_hardening.py`'s `main()` exit-code pattern.
5. Add exactly one entry to `REVIEWER_FAST_CHECKS` in
   `governance/compat/run_local_governance_hook_chain.py`, following the
   existing tuple shape (label string, command list with `--base`/`--head`/
   `--enforce`).
6. Write `governance/compat/test_check_equivalence_claim_evidence.py` with at
   least the four Required Proof Manifest tests above
   (`test_flags_claim_without_evidence`,
   `test_allows_claim_with_evidence_command`,
   `test_allows_claim_with_disposition_token`,
   `test_no_path_reference_does_not_fire`).
7. Run a read-only dry run: invoke the new checker's detection logic (not
   the git-diff-based CLI) directly against every existing file under
   `docs/reviews/` and docs/work_orders/ (directory) and record any flagged file in the
   worker return under a `Dry-Run Findings` table, without editing any of
   those files.
8. Author the worker-return packet.
9. Run:
   - `python -m pytest governance/compat/test_check_equivalence_claim_evidence.py`
   - `python governance/compat/run_worker_return_fast_gate.py`
10. Return `COMPLETE_PENDING_REVIEW`,
    `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`
    without committing.

## Evidence Requirements

- contract-conformance note mapping the checker's phrase list and
  evidence-window logic to the ASSF-T4 completion review's concrete proposal
- false-positive dry-run table against the existing `docs/reviews/` and
  docs/work_orders/ (directory) corpus
- changed-set manifest (`git diff --name-status` and `git status --short`)
- test results for both required proofs
- explicit no-commit status

Evidence Trace Block requirements:

- Claim:
- Command:
- Result:
- Key path:
- Verdict:

Base-anchor evidence:

- `dispatchBaseHead`: `a63de6d3`
- `executionBaseHead`: worker captures with `git rev-parse --short HEAD`
- `closureBaseHead`: N/A - pending review
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Worker-return fast gate:
  `python governance/compat/run_worker_return_fast_gate.py`
  plus `--pytest-target governance/compat/test_check_equivalence_claim_evidence.py`
- Committed-range `pre-closure`: N/A - pending review

## Review Gate

The reviewer must independently rerun the checker's tests and the dry run,
verify the checker satisfies the no-bottleneck constraint (one checker, one
`REVIEWER_FAST_CHECKS` entry, static pattern only, role-count-invariant), and
confirm no existing closed worker-return was edited before accepting worker
output. Worker self-approval is not closure.

## Required Execution Steps

See Execution Plan above; steps are sequential.

## Required Deliverables

### Checker File

Standalone, deterministic, read-only with respect to existing repository
state (it scans and reports; it writes nothing). No network or provider
call. Keep the file under the 600-line Python automation soft threshold.

### Test File

Covers both Required Proof Manifest assertions plus the no-false-fire case
for an isolated phrase with no nearby path-like token.

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md`

Required sections:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Status
- Required Artifact Manifest
- Core Guard Self-Protection Authorization
- Dual Agent Surface Matrix
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Machine Closure Package
- Acceptance Receipt Assertion Matrix
- Agent Operation Trace Block
- Claim Boundary

The worker return must also record `executionBaseHead`, `git status --short`,
a `dispatchWorkOrder:` line citing this work order, and a top-level `Status:`
line. Because this changeset touches
`governance/compat/run_local_governance_hook_chain.py`, the worker return must
carry a `## Core Guard Self-Protection Authorization` block listing the
protected path and the four required tokens (`Authorized guard-maintenance
scope`, `Protected paths`, `Operator authorization`, `Rollback boundary`). For
any of the required sections above that do not apply to this checker-authoring
tranche (for example a section block normally used for corpus scans this
tranche does not perform), the worker must write `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON` rather than leaving the section blank or omitting
it.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `check_equivalence_claim_evidence.py` running inside `REVIEWER_FAST_CHECKS` | the checker only flags missing evidence; it grants no additional authority | checker tests and dry-run report | no adapter implemented | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | none | this tranche exposes no CLI/MCP surface | N/A with reason: no external surface created | N/A with reason: no adapter scope exists | `NOT_APPLICABLE_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Worker requirement |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` cited for routing-format conformance only; N/A with reason: no external or legacy source is consulted |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | ASSF-T4 completion review finding -> EQC-T1 checker -> reviewer-fast gate |
| Matching local-view guard | N/A with reason |
| Owner surface | EQC-T1 checker and any future EQC-T2 widening tranche |
| Disposition | checker-authoring only; no external intake |
| Route | N/A with reason |
| Boundary | static-pattern text scan only |
| External-agent disposition | `NOT_APPLICABLE_WITH_REASON` in the Dual Agent Surface Matrix above |
| Claim boundary | the finding originates from this repository's own governed completion review |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: N/A with reason: no predecessor governed
  reference document is being rescanned
- Delta ledger status: worker must refresh in the worker-return packet.
- Routing matrix status: worker must refresh in the worker-return packet.
- Semantic sampling status: worker must include at least three samples in the
  worker-return packet.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker instruction |
|---|---|
| `UNCHANGED_FROM_INTAKE` | implement the ASSF-T4 reviewer's phrase list and evidence-window requirement as specified |
| `CHANGED_DISPOSITION` | the finding moves from `MACHINE_CHECK_CANDIDATE` to an implemented, tested checker |
| `NEW_FINDING` | record any phrase or evidence-form gap discovered while authoring the checker |
| `REMOVED_OR_REJECTED` | record any network/provider-call design or per-step/per-role gate design as rejected |

### Follow-Up Routing Matrix

| Routing lane | Worker instruction |
|---|---|
| `DO_NOW` | build the checker, hook-chain entry, tests, dry run, and worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | widening the scanned-file set beyond `docs/reviews/*.md` and worker-return blocks in docs/work_orders/ (directory) is a future EQC-T2 decision |
| `STRATEGIC_OPERATOR_DECISION` | whether to retroactively annotate any pre-existing closed worker-return flagged by the dry run is deferred to the operator |
| `OUT_OF_SCOPE` | LLM-judge verification, per-step/per-role gating, runtime/provider/live, public-sync |
| `RESOLVED_BY_DESIGN` | the single-checker, single-gate-phase, static-pattern, role-count-invariant constraint is satisfied by construction |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| EQC-T1-WO-S1 | ASSF-T4 completion review finding | equivalence claims need adjacent evidence | checker requires evidence window or disposition token tied to the same cited path | could a worker satisfy the checker with an unrelated evidence command nearby | reject |
| EQC-T1-WO-S2 | GC-018 Decision section no-bottleneck constraint | one checker, one gate phase | checker design uses no network call and one hook-chain entry | could a future repair add a second autorun entrypoint | reject |
| EQC-T1-WO-S3 | GC-018 Knowledge Absorption Blind-Spot Control Block | dry run must not retroactively edit closed artifacts | dry run is read-only; findings are reported only | could the worker "fix" a flagged existing worker-return in place | reject |

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | choose one or more: `RULE_GAP`, `MACHINE_GATE_GAP`, `PHASE_GATE_PLACEMENT_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED`, `MACHINE_CHECK_CANDIDATE`, or `REFERENCE_ONLY` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` unless a runtime/provider/cost finding arises |
| Next control action | state whether a future EQC-T2 should widen the scanned-file set or phrase list |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this tranche references internal completion-review and ASSF lane
governance findings. Public-facing documentation of the checker is a later
public-sync decision out of this tranche's scope.

## Acceptance Criteria

- [x] Required artifacts exist in allowed paths only.
- [x] The checker detects an equivalence-claim phrase near a named source
  path with no adjacent evidence-command or disposition token, proven by a
  test.
- [x] The checker does not false-fire when an evidence-command or
  disposition token is adjacent to the same cited path, proven by a test.
- [x] The checker does not false-fire on an isolated equivalence phrase with
  no nearby path-like token, proven by a test.
- [x] Exactly one new `governance/compat/check_*.py` file is created and
  exactly one new `REVIEWER_FAST_CHECKS` entry is added.
- [x] No network/provider/LLM-judge call exists in the checker.
- [x] A read-only dry run against the existing `docs/reviews/` and
  docs/work_orders/ (directory) corpus is recorded in the worker return with a
  disposition for every flagged file.
- [x] No existing closed worker-return or completion review is edited.
- [x] The worker return carries the Core Guard Self-Protection Authorization
  block and a top-level `Status:` line.
- [x] No commit is made by the worker.

Fail conditions (reviewer confirmed each condition below is absent):

- [x] More than one new checker file or more than one new autorun-list entry
  is created.
- [x] Any network/provider/LLM-judge call is added to the checker.
- [x] Any existing closed worker-return or completion review is edited.
- [x] The checker's behavior varies by declared role count or route mode.

Closure is blocked if any fail condition is present. None of the four
conditions above are present; all four checkboxes record that the reviewer
confirmed absence, not occurrence.

## Closure Checklist

- [x] All acceptance criteria satisfied or explicitly marked N/A with reason
- [x] Required tests run (`test_flags_claim_without_evidence`,
  `test_allows_claim_with_evidence_command`,
  `test_allows_claim_with_disposition_token`,
  `test_no_path_reference_does_not_fire`)
- [x] Dry-run findings table recorded in the worker return
- [x] Commit mode recorded as `WORKER_MUST_NOT_COMMIT`
- [x] Worker return uses a non-closed status and records actual
  `git status --short`
- [x] Agent Operation Trace Block is present and complete
- [x] Changed-file set from `git diff --name-status` is inside this work
  order's Allowed scope
- [x] No second checker entrypoint or second autorun-list entry was added
- [x] No existing closed worker-return or completion review was edited
- [x] Reviewer independently reruns tests and dry run before closure

## Operator Checkpoint

N/A with reason: the operator selected and scoped EQC-T1 directly, including
the no-bottleneck constraint, before this work order was authored. No extra
checkpoint is required before bounded worker execution; Stop Conditions
define the return path.

## Stop Conditions

Return `BLOCKED_WITH_REASON` if:

- the pre-implementation gate fails outside allowed scope;
- the rescan-intelligence checker precedent or the hook-chain registry is
  unavailable or has a structurally different shape than cited;
- a repair would require a second checker entrypoint, a network/provider
  call, retroactive editing of an existing closed artifact, or a commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | N/A with reason | EQC-T1 is not derived from a roadmap tranche | N/A with reason |
| GC-018 status | `docs/baselines/CVF_GC018_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_WORKER_RETURN_2026-06-25.md` | `Status: COMPLETE_PENDING_REVIEW`, accepted after reviewer field-label repair | PASS |
| Completion review | `docs/reviews/CVF_EQC_T1_WORKER_RETURN_EQUIVALENCE_CLAIM_EVIDENCE_LINTER_COMPLETION_2026-06-25.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: EQC-T1 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: EQC-T1 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported | N/A with reason |
| System loop interlock | this work order | the ASSF-T4 finding was required before this tranche; the checker becomes a standing reviewer-fast gate; no retroactive enforcement on past closed artifacts | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable files created by worker | checker file, test file, worker-return packet, plus one additive line in the hook-chain registry |
| Canonical package root | N/A with reason: not applicable to a governance checker tranche |
| Generated index or aggregate | N/A with reason: this tranche creates no generated aggregate |
| Storage migration | N/A with reason: out of scope |
| New reference-family folders | N/A with reason: no new `docs/reference/` subfolder is created |
| Layout risk | bounded single-checker addition; reviewer owns closure commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Work order status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Allowed output paths | checker/test/worker-return/one hook-chain line only | as listed | PASS |
| No-bottleneck constraint | one checker, one gate phase, static pattern, role-count-invariant | required by work order | PASS |
| Network/provider call | forbidden | forbidden by work order | PASS |
| Retroactive edit of closed artifacts | forbidden | forbidden by work order | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Worker-return EQC-T1 equivalence-claim-evidence checker only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - no-commit single-checker worker-return dispatch |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide command, test, and dry-run receipts in the return packet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide phrase-detection proof, evidence-window proof, and dry-run findings |
| invocationBoundary | governed local automation authoring and static-pattern text scanning |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | build one equivalence-claim-evidence checker, one hook-chain entry, and paired tests |
| forbiddenExpansion | no second checker entrypoint, no network/provider/LLM-judge call, no per-step/per-role gate, no retroactive edit of closed artifacts, no runtime/provider/live or public-sync behavior |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatcher |
| Provider or surface | local workspace |
| Session or invocation | EQC-T1 dispatch, 2026-06-25 |
| Working directory | repository root |
| Command or tool surface | source reads, file authoring, governance gates, git commit by reviewer only |
| Target paths | this work order; EQC-T1 GC-018 baseline |
| Allowed scope source | operator instruction to scope and author the EQC-T1 work order after agreeing the no-bottleneck constraint |
| Before status evidence | clean worktree at HEAD `a63de6d3` |
| After status evidence | EQC-T1 dispatch ready |
| Diff evidence | real-range name-status and gate output before reviewer commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | worker-return lane; no checker build performed by this dispatch |
| Agent type | dispatcher |
| Invocation ID | `cvf-eqc-t1-worker-return-equivalence-claim-evidence-linter-work-order-2026-06-25` |
| Expected manifest | this work order; EQC-T1 GC-018 baseline |
| Actual changed set | this work order; EQC-T1 GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- pre-flight fails;
- any autorun phase gate fails outside Allowed scope or cannot be repaired
  inside this work order;
- source-fidelity pass finds a missing path, invented symbol, or unverified
  role/template mapping;
- scope conflict is discovered;
- required citation cannot be found;
- implementation would exceed risk ceiling;
- reviewer raises a structural blocking objection;
- public/provenance boundary is unclear.

## Claim Boundary

This work order authorizes only a no-commit worker-return lane that builds
the EQC-T1 equivalence-claim-evidence checker, its single hook-chain entry,
paired tests, and a read-only dry run against the existing governed corpus.
It does not authorize a second checker entrypoint, a network/provider/
LLM-judge call, a per-step or per-role gate, retroactive editing of any
existing closed worker-return or completion review, runtime/provider/live
proof, public-sync, or worker commit.
