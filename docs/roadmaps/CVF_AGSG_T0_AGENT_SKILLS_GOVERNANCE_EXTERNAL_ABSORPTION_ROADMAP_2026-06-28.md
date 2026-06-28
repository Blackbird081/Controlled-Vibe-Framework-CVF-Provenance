# CVF AGSG-T0 Agent Skills Governance External Absorption Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION

Date: 2026-06-28

docType: roadmap

Batch ID: AGSG-T0

## Purpose

Record the source-verified audit of `addyosmani/agent-skills` and the
operator-supplied `CVF Agent Skills Governance Absorption Pack`, classify
what should be absorbed into CVF, and route the valuable pieces through the
existing Agent System Skills Foundation (ASSF) owner surface rather than
creating a competing skill-governance stack.

This roadmap is an absorption decision and future-work route. It does not
import the upstream plugin, activate skills, install commands, create package
instances, implement runtime selection, or approve external CLI/MCP behavior.

## Authorization / Decision

Operator authorized an external absorption audit for
`https://github.com/addyosmani/agent-skills.git` and the local
`CVF Agent Skills Governance Absorption Pack`. The decision from this audit is:

- absorb high-value skill-governance patterns as advisory input to ASSF;
- route concrete changes through AGSG-T1 source-verified reconciliation;
- move the local pack out of root into private legacy reference storage;
- reject direct import of plugin runtime, slash commands, hooks, personas, and
  prototype checkers until separate governed work proves value and authority.

## Scope

In scope:

- source-read upstream repository content and local pack content;
- classify absorption value against existing CVF owner surfaces;
- record source verification, external intake routing, claim boundary, and
  dual-agent disposition;
- open a roadmap route for the next governed tranche.

## Non-Goals

Out of scope:

- runtime skill activation;
- provider-backed execution proof;
- CLI/MCP adapter implementation;
- package instance creation;
- command or hook installation;
- public-sync or public catalog export;
- static checker implementation;
- benchmark, security, or production-readiness claim.

## Design Control Gate

AGSG work must use the existing ASSF reference family as the owner surface.
Any new field, checker, package anatomy rule, resolver rule, persona rule, or
context-packet rule must first pass AGSG-T1 reconciliation against:

- `docs/reference/agent_system_skills/README.md`;
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`;
- `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md`;
- `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md`;
- `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`.

No AGSG tranche may introduce a parallel "skill governance engine" vocabulary
when ASSF vocabulary already owns the concept.

## External Intake

| Field | Value |
|---|---|
| Upstream repository | `https://github.com/addyosmani/agent-skills.git` |
| Upstream commit audited | `30e55cb06080b3db6d89ab32cf388831e3fbf4cf` |
| Upstream commit date | `2026-06-28T02:51:20-07:00` |
| Upstream commit subject | `Merge pull request #313 from nucliweb/docs/skill-contributing-guardrails` |
| Local operator pack | `CVF Agent Skills Governance Absorption Pack` |
| Local pack disposition | moved to `.private_reference/legacy/CVF_Agent_Skills_Governance_Absorption_Pack` after audit |
| Intake decision | absorb patterns into ASSF-controlled CVF artifacts; do not copy runtime/plugin surfaces |
| Next governed move | AGSG-T1 source-verified ASSF reconciliation baseline and work order |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | `External/corpus/repo input -> input router -> old authority/blind-spot/corpus guards -> external-agent packet/checklist when applicable -> returned-output absorption table when applicable -> promote/adapt/defer/reject/block -> GC-018/work order/source verification/autorun when implementation or governed action is needed` |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; work-order dispatch-quality gate |
| Owner surface | ASSF reference family; AGSG-T1 reconciliation roadmap/work order route |
| Disposition | ADAPT into ASSF-controlled CVF artifacts; REJECT direct plugin/runtime/command/persona/hook import; DEFER checker/runtime/adapter work |
| Claim boundary | no external file becomes CVF authority by itself; no runtime, provider, adapter, public, production, benchmark, or automatic activation claim |

## Source Authority And Verification

