# CVF GC-018 Baseline - MFRP P4-C1 Automatic Evidence Collection

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION

Dispatch base head: `a0ca90e3486ca80a1f0a3ba94906c763cba00470`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer at returned-result boundary or declared safety trigger

Worker target: bounded local implementation worker

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Amendment 1 - Reviewer-Local Reachable Receipt Repair

Status: OPERATOR_AUTHORIZED_REVIEWER_LOCAL_REPAIR

Operator authorization: 2026-09-02 exact instruction to expand the returned
review change set from nine to eleven paths, keep repair reviewer-local, and
allow one post-commit local autorun receipt generation without redispatch.

The post-commit collector may invoke the existing
`run_agent_autorun_workflow_gate.py` exactly once when the current commit's
sole parent contains one eligible trusted return. The current commit is the
ordinary dedicated continuity sync: the autorun phase is `pre-closure`, base
is the trusted return commit's sole parent, and head is the current continuity
commit. This avoids the unavoidable active-session drift between material and
continuity commits while preserving trusted-record-before-machine order. The
resulting existing-family P2 receipt is validated and passed to the existing
P4 append owner. This is one internal subprocess inside the already-budgeted
collector command, not a second review, daemon, watcher, queue or provider
call.

The trusted outcome must come from an explicit committed
`Reviewer disposition:` inside an `Independent Reviewer Adjudication`
section. `Status: COMPLETE_PENDING_REVIEW` and other worker readiness tokens
are never trusted dispositions.

Receipt selection binds the exact generated pre-closure path, exact
pre-material-parent through continuity-head range, receipt integrity,
verifier identity and committed Git blob fingerprint. Other stale phase
receipts in the runtime directory are irrelevant, not competing candidates.
Generation failure, trust/order drift, fingerprint mismatch or a safety
trigger writes the unresolved marker and does not increment the sample.

Reviewer-local changed-set authority is exactly the original nine paths plus
this baseline and its paired work order: eleven total. P2 sources and P4
owners remain read-only.

## Purpose

Open P4-C1 as a bounded automatic collector for naturally occurring MFRP
shadow-canary evidence. Preserve the trusted route as controlling, avoid
per-return review, and make the M5, M10, M20, P5 and P6 reopen conditions
durable across sessions.

## Decision / Baseline

Implement one local Git post-commit collector. It may consume only an
already-valid P2 receipt and one newly committed, uniquely identified phase
return whose trusted disposition already exists in the commit. It writes only
an ignored pending journal and safety marker; checkpoint promotion remains a
reviewer/closer action at M5, M10, M20 or an admitted safety trigger.

