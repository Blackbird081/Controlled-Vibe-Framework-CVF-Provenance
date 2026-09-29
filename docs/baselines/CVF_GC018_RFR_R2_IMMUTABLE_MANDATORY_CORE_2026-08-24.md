# CVF GC-018 Baseline - RFR-R2 Immutable Mandatory Core

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R2

Dispatch base head: `804168de1997504bafd500b4159c981dec4d7627`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: current orchestrator/reviewer/closer

Worker target: separate external implementation worker

## Purpose

Authorize the bounded RFR-R2 remediation of verified findings F2-F4: prevent
registered-guard object references from mutating engine authority, make
Mandatory Gateway configuration immutable after bootstrap, and replace bypass
substring matching with exact canonical matching.

## Authorization / Decision

The operator's explicit 2026-08-24 instruction to continue R2 releases only
this local reversible tranche under the established no-commit-worker and
independent-reviewer split. R3-R6 and all external-effect lanes remain parked.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R1 accepted | `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md`; material commit `a670343706c4fa21427a55a9c2ba464b9cef6cd4` | R1 must be independently accepted before R2 | ACCEPT |
| R2 ordered | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`, R2 row | F2-F4 route to R2 | ACCEPT |
| operator authority | explicit 2026-08-24 instruction to continue R2 under the old role rules | operator releases fresh dispatch | ACCEPT |

## Scope / Target / Owner Boundary

The worker may change only the Guard Contract engine and Mandatory Gateway
implementation/tests, refresh the already-governed `CONTRACT_TO_RUNTIME`
fingerprints after semantic review, and create the R2 worker return. The
reviewer owns any repair, completion review, roadmap transition, material
commit, and later continuity sync.

## Non-Goals

No new guard, phase, provider, dependency, configuration service, token or
signature scheme, Web/MCP/CLI adapter edit, AgentExecutionRuntime edit,
credential use, live call, deployment, public synchronization, staging,
commit, or push by the worker.

## Design Control Gate

- Preserve the canonical guard set and all RFR-R1 BUILD authority behavior.
- Preserve monotonic result aggregation and mandatory disable/unregister
  rejection.
- Close F2 at the registered-engine boundary, including original registration
  references and references returned by public accessors.
- Treat Gateway configuration as a defensive immutable snapshot; nested bypass
  arrays must not remain caller-owned mutable references.
- A bypass is valid only when the canonicalized whole action equals one
  canonicalized configured bypass value. Prefix, suffix, segment, or substring
  collisions do not bypass.
- Invalid runtime values must fail closed or reject configuration
  deterministically; they must not throw accidentally during admission.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| registered guard object is stored by caller reference | RUNTIME_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 19-38 | `registerGuard` | Guard Contract engine | ACCEPT |
| guard accessors expose registered objects | RUNTIME_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 70-76 | `getGuard`; `getRegisteredGuards` | Guard Contract engine | ACCEPT |
| mandatory API checks do not protect direct object mutation | AUTHORITY_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 40-68 | `unregisterGuard`; `disableGuard` | Guard Contract engine | ACCEPT |
| Gateway config is a shallow mutable merge | CONFIGURATION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 53-74 | `DEFAULT_GATEWAY_CONFIG`; constructor | Mandatory Gateway | ACCEPT |
| Gateway config can change runtime authority | CONFIGURATION_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 248-260 | `getConfig`; `updateConfig` | Mandatory Gateway | ACCEPT |
| bypass matching accepts substrings | AUTHORITY_WIDENING_RISK | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 95-99 and 136-139 | `bypassActions.some`; `includes` | Mandatory Gateway | ACCEPT |
| tests currently require mutable config and substring bypass | TEST_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | lines 41-111 and 141-152 | mutable-config and bypass cases | Mandatory Gateway tests | ACCEPT |
| F2-F4 are verified R2 findings | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position, F2-F4 | `PARTIAL_MONOTONICITY`; configuration-authority gap; `AUTHORITY_WIDENING_RISK` | governed review | ACCEPT |
| R2 dependency is released | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md` | Work Plan and Dispatch Boundary | R2 | runtime findings roadmap | ACCEPT |
| changed Gateway/test sources are fingerprinted | FRESHNESS_DEPENDENCY | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `CONTRACT_TO_RUNTIME.sourceFingerprints` | Mandatory Gateway source/test and root test fingerprints | system-chain map | ACCEPT |

## Source Hash Manifest

