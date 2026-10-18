# NCR R1 UX/Profile Source - GC-018 Baseline

Memory class: governed-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-18
Batch ID: CVF-NCR-R1-UX-PROFILE-SOURCE-20261018
Inspection base: 8d39e708fed33ecbba5ce2e5e092738d4c4a3449
Commit mode: WORKER_MUST_NOT_COMMIT
rawMemoryReleased=false
providerExecutionAuthority: FORBIDDEN
Decision owner: LOCAL Root
Intended governed path: `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`

## Purpose

Prepare one source-only R1 user-language and selected-profile disclosure correction for the existing Work Transfer HTML flow. The finite outcome is readable Vietnamese/English job, recovery, review, Stop and pre-Build explanation in the current UI, with no change to job identity, writes or effect authority. This is the distinct UX gap in the 2026-10-18 R1/R2 exit disposition, not a recovery-source replay.

## Scope / Target / Owner Boundary

The sole worker source manifest is `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/{HtmlJobControls.tsx,ArtifactExportPanel.tsx}`. Root is Local decision owner; a shared-workspace worker is INTERNAL_AGENT. Work is a prospective source admission only until Root binds the candidate to committed current continuity and runs actual pre-dispatch gates. No source implementation is released by this draft.

The old source chain remains RETURN3/counters0,1,0,3; browser RETURN1/counters0,0,0,0; parent generation9/SCEC ordinal2/counters2,0,2,0/blockers2/freeze/prior7/LHW24. No prior actor replay, successor or budget refill is implied. New `ncr-r1-ux-profile-disclosure` is a distinct mixed-language/profile-copy issue with its own initial convergence object; it must not erase inherited evidence or blockers.

## Locked Source Contract

1. Use the existing `useLanguage()` context (`vi`/`en`) in the two touched components. Translate their user-visible control, status, error, Stop, link/reconcile and person-review copy, including accessible names. Newly introduced notices in the touched components must react to language changes. `HtmlDraftRecovery` already has a vi/en table and remains read-only; its existing stateful notice switch semantics are a retained limitation. Preserve exact wire values, user-entered text, IDs, request data and decision content.
2. `html-job-api.ts` already returns `{jobDecisions:true,effectBoundary:'LOCAL_SYNTHETIC'}` for a successful capabilities GET. Keep `jobDecisions` as the existing job-control enablement gate. Capture the exact effect-boundary enum as presentation state under the same scope/epoch checks and clear it with scope. Pass `LOCAL_SYNTHETIC` to `ArtifactExportPanel.tsx` only when the capability response also has `jobDecisions:true`. Missing/malformed enum retains job behavior and shows generic disclosure. Fallback and standalone panel use retain the generic receipt/destination warning. A prop is never permission or proof that a later POST uses the same configuration. The export POST resolves its profile separately. Configuration change and any actual receipt effect remain R2/W05 pre-live gaps.
3. The selected description before Build says that this profile renders HTML locally, uses synthetic local storage, does not request a governance receipt, and yields an unverified draft until separate review. The same authenticated person can record a local synthetic review, which is neither trusted evidence nor business acceptance. Stop is local: late result suppression does not prove remote termination, absence of a write or absence of cost. For generic/receipt-enabled fallback, retain concrete destination/data/cost uncertainty instead of suggesting guaranteed locality.
4. Preserve auth, scope/epoch/expiry fences, owner triple, job and version IDs, submitted request hash, exact HTML hash, pending journal, GET reconciliation, unknown outcome, link and decision controls, writer semantics and all server-side admission. Do not alter literal protocol enums as a localization shortcut. No new generic helper, provider/account chooser, endpoint, server, schema, storage, auth, i18n owner or runtime wiring.

## Source And Dependency Read Map

