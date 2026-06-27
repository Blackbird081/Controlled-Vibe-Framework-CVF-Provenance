# CVF GC-018 ASSF-T2 Generated Index And Progressive Resolver Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: gc018_baseline

Batch ID: ASSF-T2

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 4d8ecc06

executionBaseHead: 4d8ecc06

closureBaseHead: 4d8ecc06

## Purpose

Authorize a bounded ASSF-T2 worker-return lane that builds the first executable
ASSF data plane: compact registry source files conforming to the ASSF-T1
package contract, a deterministic generator that builds a generated skill
index from those sources, a drift checker that fails when the index diverges
from its sources, and a read-only progressive resolver that returns bounded
package metadata from task/role/phase/surface/risk selectors before any package
instruction or reference is loaded. T2 must consume the frozen ASSF-T1 package
contract instead of re-deriving schema.

This tranche follows the JSON Generated Aggregate Discipline Standard
(compact sources plus deterministic generator plus drift checker plus focused
tests). It does not implement a CLI/MCP adapter, does not activate any skill,
does not load or execute any package instruction body, and does not migrate any
existing CVF Web example or `governance/skill-library` entry.

## Source / Predecessor Evidence

The predecessor evidence is ASSF-T1 closure (canonical package contract,
accepted and committed at `2752d04e`), which froze the compact machine source
schema, identity/authority/risk/lifecycle field families, the package lifecycle
states, and the storage topology that names `registry/entries/` and
`generated/skill-index.json`. The ASSF-T0.1 absorption ledger and the existing
`governance/skill-library/specs/CVF_SKILL_SPEC.md` remain the upstream inputs
the contract already reconciled; T2 builds against the contract, not against
those upstream sources directly.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T2 is the operator-selected next move after ASSF-T1 closure |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current lane points to ASSF-T2 selection |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | Active handoff for this governed dispatch |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T2 tranche definition; T2 must consume the T1 contract |
| ASSF-T1 package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | mandatory schema and topology input to T2 |
| Generated aggregate standard | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | source/generator/drift/tests discipline |
| Existing resolver precedent | `governance/compat/run_adif_defect_resolver.py` | read-only deterministic resolver pattern to mirror |
| Existing generator/drift precedent | `governance/compat/generate_corpus_scan_registry.py` | deterministic generator and drift-checker pattern to mirror |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | continuation, legacy, and blind-spot controls |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP surface accounting |

## Decision / Baseline / Proposed Tranche

Decision: dispatch ASSF-T2 as a no-commit worker-return tranche that builds the
executable ASSF data plane. Baseline: T2 may create compact registry source
files under the contract-named registry path, a deterministic generator, a
drift checker, a read-only progressive resolver, the generated skill index, the
required folder README front doors, paired tests, and the worker-return packet.
Proposed tranche output: registry sources, generator, drift checker, resolver,
generated index, tests, and a worker-return packet for reviewer closure. No
CLI/MCP adapter, no skill activation, no package instruction execution, no
migration, no runtime/provider/live/public behavior.

## Evidence / Verification

