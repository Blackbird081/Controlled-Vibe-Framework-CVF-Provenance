# CVF GC-018 AGSG-T1 Source-Verified ASSF Reconciliation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-28

docType: baseline

Batch ID: AGSG-T1

## Purpose

Authorize and record the AGSG-T1 source-verified reconciliation of
`addyosmani/agent-skills` and the retained
`CVF_Agent_Skills_Governance_Absorption_Pack` against the current CVF Agent
System Skills Foundation (ASSF) owner surfaces.

This baseline is documentation/reference work only. It does not authorize
runtime skill activation, plugin install, slash-command import, persona
orchestration, hook install, resolver mutation, package instance creation,
checker implementation, CLI/MCP adapter implementation, provider/live proof,
public-sync, benchmark claims, security certification, production-readiness, or
automatic skill invocation.

## Scope

In scope:

- verify AGSG-T0 accepted patterns against current ASSF owner surfaces;
- decide which concepts are already covered, which need a compact CVF advisory,
  and which remain parked;
- dispatch the matching AGSG-T1 work order;
- authorize AGSG-T2 documentation-only advisory reference if T1 proves value;
- authorize AGSG-T3 checker value decision and lane closeout.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Baseline decision | Proceed with documentation-only AGSG-T1 reconciliation and AGSG-T2 advisory repair |
| Proposed tranche | AGSG-T1 source verification, AGSG-T2 advisory reference, AGSG-T3 value closeout |
| Runtime disposition | DEFERRED_WITH_REASON |
| Checker disposition | CLOSE_NO_CHECKER_NOW with concrete reopen conditions |
| Public disposition | DEFERRED_PRIVATE_ONLY |

## Non-Goals

Out of scope:

- editing ASSF runtime, resolver, generator, registry entries, or generated
  index;
- importing upstream files into CVF runtime or package roots;
- creating a `SKILL.md`, `skill.source.json`, or package instance;
- installing upstream plugin, commands, personas, hooks, or setup files;
- adapting local pack prototype checkers into executable guard code;
- public export or public catalog claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AGSG-T0 selects T1 source-verified ASSF reconciliation as next governed move | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | `AGSG-T1: Source-Verified ASSF Reconciliation` | `AGSG-T1` | AGSG-T0 roadmap | ACCEPT |
| ASSF package contract owns skill package shape and boundaries | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `SKILL.md Profile`; `Compact Machine Source Schema`; `Provider Adapter Boundary`; `Claim Boundary` | `CVF_ASSF_PACKAGE_CONTRACT.md` | ASSF package contract | ACCEPT |
| ASSF generated index is metadata-only and not runtime activation evidence | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF generated index | ACCEPT |
| ASSF resolver returns bounded metadata and does not activate skills | `governance/compat/run_assf_skill_resolver.py` | `DefectPacket.to_dict` equivalent claim boundary in resolver output; `resolve_skill_packet` docstring | `resolve_skill_packet` | ASSF metadata resolver | ACCEPT |
| ASSF intake normalization requires reverification and no self-activation | `docs/reference/agent_system_skills/CVF_ASSF_INTAKE_NORMALIZATION_CONTRACT.md` | `No-Self-Activation Invariant`; `Reverification Gate` | `candidateState` | ASSF intake normalization contract | ACCEPT |
| ASSF composition contract says loading/composing skills never grants new authority | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | `No-Automatic-Promotion Invariant`; `Capability Claim Controls`; `Internal-Agent Behavior Boundary` | `authorityCeiling`; `capabilityClaims` | ASSF composition control contract | ACCEPT |
| Dual-agent accounting requires internal and external consumer rows and adapter boundary | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | `Mandatory Dual Agent Surface Matrix` | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent surface standard | ACCEPT |
| CVF role matrix treats legacy personas as role templates, not autonomous authority | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | `Legacy Role Template Mapping`; `Forbidden Moves`; `Claim Boundary` | `role lane` | role assignment matrix | ACCEPT |
| Upstream skill anatomy requires `name` and `description` and recommends rationalization/red-flag/verification sections | `.private_reference/external_repos/agent-skills/docs/skill-anatomy.md` | `Skill File`; `Recommended Structure`; `Context Efficiency`; `Validation Checklist` | `SKILL.md`; `description` | upstream advisory source | ACCEPT |
| Upstream validator owns section exemptions in validator code, not skill frontmatter | `.private_reference/external_repos/agent-skills/scripts/validate-skills.js` | `REQUIRED_SECTIONS`; `SECTION_EXEMPT_SKILLS`; `validateSkill` | `SECTION_EXEMPT_SKILLS` | upstream advisory source | ACCEPT |
| Local pack is advisory and bounded to `ABSORPTION_SPEC_ONLY` | `.private_reference/legacy/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/00_SCOPE_AND_CLAIM_BOUNDARY.md` | `Status`; `Out of scope`; `Prohibited claims`; `Runtime upgrade path` | `ABSORPTION_SPEC_ONLY` | local advisory pack | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defectIds:

