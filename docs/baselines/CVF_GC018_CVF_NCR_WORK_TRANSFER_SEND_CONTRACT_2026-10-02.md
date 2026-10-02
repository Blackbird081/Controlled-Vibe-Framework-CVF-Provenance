# CVF GC-018 Baseline - NCR Work Transfer Send Contract

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-WORK-TRANSFER-SEND-CONTRACT

Dispatch base head: `1fcf2920fb1b63edb40ef11e783fc226d6f99bb9`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; real effect owner: operator.

## Purpose

Design the operator-selected transfer-send contract on existing owners: explicit sender confirmation to designated recipient, sender/recipient plus authorized same-workspace admin read. Contract/proposal and case plan only; no code, real data, implementation, receipt or artifact acceptance.

## Source / Predecessor Evidence

Operator selected send-only record and proposed sender/recipient plus same-workspace admin read design direction at `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_PRODUCT_SCOPE_CHECKPOINT_2026-10-02.md`. D080-D082 in `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` bind current scope. Prior source audit direct graph bounded/producer completeness partial, WT-F02/WT-F03 accepted. Existing owner comparison is required, not a new producer or backend permission.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Operator selected send-only design/read-scope direction | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_PRODUCT_SCOPE_CHECKPOINT_2026-10-02.md` | Decision / Disposition | Selected Contract Boundaries | Local/operator checkpoint | ACCEPT |
| Design-only dispatch follows bounded UI closures | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D080; D081; D082 | D082 | NCR roadmap | ACCEPT |
| Current checker and audit-derived editable draft | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | COPY; WorkTransferPage; recordToExportRequest | recordToExportRequest | existing page | ACCEPT |
| Workflow context and role validation | SOURCE_CONTRACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/agent-handoff-validator.ts` | HandoffContext; validateHandoff | HandoffContext | local validator | ACCEPT |
| Enterprise admission roles | SOURCE_CONTRACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enterprise-access.ts` | TEAM_ROLES; ADMIN_ROLES; canAccessAdmin | canAccessAdmin | existing role owner | ACCEPT |
| Audit record scope and read | SOURCE_CONTRACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | UnifiedAuditEvent; readAuditEvents | UnifiedAuditEvent | event store, read-only | ACCEPT |
| Existing handoff artifact/writer/verifier boundary | GOVERNED_CONTRACT | `docs/reference/agent_handoff/README.md` | Artifact Completion Evidence | Artifact Completion Evidence | handoff contract index | ACCEPT |

## Decision / Baseline / Proposed Tranche

After committed paired packet/hash-bound continuity/bound release PASS, worker audits source and creates three initially absent documentation/evidence/return outputs. Local reviews the source verdict. No implementation or runtime effect is released.

## Scope / Target / Owner Boundary

- `docs/reference/CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-work-transfer-send-contract-worker-evidence-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_WORKER_RETURN_2026-10-02.md`

Governing order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md`. Zero product paths, DB/server/browser/provider runs or worker commits.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - dispatcher read named source regions and exact path collisions only; no complete scan, all-files-read or repository-wide absence claim. Worker reports PARTIAL if asserting selected corpus processing, with manifest/ledger/reconciliation/exclusions/drift checks.

## Integrated Design Admission

Design-only existing-owner adaptation. Operator selected send semantics/read-scope direction; logical fields, binding joins, refusal/state plan and future manifest remain proposals. No runtime architecture/backend admission or new owner implementation.

## Implementation Contract

Contract/design only; exactly three new documentation/evidence outputs. No code/test/runtime/store/schema execution. Direction selected by operator in `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_PRODUCT_SCOPE_CHECKPOINT_2026-10-02.md`; detailed contract remains a proposal pending Local review.

