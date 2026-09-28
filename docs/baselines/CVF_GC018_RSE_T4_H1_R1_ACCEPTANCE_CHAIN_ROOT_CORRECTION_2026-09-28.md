# CVF GC-018 - RSE-T4-H1-R1 Acceptance Chain Root Correction

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-09-28

Batch ID: RSE-T4-H1-R1

Packet amendment: bind the exact worker-return path required by the independent
probe admission gate; no scope or acceptance requirement changes.

Risk ceiling: HIGH - protected governance templates and machine gates; local,
provider-free and reversible.

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one Local-executed corrective tranche for ADIF-0061 and ADIF-0062.
The tranche must establish a machine-readable acceptance join from each
dispatcher-owned required deliverable through Git-observed artifacts and
requirement-bound proof to a deterministically reduced terminal status. It
also restores the bounded tool/classifier recovery contract rejected in H1.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id RSE-T4-H1-R1 --title "Acceptance Chain Root Correction" --date 2026-09-28 --base cf0bbc1b2 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id RSE-T4-ACCEPTANCE-CHAIN-JOIN --prior-finding-set-digest 532e49a72 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence ADIF-0062 --scec-problem-key RSE-T4-ACCEPTANCE-CHAIN-JOIN --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md --scec-predecessor-sha256 FILL_AFTER_SOURCE_READ --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | protected-governance-path, internal Local execution |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | root contract, acceptance ledger, exact paths and Local phase separation |
| checkerReadAheadConfirmation | named gates inspected before packet authoring |
| docOnlyNewFields | strict acceptance-ledger JSON and RSE recovery fields |
| claimBoundary | provenance only; no implementation or external action |

## Authority Chain

