# CVF GC-018 RFR-R5 Isolation Guarantee Admission Baseline

Memory class: governed-baseline

Status: ACTIVE_BASELINE

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R5

Base head: `0ee6e76b6`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize bounded remediation of verified finding F9: bind every sandbox
isolation claim to an explicit adapter guarantee profile, reject unsupported
security-boundary requirements before execution, and expose best-effort
worker-thread behavior without presenting it as physical containment.

## Authorization / Decision

Decision: `PROCEED_WITH_RFR_R5`.

RFR-R4 is independently closed at material commit `8ec399aa5` and continuity
commit `0ee6e76b6`. The operator's standing dependency-ordered authority releases
fresh R5 dispatch while preserving external no-commit worker and independent
reviewer/closer roles.

## Scope / Target / Owner Boundary

R5 enriches the existing Safety Runtime isolation contract and its local
Runtime Adapter Hub mirror, WorkerThread adapter, tests, export barrel and
existing pre-public reference. It creates no new sandbox engine, container,
daemon, provider, credential, deployment or public owner.

## Current Verified Gap

`WorkerThreadSandboxAdapter` correctly comments that Node worker threads are
not a security boundary, but it still accepts restrictive filesystem/network
configuration, calls a host child process, and supplies inherited
`process.env`. Its result contains no dimensional guarantee/admission evidence.
The declaration can therefore be read more strongly than actual enforcement.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Required Invariants

1. The canonical dimensions are exactly filesystem, network, process,
   environment, credential, IPC, persistence and host.
2. Every executor exposes a typed, immutable guarantee profile; every result,
   including rejection/failure, carries the corresponding admission evidence.
3. Default configuration requires a security boundary and fails closed when
   the selected executor cannot guarantee every required dimension.
4. `worker_threads` never claims filesystem, network, process, credential,
   IPC, persistence or host isolation.
5. Best-effort execution requires explicit caller intent and zero required
   security dimensions; policy heuristics remain advisory, not guarantees.
6. Unsupported, duplicate, unknown, malformed or inconsistent requirements
   reject before worker/child-process creation.
7. Host environment is not implicitly copied into worker or child-process
   execution; only explicitly supplied command environment may cross.
8. Existing timeout, output, resource and policy prechecks remain bounded and
   must not be relabeled physical containment.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| canonical contract lacks dimensional guarantee/admission evidence | TYPE_GAP | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts` | types, defaults and execute | `SandboxConfig`; `SandboxResult`; `SandboxExecutor` | Safety Runtime isolation contract | ACCEPT |
| local structural mirror must remain aligned | MIRROR_OWNER | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts` | complete mirror | sandbox types and defaults | Runtime Adapter Hub | ACCEPT |
| worker thread runs host child process with inherited environment | RUNTIME_GAP | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts` | `execute`; `runInWorker` | `execFileSync`; `process.env` | WorkerThreadSandboxAdapter | ACCEPT |
| focused adapter proof owner exists | TEST_OWNER | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts` | WorkerThreadSandboxAdapter suite | worker-thread cases | Runtime Adapter Hub tests | ACCEPT |
| canonical contract proof owner exists | TEST_OWNER | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts` | execute, validation and defaults | SandboxIsolationContract suite | Safety Runtime tests | ACCEPT |
| adapter barrel owns public symbol export | EXPORT_OWNER | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts` | adapter exports | `WorkerThreadSandboxAdapter` | Runtime Adapter Hub barrel | ACCEPT |
| existing package reference needs bounded guarantee wording | REFERENCE_OWNER | `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md` | export boundary and packet consequences | Runtime Adapter Hub export surface | pre-public reference | ACCEPT |
| F9 routes to R5 | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position and Risk / Corrective Action | F9 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts` | `a6e31345a06a28090d9b031d19f3e1ed401c39a51da257288de00debaa5caebe` |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts` | `a907b31e4e5fa83024c50092debaf6d82add6b1558f31c8e1d1cba0f65b17ad4` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts` | `8a2cb4c009a822a070598a17b166a207b7ec318801cf0fca967e569aa1a6f3ca` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts` | `f450e3deb6dee7398c34d716fbab39f9ef7028d19e70cb3a47aed0708b92006d` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts` | `d9cefbda3c08e180c2f3970c689e860bd0ab88b11d801177542d21304dfc3aee` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts` | `9c0d59d0e06922ce729cdc70f3f52141edd59b642d8f7d4f427fcbce399b5e94` |
| `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md` | `4f9847a8b702159faf9c62a5f520fb104651cd1dac85bfc146aff255dc03297a` |

## Acceptance Criteria

1. All eight dimensions reconcile exactly between requirement, adapter
   profile, admission evidence and result.
2. Default and unsupported security requirements reject before execution.
3. Explicit best-effort execution is labeled non-security and cannot request
   a guaranteed dimension.
4. Environment inheritance and unknown/duplicate/malformed dimensions have
   adversarial tests.
5. Focused, package, TypeScript, governance, exact-manifest and no-commit proof
   pass with zero live/provider/network calls.

## Decision / Baseline / Proposed Tranche

Baseline: Runtime Adapter Hub focused tests pass 29/29, package tests pass
71/71, and TypeScript passes at `0ee6e76b6`. Safety Runtime local `npm test`
is unavailable because its checked-out dependency tree lacks `esbuild`; no
installation or network action is authorized. The worker must use an existing
repo-local toolchain if available or report that component exactly as blocked,
without weakening Runtime Adapter Hub proof.

Proposed tranche: one external no-commit worker, independent review, one
reviewer-owned material commit and separate continuity sync.

## Evidence / Verification

Worker evidence must include seven source hashes, exact eight-path delta,
focused/full/typecheck results, the complete dimensional admission matrix,
environment non-inheritance proof, empty staging, unchanged HEAD and zero
external calls. The reviewer independently probes rejection timing, profile
completeness, mirror parity and claim wording.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_changed_corpus_registry_coverage.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Dependency Release Evidence; Worker Return Packet Shape Contract |
| gateRunPurpose | confirm R5 packet structure after source verification; not first discovery |
| claimBoundary | structural conformance does not prove F9 remediation or closure |

## Epistemic Process Block

### Expected Result / Prediction

The existing contract/mirror/adapter owners should support typed dimensional
admission without a new sandbox subsystem.

### Evidence Comparison

Inspection confirms that the owner set exists and that actual worker-thread
behavior is weaker than its configurable policy vocabulary.

### Contradiction Or Gap Disposition

Physical containment cannot be manufactured in this tranche. Unsupported
security requirements must reject; explicit best-effort behavior remains a
bounded delegation mode.

### Claim Update

R5 is authorized for local implementation and proof only; F9 remains open
until independent review and material commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; public sync remains forbidden.

## Claim Boundary

This baseline authorizes only bounded local R5 implementation and proof. It
does not authorize container deployment, provider/live calls, credentials,
network access, public sync, push, production, R6, or worker commit.
