# CVF Agent Intelligence Absorption Roadmap
## LHW22 + LHW23 + LHW24

Memory class: POINTER_RECORD

Status: LHW22_READY_FOR_DISPATCH_LHW23_HOLD_UNTIL_LHW22_PASS_LHW24_HOLD_UNTIL_LHW23_PASS

docType: roadmap

Date: 2026-05-31

## Purpose

Define the next three documentation-only advisory waves for remaining
agent-intelligence value from the LHW20 full scan of
`.private_reference/legacy/CVF_Important/`.

This roadmap now records disposition for all `ACCEPT_AS_OWNER_MAP` concepts in
the source audit. It does not claim every accepted concept is implemented in
these three waves; concepts already closed or deferred to a separate wave are
listed explicitly.

## Scope / Target / Owner Boundary

Target: three sequential LHW advisory waves.

Owner surface: CVF private-provenance governance and documentation surfaces.

Allowed scope:

- LHW22: UCO, Agent Self-Report, Capability Registry advisory specs.
- LHW23: Model Registry, multi-factor routing, Execution Strategy advisory
  specs, held until LHW22 closure.
- LHW24: Feedback Loop to Strategy Registry, Memory Sync Protocol, Relevance
  Ranking advisory specs, held until LHW23 closure.
- Fresh GC-018 is required per wave.
- Completion reviews and session continuity updates are required only when a
  wave closes.

Forbidden scope:

- Runtime code changes.
- Route, receipt, provider, model, prompt, public-sync, or live-provider changes.
- Autonomous learning mutation.
- Production-readiness, public-readiness, or universal-governance claims.
- Demand-gated group B items without a separate operator trigger.

## Authorization / Decision

Decision: authorize LHW22 for dispatch after fresh GC-018
`docs/baselines/CVF_GC018_LHW22_AGENT_INTELLIGENCE_FOUNDATIONS_2026-05-31.md`.

LHW23 and LHW24 remain hold packets. They are planning records only until their
own prerequisites and fresh GC-018 packets exist.

Operator direction on 2026-05-31: review and repair Claude-created roadmap and
work orders, tighten guards first, then use the guards to clean the packet.

## Current Runtime Freshness Verification

The source audit is a knowledge-absorption snapshot, not the only source of
truth. Current runtime/source surfaces checked for this roadmap:

| Current source fact | Current source file | Verified path or symbol | Disposition |
|---|---|---|---|
| Provider registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry` | LHW23 must say partial, not absent |
| Provider capability registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | LHW23 must say partial, not absent |
| Role provider resolver exists in CLI | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | `resolveProviderForRole` | LHW23 owner path corrected |
| Routing policy already checks policy, health, and quota | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | `RoutingPolicyEngine` | LHW23 gap is missing full context+plan+risk strategy selection |
| Execution facade has two strategy literals | `EXTENSIONS/CVF_PLANE_FACADES/src/execution.facade.ts` | `ModelRoutingRequest.strategy` | LHW23 gap is incomplete 5-pattern taxonomy |
| Feedback ledger exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/feedback.ledger.contract.ts` | `FeedbackLedgerContract` | LHW24 must say partial, not absent |
| Learning-signal bridge exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts` | `LearningSignalIntakeBridge` | LHW24 gap is no strategy-registry update orchestrator |
| Memory lifecycle promotion and expiry exist | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | `evaluateLifecycleTransition` | LHW24 gap is no automatic sync protocol |
| Context packager uses token budget but no ranking score fields | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | `packageMemoryContext` | LHW24 relevance ranking remains valid |

## ACCEPT_AS_OWNER_MAP Coverage Disposition

Source audit:
`docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md`

| Accepted concept from audit | Roadmap disposition | Evidence / next owner |
|---|---|---|
| UCO - Capability-based constraint binding | LHW22 T1 | `CVF_GUARD_CONTRACT` + `CVF_v1.2_CAPABILITY_EXTENSION` |
| Adaptation Policy Engine (Risk Budget, Tiers, Cooldown) | SATISFIED_BY_PRIOR_CLOSURE | APE1 and LHW20 T3 closed this at advisory/runtime-advisory boundary |
| Agent Self-Report protocol | LHW22 T2 | `/api/execute` future additive response schema advisory |
| Execution Strategy Model | LHW23 T3 | Normalizes LHW20 T2 against current source surfaces |
| Feedback Loop to Strategy Registry | LHW24 T1 | LPF feedback surfaces plus missing strategy-registry coordinator |
| Memory Sync Protocol | LHW24 T2 | LPF memory lifecycle partial plus missing automatic sync protocol |
| Relevance Ranking in Context Packager | LHW24 T3 | LPF context packager owner |
| Capability Registry (Task-to-Capability-to-Agent) | LHW22 T3 | `CVF_ECO_v2.3_AGENT_IDENTITY` + capability contracts |
| Model Registry Service | LHW23 T1 | `CVF_MODEL_GATEWAY` registry surfaces |
| Multi-factor routing policy | LHW23 T2 | `RoutingPolicyEngine` + CLI role resolver surfaces |
| Artifact Store abstraction | DEFERRED_SEPARATE_WAVE | Needs Git-for-AI/artifact-store owner mapping; not bundled into LHW22-LHW24 |
| Full 9-item Security Hardening Checklist (6 remaining) | SATISFIED_BY_LHW20_T1 | LHW20 T1 documented the remaining hardening items |

## Non-Goals

- No code implementation.
- No runtime receipt field.
- No provider routing behavior change.
- No public export or public catalog claim.
- No group B demand-gated work.
- No claim that current runtime surfaces are absent when they are partial.

## Work Plan

| Wave | Status | Work order | Prerequisite |
|---|---|---|---|
| LHW22 | READY_FOR_DISPATCH | `docs/work_orders/CVF_WO_LHW22_AGENT_INTELLIGENCE_FOUNDATIONS_2026-05-31.md` | LHW20 closed; fresh GC-018 filed |
| LHW23 | HOLD_UNTIL_LHW22_PASS | `docs/work_orders/CVF_WO_LHW23_ROUTING_REGISTRY_INTELLIGENCE_2026-05-31.md` | LHW22 closure plus fresh GC-018 |
| LHW24 | HOLD_UNTIL_LHW23_PASS | `docs/work_orders/CVF_WO_LHW24_LEARNING_LOOP_COMPLETION_2026-05-31.md` | LHW23 closure plus fresh GC-018 |

## Acceptance Criteria

- LHW22 work order passes pre-dispatch guard before Claude or any implementer
  authors specs.
- LHW23 and LHW24 remain hold packets until prerequisites are met.
- Every accepted concept from the LHW20 audit has an explicit disposition.
- All source facts cite current source paths, not audit memory alone.
- Each wave remains documentation-only with `runtimeExecutionAuthorized=false`.

## Verification / Evidence

Required before LHW22 dispatch:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 21e0bb8c --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 21e0bb8c --head HEAD
```

Required before later waves:

- LHW23: LHW22 closed plus fresh LHW23 GC-018.
- LHW24: LHW23 closed plus fresh LHW24 GC-018.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance planning and work-order packet. No public artifact
or public catalog claim is made.

## Claim Boundary

Planning and dispatch-control artifact only. This roadmap authorizes LHW22
documentation-only advisory spec authoring after guard pass. It does not
authorize LHW23, LHW24, runtime implementation, public-sync export, live
provider proof, autonomous mutation, production readiness, or public readiness.
