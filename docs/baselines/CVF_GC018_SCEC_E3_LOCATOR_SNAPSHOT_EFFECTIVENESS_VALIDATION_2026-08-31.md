# CVF GC-018 Baseline - SCEC-E3 Locator Snapshot Effectiveness Validation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SCEC-E3

Dispatch base head: `8db4e9f87e4f4d63f0844e368dd4d80cf6fed3ba`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Run one bounded independent effectiveness validation of the SCEC locator-to-
content and single-snapshot control accepted at `008ff0685`. This is the
terminal foundation evaluation for the named defect, not a GC010 or product
tranche.

## Root Problem

SCEC-E2 exposed an unbound locator. T1-R3 fixed that gap, and independent review
then found two proof defects: the worker used synthetic rather than exact E2
evidence, and shared evidence paths were resolved more than once. The accepted
repair caches one byte snapshot per path across a validation tree. E3 must now
test the accepted behavior from fresh adversarial cases without editing it.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Invariant 13 requires strict UTF-8, canonical exact-unique locators, and one cached byte snapshot per evidence path per validation tree. |
| `governance/compat/check_semantic_convergence_control.py` | Accepted implementation owns snapshot caching, hash validation, locator resolution, and predecessor revalidation. |
| `docs/reviews/CVF_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_WORKER_RETURN_2026-08-31.md` | Reviewer accepted T1-R3 with exact E2 and shared-path repairs at `008ff0685`. |
| `governance/compat/test_check_semantic_convergence_control.py` | Focused 119/119 regressions are implementation evidence, not the E3 oracle. |

## Decision / Baseline

The worker must construct a fresh ephemeral harness independent of committed
test payloads. It must exercise both pure validator injection and the real
repository evidence resolver where applicable. Required families are:

1. the exact E2 artifact, immutable digest, and absent locator;
2. two bindings sharing one path with a changing resolver, proving one read;
3. a second locator available only in a resolver's second snapshot, proving no
   split-view acceptance;
4. predecessor and successor bindings sharing a path across one validation
   tree, proving cache inheritance;
5. absent, ambiguous, non-canonical, invalid-UTF-8, unreadable/non-file, and
   hash-mismatch negatives with exact codes and no misleading cascade;
6. valid accepted-review, executable-proof, shared-path, and predecessor
   controls.

Allowed verdicts are exactly:

- `EFFECTIVE_CLOSE_FOUNDATION_LOOP`
- `EFFECTIVE_WITH_ONE_NAMED_RESIDUAL`
- `INEFFECTIVE_REOPEN_FOUNDATION`

Any required negative accepted, valid control rejected by a real contract
defect, second resolver read for one path in one validation tree, or missing
exact E2 replay forces `INEFFECTIVE_REOPEN_FOUNDATION`. A non-bypass residual
may select the middle verdict only when precisely bounded. Every verdict keeps
`successorTrancheOpened: NO`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Locator binding is exact-unique and addressability-only | contract | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | invariant 13; Resolution Evidence | `resolutionEvidence` | SCEC standard | ACCEPT |
| One cache is created and threaded through predecessor validation | executable source | `governance/compat/check_semantic_convergence_control.py` | `validate_block`; `_validate_resolution_evidence` | `_evidence_snapshot_cache` | SCEC checker | ACCEPT |
| Repository reads safe file bytes | executable source | `governance/compat/check_semantic_convergence_control.py` | repository resolver | `_repo_evidence_bytes_resolver` | SCEC checker | ACCEPT |
| T1-R3 required reviewer repair | accepted review | `docs/reviews/CVF_SCEC_T1_R3_LOCATOR_TO_CONTENT_EVIDENCE_BINDING_HARDENING_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction | shared-path cache and exact E2 replay | T1-R3 review | ACCEPT |
| Focused tests pass but do not replace independent evaluation | regression source | `governance/compat/test_check_semantic_convergence_control.py` | `ResolutionEvidenceBindingTests` | 119-test suite | SCEC tests | ACCEPT |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/assessments/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_2026-08-31.md` | CREATE ten-question analysis, fresh case matrix, resolver-call ledger, verdict, and boundary |
| `docs/reviews/CVF_SCEC_E3_LOCATOR_SNAPSHOT_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md` | CREATE full no-commit return with a checker-valid ordinal-1 successor SCEC block |

No other path may change.

## Acceptance Strategy

Acceptance requires fresh case construction, exact expected-versus-observed
codes, resolver call counts, all positive controls, one mechanical verdict,
zero source edits, zero provider/network use, and an exact two-path uncommitted
manifest. Test pass means declared-evidence addressability works; it never
proves cited semantics true.

## Evidence / Verification

Run pre-implementation, focused SCEC, direct checker, fresh harness,
worker-return fast gate, diff hygiene, and exact status. No live/provider proof
is applicable.

## Negative Search And Collision Discipline

- Search roots: repository root with coverage across source, tests, docs, JSON,
  and external-evidence references.
- Search command: `rg -n "SCEC_E3|CHANGING_SHARED_PATH|CROSS_PREDECESSOR_SNAPSHOT" governance docs`.
- Structured query: exact output-path existence checks at dispatch base.
- Same-token collision result: generic snapshot language exists as accepted
  context; no competing E3 artifact or owner occurrence was found.
- Disposition: `ABSENT_E3_OUTPUTS_CONFIRMED`; contextual occurrences do not bind
  or replace the two new validation outputs.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring dispatch SCEC effectiveness validation`, role=`dispatcher`, lifecyclePhase=`dispatch`

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring dispatch SCEC effectiveness validation" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defects: `NONE_RETURNED`
- Disposition: direct read of ADIF-0055 remains required.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; Source Verification columns; active SCEC fields; prompt-envelope labels; worker-return headings |
| gateRunPurpose | Confirm the completed packet against source-read contracts, not discover structure by failure. |
| claimBoundary | Dispatch shape only; effectiveness remains pending independent evidence. |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SCEC-E3 --title "Locator Snapshot Effectiveness Validation" --date 2026-08-31 --base 8db4e9f87 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --scec-problem-key scec-locator-snapshot-effectiveness-validation --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | generic external no-commit validation profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Exact T1-R3 authority, split-view matrix, terminal verdicts, and two-path scope replace placeholders. |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | case IDs, resolver-call ledger, effectiveness verdict |
| claimBoundary | Dispatch provenance only. |

## Claim Boundary

This baseline authorizes only two SCEC-E3 validation documents. It authorizes
no checker/test/source change, GC010 or product work, provider/live activity,
public sync, deployment, production, or automatic successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation-effectiveness validation.
