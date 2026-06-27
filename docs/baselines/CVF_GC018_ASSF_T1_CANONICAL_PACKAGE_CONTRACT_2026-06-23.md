# CVF GC-018 ASSF-T1 Canonical Package Contract And Storage Topology Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-23

docType: gc018_baseline

Batch ID: ASSF-T1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: ed7d0580

executionBaseHead: PENDING_WORKER_START

closureBaseHead: f79853a4

## Purpose

Authorize a bounded, contract-definition-only ASSF-T1 worker-return lane that
freezes the canonical system-skill package contract and storage topology as a
single governed reference document. T1 must reconcile the existing CVF Skill
Spec and the accepted ASSF-T0.1 absorption candidate ledger instead of
creating a competing skill definition, and must consume the T0.1 ledger before
defining any schema field.

This is contract-definition-only by operator decision. T1 does not create the
canonical package root directory, any `SKILL.md`, any `skill.source.json`, any
generated index, any resolver, or any example package on disk. Root creation,
generated index, and resolver remain ASSF-T2 scope; migration of existing
CVF Web examples remains ASSF-T6 scope.

## Source / Predecessor Evidence

The predecessor evidence is ASSF-T0 closure (owner/surface audit), ASSF-T0.1
closure (legacy absorption candidate ledger, accepted by the Codex reviewer at
commit `c76cbac7`), and the ASSF roadmap's ASSF-T1 tranche definition. The
existing `governance/skill-library/specs/CVF_SKILL_SPEC.md` is the current
CVF-owned skill definition surface that T1 must reconcile against, not replace.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | ASSF-T1 is the operator-selected next move after ASSF-T0.1 closure |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current lane points to ASSF-T1 selection |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | Active handoff for this governed dispatch |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T1 tranche definition; T1 must consume the T0.1 ledger |
| ASSF-T0.1 audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | mandatory legacy-absorption input to T1 |
| Existing skill spec | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | current CVF skill definition surface to reconcile |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | continuation, legacy, and blind-spot controls |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | internal and external CLI/MCP surface accounting |

## Decision / Baseline / Proposed Tranche

Decision: dispatch ASSF-T1 as a no-commit, contract-definition-only
worker-return tranche. Baseline: T1 may author exactly one durable governed
reference document defining the canonical package contract and storage
topology, plus the paired worker-return packet. Proposed tranche output: the
canonical package contract reference doc and a worker-return packet for
reviewer closure. No package root, no `SKILL.md`, no `skill.source.json`, no
generated index, no resolver, no example package, no migration.

## Evidence / Verification