| Path or symbol | Observed dependency / boundary |
| --- | --- |
| `src/components/HtmlJobControls.tsx` | `useSession`, capability GET, scope and epoch checks, goal/criteria/job/reconcile/link/decision copy; current `data<{jobDecisions:true}>` discards `effectBoundary` |
| `src/lib/server/html-job-api.ts:87-88` | Successful capabilities GET includes `jobDecisions:true` and `effectBoundary:'LOCAL_SYNTHETIC'`; read-only server owner |
| `src/components/ArtifactExportPanel.tsx` | Existing `useLanguage`, `LABELS`, `preGenerateDisclosure`, Stop/status rendering and fallback generic path; presentation-only prop recipient |
| `src/components/HtmlDraftRecovery.tsx` | Read-only recovery child with existing vi/en table; no mutation of retained stateful notice semantics |
| `src/components/useHtmlBuildAttempts.ts` | Build/Stop attempt state; read-only; no cancellation or retry rewrite |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n.tsx` | Context provider; read-only; no global translation registry edit |
| `tests/e2e/ncr-r1-integrated-html-job-browser.spec.ts` and focused export/recovery tests | Read-only historical test evidence and selector map; no mutation or run in this packet |

The two selected source files have current Git blob identities respectively `198767c261b8f752f40e74fadeb2a6f096c16b82` and `d15cf7a42b703659029a13345e64be046b5f4391`; MATCH: Root reconciled actual source identities in Current Runtime Freshness Verification. These are named-file reads, not a repository census.

## Evidence / Planned Verification

Worker returns the two source files plus `docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_WORKER_RETURN_2026-10-18.md` and `docs/reviews/evidence/ncr-r1-ux-profile-source-worker-20261018.json` (exact four paths). Source-only static acceptance may use installed local `tsc --noEmit` and scoped ESLint with a safe environment and `envDir=false` where applicable. No package install, Next server, browser, provider, network, private data, `.env` loading, test mutation or test run. Keep `ArtifactExportPanel.tsx` below the 975-line near-hard size threshold; it is currently 883 lines. A static pass cannot establish actual language reactivity, keyboard/small-screen usability or pre-effect comprehension. Focused component proof and a separately admitted user-role walkthrough remain pending roadmap evidence; no R1 exit follows from this package.

Root's independent Local source review inspects the actual diff for every invariant and user-visible string, source hashes, exact four-path manifest, no test/server/write drift, and worker static evidence. It consumes valid return evidence without duplicate per-row reruns. A contradiction is named before any focused recheck. Any server or test change need stops the worker and returns one consolidated finding to Root.

After the worker's bound full return gate, Root may add one necessary Local completion review and update the existing NCR roadmap. Accepted closure material is exact six paths (worker four plus Root two); current six continuity paths are a separate synchronization phase. No optional document, registry or guard change is selected.

## Design Control Gate

The current `DESIGN.md` governs natural short Vietnamese, accessible labels and plain action/error text. The selected profile must be explained before Build at the actual UI point. This packet changes language and disclosure only; it cannot certify a user walkthrough or turn a capabilities response into immutable effect authorization.

## Decision / Baseline

DISPATCH_READY contract selected by Local under operator latest next and standing autonomous roadmap authority. This fresh action-specific source admission is the selected next step after completed exit/gap disposition, not an old actor retry. Source writes remain held until pair/current6 committed and actual bound pre-dispatch PASS; Root releases exactly one source-only worker then. No test, app/browser/provider, network, real-data or public effect is admitted.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-R1-UX-PROFILE-SOURCE-20261018 --title "NCR R1 UX profile source" --date 2026-10-18 --base 8d39e708fed33ecbba5ce2e5e092738d4c4a3449 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key ncr-r1-ux-profile-disclosure --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | web-ui-dashboard plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| checkerReadAheadConfirmation | applicable checker sources and final schema/literal fields read before release; original candidate failure retained |
| manualEditsAfterScaffold | Action-specific source, profile, UX, evidence and scope decisions |
| docOnlyNewFields | selected presentation-only effect-boundary prop; no wire/schema field |
| claimBoundary | Candidate packet only; no runtime/provider/live/public claim. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_tables.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/run_adif_defect_resolver.py |
| literalTokensReviewed | exact4 worker and exact2 dispatch; exact6 closure material; separate current6; immutable pair; SOURCE_INSPECTION; existing jobDecisions enablement and LOCAL_SYNTHETIC presentation enum; full bound return; no source test mutation/run |
| gateRunPurpose | confirmation of consolidated source-only admission and exact schema/path/authority bindings before release; not product proof |
| claimBoundary | declarations and compiler/lint cannot establish UI behavior, effect admission or R1/R2 exit |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | NOT_APPLICABLE_WITH_REASON: current private source composition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | this source admission pair |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Local verifies private CVF; no external source promotion |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - explicit named sources only; no completeness claim.

## Knowledge System Reconciliation

- Knowledge task class: NON_KNOWLEDGE_SOURCE_IMPLEMENTATION
- Source manifest: Source Verification Block and exact four worker manifest
- Source manifest hash: NOT_APPLICABLE; no corpus manifest or map produced
- Enumeration safety: filesystem-backed explicit named-file reads
- Intake registry or ledger: no knowledge intake selected
- Authority assets: immutable accepted source, Local review, design and current continuity
- Derived views: no knowledge view produced
- Semantic region ledger: no mapping regions
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: NONE within zero-asset scope
- Cross-region links: NONE
- Drift check: source pins before edits and final hash reconciliation
- Rebuildability check: Git/source manifest and named commands
- Retrieval boundary: no retrieval-readiness assertion
- Adversarial verification: no map verification selected
- Knowledge-map verdict: PARTIAL

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: named local source correction, no corpus reassessment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY. Private prospective source packet; no public-sync work.

## Epistemic Process Block

Expected Result / Prediction: bounded language and profile copy can close the named source gap without changing effects. Evidence Comparison: current source has mixed language and generic selected-flow disclosure; capabilities includes the selected boundary, while export resolves profile again. Contradiction Or Gap Disposition: presentation remains contingent and generic fallback remains. Claim Update: candidate source admission only; no runtime or stage-exit proof.

## Claim Boundary

No source edit, static check, component proof, walkthrough, provider call, test, R1/R2 stage exit, production or public claim is made by this draft.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`.

