# CVF Agent Work Order - RSPB-AI-T2 Capability Environment Snapshot Doctor Enrichment And Pre-Dispatch Consumer Implementation

Memory class: governed-worker-dispatch

rawMemoryReleased=false

Status: REVIEWER_ACCEPTED_DISPATCH_READY

docType: work_order

Date: 2026-08-16

Batch ID: RSPB-AI-T2

Dispatch base head: `c849677d2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one bounded Python source-and-test implementation worker

Reviewer/closer: independent reviewer/closer role

Worker return path: `docs/reviews/CVF_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_WORKER_RETURN_2026-08-16.md`

## Dispatch Prompt Envelope

Role: source-and-test implementation worker for `RSPB-AI-T2`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_2026-08-16.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture the clean committed HEAD at start.

Current-time notes: authority date is 2026-08-16; record actual HEAD and any
source drift before editing.

Do-not-misread notes: enrich the existing doctor owner and release consumer
only. Do not import or run candidate scanner code, expose secrets/raw paths,
mutate the environment, install dependencies, call networks/providers, or
claim that snapshot readiness grants execution authority.

Required first actions: read startup front doors, active handoff, guard
orientation, literal gotchas, paired baseline, T1 contract and completion,
every source path in Source Verification, and applicable checker sources;
capture clean execution base and run pre-implementation before editing.

Return contract: implement and test exactly the four-path manifest, create the
worker return, leave every change unstaged and uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a secret-free and non-mutating capability environment snapshot mode
inside `scripts/cvf_doctor.py`, cover its availability/UNKNOWN/redaction/TTL
contract with isolated tests, and make `scripts/run_cvf_release_gate_bundle.py`
consume it before expensive non-dry-run work. Preserve the existing doctor
mode, release live-proof rules, and evidence-versus-authority boundary.

## Operator Checkpoint

Resolved on 2026-08-16: the operator's `next` instruction opens the bounded
implementation tranche recommended by the accepted T1 completion. It does not
open acquisition, mutation, live/provider, public-sync, deployment, or
production scope.

## Authorization / Dependencies

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T1 owner contract | `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md` accepted at `d591c542a` | existing doctor must be enriched; parallel scanner is forbidden | PASS |
| T1 independent completion | `docs/reviews/CVF_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_COMPLETION_2026-08-16.md` accepted at `d591c542a` | implement only the bounded recommended slice | PASS |
| operator checkpoint | explicit `next` instruction on 2026-08-16 | authorizes this fresh implementation packet | PASS |
| clean closure state | continuity commit `c849677d2` | dispatch may be authored from clean HEAD | PASS |

## Authority Chain

Operator `next` instruction -> accepted T1 owner/value decision -> paired
GC-018 baseline -> this exact T2 work order -> no-commit worker -> independent
reviewer/closer.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | opened the bounded implementation tranche |
| dispatcher | source-verify, gate, commit, and sync this packet |
| implementation worker | edit only the four owned paths; test; do not stage or commit |
| independent reviewer/closer | inspect real diff, recompute proof, repair if bounded, commit, and sync |

## Worker Autonomy / No-Question Rule

Repair failing syntax, focused tests, or machine gates inside Allowed scope,
rerun them, and record final evidence without asking the operator. Stop only
for a source contradiction, forbidden-scope need, owner collision, or missing
authority that makes completion impossible.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator continuation of accepted repo-local T1 contract and completion |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| scope classification | R1 local read-only diagnostics and pre-dispatch consumer implementation |
| risk sensitivity | secret/path leakage, mutation, stale evidence, and accidental live-work start |
| selected role route | dispatcher authors; one no-commit worker implements; independent reviewer/closer accepts |
| Runtime/source modification | exact three Python source/test paths plus worker return |
| External evidence intake | not authorized; predecessor evidence is already normalized repo-local authority |
| Disposition | no-commit implementation after committed dispatch continuity |
| escalation condition | extra path, candidate-code use, acquisition/mutation, raw secret/path exposure, network/provider/live/public/deploy action, or authority-boundary change |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T2 --title "Capability Environment Snapshot Doctor Enrichment And Pre-Dispatch Consumer Implementation" --date 2026-08-16 --base c849677d2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact snapshot semantics, consumer short-circuit, four-path manifest, focused verification, ownership, boundaries, and return requirements |
| checkerReadAheadConfirmation | same checker family recorded in the paired baseline |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; worker execution remains pending |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "runtime implementation" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned none |
| Dispatch impact | no additional ADIF-specific constraint; canonical guards still apply |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Source Verification columns; worker-return full-gate fields; review headings; Agent Operation Trace fields; no-commit finality; public disposition |
| gateRunPurpose | derive packet/return shape before dispatch and confirm it after authoring |
| claimBoundary | this dispatch and its pending worker return only |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `AGENTS.md` | READ | root authority and task routing |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact current facts |
| `CVF_SESSION_MEMORY.md` | READ | current mode and boundary |
| `AGENT_HANDOFF_V59_2026-08-11.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | FULL_READ | worker orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal-safe artifact authoring |
| `docs/baselines/CVF_GC018_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_2026-08-16.md` | FULL_READ | paired authorization |
| `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md` | FULL_READ | binding minimal snapshot contract |
| `docs/reviews/CVF_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_COMPLETION_2026-08-16.md` | FULL_READ | accepted owner/consumer decision |
| `scripts/cvf_doctor.py` | FULL_READ | existing owner and compatibility behavior |
| `scripts/run_cvf_release_gate_bundle.py` | FULL_READ | consumer sequencing and live-proof boundary |
| `scripts/test_run_cvf_sot3_a5_release_integration.py` | SOURCE_VERIFIED | existing release integration convention and regression target |
| applicable worker-return checker sources | READ | exact pending-return shape |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| doctor already owns command discovery and version checks | RUNTIME_BEHAVIOR | `scripts/cvf_doctor.py` | lines 32-48 and 71-110 | `command_version`; `build_checks` | CVF doctor | ACCEPT |
| snapshot branch must avoid full-mode env bootstrap and mutating/network-adjacent checks | RISK_FACT | `scripts/cvf_doctor.py` | lines 51-68 and 203-217 | `is_port_listening`; `path_writable`; `bootstrap_repo_env` | CVF doctor full mode | ACCEPT |
| release bundle eagerly constructs build/typecheck/provider/secrets checks before E2E and SOT3 | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | lines 628-647 | `main` results sequence | release-gate bundle | ACCEPT |
| release subprocess helper is local and secret-safe in output decoding | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | lines 116-143 | `run_cmd`; `platform_cmd` | release-gate bundle | ACCEPT |
| minimal snapshot semantics are fixed | GOVERNED_DECISION | `docs/reference/capability_preflight_bootstrap/CVF_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_CONTRACT.md` | lines 160-208 | Minimal CVF-Native Snapshot Contract | capability preflight reconciliation | ACCEPT |
| accepted next move names doctor, isolated tests, TTL/redaction, and pre-dispatch consumer | GOVERNED_DECISION | `docs/reviews/CVF_RSPB_AI_T1_CAPABILITY_PREFLIGHT_OWNER_RECONCILIATION_AND_READ_ONLY_SNAPSHOT_VALUE_PROBE_COMPLETION_2026-08-16.md` | lines 79-89 | `PROCEED_TO_IMPLEMENTATION_WORK_ORDER` | T1 independent completion | ACCEPT |
| existing release integration tests import the bundle with local unittest conventions | TEST_CONVENTION | `scripts/test_run_cvf_sot3_a5_release_integration.py` | lines 1-27 | `unittest`; `mock`; scripts path import | release integration tests | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| two dispatch paths | absent before authoring | PASS |
| new test and worker-return paths | exact `Test-Path` results false before dispatch | PASS |
| owner collision | direct source read confirms doctor and release-bundle owners; no parallel scanner path is authorized | PASS |
| clean base | HEAD `c849677d2`; status empty before authoring | PASS |

