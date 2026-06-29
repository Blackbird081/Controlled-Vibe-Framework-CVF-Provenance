# CVF AGSK Package-Candidate Triage Roadmap

Memory class: FULL_RECORD

Status: ACTIVE_TRIAGE

docType: roadmap

Date: 2026-06-29

Batch ID: AGSK-TRIAGE

## Target

Candidates identified in the value conversion matrix of:
`docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md`

Owner surfaces under evaluation:
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md`
- `docs/reference/agent_system_skills/registry/README.md`
- `docs/reference/agent_system_skills/registry/entries/`
- `docs/reference/agent_system_skills/generated/skill-index.json`

## Authorization

Operator-authorized as `nextAllowedMove` in `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
(mode `eavc_t1_value_conversion_guard_closed_pending_agsk_package_candidate_triage`).

Source authorization chain: AGSG-T0 roadmap authorized AGSG-T1/T2/T3; all three closed
`CLOSED_PASS_BOUNDED`. AGSK reabsorption review (`docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md`)
closed `CLOSED_PASS_BOUNDED` with a value conversion matrix identifying candidate lanes.
This triage roadmap is the operator-directed next step before closing the pack or
moving to the next legacy source folder.

Commit mode: WORKER_MUST_NOT_COMMIT

## Non-Goals

Out of scope for this triage and any tranche it opens:

- runtime skill activation;
- provider-backed skill execution;
- external CLI/MCP adapter implementation;
- automatic skill-to-work-order generation;
- promotion of any package beyond its authorized status ceiling (CANDIDATE for T5);
- public catalog claims or public-sync for any package;
- benchmark, security, or production-readiness claims;
- wiring any pack-internal checker from the AGSK absorption pack into CVF;
- re-opening AGSG-T1/T2/T3 decisions already closed.

## Reviewer Correction

Reviewer check found one material defect in the worker-produced triage draft:
CVF does not have zero `CANDIDATE` skill candidates. The existing ASSF registry
source layout already contains `CANDIDATE` entries:

- `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json`

The corrected T5 gap is narrower and still valuable: CVF has no
AGSK-derived external-absorption package candidate, and no candidate entry that
uses the proposed post-T4 `riskTriggers` field. Therefore AGSK-T5 must use the
existing registry source layout rather than inventing an unverified
`packages/.../SKILL.md` package root.

## Design Control Gate

AGSG-T0 `Design Control Gate` applies unchanged:

- All AGSK work must use the existing ASSF reference family as the owner surface.
- Any new field must reconcile against `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
  and `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`.
- No AGSK tranche may introduce a parallel "skill governance engine" vocabulary
  when ASSF vocabulary already owns the concept.
- Package instances must use `skillId` pattern `cvf.<domain>.<capability_name>`.
- Status ceiling per tranche: AGSK-T4 = ADVISORY_READY; AGSK-T5 = CANDIDATE.
  Raising these ceilings requires a separate operator-authorized promotion review.

## Purpose

Make a bounded go/no-go decision for each value-conversion candidate lane from
the AGSK reabsorption review before closing the pack or moving to the next
external source folder under `.private_reference/legacy/CVF 28.06/`. This
triage is operator-authorized work (bootstrap `nextAllowedMove`).

This roadmap decides:
1. which candidate lanes open a new governed tranche;
2. which lanes are VALUE_PARKED pending a concrete reopen condition;
3. which lanes are closed as resolved by prior AGSG-T1/T2/T3 work.

No runtime activation, package instance, provider proof, public-sync, or
benchmark claim is authorized by this triage. Authorized tranches are
documentation-only at `CANDIDATE` or `ADVISORY_READY` status ceiling unless
a subsequent work order explicitly lifts that ceiling with evidence.

## Scope / Methodology

- Source: value conversion matrix from the AGSK reabsorption review (reviewer-closed)
- Prior tranche context: AGSG-T1 (reconciliation), AGSG-T2 (advisory repair),
  AGSG-T3 (checker value decision) - all CLOSED_PASS_BOUNDED
- AGSG Runtime And Adapter Lane - VALUE_PARKED (AGSG-T0 roadmap)
- Design control gate: AGSG-T0 roadmap Design Control Gate applies; new fields
  must reconcile against current ASSF contract rather than introducing parallel vocabulary

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`; inherited source review: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` |
| Enumeration command | Inherited from source review: `Get-ChildItem -Recurse -File ".private_reference\legacy\CVF 28.06\CVF_Agent_Skills_Governance_Absorption_Pack"`; source review reports 29 files |
| Manifest artifact or inline manifest | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Corpus Manifest` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Processing Ledger` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Owner-Surface Map`; this roadmap remaps deferred package/checker lanes to ASSF owner surfaces |
| Unresolved items | 0 unresolved in the inherited corpus review; this roadmap opens AGSK-T4 and AGSK-T5 and parks AGSK-T6 with explicit reopen conditions |
| Completion claim boundary | Triage-route claim only; no new corpus sweep, runtime activation, provider behavior, package activation, public-sync, or production claim |

