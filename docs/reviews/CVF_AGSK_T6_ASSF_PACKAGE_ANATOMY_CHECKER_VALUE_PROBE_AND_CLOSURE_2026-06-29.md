# CVF AGSK-T6 ASSF Package Anatomy Checker Value Probe And Closure

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-29

docType: review

Batch ID: AGSK-T6

## Purpose

Close the remaining AGSK checker blind-spot question before moving to another
external repo or folder: determine whether post-AGSK-T7 ASSF registry
candidates need a CVF-native anatomy checker, and implement only the bounded
checker if the value probe finds a real machine-check gap.

## Target

Target owner surfaces:

- `governance/compat/check_assf_package_candidate_anatomy.py`
- `governance/compat/test_check_assf_package_candidate_anatomy.py`
- ASSF hook and autorun catalogs
- ASSF registry entries and generated skill index

No package root, `SKILL.md`, resolver mutation, runtime activation,
provider/live proof, public-sync, external CLI/MCP adapter, package activation,
lifecycle promotion, direct pack checker import, or production-readiness claim
is included.

## Scope / Methodology

Method:

1. Started from clean session-sync HEAD `95220004`.
2. Audited current ASSF gates and all nine registry source entries.
3. Found a concrete anatomy gap: existing gates did not require every registry
   candidate to carry all required ASSF field-family fields, and two older
   entries lacked the post-AGSK-T4 `riskTriggers` field.
4. Added a CVF-native read-only package anatomy checker and focused unit tests.
5. Backfilled `riskTriggers: []` into the two older entries where no
   source-backed trigger list exists.
6. Regenerated the generated skill index through the existing generator.
7. Wired the checker into reviewer-fast, pre-commit, pre-push, and autorun
   command catalogs.

## Findings / Position

AGSK-T6 is justified. The gap is not speculative:

- `check_assf_skill_index_drift.py` only proves generated-index drift.
- `check_assf_certified_metadata_admission.py` only applies detailed boundary
  checks to entries with `certificationState=CERTIFIED`.
- `check_assf_external_agent_metadata_readout.py` only proves external readout
  allowlisting and adapter-boundary text.
- Before AGSK-T6, two real entries were missing `riskTriggers` even though the
  ASSF contract now requires it in the purpose-and-trigger field family.

The checker is therefore implemented, not merely parked.

## Risk / Corrective Action

Risk controlled:

- checker is read-only;
- focused tests cover pass and negative cases;
- hook wiring uses existing ASSF gate placement;
- two legacy entries are backfilled with `riskTriggers: []`, preserving
  zero-or-more contract semantics without inventing unsupported triggers;
- generated index is regenerated from source entries;
- no external pack checker code is imported.

Corrective action completed: future ASSF registry candidates cannot silently
omit required anatomy fields, lifecycle coupling, loader-boundary language,
external disposition, risk classes, or `riskTriggers`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| AGSK-T6 reopen condition is satisfied after T4 and T5/T7 candidate fixtures | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Tranche AGSK-T6; Parked Lanes Summary | AGSK-T6 Package Anatomy Checker | AGSK triage roadmap | VALUE_SET | ACCEPT |
| AGSK-T7 created multiple registry candidate fixtures | `docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md` | Registry Candidate Coverage Table | six candidate entries | AGSK-T7 worker return | EXISTS | ACCEPT |
| ASSF contract requires `riskTriggers` in the purpose-and-trigger field family | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | riskTriggers | ASSF package contract | VALUE_SET | ACCEPT |
| Registry sources are authoritative and generated index must be regenerated | `docs/reference/agent_system_skills/registry/README.md` | Purpose; Adding A New Entry | entries; generated skill index | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| Existing certified checker only checks detailed boundary for CERTIFIED entries | `governance/compat/check_assf_certified_metadata_admission.py` | check loop | certificationState | certified metadata admission checker | RUNTIME_BEHAVIOR | ACCEPT |
| Existing external readout checker checks metadata readout allowlisting, not registry anatomy | `governance/compat/check_assf_external_agent_metadata_readout.py` | `check_payload` | ALLOWED_SKILL_FIELDS | external readout checker | RUNTIME_BEHAVIOR | ACCEPT |
| Existing generator validates aggregate drift from source entries | `governance/compat/generate_assf_skill_index.py` | `validate_index_matches_sources` | validate_index_matches_sources | ASSF index generator | RUNTIME_BEHAVIOR | ACCEPT |
| New checker validates required field-family anatomy for registry entries | `governance/compat/check_assf_package_candidate_anatomy.py` | `REQUIRED_FIELDS`; `check` | check | AGSK-T6 checker | DOC_ONLY_NEW | ACCEPT |
| Focused tests cover missing riskTriggers and boundary failures | `governance/compat/test_check_assf_package_candidate_anatomy.py` | test methods | test_missing_risk_triggers_fails | AGSK-T6 tests | DOC_ONLY_NEW | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | ASSF contract, registry README, registry entries, generated index, generator, existing ASSF checkers, new checker |
| Registry entries checked | 9 entries under `docs/reference/agent_system_skills/registry/entries/` |
| Gap observed before repair | two older entries lacked `riskTriggers`; no all-candidate anatomy checker existed |
| Runtime behavior claimed | N/A_WITH_REASON: deterministic local checker only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync authorized |
| Freshness disposition | PASS - current source supports bounded checker implementation and registry backfill |