## Scope / Implementation Requirements

1. Add a dedicated `--capability-snapshot` doctor mode. When selected, it
   must not call `bootstrap_repo_env`, `build_checks`, port/socket probes,
   filesystem write probes, provider-key checks, or any mutating helper.
2. Observe exactly `git`, `python`, `node`, `npm`, and `npx`. Discovery absence
   is `MISSING`. A discovered command whose bounded version probe raises,
   times out, returns non-zero, or has unusable output is `UNKNOWN`. Only a
   successful bounded version probe is `AVAILABLE`.
3. Emit a versioned JSON snapshot with a unique snapshot identity,
   `observedAt`, `expiresAt`, fixed five-minute TTL, workspace-local scope,
   exact observation class, per-command availability/path class/version, and
   aggregate verification status plus issue reasons. Time and discovery/run
   call sites must be injectable enough for hermetic tests.
4. Never emit a raw executable path, repository absolute path, PATH listing,
   environment-variable name/value inventory, credential value/status, raw
   subprocess body beyond one bounded version line, or candidate-source fact.
   Use a small documented path-class enum and bound version text length.
5. Add pure freshness verification. An expired snapshot or malformed time is
   non-ready/fail-closed with an explicit reason. Freshness never grants
   execution, mutation, activation, approval, or owner authority.
