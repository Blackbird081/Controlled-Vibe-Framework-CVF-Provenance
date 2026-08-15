# CVF CADP-AI-T5-R2 Transport-Neutral Adapter Negative-Proof Plan

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-08-15

Batch ID: CADP-AI-T5-R2

## Purpose

Name the adversarial classes the new CADP-AI-T5-R2 transport-neutral
external-readout adapter contract
(`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-adapter.contract.ts`)
must resist, and cite the exact test in
`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-adapter.contract.test.ts`
that proves each class fails closed. This plan documents proof that already
exists in the test file; it does not itself execute a test, register a
transport, or claim implementation readiness for a live external entry
point.

## Scope / Applies To

Applies to the ten adversarial classes named in the paired work order's
Adversarial Test Matrix
(`docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R2_TRANSPORT_NEUTRAL_EXTERNAL_READOUT_ADAPTER_FOUNDATION_2026-08-15.md`).
Does not apply to any transport, MCP tool, CLI command, credential,
provider, or network surface, because none exists in this foundation
tranche. Does not apply to authentication semantics, because no
authentication owner is implemented; every request reaches a controlled
`AUTHENTICATION_REQUIRED` rejection.

## Adversarial Class Proof Matrix

| Adversarial class | Attempted input | Proving test(s) | Required outcome | Disposition |
| --- | --- | --- | --- | --- |
| valid shapes with no auth owner | a fully well-shaped ingress + freshness + candidate-metadata request | `valid shapes with no auth owner` - two tests | controlled `AUTHENTICATION_REQUIRED`; no metadata field on the response envelope | PROVEN |
| malformed/unknown/oversize/proxy/accessor input | non-object, `null`, unknown top-level field, accessor `ingress` getter, `Proxy`-wrapped request, oversize nested `requestedFields` | `malformed/unknown/oversize/proxy/accessor input` - six tests | fails before any later stage runs; accessor getter is never invoked; Proxy is rejected at the ingress boundary before deeper composition | PROVEN |
| stale/expired/invalid timestamp | freshness input observed materially later than issuance, observed after expiry, or a non-calendar timestamp | `stale/expired/invalid timestamp` - three tests | deterministic controlled rejection at the `FRESHNESS` stage; an invalid `issuedAt` never reaches the receipt constructor unguarded | PROVEN |
| secret field or private path | a secret-named candidate field or private-provenance path marker inside candidate metadata | `secret field or private path` - two tests | rejection at the `REDACTION` stage; no raw secret value appears in the serialized response | PROVEN |
| field outside allowlist | a candidate-metadata field outside the exact T5-R1 allowlist | `field outside allowlist` - one test | rejection at `ALLOWLIST` with `UNKNOWN_FIELD`; no metadata output | PROVEN |
| authority-shaped input | request-shaped injection of `accepted: true`, `authenticationVerified: true`, `externalExecutionAuthorized: true` | `authority-shaped input` - one test asserting every authority field on the response remains literal `false` | no literal-false output field can be widened by request-shaped injection | PROVEN |
| key-order and post-call mutation | repeated valid and malformed calls with identical rejecting stage/issuedAt; attempted post-call field assignment on a frozen response | `key-order and post-call mutation` - three tests | identical receipt identity across repeated calls without ambient ordinal state; `Object.freeze` on the response/receipt/issues prevents post-call mutation (throws in strict mode; field unchanged) | PROVEN |
| callback/function/port injection | a function value injected under an unknown request field | `callback/function/port injection` - one test | rejected by the public input shape before any later stage; the injected function is never invoked | PROVEN |
| root export removed or renamed | removing or renaming T5-R1 package-root exports is checker-covered; R2 exports are direct-source/typecheck confirmed but cannot be assigned the same unique `packageRootPath` by fixture schema | T4 drift checker over `T5R1_EXTERNAL_READOUT_FOUNDATION`; TypeScript check and direct reviewer read for R2 | T5-R1 drift is detected; R2 independent fixture proof remains a disclosed checker-schema residual | SATISFIED_BOUNDED_CONTRACT_ONLY |
| forbidden seam token | (structural, not unit-tested) `child_process`, `node:net`, `node:http`, `node:https`, `node:fs`, `fetch(`, `XMLHttpRequest`, or `process.env` appearing in the owned contract source | T4 drift checker `FORBIDDEN_EXECUTION_SEAM` code over both the `T5R1_EXTERNAL_READOUT_FOUNDATION` and `T5R2_EXTERNAL_READOUT_ADAPTER` fixture entries' `forbiddenSeamTokens` | checker reports a forbidden seam if any listed token appears as real code or an import/require specifier | PROVEN_BY_STRUCTURAL_CHECKER |

## Package-Root Discoverability Boundary

The T4 drift checker's fixture schema
(`governance/compat/check_cadp_authority_boundary_drift.py`, fixture
validation in `load_fixture`) treats a surface's `packageRootPath` as an
owned path that must be unique across the whole fixture; two surfaces
cannot both declare the same `packageRootPath` file. Because the T5-R1
foundation and T5-R2 adapter contracts share one package root
(`EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`), only one fixture surface may
carry package-root proof for that file. This tranche keeps package-root
proof on the `T5R1_EXTERNAL_READOUT_FOUNDATION` surface (satisfying the
work order's "T5-R1 fixture row gains only exact package-root proof"
acceptance criterion) and sets `T5R2_EXTERNAL_READOUT_ADAPTER`'s
`packageRootPath`/`requiredExportModule`/`requiredExportSymbols` to
`null`/`null`/`[]`.

This is a fixture/checker structural limit, not a source-code limit: the
adapter module's `CADP_EXTERNAL_READOUT_ADAPTER_CONTRACT_VERSION` and
`evaluateCadpExternalReadoutAdapter` symbols are still exported by name from
both `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` (internal
barrel) and `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` (package root); the
export exists in source and is confirmed by direct reading of both files,
even though the T4 checker's current one-surface-per-root schema cannot
independently re-verify that specific export block against a second
fixture row for the same file.

## Non-Test Structural Proof

Two structural checks outside the Vitest suite independently constrain
authority widening across the whole module, not only the cases the test
suite enumerates:

1. `python governance/compat/check_cadp_authority_boundary_drift.py`
   lexically scans both the `T5R1_EXTERNAL_READOUT_FOUNDATION` and
   `T5R2_EXTERNAL_READOUT_ADAPTER` fixture surface entries in
   `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
   against their contract source files, and fails on any
   `readonly <field>: false` type-position or `<field>: false`
   value-position widening, on any of the fixture's `forbiddenSeamTokens`
   appearing as real code, and (for the T5-R1 surface) on a missing
   package-root export symbol.
2. TypeScript's structural type system independently rejects, at compile
   time, any attempt to assign a non-`false` value to a field typed as the
   literal `false` on `CadpExternalReadoutAdapterResponse` (for example
   `accepted: false`, `authenticationVerified: false`), which is a second,
   compiler-enforced backstop beyond the lexical checker and the Vitest
   assertions above.

## Claim Boundary

This plan documents test coverage for a pure, deterministic, side-effect-free
adapter contract module. It proves the module fails closed against the named
runtime adversarial inputs and records the bounded R2 package-root checker
residual rather than overstating it. It makes no claim about a
live external transport, MCP tool, CLI command, network behavior, or
credential resolution, because none of those exist in this foundation
tranche, and no claim that a positive authenticated readout is possible,
because no authentication owner is implemented.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-contract reference document; no public
artifact or sync action is authorized.
