# CVF CSCC-R1-T2A Route Selection And Alibaba Provider Parity Assessment

Memory class: governed-source-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: CSCC-R1-T2A

Date: 2026-09-03

executionBaseHead: `008dfa8a0`

reworkGeneration: 1

## Purpose

Resolve the route-build exclusivity and provider-parity conflict that blocked
CSCC-R1-T2, using Alibaba as the first bounded candidate because its current
Web execution path and Gateway destination/capability owners already exist.
Evaluate all three route-selection options named by the governing work order,
compare Alibaba's current Web behavior against the Gateway generic adapter
field by field, select exactly one posture, and name the exact successor
manifest (or the exact blocking gap) without implementing anything.

**Reviewer Rework R1 note.** The prior pass selected
`READY_FOR_T2B_ALIBABA_CANONICAL_BUILD_IMPLEMENTATION` while the successor
manifest still contained open design choices dressed as a closed decision
(an "or a new co-located module, reviewer's choice" credential edit; an
unnamed second Web composition file; and an unspecified build-artifact/
build-flag/feature-branch packaging mechanism left for T2B to invent). This
rework re-derives every one of those choices directly from current source. It
closes four of them exactly and finds one (the route-build packaging
mechanism itself) cannot be closed from current source without inventing a
mechanism this repository does not have. Per the rework mandate, an
unresolved design choice means the terminal token must be downgraded rather
than papered over with confident prose; see Selected Posture And Reasoning
and Terminal Token below.

## Source / Predecessor Evidence

- `docs/reviews/CVF_CSCC_R1_T2_CANONICAL_WEB_GATEWAY_COMPOSITION_COMPLETION_2026-09-03.md`
  (T2 closed `CLOSED_BLOCKED_BOUNDED`, material `2ffe5a803`): the dormant
  `CanonicalExecutionPort`/`CanonicalExecutionAdapter` foundation is accepted,
  but `/api/execute` still calls `executeAI` directly for both initial and
  retry attempts, and the T1 contract permits only one composition-root choice
  per route build, not a provider-by-provider cutover.
- `docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md`
  (frozen T1 contract): names `CanonicalExecutionPort`, its request/result
  shapes, the additive `beforeProviderInvoke` bridge option, and the exclusive
  adapter-selection rule.
- `docs/reference/CVF_CANONICAL_EXECUTION_IDENTITY_AND_RECEIPT_JOIN_CONTRACT_2026-09-03.md`
  (frozen T1 identity contract): names `canonicalExecutionId` as the single
  join field across `GatewayReceipt`, `MaterialContextManifest`,
  `Sot3ActivationEvidenceRecord`, and `GovernanceEvidenceReceipt`.
- `docs/assessments/CVF_CSCC_R1_T0A_CANONICAL_EXECUTION_OWNERSHIP_AND_INTERFACE_RESOLUTION_2026-09-02.md`
  (frozen T0A assessment): Seam 3 and Required Decision Question 7 settle
  team-quota-versus-Gateway-quota coexistence, used directly in this rework's
  Correction 4 below.
- `docs/baselines/CVF_GC018_CSCC_R1_T2A_ROUTE_SELECTION_AND_ALIBABA_PROVIDER_PARITY_RECONCILIATION_2026-09-03.md`
  and the paired work order authorize this exact two-path source-only
  reconciliation and reserve one future Alibaba live call.

## Decision / Baseline / Proposed Tranche

Selected posture: **Alibaba-only canonical build remains the correct target
shape at the composition/credential/quota level, and this rework closes those
three ownership questions exactly. It does not select `STOP_NO_SAFE_CANONICAL_CUTOVER`
because those questions are unbuildable; it selects `STOP_NO_SAFE_CANONICAL_CUTOVER`
because the route-build exclusivity mechanism itself (Correction 3) cannot be
proved from current source** -- no build-artifact, build-flag, or
feature-branch packaging mechanism that could make the direct path's code
"not reachable in the accepted build" exists anywhere in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` today (verified by direct search;
see Correction 3 below). Keeping a READY token while leaving that mechanism
unnamed would be exactly the defect this rework exists to catch. See Selected
Posture And Reasoning and Terminal Token.

## Required Decision Matrix

### Option 1: Route-wide full parity

**Required treatment:** name every provider protocol adapter/config owner
required before one build-wide port flip.

Current Web route (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`,
line 271, `apiKeyMap`) supports six providers: `openai`, `claude`, `gemini`,
`alibaba`, `openrouter`, `deepseek`. Gateway-owned `ProviderExecutionAdapter`
implementations (the exact interface `ProviderExecutionBridge` expects,
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` lines 43-46:
`{ providerId: string; execute(input): Promise<{text, usage?}> }`) exist today
only as:

- `createOpenAiCompatibleExecuteAdapter` /
  `createCredentialBoundOpenAiCompatibleExecuteAdapter`
  (`EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`,
  lines 42-123): a generic factory, parameterized by `providerId`, `modelId`,
  `endpoint`, and a resolved secret. It is not itself bound to any provider
  until a caller supplies those parameters.
- LPCI's separate `openai`/`gpt-4o` production binding
  (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts`,
  confirmed by direct read this rework: `resolveLpciProviderBindingConfig`
  lines 66-101, `executeLpciProviderBinding` lines 103-176, `buildBridge`
  lines 178-210): constructs its own local `ProviderRegistry`,
  `ProviderHealthMonitor`, `QuotaLedger`, and `CredentialReference` per call,
  under its own credential/configuration contract, distinct from
  `/api/execute`'s `apiKeyMap` model.

