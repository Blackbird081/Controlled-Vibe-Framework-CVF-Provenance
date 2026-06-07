# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-07

Current mode marker: `lpci2_t11b_source_verification_closed_pass_bounded`
Enforcement posture: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It intentionally points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V16_2026-06-06.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `lpci2_t11b_source_verification_closed_pass_bounded`.

Active handoff:

`AGENT_HANDOFF_V16_2026-06-06.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Latest continuity note:

LPCI2-T11B Source Verification is `CLOSED_PASS_BOUNDED` at material commit
`acdbcd8b`.

Completion:
`docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md`.

Report:
`docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md`.

External result JSON:
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json`.

Result JSON SHA-256:
`sha256:0d24870a43b0e33eecddae438d669983be508eff9ed4ca4e112ffb48870fd79d`.

Result: 7/7 target records final `verificationResult=HASH_MATCH`; all path,
hash, size, and role/lineage gates passed. Finding: `BNDL-002`, `BNDL-003`,
and `BNDL-005` required Unicode path fallback from T11A candidate manifest
paths to T11A bundle manifest paths before verification. Learning disposition:
`MACHINE_CHECK_CANDIDATE`.

GC-018:
`docs/baselines/CVF_GC018_LPCI2_T11B_POLICYLOCAL_SOURCE_VERIFICATION_2026-06-07.md`.
Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11B_POLICYLOCAL_SOURCE_VERIFICATION_FOR_CLAUDE_2026-06-07.md`.
Status: `CLOSED_PASS_BOUNDED`.
Next allowed move: author a source-verified `LPCI2-T11C Classification
Pre-Check` work order.

Prior continuity note:

LPCI2-T11A Candidate And Bundle Inventory is `CLOSED_PASS_BOUNDED`.
Original T11A Candidate Inventory passed the direct six-file input scope. Codex
review required a supplement for the real `Law use case_Codex` bundle lineage;
that supplement was reviewed and accepted after path-normalization and
structural-section remediation. Completion:
`docs/reviews/CVF_LPCI2_T11A_CANDIDATE_AND_BUNDLE_INVENTORY_COMPLETION_2026-06-07.md`.

Roadmap:

`docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`

Boundary: no body extraction, OCR, content summarization, corpus ingestion,
chunking, runtime query, provider calls, public-sync, current-law claim, legal
advice quality claim, or production/public readiness. EC-02 hard boundary
remains: no current-law claim before 2026-07-01. T12 corpus ingestion remains
gated behind T11-D `READY`.

Prior continuity note:

LPCI2-T10 PolicyLocal foundation readiness is `CLOSED_PASS_BOUNDED` at
material commit `866f92cd`.

Work order:

`docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_FOR_CLAUDE_2026-06-07.md`

Worker/reviewer/closer: Codex, operator-authorized multi-role execution.

Commit mode: `OPERATOR_AUTHORIZED_CODEX_WORKER_REVIEWER_CLOSURE`.

Worker return packet:

`docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_WORKER_RETURN_2026-06-07.md`

Completion:

`docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_COMPLETION_2026-06-07.md`

Result: created local deterministic
`CVF-Workspace/Policy_Local/scripts/policylocal-foundation-readiness.py`,
generated
`CVF-Workspace/Policy_Local/data/generated/policylocal-foundation-readiness-report.json`,
hash-bound the existing T9 external artifacts, asserted AQ-01 through AQ-05
receipt values, preserved AQ-05 EC-02 plus `freshnessDisclosureApplied=true`,
and preserved the EC-02 review boundary.

External hashes: verifier
`sha256:b5f25ad12225f04a4efc94408779af599d6fdc8be1c9d930300cb3301131a4e1`;
report
`sha256:2db39d4450485f073c4ad8965c8f0a3ddaffb64337049cf53df0b68699a8baa6`.

Verification: T10 verifier PASS; work-order dispatch quality PASS; machine
closure package PASS; markdown structural completeness PASS; finding-to-
governance learning PASS; pre-commit hook PASS 36/36 for material commit
`866f92cd`.

Boundary: no provider calls, LLM/chat runtime, vector retrieval, corpus
expansion, EC-02 current-law transition before 2026-07-01, deployment,
public-sync, public/hosted/production readiness, legal advice quality,
provider-quality/cost/performance claim, Learning Orchestrator runtime
behavior, memory reinjection, high-risk promotion, or autonomous mutation.

Prior continuity note:

LPCI2-T9 PolicyLocal search runtime is
`CLOSED_PASS_BOUNDED_CORRECTION_CLEAN` at material commit `fcc9f50f`
(original T9 closure `094d82d0`).

Work order:

`docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md`

Roadmap:

`docs/roadmaps/CVF_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_ROADMAP_2026-06-07.md`

Completion:

`docs/reviews/CVF_LPCI2_T9_SEARCH_RUNTIME_COMPLETION_2026-06-07.md`

Delivered: corrected AQ-05 freshness disclosure receipt behavior/assertion,
added Acceptance Receipt Assertion Matrix, added External Artifact Hash
Manifest, closed the T9 roadmap, updated GC-051 registry evidence, hardened
the work-order template plus machine closure package checker, and clarified
session continuity files in the work-order Allowed scope.

Verification: corrected acceptance receipts PASS 5/5 with AQ-01 and AQ-05
`freshnessDisclosureApplied=true`; receipt artifact hash
`sha256:a8273e358438579360f8fde64129475f7e97e8b9fd889bba074eac083d79223f`;
combined pre-closure gates PASS at final T9 sync.

Boundary: local-deterministic pilot only; no provider calls, LLM, vector
retrieval, legal advice quality, current-law claim, production deployment,
public-sync, public/hosted/production readiness, provider-quality/cost/
performance claim, Learning Orchestrator runtime behavior, memory reinjection,
high-risk promotion, or autonomous mutation.

Prior continuity note:

QBS method reliability remediation is `CLOSED_PASS_BOUNDED`:

Work order:

`docs/work_orders/CVF_WO_QBS_METHOD_RELIABILITY_REMEDIATION_2026-06-06.md`

Completion:

`docs/reviews/CVF_QBS_METHOD_RELIABILITY_REMEDIATION_COMPLETION_2026-06-07.md`

Material commit: `2db8805e`

Post-closure checker hardening commit: `9676ae37`

Delivered:

- `quality-benchmark-suite-methodology.md` §10 gate authority paragraph
  (0.60 standing gate, 0.55 internal-planning-only), §10.1 calibration
  anchor requirement, §13 no-parity / F-1 stop-rule boundary.
- `quality-benchmark-suite-claim-ladder.md` Corpus Power Boundaries,
  Reviewer Agreement Gate, F-1 Stop-Rule Boundary, expanded Non-Claims.
- `claim-boundaries.md` F-1 closed-not-met, 48-task aggregate-only,
  reviewer gate thresholds.
- `reviewer-calibration-anchors-standard.md` pre-run anchor protocol.
- `governance/compat/check_qbs_claim_gate.py` machine checker.

Boundary: methodology/checker/calibration-standard only; no live run,
no corpus expansion, no F-1 reopen, no runtime changes.

Next allowed move: LHW24 remains the latest closed numbered LHW wave. Claude may
execute the T10 foundation readiness work order and return uncommitted
verifier/report artifacts for Codex review. EC-02 freshness review is required
on or after 2026-07-01 before any current-law or production runtime claim.

Prior continuity note:

ERH-RL1A rate limit store boundary is `CLOSED_PASS_BOUNDED`.

Material commit: `3978554c`.

Next allowed move: superseded by ERH-RL1B continuity above.

Earlier continuity note:

RTA1 receipt trace anchor is `CLOSED_PASS_BOUNDED`:

Work order:

`docs/work_orders/CVF_WO_RTA1_RECEIPT_TRACE_ANCHOR_2026-06-06.md`

Completion:

`docs/reviews/CVF_RTA1_RECEIPT_TRACE_ANCHOR_COMPLETION_2026-06-06.md`

Diagnostic:

`docs/evidence/CVF_RTA1_LIVE_PROOF_DIAGNOSTIC_2026-06-06.json`

Material commit: `8630b168`

Delivered:

- `GovernanceEvidenceReceipt.receiptIntegrity` is now an optional additive
  receipt field.
- cvf-web receipt builder adds local canonical receipt hash and optional HMAC
  signature metadata.
- `/api/execute` final response passes receipt signer and optional anchor
  environment metadata to the receipt builder without serializing signer input.
- Focused Alibaba live proof returned receipt `rcpt-env-mq2iyeyu-cak2p5` with
  `signatureStatus=SIGNED` and `externalAnchorStatus=NOT_PROVIDED`.

Boundary: local receipt integrity evidence only; no third-party immutability,
external anchor provider, public-sync, hosted readiness, production readiness,
public readiness, provider-quality claim, cost/performance claim, Learning
Orchestrator runtime behavior, or autonomous mutation.

Verification:

- Pre-dispatch and pre-implementation autorun gates: PASS.
- Focused deterministic tests: PASS, 24 tests.
- `npm run check`: PASS.
- Focused Alibaba live proof: PASS.

Next allowed move: superseded by ERH-RL1A continuity above.

Prior continuity note:

RTE1 runtime telemetry receipt expansion is `CLOSED_PASS_BOUNDED`:

Work order:

`docs/work_orders/CVF_WO_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_2026-06-06.md`

Completion:

`docs/reviews/CVF_RTE1_RUNTIME_TELEMETRY_RECEIPT_EXPANSION_COMPLETION_2026-06-06.md`

Material commit: `78cb38a8`

Delivered:

- `GovernanceEvidenceReceipt.runtimeTelemetry` is now an optional additive
  receipt field.
- cvf-web receipt builder adds sanitized `governanceTraceEntryCount`.
- `/api/execute` final response builds telemetry from existing
  `aiResult.executionTime`, route elapsed time, normalized token usage, and
  existing model-pricing cost estimate.
- Focused Alibaba live proof returned receipt `rcpt-env-mq2i7h03-ztjxy4`.

Boundary: additive receipt evidence only; no provider routing, prompt, policy,
DLP, memory, public-sync, hosted readiness, production readiness, public
readiness, cost optimization, provider-quality claim, external tracing service,
external anchor, Learning Orchestrator runtime behavior, or autonomous mutation.

Verification:

- Pre-dispatch and pre-implementation autorun gates: PASS.
- Focused deterministic tests: PASS, 20 tests.
- `npm run check`: PASS.
- Focused Alibaba live proof: PASS.

Next allowed move: superseded by RTA1 continuity above.

Prior continuity note:

EA external review finding triage is recorded:

Audit:

`docs/audits/CVF_EA_REVIEW_FINDING_TRIAGE_AND_REMEDIATION_REGISTER_2026-06-06.md`

Accepted near-term remediation lanes:

- `EA-P0 Public Surface Hygiene`: hide/remove raw public `Memory class`
  metadata and add a root public-doc completeness check.
- `EA-P1 Public Evidence Discoverability`: improve coverage/current-pointer
  and provider-dependency visibility.
- `EA-P2 Product And Refactor Debt`: CPF source grouping, large barrel review,
  package naming, and five-minute demo remain separate roadmap work.

Verification:

- `python governance/compat/check_finding_to_governance_learning.py --base e4705aa1 --head HEAD --enforce`: PASS.
- `python governance/compat/check_corpus_completeness_report_integrity.py --base e4705aa1 --head HEAD --enforce`: PASS.
- `python governance/compat/check_markdown_structural_completeness.py --base e4705aa1 --head HEAD --enforce`: PASS.
- `python governance/compat/check_corpus_scan_registry.py --base e4705aa1 --head HEAD --enforce`: PASS.

Boundary: triage/register only; no runtime/source behavior, public-sync
implementation, dependency migration, live/provider proof, hosted readiness,
production readiness, coverage claim, package refactor, or public-readiness
expansion.

Prior continuity note:

Public-doc drift and external-agent review-guide hardening is ready for
external review:

Delivered:

- New `governance/compat/check_public_doc_drift_phrases.py` checker with
  focused tests and local hook-chain wiring.
- Same-class stale public-doc repair in `docs/reference/CVF_POSITIONING.md`.
- Public-sync `docs/guides/external-agent-review-guide.md`, linked from
  public README, GET_STARTED, and the public evaluation claim boundary.

Verification:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5fdb794f --head HEAD`: PASS.
- `python governance/compat/check_public_doc_drift_phrases.py --enforce`: PASS in private and public-sync.
- `python -m pytest governance/compat/test_check_public_doc_drift_phrases.py -q`: PASS in private and public-sync.
- Public-sync `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit`: PASS.