6. Preserve existing doctor invocation and JSON behavior when snapshot mode is
   absent. Snapshot JSON exits zero only when all five prerequisites are fresh
   and `AVAILABLE`; missing, unknown, malformed, or expired evidence exits
   non-zero without remediation or mutation.
7. Add a release-bundle preflight check before the existing results sequence.
   On non-dry-run preflight failure, return a secret-safe FAIL result and do
   not call build, typecheck, provider readiness, secrets scan, E2E, or SOT3.
   On PASS, preserve the existing sequence and mandatory live-proof policy.
   Dry-run must preserve its no-execution contract and may mark preflight SKIP.
8. Add isolated unittest coverage in the single new test file. All command,
   time, and release-check effects must be mocked; no real network, provider,
   dependency installation, env bootstrap, filesystem mutation, or live proof.

## Pre-Flight Checks

1. Capture full HEAD and exact status; stop unless the worktree is clean.
2. Confirm baseline/work order are committed and the test/return paths absent.
3. Reproduce Source Verification symbol searches.
4. Run pre-implementation from captured execution base.
5. Stop on drift, collision, concurrent changes, or forbidden-path need.

## Execution Plan

1. Refactor only the minimum doctor internals needed to isolate a pure,
   injectable snapshot builder and verifier while preserving full mode.
2. Add snapshot CLI parsing/output and fail-closed exit semantics.
3. Wire one early release-bundle consumer with explicit failure short-circuit.
4. Add hermetic tests for all contract, compatibility, and short-circuit rows.
5. Run syntax, focused unit/integration, dry-run, file-size, worker-return, and
   diff checks.
6. Create the worker return, rerun final commands after the last edit, and
   hand off unstaged and uncommitted.

## Write Ownership

### Worker-Owned Writable Paths

1. `scripts/cvf_doctor.py`
2. `scripts/run_cvf_release_gate_bundle.py`
3. `scripts/test_cvf_doctor_snapshot.py`
4. `docs/reviews/CVF_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_WORKER_RETURN_2026-08-16.md`

### Reviewer-Owned Closure Paths

The paired baseline/work order, optional completion review, accepted worker
outputs, affected roadmap/catalog only if independently justified, and
continuity surfaces in a separate sync batch.

Every other path is forbidden to the worker.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/cvf_doctor.py` | implement the bounded snapshot builder/verifier and CLI mode while preserving existing mode |
| `scripts/run_cvf_release_gate_bundle.py` | add one early non-dry-run preflight consumer and failure short-circuit |
| `scripts/test_cvf_doctor_snapshot.py` | create hermetic snapshot and consumer tests |
| worker return path | create full evidence packet with exact diff, test receipts, risk disposition, and no-commit proof |

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `scripts/cvf_doctor.py` | Yes | existing observation owner enriched |
| `scripts/run_cvf_release_gate_bundle.py` | Yes | existing expensive-workflow consumer enriched |
| `scripts/test_cvf_doctor_snapshot.py` | Yes | isolated proof |
| worker return path | Yes | pending implementation evidence |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| predecessor candidate source tree | design evidence only; no import, execution, or edit |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/**` | snapshot is not execution authority |
| `EXTENSIONS/CVF_GUARD_CONTRACT/**` | snapshot cannot alter owner binding |
| `CVF_SESSION/**`; `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF*.md` | reviewer-owned continuity |
| `governance/compat/**` | no checker/hook work |
| `.github/**`; public-sync sibling clone | no CI/public work |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `scripts/test_cvf_doctor_snapshot.py` | ABSENT | ABSENT | stop on collision |
| worker return path | ABSENT | ABSENT | stop on collision |

