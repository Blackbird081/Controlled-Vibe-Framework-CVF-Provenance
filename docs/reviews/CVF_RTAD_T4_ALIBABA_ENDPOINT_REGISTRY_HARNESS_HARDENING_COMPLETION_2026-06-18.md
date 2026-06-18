# CVF RTAD-T4 Alibaba Endpoint Registry Harness Hardening Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-18

Owner: Codex

rawMemoryReleased: false

executionBaseHead: 5b13bac7

## Purpose

Close RTAD-T4 after hardening Model Gateway Alibaba endpoint handling and
bounded free-quota model registry visibility, then rerunning the governed live
harness instead of relying on a direct probe.

## Scope / Methodology

Scope:

- add a Model Gateway runtime mirror of the governed Alibaba free-quota model
  ledger;
- make Alibaba DashScope live harness default endpoint handling align with the
  current key scope while keeping explicit env override support;
- register the 18 operator-confirmed free-quota Alibaba Model Studio LLM model
  codes as bounded `complete`/`chat` candidates;
- rerun the governed Model Gateway live harness and write a secret-safe receipt.

Methodology:

1. Used the committed governed ledger under `docs/reference/model_gateway/` as
   the source for model code and expiration metadata.
2. Added runtime expiration preflight helpers for Alibaba free-quota models.
3. Updated capability registry, live harness, runner, and tests.
4. Ran Model Gateway typecheck and test suite.
5. Ran the governed live harness with an RTAD-T4 receipt path.

## Findings / Position

Position: `CLOSED_PASS_BOUNDED`.

The prior diagnostic was real: direct probes showed the current operator key
works against `dashscope-intl.aliyuncs.com`, while the old harness default used
the mainland DashScope endpoint. RTAD-T4 moves that lesson into Model Gateway
runtime code and registry metadata, so future agents do not need to remember it
from chat or provider-local memory.

## Risk / Corrective Action

| Risk | Corrective action | Result |
|---|---|---|
| Endpoint/key-scope mismatch misread as provider failure | Alibaba default endpoint now resolves to `dashscope-intl.aliyuncs.com` with env override support | PASS |
| Free-quota expiration misread as gateway failure | Runtime helper classifies `usable`, `expired`, or `unknown` before live use | PASS |
| Direct-probe-only knowledge | Governed harness rerun writes receipt with endpoint host and free-quota status | PASS |
| Broad provider parity creep | Registry metadata states bounded free-quota candidate only | PASS |
| Raw key leakage | Receipt records alias and key presence only | PASS |

## Source Verification Block

| Claimed item | Source file | Verified path or symbol | Disposition |
|---|---|---|---|
| Governed Alibaba free-quota ledger exists | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `models`; `defaultEndpointHostForCurrentKey` | ACCEPT |
| Model Gateway capability registry owns provider model visibility | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | ACCEPT |
| Governed live harness owns bridge execution proof | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | `runLiveProof` | ACCEPT |
| Live runner writes receipt artifacts | `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts` | `resolveReceiptPath`; `attemptCandidate` | ACCEPT |
| RTAD roadmap records runtime admission sequence | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md` | `## Tranche Plan` | ACCEPT |

## Implementation Summary

