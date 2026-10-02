# CVF GC-018 Baseline - NCR HTML B2 Durable Acceptance Design

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2-DESIGN

Dispatch base head: `61c774ef0b8e3db2b53b5283e4075a425532b52b`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; real effect owner: operator.

## Purpose

Authorize one selected-profile B2 documentation-only contract/design assignment, no implementation or experiment.

## Source / Predecessor Evidence

D070 and `docs/reviews/CVF_CVF_NCR_POST_B1_ROADMAP_CHECKPOINT_REASSESSMENT_2026-10-02.md` at 77bee1aba record delegated design direction; D071 binds this packet. B2a Part 2 remains proposal input, not implemented storage. Accepted transport/B1 evidence read-only and bounded.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Selected profile | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_POST_B1_ROADMAP_CHECKPOINT_REASSESSMENT_2026-10-02.md` | Design Profile Selection | DESIGN_DIRECTION_ONLY | Local | ACCEPT |
| B2a precedent | CONTRACT | `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` | Part 1; Part 2 | Part 2 | B2a | ACCEPT |
| Existing identity candidate | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | computeHtmlBytesIdentity; verifyHtmlArtifactCandidate | computeHtmlBytesIdentity; verifyHtmlArtifactCandidate | candidate helper | ACCEPT |
| Mutable generic I/O, read calls init | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | SQLiteKeyValueAdapter | SQLiteKeyValueAdapter | generic adapter | ACCEPT |
| Distinct v3 ledger owner | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v3.0_CORE_GIT_FOR_AI/artifact_ledger/artifact.ledger.ts` | ArtifactLedger | ArtifactLedger | v3 | ACCEPT |
| Governance-event storage | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py` | CREATE TABLE blocks; append_event | append_event | governance ledger | ACCEPT |
| Owner/storage gap | GOVERNED_REVIEW | `docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md` | Findings; Decision | Findings | B2 audit | ACCEPT |
| Design-only boundary | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D070/D071; Q001/Q004 | D070 | NCR | ACCEPT |

## Decision / Baseline / Proposed Tranche

After paired material/hash-bound continuity/bound release PASS, worker runs clean pre-implementation gate then creates three new design/evidence/return outputs. Local reviews design only; real account/data/path/backup/effect choices remain future prerequisites.

## Scope / Target / Owner Boundary

- `docs/reference/CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-html-b2-design-worker-evidence-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B2_DESIGN_WORKER_RETURN_2026-10-02.md`

Governing order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_2026-10-02.md`. Zero product paths, DB/server/browser/provider runs or worker commits.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source implementation packet with explicit path collision checks only; no corpus completeness or all-files-read claim. Existing source audit receipt retains its PARTIAL selected-section boundary.

## Integrated Design Admission

This assignment IS contract/design work, not product-edit admission. Start from selected-profile delta over B2a Part 2 and owner capability comparison. Produce consistent actor/identity/storage/recovery design plus planned cases. Mark schemas/interfaces PROPOSAL_NOT_IMPLEMENTED and every behavioral case NOT_EXECUTED_DESIGN_ONLY. No database or transaction experiment.

## Implementation Contract

Design outputs only. Required integrated contract:

