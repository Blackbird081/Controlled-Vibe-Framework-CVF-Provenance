# CVF GC-018 Baseline - Qwen Turbo Deprecation Migration

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-15

Batch ID: QTDM-01

Dispatch base head: `fc11bf46c2a46b09bfc1affefce0960bbbcbde72`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Independent reviewer/closer

Worker target: migration worker role (not a specific provider name)

## Purpose

Authorize a documentation-plus-source migration that removes the deprecated
`qwen-turbo` model identifier from every active runtime, configuration, test,
script, current reference authority, and user-facing active documentation
surface, replacing it with the canonical `qwen-flash` runtime alias, while
preserving immutable historical receipts, archived reviews, evidence JSON,
historical handoffs, and prior session-state entries exactly as historical
facts. This packet authorizes migration dispatch only, not implementation or
any live provider call.

## Authorization

The operator directed removal of Qwen-Turbo after the CADP-AI-T6 worker
returned BLOCKED with zero provider calls and the environment repair landed.
The authorization scope is exactly:

- remove `qwen-turbo` from active surfaces and replace with `qwen-flash`;
- record `qwen-flash-2025-07-28` as the official replacement snapshot;
- do not use `qwen3.6-flash` as canonical authority;
- preserve every immutable historical occurrence as retained legacy evidence.

The authorization does not include: a live provider call; npm/npx repair or
T6 retry; blind repository-wide replacement; mutation of protected session
state, active handoff, front door, `.env.local`, or generated aggregates; T5
adapter implementation; MCP/CLI invocation; deployment; public sync; or any
production, trusted-evidence, or cross-runtime claim.

## Dependency Release Evidence

| Dependency | Evidence | Required state | Result |
|---|---|---|---|
| T6 blocked evidence | `docs/reviews/CVF_CADP_AI_T6_LIVE_COMPATIBILITY_PROOF_WORKER_RETURN_2026-08-15.md` plus material commit `25c0b2217` | zero provider calls, blocked | SATISFIED |
| environment repair | active handoff plus commits `7d8ae252b` and `fc11bf46c` | npm/npx 10.9.2 resolve | SATISFIED |
| operator migration directive | active handoff `Core Guard Self-Protection Authorization` and session next-move | remove Qwen-Turbo, migrate to qwen-flash | SATISFIED |
| replacement authority | Alibaba Cloud Model Studio official model list and pricing pages | qwen-turbo absent from current model list; flash tier priced | SATISFIED |

## Scope

Authorize exactly one migration worker tranche that:

- enumerates and edits the exact active-surface files named in the Active-Surface Migration Manifest;
- leaves every file named in the Historical-Evidence Exclusion Manifest byte-for-byte unchanged;
- applies the Replacement Contract (qwen-flash) uniformly;
- records the official replacement snapshot `qwen-flash-2025-07-28`;
- does not perform a live provider call.

## Non-Goals

No live provider call, no T6 retry, no npm/npx repair, no blind replacement,
no session-state / active-handoff / front-door / `.env.local` mutation, no
public sync, no deployment, and no production action. No claim that the
migration itself proves provider compatibility or readiness.

## Replacement Contract

| Field | Value |
|---|---|
| Canonical runtime alias | `qwen-flash` |
| Official replacement snapshot | `qwen-flash-2025-07-28` |
| Forbidden canonical authority | `qwen3.6-flash` must not be used as canonical authority; it may remain only where it is a factual versioned snapshot in an existing ledger |
| Deprecated identifier | `qwen-turbo` is removed from active surfaces only |
| Provider lane | DashScope-compatible Alibaba lane is retained; DeepSeek and OpenAI lanes are untouched |
| Migration rule | substitute the model identifier in active surfaces; never edit a historical receipt, archive, evidence JSON, handoff archive, or prior session-state entry |

## Source Authority Table