Boundary: public-doc and guard hardening only; no runtime/source behavior,
dependency migration, live/provider proof, hosted readiness, production
readiness, provider parity, memory reinjection, high-risk promotion
implementation, Learning Orchestrator runtime behavior, or autonomous mutation.

Prior continuity note:

P1-P5 small debt remediation is ready for external review:

Audit:

`docs/audits/CVF_P1_P5_SMALL_DEBT_REMEDIATION_AUDIT_2026-06-06.md`

Delivered:

- `SECURITY.md` concrete public-safe disclosure path.
- Stale skill-count/version/handoff-link cleanup in private and public-sync docs.
- Scheduled live-governance smoke workflow.
- Secret-safe live evidence manifest script and standard.
- Source-verified backlog work orders for DEP2 `next-auth` migration, ERH-RL1
  distributed rate limiter, and QBS method reliability.

Verification:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2b39dc47 --head HEAD`: PASS.
- `python scripts/run_cvf_release_gate_bundle.py --e2e-live --json`: PASS.

Boundary: no stable Auth.js migration, Redis implementation, PostgreSQL/SSO
readiness, independent immutable anchor, benchmark quality parity, family-level
benchmark power, public/hosted/production readiness, cost/performance/provider
quality claim, memory reinjection, high-risk promotion implementation,
Learning Orchestrator runtime behavior, or autonomous mutation.

Prior continuity note:

External Review GAP 2B Web UI jargon reduction is `CLOSED_PASS_BOUNDED`:

GC-018:

`docs/baselines/CVF_GC018_GAP2B_WEB_UI_JARGON_REDUCTION_2026-06-06.md`

Evidence:

- Material closure commit: `31df9194`.
- 8 wizard components + home/landing descriptive text updated.
- Plain-language outcome labels are now primary headings; CVF terms are muted subtitles.
- All 9 external review GAPs (1, 2A, 2B, 3, 4, 5A, 5B, 6, 7, 8) are now `CLOSED_PASS_BOUNDED`.
- Tests: all green; tsc clean.
- Public Export Disposition: `DEFERRED_PRIVATE_ONLY`.

Next allowed move: stop for review. External review remediation series is complete.
Blocked without separate authorization: governance-rule retirement, dependency expansion,
public-sync or public push, live/provider proof, public/hosted/production readiness
claims, memory reinjection, high-risk promotion implementation, and autonomous mutation.

Prior external-review continuity note:

External Review GAP6 provider risk cap ENV override is `CLOSED_PASS_BOUNDED`:

GC-018:

`docs/baselines/CVF_GC018_GAP6_PROVIDER_RISK_CAP_ENV_OVERRIDE_2026-06-06.md`

Evidence:

- Material closure commit: `92d446a8`.
- ENV vars: `CVF_PROVIDER_RISK_CAP_<PROVIDER_UPPERCASE>`, `CVF_PROVIDER_RISK_CEILING`.
- 6/6 tests pass; full cvf-web suite green; tsc clean.
- Public Export Disposition: `DEFERRED_PRIVATE_ONLY`.

Earlier external-review continuity note:

External Review GAP4/GAP5 runtime durability tranche is
`CLOSED_PASS_BOUNDED`:

GC-018:

`docs/baselines/CVF_GC018_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_2026-06-06.md`

Audit:

`docs/audits/CVF_GOVERNANCE_RULE_PROOF_OF_VALUE_AUDIT_2026-06-06.md`

Completion:

`docs/reviews/CVF_EXTERNAL_REVIEW_GAP4_GAP5_RUNTIME_DURABILITY_COMPLETION_2026-06-06.md`

Evidence:

- Material closure commit: `f37df607`.
- GAP4 audit keeps governance rules with consolidation candidates only; no rule
  retirement was authorized.
- GAP5A sets only `runtime_receipt_count` to `liveEmissionWired=true` and emits
  metadata-only `OPERATIONAL_BENCHMARK_METRIC_EMITTED` audit events.
- GAP5B adds local SQLite storage adapters behind
  `CVF_STORAGE_ADAPTER_TYPE=sqlite`; Redis remains stubbed.
- Public Export Disposition: `DEFERRED_PRIVATE_ONLY`.

Earlier external-review continuity note:

External Review GAP1 Core KB pointer-ification is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_GAP1_CORE_KB_POINTER_IFICATION_2026-06-06.md`