1. Owner/overlap: compare B2a/B2b identity candidate, Web SQLite/file I/O adapters, v3 staging/ledger and governance-event SQLite. Name consumer, authority, lifetime, actual read/write semantics, identity/transaction/recovery capabilities, reusable part and missing delta with locators. Governance events are not artifact bytes. Dedicated-store proposal requires smallest owner-bound adaptation and future consumer rationale, never a repository-wide absence claim.
2. Actor/admission: authenticated operator explicitly decides on the exact displayed immutable version in its workspace. Bind server-established actor/role/scope to operation/version/bytes/freshness/permission; client-supplied role or receipt ALLOW never grants acceptance. Define unauthorized/missing actor, stale version, revoked/expired authority, edits after review and subsequent privilege changes. Refusal leaves draft; actual account/auth binding remains future prerequisite.
3. Identity/schema: exact canonical UTF-8 bytes, digest algorithm/length, artifact/version, workspace, acceptance operation, actor/decision/time and separate attempt/sourceHash/receipt evidence. No trim/re-render/derived Preview or Print digest. Content dedup is not an acceptance decision: same hash cannot erase actor/workspace/version distinctions. Conflict rules for same operation with different bytes/actor/workspace or corrupted same-hash row.
4. Store/writer: local single-host single-writer SQLite candidate, proposed atomic bytes/metadata boundary separate from event ledger. Logical constraints/interfaces, atomicity and durability assumptions, writer admission and rejected concurrent/foreign writer semantics; no DB/schema/lock created. Generic read invokes init and write upserts: proposed no-write reconciliation/readback must not init/create/migrate/repair a store; accepted bytes must not be overwritten. Generic I/O is not acceptance authority.
5. Protocol: validate actor/version/bytes, bind immutable operation intent, proposed transaction, commit then readback/hash/metadata verification before verified acknowledgment. Define before/during commit, after commit before readback/ack, failed/corrupt readback and lost-response outcomes. Never grant retry from failure or absence. Read-only classification binds correct store/workspace/operation/version/bytes and returns verified committed, definitively absent, corrupt/conflicting or UNKNOWN if unreadable/ambiguous. Missing/wrong/restored store absence is not a definitive negative. No query initializes/repairs storage.
6. Lifecycle: immutable historical acceptance versus effective current acceptance; append correction/new version, explicit revocation/expiry/deletion semantics, recovery owner and evidence. Older backup restore must not promote stale effective decisions. Actual data, backup location/key custody/retention/RPO/RTO/cost remain UNKNOWN future gates, not solved by this design.
7. Case plan: stable IDs, source requirement, precondition/input, injection stage, actor/operation/version/store tuple, expected record/ack/classification, independent future oracle/harness proposal. Cover valid accept; missing actor/forged scope; stale/superseded version; same-op same/different bytes; same-hash different actor/workspace; concurrent writer; refusal; failure before/during/after commit; lost ack; wrong/missing/unreadable store; corrupt readback; backup-restored absence/stale decision; revocation/expiry; no-write reconciliation. Every case NOT_EXECUTED_DESIGN_ONLY; a table is not test proof.
8. Future topology/admission: source-backed proposed implementation paths/functions and dependencies/schema/registry/generated/state/test consequences with rollback/deprecation proposal. Distinguish existing versus proposed paths. Separate synthetic implementation prerequisites from real account/data/path/backup/cost/effect prerequisites; no automatic future dispatch. Canonical exports, Preview/Print and accepted transport evidence unchanged.

Return one coherent design; conflicting identity/duplicate/authority/recovery rows cannot pass independently. No new runtime claim.

## Acceptance Criteria

- [ ] Exactly three new outputs from clean bound base; no source/store/historical-proof change.
- [ ] Source-bound owner comparison, including read-init/upsert gap.
- [ ] Consistent actor/version/bytes/workspace/operation and effective-versus-historical lifecycle contract.
- [ ] Proposed commit/readback/unknown-outcome protocol; no blind retry or false absence.
- [ ] Planned negative/fault cases and discriminating future oracles, all unexecuted.
- [ ] Proposed future topology and separate synthetic/real prerequisites.
- [ ] Full worker gate, actual worker ADIF query, COMPLETE_PENDING_REVIEW, no commit.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | B2 design owner | documentation only | profile/source evidence | no new runtime | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none opened | no ingress/effect grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2-DESIGN --title "NCR HTML B2 Durable Acceptance Design" --date 2026-10-02 --base 61c774ef0 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-html-b2-durable-acceptance-design --stdout` |
| generatedProfile | generic-worker-dispatch no-commit profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | selected profile, source read-init/upsert gap, design/case contract and three outputs |
| checkerReadAheadConfirmation | dispatch/release/ledger/closeability/envelope/high-risk/probe/semantic literals read |
| docOnlyNewFields | N/A with reason: existing schemas, task design fields only |
| claimBoundary | no implementation/runtime proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove durable acceptance/runtime truth |

## Current Runtime Freshness Verification

No runtime proof. Current generic SQLite read invokes init and write upserts, neither an immutable acceptance nor no-write recovery guarantee. Existing B2a identity and B2b-B2f transport remain bounded evidence. Refresh source hashes/locators without rerunning accepted browser proof.

## Evidence Requirements

Capture clean executionBaseHead/status; selected-region source manifest/hashes/locators, owner dispositions/gaps, decision rationale, case coverage with every status NOT_EXECUTED_DESIGN_ONLY, static commands/exit receipts, actual worker_execution/worker/worker-return ADIF query and exact diff. If asserting corpus processing use selected-depth PARTIAL/reconciliation, never all-files-read. No screenshot/browser/DB/transaction or real account/data evidence.

## Verification Commands

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json
git diff --check
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_2026-10-02.md
```

Source/document consistency only. No Vitest/Playwright/SQLite/HTTP/provider run or dependency install. Existing runtime evidence consumed within its own limits.

## Claim Boundary

Documentation-only proposed B2 design, no implemented owner/store/schema/admission, real account/data/artifact decision, new runtime/provider proof, durable acceptance, Q001/Q004/R0 exit or public/deploy claim. Cases unexecuted; reviewed design does not authorize implementation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
