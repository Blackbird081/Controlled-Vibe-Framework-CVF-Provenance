# CVF GC-018 Baseline - EAFR-R5 Retrieval Evidence Semantics And Admission Boundary

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R5-RETRIEVAL-EVIDENCE

Dispatch base head: `7b61a4473d2a55b818ea03c0b0f62229cf9d524a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer owner: current independent orchestrator/reviewer

Worker target: retrieval-policy boundary worker role

## Purpose

Record one bounded retrieval-evidence semantics verdict and make admitted
retrieval evidence fail closed on malformed trust metadata without weakening
the existing actor, scope, privacy, lifecycle, summary-only, or reinjection
boundaries.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R5 --title "Retrieval Evidence Semantics And Admission Boundary" --date 2026-08-25 --base 7b61a4473 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified owner reconciliation, exact eight-path manifest, semantics verdict, adversarial matrix and deterministic proof |
| checkerReadAheadConfirmation | dispatch, authority, trace, delta, epistemic and worker-return checker sources reviewed |
| docOnlyNewFields | Retrieval Evidence Semantics Verdict; Admission And Ranking Order; Adversarial Proof Matrix |
| claimBoundary | dispatch authoring only; no live, provider, public, deployment, adapter or reinjection claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R4 | `docs/reviews/CVF_EAFR_R4_PRIVATE_PROVIDER_CURRENT_CLAIM_MANIFEST_RECONCILIATION_COMPLETION_2026-08-25.md`; material commit `55d48516689e60332e7efd4e07286ab3c03c8336` | RELEASED |
| EAFR roadmap | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, R5 objective and acceptance rule | ACCEPT |
| existing memory-foundation owner | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md`, Memory Access Gate Rules | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`retrieval evidence semantics`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "retrieval evidence semantics" --role worker --lifecycle-phase implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest; no-commit status; trace labels; Public Export Disposition |
| gateRunPurpose | confirm as evidence that the source-verified dispatch already matches required shape |
| claimBoundary | structural conformance does not prove implementation correctness |

## Current Runtime Freshness Verification

Verified at HEAD `7b61a4473d2a55b818ea03c0b0f62229cf9d524a`:

- `matchesQuery` is a case-insensitive contiguous substring check over summary
  plus optional content; a trimmed empty query matches every otherwise eligible
  candidate;
- actor denial runs before retrieval, while scope, secret and blocked-lifecycle
  filters run before relevance and ranking for ordinary retrieval methods;
- caller-supplied `auditTrust` is not checked for finiteness or range in the LPF
  policy, and the HTTP route checks only JavaScript number type;
- `audit_trust` ranking uses descending caller-supplied trust then creation time;
- the readout strips content and fixes `rawMemoryReleased=false` and
  `canReinject=false`.

No live or provider call is required or authorized. R5 proves local admission
semantics and does not claim hostile admission, privilege gain, downstream
action, exploitability, provider behavior, or production exposure.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R5 requires a bounded design verdict plus executable proof | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | tranche row and acceptance criteria | EAFR-R5 | EAFR roadmap | ACCEPT |
| existing T1 owns memory read-gate doctrine | OWNER_AUTHORITY | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md` | Memory Access Gate Rules | read gate categories | memory foundation T1 contract | ACCEPT |
| owner matrix forbids duplicate receipt/gate owners | OWNER_RECONCILIATION | `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md` | Reconciliation Matrix rows 73 and 80 | retrieval receipt and access gate rows | memory foundation owner matrix | ACCEPT |
| lexical match is a relevance heuristic | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | `matchesQuery` | matchesQuery | LPF retrieval policy | ACCEPT |
| trust ranking currently accepts unchecked numbers | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | candidate interface and audit-trust sorter | auditTrust | LPF retrieval policy | ACCEPT |
| HTTP route performs type-only trust validation | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | candidate parser | auditTrust | memory readout route | ACCEPT |
| readout remains summary-only and non-reinjecting | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | sanitizer | rawMemoryReleased; canReinject | Web readout projection | ACCEPT |
| workflow passes candidates to the LPF retrieval policy after gateway admission | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | `runMemoryRuntimeWorkflowChain` | evaluateRetrievalRequest | LPF runtime workflow | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R5 baseline, work-order and return paths | all absent before authoring | PASS |
| EAFR-R5 search | only roadmap and continuity next-move references existed | PASS |
| collision decision | enrich the stable T1 contract and matrix; do not create a second retrieval-admission contract | PASS |

## Retrieval Evidence Semantics Verdict

1. `matchesQuery` is relevance selection only. A lexical hit is not admission
   authority, trust proof, truth proof, hostility proof, or permission to act.
2. `auditTrust` is bounded ranking metadata only. It must be a finite number in
   `[0,1]` before a candidate can enter any selected retrieval evidence set.
3. Actor authorization precedes candidate admission. Scope, secret/privacy,
   blocked lifecycle and valid-trust checks precede relevance and ranking.
4. Invalid candidate trust is excluded with stable reason
   `invalid_audit_trust`; it is never coerced, clamped, ranked, packaged or
   returned as admitted evidence.
5. The HTTP route rejects the whole malformed request with HTTP 400 before
   workflow construction. Boundary values `0` and `1` are accepted.
6. Existing graph/KGR evidence may be selected only when its derived
   `auditTrust` also satisfies the same finite closed interval. This does not
   authorize new graph route wiring.
7. Readout projection continues to strip raw content and return
   `rawMemoryReleased=false`, `canReinject=false`.

## Admission And Ranking Order

```text
actor gate -> candidate scope/privacy/lifecycle/trust admission
           -> method relevance selection -> method ranking -> result cap
           -> summary-only packaging/readout
```

Ranking never retroactively satisfies an earlier admission gate.

## Exact Worker Manifest

1. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
2. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts`
5. `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_SOURCE_DERIVED_REPLAY_CONTRACT.md`
6. `docs/reference/memory_foundation/CVF_MEMORY_FOUNDATION_OWNER_SURFACE_RECONCILIATION_MATRIX.md`
7. `docs/reference/CVF_MEMORY_PLANE_MAP.md`
8. `docs/reviews/CVF_EAFR_R5_RETRIEVAL_EVIDENCE_SEMANTICS_AND_ADMISSION_BOUNDARY_WORKER_RETURN_2026-08-25.md`

## Baseline Decision / Proposed Tranche

Dispatch one exact eight-path, no-commit local tranche. Any need for an owner
file outside this manifest, new route wiring, receipt schema implementation,
checker mutation, package change, external adapter, live proof, key access or
public effect returns blocked to the orchestrator.

## Evidence / Verification

The worker must return focused LPF and route tests, both package typechecks,
safe non-live package suites with pre-existing debt separated from R5
regressions, exact changed paths, pinned-input hashes, bounded semantic
searches, worker-return fast gate, unchanged HEAD and empty staging. The
reviewer independently recomputes material proof.

## Risk / Rollback

Primary risk is accidentally treating relevance or caller trust as authority,
or broadening R5 into graph/reinjection/provider behavior. Rollback is the exact
eight-path pending worker diff.

## Claim Boundary

This baseline authorizes only bounded local retrieval-policy and authenticated
readout-route admission hardening, focused deterministic proof, and
reconciliation of the three existing owner/navigation documents. It authorizes
no live/provider/network/key action, hostile exploit claim, new receipt runtime,
vector storage, graph route wiring, prompt reinjection, external CLI/MCP,
public sync, deployment, push, R1C, R6 or RFR work.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-boundary reconciliation; public-sync is
separately governed.
