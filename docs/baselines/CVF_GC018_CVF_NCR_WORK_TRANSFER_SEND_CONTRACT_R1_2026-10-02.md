# CVF GC-018 Baseline - NCR Work Transfer Send Contract R1

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-WORK-TRANSFER-SEND-CONTRACT-R1

Dispatch base head: `8204dc7ca786d7d594a84088a0bf101e21806c47`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; real effect owner: operator.

## Purpose

Repair the unratified send-contract proposal as one integrated design-only root contract. Address all D01-D04 in the controlling Local review, preserve original evidence, clarify OC-1..5 as unratified choices and extend the planned case ledger. No implementation, runtime proof, policy ratification or real effects.

## Source / Predecessor Evidence

Controlling D083 review `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_COMPLETION_2026-10-02.md` at material 6b025b15528976bcf4fea5a950f5db525f090eb9 and continuity 8204dc7ca786d7d594a84088a0bf101e21806c47. Original work order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md` is INITIAL ordinal 0; this is integrated REWORK ordinal 1 of the same root. Original contract/evidence/return are historical read-only inputs, no design ratification. Product checkpoint still governs design-only send/read direction.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| All dependent repair findings and unratified OC scope | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_COMPLETION_2026-10-02.md` | Findings / Position; Decision / Disposition | D01-D04 | Local controlling review | ACCEPT |
| Operator send-only/read direction | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_PRODUCT_SCOPE_CHECKPOINT_2026-10-02.md` | Selected Contract Boundaries | sender/recipient/admin direction | operator checkpoint | ACCEPT |
| Historical draft, not accepted semantic design | GOVERNED_PROPOSAL | `docs/reference/CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_2026-10-02.md` | Local Review Qualification; sections 8/10 | SC-CASE-050; OC-1..5 | existing proposal | ACCEPT |
| Original sealed plan and 62 unexecuted cases | GOVERNED_EVIDENCE | `docs/reviews/evidence/cvf-ncr-work-transfer-send-contract-worker-evidence-2026-10-02.json` | preAuthoringSeal; casePlan; localReviewQualification | sealed 23 versus final 27 | historical evidence | ACCEPT |
| Open root with no implementation admission | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D083; D084 | D083/D084 | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

Admit one consolidated design-only REWORK after committed/hash-bound packet release. Reviewer-local qualification cannot perform the material state/identity/refusal/case redesign (MATERIAL_DESIGN_CHANGE). Worker creates three absent R1 artifacts, original inputs preserved. No detailed OC policy ratification or implementation grant. Governing order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_R1_2026-10-02.md`.

## Scope / Target / Owner Boundary

- `docs/reference/CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_R1_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-work-transfer-send-contract-r1-worker-evidence-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_R1_WORKER_RETURN_2026-10-02.md`

