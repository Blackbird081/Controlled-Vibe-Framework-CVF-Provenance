# GC-018 Model Gateway C-02 P5 Provider Adapter Admission And Capability Negotiation

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-MODEL-GATEWAY-C02-P5-PROVIDER-ADAPTER-ADMISSION-2026-06-15

Date: 2026-06-15

Status: AUTHORIZED_P5_DETERMINISTIC_ONLY

## Purpose

Authorize Codex to implement the deterministic Model Gateway C-02 P5 provider
adapter admission record and capability negotiation layer under
`WORKER_MAY_COMMIT`.

This baseline is provider-agnostic. It does not select, prefer, or canonicalize
Alibaba, DeepSeek, or any other provider. Concrete provider adapters remain
samples only and must not appear in P5 source or tests.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_MODEL_GATEWAY`.

Worker owner: Codex creates the P5 admission source file, capability
negotiation helper, deterministic tests, additive exports, GC-051 entries,
generated aggregate update, completion review, material commit, and separate
session-sync commit.

Reviewer/committer owner: Codex reviews the real diff with machine gates,
performs allowed repairs, authors completion review, commits material work, and
synchronizes session continuity separately.

Boundary: no network, runtime secret, concrete provider binding, live proof,
provider addition, or provider preference. P4B-A bridge mutation is out of scope
for P5-A/P5-B. Bridge admission boundary (P5-C) is deferred to a separate
authorized tranche.

## Source / Predecessor Evidence

- P4C provider adapter conformance closed at material commit `8d8f0871` and
  closure-doc commit `64a80684`.
- P5 roadmap: `ROADMAP_READY_FOR_GC018` at commit `4c888aa0`.
- Current P4C conformance owner:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` (135L).
- Current bridge adapter contract:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` (268L).
- Current method gate owner:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` (106L).
- Current capability registry:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` (98L).
- Barrel exports:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (329L).
- Legacy coverage row: `MGW-001` remains `PARTIAL_RECHECK_REQUIRED`.

## Decision / Baseline / Proposed Tranche

Decision: release P5-A (adapter admission record) and P5-B (capability
negotiation) together to Claude under `WORKER_MUST_NOT_COMMIT`, provided the
implementation can stay below file-size thresholds. If P5-A alone exceeds the
threshold, Claude must split and return P5-A only, flagging P5-B for a
separate dispatch.

Baseline: CVF controls the adapter admission evidence contract. P4C conformance
is a required input to admission, not replaced by it. Capability negotiation
produces machine-readable reason codes and does not select any concrete provider.

P4B-B remains `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`.
P5-C bridge admission boundary is deferred; it is not released by this baseline.

## Authority

- Operator instruction on 2026-06-15: create P5 roadmap; next tranche is GC-018
  and a source-verified Claude work order for P5-A/P5-B.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md`.
- Active Codex work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md`.
- Superseded Claude mirror work order retained for audit:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CLAUDE_2026-06-15.md`.

## Authorized Scope

1. Create
   `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts`
   containing: `AdapterAdmissionStatus`, `AdapterAdmissionRecord`,
   `AdapterAdmissionReasonCode`, and `admitProviderAdapter()`.
2. Create
   `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts`
   containing: `CapabilityNegotiationResult`, `CapabilityNegotiationStatus`,
   and `negotiateProviderCapability()`. Split to P5-A only if file-size risk
   requires it and flag P5-B for separate dispatch.
3. Add deterministic tests in:
   `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-adapter-admission.test.ts`.
4. Add additive exports to `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` only.
5. Add GC-051 source/test entries under
   `docs/corpus-intelligence/registry/entries/` and regenerate the aggregate.
6. Author the P5 worker return.

## Not Authorized

- Reading `.env.local`.
- Calling `CredentialBoundary.resolveSecretForRuntime()`.
- Calling `fetch`, provider URLs, HTTP clients, or any network.
- Importing or modifying concrete provider adapters.
- Adding provider or model IDs as accepted provider canonicals.
- Selecting Alibaba, DeepSeek, or any provider as canonical.
- Modifying P4B-A bridge execution logic (`provider-execution-bridge.ts`
  execute path) - bridge admission boundary belongs to P5-C.
- Modifying P4C conformance source (`provider-adapter-conformance.ts`).
- Modifying existing method-gate or capability-registry source except additive
  `index.ts` exports.
- EPF wiring, Strategy Layer, AI Gateway, OCR, retrieval, or public-sync work.
- Session-state or active-handoff mutation by Claude.
- Commit, push, merge, delete, rename, or destructive operations by Claude.

## P4B-B Hold

Status: `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`.

P5 does not release live proof. A future P4B-B or equivalent live lane must
name the selected provider at that time, refresh source verification, follow
live-run diagnostic discipline, and receive explicit operator authorization for
credential and network use.

## P5-C Deferral

P5-C bridge admission boundary (bridge accepts admitted adapter evidence before
execution) is not authorized in this baseline. It requires a separate GC-018
and Claude work order after P5-A/P5-B are closed.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P5 disposition | Authorized as provider-agnostic admission and negotiation foundation |
| Closure disposition | Keep `MGW-001` partial; do not claim full legacy absorption |
| Deferred boundaries | Strategy Layer, AI Gateway, live binding, P5-C, and P4B-B remain separately deferred |

## Verification

- Pre-dispatch autorun must pass before dispatch commit.
- Worker must run type check, full Model Gateway tests, GC-051 drift check,
  worker fast gate, and diff hygiene.
- Codex owns committed-range pre-closure and session synchronization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude orchestrator, corrected by Codex reviewer |
| Provider or surface | Claude Code local workspace plus Codex local workspace |
| Session or invocation | 2026-06-15 P5 GC-018 and Codex dispatch authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Write, governance pattern inspection |
| Target paths | P5 GC-018 baseline, superseded Claude mirror work order, and active Codex work order |
| Allowed scope source | operator instruction 2026-06-15 + P5 roadmap `4c888aa0` |
| Before status evidence | HEAD `586aa56e`; P4C closed; P4B-B held; P5 roadmap ready |
| After status evidence | P5 GC-018, superseded Claude mirror work order, and active Codex work order authored, awaiting Codex dispatch commit |
| Diff evidence | pre-dispatch range `4c888aa0..HEAD` |
| Approval boundary | provider-agnostic deterministic P5-A/P5-B only |
| Claim boundary | no live provider, credential use, quota spend, provider preference, P5-C, or public claim |
| Agent type | Claude orchestrator |
| Invocation ID | `p5-provider-adapter-admission-gc018-2026-06-15` |
| Expected manifest | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CLAUDE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CLAUDE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_FOR_CODEX_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes only deterministic P5-A adapter admission record and
P5-B capability negotiation. It does not authorize P4B-B, P5-C, provider
credentials, network calls, live proof, provider/model addition, provider
preference, EPF wiring, Strategy Layer, AI Gateway absorption, public sync,
production readiness, public readiness, or raw memory release.
