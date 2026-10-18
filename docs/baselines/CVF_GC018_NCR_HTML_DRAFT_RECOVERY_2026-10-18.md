# NCR HTML Draft Recovery - Source Design And Baseline

Memory class: governed-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-18
Batch ID: CVF-NCR-HTML-DRAFT-RECOVERY-20261018
Inspection base: db3d4058910a76662b0a31dfe579f49d98b62586
Commit mode: WORKER_MUST_NOT_COMMIT
rawMemoryReleased=false
providerExecutionAuthority: FORBIDDEN
Decision owner: LOCAL technical design; operator owns real-data/effect decisions

## Purpose

Implement the approved refresh/recovery design on the selected HTML consumer as source plus bounded local-synthetic tests. Recovery serves the exact explicitly saved draft and cannot generate another export. No current runtime recovery result is asserted.

## Scope / Target / Owner Boundary

Local Root accepts this locked design for source implementation, following the operator's approval of the reported recovery sequence on2026-10-18. Reuse the existing HTML artifacts domain and admin session gate. The read-only INTERNAL_AGENT aide supplied eight-file advice; Local reverified the selected interfaces. This is a new R1 recovery outcome, not another R2C actor, renamed retry or continuation of the frozen parent problem. Parent S14/Q05/R1F/R2C, SCECordinal2/counters2,0,2,0/freeze/prior7/LHW24 stay unchanged.

1. Explicit Save after a successful export snapshots the exact displayed submitted request and exact HTML string. Editing the form must not change that saved version. Saving uses a separate endpoint, never another export. A draft not successfully saved is not advertised as recoverable.
2. New snapshot payload repository is owned by the existing artifacts domain. Governance storage adapters forbid raw AI output; chat/session/execution history and MAO graph stores are not artifact payload owners. Do not write HTML there or invent an execution record. No B2 acceptance helper activation is selected.
3. The client assigns a canonical UUID versionId once per explicit Save action. POST /api/artifacts/drafts accepts only versionId, sourceRecordId, request (the existing exact seven-field ArtifactExportRequest), html, filename, generatedAt and buildNumber. Reject unknown keys, non-strings, invalid Unicode, limits and secret-like content using the seven SECRET_PATTERNS in the existing export route; copy that bounded pattern set into the new draft contract without changing the export route. Apply it to every submitted string, including HTML. Source record association is metadata from the saving client, never authoritative audit-event reproduction.
4. Server derives principal from requireAdminApiSession(request, resource, {allowBreakGlass:false}); require normal session mode, current unexpired expiresAt, bounded non-empty userId/orgId/teamId, and reject impersonation/realUserId/realRole contexts. Never accept an owner from request headers/body/query. Bind each snapshot to the complete principal tuple and sourceRecordId. Enforce owner/record joins for Save, exact GET and list; use opaque canonical IDs and hashed principal path components. Mutating requests require a non-empty Origin equal to new URL(request.url).origin and absent or same-origin Sec-Fetch-Site, following the exact sameOrigin policy in intent-spec-review-api.ts; refuse missing/foreign origin before storage.
5. Server computes SHA-256 over exact UTF-8 HTML bytes and the full seven-field submitted-request identity with fixed key order. No trim, newline/Unicode normalization or DOM reserialization. Stored schema cvf.htmlDraftSnapshot.v1 always declares CLIENT_SUBMITTED_UNVERIFIED and DRAFT_UNACCEPTED. It carries no accepted receipt decision or trusted verification results. A hash match proves byte consistency only.
6. One immutable exclusive-create JSON snapshot per version; return SAVED only after complete write and read-back identity validation. Same ID cannot overwrite even with different payload/owner. Incomplete, corrupt, unsupported-schema, expired or failed I/O is unavailable/unknown, never success. No repair, deletion, overwrite, lock, rollback or security mutation is authorized. Any ambiguous Save result keeps that exact known ID for read-only reconciliation; no blind write retry or new export.
7. GET /api/artifacts/drafts?id=versionId retrieves exact saved bytes after owner and integrity validation; GET with sourceRecordId lists at most8 matching metadata entries, newest first with stable tie break. GET never invokes export, receipt evaluation or provider work. Return Cache-Control:no-store; errors expose no raw HTML/request/path or other owner's existence.
8. Source profile is disabled by default. The only implemented enabling profile in this packet is explicitly configured local-synthetic with an absolute isolated root and non-production mode. Do not read or change an operator's environment, active store or settings. Tests inject fixture configuration and normal-session identities; the worker does not launch a server/browser or enable the feature on a running app. Future real-data/production enablement requires actual root/custody/retention/writer decisions. Fixture TTL24h and per-record encoded-size ceiling262144B are local test-profile design bounds, not an approved real-data retention policy. No automatic expiry deletion or global disk-quota guarantee.
9. Existing Work Transfer UI gains explicit Save/recover actions through a companion component, with Vietnamese/English copy per DESIGN.md. List and restoration bind the currently selected record, current session scope and requested version; selection changes and old async responses cannot replace another draft. Restored HTML is visibly a saved unverified draft and never acquires approval badges or live verification from cached metadata. Preserve sandbox preview, filename download and current/stale submitted-version semantics. Missing/expired/corrupt/unavailable versions show a clear state and no regeneration. No raw HTML in localStorage, audit, analytics or diagnostic logs.
10. Keep ArtifactExportPanel.tsx <=970 lines (currently941) by using the companion component and a small optional callback/slot for its exact displayed snapshot. Add separate recovery tests; do not edit its existing1163-line test. Keep new source files<=350 lines and new tests<=500 lines. If topology cannot meet that scope, return one consolidated issue before widening paths.