Completion:

`docs/reviews/CVF_GAP1_CORE_KB_POINTER_IFICATION_COMPLETION_2026-06-06.md`

Evidence:

- Material closure commit: `fb9e81c5`.
- `docs/CVF_CORE_KNOWLEDGE_BASE.md` was reduced from 769 lines to 400 lines.
- Stale `131 active skills` references were removed from Core KB.
- Section XI and Section XII were verified unchanged from base.
- Rule 4 now points version/folder/status ownership to Section II plus
  `docs/reference/CVF_MODULE_INVENTORY.md`.
- Public Export Disposition: `DEFERRED_PRIVATE_ONLY`.

Earlier external-review continuity note:

External review gap-analysis intake was repaired and made trackable:

`docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md`

Earlier closure continuity note:

LE1 Live E2E Selector Flow Diagnostic is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`

Completion review:

`docs/reviews/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_COMPLETION_2026-06-06.md`

Evidence:

- Material commit: `8a6cb056`.
- Helper:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts`
- Focused live Playwright result:
  `docs/evidence/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_RESULT_2026-06-06.json`
- Release gate result:
  `docs/evidence/CVF_LE1_RELEASE_GATE_RESULT_2026-06-06.json`
- Diagnostic:
  `docs/evidence/CVF_LE1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`

