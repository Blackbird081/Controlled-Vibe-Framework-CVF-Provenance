# CVF GC-018 Baseline - RFR-R7B Optional Field Composition Seam

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-25

Batch ID: RFR-R7B-OPTIONAL-FIELD-COMPOSITION-SEAM

Dispatch base head: `e66a21554`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through standing dependency-ordered roadmap authority

Reviewer owner: current independent orchestrator/reviewer/closer

Worker target: one delegated implementation worker role

## Purpose

Repair the exact R4/R3 composition seam where an optional
`GatewayExecuteRequest` field supplied as an own data property with value
`undefined` is rejected instead of being treated as absent. Preserve strict,
fail-closed validation for required, malformed, accessor-backed, inherited,
hostile and non-`undefined` invalid inputs.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R7B-OPTIONAL-FIELD-COMPOSITION-SEAM --title "CVF RFR-R7B Optional Field Composition Seam" --date 2026-08-25 --base e66a21554 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R7A independently accepted and materially closed at 1512374e8" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified R7B owner, exact-three worker manifest, adversarial compatibility contract and no-fixture-workaround rule |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, lifecycle-hygiene, checker-read-ahead, worker-return-quality and corpus-coverage checkers were routed before authoring |
| docOnlyNewFields | none; existing governed dispatch fields are reused |
| claimBoundary | dispatch provenance only; no implementation, provider, live or production claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R7A independent acceptance | completion review and material commit `1512374e835a2d8895a4927eb086ce3e987f7e88` | R7A must close before R7B owner opens | ACCEPT |
| R7A closure continuity | session-sync commit `e66a21554` | active mode must identify R7B dispatch preparation | ACCEPT |
| reproduced R7B seam | current MCP focused run: 4/7 pass, exact three named failures | failures must trace to the same optional-own-`undefined` validator behavior | ACCEPT |
| Model Gateway baseline | R6 evidence: focused 58/58, package 288/288, TypeScript PASS | no unrelated Model Gateway regression is admitted | ACCEPT |

## Current Verified Defect

`readDataField` distinguishes a missing descriptor from an own descriptor but
marks every own descriptor as present. For optional fields this makes an own
data property whose value is `undefined` enter present-value validation. The
MCP adapter produces that ordinary JavaScript shape for omitted optional
`systemPrompt`, so downstream manifest construction fails before the provider
bridge. Three existing composition proofs reproduce the defect.

## Scope

The worker may modify only the Model Gateway material-context manifest owner,
its existing dedicated tests and the named return. The existing MCP
composition proof is read-only acceptance evidence. No MCP fixture, request
contract, bridge, package manifest, lockfile, Guard Contract, governance,
roadmap or continuity edit belongs to the worker.

## Acceptance Invariants

- An optional own data property with value `undefined` is normalized to the
  same explicit-absence representation as an omitted optional property.
- `systemPrompt`, `metadata`, and `routing` are covered independently.
- Omitted and own-`undefined` forms produce identical manifest and adapter
  input digests for otherwise identical requests.
- Required request and invocation-binding fields remain required; missing or
  `undefined` required values reject.
- Optional non-`undefined` invalid values, accessors, hostile prototypes,
  symbol material, trace drift and secret-shaped metadata remain fail-closed.
- Getters are never invoked and inherited values are never admitted.
- The three existing MCP composition failures pass without editing their test
  file or weakening expected results.
- Model Gateway focused/full tests and TypeScript pass with no regression.

## Baseline Decision

`PROCEED_BOUNDED_IMPLEMENTATION`: R7B may repair only optional-own-`undefined`
normalization at the existing Model Gateway validator boundary.

## Evidence / Verification

Required proof is the direct optional/required/accessor/prototype adversarial
matrix, the unchanged seven-test MCP composition proof, both full package
suites, both TypeScript/build commands, exact source-hash reconciliation,
worker-return fast gate and independent reviewer reproduction.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| optional request fields are typed optional | CONTRACT_SOURCE | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `GatewayExecuteRequest` | `systemPrompt?`; `routing?`; `metadata?` | unified gateway request contract | ACCEPT |
| own descriptors are always marked present | RUNTIME_SOURCE | `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts` | `readDataField` | descriptor return path | material-context manifest owner | ACCEPT |
| optional system prompt rejects present non-string | RUNTIME_SOURCE | `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts` | `buildMaterialContextManifest` | `systemPrompt.present` check | material-context manifest owner | ACCEPT |
| omission has direct tests but own undefined does not | TEST_SOURCE | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts` | optional absence test | `makeRequest`; manifest entries | Model Gateway test owner | ACCEPT |
| three MCP composition proofs fail downstream validation | COMPOSITION_TEST | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | ALLOW/success, real-engine ALLOW and shielded-error cases | existing seven-test suite | MCP composition proof owner | ACCEPT |

## Source Hash Manifest

| Path | SHA-256 at dispatch authoring | Worker disposition |
| --- | --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts` | `d1e28b6e29373ac355887f1f3e4ad5d6a28c20406b18ee96b6f53b062f2eeb5c` | editable |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts` | `b6897be896961b8e65177f7f578f906f906e894283bb03fae53c125b19cc2e33` | editable |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `52b00ddf27b0879cd523fe826eb0914482a374f65a7b6e92b3839dde98f7d994` | read/test only; byte-unchanged |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact artifact paths | all three R7B artifact `Test-Path` checks returned false before authoring | ACCEPT |
| tranche token collision | no prior `RFR-R7B`, `RFR_R7B` or exact batch-token artifact in governed artifact/session roots | ACCEPT |
| owner collision | current source, test and MCP composition proof identify one existing validator owner; no new owner is needed | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Dependency Release Evidence; Worker Return Packet Shape Contract; Agent Handoff Contract Control Block |
| gateRunPurpose | confirm final packet shape after source verification |
| claimBoundary | checker conformance does not prove the validator repair |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | exact-three worker manifest | local repair/test/return only; no commit | paired work order | repository-local TypeScript | `IMPLEMENTATION_AUTHORIZED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | existing MCP-to-Model-Gateway composition | read-only acceptance consumer; no fixture edit or live call | existing composition proof | existing injected executor | `TEST_ONLY_NO_EXTERNAL_EFFECT` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance remediation; no public-sync action is authorized.

## Claim Boundary

This baseline authorizes only the paired exact-three local worker manifest. It
does not authorize MCP fixture edits, request-schema widening, dependency
installation, provider/live/network calls, credential access, deployment,
public sync, push, production readiness or worker closure.