## Source Confidence And Reuse Decision

Source-backed selected interfaces only. The storage-adapter header forbids raw AI output and FileKeyValueAdapter.write can suppress errors. The existing session/history/MAO stores own other data contracts. A minimal payload repository inside the artifacts domain is therefore selected; it is not a second governance ledger. Real-data custody is not selected by the source profile. Browser storage or file reopen would not provide the server-bound recovery contract required here.

The existing FileIntentSpecAcceptanceStore is also scoped out: its concrete adapter validates SPEC_REVIEW_ONLY_NO_BUILD_AUTHORITY review candidates, uses intent-specific actor/schema/locking/security contracts and cannot accept HTML payloads through its current port. It is a source pattern, not an HTML storage owner. Future real-data security must reuse/admit the applicable private-profile controls; this source-only fixture profile makes no Windows ACL or power-loss guarantee.

## Evidence / Planned Verification

| Requirement | Required proof |
| --- | --- |
| REQ-CONTRACT | strict DTO, exact UTF8/input identity and untrusted draft semantics |
| REQ-STORE | real disposable-file byte round trip, exclusive collision/concurrency, tamper/partial/expired/I/O and principal joins |
| REQ-ROUTE | existing admin-session seam with normal principal, same-origin mutation, feature-off and synthetic-profile guards, read-only GET/list |
| REQ-UI | explicit Save of displayed version, actual callback composition, old-response/selection isolation, restore and stale behavior |
| REQ-NOREPLAY | export/receipt/provider call counts remain zero during Save, lookup, list, restore and failure reconciliation |
| REQ-RETURN | complete bound worker return, original outcomes, exact14 and pending Local probe |

## Decision / Baseline

SOURCE_DESIGN_ACCEPTED_BOUNDED. Worker release is conditional on committed bound pre-dispatch PASS and current authority matching this pair. The new implementation stage is source-only with synthetic fixture I/O; no running application profile, provider work, R2C replay, business acceptance, deletion or public/deploy effect is released.

## Epistemic Process Block

