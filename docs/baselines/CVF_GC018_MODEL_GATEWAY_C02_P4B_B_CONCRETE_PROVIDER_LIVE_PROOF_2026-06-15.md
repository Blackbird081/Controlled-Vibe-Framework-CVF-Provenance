# GC-018 Model Gateway C-02 P4B-B Concrete Provider Live Proof

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-MODEL-GATEWAY-C02-P4B-B-CONCRETE-PROVIDER-LIVE-PROOF-2026-06-15

Date: 2026-06-15

Status: DRAFT_NEGATIVE_SAMPLE_DO_NOT_DISPATCH

## Purpose

Reviewer note: this packet is retained as a negative dispatch-authoring sample
after dispatch packet authoring guard hardening. It is not authorized for
implementation until a later governed repair packet replaces or corrects it.

Original intent was to authorize Codex to execute P4B-B-T0: the
source-verified live-proof packet, provider-selection matrix, and dry-run
authorization gate. T0 is doc-only -- no live provider call, no credential
secret, no network.

Live execution (T1/T2/T3) is NOT authorized by this baseline. A separate
GC-018 with explicit operator live-proof authorization is required before any
provider call may run.

## Scope / Target / Owner Boundary

Target: EXTENSIONS/CVF_MODEL_GATEWAY and docs/.

Worker/implementer owner: Codex produces the T0 doc-only artifacts:

- provider-selection matrix (which adapters exist, what env vars they expect,
  what model ids they use);
- dry-run authorization gate test (verifies harness refuses to run without
  explicit live flag);
- T1 harness skeleton that initializes bridge + admission records without
  calling a provider;
- updated legacy coverage index row if warranted;
- completion review;
- session continuity update in a separate commit.

Boundary: T0 output is all doc and test. No live API call, no env var read
with real secrets, no network, no fetch to a provider URL, no quota spend.
The dry-run gate must confirm that the harness returns a classified diagnostic
when the live flag is absent, not a provider response.

## Source / Predecessor Evidence

- P5-C completed: provider-execution-bridge.ts now contains admissionRecords
  field (line 51) and guard block (lines 156-171).
- Bridge adapter.execute() is at line 173 (post-P5-C).
- buildShieldedErrorResult is at line 264 (post-P5-C).
- admission_blocked union member: unified-gateway-interface-contract.ts line 16.
- CredentialBoundary.resolveMetadata at credential-boundary.ts line 21.
- CredentialBoundary.resolveSecretForRuntime at credential-boundary.ts line 33.
- Alibaba sample adapter: providers/alibaba/stream-adapter.ts line 28
  (createAlibabaQwenTurboStreamAdapter).
- DeepSeek sample adapter: providers/deepseek/json-mode-adapter.ts line 28
  (createDeepSeekChatJsonModeAdapter).
- P4B-B roadmap: ROADMAP_AUTHORIZATION_REQUIRED at commit 5fd4dbd2 or later.
- Active session state: CVF_SESSION/ACTIVE_SESSION_STATE.json.
- Active handoff: AGENT_HANDOFF_V19_2026-06-15.md or active successor.

## Decision / Baseline / Proposed Tranche

Decision: release P4B-B-T0 to Codex under WORKER_MAY_COMMIT. T0 is doc-only
and does not require live credential authorization.

Baseline: Codex produces a provider-selection matrix, a dry-run gate test,
and a harness skeleton. Codex may NOT run the harness against a real provider
or read real API keys in this tranche.

Live tranches T1/T2/T3 require a fresh GC-018 with:

```
I authorize Model Gateway C-02 P4B-B concrete provider live proof for
provider(s): <operator-selected provider ids>, using operator-supplied
environment variables only. The agent may run the approved live proof commands
without printing raw secrets.
```

Without that text from the operator, all T1/T2/T3 work is forbidden.

## Authority

- Operator instruction on 2026-06-15: create Codex work order using same-session
  pattern as P5/P5-C (SINGLE_AGENT_MULTI_ROLE_CODEX, WORKER_MAY_COMMIT).
- P4B-B roadmap:
  docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_ROADMAP_2026-06-15.md.
- Active session state: CVF_SESSION/ACTIVE_SESSION_STATE.json.
- Active handoff: AGENT_HANDOFF_V19_2026-06-15.md.
- Work order:
  docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_FOR_CODEX_2026-06-15.md.

