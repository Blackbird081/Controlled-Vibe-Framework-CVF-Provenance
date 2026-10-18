# NCR HTML Draft Recovery Browser - Source Design And Baseline

Memory class: governed-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-18
Batch ID: CVF-NCR-HTML-DRAFT-RECOVERY-BROWSER-20261018
Inspection base: 74d355684ac141b3142811aeaab0dc452d0dd5a4
Commit mode: WORKER_MUST_NOT_COMMIT
rawMemoryReleased=false
providerExecutionAuthority: FORBIDDEN
Decision owner: LOCAL technical design; operator owns real-data/effect decisions

## Purpose

Deliver the next bounded app/browser recovery contribution with real Chromium and isolated synthetic HTTP/file behavior. Production and real-data activation remain OFF.

## Scope / Target / Owner Boundary

Local admits one finite receiving outcome: real Chromium uses the actual Work Transfer page and local export/draft HTTP routes to Save, refresh and recover the exact unverified HTML version. This continues the accepted recovery source at b75bf181b; it is not a R2C actor, retry, engine campaign or parent-counter reset. Operator continuation and standing orchestration authority cover source, isolated local synthetic app effects and review; actual-data/provider/public effects remain parked.

1. Add one server-only local-synthetic resolver in the existing artifacts domain. Actual draft GET/POST use its explicit profile; no config and NODE_ENV=production always remain OFF. Require explicit synthetic selection, absolute fresh owned root and an exclusive fixture marker (schema/version, synthetic-only, run identity); reject malformed/missing/unsafe marker/root. No arbitrary caller body/header grants a profile. Restrict enabled app profile to the declared synthetic record-ID prefix. Existing injected unit-test seam remains separate. Do not introduce a real-data profile or activation UI.
2. Preserve strict snapshot bytes/hash/schema, normal requireAdminApiSession with break-glass false, complete owner/record/version joins, same-origin mutation, no-store and CLIENT_SUBMITTED_UNVERIFIED/DRAFT_UNACCEPTED. Source wiring must not promote a draft or cached receipt. Leave store, contract, panel and companion implementation unchanged unless an actual blocker is consolidated to Local.
3. Use installed Playwright Chromium and the actual Next app, current WorkTransferPage, ArtifactExportPanel, HtmlDraftRecovery, normal local_mock session and real local export/draft handlers. Intercept only synthetic audit GET fixtures and explicitly declared fault injection (abort/delay draft traffic). No fake export result, fake Save success, forged browser recovery response, auth mock, provider/model call or governance-evaluate dispatch. This is mechanical UI/transport/persistence proof, not AI-governance efficacy or business acceptance.
4. One dedicated finite runner/config/preload owns a fresh loopback localhost:3033 server, browser context, nonce/root/dist/logs and synthetic file-adapter paths. Require unused port and no server reuse. Run direct installed Next/Playwright binaries; no npm predev/prebuild, dependency install or generic live config. Start child with an explicit safe environment allowlist (never spread inherited env), fixture-only local auth material, empty NEXTAUTH_URL and matching loopback AUTH_URL/baseURL. Prevent loading operator .env files before Next initialization; source-verify/intercept Next env loading plus deny private .env reads. Do not print/read operator credential values. Unit-proof this boundary before app startup.
5. Enforce loopback-only network in Node server and Chromium; block governance-evaluate before dispatch and record attempts without tokens/headers/query/body. Block all external traffic, including passive fonts; distinguish blocked attempts from successful network. Browser stores/settings/fixtures belong to the fresh context only. Audit, policy snapshots and every touched server-side store must point at owned synthetic roots; no Redis, existing SQLite or private store fallback. Read the actual auth/storage/config owners before first edit.
6. Preflight before Build/Save verifies profile sentinel/root, default/prod OFF unit tests, final source/config/preload/browser hashes, sanitized child environment, active post-init fence, actual normal unexpired session, owned process/port, and zero evaluate/provider dispatch. Freeze a source/run manifest before first browser effect; record actual startup and artifact outcomes, not assumed readiness. Do not bind a packet to its own future hash.
7. Real journey: select synthetic audit A, edit recognizable Unicode/CRLF input, Build once, record request and raw response, explicitly Save, capture version ID, reload, reselect A, list/recover that ID, compare exact UTF8 HTML bytes/hash with saved file/read response/download. Recovery reads must add zero export/provider/evaluate calls; restored UI is visibly unverified/unaccepted and sandboxed. Current/stale submitted-version semantics stay intact.
8. In the same finite journey test a failed/delayed draft read without regeneration, session logout/login or switch with stale response suppression/owner denial, and one ambiguous Save response after the real server received it. Keep its exact ID, block duplicate POST and reconcile by real GET. At most2 explicit Builds and2 Save attempts per run; no blind retry. Do not claim ambiguous ID survival across refresh: that ID is currently memory-only; successful saved versions recover by record list.
9. Record each original failure, exact argv/exits/durations, request method/status/counts, source/binary/preload pins, marker/run identity, synthetic output sizes/hashes and positive process/port teardown. Preserve raw fixture HTML/download/response and logs under the run root; never persist real cookies, auth headers or provider bodies. Do not use trace/video capture that records tokens. Stop on fence/unknown ownership failure, do not target unrelated processes. Retain fixture/build directories; no recursive deletion is authorized.
10. Fresh unique NEXT_DIST_DIR is an owned ignored build directory. Before server start capture exact tsconfig.json and next-env.d.ts bytes/hashes; the runner may restore only these two verified Next-generated transient changes after owned server teardown, restoring the exact captured preimages. Detect other tracked drift and return it; never blanket git restore. All source/test final changes are exact12 below; those two transient paths must be unchanged at return.
11. One worker90min including startup/edit/unit/type/lint/browser/gates/return; <=4 focused unit starts,2 tsc,2 lint,3 full-return gate attempts and2 browser runner starts. Browser runner has <=15min hard deadline including server startup/teardown, retries=0 and one Chromium worker. A second run requires a named diagnosed failure/information gain inside the same ceiling; never replay ambiguous state in the same root. Raw output <=256MiB plus owned build output<=1GiB per run; fixtures<=32 snapshots/8MiB. Root review target10min, ceiling30min including one distinct browser probe (one fresh runner/context/root, <=1 Build/Save), no broad duplicate suite. No old runtime cap/deadline transfer.
12. Keep new source<=350 lines/tests<=500 (runner<=450). Source/helper/test topology is exact and includes independent harness tests. Produce one consolidated blocker before a new file/path/effect. Worker may resolve ordinary mechanical choices without questions, but cannot widen authority, stage/commit, launch another agent or claim closure. Local owns final technical disposition and metadata.

