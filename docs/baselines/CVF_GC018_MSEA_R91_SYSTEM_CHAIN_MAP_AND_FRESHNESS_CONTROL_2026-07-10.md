# CVF GC-018 Baseline - MSEA-R91 System Chain Map And Freshness Control

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-R91

Dispatch base head: `252fe1a3e`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer role

Worker target: delegated worker role

## Purpose

Build Deliverable B as a truthful whole-picture CVF system-chain map grounded
only in reviewer-accepted MSEA-R90 Audit A, then add a durable freshness control
that detects source drift and produces an automatic weekly reminder without
silently rewriting semantic verdicts.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R91 --title "System Chain Map And Freshness Control" --date 2026-07-10 --base 252fe1a3e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: MSEA-R90 Audit A reviewer acceptance at 645df8b83 and operator continuation on 2026-07-10." --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with source-verified map, fingerprint, scheduled reminder, path-correction, protected-checker, and reviewer-closure requirements. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| docOnlyNewFields | laneId, planeRange, currentPosture, sourceFingerprints, lastVerifiedDate, maxAgeDays, freshnessState, operatorReadout, nextReviewAction |
| claimBoundary | Dispatch authoring only; no map, checker, workflow, or freshness behavior exists until worker output is reviewed and committed. |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MSEA-R90 Audit A | `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`, status `REVIEWER_ACCEPTED_BOUNDED`, material commit `645df8b83` | Deliverable B may use only accepted Audit A findings and their explicit limits. | PASS |
| Operator continuation | Operator instructed Codex to continue after R90 closure on 2026-07-10. | Fresh packet authoring and bounded implementation may proceed. | PASS |
| R72F boundary | R90 closure keeps `RETIREMENT_HOLD_SOURCE_GAP` unchanged. | R91 must not reopen or alter checker lifecycle. | PASS |
| Advisory cleanup | R90 continuity parks relocation as a separate cleanup after canonical owners exist. | R91 creates canonical owners but does not move the advisory directory. | PASS |

## Source Authority

1. `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`.
2. `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`.
3. `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`.
4. Frozen doctrine and current sources cited by Audit A.
5. Current hook catalogs, autorun catalog, and documentation workflow for
   implementation wiring.

Temporary advisory reports are historical context only and are not authority.

## Baseline Decision

Open MSEA-R91 as one bounded protected-governance implementation tranche. The
map, drift detector, reminder workflow, path corrections, tests, and GC-051
metadata form one acceptance unit because the freshness control must pass on
the canonical map at first closure.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Audit A accepted status | `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md` | Status line 5; Decision section lines 74-84 | `REVIEWER_ACCEPTED_BOUNDED` | MSEA-R90 reviewer completion | ACCEPT |
| Five accepted lanes | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md` | Lane headings lines 67, 116, 194, 298, 335; Decision lines 429-452 | five Audit A lane verdicts | MSEA-R90 Audit A | ACCEPT |
| Machine evidence owner | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json` | `chainEdges`, `manifestRecords`, `pathDispositions` | `chainEdges` | MSEA-R90 evidence schema | ACCEPT |
| GC-019 stale citation | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | line 54 | `GC-019` evidence path | Governance Control Matrix row | ACCEPT |
| Operational index stale/missing citations | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | lines 22-24, 38, 41, 46-47, 58 | lookup-table evidence paths | Operational Reference Index | ACCEPT |
| Autorun common command owner | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` line 54 | `_common_commands` | agent autorun command catalog | ACCEPT |
| Pre-commit hook owner | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `PRE_COMMIT_CHECKS` line 6 | `PRE_COMMIT_CHECKS` | local hook catalog | ACCEPT |
| Pre-push hook owner | `governance/compat/local_governance_hook_catalog_pre_push.py` | `PRE_PUSH_CHECKS` line 6 | `PRE_PUSH_CHECKS` | local hook catalog | ACCEPT |
| Reviewer-fast hook owner | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` line 6 | `REVIEWER_FAST_CHECKS` | local hook catalog | ACCEPT |
| CI workflow owner | `.github/workflows/documentation-testing.yml` | workflow name line 1 and trigger block line 3 | `Documentation & Testing` | GitHub Actions workflow | ACCEPT |
| Existing freshness checker pattern | `governance/compat/check_roadmap_closure_freshness.py` | `validate_roadmap_closure_freshness` line 164; `main` line 197 | `validate_roadmap_closure_freshness` | roadmap closure freshness checker | ACCEPT |
| Existing unit-test pattern | `governance/compat/test_check_roadmap_closure_freshness.py` | test functions lines 15, 35, 58, 78 | focused freshness tests | pytest module | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim blocked? |
|---|---|---|
| laneId | Stable five-lane identifier shared by Markdown and JSON. | Yes |
| planeRange | L0-L6 doctrine mapping and non-doctrine component scope. | Yes |
| currentPosture | Accepted current, partial, historical, or future status. | Yes |
| sourceFingerprints | Repo-relative path plus SHA-256 used for drift detection. | Yes |
| lastVerifiedDate | UTC date of the last semantic review. | Yes |
| maxAgeDays | Maximum accepted review age; initial value 30. | Yes |
| freshnessState | CURRENT, SOURCE_DRIFT, PATH_MISSING, MAP_DRIFT, or AGE_EXPIRED. | Yes |
| operatorReadout | Human-readable CLI/CI message and remediation. | Yes |
| nextReviewAction | Bounded action required when stale. | Yes |

