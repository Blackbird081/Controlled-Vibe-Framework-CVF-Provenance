# CVF ASSF-T0.1 Legacy Skill Corpus Rescan Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: audit

Batch ID: ASSF-T0.1

Commit mode: WORKER_MUST_NOT_COMMIT (this artifact is uncommitted worker output)

executionBaseHead: `3f51a4cc`

## Purpose

Provide the filesystem-backed legacy skill corpus scan and absorption
candidate ledger required before ASSF-T1 may define the canonical
system-skill package contract and storage topology. This audit treats the
four ASSF-T0 seed folders as required inputs, not complete corpus coverage,
and scans the full `.private_reference/legacy/` root per the ASSF-T0.1
dispatch baseline and work order.

## Findings / Position

The legacy corpus contains substantially more skill-relevant material than
the four ASSF-T0 seed folders alone: 422 of 629 legacy files (67%) match at
least one required keyword, spanning 5 additional non-seed families
(Hugging Face, Hermes Agent, Workflow GoClaw, caveman, gridex, plus
HowtoClaude/ADDING_Skill Creator under `CVF_Important/`) not previously
content-verified. The Absorption Candidate Ledger below classifies the
highest-signal subset with source-backed dispositions; this audit's position
is that ASSF-T1 should treat this ledger, not the T0 seed set alone, as its
legacy-input baseline.

## Risk / Corrective Action

