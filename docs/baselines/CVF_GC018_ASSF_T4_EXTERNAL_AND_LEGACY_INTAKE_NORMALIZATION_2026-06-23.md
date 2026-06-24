# CVF GC-018 ASSF-T4 External And Legacy Intake Normalization Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: gc018_baseline

Batch ID: ASSF-T4

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 050741bb

executionBaseHead: 5a4f9591

closureBaseHead: 5a4f9591

## Purpose

Authorize a bounded ASSF-T4 worker-return lane that defines, as a contract
document only, the External And Legacy Intake Normalization mapping: the
governed way external skill screening dispositions and legacy absorption
ledger dispositions are unified into the frozen ASSF-T1 package candidate
shape, always as `CANDIDATE`, never self-activated. The contract must
preserve provenance, license, and security fields, and must reject any
provider-local or legacy claim that cannot be reverified against a
CVF-governed source.

This tranche is contract-definition-only, mirroring the ASSF-T1 and ASSF-T3
precedents. It does not implement a normalizer, promoter, resolver,
generator, or any code; it does not create a real skill candidate entry; it
does not run an external or legacy scan; it does not activate, promote, or
set any skill `ACTIVE`; it does not implement a CLI/MCP adapter or any
runtime/provider/live behavior.

## Source / Predecessor Evidence

The predecessor evidence is ASSF-T3 closure (Learning And ADIF Promotion
Bridge contract, accepted and committed at `3a481db5`), which defined the
first intake lane (learning signals and defect findings) into the ASSF
candidate shape. ASSF-T4 defines the parallel intake lane for external and
legacy sources. ASSF-T1 closure (canonical package contract at `2752d04e`)
remains the schema authority: the candidate shape, the package lifecycle
states, and the provenance fields. The two upstream intake vocabularies the
normalization unifies already exist: the external skill screening matrix
dispositions and the ASSF-T0.1 legacy absorption ledger dispositions.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T4 is the operator-selected next move after ASSF-T3 closure |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current lane points to ASSF-T4 selection |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | Active handoff for this governed dispatch |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T4 tranche definition |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | mandatory candidate shape and lifecycle authority |
| ASSF-T3 promotion bridge contract | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | sibling intake-lane contract whose candidate shape, dedupe, threshold, reviewer/UAT, and no-self-activation pattern T4 reuses |
| External skill screening matrix | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | external-intake disposition vocabulary and normalization-field source |
| ASSF-T0.1 legacy absorption ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | legacy-intake disposition vocabulary source |
| Legacy absorption coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | canonical legacy coverage index |
| External knowledge absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external-intake routing authority |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | continuation, legacy, and blind-spot controls |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP surface accounting |

## Decision / Baseline / Proposed Tranche

Decision: dispatch ASSF-T4 as a no-commit, contract-definition-only
worker-return tranche that authors the External And Legacy Intake
Normalization contract document. Baseline: T4 may create one new governed
reference document under `docs/reference/agent_system_skills/` defining the
normalization mapping, and the worker-return packet. Proposed tranche
output: the normalization contract document and a worker-return packet for
reviewer closure. No normalizer code, no promoter, no resolver, no generator,
no real candidate entry, no external or legacy scan, no skill activation, no
CLI/MCP adapter, no migration, no runtime/provider/live/public behavior.

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

