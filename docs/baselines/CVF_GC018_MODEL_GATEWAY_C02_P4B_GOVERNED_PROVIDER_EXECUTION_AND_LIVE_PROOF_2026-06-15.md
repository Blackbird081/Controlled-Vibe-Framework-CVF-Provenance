# GC-018 Model Gateway C-02 P4B Continuation Governance Baseline

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-MODEL-GATEWAY-C02-P4B-A-PROVIDER-EXECUTION-2026-06-15

Date: 2026-06-15

Status: AUTHORIZED_P4B_A_ONLY_P4B_B_HOLD

## Purpose

Authorize Claude to implement the deterministic Model Gateway C-02 P4B-A
Provider Execution Bridge under `WORKER_MUST_NOT_COMMIT`.

This baseline does not authorize P4B-B live proof. Live credential access,
network use, and quota consumption remain held pending a fresh explicit
operator checkpoint and refreshed source verification for the selected
provider adapter.

## Scope / Target / Owner Boundary

Target: P4B-A inside `EXTENSIONS/CVF_MODEL_GATEWAY`.

Worker owner: Claude creates only the bridge, deterministic tests, additive
exports, GC-051 entries, and worker return.

Reviewer/committer owner: Codex reviews the real diff, authors completion,
commits material work, and synchronizes session continuity separately.

Boundary: no network, runtime secret, concrete provider binding, or P4B-B.

## Source / Predecessor Evidence

- P3 contract and P4A skeleton closed at material commit `5d46bc62`.
- Current routing owner: `RoutingPolicyEngine` in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`.
- Current credential owner: `CredentialBoundary` in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts`.
- Current receipt owner: `GatewayReceiptBuilder` in
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`.
- Legacy coverage row: `MGW-001` remains `PARTIAL_RECHECK_REQUIRED`.

## Decision / Baseline / Proposed Tranche

Decision: release deterministic P4B-A to Claude under
`WORKER_MUST_NOT_COMMIT`.

Baseline: reuse current source owners and introduce only the provider-neutral
injected adapter contract needed to test execution orchestration.

Proposed later tranche: P4B-B remains held and is not dependency-released by
this baseline.

## Authority

- Operator instruction on 2026-06-15: Codex repairs the draft and Claude may
  execute the corrected work order.
- P4A closure:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`.
- Roadmap:
  `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_ROADMAP_2026-06-15.md`.
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_FOR_CLAUDE_2026-06-15.md`.

## Authorized Scope

1. Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`.
2. Define the provider-neutral injected adapter contract and deterministic
   bridge described by the roadmap and work order.
3. Reuse existing routing, credential metadata, health, quota, and receipt
   owners without changing them.
4. Add deterministic bridge tests.
5. Add additive exports to `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`.
6. Add GC-051 source/test entries and regenerate the aggregate.
7. Author the P4B-A worker return.

## P4B-B Hold

Status: `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`.

The worker must not:

- read `.env.local`;
- resolve a runtime secret;
- call a provider API or any network endpoint;
- import or modify the Alibaba or DeepSeek adapter for execution;
- consume live quota;
- author or claim a live proof receipt;
- rerun a failed live call.

P4B-B requires a refreshed GC-018 and work order after the operator explicitly
authorizes the credential/provider checkpoint.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P4B-A disposition | Authorized as the provider execution bridge contribution |
| Closure disposition | Keep `MGW-001` partial; do not claim full legacy absorption |
| Deferred boundaries | Strategy Layer and AI Gateway remain separately deferred |

## Core Guard Self-Protection Authorization

Not applicable to the worker implementation. No `governance/compat`,
`CVF_SESSION`, root handoff, or front-door file is in worker write ownership.

Reviewer-owned session synchronization is a separate commit after the material
dispatch or closure commit.

## Not Authorized

- Existing source mutation except additive `src/index.ts` exports.
- Existing provider adapter mutation.
- `UnifiedGatewaySkeletonImpl` mutation.
- Live/provider/network/secret work.
- Provider or model addition.
- EPF, Strategy Layer, AI Gateway, OCR, retrieval, or public-sync work.
- Session-state or active-handoff mutation by Claude.
- Commit, push, merge, or destructive operations.

## Verification

- Source verification must use the exact current runtime symbols.
- Pre-dispatch autorun and dispatch steward must pass.
- Worker must run type check, full Model Gateway tests, GC-051 drift check,
  worker-return fast gate, and diff hygiene.
- Codex owns committed-range pre-closure and session synchronization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 P4B-A dispatch repair |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source inspection, apply_patch, governance gates |
| Target paths | P4B roadmap, GC-018, P4B-A work order |
| Allowed scope source | operator instruction 2026-06-15 |
| Before status evidence | Claude draft present and uncommitted at HEAD `55e4a829` |
| After status evidence | corrected P4B-A dispatch packet |
| Diff evidence | material commit range and pre-dispatch gates |
| Approval boundary | P4B-A deterministic implementation only |
| Claim boundary | no live provider, credential use, quota spend, or public claim |
| Agent type | Codex orchestrator |
| Invocation ID | `p4b-a-dispatch-repair-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes only deterministic P4B-A implementation. It does not
prove or authorize live provider behavior, credential use, provider quality,
cost improvement, public readiness, production readiness, or P4B-B.
