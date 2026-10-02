# CVF GC-018 Baseline - NCR HTML Secret Refusal Recovery

Memory class: governed-dispatch-baseline
Text Encoding Exception: existing Vietnamese recovery literal quoted for exact UI oracle.

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-SECRET-REFUSAL-RECOVERY

Dispatch base head: `ccf29de7eb35e51e198674caf0fc69cf54c15253`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; real effect owner: operator.

## Purpose

Fix F-01 source-proven route/panel error-literal mismatch so the existing localized secret-refusal recovery is selected for the current export route response. Pure local UI presentation and mocked response proof, no secret-scan, route, auth, receipt or provider behavior change.

## Source / Predecessor Evidence

D089 controlling review `docs/reviews/CVF_CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_COMPLETION_2026-10-02.md` confirms F-01 at current source bytes: exact route error differs from panel matcher. D090 selects a pure UI alias repair on existing panel/test, with read-only route fixture pin and independent EN/VI oracle. No runtime secret refusal or stopped-root successor is inferred.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| F-01 accepted source finding, executable proof absent | GOVERNED_REVIEW | `docs/reviews/CVF_CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_COMPLETION_2026-10-02.md` | Findings / Position; Decision / Disposition | F-01 | Local | ACCEPT |
| Current route rejects secret-like fields with artifact-export-fields literal | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | Object.values(fields).some(hasSecretPattern) | POST | export route read-only | ACCEPT |
| UI matcher accepts only older source-content literal; error forwarding preserves payload string | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | recoveryMessageFor; handleGenerate catch; export-error-recovery | recoveryMessageFor | panel | ACCEPT |
| Existing mock test uses older error; bilingual label strings already exist | SOURCE_CONTRACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | maps the secret-pattern rejection to plain-language recovery | ArtifactExportPanel test | mocked local UI | ACCEPT |
| Narrow correction selected, send/B2 still STOP | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D089; D090 | NCR-R1 | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

After paired material commit/hash-bound continuity/bound release PASS, worker modifies existing panel/test and creates exactly three proof outputs under `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_2026-10-02.md`. Local reviews/commits. No actual route/provider/store or broader pilot.

## Scope / Target / Owner Boundary

Exactly five worker paths: modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; create `docs/reference/CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_2026-10-02.md`, `docs/reviews/evidence/cvf-ncr-html-secret-refusal-recovery-worker-evidence-2026-10-02.json`, `docs/reviews/CVF_CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_WORKER_RETURN_2026-10-02.md`. No new source/helper/test module, dependency, route/config/registry/roadmap/continuity write. No actual HTTP/store/provider/browser/server/build or worker commit.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named owner/test admission and exact output collisions only; no corpus scan or producer completeness claim. Prior source-audit partial coverage stays partial.

## Integrated Design Admission

Existing recoveryMessageFor owner and bilingual labels suffice. Add one exact canonical error alias, retain exact legacy compatibility; pin fixture to read-only route literal. No new helper module, route/schema/shared framework or architecture. Independent localized presentation defect, not stopped send/B2 identity/finality objective.

## Implementation Contract

Fix F-01 only, two existing code/test owners and three new proof outputs.

1. In recoveryMessageFor add an exact match for `Potential secret-like value detected in artifact export fields.` to the existing secretRefusalRecovery branch. Keep the existing exact legacy alias `Potential secret-like value detected in source content.` for existing callers/tests. No substring/regex catch-all classification or normalized input acceptance. Do not alter either localized label: EN `This text looks like it may contain a private key or token. Remove that value and try again.`; VI `Nội dung này có vẻ chứa khóa riêng tư hoặc mã token. Hãy xóa giá trị đó rồi thử lại.`. Preserve raw error secondary detail, latest-attempt error association, prior-preview/version context and missing-field mapping. This changes presentation only, never route admission or secret detection.
2. Add independently runnable rendered actual-panel cases for the current route literal in EN and VI. Mock only fetch responses with synthetic 400 payload; no real request and no importing/evaluating the route. Assert literal localized recovery text, raw canonical error detail, no generated candidate/callback on refusal. Keep all existing meaningful regressions.
3. Pin the response fixture to read-only route source in the existing test file using installed Node file-reading APIs. Assert the canonical error literal is the one in the current secret-refusal NextResponse branch; fail clearly if absent/ambiguous/changed. A bounded source extraction plus exact expected literal is enough; do not execute route code, import auth/proof helpers, add parser dependencies or a new shared constant module. Neither a duplicate handwritten mock string without source comparison nor broad /secret-like/i is sufficient. Expected UI text must be literal oracle, not read back from component LABELS.
4. Add focused compatibility/fallback controls: exact legacy alias still gets recovery and preserves raw detail; missing-field rejection retains recovery; an unrelated synthetic error containing words secret-like/private key (but neither recognized literal) remains the raw fallback with no secret-specific detail branch. This prevents broader classification. These unchanged controls are expected green on old code, not forced red. Preserve the existing unknown-error fallback and attempt/version handling.
5. Before product edits, seal evidence plan with case IDs, independently runnable test selectors, literal oracles, expected old outcomes and raw pre-edit panel/test/route hashes. Test-file construction can precede old-code red capture; product panel is untouched until both EN and VI current-route cases have individually failed. Capture each targeted failure independently; source pin and compatibility controls should pass on old code. Preserve seal, append deviations honestly, separate final hashes. No chronology claim beyond actual receipts/snapshot.
6. After fix run the focused existing panel test file, installed tsc --noEmit and two-file eslint --max-warnings=0. No broad suite, route test run, browser/build/server/HTTP/provider/module execution, dependency install or mutation campaign. Existing suite covers closed B1 features; consume prior proof and retain regressions rather than add duplicate milestones. The new proof is mocked UI response mapping, not governance refusal or secret-scan effectiveness.
7. Return exact five paths: concise reference, JSON with sealed plan/pre-edit and separate final hashes, actual red/green commands/exits/assertions, source pin/current EN/VI/legacy/fallback/missing-field controls, preserved regressions, actual worker ADIF and full return gate; COMPLETE_PENDING_REVIEW or one consolidated BLOCKED_WITH_REASON. No commit, no other repair, no send/B2 successor or runtime readiness claim.

