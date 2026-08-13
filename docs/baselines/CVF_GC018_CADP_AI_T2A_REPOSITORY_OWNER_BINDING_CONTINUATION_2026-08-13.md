# CVF GC-018 Baseline - CADP-AI-T2A Repository-Owned Capability Evidence Binding

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-13

Batch ID: CADP-AI-T2A

Dispatch base head: `86e06ab84896e3433f0484551facc2c6a08bb480`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: implementation worker

## Purpose

Continue T2 from its accepted fail-closed checkpoint and implement the missing
source-verified owner seam. The private provenance repository's committed Git
object database is the authority source; a caller may request a committed
grant by path but may not supply, mint, replace or mutate the grant data.

## Authorization

The operator explicitly authorized completion of T2 on 2026-08-13, including
the runtime or live proof genuinely required. This releases the owner-specific
continuation only. It does not authorize public sync, deployment or production
claims.

## Scope

The implementation may:

- add one committed repository-owned capability grant;
- resolve the canonical repository from the production module location;
- read only committed `HEAD` blobs through argument-array Git subprocesses;
- verify grant schema and SHA-256 pins before producing an opaque handle;
- keep handle identity in module-private state;
- persist invocation/retry/replay consumption atomically in a private SQLite
  state file;
- reconcile work-order, capability, assignment, action, transport, resource,
  credential-reference, time, trace, receipt and replay constraints;
- adapt CADP evidence validation to consume the verified owner handle;
- add adversarial tests and package-boundary proof.

## Non-Goals

No caller-authored grant object, arbitrary repository root, injected owner
source, test-double authority, raw secret, provider execution, external CLI/MCP
adapter, public sync, deployment or production-readiness claim is authorized.
Live provider proof is not required unless implementation evidence makes a
provider behavior claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification Block; exact manifest; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirmation after source inspection and packet authoring, not first discovery |
| claimBoundary | checker conformance cannot prove Git authority isolation, replay durability or absence of an authority escape hatch |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| committed Git blobs can be the private provenance authority | current repository boundary | `AGENTS.md` | Critical Repository Boundary | private provenance repository | CVF authority hierarchy | ACCEPT |
| current owner module has no source | current runtime truth | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | direct implementations | `isBoundCapabilityOwner` | owner-binding contract | ACCEPT |
| CADP high ranks consume an owner handle | current contract truth | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | compatibility evidence validator | `validateCompatibilityEvidence` | CADP contract | ACCEPT |
| workflow trace has concrete receipt identity | current contract truth | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts` | execution trace schema | `WorkflowStepExecutionTrace` | workflow-binding contract | ACCEPT |
| receipt binding derives emission from trace | current contract truth | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | receipt emission functions | `emitStepReceipt` | receipt-binding contract | ACCEPT |
| durable SQLite is available in owning package | current implementation truth | `EXTENSIONS/CVF_GUARD_CONTRACT/src/audit/sqlite-db.ts` | database owner | `AuditDatabase` | Guard Contract audit owner | ACCEPT |
| provider API key is an owner-signing key | authority claim | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | credential reference boundary | `CredentialReference` | Model Gateway credential owner | REJECT |

## Trust Boundary Decision

The repository object database is the trust root because grant and artifact
bytes must already be committed under CVF governance. Public code may accept
only a normalized grant path. It must derive all grant fields and artifacts
from `HEAD`, verify exact content hashes, and reject dirty-working-tree bytes.

An API key must never be reused as an owner-signing secret. Same-process code
with repository-write or process-environment control remains inside the trusted
operator boundary; remote/caller input remains outside it.

## Acceptance Criteria

- caller objects, copied handles, JSON, prototypes, proxies and alternate Git
  repositories cannot create an accepted owner;
- an eligible committed grant produces one opaque handle;
- every bound artifact is re-read from `HEAD` and matches its SHA-256 pin;
- work-order/capability versions and all constraint fields reconcile exactly;
- missing trace/receipt linkage fails closed;
- invocation and retry ceilings survive module/process reopen through SQLite;
- duplicate invocation IDs are rejected atomically;
- no raw secret is stored in grant, handle projection, DB or evidence output;
- F11 closes only after independent adversarial review.

## Decision / Baseline

`DISPATCH_READY` for the T2A no-commit implementation worker. The baseline
selects committed Git blobs as the authority source and private SQLite as the
replay-state owner. Any implementation that admits caller-authored grant data
is outside this baseline and must be rejected.

## Evidence / Verification

Dispatch evidence consists of checkpoint commit `f4b99100e`, the committed
review and worker return it contains, the checkpoint receipt, SHA-256-pinned
grant artifacts, source verification above and the pre-dispatch autorun gate.
Implementation and F11-closure evidence remain pending.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| prior T2A artifact paths | exact path checks before authoring found no existing T2A packet or grant | NEW_PATHS |
| existing owner registry | repository search found no production source capable of creating a genuine owner handle | SOURCE_GAP_CONFIRMED |
| existing durable store | Guard Contract SQLite audit owner exists but has no capability-grant/replay schema | ENRICH_EXISTING_PACKAGE |
| collision decision | T2A continues T2 and does not overwrite the committed blocked review | ADDITIVE_CONTINUATION |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T2A --title "Repository-Owned Capability Evidence Binding" --date 2026-08-13 --base f4b99100e8d5f84313ebe9b41d410dcbb8df831c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source rows, trust-root decision, scope, acceptance and claim boundary |
| checkerReadAheadConfirmation | applicable checker sources inspected before governed authoring |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defect count: 0.

Returned defects: NONE_RETURNED

Dispatch impact: independent probes remain mandatory because an empty resolver
result is not correctness evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation packet; no public-sync action or
artifact is authorized.

## Claim Boundary

This baseline authorizes a repository-owned, local T2 authority seam and
durable replay state. It makes no provider/live, external interception,
deployment, public or production-readiness claim.
