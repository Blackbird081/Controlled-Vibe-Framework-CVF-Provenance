# CVF GC-018 - NIS T1B Server Acceptance Contract

Memory class: governed-maintenance-baseline
docType: gc018
Status: APPROVED_FOR_LOCAL_IMPLEMENTATION
Date: 2026-10-05
Batch ID: CVF-NIS-T1B-B
baseHead: cc98c79657f86890624fc3a60becd0f2e8adfda3
providerExecutionAuthority: FORBIDDEN

## Purpose

Operator instruction on 2026-10-05: continue. Build the missing server-side
identity/content/store-readback contract after the portable T1B-A candidate.
Local implements and verifies directly. Existing T1B-A work remains uncommitted
and must be preserved. This tranche does not close full T1B or S1.

## Scope / Target / Owner Boundary

Four new files under EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/:

- intent-spec-actor.ts
- intent-spec-actor.test.ts
- intent-spec-acceptance.ts
- intent-spec-acceptance.test.ts

Admission artifact: this baseline. Receipts/evidence under
.cvf/runtime/nis-t1b-b-20261005. Preserve all existing dirty paths, including
T1B-A. No existing authentication policy, API route, UI or storage adapter edit.
No filesystem transaction, persistence backend, account configuration, runtime
server, provider, migration, dependency installation, commit or public sync.
CCMA, S05/C1/send/B2, Q001/Q004, P11 and FLAL T4/T5 remain parked.

## Source / Predecessor Evidence

Reuse docs/baselines/CVF_GC018_NIS_T1B_PORTABLE_REVIEW_BINDING_2026-10-05.md
and the existing Auth.js session owner. Do not promote the portable name into
an authenticated actor. Current session authority pair retains terminal FR2
history only; new NIS authority is the operator instruction plus these baselines.

## Source Verification Block

| Claimed item | Source file | Verified section | Disposition |
|---|---|---|---|
| Existing request-bound Auth.js identity | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts | verifySessionCookie; resolveBaseSessionFromRequest | ACCEPT |
| Non-development OAuth binding and fail-closed configuration | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts | validateAuthEnvironmentInvariants; signIn; jwt | ACCEPT |
| Legacy cookie helper has fallback secret; do not select | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/auth.ts | FALLBACK_SECRET; getSecret | ACCEPT |
| Portable candidate exact file layout and hash | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-confirmation.ts | createSpecConfirmationCandidate | ACCEPT |
| Six decisions and current draft renderer | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | INTENT_REVIEW_QUESTIONS; buildReviewedDraftPacket | ACCEPT |
| Durable evidence adapter excludes raw briefs | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts | Secret-safe | ACCEPT |

## Decision / Baseline / Proposed Tranche

Owner/route: enrich the existing Web app-builder consumer through a server-only
contract, with Auth.js as identity owner. Actor comes only from the existing
request verifier; reject absent/expired/unknown identities, viewer role and
impersonation. Preserve a local-test assurance label for development fixtures.
Content comes from the exact candidate bytes, strictly validated and rehashed.
Storage port requires create-if-absent then exact-byte readback before returning
a bounded readback result. A supplied port is not evidence of durability.

Proposed persistence profile for later admission: one host, private user-owned
immutable files, isolated from governance-event stores. No actual directory,
real data, writer, recovery promise or production configuration is selected
or enabled here. A concrete backend needs its own failure/recovery proof;
high-risk transactions route through
docs/reference/CVF_HIGH_RISK_LOCAL_TRANSACTION_PROOF_STANDARD_2026-09-22.md.
Do not bypass its independent-probe obligations by calling port tests durable.

## Implementation Contract

1. Obtain request-bound actor identity, capture an owned immutable context,
   and recheck its lifetime before preparing and completing a commit attempt.
   Client actor fields, plain objects and impersonated sessions cannot qualify.
2. Accept only bounded UTF-8 canonical candidate bytes. Reject malformed JSON,
   duplicate/extra fields, unknown schema/scope, nonfinite revisions, stale or
   unresolved decisions, inconsistent source fields, draft mismatch and hashes.
   A self-consistent hash does not bypass content validation.
3. Bind exact source-file SHA-256, authenticated-owner actor identity and server
   preparation time into an immutable candidate with deterministic byte identity.
   Keep the self-declared name as an annotation, not actor authority.
4. Commit port errors, absent/different readback and expiry after I/O must fail
   closed. Never synthesize success from an in-memory fallback or hash supplied
   by a caller. Copy all arrays before giving them to or receiving them from ports.
5. Return STORE_PORT_READBACK_VERIFIED only for a matching result, with explicit
   NO_DURABILITY_OR_BUILD_AUTHORITY claim boundary. No accepted-spec state yet.
6. Tests use synthetic identities and injected in-memory ports; they prove
   contract behavior only, not OAuth liveness, filesystem durability or AI governance.

## Risk / Corrective Action

An I/O error can occur after an adapter wrote bytes. Report unconfirmed rather
than inventing rollback or approval. Port-only proof cannot establish atomic
publication, restart recovery, cross-process writer exclusion or power-loss
durability. Keep concrete store, authenticated operator exercise and UI join
pending until separately admitted. No raw brief enters governance adapters.

## Evidence / Verification Requirements

Pre-implementation gate before source edits. Focused adversarial parser,
identity provenance, lifetime, actor ownership, failed write/read and exact
readback tests; typecheck and lint new files. Consume T1B-A evidence without
rerunning its unchanged UI implementation. Pin all prior dirty paths and final
source bytes. No live/provider proof and no committed closure claim.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - named local contract scope, no repository-wide claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION - no external payload acquisition or conversion.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - four named source files; no repository-wide processing claim

## Epistemic Process Block

Expected Result / Prediction: forged/stale contexts or altered files and failed
ports cannot return a successful current content-binding result.
Evidence Comparison: pending implementation checks.
Contradiction Or Gap Disposition: concrete store and live identity proof remain open.
Claim Update: admitted contract slice only, no completed T1B/S1 claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_gc018_stop_boundary_semantics.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py |
| literalTokensReviewed | Source Verification Block; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of bounded source authority before implementation; not first discovery |
| claimBoundary | server contract tests only; no actual persistence or authenticated operator exercise |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class reviewer --role reviewer --lifecycle-phase review --json`.
Returned defects: NONE_RETURNED.
Reuse the same task-class resolver evidence collected on 2026-10-05.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

One Local actor; unconnected server contract only. No independent review,
authenticated live exercise, durable acceptance, release or BUILD permission.