## Pre-Existing Dirty Path Exemptions

N/A with reason: dispatch worktree was clean; no dirty-path exemption exists.

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| available state | `scripts/cvf_doctor.py` | `AVAILABLE` | Yes |
| missing state | `scripts/cvf_doctor.py` | `MISSING` | Yes |
| unknown state | `scripts/cvf_doctor.py` | `UNKNOWN` | Yes |
| observed time | `scripts/cvf_doctor.py` | `observedAt` | Yes |
| expiry time | `scripts/cvf_doctor.py` | `expiresAt` | Yes |
| fixed TTL | `scripts/cvf_doctor.py` | `300` | Yes |
| git observation | `scripts/cvf_doctor.py` | `git` | Yes |
| python observation | `scripts/cvf_doctor.py` | `python` | Yes |
| node observation | `scripts/cvf_doctor.py` | `node` | Yes |
| npm observation | `scripts/cvf_doctor.py` | `npm` | Yes |
| npx observation | `scripts/cvf_doctor.py` | `npx` | Yes |
| CLI mode | `scripts/cvf_doctor.py` | `--capability-snapshot` | Yes |
| early consumer | `scripts/run_cvf_release_gate_bundle.py` | `Capability environment preflight` | Yes |
| no-commit handoff | worker return | `WORKER_MUST_NOT_COMMIT honored` | Yes |

## Required Proof Manifest Atomic Literal Discipline

Each required literal must appear atomically in the named artifact. Equivalent
prose, split strings, comments alone, or a literal present only in this work
order do not satisfy handoff proof.

## Focused Test Matrix

| Case | Required result |
|---|---|
| each of five commands has successful version probe | `AVAILABLE`; bounded version; redacted path class |
| command not discovered | `MISSING`, not UNKNOWN |
| discovered command raises, times out, fails, or has unusable output | `UNKNOWN`, not AVAILABLE |
| snapshot generated at injected time | exact `observedAt`, five-minute `expiresAt`, unique ID, workspace-local scope |
| fresh complete snapshot | ready/PASS |
| expired or malformed freshness | non-ready/fail-closed with reason |
| output serialization | no raw absolute executable/repo path, PATH, env value, token, or credential field |
| snapshot CLI branch | does not invoke env bootstrap, port/socket, write probe, or full doctor checks |
| legacy doctor branch | existing status/check JSON shape remains compatible |
| release preflight FAIL | all expensive check functions remain uncalled and result is secret-safe FAIL |
| release preflight PASS | existing check order and SOT3 mandatory behavior remain |
| release dry-run | preflight is SKIP/no command execution; existing dry-run semantics remain |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | doctor builder and release-bundle preflight | local read-only evidence may block workflow; never grants authority | focused tests and reviewer recomputation | repository-native Python | IMPLEMENTED |
| EXTERNAL_AGENT_CLI_MCP | `python scripts/cvf_doctor.py --capability-snapshot --json` | local CLI JSON only; no auth, mutation, remote invocation, or public promise | CLI/schema and redaction tests | CLI is implemented in scope; MCP remains deferred | CONTRACT_ONLY |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | role-neutral dispatch; implementation worker; independent reviewer/closer |
| phase | dispatch, implementation, review, closure conversion |
| baseHeadFor(phase) | dispatchBaseHead=`c849677d2`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | worker four-path manifest; reviewer closure and continuity separately |
| traceScope(phase, actor) | worker records edits/tests/diff; reviewer independently recomputes |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; reviewer/closer commits |
| crossBatchIsolation | clean start; no concurrent/unrelated path changes |
| nextMoveSurfaces | reviewer updates governed state only after acceptance |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Single agent owns implementation and review | NO |
| Role separation ledger | delegated worker owns implementation/return; independent reviewer/closer owns acceptance, commit, and continuity |
| Evidence basis | repo-local source, actual diff, hermetic tests, CLI smoke/dry-run, and governance gates |
| Self-review boundary | worker may self-check but may not accept, close, stage, or commit its own output |
| Gate sequence | pre-dispatch by dispatcher; pre-implementation/tests/fast return by worker; reviewer-return and material-only pre-closure by reviewer |
| Escalation conditions | manifest expansion, owner contradiction, candidate use, mutation, secret/raw path, network/provider/live/public/deploy, destructive action, or claim expansion |
| Worker | delegated implementation worker |
| Reviewer / committer | independent reviewer/closer |
| Human escalation checkpoint | scope or policy expansion only |
| Collusion boundary | reviewer inspects real diff and reruns required checks |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_COMPLETION_2026-08-16.md` (optional; prefer corrected worker return when sufficient) |
| reviewerOwnedClosurePaths | accepted four worker outputs; baseline; work order; justified owner/catalog state; continuity separately |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RSPB_AI_T2_CAPABILITY_ENVIRONMENT_SNAPSHOT_DOCTOR_ENRICHMENT_AND_PRE_DISPATCH_CONSUMER_IMPLEMENTATION_WORKER_RETURN_2026-08-16.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Source Inventory;
Gate Evidence; Checker Source Read-Ahead Block; Agent Operation Trace Block;
Delta Execution Claim Boundary Control Block; External Knowledge Intake
Routing; Rescan Intelligence Hardening; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Epistemic Process
Block; Public Export Disposition; Machine Closure Package; Claim Boundary;
git status --short; Changed Files; Worker Experience Retrospective; Command
Evidence; No-Commit Statement.

## Required Checks

Run from repository root:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m py_compile scripts/cvf_doctor.py scripts/run_cvf_release_gate_bundle.py scripts/test_cvf_doctor_snapshot.py
python -m unittest scripts.test_cvf_doctor_snapshot
python -m unittest scripts.test_run_cvf_sot3_a5_release_integration
python scripts/cvf_doctor.py --capability-snapshot --json
python scripts/run_cvf_release_gate_bundle.py --dry-run
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_cvf_doctor_snapshot.py
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
git rev-parse HEAD
```