## Acceptance Criteria

- [ ] Clean released base, two existing source/test owners and three absent outputs; exact five paths, no commit.
- [ ] Canonical current route literal selects exact existing EN/VI recovery, raw error stays visible and refusal generates no candidate/callback.
- [ ] Read-only source pin proves mocked canonical error agrees with current route refusal; no route imports or calls.
- [ ] Exact legacy alias, missing-field recovery and unrelated-error raw fallback retained; no broad classifier or authority change.
- [ ] Sealed old-outcome plan; independently captured EN/VI old-code failures; source pin/unchanged controls honestly green; deviations append-only.
- [ ] Focused panel suite, type/lint PASS; final hashes separate; all eight proof IDs and full return compliant.
- [ ] No HTTP/store/provider/browser/build, secret-scan/auth/receipt/job/cancel mutation or send/B2/Q001/Q004/P11 closure.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | existing ArtifactExportPanel | local exact error-to-recovery mapping | focused UI unit proof, no real-user policy proof | same export endpoint, read-only route | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none opened | no ingress/effect grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-SECRET-REFUSAL-RECOVERY --title NCR HTML Secret Refusal Recovery --date 2026-10-02 --base ccf29de7eb35e51e198674caf0fc69cf54c15253 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-html-secret-refusal-recovery --stdout` |
| generatedProfile | generic-worker-dispatch INITIAL internal no-commit profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | adapted existing local UI packet guards; exact current/legacy error aliases, source-pinned rendered recovery/control proof, current base and independent F-01 root |
| checkerReadAheadConfirmation | dispatch/ledger/release/closeability/envelope/structure/high-risk/read-ahead/semantic constants and literal traps read before authoring |
| docOnlyNewFields | N/A with reason: existing guard contracts only |
| claimBoundary | dispatch admission only, no executable proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove runtime reachability/policy enforcement |

## Current Runtime Freshness Verification

Clean HEAD ccf29de7eb35e51e198674caf0fc69cf54c15253; source-only admission. Current route secret branch returns artifact-export-fields error, panel matches source-content error only, handleGenerate forwards payload.error unchanged to attemptError/recovery. Existing test mocks older string. Bilingual recovery text exists and needs no rewrite. Accepted D089 F-01 is source-proven unexecuted; new rendered cases discriminate the mismatch. No product or provider execution during authoring.

## Evidence Requirements

Sealed case/oracle plan and source hashes, actual independent EN/VI current-route old-code red, source fixture pin, exact legacy/fallback/missing-field controls, focused final UI/type/lint exits and final hashes. Full return and exact path evidence; no runtime-governance claims.

## Verification Commands

From Web package directory `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`, using installed local tools only:

```powershell
npx --no-install vitest run 'src/components/ArtifactExportPanel.test.tsx'
npx --no-install tsc --noEmit
npx --no-install eslint 'src/components/ArtifactExportPanel.tsx' 'src/components/ArtifactExportPanel.test.tsx' --max-warnings=0
```

Targeted Vitest red-before-product-change and final green are required. No live mode/real AI governance assertion; mock fetch response and actual panel render confine this to local UI recovery presentation. No build/dev/Playwright/HTTP/store/provider/dependency install. tsc may emit tsbuildinfo locally: restore only a test-generated tracked byproduct to its captured pre-run bytes if necessary, disclose exact cleanup and never reset unrelated dirt.

From repository root:

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json
git diff --check
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_2026-10-02.md
```

## Claim Boundary

Local UI error presentation only. Mocked rejection payload and read-only route literal pin do not prove secret detection, real route/auth/receipt/provider enforcement, cancellation, durable acceptance, server outcome or production readiness. Send/B2 STOP; Q001/Q004/P11/effects/public/deploy parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_COMPLETION_2026-10-02.md` |
| Chain map route | Local F-01 recovery mapping admission |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing ArtifactExportPanel and read-only export route |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | source-backed F-01 recovery mapping; Local decision owner |


## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```


## Independent Objective And Evidence Reuse

This INITIAL objective is HTML_SECRET_REFUSAL_RECOVERY_LITERAL_MISMATCH, not send identity/scope or B2 acceptance. F-01 is an existing panel string-coupling defect accepted by D089; scoped mapping can be proven without either stopped root. The source audit order is closed and not replayed. Prior B1 attempt/version/isolation proof is reused and its tests retained; no runtime milestones or new parser/shared framework. No send/B2 root reset, renamed repair, rule change or effect authority.