Governing order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_R1_2026-10-02.md`. Zero product paths, DB/server/browser/provider runs or worker commits.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - dispatcher read named source regions and exact path collisions only; no complete scan, all-files-read or repository-wide absence claim. Worker reports PARTIAL if asserting selected corpus processing, with manifest/ledger/reconciliation/exclusions/drift checks.

## Integrated Design Admission

ROOT_CONTRACT_REQUIRED, INTEGRATED_ROOT_CONTRACT; same root and problem key, one consolidated design repair. No backend/runtime admission. B2 STOP/NO_SUCCESSOR preserved.

## Implementation Contract

1. D01 finality: a missing lookup row never establishes RECONCILED_NOT_RECORDED. Distinguish in-flight, stale/untrusted read, unknown outcome, recorded outcome and an authoritative terminal no-record result. Define logical evidence obligations for writer terminality/no-late-write, freshness, matching identity and authority. When any obligation is absent, keep INDETERMINATE and refuse automatic retry/new request. Same-key replay is permissible only under a separately specified future atomic idempotency guarantee, never inferred from absence. No actual writer/store/witness selected or tested. Include stale-read, late-commit, positive admitted terminal-evidence and denied missing-evidence cases. If no independent non-B2 proof is available, classify gate NOT_ADMITTED and keep implementation blocked; no stopped B2 witness/restore successor.
2. D02 identity: define immutable logical request fingerprint, equality semantics and key namespace including trusted workspace/sender and requestId. Cover same key/same logical request, same key/different packet version, recipient, workspace or sender; define exclusions such as transport timestamps without changing logical identity. Changed logical request under the same scoped key is an explicit refusal, not duplicate success. Packet identity alone must not create a global ban on sending the same version to another recipient. Define duplicate/conflict scope per logical send, include cross-workspace/sender collision and concurrent replay plans, and disclose future atomicity obligations. No physical schema/backend chosen.
3. D03 binding: refusal depends on fallback/unverified provenance, not string spelling. A trusted verified org_cvf/team_eng binding can be legitimate; client-only fallback with those values remains refused. Unknown-user may be a sentinel only if the actual verified identity contract says so. Include positive verified default-looking values, negative identical strings from fallback/unverified source, malformed/missing bindings and same-workspace admin scope. Separate workflow role from enterprise read authority.
4. D04 evidence: preserve all original artifacts/seal and 62 NOT_EXECUTED_PLANNED cases as immutable historical inputs. Map original IDs/cases to retained, superseded or revised R1 cases with reasons, no silent deletion. Disclose original sealed refusal range 23 versus final 27; do not retroactively reseal it or claim scratchpad invocation/chronology was reproduced. Seal the R1 plan before authoring with an exact reproducible byte recipe and retained canonical payload inside R1 evidence (UTF-8, JSON sorted keys, separators comma/colon, ensure_ascii true, no BOM/no trailing newline); SHA-256 that payload excluding its digest. Final source/output hashes separate, no self-cycle. Record all post-seal deviations honestly. Embed cross-check command/script and actual aggregate result in an allowed artifact, avoiding dependence on an untracked scratchpad script.
5. OC decisions: OC-1 deny break-glass read, OC-2 refuse unverified send and OC-5 refuse self-send are Local conservative recommendations for design review, not operator ratification. OC-3 remains a source-backed owner comparison with no selection; no invented runtime availability. OC-4 design cardinality is one recipient per logical send, with a distinct send to a different recipient evaluated independently under scoped identity/permission. This does not authorize a batch/multi-recipient endpoint or impose an unapproved per-packet-version recipient ban. Provide a decision table: operator direction versus Local recommendation versus unresolved operator/owner gate. No detailed policy deemed approved merely by executing this order.
6. Keep trusted sender/recipient/workspace/read binding, packet verification, stages and send-versus-acknowledgment-versus-artifact-acceptance distinctions. Reuse original source graph within its partial boundary, refresh named source hashes only and inspect changed regions if drift; no full producer rescan or runtime experiment. Revised case counts follow actual obligations, not a fixed quota; every requirement/refusal/state/transition ID must map to explicit positive/negative/unknown-outcome cases as applicable. Every case remains NOT_EXECUTED_PLANNED; aggregate static coverage PASS_STATIC_ONLY is not semantic or behavioral acceptance.
7. Return all D01-D04 and OC dispositions together with remaining UNKNOWN gates, known dependencies, planned future independent proof and proposed implementation manifest (proposal only). If a dependency requires B2 stopped architecture or actual authority/store selection, disclose and leave NOT_ADMITTED; do not synthesize a mechanism or declare the root resolved. Local decides acceptance after return.

## Acceptance Criteria

- [ ] Three absent R1 outputs only, original proposal/evidence/seal/62 cases retained; no product/test/runtime mutation or worker commit.
- [ ] D01 terminality/freshness/authority/matching identity obligations; missing row alone stays INDETERMINATE and no automatic retry.
- [ ] D02 scoped immutable request fingerprint, changed logical request refusal and explicit per-send conflict scope with case plan.
- [ ] D03 provenance-based binding refusals and positive verified default-looking collision case.
- [ ] D04 original delta disclosed; R1 canonical seal payload retained/recomputable, final hashes separate, deviations and embedded cross-check preserved.
- [ ] OC-1..5 decision table unratified; one recipient per send, no global per-packet ban or backend selection.
- [ ] Full requirement/refusal/state/transition and original-to-R1 case mapping, every case NOT_EXECUTED_PLANNED and aggregate PASS_STATIC_ONLY.
- [ ] Eight proof IDs/full gate, explicit UNKNOWN and implementation NOT_ADMITTED; no B2 dependency workaround or root closure.

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
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-WORK-TRANSFER-SEND-CONTRACT-R1 --dispatch-kind REWORK --review-round-count 1 --root-cause-cluster-id TRANSFER_SEND_IDENTITY_SCOPE_CONTRACT_UNSPECIFIED --prior-finding-set-digest df1f67c34c1427ad68a2c9f87474ec81b107c10e7b429dc38fca70c46271f442 --scec-problem-key cvf-ncr-work-transfer-send-contract --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --stdout` |
| generatedProfile | generic-worker-dispatch REWORK internal no-commit profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | preserved original owner controls; integrated D01-D04, OC non-ratification, retained historical inputs, SCEC same-root counters and exact R1 manifest |
| checkerReadAheadConfirmation | dispatch/ledger/release/closeability/envelope/structure/high-risk/read-ahead/review-cost/semantic sources read before authoring |
| docOnlyNewFields | proposals only, no runtime schema |
| claimBoundary | static contract design only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove runtime reachability/policy enforcement |

## Current Runtime Freshness Verification

Clean authoring base 8204dc7ca786d7d594a84088a0bf101e21806c47; D083 DESIGN_NOT_RATIFIED. Historical 14 hashes/32 locators/62 planned cases are static evidence, not runtime proof. Review material 6b025b15528976bcf4fea5a950f5db525f090eb9. No product or real binding change; WT-F02/WT-F03 closed, B2 STOP/NO_SUCCESSOR unchanged.

## Evidence Requirements

Clean released base and exactly three absent R1 outputs; original inputs remain read-only. Review finding-set digest SHA-256(raw bytes of docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_COMPLETION_2026-10-02.md)=df1f67c34c1427ad68a2c9f87474ec81b107c10e7b429dc38fca70c46271f442. Source/output hashes, reproducible R1 seal payload/recipe, full original-to-R1 case/ID delta and post-seal deviations; source-backed D01-D04/OC dispositions; embedded aggregate cross-check command/result; all cases NOT_EXECUTED_PLANNED. No raw-seal chronology attestation, false behavioral PASS or root-closure claim.

## Verification Commands

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json
git diff --check
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_SEND_CONTRACT_R1_2026-10-02.md
```

Source/document consistency only. No Vitest/Playwright/HTTP/provider/SQLite execution, module import, dependency install or reading runtime stores/secrets. Required PASS_TARGETED_DEFECT_CLASS, if return guard requires it, must be qualified PASS_STATIC_ONLY with actual graph/coverage check, not runtime proof.

## Claim Boundary

Contract/design and static case coverage only. No executable send/read/provenance, real identity/workspace/data/store binding, backend implementation, artifact acceptance, durable B2/Q001/Q004/P11 closure, provider call, public sync or deployment claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY


## Review Gate

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. Local reviews D01-D04/OC and integrated case mapping with static/source receipts; no broad runtime rerun. Detailed design remains pending ratification and implementation NOT_ADMITTED. Use routine MFRP M5/M10/safety/M20.