No Gateway-owned adapter instance exists today for `claude`, `gemini`,
`alibaba`, `openrouter`, or `deepseek`. A route-wide flip would require, at
minimum: one `ProviderExecutionAdapter` construction per provider (five new
instances plus reconciling the existing LPCI `openai` binding with
`/api/execute`'s own `apiKeyMap`/`resolveAlibabaApiKey`-style resolution
model), one `CredentialReference`/`envNames` entry per provider constructed at
each call site (`EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts`,
verified this rework to have no static registry -- see Correction 5), one
`ProviderRegistry` entry per provider
(`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`), capability-registry
coverage matching each provider's real request/response shape (the generic
adapter's `stream: false`-only, no-`enable_thinking` request body would silently
misrepresent every non-Alibaba-compatible or Alibaba-specialized provider
behavior), and route-level `ProviderHealthMonitor`/`QuotaLedger` wiring for
all six. This is the T2 completion review's original blocker restated: full
parity is not proved for five of six providers and is out of scope for one
bounded tranche.

**Disposition: not selected.** Too large for one bounded successor; the
per-provider adapter/config work is not named anywhere in current source.

### Option 2: Alibaba-only canonical build

**Required treatment:** require non-Alibaba requests to fail closed in that
build and keep a separate direct rollback build; prove this satisfies T1
without mixed active paths.

The frozen T1 Compatibility / Rollback Matrix
(`docs/reference/CVF_CANONICAL_EXECUTION_PORT_INTERFACE_CONTRACT_2026-09-03.md`,
"Exclusive adapter selection" row) states, verbatim: "Web owns exactly one
composition-root choice per route build: either the current direct `executeAI`
plus `admitAndInvokeProvider` path, or the canonical port-backed Gateway
adapter. Both are never wired active on the same route build (T0A seam 4
rollback rule)." The unit of exclusivity named here is **the route build**,
singular. A genuinely separate Alibaba-only build (its own composition-root
wiring, with every non-Alibaba `routedProvider` value failing closed before
reaching either `executeAI` or the canonical port) would be a distinct route
build from the existing direct build that continues to serve all six
providers unchanged, and under that textual reading would not violate "both
are never wired active on the same route build."