No daemon, watcher, queue, provider call, network call, P2 schema mutation,
phase-work manufacture, semantic re-execution or new receipt family is
authorized.

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
| --- | --- | --- |
| accepted P4 return | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md`; SHA-256 `e779eabf09787e0642bac5cb48a9b0557365eb53ae6bd0e4bfcfd5c42010d176` | ACCEPT |
| sample-gated reopen amendment | `docs/baselines/CVF_MFRP_P4_SAMPLE_GATED_P5_REOPEN_AMENDMENT_2026-09-02.md`; SHA-256 `66dc6be0b1c8b0de7ffd7d652e9d4525064d55ce62be8ffd42bdda95a6f0b58d` | ACCEPT |
| existing P2/P4 seams | named functions in the paired work order Source Verification Block | ACCEPT |

## Scope / Target / Owner Boundary

The baseline owns only the P4-C1 dispatch contract. Worker scope is the exact
nine-path manifest; reviewer/closer owns adjudication, commit, checkpoint
promotion and session sync. P2, accepted P4 evidence and P5/P6 authority are
read-only.

## Order Of Record And Trust Boundary

The trusted disposition must be committed before the post-commit hook reveals
a machine outcome. The collector proves only receipt-local linkage and
consistency over the P2/P4 overlap; it never converts agreement into
correctness or authority.

The pre-commit receipt's `worktreeFingerprint` must equal a fingerprint
reconstructed from immutable Git blobs for the committed range. Receipt
integrity, verifier identity, base/head ancestry, unique return selection and
declared metadata must all pass. Missing, ambiguous, stale or mismatched inputs
produce an explicit skip code and do not increment `eligibleCount`.

## Pending Evidence Boundary

The automatic collector starts from the committed P4 evidence ledger and writes
a repository-bounded ignored pending journal under
`.cvf/runtime/mfrp-p4-shadow-canary/`. Each accepted row embeds the validated
receipt content/digest and immutable Git identities. The runtime path is not
the durable evidence owner; at a checkpoint, reviewer/closer independently
reconciles and promotes accepted rows into the existing governed P4 ledger.

A safety condition writes an unresolved marker in that same ignored directory.
The next pre-commit must fail closed while the marker exists. Only
reviewer/closer adjudication may clear it; post-commit itself never rewrites or
reverts a trusted commit.

## Eligible Return Metadata

Reuse the existing worker-return artifact. The scaffold gains one optional
`P4 Automatic Evidence Observation Block` with exact scalar fields for:
eligibility, seven-phase label, hard-obligation locator and pattern, and
source-authority locator. This is observation metadata, not a second packet or
an authority claim.

The trusted disposition is reviewer/closer-owned and must already be present in
the committed return. Exactly one eligible return is allowed per collection
event. Zero or multiple candidates are recorded as skipped without guessing.

## Review Admission And Governance Tax

There is no pre-execution review and no routine review per collected row.
Reviewer work is admitted only at M5, M10, M20 or by an existing P4 safety
trigger. Small evidence-determined repairs at review remain reviewer-local
under the Review Cost standard; implementation is not recreated.

One post-commit collector invocation is the maximum marginal shadow command per
eligible return. Ineligible commits terminate after bounded identity/metadata
inspection and do not invoke the P4 comparator.

## Reopen Chain

| Gate | Exact condition | Effect |
| --- | --- | --- |
| P4-C1 collection active | implementation accepted and committed; hook installed through the existing hook path | natural collection may run |
| M5 | `eligibleCount >= 5` or safety trigger | one bounded checkpoint review |
| M10 | `eligibleCount >= 10` or safety trigger | one bounded checkpoint review |
| M20 | `eligibleCount >= 20` | final sample checkpoint may be adjudicated immediately |
| day 30 with fewer than 20 | calendar sunset reached and `eligibleCount < 20` | `INSUFFICIENT_EVIDENCE`; P5 remains closed |
| P5 | M20 plus safety, audit, recall, evidence-quality and governance-tax gates pass in a separate reviewer decision | selective Core activation may open |
| P6 | P5 Core closure accepted and downstream release explicitly recorded | bounded seven-phase/downstream adoption may open |
| project/workspace application | P6 adoption evidence accepted | project-specific update may be separately authorized |

Calendar waiting is not required after M20. No row, checkpoint or elapsed date
automatically opens P5 or P6.

## Required Artifact Manifest

| Path | Action |
| --- | --- |
| `.githooks/post-commit` | CREATE bounded collector launcher |
| `.githooks/pre-commit` | MODIFY unresolved-safety-marker fail-closed check |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | CREATE collection owner |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | CREATE hostile and integration tests |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | MODIFY optional observation block |
| `governance/compat/run_worker_return_scaffold.py` | MODIFY same optional observation block |
| `governance/compat/test_run_worker_return_scaffold.py` | MODIFY parity tests |
| `scripts/install-cvf-git-hooks.ps1` | MODIFY installed-hook disclosure |
| `docs/reviews/CVF_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_WORKER_RETURN_2026-09-02.md` | CREATE worker return; reviewer adjudication/repair evidence in place |

Worker equality remains the original nine paths. Amendment 1 reviewer-local
equality is exactly those nine plus this baseline and paired work order,
eleven total. No deletion or rename is authorized.

## Acceptance Boundary

Implementation must prove: valid natural linkage increments once; duplicate,
ambiguous, stale, tampered, rebound and fingerprint-mismatched inputs do not;
safety markers block the next commit; ordinary irrelevant commits remain
non-blocking; P4 comparator ownership is reused; pending journal writes are
atomic and deterministic except declared timing fields; and no provider,
network, live or public effect occurs.

## Evidence / Verification

Require exact changed-set equality, focused tests twice, pre-implementation
and pre-closure autorun receipts, Git ancestry/blob evidence, deterministic
skip/append behavior, unresolved-marker proof, zero provider/network calls and
worker no-stage/no-commit evidence.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION --title "MFRP P4-C1 Automatic Evidence Collection" --date 2026-09-02 --base a0ca90e3486ca80a1f0a3ba94906c763cba00470 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with P4-C1 trust, collection, reopen, manifest and verification contracts |
| checkerReadAheadConfirmation | checker sources listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | P4 observation metadata names only; runtime ownership deferred to implementation |
| claimBoundary | dispatch provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`protected governance path implementation`,
role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "protected governance path implementation" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned zero items |
| Dispatch impact | no additional defect-specific constraint |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Claim Boundary; Public Export Disposition |
| gateRunPurpose | confirmation of baseline evidence after checker source read-ahead |
| claimBoundary | bounded to this dispatch baseline |

## Claim Boundary

This baseline authorizes only P4-C1 local automatic evidence collection and its
tests. It does not activate P5, P6, any seven-phase route replacement, or any
project/workspace rollout.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance implementation; no public-sync authorization.
