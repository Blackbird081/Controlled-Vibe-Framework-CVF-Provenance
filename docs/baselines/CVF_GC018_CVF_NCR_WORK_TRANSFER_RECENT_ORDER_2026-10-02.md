# CVF GC-018 Baseline - NCR Work Transfer Recent Order

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-WORK-TRANSFER-RECENT-ORDER

Dispatch base head: `a942f03dde06ade87a3f02fe144d3d6c6555ea05`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; real effect owner: operator.

## Purpose

Correct WT-F03 within the existing Work Transfer page: newest-first timestamp order before the eight-record cap, with meaningful focused UI regressions. Do not alter audit-store ordering or transfer authority.

## Source / Predecessor Evidence

Accepted source audit `docs/reviews/CVF_CVF_NCR_HTML_WORK_TRANSFER_SOURCE_RECORD_REACHABILITY_COMPLETION_2026-10-02.md` at 408039c78 confirms WT-F03 and chooses page-local correction admission. D076/D077 in `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` authorize this narrow technical task. No producer/role definition decision follows; prior audit limitations and B2 STOP remain. Admission source audit found no extra owner/file or dependency needed: existing page and existing test suffice.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| WT-F03 accepted source finding; selected smaller technical step | GOVERNED_REVIEW | `docs/reviews/CVF_CVF_NCR_HTML_WORK_TRANSFER_SOURCE_RECORD_REACHABILITY_COMPLETION_2026-10-02.md` | Findings / Position; Risk / Corrective Action | History order | Local reviewer | ACCEPT |
| Page slice and selected export mapping | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | WorkTransferPage; recordToExportRequest | recordToExportRequest | Work Transfer page | ACCEPT |
| Existing three UI tests and mock surfaces | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.test.tsx` | WorkTransferPage | WorkTransferPage | page test | ACCEPT |
| Upstream ascending timestamp ordering | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | readControlPlaneEvents | readControlPlaneEvents | event-store owner, read-only | ACCEPT |
| Installed local test runner and live selection exclusion | SOURCE_CONTRACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts` | test include/exclude | defineConfig | Vitest config, read-only | ACCEPT |
| Bounded recent-order admission | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D076; D077 | D077 | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

After committed paired packet/hash-bound continuity/bound release PASS, worker changes two existing source/test paths and creates exactly three proof/reference/return outputs. Test-first old-code red then final green; Local reviews/commits. No broader runtime pilot.

## Scope / Target / Owner Boundary

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.test.tsx`
- `docs/reference/CVF_NCR_WORK_TRANSFER_RECENT_ORDER_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-work-transfer-recent-order-worker-evidence-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_RECENT_ORDER_WORKER_RETURN_2026-10-02.md`

Governing order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_RECENT_ORDER_2026-10-02.md`. No other source/config/test/registry/continuity path, global store-order change, real endpoint/store/browser/provider access or worker commit.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named owner/test admission and exact output collisions only; no corpus scan or producer completeness claim. Prior source-audit partial coverage stays partial.

## Integrated Design Admission

Bounded adaptation of one page response-to-display step. Existing owner/table order is canonical upstream and remains unchanged. The integrated contract below fixes order-before-cap, copy non-mutation, stable ties and ID-bound selection; planned rendered oracles distinguish old behavior before edit. No new architecture, API, durable schema or cross-owner adaptation required. Worker records pre-edit plan/hashes before product edits; no additional review round.

## Implementation Contract

Fix WT-F03 in the existing page only. Two existing product/test files plus three new documentation/evidence/return outputs. No wider transfer semantics or history access change.

1. At the page's successful audit-list response, derive the display list from a copy, order timestamps newest first, then cap at eight. Match the existing owner's canonical timestamp-string ordering (the store uses timestamp.localeCompare), with descending direction locally. Preserve upstream relative order for equal timestamps; preserve record objects/IDs. Do not mutate the response array or sort the shared store. Do not merely reverse/sort an already sliced first-eight list. Implementation technique within these two files is worker-owned; no new helper file, library or comparator exported solely for tests.
2. Keep current endpoint, session/role/data-scope policy, loading/error/empty handling, selection/deselection and recordToExportRequest mapping. Current Vietnamese/English recent titles stay: the behavioral ordering is corrected to match them. No relabel as an admin audit product, no definition/filter/producer that makes events transfers, no actor/scope correction, no export provenance or receipt change. Malformed/legacy/non-canonical timestamp or missing-field schema repair stays outside scope; disclose this boundary rather than invent a fallback policy.
3. Extend `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.test.tsx` using existing React Testing Library/Vitest. Render the actual page with a synthetic mocked GET response, at least twelve distinguishable canonical-UTC timestamped audit records. Ascending input reproduces old oldest-eight bug; deliberately shuffled input verifies sort-before-cap independent of input order. Assert rendered record IDs/order against a literal expected sequence and absence of excluded IDs, not a second copy of the production comparator. The old implementation must fail a focused targeted test for the intended order/limit reason before product edit; capture actual command/exit/assertion. Never call a real endpoint.
4. Verify response non-mutation with frozen or before/after original array/order/record data, equal-timestamp stability, fewer than eight, exactly eight, empty success, unsuccessful payload/rejected fetch, and existing Vietnamese/English structure. No broad field validation or duplicate Print/Preview suite. Strengthen mock isolation/reset as needed within this existing test so new tests do not leak response state into existing tests.
5. Click a displayed newest record, assert the mocked ArtifactExportPanel receives its expected existing initialRequest (including ID-derived anchor/action/path), then deselect. This verifies reordering did not turn displayed identity into an array-index mismatch; do not invoke ArtifactExportPanel runtime or its export endpoint. Keep panel module mocked and test real page event handlers.
6. Before product edits, record a small integrated plan and case-to-oracle matrix in evidence/reference, with the two pre-edit source digests. Source hashes sealed before changes must not be replaced by final hashes; record final hashes separately. No pre-execution review round is required. After implementation, run targeted page Vitest, tsc --noEmit and eslint of only these two files with --max-warnings=0 using installed local tools. Do not install dependencies, run build/dev/browser/DB/provider/live tests or a full unit suite. Capture commands, exits, counts and actual executable-sequence assertion evidence. Test fixtures are structural/local UI proof only, not AI governance or real-user access proof.
7. Return exact five-path diff and three new outputs: bounded implementation/proof reference; evidence JSON with clean executionBaseHead/status, pre-edit plan/hash, red/green receipt, explicit rendered expected/observed sequences, non-mutation/stability/selection checks, focused type/lint and boundary receipts; pending worker return with all eight proof IDs and full worker gate. No self-hash cycle or unsupported behavioral claim. If focused lint/type exposes an unrelated pre-existing issue, disclose source/command; no forbidden-file repair or silent waiver.

