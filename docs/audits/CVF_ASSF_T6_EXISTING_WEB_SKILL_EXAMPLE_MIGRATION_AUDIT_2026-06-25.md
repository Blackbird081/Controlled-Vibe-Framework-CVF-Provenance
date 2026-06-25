# CVF ASSF-T6 Existing Web Skill Example Migration Audit

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-06-25

docType: audit

Batch ID: ASSF-T6

## Purpose

Enumerate current CVF Web skill and template surfaces, classify each against
the ASSF-T6 Web Projection Contract vocabulary, and record the migration
disposition for each. This audit is input to future ASSF-T7 certification
planning and does not activate, certify, or promote any example.

## Scope And Methodology

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/` skill and template
surfaces as of execution base HEAD `ffa421f2`.

Enumeration was performed using filesystem-backed directory walk covering
`rg --files --hidden --no-ignore EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`
filtered to `(skill|template|spec-first|recommender|types)` patterns. The
worker recorded exact found paths; no exhaustive coverage is claimed beyond the
executed search root.

## Enumeration Commands And Evidence

### Command 1: File enumeration

```
python -c "
import os, re
root = 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src'
pat = re.compile(r'(skill|template|spec.first|recommender|types)', re.IGNORECASE)
for dirpath, dirs, files in os.walk(root):
    for f in files:
        rel = os.path.join(dirpath, f).replace(chr(92), '/')
        if pat.search(rel):
            print(rel)
"
```

Result (57 paths found under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`):

```
actions/skills.ts
app/(dashboard)/skills/page.tsx
app/(dashboard)/skills/search/page.tsx
app/(dashboard)/skills/[domain]/[skill]/page.tsx
app/landing/components/TemplateShowcase.tsx
components/SkillDetailView.test.tsx
components/SkillDetailView.tsx
components/SkillGraph.tsx
components/SkillLibrary.i18n.test.tsx
components/SkillLibrary.test.tsx
components/SkillLibrary.tsx
components/SkillPlanner.test.tsx
components/SkillPlanner.tsx
components/SkillSearch.test.tsx
components/SkillSearchBar.tsx
components/TemplateCard.tsx
components/TemplateMarketplace.tsx
components/TemplatePreviewModal.tsx
components/TemplateSuggester.tsx
components/__fixtures__/skills-index.fixture.json
data/skill-template-map.json
lib/front-door-template-standard.test.ts
lib/frontdoor-skills.ts
lib/skill-corpus-governance.test.ts
lib/skill-planner.test.ts
lib/skill-planner.ts
lib/skill-search.test.ts
lib/skill-search.ts
lib/skill-template-map.test.ts
lib/skill-template-map.ts
lib/spec-first-mediation.test.ts
lib/spec-first-mediation.ts
lib/template-i18n.test.ts
lib/template-i18n.ts
lib/template-intent.ts
lib/template-loader.test.ts
lib/template-loader.ts
lib/template-recommender.test.ts
lib/template-recommender.ts
lib/templates/business.ts
lib/templates/content.ts
lib/templates/development.ts
lib/templates/governance-enforcement.test.ts
lib/templates/hr.ts
lib/templates/index.test.ts
lib/templates/index.ts
lib/templates/marketing.ts
lib/templates/product.ts
lib/templates/research.ts
lib/templates/security.ts
lib/templates/technical.ts
types/governance-engine.ts
types/index.ts
types/skill.ts
types/workflow-pack.ts
lib/ai/types.ts
lib/lpci/types.ec02.test.ts
lib/lpci/types.ts
```

### Command 2: Template-to-skill mapping data

Key values read from `data/skill-template-map.json` (full file read):
- 67 `templateToSkillMap` entries mapping template IDs to legacy domain/skillId pairs
- 2 exempt template IDs (`individual_skills_folder`, `vibe_workflow_folder`) with recorded exemption reason
- 10 `categoryToDomainMap` entries

### Command 3: Mapping function verification

Read from `lib/skill-template-map.ts`:
- Header comment confirms: "Templates = INPUT side (help users create specs via forms) / Skills = KNOWLEDGE side (detailed governance + UAT metadata)"
- Exports: `templateToSkillMap`, `getSkillForTemplate`, `getTemplatesForSkill`, `getTemplatesForDomain`, `categoryToDomainMap`

### Command 4: Web Skill type interface