## Corpus Completeness And Report Integrity

- Corpus task class: TRIAGE_OF_PRIOR_COMPLETE_ABSORPTION
- Corpus root: `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`
- Snapshot time: inherited from `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md`
- Enumeration command: inherited filesystem-backed `Get-ChildItem -Recurse -File ".private_reference\legacy\CVF 28.06\CVF_Agent_Skills_Governance_Absorption_Pack"` from the source review
- Manifest artifact or inline manifest: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Corpus Manifest`
- Manifest hash: inherited hash prefix `249dc5bf1200dbdc` from the source review
- Processing ledger artifact or inline ledger: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Processing Ledger`
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=29; ledger_terminal=29; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: source review reports 8 ADAPTED + 16 NO_NEW_VALUE + 2 DEFERRED + 3 REJECTED = 29
- Drift check: this roadmap does not re-enumerate the local source folder; it relies on the closed source review and narrows deferred lanes into T4/T5/T6
- Output traceability: every opened lane maps to ASSF contract, registry, or advisory owner surfaces named in this roadmap
- Adversarial verification: reviewer corrected the false zero-CANDIDATE claim by checking existing ASSF registry entries before authorizing T5
- Corpus verdict: PARTIAL - triage of prior COMPLETE_VERIFIED source review; no new corpus completeness claim is made here

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | legacy source family -> complete AGSK reabsorption review -> value conversion matrix -> package-candidate triage -> ASSF contract/registry owner surfaces -> source-verified work order before implementation |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json` |
| Disposition | ADAPT as bounded AGSK package-candidate triage roadmap; T4 and T5 open; T6 parked |
| Claim boundary | route-selection only; no runtime activation, provider proof, public-sync, package activation, or production claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| AGSK review rows for files 9-14 and 20-22 | Skill anatomy, anti-rationalization, persona, context, activation, and receipt doctrine already rewritten into ASSF advisory language | DOCTRINE_ADAPTED | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | None; resolved by prior AGSG-T2 advisory repair | Documentation-only doctrine; no runtime or package activation |
| `sample_capability_manifest.json` activation fields | `activation.risk_triggers` gives structured pattern-level escalation not present in current ASSF package contract | PACKAGE_CANDIDATE | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Execute AGSK-T4 before any package candidate consumes the field | Contract field only; cannot grant authority above package authority ceiling |
| `cvf-governance-external-absorption` candidate concept | Existing external absorption governance can become a CANDIDATE registry entry using the post-T4 contract | PACKAGE_CANDIDATE | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`; `docs/reference/agent_system_skills/generated/skill-index.json` | Execute AGSK-T5 after AGSK-T4 closes | Candidate metadata only; no resolver activation, provider call, CLI/MCP adapter, or runtime behavior |
| AGSK activation resolver states | Risk-aware resolver states may become executable selection behavior only after approved package candidates exist | RUNTIME_CANDIDATE | Pending future ASSF runtime or resolver work order | Park until at least one package reaches APPROVED through a later promotion review | No runtime implementation authorized by this roadmap |
| Pack-internal package anatomy checker requirements | Checker requirements may justify a CVF-native package anatomy checker after T4/T5 produce concrete fixtures | CHECKER_CANDIDATE | Pending future `governance/compat` checker work order | Park AGSK-T6 until T4/T5 close and a concrete repeated defect or high-risk gap exists | No checker wiring or hook-chain mutation authorized |
| Pack-internal Python checkers | Direct checker import would create a shadow gate using pack-local schema and tokens | REJECT_DIRECT_IMPORT | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` rejected-items ledger | None; future checker must be CVF-native and source-verified | No direct import, no hook install, no runtime mutation |
| README, TREEVIEW, already-covered evidence receipts | Inventory and summary files add no package/runtime/checker value beyond the closed reabsorption review and prior AGSG owner surfaces | NO_PACKAGE_OR_RUNTIME_VALUE | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` | None; keep as provenance only | No runtime, package, or checker action |