Verification for dispatch uses the Source Verification Block below, the
dispatch-quality gate, the dispatch-prompt-envelope gate, the roadmap closure
freshness gate, the autorun pre-dispatch gate, and the commit steward
preflight. Worker execution evidence belongs in the worker-return artifacts.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T1 must define the package contract and reconcile the CVF Skill Spec and the T0.1 ledger rather than create a competing definition | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T1 - Canonical Package Contract And Storage Topology | reconcile existing CVF Skill Spec and the ASSF-T0.1 legacy absorption ledger | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| ASSF-T1 must consume the T0.1 candidate ledger before schema work | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Continuation Decision; Next control action | ASSF-T1 must consume the T0.1 candidate ledger before schema | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| The existing CVF Skill Spec defines seven required sections | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | Required Sections | Skill Identity; Intent Layer; Capability Layer; Risk Profile; Authority Mapping | skill spec | VALUE_SET | ACCEPT |
| The existing CVF Skill Spec defines four skill classification classes | `governance/skill-library/specs/CVF_SKILL_SPEC.md` | Skill Classification | Assistive; Advisory; Executable; Analytical | skill spec | VALUE_SET | ACCEPT |
| The T0.1 absorption ledger provides legacy schema and lifecycle candidates T1 must reconcile | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | Absorption Candidate Ledger | Absorption Candidate Ledger | ASSF-T0.1 audit | EXISTS | ACCEPT |
| Generated aggregates require compact sources and generator discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated source layout discipline | generated source layout | generated aggregate standard | LITERAL_INVARIANT | ACCEPT |
| Dual consumer accounting requires internal and external CLI/MCP rows | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | INTERNAL_AGENT; EXTERNAL_AGENT_CLI_MCP | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |
| The current product skill concept is a form-based template surface, not a canonical agent package contract | `docs/concepts/skill-system.md` | What is a Skill | form-based template | current product skill concept | EXISTS | ACCEPT |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | ASSF-T1 - Canonical Package Contract And Storage Topology (contract-definition-only) |
| Closure status | CLOSED_PASS_BOUNDED |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Codex reviewer/closer |
| Reason for no worker commit | The package contract becomes the authority every later ASSF tranche depends on; the reviewer must validate reconciliation fidelity against the CVF Skill Spec and the T0.1 ledger before material closure |
| Next tranche blocked | ASSF-T2 generated index and resolver remain parked until ASSF-T1 closure |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T1 dispatch instruction | Required evidence | Disposition |
|---|---|---|---|
| Define the system `SKILL.md` profile | worker authors the SKILL.md section profile in the contract doc | SKILL.md profile section | READY |
| Define the compact machine source schema | worker enumerates the `skill.source.json` field schema in the contract doc | source schema section | READY |
| Define identity, authority, risk, and lifecycle fields | worker defines these field families reconciled with the CVF Skill Spec | field family definitions | READY |
| Define package layout and storage topology | worker describes the topology without creating it on disk | topology section, no directory created | READY |
| Reconcile existing CVF Skill Spec | worker maps each CVF Skill Spec required section to a contract field | reconciliation table | READY |
| Consume the T0.1 absorption ledger | worker maps T0.1 ledger candidates to contract fields or explicit deferral | ledger-consumption table | READY |
| Account for internal and external agents | worker includes the Dual Agent Surface Matrix | matrix with internal and external CLI/MCP rows | READY |
| Define provider adapter boundary | worker states the adapter/export boundary that never becomes canonical authority | adapter boundary section | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | the canonical package contract this tranche defines; proposed root `docs/reference/agent_system_skills/` | T1 defines the contract only; no loader, resolver, or package authority is implemented; loading must never widen authority | contract reconciliation tables and the T0.1 ledger | N/A with reason: no internal loader or resolver is implemented by T1 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP skill discovery or load adapter | T1 defines the external-agent disposition field in the contract; it does not implement, expose, or authorize any adapter | dual-agent standard and the contract's external-agent disposition field | Deferred adapter boundary; any CLI/MCP adapter requires separate GC-018 and source-verified work order | `DEFERRED_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
|---|---|
| Legacy scan classification | INHERITED_FROM_T0_1 |
| Scan root | `.private_reference/legacy/` (already enumerated and classified by ASSF-T0.1) |
| Inherited evidence | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` Absorption Candidate Ledger |
| Required worker action | consume the T0.1 ledger; do not re-run the full legacy scan; reconcile its `ABSORB_AS_*` candidates into contract fields or record explicit deferral |
| Forbidden shortcut | treating the CVF Skill Spec alone, chat memory, or provider memory as the sole contract input while ignoring the T0.1 ledger |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
|---|---|
| Competing definition | worker must reconcile, not replace, the existing CVF Skill Spec; a mapping table is required |
| Ledger ignored | worker must map each T0.1 `ABSORB_AS_*` ledger row to a contract field or an explicit deferral disposition |
| Premature root creation | worker must not create the package root, `SKILL.md`, `skill.source.json`, generated index, resolver, or any example package |
| Provider/legacy authority promotion | the contract must keep legacy and external content as candidate input until re-expressed in CVF-owned packages with review/UAT |
| External-adapter omission | the contract must define an external-agent CLI/MCP disposition field and account for it in the Dual Agent Surface Matrix |

## Corpus Completeness And Report Integrity

- Corpus task class: WORK_ORDER_DISPATCH.
- Corpus root: ASSF roadmap, this GC-018 baseline, the matching T1 work order, the CVF Skill Spec, and the ASSF-T0.1 audit ledger.
- Snapshot time: 2026-06-23.
- Enumeration command: dispatch source reads of the named authority files plus inheritance of the ASSF-T0.1 `rg --files --hidden --no-ignore .private_reference/legacy` evidence.
- Manifest artifact or inline manifest: this baseline and the matching T1 work order define the required output manifest; the legacy corpus manifest is inherited from the accepted ASSF-T0.1 audit.
- Manifest hash: N/A with reason: dispatch packet only; the legacy corpus snapshot was owned and accepted by ASSF-T0.1.
- Processing ledger artifact or inline ledger: ASSF-T1 worker return and
  completion review.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=dispatch_packet_only; legacy_ledger=inherited_from_accepted_T0_1; ledger_terminal=deferred_to_worker_return; exclusions=package root creation, SKILL.md, source schema files, generated index, resolver, example package, migration, runtime, provider/live, public-sync; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no canonical package root directory; no `SKILL.md`; no `skill.source.json`; no generated index; no resolver; no example package; no migration of existing CVF Web examples; no runtime/provider/live/public behavior; no CLI/MCP adapter implementation.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no generated aggregate created by dispatch.
- Drift check: N/A with reason: no generated aggregate created by dispatch.
- Output traceability: worker return must map every contract field to a CVF Skill Spec section, a T0.1 ledger row, a roadmap requirement, or an explicit new-field justification.
- Adversarial verification: worker must explicitly reject a contract that ignores the T0.1 ledger or replaces the CVF Skill Spec.
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Required route | consume the accepted ASSF-T0.1 absorption candidate ledger plus the existing CVF Skill Spec |
| Chain map route | legacy source family -> ASSF-T0.1 candidate ledger -> ASSF-T1 contract reconciliation -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T1 canonical package contract and future ASSF-T2/T4 work |
| Disposition | candidate intake only; no direct canonical authority or activation |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority, until re-expressed in reviewed CVF-owned packages |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`
- Delta ledger status: REQUIRED_BY_WORKER_RETURN
- Routing matrix status: REQUIRED_BY_WORKER_RETURN
- Semantic sampling status: REQUIRED_BY_WORKER_RETURN
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
|---|---|
| `UNCHANGED_FROM_INTAKE` | the T0.1 ledger and CVF Skill Spec remain the contract inputs |
| `CHANGED_DISPOSITION` | T1 changes the absorption candidates from classified-input status to reconciled contract fields or explicit deferrals |
| `NEW_FINDING` | any contract field not derivable from the CVF Skill Spec or the T0.1 ledger must be justified as a new field |
| `REMOVED_OR_REJECTED` | provider-local or unverifiable legacy claims are rejected from the contract |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
|---|---|
| `DO_NOW` | author the contract reference doc and worker-return packet |
| `SEPARATE_RUNTIME_TRANCHE` | generated index, resolver, and CLI/MCP adapter remain ASSF-T2/T5/T7 scope |
| `STRATEGIC_OPERATOR_DECISION` | package root creation and example package scaffolding deferred to a later operator-selected tranche |
| `OUT_OF_SCOPE` | migration of existing CVF Web examples, public-sync, runtime/provider/live |
| `RESOLVED_BY_DESIGN` | contract-definition-only scope prevents premature package-root authority |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T1-S1 | roadmap ASSF-T1 tranche | reconcile, do not replace, the CVF Skill Spec | reconciliation table required | could T1 author a fresh competing definition? | rejected |
| ASSF-T1-S2 | roadmap Next control action | T1 must consume the T0.1 ledger before schema | ledger-consumption table required | could T1 define schema from the Skill Spec alone? | rejected |
| ASSF-T1-S3 | dual-agent standard | external CLI/MCP disposition required | matrix and contract field required | could an internal-only contract pass? | rejected |

