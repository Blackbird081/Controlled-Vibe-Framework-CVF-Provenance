# CVF GC-018 - NIS T1B Private File Store

Memory class: governed-maintenance-baseline
docType: gc018
Status: APPROVED_FOR_LOCAL_IMPLEMENTATION
Date: 2026-10-05
Batch ID: CVF-NIS-T1B-C
baseHead: cc98c79657f86890624fc3a60becd0f2e8adfda3
providerExecutionAuthority: FORBIDDEN

## Purpose

Operator instruction on 2026-10-05: continue. Implement the concrete isolated
file adapter for the admitted NIS content-binding port. Local remains the sole
implementation/test actor; independent reviewer proof remains pending.

## Scope / Target / Owner Boundary

Two new source paths under EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/:

- intent-spec-file-store.ts
- intent-spec-file-store.test.ts

Admission artifact: this baseline. Ignored evidence/receipts under
.cvf/runtime/nis-t1b-c-20261005. Preserve all prior dirty paths, including A/B.
File operations during tests use synthetic briefs and a test-owned temporary
root only. No real-data path, API/UI integration, identity/account setup,
provider, dependency, deployment, commit or public sync. No governance adapter
reuse. CCMA/S05/C1/send/B2/Q001/Q004/P11/FLAL boundaries remain unchanged.

## Source / Predecessor Evidence

Predecessor admission:
docs/baselines/CVF_GC018_NIS_T1B_SERVER_ACCEPTANCE_CONTRACT_2026-10-05.md.
Existing byte/actor contracts control what can be stored. This new consumer
adapter has no default directory and is not automatically initialized.

## Source Verification Block

| Claimed item | Source file | Verified section | Disposition |
|---|---|---|---|
| Identity is owned by the request verifier | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-actor.ts | resolveIntentSpecActor; assertCurrentIntentSpecActor | ACCEPT |
| Store port requires owned actor/candidate and exact readback | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | IntentSpecAcceptanceStorePort; commitIntentSpecAcceptanceCandidate | ACCEPT |
| Source file structure and content admission | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts | prepareIntentSpecAcceptance | ACCEPT |
| Generic evidence adapters are not raw-brief stores | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts | Secret-safe | ACCEPT |

## Decision / Baseline / Proposed Tranche

Owner/route: existing NIS Web consumer, dedicated private artifact port.
Profile: one trusted host and an explicitly supplied existing private root.
Namespace is SHA-256 over user/org/team IDs; record ID is SHA-256 over exact
record bytes. No raw actor ID becomes a filesystem path. Only the root owner
may mutate this directory; hostile filesystem owners and permissions/DACL
enforcement are outside this profile. Mode bits are not Windows ACL proof.

Publish only after an exclusive temporary file is written and file-flushed.
Use a no-replace hard link to the final content-addressed filename, then
read back and verify it. If the filesystem does not support the operation,
fail closed; do not fall back to overwrite/rename or in-memory success.
No directory-flush or power-loss durability promise is made. Local restart
readability and exact content are the bounded test targets.

## Implementation Contract

1. Require a branded current actor and explicit absolute non-root directory;
   reject symlink/junction roots/namespaces and non-file committed records.
2. Validate every record against its filename hash, exact schema, source-file
   hash and existing source admission. Writes must bind the current actor;
   reads may return historical role metadata only within the same principal.
3. Stage each write in an exclusively created random temporary file, flush and
   close it before no-replace publication. Identical existing data is idempotent;
   corrupt/conflicting data is an error and cannot be overwritten.
4. Remove only the temporary file owned by that invocation; initialization
   failure must not delete somebody else's file. Never remove a committed
   record to manufacture rollback. Post-publication errors remain unconfirmed.
5. Readers ignore uncommitted temporary files; missing records return null,
   corruption/permission/I/O failures throw. Recheck actor lifetime after I/O.
6. Test real local filesystem roundtrip, new-instance reads, a second-process
   byte read, actor isolation, unsafe paths, concurrency and injected failures.
   Synthetic identity fixtures do not prove production login or authorization.

## Risk / Corrective Action

Elevated local filesystem publication. No ACL mutation or existing-record
rollback is authorized. Clean only writer-owned temporary files during normal
failure; interrupted writers may leave orphan temporary files which readers
ignore. No automatic scavenger or real-root cleanup is authorized.

Transaction proof owner:
docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md.
No new work order/delegation is created for this direct same-actor bounded
implementation. Its formal independent reviewer/security proof is not claimed
by local tests. Keep PENDING_REVIEWER_EXECUTION for any formal transaction
acceptance, and retain NO_DURABILITY_OR_BUILD_AUTHORITY in the existing result.
Concrete implementation/tests do not authorize production join or runtime use.

## Evidence / Verification Requirements

Pre-implementation admission before source edits. Focused new filesystem tests,
TypeScript and lint. Consume unchanged A/B evidence. Pin prior dirty paths and
final source/receipt bytes. Record capability limitations and retained failures.
Do not call a same-actor child-process read an independent reviewer probe.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - two named source paths, no repository-wide claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION - no external source acquisition or conversion.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - two named source paths; no repository-wide processing claim

## Epistemic Process Block

Expected Result / Prediction: only complete current-actor records become readable
under their exact content identity; publication/failure never overwrites records.
Evidence Comparison: pending local implementation tests.
Contradiction Or Gap Disposition: independent transaction/security proof, real
identity exercise, directory durability and production UI/API join remain open.
Claim Update: bounded local adapter implementation only; no complete T1B/S1.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_gc018_stop_boundary_semantics.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_high_risk_local_transaction_proof.py |
| literalTokensReviewed | Source Verification Block; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Returned defects: NONE_RETURNED; PENDING_REVIEWER_EXECUTION |
| gateRunPurpose | confirmation of direct bounded source authority before implementation; not first discovery |
| claimBoundary | same-actor local filesystem tests only; no formal independent transaction proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class reviewer --role reviewer --lifecycle-phase review --json`.
Returned defects: NONE_RETURNED.
Reuse the same role/task-class resolver evidence from 2026-10-05.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Concrete isolated adapter only. No real data, live authentication, power-loss
durability, independent reviewer proof, accepted-spec state or BUILD grant.