- `ADIF-0001`
- `ADIF-0002`
- `ADIF-0007`
- `ADIF-0006`

Disposition: all returned defects are handled through direct source
verification, explicit no-runtime boundaries, concrete closure evidence, and
gate-backed dispatch/closure checks.

## Negative Search And Collision Discipline

| Search token | Exact search command or query | Search roots | Same-token collision result | Disposition |
|---|---|---|---|---|
| `CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | `rg "CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY" docs/reference/agent_system_skills docs/baselines docs/work_orders docs/reviews docs/roadmaps` | `docs/reference/agent_system_skills`; `docs/baselines`; `docs/work_orders`; `docs/reviews`; `docs/roadmaps` | collisions in this batch only after authoring | NEW_DOCUMENTATION_REFERENCE |
| source verification dispositions | Source Verification Block review | this baseline | final source table retains only `ACCEPT` rows | PASS |
| runtime/checker implementation target | Scope and Non-Goals review | this baseline and work order target paths | runtime/checker path tokens appear only as forbidden-scope text | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | `External/corpus/repo input -> input router -> old authority/blind-spot/corpus guards -> external-agent packet/checklist when applicable -> returned-output absorption table when applicable -> promote/adapt/defer/reject/block -> GC-018/work order/source verification/autorun when implementation or governed action is needed` |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; work-order dispatch-quality gate |
| Owner surface | ASSF reference family; AGSG-T1 reconciliation baseline and work order |
| Disposition | ADAPT high-value patterns into CVF-owned advisory reference; REJECT direct runtime/plugin import; DEFER checker/runtime/adapter work |
| Claim boundary | external inputs are advisory only and do not become CVF authority without CVF-owned artifact and source verification |

## Reconciliation Findings

| AGSG pattern | Current CVF owner | Finding | T1 disposition |
|---|---|---|---|
| Skill anatomy with trigger, boundaries, process, red flags, and verification | ASSF-T1 package contract | Covered structurally, but upstream gives a concise practical anatomy lens worth preserving as advisory wording | ADAPT_TO_T2_REFERENCE |
| Anti-rationalization tables | Guard orientation, ADIF, work-order closure quality, ASSF risk/evidence fields | Partly covered by process guards, but no ASSF-specific advisory translates rationalizations into package review signals | ADAPT_TO_T2_REFERENCE |
| Progressive disclosure | ASSF-T1 `SKILL.md Profile`; ASSF-T2 resolver/index boundaries | Covered; reinforce "metadata first, body later" in AGSG-T2 without resolver mutation | ADAPT_TO_T2_REFERENCE |
| Persona/command/skill separation | Role matrix, handoff, dual-agent standard | Covered; preserve as role-boundary warning only | ADAPT_TO_T2_REFERENCE |
| Validator-owned exemptions | Current ASSF index/generator and guard culture | Useful checker principle, but no repeated ASSF defect justifies a new checker now | DEFER_TO_T3_VALUE_DECISION |
| Runtime skill activation | ASSF runtime lanes, provider/live standards | Not authorized and not needed for this absorption | VALUE_PARKED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Expected evidence | Disposition |
|---|---|---|---|
| Source verification table against CVF owner surfaces | Source Verification Block | source-verification disposition rows | SATISFIED |
| No duplicate package standard unless a concrete ASSF gap is proven | Reconciliation Findings; Non-Goals | T2 is advisory only, not a replacement standard | SATISFIED |
| Finding-to-governance-learning table | Finding-To-Governance Learning | Each accepted pattern maps to a CVF learning action | SATISFIED |
| Explicit value-parked rows | Parked And Reopen Conditions | Runtime/checker/adapter lanes have concrete reopen conditions | SATISFIED |
| Session/handoff update after commit | Session-sync plan | Dedicated session-sync commit after material commit | SATISFIED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | AGSG-T1/T2/T3 documentation artifacts and existing ASSF references | Internal agents may use the advisory as source-verified documentation context only; no package load, activation, resolver mutation, or authority expansion | this baseline plus cited ASSF source verification | N/A with reason: documentation-only advisory lane | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future ASSF adapter or public-safe projection only if separately authorized | No external agent support is implemented or implied; external consumers cannot mutate skill state, resolver state, or generated index | ASSF-T1/T4/T5 external-disposition fields and dual-agent standard | separate GC-018/work order/provider-safe evidence required before any adapter | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

- AGSG-T1 source-verifies every accepted pattern against ASSF or another CVF
  owner surface.
- AGSG-T2 may be authored only as a compact advisory reference and must not
  edit runtime/source/checker files.
- AGSG-T3 must decide checker value and record concrete reopen conditions.
- The AGSG-T0 roadmap may close only after T1/T2/T3 artifacts exist and all
  closure gates pass.
- No public export, runtime/provider, package activation, or automatic skill
  invocation claim is made.

## Fail Conditions

- Any source fact is inferred from upstream or local pack without a CVF owner
  surface mapping.
- Any artifact claims production-ready skill governance, runtime enforcement,
  provider-backed proof, CLI/MCP readiness, security certification, or
  automatic safe skill invocation.
- Any checker implementation is added without a repeated defect, source-verified
  field mapping, test plan, and fresh implementation work order.
- Any generated ASSF aggregate is edited directly.

## Verification / Evidence

Required before material commit:

- `git diff --check`;
- `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 940ffadd --head HEAD --enforce`;
- material commit hook chain.

## Current Runtime Freshness Verification

| Runtime claim | Current source checked | Evidence | Disposition |
|---|---|---|---|
| Runtime/checker/source files are outside this batch | staged changed set | `git diff --cached --name-status` shows only AGSG governed markdown/reference files | PASS |
| ASSF generated registry/index is outside this batch | staged changed set | no `docs/reference/agent_system_skills/generated/` or `registry/entries/` path in the changed set | PASS |
| Runtime behavior is not certified | claim boundary and non-goals | no runtime test, provider call, package activation, or checker execution is used as evidence | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_COMPLETION_REVIEW_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON changed | `git diff --cached --name-status` excludes registry JSON paths | PASS |
| Registry Markdown | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | top `Status: ACTIVE_REFERENCE` | PASS |
| External evidence digest | this baseline Source Verification Block | upstream/local advisory inputs are mapped to CVF owner surfaces; sha256 samples: upstream README `68F8BD0777211B4B368722B5DA9849D23D9BACCD660DA294E68B14C24D267FBB`; local scope `8AB56812C0FA9F036003D81C0CAA3D8255E046EBA3AF15D5892E2EEA92FCF15D` | PASS |
| System loop interlock | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | next move closes AGSG lane and parks runtime/checker lanes | PASS |
| Session continuity | session-sync commit after material commit | N/A with reason: intentionally split from material commit | PASS |
| T1 baseline | `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| T1 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| T2 advisory reference | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | top `Status: ACTIVE_REFERENCE` | PASS |
| T3 closeout | `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |
| AGSG-T0 roadmap | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | top `Status: CLOSED_PASS_BOUNDED` | PASS |

| Closure item | Evidence | Status |
|---|---|---|
| Baseline status | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGSG_T0_AGENT_SKILLS_GOVERNANCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` updates to `Status: CLOSED_PASS_BOUNDED` in this batch | PASS |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | PASS |
| T2 advisory reference | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | PASS |
| T3 closeout | `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | PASS |
| Runtime/provider/public claims | N/A with reason: explicitly out of scope | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| AGSG-T1-Q1 | `docs/baselines/CVF_GC018_AGSG_T1_SOURCE_VERIFIED_ASSF_RECONCILIATION_2026-06-28.md` | `Status` | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| AGSG-T1-Q2 | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | `Status` | `ACTIVE_REFERENCE` | `ACTIVE_REFERENCE` | PASS |
| AGSG-T1-Q3 | `docs/reviews/CVF_AGSG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | `Decision / Disposition` | `CLOSE_AGSG_ABSORPTION_LANE_NO_CHECKER_NOW` | `CLOSE_AGSG_ABSORPTION_LANE_NO_CHECKER_NOW` | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSG-T1 source-verified ASSF reconciliation baseline |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - documentation/source-verification only |
| receiptEvidence | N/A with reason: no runtime receipt, provider call, adapter run, checker execution, or package activation |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source verification table, roadmap trace matrix, and closure package rows |
| invocationBoundary | local governed artifact authoring only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | source-verified reconciliation and advisory-route authorization |
| forbiddenExpansion | no runtime activation, plugin import, command import, persona orchestration, hook install, checker implementation, resolver mutation, package instance, CLI/MCP adapter, provider/live proof, public-sync, benchmark, security certification, or production-readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline cites private provenance workspace paths and local
operator-supplied advisory material. Public-safe publication would require a
separate redaction and public-sync authorization.

## Claim Boundary

This baseline authorizes and records documentation-only AGSG reconciliation. It
does not implement any runtime, resolver, package, checker, provider, public,
security, benchmark, production, or external-agent behavior.