| Claim | Authority source | Disposition |
|---|---|---|
| Qwen-Turbo snapshot retirement and replacement | `https://www.alibabacloud.com/help/en/model-studio/model-depreciation` (`Deprecated on January 30, 2026`) | ACCEPT: `qwen-turbo-2024-09-19` is deprecated and its replacement is `qwen-flash-2025-07-28` |
| canonical alias and snapshot equivalence | `https://www.alibabacloud.com/help/en/model-studio/qwen-flash` (`qwen-flash`; `Snapshot Versions`) | ACCEPT: `qwen-flash` is functionally equivalent to `qwen-flash-2025-07-28` |
| active migration direction | operator deprecation directive 2026-08-15 recorded in active handoff and session next-move | ACCEPT: remove deprecated Qwen-Turbo authority from active CVF surfaces |

## Active-Surface Migration Manifest

Class A - Runtime source (non-test, non-archive), exact 9 files:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/alibaba-dashscope-provider.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai-providers.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProviderSwitcher.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Settings.tsx`

Class B - Active test/support files (non-archive) under `EXTENSIONS`, exact 73
files. The set is the 72 dispatch-base `qwen-turbo` hits plus the blocked T6
test carrying the provisional `qwen3.6-flash` identifier:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/*.test.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/*.test.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/*.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/*.alibaba.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/*.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.*.test.ts` and `route.*.live.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/*.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/**/*.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/*.spec.ts` plus `tests/e2e/utils.ts`
- `EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/tests/*.test.ts`