Read from `types/skill.ts`:
- `Skill` interface fields include: `id`, `title`, `domain`, `difficulty`, `summary`, `path`, `content`, `riskLevel`, `allowedRoles`, `allowedPhases`, `authorityScope`, `autonomy`, `uatStatus`, `specScore`, `corpusClass`, `frontDoorVisible`, `frontDoorTier`, `trustedBenchmarkSurface`, `linkedTemplates`, `corpusNote`
- Notably: no `certificationState` field from ASSF-T1 -- the Web Skill type predates ASSF certification architecture

## Risk / Corrective Action

Risk: classifying any entry as `CERTIFIED_PACKAGE_PROJECTION` without
certification evidence, or omitting the external-agent CLI/MCP disposition,
would create a false certification claim or governance gap.

Corrective action: all 67 `templateToSkillMap` entries, 2 folder templates, and
10 category-to-domain mappings were classified using only the projection contract
vocabulary; `CERTIFIED_PACKAGE_PROJECTION` was not assigned to any entry;
`DEFERRED_WITH_REASON` was applied to all external-agent dispositions.

## Findings / Key Finding

No current CVF Web skill or template example holds ASSF-T1 package
certification. The Web `Skill` interface does not include `certificationState`
from the ASSF-T1 Compact Machine Source Schema. The `templateToSkillMap`
references legacy skill library entries (`domain` + `skillId` pairs) that
predate ASSF governance. The front-door skills fetch (`fetchFrontDoorSkillRecords`)
is a read-only display feed from `skill-index.json`, not an activation channel.

This is consistent with the epistemic prediction: existing Web examples are
presentation mappings or candidates, not certified ASSF package projections.

## Classification Ledger

Classification vocabulary defined in `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md`.

### Group 1: Template-to-Skill Mapping Entries (67 entries)

All 67 entries in `data/skill-template-map.json > templateToSkillMap` share the same disposition:

| Attribute | Value |
|---|---|
| Surface | `data/skill-template-map.json` `templateToSkillMap` object |
| Reference type | Legacy skill domain/skillId mapping (e.g., `{ "domain": "business_analysis", "skillId": "04_business_plan" }`) |
| ASSF certification evidence | NONE -- no package registry entry, no `certificationState` |
| Classification | `PACKAGE_CANDIDATE` |
| Reason | Entries map template IDs to legacy skill library entries; they predate ASSF certification; any future certified package projection must go through ASSF-T7+ certification and then update this mapping |
| Next action | No immediate action; mapping may be updated by a future ASSF-T7+ certification work order when individual legacy skills are certified as ASSF packages |

Representative sample (full list of 67 entries is in `data/skill-template-map.json`):

| Template ID | Domain | Skill ID | Classification |
|---|---|---|---|
| `business_strategy_wizard` | `business_analysis` | `04_business_plan` | `PACKAGE_CANDIDATE` |
| `strategy_analysis` | `business_analysis` | `01_strategy_analysis` | `PACKAGE_CANDIDATE` |
| `risk_assessment` | `business_analysis` | `02_risk_assessment` | `PACKAGE_CANDIDATE` |
| `system_design_wizard` | `technical_review` | `02_architecture_review` | `PACKAGE_CANDIDATE` |
| `code_review` | `technical_review` | `01_code_review` | `PACKAGE_CANDIDATE` |
| `documentation` | `content_creation` | `01_documentation` | `PACKAGE_CANDIDATE` |
| `app_builder_wizard` | `app_development` | `01_app_requirements_spec` | `PACKAGE_CANDIDATE` |
| `vibe_to_spec` | `app_development` | `01_app_requirements_spec` | `PACKAGE_CANDIDATE` |
| `api_design` | `app_development` | `05_api_design_spec` | `PACKAGE_CANDIDATE` |
| `seo_audit` | `marketing_seo` | `01_seo_audit` | `PACKAGE_CANDIDATE` |
| `web_ux_redesign_system` | `product_ux` | `cvf_web_ux_redesign_system` | `PACKAGE_CANDIDATE` |
| `web_build_handoff` | `product_ux` | `cvf_web_ux_redesign_system` | `PACKAGE_CANDIDATE` |
| `gdpr_compliance` | `security_compliance` | `02_data_privacy_compliance` | `PACKAGE_CANDIDATE` |
| `data_analysis_wizard` | `finance_analytics` | `01_finance_analysis_system` | `PACKAGE_CANDIDATE` |
| ... (53 additional entries follow same pattern) | | | `PACKAGE_CANDIDATE` |

### Group 2: Exempt Template IDs (2 entries)

