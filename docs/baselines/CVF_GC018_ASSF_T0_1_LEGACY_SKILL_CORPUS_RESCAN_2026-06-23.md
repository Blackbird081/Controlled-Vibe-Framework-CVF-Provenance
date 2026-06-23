# CVF GC-018 ASSF-T0.1 Legacy Skill Corpus Rescan Baseline

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-23

docType: gc018_baseline

Batch ID: ASSF-T0.1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: ab7ca99b

executionBaseHead: PENDING_WORKER_START

closureBaseHead: PENDING_WORKER_RETURN

## Purpose

Authorize a bounded ASSF-T0.1 worker-return lane that scans the legacy tree for
skill-related knowledge, classifies absorption candidates, and returns an audit
packet for Codex review before ASSF-T1 freezes the canonical skill package
contract or storage topology.

This baseline exists because ASSF-T0 closed with only a bounded owner/surface
audit. The operator identified the currently opened legacy folders as seeds,
not complete skill-corpus coverage. T0.1 must therefore produce filesystem
evidence before any schema, package root, generated index, resolver, migration,
runtime adapter, public-sync, or activation work proceeds.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | Requires ASSF-T0.1 or another fresh authorized lane before ASSF-T1 |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current mode parks ASSF-T1 behind T0.1 |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | Active handoff for this governed dispatch |
| Roadmap | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | ASSF-T0.1 mandatory precondition |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source Verification and dispatch packet shape |
| GC-018 template | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | Legacy scan, blind-spot, and corpus completeness controls |
| Dual-agent standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Internal and external CLI/MCP surface accounting |
| External intake chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Legacy source family routes to absorption control |

## Source / Predecessor Evidence

The predecessor evidence is ASSF-T0 closure plus the roadmap's mandatory T0.1
precondition. Seed legacy folders are verified inputs, not sufficient corpus
coverage. This baseline dispatches a worker-return rescan instead of closing
the legacy corpus claim.

## Decision / Baseline / Proposed Tranche

Decision: dispatch ASSF-T0.1 as a no-commit worker-return tranche. Baseline:
T0.1 may scan and classify legacy skill-relevant knowledge only. Proposed
tranche output: audit ledger plus worker-return packet for reviewer closure.

## Evidence / Verification

Verification for dispatch uses the Source Verification Block, dispatch-quality
gate, roadmap closure freshness gate, autorun pre-dispatch gate, and commit
steward preflight. Worker execution evidence belongs in the worker-return
artifacts.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-T0.1 is mandatory before ASSF-T1 | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Mandatory Legacy Skill Rescan Gate; ASSF-T0.1 tranche | `ASSF-T0.1` | ASSF roadmap | VALUE_SET | ACCEPT |
| T0.1 may scan and classify but must not migrate, package, index, activate, public-sync, or implement runtime adapters | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | Required T0.1 output; ASSF-T0.1 tranche | no migration/package/index/runtime/public/adapter | ASSF roadmap | LITERAL_INVARIANT | ACCEPT |
| Work orders require Source Verification before implementation | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Mandatory Work Order Source Verification | `Source Verification Block` | work-order template | LITERAL_INVARIANT | ACCEPT |
| GC-018 legacy-adjacent work requires a Legacy Spec Scan Block | `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` | Legacy Spec Scan Block | `Legacy Spec Scan Block` | GC-018 template | LITERAL_INVARIANT | ACCEPT |
| Dual consumer accounting requires internal and external CLI/MCP rows | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent surface standard | LITERAL_INVARIANT | ACCEPT |
| Legacy ADK SkillToolset notes contain progressive disclosure and three-layer skill normalization concepts | `.private_reference/legacy/CVF_Important/ADK SkillToolset/Thong_tin.md` | ADK SkillToolset and Progressive Disclosure notes | L1 metadata; L2 instructions; L3 resources | legacy source family | EXISTS | ACCEPT |
| Legacy ADK assimilation log records Progressive Disclosure Policy, Skill Normalization Schema, trigger patterns, and governance signals | `.private_reference/legacy/CVF_Important/ADK SkillToolset/CVF_KNOWLEDGE_ASSIMILATION_LOG.md` | Absorbed Knowledge Modules | Progressive Disclosure Policy; Skill Normalization Schema | legacy source family | EXISTS | ACCEPT |
| Legacy Windows normalization notes record PowerShell/Windows compatibility risks for skills | `.private_reference/legacy/CVF_Important/Windows_Skill_Normalization/Thong_tin.md` | Windows skill normalization notes | PowerShell compatibility; shell metadata | legacy source family | EXISTS | ACCEPT |
| Legacy skill formation notes record learn, extract, structure, save, reuse and SKILL.md package pattern | `.private_reference/legacy/CVF_Important/ADDING_CVF_Skill Formation Layer/Thong_tin.md` | Skill Formation Layer notes | Learn -> Compile -> Store; SKILL.md | legacy source family | EXISTS | ACCEPT |
| Legacy Memento notes record that skill evolution must be proposal, verification, approval, and reinjection, not direct production mutation | `.private_reference/legacy/CVF 16.5/Memento-Skills/GOVERNED_SKILL_EVOLUTION_SPEC.md` | Hard Rules; Security Position | No self-write into production; governed reinjection | legacy source family | LITERAL_INVARIANT | ACCEPT |