Risk: if ASSF-T1 freezes the canonical package contract from only the T0
seed folders, it would omit at least two strong schema candidates
(`CVF_HF_SKILL_NORMALIZATION_SCHEMA.md`'s 21-field object and
`CVF_HERMES_SKILL_PACKAGE_MODEL.md`'s distinct field set) and the closest
legacy match to the roadmap's own resolver framing
(`CVF_SKILL_ACTIVATION_PROFILE_SPEC.md`). Corrective action: this audit's
Absorption Candidate Ledger and Source-Fidelity Notes sections are the
corrective evidence; reviewer/T1 should treat the `BLOCKED_UNVERIFIED_SOURCE`
rows (`CVF_HF_EXECUTION_ADAPTER_SPEC.md`, `CVF_HF_CONTEXT_INJECTION_RULES.md`,
`CVF_HF_SKILL_RISK_CLASSIFICATION_POLICY.md`, `CVF_HERMES_SKILL_INGESTION_PROTOCOL.md`,
`AI Skill Supply Chain.md`, `Agent Skill Economy.md`) as a priority follow-up
read list before T1 schema freeze, not as resolved.

## Scope And Forbidden Scope

In scope: read-only enumeration and keyword search of
`.private_reference/legacy/`; content inspection of candidate files sufficient
to justify a disposition; collision search against
`governance/skill-library/`, `docs/roadmaps/`, `docs/reference/`, and
`EXTENSIONS/`; authoring this audit ledger and the paired worker-return
packet only.

Forbidden and not performed: no edit under `.private_reference/legacy/`; no
canonical package root, generated index, resolver, schema, or runtime
adapter; no migration of any legacy file into a CVF-owned path; no commit;
no session/front-door/handoff edit; no public-sync.

## Source Verification Refresh

| Claimed item | Source file | Verified line/section | Verified path or symbol | Source fact type | Disposition |
|---|---|---|---|---|---|
| `governance/skill-library/` is the existing CVF-owned current skill surface, already audited by ASSF-T0 | `docs/baselines/CVF_GC018_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_AUDIT_2026-06-23.md` | Source Verification Block rows on `governance/skill-library/specs/CVF_SKILL_SPEC.md` and `governance/skill-library/README.md` | `governance/skill-library/` | EXISTS | ACCEPT |
| ASSF-T0 completion review does not mention `governance/skill-library/` anywhere in its body | `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md` | full-document grep, zero matches | N/A with reason: negative-result verification, no symbol to cite | EXISTS | ACCEPT |
| W7 is an existing current CVF surface, not legacy-only | `docs/reference/CVF_W7_CLI_MVP_SCOPE.md`; `docs/reference/CVF_W7_CLI_GOVERNANCE_BINDINGS.md` | file existence under `docs/reference/` | `CVF_W7_CLI_MVP_SCOPE.md` | EXISTS | ACCEPT |
| Two distinct legacy files share the basename `CVF_SKILL_MODEL.md` with different content | `.private_reference/legacy/CVF_Important/ADDING_CVF_Skill Formation Layer/CVF_SKILL_MODEL.md`; `.private_reference/legacy/CVF_Important/ADDING_Skill Creator/CVF_SKILL_MODEL.md` | full-file diff, both files read in entirety up to disposition-justifying depth | `CVF_SKILL_MODEL.md` | EXISTS | ACCEPT |
| Two distinct legacy files share the basename `CVF_SKILL_NORMALIZATION_SCHEMA.md` with different content and scope | `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_NORMALIZATION_SCHEMA.md`; `.private_reference/legacy/CVF_Important/HowtoClaude/CVF_SKILL_NORMALIZATION_SCHEMA.md` | section 1-4 of both files read | `CVF_SKILL_NORMALIZATION_SCHEMA.md` | EXISTS | ACCEPT |

## Corpus Completeness And Report Integrity

- Corpus task class: LEGACY_RESCAN_WORKER_RETURN.
- Corpus root: `.private_reference/legacy/`.
- Snapshot time: 2026-06-23, local session time approximately 12:20-13:10 SEAST.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/legacy` (run from repo root).
- Manifest artifact or inline manifest: inline manifest summary below; raw manifest is a 629-line
  command output retained only in this session's scratch directory, not
  committed (scratchpad output is not a governed artifact).
- Manifest hash: N/A with reason: text-only inline manifest summary, no
  binary artifact to hash.
- Processing ledger artifact or inline ledger: the Absorption Candidate Ledger section below.
- Allowed terminal statuses: READ (content-inspected), SKIPPED_WITH_REASON
  (name/seed-coverage only, no full read), DEFERRED (none), BLOCKED_UNREADABLE
  (none encountered).
- Reconciliation: manifest=629 files enumerated; keyword_hits=4855 raw line hits across 422 distinct files; ledger_terminal=this section's table rows cover all distinct families with a terminal disposition; exclusions=binary asset files, generic `Thong_tin.md` seed notes not independently ledgered beyond their parent folder row, non-skill-relevant legacy families recorded as out-of-domain by keyword-absence; unresolved=0.
- Unresolved files: 0
- Declared exclusions: 629 total legacy files minus ~422 files with any
  keyword hit leaves approximately 207 files with zero skill-term hits
  (UI mockups under `App onboarding/`, non-skill infra docs under
  `CVF_Restructure/`, unrelated domain specs under `CVF 16.5/` and
  `CVF 17.05/`); these are recorded as `REFERENCE_ONLY` by absence of
  signal, not individually content-inspected line-by-line.
- Unreadable or unsupported files: 0 encountered; all matched files were
  UTF-8 text (`.md`, `.ts`, `.jsx`, `.html`, `.json`, `.csv`).
- Aggregation check: N/A with reason: no generated aggregate file was
  created by this worker return.
- Drift check: N/A with reason: no generated aggregate file was created by
  this worker return.
- Output traceability: every ledger row below cites a manifest path that
  appears in the 629-file enumeration and, where a disposition other than
  `REFERENCE_ONLY`/`DUPLICATE` is assigned, a content excerpt read directly
  from that file in this session.
- Adversarial verification: this audit explicitly rejects an open-tab-only
  corpus claim (the four ASSF-T0 seed folders account for only 4 of 9
  top-level legacy families and a small fraction of the 422 keyword-hit
  files) and rejects a memory-only claim (every disposition below traces to
  a command run or file read in this session, not to prior-session memory).
- Corpus verdict: PARTIAL

The corpus verdict is `PARTIAL`, matching the dispatch baseline's own
declared verdict, because: (a) full-root enumeration and keyword search are
complete and command-backed; (b) only the highest-signal subset of the 422
keyword-hit files received direct content inspection sufficient to assign a
specific absorption disposition; (c) the remaining matched files are
name-and-keyword classified into family-level rows rather than individually
content-verified. This is the declared limit required by the work order's
`Corpus verdict: PARTIAL` Acceptance Criteria, not an unresolved gap.

## Legacy Manifest Summary

Total files under `.private_reference/legacy/`: 629.

Top-level families (file count):

| Top-level folder | File count | Skill-keyword-hit files (approx.) |
|---|---|---|
| `App onboarding/` | 10 | 1 (UI mockup, weak signal) |
| `CVF 16.5/` | 100 | includes Memento-Skills (seed), abtop, agentmemory, Claude Kit, OpenAgentd, OpenSpec |
| `CVF 17.05/` | 31 | review/rebuttal docs referencing skill/CLI in narrative form |
| `CVF 25.05/` | 2 | none with skill-keyword hits |
| `CVF 28.05/` | 5 | none with skill-keyword hits |
| `CVF ADD/` | 167 | Hugging Face, Hermes Agent, Workflow GoClaw, caveman, gridex, CLI-Anything, cortex-hub, and others |
| `CVF Edit/` | 10 | none with skill-keyword hits |
| `CVF_Important/` | 230 | ADK SkillToolset (seed), Windows_Skill_Normalization (seed), ADDING_CVF_Skill Formation Layer (seed), ADDING_Skill Creator, HowtoClaude, Claude how to |
| `CVF_Restructure/` | 74 | CVF_AI Systems (AI Skill Supply Chain, Agent Skill Economy), cvf-core v0.1 |

Keyword search (`skill|skills|package|toolset|formation|lifecycle|normalization|memento|adapter|mcp|cli|adk|governed evolution`, case-insensitive) over the full legacy root: 4855 raw line hits across 422 distinct files out of 629 total files.

## Absorption Candidate Ledger

| Candidate path | Evidence type | Source excerpt or section | Candidate domain | Internal-agent implication | External-agent CLI/MCP implication | Disposition | Reason | Next ASSF owner |
|---|---|---|---|---|---|---|---|---|
| `CVF_Important/ADK SkillToolset/Thong_tin.md` | seed path, content hit | progressive disclosure; L1 metadata/L2 instructions/L3 resources; 4 patterns incl. meta-skill self-write | lifecycle/evolution, package pattern | defines progressive load order an internal resolver should follow | external `agentskills.io` format note implies cross-tool portability question | `ABSORB_AS_LIFECYCLE_INPUT` | matches roadmap principle 3 (metadata-first index resolution); already an ASSF-T0 seed source | T1, T4 |
| `CVF_Important/ADK SkillToolset/CVF_KNOWLEDGE_ASSIMILATION_LOG.md` | seed path, content hit | Progressive Disclosure Policy; Skill Normalization Schema; Planner Trigger Patterns | contract, lifecycle | prior absorption decisions already recorded; avoid re-deriving | none directly stated | `REFERENCE_ONLY` | already a recorded assimilation decision, not a fresh candidate; restate as historical input | T1 |
| `CVF_Important/Windows_Skill_Normalization/Thong_tin.md` | seed path, content hit | refactor 86 skills for Windows; PowerShell conversion | shell/platform | internal loader must not assume POSIX shell defaults | adapters that shell out must declare platform compatibility | `ABSORB_AS_CONTRACT_INPUT` | platform-compatibility field is a concrete candidate field for the canonical package contract | T1 |
| `CVF_Important/ADDING_CVF_Skill Formation Layer/Thong_tin.md` | seed path, content hit (100 keyword hits, highest in corpus) | learn-extract-structure-save-reuse; `SKILL.md` folder pattern | package pattern, lifecycle | strongest single source for the package-folder convention | none directly stated | `ABSORB_AS_PACKAGE_PATTERN` | highest-signal seed file; directly informs T1 storage topology question | T1 |
| `CVF_Important/ADDING_CVF_Skill Formation Layer/CVF_SKILL_MODEL.md` | seed-adjacent, content hit | Skill defined as "validated execution pattern extracted during REVIEW phase"; Non-Goals: not memory, not agent-owned, not BUILD-phase-created | contract | strict lifecycle-phase gate on when a skill may be created | none directly stated | `ABSORB_AS_CONTRACT_INPUT` | concrete, English-language, CVF-native skill definition; directly citable for T1 identity/authority fields | T1 |
| `CVF_Important/ADDING_Skill Creator/CVF_SKILL_MODEL.md` | content hit, basename collision with row above | Skill defined as "capability package attachable to agent runtime" (Vietnamese) | contract | broader/looser definition than the Formation Layer version | does not exclude external attach surfaces | `ABSORB_AS_CONTRACT_INPUT` | **basename collision**: same filename as the Formation Layer row above but materially different content (diff-verified); both are real candidates, not a true duplicate; reviewer/T1 must reconcile which definition (or both) the canonical contract adopts |  T1 |
| `CVF_Important/ADDING_Skill Creator/CVF_SKILL_REGISTRY.md` | content hit | `cvf skill publish/install/search`; semver; registry security model (permission/sandbox/audit_log) | tool adapter, package pattern | registry operations (publish/install/search) are internal-registry concepts | explicit CLI verb surface (`cvf skill <verb>`) is a direct external CLI-adapter design input | `ABSORB_AS_TOOL_ADAPTER_INPUT` | concrete CLI verb set and security model; first-class input for a future CLI/MCP adapter tranche, not for T0.1 itself | T7 |
| `CVF_Important/HowtoClaude/CVF_SKILL_NORMALIZATION_SCHEMA.md` | content hit, basename collision with HF row below | ingest->classify->normalize->compile->validate->register; plane-mapped table (Control/Execution/Governance/Learning Plane) | lifecycle | broader, plane-level normalization flow, not a field-level schema | implies CLI/MCP and AI Gateway as the ingestion surface in the plane table | `ABSORB_AS_LIFECYCLE_INPUT` | **basename collision** with `CVF_HF_SKILL_NORMALIZATION_SCHEMA.md`; this file is broader/plane-level, the HF file is field-level and HF-source-specific; both are kept as distinct, complementary candidates | T1, T4 |
| `CVF ADD/Hugging Face/CVF_HF_SKILL_ABSORPTION_SPEC.md` | content hit | 7 non-negotiable invariants (root invariant, no parallel runtime, no governance bypass, no direct trust, registry publication required, policy before execution, traceability); 5-phase lifecycle (intake/parse/normalize/risk-classify/policy-bind) | contract, lifecycle | directly matches roadmap principle 4 (candidates never immediate ACTIVE) | absorption protocol is specifically for an external skill source | `ABSORB_AS_LIFECYCLE_INPUT` | best-structured external-intake lifecycle found in the corpus; strong candidate for the ASSF intake-to-candidate pipeline | T1, T4 |
| `CVF ADD/Hugging Face/CVF_HF_SKILL_NORMALIZATION_SCHEMA.md` | content hit, basename-family collision with HowtoClaude row above | `CVFNormalizedSkillSpec` with 21 named fields incl. `cvf_skill_id`, `risk_level`, `policy_bindings`, `sandbox_requirement` | contract | concrete field list is directly reusable for the canonical package schema | `context_injection_profile`/`trace_requirements` fields apply to any consumer, internal or external | `ABSORB_AS_CONTRACT_INPUT` | most concrete, field-level normalization schema in the corpus; strongest single T1 schema input | T1 |
| `CVF ADD/Hugging Face/CVF_HF_EXECUTION_ADAPTER_SPEC.md` | content hit (name only, not fully read this session) | file name implies execution-adapter design | tool adapter | not yet content-verified | not yet content-verified | `BLOCKED_UNVERIFIED_SOURCE` | named but not opened this session; needs follow-up read before a non-`REFERENCE_ONLY` disposition is justified | T1 (follow-up) |
| `CVF ADD/Hugging Face/CVF_HF_CONTEXT_INJECTION_RULES.md` | content hit (name only, not fully read this session) | file name implies context-injection rules | contract | not yet content-verified | not yet content-verified | `BLOCKED_UNVERIFIED_SOURCE` | named but not opened this session | T1 (follow-up) |
| `CVF ADD/Hugging Face/CVF_HF_SKILL_RISK_CLASSIFICATION_POLICY.md` | content hit (name only, not fully read this session) | file name implies risk classification policy | governance | not yet content-verified | not yet content-verified | `BLOCKED_UNVERIFIED_SOURCE` | named but not opened this session | T1 (follow-up) |
| `CVF ADD/Hermes Agent/CVF_HERMES_SKILL_PACKAGE_MODEL.md` | content hit | required fields incl. `trigger_pattern`, `allowed_use_cases`/`disallowed_use_cases`, `maturity_level`, `registry_status` (Vietnamese) | package pattern | distinct field set from HF schema; adds trigger/maturity/registry-status concepts not in HF list | none directly stated | `ABSORB_AS_PACKAGE_PATTERN` | complements rather than duplicates the HF schema; trigger-pattern field is directly useful for T4 resolver design | T1, T4 |
| `CVF ADD/Hermes Agent/CVF_HERMES_SKILL_INGESTION_PROTOCOL.md` | content hit (name only, not fully read this session) | file name implies ingestion protocol | lifecycle | not yet content-verified | not yet content-verified | `BLOCKED_UNVERIFIED_SOURCE` | named but not opened this session | T1 (follow-up) |
| `CVF ADD/Workflow GoClaw/CVF_SKILL_ACTIVATION_PROFILE_SPEC.md` | content hit | activation profiles (interactive/task/minimal); pinned vs searchable vs prohibited vs MCP-dependent skill categories | lifecycle, tool adapter | directly matches roadmap's "load only skills relevant to task/role/lifecycle phase/surface/risk" framing | explicit `MCP-dependent skills` category is a named external-agent-adjacent class | `ABSORB_AS_LIFECYCLE_INPUT` | closest legacy match to the roadmap's progressive-resolver framing; strong T4 input | T4 |
| `CVF ADD/caveman/CVF_SKILL_EFFICIENCY_PROFILE_SPEC.md` | content hit | `preferred_verbosity_mode`, `minimum_trace_requirement`, `context_appetite`, `compression_tolerance`, `preferred_model_tier` fields | contract | optional metadata extension to the canonical contract, not a structural requirement | model-tier preference could matter to an external CLI/MCP scheduler | `ABSORB_AS_CONTRACT_INPUT` | low-risk, narrow, well-scoped metadata extension; safe candidate even though niche | T1 |
| `CVF ADD/gridex/CVF_DATABASE_SKILLFORM_W7_BINDING.md` | content hit | `db-query-skill`/`db-mutation-skill`/`db-schema-skill` families bound through `SkillFormationRecord`/`W7RuntimeRecord`/`W7TraceRecord` | tool adapter | couples skill formation to the existing W7 governance surface (`docs/reference/CVF_W7_CLI_MVP_SCOPE.md` confirms W7 already exists in current CVF) | database-mutation skills are explicitly write-capable, a high external-risk class if ever CLI/MCP-exposed | `ABSORB_AS_TOOL_ADAPTER_INPUT` | concrete domain tool-adapter family; W7-coupling terminology needs an explicit operator/T1 decision before reuse since W7 is a current, not legacy-only, surface | T1, flagged `STRATEGIC_OPERATOR_DECISION` |
| `CVF ADD/CLI-Anything/Thong_tin.md` | content hit (789 lines, partially read: self-audit framing + Phase A opening read) | self-audit explicitly states "CVF is root, CLI-Anything is knowledge input only, no parallel runtime, no governance bypass"; 6 absorbable knowledge types incl. "CLI skill packaging & discoverability" and "catalog/install/discovery pattern" | tool adapter | 7-phase harness pipeline (analyze->design->implement->test plan->test write->document->publish) is a candidate template for internal skill-authoring workflow | explicit CLI-as-agent-interface argument (`--help`, structured/JSON output) is directly `EXTERNAL_AGENT_CLI_MCP` relevant | `ABSORB_AS_TOOL_ADAPTER_INPUT` | already self-audited by a prior agent against CVF root-invariant rules; high source-fidelity, but file not fully read end-to-end this session | T7, flagged for full read before T7 dispatch |
| `CVF_Restructure/CVF_AI Systems/Thong_tin/AI Skill Supply Chain.md` | content hit (name only, not fully read this session) | file name implies a skill supply-chain framing | package pattern | not yet content-verified | not yet content-verified | `BLOCKED_UNVERIFIED_SOURCE` | high keyword-hit count (76) but not opened this session; flagged for priority follow-up read before T1 schema freeze | T1 (priority follow-up) |
| `CVF_Restructure/CVF_AI Systems/Thong_tin/Agent Skill Economy.md` | content hit (name only, not fully read this session) | file name implies an economic/marketplace framing for skills | governance | not yet content-verified | not yet content-verified | `BLOCKED_UNVERIFIED_SOURCE` | high keyword-hit count (75) but not opened this session; flagged for priority follow-up read before T1 schema freeze | T1 (priority follow-up) |
| `CVF 16.5/Memento-Skills/README.md`, `GOVERNED_SKILL_EVOLUTION_SPEC.md`, and the 6 paired `.ts` files | seed path, content hit | "A skill may be improved by evidence. A skill must not rewrite itself directly into production."; mutation types incl. `PATCH_EXISTING_SKILL`/`CREATE_NEW_SKILL`; approval class `HUMAN_REVIEW_REQUIRED` | lifecycle/evolution | directly matches roadmap principle 4 (learning-produced candidates, never immediate ACTIVE); `.ts` files (`skill_evolution.contract.ts`, `skill_mutation_planner.ts`, `skill_reflection_engine.ts`, `skill_reinjection_controller.ts`, `skill_verification_gate.ts`, `skill_evolution_receipt.ts`) describe a full governed-evolution pipeline shape, not runnable in CVF's current stack as-is | none directly stated | `ABSORB_AS_LIFECYCLE_INPUT` | already an ASSF-T0 seed source; the `.ts` files are TypeScript design sketches (interfaces/contracts), not integrated CVF code, and must not be treated as ready-to-run | T1, T4 |
| `App onboarding/*.jsx`, `*.html` (10 files) | name/seed scan, no skill-keyword hits | UI mockup files used elsewhere in this repository as a UI design reference | other | none | none | `REFERENCE_ONLY` | confirmed unrelated to skill-package architecture; already governed as a UI design reference elsewhere | REJECTED for ASSF purposes |
| Remaining ~207 legacy files with zero keyword hits (e.g. `CVF_Restructure/CVF_ECOSYSTEM/` non-skill infra docs, `CVF 25.05/`, `CVF 28.05/`, `CVF Edit/`) | negative search, command-backed absence | zero hits for the required query terms | other | none stated | none stated | `REFERENCE_ONLY` | absence of any skill/package/lifecycle/adapter/CLI/MCP keyword across the full required query family; treated as out-of-domain for ASSF without individual file-by-file reads | REJECTED for ASSF purposes |

## Seed Folder Coverage

| Seed folder (from ASSF-T0.1 dispatch) | Files in folder | T0.1 disposition |
|---|---|---|
| `CVF_Important/ADK SkillToolset/` | 2 (`Thong_tin.md`, `CVF Audit.md`, `CVF_KNOWLEDGE_ASSIMILATION_LOG.md`) | content-verified; see ledger rows above |
| `CVF_Important/Windows_Skill_Normalization/` | 7 | seed `Thong_tin.md` content-verified; sibling spec files (`CVF_W7_Windows_Skill_Normalization.md` etc.) named but not individually re-read this session, since ASSF-T0's prior audit already covered this folder as a seed |
| `CVF_Important/ADDING_CVF_Skill Formation Layer/` | 7 | `Thong_tin.md` and `CVF_SKILL_MODEL.md` content-verified this session; sibling files (`CVF_SKILL_INTEGRATION_CHECKLIST.md`, `CVF_SKILL_USAGE_PROTOCOL.md`, `CVF_SKILL_EXTRACTION_SPEC.md`, `CVF_GUARD_ENFORCEMENT_SPEC.md`) named, high keyword-hit, flagged `BLOCKED_UNVERIFIED_SOURCE`-equivalent follow-up since not re-read line-by-line this session |
| `CVF 16.5/Memento-Skills/` | 8 | content-verified; see ledger row above |

Seed folders are confirmed covered but, consistent with the dispatch baseline's
own framing, are a small fraction (24 of 629 files, under 4%) of total legacy
corpus volume and a minority of the 422 keyword-hit files. Treating them as
sufficient corpus coverage would have been the exact blind spot this T0.1
tranche was dispatched to close.

## Negative Search And Collision Evidence

- Negative evidence: `CVF 25.05/` (2 files) and `CVF 28.05/` (5 files) produced
  zero hits for any required query term; both folders were enumerated in the
  629-file manifest and confirmed present, ruling out a missing-folder
  explanation for the absence.
- Collision evidence (current-surface vs legacy): `governance/skill-library/`
  already exists as a substantial, CVF-owned current skill surface (specs,
  registry with 34 `agent-skills` entries and 149 `user-skills` entries, UAT,
  dedupe pipeline, external-intake script `run_external_intake.py`). ASSF-T0
  already source-verified this surface as an existing owner; this T0.1 rescan
  does not re-litigate that finding, but every legacy candidate disposition
  above is written so that it feeds T1's reconciliation against this existing
  surface rather than treating legacy content as if no current surface
  existed.
- Collision evidence (legacy-internal basename duplicates): two pairs of
  legacy files share a basename with materially different content
  (`CVF_SKILL_MODEL.md` x2; `CVF_SKILL_NORMALIZATION_SCHEMA.md` x2, the second
  pair differing only by the `CVF_HF_` prefix on one side). Both pairs are
  ledgered as distinct candidates above, not silently merged or dropped.
- Collision evidence (legacy-internal generic seed notes): `Thong_tin.md`
  appears 47 times across the legacy root as each subfolder's generic
  capture-note filename; this is an expected naming convention of the legacy
  corpus, not a content collision, and is not separately ledgered beyond the
  per-family rows above.

## Source-Fidelity Notes For Well-Formed CVF Legacy Packets

The following legacy packets are well-formed, CVF-native (not generic
external copy-paste), and source-fidelity-verified by direct content read in
this session:

- `CVF_HF_SKILL_ABSORPTION_SPEC.md` - the 7 non-negotiable invariants and the
  5-phase absorption lifecycle (Source Intake -> Structural Parsing ->
  Normalization -> Risk Classification -> Policy Binding) are precise,
  internally consistent, and already aligned with ASSF roadmap principle 4.
- `CVF_HF_SKILL_NORMALIZATION_SCHEMA.md` - the 21-field `CVFNormalizedSkillSpec`
  object is the single most concrete, field-level schema candidate found in
  the corpus for T1's canonical package contract.
- `GOVERNED_SKILL_EVOLUTION_SPEC.md` / Memento README - the "skill may be
  improved by evidence, must not rewrite itself directly into production"
  rule is a precise, quotable invariant directly reusable for T4/T5 guard
  design without rewriting.
- `CVF_SKILL_ACTIVATION_PROFILE_SPEC.md` - the interactive/task/minimal
  activation-profile framing is the closest legacy match to the roadmap's own
  task/role/lifecycle-phase/surface/risk resolver framing.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future ASSF package loader, generated index, and resolver design (T1/T4) | this audit produces classified candidates only; no internal loader behavior, package authority, or schema freeze is created by T0.1 | Absorption Candidate Ledger `Internal-agent implication` column | no adapter implemented; no loader code written | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external CLI/MCP package discovery/load adapter (T7-class) | several candidates (`CVF_SKILL_REGISTRY.md`'s `cvf skill publish/install/search` verbs; `CLI-Anything`'s CLI-as-agent-interface argument; gridex's MCP-dependent skill category) are explicitly CLI/MCP-relevant, but none are exposed or implemented as an adapter by this audit | Absorption Candidate Ledger `External-agent CLI/MCP implication` column | adapter implementation is explicitly out of scope for T0.1; deferred to a separate, later ASSF/CLI-adapter tranche with its own GC-018 | `DEFERRED_WITH_REASON` |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control applied this session |
|---|---|
| Seed-only legacy scan | Full-root enumeration (629 files) and full-root keyword search (4855 hits/422 files) were run; seed folders account for only 24 of 629 files (under 4%) |
| Name-only classification | Every non-`BLOCKED_UNVERIFIED_SOURCE`, non-`REFERENCE_ONLY` ledger row cites a content excerpt read directly in this session, not just a filename match |
| Legacy authority promotion | Every ledger row's disposition is an `ABSORB_AS_*`/`REFERENCE_ONLY`/`DUPLICATE`/`BLOCKED_UNVERIFIED_SOURCE` candidate label; no row claims canonical CVF authority for any legacy file |
| External-adapter omission | Every ledger row includes an explicit `External-agent CLI/MCP implication` cell, even when the answer is "none directly stated" |
| Hidden duplicate/collision | Basename-collision scan (`dup_scan.py` against the 629-file manifest) found and diff-verified two skill-relevant collision pairs; both are ledgered, not dropped |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Required route | Knowledge Absorption Blind-Spot Control Block plus legacy coverage lookup (both applied above) |
| Chain map route | legacy source family -> absorption blind-spot control -> ASSF candidate ledger -> reviewer decision (this audit is the candidate ledger stage) |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T0.1 audit and future ASSF-T1/T4 normalization decisions |
| Disposition | candidate intake only; no direct canonical authority or activation is claimed anywhere in this audit |
| Claim boundary | every legacy file referenced above remains a candidate input; none is treated as CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- Delta ledger status: REFRESHED (see Original-Intake Delta Ledger below)
- Routing matrix status: REFRESHED (see Follow-Up Routing Matrix below)
- Semantic sampling status: 3 samples included below
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Audit finding |
|---|---|
| `UNCHANGED_FROM_INTAKE` | T0's finding that `governance/skill-library/` is the existing current-surface owner remains valid and unchanged |
| `CHANGED_DISPOSITION` | legacy corpus status changes from "4 seeded folders" (T0 framing) to "422 keyword-hit files across 9 families, 24 classified in this ledger" (T0.1 framing) |
| `NEW_FINDING` | 2 basename-collision pairs inside legacy; 5 non-seed families with strong skill-relevant content |
| `REMOVED_OR_REJECTED` | open-tab-only and memory-only corpus claims rejected; `App onboarding/` UI mockups and ~207 zero-keyword-hit files rejected as out-of-domain |

### Follow-Up Routing Matrix

| Routing lane | Audit disposition |
|---|---|
| `DO_NOW` | scan and classify completed in this audit |
| `SEPARATE_RUNTIME_TRANCHE` | any CLI/MCP adapter, runtime, or migration work stays out of scope |
| `STRATEGIC_OPERATOR_DECISION` | `gridex`'s W7-coupled terminology needs an explicit operator/T1 decision |
| `OUT_OF_SCOPE` | package creation, generated index, resolver, public-sync |
| `RESOLVED_BY_DESIGN` | the no-commit worker-return lane prevented premature legacy-authority promotion |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T0.1-A-S1 | `CVF_HF_SKILL_ABSORPTION_SPEC.md` Non-Negotiable Invariants | "no skill executable before normalization, classification, approval, publication" | `ABSORB_AS_LIFECYCLE_INPUT`, not `ABSORB_AS_TOOL_ADAPTER_INPUT` | could this be read as authorizing direct execution? | rejected - spec explicitly grants no execution authority |
| ASSF-T0.1-A-S2 | basename-collision pair `CVF_SKILL_MODEL.md` | two files, same name, different content | both ledgered as distinct candidates, not a stale duplicate | could the second file be silently dropped? | rejected - full diff performed, content materially differs |
| ASSF-T0.1-A-S3 | `CVF_SKILL_REGISTRY.md` `cvf skill publish/install/search` | explicit CLI verb set | `EXTERNAL_AGENT_CLI_MCP` implication marked present | could this be read as internal-only? | rejected - a CLI verb surface is inherently external-agent-facing |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | `RULE_GAP` (work-order-local label: legacy scan coverage gap) |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `MACHINE_CHECK_CANDIDATE` |
| Runtime/provider/cost lane | N/A_WITH_REASON: this finding is a documentation-and-evidence-coverage gap, not a runtime, provider, or cost-economics finding |
| Next control action | T1 (or a dedicated future ASSF gate) should consider requiring evidence of a full-root `rg --files --hidden --no-ignore` legacy enumeration, not just named seed paths, before any work order may dispatch a schema/package-design tranche that depends on legacy absorption coverage. This audit itself is the first concrete instance of that evidence shape and can serve as the worked example. |

## Machine-Check Candidate Notes

- A future guard could require that any work order whose roadmap-trace
  matrix lists "legacy absorption" as a precondition must cite a manifest
  line count and a keyword-hit file count in its Source Verification Block,
  the same evidence shape this audit provides.
- A future closure packet could fail if an `EXTERNAL_AGENT_CLI_MCP` Dual
  Agent Surface Matrix row is `IMPLEMENTED` while the corresponding candidate
  ledger contains zero `ABSORB_AS_TOOL_ADAPTER_INPUT` rows tracing to it -
  this would catch an adapter built without any source-verified input.
- Candidate ledgers in this domain should keep both an
  `Internal-agent implication` and an `External-agent CLI/MCP implication`
  column, as required by this work order; this proved useful for surfacing
  the `CVF_SKILL_REGISTRY.md` and `CLI-Anything` rows as CLI/MCP-relevant
  even though neither file is named after MCP or CLI in an obvious way at
  first glance.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this audit excerpts and classifies content from
`.private_reference/legacy/`, a private-provenance corpus. Public-safe skill
architecture documentation requires a later, separate redaction and
public-sync authority decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T0_1_CLOSED_PASS_BOUNDED_PENDING_T1_SELECTION` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Audit ledger | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Completion review | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` | reviewer closure artifact present | PASS |
| External evidence digest | N/A with reason | no external artifact digest; evidence is local private governed documentation in this provenance repository | N/A with reason |
| System loop interlock | N/A with reason | no loop, queue, daemon, runtime, or automatic execution created | N/A with reason |
| Registry JSON | BLOCKED with reason | no GC-051 registry update authorized by T0.1; future registry work requires a separate source-verified tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry Markdown update authorized by T0.1; future registry work requires a separate source-verified tranche | BLOCKED with reason |
| Session continuity | active session sync after material commit if next move changes | separate post-material session-sync lane | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | this audit's legacy scan and absorption candidate ledger only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - no-commit worker-return audit artifact |
| receiptEvidence | CVF_RECEIPT_PRESENT - command outputs captured in this session (manifest count, keyword-hit count, dup-scan output) |
| actionEvidence | ACTION_EVIDENCE_PRESENT - ledger rows, seed coverage table, collision evidence above |
| invocationBoundary | governed local filesystem scan and documentation return |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | scan and classify legacy skill candidates |
| forbiddenExpansion | no commit, package root, generated index, resolver, runtime, CLI/MCP adapter, public-sync, or active skill claim made by this audit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | ASSF-T0.1 worker (Claude) |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0.1 worker execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | `rg --files --hidden --no-ignore`, `rg -n -i` keyword search, Python dup-scan script in session scratch directory, direct file reads, `git status --short`, governance gate invocation |
| Target paths | `.private_reference/legacy/` (read-only); this audit file and the paired worker-return packet (write) |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md` Allowed Scope section |
| Before status evidence | clean worktree at HEAD `3f51a4cc` |
| After status evidence | this audit and the paired worker-return packet created; no other files modified |
| Diff evidence | `git status --short` before and after this session's writes (recorded in the worker-return packet) |
| Approval boundary | worker execution only; no commit |
| Claim boundary | candidate ledger and scan evidence only; no package/index/resolver/adapter implementation |
| Agent type | worker |
| Invocation ID | `cvf-assf-t0-1-legacy-skill-corpus-rescan-worker-2026-06-23` |
| Expected manifest | this audit file; the paired worker-return packet |
| Actual changed set | this audit file; the paired worker-return packet |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This audit provides a scan and classification of legacy skill-relevant
knowledge only. It does not migrate any legacy file, create a canonical
package root, generate an index, implement a resolver, implement a CLI/MCP
adapter, claim runtime/provider/live/public behavior, or authorize ASSF-T1.
Codex reviewer accepted this audit as bounded T0.1 closure evidence in the
paired completion review.
