# CVF GC-018 - RSPB-AI-T13 ASSF Package Metadata To Capability Preflight Candidate Binding Kernel

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_IMPLEMENTATION

Batch ID: RSPB-AI-T13

Dispatch base head: `f25420cf2d852a653206bb901b06f10267eb13ae`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: current orchestrator/reviewer

Worker target: external implementation worker

rawMemoryReleased=false

## Purpose

Authorize one pure Guard Contract seam that validates caller-supplied ASSF
package metadata and projects a bounded capability-preflight candidate without
loading, activating, resolving, executing, or mutating any package or registry.

## Value / Cost Decision

The 205-file ledger is reused. Integrity, secret-safety, promotion, route,
snapshot, policy, receipt, and closure candidates were rejected as duplicate
or already absorbed through T4-T12. The one-file ASSF binding draft retains a
non-duplicate owner-composition gap and is small enough for a P2 bounded pass.

## Decision / Baseline

Implement a CVF-native pure evaluator in Guard Contract. The evaluator may
project candidate evidence only. Every result must deny activation, loading,
execution, mutation, acquisition, provider/live, and external-adapter authority.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RSPB-AI-T13 --title "ASSF Package Metadata To Capability Preflight Candidate Binding Kernel" --date 2026-08-17 --base c5ad52456eda067d7616dff657753ca4388639bf --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit and package-skill trigger stubs |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | selected cluster, source decisions, pure contract, exact worker scope, proportional proof |
| checkerReadAheadConfirmation | dispatch-quality, TPGR, packet authority/encoding, operation trace, worker-return fast gate |
| docOnlyNewFields | candidate binding result vocabulary only |
| claimBoundary | dispatch baseline only; no package lifecycle or runtime state changes |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption-implementation --role dispatcher --lifecycle-phase pre-dispatch --surface-selector EXTENSIONS/CVF_GUARD_CONTRACT --risk-ceiling MEDIUM --json`

Returned defects: NONE_RETURNED

## Evidence / Verification

The accepted T0 manifest has 205 rows. This tranche selects one fully read row
and preserves 204 prior dispositions. Its SHA-256 was recomputed at dispatch.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Source Verification Block; Work-Order Fulfillment Manifest; Task Governance Routing Manifest; Agent Operation Trace Block; worker-return profile |
| gateRunPurpose | confirmation after source inspection |
| claimBoundary | checker compliance does not prove semantic acceptance or runtime behavior |

## Authorization / Source

Operator authorized the orchestrator to select the next high-value local
cluster and create a no-commit work order for manual transfer to another agent.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| mixed-origin binding proposal | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/agent_system_skills/CVF_ASSF_PREFLIGHT_BINDING_CONTRACT.md` | complete file | `authorityStatus` | proposal draft | REJECT |
| ASSF package field families | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `skillId`; `status`; `riskCeiling`; `authorityCeiling`; `dependencies`; `conflicts`; `platformCompatibility` | ASSF package contract | ACCEPT |
| package lifecycle cannot self-advance | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Self-Activation Invariant | `status` | ASSF composition contract | ACCEPT |
| current metadata entry shape | `docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json` | complete object | `skillId`; `candidateState`; `externalCliMcpDisposition` | ASSF registry entry schema | ACCEPT |
| current closure evidence owner | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-bootstrap-closure-evidence-bundle.contract.ts` | exported result | `authorityStatus`; `taskAuthorityGranted` | Guard Contract T12 | ACCEPT |

## Selected Cluster Evidence

| Selected ledger path | SHA-256 | Bytes | Disposition |
| --- | --- | ---: | --- |
| `docs/reference/agent_system_skills/CVF_ASSF_PREFLIGHT_BINDING_CONTRACT.md` | `984ec80802dbcfa304eaecc254963e976dceee9530982294c4fabfabaf1929d9` | 1797 | ADAPT bounded mapping idea; reject draft as authority |

## Mixed-Origin Derived Synthesis Provenance

The selected file is `MIXED_ORIGIN` and non-authoritative. Only independently
reviewed CVF-native output may become accepted repository evidence.

## Absorption Efficiency And Provenance Reuse

Reuse T0 inventory and ledger. Recompute the selected hash and read that file
fully. Do not rescan the other 204 rows or reproduce unrelated live/public proof.

## Absorption Decision Vector

ADAPT the candidate-only mapping seam; preserve canonical ASSF field owners;
REJECT registry loading, lifecycle mutation, resolver/loader behavior, raw
secret transfer, and direct proposal import.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| ASSF binding draft | candidate-only normalization | PACKAGE_CANDIDATE | Guard Contract | rewrite as pure evaluator | no loader or activation |
| lifecycle rule | ineligible state cannot become runnable | DOCTRINE_ADAPTED | result invariants/tests | fail closed | no state change |
| composition fields | dependency/conflict evidence | PACKAGE_CANDIDATE | bounded projection | validate only | no graph resolution |
| runtime interpretations | resolver/loader opportunity | RUNTIME_CANDIDATE | separate future owner | defer unless operator opens runtime tranche | no runtime in T13 |
| checker interpretations | metadata conformance opportunity | CHECKER_CANDIDATE | existing ASSF checker family | reject duplicate checker tranche | no checker edit |
| direct proposal source | unreviewed draft implementation authority | REJECT_DIRECT_IMPORT | none | rewrite CVF-native | no import |
| adapter text | external disposition boundary | NO_PACKAGE_OR_RUNTIME_VALUE | false authority outputs | preserve denial | no CLI/MCP |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | retained local Capability Preflight Bootstrap folder |
| Enumeration command | predecessor `rg --files --hidden --no-ignore`; one named selection |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | ASSF package/composition contracts and Guard Contract |
| Unresolved items | 0 selected rows; implementation pending |
| Completion claim boundary | selected one-file cluster only |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| artifact integrity | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-acquisition-receipt-verification.contract.ts` | NO_NEW_VALUE | already checks plan/artifact digest | reject duplicate tranche |
| secret safety | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts`; T9/T12 adjacent contracts | NO_NEW_VALUE | already fail-closed | reject duplicate tranche |
| learning promotion | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/capability-learning-candidate-projection.ts` | NO_NEW_VALUE | pending/null/false already enforced | reject duplicate tranche |
| ASSF to preflight binding | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; Guard Contract barrels | ENRICH_EXISTING | pure candidate-binding evaluator is the retained delta | implement T13 |