**This rework finds that reading cannot be exercised safely from current
source**, because "distinct route build" requires an actual build-time or
deploy-time mechanism that keeps the direct path's code out of the accepted
Alibaba build, and no such mechanism exists anywhere in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` today. See Correction 3 below for
the exact negative-search evidence and why this blocks the READY token.

**Disposition: correct target shape at the composition/credential/quota
level (see Corrections 2, 4, 5), but not provably safe to build under T1's
exclusivity rule with current source's packaging mechanisms (see
Correction 3).**

### Option 3: Mixed provider transition

**Required treatment:** treat as a T1 contract amendment; name the exact
invariant preventing duplicate/bypass paths and the amendment manifest.

A mixed transition (e.g., Alibaba and one other provider routed through the
canonical port while the remaining four stay on the direct path, all within
one deployed route build) would require the exclusivity rule itself to change
from "one path per route build" to "one path per provider per route build."
That is a T1 text amendment, not an implementation choice: the current
contract's rollback matrix names no provider-scoped exception, and the Future
T2 Deterministic Test-Name Manifest's risk class 8
("`exactly one of the direct executeAI adapter or the canonical port adapter
is wired per route build`") is written at route-build granularity. The
amendment would need to name the exact invariant that prevents a single
request from being dual-routed or silently bypassed when its provider is
ambiguous between the two paths, and the amendment manifest would itself
require a fresh T1B contract tranche with its own independent review before
any implementation.

**Disposition: not selected.** No current evidence justifies opening a T1
amendment before Option 2's packaging gap (Correction 3) is even closed;
escalating to a contract change first would be premature, and would not by
itself solve the packaging-mechanism gap either (a mixed-path build has the
identical "how is this actually packaged/deployed" question as an
Alibaba-only build).

## Required Source Matrix (Alibaba-Specific, Field-Level)

| Concern | Current owner | Gap |
| --- | --- | --- |
| Endpoint / destination classification | Web: hardcoded literal `https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions` inside `executeAlibaba` (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`, line 280). Gateway: `GATEWAY_DERIVED_ENDPOINTS` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/adapter-destination-policy.ts`, lines 26-29) maps `ALIBABA_DASHSCOPE_INTL_ENDPOINT`/`ALIBABA_DASHSCOPE_MAINLAND_ENDPOINT` (from `alibaba-free-quota-model-ledger.ts`) to provider id `"alibaba"` for destination classification only. | The Gateway destination policy already recognizes the same intl endpoint host that Web hardcodes, so the destination side is aligned. No gap for classification itself; the gap is that no adapter yet calls through this classification for a real Alibaba `execute`. |
| API-key alias resolution vs Gateway `CredentialReference` | **Closed exactly this rework (Correction 5).** Web: `resolveAlibabaApiKey` (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts`, lines 1-19, exported as `ALIBABA_API_KEY_ENV_NAMES`) checks four ordered env names, in this exact order: `ALIBABA_API_KEY`, `DASHSCOPE_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`, `CVF_ALIBABA_API_KEY`, and returns the first non-empty trimmed value. Gateway: `CredentialReference` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts`, lines 3-7) is a plain data interface `{ providerId, keyId, envNames: string[] }` with **no static registry anywhere in the file** -- `CredentialBoundary` (lines 18-41) is a class instantiated per call site and its `resolveSecret`/`resolveMetadata` methods accept a `CredentialReference` value as an argument; nothing in `credential-boundary.ts` stores or looks up a provider-to-reference mapping. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` (lines 112-120) confirms the actual pattern in use today: the Web-side caller constructs `new CredentialBoundary(env)` and a local `const credentialReference: CredentialReference = { providerId, keyId, envNames }` object at its own call site, then passes both into its own bridge-construction helper. | **No gap remains for the pattern itself.** The Web composition owner must construct the Alibaba `CredentialReference` locally, exactly as `provider-binding.ts` does for OpenAI, naming `envNames: ['ALIBABA_API_KEY', 'DASHSCOPE_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY', 'CVF_ALIBABA_API_KEY']` in that exact order. `credential-boundary.ts` itself is never edited. See Correction 5 for the exact owning module/function names. |
| Provider/model registry and capability method | `PROVIDER_CAPABILITY_REGISTRY` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`, lines 70-99) already lists `alibaba` with four named models (`qwen-flash`, `qwen-vl-plus`, `qwen3-32b`, `qwen3-235b-a22b-thinking-2507`) plus the free-quota ledger models, with method arrays including `complete`, `chat`, `stream`, `vision`, `reasoning`. | The registry records supported *methods* but carries no field anywhere for the Alibaba-specific `enable_thinking` request parameter, the `qvq-*` streaming-only model class, or per-model max-token/temperature defaults. A conformant adapter built against this registry alone would not know to send `enable_thinking` or to force `stream: true` for `qvq-*` models; that behavior currently lives only in Web's `executeAlibaba` (`isQwen3Model`, `isQwen3ThinkingModel`, `isAlibabaStreamingOnlyModel`, `providers.ts` lines 14-24). |
| Routing / health / Gateway quota vs Web team quota | **Closed exactly this rework (Correction 4).** Gateway: `QuotaLedger.canUse` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts`, lines 52-77, confirmed by direct read this rework), a per-`providerId`/`modelId` request/token counter, structurally independent of any team or billing concept -- it has no `teamId` field anywhere in `QuotaRequest`/`QuotaUsage`/`QuotaDecision`. Web: `checkTeamQuota(session?.teamId)` (`route.ts` line 346) is a per-team USD budget check. `docs/assessments/CVF_CSCC_R1_T0A_CANONICAL_EXECUTION_OWNERSHIP_AND_INTERFACE_RESOLUTION_2026-09-02.md`, Seam 3 (lines 171-181) and Required Decision Question 7 (lines 237-238), settles this exactly, verbatim: "They answer different questions and coexist as two sequential, non-overlapping gates: `checkTeamQuota` (Web, USD/billing-window, per team) runs first and is unaffected by port composition ... `QuotaLedger.canUse` (Gateway, token/`estimatedTokens`, per provider/model) runs later, inside the port call ... as established in seam 3. Neither is asked to answer the other's question, so there is no duplicate semantic, only two distinct caps applied in sequence." | **No gap remains.** Gateway `QuotaLedger` is additive, not a replacement: for an Alibaba canonical-build request, `checkTeamQuota` remains the upstream team/USD gate, checked before the port call in its current unchanged position (`route.ts` line 346, upstream of `assertNonVisionExecutionPathIsDirect()`/`admitAndInvokeProvider` at line 802); `QuotaLedger.canUse` then runs as one of `ProviderExecutionBridge.execute`'s own pre-adapter stops (Pre-Adapter Stop Table, T1 contract, "Quota exceeded" row, `errorClass: quota_exceeded`), strictly inside the port call, after team quota has already passed. Both gates must independently pass for an Alibaba request to reach the adapter; either can independently deny. See Correction 4 for the exact deterministic test naming this. |
| Concrete `ProviderExecutionAdapter` compatibility | `ProviderExecutionAdapter` interface (`provider-execution-bridge.ts`, lines 43-46): `{ readonly providerId: string; execute(input: ProviderExecutionAdapterInput): Promise<ProviderExecutionAdapterResult> }`, where `ProviderExecutionAdapterResult` is `{ text: string; usage?: { inputTokens, outputTokens } }`. The existing Alibaba-named module, `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts`, exports `createAlibabaQwenTurboStreamAdapter`, which returns `{ async *stream(request: StreamRequest): AsyncIterable<StreamContract> }` (lines 29-74). | **Verified structurally non-conformant, not merely non-conformant by convention.** The stream-adapter object has no `providerId` field at all and no `execute` method; it has a generator method named `stream` with a completely different signature and return shape (`AsyncIterable<StreamContract>` chunks, not a single `Promise<{text, usage?}>`). `evaluateProviderAdapterConformance`'s Rule 1 (`provider-adapter-conformance.ts`, lines 63-68) checks `adapter.providerId !== providerId`; the stream-adapter object would fail this check by having `adapter.providerId === undefined`, confirming the T2 rework's general finding ("provider-specific adapter-named modules are not automatically bridge-conformant") applies concretely to Alibaba. No `ProviderExecutionAdapter`-conformant Alibaba implementation exists anywhere in `EXTENSIONS/CVF_MODEL_GATEWAY/src` today. |
| Canonical attempt boundary and exactly-once accounting | Frozen by T1 (`CanonicalExecutionAttemptBoundary`, `attemptBoundary` field, mandatory on `CanonicalExecutionPortRequest`) and implemented, dormant, by T2's `CanonicalExecutionAdapter` (`EXTENSIONS/CVF_MODEL_GATEWAY/src/canonical-execution-port.ts`, lines 84-134) and `ProviderExecutionBridge.execute`'s callback invocation (`provider-execution-bridge.ts`, lines 142-237, confirmed by direct read this rework of the routing/adapter-lookup sequence). This machinery is provider-neutral; it does not need Alibaba-specific work once a conformant Alibaba `ProviderExecutionAdapter` exists and is registered in the bridge's `adapters: Map<string, ProviderExecutionAdapter>`. | No gap in the boundary/accounting mechanism itself; the gap is purely the missing adapter registration (see row above) that would let this mechanism ever reach an Alibaba `adapter.execute` call. |
| Initial/retry response mapping and output validation | Web: `executeAlibaba` builds `ExecutionResponse` with provider-specific usage mapping that differs by branch  -  streaming-only models (line 322-335) map `data.tokensUsed` only into `usage.totalTokens` (no input/output split), while non-streaming models (line 337-350) map `data.usage.prompt_tokens`/`completion_tokens`/`total_tokens` into `usage.inputTokens`/`outputTokens`/`totalTokens`. Gateway: `createOpenAiCompatibleExecuteAdapter`'s `readUsage` (`openai-compatible-execute-adapter.ts`, lines 137-155) always expects a single flat `usage` object as `{prompt_tokens, completion_tokens}` or `{input_tokens, output_tokens}`, with no streaming-response SSE-parsing path at all (`stream: false` is hardcoded at line 84). | The generic adapter cannot produce a correct result for any `qvq-*` streaming-only Alibaba model, because it never sets `stream: true` and has no SSE parser; it would receive a non-streaming-shaped response from an endpoint that (per Web's own comment, `providers.ts` line 313-317) actively rejects certain models on the non-streaming path with `model_not_supported`. For non-streaming Qwen models the two usage shapes are compatible, but the `enable_thinking` field is never sent by the generic adapter, so a `qwen3-*thinking` model would run in default (non-thinking) mode through Gateway while running in thinking mode through the current Web direct path  -  a real behavioral divergence, not just a missing convenience field. |
| Receipt / manifest / canonical-ID correlation | Frozen and implemented by T1/T2 (`canonicalExecutionId` propagation through `GatewayReceipt`, `MaterialContextManifest`; see identity contract). Provider-neutral. | No Alibaba-specific gap; this layer is ready once an adapter exists. |
| Rollback build behavior | Current route (`route.ts` line 802, `assertNonVisionExecutionPathIsDirect()`, called before both the initial call at line 805 and the retry call at line 863) already hard-asserts the direct `executeAI` path for every non-vision request, for every provider including Alibaba. This *is* today's de facto "direct rollback build": there is only one deployed build right now, and it is 100% direct. `NON_VISION_EXECUTION_PATH_SELECTION` and `assertNonVisionExecutionPathIsDirect()` are already implemented and owned by `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.ts` (lines 42-58, confirmed by direct read this rework), which is the file this rework's Correction 2 requires the Alibaba composition to extend. | **Not closed -- this is the blocking gap named in Correction 3.** `NON_VISION_EXECUTION_PATH_SELECTION` is a runtime-checked source constant that governs which branch of already-compiled code executes; it is not a build-artifact/build-flag/feature-branch mechanism that removes the other branch's code from an accepted build. No such build-exclusion mechanism exists anywhere in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` (confirmed by direct search this rework for `next.config`/`BUILD_VARIANT`/`FEATURE_FLAG`/build-time env-gated route variants: zero matches). Building the Alibaba-only canonical variant under the work order's exact required shape (code "actually not reachable in the accepted build") therefore has no current-source mechanism to implement it with. |
| Deterministic zero-call rejection plus one future live positive proof | Not yet designed in source; named in the Successor Implementation Manifest below, gated on Correction 3's resolution. | See manifest. |