| Path | SHA-256 at dispatch base |
| --- | --- |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | `159a936f4ab99fc96daa2ca5eaef4cf14f1e6b446932a8458466d97faa28e387` |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | `4f1de18834bf2213436bbfaed8dbd91c58cbf0f3e086c57545aed1e85ae34375` |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | `12e513c836f1fd258417be2d9ced2424df6926210a10b02bce0e88fb9235c204` |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.test.ts` | `6f9519ea039500272cb52d08454bc0ed77b8c952315c062b8b7faa3592116201` |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `88d3a209bd66e7ba12e8c80e21ad7e383b7d588e50cd4f7533cf8f7be5ef9945` |

## Acceptance Criteria

1. Mutating the original guard after registration cannot change registered ID,
   enabled state, priority, evaluation function, or evaluation ordering.
2. Mutating a value returned by `getGuard()` or `getRegisteredGuards()` cannot
   change engine behavior; mandatory guards remain non-disableable and
   non-unregisterable, while supported non-mandatory disable semantics remain.
3. Gateway construction defensively snapshots and freezes authority-bearing
   configuration, including `bypassActions`; caller and getter mutations have
   no effect.
4. Runtime configuration mutation after bootstrap is rejected explicitly and
   cannot turn off enforcement, hard blocking, or hard escalation.
5. Only normalized whole-value bypass matches return `BYPASS`; all prefix,
   suffix, delimiter, case-fold collision, empty-entry, and substring attacks
   are covered by negative tests.
6. Existing Web no-bypass composition and RFR-R1 behavior remain green without
   editing Web or RFR-R1 files.
7. Focused, full-package, TypeScript, freshness, file-size, worker-return, diff,
   status, unchanged-HEAD, and empty-staging proof pass.

## Decision / Baseline / Proposed Tranche

Decision: `PROCEED_WITH_RFR_R2`.

Baseline: RFR-R1 is closed bounded. F2-F4 remain verified local authority
hardening gaps in existing owners.

Proposed tranche: one external no-commit worker implementation followed by
independent review, one reviewer-owned material commit, and a separate
continuity commit only after acceptance.

## Evidence / Verification

Worker evidence must identify exact source hashes, execution base, changed set,
staging state, focused/full/typecheck results, system-chain semantic decision,
worker-return gate, file-size result, and zero external calls. Reviewer must
independently probe object/reference mutation, nested configuration mutation,
and bypass collisions before acceptance.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R2 --title "Runtime Finding Remediation R2 Immutable Mandatory Core" --date 2026-08-24 --base 804168de1997504bafd500b4159c981dec4d7627 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R1 closed bounded at a670343706c4fa21427a55a9c2ba464b9cef6cd4 and operator authorized R2 on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified F2-F4 invariants, hashes, exact manifest, role split, negative matrix and claim boundaries |
| checkerReadAheadConfirmation | work-order, read-ahead, dispatch-envelope, lifecycle and dual-surface checker sources/standards reviewed before authoring |
| docOnlyNewFields | none; implementation details are worker-owned inside the bounded invariant |
| claimBoundary | scaffold provenance is dispatch evidence, not implementation proof |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_system_chain_map_freshness.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; exact Source Verification columns; Dependency Release Evidence; Worker Return Packet Shape Contract; six-column Dual Agent Surface Matrix |
| gateRunPurpose | confirm the R2 packet shape and evidence after checker-source read-ahead; not first discovery |
| claimBoundary | structural conformance does not prove F2-F4 implementation or closure |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| proposed artifact paths | `Test-Path` returned false for the R2 baseline, work order, worker return, and completion review before authoring | ABSENT_BEFORE_AUTHORING |
| same-tranche token search | search roots `docs` and `CVF_SESSION`; query `rg -n "RFR-R2|Immutable Mandatory Core|immutable mandatory core" docs CVF_SESSION` found only the roadmap's generic R2 row | NO_SAME_OWNER_COLLISION |
| owner collision | source/tests/docs/JSON/external-evidence coverage confirms F2-F4 enrich `GuardRuntimeEngine` and `MandatoryGateway`; no competing owner is created | EXISTING_OWNER_ENRICHMENT |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | YES_LOCAL_SOURCE_ONLY |
| freshnessVerificationMode | LOCAL_SOURCE_AND_TEST_RECOMPUTE_REQUIRED |
| reason | this packet authorizes local authority hardening but no provider/live, deployed, production, or universal-adoption claim |
| requiredFutureAction | reviewer reruns local proof and the system-chain freshness guard; any later live claim requires separate authority |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Guard Contract engine and Mandatory Gateway | local F2-F4 source/test hardening only; worker never commits | verified sources, focused/package tests, independent review | repository-local TypeScript APIs only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no R2 adapter change | no CLI/MCP ingress, authentication, approval, receipt, raw-data, mutation, or public authority | exact worker manifest excludes external adapters | deferred to an independently authorized adapter owner; no invocation | DEFERRED_WITH_REASON |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: RFR-R2 changes in-memory Guard Contract and Gateway
authority behavior only; it creates no persistence, registry, queue, durable
storage, relocation, or migration owner.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint; canonical dispatch and review guards remain binding |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | RFR-R2 dispatch authority only |
| claimDisposition | CLAIM_REJECTED until worker evidence and independent review pass |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatcher made no production-source edit |
| invocationBoundary | governed local document authoring and pre-dispatch checks |
| interceptionBoundary | no provider, network, CLI/MCP, deployment, public, or production interception |
| claimLanguage | dispatch-ready local remediation only |
| forbiddenExpansion | R3-R6, external adapters, provider/live, credentials, deployment, public sync, push, or production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes bounded RFR-R2 construction and local proof only. It
does not prove implementation, live behavior, universal adoption, deployment,
public export, or closure of F2-F4.