- ADIF-0001 - Exhaustive directory claim omits actual children: this dispatch makes no exhaustive-directory claim; it cites named source families (external screening matrix, T0.1 ledger) by path, not by claiming a complete folder listing.
- ADIF-0002 - Provider-local interaction accepted as authority: the normalization explicitly rejects any provider-local or legacy claim that cannot be reverified against a CVF-governed source, and keeps normalized output at `CANDIDATE` pending reviewer decision.
- ADIF-0006 - Source Verification symbol cell contains a value/type: the Source Verification Block below puts only field/path/symbol names in the verified-symbol column, never value assignments or type annotations.
- ADIF-0007 - Gate keyword in exclusion prose triggers wrong evidence class: scope-exclusion sentences avoid bare gate-trigger tokens; this dispatch is a contract-definition tranche with no new corpus scan, readiness, or provider claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T4 must unify external skill screening and legacy absorption into the package-candidate contract, preserve provenance/license/security, and reject provider-local or legacy claims that cannot be reverified against CVF-governed sources | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T4 - External And Legacy Intake Normalization | reject provider-local or legacy claims | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The package contract defines the candidate shape and lifecycle states a normalized candidate must use | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | CANDIDATE; PROPOSED; APPROVED; ACTIVE; DEPRECATED; RETIRED; REJECTED | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The package contract defines the provenance fields a normalized candidate must populate | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | originLane | ASSF-T1 contract | VALUE_SET | ACCEPT |
| A sibling intake-lane contract already defines the candidate shape, no-self-activation invariant, and reviewer/UAT pattern T4 reuses | `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md` | No-Self-Activation Invariant | No-Self-Activation Invariant | ASSF-T3 bridge contract | LITERAL_INVARIANT | ACCEPT |
| The external skill screening matrix defines the external-intake disposition vocabulary T4 must reconcile | `docs/reference/archive/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md` | screening disposition column | ACCEPT_AS_PATTERN; DEFER_RUNTIME_GATED; MERGE_AS_PATTERN | external skill screening matrix | VALUE_SET | ACCEPT |
| The ASSF-T0.1 legacy ledger defines the legacy-intake disposition vocabulary T4 must reconcile | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | Absorption Candidate Ledger | ABSORB_AS_CONTRACT_INPUT; REFERENCE_ONLY; BLOCKED_UNVERIFIED_SOURCE | ASSF-T0.1 audit ledger | VALUE_SET | ACCEPT |
| The legacy absorption coverage index is the canonical legacy coverage authority | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | coverage index | CVF_LEGACY_ABSORPTION_COVERAGE_INDEX | legacy coverage index | EXISTS | ACCEPT |
| The external knowledge absorption chain map is the external-intake routing authority | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | chain map | CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP | external absorption chain map | EXISTS | ACCEPT |
| Dual consumer accounting requires internal and external CLI/MCP rows | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | ASSF-T4 - External And Legacy Intake Normalization (contract-definition-only) |
| Dispatch status | CLOSED_PASS_BOUNDED |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Codex reviewer/closer |
| Reason for no worker commit | The normalization contract defines how external and legacy evidence become skill candidates and how unverifiable claims are rejected; the reviewer must validate that the mapping preserves provenance/license/security, reuses the no-self-activation pattern, and rejects unreverifiable claims before material closure |
| Next tranche blocked | ASSF-T5 composition/dependency/conflict/capability controls remains parked until ASSF-T4 closure |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T4 dispatch instruction | Required evidence | Disposition |
|---|---|---|---|
| Unify external skill screening into the package-candidate contract | worker defines the external-screening-disposition-to-ASSF-candidate mapping | mapping table from external screening dispositions to ASSF candidate fields/states | READY |
| Unify legacy absorption into the package-candidate contract | worker defines the legacy-ledger-disposition-to-ASSF-candidate mapping | mapping table from T0.1 ledger dispositions to ASSF candidate fields/states | READY |
| Preserve provenance, license, and security | worker requires provenance/license/security fields on every normalized candidate | provenance/license/security field requirement in the contract | READY |
| Reject claims that cannot be reverified against CVF-governed sources | worker defines a reverification gate that routes unverifiable claims to a rejected/blocked outcome | reverification gate mapping `BLOCKED_UNVERIFIED_SOURCE` and unverifiable external claims to REJECTED/blocked | READY |
| No self-activation | worker reuses the ASSF-T3 no-self-activation invariant; normalized output is always CANDIDATE | no-self-activation invariant statement | READY |
| Account for internal and external agents | worker return includes the Dual Agent Surface Matrix | matrix with internal and external CLI/MCP rows | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the normalization contract that future internal intake tooling will consume | T4 defines the mapping and gates only; it implements no normalizer and grants no authority to set a candidate APPROVED or ACTIVE | the normalization contract document and its conformance to the ASSF-T1 lifecycle states | N/A with reason: no internal normalizer is implemented by T4 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP external-intake or candidate-review adapter | T4 records the external-agent disposition in the normalization contract; it does not implement, expose, or authorize any adapter | dual-agent standard and the ASSF-T1 external-agent disposition field | Deferred adapter boundary; any CLI/MCP adapter requires separate GC-018 and source-verified work order | `DEFERRED_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
|---|---|
| Legacy scan classification | INHERITED_FROM_T0_1 |
| Scan root | `.private_reference/legacy/` (already enumerated by ASSF-T0.1) |
| Inherited evidence | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`; `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Required worker action | define the normalization mapping against the existing external screening and T0.1 ledger disposition vocabularies and the ASSF-T1 contract; do not re-run any external or legacy scan |
| Forbidden shortcut | inventing a new candidate shape instead of reusing the ASSF-T1 contract; accepting a legacy or external claim without a reverification path |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
|---|---|
| Re-deriving candidate shape | worker must reuse the frozen ASSF-T1 contract lifecycle states and provenance fields; a conformance mapping is required |
| Self-activation | the normalization contract must reuse the ASSF-T3 no-self-activation invariant; normalized output is always CANDIDATE |
| Evidence laundering | an external or legacy claim remains evidence, not authority; unverifiable claims must route to REJECTED/blocked |
| Provenance loss | every normalized candidate must carry provenance, license, and security back to its external or legacy source |
| Reverification bypass | the contract must define a reverification gate against CVF-governed sources; provider-local claims that cannot be reverified are rejected |
| External-adapter omission | the normalization contract must carry an external-agent CLI/MCP disposition field |
| New folder front door | the `docs/reference/agent_system_skills/` reference family already has a README front door; the new contract document is added in that existing family |

## Corpus Completeness And Report Integrity

- Corpus task class: WORK_ORDER_DISPATCH.
- Corpus root: ASSF roadmap, this GC-018 baseline, the matching T4 work order, the ASSF-T1 package contract, the ASSF-T3 bridge contract, the external screening matrix, and the ASSF-T0.1 ledger.
- Snapshot time: 2026-06-23.
- Enumeration command: this dispatch inherits the filesystem-backed legacy enumeration `rg --files --hidden --no-ignore .private_reference/legacy` accepted by ASSF-T0.1, and the worker must enumerate the ASSF reference family with `rg --files --hidden --no-ignore docs/reference/agent_system_skills docs/reference/archive docs/reference/external_agent_review` before authoring the normalization contract.
- Manifest artifact or inline manifest: this baseline and the matching T4 work order define the required output manifest.
- Manifest hash: N/A with reason: dispatch packet only; the legacy corpus snapshot was owned by ASSF-T0.1 and the schema by ASSF-T1.
- Processing ledger artifact or inline ledger: the worker-return's Required Artifact Manifest and conformance mapping sections.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=normalization_contract_plus_worker_return; schema=inherited_from_accepted_T1; ledger_terminal=deferred_to_worker_return; exclusions=normalizer code, promoter, resolver, generator, real candidate entry, external/legacy scan, skill activation, CLI/MCP adapter, runtime, provider/live, public-sync; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no normalizer code; no promoter/resolver/generator; no real candidate entry; no external or legacy scan; no skill activation; no CLI/MCP adapter; no migration; no runtime/provider/live/public behavior.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: T4 is contract-definition-only and creates no generated aggregate.
- Drift check: N/A with reason: T4 creates no generated aggregate.
- Output traceability: the worker-return maps each normalization mapping rule to a roadmap requirement and to the external/legacy/ASSF-T1 source it reuses.
- Adversarial verification: the reviewer must confirm the normalization contract preserves provenance/license/security, reuses the no-self-activation invariant, and rejects unreverifiable claims rather than silently accepting them.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Required route | external and legacy sources remain evidence; the normalization promotes them only to CANDIDATE pending reviewer decision, and rejects unreverifiable claims |
| Chain map route | external screening or legacy ledger disposition -> ASSF-T4 normalization mapping -> ASSF CANDIDATE or REJECTED -> reviewer decision -> UAT -> APPROVED/ACTIVE or REJECTED |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T4 normalization contract and future ASSF-T5 work |
| Disposition | candidate intake only; normalization never activates a skill |
| Claim boundary | external and legacy skills remain candidate inputs, not CVF authority; unverifiable claims are rejected |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T3_LEARNING_AND_ADIF_PROMOTION_BRIDGE_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_PROMOTION_BRIDGE_CONTRACT.md`
- Delta ledger status: REQUIRED_BY_WORKER_RETURN
- Routing matrix status: REQUIRED_BY_WORKER_RETURN
- Semantic sampling status: REQUIRED_BY_WORKER_RETURN
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
|---|---|
| `UNCHANGED_FROM_INTAKE` | the ASSF-T1 contract lifecycle states and the ASSF-T3 no-self-activation invariant remain authority |
| `CHANGED_DISPOSITION` | T4 adds the external/legacy intake lane alongside the T3 learning/ADIF lane, mapping screening and ledger dispositions to the ASSF candidate shape |
| `NEW_FINDING` | any field a normalized candidate needs that the ASSF-T1 contract does not define must be raised as a contract gap, not silently invented |
| `REMOVED_OR_REJECTED` | any acceptance of an unreverifiable provider-local or legacy claim, or any self-activation path, is rejected |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
|---|---|
| `DO_NOW` | author the normalization contract and the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | a normalizer implementation, resolver wiring, and any runtime activation remain later-tranche scope |
| `STRATEGIC_OPERATOR_DECISION` | whether a future tranche implements an executable normalizer is deferred to the operator |
| `OUT_OF_SCOPE` | migration of existing CVF Web examples, public-sync, runtime/provider/live |
| `RESOLVED_BY_DESIGN` | contract-only scope, the no-self-activation invariant, and the reverification gate prevent premature activation and evidence laundering |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T4-S1 | roadmap ASSF-T4 tranche | unverifiable provider-local or legacy claims must be rejected | reverification gate required | could an external claim with no CVF-governed source be accepted as CANDIDATE? | rejected |
| ASSF-T4-S2 | roadmap ASSF-T4 tranche | provenance/license/security must be preserved | provenance/license/security fields required | could a normalized candidate drop its source license? | rejected |
| ASSF-T4-S3 | dual-agent standard | external CLI/MCP disposition required | normalization contract must carry the field | could the contract omit the external-agent disposition? | rejected |

