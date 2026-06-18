# CVF Model Gateway C-02 P5 Provider Adapter Admission And Capability Negotiation Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-15

rawMemoryReleased=false

Roadmap class: model-gateway-foundation

## Authorization / Decision

Operator instruction on 2026-06-15 requested the next roadmap after P4C and
the autorun range-shape guard hardening. The next move must stay foundation
level, must not enter a narrow provider use case, and must not make Alibaba or
DeepSeek the product design center.

Decision: create a P5 roadmap for provider-agnostic adapter admission and
capability negotiation. This roadmap prepares CVF to accept user-supplied
adapters under control, without selecting or privileging any concrete provider.

## Purpose

P4B-A established a deterministic `ProviderExecutionBridge` with injected
adapters. P4C established deterministic provider-adapter conformance. The
remaining foundation gap is the admission lifecycle between those two surfaces:

1. a candidate adapter can conform locally;
2. CVF still needs a governed record that says whether that adapter is admitted
   for a provider/model/method boundary;
3. the bridge should eventually consume only admitted adapter evidence, not an
   arbitrary injected object with no admission trace.

P5 is valuable because it generalizes Model Gateway beyond current live-test
providers. A user may bring any adapter later; CVF core should control the
adapter admission evidence, capability negotiation, and execution boundary.

## Scope

### In Scope

- Define a deterministic provider-agnostic adapter admission record.
- Use P4C conformance as a required input, not a replacement.
- Add capability negotiation for requested provider/model/method against the
  declared capability registry and supported method aliases.
- Produce machine-readable admission statuses such as `admitted`, `blocked`,
  and `needs_operator_authorization`.
- Preserve `liveExecutionAuthorized=false` for P5.
- Keep concrete provider adapters as samples only, not canonical sources.
- Prepare a later work order for Claude to implement deterministic source,
  tests, registry entries, and worker-return evidence.

### Out Of Scope

- Live provider/API calls, network, `fetch`, provider endpoints, `.env.local`,
  runtime secret access, quota spend, or live-run diagnostics.
- Choosing Alibaba, DeepSeek, OpenAI, or any provider as canonical.
- Adding a new provider or model.
- P4B-B concrete live proof.
- EPF wiring, Strategy Layer implementation, AI Gateway absorption, public
  sync, production readiness, or public readiness.
- Legacy folder scan or broad knowledge absorption.

## Non-Goals

- Do not prove provider quality, cost, latency, availability, or live behavior.
- Do not build a marketplace, plugin installer, or co-work product layer.
- Do not grant autonomous adapter mutation authority.
- Do not bypass P4C conformance.
- Do not let `ProviderExecutionBridge` execute unadmitted adapters in the P5
  target design.

## Design Control Gate

| Control | P5 decision |
|---|---|
| Foundation value | High: turns P4C conformance into reusable adapter admission evidence |
| Provider neutrality | Required: no hardcoded accepted provider IDs |
| Live boundary | P4B-B remains `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION` |
| Credential boundary | metadata flags only; no secret reads |
| Existing owner reuse | P4C conformance, provider method gate, capability registry, P4B-A bridge |
| Legacy disposition | cite `MGW-001`; no new legacy scan |
| Claim boundary | deterministic local admission and negotiation only |

## Proposed P5 Tranche Sequence

| Tranche | Name | Scope | Stop condition |
|---|---|---|---|
| P5-A | Adapter Admission Record | admission record type, status, reason codes, trace fields | source owner mismatch or status taxonomy bloat |
| P5-B | Capability Negotiation | method normalization, supported-method negotiation, blocked/fallback reasons | provider-specific branching or invented registry fields |
| P5-C | Bridge Admission Boundary | bridge accepts admitted adapter evidence before execution | any live call, credential read, or concrete provider binding |