Exactness rule: the globs above are family summaries only, not write authority.
Before editing, the worker must expand the 72 `qwen-turbo` hits at dispatch
base, add exactly
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts`,
record the resulting 73-path enumeration in the worker return, and edit no
other Class B path. Any count or path mismatch returns `BLOCKED_WITH_REASON`.
The exact dispatch-base enumeration command is:

```powershell
git grep -l -i 'qwen-turbo' -- 'EXTENSIONS' | Where-Object { $_ -match '(?i)(test|spec)\.(ts|tsx|js|mjs|py)$' -or $_ -eq 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts' }
```

Expected count: 72 before adding the one provisional SOT3 path.

Class C - Active scripts (non-archive), exact 25 files:

- `scripts/cvf_provider_check.py`
- `scripts/evaluate_cvf_provider_lane_certification.py`
- `scripts/pvv_cp3b_batch_runner.py`
- `scripts/pvv_phase_a_batch_runner.py`
- `scripts/pvv_phase_a_pilot.py`
- `scripts/run_cvf_alibaba_live_canary.py`
- `scripts/run_cvf_provider_live_canary.py`
- `scripts/run_cvf_multi_provider_live_smoke.py`
- `scripts/run_cvf_sot3_a3_live_proof.py`
- `scripts/run_pm2_streaming_live_proof.py`
- `scripts/run_cvf_c2_memory_reinjection_live_probe.mjs`
- `scripts/run_cvf_c5_web_release_gate_probe.mjs`
- `scripts/run_cvf_hosted_readiness_probe.mjs`
- `scripts/run_cvf_m1_durable_memory_live_probe.mjs`
- `scripts/run_cvf_p1_noncoder_e2e_probe.mjs`
- `scripts/run_cvf_r2_durable_memory_route_live_probe.mjs`
- `scripts/run_cvf_s1_durable_memory_write_route_live_probe.mjs`
- `scripts/run_cvf_s3_governance_benchmark_probe.mjs`
- `scripts/run_cvf_wc1_workflow_chain_probe.mjs`
- `scripts/run_evt2_live_latency_measurement.js`
- `scripts/run_evt4_output_quality_ab.js`
- `scripts/run_phase2b_live_governance_receipt_probe.mjs`
- `scripts/run_post_phase2b_provider_stability_probe.mjs`
- `scripts/test_run_cvf_sot3_a5_release_integration.py`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`

Class D - Current reference authority (non-archive), exact 7 files:

- `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md`
- `docs/reference/CVF_LHW23_T1_MODEL_REGISTRY_SERVICE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md`
- `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md`
- `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json`
- `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.md`

Class E - User-facing active documentation, exact 5 files:

- `README.md`
- `ARCHITECTURE.md`
- `docs/CVF_CORE_KNOWLEDGE_BASE.md`
- `docs/CVF_INCREMENTAL_TEST_LOG.md`
- `docs/guides/CVF_DEMO_SCRIPT_2026-04-21.md`

## Historical-Evidence Exclusion Manifest

The following path families are immutable historical facts and MUST NOT be
edited by the migration worker:

- `CVF_SESSION/handoffs/archive/**`
- `CVF_SESSION/state/entries/**` (prior session-state entries)
- existing `docs/baselines/**`, `docs/work_orders/**`, `docs/reviews/**`,
  `docs/roadmaps/**`, `docs/assessments/**`, and `docs/audits/**`, except the
  new worker return and exact active files separately named by this baseline
- `docs/reference/archive/**`, `docs/reference/evidence/**`, `docs/guides/archive/**`
- `docs/evidence/**`, `docs/reviews/evidence/**`, `docs/audits/alibaba-canary/**`
- `docs/assessments/**/*.jsonl` and `*.json` raw evidence, `docs/baselines/pvv_*` evidence
- `docs/logs/**`
- `.private_reference/**` (retained legacy corpus)
- `docs/reference/CVF_LIVE_EVIDENCE_PUBLICATION_PACKET_2026-04-21.md` and `docs/reference/CVF_W114_PUBLIC_EVIDENCE_PACKET_2026-04-23.md` (historical evidence packets)
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (historical review notes)

Every remaining historical `qwen-turbo` occurrence is classified as retained
legacy evidence, never active configuration. The QTDM-01 baseline, work order,
worker return, and future completion record may name the deprecated identifier
only as the deprecation owner/evidence chain, never as runtime configuration.

## Session-Sync Surfaces (Steward-Owned, Not Worker)

The following protected surfaces reference the migration directive and are
updated by the session-sync steward in a separate commit AFTER material
migration acceptance, never by the migration worker:

- `AGENT_HANDOFF_V59_2026-08-11.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`

## Machine Guard Proposal

Propose a new machine guard `governance/compat/check_qwen_turbo_active_reference.py`
plus its test that fails pre-implementation when `qwen-turbo` (case-insensitive)
appears in an active surface (runtime source, test, script, current reference
authority, or user-facing active doc) and does not fire on archive, evidence,
receipt, or prior-session-state paths. Promotion is staged: dispatch proposal
first, independent review, then a separate governed checker tranche. Neither
the worker nor the migration reviewer may create or edit guard code in QTDM-01.

## GC-051 Registry Obligations

Any new governed artifact or test created by the migration (the proposed
machine guard and its test) must be registered in the corpus scan registry
per GC-051 with a source entry and regenerated aggregate in the same material
batch. No corpus source path is added by the identifier migration itself.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| provider cert evaluator pins alibaba to qwen-turbo | VALUE_SET | `scripts/evaluate_cvf_provider_lane_certification.py` | `PROVIDERS` | `qwen-turbo` | provider certification evaluator | ACCEPT |
| model gateway capability registry lists qwen-turbo | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | `PROVIDER_CAPABILITY_REGISTRY` | model gateway provider capability registry | ACCEPT |
| model gateway provider registry enforces routable admission | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry` class | `assertAllowed`; `listRoutable` | model gateway provider registry | ACCEPT |
| web provider defaults to qwen-turbo | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai-providers.ts` | `AlibabaDashScopeWebProvider` constructor | `config.model || 'qwen-turbo'` | web AI provider adapter | ACCEPT |
| migration directive is current authority | LITERAL_INVARIANT | `AGENT_HANDOFF_V59_2026-08-11.md` | Next Allowed Move and Core Guard Self-Protection Authorization | `qwen-flash` replacement | active handoff | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `Source Verification Block`; `Checker Source Read-Ahead Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition`; `Reviewer Closure Conversion`; `Worker Autonomy / No-Question Rule`; `WORKER_MUST_NOT_COMMIT`; `Replacement Contract`; `Machine Guard Proposal` |
| gateRunPurpose | confirmation and evidence after reading checker source ahead of writing |
| claimBoundary | structural read-ahead does not prove migration correctness or provider compatibility |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id QTDM-01 --title "Qwen Turbo Deprecation Migration" --date 2026-08-15 --base fc11bf46c2a46b09bfc1affefce0960bbbcbde72 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | dispatch, source verification, agent handoff contract, reviewer closure conversion, worker return shape, trace, delta block, public disposition, claim boundary |
| manualEditsAfterScaffold | bound migration semantics, replacement contract, active/historical manifests, machine guard proposal, GC-051 obligations |
| checkerReadAheadConfirmation | checker sources listed in the preceding block were read before authoring |
| docOnlyNewFields | `Replacement Contract`; `Active-Surface Migration Manifest`; `Historical-Evidence Exclusion Manifest`; `Machine Guard Proposal`; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no live, runtime, provider, public-sync, or production behavior is implemented |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Path existence for the two QTDM-01 dispatch artifact paths | both proposed baseline and work order paths were absent before authoring | ABSENT_BEFORE_AUTHORING |
| Bounded collision search | searched `git grep -l qwen-turbo` across the repository plus `git grep -l qwen-flash`; 427 qwen-turbo files and 6 qwen-flash files enumerated; no existing QTDM-01 packet | EXISTING_OWNER_SURFACES_REUSED |
| Collision decision | provider registry, release gate bundle, and session surfaces remain their existing owners; the migration packet adds a new baseline and work order only | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`qwen`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector qwen --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; no-live-call and preserve-historical boundaries remain mandatory |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact or recommendation is ingested; official pricing pages are cited as lifecycle authority only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources plus the cited official lifecycle pages support this dispatch |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | active runtime/test/script/reference surfaces under `EXTENSIONS`, `scripts`, and `docs` | identifier migration only; no runtime/source semantic change, no live call, no session mutation | source-verified manifests and future worker return | none introduced | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP surface | no invocation, launch, credential, mutation, or public authority | T5 decision remains deferred | future fresh packet required | `DEFERRED_WITH_REASON` |

## Decision / Baseline

Proceed with one identifier-only Qwen-Turbo deprecation migration after
independent reviewer acceptance. The worker edits only the Active-Surface
Migration Manifest, preserves every Historical-Evidence Exclusion Manifest
path, applies the `qwen-flash` Replacement Contract, and performs no live
provider call.

## Evidence / Verification

Source verification above establishes the dispatch boundary and the manifests
only. The worker and independent reviewer own the migration correctness.
Pre-dispatch gates must pass before handoff.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Qwen-Turbo deprecation migration dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, interception, or migration completion is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created by this dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, provider, live, or migration action occurs during dispatch authoring |
| invocationBoundary | local read-only source verification and governed document authoring only |
| interceptionBoundary | no wrapper, proxy, runtime gate, or process interception |
| claimLanguage | migration authorization only, pending independent review |
| forbiddenExpansion | no live provider call, no T6 retry, no npm/npx repair, no blind replacement, no session mutation, no public export, no production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance migration dispatch with no public-sync authorization.

## Claim Boundary

This baseline authorizes only an identifier-level deprecation migration
dispatch. It does not implement the migration, does not perform or prove any
live provider call, does not authorize T6 retry or environment repair, and
does not claim provider compatibility, production readiness, or cross-runtime
determinism. Historical receipts, archives, evidence JSON, handoffs, and prior
session-state entries remain immutable historical facts.
