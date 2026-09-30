# CVF GC-018 Baseline - NCR HTML B2a Synthetic Acceptance Candidate

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2A-SYNTHETIC-CONTRACT

Dispatch base head: `f8790a475`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize an isolated, synthetic B2a contract candidate that identifies the exact UTF-8 HTML bytes of a submitted export and keeps receipt evidence separate from an artifact acceptance decision. This does not create an active accept path or durable artifact store.

## Source / Predecessor Evidence

The operator agreed on 2026-09-30 to single-host, one-writer design and synthetic proof first, with Profile A retained. The B2 audit at material `2364bfbaa` found no authorized exact-HTML acceptance owner. Existing Web SQLite code is a single-node design precedent only.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| B2 is conditional on Q001/Q004 and writer/profile | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D034, D037, Q001, Q004 | B2 | NCR roadmap | ACCEPT |
| Export route returns transient HTML and sourceHash covers source text only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | buildHtml and POST | html, sourceHash | HTML export route | ACCEPT |
| Receipt helper submits an excerpt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | fetchGovernanceReceipt | fetchGovernanceReceipt | Governance evaluation helper | ACCEPT |
| B1 binds displayed result to an attempt, without durability | `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_COMPLETION_2026-09-30.md` | Decision and Claim Boundary | B1 | Local review | ACCEPT |
| A local single-node SQLite implementation exists for another bounded owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | class declaration, constructor and create | PendingAgentExecutionSqliteStore | pending-execution owner, not HTML artifact owner | ACCEPT_BOUNDED |
| B2 owner audit rejects implementation dispatch under the prior authority | `docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md` | Decision / Disposition | REVIEW_COMPLETE_NO_DISPATCH | Local audit | ACCEPT; operator later approved only synthetic design/proof |

## Decision / Baseline / Proposed Tranche

B2a is a pure, unconnected candidate. The worker may define a typed artifact identity envelope and deterministic exact-byte SHA-256 helper, plus synthetic tests and a design contract. It must use the actual HTML string bytes supplied to the candidate, including generated timestamp and all rendered fields. Receipt attempt ID is supporting evidence, never acceptance. No real actor authorization, acceptance decision, persistence or route integration is claimed.

The future design contract proposes operator-only explicit acceptance, immutable version, a separate authoritative artifact store on one local host, single writer, commit-before-ack, readback/hash check, unknown-outcome reconciliation and recovery ownership. It must label those as proposed and leave backup/key custody, retention, RPO/RTO, real data, Profile B/C and pilot effect for operator decision.

## Scope / Target / Owner Boundary

Allowed worker paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts`; its adjacent `html-artifact-acceptance-candidate.test.ts`; `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; and `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md`. All are create paths. The worker must not import the candidate from a route, page or production composition root. Local owns review, commits and continuity.

## Acceptance Criteria

1. Distinct rendered HTML bytes produce distinct identity under tests covering same source text with changed title, boundary or timestamp; UTF-8/non-ASCII bytes are handled explicitly.
2. Repeated identical bytes produce one stable hash; a one-byte mutation fails verification.
3. Version/attempt and receipt identifiers remain distinct; a synthetic ALLOW receipt cannot set accepted state.
4. The reference contract states future actor, store, transaction, readback, retry/unknown and recovery interfaces as proposals with explicit unsolved operator choices.
5. Only the four allowed paths change; focused tests, TypeScript and worker-return fast gate pass without route, database, provider, network or real data access.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | isolated candidate helper and reference contract | synthetic identity only; no active accept effect | source rows above and pending tests | no active adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2a interface | no ingress, auth, raw data, receipt or mutation grant | NCR D037 and bounded packet scope | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, focused Vitest, TypeScript and worker-return fast gate. Reviewer verifies no active import path and independently checks one byte-identity negative case. Tests prove only the isolated candidate contract, not disk durability, backup recovery, browser UI or live governance behavior.

## Operator Checkpoints

Profile A remains. Operator retains designation of the actual accepting actor/account, source/instance and classification of real data, store location, writer/fencing model, backup location and key custody, retention/deletion, RPO/RTO, cost and pilot/live effect. A separate work order is required for durable store or active acceptance.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2-SYNTHETIC-CONTRACT --title "NCR HTML B2 Synthetic Acceptance Contract" --date 2026-09-30 --base f8790a475 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2a identity and design-only scope |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact four-path scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review |
| claimBoundary | Static gate PASS cannot prove B2 runtime behavior |

## Claim Boundary

This baseline authorizes an isolated synthetic identity candidate and design contract only. It does not accept HTML, persist bytes, grant production writer rights, close Q001/Q004, or authorize real data, provider/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