Recommended first tranche: P5-A + P5-B together only if the implementation can
stay below file-size thresholds. Otherwise split P5-A first.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| P4C conformance input exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 26 | `ProviderAdapterConformanceInput` | provider adapter conformance | ACCEPT |
| P4C conformance report exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 35 | `ProviderAdapterConformanceReport` | provider adapter conformance | ACCEPT |
| P4C local evaluator exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | line 54 | `evaluateProviderAdapterConformance` | provider adapter conformance | ACCEPT |
| P4C keeps live execution unauthorized | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts` | lines 44 and 121 | `liveExecutionAuthorized` | provider adapter conformance report | ACCEPT |
| P4B-A adapter contract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 37 | `ProviderExecutionAdapter` | provider execution bridge | ACCEPT |
| P4B-A bridge execute method exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | line 73 | `execute` | ProviderExecutionBridge | ACCEPT |
| Provider registry register method exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 38 | `register` | ProviderRegistry | ACCEPT |
| Provider registry assert method exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 96 | `assertAllowed` | ProviderRegistry | ACCEPT |
| Provider capability file shape exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 34 | `ProviderCapabilityFile` | provider method contract | ACCEPT |
| Method normalization exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 24 | `normalizeProviderMethodName` | provider method gate | ACCEPT |
| Capability lookup exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 46 | `findProviderCapability` | provider method gate | ACCEPT |
| Supported method listing exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | line 89 | `listRegistrySupportedMethods` | provider method gate | ACCEPT |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P5 contribution | Adds adapter admission and capability negotiation above P4C conformance |
| Closure rule | P5 must not promote `MGW-001` to complete |
| P4B-B rule | Concrete live proof remains held and separate |

No new legacy scan is authorized by this roadmap.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Admission result is provider-agnostic and contains no hardcoded accepted providers | source review and tests |
| AC2 | Non-conformant P4C reports always block admission | deterministic tests |
| AC3 | Conformant adapter can become `admitted` only when provider/model/method capability negotiation passes | deterministic tests |
| AC4 | Missing provider, missing model, unsupported method, and alias normalization produce explicit reason codes | deterministic tests |
| AC5 | Admission output records `liveExecutionAuthorized=false` | deterministic tests |
| AC6 | No provider URL, network call, `.env.local`, API key token, or runtime secret access appears in P5 files | negative search |
| AC7 | Source and test files remain below governed file-size thresholds | file-size guard |
| AC8 | Model Gateway type check and full test suite pass | command evidence |
| AC9 | GC-051 entries are added for new governed source/test files | registry drift check |

## Verification

Future P5 implementation work order must require:

- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `npm test -- --run` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `python governance/compat/generate_corpus_scan_registry.py --check`.
- `python governance/compat/run_worker_return_fast_gate.py`.
- `git diff --check`.
- Negative search for concrete provider preference, network calls, credential
  access, and live-proof vocabulary in new P5 source/test files.

## Work Plan

| Step | Owner | Output | Stop condition |
|---|---|---|---|
| 1 | Codex | P5 roadmap | roadmap gate failure |
| 2 | Codex | GC-018 baseline and source-verified work order | dispatch-quality failure |
| 3 | Claude | deterministic P5-A/P5-B implementation under `WORKER_MUST_NOT_COMMIT` | forbidden scope or source mismatch |
| 4 | Claude | focused tests, GC-051 entries, worker return | reviewer-fast failure outside allowed scope |
| 5 | Codex | review, allowed repair, completion review, material commit | blocking design or governance finding |
| 6 | Codex | session/handoff sync if needed | active-session state failure |

## Risk And Corrective Action

| Risk | Control |
|---|---|
| Adapter admission becomes provider-specific | hard negative search and fake-provider tests |
| P5 duplicates P4C conformance | admission must consume P4C report rather than reimplement all checks |
| Bridge executes arbitrary injected adapter | P5-C requires admitted adapter evidence boundary |
| Live proof slips into deterministic tranche | P4B-B remains explicit hold; P5 keeps `liveExecutionAuthorized=false` |
| Capability negotiation invents registry fields | source verification against existing method/capability owners |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance Model Gateway roadmap. No public-sync batch is
authorized.

## Claim Boundary

This roadmap defines the next foundation direction only. It does not implement
P5, dispatch Claude, authorize live provider/API calls, read credentials, add
providers/models, wire EPF, implement Strategy Layer, absorb AI Gateway,
public-sync, or claim production/public readiness.

## GFC-T3 Closure Note (2026-06-18)

This roadmap is closed bounded per GFC-T3 Roadmap State Hygiene Remediation
(work order `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`).
Closure evidence: `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md`
(status `CLOSED_PASS_BOUNDED`); session memory records material commit `a4907f2c`. Status line
updated from `ROADMAP_READY_FOR_GC018` to `ROADMAP_CLOSED_PASS_BOUNDED` by GFC-T3 worker.

## Current Runtime Freshness Verification

NOT_APPLICABLE_WITH_REASON: this roadmap's GFC-T3 closure note adds governance metadata only; no runtime source symbols were modified or introduced.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md` | GFC-T3 work order authorizes this status-line change; GC-018 baseline approves scope | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_PACKET_2026-06-18.md` | worker packet Status: COMPLETE_PENDING_REVIEW; this row marked REMEDIATED | PASS |
| Roadmap state | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_ROADMAP_2026-06-15.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | governance-doc-only tranche | no GC-051 registry mutation authorized or required | BLOCKED with reason: governance-doc-only status remediation |
| Registry Markdown | governance-doc-only tranche | no registry markdown update authorized or required | BLOCKED with reason: governance-doc-only status remediation |
| External evidence digest | all evidence is repo-local and git-tracked | no external artifacts or digests needed | N/A with reason |
| System loop interlock | no runtime system loop required | no API interlock needed for governance status remediation | N/A with reason |
| Session continuity | session mode unchanged | no session state file modification authorized for GFC-T3 worker | N/A with reason |
| Tranche completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P5_PROVIDER_ADAPTER_ADMISSION_AND_CAPABILITY_NEGOTIATION_COMPLETION_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED`; material commit `a4907f2c` | PASS |
| Public-sync | N/A with reason: private provenance, `DEFERRED_PRIVATE_ONLY` | N/A | N/A with reason |