## Mandatory Blind-Spot Control Block

Only the named ASSF binding draft is claimed fully processed here. The other
204 ledger rows retain their accepted T0 dispositions.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | selected mixed-origin copied-folder file |
| Upstream or source-mirror disposition | accepted predecessor evidence reused; no fetch |
| Enumeration or manifest plan | accepted 205-file manifest plus one selected row |
| Per-file terminal-ledger plan | selected exact hash in this baseline |
| Owner or overlap route | canonical ASSF contracts -> Guard Contract seam |
| Value-disposition route | pure mapping now; runtime/activation rejected |
| Claim boundary | no rescan, direct import, registry edit, loader, or execution |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | ledger -> one file -> canonical-owner comparison -> pure kernel |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | ASSF references and Guard Contract |
| Disposition | ADAPT one missing seam; reject duplicates and effects |
| Claim boundary | registry/runtime dependency and authority transfer are forbidden |

## Corpus Completeness And Report Integrity

- Corpus task class: selected capability-cluster absorption.
- Corpus root: one selected local file.
- Snapshot time: 2026-08-17 dispatch.
- Enumeration command: predecessor `rg --files --hidden --no-ignore` plus named selection.
- Manifest artifact or inline manifest: accepted T0 manifest and selected row above.
- Manifest hash: selected SHA-256 above.
- Processing ledger artifact or inline ledger: accepted T0 205-row ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=1; ledger_terminal=1; exclusions=204; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: 204 files outside this cluster.
- Unreadable or unsupported files: none selected.
- Aggregation check: 1 + 204 = 205.
- Drift check: worker recomputes one hash.
- Output traceability: selected source to exact five worker paths.
- Adversarial verification: lifecycle, authority, hostile-shape, bounds, and mutation-isolation tests.
- Corpus verdict: PARTIAL