## Authorized Scope (T0 only)

1. Create EXTENSIONS/CVF_MODEL_GATEWAY/docs/p4b-b-provider-selection-matrix.md:
   - table of existing sample adapters, their provider ids, model ids,
     required env var names (names only, no values), and contract methods;
   - operator-selection note: no provider is canonical; operator chooses.
2. Create EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts:
   - tests that confirm harness construction succeeds without a real API key;
   - tests that confirm dry-run execution returns a classified diagnostic
     (credential_shielded or admission_blocked) instead of a live response;
   - negative assertions: no fetch call, no real secret read, no live response.
3. Create EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts:
   - harness that constructs ProviderExecutionBridge with routing, credential
     boundary, health, quota, receipt builder, an operator-supplied adapter,
     and an admitted AdapterAdmissionRecord;
   - harness accepts a liveAuthorized: boolean flag; when false, returns a
     dry-run diagnostic without calling adapter.execute;
   - harness does NOT call resolveSecretForRuntime without liveAuthorized=true;
   - harness does NOT import fetchImpl or call network without liveAuthorized=true.
4. Create GC-051 entry files for the three new governed artifacts.
5. Regenerate docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json.
6. Author completion review.

## Not Authorized

- Reading .env.local or resolving a live runtime credential.
- Calling CredentialBoundary.resolveSecretForRuntime with a real key present.
- Calling fetch, provider URLs, or any network in harness or test.
- Running harness with liveAuthorized=true.
- Calling createAlibabaQwenTurboStreamAdapter or createDeepSeekChatJsonModeAdapter
  with real options in tests.
- Selecting Alibaba, DeepSeek, or any provider as canonical CVF product scope.
- Adding a new provider or model id.
- Removing or modifying existing bridge, admission, or conformance behavior.
- T1/T2/T3 live execution without operator authorization text.
- Public-sync, EPF, Strategy Layer, AI Gateway, or scope expansion.
- Raw memory release.

## P4B-B Live Tranche Hold

Status: HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION.

T1/T2/T3 require a fresh GC-018 with explicit operator authorization naming
provider ids, env var aliases, and live quota consent. This baseline does not
release those tranches.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md |
| Row | MGW-001 |
| Current status | PARTIAL_RECHECK_REQUIRED |
| P4B-B-T0 contribution | documents live-proof boundary; does not close gap |
| Closure rule | MGW-001 may update to reflect T0 doc but must not claim complete |
| T1/T2 rule | Live proof row closure requires separate authorization |

## Verification

- Pre-dispatch autorun must pass before material commit.
- Codex must run type check, full Model Gateway tests, GC-051 drift check,
  worker fast gate, and diff hygiene before commit.
- Codex owns committed-range pre-closure and session synchronization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (GC-018 and work order author) |
| Provider or surface | Claude Code local workspace |
| Session or invocation | 2026-06-15 P4B-B-T0 dispatch authoring |
| Working directory | d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | Read, Write, Bash wc/line verification |
| Target paths | P4B-B GC-018 and Codex work order |
| Allowed scope source | operator instruction 2026-06-15 + P4B-B roadmap |
| Before status evidence | P5-C complete; P4B-B roadmap ROADMAP_AUTHORIZATION_REQUIRED |
| After status evidence | P4B-B-T0 GC-018 and work order authored for Codex |
| Diff evidence | dispatch range from current HEAD |
| Approval boundary | T0 doc-only; T1/T2/T3 require separate live authorization |
| Claim boundary | no live provider, credential use, quota spend, provider preference, or public claim |
| Agent type | Claude Code (GC-018 + work order author role) |
| Invocation ID | p4b-b-t0-doc-only-gc018-2026-06-15 |
| Expected manifest | docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_2026-06-15.md; docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_FOR_CODEX_2026-06-15.md |
| Actual changed set | docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_2026-06-15.md; docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_B_CONCRETE_PROVIDER_LIVE_PROOF_FOR_CODEX_2026-06-15.md |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes only P4B-B-T0 doc-only work. It does not authorize
live provider calls, credential reads, network use, provider preference,
provider addition, EPF wiring, Strategy Layer, AI Gateway absorption, public
sync, production readiness, public readiness, or raw memory release.