- Operator instruction on 2026-09-28: Local must complete foundation repair
  before returning to the NCR roadmap and must not dispatch Claude.
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md`
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md`
- `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md`
- `docs/reviews/evidence/rse-t4-h1-independent-probe-2026-09-28.json`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V63_2026-09-18.md`

## Source Verification

| Claim | Source evidence | Disposition |
|---|---|---|
| Work-order template is inside the GC-023 near-hard margin | 1,181 lines at authoring; hard threshold 1,200 and near-hard margin 25 | ACCEPT |
| Operation-trace manifest comparison fails open when no expected path parses | `governance/compat/check_agent_operation_trace.py`, `_check_manifest_delta` | ACCEPT |
| Completion consistency uses lexical manifest-delta phrases | `governance/compat/check_worker_return_quality_gate.py`, `_required_gate_consistency_issues` | ACCEPT |
| Worker-return fast gate does not run an acceptance-ledger checker | `governance/compat/run_worker_return_fast_gate.py`, `build_commands` | ACCEPT |
| H1 passed structural gates but failed four independent semantic mutations | H1 completion and independent probe | ACCEPT |
| No canonical acceptance-ledger checker exists | targeted `rg` over `governance/compat` and work-order references | ACCEPT |

Source hashes at authoring:

- template: `b574e52d6cc6e193ca4a36ec84fe9523d1a3543bfc51bac8b5b49692f04bffbd`
- operation trace checker: `3191d9d661a22120fdf357cd8b1d04c47b57ccc7186d7010abc1af116a7f6197`
- worker-return checker: `692b44359d37b80173b6e0fe5e43f528aead8527fe89ddace7ef55d93b25d074`
- worker-return fast gate: `ba423a8ec9760607672e64d3a549421178efb68d4a8dfbb48561d2f924cd848e`

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044. Origin defects
ADIF-0061 and ADIF-0062 are also binding. Exact manifests, checker read-ahead,
strict literals, protected-path authorization and phase separation address the
returned risks.

## Root Contract

The accepted chain is:

`requirementId -> dispatcher-owned expected artifacts/proofs ->
Git-observed actual artifacts -> return evidence bound by requirementId ->
deterministic reducer -> terminal status`

Mandatory semantics:

1. the work order carries one fenced, strict-JSON requirement ledger;
2. requirement IDs are unique and stable;
3. every mandatory row names at least one expected artifact and proof ID;
4. the return carries one fenced, strict-JSON evidence ledger with exactly one
   row per requirement ID;
5. actual artifacts are compared with Git-observed changes, not trusted from
   worker prose;
6. proof references must resolve to declared proof IDs and existing artifacts
   or exact command-evidence IDs;
7. missing, duplicate, unknown or unparseable rows fail closed;
8. all mandatory rows `PASS` is the only state that permits
   `COMPLETE_PENDING_REVIEW`; otherwise the only allowed state is
   `BLOCKED_WITH_REASON`;
9. the legacy Agent Operation Trace expected manifest may not fail open; and
10. tool/classifier applicability and event fields use exact literals, numeric
    nonnegative counts and cross-field invariants.

## Scope

Allowed: one acceptance-ledger standard/checker/test family; RSE recovery
addendum; bounded template extraction; scaffold projection; existing dispatch,
return and trace checker integration; focused tests; Local worker return and
review evidence.

Forbidden: NCR P10/P11, provider/network calls, UI automation, classifier
bypass, platform interception, public sync, deployment, unrelated refactors,
generated session aggregate edits during material implementation.

## Architecture Decision

Use a dedicated pure-Python acceptance-ledger checker and import its validation
functions into the already wired dispatch and worker-return gates. Keep Git
observation in the checker/reviewer boundary. Do not create a daemon, database,
runtime service or second execution ledger.

## Decision / Baseline / Proposed Tranche

Decision: open exactly RSE-T4-H1-R1 as the root corrective tranche. Baseline:
H1 is rejected and restored at `532e49a72`; ADIF-0062 at `0caf9ac47` controls
the systemic scope. Proposed tranche: strict acceptance ledger plus retained
RSE classifier recovery semantics, followed by Local hostile review and
terminal foundation closure. NCR stays parked.

## Evidence / Verification

Required evidence is the exact work-order ledger, Git-observed changed set,
focused checker tests, template size measurement, H1 mutation replay, a fresh
review-phase hostile probe, worker-return fast gate and committed closure
ranges. Component shape tests alone are insufficient.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | status, exact route, manifest paths, JSON fences, closeability gate IDs, size threshold and protected-path authorization |
| gateRunPurpose | confirmation/evidence after source-first packet authoring |
| claimBoundary | source read-ahead only; no PASS claim before execution |

## Near-Threshold Owner Maintainability Plan

Active entrypoint: `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`.
Current count: 1,181 lines. Hard threshold: 1,200 lines. Extract the detailed
fulfillment/acceptance-ledger rules into a work-order-template addendum and
leave a compact mandatory pointer. Minimum shrink target: 50 lines. The parent
template remains in Allowed scope and must finish below 1,131 lines.

## Acceptance

- strict work-order and return JSON ledgers pass positive fixtures;
- malformed JSON, duplicate/unknown/missing IDs, missing artifact, unbound
  proof, Git mismatch and terminal-status contradiction fail;
- the four H1 classifier mutations fail;
- expected-manifest prose with no parseable path fails closed;
- template shrinks by at least 50 lines;
- focused suites, author/reviewer gates and Local independent hostile probe
  pass;
- no provider, network, public or NCR action occurs.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Lane | Disposition | Control action |
|---|---|---|---|---|
| Acceptance facts are not joined end to end | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | strict ledger checker and reducer |
| Expected manifest can be unparseable and silently skipped | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | fail closed |
| H1 fixed known shapes but missed semantic contradictions | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | chain-first standard plus hostile fixtures |
| Template feasibility was discovered after execution | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | pre-authorized extraction and size assertion |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: exact protected governance paths named by
the paired RSE-T4-H1-R1 work order, including template extraction and checker
integration. Protected paths: the paired packet, work-order template/addendum,
RSE reference, scaffolds, acceptance/dispatch/return/trace checkers, fast gate,
their focused tests, Local return and completion evidence. Operator
authorization: explicit instruction for Local to execute the foundation repair
fully before NCR. Rollback boundary: revert only RSE-T4-H1-R1 material;
preserve H1 rejection evidence, ADIF-0061/0062 and all NCR P9 truth.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline authorizes repository-local governance contracts, checkers and
tests only. It does not control an external classifier, prove universal agent
compliance, reopen NCR, or authorize provider/live/public/deployment effects.