Returned 27; IDs: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006. Raw `.cvf/runtime/ncr-r1-ux-profile-20261018/planning/adif-dispatch.json` SHA256 `669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687`.

Impact: selected named source only; no corpus claim, provider memory authority, protected worker write, detached process, broad proof reuse or runtime promotion. Exact pair/worker/closure/current6 scopes, actual source fields, independent Local review and mandatory gate/raw-failure retention handle applicable items. No new guard selected.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT Local dispatcher/reviewer; decision owner=LOCAL |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-r1-ux-profile-source-admission-20261018 |
| Working directory | repository root |
| Command or tool surface | named source analysis; two read-only planning aides; pair authoring and mandatory governance checks |
| Target paths | `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` |
| Allowed scope source | operator next and standing autonomous roadmap continuation; selected R1/R2 exit-gap disposition |
| Before status evidence | 8d39e708fed33ecbba5ce2e5e092738d4c4a3449; git status --short = clean; clean worktree before admission |
| After status evidence | exact2 source admission pair; source implementation awaits committed current6 and bound pre-dispatch PASS |
| Diff evidence | git diff --name-status; git diff --check; exact2 reconciliation |
| Approval boundary | source2 UI presentation plus return2 only; no protected worker path or effect |
| Claim boundary | source contract only; no source/runtime proof before execution |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-r1-ux-profile-source-admission-20261018 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_PROFILE_SOURCE_2026-10-18.md` |
| Manifest delta | MATCH exact2 dispatch material; current6 separately |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | source-only R1 language and profile description |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: actual source/static evidence only at return |
| receiptEvidence | N/A with reason: no governance receipt selected |
| actionEvidence | N/A with reason: source edits have not begun |
| invocationBoundary | one INTERNAL_AGENT source task; mandatory gates; no app/browser/provider invocation |
| interceptionBoundary | no runtime interception or universal enforcement claim |
| claimLanguage | exact pins, source inspection and actual compiler/lint outputs only |
| forbiddenExpansion | server/schema/auth/writer/guard/test/runtime/real data/production/public/deploy |

## Current Runtime Freshness Verification

Source identity at inspection HEAD `8d39e708fed33ecbba5ce2e5e092738d4c4a3449`; raw-byte named-file record `.cvf/runtime/ncr-r1-ux-profile-20261018/source-freshness.json` SHA256 `b6918cb9c9fb30b94c4c2899f238150cb539bd90aa7874e53ff03da5c8b2f0c2`. Selected source2 exists; return2 planned paths are unoccupied. No runtime was started; refresh identity if any source changes before release.

| Source file | SHA256 |
|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx | b5b3e2c84913f5bac67e805365431af2c5a461e3066f1fe635080db784dbbc2a |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx | 999f6710d4d9f18268c86f707be709f8e6aaddcb2d449656a3fa27c53f4cada8 |

## Negative Search And Collision Discipline

No negative owner-absence claim is selected. Both component owners and the server capability field exist at the stated source pins; Root checked named paths/symbols. User data and protocol strings are not translated. No repository-wide inference is made.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Root-only exact current6 session metadata for dispatch/result binding; no guard or product semantics change.

Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: standing autonomous roadmap orchestration and necessary session synchronization.
Rollback boundary: current6 only; source pair and source material remain separate commits.