## Checker Value Probe Matrix

| Probe question | Evidence | Decision |
|---|---|---|
| Does current drift checker enforce field-family anatomy? | `generate_assf_skill_index.py` validates aggregate equality only | NO |
| Does certified metadata checker cover all candidates? | detailed checks run only for `certificationState=CERTIFIED` | NO |
| Does external readout checker cover source entry anatomy? | readout allowlist check only | NO |
| Is there a real data defect, not hypothetical value? | `cvf-dispatch-quality-reviewer.json` and `cvf-worker-return-author.json` lacked `riskTriggers` | YES |
| Can a bounded CVF-native checker close the gap without runtime activation? | new read-only checker plus focused tests | YES |
| Should AGSK pack checker code be imported directly? | prior AGSK review rejected direct pack checker import | NO |

## Implementation Summary

| Surface | Change | Boundary |
|---|---|---|
| `governance/compat/check_assf_package_candidate_anatomy.py` | added read-only all-entry anatomy checker | no provider, runtime, resolver, package activation, or filesystem mutation |
| `governance/compat/test_check_assf_package_candidate_anatomy.py` | added five focused unit tests | local deterministic tests only |
| ASSF hook/autorun catalogs | wired checker into reviewer-fast, pre-commit, pre-push, and autorun command catalog | same ASSF gate family as existing certified/readout checks |
| two ASSF-T2 registry entries | added `riskTriggers: []` | zero-or-more field backfill; no trigger invented |
| generated index | regenerated from registry sources | generator-owned aggregate only |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement and wire the AGSK-T6 ASSF package
candidate anatomy checker, focused tests, ASSF hook catalog entries, registry
backfill, generated index regeneration, and this closure review.

Protected paths:

