# CVF GC-018 Baseline - CSCC-R1-T2 Canonical Web Gateway Composition

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CSCC-R1-T2

Dispatch base head: 066a07911

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator; reviewer owner: orchestrator/reviewer; worker target: delegated implementation worker.

## Purpose

Authorize one bounded deterministic implementation tranche that realizes the
accepted T1 contracts: a Gateway-owned canonical execution port, one Web text
composition path through that port, atomic Web attempt admission immediately
before the Gateway adapter call, additive receipt identity, and reversible
single-path rollback.

## Decision / Baseline / Proposed Tranche

T1 is independently accepted at material commit `f93b00e42` with terminal
`READY_FOR_T2_CANONICAL_WEB_GATEWAY_COMPOSITION`. T2 may implement and test the
frozen contract in the exact allowed manifest below. It may not run a provider,
claim live proof, remove the direct rollback implementation, or open T3.

## Authorized Scope

- additive Model Gateway port, bridge option, request identity, receipt and
  manifest fields plus package export;
- Web-owned canonical composition adapter for non-vision text attempts;
- propagation from the existing Web envelope into SOT3, Gateway and the Web
  governance receipt;
- deterministic tests for all ten T1 risk classes;
- worker return with exact no-commit and zero-call evidence.

## Forbidden Scope

GC-010, MAO ingress/launch, P2, P4, canary data, MFRP decisions, vision
execution, real-provider/live proof, deployment, public sync, downstream
workspace adoption, provider expansion, credential-store replacement, schema
version split, direct-path deletion, and successor release are forbidden.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| accepted T1 contracts | `docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md` at material commit `f93b00e42` | accepted terminal plus exact two frozen reference contracts releases fresh T2 dispatch | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CSCC-R1-T2 --title "Canonical Web Gateway Composition" --date 2026-09-03 --base 066a07911 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker plus no-commit and Web trigger stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with T1 authority, exact scope, source evidence, gates and exclusions |
| checkerReadAheadConfirmation | dispatch, envelope, trace, handoff, SCEC, routing, delta, public and structural checker sources |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; no implementation evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | exact manifest, CVF-source authority, no-commit split, atomic admission tests and bounded timeout discipline |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch status; source-table columns; SCEC fields; handoff fields; trace labels; public disposition |
| gateRunPurpose | confirm packet conformance after source and contract reconciliation |
| claimBoundary | conformance does not prove runtime behavior or replace independent review |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T2 is released for dispatch authoring | accepted closure | `docs/reviews/CVF_CSCC_R1_T1_CANONICAL_EXECUTION_PORT_AND_RECEIPT_JOIN_CONTRACT_FREEZE_COMPLETION_2026-09-03.md` | Findings / Position | `READY_FOR_T2_CANONICAL_WEB_GATEWAY_COMPOSITION` | T1 reviewer/closer | ACCEPT |
| exact port and ten tests | frozen contract | `docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md` | stable types through test-name manifest | `CanonicalExecutionPort` | Model Gateway | ACCEPT |
| exact identity propagation | frozen contract | `docs/reference/CVF_CANONICAL_EXECUTION_IDENTITY_AND_RECEIPT_JOIN_CONTRACT_2026-09-03.md` | four-owner matrix | `canonicalExecutionId` | Web, SOT3 and Gateway evidence owners | ACCEPT |
| current direct calls and attempt boundary | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` | text initial/retry branches and call-start function | `admitAndInvokeProvider`; `recordProviderCallStart` | Web execute route | ACCEPT |
| current Gateway seam | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | execute options and adapter call | `ProviderExecutionBridge` | Model Gateway | ACCEPT |
| package dependency already exists | package source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | `cvf-model-gateway` | Web package | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact baseline, work order and worker-return targets | all returned false before authoring | ACCEPT |
| source symbols | T1 verified no competing `CanonicalExecutionPort`, `canonicalExecutionId`, or `beforeProviderInvoke` source symbols | ACCEPT_PREDECESSOR_EVIDENCE |
| collision decision | reserve exact dispatch and worker paths; all other lanes remain isolated | ACCEPT_NO_COLLISION |

## Completion Standard

Worker returns `COMPLETE_PENDING_REVIEW` only when the exact manifest is
reconciled, Gateway and Web typechecks pass, focused deterministic tests cover
all ten frozen risk classes, non-live Web regression tests pass, provider and
external invocation counts remain zero, HEAD is unchanged, and staged diff is
empty. Any contract contradiction returns `BLOCKED_WITH_REASON`.

## Evidence / Verification

Pre-implementation gate, both package typechecks, focused Vitest suites,
static negative import/call-path searches, full worker-return gate, exact diff
and status reconciliation. No release-quality live bundle is authorized.

## Web/UI Claim Boundary

| Field | Value |
| --- | --- |
| DESIGN.md read | confirmed by dispatcher; worker must reread before implementation |
| UI claim boundary | no UI surface is in scope; route behavior is deterministic local composition only |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | current private source and accepted CVF review authority only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline, paired work order and frozen T1 contracts |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for runtime/readiness claims |
| Claim boundary | delegated output is pending evidence, not canonical authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private bounded implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes deterministic local T2 implementation and tests in
the paired exact manifest only. It proves no composition until independent
review accepts executable evidence and grants no T3, live, production, public,
MAO, GC-010, P2, P4, canary or downstream authority.
