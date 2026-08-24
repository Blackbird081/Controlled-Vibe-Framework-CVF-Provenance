# CVF GC-018 RFR-R4 Material Context Manifest Baseline

Memory class: governed-baseline

Status: ACTIVE_BASELINE

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R4

Base head: `deaa1b750`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize bounded RFR-R4 remediation of verified finding F5: create a
secret-safe material-context manifest for the existing Model Gateway execute
path and bind it to the exact invocation evidence without copying raw model
inputs into receipts or evidence.

## Authorization / Decision

Decision: `PROCEED_WITH_RFR_R4`.

RFR-R3 is independently closed bounded at material commit `a18ba512f`. The
operator's standing dependency-ordered roadmap authority releases fresh R4
dispatch authoring while preserving the external no-commit worker and current
independent reviewer/closer roles.

## Scope / Target / Owner Boundary

R4 enriches the existing Model Gateway request, ProviderExecutionBridge,
tests, export barrel, and existing Truth Foundation reference contract. The
Model Gateway remains runtime owner. Truth Foundation supplies vocabulary and
authority boundaries only; no Truth Kernel runtime, database, verifier,
provider, credential, network, public, or deployment owner is opened.

## Current Verified Gap

`ProviderExecutionBridge.execute()` forwards prompt, optional system prompt,
metadata, selected provider/model, policy and routing-derived state into an
invocation and returns a receipt, but no single secret-safe record inventories
the material model-visible context classes and binds each class to source,
version, authority, transformation, scope and the exact trace. Existing
receipt fields record selected execution state only; they do not establish
complete input provenance.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Required Invariants

1. Every material context class supported by the current execute path is
   represented exactly once or explicitly marked absent/not-applicable.
2. Manifest entries bind context class, source reference, source version,
   authority/provenance label, transformation, scope, trace and digest.
3. Raw prompt, system prompt, metadata values, credentials, tokens, signed
   headers and secret-bearing fields never appear in manifest output.
4. Digests are deterministic for semantically identical supported inputs;
   unsupported, cyclic, accessor-hostile or secret-bearing input fails closed.
5. Manifest trace must equal request, routing decision, adapter input, response
   and receipt trace. Missing/mismatched manifest evidence stops before adapter.
6. Stopped requests and adapter failures return bounded manifest disposition
   without claiming successful provider execution.
7. Existing policy, routing, credential, health, quota, admission, receipt and
   shielded-error behavior remains intact.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| bridge forwards model-visible inputs without a manifest | RUNTIME_GAP | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | adapter invocation and success/failure results | `execute` | ProviderExecutionBridge | ACCEPT |
| execute request owns prompt, system prompt, policy, routing and metadata | REQUEST_OWNER | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayExecuteRequest` | `GatewayExecuteRequest` | unified gateway contract | ACCEPT |
| existing bridge tests own deterministic no-network composition | TEST_OWNER | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts` | ProviderExecutionBridge suites | `makeRequest`; `makeBridgeOptions` | Model Gateway tests | ACCEPT |
| barrel exports bridge contracts | EXPORT_OWNER | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Provider Execution Bridge exports | `ProviderExecutionBridge` | Model Gateway barrel | ACCEPT |
| Truth contract defines reference-not-copy and provenance/evidence minimums | GOVERNANCE_REFERENCE | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Reference-Not-Copy Rule; Provenance Label Contract; Evidence Record Minimum | provenance vocabulary | Truth Foundation reference | ACCEPT |
| F5 routes to R4 | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position | F5 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `b678e0192726c1adf40347637c17395b2eabe25e0e4ecacb6f141ddffd1c7a3c` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts` | `ad930ab62fc13977162a710b23572c5df6c2ea8796d635ccec8720a4c7527d6c` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `97f99a936fb00f118146d319e7ded76279848ba2027f530ff13d113a0b5975b3` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | `f8d1cabe54ca05d81b82be9428e11e866cef0ca63d1cc56fe5d8ae1680da5932` |
| `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | `e496b93b02b91c394152103367a5925d026ed1ee954e6e62e6fcc2d5e4334093` |

## Acceptance Criteria

1. Exact supported context classes reconcile to a deterministic manifest.
2. Raw/sensitive material is absent from every serialized manifest/result.
3. Missing, malformed, duplicate, unknown, mismatched or hostile evidence
   fails before adapter invocation.
4. Success, stopped and failure results preserve trace-bound manifest status
   without overclaiming execution.
5. Focused, full package, TypeScript, governance, manifest and no-commit proof
   pass with zero provider/live calls.

## Decision / Baseline / Proposed Tranche

Baseline: focused bridge tests pass 22/22 and TypeScript passes at `deaa1b750`.

Proposed tranche: one external no-commit worker, independent review, one
reviewer-owned material commit and separate continuity sync.

## Evidence / Verification

Worker evidence must include five source hashes, exact eight-path delta,
focused/full/typecheck results, deterministic and hostile-input matrices,
empty staging, unchanged HEAD and zero external calls. Reviewer independently
probes canonicalization, secret leakage, trace mismatch and completeness.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_changed_corpus_registry_coverage.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Dependency Release Evidence; Worker Return Packet Shape Contract |
| gateRunPurpose | confirm R4 packet structure after source verification; not first discovery |
| claimBoundary | structural conformance does not prove F5 implementation or closure |

## Epistemic Process Block

### Expected Result / Prediction

Existing request, bridge, receipt and Truth vocabulary owners should support a
bounded secret-safe manifest without a new subsystem.

### Evidence Comparison

Source inspection confirms the owner set and the missing complete invocation
context binding. The bridge already centralizes the exact pre-adapter boundary.

### Contradiction Or Gap Disposition

Truth Foundation vocabulary is documentation-only and cannot become runtime
authority. R4 adapts it into a Model Gateway-owned local contract.

### Claim Update

R4 is authorized for local implementation and proof only; F5 remains open
until independent review and material commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; public sync remains forbidden.

## Claim Boundary

This baseline authorizes only bounded local R4 implementation and proof. It
does not authorize provider/live calls, credentials, deployment, public sync,
push, production, R5-R6, or worker commit.
