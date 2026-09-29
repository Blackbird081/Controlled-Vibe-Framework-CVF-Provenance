# CVF GC-018 Baseline - QBS Lineage Reconciliation R1

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-QBS-LINEAGE-R1

dispatchBaseHead: `4494d6cce`

rawMemoryReleased: false

## Purpose

Authorize one bounded provenance-owned reconciliation of QBS contracts whose
tests remain in the public projection after later projection commits replaced
their paired runtime implementation. The public repository is evidence only;
current provenance source and this packet are the implementation authority.

## Baseline Decision

Decision: `QBS_LINEAGE_RECONCILIATION_R1_AUTHORIZED_BOUNDED`

The operator explicitly confirmed this tranche on 2026-08-05. Authority covers
only local runtime/source reconciliation, focused offline tests, review, and
provenance closure. It does not authorize a QBS benchmark rerun, provider call,
live proof, downstream mutation, governance-latency work, or public export.

## Scope / Applies To

Allowed provenance paths are the fifteen source/test paths named in the paired
work order plus its worker-return artifact. The sibling public-sync clone stays
read-only throughout implementation and review.

## Operator Authority Amendment - Alibaba Live Evidence

On 2026-08-05 the operator explicitly authorized Alibaba API-key live testing
to obtain real evidence. This supersedes the earlier no-live boundary only for
one targeted QBS ALLOW proof with a one-call ceiling, secret-safe diagnostics,
and no benchmark rerun. It does not authorize public mutation, downstream
mutation, broad live suites, or provider comparison.

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | explicit operator confirmation after the proposed QBS lineage-reconciliation tranche |
| Current source authority | provenance HEAD `4494d6cce` |
| Historical evidence | public commits `4e37e8644`, `f196bc04b`, `37b01a953`, `57fd8c3f5`, `d44517cd0`, `791b07e5c`, and `188e6fd73` |
| Repository boundary | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-QBS-LINEAGE-R1 --title "QBS Lineage Reconciliation R1" --date 2026-08-05 --base 4494d6cce --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with verified QBS lineage, exact paths, offline verification, and stop conditions. |
| checkerReadAheadConfirmation | Dispatch-quality, handoff, ADIF, worker-return, and governed artifact checkers reviewed. |
| docOnlyNewFields | `QBS_LINEAGE_RECONCILIATION_R1_AUTHORIZED_BOUNDED` |
| claimBoundary | Dispatch authority only; no implementation, live, benchmark, or export claim. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Declared request risk exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | `EnforcementInput` | `cvfRiskLevel` | `EnforcementInput` | ACCEPT |
| Current enforcement ignores declared risk in the sync path | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | `evaluateEnforcement` | `evaluateRiskGate` | `evaluateEnforcement` | ACCEPT |
| QBS family input already exists | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | `ExecutionRequest` | `qbsFamily` | `ExecutionRequest` | ACCEPT |
| Prompt contract has a governed extension seam | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts` | `buildExecutionPrompt` | `buildExecutionPrompt` | prompt builder | ACCEPT |
| Intent router exposes weak-confidence fallback | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router.ts` | `routeIntent` | `fallback` | `IntentRouteResult` | ACCEPT |
| Execute route owns stopped response payloads | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | enforcement and safety branches | `POST` | execute API route | ACCEPT |

Historical public test failures are retained as read-only lineage evidence in
the Authority Chain; they are not promoted into this Source Verification table.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Disclosure count: 20

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status, Source Verification Block, ADIF Defect Registry Disclosure, Agent Handoff Contract Control Block, Reviewer Closure Conversion, Public Export Disposition |
| gateRunPurpose | Confirm dispatch shape before runtime implementation. |
| claimBoundary | Checker-shape evidence only. |

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| Historical contracts are provenance-owned | source is implemented and tested in provenance, not copied as public authority |
| Fifteen known failures are resolved | the five focused public-history test files pass from provenance |
| Family mapping remains bounded | mapper unit tests cover accepted family values, mappings, and null fallback |
| No unrelated regression | full non-live cvf-web suite passes or any pre-existing failure is separately evidenced |
| Public clone remains unchanged | public HEAD `27137db4d` and clean status |
| Bounded provider evidence | one targeted Alibaba call at most; HTTP/result and receipt summary recorded without raw key or raw output |

## Stop Conditions

- Any required change outside the paired work order's explicit manifest.
- Any second provider call, non-Alibaba provider, broad live suite, or QBS benchmark rerun.
- Any deletion or weakening of the retained public-history tests to obtain green.
- Any public mutation, downstream mutation, governance-latency work, or F-1 reopening.
- Any historical hunk that conflicts with a newer provenance contract and cannot
  be adapted inside the named paths.

## Evidence / Verification

Required evidence is the six focused Vitest files, TypeScript typecheck, one
full non-live cvf-web suite, exact changed-set status, public-sync clean status,
and worker-return fast gate. All provider-key variables remain cleared.

## Claim Boundary

Bounded QBS source/test lineage reconciliation only. No benchmark score,
provider quality, public release, production readiness, or causal-governance
claim is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: provenance implementation and review must close before a separate
public projection/export decision.