## Candidate Triage Decision Table

Each row corresponds to one lane from the value conversion matrix.

| Lane | Source items | Current CVF coverage | Gap found | Triage decision | Authorized tranche |
|---|---|---|---|---|---|
| DOCTRINE_ADAPTED | Files 9-14, 20-22 (anatomy, anti-rationalization, persona, context, activation, receipt doctrine) | ASSF advisory (`CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md`) at ADVISORY_READY | No gap; doctrine already holds pattern and signal tables | RESOLVED_BY_PRIOR_TRANCHE (AGSG-T2) | None |
| PACKAGE_CANDIDATE - activation sub-fields | File 3 (`sample_capability_manifest.json`): `activation.use_when`, `activation.do_not_use_when`, `activation.risk_triggers` | ASSF package contract has flat `useWhen`, `doNotUseWhen` in Purpose-and-trigger family; `riskCeiling` in Selectors; **no `riskTriggers` list field** | Gap: `riskTriggers` as a structured list of pattern-triggered risk escalation entries is NOT in the current ASSF contract schema | OPEN_TRANCHE -> AGSK-T4 | AGSK-T4 (see Tranche AGSK-T4) |
| PACKAGE_CANDIDATE - contract field standard | File 24 (`CAPABILITY_PACKAGE_CONTRACT.md`): full field list including checker validation requirements | ASSF contract (`CVF_ASSF_PACKAGE_CONTRACT.md`) already covers identity, provenance, purpose, selectors, capability, risk, lifecycle, composition, internal/external disposition, platform, efficiency | Partial gap: contract checker validation requirements exist in the pack but CVF has no machine-enforceable contract anatomy checker; AGSG-T3 deferred checker wiring pending concrete repeated defect | CONDITIONAL - open AGSK-T6 only after AGSK-T4 closes and adds riskTriggers; checker value is insufficient without the new field | VALUE_PARKED_T6_PENDING_T4 |
| RUNTIME_CANDIDATE - activation resolver states | Files 11, 22: risk-aware resolver decision states (deny, optional, required, approval_required, defer) and risk escalation table | ASSF intake normalization contract defines `candidateState`, `APPROVED`, `ACTIVE` lifecycle; no resolver implementation exists | Gap acknowledged; resolver implementation requires package instances first; 0 ACTIVE packages currently | VALUE_PARKED (same as AGSG-T0 runtime lane) | None; reopen condition: at least one package reaches APPROVED state through AGSK-T5 |
| CHECKER_CANDIDATE - package anatomy checker | Files 24, 26-28: checker requirements, pack-internal checker examples | AGSG-T3 evaluated checker value; T3 acceptance criteria required "justified by a concrete repeated defect or high-risk gap" and "CVF-native test fixtures" | No new repeated defect evidence since T3 closed; checker candidate remains conditional on riskTriggers field being added | VALUE_PARKED_T6_PENDING_T4 (same as PACKAGE_CANDIDATE - contract field standard row above) | None |
| AGSK_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE | Capability CVF consistently governs: `cvf-governance-external-absorption` | ASSF registry already has CANDIDATE entries for dispatch quality review and worker return authoring, but none for external absorption and none consuming `riskTriggers` | Gap: no AGSK-derived external-absorption candidate entry exists in the authoritative registry source layout; T5 can prove post-T4 contract fitness without runtime activation | OPEN_TRANCHE -> AGSK-T5 (documentation-only, status ceiling CANDIDATE) | AGSK-T5 (see Tranche AGSK-T5) |
| REJECT_DIRECT_IMPORT - pack-internal checkers | Files 26-28 (Python checkers from the pack) | CVF governance hook chain; AGSG-T3 decision | Rejection confirmed; no gap | RESOLVED_BY_PRIOR_TRANCHE (AGSG-T3 and reabsorption review) | None |

## Tranche AGSK-T4: ASSF Contract `riskTriggers` Field Addition

Status: OPEN

### Objective

Add `riskTriggers` as a structured field in the "Purpose and trigger" or
"Risk and authority" family of `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`.