Previous continuity note:

MLW7 Runtime Adapter Boundary GC-018 is
`GC018_AUTHORIZED_HOLD_FOR_WORK_ORDER`:

`docs/baselines/CVF_GC018_MLW7_RUNTIME_ADAPTER_BOUNDARY_2026-06-05.md`

Material commit: `7d7d6eda`.

The baseline selects `MLW7-RTAD1` as the next source-verified work-order
candidate: runtime adapter boundary/admission authoring only. It does not
authorize runtime adapter implementation, package install, external execution,
external repo ingestion, delegation approval, registry authority, marketplace
publication, public-sync, live/provider proof, hosted readiness, production
readiness, public readiness, memory reinjection, automatic promotion,
high-risk promotion implementation, Learning Orchestrator runtime behavior, or
autonomous mutation.

Next allowed move: author the source-verified `MLW7-RTAD1` runtime adapter
boundary/admission work order, or stop for review. Any actual runtime adapter
implementation, install/execute path, delegation/registry authority,
marketplace/public claim, public-sync, live proof, hosted readiness,
production readiness, public readiness, memory reinjection, automatic
promotion, high-risk promotion implementation, or autonomous mutation requires
separate explicit authorization.

Previous continuity note:

MLW-NRD1 Next Runtime Decision Readout is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_MLW_NRD1_NEXT_RUNTIME_DECISION_READOUT_2026-06-05.md`

Completion review:

`docs/reviews/CVF_MLW_NRD1_NEXT_RUNTIME_DECISION_READOUT_COMPLETION_2026-06-05.md`

Material commit: `efd4dc85`.

Next allowed move: choose a separate operator-authorized lane: MLW7 external
execution/runtime adapter GC-018, MLW8 optimization/benchmark/cost proof
GC-018, LO2 high-risk promotion implementation GC-018, public-sync/export
order, live/provider proof order, or stop for review. Hosted readiness,
production readiness, public readiness, memory reinjection, automatic
promotion, and autonomous mutation remain blocked without separate
authorization.

Previous continuity note:

MLW Next Runtime Decision GC-018 is `GC018_AUTHORIZED_HOLD_FOR_WORK_ORDER`:

`docs/baselines/CVF_GC018_MLW_NEXT_RUNTIME_DECISION_2026-06-05.md`

The baseline selects `MLW-NRD1` as the next source-verified work-order
candidate: a route-visible advisory decision/readout surface that classifies
which MLW runtime lane is eligible next. It does not authorize route wiring,
external capability execution, runtime adapter authority, automatic
optimization, benchmark/cost proof, high-risk promotion implementation,
public-sync, live proof, hosted readiness, production readiness, public
readiness, memory reinjection, automatic promotion, or autonomous mutation.

Superseded next-move note: MLW-NRD1 work-order authoring is complete at
material commit `7352799f`.

Earlier continuity note:

Public-Safe Memory/Learning Summary packet is `CLOSED_PASS_BOUNDED`:

GC-018:
`docs/baselines/CVF_GC018_PUBLIC_SAFE_MEMORY_LEARNING_SUMMARY_2026-06-05.md`

Work order:
`docs/work_orders/CVF_WO_PUBLIC_SAFE_MEMORY_LEARNING_SUMMARY_2026-06-05.md`

Summary:
`docs/reference/CVF_PUBLIC_SAFE_MEMORY_LEARNING_SUMMARY_2026-06-05.md`

Review:
`docs/reviews/CVF_PUBLIC_SAFE_MEMORY_LEARNING_SUMMARY_REVIEW_2026-06-05.md`

Material commit: `c42bc8d4`.

The packet closes only a private, public-safe synthesis of LO1, LO2, MLW7,
MLW8, and closure-packaging preflight evidence. Public Export Disposition is
`DEFERRED_PRIVATE_ONLY`. It does not authorize public-sync, public push,
runtime implementation, live/provider proof, hosted readiness, production
readiness, public readiness, automatic promotion, memory reinjection, or
autonomous mutation.

LO2 High-Risk Promotion Decision Boundary is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_LO2_HIGH_RISK_PROMOTION_DECISION_BOUNDARY_2026-06-05.md`

