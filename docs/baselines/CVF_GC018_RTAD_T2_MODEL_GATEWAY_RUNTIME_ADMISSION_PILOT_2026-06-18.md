# CVF GC-018 RTAD-T2 Model Gateway Runtime Admission Pilot

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-06-18

Owner: Codex

rawMemoryReleased: false

GC-018 class: runtime-entry-admission-model-gateway-pilot

## Purpose

Authorize a bounded RTAD-T2 work order for a Model Gateway runtime-admission
pilot. The pilot must validate the current local Model Gateway entry boundary
from source and deterministic tests before any later live/provider or MCP
gateway work is opened.

## Authorization / Decision

Operator selected Model Gateway as the first runtime focus on 2026-06-18.
RTAD-T1 accepted that selection in
`docs/reviews/CVF_RTAD_T1_MODEL_GATEWAY_RUNTIME_PILOT_SELECTION_2026-06-18.md`.

Decision: AUTHORIZE RTAD-T2 dispatch for a local deterministic Model Gateway
runtime-admission pilot. This baseline does not authorize live/provider calls,
credential use, public-sync, registry mutation, release-readiness claims,
external-facing claims, or MCP gateway implementation.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | AUTHORIZE |
| Baseline | `f74dab2f` |
| Proposed tranche | RTAD-T2 Model Gateway Runtime Admission Pilot |
| Worker | Codex |
| Commit mode | `WORKER_MAY_COMMIT` |
| Reviewer/closer | Codex single-agent multi-role with operator as escalation point |
| Runtime authorization | Local deterministic Model Gateway checks only |
| Live/provider authorization | Not authorized |

## Source Authority

- RTAD roadmap:
  `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`
- RTAD-T1 selection:
  `docs/reviews/CVF_RTAD_T1_MODEL_GATEWAY_RUNTIME_PILOT_SELECTION_2026-06-18.md`
- Model Gateway P4B-B live-proof completion:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P4B_B_LIVE_PROOF_T2_COMPLETION_2026-06-15.md`
- Model Gateway runtime source:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
- Model Gateway package manifest:
  `EXTENSIONS/CVF_MODEL_GATEWAY/package.json`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RTAD-T0 left runtime parked until fresh runtime-specific GC-018/work order | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md` | `## Current Runtime Freshness Verification` | RTAD runtime parked boundary | RTAD roadmap | ACCEPT |
| RTAD-T1 selected Model Gateway as first pilot | `docs/reviews/CVF_RTAD_T1_MODEL_GATEWAY_RUNTIME_PILOT_SELECTION_2026-06-18.md` | `## Selection Decision` | `EXTENSIONS/CVF_MODEL_GATEWAY` | RTAD-T1 decision | ACCEPT |
| Provider execution bridge has a stable execute entrypoint | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 58-78 | `ProviderExecutionBridge` | Model Gateway source | ACCEPT |
| Bridge admission guard exists and consumes adapter admission records | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-bridge-admission-guard.ts` | lines 14-35 | `checkBridgeAdmission` | Model Gateway source | ACCEPT |
| Provider adapter admission exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | lines 19-56 | `admitProviderAdapter` | Model Gateway source | ACCEPT |
| Capability negotiation exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts` | lines 13-36 | `negotiateProviderCapability` | Model Gateway source | ACCEPT |
| Prior proof harness exists but network mode remains out of scope here | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | lines 42-100 and 190-274 | `runLiveProof` | Model Gateway source | ACCEPT |
| Deterministic check/test scripts exist | `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` | scripts block | `check`; `test` | Model Gateway package manifest | ACCEPT |

## Authorized Deliverables

RTAD-T2 worker may create:

- `docs/reviews/CVF_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_PACKET_2026-06-18.md`
- `docs/reviews/CVF_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_COMPLETION_2026-06-18.md`
- optional local no-network evidence receipt under
  `docs/reviews/evidence/rtad-t2-model-gateway-runtime-admission-pilot-2026-06-18.json`

RTAD-T2 worker may edit only if a deterministic local pilot requires it:

- focused test or script files under `EXTENSIONS/CVF_MODEL_GATEWAY/`;
- GC-051 corpus registry source entries and generated aggregate only if a new
  source/test/script file is created and must be indexed.

No edit is required if current deterministic source and tests already satisfy
the pilot boundary.

## Forbidden Scope

RTAD-T2 must not:

- run live/provider API calls;
- read, print, or use provider credentials;
- edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`;
- edit `PROVIDER_CAPABILITY_REGISTRY` or provider capability registry entries;
- edit public-sync;
- implement MCP gateway/tooling;
- claim release readiness or external-facing readiness;
- mutate active session or handoff files except in a separate session-sync
  range after material closure.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker packet re-verifies current Model Gateway source symbols from disk before executing checks. |
| AC2 | `npm run check` passes in `EXTENSIONS/CVF_MODEL_GATEWAY`. |
| AC3 | `npm test` passes in `EXTENSIONS/CVF_MODEL_GATEWAY`, or any failure is classified with a source-backed blocker. |
| AC4 | Pilot packet records whether a no-network evidence receipt was produced or why it was not needed. |
| AC5 | No live/provider credential, public-sync, registry mutation, MCP implementation, production-readiness, or public-readiness claim appears in the completion. |
| AC6 | Any finding is promoted to a governed artifact disposition, not provider-local memory only. |

## Evidence / Verification

Required before RTAD-T2 closure:

- `git rev-parse --short HEAD`;
- `git status --short`;
- source-symbol re-verification using `rg -n`;
- `npm run check` from `EXTENSIONS/CVF_MODEL_GATEWAY`;
- `npm test` from `EXTENSIONS/CVF_MODEL_GATEWAY`;
- `git diff --check`;
- pre-closure autorun gate on the accepted material range;
- session-sync steward only after material closure if next move changes.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-admission baseline. No public-sync batch is
authorized.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `ORCHESTRATOR_PACKET_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `WORK_ORDER_ADDED` |
| Next control action | RTAD-T2 work order runs a source-backed local Model Gateway admission pilot before any live/provider or MCP work |
| Worker blame | `N/A_WITH_REASON`: this baseline narrows the next runtime step |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 RTAD-T2 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | RTAD roadmap; RTAD-T1 packet; this GC-018; RTAD-T2 work order |
| Allowed scope source | operator selected Model Gateway and asked Codex to continue RTAD-T1/T2 |
| Before status evidence | base `f74dab2f`; RTAD-T0 closed and runtime parked |
| After status evidence | pending RTAD-T2 dispatch commit |
| Diff evidence | `git diff --name-status f74dab2f..HEAD` |
| Approval boundary | GC-018 and work-order dispatch only |
| Claim boundary | no runtime/provider/live/public-sync/registry/product mutation in this dispatch batch |
| Expected manifest | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`; `docs/reviews/CVF_RTAD_T1_MODEL_GATEWAY_RUNTIME_PILOT_SELECTION_2026-06-18.md`; `docs/baselines/CVF_GC018_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_FOR_CODEX_2026-06-18.md` |
| Actual changed set | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`; `docs/reviews/CVF_RTAD_T1_MODEL_GATEWAY_RUNTIME_PILOT_SELECTION_2026-06-18.md`; `docs/baselines/CVF_GC018_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_FOR_CODEX_2026-06-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This GC-018 authorizes only RTAD-T2 dispatch for a local deterministic Model
Gateway runtime-admission pilot. It does not authorize live/provider proof,
credential use, registry mutation, public-sync, MCP implementation, production
readiness, or external-facing readiness.