Expected Result / Prediction: explicit immutable Save plus owner-bound read separates recovery from generation. Evidence Comparison: current panel loses React state on reload; selected stores do not own raw HTML snapshots. Contradiction Or Gap Disposition: add the smallest payload repository inside the existing artifacts domain and reuse session auth. Claim Update: design accepted for bounded source implementation; actual behavior remains pending proof.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-HTML-DRAFT-RECOVERY-20261018 --title "NCR HTML Draft Recovery" --date 2026-10-18 --base db3d40589 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key ncr-html-draft-refresh-recovery --no-evidence-readiness-applicable --stdout` |
| generatedProfile | web-ui-dashboard |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: source-verified explicit Save contract; independent synthetic source lane; exact14 worker outputs; current9/6 release |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_core_guard_self_protection.py |
| docOnlyNewFields | DOC_ONLY_NEW: recovery DTO/profile/schema and future implementation paths defined below |
| claimBoundary | Authoring provenance and prospective source contract only. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| selected consumer | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx | WorkTransferPage | WorkTransferPage | current HTML consumer or storage/auth owner | ACCEPT |
| exact displayed request/result | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx | DisplayedResult; handleGenerate | DisplayedResult; handleGenerate | current HTML consumer or storage/auth owner | ACCEPT |
| export returns bytes without snapshot storage | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts | POST | POST | current HTML consumer or storage/auth owner | ACCEPT |
| session authentication | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/admin-session.ts | requireAdminApiSession | requireAdminApiSession | current HTML consumer or storage/auth owner | ACCEPT |
| adapter payload restriction | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts | module header; FileKeyValueAdapter.write | module header; FileKeyValueAdapter.write | current HTML consumer or storage/auth owner | ACCEPT |
| conversation store domain | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/session-store.ts | ChatSession; saveSession | ChatSession; saveSession | current HTML consumer or storage/auth owner | ACCEPT |
| browser execution history domain | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/store.ts | useExecutionStore | useExecutionStore | current HTML consumer or storage/auth owner | ACCEPT |
| MAO graph storage domain | EXISTS | EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts | MaoFileRunStore | MaoFileRunStore | current HTML consumer or storage/auth owner | ACCEPT |
| intent-specific immutable store | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-file-store.ts | FileIntentSpecAcceptanceStore | FileIntentSpecAcceptanceStore | intent-spec acceptance store | ACCEPT |
| same-origin mutation policy | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-review-api.ts | sameOrigin | sameOrigin | intent-spec review API | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=100.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`. Exit0, 27 returned; truncated=false. Retained `.cvf/runtime/ncr-html-draft-recovery-20261018/adif.json`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Dispatch impact: exact source/output union, raw-output restrictions, no provider-memory authority, truthful source-only proof and mandatory final-byte return gate.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_core_guard_self_protection.py |
| literalTokensReviewed | Dispatch Prompt Envelope; acceptance-ledger-json; exact manifest and gate graph; source versus DOC_ONLY_NEW; independent pending probe; internal coordination; private export |
| gateRunPurpose | confirmation/evidence of the prepared source packet, not first discovery |
| claimBoundary | Targeted operative predicates; no corpus-wide or runtime proof claim. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | current private consumer/source -> Local design -> scoped implementation and review |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | current NCR HTML artifacts consumer and Local design owner |
| Disposition | NOT_APPLICABLE_WITH_REASON: named internal source only |
| Claim boundary | Shared-workspace planning aide and implementation worker are INTERNAL_AGENT; Local decides. |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - targeted named-source design and code task; no full scan, inventory or all-files-read claim.

## Knowledge System Reconciliation

- Knowledge task class: NON_KNOWLEDGE_SOURCE_IMPLEMENTATION
- Source manifest: Source Verification Block in this artifact; targeted symbols only
- Source manifest hash: NOT_APPLICABLE; no corpus manifest or knowledge map produced
- Enumeration safety: filesystem-backed explicit named-file reads; no directory inventory
- Intake registry or ledger: no knowledge intake selected
- Authority assets: current pair, no knowledge-map authority
- Derived views: no knowledge view produced
- Semantic region ledger: no mapping regions in this task
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: NONE within zero-asset mapping scope
- Cross-region links: NONE
- Drift check: no knowledge map asserted
- Rebuildability check: source identity through git and packet; no map production
- Retrieval boundary: no retrieval-readiness assertion
- Adversarial verification: no map verification selected
- Knowledge-map verdict: PARTIAL

Reason: source task delivers no knowledge map.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: targeted new source implementation; no corpus reassessment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source implementation and synthetic proof; public sync is separate.

## Claim Boundary

Accepted source design only. Unit/fixture proof cannot establish real auth deployment, AI governance efficacy, live provider behavior, R1/R2 stage exit or R3/R4 durability readiness.
