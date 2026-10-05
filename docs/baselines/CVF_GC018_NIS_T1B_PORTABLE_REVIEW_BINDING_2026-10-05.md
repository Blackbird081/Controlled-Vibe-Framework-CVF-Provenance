# CVF GC-018 - NIS T1B Portable Review Binding

Memory class: governed-maintenance-baseline
docType: gc018
Status: APPROVED_FOR_LOCAL_IMPLEMENTATION
Date: 2026-10-05
Batch ID: CVF-NIS-T1B-A
baseHead: bd47968b316744edd55e6f89cc4f9f6d1913e2b3
providerExecutionAuthority: FORBIDDEN

## Purpose

Operator instruction on 2026-10-05: "commit. tiep". After the T1A material
commit, continue the content-confirmation dependency through a bounded portable
review-binding candidate. Local owns source selection, implementation and
verification directly; no independent reviewer identity is claimed.

## Scope / Target / Owner Boundary

Use the existing app-builder review/export surface. T1B-A produces a portable
file candidate binding exact review state, current rendered draft, language,
self-declared reviewer name and timestamp. Re-reading a selected file checks
it against the exact candidate still held by this consumer. Download initiation
is not a saved-file receipt. Matching file readback is not server durability,
authenticated acceptance, semantic completeness or build authorization.

Allowed source paths, prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/:

- lib/intent-spec-confirmation.ts
- lib/intent-spec-confirmation.test.ts
- components/IntentSpecConfirmation.tsx
- components/IntentSpecConfirmation.test.tsx
- components/IntentSpecReview.tsx

Allowed admission artifact: this baseline. Ignored evidence belongs under
.cvf/runtime/nis-t1b-20261005. Preserve the nine prior dirty paths. No API,
backend store, adapter, dependency, provider, deployment or public-sync change.
CCMA, S05/C1/send/B2, Q001/Q004, P11 and FLAL T4/T5 remain parked.

## Source / Predecessor Evidence

NIS-T1A material commit bd47968b316744edd55e6f89cc4f9f6d1913e2b3;
docs/baselines/CVF_GC018_NIS_T1A_INTENT_SPEC_REVIEW_2026-10-05.md.
Current roadmap owner remains
docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md.
This is a bounded dependency slice, not activation of stopped NCR lanes.

## Source Verification Block

| Claimed item | Source file | Verified section | Disposition |
|---|---|---|---|
| Review revision and pending decisions | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review.ts | IntentSpecReviewState; buildReviewedDraftPacket | ACCEPT |
| Existing consumer insertion point | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/IntentSpecReview.tsx | IntentSpecReview | ACCEPT |
| Chat persistence is not exact spec acceptance | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/session-store.ts | saveSession; loadSession | ACCEPT |
| Approval store is execution-oriented and suppresses persistence failures | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts | persist; set | ACCEPT |
| Existing durable adapters forbid raw prompts/private memory payloads | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts | Claim boundary; Secret-safe | ACCEPT |
| HTML helper uses Node crypto and belongs to stopped HTML scope | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts | Claim boundary; sha256Hex | ACCEPT |
| Web design owner | DESIGN.md (canonical contract) | Accessibility and Language | ACCEPT |

## Decision / Baseline / Proposed Tranche

Owner/route: ENRICH_EXISTING Web app-builder consumer. Do not route raw spec
content into governance event adapters or execution approvals. Browser-native
Web Crypto hashes UTF-8 bytes without a new package or a stopped HTML import.
Use a user-managed portable file, no server persistence profile yet. Exact
content binding is useful before choosing authenticated acceptance storage;
it does not substitute for that choice. Reviewer identity is self-declared.

## Implementation Contract

1. Only a current acknowledged review with no pending items can create a
   confirmation candidate; require an explicit nonempty reviewer name.
2. Capture an owned immutable snapshot before asynchronous hashing. Bind
   all review state, exact draft, language, reviewer and timestamp. Never
   trust a caller-supplied content hash or a matching revision number alone.
3. Show and export the candidate only for the exact current snapshot. Edits,
   language or reviewer changes invalidate it immediately, including when
   hashing or file readback is still in flight. Failed work stays failed.
4. JSON file readback must match the exact candidate bytes; alteration,
   another candidate and failed reads cannot become a successful receipt.
   Cap file size before reading. No imported instructions or state adoption.
5. Label download requested separately from file readback verified. Losing
   the session loses the local expected binding; no reload restoration,
   signatures, authenticated actor or server commit/readback claim.
6. Tests assert pure binding and UI interaction only, not AI governance.

## Risk / Corrective Action

Files contain the user's brief and answers. The user deliberately downloads
or selects the file; do not write it silently to a shared backend. Content
hashes detect mismatches against the current expected bytes, not forgery by
a malicious reviewer. Full T1B still needs an authenticated actor and a
selected fail-closed store/recovery profile before durable acceptance.

## Evidence / Verification Requirements

Run pre-implementation admission before source edits, then focused positive,
mutation, stale async, malformed-file and failure tests, TypeScript and new
file lint. Consume T1A evidence; rerun its UI tests only because its panel
changes. Record current source hashes and preserve prior dirty-path hashes.
No live provider call, runtime server or external persistence proof authorized.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - named consumer slice; no repository-wide conclusion.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION - no upstream code or template payload copied.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - five named source paths; no complete scan claim

## Epistemic Process Block

Expected Result / Prediction: exact current candidate survives file roundtrip;
any edit or mismatched readback remains unconfirmed.
Evidence Comparison: pending implementation verification.
Contradiction Or Gap Disposition: authenticated durable acceptance remains open.
Claim Update: admitted bounded candidate slice only; no complete S1 claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_baseline_update_compat.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_gc018_stop_boundary_semantics.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_agent_packet_authority_and_encoding.py |
| literalTokensReviewed | Source Verification Block; Text Encoding Exception; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source authority and admission before edits; not first discovery |
| claimBoundary | exact portable candidate and current-session file readback only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python -B governance/compat/run_adif_defect_resolver.py --task-class reviewer --role reviewer --lifecycle-phase review --json`.
Returned defects: NONE_RETURNED.
Consume the same actor/task-class resolver evidence already collected on
2026-10-05; no new external/reviewer identity or task-class claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T1B-A only. No durable acceptance, authenticated reviewer, server commit,
semantic completeness, independent review, provider/live or build claim.