## Continuation Decision

| Field | Disposition |
|---|---|
| Selected tranche | ASSF-T0.1 - Legacy Skill Corpus Rescan And Absorption Candidate Ledger |
| Dispatch status | DISPATCH_READY |
| Worker commit authority | WORKER_MUST_NOT_COMMIT |
| Reviewer closer | Codex reviewer/closer |
| Reason for no worker commit | Legacy absorption affects future canonical package architecture; reviewer must validate corpus coverage and source-fidelity before material closure |
| Next tranche blocked | ASSF-T1 remains parked until T0.1 closure |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T0.1 dispatch instruction | Required evidence | Disposition |
|---|---|---|---|
| Scan the broader legacy tree rather than open tabs only | Worker must enumerate `.private_reference/legacy/` with filesystem commands and keyword search | manifest command, manifest path, and candidate ledger | READY |
| Include seed folders but treat them as incomplete | Seed folders are required inputs, not the corpus boundary | seed coverage rows plus broader scan results | READY |
| Produce absorption candidate ledger | Worker must classify candidate files/folders using the roadmap dispositions | audit ledger with terminal status per candidate | READY |
| Preserve legacy as non-canonical input | Worker must state that legacy becomes authority only after CVF-owned forward artifact review | claim boundary and disposition notes | READY |
| Do not migrate or implement packages/adapters | Forbidden scope blocks package root, index, resolver, runtime, public-sync, and CLI/MCP implementation | git status, changed-set manifest, and claim boundary | READY |
| Account for internal and external agents | Worker return must include Dual Agent Surface Matrix | matrix with internal and external CLI/MCP rows | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF roadmap, this GC-018 baseline, and T0.1 work order | May read and classify legacy sources only; may not create active package authority, generated index, resolver, or runtime behavior | Source Verification rows and future worker-return corpus ledger | N/A with reason: no internal package loader or resolver is implemented by T0.1 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | Future CLI/MCP skill discovery or load adapter | External agents must receive normalized CVF package contracts only after later adapter tranche; no legacy source is exposed as adapter-ready authority | Dual-agent standard and external intake chain map | Deferred adapter boundary; any CLI/MCP adapter requires separate GC-018 and source-verified work order | `DEFERRED_WITH_REASON` |

## Legacy Spec Scan Block

| Field | Disposition |
|---|---|
| Legacy scan classification | REQUIRED |
| Scan root | `.private_reference/legacy/` |
| Required seed paths | `.private_reference/legacy/CVF_Important/ADK SkillToolset/`; `.private_reference/legacy/CVF_Important/Windows_Skill_Normalization/`; `.private_reference/legacy/CVF_Important/ADDING_CVF_Skill Formation Layer/`; `.private_reference/legacy/CVF 16.5/Memento-Skills/` |
| Required query families | skill, skills, package, toolset, formation, lifecycle, normalization, memento, adapter, MCP, CLI, ADK, governed evolution |
| Required output | filesystem-backed manifest and absorption candidate ledger |
| Required terminal dispositions | `ABSORB_AS_CONTRACT_INPUT`; `ABSORB_AS_LIFECYCLE_INPUT`; `ABSORB_AS_PACKAGE_PATTERN`; `ABSORB_AS_TOOL_ADAPTER_INPUT`; `REFERENCE_ONLY`; `DUPLICATE`; `REJECT_DIRECT`; `BLOCKED_UNVERIFIED_SOURCE` |
| Forbidden shortcut | treating currently opened folders, T0 bounded owner counts, chat memory, or provider memory as corpus coverage |