## Source Confidence And Reuse Decision

Reuse the accepted HTML artifact payload owner and current real Work Transfer/export path. The current draft entrypoint calls the factory without a profile and is OFF; profile wiring is the concrete current source gap. Reuse existing browser login/audit fixture patterns, not old effect grants. The old browser fence binds a different persistent-profile actor and does not qualify this server/network/environment boundary. No alternate Vite/proxy runtime or parallel ledger is selected.

## Evidence / Planned Verification

| Requirement | Required proof |
|---|---|
| REQ-PROFILE | explicit nonproduction synthetic profile, sentinel/prefix, actual route join, default/prod OFF |
| REQ-ISOLATION | allowlisted child, no .env/private stores/network, pure boundary proof, owned teardown/restore |
| REQ-JOURNEY | real app/export/Save/refresh/exact bytes and fault/session/unknown-state behavior |
| REQ-NOREPLAY | actual request counts and no provider/evaluate dispatch on recovery |
| REQ-RETURN | complete bound evidence, original outcomes, exact12 and no remaining transient/process drift |

## Decision / Baseline

DESIGN_ACCEPTED_BOUNDED. One source implementation plus isolated synthetic app/browser proof is admitted only after this pair is committed, current continuity is bound and pre-dispatch passes. This grants no provider/live, real-data, deletion, production, R2C replay or public/deploy effect.

## Epistemic Process Block

Expected Result / Prediction: explicit profile wiring should compose accepted snapshot semantics with actual Chromium reload recovery. Evidence Comparison: current route is OFF and old browser clears unsaved result; source-only fixtures do not prove app behavior. Contradiction Or Gap Disposition: one narrow nonproduction synthetic join and finite actual-app proof, no alternate runtime or ledger. Claim Update: design admitted; browser outcome remains pending.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-HTML-DRAFT-RECOVERY-BROWSER-20261018 --title "NCR HTML Draft Recovery Browser" --date 2026-10-18 --base 74d355684 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key ncr-html-draft-recovery-app-browser --no-evidence-readiness-applicable --stdout` |
| generatedProfile | web-ui-dashboard |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: current real-app profile gap, finite isolated browser proof, exact12 worker and9/6 release |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_core_guard_self_protection.py |
| docOnlyNewFields | DOC_ONLY_NEW: recovery DTO/profile/schema and future implementation paths defined below |
| claimBoundary | Authoring provenance and prospective source contract only. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-recovery-api.ts | draftRouteHandlers; normalPrincipal | draftRouteHandlers; normalPrincipal | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/drafts/route.ts | GET; POST | GET; POST | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlDraftRecovery.tsx | HtmlDraftRecovery | HtmlDraftRecovery | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/ncr-work-transfer-browser.spec.ts | preflight; Work Transfer selection | preflight; Work Transfer selection | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts | login; loginAs | login; loginAs | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/admin-session.ts | requireAdminApiSession | requireAdminApiSession | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts | SessionCookie; verifySessionCookie | SessionCookie; verifySessionCookie | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts | auth; authSecret | auth; authSecret | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts | buildEventListAdapter; buildKeyValueAdapter | buildEventListAdapter; buildKeyValueAdapter | current recovery/auth/browser/config owner | ACCEPT |
| selected existing owner | EXISTS | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts | nextConfig | nextConfig | current recovery/auth/browser/config owner | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=100.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`. Exit0, 27 returned; truncated=false. Retained `.cvf/runtime/ncr-html-draft-recovery-browser-20261018/adif.json`.

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

Accepted design only until actual proof. Mechanical app/browser transport and synthetic file identity do not prove AI governance efficacy, deployed real-data security, R1/R2 stage exit or R3/R4 durability.