`riskTriggers` models pattern-triggered risk escalation entries beyond a flat
ceiling: each trigger is a {pattern, condition, escalated_risk_class} triplet.
This is a documentation-only contract change; it does not create package
instances, a resolver, or runtime behavior.

### Source Evidence

- `sample_capability_manifest.json` (file 3 in reabsorption review), field
  `activation.risk_triggers`: structured list; each entry has `condition`,
  `escalated_risk`, and `required_approval` sub-fields.
- Current ASSF contract "Purpose and trigger" family: `useWhen`, `doNotUseWhen`
  (flat strings or lists); "Selectors" family: `riskCeiling` (single value).
- Gap: no entry-level risk escalation trigger list; current schema cannot express
  "if the input mentions X, escalate risk class from R1 to R2 and require
  approval".

### Minimum Outputs

- Patch to `CVF_ASSF_PACKAGE_CONTRACT.md`: add `riskTriggers` to the compact
  machine source schema field families table and to the risk fields reference
  table; write a rule for it (list of trigger entries; each entry must name a
  pattern, escalated risk class, and any required approval or safe-stop override).
- Source verification row in the updated contract: trace `riskTriggers` to the
  capability manifest JSON evidence and to the current ASSF-T1 risk field table.
- Finding-to-governance learning entry: record this as a `RULE_GAP` that the
  prior T1 contract authoring did not anticipate pattern-level risk escalation.
- Updated `CVF_ASSF_PACKAGE_CONTRACT.md` version line and status annotation
  noting T4 repair.
- Status ceiling: `ADVISORY_READY` - the field definition is advisory until a
  checker enforces it.
- No package instances, resolver changes, hook installs, or runtime claims.

### Acceptance Criteria

- `riskTriggers` appears in the compact machine source schema table with a rule.
- Rule specifies: entry structure (pattern, escalated_risk_class,
  required_approval OR safe_stop), minimum cardinality (zero or more entries),
  and authority ceiling (riskTriggers cannot grant authority beyond the package's
  authorityCeiling).
- Source verification row traces to the capability manifest JSON.
- Finding-to-governance learning entry uses GC-049 canonical vocabulary.
- All governance gate runners pass on the changed range.
- No runtime, provider, package instance, or production claim.

### GC-018 Candidate Block

```
GC-018 Continuation Candidate
- Candidate ID: AGSK-T4-riskTriggers-field-2026-06-29
- Date: 2026-06-29
- Parent roadmap / wave: docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md
- Proposed scope: add riskTriggers field to CVF_ASSF_PACKAGE_CONTRACT.md; documentation-only contract repair
- Continuation class: STRUCTURAL
- Active quality assessment: N/A with reason: triage roadmap is a new dispatch, not a reopening of a closed materially-delivered batch
- Assessment date: 2026-06-29
- Weighted total: N/A with reason (new dispatch)
- Lowest dimension: N/A with reason (new dispatch)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: concrete proven gap (riskTriggers absent from ASSF schema); documentation-only change; no runtime or package-instance risk
- Quality protection commitments: change must be source-verified against the capability manifest JSON; must not alter any existing required field; status ceiling ADVISORY_READY
- Why now: triage is operator-authorized as next-allowed-move; deferred riskTriggers gap becomes stale if not addressed before package instances are authored in T5
- Active-path impact: LIMITED (documentation-only ASSF contract repair; does not change any implemented checker or runtime)
- Risk if deferred: T5 package instances authored with incomplete contract schema will not have a riskTriggers entry, creating a contract drift defect
- Lateral alternative considered: YES
- Why not lateral shift: existing ASSF contract is the correct owner surface; alternative would be adding the field to the ASSF advisory, but the advisory is not machine-checkable and the contract is the authority for the field schema
- Real decision boundary improved: YES
- Expected enforcement class: GOVERNANCE_DECISION_GATE (advisory-only until AGSK-T6 checker is opened)
- Required evidence if approved:
  - updated CVF_ASSF_PACKAGE_CONTRACT.md with riskTriggers field in compact machine source schema table
  - source verification row tracing riskTriggers to sample_capability_manifest.json
  - finding-to-governance learning entry

Depth Audit
- Risk reduction: 1
- Decision value: 2
- Machine enforceability: 1
- Operational efficiency: 1
- Portfolio priority: 1
- Total: 6
- Decision: CONTINUE
- Reason: concrete schema gap with low-risk documentation-only fix; improves T5 contract precision

Authorization Boundary
- Authorized now: YES
- If YES, next batch name: AGSK-T4
- If NO, reopen trigger: N/A
```