## Scope / Allowed Changes

- Create one stable system-chain reference family with a human whole-picture
  map, machine JSON, and freshness standard.
- Correct the eleven archive-moved citations recorded by R90.
- For the one missing H2 citation, remove the dead link or mark it explicitly
  missing; do not substitute a sibling artifact without source-backed semantic
  equivalence.
- Create a read-only freshness checker and focused tests.
- Wire the checker into autorun, pre-commit, pre-push, reviewer-fast, current
  documentation CI, and one weekly scheduled reminder workflow.
- Add/update GC-051 registry source and regenerate its JSON aggregate if the
  changed reference/review surfaces require coverage.
- Create a no-commit worker return.

## Forbidden Scope

- No Web/dashboard implementation or claim of unified 186-checker UI.
- No runtime/provider/live/API behavior, MCP/CLI adapter, public-sync, or push.
- No R72F lifecycle change, checker retirement, cross-family checker edit, or
  conformance scenario change.
- No automatic semantic verdict rewrite. Automation may detect drift and
  instruct a review; only a governed review may update conclusions.
- No relocation, deletion, or renaming of the advisory directory.
- No session-state or active-handoff mutation by the worker.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only system-chain freshness
checker and focused test; add only its command entry to existing hook/autorun
catalogs and current documentation workflow; add one weekly read-only workflow.

Protected paths:

- `governance/compat/check_system_chain_map_freshness.py`
- `governance/compat/test_check_system_chain_map_freshness.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `.github/workflows/documentation-testing.yml`
- `.github/workflows/system-chain-map-freshness.yml`

Operator authorization: the operator required the rebuilt scan/map to remain
current through automatic updating or reminders and then instructed Codex to continue after
R90 closure.

Rollback boundary: revert only R91 map, freshness control, path corrections,
registry metadata, wiring, tests, worker return, and reviewer completion. Do
not revert R90 Audit A, R72F lifecycle authority, or prior hook controls.

Scope boundary: this authorization does not permit semantic auto-editing,
runtime/product code, provider/live proof, public-sync, session mutation, or
advisory-directory relocation.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain map freshness`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "system-chain map freshness" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: exact query returned no entries. |
| Dispatch impact | Source hashes, literal line checks, generated-registry discipline, and role boundaries remain explicit despite no ADIF match. |

## Planned Artifact Manifest

The worker-owned manifest is defined exactly in the paired work order. It
contains the three reference/map files, two path-owner corrections, checker,
tests, four local catalog surfaces, two workflow surfaces, any required GC-051
entry+aggregate pair, and one worker return.

## Acceptance Criteria

- [ ] Whole-picture map uses only R90 accepted findings and distinguishes
      current, partial, historical, and future surfaces.
- [ ] Markdown and JSON share exactly five stable lane IDs and verdicts.
- [ ] Every fingerprinted source path exists and its SHA-256 recomputes.
- [ ] Freshness checker fails on missing path, fingerprint mismatch, map/JSON
      mismatch, and age greater than 30 days.
- [ ] Checker passes on the committed R91 map and emits actionable remediation.
- [ ] Weekly workflow runs read-only checker without credentials or mutation.
- [ ] Eleven stale paths are archive-qualified; missing H2 link is not replaced
      without proof.
- [ ] Focused tests and all applicable governance gates pass.
- [ ] Worker does not commit.

## Evidence / Verification