External materials are advisory inputs only. CVF authority for skill
governance remains under CVF-governed reference surfaces, session state,
roadmaps, work orders, reviews, and source files.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| CVF already has a canonical agent system-skill reference family | `docs/reference/agent_system_skills/README.md` | `Purpose`; `Scope Boundary`; `Current Disposition` | `docs/reference/agent_system_skills/` | ASSF reference family | ACCEPT |
| ASSF package contract owns skill package shape and boundaries | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `SKILL.md Profile`; `Compact Machine Source Schema`; `Provider Adapter Boundary`; `Claim Boundary` | `CVF_ASSF_PACKAGE_CONTRACT.md` | ASSF package contract | ACCEPT |
| ASSF-T1 does not authorize runtime, package instances, generated index, resolver, public-sync, or CLI/MCP adapter behavior | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `Scope / Applies To`; `Storage Topology`; `Claim Boundary` | ASSF-T1 forbidden expansion | ASSF package contract | ACCEPT |
| ASSF intake normalization already defines external skill intake as CANDIDATE-only with reverification and no self-activation | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | `Purpose`; `No-Self-Activation Invariant`; `Reverification Gate` | `candidateState`; `APPROVED`; `ACTIVE` | ASSF-T4 normalization contract | ACCEPT |
| External CLI/MCP skill projection is deferred and requires separate adapter authorization | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | `Dual Agent Surface Matrix`; `External-Agent CLI/MCP Disposition` | `externalCliMcpDisposition` | ASSF-T4 normalization contract | ACCEPT |
| Dual-agent surfaces must account for internal and external agent consumers | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | `Mandatory Dual Agent Surface Matrix`; `Failure Modes`; `Claim Boundary` | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent surface standard | ACCEPT |
| CVF roles and personas are role lanes, not autonomous authority | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | `Role Assignment Rule`; `Forbidden Moves`; `Legacy Role Template Mapping` | role lane assignment | agent role assignment matrix | ACCEPT |
| Upstream skills are structured around commands, 24 skills, verification, and anti-rationalization tables | `.private_reference/external_repos/agent-skills/README.md` | `Commands`; `All 24 Skills`; `How Skills Work`; `Why Agent Skills?` | `skills/`; `commands/`; `agents/` | upstream advisory source | ACCEPT |
| Upstream skill anatomy requires frontmatter and recommends rationalization, red flag, and verification sections | `.private_reference/external_repos/agent-skills/docs/skill-anatomy.md` | `Skill File`; `Recommended Structure`; `Context Efficiency`; `Validation Checklist` | `SKILL.md`; `name`; `description` | upstream advisory source | ACCEPT |
| Upstream personas are separate from skills and commands, and personas do not call other personas | `.private_reference/external_repos/agent-skills/docs/agents.md` | `How personas relate to skills and commands`; `Rules for personas` | `Skill`; `Persona`; `Command` | upstream advisory source | ACCEPT |
| Upstream validator enforces frontmatter, section checks, and validator-owned exemptions | `.private_reference/external_repos/agent-skills/scripts/validate-skills.js` | `REQUIRED_SECTIONS`; `SECTION_EXEMPT_SKILLS`; `validateSkill` | `REQUIRED_SECTIONS` | upstream advisory source | ACCEPT |
| Local pack explicitly bounds itself to `ABSORPTION_SPEC_ONLY` and excludes runtime/provider claims | `.private_reference/legacy/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/00_SCOPE_AND_CLAIM_BOUNDARY.md` | `Scope`; `Out of scope`; `Prohibited claims`; `Runtime upgrade path` | `ABSORPTION_SPEC_ONLY` | local advisory pack | ACCEPT |
| Local pack proposes capability package, activation resolver, anti-rationalization, context, persona, and evidence receipt patterns | `.private_reference/legacy/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/03_ABSORPTION_MAP.md` | `Absorption map`; `Risk map`; `Claim boundary` | capability package mapping | local advisory pack | ACCEPT |

## External Evidence Manifest

