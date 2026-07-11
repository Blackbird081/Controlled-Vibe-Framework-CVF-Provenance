# CVF MSEA-R94-T0 Contract To Runtime 50 Row Inventory

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: audit

Date: 2026-07-11

Batch ID: MSEA-R94-T0

Worker: delegated worker role

executionBaseHead: `5d6d8b98f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Machine companion: `docs/audits/CVF_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_EVIDENCE_2026-07-11.json`

Revision: Round 2 (testPairingStatus recomputed, matrixClaim restored, catalog evidence strengthened).

## Purpose

Complete a source-backed contract-to-runtime inventory for all 50 Governance Control Matrix rows, independently classifying implementation, invocation, test pairing, and operator/evidence routing.

## Target / Source

Target: `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` Control Matrix rows GC-001 through GC-050.

Source authority: the matrix table; cited primary evidence files; current runtime, checker, catalog, workflow, hook, CI, and test files at executionBaseHead `5d6d8b98f`.

## Scope / Methodology

Filesystem-backed direct reads, `rg` searches, catalog cross-referencing. Each row traced independently. GC-001 through GC-008 freshly re-derived with contract-vs-protocol guard distinction. Test files verified by existence check and import verification (`importlib.util.spec_from_file_location` pattern). Catalog membership verified by literal string match in catalog source files.

## Findings / Position

### Contract vs Protocol Guard Split (GC-001 through GC-008)

The matrix cites `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/` for all 8 RUNTIME_GUARD controls. These contract guards are exported from `index.ts:34-41` and registered by `createGuardEngine()` at `index.ts:115-130`. Production callers exist in cvf-web.

`CVF_GUARD_CONTRACT/src/index.test.ts` tests all 8 contract guards. GC-004 and GC-007 cite this test and pair correctly. The other 6 rows cite protocol guard tests from `PHASE_GOVERNANCE_PROTOCOL` -- a mismatch.

### Test Pairing Findings

- 28 rows have verified matching standalone test files
- 12 rows genuinely lack standalone tests (confirmed by complete repo search)
- 6 rows have cited test pairing mismatches
- 2 rows have no applicable test (human/template enforced gates)

### Disposition Summary

| Disposition | Count |
|---|---|
| CONTRACT_ONLY_WITH_REASON | 2 |
| IMPLEMENTED_NOT_INVOCATION_PROVEN | 4 |
| INVOKED_TEST_PAIRING_MISMATCH | 6 |
| PROVEN_CONNECTED | 26 |
| PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST | 12 |
| **Total** | **50** |

### Enforcement Class Aggregation

| Enforcement Class | Count |
|---|---|
| RUNTIME_GUARD | 8 |
| GATEWAY_PRECONDITION | 2 |
| APPROVAL_CHECKPOINT | 6 |
| CI_REPO_GATE | 31 |
| GOVERNANCE_DECISION_GATE | 3 |
| **Total** | **50** |

### 50-Row Source-Claim Table

| Row ID | Governance Rule | Primary Owner | Enforcement Class | Active Entrypoints | Primary Evidence |
|---|---|---|---|---|---|
| GC-001 | AI agents cannot act in human-only phases... | PhaseGateGuard | RUNTIME_GUARD | shared guard engine, runtime SDK, Web/AP... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/phase-gat... |
| GC-002 | high-risk actions must escalate or block... | RiskGateGuard | RUNTIME_GUARD | shared guard engine, runtime SDK, multi-... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/risk-gate... |
| GC-003 | non-human actors cannot approve, deploy, merge, or override ... | AuthorityGateGuard | RUNTIME_GUARD | shared guard engine, runtime SDK, Web ex... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority... |
| GC-004 | mutating AI actions require ai_commit evidence... | AiCommitGuard | RUNTIME_GUARD | shared guard engine, runtime SDK default... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/ai-commit... |
| GC-005 | mutations must stay within budget... | MutationBudgetGuard | RUNTIME_GUARD | shared guard engine, runtime SDK default... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/mutation-... |
| GC-006 | file mutations must stay inside declared file scope... | FileScopeGuard | RUNTIME_GUARD | shared guard engine, runtime SDK, multi-... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/file-scop... |
| GC-007 | protected governance/root paths cannot be modified freely... | ScopeGuard | RUNTIME_GUARD | shared guard engine, runtime SDK default... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/scope.gua... |
| GC-008 | request, agent, and trace evidence must exist for governed a... | AuditTrailGuard | RUNTIME_GUARD | shared guard engine, runtime SDK default... | EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/audit-tra... |
| GC-009 | every execution channel must pass through guard evaluation f... | MandatoryGateway | GATEWAY_PRECONDITION | guard contract runtime helpers, channel ... | EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandator... |
| GC-010 | governed helper runtime must stop on approval-required escal... | AgentExecutionRuntime | GATEWAY_PRECONDITION | guard contract runtime helpers, governed... | EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-ex... |
| GC-011 | governed BUILD requires plan evidence before execution proce... | PipelineOrchestrator | APPROVAL_CHECKPOINT | runtime orchestrator, SDK bridge workflo... | EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/pipeline.orchestrator.ts, EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/pipeline.orchestrator.test.ts |
| GC-012 | governed BUILD and FREEZE checkpoints require explicit appro... | PipelineOrchestrator | APPROVAL_CHECKPOINT | runtime orchestrator, SDK bridge workflo... | EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/sdk.test.ts, EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/pipeline.orchestrator.test.ts |
| GC-013 | governed FREEZE requires execution and review evidence befor... | PipelineOrchestrator | APPROVAL_CHECKPOINT | runtime orchestrator, SDK bridge workflo... | EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/pipeline.orchestrator.ts, docs/baselines/archive/CVF_SYSTEM_UNIFICATION_PHASE2_CONTROL_LOOP_DELTA_2026-03-20.md |
| GC-014 | rollback actions must preserve failure reason and rollback e... | ExtensionBridge | APPROVAL_CHECKPOINT | cross-extension workflow runtime... | EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/wiring/extension.bridge.ts, EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/extension.bridge.test.ts |
| GC-015 | baseline artifact must be updated after every substantive ch... | check_baseline_update_compat.py | CI_REPO_GATE | CI, local pre-push hook chain... | governance/compat/check_baseline_update_compat.py,... |
| GC-016 | docs, bug, and test evidence must remain historically consis... | docs governance + bug/test compat gates | CI_REPO_GATE | CI, local hooks... | governance/compat/check_docs_governance_compat.py,... |
| GC-017 | release/readiness claims must stay aligned with actual refer... | check_release_manifest_consistency.py | CI_REPO_GATE | CI, release-readiness verification... | governance/compat/check_release_manifest_consisten... |
| GC-018 | roadmap deepening and breadth expansion must stop unless dep... | CVF_DEPTH_AUDIT_GUARD + roadmap depth-audit register + check_depth_audit_continuation_compat.py + check_gc018_stop_boundary_semantics.py | GOVERNANCE_DECISION_GATE | roadmap continuation decisions, CI, loca... | governance/toolkit/05_OPERATION/CVF_DEPTH_AUDIT_GU... |
| GC-019 | major structural changes must complete audit -> independent ... | CVF_STRUCTURAL_CHANGE_AUDIT_GUARD + structural audit packet + independent review packet | GOVERNANCE_DECISION_GATE | restructuring roadmap execution, structu... | governance/toolkit/05_OPERATION/CVF_STRUCTURAL_CHA... |
| GC-020 | governed work pauses/transfers must classify the transition ... | CVF_AGENT_HANDOFF_TRANSITION_GUARD + CVF_AGENT_HANDOFF_GUARD + handoff compat gate | APPROVAL_CHECKPOINT | pause/resume checkpoints, agent-to-agent... | governance/compat/check_agent_handoff_guard_compat... |
| GC-021 | low-risk additive work inside an already-authorized tranche ... | CVF_FAST_LANE_GOVERNANCE_GUARD | CI_REPO_GATE | additive tranche-local implementation ba... | governance/compat/check_fast_lane_governance_compa... |
| GC-022 | memory-bearing governance records must declare the right dur... | CVF_MEMORY_GOVERNANCE_GUARD | CI_REPO_GATE | evidence-bearing docs, storage-taxonomy ... | governance/compat/check_memory_governance_compat.p... |
| GC-023 | governed files must stay under class-specific maintainabilit... | CVF_GOVERNED_FILE_SIZE_GUARD | CI_REPO_GATE | governed source/test/frontend surface... | governance/compat/check_governed_file_size.py... |
| GC-024 | once a governed test surface is split, its canonical ownersh... | CVF_TEST_PARTITION_OWNERSHIP_GUARD | CI_REPO_GATE | tranche-local test extraction... | governance/compat/check_test_partition_ownership.p... |
| GC-025 | new or resumed governed sessions must load one canonical boo... | CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD | CI_REPO_GATE | new chat/session startup... | governance/compat/check_session_governance_bootstr... |
| GC-026 | governed tranche posture changes must update the canonical p... | CVF_PROGRESS_TRACKER_SYNC_GUARD | CI_REPO_GATE | tranche closure, continuation authorizat... | governance/compat/check_progress_tracker_sync.py... |
| GC-027 | canonical multi-agent intake review documentation must stay ... | CVF_MULTI_AGENT_REVIEW_DOC_GUARD | CI_REPO_GATE | multi-agent proposal evaluation... | governance/compat/check_multi_agent_review_governa... |
| GC-028 | live AI Boardroom deliberation must converge through a canon... | BoardroomTransitionGateContract | APPROVAL_CHECKPOINT | live control-plane boardroom sessions... | governance/compat/check_boardroom_runtime_governan... |
| GC-029 | touched extension packages must pass their own package-level... | CVF_EXTENSION_PACKAGE_CHECK_GUARD | CI_REPO_GATE | extension-local source/test/config chang... | governance/compat/check_extension_package_check.py... |
| GC-030 | new or materially revised governance guards must satisfy the... | CVF_GUARD_AUTHORING_STANDARD_GUARD | CI_REPO_GATE | new guard creation, material guard revis... | governance/compat/check_guard_authoring_standard.p... |
| GC-031 | every dedicated rotation guard must register its active wind... | CVF_ACTIVE_WINDOW_REGISTRY_GUARD | CI_REPO_GATE | dedicated rotation guards, archive tooli... | governance/compat/check_active_window_registry.py... |
| GC-032 | governed packets must be authored from source truth... | CVF_GOVERNED_ARTIFACT_AUTHORING_GUARD | CI_REPO_GATE | governed docs authoring... | governance/compat/check_governed_artifact_authorin... |
| GC-033 | governed package public barrels must remain thin routing sur... | CVF_PUBLIC_SURFACE_MAINTAINABILITY_GUARD | CI_REPO_GATE | CPF public barrel maintenance... | governance/compat/check_cpf_public_surface_maintai... |
| GC-034 | governed barrel smoke tests must remain small... | CVF_BARREL_SMOKE_OWNERSHIP_GUARD | CI_REPO_GATE | CPF barrel smoke maintenance... | governance/compat/check_cpf_public_surface_maintai... |
| GC-035 | governed CPF batch families must adopt the shared batch help... | CVF_SHARED_BATCH_HELPER_ADOPTION_GUARD | CI_REPO_GATE | CPF batch-contract maintenance... | governance/compat/check_cpf_batch_helper_adoption.... |
| GC-036 | canonical summary docs must stay separate from typed evidenc... | CVF_CANON_SUMMARY_EVIDENCE_SEPARATION_GUARD | CI_REPO_GATE | whitepaper/tracker/handoff maintenance... | governance/compat/check_canon_summary_evidence_sep... |
| GC-037 | visible repository roots must be lifecycle-classified before... | CVF_REPOSITORY_LIFECYCLE_CLASSIFICATION_GUARD | CI_REPO_GATE | pre-public repository cleanup... | governance/compat/check_repository_lifecycle_class... |
| GC-038 | visible repository roots must be exposure-classified... | CVF_REPOSITORY_EXPOSURE_CLASSIFICATION_GUARD | CI_REPO_GATE | pre-public publication planning... | governance/compat/check_repository_exposure_classi... |
| GC-039 | no P3 structural relocation may proceed without explicit rea... | CVF_PREPUBLIC_P3_READINESS_GUARD | CI_REPO_GATE | pre-public P3 readiness review... | governance/compat/check_prepublic_p3_readiness.py... |
| GC-040 | governed CPF and EPF batch contracts must preserve determini... | CVF_BATCH_CONTRACT_DETERMINISM_GUARD | CI_REPO_GATE | governed batch-contract maintenance... | governance/compat/check_batch_contract_determinism... |
| GC-041 | workers must inherit canonical surface scan state from one m... | CVF_SURFACE_SCAN_CONTINUITY_GUARD | CI_REPO_GATE | fresh quality assessment... | governance/compat/check_surface_scan_registry.py... |
| GC-042 | product-value claims must use one frozen evidence chain... | CVF_PRODUCT_VALUE_VALIDATION_GUARD | CI_REPO_GATE | product-value validation planning... | governance/compat/check_product_value_validation_g... |
| GC-043 | knowledge absorption must default to doctrine-first... | CVF_KNOWLEDGE_ABSORPTION_PRIORITY_GUARD | CI_REPO_GATE | knowledge-absorption roadmaps... | governance/compat/check_knowledge_absorption_prior... |
| GC-044 | skill/template intake must use one deterministic CVF-standar... | CVF_TEMPLATE_SKILL_STANDARD_GUARD | CI_REPO_GATE | repo-derived skill intake... | governance/compat/check_template_skill_standard_gu... |
| GC-045 | new governed Markdown files must include required structural... | CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD | CI_REPO_GATE | new governed Markdown files... | governance/compat/check_markdown_structural_comple... |
| GC-046 | multi-agent absorption reviews must use Evidence Trace Block... | CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD | GOVERNANCE_DECISION_GATE | multi-agent absorption reviews... | governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_A... |
| GC-047 | bounded-corpus reports must prove source-corpus completeness... | CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD | CI_REPO_GATE | folder/file-based agent tasks... | governance/compat/check_corpus_completeness_report... |
| GC-048 | corpus-derived knowledge maps must preserve source authority... | CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_GUARD | CI_REPO_GATE | architecture maps, semantic-region ledge... | governance/compat/check_corpus_to_knowledge_map_re... |
| GC-049 | core guard/control files are frozen by default... | CVF_CORE_GUARD_SELF_PROTECTION_GUARD | CI_REPO_GATE | guard scripts, hook chains... | governance/compat/check_core_guard_self_protection... |
| GC-050 | corpus-derived intelligence classification must use a ledger... | CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_GUARD | CI_REPO_GATE | corpus classification ledgers... | governance/compat/check_corpus_intelligence_classi... |

Full six-field matrix claims are in the JSON companion `matrixClaim` objects.

### 50-Row Classification Ledger

| Row ID | Enforcement Class | Implementation | Invocation | Test Pairing | Operator/Evidence | Disposition |
|---|---|---|---|---|---|---|
| GC-001 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | CITED_TEST_PAIRING_MISMATCH | WEB_API_ROUTE | INVOKED_TEST_PAIRING_MISMATCH |
| GC-002 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | CITED_TEST_PAIRING_MISMATCH | WEB_API_ROUTE | INVOKED_TEST_PAIRING_MISMATCH |
| GC-003 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | CITED_TEST_PAIRING_MISMATCH | WEB_API_ROUTE | INVOKED_TEST_PAIRING_MISMATCH |
| GC-004 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | WEB_API_ROUTE | PROVEN_CONNECTED |
| GC-005 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | CITED_TEST_PAIRING_MISMATCH | WEB_API_ROUTE | INVOKED_TEST_PAIRING_MISMATCH |
| GC-006 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | CITED_TEST_PAIRING_MISMATCH | WEB_API_ROUTE | INVOKED_TEST_PAIRING_MISMATCH |
| GC-007 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | WEB_API_ROUTE | PROVEN_CONNECTED |
| GC-008 | RUNTIME_GUARD | IMPLEMENTED | INVOKED | CITED_TEST_PAIRING_MISMATCH | WEB_API_ROUTE | INVOKED_TEST_PAIRING_MISMATCH |
| GC-009 | GATEWAY_PRECONDITION | IMPLEMENTED | NO_CONFIRMED_PRODUCTION_CALLER_FOUND | TEST_PAIRS_WITH_CITED_SOURCE | NO_OPERATOR_SURFACE | IMPLEMENTED_NOT_INVOCATION_PROVEN |
| GC-010 | GATEWAY_PRECONDITION | IMPLEMENTED | NO_CONFIRMED_PRODUCTION_CALLER_FOUND | TEST_PAIRS_WITH_CITED_SOURCE | NO_OPERATOR_SURFACE | IMPLEMENTED_NOT_INVOCATION_PROVEN |
| GC-011 | APPROVAL_CHECKPOINT | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | WEB_API_ROUTE | PROVEN_CONNECTED |
| GC-012 | APPROVAL_CHECKPOINT | IMPLEMENTED | INVOKED | NO_SPECIFIC_TEST_FOR_DISTINCT_SEMANTICS | WEB_API_ROUTE | IMPLEMENTED_NOT_INVOCATION_PROVEN |
| GC-013 | APPROVAL_CHECKPOINT | IMPLEMENTED | INVOKED | NO_SPECIFIC_TEST_FOR_DISTINCT_SEMANTICS | WEB_API_ROUTE | IMPLEMENTED_NOT_INVOCATION_PROVEN |
| GC-014 | APPROVAL_CHECKPOINT | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | WEB_API_ROUTE | PROVEN_CONNECTED |
| GC-015 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-016 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-017 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-018 | GOVERNANCE_DECISION_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-019 | GOVERNANCE_DECISION_GATE | IMPLEMENTED | HUMAN_TEMPLATE_ENFORCED | NO_TEST_APPLICABLE | NO_MACHINE_SURFACE | CONTRACT_ONLY_WITH_REASON |
| GC-020 | APPROVAL_CHECKPOINT | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-021 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-022 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-023 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-024 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-025 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-026 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-027 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-028 | APPROVAL_CHECKPOINT | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-029 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-030 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-031 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-032 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-033 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-034 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-035 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-036 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-037 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-038 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-039 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-040 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-041 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-042 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |
| GC-043 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-044 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-045 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-046 | GOVERNANCE_DECISION_GATE | IMPLEMENTED | HUMAN_TEMPLATE_ENFORCED | NO_TEST_APPLICABLE | NO_MACHINE_SURFACE | CONTRACT_ONLY_WITH_REASON |
| GC-047 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-048 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-049 | CI_REPO_GATE | IMPLEMENTED | INVOKED | TEST_PAIRS_WITH_CITED_SOURCE | CLI_AGGREGATE | PROVEN_CONNECTED |
| GC-050 | CI_REPO_GATE | IMPLEMENTED | INVOKED | CHECKER_HAS_NO_STANDALONE_TEST | CLI_AGGREGATE | PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST |

## Risk / Corrective Action

### Repair Candidates by Priority

1. **GC-001,002,003,005,006,008** (HIGH, 6 rows): CITED_TEST_PAIRING_MISMATCH. Fix: update matrix evidence to cite `CVF_GUARD_CONTRACT/src/index.test.ts`.

2. **GC-009, GC-010** (MEDIUM, 2 rows): IMPLEMENTED_NOT_INVOCATION_PROVEN. No production caller found.

3. **GC-012, GC-013** (MEDIUM, 2 rows): IMPLEMENTED_NOT_INVOCATION_PROVEN. Share PipelineOrchestrator owner with GC-011.

4. **12 rows** (LOW): PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST. Genuinely lack standalone tests. No repair needed for these rows.

5. **GC-019, GC-046** (LOW, 2 rows): CONTRACT_ONLY_WITH_REASON. Human/template enforced. No repair needed.

## Corpus Completeness And Report Integrity

- Corpus task class: GOVERNANCE_CONTROL_MATRIX_50_ROW_AUDIT
- Corpus root: `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` Control Matrix table
- Snapshot time: 2026-07-11 at executionBaseHead `5d6d8b98f`
- Enumeration command: filesystem-backed direct reads; `rg --files --hidden --no-ignore` for caller searches; os.path.isfile() for test file existence
- Manifest artifact or inline manifest: JSON companion `sourceManifest` (82 files)
- Manifest hash normalization: sort-records-by-path-ordinal; serialize-each-as-path-TAB-terminalStatus; join-with-LF-no-trailing; encode-UTF-8-no-BOM; sha256-lowercase-hex
- Manifest hash: SHA-256 `5bd27a365a1a265a165f863df9b614e7d779d13e005342b122f4aaeba5aae433` (algorithm: sha256)
- Processing ledger artifact or inline ledger: JSON companion `rows` array (50 entries)
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=82, ledger_terminal=50, exclusions=0, unresolved=0
- Unresolved files: 0
- Unreadable or unsupported files: 0
- Declared exclusions: unrelated repository trees, build outputs, and live runtime execution are outside this bounded 50-row source inventory
- Aggregation check: 50 unique row IDs; disposition and enforcement-class totals each equal 50; operator evidence covers 50 of 50 rows
- Drift check: executionBaseHead `5d6d8b98f` and all cited source paths were checked during reviewer intake
- Output traceability: every ledger row maps to structured implementation, invocation, test-pairing, operator-route, and matrix-claim evidence
- Adversarial verification: contract-versus-protocol identity, production callers, standalone tests, catalog lines, and manifest canonicalization were independently challenged
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Claim Boundary

This audit classifies 50 rows at executionBaseHead `5d6d8b98f`. No implementation, repair, or T1-T4 work. PROVEN_CONNECTED_BOUNDED_NO_STANDALONE_TEST bounds the connection claim: invocation is proven through catalog membership; standalone test absence is explicitly disclosed.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | 50-row contract-to-runtime read-only inventory |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | ACTION_EVIDENCE_PRESENT |
| invocationBoundary | read-only filesystem reads, rg searches, catalog cross-referencing |
| interceptionBoundary | no provider, runtime, IDE, MCP, Web, CLI-adapter, or public interception |
| claimLanguage | classification evidence from current source only |
| forbiddenExpansion | no matrix, runtime, checker, hook, workflow, Web, lifecycle, public, or session mutation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Rescan Intelligence Hardening

NOT_APPLICABLE_WITH_REASON

N/A with reason: R94-T0 is a fresh inventory from the current Governance Control Matrix, not a rescan or intake refresh. No prior surface-scan state was inherited and no rescan pipeline was used. All 50 rows are new classifications from current source.

- Original source artifact: N/A with reason: no prior rescan source exists
- Predecessor intake artifact: N/A with reason: no predecessor intake
- Delta ledger status: N/A with reason: no delta ledger applicable
- Routing matrix status: N/A with reason: no routing matrix applicable
- Semantic sampling status: N/A with reason: no semantic sampling performed
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

No prior intake exists. All 50 rows are new classifications from current source at executionBaseHead `5d6d8b98f`.

Delta categories:
- UNCHANGED_FROM_INTAKE: 0 (no prior intake)
- CHANGED_DISPOSITION: 0 (no prior intake)
- NEW_FINDING: 50 (all rows are fresh classifications)
- REMOVED_OR_REJECTED: 0 (no prior intake)

### Follow-Up Routing Matrix

No routing matrix is applicable. This is a read-only inventory, not a rescan or intake refresh.

Routing lanes:
- DO_NOW: N/A with reason: no rescan findings to act on
- SEPARATE_RUNTIME_TRANCHE: N/A with reason: no runtime work authorized
- STRATEGIC_OPERATOR_DECISION: N/A with reason: no strategic decision required
- OUT_OF_SCOPE: this inventory is complete; follow-up is reviewer-owned
- RESOLVED_BY_DESIGN: N/A with reason: no design-resolution items

### Semantic Sampling / Adversarial Review

No semantic sampling was performed. Adversarial verification was limited to the contract/runtime split detection, collision checks, and catalog membership verification documented in the Corpus Completeness section.

- sampleId: N/A with reason: no sampling performed
- source section: N/A with reason: no sampling performed
- source claim: N/A with reason: no sampling performed
- disposition checked: N/A with reason: no sampling performed
- adversarial challenge: N/A with reason: no sampling performed
- verdict: N/A with reason: no sampling performed
