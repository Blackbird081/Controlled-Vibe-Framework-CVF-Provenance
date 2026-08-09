# CVF LPCI-1 Web UC-01 Context-To-LLM Provider-Binding Design Audit

Memory class: FULL_RECORD

Status: INDEPENDENTLY_ACCEPTED_BOUNDED

Date: 2026-08-09

docType: audit

Batch ID: LPCI1-WEB-UC01-PROVIDER-BINDING-DESIGN

## Purpose

Define the complete DESIGN-only composition boundary that can replace the
current LPCI query route's local provider ownership with the existing Model
Gateway control plane in a later, separately authorized BUILD tranche. This
audit resolves UC-04 at design level only. It does not implement, execute, or
prove a provider binding.

## Target / Source

Target: the future provider-binding seam between the cvf-web LPCI query route
and the existing Model Gateway package.

Canonical dispatch sources:

- `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md`
- `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`
- `docs/baselines/CVF_GC018_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md`
- root visual contract `DESIGN.md`

Package-local source aliases used below avoid treating implementation files as
an external scan corpus:

- `cvf-web:` means a path relative to the existing cvf-web package root.
- `model-gateway:` means a path relative to the existing cvf-model-gateway
  package root.

## Scope / Methodology

The audit directly inspected the current LPCI route, the accepted S1
conformance contract, the Model Gateway capability registry, credential
boundary, execution bridge, routing contract, receipt contract, public export
surface, cvf-web package manifest, and safe example environment file. It then
compared three ownership/composition options against UC-04's AND rule:

1. reuse the existing current route-local direct-fetch behavior;
2. compose the route through the existing Model Gateway with a thin
   LPCI-specific projection/binding seam;
3. create a second LPCI-specific generic provider registry/gateway.

No source, runtime, test, config, manifest, provider, secret, or live execution
surface was changed or invoked. Secret-bearing local environment files were not
opened.

## Current Source Facts