**Field-by-field comparison note on the "OpenAI-compatible" label.** The
generic Gateway adapter's own file comment and the T2A Source Verification
Block both describe Alibaba's endpoint as "OpenAI-compatible." The comparison
above shows this label is true only for the request/response *envelope shape*
(chat-completions-style `messages`/`choices` JSON) of the non-streaming,
non-thinking case. It is false for: streaming-only models (`isStreamingOnlyModel`,
forced `stream: true` plus SSE parsing, entirely absent from the generic
adapter); `enable_thinking` (Alibaba/Qwen-specific, absent from the generic
adapter and from the capability registry's metadata); timeout (Web sets an
explicit `AbortSignal.timeout(resolveProviderTimeoutMs())` and a `Connection:
close` header per a documented W133 keep-alive defect; the generic adapter
sets no default timeout and passes through only a caller-supplied `signal`);
error classification (Web wraps non-OK responses in `ProviderHttpStatusError`
carrying the real HTTP status and gives a specialized message for
`model_not_supported` on streaming-only models; the generic adapter throws a
single generic `Error("OpenAI-compatible provider request failed")` with no
status code preserved); and usage mapping (two different shapes by branch, as
above, versus the generic adapter's one flat shape). This assessment does not
assume compatibility from the "OpenAI-compatible" name; every claim above is
sourced to an exact line range on both sides.

## The 11 Mandatory Corrections (Rework R1)

### Correction 1: eliminate every still-open choice

Applied throughout this document and the paired worker return. Every
occurrence of "or a new co-located module," "reviewer's choice," or an
unnamed packaging mechanism from the prior pass has been replaced below with
either a single exact answer (Corrections 2, 4, 5, 6) or an explicit,
honestly-flagged gap that changes the terminal token (Correction 3) rather
than papered over with prose.

### Correction 2: exactly one Web composition owner

**Closed exactly.** The Web composition owner remains exactly
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.ts`.
This rework read the file directly: it already exports
`NON_VISION_EXECUTION_PATH_SELECTION`, `assertNonVisionExecutionPathIsDirect`,
`CanonicalWebGatewayExecutor`, and `createCanonicalWebGatewayExecutor(bridge:
ProviderExecutionBridge)` (lines 26-149) -- a generic factory that already
accepts any caller-constructed `ProviderExecutionBridge`, not one hardcoded to
a specific provider set. No new file
(`canonical-web-alibaba-composition.ts` or any similarly named module) is
created. The successor manifest below adds, inside this same existing file,
one new exported factory function
(`buildAlibabaOnlyCanonicalBridge`, see manifest) that constructs an
Alibaba-scoped `ProviderExecutionBridge` (one adapter entry, one credential
reference, one registry entry) and reuses the file's existing
`createCanonicalWebGatewayExecutor` unchanged, plus one new exported guard
function (`assertRoutedProviderIsAlibabaOrRejectClosed`, see manifest) that
performs the fail-closed check named in Correction 3's provable half. This
extension does not violate any existing size/responsibility boundary the file
declares in its own header comment (it already documents itself as "the ONLY
module in `cvf-web` that constructs a `CanonicalExecutionPortRequest`"); an
Alibaba-scoped bridge-construction helper is additive composition-root code
of the same kind the file already contains for the generic case, not a second
responsibility class.

### Correction 3: close the route-build selection mechanism exactly

**Not closed. This is the reason the terminal token is downgraded.**
Evaluating the required shape point by point against current source:

- *Same `/api/execute` canonical ingress, not a second route entrypoint*:
  provable. Nothing in the work order or current source requires a second
  Next.js route file; the existing `route.ts` call sites
  (`assertNonVisionExecutionPathIsDirect()` at lines 802 and 863) are the
  correct edit points for a future implementation.
- *Hardcoded composition constant flipped from `'direct'` to `'port'` in the
  accepted implementation commit itself*: provable and already exactly
  mechanized. `NON_VISION_EXECUTION_PATH_SELECTION: 'direct' | 'port' = 'direct'`
  and `assertNonVisionExecutionPathIsDirect()` already exist in
  `canonical-web-gateway-execution.ts` lines 51-58 for exactly this purpose;
  flipping the literal and updating the assertion (or adding a parallel
  `assertRoutedProviderExecutionPathForAlibabaBuild()`) in one reviewed commit
  is a literal single-line-class change, git-diffable, not a runtime switch.
- *Non-Alibaba requests fail closed before any provider invocation*: provable
  and exactly nameable. The guard belongs inside the composition owner
  (`canonical-web-gateway-execution.ts`) as a new function,
  `assertRoutedProviderIsAlibabaOrRejectClosed(routedProvider: AIProvider):
  void` (or an equivalent typed-rejection-returning variant), called at the
  route's existing call sites before `admitAndInvokeProvider`/the port call,
  inspecting `routedProvider` and returning/throwing a typed rejection for any
  value other than `'alibaba'` strictly before either `executeAI` or
  `CanonicalWebGatewayExecutor.execute` is reached. This is provable because
  it requires no new mechanism -- it is an ordinary guard clause of the same
  shape as the file's existing `assertNonVisionExecutionPathIsDirect()`.
- *Rollback as a single-line constant revert, git-diffable, not a runtime
  switch*: provable for the constant itself (same reasoning as above), but
  **this rollback claim's precondition is that the constant genuinely governs
  which code is active in a given deployed build**. It does today for a
  single build (today's one deployed build is 100% direct, per the Rollback
  Build Behavior matrix row above) -- but the work order requires a *second*,
  separately built/deployed Alibaba-only build to exist *simultaneously
  available for deployment-time selection* alongside the direct build,
  specifically so that the direct path's code is "actually not reachable in
  the accepted [Alibaba] build," not merely inert behind a runtime `if`.
- **The unprovable element: a build-artifact, build-flag, or feature-branch
  mechanism that produces two independently deployable builds from one
  source tree, one of which excludes the direct path's code.** This rework
  searched `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` directly (glob over
  `*.ts`, `*.js`, `*.json`, `*.mjs` for `next.config`, `BUILD_VARIANT`,
  `FEATURE_FLAG`, `process.env.BUILD`, `deploy.*variant`, `route-variant`) and
  found **zero matches**. No Next.js multi-build configuration, no CI
  feature-branch deploy split, no build-time environment-gated route
  variant, and no separate deployment-artifact pipeline exists anywhere in
  the Web package today. The existing `NON_VISION_EXECUTION_PATH_SELECTION`
  constant governs a runtime branch inside one compiled build; it does not,
  and by itself cannot, remove the other branch's code from that build's
  bundle. Naming "a future implementer will create a build flag" would be
  exactly the kind of unresolved design choice this rework is required to
  refuse to paper over.

**Conclusion on Correction 3: the exact shape required by the work order is
not provable from current source.** T1's "one composition-root choice per
route build" text is satisfiable today only by the weaker reading already
implemented (`NON_VISION_EXECUTION_PATH_SELECTION` as a single runtime-checked
constant governing one deployed build's behavior) -- which is what today's
single direct build already is. A genuinely separate Alibaba-only *build* in
the strong sense the work order requires cannot be asserted ready without
inventing a packaging mechanism this repository does not have. This finding
is the direct cause of the terminal token downgrade below.

### Correction 4: close quota ownership exactly

**Closed exactly.** `checkTeamQuota` remains the upstream team/USD gate for
Alibaba canonical-build requests, checked before the port call, in its
current unchanged position (`route.ts` line 346). Gateway's `QuotaLedger` is
**additive**, not a replacement: it is a second, independent
per-provider/model token gate that runs in addition to team quota, strictly
inside `ProviderExecutionBridge.execute` as one of its own pre-adapter stops,
after team quota has already passed upstream in Web. Both must pass; either
can independently deny. This is settled by the frozen T0A assessment, Seam 3
and Required Decision Question 7 (quoted verbatim in the Required Source
Matrix row above), not invented by this rework. One deterministic test that
would prove the two gates coexist correctly: construct a synthetic `teamId`
whose `checkTeamQuota` usage is one cent under its USD cap and a synthetic
Alibaba `providerId`/`modelId` pair whose `QuotaLedger` usage is one estimated
token under its configured `estimatedTokensPerDay` limit; assert a request
that would push team USD over cap is denied by `checkTeamQuota` before the
port is ever called (zero `QuotaLedger.canUse` invocations), and separately
assert a request within team budget but whose `estimatedTokens` would push
the Gateway token ledger over its cap is denied by `QuotaLedger.canUse`
(`errorClass: quota_exceeded`) after team quota already passed, in both cases
with zero adapter calls.

### Correction 5: close credential ownership exactly

**Closed exactly.** `credential-boundary.ts` was read directly this rework
(reproduced in full in the Required Source Matrix row above): it declares
only the `CredentialReference` interface, the `CredentialMetadata` interface,
and the `CredentialBoundary` class with `resolveMetadata`/
`resolveSecretForRuntime`/private `resolveSecret` methods. **There is no
static registry mechanism in this file.** `CredentialBoundary` is
instantiated per call site (confirmed by `provider-binding.ts` lines 112-120,
the LPCI pattern: `new CredentialBoundary(env)` plus a locally constructed
`CredentialReference` object, both built inside the caller's own function,
never inside `credential-boundary.ts`). Therefore:

- `credential-boundary.ts` is **never edited** by the successor tranche.
- The exact module/function that constructs the Alibaba `CredentialReference`
  is a new function inside the Web composition owner,
  `canonical-web-gateway-execution.ts` (Correction 2's single owner):
  `buildAlibabaCredentialReference(): CredentialReference`, returning
  `{ providerId: 'alibaba', keyId: 'alibaba-canonical', envNames:
  ['ALIBABA_API_KEY', 'DASHSCOPE_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY',
  'CVF_ALIBABA_API_KEY'] }` -- this exact four-name, exact-order list is read
  directly from `alibaba-env.ts`'s `ALIBABA_API_KEY_ENV_NAMES` export (lines
  1-6), not re-derived or reordered.
- The exact module/factory that resolves the secret for the Alibaba adapter
  at call time is `CredentialBoundary.resolveMetadata`
  (`credential-boundary.ts` lines 21-31), called from inside
  `ProviderExecutionBridge.execute` (`provider-execution-bridge.ts` line 132,
  confirmed by direct read this rework of the pre-adapter sequence),
  returning only non-secret `CredentialMetadata` (`providerId`, `keyId`,
  `available`, `source`, `fingerprint`, `redactedValue`) -- never the raw
  secret. The raw secret value flows only from `resolveAlibabaApiKey`-
  equivalent env lookup (performed internally by `CredentialBoundary`'s
  private `resolveSecret`, lines 37-41) into
  `CredentialBoundary.resolveSecretForRuntime`, which the new
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/execution-adapter.ts`
  adapter (named in the Successor Implementation Manifest) calls directly at
  the point it makes its HTTP request -- never through the bridge, receipt,
  or manifest layer, consistent with the `credentialShielded: true` invariant
  already asserted on every Gateway error envelope
  (`provider-execution-bridge.ts` lines 258, 279, 315, 343, confirmed present
  by the frozen T0A assessment's Question 8).
- Raw secret values are kept out of receipts, errors, and logs by
  `CredentialMetadata` (`credential-boundary.ts` lines 9-16): it carries only
  `fingerprint`/`redactedValue` (both derived through `fingerprintSecret`/
  `redactSecret`, lines 44-53, which hash or truncate the secret, never pass
  it through), never the raw value itself. The new Alibaba execution adapter's
  own error-mapping path must not interpolate a caught HTTP-error's message
  body into any thrown error, receipt `reason`, or log line without first
  confirming that body cannot echo the `Authorization` header value (Alibaba's
  DashScope endpoint does not echo request headers in error bodies per Web's
  existing `executeAlibaba` error handling, but the new adapter must apply the
  same non-interpolation discipline `sanitizeReceiptMetadata`
  (`gateway-receipt.ts` lines 128-140, confirmed present by direct read this
  rework) already applies to receipt metadata).

### Correction 6: separate rollback tests, never "or"

**Closed exactly.** The successor manifest's Test Manifest section below
lists two distinct, both-required test suites with no "or" between them:
**Direct rollback build tests** (proving a revert of the composition constant
restores exact current `executeAI`-based behavior for all six providers,
byte-identical, unchanged) and **Alibaba canonical build tests** (proving
non-Alibaba requests fail closed via the named rejection path with zero
adapter/provider calls, AND that Alibaba requests succeed through the port
with exactly-once admission/call-start per T1's frozen invariants). These are
recorded as separate numbered items in the Test Manifest, each with its own
proof obligation; neither substitutes for the other.

### Correction 7: Semantic Convergence Outcome corrected to SUCCESSOR

Applied in the paired worker return's Semantic Convergence Outcome block:
`chainMode: SUCCESSOR`, `chainOrdinal: 1`, `predecessor.path` and
`predecessor.sha256` set to the exact values supplied by the rework
instruction, `blockerDelta.prior` set to the predecessor's own `current` set
verbatim, `blockerDelta.resolved: []`, `resolutionEvidence: {}`, and
`retained`/`new`/`current` reflecting the genuinely still-open state after
this rework (see that block for the exact reconciliation).

### Correction 8: fix the live-run diagnostic reference

**Closed as a named finding, not silently fixed (out of write scope).** This
rework verified file existence directly before citing anything: the real
file exists at `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
(confirmed present on disk this rework). The non-`archive/` path
`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` does **not**
exist on disk (confirmed absent this rework) and is **not** cited as
`FULL_READ` anywhere in this document or the paired worker return.

**Named finding:** `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`,
line 85, its "Mandatory Live Run Diagnostics" row, still points to the
non-`archive/` path (`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`),
which does not exist at that location. This is stale documentation-path drift
in the canonical routing/carrier index. The routing index is not one of this
tranche's two owned files (`docs/assessments/` and `docs/reviews/` only), so
this rework does not and cannot repair it directly. A successor or closer
must repair that routing-index reference before any live rerun that depends
on a reader resolving the live-run diagnostic standard through the routing
index is attempted.

### Correction 9: worker-return scalars

Applied in the paired worker return: `reworkGeneration: 1`;
`consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES`;
`providerCallCount: 0`; `successorTrancheOpened: NO`.

### Correction 10: terminal token decision

See Selected Posture And Reasoning and Terminal Token below. The token is
**downgraded to `STOP_NO_SAFE_CANONICAL_CUTOVER`** because Correction 3
cannot be closed with an exact citation to an existing mechanism; every other
correction (2, 4, 5, 6) closes exactly, but the rework instructions are
explicit that any one open gap in build/composition/rollback ownership
requires the downgrade, not a partial READY token.

### Correction 11: gates rerun after edits

See Command Evidence in the paired worker return.

## Selected Posture And Reasoning

**Composition, credential, and quota ownership (Corrections 2, 4, 5) are
fully closed** with exact source citations, as detailed above: exactly one
Web composition owner file, exactly one credential-construction pattern
(per-call-site, matching the existing LPCI precedent), and exactly one quota
coexistence model (additive, sequential, already settled by frozen T0A text).
None of these three requires a T1 amendment or leaves any option list; each
has a single concrete answer.

**The route-build packaging mechanism (Correction 3) is not closed**, and
this is the deciding factor for the terminal token. T1's frozen text ("Web
owns exactly one composition-root choice per route build ... Both are never
wired active on the same route build") is satisfiable today only in the weak
sense already implemented: one runtime-checked constant governing one
deployed build's active path. The work order's required strong sense --
two independently deployable builds, one of which has the direct path's code
"actually not reachable," selected at deploy time -- has no implementing
mechanism anywhere in current source. Asserting this is buildable without
naming that mechanism would be exactly the "reviewer's choice" /
option-list defect this rework exists to eliminate. Per the rework mandate
("if you cannot prove this exact shape ... you must NOT keep the READY token
-- downgrade to `STOP_NO_SAFE_CANONICAL_CUTOVER`"), this assessment downgrades
the terminal token.

This is not a rejection of Alibaba as the correct first bounded candidate --
the field matrix and Corrections 2/4/5 show the composition-level work is
well-scoped and mostly already exists (the composition owner file, the
credential-construction pattern, and the quota-coexistence rule are all
already established elsewhere in source). It is specifically a finding that
the *route-build exclusivity mechanism* T1 requires has no current-source
implementation, and inventing one is out of this tranche's scope (it would
itself be a new design decision requiring independent review, most likely a
CI/deployment-configuration decision rather than a `cvf-web` source-code
decision).

## Successor Implementation / Test / Live-Proof Manifest

**This manifest is recorded for successor traceability only. It is not an
authorization to proceed to T2B.** Per the Terminal Token below, a successor
must first resolve Correction 3 (name and get independently reviewed an
actual build/deployment mechanism that satisfies T1's exclusivity rule) before
any of the following implementation work is authorized.

### Files to create

| File | Purpose |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/execution-adapter.ts` | New `ProviderExecutionAdapter`-conformant Alibaba adapter (`providerId: "alibaba"`, `execute(input): Promise<{text, usage?}>`), reusing `classifyAdapterDestination` for the endpoint, branching on `isAlibabaStreamingOnlyModel`/`isQwen3Model`/`isQwen3ThinkingModel`-equivalent model checks (ported from `providers.ts` lines 14-24), sending `enable_thinking` on the same condition Web uses today, mapping both streaming (SSE) and non-streaming response shapes into the single `{text, usage}` result shape, and calling `CredentialBoundary.resolveSecretForRuntime` directly at its own HTTP call site (never returning the raw secret to any caller). Does not reuse `providers/alibaba/stream-adapter.ts` as-is; that module's `stream` shape is kept only for its existing non-canonical caller, if any, and is not repurposed. |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/providers/alibaba/execution-adapter.test.ts` | Focused adapter tests (see Test Manifest below). |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.test.ts` (extended, not new) | Adds the Alibaba composition-owner tests (see Test Manifest below) to the existing test file for this owner. No new test file for a new composition module, matching Correction 2's single-owner rule. |

### Files to edit

| File | Exact edit |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/canonical-web-gateway-execution.ts` | Add exactly two new exported functions to this existing file: (1) `buildAlibabaCredentialReference(): CredentialReference`, returning `{ providerId: 'alibaba', keyId: 'alibaba-canonical', envNames: ['ALIBABA_API_KEY', 'DASHSCOPE_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY', 'CVF_ALIBABA_API_KEY'] }`; (2) `assertRoutedProviderIsAlibabaOrRejectClosed(routedProvider: string): void`, throwing/returning a typed rejection for any `routedProvider !== 'alibaba'`, called before either `executeAI` or the port is reached. No new file is created for either function (Correction 2). This edit is recorded here for successor traceability; it is not authorized until Correction 3 is independently resolved. |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | **Blocked on Correction 3.** The exact edit cannot be specified without first naming the build/deployment mechanism that makes this a genuinely separate route build from today's direct build; specifying an edit to this file today would silently assume an unresolved design choice (exactly what Correction 1 forbids). No edit is named here. |

### Test manifest (deterministic, zero live calls unless noted)

**Direct rollback build tests** (proof obligation: reverting the composition
constant restores exact current `executeAI`-based behavior for all six
providers, unchanged):

1. **Rollback byte-identical behavior** -- a request routed through the
   existing, unmodified direct build (constant at `'direct'`) for each of the
   six providers (`openai`, `claude`, `gemini`, `alibaba`, `openrouter`,
   `deepseek`) asserts byte-identical behavior to today's `executeAI` path,
   confirming the rollback build is untouched by the Alibaba composition
   addition.

**Alibaba canonical build tests** (proof obligation: non-Alibaba requests
fail closed AND Alibaba requests succeed through the port with
exactly-once admission/call-start; both required, not alternatives):

1. **Deterministic rejection** -- a non-`'alibaba'` `routedProvider` value in
   the Alibaba-only build fails closed via
   `assertRoutedProviderIsAlibabaOrRejectClosed` before any admission or
   adapter call; assert zero `admittedCount`/`providerCallCount` change, a
   named typed rejection, and zero adapter/provider invocations.
2. **Initial call (mocked fetch)** -- a mocked non-streaming Qwen3 request
   asserts the adapter sends `enable_thinking` matching Web's current rule and
   maps usage identically to `executeAlibaba`'s non-streaming branch.
3. **Streaming-only model (mocked fetch)** -- a mocked `qvq-*` request asserts
   the adapter forces `stream: true`, parses SSE, and maps `usage.totalTokens`
   only (matching `executeAlibaba`'s streaming branch), never the flat
   `readUsage` shape.
4. **Quota coexistence (Correction 4)** -- a synthetic `teamId` near its USD
   cap and a synthetic Alibaba `providerId`/`modelId` near its
   `estimatedTokensPerDay` cap each independently deny a request before any
   adapter call, in two separate assertions (team-quota denial happens before
   the port is called at all; Gateway-quota denial happens inside the port
   call, after team quota already passed).
5. **Retry** -- a second port call with the same `canonicalExecutionId`
   asserts a fresh `attemptIndex` per the frozen T1 Retry row and no reuse of
   the first call's admission state.
6. **Lineage / identity correlation** -- one full canonical Alibaba execution
   asserts `GatewayReceipt.canonicalExecutionId`, `MaterialContextManifest.canonicalExecutionId`,
   and (when SOT3 activation occurred) `Sot3ActivationEvidenceRecord.canonicalExecutionId`
   are equal, per the frozen T1 identity contract's Cross-Document Agreement
   Check.
7. **Secret-safety** -- a test asserts the new adapter and the two new
   composition-owner functions never log, return, or embed the resolved
   secret value or `Authorization` header content in any error message,
   receipt, or manifest field, mirroring `sanitizeReceiptMetadata`'s existing
   redaction pattern and `CredentialMetadata`'s exclusion of the raw value.

### Bounded one-call live-proof plan (T2B, not this tranche, and gated on Correction 3)

After Correction 3 is independently resolved, every deterministic test above
passes, and the reviewer accepts the resulting T2B implementation: run
exactly one live call through the new canonical Alibaba composition using
`resolveAlibabaApiKey` (or the new Gateway `CredentialReference` resolving the
same env names) strictly by reference, never printing or logging the resolved
value; record provider id, model id, latency, `canonicalExecutionId`, and the
resulting `GatewayReceipt`'s non-secret fields (`keyId`, `fingerprint`,
`traceId`) as the proof artifact. On any failure, timeout, or ambiguous
result, stop immediately, record a secret-safe diagnostic per
`docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` (the
verified real path; see Correction 8), and require fresh reviewer
authorization before any repeat call. This consumes the operator's reserved
`authorizedFutureLiveInvocationCeiling: 1` grant from the T2A baseline; it is
not exercised by this tranche (`currentTrancheLiveInvocationCeiling: 0` is
honored throughout).

## Evidence / Verification

- Current-source symbol and owner recomputation: every claim in the Required
  Source Matrix above and in Corrections 2-6, 8 is cited to an exact file and
  line range read directly at `executionBaseHead` `008dfa8a0` during this
  rework, not carried forward from the prior pass without re-verification.
- Exact T1 selection-language comparison: the "Exclusive adapter selection"
  row of the frozen T1 port contract's Compatibility / Rollback Matrix is
  quoted verbatim in Option 2 and Selected Posture And Reasoning above.
- Exact T0A Seam-3/Question-7 citation for quota coexistence: quoted verbatim
  in Correction 4 and the Required Source Matrix's quota row.
- Negative-search evidence for Correction 3: a direct glob search over
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` (`*.ts`, `*.js`, `*.json`,
  `*.mjs`) for `next.config|BUILD_VARIANT|FEATURE_FLAG|process.env.BUILD|deploy.*variant|route-variant`
  returned zero matches, performed directly during this rework.
- File-existence verification for Correction 8: both the archive path and the
  non-archive path were checked for existence on disk directly during this
  rework before either was cited or flagged.
- Structural conformance verification: `evaluateProviderAdapterConformance`'s
  Rule 1 (`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-conformance.ts`,
  lines 63-68) was read directly to confirm the Alibaba stream-adapter's
  missing `providerId` field would fail conformance structurally, not only by
  naming convention.
- Pre-implementation governance gate:
  `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 008dfa8a0 --head HEAD`
  run after this rework's edits, with results recorded in the paired worker
  return's Command Evidence section.
- Exact two-path worker manifest, unchanged worker HEAD, and zero calls:
  verified via `git status --short --untracked-files=all` and
  `git rev-parse --short HEAD`, recorded in the paired worker return.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: bounded no-commit rework of an existing pending-review pair, not a
corpus rescan; every source claim is re-verified individually against current
source rather than compared against a corpus intake ledger.

## Claim Boundary

This assessment closes four of the prior pass's open design choices
(composition ownership, quota ownership, credential ownership, rollback test
separation) with exact source citations, and honestly identifies one
(route-build packaging mechanism) that current source cannot close. It does
not implement, edit, or test any runtime file, does not invoke any provider
or network call, does not read or print any credential value, does not amend
the frozen T1 contracts, and does not open T2B. The terminal token below is
the direct consequence of the one unclosed choice, not a partial or
conditional READY state.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-reconciliation assessment; no public-sync authority.