| Source | Audited artifact | SHA-256 |
|---|---|---|
| upstream | `README.md` | `68F8BD0777211B4B368722B5DA9849D23D9BACCD660DA294E68B14C24D267FBB` |
| upstream | `docs/skill-anatomy.md` | `3A5F57BDB384AEF91723BF6F4CAEC780E15A7A1E34453CEC41D73419AC187989` |
| upstream | `docs/agents.md` | `FF4FCF35EB98CED49E3F87AE1C443535CB5EADDFF25EFE0BCA916C856B816F60` |
| upstream | `scripts/validate-skills.js` | `C1B48EFE1DE1FA41F3A07179FCF1AE80A9E40F9E408C209021B95016EF6AE895` |
| upstream | `skills/using-agent-skills/SKILL.md` | `0C34BE229C87FBB61DC8B645E7F91D1A9103214D363D0F6BEA78F1FACB8928E3` |
| upstream | `skills/spec-driven-development/SKILL.md` | `62A904BD7DE79E8833D92086FE5DE8A48D1D964B06416C82AA34422C17066774` |
| upstream | `skills/incremental-implementation/SKILL.md` | `3C39229FCC03856CF99D68672442E2DD1083F09BA75678E9AF0216A8BCA4E642` |
| local pack | `00_SCOPE_AND_CLAIM_BOUNDARY.md` | `8AB56812C0FA9F036003D81C0CAA3D8255E046EBA3AF15D5892E2EEA92FCF15D` |
| local pack | `01_AGENT_SKILLS_REPO_AUDIT.md` | `DE82B657E8E558B83251862A59CC4C0760E0157C3620A3B7575FBA5C7863DC92` |
| local pack | `04_CVF_CAPABILITY_PACKAGE_STANDARD.md` | `49362F55E75670A951CC1AA34D30CC082E3450B5C69FC86492C9A3475E0122DF` |
| local pack | `05_SKILL_ACTIVATION_RESOLVER.md` | `4C930941A6E6F4F6D36C45497030002FE8F1E844CFCCD24C3D42BCF29E7BBEE2` |
| local pack | `06_ANTI_RATIONALIZATION_GUARD.md` | `49D8439B9FAE6E211D947600C53EFAF2A79BBA2461A083F850A00C12B53AE450` |
| local pack | `07_PERSONA_ORCHESTRATION_BOUNDARY.md` | `B021596C4BA48B58CE2AB3C0E5CF087569CD2876D4C4AEA1CECC17A550F0C9E8` |
| local pack | `10_VERIFICATION_AND_EVIDENCE_RECEIPT.md` | `1F6B42D81013CEBE5A1F46F0D4278AD4885677A4ACF98B4BDBF9605F07B01BA8` |
| local pack | `governance/compat/check_skill_capability_claim_boundary.py` | `4776DE6AC668ABD666885189538D14AF619322F7938EBF8911AD1AF3DAB81625` |

## Audit Findings

### High-Value Patterns

| Pattern | Value to CVF | Absorption route |
|---|---|---|
| Skill anatomy with `name`, `description`, trigger, process, red flags, verification | Gives ASSF a practical package-shape lens beyond abstract schema fields | Reconcile with ASSF-T1 `SKILL.md Profile` and compact source schema |
| Anti-rationalization tables | Converts common agent excuses into reviewable guard signals | Evaluate as ASSF/ADIF/guard advisory input before any checker |
| Progressive disclosure | Matches CVF's need to load metadata before full instruction bodies | Reconcile with ASSF-T1 `resolverBehavior` and ASSF-T2 metadata resolver boundary |
| Persona, command, skill separation | Helps avoid unmanaged multi-agent role expansion | Map to CVF role matrix, handoff, and dual-agent standards |
| Validator-owned exemptions | Useful pattern for preventing self-declared bypasses in candidate packages | Candidate AGSG-T3 checker/value decision after T1 reconciliation |
| Evidence-first verification language | Reinforces CVF closure rule: activation or advisory use is not proof | Map into ASSF evidence requirements and work-order receipts |

### Rejected Direct Imports