The snapshot smoke command may return non-zero only when its JSON correctly
identifies a real local `MISSING` or `UNKNOWN` prerequisite; that environment
result is evidence, not an implementation failure. All unit/integration and
governance commands must pass. No live release command is authorized.

## Verification Commands

Use the exact Required Checks block. The mandatory return gate is
`python governance/compat/run_worker_return_fast_gate.py --pytest-target scripts/test_cvf_doctor_snapshot.py`;
individual checker substitution is forbidden.

## Evidence Requirements

- exact execution HEAD before and after, actual four-path diff, and empty
  cached diff;
- hermetic tests proving every Focused Test Matrix row after the last edit;
- valid snapshot JSON smoke evidence with no raw path or secret-bearing field;
- release dry-run compatibility and existing SOT3 integration regression PASS;
- file-size and worker-return fast gate PASS;
- explicit statement that no candidate code, env bootstrap in snapshot mode,
  mutation, network/provider/live action, staging, or commit occurred.

dispatchBaseHead: `c849677d2`

executionBaseHead: worker captures current committed dispatch HEAD at start

closureBaseHead: N/A - pending independent review

## Acceptance Criteria

- [ ] Exactly four worker-owned outputs are changed or created.
- [ ] Snapshot mode observes only the five allow-listed commands and is
  secret-free, path-redacted, non-mutating, and independent of env bootstrap.
- [ ] AVAILABLE, MISSING, UNKNOWN, TTL expiry, malformed freshness, and
  bounded output have hermetic positive/negative tests.
- [ ] Existing doctor behavior remains compatible outside snapshot mode.
- [ ] Release consumer short-circuits every expensive check on preflight FAIL
  and preserves existing behavior on PASS and dry-run.
- [ ] Snapshot evidence has no grant/approval/execution-authority semantics.
- [ ] Required tests and gates pass after the last edit.
- [ ] Worker return is `COMPLETE_PENDING_REVIEW`; HEAD and staging are unchanged.

Fail conditions: extra path; raw secret/path/PATH/env output; candidate-code
use; snapshot mutation; missing fail-closed UNKNOWN/expiry; expensive check
called after preflight failure; live/provider/network action; public sync;
authority expansion; worker stage or commit.

## Review Gate

