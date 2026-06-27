# CVF GC-018 Baseline: ASSF-PIC-T4 Web Projection Bridge Decision

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: baseline

Batch ID: ASSF-PIC-T4

dispatchBaseHead: ecfc911b

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | release and close ASSF-PIC-T4 as a decision-only tranche |
| Baseline | Web projection bridge remains deferred under certification hold |
| Proposed tranche | `ASSF-PIC-T4` |
| Worker route | Codex single-agent multi-role execution |
| Closure posture | `CLOSED_PASS_BOUNDED` |

## Purpose

Release and close ASSF-PIC-T4 as a bounded Web projection bridge decision for
the selected candidate `cvf-dispatch-quality-reviewer`. This baseline records
that no Web projection bridge is released because the candidate remains
uncertified and UAT has not started.

## Scope / Methodology

Applies to decision evidence only:

- Web projection decision;
- schema bridge disposition;
- external-agent adapter disposition;
- roadmap T4/T5 status update after accepted closure.

Does not apply to Web runtime source, registry source, generated index,
resolver source, package roots, adapter implementation, provider/live proof,
public-sync, push, activation, or package certification.

## Evidence / Verification

| Evidence | Result |
|---|---|
| `python governance/compat/check_assf_skill_index_drift.py` | PASS - skill index is in sync with registry entry sources |
| `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | returned one metadata item for `cvf-dispatch-quality-reviewer` with candidate status and deferred external adapter disposition |
| Source reads | T2/T3 completions, selected registry entry, Web projection contract, lifecycle guard contract, and T6 Web audit |

## Findings / Position

The T4 decision is `WEB_PROJECTION_DEFERRED_CERTIFICATION_HELD`.

The selected candidate remains `uatState: NOT_STARTED` and
`certificationState: NOT_STARTED`. The Web projection contract permits
`CERTIFIED_PACKAGE_PROJECTION` only after package certification evidence exists.
The T7 lifecycle guard requires `uatState: PASSED` before
`certificationState: CERTIFIED`. The T6 audit confirms the current Web `Skill`
type carries `corpusClass`, not ASSF `certificationState`, and found zero
certified Web projections.

## Dependency Release Evidence

| Dependency | Status | Evidence |
|---|---|---|
| WODS reopen condition was handled before PIC-T4 | SATISFIED | WODS-T4 closure commit `0d81a814`; session-sync commit `ecfc911b` |
| PIC-T3 closed bounded | SATISFIED | `docs/reviews/CVF_ASSF_PIC_T3_GENERATED_INDEX_RESOLVER_INTEGRATION_DECISION_COMPLETION_2026-06-26.md` |
| Candidate lifecycle remains not certified | SATISFIED | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` |
| Web projection bridge requires certification and separate schema work | SATISFIED | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC-T4 is Web projection bridge decision | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | `ASSF-PIC-T4 - Web Projection Bridge Decision` | `ASSF-PIC-T4` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| Candidate UAT remains not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| Candidate certification remains not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `certificationState` | ASSF registry entry | VALUE_SET | ACCEPT |
| Candidate external adapter remains deferred | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | root object | `externalCliMcpDisposition` | ASSF registry entry | VALUE_SET | ACCEPT |
| Web certified projection token requires certification evidence | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Classification Vocabulary | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Web display is not certification evidence | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Canonical-Vs-Presentation Boundary | `PACKAGE_CANDIDATE` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Bridge requires certified package and Web schema work | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Web Projection Certification Bridge | `CERTIFIED_PACKAGE_PROJECTION` | ASSF lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| Current Web type lacks ASSF certification field | `docs/audits/CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | Findings / Position | `corpusClass` | ASSF-T6 audit | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Selected registry entry | read current source entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lifecycle fields remain not started; external adapter remains deferred |
| Generated index drift | ran current drift check before T4 closure | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Resolver readout | ran current resolver query before T4 closure | `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role dispatcher --phase DISPATCH_AUTHORING --surface governance/compat --risk-ceiling R0` | candidate metadata readout only; no activation or adapter authority |
| Web projection surface | read current contract and T6 audit | `CVF_ASSF_WEB_PROJECTION_CONTRACT.md`; `CVF_ASSF_T6_EXISTING_WEB_SKILL_EXAMPLE_MIGRATION_AUDIT_2026-06-25.md` | bridge deferred; no Web runtime path changed |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied: this baseline names bounded files only, cites
CVF-governed sources, treats keyword-heavy boundary text as scope control, and
keeps symbol cells to field names or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator direction to governed GC-018/source-verification/closure lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-PIC-T4 baseline |
| Disposition | no external material absorbed |
| Claim boundary | repository-local decision evidence only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T4 decision artifacts | internal agents may treat the selected candidate as candidate-only; no certified Web projection, activation, package execution, registry mutation, or Web bridge is authorized | T2/T3 closures, registry entry, T6/T7 contracts | no internal Web loader or bridge is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future package projection or adapter readout | external agents cannot certify, mutate, activate, execute, or consume package instructions through this decision | registry external disposition and adapter honesty rules | adapter remains deferred and requires a later source-verified work order | `DEFERRED_WITH_REASON` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_FOR_CODEX_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PIC_T4_WEB_PROJECTION_BRIDGE_DECISION_COMPLETION_2026-06-26.md` | `Reviewer verdict: CLOSED_PASS_BOUNDED`; `Web projection disposition: WEB_PROJECTION_DEFERRED_CERTIFICATION_HELD` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | T4 `Status: CLOSED_PASS_BOUNDED`; T5 `Status: READY_FOR_GC018_AFTER_T4_CLOSURE` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized by ASSF-PIC-T4 | no registry JSON in changed set | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized by ASSF-PIC-T4 | no registry Markdown mutation | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external artifact is created | no external digest applies | N/A with reason |
| System loop interlock | this baseline and T4 completion review | no package activation, runtime loop, provider call, public-sync, or worker commit occurred | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded from material changed set | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance decision; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T4 Web projection bridge decision |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- decision-only closure |
| receiptEvidence | CVF_RECEIPT_PRESENT - source reads, drift check, resolver readout, and local governance gates are recorded in closure |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency evidence, ADIF disclosure, and completion review |
| invocationBoundary | governed local documentation and read-only local checks only |
| interceptionBoundary | no provider, CLI, MCP, Web runtime, adapter, or package execution interception claim |
| claimLanguage | defers Web projection bridge because certification and schema prerequisites are absent |
| forbiddenExpansion | no package instance, certification decision, lifecycle mutation, registry mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, or session-sync in material commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex multi-role dispatcher/worker/reviewer/closer |
| Agent type | single-agent multi-role |
| Provider or surface | local workspace |
| Session or invocation | ASSF-PIC-T4, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Before status evidence | HEAD `ecfc911b`; `git status --short` returned no paths |
| Target paths | this baseline; paired work order; decision review; completion review; ASSF-PIC roadmap |
| Claim boundary | decision-only closure; no runtime, Web, adapter, generated-index, resolver, registry, provider, public, or session-sync mutation |

## Claim Boundary

This baseline closes only the ASSF-PIC-T4 decision. It does not create,
certify, activate, project, execute, export, or adapt any package.