| Upstream or pack surface | Decision | Reason |
|---|---|---|
| Upstream plugin install flow | REJECT_DIRECT_IMPORT | Provider/plugin installation is not CVF authority and would bypass ASSF intake gates |
| Upstream slash commands | REJECT_DIRECT_IMPORT | CVF already owns phase gates and work-order dispatch; slash commands can only inform phase mapping |
| Upstream personas as autonomous subagents | REJECT_DIRECT_IMPORT | CVF roles require bounded assignment, handoff, and reviewer control |
| Upstream hooks and platform setup docs | REJECT_DIRECT_IMPORT | Runtime/provider behavior requires separate source-verified work order and evidence |
| Local pack prototype checkers | DEFER_TO_VALUE_DECISION | Useful concepts, but CVF should not add duplicate checkers until ASSF gaps are source-verified |
| Local pack extension folder | REJECT_DIRECT_IMPORT | It is an external-agent advisory scaffold, not a CVF-owned extension release |

## Work Plan

### AGSG-T1: Source-Verified ASSF Reconciliation

Status: PROPOSED_NEXT

Objective: compare upstream and local-pack patterns against the current ASSF
contracts, generated index, resolver, normalization contract, role matrix,
dual-agent surface standard, and template-skill guard. Produce a bounded
reconciliation artifact that says which concepts are already covered, which
need wording repair, and which should route to ASSF-T5 or later checker work.

Minimum outputs:

- GC-018 baseline and work order for `AGSG-T1`;
- source verification table against current CVF owner surfaces;
- no duplicate package standard unless a concrete ASSF gap is proven;
- finding-to-governance-learning table for each accepted pattern;
- explicit value-parked rows for low-value or already-covered lanes;
- updated session/handoff state after commit.

Acceptance criteria:

- every accepted pattern maps to an existing CVF owner surface or to a named
  follow-up tranche;
- every rejected/deferred pattern has a concrete reopen condition;
- no runtime, provider, CLI/MCP, public, benchmark, or automatic activation
  claim is made;
- local pack remains in legacy and is not cited as canonical authority.

### AGSG-T2: ASSF Capability Advisory Repair

Status: HOLD_UNTIL_AGSG_T1_PASS

Objective: only if T1 proves a gap, author a compact CVF reference addendum or
ASSF contract patch for capability anatomy, anti-rationalization, progressive
context, receipt shape, or persona boundary. The patch must reuse ASSF terms
instead of introducing a parallel "skill governance engine" vocabulary.

Acceptance criteria:

- patch is limited to current ASSF owner files or a clearly named reference
  addendum;
- any new field is marked as existing source, new doc-only field, or blocked;
- dual-agent surface matrix records internal and external CLI/MCP disposition;
- no package instance or runtime selector is created.

### AGSG-T3: Static Checker And Value Decision

Status: HOLD_UNTIL_AGSG_T1_PASS

Objective: decide whether a checker is worth adding for capability-package
claim boundary, validator-owned exemptions, or resolver schema drift. Prototype
checker ideas from the local pack may be reused only after adapting them to
current ASSF field names and CVF guard conventions.

Acceptance criteria:

- checker value is justified by a concrete repeated defect or high-risk gap;
- test fixtures are CVF-native and do not depend on the legacy pack path;
- checker is wired only through authorized guard surfaces;
- no production/runtime assurance is claimed from static checks.

### AGSG Runtime And Adapter Lane

Status: VALUE_PARKED

Reopen condition: reopen only after AGSG-T1 closes and a later operator-selected
ASSF adapter or runtime roadmap names the exact package source, resolver,
adapter surface, provider/tool evidence requirement, and public boundary.

Blocked work:

- runtime skill activation;
- provider-backed skill execution;
- external CLI/MCP adapter;
- slash-command import;
- automatic skill-to-work-order generation;
- public catalog claims.

## Acceptance Criteria

- AGSG-T0 roadmap records upstream commit, local pack disposition, source
  authority, external intake routing, dual-agent surface disposition, and
  public export disposition.
- Root-level `CVF Agent Skills Governance Absorption Pack` is no longer present.
- The local pack is retained only under ignored private legacy reference
  storage.
- Material commit contains the roadmap only.
- Session-sync commit updates current mode, next allowed move, active handoff,
  and active session state after the material commit.

## Verification / Evidence

Required checks before material commit:

- `git diff --cached --check`;
- `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 75060e4f --head HEAD --enforce`;
- material commit hook chain.

Required checks before session-sync commit:

- active session state generator;
- session-sync commit steward preflight;
- session-sync commit hook chain.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF reference family and future AGSG-T1 reconciliation artifact | Roadmap and source-verification guidance only; no skill activation, package instance, or resolver mutation | this roadmap plus cited ASSF references | no internal loader or runtime selector implemented by AGSG-T0 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | potential future ASSF external projection | External agent consumption remains deferred; no CLI/MCP adapter, package export, or mutation path is authorized | dual-agent standard and ASSF-T4 external disposition | separate GC-018/work order/provider-safe evidence required before any adapter | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning

| Finding | CVF learning | Routed action |
|---|---|---|
| External skills package is strongest when it encodes workflow and verification, not broad prose | ASSF should prefer package anatomy that proves trigger, boundary, procedure, red flags, and evidence | AGSG-T1 reconciliation |
| Validator-owned exemptions prevent self-authorized bypasses | CVF candidate packages should not be able to exempt themselves from guard requirements | AGSG-T3 value decision |
| Persona and command composition is useful but risky | CVF role/handoff standards must remain the orchestrator; personas are lenses, not authority | AGSG-T1 and possible ASSF-T5 input |
| Anti-rationalization tables are high signal | Repeated rationalization patterns may become ADIF or guard entries only after source-backed defect evidence | AGSG-T1 disposition |
| Local pack overlaps existing ASSF controls | Absorption should reconcile and reduce duplication instead of creating a new skill-governance family | AGSG-T1 mandatory non-duplication check |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local workspace |
| Session or invocation | AGSG-T0 external absorption audit, 2026-06-28 |
| Working directory | repository root |
| Command or tool surface | `rg`, `git clone`, `git log`, `Get-Content`, `Get-FileHash`, `Move-Item`, `apply_patch` |
| Target paths | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `.private_reference/legacy/CVF_Agent_Skills_Governance_Absorption_Pack` |
| Allowed scope source | operator request to audit `addyosmani/agent-skills.git` and `CVF Agent Skills Governance Absorption Pack` under old external-absorption rules |
| Before status evidence | `git rev-parse --short HEAD` returned `75060e4f`; local pack was untracked at root before move |
| After status evidence | roadmap authored; local pack moved into ignored private legacy reference storage |
| Diff evidence | pre-commit gates and `git diff --name-status` to be captured before material commit |
| Approval boundary | operator requested audit and absorption; no runtime/import/push requested |
| Claim boundary | roadmap and absorption decision only; no package implementation, checker implementation, runtime activation, provider proof, public-sync, or adapter |
| Agent type | orchestrator/auditor |
| Invocation ID | `cvf-agsg-t0-agent-skills-external-absorption-2026-06-28` |
| Expected manifest | this roadmap only in tracked files; ignored private-reference legacy move outside commit manifest |
| Actual changed set | this roadmap only in tracked files; to be verified before material commit |
| Manifest delta | N/A with reason: no tracked legacy folder import; local pack moved to ignored legacy storage |
| Deletion or rename disposition | root local pack removed from root by move into `.private_reference/legacy/`; no tracked delete because the pack was untracked |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSG-T0 external absorption roadmap and root-folder legacy relocation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - source-read audit and roadmap routing only |
| receiptEvidence | N/A with reason: no runtime skill invocation, provider call, adapter run, checker implementation, or benchmark proof |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source verification table, external evidence manifest, local pack move, and material commit evidence |
| invocationBoundary | local documentation authoring and ignored private-reference folder move |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | AGSG-T0 routes advisory skill-governance patterns into ASSF reconciliation |
| forbiddenExpansion | no package instance, resolver mutation, checker implementation, CLI/MCP adapter, plugin install, command import, runtime activation, provider/live proof, public-sync, or security certification |

## Claim Boundary

AGSG-T0 proves only that the upstream repository and local pack were audited and
that their useful governance patterns have been routed into a CVF-owned ASSF
reconciliation roadmap. It does not prove production-ready skill governance,
runtime enforcement, provider-backed proof, benchmark value, automatic safe
skill invocation, CLI/MCP readiness, or security certification.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap cites private provenance workspace paths and a local
operator-supplied absorption pack. Public-safe publication would require a
separate redaction and public-sync authorization.