| Requirement | Dispatch control |
|---|---|
| Avoid repeated omission | the contract must map every CVF Skill Spec required section and every T0.1 `ABSORB_AS_*` row |
| Preserve useful legacy detail | the worker must carry forward reconciled legacy field candidates, not silently drop them |
| Convert review friction into learning | the worker must record a finding-to-governance disposition for any contract gap class |
| Keep machine-check candidate visible | the worker must state whether a future guard should verify contract/index consistency before ASSF-T2 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline consuming a private legacy
absorption ledger. Public-facing skill architecture, README, or CLI/MCP
documentation requires a later public-safe artifact and public-sync batch.

## Acceptance Criteria

- ASSF-T1 work order is source-verified against the roadmap, the CVF Skill
  Spec, the T0.1 ledger, and the dual-agent standard.
- Worker return is constrained to author exactly one canonical package
  contract reference document plus the worker-return packet; no commit, no
  package root, no `SKILL.md`, no `skill.source.json`, no generated index, no
  resolver, no example package, no migration.
- The contract reconciles every CVF Skill Spec required section and maps every
  T0.1 `ABSORB_AS_*` ledger row to a contract field or explicit deferral.
- Dual Agent Surface Matrix accounts for internal agents and external CLI/MCP
  agents.
- ASSF-T2 remains parked until ASSF-T1 closure.