## Knowledge Absorption Blind-Spot Control Block

| Blind spot | Control |
|---|---|
| Seed-only legacy scan | Worker must scan the full legacy root and record exact enumeration command |
| Name-only classification | Worker must inspect enough content to justify disposition and record source-fidelity notes for well-formed CVF legacy packets |
| Legacy authority promotion | Worker must keep legacy as candidate input until re-expressed in CVF-owned forward artifacts |
| External-adapter omission | Worker return must classify whether each relevant candidate affects internal package design, external CLI/MCP adapter design, or both |
| Hidden duplicate/collision | Worker must run negative-search/collision queries and record duplicates instead of silently dropping them |

## Corpus Completeness And Report Integrity

- Corpus task class: WORK_ORDER_DISPATCH.
- Corpus root: ASSF roadmap, this GC-018 baseline, and required future worker scan root `.private_reference/legacy/`.
- Snapshot time: 2026-06-23.
- Enumeration command: dispatch source reads plus future worker command `rg --files --hidden --no-ignore .private_reference/legacy`.
- Manifest artifact or inline manifest: this baseline and the matching T0.1 work order define the required manifest; future worker must create the actual scan manifest or inline manifest in the worker-return audit.
- Manifest hash: N/A with reason: dispatch packet only; worker owns corpus snapshot evidence.
- Processing ledger artifact or inline ledger: PENDING_WORKER_RETURN.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=dispatch_packet_only; ledger_terminal=deferred_to_worker_return; exclusions=package creation, migration, runtime, provider/live, public-sync, generated index, resolver, and adapter implementation; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no edits under `.private_reference/legacy/`; no canonical package root; no generated index; no resolver; no runtime/provider/live/public behavior; no CLI/MCP adapter implementation.
- Unreadable or unsupported files: PENDING_WORKER_RETURN.
- Aggregation check: N/A with reason: no generated aggregate created by dispatch.
- Drift check: N/A with reason: no generated aggregate created by dispatch.
- Output traceability: worker return must map every terminal conclusion to a manifest row, source path, command evidence, and allowed disposition.
- Adversarial verification: worker must explicitly reject open-tab-only and memory-only corpus claims.
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Legacy source family |
| Required route | Knowledge Absorption Blind-Spot Control Block plus legacy coverage lookup |
| Chain map route | legacy source family -> absorption blind-spot control -> ASSF candidate ledger -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T0.1 audit and future ASSF-T1/T4 normalization decisions |
| Disposition | candidate intake only; no direct canonical authority or activation |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- Delta ledger status: REQUIRED_BY_WORKER_RETURN
- Routing matrix status: REQUIRED_BY_WORKER_RETURN
- Semantic sampling status: REQUIRED_BY_WORKER_RETURN
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Dispatch treatment |
|---|---|
| `UNCHANGED_FROM_INTAKE` | T0 remains closed bounded as owner/surface audit |
| `CHANGED_DISPOSITION` | T0.1 changes legacy corpus status from precondition to dispatch-ready no-commit rescan |
| `NEW_FINDING` | seed folders are not full corpus coverage |
| `REMOVED_OR_REJECTED` | open-tab-only and memory-only corpus claims are rejected |

### Follow-Up Routing Matrix

| Routing lane | Dispatch treatment |
|---|---|
| `DO_NOW` | execute T0.1 scan and ledger |
| `SEPARATE_RUNTIME_TRANCHE` | runtime/provider/adapter implementation remains forbidden |
| `STRATEGIC_OPERATOR_DECISION` | ASSF-T1 resumes only after T0.1 closure and operator selection if needed |
| `OUT_OF_SCOPE` | migration, package creation, generated index, resolver, public-sync |
| `RESOLVED_BY_DESIGN` | no-commit worker-return lane prevents premature legacy authority promotion |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T0.1-S1 | roadmap Mandatory Legacy Skill Rescan Gate | seed paths are not full corpus | T0.1 dispatch required | Could T1 proceed from T0 only? | rejected |
| ASSF-T0.1-S2 | Memento hard rules | no direct production mutation | no package activation | Could legacy skill evolution self-write? | rejected |
| ASSF-T0.1-S3 | dual-agent standard | external CLI/MCP row required | matrix required | Could internal-only skill design pass? | rejected |