| Requirement | Dispatch control |
|---|---|
| Avoid repeated omission | the normalization contract must define both the external side and the legacy side, not only one |
| Preserve useful evidence detail | normalized candidates must carry provenance/license/security back to the originating external or legacy source |
| Convert review friction into learning | the worker must record a finding-to-governance disposition for any contract gap found while authoring the normalization |
| Keep machine-check candidate visible | the worker must state whether a future tranche should add a checker that normalized candidates carry valid reverifiable provenance |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the normalization contract references private legacy provenance and
external screening evidence. Public-facing intake documentation requires a
later public-safe artifact and public-sync batch.

## Acceptance Criteria

- ASSF-T4 work order is source-verified against the roadmap, the ASSF-T1
  contract, the ASSF-T3 bridge contract, the external screening matrix, the
  ASSF-T0.1 ledger, and the dual-agent standard.
- Worker return is constrained to author the normalization contract document
  and the worker-return packet; no normalizer code, no promoter/resolver/
  generator, no real candidate entry, no external or legacy scan, no skill
  activation, no CLI/MCP adapter, no migration, no commit.
- The normalization contract reuses the ASSF-T1 lifecycle states and the
  ASSF-T3 no-self-activation invariant rather than inventing weaker ones.
- The normalization contract requires provenance, license, and security on
  every normalized candidate and defines a reverification gate that rejects
  claims that cannot be reverified against CVF-governed sources.