Verification for dispatch uses the Source Verification Block below, the
dispatch-quality gate, the dispatch-prompt-envelope gate, the foundation
storage layout gate, the roadmap closure freshness gate, the autorun
pre-dispatch gate, and the commit steward preflight. Worker execution evidence
belongs in the worker-return artifacts.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T2 must create compact registry sources, a deterministic generator, a drift check, and a resolver returning bounded metadata before loading instructions | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T2 - Generated Index And Progressive Resolver | resolver that returns bounded package metadata | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| ASSF-T2 must consume the ASSF-T1 package contract before creating generated index or resolver surfaces | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Next control action | ASSF-T2 must consume the ASSF-T1 package contract | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The package contract defines the compact machine source schema field families T2 sources must conform to | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | Identity; Provenance; Selectors; Risk and authority; Lifecycle | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The package contract names the storage topology with registry entries and a generated index path | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Storage Topology | generated | ASSF-T1 contract | LITERAL_INVARIANT | ACCEPT |
| The package contract defines the package lifecycle states a resolver must respect | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | CANDIDATE; PROPOSED; APPROVED; ACTIVE; DEPRECATED; RETIRED; REJECTED | ASSF-T1 contract | VALUE_SET | ACCEPT |
| The generated aggregate pattern requires compact sources, a deterministic generator, a drift checker, and focused tests | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Rule | deterministic generator | generated aggregate standard | LITERAL_INVARIANT | ACCEPT |
| Creating a generated aggregate requires recording a generated-source-layout closure token | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Closure Requirement | GENERATED_SOURCE_LAYOUT_ADDED | generated aggregate standard | VALUE_SET | ACCEPT |
| A read-only deterministic resolver pattern already exists to mirror | `governance/compat/run_adif_defect_resolver.py` | resolve_defect_packet | resolve_defect_packet | ADIF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| A deterministic generator and drift-checker pair already exists to mirror | `governance/compat/generate_corpus_scan_registry.py` | generator entry point | generate_corpus_scan_registry | corpus registry generator | EXISTS | ACCEPT |
| Dual consumer accounting requires internal and external CLI/MCP rows | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | ASSF-T2 - Generated Index And Progressive Resolver (full executable data plane) |
| Dispatch status | CLOSED_PASS_BOUNDED |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Codex reviewer/closer |
| Reason for no worker commit | The generator, drift checker, and resolver become the executable ASSF data plane every later tranche depends on; the reviewer must validate determinism, read-only behavior, contract conformance, and test coverage before material closure |
| Next tranche blocked | ASSF-T3 learning/ADIF promotion bridge remains parked until ASSF-T2 closure |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T2 dispatch instruction | Required evidence | Disposition |
|---|---|---|---|
| Create compact registry sources | worker authors at least one contract-conforming compact registry source under the registry path | registry source file(s) plus README front door | READY |
| Create a deterministic generator | worker builds a generator that rebuilds the index byte-stably from sources | generator script plus determinism test | READY |
| Create a drift check | worker builds a checker that fails when the index diverges from sources | drift checker plus drift-detection test | READY |
| Create a progressive resolver | worker builds a read-only resolver returning bounded metadata from selectors before loading instructions | resolver script plus selector tests | READY |
| Resolver returns metadata before loading instructions | resolver reads only the generated index/sources; it does not open package instruction bodies | read-only proof test | READY |
| Consume the ASSF-T1 contract | worker maps each registry source field to a contract field family | contract-conformance table | READY |
| Account for internal and external agents | worker return includes the Dual Agent Surface Matrix | matrix with internal and external CLI/MCP rows | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the ASSF resolver, generator, drift checker, and generated index this tranche builds | T2 implements read-only selection and deterministic generation only; loading metadata never widens authority and never executes a package instruction body | resolver/generator/drift tests and the generated index | N/A with reason: no internal package-instruction loader or executor is implemented by T2 | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill discovery or load adapter | T2 records the external-agent disposition in the registry sources and resolver output; it does not implement, expose, or authorize any adapter | dual-agent standard and the contract external-agent disposition field | Deferred adapter boundary; any CLI/MCP adapter requires separate GC-018 and source-verified work order | `DEFERRED_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
|---|---|
| Legacy scan classification | INHERITED_FROM_T0_1_AND_T1 |
| Scan root | `.private_reference/legacy/` (already enumerated by ASSF-T0.1 and reconciled into the ASSF-T1 contract) |
| Inherited evidence | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`; `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| Required worker action | build registry sources conforming to the contract; do not re-run the legacy scan or re-derive schema |
| Forbidden shortcut | hand-editing the generated index instead of regenerating it from sources; bypassing the contract field families |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
|---|---|
| Re-deriving schema | worker must consume the frozen ASSF-T1 contract; a contract-conformance table is required |
| Hand-edited aggregate | the generated index must be produced only by the deterministic generator; the drift checker must fail on a hand-edited index |
| Resolver loads instructions | the resolver must read only metadata/sources and must never open a package instruction body; a read-only proof test is required |
| Authority widening | resolving or loading metadata must never raise a package authority ceiling |
| External-adapter omission | the registry sources and resolver output must carry an external-agent CLI/MCP disposition field |
| New folder front door | any new `docs/reference/agent_system_skills/` subfolder containing a governed `.md` must include a README front door, named in the artifact manifest up front |

## Corpus Completeness And Report Integrity

- Corpus task class: WORK_ORDER_DISPATCH.
- Corpus root: ASSF roadmap, this GC-018 baseline, the matching T2 work order, the ASSF-T1 package contract, and the generated aggregate standard.
- Snapshot time: 2026-06-23.
- Enumeration command: this dispatch inherits the filesystem-backed legacy enumeration `rg --files --hidden --no-ignore .private_reference/legacy` accepted by ASSF-T0.1, and the worker must enumerate the ASSF reference family with `rg --files --hidden --no-ignore docs/reference/agent_system_skills governance/compat` before building registry sources.
- Manifest artifact or inline manifest: this baseline and the matching T2 work order define the required output manifest.
- Manifest hash: N/A with reason: dispatch packet only; the legacy corpus snapshot was owned and accepted by ASSF-T0.1 and the schema by ASSF-T1.
- Processing ledger artifact or inline ledger: the worker-return's Required Artifact Manifest and Contract Conformance Table sections.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=11_deliverables_returned; schema=inherited_from_accepted_T1; ledger_terminal=all_11_confirmed_present; exclusions=CLI/MCP adapter, skill activation, package instruction execution, migration, runtime, provider/live, public-sync; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no CLI/MCP adapter; no skill activation; no package instruction body execution; no migration of existing CVF Web examples or `governance/skill-library` entries; no runtime/provider/live/public behavior.
- Unreadable or unsupported files: 0.
- Aggregation check: the worker built the generated skill index from per-entry registry sources; the reviewer independently re-ran the drift checker and confirmed PASS.
- Drift check: `python governance/compat/check_assf_skill_index_drift.py` confirmed PASS, independently re-run by the reviewer.
- Output traceability: the worker-return's Contract Conformance Table maps every registry source field to a contract field family; the completion review's Roadmap-To-Work-Order Trace Matrix maps every resolver behavior to a roadmap requirement.
- Adversarial verification: the reviewer independently confirmed the resolver is read-only by source inspection (no SKILL.md or `packages/` path exists in the module) and confirmed the generated index regenerates byte-stably from sources via the worker's tempdir-isolated determinism test, independently re-run.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Required route | consume the accepted ASSF-T1 contract, which already reconciled the ASSF-T0.1 absorption ledger |
| Chain map route | legacy source family -> ASSF-T0.1 candidate ledger -> ASSF-T1 contract -> ASSF-T2 registry sources and resolver -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T2 generated index and resolver and future ASSF-T3/T4 work |
| Disposition | candidate intake only; resolver selection never activates a skill |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority; resolver output is metadata only |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- Delta ledger status: REQUIRED_BY_WORKER_RETURN
- Routing matrix status: REQUIRED_BY_WORKER_RETURN
- Semantic sampling status: REQUIRED_BY_WORKER_RETURN
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
|---|---|
| `UNCHANGED_FROM_INTAKE` | the ASSF-T1 contract field families and lifecycle states remain the schema authority |
| `CHANGED_DISPOSITION` | T2 changes the contract from a definition into executable registry sources, a generator, a drift checker, and a resolver |
| `NEW_FINDING` | any field a registry source needs that the contract does not define must be raised as a contract gap, not silently invented |
| `REMOVED_OR_REJECTED` | hand-edited aggregates and instruction-loading resolver behavior are rejected |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
|---|---|
| `DO_NOW` | build registry sources, generator, drift checker, resolver, generated index, tests, and the worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | CLI/MCP adapter and any runtime activation remain ASSF-T5/T7 scope |
| `STRATEGIC_OPERATOR_DECISION` | learning/ADIF promotion into registry sources is deferred to ASSF-T3 |
| `OUT_OF_SCOPE` | migration of existing CVF Web examples, public-sync, runtime/provider/live |
| `RESOLVED_BY_DESIGN` | read-only resolver and drift-checked generator prevent premature activation or aggregate drift |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T2-S1 | roadmap ASSF-T2 tranche | resolver returns metadata before loading instructions | read-only resolver required | could the resolver open a package instruction body? | rejected |
| ASSF-T2-S2 | generated aggregate standard Rule | aggregate built only by deterministic generator | drift checker required | could the index be hand-edited? | rejected |
| ASSF-T2-S3 | dual-agent standard | external CLI/MCP disposition required | matrix and source field required | could an internal-only resolver pass? | rejected |

| Requirement | Dispatch control |
|---|---|
| Avoid repeated omission | the resolver must respect every contract lifecycle state and selector family |
| Preserve useful legacy detail | registry sources must carry the provenance fields the contract reconciled from the T0.1 ledger |
| Convert review friction into learning | the worker must record a finding-to-governance disposition for any contract gap found while building sources |
| Keep machine-check candidate visible | the worker must state whether the drift checker should be wired into an autorun phase before ASSF-T3 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the registry sources carry provenance reconciled from a private legacy
absorption ledger. Public-facing skill index, README, or CLI/MCP documentation
requires a later public-safe artifact and public-sync batch.

## Acceptance Criteria

- ASSF-T2 work order is source-verified against the roadmap, the ASSF-T1
  contract, the generated aggregate standard, and the dual-agent standard.
- Worker return is constrained to build the registry sources, generator, drift
  checker, resolver, generated index, required folder READMEs, and tests; no
  commit, no CLI/MCP adapter, no skill activation, no package instruction
  execution, no migration.
- The generated index is produced only by the deterministic generator and the
  drift checker fails on a hand-edited index.
- The resolver is read-only, deterministic, and returns metadata without
  loading any package instruction body.
- Dual Agent Surface Matrix accounts for internal agents and external CLI/MCP
  agents.
- ASSF-T3 remains parked until ASSF-T2 closure.

## Fail Conditions

Fail dispatch or return if the packet re-derives schema instead of consuming
the ASSF-T1 contract, hand-edits the generated index, builds a resolver that
loads or executes package instruction bodies, widens authority on load,
implements a CLI/MCP adapter or runtime activation, omits external-agent
disposition, changes forbidden paths, or claims runtime/provider/live/public
behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T2_CLOSED_PASS_BOUNDED_PENDING_T3_SELECTION` | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_WORKER_RETURN_2026-06-23.md` | `Status: COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, accepted after reviewer repair | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Generated source layout | registry sources plus generator plus drift checker | `GENERATED_SOURCE_LAYOUT_ADDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | BLOCKED with reason: ASSF-T2 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | BLOCKED with reason: ASSF-T2 is not authorized to update GC-051 corpus registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason | no external evidence imported in this tranche | N/A with reason |
| System loop interlock | this baseline | T1 contract was required before T2 and is now consumed; T2 is required before T3; no automatic package activation | PASS |
| Session continuity | active session sync after material commit | separate session-sync lane after material commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Build scope | generator, drift, resolver, registry sources, generated index, tests | as specified | PASS |
| T1 contract consumption | required | required by work order | PASS |
| Generated index hand-edit | forbidden; drift-checked | forbidden by work order | PASS |
| Resolver instruction loading | forbidden; read-only | forbidden by work order | PASS |
| External CLI/MCP disposition | present | Dual Agent Surface Matrix row present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T2 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch-ready executable data-plane worker-return lane only |
| receiptEvidence | N/A with reason: worker has not built the data plane yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded generated index, generator, drift checker, and read-only resolver |
| forbiddenExpansion | no CLI/MCP adapter, skill activation, package instruction execution, migration, runtime/provider/live, public-sync, or hand-edited aggregate |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T2 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, file authoring, governance gates |
| Target paths | this baseline; matching T2 work order; ASSF roadmap context reads |
| Allowed scope source | operator instruction to author the ASSF-T2 work order with full executable scope |
| Before status evidence | clean HEAD `4d8ecc06` |
| After status evidence | ASSF-T2 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no data-plane build |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t2-generated-index-and-progressive-resolver-dispatch-2026-06-23` |
| Expected manifest | this baseline; matching T2 work order |
| Actual changed set | this baseline; matching T2 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes ASSF-T2 worker-return execution only. It does not build
the data plane, close ASSF-T2, implement a CLI/MCP adapter, activate any skill,
execute any package instruction body, migrate any existing CVF Web example, run
provider/live proof, public-sync, or authorize ASSF-T3.
