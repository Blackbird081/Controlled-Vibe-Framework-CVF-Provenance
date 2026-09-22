# CVF GC-018 Baseline - High-Risk Local Transaction Proof Foundation T1

Memory class: governed-dispatch-baseline

Status: AUTHORIZED_FOR_DISPATCH

Batch ID: CVF-HRLTP-T1

Dispatch base head: `6fc501439a96b1023aacab06a6937e7bf2677f20`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT`

## Purpose

Convert the repeated ACEL local-transaction proof failures into a reusable CVF
rule, machine check, focused tests, and the earliest relevant local hook. The
foundation must reject evidence that substitutes mutex shape, timeout, or
textual ACL equality for a real competing process, exception-safe ownership,
semantic security restoration, and immutable final evidence.

## Authority And Learning Trigger

The operator approved foundation uplift after the ACEL G1 T3C-C1 AR1 review.
The accepted AR1 closure exposed four reusable defect classes:

1. a mutex-shaped test did not prove exclusion of a real second writer;
2. failure immediately after acquisition could strand the transaction guard;
3. ACL rollback compared an incomplete representation rather than the full
   security state;
4. a return could be edited after its reported final validation digest.

Per `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`,
the justified response is a written rule, a machine check, and early autorun
enforcement. This baseline authorizes that bounded conversion only.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-HRLTP-T1 --title "High-Risk Local Transaction Proof Foundation T1" --date 2026-09-22 --base 6fc501439 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with the accepted AR1 defect classes, bounded implementation manifest, evidence contract, source verification, and claim boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | `High-Risk Local Transaction Proof Applicability`; `transactionTarget`; `productionPathPeer`; `deterministicBarrierProtocol`; `enteredBeforeReleaseOracle`; `postAcquireFailureInjection`; `semanticSecurityTuple`; `rollbackExactness`; `finalEvidenceHashBinding`; `independentProbeRequired` |
| claimBoundary | Dispatch design provenance only; no implementation or runtime behavior is claimed. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-guard-authoring`, role=`INTERNAL_AGENT`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "governance-guard-authoring" --role INTERNAL_AGENT --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No registered ADIF entry changes this bounded implementation contract. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Checker Source Read-Ahead Block; Source Verification Block; Core Guard Self-Protection Authorization; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; WORKER_MUST_NOT_COMMIT |
| gateRunPurpose | Confirmation evidence after source read-ahead, not first discovery. |
| claimBoundary | Applies to dispatch shape only; implementation must read its new checker and tests before return authoring. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Repeated non-obvious defects should become a written rule, machine check, then earliest autorun gate. | EXISTS | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | learning sequence | rule-to-check-to-gate sequence | CVF learning philosophy | ACCEPT |
| AR1 required a real same-writer peer and deterministic barrier proof. | EXISTS | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md` | acceptance criteria | peer/barrier requirements | ACEL AR1 work order | ACCEPT |
| AR1 closure records post-acquire cleanup, semantic DACL restoration, and stable return digest evidence. | EXISTS | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` | findings and verification | AR1 correction evidence | accepted worker return | ACCEPT |
| Protected compatibility checkers require explicit Core Guard authorization. | EXISTS | `governance/compat/check_core_guard_self_protection.py` | protected-path logic | `governance/compat/` | Core Guard checker | ACCEPT |
| Reviewer-fast, pre-commit, and pre-push command lists are separately owned catalogs. | EXISTS | `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` | command list declarations | `REVIEWER_FAST_CHECKS`; `PRE_COMMIT_CHECKS`; `PRE_PUSH_CHECKS` | local governance hook catalogs | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned baseline, work order, standard, and checker paths | `Test-Path` returned `False` for all four paths before authoring. | PASS |
| Existing rule collision | `rg` found only the tranche-specific post-acquire requirement in the ACEL AR1 work order and no reusable high-risk transaction proof standard/checker. | PASS |
| Collision decision | Create a new reusable rule; do not modify the closed AR1 evidence. | PASS |

## Architecture Decision

Use an explicit opt-in applicability marker on current work orders, backed by
risk-token detection that requires the author to declare either `REQUIRED` or
`NOT_APPLICABLE_WITH_REASON`. For `REQUIRED`, the checker must validate a
machine-readable contract containing all nine proof fields. This avoids
retroactively failing historical packets while preventing new high-risk work
from silently omitting the proof plan.

The checker enters `reviewer-fast`, `pre-commit`, and `pre-push`. Reviewer-fast
is the earliest relevant admission point because the contract governs both
dispatch quality and returned evidence. The general hook runner remains
unchanged because its command catalogs are already extracted owners.

## Decision

Authorize one bounded implementation tranche using the exact manifest in the
paired work order. Reviewer acceptance requires machine enforcement and
adversarial tests; prose-only guidance is insufficient.

## Required Evidence

- focused checker tests covering every trigger and every required field;
- membership evidence for reviewer-fast, pre-commit, and pre-push;
- aggregate worker-return fast-gate output;
- exact changed-set reconciliation;
- stable worker-return SHA-256 before and after the final gate;
- reviewer-owned independent probe left pending at worker return.

## Acceptance Boundary

The implementation is accepted only when focused positive and adversarial
tests prove:

- a risk-bearing packet without an applicability disposition fails;
- a `REQUIRED` packet missing any proof field fails;
- a reasoned non-applicable packet passes only when no high-risk trigger is
  present;
- a complete required contract passes;
- all three hook catalogs contain the checker;
- the worker return records a reviewer-independent probe disposition and a
  final evidence hash before and after the final gate with no intervening edit.

## Claim Boundary

This baseline authorizes a documentation-and-machine-governance foundation.
It does not prove any target transaction implementation, Windows ACL behavior,
provider call, production readiness, public export, or live execution.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Private repository governance documentation and static checker design only. |
| claimDisposition | CLAIM_REJECTED: no target runtime execution or interception is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | No provider, live, public, or target-runtime invocation. |
| interceptionBoundary | No direct interception or mandatory runtime wrapper. |
| claimLanguage | Authorization baseline, not implemented behavior. |
| forbiddenExpansion | No ACEL runtime, provider, public, Web, MCP, or production expansion. |

## Current Runtime Freshness Verification

| Field | Disposition |
| --- | --- |
| Runtime/source paths checked | Accepted AR1 work order and return, current work-order template, Core Guard checker, and extracted hook catalogs. |
| Runtime behavior claimed | N/A_WITH_REASON: baseline authorizes repository governance only. |
| Helper/checker implementation claimed | NOT_IMPLEMENTED_YET: worker implementation is the next bounded phase. |
| Provider/live proof claimed | N/A_WITH_REASON: no provider or live call. |
| Public-sync claimed | N/A_WITH_REASON: deferred private-only. |
| Freshness disposition | PASS for dispatch authority; no target-runtime freshness or safety claim. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance governance hardening tranche; no public
artifact or public-sync mutation is authorized.