## Fail Conditions

Fail dispatch or return if the packet authors a competing skill definition
instead of reconciling the CVF Skill Spec, ignores the T0.1 ledger, creates a
package root or any package/schema/index/resolver file, promotes legacy or
external content to canonical authority, omits external-agent disposition,
changes forbidden paths, or claims runtime/provider/live/public behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T1_CLOSED_PASS_BOUNDED_PENDING_T2_SELECTION` | PASS |
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_FOR_WORKER_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_WORKER_RETURN_2026-06-23.md` | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Contract reference doc | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_ASSF_T1_CANONICAL_PACKAGE_CONTRACT_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry or generated skill-index update authorized by T1 | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry Markdown or generated skill-index update authorized by T1 | BLOCKED with reason |
| External evidence digest | N/A with reason | no external artifact digest; evidence is local governed documentation | N/A with reason |
| System loop interlock | this file | no loop, queue, daemon, runtime, or automatic activation created | PASS |
| Session continuity | active session sync after material commit if next move changes | separate session-sync lane after material commit | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Closure status | `CLOSED_PASS_BOUNDED` | `CLOSED_PASS_BOUNDED` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Contract scope | contract-definition-only | contract-definition-only | PASS |
| T0.1 ledger consumption | required | required by work order | PASS |
| External CLI/MCP disposition | present | Dual Agent Surface Matrix row present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T1 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch-ready contract-definition-only worker-return lane only |
| receiptEvidence | N/A with reason: worker has not authored the contract yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded canonical package contract definition document |
| forbiddenExpansion | no package root, `SKILL.md`, `skill.source.json`, generated index, resolver, example package, migration, runtime/provider/live, public-sync, active skill, or CLI/MCP adapter implementation |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T1 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, file authoring, governance gates |
| Target paths | this baseline; matching T1 work order; ASSF roadmap context reads |
| Allowed scope source | operator instruction to change role and author the ASSF-T1 work order |
| Before status evidence | clean HEAD `ed7d0580` |
| After status evidence | ASSF-T1 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no contract authoring |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t1-canonical-package-contract-dispatch-2026-06-23` |
| Expected manifest | this baseline; matching T1 work order |
| Actual changed set | this baseline; matching T1 work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes ASSF-T1 worker-return execution only, and only as a
contract-definition-only tranche. It does not author the contract, close
ASSF-T1, create the canonical package root, create any `SKILL.md` or
`skill.source.json`, generate an index, implement a resolver, create an example
package, migrate any existing CVF Web example, run provider/live proof,
public-sync, or authorize ASSF-T2.