Baseline:
`docs/baselines/CVF_GC018_LO2_HIGH_RISK_PROMOTION_DECISION_BOUNDARY_2026-06-05.md`

Reference:
`docs/reference/CVF_LO2_HIGH_RISK_PROMOTION_DECISION_BOUNDARY_2026-06-05.md`

Completion:
`docs/reviews/CVF_LO2_HIGH_RISK_PROMOTION_DECISION_BOUNDARY_COMPLETION_2026-06-05.md`

LO2 closes the high-risk promotion lane as a review-only decision boundary:
MLW5 audit validation, MLW6 simulation/failure evidence, and adaptation policy
evidence are prerequisites; `automaticPromotionAuthorized=false` and
`autonomousMutationAuthorized=false` remain binding.

MLW7 Optional External Capability Ingestion is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_2026-06-05.md`

Completion:
`docs/reviews/CVF_MLW7_OPTIONAL_EXTERNAL_CAPABILITY_INGESTION_COMPLETION_2026-06-05.md`

Runtime helper:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw7-external-capability-ingestion.ts`

MLW8 Efficiency And Overconstraint Feedback is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_2026-06-05.md`

Completion:
`docs/reviews/CVF_MLW8_EFFICIENCY_OVERCONSTRAINT_FEEDBACK_COMPLETION_2026-06-05.md`

Runtime helper:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw8-efficiency-overconstraint-feedback.ts`

