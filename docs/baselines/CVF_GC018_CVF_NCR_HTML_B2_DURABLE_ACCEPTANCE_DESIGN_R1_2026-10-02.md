# CVF GC-018 Baseline - NCR HTML B2 Durable Acceptance Design R1

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2-DESIGN-R1

Dispatch base head: `17ae5b9586ee1fdd0fe6a73d0f37b4ab4419f8a2`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; real effect owner: operator.

## Purpose

Authorize one consolidated documentation-only rework of the unratified R0 B2 design. Resolve six dependent findings in the existing B2_ACCEPTANCE_DESIGN_UNSPECIFIED cluster; no implementation or behavioral experiment.

## Source / Predecessor Evidence

R0 at execution base `17ae5b9586ee1fdd0fe6a73d0f37b4ab4419f8a2` is unratified. `docs/reviews/CVF_CVF_NCR_HTML_B2_DESIGN_R0_LOCAL_REVIEW_2026-10-02.md` SHA-256 `acd6c094fce6f7f83a11fe92c6877dfc93353c62c9a921c16bf39699d66e1d0b` records structural PASS, thirteen matching source hashes and F01-F06 semantic findings. D072 authorizes one documentation-only R1 within selected D070 direction. R0 candidate contents are preserved in committed dispatch-base history; no design acceptance follows from recording them.

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
| Design-only boundary | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D070/D072; Q001/Q004 | D070 | NCR | ACCEPT |

## Decision / Baseline / Proposed Tranche

After paired material/hash-bound continuity/bound release PASS, worker runs clean pre-implementation gate then revises the three existing candidate outputs. Resolve the integrated six-finding set, not isolated wording. Local reviews proposed design only; all real-effect decisions remain future prerequisites.

## Scope / Target / Owner Boundary

- `docs/reference/CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-html-b2-design-worker-evidence-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B2_DESIGN_WORKER_RETURN_2026-10-02.md`

Governing order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_R1_2026-10-02.md`. Zero product paths, DB/server/browser/provider runs or worker commits.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source implementation packet with explicit path collision checks only; no corpus completeness or all-files-read claim. Existing source audit receipt retains its PARTIAL selected-section boundary.

## Integrated Design Admission

This assignment IS contract/design work, not product-edit admission. Start from selected-profile delta over B2a Part 2 and owner capability comparison. Produce consistent actor/identity/storage/recovery design plus planned cases. Mark schemas/interfaces PROPOSAL_NOT_IMPLEMENTED and every behavioral case NOT_EXECUTED_DESIGN_ONLY. No database or transaction experiment.

## Implementation Contract

Repair B2D-F01 through B2D-F06 from `docs/reviews/CVF_CVF_NCR_HTML_B2_DESIGN_R0_LOCAL_REVIEW_2026-10-02.md` as one coherent design/case-plan revision. Preserve original items 1-8, selected profile and named-owner reuse; the finding set adds no runtime/effect authority.

1. F01: consistent metadata mutation/generation design versus immutable bytes/decisions; commit, takeover, restore and rollback constraints.
2. F02: total operation state machine including attempts without decisions, conflicts in every state, terminal aborted/fenced replay and explicit new-operation policy; shared verified blob reuse without duplicate INSERT.
3. F03: lineage-head-first effective rule without fallback; basedOnDecisionId when head is ineffective; multi-version revocation/expiry/correction cases.
4. F04: proposed writer lifetime admission, crash/release/takeover/epoch protocol, including a second same-epoch process after the first commits. Keep the selected single-writer direction; no lock/runtime implementation.
5. F05: witness freshness contract covering acceptance, lifecycle, epoch and restore transitions; fail-closed current absence/effectiveness without required freshness evidence; silent same-store-id restore with lost decision/revocation/fencing history. Witness implementation/custody remain future gates.
6. F06: pre-write versus post-intent refusal effects; ALREADY_EFFECTIVE information versus exact actor/operation acceptance; another actor's original decision cannot acknowledge the submitted intent.

Provide a finding-to-design-to-case matrix for all six IDs. Every case NOT_EXECUTED_DESIGN_ONLY; static findings resolution PASS_STATIC_ONLY at most. Do not turn a coverage count or required PASS_TARGETED_DEFECT_CLASS token into behavioral proof. Unknown accounts/roles/workspace/store/key/backup/retention/RPO/RTO/cost stay unknown; synthetic witness assumptions must be labelled, not deployed.

No source, database, schema, lock, witness, server, browser, provider or real effect. No new worker output path. Current R0 snapshots are retained in the committed dispatch base as unratified evidence; revision of the same three candidate outputs is explicitly allowed by R1.

## Acceptance Criteria

- [ ] Revise exactly the three existing worker outputs from clean released R1 base; no product/runtime/effect or worker commit.
- [ ] F01-F06 integrated corrections and finding-to-design-to-case evidence matrix.
- [ ] Retain source-bound owner comparison, exact bytes and server actor/default-deny/receipt separation.
- [ ] Coherent metadata, operations, lifecycle head, writer admission, witness freshness and exact-intent outcomes.
- [ ] Every behavioral case NOT_EXECUTED_DESIGN_ONLY; static checks PASS_STATIC_ONLY, never runtime proof.
- [ ] Unknown operator facts remain explicit; no automatic implementation dispatch.
- [ ] Full worker return gate COMPLIANT; COMPLETE_PENDING_REVIEW; reworkGeneration=1.

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2-DESIGN-R1 --title "NCR HTML B2 Durable Acceptance Design R1" --date 2026-10-02 --base 17ae5b9586ee1fdd0fe6a73d0f37b4ab4419f8a2 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --review-round-count 1 --root-cause-cluster-id B2_ACCEPTANCE_DESIGN_UNSPECIFIED --prior-finding-set-digest acd6c094fce6f7f83a11fe92c6877dfc93353c62c9a921c16bf39699d66e1d0b --scec-problem-key cvf-ncr-html-b2-durable-acceptance-design --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_2026-10-02.md --scec-predecessor-sha256 60f92006539a7a37424bb604ad0cb27779f77d1bc2de3cac61f7b6b78c019f56 --stdout` |
| generatedProfile | generic-worker-dispatch no-commit REWORK round-one profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | existing three-output revision, consolidated F01-F06, metadata/operation/lifecycle/writer/witness/exact-intent design boundaries |
| checkerReadAheadConfirmation | dispatch/release/ledger/closeability/envelope/high-risk/probe/semantic literals read before packet authoring |
| docOnlyNewFields | N/A with reason: existing contracts only |
| claimBoundary | proposed design only; no implemented mechanism |

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
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2_DURABLE_ACCEPTANCE_DESIGN_R1_2026-10-02.md
```

Source/document consistency only. No Vitest/Playwright/SQLite/HTTP/provider run or dependency install. Existing runtime evidence consumed within its own limits.

## Claim Boundary

Documentation-only proposed B2 design, no implemented owner/store/schema/admission, real account/data/artifact decision, new runtime/provider proof, durable acceptance, Q001/Q004/R0 exit or public/deploy claim. Cases unexecuted; reviewed design does not authorize implementation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
