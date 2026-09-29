# CVF GC-018 Baseline - TPGR-R5 Shadow Command Applicability And Receipt Invalidation Design

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: TPGR-R5

Dispatch base head: `dbaae72776ca6e50ae73a4e3baac327de1ef9ce5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: CVF reviewer/orchestrator

Worker target: delegated design worker

## Purpose

Design, without implementing, the smallest command-applicability and receipt-
invalidation contract that could make R4's eight-field shadow interface
machine-checkable later without creating a second command catalog, receipt
store, lifecycle, or router.

## Authorization / Source

R4 is independently accepted at
`dbdc0888e5c80cc507fb819d569a58083c2a533e` with final disposition
`PROCEED_TO_R5_SHADOW_COMMAND_AND_RECEIPT_INVALIDATION`. The operator's
standing CVF-governed authorization permits this fresh documentation-only R5
dispatch. It does not authorize implementation.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R4 accepted material | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md`; `docs/reviews/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_WORKER_RETURN_2026-08-18.md`; commit `dbdc0888e` | RELEASED |
| R4 closure continuity | `CVF_SESSION/state/entries/tpgrR4ShadowInterfaceAndClaimVocabularyDesignClosed20260818.json`; commit `dbaae7277` | RELEASED |
| selective execution | TPGR remains shadow-only and legacy bundle remains mandatory | NOT_AUTHORIZED |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id TPGR-R5 --title "Shadow Command Applicability And Receipt Invalidation Design" --date 2026-08-18 --base dbaae72776ca6e50ae73a4e3baac327de1ef9ce5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with R5 source evidence, exact design contract, exact four-path lifecycle, hostile cases, and role boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| docOnlyNewFields | `commandApplicability`, `receiptOwnerRef`, `invalidationEvent`, `invalidationScope`, `recomputeFromNode`, `historicalDisposition` |
| claimBoundary | dispatch provenance only; no command, checker, receipt schema, runtime, provider, public, Web, or MCP behavior is implemented |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: 22; not truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | exact source paths, checker read-ahead, no-commit ownership, exact manifest, one-pass review graph, and no authority aggregation are mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch-ready status, Source Verification columns, scaffold fields, baseline structural groups, no-commit terms, task routing JSON block, and allowed worker-return status/headings |
| gateRunPurpose | confirm dispatch shape after source-led authoring, not discover requirements |
| claimBoundary | structural conformance evidence only; semantic correctness remains reviewer-owned |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R5 is the accepted next design step | predecessor disposition | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Final Disposition; R5 Candidate Command/Receipt Invalidation Manifest | assessment path | R4 reviewer-accepted design | ACCEPT |
| eight-field interface and exact vocabulary remain binding inputs | design contract | `docs/assessments/CVF_TPGR_R4_SHADOW_INTERFACE_AND_CLAIM_VOCABULARY_DESIGN_2026-08-18.md` | Shadow Interface Field Table; Exact Claim Vocabulary; Independent repair reflected in corpus proof and hostile cases | assessment path | R4 design | ACCEPT |
| current command universe has one canonical autorun catalog | current implementation fact | `governance/compat/agent_autorun_command_catalog.py` | command catalog definitions | `_common_commands` | autorun command catalog | ACCEPT |
| TPGR remains shadow-only | authority fact | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock; Activation Rule | standard path | TPGR standard | ACCEPT |
| external critique is advisory only | authority boundary | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Reconciliation Matrix; Generalized Architecture Boundary | reconciliation path | accepted CVF reconciliation | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| exact four R5 paths | `Test-Path` returned false for baseline, work order, assessment, and worker-return targets before authoring | PASS |
| namespace collision | `rg -n "TPGR_R5_SHADOW_COMMAND_APPLICABILITY_AND_RECEIPT_INVALIDATION_DESIGN" docs CVF_SESSION` returned no prior artifact | PASS |
| collision decision | exact new namespace available | CREATE_NEW |

## Design Contract

R5 must design by reference only:

- a command-applicability matrix for each R4 field/token invariant, using the
  existing autorun catalog as the only command-universe owner;
- applicability values exactly `ALWAYS`, `CONDITIONAL`, or
  `NOT_APPLICABLE_WITH_REASON`, with objective predicates and fail-closed
  behavior;
- receipt ownership and invalidation-event semantics without a new receipt
  store or schema implementation;
- earliest-affected-node invalidation, immutable historical evidence, and
  fresh-evidence re-earning rules;
- a dependency graph showing which standard/checker/catalog/owner changes
  expire which shadow claims;
- false-positive controls so descriptive prose and historical archives do not
  become accidental claim assertions;
- a zero-edit R6 candidate manifest and one allowed final disposition.

R5 must not design selective omission as active behavior. All current gates
continue to run through `RUN_FULL_LEGACY_BUNDLE`.

## Proposed Tranche

One no-commit external design worker creates exactly the two output paths
named in the work order. The reviewer independently verifies semantics,
repairs only within those two paths, and owns commit and continuity.

## Evidence / Verification

Evidence must include exact command catalog owner references, R4 field/token
coverage reconciliation, hostile-case outcomes, invalidation precedence,
zero-edit path manifest, actual worktree status, worker-return fast gate, full
pre-implementation gate, and no-commit proof.

## Stop Conditions

Return revision, narrowing, or stop if R5 creates a second command catalog or
receipt store; lets a worker select applicability or current eligibility;
allows a stale receipt to remain current after an owner/checker/source change;
uses terminal ledger disposition as semantic-read proof; enables selective
execution; cannot define false-positive boundaries; or exceeds the existing
Layer A evidence cost it is meant to route.

## Allowed Final Dispositions

- `PROCEED_TO_R6_SHADOW_REPLAY_AND_MIGRATION_DESIGN`
- `REVISE_R5_COMMAND_RECEIPT_DESIGN`
- `NARROW_TO_RECEIPT_INVALIDATION_ONLY`
- `STOP_TPGR_SECOND_UPGRADE`

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/orchestrator as dispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | TPGR-R5 dispatch authoring, 2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold preview, resolver, collision checks, apply_patch, gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | R4 accepted disposition plus standing operator authorization |
| Before status evidence | clean at `dbaae72776ca6e50ae73a4e3baac327de1ef9ce5` |
| After status evidence | exactly two dispatch artifacts before material commit |
| Diff evidence | `git diff --name-status`; untracked paths via `git status --short` |
| Approval boundary | documentation-only R5 dispatch |
| Claim boundary | no implementation or external effect |
| Agent type | internal reviewer/orchestrator |
| Invocation ID | `tpgr-r5-dispatch-2026-08-18` |
| Expected manifest | this baseline; paired work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R5 documentation-only dispatch |
| claimDisposition | CLAIM_REJECTED: no runtime execution-control or selective-command behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two governed dispatch artifacts are authored and checked |
| invocationBoundary | local documentation and governance gates only |
| interceptionBoundary | no direct interception, wrapper, proxy, runtime gate, or agent coding control |
| claimLanguage | candidate design authority only |
| forbiddenExpansion | no standard/checker/registry/catalog/hook mutation, source intake, runtime/provider/live/public/deploy/production action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; public sync is outside scope.

## Claim Boundary

This baseline authorizes only the two-file R5 design return. It does not
authorize implementation, command omission, checker edits, receipt persistence,
R6-R9, T15, source intake, runtime, provider/live, public sync, deployment, or
production.