Closure Packaging Preflight Hardening is `CLOSED_PASS_BOUNDED`:

`docs/work_orders/CVF_WO_CLOSURE_PACKAGING_PREFLIGHT_HARDENING_2026-06-05.md`

Completion:
`docs/reviews/CVF_CLOSURE_PACKAGING_PREFLIGHT_HARDENING_COMPLETION_2026-06-05.md`

Checker:
`governance/compat/check_closure_packaging_preflight.py`

It adds an early structural preflight to catch stale closed-artifact wording,
git-derived or bare `rg --files` corpus enumeration, closure diff path
overclaims, and missing checker-recognized core-guard authorization before the
full pre-closure bundle emits a longer finding list.

Superseded next-move note: public-safe memory/learning summary execution is
complete. The MLW-NRD1 source-verified work order authorized by
`docs/baselines/CVF_GC018_MLW_NEXT_RUNTIME_DECISION_2026-06-05.md` is now
ready for operator review.

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Owner Surface

Owner surface: CVF active session startup, continuity routing, and front-door
rule pointers for new or resumed agents.

## Protocol

Agents must treat this file as a compact pointer record, then resolve the
machine-readable registry, active review queue, active handoff, and required
startup guards before material governed work.

## Active Rule Additions

Blind-Spot Prevention Standard upgraded to v2 (2026-06-01). Two new
machine-verifiable rules added based on the LHW20 regression (24 subfolders /
230 files vs claimed 13 / 97):

- **Gate 1 — FILESYSTEM_LISTING_REQUIRED:** Agent MUST run
  `Get-ChildItem -Directory` (or equivalent) on the root folder and include
  raw shell output in Gate 1. Self-reported subfolder counts without shell
  output are not valid evidence; verdict is BLOCKED.
- **Gate 7 — COMPLETENESS_CROSS_CHECK:** Before claiming `CLEAR`, agent MUST
  produce a cross-check table: Gate 1 subfolder list MINUS Gate 3 subfolder
  list = UNREAD set. Each unread subfolder must have an explicit disposition.
  CLEAR without this table is a governance defect.