## Acceptance Criteria

- [ ] Clean bound released base; two known existing source/test files and three absent new outputs; exact five worker paths, no commit.
- [ ] Newest-first by existing canonical timestamp order before eight-item cap; source response and equal-timestamp order preserved.
- [ ] Targeted old-code red then fixed-code green, with actual page rendered sequence and literal expected IDs for >8 ascending/shuffled inputs.
- [ ] Non-mutation, ties, short/exact-eight/empty/error and language regressions; actual page selection/deselection maps displayed identity correctly.
- [ ] No endpoint/store/role/scope/producer/export-policy edit; missing-field/timestamp policy remains outside scope.
- [ ] Pre-edit plan/source hashes distinct from final digests, focused Vitest/type/lint receipts and eight-proof ledger join.
- [ ] Full return gate COMPLIANT; COMPLETE_PENDING_REVIEW; WORKER_MUST_NOT_COMMIT honored.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | existing Work Transfer page | local presentation order only | focused UI unit proof, no real-user policy proof | same endpoint/export panel | BOUNDED_IMPLEMENTATION |
| EXTERNAL_AGENT_CLI_MCP | none opened | no ingress/effect grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-WORK-TRANSFER-RECENT-ORDER --title "NCR Work Transfer Recent Order" --date 2026-10-02 --base a942f03dde06ade87a3f02fe144d3d6c6555ea05 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-work-transfer-recent-list-order --stdout` |
| generatedProfile | generic-worker-dispatch INITIAL internal no-commit profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | page-local newest-first/cap/non-mutation/stability/selection contract, two existing code/test files and three new proof outputs |
| checkerReadAheadConfirmation | dispatch/release/ledger/closeability/envelope/structural/high-risk/read-ahead/semantic constants and literal traps read before authoring |
| docOnlyNewFields | N/A with reason: existing guard contracts only |
| claimBoundary | dispatch admission, not executed behavior proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove runtime reachability/policy enforcement |

## Current Runtime Freshness Verification

No new runtime execution during authoring. Clean HEAD a942f03dde06ade87a3f02fe144d3d6c6555ea05; page still data.slice(0, 8) and store still ascending timestamp order; page test currently mocks empty success. Read current code/config/package sources, consume accepted WT-F03 only; no rerun of previous audit, Print/Preview or warm Docker walkthrough.

## Evidence Requirements

Clean executionBaseHead/status; pre-edit plan/source digests; actual red/green rendered explicit sequences and independent input non-mutation oracle; tie/selection/empty/error and language checks; type/lint receipts; final digests and exact five-path diff; worker ADIF and full gate. No screenshot/browser/provider/governance-runtime proof.

## Verification Commands

From Web package directory `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`, using installed local tools only:

```powershell
npx --no-install vitest run 'src/app/(dashboard)/work-transfer/page.test.tsx'
npx --no-install tsc --noEmit
npx --no-install eslint 'src/app/(dashboard)/work-transfer/page.tsx' 'src/app/(dashboard)/work-transfer/page.test.tsx' --max-warnings=0
```

Targeted Vitest red-before-product-change and final green are required. No live mode/real AI governance assertion; mock GET/panel confines this to local UI structure/order/selection. No build/dev/Playwright/HTTP/store/provider/dependency install. tsc may emit tsbuildinfo locally: restore only a test-generated tracked byproduct to its captured pre-run bytes if necessary, disclose exact cleanup and never reset unrelated dirt.

From repository root:

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json
git diff --check
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_WORK_TRANSFER_RECENT_ORDER_2026-10-02.md
```

## Claim Boundary

Only local rendered list order/cap/non-mutation/selection in named synthetic UI fixtures may be proven. No transfer producer, real account/workspace authorization, governance API enforcement, artifact acceptance, durable B2/Q001/Q004/P11 closure, public sync or deployment claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_Q001_DOCKER_BROWSER_UI_WALKTHROUGH_2026-09-29.md` |
| Chain map route | Local source-record reachability reconciliation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing Work Transfer, audit route, admin session and control-plane events |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | source audit only; Local decision owner |


## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

