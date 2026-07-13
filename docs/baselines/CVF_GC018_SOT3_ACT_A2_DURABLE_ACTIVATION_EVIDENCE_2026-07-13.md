# CVF GC-018 Baseline - SOT3 Activation A2 Durable Activation Evidence

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-13

Baseline ID: GC-018-SOT3-ACT-A2

dispatchBaseHead: `656c176a2`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Authorize one bounded A2 tranche that persists a durable, integrity-bound
record of each A1 SOT3 activation before provider prompt construction. The
record must support restart lookup and deterministic replay inspection without
storing raw knowledge content, prompts, provider output, or secrets.

## Target / Source

The target is the A1 knowledge-context activation seam in CVF Web. Current
runtime source, the SOT3 owner types, the A1 completion review, and the parent
activation roadmap control over chat or provider-local memory.

## Scope / Methodology

Add a dedicated local-file activation-evidence store, extend the A1 adapter to
return source-backed lifecycle traces, persist one request-level batch after
SOT3 evaluation and before prompt construction, and prove atomicity, duplicate
handling, restart lookup, corrupt-file preservation, and persistence-failure
behavior with deterministic local tests.

## Findings / Position

The A1 product path is wired and exposes layer IDs, but it does not retain the
full receipt, policy/rule, Flow scope, packet hash, or a durable replay record.
The generic file storage surfaces are not A2 owners: one writes directly and
can repair/reset corrupt state, while another catches persistence failure and
only warns. A2 therefore requires a focused store with explicit failure
propagation and no silent repair.

## Risk / Corrective Action

Risk is R2 because evidence persistence is inserted into provider-context
construction. Controls are an activation-specific schema, same-directory
temporary file plus atomic rename, integrity verification on read, serialized
process-local append, idempotent duplicate semantics, corrupt-byte
preservation, configuration-only rollback through `OFF`, and reviewer-owned
closure and commit.

## Decision / Baseline / Proposed Tranche

