# CVF GC-018 RTAD-T3 Model Gateway Live Run

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-18

Owner: Codex

rawMemoryReleased: false

GC-018 class: runtime-entry-admission-model-gateway-live-run

## Purpose

Authorize and record the bounded RTAD-T3 Model Gateway live proof requested by
the operator after RTAD-T2 deterministic closure.

## Authorization / Decision

Operator authorization was given in chat on 2026-06-18: Codex may use existing
available API keys for a Model Gateway live run. This authorization is bounded
to a secret-safe proof through the existing Model Gateway live-proof harness.

Decision: AUTHORIZE_AND_CLOSE RTAD-T3 as a bounded live proof. This baseline
does not authorize provider registry mutation, public-sync, MCP gateway
implementation, release-facing claims, external-facing readiness, provider
ranking, or raw key disclosure.

## Decision / Baseline / Tranche

| Field | Disposition |
|---|---|
| Decision | AUTHORIZE_AND_CLOSE |
| Execution base | `d3060e64` |
| Tranche | RTAD-T3 Model Gateway Live Run |
| Worker | Codex |
| Commit mode | `WORKER_MAY_COMMIT` |
| Reviewer/closer | Codex single-agent multi-role |
| Live/provider authorization | Existing available API keys, bounded proof only |
| Secret boundary | Raw keys must not be printed, written, or committed |

## Source Authority

- RTAD roadmap:
  `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`
- RTAD-T2 deterministic closure:
  `docs/reviews/CVF_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_COMPLETION_2026-06-18.md`
- Model Gateway live-proof harness:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
- Existing approved key source:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RTAD-T2 closed local deterministic Model Gateway pilot | `docs/reviews/CVF_RTAD_T2_MODEL_GATEWAY_RUNTIME_ADMISSION_PILOT_COMPLETION_2026-06-18.md` | `## Findings / Position` | `CLOSED_PASS_BOUNDED` | RTAD-T2 closure | ACCEPT |
| Live proof harness exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `runLiveProof` export | `runLiveProof` | Model Gateway live-proof harness | ACCEPT |
| Live proof chain uses credential boundary | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `CredentialBoundary` import/use | `CredentialBoundary` | Model Gateway credential boundary | ACCEPT |
| Live proof chain uses provider bridge | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | bridge construction and execute call | `ProviderExecutionBridge` | Model Gateway provider bridge | ACCEPT |
| Operator-approved local key file exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` | file existence and alias-only scan | key aliases only, values not read into evidence | local secret source | ACCEPT |

## Authorized Deliverables

- `docs/work_orders/CVF_AGENT_WORK_ORDER_RTAD_T3_MODEL_GATEWAY_LIVE_RUN_FOR_CODEX_2026-06-18.md`
- `docs/reviews/CVF_RTAD_T3_MODEL_GATEWAY_LIVE_RUN_COMPLETION_2026-06-18.md`
- `docs/reviews/evidence/rtad-t3-model-gateway-live-run-receipt-2026-06-18.json`
- RTAD roadmap update for RTAD-T3 closure.

## Forbidden Scope

RTAD-T3 must not:

- print or commit raw API keys;
- mutate provider registries or provider capability registries;
- implement MCP gateway/tooling;
- edit public-sync;
- claim release readiness, production readiness, or public readiness;
- promote any provider as canonical, preferred, or ranked;
- perform repeated live reruns after a failure without recording a diagnostic.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Live run uses existing available keys only through secret-safe environment handling. |
| AC2 | Receipt records key alias and presence only, never raw key values. |
| AC3 | At least one provider path reaches `ProviderExecutionBridge.execute` and returns a governed receipt/response. |
| AC4 | Any failed or partial candidate records a safe diagnostic before any later rerun. |
| AC5 | Completion states the bounded claim and does not claim release/public/external readiness. |

## Evidence / Verification

- Live run command through `npx tsx -` from `EXTENSIONS/CVF_MODEL_GATEWAY`.
- Receipt:
  `docs/reviews/evidence/rtad-t3-model-gateway-live-run-receipt-2026-06-18.json`
- Secret-safety scan before commit.
- `git diff --check`.
- pre-closure autorun on committed material range.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance live proof using operator-local credentials. No
public-sync batch is authorized.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RUNTIME_SIGNAL_GAP` |
| Learning lane | `RUNTIME_BEHAVIOR_LEARNING` |
| Escalation state | `NO_NEW_RULE_NEEDED` |
| Next control action | Record bounded live proof result and keep MCP/registry/public-sync parked |
| Worker blame | `N/A_WITH_REASON`: operator-authorized live proof was bounded and diagnostic-backed |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 RTAD-T3 live-run authorization |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, npx tsx, Model Gateway live-proof harness |
| Target paths | this GC-018; RTAD-T3 work order; RTAD-T3 completion; RTAD-T3 receipt; RTAD roadmap |
| Allowed scope source | operator chat authorization on 2026-06-18 |
| Before status evidence | execution base `d3060e64`; RTAD-T2 closure sync complete |
| After status evidence | RTAD-T3 live proof receipt written |
| Diff evidence | `git diff --name-status d3060e64..HEAD` |
| Approval boundary | bounded secret-safe Model Gateway live proof |
| Claim boundary | no raw key disclosure, registry mutation, MCP implementation, public-sync, release readiness, external-facing readiness, or provider ranking |
| Expected manifest | this GC-018; RTAD-T3 work order; RTAD-T3 completion; RTAD-T3 receipt; RTAD roadmap |
| Actual changed set | this GC-018; RTAD-T3 work order; RTAD-T3 completion; RTAD-T3 receipt; RTAD roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

RTAD-T3 proves only one bounded live Model Gateway path using existing
operator-approved local keys. It does not prove general provider readiness,
release readiness, public readiness, registry readiness, MCP readiness, or
external-facing readiness.
