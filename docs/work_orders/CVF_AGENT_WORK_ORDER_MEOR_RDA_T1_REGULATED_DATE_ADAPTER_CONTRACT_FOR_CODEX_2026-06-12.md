# CVF Agent Work Order: MEOR-RDA-T1 Regulated-Date Adapter Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-12

Worker: Codex

Reviewer: Codex in separated reviewer pass

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `d1140459`

executionBaseHead: `d1140459`

closureBaseHead: `43f83c9f`

GC-018:
`docs/baselines/CVF_GC018_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_2026-06-12.md`

Parent roadmap:
`docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md`

## Purpose

Author the specification-only regulated-date adapter contract and JSON
semantics that map regulated-domain lifecycle concepts into MEOR metadata
requirements.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 continue after MEOR foundation closure | ACCEPT |
| MEOR-T5 completion | `docs/reviews/CVF_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| Parent roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | ACTIVE_RDA_T1_CLOSED_RDA_T2_AUTHORIZATION_READY |
| RDA-T1 GC-018 | `docs/baselines/CVF_GC018_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_2026-06-12.md` | CLOSED_PASS_BOUNDED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Lock adapter semantics before build | author contract and JSON semantics | reference artifacts | JSON parse and review |
| Keep regulated fields profile-scoped | include non-global default rules | contract section | source-verified DSCP profile evidence |
| Preserve MEOR evidence basis | map to MEOR evidence values | semantics JSON | MEOR contract/semantics citations |
| Keep Policy_Local downstream | forbid external path mutation | changed-path proof | git diff/status |
| Prepare implementation safely | define RDA-T2 handoff boundary | completion review | claim boundary |

## Intake Role Routing Decision

- Intake summary: after MEOR foundation closure, define a regulated-domain
  adapter contract before implementation.
- Scope classification: bounded specification-only governance tranche.
- Risk sensitivity: high claim-boundary sensitivity, low runtime risk.
- routeMode: `SINGLE_AGENT_MULTI_ROLE`;
- reason: small contract-authoring tranche with no runtime implementation and
  machine gates available.
- role separation basis: authoring, review, closure, and continuity are
  recorded as separate passes.
- Escalation condition: stop if runtime implementation, external Policy_Local
  edits, provider use, public-sync, or readiness claim expansion becomes
  necessary.

## Single-Agent Multi-Role Control Block

- Role separation ledger: contract author, source verifier, reviewer, and
  continuity updater are separate passes.
- Evidence basis: current source files, canonical contracts, committed MEOR
  closure, machine gates, and changed-path proof.
- Self-review boundary: no independent external review is claimed.
- Escalation conditions: runtime/source edit, external workspace edit,
  provider/API-key use, public-sync, irreversible action, or claim-boundary
  change.
- Gate sequence: reviewer-fast, pre-dispatch, pre-implementation,
  pre-closure, pre-push if push is later authorized.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Source verifier | Codex verification pass | confirm existing fields and owner surfaces |
| Contract author | Codex authoring pass | write adapter contract and JSON semantics |
| Reviewer | Codex review pass | check boundary, examples, and no-runtime scope |
| Continuity updater | Codex sync pass | update state, memory, and handoff |

## Worker Autonomy / No-Question Rule

Repair allowed-scope documentation, continuity, formatting, and gate failures
without asking the operator. Escalate only when the repair would require
runtime/source implementation, external Policy_Local edits, provider use,
public-sync, or claim-boundary expansion.

## Required First Reads

1. Parent RDA roadmap.
2. RDA-T1 GC-018 baseline.
3. MEOR-T5 completion review.
4. MEOR contract and semantics.
5. DSCP profile contract and metadata requirement bridge.
6. LPCI types and EC-02 semantics.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MEOR requirement identity field exists | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | line 56 | `requirementId` | MEOR contract | EXISTS | ACCEPT |
| MEOR observed/evidence/resolution/downstream fields exist | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | lines 58-62 | `observedState`, `evidenceBasis`, `resolutionState`, `downstreamDisposition` | MEOR contract | EXISTS | ACCEPT |
| MEOR semantics contract version exists | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | line 2 | `contractVersion` | MEOR semantics JSON | VALUE_SET | ACCEPT |
| MEOR downstream values include retain/re-evaluate | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | lines 23-24 | `downstreamDispositions` | MEOR semantics JSON | EXISTS | ACCEPT |
| Extraction evaluator exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | line 150 | `evaluate_metadata_evidence` | Python function | EXISTS | ACCEPT |
| Extraction evaluator emits MEOR field names | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | lines 210-214 | `observedState`, `evidenceBasis`, `resolutionState`, `downstreamDisposition` | `adapt_metadata_evaluation_to_scan_finding` output | RUNTIME_BEHAVIOR | ACCEPT |
| DSCP profile metadata requirements exist | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 69-71 | `metadataRequirements` | `DscpDomainProfile` | EXISTS | ACCEPT |
| DSCP regulated support flag exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 67 | `supportsDocumentStatus` | `DscpDomainProfile` | EXISTS | ACCEPT |
| DSCP requirement bridge exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 68 | `buildDscpMetadataRequirementBridge` | TypeScript function | EXISTS | ACCEPT |
| LPCI lifecycle enum exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 20 | `DocumentStatus` | TypeScript type | EXISTS | ACCEPT |
| LPCI lifecycle fields exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 40-42 | `effectiveDate`, `promulgationDate`, `documentStatus` | LPCI record types | EXISTS | ACCEPT |
| EC-02 gate token is documented | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | line 5 | `ec02GateToken` | EC-02 semantics JSON | VALUE_SET | ACCEPT |
| EC-02 hard boundary remains active | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | lines 53-56 | `ec02Boundary`, `noRecordMayReceive` | EC-02 semantics JSON | LITERAL_INVARIANT | ACCEPT |
| EC-T1 accepts documentStatus | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | lines 153-162 | `documentStatus` | EC-T1 decision | VALUE_SET | ACCEPT |
| EC-T1 keeps non-regulatory domains from inheriting lifecycle fields | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | lines 202-225 | `supportsDocumentStatus` | EC-T1 decision | LITERAL_INVARIANT | ACCEPT |
| EC-T1 confirms BLOCKED_UNTIL_2026-07-01 remains active | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | lines 232-251 | `BLOCKED_UNTIL_2026-07-01` | EC-T1 decision | LITERAL_INVARIANT | ACCEPT |

## New Doc-Only Fields

| Proposed field | Artifact owner | Purpose | Runtime status |
| --- | --- | --- | --- |
| `adapterVersion` | RDA-T1 semantics JSON | version the adapter contract | DOC_ONLY_NEW |
| `regulatedConceptMappings` | RDA-T1 semantics JSON | map domain lifecycle concepts to MEOR requirement IDs | DOC_ONLY_NEW |
| `regulatedProfileEligibility` | RDA-T1 semantics JSON | record profile-scoped eligibility rules | DOC_ONLY_NEW |
| `nonRegulatoryDefaultDisposition` | RDA-T1 semantics JSON | specify NOT_APPLICABLE behavior for non-regulatory profiles | DOC_ONLY_NEW |
| `downstreamGateCandidate` | RDA-T1 semantics JSON | document later EC gate candidate without activating runtime | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

Runtime/source freshness was checked at base `d1140459` using direct source
files named in the Source Verification Table. RDA-T1 does not claim newly
implemented runtime behavior. It authorizes contract and JSON semantics only.

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:
`docs/reviews/CVF_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_COMPLETION_2026-06-12.md`

priorVerificationAnchor: `6c2ad2b3`

freshRecomputeRequired: NO

RDA-T1 reuses MEOR-T5 closure evidence for the foundation release boundary and
uses the Source Verification Table above for current repo source facts. It
does not consume external Policy_Local evidence, source bundles, binary hashes,
or extracted text.

unicodePathHandling: `N/A with reason - RDA-T1 does not open Unicode external paths or extracted-text paths; any future path handling must use literal paths and UTF-8-safe readers.`

extractedTextAuthority: `N/A with reason`

Encoding rule: all new RDA-T1 artifacts must default to ASCII. If an evidence
quote or path requires non-ASCII, the artifact must record the exception and
reason.

## Pre-Flight Checks

1. Confirm MEOR-T5 closure commit `6c2ad2b3` and sync `d1140459`.
2. Confirm parent roadmap, GC-018, and this work order are in dispatch state.
3. Confirm Source Verification rows cite existing files and source line
   evidence.
4. Confirm no external Policy_Local path is changed.
5. Run reviewer-fast and pre-dispatch autorun before closure execution.

## Allowed Scope

- RDA-T1 baseline, work order, contract, semantics, examples, completion;
- parent RDA roadmap;
- active state, memory, and handoff continuity.

## Forbidden Scope

- runtime/source implementation;
- external Policy_Local paths;
- candidate metadata correction;
- EC-T5/EC-T6 activation;
- retrieval, OCR, corpus ingestion, provider/API-key use;
- public-sync, production readiness, or public readiness.

## Required Artifact Manifest

| Artifact | Required action | Notes |
| --- | --- | --- |
| `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_CONTRACT_2026-06-12.md` | CREATE | canonical adapter contract |
| `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | CREATE | machine-readable semantics |
| `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | CREATE | completion review |
| parent roadmap | UPDATE | T1 closure state |
| this work order | UPDATE | closure state |
| active continuity | UPDATE | next allowed move |

## Work-Order Fulfillment Manifest

| Required artifact | Fulfillment rule | Closure status before execution |
| --- | --- | --- |
| Adapter contract | must be created before RDA-T1 closure | PASS |
| Adapter semantics JSON | must parse and align with contract | PASS |
| Completion review | must record bounded closure and gates | PASS |
| Parent roadmap update | must move RDA-T1 to closed or blocked | PASS |
| Continuity update | must name next allowed move | PASS |

## Write Ownership

| Path | Action |
| --- | --- |
| `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_CONTRACT_2026-06-12.md` | CREATE |
| `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | CREATE |
| `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | CREATE |
| RDA-T1 baseline | UPDATE |
| this work order | UPDATE |
| parent RDA roadmap | UPDATE |
| active state, memory, and handoff | UPDATE |
| runtime source and external Policy_Local paths | FORBIDDEN |

## Execution Plan

1. Author the Markdown adapter contract.
2. Author the JSON semantics and parse it.
3. Include regulated and non-regulatory examples.
4. Record invalid combinations and fail-closed rules.
5. Update roadmap/work-order/baseline closure status.
6. Run reviewer-fast and pre-closure gates.
7. Commit and sync continuity.

## Evidence Requirements

- JSON parse evidence;
- source-verification preservation;
- changed-path proof excluding runtime source and external Policy_Local;
- reviewer-fast and pre-closure autorun evidence;
- explicit claim boundary.

## Acceptance Criteria

1. T1 creates contract and semantics only.
2. All new adapter fields are marked doc-only.
3. Regulated lifecycle fields remain profile-scoped.
4. Non-regulatory profiles do not receive lifecycle defaults.
5. `QUERY_CLASS_GATED` is documented as a candidate downstream gate only.
6. No runtime/source or external Policy_Local file changes occur.
7. Closure includes Machine Closure Package, learning disposition, and Public
   Export Disposition.

## Review Gate

Reject closure if it implies metadata truth, legal/current status, Policy_Local
readiness, EC activation, retrieval readiness, provider behavior, public
readiness, or production readiness.

## Closure Checklist

- [x] Contract authored.
- [x] JSON semantics authored and parsed.
- [x] Regulated and non-regulatory examples included.
- [x] No runtime or external use-case changes.
- [x] Reviewer-fast and pre-closure pass.
- [x] Continuity sync completed.

## Return-To-Orchestrator Conditions

Return if RDA-T1 cannot close without runtime changes, external workspace
edits, operator evidence, provider/API-key use, public-sync, or readiness
claim expansion.

## Operator Checkpoint

operator.checkpoint.waiver: operator instructed Codex to continue. No
additional checkpoint is required inside this specification-only scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | parent roadmap | RDA-T1 closed; RDA-T2 ready only for fresh authorization | PASS |
| Registry JSON | N/A with reason: T1 creates docs-only contract artifacts | no registry change because T1 creates no corpus/search/classification source | BLOCKED with reason: not applicable to spec-only RDA-T1 |
| Registry Markdown | N/A with reason: T1 creates docs-only contract artifacts | no registry change because T1 creates no corpus/search/classification source | BLOCKED with reason: not applicable to spec-only RDA-T1 |
| External evidence digest | N/A with reason: repo-local contract work | no external evidence | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation | docs-only contract | N/A with reason |
| Session continuity | active state/memory/handoff | RDA-T1 execution next | PASS |

## Claim Boundary

This work order authorizes specification-only adapter contract work. It does
not authorize runtime implementation, Policy_Local mutation, metadata
correction, EC activation, retrieval, provider use, public-sync, production
readiness, public readiness, or autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private adapter dispatch work order; no public-sync authorized.