| Template ID | Exemption reason | Classification |
|---|---|---|
| `individual_skills_folder` | Folder-navigation surface with `isFolder=true`; child templates carry skill mappings; exempted at 2026-05-20 by HN1 Fast-Lane audit | `LEGACY_REFERENCE_ONLY` |
| `vibe_workflow_folder` | Folder-navigation surface with `isFolder=true`; child templates carry skill mappings; exempted at 2026-05-20 by HN1 Fast-Lane audit | `LEGACY_REFERENCE_ONLY` |

Reason: folder-navigation surfaces are not skill documents and are not ASSF package candidates without separate review of their child structures.

### Group 3: Category-to-Domain Map (10 categories)

| Category | Domain | Classification |
|---|---|---|
| `business` | `business_analysis` | `LEGACY_REFERENCE_ONLY` |
| `technical` | `technical_review` | `LEGACY_REFERENCE_ONLY` |
| `content` | `content_creation` | `LEGACY_REFERENCE_ONLY` |
| `development` | `app_development` | `LEGACY_REFERENCE_ONLY` |
| `marketing` | `marketing_seo` | `LEGACY_REFERENCE_ONLY` |
| `product` | `product_ux` | `LEGACY_REFERENCE_ONLY` |
| `security` | `security_compliance` | `LEGACY_REFERENCE_ONLY` |
| `research` | `ai_ml_evaluation` | `LEGACY_REFERENCE_ONLY` |
| `finance` | `finance_analytics` | `LEGACY_REFERENCE_ONLY` |
| `hr` | `hr_operations` | `LEGACY_REFERENCE_ONLY` |

Reason: category-to-domain mappings are UI routing hints only, not skill or package definitions. They cannot be certified without a separate per-domain ASSF certification work order.

### Group 4: CVF Web Skill Runtime Components (display surfaces)

| Surface | Classification | Reason |
|---|---|---|
| `components/SkillLibrary.tsx` | `LEGACY_REFERENCE_ONLY` | Read-only display component; no ASSF certification claim |
| `components/SkillDetailView.tsx` | `LEGACY_REFERENCE_ONLY` | Read-only display component |
| `components/SkillGraph.tsx` | `LEGACY_REFERENCE_ONLY` | Visualization surface; no package authority |
| `components/SkillPlanner.tsx` | `LEGACY_REFERENCE_ONLY` | Planning UI; no activation |
| `components/SkillSearchBar.tsx` | `LEGACY_REFERENCE_ONLY` | Search UI only |
| `components/TemplateSuggester.tsx` | `LEGACY_REFERENCE_ONLY` | Recommendation UI; no authority |
| `lib/frontdoor-skills.ts` | `LEGACY_REFERENCE_ONLY` | Read-only display feed; not an activation channel |
| `lib/skill-planner.ts` | `LEGACY_REFERENCE_ONLY` | Planning logic; no package instance creation |
| `lib/skill-search.ts` | `LEGACY_REFERENCE_ONLY` | Search index logic; no authority |
| `lib/template-recommender.ts` | `LEGACY_REFERENCE_ONLY` | Recommendation logic; no authority |
| `types/skill.ts` | `LEGACY_REFERENCE_ONLY` | Web-only type surface; `corpusClass` field predates ASSF `certificationState` |

### Group 5: `CERTIFIED_PACKAGE_PROJECTION` Entries

None found. No existing CVF Web skill or template example has ASSF-T1+ package
certification evidence. No entries qualify for `CERTIFIED_PACKAGE_PROJECTION`
at this audit date.

### Group 6: `REJECTED_WITH_REASON` Entries

None found. No existing example requires rejection; all are classified as
candidate or legacy reference.

## Summary Table

| Classification token | Count | Notes |
|---|---|---|
| `CERTIFIED_PACKAGE_PROJECTION` | 0 | None; ASSF-T7 certification not yet performed |
| `PACKAGE_CANDIDATE` | 67 | All `templateToSkillMap` entries; candidates for future ASSF-T7 certification |
| `LEGACY_REFERENCE_ONLY` | 12 + 10 + 2 = 24 (plus runtime components) | Category map, folder templates, display components |
| `DUPLICATE_OR_SUPERSEDED` | 0 | None found |
| `REJECTED_WITH_REASON` | 0 | None found |

## External-Agent CLI/MCP Disposition

No existing CVF Web skill or template surface may be read by an external agent
through an authorized CLI/MCP adapter -- because no adapter contract exists
at this audit date. Any future external projection readout requires a separate
source-verified adapter work order citing this audit and the T6 projection
contract.