- `governance/compat/check_assf_package_candidate_anatomy.py`
- `governance/compat/test_check_assf_package_candidate_anatomy.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Operator authorization: operator explicitly asked to reopen AGSK-T6 and truly
finish the AGSK repo/folder before moving to another external repo.

Rollback boundary: revert the AGSK-T6 material commit only; if reverting,
remove the checker/test/hook wiring, remove the two `riskTriggers` backfills,
regenerate the skill index, and leave AGSK-T7 material commit `aa4d932a`
intact unless separately reopened.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`; inherited source review: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` |
| Enumeration command | inherited from source review: `Get-ChildItem -Recurse -File ".private_reference\legacy\CVF 28.06\CVF_Agent_Skills_Governance_Absorption_Pack"` |
| Manifest artifact or inline manifest | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Corpus Manifest` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Processing Ledger` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | AGSK-T6 owner surfaces are `governance/compat/`, ASSF registry entries, and generated skill index |
| Unresolved items | 0 unresolved in inherited review; AGSK-T6 resolves the package-anatomy checker candidate |
| Completion claim boundary | AGSK-T6 checker and registry-shape closeout only; no new corpus sweep, runtime, provider, package activation, public-sync, or production claim |

## Corpus Completeness And Report Integrity

- Corpus task class: CHECKER_VALUE_PROBE_FOR_PRIOR_COMPLETE_ABSORPTION
- Corpus root: `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`
- Snapshot time: inherited from AGSK reabsorption review
- Enumeration command: inherited filesystem-backed `Get-ChildItem -Recurse -File ".private_reference\legacy\CVF 28.06\CVF_Agent_Skills_Governance_Absorption_Pack"`
- Manifest artifact or inline manifest: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Corpus Manifest`
- Manifest hash: inherited hash prefix `249dc5bf1200dbdc`
- Processing ledger artifact or inline ledger: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Processing Ledger`
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=29; ledger_terminal=29; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: inherited source review reports 8 ADAPTED + 16 NO_NEW_VALUE + 2 DEFERRED + 3 REJECTED = 29
- Drift check: AGSK-T6 performs targeted checker value probe after AGSK-T7 candidate creation
- Output traceability: checker value maps to AGSK triage T6, T7 candidate fixtures, and ASSF contract field families
- Adversarial verification: checker implementation does not imply package activation
- Corpus verdict: PARTIAL - checker value probe based on prior COMPLETE_VERIFIED review and post-T7 fixtures

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | legacy source family -> AGSK reabsorption review -> AGSK triage roadmap -> AGSK-T7 candidate fixtures -> AGSK-T6 CVF-native anatomy checker |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| Owner surface | `governance/compat/check_assf_package_candidate_anatomy.py`; `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json` |
| Disposition | ADAPT checker candidate into CVF-native deterministic anatomy checker and registry backfill |
| Claim boundary | checker and metadata-only registry shape; no runtime, provider, package activation, external adapter, public-sync, or production claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| AGSK triage T6 checker candidate | package anatomy checker value after concrete fixtures | CHECKER_CANDIDATE | `governance/compat/check_assf_package_candidate_anatomy.py` | implemented by AGSK-T6 | read-only checker only |
| AGSK-T7 candidate fixtures | multiple ASSF entries expose real field-family validation target | CHECKER_FIXTURE | ASSF registry entries | consumed by checker and tests | metadata-only |
| ASSF-T4 `riskTriggers` field | required field-family entry absent in two older candidates | REGISTRY_BACKFILL | two ASSF-T2 registry entries | added `riskTriggers: []` and regenerated index | no lifecycle promotion |
| pack-internal Python checkers | direct import remains rejected | REJECT_DIRECT_IMPORT | none | none | no direct import |
| activation resolver runtime states | executable resolver remains conditional | RUNTIME_CANDIDATE | conditional future work order | remains parked | no runtime in AGSK-T6 |

## Mandatory Blind-Spot Control Block

| Gate | Evidence |
|---|---|
| Gate 1: absorption source enumerated | inherited from AGSK reabsorption review (29 files enumerated) |
| Gate 2: all files listed | inherited source review lists 29 files with full manifest |
| Gate 3: each file has terminal status | inherited source review processing ledger has terminal rows for all 29 files |
| Gate 4: reconciliation passes | inherited: manifest=29; ledger_terminal=29; unresolved=0 |
| Gate 5: adapted/deferred items traced | AGSK-T6 traces the deferred checker candidate to a CVF-native checker and closes the package-anatomy machine-check gap |
| Blind-spot verdict | CLEAR_FOR_AGSK_T6_CHECKER_VALUE_AND_IMPLEMENTATION |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | `MACHINE_CHECK_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `CHECKER_IMPLEMENTED_AND_WIRED` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` |
| Next control action | AGSK package-anatomy checker now runs in reviewer-fast, pre-commit, pre-push, and autorun command catalog |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: If AGSK-T6 is worth opening, current ASSF
candidate fixtures should reveal a gap that existing ASSF gates do not cover.

Evidence Comparison: The audit found exactly that gap: two source entries lacked
`riskTriggers`, while existing ASSF gates did not require all candidate entries
to carry the full field-family anatomy.

Contradiction Or Gap Disposition: The initial possibility that AGSK-T6 could
remain parked is rejected because a real machine-check gap exists.

Claim Update: AGSK-T6 changes from value-parked checker candidate to
implemented bounded checker; runtime and adapter lanes remain parked.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-T6 deterministic ASSF package candidate anatomy checker |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - focused unit tests, direct checker run, ASSF drift and boundary checks, reviewer-fast/pre-commit gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT - checker, tests, hook wiring, registry backfill, generated index |
| invocationBoundary | local deterministic governance checker only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | validates registry candidate anatomy and bounded metadata fields |
| forbiddenExpansion | no runtime, provider/live, resolver mutation, package body, `SKILL.md`, external adapter, direct pack checker import, public-sync, package activation, lifecycle promotion, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | Codex local workspace |
| Session or invocation | AGSK-T6 checker value probe and implementation, 2026-06-29 |
| Working directory | repository root |
| Command or tool surface | source reads, JSON audit, apply_patch, generator, unittest, governance gates |
| Target paths | AGSK-T6 checker/test/hook wiring, two ASSF registry entries, generated index, this review |
| Allowed scope source | operator requested AGSK-T6 reopen to finish AGSK repo/folder before moving to another repo |
| Before status evidence | clean HEAD `95220004`; AGSK-T7 closed at `aa4d932a` |
| After status evidence | material paths pending review/commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | AGSK-T6 checker and registry-shape repair only |
| Claim boundary | repo-local deterministic checker; no runtime/provider/public claim |
| Agent type | reviewer/closer |
| Invocation ID | `agsk-t6-assf-package-anatomy-checker-2026-06-29` |
| Expected manifest | `governance/compat/check_assf_package_candidate_anatomy.py`; `governance/compat/test_check_assf_package_candidate_anatomy.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`; `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json`; `docs/reference/agent_system_skills/generated/skill-index.json`; `docs/reviews/CVF_AGSK_T6_ASSF_PACKAGE_ANATOMY_CHECKER_VALUE_PROBE_AND_CLOSURE_2026-06-29.md` |
| Actual changed set | `governance/compat/check_assf_package_candidate_anatomy.py`; `governance/compat/test_check_assf_package_candidate_anatomy.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`; `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json`; `docs/reference/agent_system_skills/generated/skill-index.json`; `docs/reviews/CVF_AGSK_T6_ASSF_PACKAGE_ANATOMY_CHECKER_VALUE_PROBE_AND_CLOSURE_2026-06-29.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator directly authorized AGSK-T6 value-probe and implementation in this reviewer/closer batch | no separate work order changed | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_T6_ASSF_PACKAGE_ANATOMY_CHECKER_VALUE_PROBE_AND_CLOSURE_2026-06-29.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | AGSK-T6 parked condition satisfied by AGSK-T7 fixtures and this closure | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`; `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` | `riskTriggers: []` present; generated index drift check PASS | PASS |
| Registry Markdown | `docs/reference/agent_system_skills/registry/README.md` | registry source/generator discipline preserved; no markdown registry change required | PASS |
| External evidence digest | N/A with reason: inherited AGSK reabsorption manifest/ledger digest is cited; no new external digest created | no new external source artifact changed | N/A with reason |
| System loop interlock | ASSF hook/autorun catalogs | checker listed in reviewer-fast, pre-commit, pre-push, and autorun command catalog | PASS |
| Checker source | `governance/compat/check_assf_package_candidate_anatomy.py` | direct checker PASS | PASS |
| Focused tests | `governance/compat/test_check_assf_package_candidate_anatomy.py` | `python -m unittest governance.compat.test_check_assf_package_candidate_anatomy` ran 5 tests OK | PASS |
| Session continuity | active state/front door/handoff | N/A with reason: session-sync is a separate post-material commit if AGSK-T6 material is accepted | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this closure cites private AGSK provenance under `.private_reference/legacy/`.
Public-safe publication requires separate redaction and public-sync authorization.

## Claim Boundary

AGSK-T6 closes only the ASSF package-candidate anatomy checker gap for the AGSK
absorption pack. It does not activate any skill, create package bodies, import
external checker code, implement resolver/runtime behavior, expose CLI/MCP
adapters, perform provider/live proof, publish public artifacts, promote
candidate lifecycle state, or claim production readiness.