Changed runtime and test surfaces:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`

Changed governance/evidence surfaces:

- `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`
- `docs/reviews/CVF_RTAD_T4_ALIBABA_ENDPOINT_REGISTRY_HARNESS_HARDENING_COMPLETION_2026-06-18.md`
- `docs/reviews/evidence/rtad-t4-alibaba-endpoint-registry-harness-receipt-2026-06-18.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-alibaba-free-quota-ledger-source.json`
- `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-alibaba-stream-adapter-source.json`
- `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-provider-capability-registry-source.json`
- `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-provider-capability-registry-tests.json`

## Live Run Diagnostic

| Provider | Model | Endpoint host | Free-quota status | Outcome | Latency ms | Diagnostic class |
|---|---|---|---|---|---|---|
| alibaba | qwen3.7-plus | `dashscope-intl.aliyuncs.com` | `usable` | PASS | 5587 | N/A with reason: provider returned governed response |

## Evidence Receipt

Receipt:
`docs/reviews/evidence/rtad-t4-alibaba-endpoint-registry-harness-receipt-2026-06-18.json`

Secret-safety note: the receipt records `keyAliasUsed: DASHSCOPE_API_KEY` and
`keyPresent: true` only. It does not record raw API key values.

## Gate Results

| Gate | Command | Result |
|---|---|---|
| Model Gateway typecheck | `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY` | PASS |
| Model Gateway tests | `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY` | PASS, 29 files / 219 tests |
| Governed live harness | `npx tsx EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts` with RTAD-T4 receipt path | PASS |
| Diff hygiene | `git diff --check` | pending final pre-commit run |
| Pre-closure autorun | `run_agent_autorun_workflow_gate.py --phase pre-closure --base 5b13bac7 --head HEAD` | pending final material range |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator directly authorized Codex to proceed after accepting RTAD-T4 recommendation | no delegated worker order in this batch | N/A with reason |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md` | `Status: RTAD_T4_CLOSED_PASS_BOUNDED` | PASS |
| Evidence receipt | `docs/reviews/evidence/rtad-t4-alibaba-endpoint-registry-harness-receipt-2026-06-18.json` | `overall: PASS` | PASS |
| Registry JSON | BLOCKED with reason: no product provider JSON registry exists for this package; Model Gateway provider capability registry is TypeScript | TypeScript registry updated instead | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: stable ledger front door already exists at `docs/reference/model_gateway/README.md`; no new Markdown registry needed | no registry Markdown path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: live receipt is repo-local governed evidence | no external digest path changed | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit authorized | no interlock path changed | N/A with reason |
| Session continuity | separate session-sync follows material commit if needed | active handoff update after material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Criterion | Required value | Observed value | Status |
|---|---|---|---|
| Overall receipt result | PASS | PASS | PASS |
| Endpoint host | current key-compatible host | `dashscope-intl.aliyuncs.com` | PASS |
| Free-quota preflight | model usable before live call | `freeQuotaStatus: usable` | PASS |
| Registry coverage | 18 free-quota models visible in capability registry | test covers all ledger rows | PASS |
| Raw key safety | no raw keys in receipt | alias/presence only | PASS |
| Readiness boundary | no release/public/external readiness claim | bounded runtime hardening only | PASS |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance live proof using operator-local credentials. No
public-sync batch is authorized.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RUNTIME_SIGNAL_GAP` |
| Learning lane | `RUNTIME_BEHAVIOR_LEARNING` |
| Escalation state | `RULE_AND_RUNTIME_CONTROL_ADDED` |
| Next control action | Use runtime endpoint resolver and free-quota preflight before future Alibaba live harness runs |
| Worker blame | `N/A_WITH_REASON`: the finding came from live provider/key scope evidence, not worker negligence |

## Epistemic Process Block

### Expected Result / Prediction

If the endpoint/key-scope diagnostic was correct, the governed harness should
pass when using the international DashScope endpoint and a still-usable
free-quota model.

### Evidence Comparison

The prediction matched the evidence: Alibaba `qwen3.7-plus` passed through the
governed bridge with endpoint host `dashscope-intl.aliyuncs.com` and
`freeQuotaStatus: usable`.

### Contradiction Or Gap Disposition

No contradiction remains for this bounded claim. The result does not prove
broad provider reliability or parity.

### Claim Update

Claim upgraded from direct diagnostic knowledge to governed runtime handling
and a passing governed harness receipt.

## Evidence Trace Block

| Artifact | Evidence |
|---|---|
| Source authority | operator-supplied Alibaba screenshots, governed ledger under `docs/reference/model_gateway/`, RTAD roadmap, Model Gateway source |
| Runtime changes | Alibaba endpoint resolver, capability registry metadata, live harness runner preflight |
| Live receipt | `docs/reviews/evidence/rtad-t4-alibaba-endpoint-registry-harness-receipt-2026-06-18.json` |
| Command output | `P4B-B candidate alibaba/qwen3.7-plus: PASS endpointHost=dashscope-intl.aliyuncs.com freeQuotaStatus=usable latencyMs=5587` |
| Secret safety | alias-only receipt and no raw key output |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 RTAD-T4 Alibaba endpoint registry harness hardening |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, npm, npx tsx, Model Gateway live-proof harness, governance gates |
| Target paths | runtime helper, capability registry, endpoint harness, runner, tests, RTAD roadmap, this completion, RTAD-T4 receipt |
| Allowed scope source | operator accepted Codex recommendation to open RTAD-T4 after Alibaba endpoint/free-quota finding |
| Before status evidence | execution base `5b13bac7`; RTAD-T3 closed; Alibaba free-quota ledger committed |
| After status evidence | RTAD-T4 material diff ready for commit |
| Diff evidence | `git diff --name-status 5b13bac7..HEAD` |
| Approval boundary | bounded Alibaba endpoint/free-quota registry hardening and governed harness rerun |
| Claim boundary | no raw key disclosure, public-sync, MCP implementation, release readiness, external-facing readiness, provider ranking, or broad provider parity |
| Agent type | Codex |
| Invocation ID | `rtad-t4-alibaba-endpoint-registry-harness-hardening-codex-2026-06-18` |
| Expected manifest | `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-alibaba-free-quota-ledger-source.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-alibaba-stream-adapter-source.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-provider-capability-registry-source.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-provider-capability-registry-tests.json`; `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`; `docs/reviews/CVF_RTAD_T4_ALIBABA_ENDPOINT_REGISTRY_HARNESS_HARDENING_COMPLETION_2026-06-18.md`; `docs/reviews/evidence/rtad-t4-alibaba-endpoint-registry-harness-receipt-2026-06-18.json` |
| Actual changed set | `EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-alibaba-free-quota-ledger-source.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-alibaba-stream-adapter-source.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-provider-capability-registry-source.json`; `docs/corpus-intelligence/registry/entries/model-gateway-rtad-t4-provider-capability-registry-tests.json`; `docs/roadmaps/CVF_RUNTIME_ENTRY_ADMISSION_ROADMAP_2026-06-18.md`; `docs/reviews/CVF_RTAD_T4_ALIBABA_ENDPOINT_REGISTRY_HARNESS_HARDENING_COMPLETION_2026-06-18.md`; `docs/reviews/evidence/rtad-t4-alibaba-endpoint-registry-harness-receipt-2026-06-18.json` |
| Manifest delta | MATCH after final diff check |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

RTAD-T4 closes only Alibaba endpoint handling, bounded free-quota registry
visibility, expiration preflight, and one governed harness rerun. It does not
claim provider ranking, broad provider parity, MCP readiness, release
readiness, public readiness, external-facing readiness, or general provider
reliability.