- Dual Agent Surface Matrix accounts for internal agents and external CLI/MCP
  agents.
- ASSF-T5 remains parked until ASSF-T4 closure.

## Fail Conditions

Fail dispatch or return if the packet invents a new candidate shape instead
of reusing the ASSF-T1 contract, defines a self-activation path, accepts an
unreverifiable provider-local or legacy claim, drops provenance/license/
security, omits either the external side or the legacy side, omits
external-agent disposition, implements normalizer code or a CLI/MCP adapter,
changes forbidden paths, or claims runtime/provider/live/public behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T4_CLOSED_PASS_BOUNDED_PENDING_T5_SELECTION` | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer repairs | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T4_EXTERNAL_AND_LEGACY_INTAKE_NORMALIZATION_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T4 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T4 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no new external evidence imported; T4 reuses existing screening and ledger dispositions | N/A with reason |
| System loop interlock | this baseline | T3 bridge contract was required before T4 and is now closed; T4 is required before T5; no automatic package activation | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch status | dispatched then closed | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | normalization contract document plus worker return only | as specified | PASS |
| T1 contract consumption | required | required by work order | PASS |
| Self-activation path | forbidden | forbidden by work order | PASS |
| Provenance/license/security preservation | required | required by work order | PASS |
| Reverification gate for unverifiable claims | required | required by work order | PASS |
| External CLI/MCP disposition | present | Dual Agent Surface Matrix row present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T4 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - contract-definition worker-return lane, now closed |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-closure and reviewer-fast autorun receipts recorded in the completion review |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded external-and-legacy intake normalization contract document |
| forbiddenExpansion | no normalizer code, promoter, resolver, generator, real candidate entry, skill activation, CLI/MCP adapter, migration, runtime/provider/live, or public-sync |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T4 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver query, file authoring, governance gates |
| Target paths | this baseline; matching T4 work order; ASSF roadmap and source context reads |
| Allowed scope source | operator instruction to author the ASSF-T4 work order; operator selected contract-definition-only scope |
| Before status evidence | clean worktree at HEAD `050741bb` (`git status --short` empty before this dispatch pair) |
| After status evidence | ASSF-T4 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no normalization contract authoring |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t4-external-and-legacy-intake-normalization-dispatch-2026-06-23` |
| Expected manifest | this baseline; matching T4 work order |
| Actual changed set | this baseline; matching T4 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes ASSF-T4 worker-return execution only. It does not
author the normalization contract, close ASSF-T4, implement a normalizer or
any code, create a real skill candidate, activate any skill, run an external
or legacy scan, implement a CLI/MCP adapter, run provider/live proof,
public-sync, or authorize ASSF-T5.