## Tranche AGSK-T5: First AGSK External-Absorption Package Candidate

Status: OPEN (dependent on AGSK-T4 close for correct contract fields)

### Objective

Author the first AGSK-derived external-absorption skill candidate
`cvf-governance-external-absorption` at `CANDIDATE` lifecycle state,
demonstrating the ASSF package contract shape with a real CVF capability. The
external absorption capability is chosen because:
- CVF has the most governed evidence for it (two closed checker tranches, a
  standard, a chain map, and a multi-file review);
- it is documentation-only and does not require provider or runtime proof;
- it gives the ASSF package contract a concrete worked example that future
  packages can reference.

### Source Evidence

- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` -
  defines the governed process for external absorption;
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` -
  defines the chain map route;
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` (current
  plus T4 `riskTriggers`) - the contract the package must conform to;
- `docs/reference/agent_system_skills/registry/README.md` - authoritative
  source layout and generator flow for skill candidate entries;
- `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`
  and `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json`
  - existing CANDIDATE entries and registry field examples;
- `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` -
  provides the manifest, ledger, and triage evidence proving the capability is real.

### Minimum Outputs

- `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`
  with all compact machine source schema required field families: Identity,
  Provenance, Purpose and trigger (including `riskTriggers`), Selectors,
  Capability, Risk and authority, Lifecycle (status=CANDIDATE), Composition,
  Internal disposition, External disposition, Platform.
- Regenerated `docs/reference/agent_system_skills/generated/skill-index.json`
  using `python governance/compat/generate_assf_skill_index.py --generate`.
- Drift proof using `python governance/compat/check_assf_skill_index_drift.py`.
- Status in the registry entry: `CANDIDATE` - not selectable for resolver use
  until promoted through a separate governed review.
- Source verification section in a paired commit note or worker-return packet
  tracing each schema field back to the ASSF contract.
- No resolver implementation, no CLI/MCP adapter, no runtime claim, no provider
  proof, no public-sync.

### Acceptance Criteria

- Registry entry conforms to all ASSF contract required fields (post-T4 schema
  including `riskTriggers`) and follows the existing registry source layout.
- `status = CANDIDATE` and `candidateState = CANDIDATE`; no higher lifecycle
  state claimed.
- `externalCliMcpDisposition = DEFERRED_WITH_REASON` (no adapter authorized).
- `registryOrder` uses the next available value after existing entries.
- Generated skill index is regenerated from source and drift check passes.
- Finding-to-governance learning entry maps this to the `VALUE_CONVERSION_GAP`
  defect class from the reabsorption review (prior AGSK closure did not produce a package instance).
- All governance gate runners pass on the changed range.
- No runtime, provider, package-instance activation, or production claim.

### GC-018 Candidate Block

```
GC-018 Continuation Candidate
- Candidate ID: AGSK-T5-first-package-instance-2026-06-29
- Date: 2026-06-29
- Parent roadmap / wave: docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md
- Proposed scope: author AGSK-derived external-absorption skill candidate cvf-governance-external-absorption at CANDIDATE state
- Continuation class: STRUCTURAL
- Active quality assessment: N/A with reason: new dispatch, not a reopening of a materially-delivered batch
- Assessment date: 2026-06-29
- Weighted total: N/A with reason (new dispatch)
- Lowest dimension: N/A with reason (new dispatch)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: no AGSK-derived external-absorption candidate exists; a CANDIDATE-state registry entry proves post-T4 contract fitness without runtime risk
- Quality protection commitments: status ceiling CANDIDATE; no resolver, no CLI/MCP adapter; no promotion without separate review; generated index must be source-regenerated
- Why now: triage is operator-authorized; AGSK-T4 adds riskTriggers which T5 should consume; deferring T5 means the riskTriggers field will have no concrete consumer
- Active-path impact: LIMITED (one registry source entry plus regenerated index; no runtime surface modified)
- Risk if deferred: AGSK reabsorption remains pattern-only; riskTriggers field added in T4 has no concrete candidate consumer
- Lateral alternative considered: YES
- Why not lateral shift: the ASSF contract requires a real package to be the authority test; an abstract mock would not prove contract fitness
- Real decision boundary improved: YES
- Expected enforcement class: GOVERNANCE_DECISION_GATE (CANDIDATE state; no runtime gate until promotion)
- Required evidence if approved:
  - docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json (status=CANDIDATE)
  - regenerated docs/reference/agent_system_skills/generated/skill-index.json
  - check_assf_skill_index_drift.py PASS
  - source verification tracing each schema field to the ASSF contract