| Fact ID | Classification | Source file | Verified symbol or section | Current fact |
| --- | --- | --- | --- | --- |
| CF-01 | CURRENT_SOURCE_FACT | cvf-web: `src/app/api/lpci/query/route.ts` | `POST` | The route reads `LPCI_LLM_API_KEY`, defaults `LPCI_LLM_ENDPOINT` and `LPCI_LLM_MODEL`, and performs provider `fetch` directly. |
| CF-02 | CURRENT_SOURCE_FACT | cvf-web: `src/app/api/lpci/query/route.ts` | provider request and result branches | Missing key returns `NO_PROVIDER_CONFIGURED`; provider failure returns a safe `PROVIDER_ERROR`; no Model Gateway package is called. |
| CF-03 | CURRENT_SOURCE_FACT | cvf-web: `package.json` | `dependencies` | The cvf-web package does not currently declare a Model Gateway package dependency. |
| CF-04 | CURRENT_SOURCE_FACT | cvf-web: `.env.example` | provider variables | The safe example documents generic provider keys and `DEFAULT_AI_PROVIDER`; it does not document the three-variable LPCI binding contract. |
| CF-05 | CURRENT_SOURCE_FACT | model-gateway: `src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | The existing owner declares provider/model capabilities, including OpenAI `gpt-4o`, DeepSeek `deepseek-chat`, and Alibaba Qwen models. It does not declare the route's current `gpt-4o-mini` default. |
| CF-06 | CURRENT_SOURCE_FACT_WITH_GAP | model-gateway: `src/credential-boundary.ts` | `CredentialReference`, `CredentialMetadata`, `CredentialBoundary.resolveMetadata`, private `resolveSecret` | Credential references and secret-safe metadata are separate from runtime secret resolution, but current `resolveSecret` selects the first `Boolean(value)` environment value. A whitespace-only value is therefore currently reported available; trim-empty rejection does not exist. |
| CF-07 | CURRENT_SOURCE_FACT | model-gateway: `src/provider-execution-bridge.ts` | `ProviderExecutionBridge.execute` | The bridge composes routing, credentials, health, quota, admission, adapters, and receipts; denied/no-candidate/credential/adapter branches fail without returning a successful response. |
| CF-08 | CURRENT_SOURCE_FACT | model-gateway: `src/unified-gateway-interface-contract.ts` | `GatewayExecuteRequest`, `GatewayExecuteResponse`, `GatewayErrorEnvelope` | The public contract defines the execute request plus response and error envelopes. `GatewayExecuteRequest` contains optional `preferredModel`, but the execution bridge does not consume that field for routing enforcement. |
| CF-09 | CURRENT_SOURCE_FACT | model-gateway: `src/provider-execution-bridge.ts` | `ProviderExecutionBridgeResult` | The bridge-specific result, not the unified interface contract, carries optional `response`, optional `error`, and required `receipt`. |
| CF-10 | CURRENT_SOURCE_FACT | model-gateway: `src/routing-policy.ts` | `RoutingRequest`, `RoutingPolicyEngine.decide`, `orderedProviders` | Exact model filtering uses `requestedModelId`; capability filtering uses `requiredCapabilities`; policy `allowedProviderIds` constrains routable providers. `preferredProviderId` only changes ordering and by itself permits another provider candidate. |
| CF-11 | CURRENT_SOURCE_FACT | model-gateway: `src/gateway-receipt.ts` | receipt builder and sanitizer | Gateway receipts are trace-addressable and sanitize metadata keys that resemble keys, secrets, tokens, or credentials. |
| CF-12 | CURRENT_SOURCE_FACT | S1 conformance spec | provider projection, outcome union, audit correlation | The provider may receive only `modelEvidenceProjection`; client-visible provider failure is fixed and safe; route `auditId` must equal `auditReceipt.auditId`. |

These are observations, not claims that the future binding already exists.

## Findings / Position

### Composition option comparison

| Option | Ownership shape | Benefits | Defects / risks | Decision |
| --- | --- | --- | --- | --- |
| A. Keep direct route-local fetch | The LPCI route continues to own endpoint defaults, model selection, credentials, HTTP execution, and provider failure mapping | Smallest immediate diff | Duplicates generic provider ownership, bypasses the existing routing/credential/admission/receipt owners, preserves unsupported implicit defaults, and cannot satisfy the UC-04 Model Gateway binding conjunct | REJECT |
| B. Thin LPCI binding over existing Model Gateway | LPCI owns only S1 projection, LPCI policy selection, result validation, and LPCI outcome/audit mapping; Model Gateway retains generic execution ownership | Reuses source-backed capability, credential, routing, adapter, admission, and receipt contracts while preserving LPCI-specific public boundaries | Requires a future package/import composition seam and explicit config translation; these are BUILD obligations, not current facts | SELECT |
| C. Parallel LPCI provider registry/gateway | A new LPCI subsystem owns its own providers, adapters, credentials, routing, and receipts | Could be tailored to one route | Creates a second generic provider owner, invites registry and policy drift, weakens receipt consistency, and contradicts the source-backed reuse requirement | REJECT |

Selected position: Option B. The future route must compose the existing
`ProviderExecutionBridge`; it must not wrap the current direct `fetch` and call
that a gateway, and it must not create a parallel generic provider owner.

### Selected ownership boundary

| Responsibility | Owner | Boundary |
| --- | --- | --- |
| S1 public-record clearance and `modelEvidenceProjection` construction | LPCI route/domain | Must complete before any Gateway call. Only the accepted projection enters the prompt. |
| Provider/model capability declaration | Existing Model Gateway capability registry | LPCI may validate against it but must not fork or shadow it. |
| Provider routing and model selection | Existing Model Gateway routing owner | LPCI supplies an exact admitted pair through singleton `policy.allowedProviderIds`, `routing.requestedModelId`, and required `complete` capability. `preferredProviderId` may preserve ordering but is not an enforcement control. |
| Credential resolution and secret-safe metadata | Existing Model Gateway credential boundary | Model Gateway must first harden whitespace handling. LPCI then creates a reference and performs secret-safe metadata preflight; LPCI never reads or trims the raw value. |
| Provider adapter execution, health, quota, admission, receipt | Existing Model Gateway execution bridge and injected owners | No route-local provider HTTP client remains after the future BUILD. |
| LPCI result validation and S1 outcome mapping | LPCI binding/route | Gateway success is necessary but not sufficient for `ANSWER_EMITTED`. |
| LPCI audit receipt and client response | Existing LPCI audit/route owner | Existing S1 `auditId` equality and client-safe response rules remain controlling. |

### DOC_ONLY_NEW composition seam

The following names are design vocabulary, not existing runtime symbols:

- `LpciModelGatewayBinding` - DOC_ONLY_NEW thin cvf-web composition seam.
- `resolveLpciProviderBindingConfig` - DOC_ONLY_NEW fail-closed parser and
  translator for the three LPCI variables.
- `LpciGatewayCorrelation` - DOC_ONLY_NEW server-internal correlation record
  containing only Gateway trace/receipt identifiers and the resulting LPCI
  audit identifier.
- `LPCI_PROVIDER_BINDING_INVALID` - DOC_ONLY_NEW internal diagnostic class;
  it is never a new client outcome.

The seam accepts an already-cleared S1 projection and injected existing Model
Gateway owners. It builds one Gateway request, validates one
`ProviderExecutionBridgeResult`,
and maps it back into existing LPCI outcomes. It owns no provider registry,
adapter, generic retry, fallback, quota, credential store, or generic receipt.

## Complete LPCI Configuration Contract

All three variables form one atomic contract. Adding them to an example file
without composing the package and bridge does not satisfy UC-04.

| Variable | Future contract | Validation | Absence / invalid disposition | Secret boundary |
| --- | --- | --- | --- | --- |
| `LPCI_LLM_API_KEY` | Remains the LPCI deployment input for the selected provider credential. The binding creates an existing `CredentialReference` whose `envNames` contains `LPCI_LLM_API_KEY` and whose `keyId` is LPCI-scoped. A future Model Gateway prerequisite must change secret availability so missing or trim-empty values are unavailable. LPCI then calls only `CredentialBoundary.resolveMetadata` before bridge execution. | Accept only `CredentialMetadata.available=true` from the hardened boundary. LPCI must not read, trim, compare, or otherwise handle the raw value. Metadata resolution is allowed; bridge/adapter/network execution is not. | Missing or whitespace-only means incomplete provider configuration: metadata preflight only, zero `ProviderExecutionBridge.execute`, adapter, and network calls, and existing `NO_PROVIDER_CONFIGURED`. | Never log, hash into a public receipt, return to the client, place in prompt/metadata, or print in diagnostics. Only existing secret-safe credential metadata may cross the credential boundary. |
| `LPCI_LLM_MODEL` | Required qualified selector with exact syntax `providerId/modelId`, split on one `/`. No default. | Both tokens non-empty; provider and model must be an exact capability-registry pair; model must include `complete`; selected provider must match the injected adapter/routing registry. | Missing/blank means `NO_PROVIDER_CONFIGURED`. Malformed or unsupported pair fails before execution and maps to safe `PROVIDER_ERROR`. | Non-secret, but client errors still do not disclose provider/model detail. |
| `LPCI_LLM_ENDPOINT` | Optional deployment assertion/override. Absent means use the admitted existing adapter's canonical endpoint. Present means it must normalize to an allowlisted canonical endpoint for the selected provider. It never selects a provider and is not a Gateway request field. | Absolute HTTPS URL, no userinfo, fragment, or arbitrary host; exact normalized provider allowlist match. | Invalid or provider-mismatched value fails before execution and maps to safe `PROVIDER_ERROR`; no arbitrary endpoint fetch. | Non-secret, but the value is not returned in client errors or copied into the public audit receipt. |

The current implicit endpoint/model defaults are deliberately not carried
forward. In particular, `gpt-4o-mini` cannot be silently translated because it
is not an exact current capability-registry model entry. A future addition of
that model belongs to the existing Model Gateway owner and needs its own
source-backed authorization.

## Request, Result, Receipt, And Audit Mapping

### Request mapping

| LPCI input | Gateway field | Rule |
| --- | --- | --- |
| Fresh server-generated correlation token | `traceId` | Must be unique for the request and retained only for server-side correlation. |
| Deterministic instructions plus serialized `modelEvidenceProjection` | `prompt` / `systemPrompt` | No full corpus row, private receipt, raw artifact, credential, endpoint, or unrelated request metadata may enter either string. |
| Configured provider | `policy.allowedProviderIds` | Must be the singleton array `[configuredProviderId]`. This is the provider enforcement boundary and prevents cross-provider fallback. |
| Configured model | `routing.requestedModelId` | Must equal `configuredModelId`; do not rely on request `preferredModel`, which the current bridge ignores. |
| Required method | `routing.requiredCapabilities` | Must be exactly `['complete']` for this text-completion use case. |
| Optional ordering hint | `routing.preferredProviderId` | May equal `configuredProviderId`, but it is redundant with the singleton allowlist and is never cited as enforcement. |
| LPCI execution policy | `policy` | Must be an explicit approved policy context with the singleton allowed-provider constraint; no permissive implicit policy. |
| Metadata | omitted or minimal safe constants | Query text, evidence records, credentials, endpoint, and audit receipt are forbidden in metadata because adapters receive it. |

### Result and correlation mapping

1. Treat the returned value as `ProviderExecutionBridgeResult`. Require no
   error, non-empty `GatewayExecuteResponse.text`, and a receipt.
2. Require response and receipt trace identifiers equal the request trace.
   Also require `response.model.providerId` and `receipt.providerId` equal
   `configuredProviderId`, and `response.model.modelId` plus
   `receipt.selectedModelId` equal `configuredModelId`. Any mismatch fails
   closed.
3. Treat the Gateway receipt as server-internal control evidence. Do not expose
   it in the S1 client response and do not replace the LPCI audit receipt with
   it.
4. Build the existing LPCI audit receipt through the accepted route owner and
   preserve `response.auditId == response.auditReceipt.auditId`.
5. Construct DOC_ONLY_NEW `LpciGatewayCorrelation` only after both receipts
   exist. Missing or mismatched identifiers fail closed; no answer is emitted.
6. Persist or expose no new correlation surface in this DESIGN. A later BUILD
   may keep the record request-local or write it only through a separately
   authorized secret-safe diagnostic owner.

## Fail-Closed Matrix

| Condition | Calls allowed | Internal disposition | Existing client outcome / message boundary |
| --- | --- | --- | --- |
| API key missing or whitespace-only after hardened secret-safe metadata preflight | metadata resolution only; zero bridge, adapter, and network calls | incomplete binding config | `NO_PROVIDER_CONFIGURED` |
| Qualified model absent | zero bridge and adapter calls | incomplete binding config | `NO_PROVIDER_CONFIGURED` |
| Qualified selector malformed | zero calls | `LPCI_PROVIDER_BINDING_INVALID` | `PROVIDER_ERROR`, fixed safe message |
| Provider/model unsupported or capability missing | zero calls | capability admission failure | `PROVIDER_ERROR`, fixed safe message |
| Endpoint override invalid or mismatched | zero calls | endpoint assertion failure | `PROVIDER_ERROR`, fixed safe message |
| Credential reference unavailable | zero adapter calls | existing credential-resolution error/receipt | `PROVIDER_ERROR`, fixed safe message |
| Routing policy denial or approval not granted | zero adapter calls | existing routing disposition/receipt | `PROVIDER_ERROR`, fixed safe message |
| No eligible candidate | zero adapter calls | existing no-candidate disposition/receipt | `PROVIDER_ERROR`, fixed safe message |
| Adapter/provider error | at most the calls admitted by existing Gateway policy | existing shielded Gateway error/receipt | `PROVIDER_ERROR`, fixed safe message |
| Empty, malformed, or otherwise invalid Gateway output | one admitted execution may have occurred; no answer emission | LPCI result-validation failure | `PROVIDER_ERROR`, fixed safe message |
| Gateway response/receipt trace mismatch or missing correlation | no answer emission | correlation failure | `PROVIDER_ERROR`, fixed safe message |
| Response/receipt provider or model differs from configured exact pair | no answer emission; no second provider attempt by LPCI | exact-pair validation failure | `PROVIDER_ERROR`, fixed safe message |
| S1 has no cleared candidate | zero Gateway and adapter calls | existing S1 abstention/grounding branch | Existing non-provider outcome; provider binding is not entered |

No failure branch may fall back to the current route-local `fetch`, another
provider, an arbitrary endpoint, an unregistered model, or a client-visible raw
provider diagnostic.

## UI And Interaction Implications

The selected design preserves the existing calm, evidence-first UI contract:

- loading remains in the existing result surface and does not disclose provider
  selection;
- `NO_PROVIDER_CONFIGURED` presents a short operator-configuration-required
  next action without echoing key, endpoint, provider, or model details;
- `PROVIDER_ERROR` remains a stable safe message and may show only the existing
  route audit/correlation identifier where already authorized;
- success continues to present answer, citations/evidence, and existing audit
  affordances; Gateway receipt, provider internals, routing rationale, and raw
  diagnostics remain server-internal;
- no additional dashboard, settings form, animation, visual hierarchy, or UI
  state is required by this DESIGN.

## Future BUILD Manifest And Import Seam

This is a responsibility manifest, not authorization and not a current-state
claim.

| Candidate future surface | Classification | Required BUILD responsibility |
| --- | --- | --- |
| cvf-web package manifest | FUTURE_BUILD_CANDIDATE | Declare an auditable import/dependency seam to the existing Model Gateway package; a copied implementation is forbidden. |
| cvf-web LPCI route | FUTURE_BUILD_CANDIDATE | Remove direct provider `fetch` and direct default ownership; invoke the thin binding only after S1 clearance. |
| cvf-web `src/lib/lpci/provider-binding.ts` | DOC_ONLY_NEW path | Implement `LpciModelGatewayBinding` and config translation with injected existing Gateway owners. |
| cvf-web safe example environment file | FUTURE_BUILD_CANDIDATE | Document all three variables together, qualified model syntax, optional endpoint assertion, and secret rules. This documentation alone is insufficient. |
| Existing or new LPCI focused tests | FUTURE_BUILD_CANDIDATE | Prove no-call and safe-mapping branches without network access. |
| Model Gateway credential boundary and focused tests | FUTURE_BUILD_PREREQUISITE owned by Model Gateway | Change secret availability to treat missing and trim-empty environment values as unavailable without exposing the value; prove metadata unavailable for whitespace and preserve raw-secret shielding. This prerequisite must land before LPCI relies on metadata preflight. |
| Existing Model Gateway public export surface | FUTURE_BUILD_CANDIDATE | Reuse only exported contracts; any missing export must be separately source-verified rather than bypassed with copied internals. |

A later BUILD packet must source-verify exact package-manager compatibility,
import names, construction dependencies, adapter availability, policy context,
and endpoint ownership at its own base HEAD. This DESIGN does not guess those
implementation details.

## Deterministic Synthetic Proof Contract

The later BUILD must use injected fake registries/resolvers/adapters and no
network or live credentials. Minimum deterministic cases:

| Proof ID | Fixture | Required observation |
| --- | --- | --- |
| SP-01 | Valid `openai/gpt-4o`, non-secret fake credential, canonical endpoint assertion, one admitted fake adapter, cleared S1 projection | Request has singleton `allowedProviderIds=['openai']`, `requestedModelId='gpt-4o'`, and `requiredCapabilities=['complete']`; exactly one OpenAI fake adapter call; prompt contains only accepted projection; response and receipt identify the exact pair; existing `ANSWER_EMITTED` with LPCI audit equality. |
| SP-02 | Missing or whitespace-only `LPCI_LLM_API_KEY` through the hardened CredentialBoundary | Secret-safe `resolveMetadata` may run and returns unavailable; `NO_PROVIDER_CONFIGURED`; zero `ProviderExecutionBridge.execute`, adapter, and network calls; LPCI never reads/trims raw secret. |
| SP-03 | Missing/blank `LPCI_LLM_MODEL` | `NO_PROVIDER_CONFIGURED`; zero calls. |
| SP-04 | `openai/gpt-4o-mini` or unknown provider/model | Safe `PROVIDER_ERROR`; zero adapter calls; proves exact registry admission and no current-default fallback. |
| SP-05 | Arbitrary or provider-mismatched endpoint | Safe `PROVIDER_ERROR`; zero adapter calls. |
| SP-06 | Existing routing denial/no candidate | Safe `PROVIDER_ERROR`; zero adapter calls; receipt stays server-internal. |
| SP-07 | Credential unavailable | Safe `PROVIDER_ERROR`; zero adapter calls; no secret in output, logs, or receipt projection. |
| SP-08 | Fake adapter error | Safe `PROVIDER_ERROR`; no raw message/status/endpoint/model reaches client. |
| SP-09 | Empty response, missing receipt, or trace mismatch | No answer emission; safe `PROVIDER_ERROR`; correlation fails closed. |
| SP-10 | No cleared S1 candidate | Existing S1 non-provider outcome; binding/fake adapter call count remains zero. |
| SP-11 | Configured provider is unavailable while another healthy provider offers the same requested model/capability | Singleton `allowedProviderIds` yields no cross-provider candidate; zero other-provider adapter calls; safe `PROVIDER_ERROR`. |
| SP-12 | Bridge response or receipt names a provider/model other than the configured pair | LPCI emits no answer and maps safe `PROVIDER_ERROR`; no LPCI retry or fallback occurs. |

Source-level assertions must also prove that direct route-local provider
`fetch` is absent after BUILD and that the package/import seam exists. A safe
example environment edit without those two assertions is an explicit failure.

## Risk / Corrective Action

| Risk | Corrective action required before or during BUILD |
| --- | --- |
| Mistaking documentation for binding | Require package/import, route-composition, and synthetic proof evidence together. |
| Treating the capability registry as a complete runtime router registry | Source-verify and inject the existing routing registry/adapters/admission records; do not manufacture a second registry. |
| Treating `preferredModel` or `preferredProviderId` as exact-pair enforcement | Use singleton `policy.allowedProviderIds`, `routing.requestedModelId`, and `requiredCapabilities=['complete']`; validate response and receipt identities after execution. |
| Treating whitespace credential text as unavailable under current source | Land the Model Gateway-owned trim-empty hardening and focused tests first; use only secret-safe metadata preflight from LPCI. |
| Keeping old defaults for convenience | Remove implicit model/endpoint defaults and enforce the atomic contract. |
| Leaking secrets through metadata, receipts, logs, or client errors | Keep raw values inside the credential resolver and test negative string absence across every outward surface. |
| Sending non-public S1 context to the provider | Build the Gateway prompt only from accepted `modelEvidenceProjection`; prove exact prompt shape. |
| Conflating Gateway receipt with LPCI audit receipt | Validate both independently and correlate server-side; preserve the S1 audit schema and equality rule. |
| Claiming live readiness from synthetic proof | Keep synthetic proof as build correctness only; live proof requires separate fresh provider/live authority after independent DESIGN acceptance. |

## Decision / Disposition

DESIGN_INDEPENDENTLY_ACCEPTED_BOUNDED

The selected design is a thin LPCI projection/binding seam composed over the
existing Model Gateway. Status quo direct provider ownership and a parallel
LPCI generic provider owner are rejected. The three-variable config contract,
ownership split, failure mappings, UI boundary, future BUILD manifest, and
synthetic proof contract are now explicit.

Lifecycle remains one strict chain:

1. this complete DESIGN is independently reviewed and accepted, including the
   UC-04 Model Gateway binding and three-variable config contract;
2. only after that acceptance may a separate fresh authority open provider/live
   execution or a BUILD tranche;
3. no current runtime, provider, live, deployment, readiness, or public claim
   follows from this audit.

## Claim Boundary

This audit is documentation design only. It does not assert that Model Gateway
is imported by cvf-web, that any provider/model is deployable, that any adapter
is configured, that any environment value exists, or that any route behavior
has changed. It authorizes no runtime/test/config/package/provider/live/public/
session mutation or execution. All DOC_ONLY_NEW names and future paths remain
nonexistent design candidates until a separate source-verified BUILD authority
accepts them.

## Independent Reviewer Acceptance

The primary reviewer independently accepted this DESIGN after R1 source-
fidelity repair. Acceptance is bounded by three mandatory future BUILD
conditions: use the bridge result type rather than a nonexistent unified result
type; constrain routing with a singleton provider allowlist, exact requested
model, and required completion capability; and land Model Gateway-owned
trim-empty credential hardening before LPCI relies on secret-safe metadata
preflight. This acceptance authorizes no BUILD or provider/live action.
