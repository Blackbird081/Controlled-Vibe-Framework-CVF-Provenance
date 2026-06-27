# GC-018 Model Gateway C-02 P4C Provider Adapter Contract Conformance

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-MODEL-GATEWAY-C02-P4C-PROVIDER-ADAPTER-CONFORMANCE-2026-06-15

Date: 2026-06-15

Status: AUTHORIZED_P4C_DETERMINISTIC_ONLY

## Purpose

Authorize Claude to implement the deterministic Model Gateway C-02 P4C provider
adapter contract conformance layer under `WORKER_MUST_NOT_COMMIT`.

This baseline is provider-agnostic. It does not select, prefer, or canonicalize
Alibaba, DeepSeek, or any other provider. Current concrete adapters may be read
as source examples only.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_MODEL_GATEWAY`.

Worker owner: Claude creates the P4C conformance helper, deterministic tests,
additive exports, GC-051 entries, generated aggregate update, and worker return.

Reviewer/committer owner: Codex reviews the real diff, performs allowed
repairs, authors completion review, commits material work, and synchronizes
session continuity separately.

Boundary: no network, runtime secret, concrete provider binding, live proof,
provider addition, or provider preference.

## Source / Predecessor Evidence

- P4B-A provider execution bridge closed at material commit `3c5b1d3d` and
  closure-doc commit `a21f3e65`.
- Current provider-neutral adapter contract:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`.
- Current method capability owner:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`.
- Current method gate owner:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`.
- Current static capability registry:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`.
- Legacy coverage row: `MGW-001` remains `PARTIAL_RECHECK_REQUIRED`.

## Decision / Baseline / Proposed Tranche

Decision: release P4C deterministic adapter conformance to Claude under
`WORKER_MUST_NOT_COMMIT`.

Baseline: CVF controls the adapter admission contract, not provider choice.
Future users may supply any provider adapter when it satisfies conformance and
when live credential authorization is separately granted.

P4B-B remains held and is not dependency-released by this baseline.

## Authority

- Operator instruction on 2026-06-15: create a Claude work order; Alibaba and
  DeepSeek are current live-run samples only, not the CVF design center.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`.
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md`.

## Authorized Scope

1. Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts`.
2. Define a provider-agnostic deterministic conformance evaluator.
3. Reuse current provider method contract and method gate helpers.
4. Add deterministic tests with fake adapters and fake capability records.
5. Add additive exports to `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`.
6. Add GC-051 source/test entries and regenerate the aggregate.
7. Author the P4C worker return.

## Not Authorized

- Reading `.env.local`.
- Calling `CredentialBoundary.resolveSecretForRuntime()`.
- Calling `fetch`, provider URLs, HTTP clients, or any network.
- Importing or modifying concrete provider adapters.
- Adding provider or model IDs.
- Selecting Alibaba, DeepSeek, or any provider as canonical.
- EPF wiring, Strategy Layer, AI Gateway, OCR, retrieval, or public-sync work.
- Session-state or active-handoff mutation by Claude.
- Commit, push, merge, delete, rename, or destructive operations by Claude.

## P4B-B Hold

Status: `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`.

P4C does not release live proof. A future P4B-B or equivalent live lane must
name the selected provider at that time, refresh source verification, follow
live-run diagnostic discipline, and receive explicit operator authorization for
credential and network use.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P4C disposition | Authorized as provider-agnostic adapter conformance foundation |
| Closure disposition | Keep `MGW-001` partial; do not claim full legacy absorption |
| Deferred boundaries | Strategy Layer, AI Gateway, and live binding remain separately deferred |

## Verification

- Pre-dispatch autorun must pass before dispatch commit.
- Worker must run type check, full Model Gateway tests, GC-051 drift check,
  worker fast gate, and diff hygiene.
- Codex owns committed-range pre-closure and session synchronization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 P4C dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source inspection, apply_patch, governance gates |
| Target paths | P4C roadmap, GC-018, and Claude work order |
| Allowed scope source | operator instruction 2026-06-15 |
| Before status evidence | HEAD `1baba8c9`; P4B-A closed; P4B-B held |
| After status evidence | P4C dispatch packet ready |
| Diff evidence | pre-dispatch range `1baba8c9..HEAD` |
| Approval boundary | provider-agnostic deterministic conformance only |
| Claim boundary | no live provider, credential use, quota spend, provider preference, or public claim |
| Agent type | Codex orchestrator |
| Invocation ID | `p4c-provider-adapter-conformance-dispatch-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes only deterministic P4C adapter conformance. It does
not prove or authorize live provider behavior, credential use, provider quality,
provider preference, cost improvement, public readiness, production readiness,
or P4B-B.