Active standard: `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

Fast Lane authorization: `docs/baselines/CVF_GC021_BLINDSPOT_STANDARD_UPGRADE_2026-06-01.md`

All future LHW absorption scans must reference the 2026-06-01 version.

Corpus Completeness And Report Integrity is now the general control for any
folder/file-based inventory, report, extraction, comparison, audit, migration,
or knowledge-absorption task:

- Standard:
  `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- Guard:
  `governance/toolkit/05_OPERATION/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD.md`
- Checker:
  `governance/compat/check_corpus_completeness_report_integrity.py`

Before claiming completeness, agents must provide filesystem-backed manifest,
file-level processing ledger, reconciliation, explicit exclusions and
unreadable formats, aggregation check, drift check, traceability, adversarial
verification, and an allowed corpus verdict. `COMPLETE_VERIFIED` requires zero
unresolved files. The guard proves evidence discipline, not perfect semantic
understanding.

Corpus-To-Knowledge-Map Reconciliation is now the follow-on control for
corpus-derived knowledge maps, semantic-region ledgers, architecture
reconciliations, Memory syntheses, graphification plans, and
retrieval-readiness claims:

- Method:
  `docs/reference/CVF_KNOWLEDGE_SYSTEM_METHOD_STANDARD_2026-06-01.md`
- Standard:
  `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
- Guard:
  `governance/toolkit/05_OPERATION/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_GUARD.md`
- Checker:
  `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`

GC-048 distinguishes source authority from rebuildable graph, semantic-region,
Palace, summary, cache, snapshot, and retrieval views. It requires
mapped/deferred/unmapped reconciliation, drift and rebuildability checks,
retrieval boundaries, and adversarial verification.

Work-order dispatch quality is machine-enforced by:

`governance/compat/check_work_order_dispatch_quality.py`

Worker autonomy dispatch prompting is now standardized:

`docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`

READY/DISPATCHED work orders must include a Worker Autonomy / No-Question Rule
so routine allowed-scope remediation is not escalated to the operator as a
preference question.

Governed file-size maintainability now requires proactive rotation/splitting
instead of last-minute text compression when active governed files approach
hard thresholds.

This applies to broad external knowledge absorption records, session front
doors, handoffs, reviews, work orders, and other blocked work classes that
would become hard to test or review if oversized.

Redefine size guard:

`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`

Agent autorun workflow control is mandatory for governed work phases. Agents
must pass the phase wrapper before dispatch, implementation, closure, or push:

`governance/compat/run_agent_autorun_workflow_gate.py`

Canonical autorun standard:

`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Autorun gates are now range-aware. Governed closure must use a captured
`baseHead` and a non-empty committed range; `--base HEAD --head HEAD` is not
valid closure evidence for changed artifacts. Source Verification false
invariants require literal source proof or runtime-path proof.

Latest-closure continuity is now machine-enforced. When a connector wave is
closed, the active front door, state registry, and handoff must all reference
the latest closed LHW wave; stale lower-wave `nextAllowedMove` text blocks the
active-session gate.

Closure finality is now machine-enforced. Closed-equivalent governed artifacts
must not retain `| OPEN |` rows, unchecked `- [ ]` checklist items, stale
roadmap dispatch/hold residue, or Fast Lane active/pass status conflicts.

Status-token and Source Verification symbol hygiene are now machine-enforced:
`HOLD_*`, `DRAFT`, or `PROPOSED` statuses must not contain `CLOSED`, and
`Verified path or symbol` cells must contain only symbols only, not value
assignments such as `rawMemoryReleased: false`.

Allowed-scope and whole-wave range closure hygiene are now machine-enforced:
single-work-order closure ranges must not include files outside Allowed scope,
closed LHW wave roadmaps must be checked with a full T1/T2/T3 changed range,
and connector spec line-count claims must match the current file.

Agent-error learning philosophy is now canonical:

`docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

Repeated agent mistakes are governance training samples, not merely worker
blame. Promote repeated defects from finding to written rule, from rule to
machine check, and from late machine check to the earliest applicable autorun
phase gate.

Allowed-scope gate remediation is now mandatory. If an autorun or machine guard
fails on files/artifacts inside the dispatched work order's Allowed scope, the
assigned agent must repair and rerun the gate instead of asking the non-coder
operator whether to perform routine cleanup. Operator escalation is reserved for
scope expansion, claim-boundary changes, `HOLD_*` release, risk changes,
public-sync, live/provider proof, secrets/quota, forbidden paths, or destructive
operations.

IDE-extension multi-provider execution logging is now machine-enforced:

`docs/reference/CVF_IDE_EXTENSION_MULTI_PROVIDER_EXECUTION_LOG_STANDARD_2026-05-29.md`

`governance/compat/check_multi_provider_execution_log.py`

Mixed-provider sessions using VS Code extension tabs, Antigravity, direct
provider scripts, CLI, MCP, or browser agents must record provider/model,
execution surface, role, evidence basis, commit range, direct-provider-proof
boundary, quality findings, cost attribution, and an Execution Attribution
Block that separates roadmap/order author, worker/executor, and reviewer/closer
when closing governed work or claiming provider effectiveness. Autorun and
local hook chains now fail missing or overclaimed multi-provider execution logs.

Finding-to-governance learning disposition is now machine-enforced:

`docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md`

`governance/compat/check_finding_to_governance_learning.py`

Changed logs, reviews, assessments, or audits that record findings or known
issues must classify each material finding into governance/control-plane,
runtime-behavior, provider-output, cost/economics, or documentation-only
learning lanes, with next control action.

Learning Signal Intake Bridge is now the typed Learning Plane intake route for
those learning lanes:

`docs/reference/CVF_LEARNING_SIGNAL_INTAKE_BRIDGE_STANDARD_2026-05-29.md`

`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`

Runtime/provider/cost candidates, phase-gate placement gaps, design-review
candidates, and machine-check candidates must normalize into
`LearningSignalIntakeRecord` / `LearningFeedbackInput` before a follow-up
roadmap claims Learning Plane routing. Autonomous mutation remains false unless
a separate governed roadmap authorizes it.

Public export disposition is now machine-enforced:

`docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md`

`governance/compat/check_public_export_disposition.py`

Changed closed roadmaps, final wave completion packets, and public catalog
claims must state whether the work is `EXPORTED`, `DEFERRED_PRIVATE_ONLY`, or
`BLOCKED_MISSING_PUBLIC_ARTIFACTS`. Private provenance closure does not imply
public-sync catalog export.

LHW scope rejection is not source rejection. For doc-only LHW connector waves,
families such as `abtop` or `gridex` that require live route execution must be
labeled `rejected from this LHW wave (doc-only scope) - requires live route;
eligible for separate live-proof roadmap post-LHW`, not globally rejected.
Finish absorption of remaining `PARTIALLY_ABSORBED` LH1 connector value before
opening separate live-proof roadmaps.

## Next Allowed Move

LPCI2-T11B Source Verification is `CLOSED_PASS_BOUNDED`.

Completion:
`docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md`

Current mode:
`lpci2_t11b_source_verification_closed_pass_bounded`.

Next allowed move: author a source-verified `LPCI2-T11C Classification
Pre-Check` work order.

T11C must consume T11B resolved-path evidence, carry forward the Unicode
path-fidelity finding, preserve EC-02, and classify only the T11B-verified
target records before T11D readiness aggregation. T11C must not perform body
extraction, OCR, corpus ingestion, chunking, runtime query, provider calls,
public-sync, current-law claims, legal advice quality claims,
production/public readiness claims, memory reinjection, high-risk promotion,
or autonomous mutation. EC-02 freshness review is required on or after
2026-07-01 before any current-law or production runtime claim.

The prior product lanes remain parked: DEP2 next-auth stable migration is
`HARD_BLOCKED`, external receipt-anchor provider/service selection is
`PARKED_PENDING_OPERATOR_DECISION`, and live Redis service proof is
`PARKED_PENDING_CREDENTIALS`.

LHW24 remains the latest closed numbered LHW wave in the state registry.

Blocked without separate authorization and passing phase gates: provider calls,
chat runtime, vector/embedding retrieval, legal advice quality claim,
latest-law claim, public-sync, public/hosted/production readiness claims, QBS
rerun, output-quality parity or L4/L5 quality claim,
cost/performance/provider-quality claims, memory reinjection, high-risk
promotion implementation, Learning Orchestrator runtime behavior, and
autonomous mutation.

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