Worker handoff is not closure. The independent reviewer must inspect all four
paths, verify no direct candidate-code derivation, rerun required tests and
gates, validate short-circuit call evidence and redaction, accept or repair the
bounded diff, create the material commit, and run material-only committed-range
pre-closure before continuity changes.

## Epistemic Process Block

Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION

Expected Result / Prediction: the accepted slice can enrich the current doctor
and stop expensive release work early with low maintenance cost, without a
parallel scanner or authority coupling.

Evidence Comparison Requirement: compare actual diff, hermetic tests, CLI
snapshot, release dry-run, and file-size result against the prediction.

Contradiction Handling Requirement: any need for candidate code, extra owner,
mutation, raw sensitive output, or live proof requires a Contradiction Or Gap
Disposition and stop.

Claim Update Requirement: classify result as confirmed, narrowed, revised, or
blocked without extending to production/public readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | RSPB-AI-T2 dispatch authoring, 2026-08-16 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, scaffold helper, ADIF resolver, patch edits, governance gates, git status/diff |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator `next` instruction plus accepted T1 contract/completion |
| Before status evidence | clean HEAD `c849677d2` |
| After status evidence | exact two-file dispatch authoring set before commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | author packet only; implementation begins from later committed post-sync HEAD |
| Claim boundary | local dispatch evidence only; no implementation/runtime result yet |
| Agent type | dispatcher |
| Invocation ID | `rspb-ai-t2-dispatch-2026-08-16` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSPB-AI-T2 source/test implementation dispatch authoring |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: packet and current-source verification only |
| receiptEvidence | CVF_RECEIPT_PRESENT: local command and gate evidence captured before dispatch commit |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact two-file dispatch diff |
| invocationBoundary | local documentation authoring and static source inspection only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, runtime, or adapter interception claim |
| claimLanguage | dispatch is ready for a later no-commit worker after committed continuity sync |
| forbiddenExpansion | no candidate scanner, acquisition/mutation, secrets/raw paths, network/provider/live, MCP, public sync, deployment, or production |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason - worker may not edit a
protected governance or session path.

Protected paths: N/A with reason - none in the worker manifest.

Operator authorization: N/A with reason - no protected-path worker edit.

Rollback boundary: N/A with reason - no protected-path worker edit.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | predecessor T1 already normalized provenance and owner decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing doctor and release-bundle paths |
| Disposition | NOT_APPLICABLE_WITH_REASON: implementation consumes only accepted repo-local authority |
| Claim boundary | private local candidate remains design evidence, not source authority |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing `scripts/` diagnostic and release workflow owner family |
| Storage decision | enrich two existing owners and add one colocated isolated test |
| Existing aggregate impact | none |
| Generated state impact | none; snapshot is process-local and not persisted |
| Durable governance boundary | no durable registry, route, index, receipt store, or new foundation is created |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this implementation consumes the already accepted
RSPB-AI-T1 decision and makes no new corpus, rescan, or legacy-coverage claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; public sync is forbidden.

## Closure Checklist

- [ ] All four worker-owned outputs are present and no extra path changed.
- [ ] Focused tests, regression tests, syntax, dry-run, file-size, and fast
  return gate pass after the last worker edit.
- [ ] Worker return records actual pending status, empty staged diff, unchanged
  HEAD, and `WORKER_MUST_NOT_COMMIT` compliance.
- [ ] Independent reviewer recomputes proof and owns material commit.
- [ ] Material-only pre-closure passes before separate continuity sync.
- [ ] Public catalog is N/A with reason unless a later public-sync packet is authorized.

## Return-To-Orchestrator Conditions

Return without continuing if a required current source or authority artifact
is missing or contradictory; if completion needs any fifth worker path; if
the snapshot cannot remain non-mutating and secret/path-redacted; if the
release consumer cannot short-circuit without altering mandatory live-proof
semantics; or if any candidate-code, acquisition, network/provider/live,
public-sync, deployment, production, destructive, staging, or commit action
would be required.

## Claim Boundary

This work order authorizes a bounded no-commit implementation and hermetic
tests only. It does not accept the worker's output, import candidate code,
grant capability authority, prove live/production behavior, or authorize
network/provider use, public export, deployment, or production operation.