## Rescan Intelligence Hardening

- Original source artifact: accepted T0 205-file ledger.
- Predecessor intake artifact: RSPB-AI-T0 dual-corpus intake audit.
- Delta ledger status: reused with one fresh hash.
- Routing matrix status: one-file ASSF binding cluster selected.
- Semantic sampling status: selected file fully read.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Evidence |
| --- | --- |
| UNCHANGED_FROM_INTAKE | 204 rows retain prior dispositions |
| CHANGED_DISPOSITION | one ASSF binding draft selected for bounded adaptation |
| NEW_FINDING | pure candidate-binding evaluator absent |
| REMOVED_OR_REJECTED | duplicate integrity, secret, promotion and runtime interpretations |

### Follow-Up Routing Matrix

| Route | Disposition |
| --- | --- |
| DO_NOW | exact-five pure T13 kernel |
| SEPARATE_RUNTIME_TRANCHE | registry resolver/loader or package activation |
| STRATEGIC_OPERATOR_DECISION | any lifecycle mutation or external adapter |
| OUT_OF_SCOPE | provider/live, public, deploy, production |
| RESOLVED_BY_DESIGN | caller-supplied metadata and literal false grants |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| RSPB-T13-S1 | complete binding draft | normalize ASSF metadata | ADAPT | draft could invent authority | CANDIDATE_ONLY_REQUIRED |
| RSPB-T13-S2 | lifecycle rule | ineligible package stays ineligible | ADAPT | readiness could override lifecycle | FAIL_CLOSED_REQUIRED |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: no ASSF package lifecycle surface changes.

Target lifecycle state: N/A with reason: output remains `CANDIDATE_ONLY`.

Prior phase evidence: canonical ASSF package and composition contracts.

Next forbidden skip: package creation, promotion, activation, loading, or use
proof requires a separate governed tranche.

Runtime/provider proof: N/A with reason: no runtime/provider action authorized.

Claim boundary: metadata-binding design only, not skill productionization.

## Epistemic Process Block

### Expected Result / Prediction

A pure candidate projection can preserve useful ASSF metadata while opening no
package lifecycle, registry, resolver, loader, or execution authority.

### Evidence Comparison

Canonical ASSF owners already define metadata and lifecycle controls. Guard
Contract lacks only the bounded translation seam proposed by the selected row.

### Contradiction Or Gap Disposition

The proposal's broad consumer language is narrowed to caller-supplied evidence
and literal false grants. Runtime interpretations are rejected.

### Claim Update

T13 may implement one pure candidate-binding evaluator, subject to independent
review. No runtime integration claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | RSPB-AI-T13 baseline authoring, 2026-08-17 |
| Working directory | repository root at `f25420cf2` |
| Command or tool surface | ledger parsing, full selected-file read, overlap search, Git |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator request to create next no-commit worker order |
| Before status evidence | clean worktree at dispatch base |
| After status evidence | dispatch artifacts pending reviewer-owned commit |
| Diff evidence | `git diff --name-status`; `git diff --check` |
| Approval boundary | dispatch authoring only |
| Claim boundary | pure candidate-binding design only |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `rspb-ai-t13-dispatch-2026-08-17` |
| Expected manifest | this baseline; paired work order; continuity surfaces authorized by current handoff |
| Actual changed set | reviewer verifies before dispatch commit |
| Manifest delta | reviewer verifies before dispatch commit |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | pure caller-supplied ASSF metadata to candidate evidence projection |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no package use or execution receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no action is authorized |
| invocationBoundary | explicit pure function call only |
| interceptionBoundary | registry, filesystem, resolver, loader, provider, and tool interception are forbidden |
| claimLanguage | candidate evidence projection only |
| forbiddenExpansion | activation, loading, mutation, execution, CLI/MCP, provider/live, public, deploy, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This baseline authorizes only the exact-five no-commit implementation packet.
It does not authorize ASSF registry/index edits, package lifecycle changes,
resolver/loader invocation, instruction-body reads, runtime, provider/live,
public sync, deployment, or production use.