1. Define one send action and logical record: authenticated sender explicitly confirms sending one identified packet to one designated recipient. Separate intent/draft, submitted request, server-recorded send, recipient acknowledgment and artifact acceptance. Cover send only. A validator ALLOW, audit event, admin seed or HTTP success alone is not the business send. No receipt/acknowledgment/acceptance may be inferred without the selected boundary's evidence.
2. Specify server-derived actor, verified recipient and workspace bindings; do not accept caller-supplied actor/role/workspace as authority. Workflow AgentRole is not TeamRole permission. Design read policy is sender/recipient or authorized owner/admin oversight within that record's verified workspace; no cross-workspace override, arbitrary recipient lookup or break-glass inheritance assumed. Treat account mapping, membership resolution, admin binding and real workspace as UNKNOWN future gates. Define denial cases for missing/invalid/revoked/foreign bindings, impersonation/delegation and service/internal callers rather than inventing authority.
3. Define required logical packet reference/version, stable identity and evidence pointers, including how unverified/nonexistent/mutable references are classified. Compare current draft export and existing handoff writer/artifact/verifier invariant. Do not claim source hash or editable draft anchors provide immutable provenance. Propose minimum logical fields, origin/classification, trusted versus submitted fields and refusal/unknown states; no migration, schema file, new database or physical store path selection. Do not require real document reads or process operator Downloads data.
4. Compare existing owners on responsibility/mandatory call path/failure boundary: Work Transfer page and validator, enterprise access/admin-session, audit route/control-plane events/storage adapter and handoff completion contract. Consume accepted partial source graph; no complete producer re-scan or absence claim. Determine what can be adapted and what needs a separately authorized owner change. Existing store adapter does not by itself prove scope, transactional send semantics or provenance. Supply proposed producer->verifier->consumer joins and future implementation manifest as proposals only.
5. Specify logical idempotency/duplicate/conflicting recipient or packet-version handling, failed admission/failed validation, persistence failure, timeout/unknown outcome and read-only reconciliation classification. No blind retry, no invented durable guarantee, no acceptance store/witness/OS lock, backup mechanism or B2 successor. If existing evidence cannot justify recorded-send acknowledgment, name its future implementation gate. Recovery, backup/retention/custody/cost and actual account/workspace/store remain UNKNOWN; no design may report a real send or durable acceptance until separate proof exists.
6. Seal a small pre-authoring plan and selected source hashes before drafting the contract, retain seal and final output digests separately. Supply independently identified positive/refusal/unknown case plan for every normative requirement, classification/state transition and binding boundary. All behavioral cases NOT_EXECUTED_PLANNED. A static requirement-to-case cross-check with actual command/exit and reconciled IDs may be PASS_STATIC_ONLY; not executable send/access/provenance proof. Return self-proof PASS_TARGETED_DEFECT_CLASS only with explicit PASS_STATIC_ONLY design-coverage qualification required by the existing return gate. Do not invent test counts or simulate runtime to replace unknowns.
7. Return `docs/reference/CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md`, `docs/reviews/evidence/cvf-ncr-work-transfer-send-contract-worker-evidence-2026-10-02.json`, `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_WORKER_RETURN_2026-10-02.md` with source authority/locator/hash/depth, owner overlap, requirement/refusal/state/case ledger, open design choices and future gates, static receipts and actual worker ADIF/full return. COMPLETE_PENDING_REVIEW or consolidated BLOCKED_WITH_REASON; no commit, new tests, package/build/server/HTTP/browser/DB/provider run or worker scope expansion.

## Acceptance Criteria

- [ ] Clean released base and three absent new outputs; no product/runtime edit or worker commit.
- [ ] Send-only logical semantics separate validator/audit/seed from business send, receipt and artifact acceptance.
- [ ] Trusted sender/recipient/workspace binding and same-workspace read policy/refusals; workflow versus enterprise roles separated.
- [ ] Packet/version/evidence identity distinguishes editable/unverified references from authoritative provenance; missing evidence fails closed.
- [ ] Existing-owner responsibility/call-path/failure comparison and proposed future joins/manifest; no invented producer absence or automatic store selection.
- [ ] Duplicate/conflict/unknown-outcome/reconciliation boundaries and future proof gates; B2 remains STOP/NO_SUCCESSOR.
- [ ] Intact pre-authoring seal; requirement/state/refusal IDs covered by NOT_EXECUTED_PLANNED cases; static coverage qualified PASS_STATIC_ONLY.
- [ ] Eight proof IDs/full return COMPLIANT, pending Local review; real bindings/backend/cost/recovery UNKNOWN.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Work Transfer source graph | documentation only | governed sources and selected locators | no runtime/import execution | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none opened | no ingress/effect grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-WORK-TRANSFER-SEND-CONTRACT --title NCR Work Transfer Send Contract --date 2026-10-02 --base 1fcf2920fb1b63edb40ef11e783fc226d6f99bb9 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-work-transfer-send-contract --stdout` |
| generatedProfile | generic-worker-dispatch INITIAL internal no-commit profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | adapted prior three-output source packet controls; operator-selected send/read direction, new contract/case ledger/source authority and independent problem key |
| checkerReadAheadConfirmation | dispatch/ledger/release/closeability/envelope/structure/high-risk/read-ahead/semantic requirements read before authoring |
| docOnlyNewFields | logical contract fields are proposals, not machine runtime schema |
| claimBoundary | contract/design, no executable behavior proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove runtime reachability/policy enforcement |

## Current Runtime Freshness Verification

Clean authoring base 1fcf2920fb1b63edb40ef11e783fc226d6f99bb9; accepted source graph partial and direct consumer findings bounded; current page is local checker plus audit-labelled editable draft/history. No runtime proof, real identity/workspace/store or repository-wide producer absence. WT-F02/WT-F03 closed; consume evidence without rerun.

## Evidence Requirements

Clean released executionBaseHead/status; sealed pre-authoring plan/source hashes; source-backed owner comparison; logical requirement/refusal/state/case ledger with static reconciliation receipts; final output hashes without self-cycle; explicit UNKNOWN and NOT_EXECUTED_PLANNED behavior; actual ADIF/full return. PASS_STATIC_ONLY is design coverage, never runtime proof.

## Verification Commands

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json
git diff --check
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md
```

Source/document consistency only. No Vitest/Playwright/HTTP/provider/SQLite execution, module import, dependency install or reading runtime stores/secrets. Required PASS_TARGETED_DEFECT_CLASS, if return guard requires it, must be qualified PASS_STATIC_ONLY with actual graph/coverage check, not runtime proof.

## Claim Boundary

Contract/design and static case coverage only. No executable send/read/provenance, real identity/workspace/data/store binding, backend implementation, artifact acceptance, durable B2/Q001/Q004/P11 closure, provider call, public sync or deployment claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
