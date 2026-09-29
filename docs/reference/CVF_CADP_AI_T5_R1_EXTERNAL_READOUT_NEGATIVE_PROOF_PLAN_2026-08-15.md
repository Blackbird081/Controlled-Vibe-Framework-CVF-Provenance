# CVF CADP-AI-T5-R1 External Readout Negative-Proof Plan

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-08-15

Batch ID: CADP-AI-T5-R1

## Purpose

Name the adversarial classes the new CADP-AI-T5-R1 external readout
foundation contract (`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.ts`)
must resist, and cite the exact test in
`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/cadp-external-readout-foundation.contract.test.ts`
that proves each class fails closed. This plan documents proof that already
exists in the test file; it does not itself execute a test, register a
transport, or claim implementation readiness for a live external entry
point.

## Scope / Applies To

Applies to the eight adversarial classes named in the paired work order's
Adversarial Test Matrix
(`docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R1_EXTERNAL_READOUT_AUTHORITY_FOUNDATION_2026-08-15.md`).
Does not apply to any transport, MCP tool, CLI command, credential,
provider, or network surface, because none exists in this foundation
tranche.

## Adversarial Class Proof Matrix

| Adversarial class | Attempted input | Proving test(s) | Required proof-of-fail-closed behavior | Disposition |
| --- | --- | --- | --- | --- |
| authority widening | any authority-adjacent field set to `true` on the exact metadata allowlist | `exact metadata field allowlist (adversarial: authority widening)` - six field-specific tests plus a missing-field test | validator rejects every widened field; a field that is merely absent (not `false`) is also rejected | PROVEN |
| unknown fields | ingress payload includes a top-level or `requestedFields` field outside the exact allowlist | `ingress schema/size validator (adversarial: unknown fields)` - two tests; `caller identity input contract (adversarial: identity mismatch)` unknown-field test; `exact metadata field allowlist (adversarial: authority widening)` unknown-field test | validator returns a typed `UNKNOWN_FIELD` issue and `valid: false`; no silent pass-through | PROVEN |
| oversize input | `requestedFields` or nested `requestedScope` exceeds the exact size bound | `ingress schema/size validator (adversarial: oversize input)` - two tests | size validator rejects with `REQUEST_TOO_LARGE` before allowlist/redaction logic runs, per the field-order in `validateCadpExternalReadoutIngress` | PROVEN |
| secret / private provenance | payload field name matches `CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES`, or a string value contains a private-provenance path marker | `redaction contract (adversarial: secret / private provenance)` - parameterized test over every redacted field name, plus a path-marker test and a never-re-emitted serialization test | redaction function rejects and lists the field; the redacted field's raw value never appears in the function's own JSON-serialized result | PROVEN |
| replay | freshness input observed materially before `issuedAt`, or after `expiresAt` | `replay/freshness contract (adversarial: replay)` - two tests (`INVALID` for before-issue, `EXPIRED` for after-expiry) | freshness check returns an explicit `INVALID` or `EXPIRED` disposition with a `REPLAY_WINDOW_EXCEEDED` issue, never `FRESH` | PROVEN |
| stale request | freshness input observed materially later than issuance but still inside the expiry window | `replay/freshness contract (adversarial: stale request)` - one test | freshness check returns explicit `STALE` disposition with a `STALE_REQUEST` issue | PROVEN |
| identity mismatch | caller identity input with a malformed `callerId` shape or a non-string `callerId` | `caller identity input contract (adversarial: identity mismatch)` - two tests plus the ingress-level identity propagation covered by `caller identity input contract (positive)` | identity validator returns a typed `INVALID_CALLER_IDENTITY` issue; no silent acceptance | PROVEN |
| mutation/activation/execution/provider flags | any new type's authority-adjacent field inspected for a non-`false` value; receipt's `receiptGrants*` fields inspected | `mutation/activation/execution/provider flags (adversarial)` - one test asserting every authority field on both the allowlisted-metadata type and the receipt type is literal `false`; the test itself performs no mutation, activation, execution, or provider call | every exported type's authority-adjacent field is absent or literal `false`; no test in the suite exercises an actual mutation, activation, execution, or provider call | PROVEN |

Supplemental reviewer hardening: the deterministic receipt suite also proves
that equivalent object-key order produces the same hash, the returned payload
is an independently owned recursively frozen snapshot, impossible calendar
timestamps fail closed, and an accessor named `toJSON` is rejected with zero
getter calls. These probes prevent structural test success from masking an
impure or caller-code-executing serialization path.

## Non-Test Structural Proof

Two structural checks outside the Vitest suite independently constrain
authority widening across the whole module, not only the cases the test
suite enumerates:

1. `python governance/compat/check_cadp_authority_boundary_drift.py` lexically
   scans the new `T5R1_EXTERNAL_READOUT_FOUNDATION` fixture surface entry in
   `governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`
   against the contract source file, and fails on any `readonly <field>: false`
   type-position or `<field>: false` value-position widening, and on any of
   the fixture's `forbiddenSeamTokens` (`child_process`, `node:net`,
   `node:http`, `node:https`, `node:fs`, `fetch(`, `XMLHttpRequest`,
   `process.env`) appearing as a real import/require specifier or in code.
2. TypeScript's structural type system independently rejects, at compile
   time, any attempt to assign a non-`false` value to a field typed as the
   literal `false` (for example `receiptGrantsExecution: false` on
   `CadpExternalReadoutReceipt`), which is a second, compiler-enforced
   backstop beyond the lexical checker and the Vitest assertions above.

## Claim Boundary

This plan documents test coverage for a pure, deterministic, side-effect-free
contract module. It proves the module fails closed against the eight named
adversarial input classes at the shape/type level and via the T4 lexical
drift checker. It makes no claim about a live external transport, MCP tool,
CLI command, network behavior, or credential resolution, because none of
those exist in this foundation tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-contract reference document; no public
artifact or sync action is authorized.
