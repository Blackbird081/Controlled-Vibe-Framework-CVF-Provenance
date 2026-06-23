# CVF GC-018 ASSF-T3 Learning And ADIF Promotion Bridge Baseline

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-23

docType: gc018_baseline

Batch ID: ASSF-T3

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: b1969159

executionBaseHead: PENDING_WORKER_START

closureBaseHead: PENDING_WORKER_RETURN

## Purpose

Authorize a bounded ASSF-T3 worker-return lane that defines, as a contract
document only, the Learning And ADIF Promotion Bridge: the governed mapping
by which repeated, accepted learning evidence (LSC learning signals) and
recorded agent-defect findings (ADIF entries) become ASSF skill candidates
in the frozen ASSF-T1 package contract shape, always as `CANDIDATE`, never
self-activated. The contract must define dedupe by root-cause group, an
evidence threshold, a reviewer decision gate, a UAT requirement, and
explicit rejection or session-local outcomes.

This tranche is contract-definition-only, mirroring the ASSF-T1 precedent.
It does not implement a promoter, resolver, generator, drift checker, or any
code; it does not create a real skill candidate entry; it does not run a
learning scan; it does not activate, promote, or set any skill `ACTIVE`; it
does not implement a CLI/MCP adapter or any runtime/provider/live behavior.

## Source / Predecessor Evidence

The predecessor evidence is ASSF-T2 closure (generated index and progressive
resolver, accepted and committed at `3746bd48`), which built the executable
ASSF data plane (registry sources, deterministic generator, drift checker,
read-only resolver) against the frozen ASSF-T1 contract. ASSF-T1 closure
(canonical package contract at `2752d04e`) remains the schema authority: the
compact machine source schema field families, the package lifecycle states
(`CANDIDATE`, `PROPOSED`, `APPROVED`, `ACTIVE`, `DEPRECATED`, `RETIRED`,
`REJECTED`), and the provenance fields a promoted candidate must populate.
The two upstream evidence sources the bridge promotes from already exist:
the LSC promotion-threshold policy and signal-ledger entry shape, and the
ADIF defect entry registry plus its read-only resolver.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T3 is the operator-selected next move after ASSF-T2 closure |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current lane points to ASSF-T3 selection |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | Active handoff for this governed dispatch |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T3 tranche definition |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | mandatory candidate shape and lifecycle authority |
| ASSF-T2 resolver foundation | `governance/compat/run_assf_skill_resolver.py` | the data plane the promoted candidates feed |
| LSC promotion threshold policy | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | learning-evidence threshold and dedupe authority to reuse |
| LSC signal ledger entry shape | `docs/reference/learning_signal_chain/CVF_LEARNING_SIGNAL_LEDGER_ENTRY_TEMPLATE.json` | learning-evidence source shape |
| ADIF entry template | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | defect-finding source shape and promotionState ladder |
| ADIF defect resolver | `governance/compat/run_adif_defect_resolver.py` | defect-finding read-only query surface |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | continuation, legacy, and blind-spot controls |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP surface accounting |

## Decision / Baseline / Proposed Tranche

Decision: dispatch ASSF-T3 as a no-commit, contract-definition-only
worker-return tranche that authors the Learning And ADIF Promotion Bridge
contract document plus its required reference-family README is already
present. Baseline: T3 may create one new governed reference document under
`docs/reference/agent_system_skills/` defining the promotion bridge mapping,
and the worker-return packet. Proposed tranche output: the bridge contract
document and a worker-return packet for reviewer closure. No promoter code,
no resolver, no generator, no drift checker, no real candidate entry, no
learning scan, no skill activation, no CLI/MCP adapter, no migration, no
runtime/provider/live/public behavior.

## Evidence / Verification