Required evidence includes deterministic JSON parsing, source-hash
recomputation, focused positive and negative tests, real-repository checker
PASS, exact catalog/workflow binding checks, weekly workflow permission and
secret scan, GC-051 aggregate drift check, worker-return fast gate, and exact
changed-set evidence with unchanged worker HEAD.

Fail conditions:

- [ ] Deliverable B copies temporary scout claims as authority.
- [ ] Automation rewrites semantic verdicts or source owners automatically.
- [ ] Any protected path outside the authorization block changes.
- [ ] Any runtime, provider/live, public, session, lifecycle, or relocation
      change enters the worker set.
- [ ] Weekly workflow requires a secret or mutating permission.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: MULTI_AGENT_MULTI_ROLE

rolePattern: MULTI_AGENT_MULTI_ROLE

phase: dispatch, worker execution, reviewer closure, optional session sync

baseHeadFor(phase): dispatchBaseHead=`252fe1a3e`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_MUST_CAPTURE_AT_CLOSURE

changedSetScope(phase): dispatch pair; exact worker manifest in paired work order; reviewer-owned closure paths only

traceScope(phase, actor): exact reads, commands, source hashes, tests, changed paths, diffs, and per-role base anchors

commitOwner(phase): worker commit forbidden; reviewer/closer owns accepted material commit

crossBatchIsolation: no Web UI, runtime/provider/live, public-sync, session, lifecycle, or advisory relocation

nextMoveSurfaces: reviewer updates continuity only after accepted closure

dispatchBaseHead: `252fe1a3e`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | system-chain README, JSON, standard, checker output | Repo-local read and gate surfaces only | focused tests and worker return | no external adapter | IMPLEMENT_AND_TEST |
| `EXTERNAL_AGENT_CLI_MCP` | N/A with reason: no external adapter is authorized | No ingress, auth, mutation, receipt, or remote execution claim | Forbidden Scope | remains separate | N/A_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `ADIF Defect Registry Disclosure`; `Core Guard Self-Protection Authorization`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Checker Source Read-Ahead Block`; `Public Export Disposition` |
| gateRunPurpose | Confirm dispatch shape after direct source read, not discover requirements. |
| claimBoundary | Dispatch-only evidence; worker implementation truth remains pending. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a five-lane whole-picture map can be made useful
without presenting partial links as complete, and file fingerprints plus an
age threshold can provide durable reminders without semantic auto-editing.

Evidence Comparison Requirement: worker compares the implemented map and all
negative freshness fixtures against this prediction.

Contradiction Handling Requirement: any contradiction with R90 Audit A keeps
the affected lane partial and returns a contradiction ledger; it is not
silently resolved.

Claim Update Requirement: worker records whether B and freshness control are
confirmed, narrowed, or blocked.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local provenance repository |
| Session or invocation | MSEA-R91 dispatch authoring, 2026-07-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, rg, scaffold helper, ADIF resolver, apply_patch, governance gates, git |
| Target paths | paired MSEA-R91 baseline and work order |
| Allowed scope source | R90 next-move state and operator continuation |
| Before status evidence | clean `252fe1a3e` |
| After status evidence | dispatch pair pending dispatch commit |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | bounded B map, path correction, freshness checker/tests/wiring, weekly reminder |
| Claim boundary | no implementation or runtime behavior claimed by dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r91-dispatch-2026-07-10` |
| Expected manifest | MSEA-R91 baseline and work order |
| Actual changed set | MSEA-R91 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | dispatch authorization for repo-local map and freshness control |
| claimDisposition | CLAIM_REJECTED_NO_EXECUTION: no worker implementation exists yet |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no implementation receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification and dispatch gates only |
| invocationBoundary | manual dispatch authoring |
| interceptionBoundary | no IDE, shell, filesystem, provider, CLI, MCP, or Web interception claim |
| claimLanguage | planned read-only checker and scheduled reminder |
| forbiddenExpansion | semantic auto-edit, runtime/provider/live, public, session, lifecycle, and relocation remain forbidden |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R91 begins in the private provenance workspace; no public-sync scope is
authorized.

## Claim Boundary

This baseline authorizes a bounded whole-picture reference, deterministic
freshness detection, path-owner repair, tests, local/CI wiring, and weekly
read-only reminder. It does not claim the work already exists and does not
authorize semantic auto-repair, a Web dashboard, runtime/provider/live work,
public export, lifecycle changes, session mutation, or advisory relocation.