DISPATCH_READY: one no-commit A2 implementation. A3 live provider proof, A4
adverse-path live proof, A5 claim closure, public export, database/distributed
ledger work, production readiness, and user validation remain outside scope.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A1 implementation and review | `docs/reviews/CVF_SOT3_ACT_A1_SCOPED_KNOWLEDGE_CONTEXT_PRODUCT_ADAPTER_COMPLETION_2026-07-13.md`; material commit `149832b16` | A1 must carry its accepted bounded-pass disposition and `PRODUCT_PATH_WIRED_LOCAL` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md`; session-sync commit `656c176a2` | roadmap status must route next to fresh A2 packet authoring | ACCEPT |
| Session routing | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; generated aggregate at `656c176a2` | current mode and next allowed move must name A2 packet authoring only | ACCEPT |
| Operator checkpoint | operator instruction on 2026-07-13 | continue the next work order | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| A1 resolves SOT3 context before prompt construction | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | `resolveKnowledgeContext` evaluation and prompt blocks | `resolveKnowledgeContext` | execute knowledge-context helper | ACCEPT |
| Provider execution follows the knowledge helper | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | execute path | `executeAI` | execute route | ACCEPT |
| A1 computes the Refinery-owned packet hash | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | packet construction | `computeRefineryPacketHash` | SOT3 knowledge adapter | ACCEPT |
| A1 currently returns summarized layer identifiers | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | activation-result declaration | `Sot3KnowledgeActivationResult` | SOT3 knowledge adapter | ACCEPT |
| Kernel decision carries request, packet, policy, rule, result, reason, verification, and time fields | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/kernel-decision.ts` | `KernelDecision` declaration | `KernelDecision` | Truth Kernel decision contract | ACCEPT |
| Truth receipt carries decision binding, evidence, versions, predecessor, and receipt hash | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-receipt.ts` | `TruthReceipt` declaration | `TruthReceipt` | Truth Kernel receipt contract | ACCEPT |
| Truth reference binds receipt, scope, validity, version, and state | EXISTS | `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts` | `TruthReference` declaration | `TruthReference` | Truth Kernel reference contract | ACCEPT |
| Flow package owns recipient, role, task, phase, truth references, restrictions, routing, expiry, and acknowledgement | EXISTS | `EXTENSIONS/CVF_TRUTH_FLOW/src/types/distribution-package.ts` | `DistributionPackage` declaration | `DistributionPackage` | Truth Flow distribution contract | ACCEPT |
| Existing knowledge file store uses temporary write then rename | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `FileBackedKnowledgeStore._persist` | `_persist` | knowledge store | ACCEPT |
| Existing knowledge file store catches persistence errors and warns | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts` | `FileBackedKnowledgeStore._persist` error branch | `_persist` | knowledge store | REJECT |
| Generic event-list adapter writes its main file directly | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | `FileEventListAdapter.writeAll` | `writeAll` | generic storage adapter | REJECT |
| Generic event-list adapter may repair/reset corrupt state | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | read/initialization recovery branches | `FileEventListAdapter` | generic storage adapter | REJECT |
| Runtime evidence directory is ignored from Git | VALUE_SET | `.gitignore` | CVF runtime entries | `.cvf/runtime/` | repository ignore policy | ACCEPT |
| Existing route tests observe the provider prompt and call count | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.knowledge.test.ts` | mocked execute tests | `executeAIMock` | execute knowledge route test | ACCEPT |

REJECT rows reject direct reuse for A2 semantics; they do not declare the
existing owners defective for their original purposes.

## New Doc-Only Fields

These names are proposed by A2 and do not exist at dispatch time.

| Proposed field or symbol | Type | Required semantics |
|---|---|---|
| `CVF_SOT3_ACTIVATION_EVIDENCE_PATH` | `DOC_ONLY_NEW` | optional file path; default `.cvf/runtime/sot3-activation-evidence.json` |
| `cvf.sot3.activation-evidence.v1` | `DOC_ONLY_NEW` | versioned document schema for request-level activation batches |
| `Sot3KnowledgeLifecycleTrace` | `DOC_ONLY_NEW` | one source-backed trace per evaluated chunk from Source through Flow |
| `Sot3ActivationEvidenceRecord` | `DOC_ONLY_NEW` | request/actor scope, mode, result, traces, timestamps, diagnostic class, schema version, and integrity hash |
| `DUPLICATE_NOOP` | `DOC_ONLY_NEW` | same record identity and integrity hash already stored; no mutation |
| `SOT3_EVIDENCE_DUPLICATE_CONFLICT` | `DOC_ONLY_NEW` | same record identity with different integrity hash; reject without mutation |
| `SOT3_EVIDENCE_CORRUPT_STORE` | `DOC_ONLY_NEW` | main evidence file cannot be parsed or validated; preserve bytes and stop |
| `SOT3_EVIDENCE_PERSISTENCE_FAILED` | `DOC_ONLY_NEW` | temporary write or atomic replace failed and propagated to the activation caller |
| `EVIDENCE_PERSISTENCE_FAILED` | `DOC_ONLY_NEW` | A1 activation failure-stage extension used by route policy and audit |
| `SOT3_ACTIVATION_EVIDENCE_PERSISTED` | `DOC_ONLY_NEW` | secret-safe audit projection of persistence disposition and record identity |

## Acceptance Criteria

- One request-level evidence record contains actor and tenant scope, activation
  mode/outcome, timestamps, diagnostic class, schema version, integrity hash,
  and one lifecycle trace per evaluated chunk.
- Each trace uses actual owner outputs for source/collection/chunk identity,
  Refinery packet/hash, Kernel decision/receipt/reference and policy/rule
  versions, and Flow package/recipient/lifecycle/acknowledgement.
- No raw chunk content, prompt, provider output, API key, token, or secret is
  persisted or emitted in audit.
- Persistence is ordered after SOT3 evaluation and before prompt construction
  or provider execution.
- A same-identity/same-hash duplicate is an idempotent no-op; a same-identity
  different-hash duplicate is rejected without changing the main file.
- A fresh store instance can load and find a valid record after restart.
- Corrupt main bytes are preserved and cause a classified error; no automatic
  reset, overwrite, seed, or repair is allowed.
- Temporary write plus same-directory atomic rename preserves the prior valid
  main file on partial-write, write, or rename failure.
- `OFF` performs no SOT3 evidence write. `SHADOW` preserves its A1 downstream
  context contract while auditing persistence failure. `ENFORCE` persistence
  failure admits no knowledge block, while the existing request may continue
  once without knowledge under the A1 whole-request policy.
- Focused tests, existing knowledge tests, non-live suite, typecheck, build,
  file-size enforcement, and worker-return gate pass without external provider
  invocation.

## Evidence / Verification

Require schema and integrity fixtures; restart, duplicate, corrupt-file,
leftover-temp, and injected write/rename failure tests; multi-chunk trace
cardinality; mode/prompt/call-count/audit assertions; ordering evidence; diff,
status, and unchanged worker HEAD evidence.

## Stop Conditions

- durable evidence would require raw content, prompts, provider output, keys,
  or secrets;
- an owner field must be guessed rather than carried from an actual A1/SOT3
  output;
- atomic replace cannot preserve the prior valid main document;
- corrupt input is reset, overwritten, or silently repaired;
- A2 requires database, migration, distributed ledger, SOT3 owner-package
  mutation, external provider call, or a new whole-request denial policy;
- an allowed-scope repair cannot satisfy a mandatory checker without expansion.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021,
ADIF-0024, ADIF-0028.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Source Verification Block; New Doc-Only Fields; Dependency Release Evidence; ADIF Defect Registry Disclosure; Public Export Disposition |
| gateRunPurpose | confirmation and evidence after direct source and checker review; not first discovery |
| claimBoundary | dispatch baseline only; no A2 implementation, durable proof, or live proof |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-ACT-A2 --title "Durable Activation Evidence" --date 2026-07-13 --base 656c176a2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SOT3-ACT-A1 closed at 149832b16" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with source-verified evidence schema, atomicity, failure, mode, test, handoff, and claim contracts |
| checkerReadAheadConfirmation | dispatch, handoff, trace, public-export, and file-size guards |
| docOnlyNewFields | evidence path/schema, lifecycle trace, record, persistence dispositions, failure stage, and audit event listed above |
| claimBoundary | dispatch authoring provenance only |

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md applicability | N/A with reason: A2 changes server-side evidence persistence and tests only; no visible UI or frontend design |
| UI claim boundary | no visible, hosted, production, or live-data claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance A2 dispatch packet only.

## Claim Boundary

This baseline authorizes bounded local A2 implementation and deterministic
proof only. Successful closure may claim
`DURABLE_EVIDENCE_REPLAY_PROVEN_LOCAL`; it cannot claim live provider behavior,
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, production readiness, public availability,
distributed durability, or user validation.