Verification for dispatch uses the Source Verification Block below, the
dispatch-quality gate, the ADIF defect registry disclosure gate, the
dispatch-prompt-envelope gate, the foundation storage layout gate, the
roadmap closure freshness gate, the autorun pre-dispatch gate, and the
commit steward preflight. Worker execution evidence belongs in the
worker-return artifacts.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Exhaustive directory claim omits actual children: this dispatch makes no exhaustive-directory claim; the bridge contract enumerates only named source families (LSC, ADIF) by citation, not by claiming a complete folder listing.
- ADIF-0002 - Provider-local interaction accepted as authority: the bridge explicitly keeps promoted skills as `CANDIDATE` requiring reviewer decision and UAT; no provider-local or agent-memory output is treated as authority.
- ADIF-0006 - Source Verification symbol cell contains a value/type: the Source Verification Block below puts only field/path/symbol names in the verified-symbol column, never value assignments or type annotations.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class: scope-exclusion sentences avoid bare gate-trigger tokens; this dispatch is a contract-definition tranche with no corpus scan, readiness, or provider claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T3 must map repeated accepted learning evidence into skill candidates with dedupe, source authority, evidence threshold, reviewer decision, UAT, and explicit rejection/session-local outcomes, with no self-activation | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T3 - Learning And ADIF Promotion Bridge | No self-activation | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The package contract defines the candidate shape and lifecycle states a promoted candidate must use | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | CANDIDATE; PROPOSED; APPROVED; ACTIVE; DEPRECATED; RETIRED; REJECTED | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The package contract defines the provenance fields a promoted candidate must populate | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | originLane | ASSF-T1 contract | VALUE_SET | ACCEPT |
| A read-only ASSF resolver foundation already exists that promoted candidates feed | `governance/compat/run_assf_skill_resolver.py` | resolve | resolve | ASSF resolver | EXISTS | ACCEPT |
| Learning-evidence promotion already has a governed threshold and dedupe-by-root-cause policy to reuse | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | De-dup before promotion | rootCauseGroupId | LSC-T4 promotion threshold policy | LITERAL_INVARIANT | ACCEPT |
| Learning-evidence promotion recommendation is not promotion execution | `docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md` | Promotion recommendation is not promotion execution | Promotion recommendation is not promotion execution | LSC-T4 promotion threshold policy | LITERAL_INVARIANT | ACCEPT |
| The ADIF entry template defines the defect-finding source shape and a promotion ladder | `docs/reference/agent_defect_intelligence/CVF_ADIF_ENTRY_TEMPLATE.md` | Required Fields | promotionState | ADIF entry template | VALUE_SET | ACCEPT |
| A read-only ADIF defect resolver already exists to query findings | `governance/compat/run_adif_defect_resolver.py` | resolve_defect_packet | resolve_defect_packet | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| Dual consumer accounting requires internal and external CLI/MCP rows | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | ASSF-T3 - Learning And ADIF Promotion Bridge (contract-definition-only) |
| Dispatch status | DISPATCH_READY |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Codex reviewer/closer |
| Reason for no worker commit | The bridge contract defines how learning and defect evidence become skill candidates; the reviewer must validate that the mapping preserves dedupe, threshold, reviewer-decision, UAT, and no-self-activation before material closure |
| Next tranche blocked | ASSF-T4 external/legacy intake normalization remains parked until ASSF-T3 closure |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T3 dispatch instruction | Required evidence | Disposition |
|---|---|---|---|
| Map repeated accepted learning evidence into skill candidates | worker defines the LSC-signal-to-ASSF-candidate mapping in the bridge contract | mapping table from LSC signal fields to ASSF candidate fields | READY |
| Map recorded ADIF findings into skill candidates | worker defines the ADIF-entry-to-ASSF-candidate mapping in the bridge contract | mapping table from ADIF entry fields to ASSF candidate fields | READY |
| Require dedupe | worker reuses the LSC root-cause-group dedupe rule in the bridge contract | dedupe rule citing rootCauseGroupId | READY |
| Require source authority and evidence threshold | worker reuses the LSC-T4 threshold policy as the promotion floor | threshold rule citing LSC-T4 | READY |
| Require reviewer decision and UAT | worker defines the reviewer-decision gate and UAT requirement before any candidate advances past CANDIDATE | reviewer-decision and UAT gate definition | READY |
| Require explicit rejection or session-local outcomes | worker defines REJECTED and session-local outcome paths | rejection/session-local outcome definition | READY |
| No self-activation | worker contract forbids any promotion path that sets a skill APPROVED or ACTIVE without reviewer decision and UAT | no-self-activation invariant statement | READY |
| Account for internal and external agents | worker return includes the Dual Agent Surface Matrix | matrix with internal and external CLI/MCP rows | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the bridge contract that internal promotion tooling will later consume | T3 defines the mapping and gates only; it implements no promoter and grants no authority to set a candidate APPROVED or ACTIVE | the bridge contract document and its conformance to the ASSF-T1 lifecycle states | N/A with reason: no internal promoter is implemented by T3 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP promotion or candidate-review adapter | T3 records the external-agent disposition in the bridge contract; it does not implement, expose, or authorize any adapter | dual-agent standard and the ASSF-T1 external-agent disposition field | Deferred adapter boundary; any CLI/MCP adapter requires separate GC-018 and source-verified work order | `DEFERRED_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
|---|---|
| Legacy scan classification | INHERITED_FROM_T0_1_AND_T1 |
| Scan root | `.private_reference/legacy/` (already enumerated by ASSF-T0.1 and reconciled into the ASSF-T1 contract) |
| Inherited evidence | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`; `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| Required worker action | define the promotion bridge against the existing LSC and ADIF source shapes and the ASSF-T1 contract; do not re-run any legacy or learning scan |
| Forbidden shortcut | inventing a new candidate shape instead of reusing the ASSF-T1 contract; treating a learning signal or ADIF finding as already-promoted authority |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
|---|---|
| Re-deriving candidate shape | worker must reuse the frozen ASSF-T1 contract lifecycle states and provenance fields; a conformance mapping is required |
| Self-activation | the bridge contract must forbid any path that reaches APPROVED or ACTIVE without reviewer decision and UAT |
| Dedupe omission | the bridge must reuse the LSC root-cause-group dedupe rule so one root cause yields one candidate |
| Threshold bypass | the bridge must reuse the LSC-T4 threshold policy as the promotion floor, not a new lower bar |
| Evidence laundering | a learning signal or ADIF finding remains evidence, not authority; the bridge must keep promoted output at CANDIDATE pending review |
| External-adapter omission | the bridge contract must carry an external-agent CLI/MCP disposition field |
| New folder front door | the `docs/reference/agent_system_skills/` reference family already has a README front door; the new contract document is added in that existing family |

## Corpus Completeness And Report Integrity

- Corpus task class: WORK_ORDER_DISPATCH.
- Corpus root: ASSF roadmap, this GC-018 baseline, the matching T3 work order, the ASSF-T1 package contract, the LSC-T4 threshold policy, and the ADIF entry template.
- Snapshot time: 2026-06-23.
- Enumeration command: this dispatch inherits the filesystem-backed legacy enumeration `rg --files --hidden --no-ignore .private_reference/legacy` accepted by ASSF-T0.1, and the worker must enumerate the ASSF reference family with `rg --files --hidden --no-ignore docs/reference/agent_system_skills docs/reference/learning_signal_chain docs/reference/agent_defect_intelligence` before authoring the bridge contract.
- Manifest artifact or inline manifest: this baseline and the matching T3 work order define the required output manifest.
- Manifest hash: N/A with reason: dispatch packet only; the legacy corpus snapshot was owned by ASSF-T0.1 and the schema by ASSF-T1.
- Processing ledger artifact or inline ledger: the worker-return's Required Artifact Manifest and conformance mapping sections.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=bridge_contract_plus_worker_return; schema=inherited_from_accepted_T1; ledger_terminal=deferred_to_worker_return; exclusions=promoter code, resolver, generator, drift checker, real candidate entry, learning scan, skill activation, CLI/MCP adapter, runtime, provider/live, public-sync; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no promoter code; no resolver/generator/drift checker; no real candidate entry; no learning or legacy scan; no skill activation; no CLI/MCP adapter; no migration; no runtime/provider/live/public behavior.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: T3 is contract-definition-only and creates no generated aggregate.
- Drift check: N/A with reason: T3 creates no generated aggregate.
- Output traceability: the worker-return maps each bridge contract mapping rule to a roadmap requirement and to the LSC/ADIF/ASSF-T1 source it reuses.
- Adversarial verification: the reviewer must confirm the bridge contract forbids self-activation and reuses the existing dedupe and threshold rules rather than inventing weaker ones.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Required route | learning signals and ADIF findings remain evidence; the bridge promotes them only to CANDIDATE pending reviewer decision and UAT |
| Chain map route | learning signal or defect finding -> ASSF-T3 bridge mapping -> ASSF CANDIDATE -> reviewer decision -> UAT -> APPROVED/ACTIVE or REJECTED |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T3 bridge contract and future ASSF-T4 work |
| Disposition | candidate intake only; promotion never activates a skill |
| Claim boundary | learning and defect evidence remain inputs, not CVF authority; the bridge output is a CANDIDATE proposal only |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- Delta ledger status: REQUIRED_BY_WORKER_RETURN
- Routing matrix status: REQUIRED_BY_WORKER_RETURN
- Semantic sampling status: REQUIRED_BY_WORKER_RETURN
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
|---|---|
| `UNCHANGED_FROM_INTAKE` | the ASSF-T1 contract lifecycle states and the LSC-T4 threshold/dedupe rules remain authority |
| `CHANGED_DISPOSITION` | T3 connects the existing LSC and ADIF evidence shapes to the ASSF candidate shape via a new bridge contract |
| `NEW_FINDING` | any field a promoted candidate needs that the ASSF-T1 contract does not define must be raised as a contract gap, not silently invented |
| `REMOVED_OR_REJECTED` | any promotion path that reaches APPROVED or ACTIVE without reviewer decision and UAT is rejected |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
|---|---|
| `DO_NOW` | author the bridge contract and the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | a promoter implementation, resolver wiring, and any runtime activation remain later-tranche scope |
| `STRATEGIC_OPERATOR_DECISION` | whether a future tranche implements an executable promoter is deferred to the operator |
| `OUT_OF_SCOPE` | migration of existing CVF Web examples, public-sync, runtime/provider/live |
| `RESOLVED_BY_DESIGN` | contract-only scope and the no-self-activation invariant prevent premature activation |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T3-S1 | roadmap ASSF-T3 tranche | promoted evidence becomes a candidate, never self-activated | no-self-activation invariant required | could a high-threshold signal auto-promote to ACTIVE? | rejected |
| ASSF-T3-S2 | LSC-T4 threshold policy | one root cause yields one promotion count | dedupe-by-root-cause required | could two projections of one root cause inflate the count? | rejected |
| ASSF-T3-S3 | dual-agent standard | external CLI/MCP disposition required | bridge contract must carry the field | could a bridge contract omit the external-agent disposition? | rejected |

| Requirement | Dispatch control |
|---|---|
| Avoid repeated omission | the bridge contract must define both the learning side and the ADIF side, not only one |
| Preserve useful evidence detail | promoted candidates must carry provenance back to the originating signal or finding |
| Convert review friction into learning | the worker must record a finding-to-governance disposition for any contract gap found while authoring the bridge |
| Keep machine-check candidate visible | the worker must state whether a future tranche should add a checker that the bridge contract is honored |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the bridge contract references private learning-signal and defect
provenance. Public-facing promotion documentation requires a later
public-safe artifact and public-sync batch.

## Acceptance Criteria

- ASSF-T3 work order is source-verified against the roadmap, the ASSF-T1
  contract, the LSC-T4 threshold policy, the ADIF entry template, and the
  dual-agent standard.
- Worker return is constrained to author the bridge contract document and the
  worker-return packet; no promoter code, no resolver/generator/drift checker,
  no real candidate entry, no learning scan, no skill activation, no CLI/MCP
  adapter, no migration, no commit.
- The bridge contract reuses the ASSF-T1 lifecycle states, the LSC root-cause
  dedupe rule, and the LSC-T4 threshold policy rather than inventing weaker
  ones.
- The bridge contract forbids any path that reaches APPROVED or ACTIVE without
  reviewer decision and UAT.
- Dual Agent Surface Matrix accounts for internal agents and external CLI/MCP
  agents.
- ASSF-T4 remains parked until ASSF-T3 closure.

## Fail Conditions

Fail dispatch or return if the packet invents a new candidate shape instead of
reusing the ASSF-T1 contract, defines a self-activation path, weakens the LSC
dedupe or threshold rules, omits either the learning side or the ADIF side,
omits external-agent disposition, implements promoter code or a CLI/MCP
adapter, changes forbidden paths, or claims runtime/provider/live/public
behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | reviewer updates roadmap status on closure | PENDING |
| GC-018 status | this file | `Status: DISPATCH_READY` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_FOR_WORKER_2026-06-23.md` | `Status: DISPATCH_READY` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_WORKER_RETURN_2026-06-23.md` | PENDING_WORKER_RETURN | PENDING |
| Completion or reviewer artifact | a reviewer-created completion review under the reviews directory | reviewer-owned after return | PENDING |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T3 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T3 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported in this tranche | N/A with reason |
| System loop interlock | this baseline | T2 data plane was required before T3 and is now closed; T3 is required before T4; no automatic package activation | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PENDING |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | bridge contract document plus worker return only | as specified | PASS |
| T1 contract consumption | required | required by work order | PASS |
| Self-activation path | forbidden | forbidden by work order | PASS |
| Dedupe and threshold reuse | required | required by work order | PASS |
| External CLI/MCP disposition | present | Dual Agent Surface Matrix row present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T3 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch-ready contract-definition worker-return lane only |
| receiptEvidence | N/A with reason: worker has not authored the bridge contract yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded learning-and-defect promotion bridge contract document |
| forbiddenExpansion | no promoter code, resolver, generator, drift checker, real candidate entry, skill activation, CLI/MCP adapter, migration, runtime/provider/live, or public-sync |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T3 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this baseline; matching T3 work order; ASSF roadmap and source context reads |
| Allowed scope source | operator instruction to author the ASSF-T3 work order; operator selected contract-definition-only scope |
| Before status evidence | clean HEAD `b1969159` |
| After status evidence | ASSF-T3 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no bridge contract authoring |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t3-learning-and-adif-promotion-bridge-dispatch-2026-06-23` |
| Expected manifest | this baseline; matching T3 work order |
| Actual changed set | this baseline; matching T3 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes ASSF-T3 worker-return execution only. It does not
author the bridge contract, close ASSF-T3, implement a promoter or any code,
create a real skill candidate, activate any skill, run a learning scan,
implement a CLI/MCP adapter, run provider/live proof, public-sync, or
authorize ASSF-T4.