Depth Audit
- Risk reduction: 1
- Decision value: 2
- Machine enforceability: 1
- Operational efficiency: 1
- Portfolio priority: 2
- Total: 7
- Decision: CONTINUE
- Reason: first AGSK-derived external-absorption candidate proves post-T4 contract fitness; documentation-only, low risk

Authorization Boundary
- Authorized now: YES (pending AGSK-T4 close to get correct riskTriggers field definition)
- If YES, next batch name: AGSK-T5
- If NO, reopen trigger: N/A
```

## Tranche AGSK-T6: ASSF Package Anatomy Checker (Parked)

Status: VALUE_PARKED

Reopen condition: reopen only after AGSK-T4 closes (riskTriggers field defined)
AND AGSK-T5 closes (first AGSK-derived candidate authored). A concrete repeated defect
or high-risk gap must be demonstrated by the T5 package instance before a checker
is worth adding. Until then, AGSG-T3's value-decision result (defer checker until
gap is proven) stands.

Blocked work:
- wiring any pack-internal checker into CVF governance hook chain;
- adding a CVF-native `check_assf_capability_package_anatomy.py` without prior
  package instance evidence;
- claiming checker-supported status for any package without a wired checker.

## Parked Lanes Summary

| Lane | Parked reason | Reopen condition |
|---|---|---|
| AGSK Runtime And Adapter Lane | No ACTIVE packages; same as AGSG-T0 VALUE_PARKED decision | At least one package reaches APPROVED state through AGSK-T5 promotion review |
| AGSK-T6 Package Anatomy Checker | No post-T4 `riskTriggers` candidate to test against; no repeated defect since AGSG-T3 | AGSK-T4 and AGSK-T5 both closed; concrete defect or gap demonstrated |
| Additional AGSK/external-absorption skill candidates (T5+) | T5 must prove contract shape for this lane before adding more AGSK-derived entries | Operator selects next candidate after T5 closes; must each follow ASSF contract and registry source layout |
| External CLI/MCP skill projection | Dual-agent standard requires separate adapter authorization | Separate runtime/adapter work order with source verification and provider proof |

## Work Plan

### AGSK-T4: ASSF Contract riskTriggers Field Addition

Status: OPEN

See Tranche AGSK-T4 above for full objective, minimum outputs, and GC-018 candidate block.

Summary: documentation-only patch to `CVF_ASSF_PACKAGE_CONTRACT.md` adding
`riskTriggers` field with entry structure rule; source-verified against
`sample_capability_manifest.json`; status ceiling ADVISORY_READY.

### AGSK-T5: First AGSK External-Absorption Package Candidate

Status: OPEN (start after AGSK-T4 closes)

See Tranche AGSK-T5 above for full objective, minimum outputs, and GC-018 candidate block.

Summary: author `cvf-governance-external-absorption` registry entry at
`CANDIDATE` lifecycle state under
`docs/reference/agent_system_skills/registry/entries/`; regenerate the skill
index; demonstrate ASSF contract schema with a concrete CVF capability;
documentation-only.

### AGSK-T6: ASSF Package Anatomy Checker

Status: VALUE_PARKED

See Tranche AGSK-T6 above for reopen condition and blocked work.

## Acceptance Criteria

For this triage roadmap:

- Each candidate lane has an explicit decision (OPEN_TRANCHE, VALUE_PARKED,
  RESOLVED_BY_PRIOR_TRANCHE) in the candidate triage decision table.
- Each OPEN_TRANCHE decision has a GC-018 candidate block with a depth audit
  and an authorization boundary.
- Each VALUE_PARKED lane has an explicit reopen condition.
- No runtime, package instance, checker implementation, provider proof,
  public-sync, or promotion claim is made by the triage itself.

For AGSK-T4 (riskTriggers field):

- `riskTriggers` field appears in the ASSF contract compact machine source
  schema table with entry structure rule and authority ceiling constraint.
- Source verification row traces the field to `sample_capability_manifest.json`.
- All governance gate runners pass on the committed range.

For AGSK-T5 (first AGSK external-absorption package candidate):

- `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`
  produced and conforming to all ASSF required field families.
- `candidateState = CANDIDATE` in the registry entry.
- External disposition = `DEFERRED_WITH_REASON` in the registry entry.
- `docs/reference/agent_system_skills/generated/skill-index.json` regenerated
  from the registry sources.
- All governance gate runners pass on the committed range.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/agent_system_skills/registry/README.md`; `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json`; `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| Runtime behavior claimed | N/A_WITH_REASON: this roadmap performs documentation, intake routing, and candidate-tranche authorization only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior, provider routing, or model/API behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports bounded roadmap routing only; implementation requires fresh AGSK-T4 and AGSK-T5 governed work |

## Verification

Gate runners to run after each tranche commit (on the real committed range, not `HEAD..HEAD`):

- `python governance/compat/check_markdown_structural_completeness.py --base <base> --head HEAD --enforce`
- `python governance/compat/check_epistemic_process_packet.py --base <base> --head HEAD --enforce`
- `python governance/compat/check_depth_audit_continuation_compat.py --base <base> --head HEAD --enforce`
- `git diff --name-status <base> HEAD`
- `git status --short`

For AGSK-T4 (contract patch):

- `python governance/compat/check_markdown_structural_completeness.py --enforce` on the changed contract
- Manual source verification: confirm `riskTriggers` field traces to `sample_capability_manifest.json` lines

For AGSK-T5 (package candidate):

- `python governance/compat/generate_assf_skill_index.py --generate`
- `python governance/compat/check_assf_skill_index_drift.py`
- Compact source schema field family check against ASSF contract required families

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: operator-directed triage roadmap, no separate work order changed in this batch | no work order path changed | N/A with reason |
| Completion or reviewer artifact | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | `Status: ACTIVE_TRIAGE`; reviewer correction block present | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | current top `Status: ACTIVE_TRIAGE`; AGSK-T4 and AGSK-T5 opened; AGSK-T6 parked | PASS |
| Registry JSON | `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json` | existing registry source layout verified; no registry mutation authorized until AGSK-T5 | PASS |
| Registry Markdown | `docs/reference/agent_system_skills/registry/README.md` | registry source and generator flow verified; roadmap directs T5 to this owner surface | PASS |
| External evidence digest | N/A with reason: external evidence is inherited from the closed AGSK reabsorption review manifest and ledger, not a new external artifact digest | no new external evidence digest path changed | N/A with reason |
| System loop interlock | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_corpus_completeness_report_integrity.py` | direct gates pass on `0f95454c..HEAD`; reviewer-fast rerun required before commit | PASS |
| Session continuity | N/A with reason: material roadmap commit does not change session state; reviewer/closer session-sync commit follows after material commit if accepted | no session state path changed in this material artifact | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| AGSK-TRIAGE-Q1 | `docs/reference/agent_system_skills/registry/entries/` | CANDIDATE entry count before T5 | at least 1 existing CANDIDATE entry | 2 existing entries: `cvf-dispatch-quality-reviewer`, `cvf-worker-return-author` | PASS |
| AGSK-TRIAGE-Q2 | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `riskTriggers` field presence before T4 | absent before T4 | absent; T4 required | PASS |
| AGSK-TRIAGE-Q3 | external absorption core gate | violations | 0 | 0 on `0f95454c..HEAD` | PASS |
| AGSK-TRIAGE-Q4 | external absorption value conversion gate | violations | 0 | 0 on `0f95454c..HEAD` | PASS |
| AGSK-TRIAGE-Q5 | corpus completeness gate | violations | 0 | 0 on `0f95454c..HEAD` | PASS |

## Claim Boundary

This roadmap decides which candidate lanes open new tranches. It does not:
- create any package instance;
- implement any checker;
- activate any skill;
- prove any runtime or provider behavior;
- grant production, public-sync, or promotion authority.

AGSK-T4 and AGSK-T5 are documentation-only with status ceilings `ADVISORY_READY`
and `CANDIDATE` respectively. Promotion beyond these ceilings requires a separate
operator-authorized review with source verification, governance gate evidence,
and explicit promotion authorization.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap cites `.private_reference/legacy/` paths and private AGSK
reabsorption provenance. Public-safe publication requires separate redaction and
public-sync authorization.
