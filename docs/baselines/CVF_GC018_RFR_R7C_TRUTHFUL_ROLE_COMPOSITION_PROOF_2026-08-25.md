# CVF GC-018 Baseline - RFR-R7C Truthful Role Composition Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-25

Batch ID: RFR-R7C-TRUTHFUL-ROLE-COMPOSITION-PROOF

Dispatch base head: `365d411ee`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through standing dependency-ordered roadmap authority

Reviewer owner: current independent orchestrator/reviewer/closer

Worker target: one delegated test-only worker role

## Purpose

Reconcile one stale MCP composition positive-path fixture with the accepted
R7A truthful-action contract: `AI_AGENT`/`ORCHESTRATOR` execution blocks while
an already authorized `OPERATOR` execution may reach canonical ALLOW. Restore
the full MCP suite without changing production authority or runtime code.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R7C-TRUTHFUL-ROLE-COMPOSITION-PROOF --title "CVF RFR-R7C Truthful Role Composition Proof" --date 2026-08-25 --base 365d411ee --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R7B independently accepted and materially closed at 79ca7e542" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified one-test residual, exact-two worker manifest, immutable authority boundary and positive/negative role proof |
| checkerReadAheadConfirmation | applicable dispatch, handoff, worker-return, corpus and artifact checkers routed before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no test result or runtime behavior claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R7A truthful role semantics | R7A completion review at material `1512374e8` | AI-agent/orchestrator BLOCK and OPERATOR ALLOW must remain invariant | ACCEPT |
| R7B bounded closure | completion review and material `79ca7e542` | optional-field repair must close before fixture reconciliation | ACCEPT |
| R7B continuity | `365d411ee` | active mode must identify R7C preparation | ACCEPT |
| exact residual | independent MCP focused 31/32 and package 779/780 | only the named real-engine positive case may change | ACCEPT |

## Current Verified Gap

The composition proof's shared `VALID_INPUT` uses `agentRole: 'AI_AGENT'`.
Its positive real-engine case expects ALLOW, but canonical R7A behavior
truthfully blocks that role/action pair at `authority_gate`. Other accepted
tests already prove a real OPERATOR execute ALLOW and AI-agent/orchestrator
execute BLOCK. The residual is a test-role mismatch, not a production defect.

## Scope

The worker may edit only the existing MCP composition proof and create the
named return. Guard Contract, all production source, Model Gateway, other
tests, package manifests, lockfiles, governance, roadmap and continuity are
forbidden. The worker must not change shared fixtures in a way that weakens
negative cases.

## Acceptance Invariants

- The real-engine positive composition case uses an already authorized role
  and reaches ALLOW with truthful `execute` action semantics.
- Existing AI-agent/orchestrator BLOCK proof remains byte-unchanged in its
  owning test file and passes.
- The real risk-gate BLOCK composition case still blocks by `risk_gate`.
- No production source, authority matrix, role normalization, action label,
  guard order or runtime schema changes.
- Composition proof passes 7/7 and MCP package passes 780/780.

## Baseline Decision

`PROCEED_TEST_ONLY_IMPLEMENTATION`: reconcile one stale positive fixture only.
Authority widening and runtime relabeling are explicitly rejected.

## Evidence / Verification

Required proof is the focused 7-test composition suite, the existing 25-test
execute suite, full MCP 780-test package, TypeScript build, three source hashes,
worker-return fast gate and exact two-path worker manifest.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| positive fixture inherits AI_AGENT | TEST_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `VALID_INPUT`; real-engine ALLOW case | `VALID_INPUT` | MCP composition test | ACCEPT |
| OPERATOR execute ALLOW is already proved | TEST_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | registered MCP tool composition | OPERATOR ALLOW test | MCP execute test | ACCEPT |
| AI-agent/orchestrator execute BLOCK is already proved | TEST_SOURCE | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | registered MCP tool composition | AI-agent BLOCK test | MCP execute test | ACCEPT |
| canonical matrix permits OPERATOR execute but not AI-agent execute | CONTRACT_SOURCE | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `AUTHORITY_MATRIX` | `AUTHORITY_MATRIX` | Guard Contract | ACCEPT |

## Source Hash Manifest

| Path | SHA-256 at dispatch | Authority |
| --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `52b00ddf27b0879cd523fe826eb0914482a374f65a7b6e92b3839dde98f7d994` | edit |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | `5a00e42bef507966928ff6f4b0fce862676ce611a7ee4e828d879db7320ae52d` | read/test only; MATCH required |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | `901e3f25ed1f6a2ab4e9f9eeaa2fc98a7dcf985cb3474eb6245ad1b844fc537c` | read/hash only; MATCH required |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact artifact paths | three `Test-Path` checks false before authoring | ACCEPT |
| source owner | one failing test and existing role proofs identified | ACCEPT |
| production collision | no production edit is necessary or authorized | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Dependency Release Evidence |
| gateRunPurpose | confirm final dispatch shape after source verification |
| claimBoundary | checker conformance does not prove the test reconciliation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance test repair; no public-sync action is authorized.

## Claim Boundary

This baseline authorizes one MCP test edit and one worker return only. It does
not authorize production, Guard Contract, authority, Model Gateway, package,
installation, provider/live/network, credential, deployment, public-sync,
push or production-readiness changes.