| Requirement | Dispatch control |
|---|---|
| Avoid repeated omission | Full legacy-root enumeration is mandatory |
| Preserve useful legacy detail | Worker must identify well-formed CVF packets and reusable format/content candidates |
| Convert review friction into learning | Worker must include finding-to-governance learning disposition for any repeated omission class |
| Keep machine-check candidate visible | Worker must state whether a future guard should require legacy scan evidence before ASSF schema dispatch |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline. Public-facing skill architecture,
README, package catalogs, or CLI/MCP documentation require a later public-safe
artifact and public-sync batch.

## Acceptance Criteria

- ASSF-T0.1 work order is source-verified against roadmap, standards, and seed
  legacy files.
- Worker return is constrained to scan, classify, and report; no commit,
  migration, package root, generated index, resolver, runtime adapter,
  public-sync, or activation.
- Dual Agent Surface Matrix accounts for internal agents and external CLI/MCP
  agents.
- ASSF-T1 remains parked until T0.1 closure.

## Fail Conditions

Fail dispatch or return if the packet treats seed folders as complete corpus
coverage, promotes legacy files to canonical authority, omits external-agent
disposition, changes forbidden paths, creates package/index/runtime surfaces,
or claims closure without filesystem-backed manifest and ledger evidence.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | `Status: ASSF_T0_1_DISPATCH_READY` | PASS |
| GC-018 status | this file | `Status: DISPATCH_READY` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md` | `Status: DISPATCH_READY` | PASS |
| Worker return | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` | PENDING_WORKER_RETURN | PENDING |
| Audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | PENDING_WORKER_RETURN | PENDING |
| Registry JSON | N/A with reason | no GC-051 registry update authorized by dispatch | N/A with reason |
| Registry Markdown | N/A with reason | no GC-051 registry update authorized by dispatch | N/A with reason |
| Session continuity | active session sync after material commit if next move changes | separate session-sync lane | PENDING |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Dispatch status | `DISPATCH_READY` | `DISPATCH_READY` | PASS |
| Worker commit authority | `WORKER_MUST_NOT_COMMIT` | `WORKER_MUST_NOT_COMMIT` | PASS |
| Legacy scan root | `.private_reference/legacy/` | `.private_reference/legacy/` | PASS |
| External CLI/MCP disposition | present | Dual Agent Surface Matrix row present | PASS |
| Runtime/provider/live claim | none | none | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-T0.1 dispatch baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - dispatch-ready worker-return lane only |
| receiptEvidence | N/A with reason: worker has not run scan yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT - Source Verification rows and governed dispatch artifact |
| invocationBoundary | roadmap-derived work-order authoring |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | authorizes a bounded legacy scan and absorption candidate ledger |
| forbiddenExpansion | no migration, package root, generated index, resolver, runtime/provider/live, public-sync, active skill, or CLI/MCP adapter implementation |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0.1 work-order dispatch, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governance gates, git commit |
| Target paths | this baseline; matching T0.1 work order; ASSF roadmap |
| Allowed scope source | operator instruction to create work order after T0.1 requirement |
| Before status evidence | clean HEAD `ab7ca99b` |
| After status evidence | ASSF-T0.1 dispatch ready; worker-return lane required |
| Diff evidence | real-range name-status and gate output before commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution and no legacy migration |
| Agent type | dispatcher |
| Invocation ID | `cvf-assf-t0-1-legacy-skill-corpus-rescan-dispatch-2026-06-23` |
| Expected manifest | this baseline; matching T0.1 work order; ASSF roadmap |
| Actual changed set | this baseline; matching T0.1 work order; ASSF roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This baseline authorizes ASSF-T0.1 worker-return execution only. It does not
perform the legacy scan, close T0.1, create the canonical skill package root,
generate an index, implement a resolver, migrate legacy files, activate any
skill, implement CLI/MCP adapters, run provider/live proof, public-sync, or
authorize ASSF-T1.