Disposition for all audited entries: `DEFERRED_WITH_REASON` for external-agent
CLI/MCP access.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | ASSF_WEB_PROJECTION_INTERNAL_GATE |
| Matching local-view guard | N/A with reason -- no external knowledge guard needed; all sources are CVF-owned repository files at HEAD `ffa421f2` |
| Owner surface | CVF internal Web source files (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/`) and ASSF-T1 package contract |
| Disposition | `N/A_WITH_REASON` -- no external knowledge, external-agent packet, or external return was consumed; Web source files are CVF-owned repository artifacts consulted as internal source evidence only |
| Route | T6 Web surfaces consumed as internal source evidence for classification |
| Boundary | no external-agent packet or provider knowledge elevated to CVF authority |
| External-agent disposition | `DEFERRED_WITH_REASON` |
| Claim boundary | no external knowledge absorption claim |

## Finding-To-Governance Learning Disposition

- Defect class: `RULE_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `DESIGN_REVIEW_REQUIRED`
- Next control action: ASSF-T7 must bridge the `corpusClass` -> `certificationState` schema gap and certify individual packages before any Web example may be classified `CERTIFIED_PACKAGE_PROJECTION`.

- Finding: No existing CVF Web skill or template example qualifies as `CERTIFIED_PACKAGE_PROJECTION`.
- Finding: CVF Web `Skill` type uses `corpusClass` not ASSF-T1 `certificationState`; schema gap confirmed.

- Runtime/provider/cost learning lane: `N/A_WITH_REASON` -- T6 is a documentation and audit tranche; no runtime execution is performed.

## Rescan Intelligence Hardening

- Original source artifact: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` at HEAD `ffa421f2`
- Predecessor intake artifact: N/A with reason -- T6 is the first formal classification audit for this surface
- Delta ledger status: N/A with reason -- first audit; no prior delta; baseline classification established
- Routing matrix status: REFRESHED -- see Follow-Up Routing Matrix below
- Semantic sampling status: COMPLETE -- one adversarial sample below
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Record |
|---|---|
| `UNCHANGED_FROM_INTAKE` | N/A with reason: first audit; no predecessor intake for this surface |
| `CHANGED_DISPOSITION` | N/A with reason: first audit; no prior classification to compare |
| `NEW_FINDING` | schema gap (`corpusClass` vs `certificationState`) confirmed; 67 entries classified `PACKAGE_CANDIDATE`; 0 entries `CERTIFIED_PACKAGE_PROJECTION` |
| `REMOVED_OR_REJECTED` | N/A with reason: no prior classifications to remove |

### Follow-Up Routing Matrix

| Routing lane | Record |
|---|---|
| `DO_NOW` | all 67 template-map entries, 2 folder templates, and 10 category-to-domain mappings classified; audit ledger authored; schema gap recorded |
| `SEPARATE_RUNTIME_TRANCHE` | Web route/component changes, package activation, and CLI/MCP adapter require a separately authorized tranche |
| `STRATEGIC_OPERATOR_DECISION` | operator should select ASSF-T7 (certification, UAT, drift detection, deprecation, and retirement guard) or another governed lane |
| `OUT_OF_SCOPE` | ASSF-T7 package certification, Web type bridge (`corpusClass` -> `certificationState`), CLI/MCP adapter, public-sync, runtime/provider/live, package instances, SKILL.md, skill.source.json |
| `RESOLVED_BY_DESIGN` | contract-only scope resolves certification-overreach risk by design; no-activation invariant prevents unauthorized projection |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T6-AU-S1 | Classification Ledger Group 1 | `web_ux_redesign_system` classified `PACKAGE_CANDIDATE` | T1 schema requires ULID-format `certificationState`; Web uses `corpusClass` | could `cvf_web_ux_redesign_system` be a valid ASSF package ID? | REJECT -- ASSF-T1 requires ULID format; `cvf_web_ux_redesign_system` is a legacy skill library path fragment; `PACKAGE_CANDIDATE` confirmed |
| ASSF-T6-AU-S2 | Classification Ledger Group 1 | `web_build_handoff` classified `PACKAGE_CANDIDATE` | same schema gap applies | could any current entry meet T1 certification requirements? | REJECT -- no entry has a ULID package ID, `certificationState`, or GC-018 evidence; all remain `PACKAGE_CANDIDATE` |

## Corpus Completeness And Report Integrity

- Corpus task class: REFERENCE_AUDIT_CLASSIFICATION.
- Corpus root: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/` skill and template surfaces enumerated at HEAD `ffa421f2`.
- Snapshot time: 2026-06-25, worker execution session.
- Enumeration command: filesystem-backed walk using `rg --files --hidden --no-ignore` equivalent (Python `os.walk` over the same root); bounded to paths matching `(skill|template|spec-first|recommender|types)` pattern.
- Manifest artifact or inline manifest: Classification Ledger table and Enumeration Evidence section above.
- Manifest hash: N/A with reason: text-only audit; no binary artifact to hash.
- Processing ledger artifact or inline ledger: Classification Ledger groups 1-6 above.
- Allowed terminal statuses: `CLASSIFIED` for all audited entries; `READ` for all named source files reviewed; `SKIPPED_WITH_REASON` not used; `DEFERRED` not used; `BLOCKED_UNREADABLE` not encountered.
- Reconciliation: manifest=67_template_map_entries_plus_2_exempt_plus_category_and_display_components; ledger_terminal=all_entries_classified; exclusions=runtime implementation, generated-index mutation, package instance creation; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: audit does not claim exhaustive coverage of all 57 matched paths; focuses on classification-relevant data surfaces (`skill-template-map.json`, `types/skill.ts`, `frontdoor-skills.ts`) and representative component list.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: T6 is an audit tranche and creates no generated aggregate.
- Drift check: N/A with reason: T6 creates no generated aggregate.
- Output traceability: all classified entries are recorded in the Classification Ledger table; source facts are in the Source Verification Block and Enumeration Commands And Evidence section.
- Adversarial verification: no classification token was assigned without verifying against the projection contract vocabulary; `CERTIFIED_PACKAGE_PROJECTION` was confirmed absent; the schema gap was verified by direct inspection of `types/skill.ts` vs T1 `certificationState`.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| `templateToSkillMap` has 67 entries across legacy domains | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` | `templateToSkillMap` | `templateToSkillMap` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| Two folder templates are exempt from skill mapping | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json` | `exemptTemplateIds` | `exemptTemplateIds` | CVF Web skill-template mapping | EXISTS | ACCEPT |
| Web `Skill` interface uses `corpusClass` not ASSF `certificationState` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | `Skill` interface | `corpusClass` | CVF Web Skill type | EXISTS | ACCEPT |
| Front-door skills fetch is read-only display; not activation | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | `fetchFrontDoorSkillRecords` | `fetchFrontDoorSkillRecords` | CVF Web frontdoor-skills | EXISTS | ACCEPT |
| Template aggregation is a UI composition of domain templates | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/index.ts` | `export const templates` | `templates` | CVF Web template aggregator | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Reference audit and classification`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects:
- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0006: Source Verification symbol cell contains a value/type
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class

Remediation applied:
- ADIF-0001: Enumeration records exact search root and bounded results; no claim to exhaustive Web source coverage.
- ADIF-0002: Source verification uses current repository files read at HEAD `ffa421f2`; no provider-local memory cited.
- ADIF-0006: Symbol cells contain bare field names and function names only.
- ADIF-0007: Scope exclusions are in the Scope section; not used as evidence for classification or registries.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | This audit and the T6 projection contract | Internal agents may read classification dispositions and use them for T7 planning; they may not promote any entry to certified without T7 evidence | T6 projection contract, T1 package contract, this audit classification ledger | no internal activation or registry mutation is authorized by this audit | `AUDIT_CLASSIFICATION_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | Future external CLI/MCP that queries projection metadata | No external agent may activate, certify, or mutate entries based on this audit; adapter authorization requires a separate work order | T6 projection contract adapter-separation invariant, T1 `externalCliMcpDisposition` field | all classified entries carry `DEFERRED_WITH_REASON` for external CLI/MCP access | `DEFERRED_WITH_REASON` |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T6 existing Web skill/template example migration audit |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- documentation and classification only |
| receiptEvidence | N/A with reason: no runtime execution or provider call |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- enumeration commands, read evidence, and classification ledger |
| invocationBoundary | governed local repository audit only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, or Web runtime interception claim |
| claimLanguage | classifies existing Web examples for future migration planning; does not activate, certify, or promote any example |
| forbiddenExpansion | no package instance creation, registry entry, SKILL.md, generated-index mutation, runtime code, CLI/MCP adapter, public-sync, session state edit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: references private provenance repository paths and internal architecture
governance. Public-safe export requires separate redaction and public-sync
authorization.

## Claim Boundary

This audit classifies existing CVF Web skill and template surfaces for future
migration planning. It does not certify any package, activate any skill, change
CVF Web runtime surfaces, create any package instance, or authorize CLI/MCP
adapter behavior. No package activation claim. No public-sync claim.
